#!/bin/bash
# LaTeX Compilation Script for sn-article.tex
# This script compiles the document with bibliography processing
# Run from project root directory - script will change to draft/ automatically

# Don't exit on error - LaTeX often generates PDFs despite warnings
set +e

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DRAFT_DIR="${SCRIPT_DIR}/draft"

# Change to draft directory
cd "$DRAFT_DIR" || { echo "Error: Cannot access draft directory"; exit 1; }

echo "=== LaTeX Compilation Script ==="
echo "Working directory: $DRAFT_DIR"
echo ""

# Step 1: First pdflatex pass
echo "Step 1/4: First pdflatex pass..."
pdflatex -interaction=nonstopmode sn-article.tex > /dev/null 2>&1
echo "  ✓ First pass complete"

# Step 2: BibTeX for bibliography
echo "Step 2/4: Processing bibliography with BibTeX..."
bibtex sn-article > /dev/null 2>&1
echo "  ✓ Bibliography processed"

# Step 3: Second pdflatex pass (resolve citations)
echo "Step 3/4: Second pdflatex pass (resolving citations)..."
pdflatex -interaction=nonstopmode sn-article.tex > /dev/null 2>&1
echo "  ✓ Citations resolved"

# Step 4: Third pdflatex pass (finalize references)
echo "Step 4/4: Third pdflatex pass (finalizing references)..."
pdflatex -interaction=nonstopmode sn-article.tex > compile_output.log 2>&1
echo "  ✓ Final pass complete"
echo ""

# Check for fatal errors (but allow non-fatal ones if PDF is generated)
if [ -f sn-article.pdf ]; then
    echo "✓ PDF generated successfully!"
    # Check for errors but don't fail if PDF exists
    if grep -q "LaTeX Error" compile_output.log; then
        echo "⚠ WARNING: Some errors detected (check log for details)"
        grep "LaTeX Error" compile_output.log | head -3
    fi
else
    echo "✗ FATAL: PDF not generated!"
    grep "Error" compile_output.log | head -5
    exit 1
fi

# Report warnings
WARNINGS=$(grep -c "LaTeX Warning" compile_output.log || echo "0")
UNDEFINED=$(grep -c "undefined" compile_output.log || echo "0")
MULTIPLY_DEFINED=$(grep -c "multiply-defined" compile_output.log || echo "0")

echo ""
echo "=== Compilation Summary ==="
echo "PDF generated: draft/sn-article.pdf"
if [ -f sn-article.pdf ]; then
    PAGES=$(pdfinfo sn-article.pdf 2>/dev/null | grep Pages | awk '{print $2}' || echo "unknown")
    SIZE=$(ls -lh sn-article.pdf | awk '{print $5}')
    echo "Pages: $PAGES"
    echo "Size: $SIZE"
fi
echo "Warnings: $WARNINGS"
echo "Undefined references: $UNDEFINED"
echo "Multiply-defined labels: $MULTIPLY_DEFINED"
echo ""
echo "Full log saved to: draft/compile_output.log"
