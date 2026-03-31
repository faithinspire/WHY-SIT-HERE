#!/usr/bin/env python3
"""
FORCE BUILD - Complete PDF with ALL Book Content
Generates "Why Sit Here and Die?" with guaranteed full content
"""

from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm, pt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image, KeepTogether
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from datetime import datetime
import json
import sys

print("=" * 70)
print("BUILDING COMPLETE PDF - FORCING ALL CONTENT")
print("=" * 70)

# Load book content
print("\n[1/5] Loading book data...")
try:
    with open('book-data-complete.js', 'r', encoding='utf-8') as f:
        content = f.read()
        start = content.find('{')
        end = content.rfind('}') + 1
        book_data = json.loads(content[start:end])
    print("✓ Book data loaded successfully")
    print(f"  - Chapters: {len(book_data['chapters'])}")
    print(f"  - Author: {book_data['metadata']['author']}")
except Exception as e:
    print(f"✗ Error loading book data: {e}")
    sys.exit(1)

# PDF Configuration
PDF_FILE = "Why_Sit_Here_and_Die_Complete.pdf"
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 0.6 * inch

# Colors
GOLD = colors.HexColor('#c9a84c')
BLACK = colors.HexColor('#0a0a0a')
CREAM = colors.HexColor('#f5f0e8')
DARK_BG = colors.HexColor('#1a1a1a')

print("\n[2/5] Creating PDF document...")

# Custom canvas for background
class BackgroundCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)

    def showPage(self):
        # Black background
        self.setFillColor(BLACK)
        self.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
        
        # Gold border
        self.setStrokeColor(GOLD)
        self.setLineWidth(1.5)
        self.rect(0.4*inch, 0.4*inch, PAGE_WIDTH - 0.8*inch, PAGE_HEIGHT - 0.8*inch, fill=0, stroke=1)
        
        # Page number
        self.setFont("Helvetica", 9)
        self.setFillColor(GOLD)
        page_num = self.getPageNumber()
        self.drawString(PAGE_WIDTH - 0.8*inch, 0.5*inch, str(page_num))
        
        canvas.Canvas.showPage(self)

# Create PDF
doc = SimpleDocTemplate(
    PDF_FILE,
    pagesize=A4,
    rightMargin=MARGIN,
    leftMargin=MARGIN,
    topMargin=MARGIN,
    bottomMargin=MARGIN,
    title="Why Sit Here and Die?",
    author="Olushola Odunuga Paul",
    subject="A life-and-leadership wake-up call from 2 Kings 7",
    creator="Ruach Apostolic Center"
)

# Define Styles
styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'Title',
    parent=styles['Heading1'],
    fontSize=36,
    textColor=GOLD,
    spaceAfter=12,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold',
    letterSpacing=2
)

subtitle_style = ParagraphStyle(
    'Subtitle',
    parent=styles['Normal'],
    fontSize=14,
    textColor=CREAM,
    spaceAfter=8,
    alignment=TA_CENTER,
    fontName='Helvetica-Oblique',
    leading=18
)

chapter_title_style = ParagraphStyle(
    'ChapterTitle',
    parent=styles['Heading2'],
    fontSize=18,
    textColor=GOLD,
    spaceAfter=10,
    spaceBefore=10,
    fontName='Helvetica-Bold'
)

body_style = ParagraphStyle(
    'Body',
    parent=styles['Normal'],
    fontSize=12,
    textColor=CREAM,
    spaceAfter=10,
    alignment=TA_JUSTIFY,
    fontName='Helvetica',
    leading=18,
    leftIndent=0.2*inch,
    rightIndent=0.2*inch
)

hook_style = ParagraphStyle(
    'Hook',
    parent=styles['Normal'],
    fontSize=11,
    textColor=GOLD,
    spaceAfter=10,
    alignment=TA_CENTER,
    fontName='Helvetica-Oblique',
    leading=16,
    leftIndent=0.4*inch,
    rightIndent=0.4*inch
)

author_style = ParagraphStyle(
    'Author',
    parent=styles['Normal'],
    fontSize=11,
    textColor=CREAM,
    spaceAfter=6,
    alignment=TA_CENTER,
    fontName='Helvetica'
)

print("✓ PDF document created")

# Build content
print("\n[3/5] Building PDF content...")
story = []

