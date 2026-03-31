#!/usr/bin/env python3
"""
Professional PDF Book Generator with Background and Styling
Generates "Why Sit Here and Die?" as a complete, professionally designed PDF
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image, PageTemplate, Frame
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from datetime import datetime
import json
import re

# Load book content
try:
    with open('book-data-complete.js', 'r') as f:
        content = f.read()
        # Extract JSON from JavaScript
        start = content.find('{')
        end = content.rfind('}') + 1
        book_data = json.loads(content[start:end])
except:
    print("Error loading book data. Make sure book-data-complete.js exists.")
    exit(1)

# PDF Configuration
PDF_FILE = "Why_Sit_Here_and_Die_Complete.pdf"
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 0.75 * inch
GOLD_COLOR = colors.HexColor('#c9a84c')
BLACK_COLOR = colors.HexColor('#0a0a0a')
CREAM_COLOR = colors.HexColor('#f5f0e8')
BURGUNDY_COLOR = colors.HexColor('#3d0c11')
LIGHT_BG = colors.HexColor('#1a1a1a')

class NumberedCanvas(canvas.Canvas):
    """Canvas with page numbers and background"""
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._bg_drawn = False

    def showPage(self):
        # Draw background
        self.setFillColor(BLACK_COLOR)
        self.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
        
        # Draw decorative border
        self.setStrokeColor(GOLD_COLOR)
        self.setLineWidth(2)
        self.rect(0.5*inch, 0.5*inch, PAGE_WIDTH - inch, PAGE_HEIGHT - inch, fill=0, stroke=1)
        
        # Draw page number
        self.setFont("Helvetica", 10)
        self.setFillColor(GOLD_COLOR)
        page_num = self.getPageNumber()
        self.drawString(PAGE_WIDTH - 1*inch, 0.5*inch, str(page_num))
        
        canvas.Canvas.showPage(self)

# Create PDF with custom canvas
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

# Title Style
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=32,
    textColor=GOLD_COLOR,
    spaceAfter=12,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold',
    letterSpacing=3
)

# Subtitle Style
subtitle_style = ParagraphStyle(
    'CustomSubtitle',
    parent=styles['Normal'],
    fontSize=14,
    textColor=CREAM_COLOR,
    spaceAfter=6,
    alignment=TA_CENTER,
    fontName='Helvetica-Oblique',
    leading=18
)

# Chapter Title Style
chapter_title_style = ParagraphStyle(
    'ChapterTitle',
    parent=styles['Heading2'],
    fontSize=20,
    textColor=GOLD_COLOR,
    spaceAfter=12,
    spaceBefore=12,
    fontName='Helvetica-Bold',
    letterSpacing=2
)

# Body Text Style (14pt)
body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['Normal'],
    fontSize=14,
    textColor=CREAM_COLOR,
    spaceAfter=12,
    alignment=TA_JUSTIFY,
    fontName='Helvetica',
    leading=22,
    leftIndent=0.3*inch,
    rightIndent=0.3*inch
)

# Hook/Quote Style
hook_style = ParagraphStyle(
    'Hook',
    parent=styles['Normal'],
    fontSize=13,
    textColor=GOLD_COLOR,
    spaceAfter=12,
    alignment=TA_CENTER,
    fontName='Helvetica-Oblique',
    leading=18,
    leftIndent=0.5*inch,
    rightIndent=0.5*inch
)

# Author Style
author_style = ParagraphStyle(
    'Author',
    parent=styles['Normal'],
    fontSize=12,
    textColor=CREAM_COLOR,
    spaceAfter=6,
    alignment=TA_CENTER,
    fontName='Helvetica'
)

# Build PDF Content
story = []

# ===== TITLE PAGE =====
story.append(Spacer(1, 2*inch))
story.append(Paragraph("WHY SIT HERE AND DIE?", title_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph(book_data['metadata']['subtitle'], subtitle_style))
story.append(Spacer(1, 0.8*inch))
story.append(Paragraph(f"by {book_data['metadata']['author']}", author_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph(book_data['metadata']['church'], author_style))
story.append(Spacer(1, 1.5*inch))
story.append(Paragraph(f"© {book_data['metadata']['year']} {book_data['metadata']['author']}", author_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("All rights reserved.", author_style))
story.append(PageBreak())

# ===== DEDICATION =====
story.append(Spacer(1, 1*inch))
story.append(Paragraph("DEDICATION", chapter_title_style))
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph(book_data['frontMatter']['dedication'], body_style))
story.append(PageBreak())

# ===== EPIGRAPH =====
story.append(Spacer(1, 1.5*inch))
story.append(Paragraph("EPIGRAPH", chapter_title_style))
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph(book_data['frontMatter']['epigraph'], hook_style))
story.append(PageBreak())

# ===== FOREWORD =====
story.append(Paragraph("FOREWORD", chapter_title_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph(book_data['frontMatter']['foreword'], body_style))
story.append(PageBreak())

# ===== TABLE OF CONTENTS =====
story.append(Paragraph("TABLE OF CONTENTS", chapter_title_style))
story.append(Spacer(1, 0.3*inch))

toc_data = [['Chapter', 'Title', 'Page']]
page_num = 1
for i, ch in enumerate(book_data['chapters']):
    toc_data.append([f"Ch {ch['number']}", ch['title'], str(page_num)])
    page_num += 2  # Estimate 2 pages per chapter

toc_table = Table(toc_data, colWidths=[1*inch, 3.5*inch, 0.75*inch])
toc_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), GOLD_COLOR),
    ('TEXTCOLOR', (0, 0), (-1, 0), BLACK_COLOR),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 12),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), LIGHT_BG),
    ('TEXTCOLOR', (0, 1), (-1, -1), CREAM_COLOR),
    ('GRID', (0, 0), (-1, -1), 1, GOLD_COLOR),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 11),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [LIGHT_BG, colors.HexColor('#252525')]),
]))
story.append(toc_table)
story.append(PageBreak())

# ===== CHAPTERS =====
for chapter in book_data['chapters']:
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph(f"CHAPTER {chapter['number']}", chapter_title_style))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph(chapter['title'], subtitle_style))
    story.append(Spacer(1, 0.3*inch))
    
    # Chapter Hook/Quote
    story.append(Paragraph(f'"{chapter["hook"]}"', hook_style))
    story.append(Spacer(1, 0.4*inch))
    
    # Chapter Content
    content_text = chapter['content']
    # Split into paragraphs
    paragraphs = content_text.split('\n\n')
    for para in paragraphs:
        if para.strip():
            # Clean up the paragraph
            clean_para = para.strip().replace('\n', ' ')
            story.append(Paragraph(clean_para, body_style))
            story.append(Spacer(1, 0.15*inch))
    
    story.append(PageBreak())

# ===== CONCLUSION =====
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph("CONCLUSION", chapter_title_style))
story.append(Spacer(1, 0.3*inch))
conclusion_text = book_data['conclusion'].replace('\n', ' ')
story.append(Paragraph(conclusion_text, body_style))
story.append(PageBreak())

# ===== ABOUT THE AUTHOR =====
story.append(Spacer(1, 0.5*inch))
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

# Build PDF with custom canvas
doc.build(story, canvasmaker=NumberedCanvas)

print(f"✅ Professional PDF Generated Successfully!")
print(f"   File: {PDF_FILE}")
print(f"   Format: A4 (210 x 297 mm)")
print(f"   Font Size: 14pt (body text)")
print(f"   Font: Helvetica (professional)")
print(f"   Colors: Gold (#c9a84c), Cream (#f5f0e8), Black (#0a0a0a)")
print(f"   Background: Black with gold borders")
print(f"   Content: Complete book with all chapters")
print(f"   Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"\n📖 Book Contents:")
print(f"   - Title Page")
print(f"   - Dedication")
print(f"   - Epigraph")
print(f"   - Foreword")
print(f"   - Table of Contents")
print(f"   - Chapters 1-18 (Full content)")
print(f"   - Conclusion")
print(f"   - About the Author")
