#!/bin/bash
# Batch render Mermaid diagrams to PNG and SVG
# Requires: npm install -g @mermaid-js/mermaid-cli

echo "========================================"
echo "Mermaid Diagram Batch Renderer"
echo "========================================" 
echo ""

# Check if mmdc is installed
if ! command -v mmdc &> /dev/null; then
    echo "❌ Error: mermaid-cli not installed"
    echo ""
    echo "Install with:"
    echo "  npm install -g @mermaid-js/mermaid-cli"
    echo ""
    exit 1
fi

# Determine repository root
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
cd "$ROOT_DIR"

# Collect module diagram files
mapfile -t mmd_files < <(find modules -type f -path "*/diagrams/*.mmd" | sort)
mmd_count=${#mmd_files[@]}

if [ "$mmd_count" -eq 0 ]; then
    echo "❌ No .mmd files found in modules/*/diagrams"
    echo "Run python3 tools/kanban/json_to_mermaid.py first"
    exit 1
fi

echo "Found $mmd_count Mermaid diagram files"
echo ""

# Render each .mmd file
for file in "${mmd_files[@]}"; do
    filename="${file%.mmd}"
    echo "Rendering $file..."
    
    # Generate PNG
    mmdc -i "$file" -o "${filename}.png" -b transparent 2>/dev/null && \
        echo "  ✓ Created ${filename}.png" || \
        echo "  ✗ Failed ${filename}.png"
    
    # Generate SVG
    mmdc -i "$file" -o "${filename}.svg" -b transparent 2>/dev/null && \
        echo "  ✓ Created ${filename}.svg" || \
        echo "  ✗ Failed ${filename}.svg"
    
    echo ""
done

echo "========================================"
echo "✓ Rendering complete!"
echo "========================================"



