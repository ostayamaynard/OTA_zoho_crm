
import re
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from reportlab.lib import colors

def parse_markdown_to_pdf(input_file, output_file):
    doc = SimpleDocTemplate(output_file, pagesize=letter,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)
    
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    
    # Custom styles
    title_style = styles["Heading1"]
    title_style.alignment = TA_LEFT
    
    h2_style = styles["Heading2"]
    h2_style.spaceBefore = 12
    h2_style.spaceAfter = 6
    h2_style.textColor = colors.HexColor("#204a87")

    h3_style = styles["Heading3"]
    h3_style.spaceBefore = 10
    h3_style.spaceAfter = 4
    
    body_style = styles["BodyText"]
    body_style.spaceAfter = 6
    
    bullet_style = ParagraphStyle('Bullet', parent=styles['BodyText'], bulletIndent=10, leftIndent=20, spaceAfter=2)
    nested_bullet_style = ParagraphStyle('NestedBullet', parent=styles['BodyText'], bulletIndent=30, leftIndent=40, spaceAfter=2)

    story = []
    
    with open(input_file, 'r') as f:
        lines = f.readlines()
        
    list_buffer = []
    in_list = False
    
    def flush_list():
        nonlocal list_buffer, in_list
        if list_buffer:
            # Simple approach: add all as individual list items
            # ReportLab's ListFlowable is great but can be complex with mixed nesting.
            # We'll just append them as Paragraphs with bullet points for simplicity and reliability
            for item_text, level in list_buffer:
                style = nested_bullet_style if level > 0 else bullet_style
                # ReportLab supports basic XML tags like <b>, <i>
                # Markdown bold **text** -> <b>text</b>
                formatted_text = format_inline_markdown(item_text)
                story.append(Paragraph(f"• {formatted_text}", style))
            list_buffer = []
            in_list = False
            story.append(Spacer(1, 6))

    def format_inline_markdown(text):
        # Bold: **text** -> <b>text</b>
        text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
        # Italic: *text* -> <i>text</i> (careful with bullet points)
        # Code: `text` -> <font face="Courier">text</font>
        text = re.sub(r'`(.*?)`', r'<font face="Courier">\1</font>', text)
        return text

    for line in lines:
        line = line.strip()
        
        if not line:
            flush_list()
            continue
            
        # Horizontal Rule
        if line.startswith('---'):
            flush_list()
            story.append(Spacer(1, 12))
            # Add a line drawing if we wanted, but spacer is fine for now
            continue
            
        # Headers
        if line.startswith('# '):
            flush_list()
            story.append(Paragraph(format_inline_markdown(line[2:]), title_style))
            story.append(Spacer(1, 12))
        elif line.startswith('## '):
            flush_list()
            story.append(Paragraph(format_inline_markdown(line[3:]), h2_style))
        elif line.startswith('### '):
            flush_list()
            story.append(Paragraph(format_inline_markdown(line[4:]), h3_style))
            
        # List Items
        elif line.startswith('* ') or line.startswith('- '):
            # Level 0 list
            list_buffer.append((line[2:], 0))
            in_list = True
        elif line.startswith('    * ') or line.startswith('    - '):
            # Level 1 list (nested)
            list_buffer.append((line[6:], 1))
            in_list = True
            
        # Body Text
        else:
            flush_list()
            # Handle bold lines that aren't headers (e.g., "**The Change:** ...")
            formatted_text = format_inline_markdown(line)
            story.append(Paragraph(formatted_text, body_style))

    flush_list()
    
    doc.build(story)
    print(f"PDF generated: {output_file}")

if __name__ == "__main__":
    input_md = 'docs/dev-impact-analysis-transcript.md'
    output_pdf = 'docs/dev-impact-analysis-transcript.pdf'
    try:
        parse_markdown_to_pdf(input_md, output_pdf)
    except Exception as e:
        print(f"Failed to generate PDF: {e}")




