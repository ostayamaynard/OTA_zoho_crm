#!/usr/bin/env python3
"""
Mermaid Diagram Syntax Auditor

Validates all .mmd files in the repository against Mermaid syntax rules.
Reference: https://mermaid.js.org/intro/
"""

import os
import re
import json
from pathlib import Path

# Base directory
BASE_DIR = Path('/home/user/zoho_crm')

def find_all_mermaid_files():
    """Find all .mmd files in the repository."""
    return list(BASE_DIR.rglob('*.mmd'))

def validate_mermaid_syntax(file_path):
    """Validate Mermaid diagram syntax."""
    issues = []
    warnings = []

    with open(file_path, 'r') as f:
        content = f.read()

    lines = content.split('\n')

    # Check for markdown code fence wrapping (should NOT be in .mmd files)
    if content.strip().startswith('```'):
        issues.append("File contains markdown code fences (```mermaid). Remove them for .mmd files.")
        # Strip fences for further analysis
        content = re.sub(r'^```mermaid\s*', '', content.strip())
        content = re.sub(r'\s*```\s*$', '', content)
        lines = content.split('\n')

    # Track state
    in_subgraph = 0
    found_diagram_type = False
    diagram_type = None
    line_count = len(lines)

    # Valid diagram types
    valid_types = [
        'flowchart', 'graph', 'sequenceDiagram', 'classDiagram',
        'stateDiagram', 'stateDiagram-v2', 'erDiagram', 'journey',
        'gantt', 'pie', 'quadrantChart', 'requirementDiagram',
        'gitGraph', 'mindmap', 'timeline', 'zenuml', 'sankey-beta',
        'xychart-beta', 'block-beta'
    ]

    # Valid directions for flowchart/graph
    valid_directions = ['TB', 'TD', 'BT', 'RL', 'LR']

    # Check for YAML frontmatter (valid since Mermaid v9.2.0)
    in_frontmatter = False
    has_frontmatter = False

    for i, line in enumerate(lines, 1):
        stripped = line.strip()

        # Skip empty lines and comments
        if not stripped or stripped.startswith('%%'):
            continue

        # Handle YAML frontmatter
        if stripped == '---':
            if not has_frontmatter:
                in_frontmatter = True
                has_frontmatter = True
                continue
            elif in_frontmatter:
                in_frontmatter = False
                continue

        if in_frontmatter:
            continue  # Skip frontmatter content

        # Check for diagram type declaration
        if not found_diagram_type:
            # Check for init directive first
            if stripped.startswith('%%{init:'):
                continue

            # Look for diagram type
            for dtype in valid_types:
                if stripped.startswith(dtype):
                    found_diagram_type = True
                    diagram_type = dtype

                    # Check direction for flowchart/graph
                    if dtype in ['flowchart', 'graph']:
                        parts = stripped.split()
                        if len(parts) >= 2:
                            direction = parts[1]
                            if direction not in valid_directions:
                                issues.append(f"Line {i}: Invalid direction '{direction}'. Use: {', '.join(valid_directions)}")
                    break

            if not found_diagram_type and not stripped.startswith('%%'):
                # First non-comment, non-init line should be diagram type
                issues.append(f"Line {i}: Expected diagram type declaration. Found: '{stripped[:50]}...'")
                found_diagram_type = True  # Stop checking
            continue

        # Flowchart/Graph specific validation
        if diagram_type in ['flowchart', 'graph']:
            # Check subgraph syntax
            if stripped.startswith('subgraph'):
                in_subgraph += 1
                # Check for subgraph name
                match = re.match(r'subgraph\s+(\w+)(?:\[.*\])?', stripped)
                if not match and stripped != 'subgraph':
                    # Check for quoted names
                    if not re.match(r'subgraph\s+["\'].*["\']', stripped):
                        if '[' not in stripped:
                            warnings.append(f"Line {i}: Subgraph should have an ID: 'subgraph id[\"Label\"]'")

            elif stripped == 'end':
                if in_subgraph > 0:
                    in_subgraph -= 1
                else:
                    issues.append(f"Line {i}: Unexpected 'end' - no matching subgraph")

            # Check node definitions
            elif '-->' in stripped or '---' in stripped or '-.->':
                # Edge definition - check for common issues

                # Check for spaces in node IDs without quotes
                node_pattern = r'([A-Za-z_][A-Za-z0-9_]*)'

                # Check arrow syntax
                if '-- >' in stripped:
                    issues.append(f"Line {i}: Invalid arrow syntax '-- >'. Use '-->' without space")
                if '- ->' in stripped:
                    issues.append(f"Line {i}: Invalid arrow syntax '- ->'. Use '-->' or '-.->")

                # Check for unbalanced brackets in labels
                if '[' in stripped:
                    open_count = stripped.count('[')
                    close_count = stripped.count(']')
                    if open_count != close_count:
                        issues.append(f"Line {i}: Unbalanced brackets [ ] in node label")

                if '(' in stripped:
                    # Exclude classDef patterns
                    if 'classDef' not in stripped:
                        open_count = stripped.count('(')
                        close_count = stripped.count(')')
                        if open_count != close_count:
                            issues.append(f"Line {i}: Unbalanced parentheses ( ) in node")

                if '{' in stripped:
                    if 'init' not in stripped:
                        open_count = stripped.count('{')
                        close_count = stripped.count('}')
                        if open_count != close_count:
                            issues.append(f"Line {i}: Unbalanced braces {{ }} in node")

            # Check classDef syntax
            elif stripped.startswith('classDef'):
                if not re.match(r'classDef\s+\w+\s+', stripped):
                    issues.append(f"Line {i}: Invalid classDef syntax. Use: 'classDef className styles'")

            # Check class application syntax
            elif stripped.startswith('class '):
                if not re.match(r'class\s+[\w,]+\s+\w+', stripped):
                    issues.append(f"Line {i}: Invalid class syntax. Use: 'class node1,node2 className'")

            # Check direction inside subgraph
            elif stripped.startswith('direction'):
                if in_subgraph == 0:
                    warnings.append(f"Line {i}: 'direction' should be inside a subgraph")
                parts = stripped.split()
                if len(parts) >= 2 and parts[1] not in valid_directions:
                    issues.append(f"Line {i}: Invalid direction '{parts[1]}'")

            # Check for common syntax errors
            if '|>' in stripped and '--|>' not in stripped and '--o' not in stripped:
                warnings.append(f"Line {i}: Did you mean '--|>' for arrow with text?")

            # Check for HTML in labels
            if '<br>' in stripped.lower() or '<br/>' in stripped.lower():
                # This is fine in Mermaid
                pass
            elif '<small>' in stripped.lower():
                # This is fine in Mermaid
                pass
            elif '<' in stripped and '>' in stripped:
                # Could be HTML - check if it's valid
                if not re.search(r'<(br|small|b|i|u|s|sub|sup)/?>', stripped, re.I):
                    if '-->' not in stripped and '-.->-' not in stripped:
                        warnings.append(f"Line {i}: Possible invalid HTML tag in label")

    # Check for unclosed subgraphs
    if in_subgraph > 0:
        issues.append(f"Unclosed subgraph(s): {in_subgraph} 'end' statement(s) missing")

    # Check for empty file
    if not found_diagram_type:
        issues.append("No diagram type declaration found")

    return {
        'valid': len(issues) == 0,
        'issues': issues,
        'warnings': warnings,
        'diagram_type': diagram_type,
        'line_count': line_count
    }