# TITLE PAGE
story.append(Spacer(1, 2*inch))
story.append(Paragraph("WHY SIT HERE AND DIE?", title_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph(book_data['metadata']['subtitle'], subtitle_style))
story.append(Spacer(1, 0.8*inch))
story.append(Paragraph(f"by {book_data['metadata']['author']}", author_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph(book_data['metadata']['church'], author_style))
story.append(Spacer(1, 1.5*inch))
story.append(Paragraph(f"© {book_data['metadata']['year']}", author_style))
story.append(PageBreak())

# DEDICATION
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph("DEDICATION", chapter_title_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph(book_data['frontMatter']['dedication'], body_style))
story.append(PageBreak())

# EPIGRAPH
story.append(Spacer(1, 1*inch))
story.append(Paragraph("EPIGRAPH", chapter_title_style))
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph(book_data['frontMatter']['epigraph'], hook_style))
story.append(PageBreak())

# FOREWORD
story.append(Paragraph("FOREWORD", chapter_title_style))
story.append(Spacer(1, 0.3*inch))
foreword_text = book_data['frontMatter']['foreword'].replace('\n', ' ')
story.append(Paragraph(foreword_text, body_style))
story.append(PageBreak())

# TABLE OF CONTENTS
story.append(Paragraph("TABLE OF CONTENTS", chapter_title_style))
story.append(Spacer(1, 0.3*inch))

toc_data = [['Chapter', 'Title']]
for ch in book_data['chapters']:
    toc_data.append([f"Ch {ch['number']}", ch['title']])

toc_table = Table(toc_data, colWidths=[1.2*inch, 3.8*inch])
toc_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), GOLD),
    ('TEXTCOLOR', (0, 0), (-1, 0), BLACK),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 11),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
    ('BACKGROUND', (0, 1), (-1, -1), DARK_BG),
    ('TEXTCOLOR', (0, 1), (-1, -1), CREAM),
    ('GRID', (0, 0), (-1, -1), 1, GOLD),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 10),
]))
story.append(toc_table)
story.append(PageBreak())

# CHAPTERS - FORCE ALL CONTENT
print(f"  Adding {len(book_data['chapters'])} chapters...")
for i, chapter in enumerate(book_data['chapters']):
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph(f"CHAPTER {chapter['number']}", chapter_title_style))
    story.append(Spacer(1, 0.15*inch))
    story.append(Paragraph(chapter['title'], subtitle_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Hook
    hook_text = f'"{chapter["hook"]}"'
    story.append(Paragraph(hook_text, hook_style))
    story.append(Spacer(1, 0.3*inch))
    
    # Content - FORCE ALL TEXT
    content_text = chapter['content']
    if content_text:
        # Split and clean paragraphs
        paragraphs = content_text.split('\n\n')
        for para in paragraphs:
            if para.strip():
                clean_para = para.strip().replace('\n', ' ')
                story.append(Paragraph(clean_para, body_style))
                story.append(Spacer(1, 0.1*inch))
    
    story.append(PageBreak())
    print(f"  ✓ Chapter {chapter['number']} added")

# CONCLUSION
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("CONCLUSION", chapter_title_style))
story.append(Spacer(1, 0.3*inch))
conclusion_text = book_data['conclusion'].replace('\n', ' ')
story.append(Paragraph(conclusion_text, body_style))
story.append(PageBreak())

# ABOUT AUTHOR
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("ABOUT THE AUTHOR", chapter_title_style))
story.append(Spacer(1, 0.3*inch))
about_text = f"""
{book_data['metadata']['author']} is the Lead Pastor of {book_data['metadata']['church']}.
A preacher, teacher, and technology professional, he writes at the intersection of faith, leadership, and practical life.

"I wrote this book for the person I used to be—and sometimes still am."

This book was forged in a furnace of personal struggle and divine encounter. He writes not as someone who has arrived,
but as someone who has learned one thing clearly: sitting is not a strategy. Movement is.
"""
story.append(Paragraph(about_text, body_style))

print("✓ All content added to story")

# Build PDF
print("\n[4/5] Building PDF file...")
try:
    doc.build(story, canvasmaker=BackgroundCanvas)
    print("✓ PDF built successfully")
except Exception as e:
    print(f"✗ Error building PDF: {e}")
    sys.exit(1)

# Verify
print("\n[5/5] Verifying PDF...")
import os
if os.path.exists(PDF_FILE):
    file_size = os.path.getsize(PDF_FILE)
    print(f"✓ PDF file created: {PDF_FILE}")
    print(f"  File size: {file_size:,} bytes ({file_size/1024:.1f} KB)")
else:
    print(f"✗ PDF file not found!")
    sys.exit(1)

print("\n" + "=" * 70)
print("✅ PDF GENERATION COMPLETE")
print("=" * 70)
print(f"\nFile: {PDF_FILE}")
print(f"Format: A4 (210 x 297 mm)")
print(f"Font: Helvetica, 12pt body")
print(f"Colors: Gold (#c9a84c), Cream (#f5f0e8), Black (#0a0a0a)")
print(f"Background: Black with gold borders")
print(f"Content: COMPLETE BOOK (All chapters, front matter, conclusion)")
print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("\n📖 Book Contents:")
print("  ✓ Title Page")
print("  ✓ Dedication")
print("  ✓ Epigraph")
print("  ✓ Foreword")
print("  ✓ Table of Contents")
print(f"  ✓ Chapters 1-{len(book_data['chapters'])} (FULL CONTENT)")
print("  ✓ Conclusion")
print("  ✓ About the Author")
print("\n" + "=" * 70)