def main():
    """Run the Mermaid syntax audit."""
    print("=" * 80)
    print("MERMAID DIAGRAM SYNTAX AUDIT")
    print("=" * 80)
    print()

    files = find_all_mermaid_files()
    print(f"Found {len(files)} Mermaid diagram files")
    print()

    results = {
        'total': len(files),
        'valid': 0,
        'with_issues': 0,
        'with_warnings': 0,
        'files': []
    }

    # Group by module
    modules = {}
    for f in files:
        parts = f.parts
        if 'modules' in parts:
            idx = parts.index('modules')
            if idx + 1 < len(parts):
                module = parts[idx + 1]
                if module not in modules:
                    modules[module] = []
                modules[module].append(f)

    all_issues = []
    all_warnings = []

    for module in sorted(modules.keys()):
        print(f"## {module.title()} Module")
        print()

        for file_path in sorted(modules[module]):
            result = validate_mermaid_syntax(file_path)
            filename = file_path.name

            status = "✅" if result['valid'] else "❌"
            if result['valid'] and result['warnings']:
                status = "⚠️"

            print(f"### {filename}")
            print(f"- **Type:** {result['diagram_type'] or 'Unknown'}")
            print(f"- **Lines:** {result['line_count']}")
            print(f"- **Status:** {status}")

            if result['issues']:
                print(f"- **Issues ({len(result['issues'])}):**")
                for issue in result['issues']:
                    print(f"  - {issue}")
                    all_issues.append(f"{filename}: {issue}")
                results['with_issues'] += 1

            if result['warnings']:
                print(f"- **Warnings ({len(result['warnings'])}):**")
                for warning in result['warnings']:
                    print(f"  - {warning}")
                    all_warnings.append(f"{filename}: {warning}")
                results['with_warnings'] += 1

            if result['valid']:
                results['valid'] += 1

            results['files'].append({
                'path': str(file_path),
                'name': filename,
                'module': module,
                'valid': result['valid'],
                'issues': result['issues'],
                'warnings': result['warnings']
            })

            print()

        print()

    # Summary
    print("=" * 80)
    print("AUDIT SUMMARY")
    print("=" * 80)
    print()
    print(f"**Total Files:** {results['total']}")
    print(f"**Valid:** {results['valid']}")
    print(f"**With Issues:** {results['with_issues']}")
    print(f"**With Warnings:** {results['with_warnings']}")
    print()

    if all_issues:
        print("### All Issues")
        for issue in all_issues:
            print(f"- {issue}")
        print()

    if all_warnings:
        print("### All Warnings")
        for warning in all_warnings:
            print(f"- {warning}")
        print()

    # Final result
    if results['with_issues'] == 0:
        print("**Overall Result:** ✅ ALL DIAGRAMS VALID")
    else:
        print(f"**Overall Result:** ❌ {results['with_issues']} DIAGRAM(S) HAVE ISSUES")

    return results

if __name__ == '__main__':
    main()
