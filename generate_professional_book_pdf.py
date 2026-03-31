#!/usr/bin/env python3
"""
Professional PDF Book Generator
Generates "Why Sit Here and Die?" as an international standard PDF
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from datetime import datetime
import json

# Load book content
with open('book-data-complete.js', 'r') as f:
    content = f.read()
    # Extract JSON from JavaScript
    start = content.find('{')
    end = content.rfind('}') + 1
    book_data = json.loads(content[start:end])

# PDF Configuration
PDF_FILE = "Why_Sit_Here_and_Die_Professional.pdf"
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 0.75 * inch
GOLD_COLOR = colors.HexColor('#c9a84c')
BLACK_COLOR = colors.HexColor('#0a0a0a')
CREAM_COLOR = colors.HexColor('#f5f0e8')
BURGUNDY_COLOR = colors.HexColor('#3d0c11')

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

# Title Style
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=28,
    textColor=GOLD_COLOR,
    spaceAfter=12,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold',
    letterSpacing=2
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
    fontSize=18,
    textColor=GOLD_COLOR,
    spaceAfter=12,
    spaceBefore=12,
    fontName='Helvetica-Bold',
    letterSpacing=1
)

# Body Text Style (14pt as requested)
body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['Normal'],
    fontSize=14,
    textColor=CREAM_COLOR,
    spaceAfter=12,
    alignment=TA_JUSTIFY,
    fontName='Helvetica',
    leading=20,
    leftIndent=0.25*inch,
    rightIndent=0.25*inch
)

# Hook/Quote Style
hook_style = ParagraphStyle(
    'Hook',
    parent=styles['Normal'],
    fontSize=12,
    textColor=GOLD_COLOR,
    spaceAfter=12,
    alignment=TA_CENTER,
    fontName='Helvetica-Oblique',
    leading=16,
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
story.append(Spacer(1, 1.5*inch))
story.append(Paragraph("WHY SIT HERE AND DIE?", title_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph(book_data['metadata']['subtitle'], subtitle_style))
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph(f"by {book_data['metadata']['author']}", author_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph(book_data['metadata']['church'], author_style))
story.append(Spacer(1, 1*inch))
story.append(Paragraph(f"© {book_data['metadata']['year']} {book_data['metadata']['author']}", author_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("All rights reserved.", author_style))
story.append(PageBreak())

# ===== DEDICATION =====
story.append(Paragraph("DEDICATION", chapter_title_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph(book_data['frontMatter']['dedication'], body_style))
story.append(PageBreak())

# ===== EPIGRAPH =====
story.append(Paragraph("EPIGRAPH", chapter_title_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph(book_data['frontMatter']['epigraph'], hook_style))
story.append(PageBreak())

# ===== FOREWORD =====
story.append(Paragraph("FOREWORD", chapter_title_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph(book_data['frontMatter']['foreword'], body_style))
story.append(PageBreak())

# ===== PREFACE =====
story.append(Paragraph("PREFACE", chapter_title_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph(book_data['frontMatter']['preface'], body_style))
story.append(PageBreak())

# ===== TABLE OF CONTENTS =====
story.append(Paragraph("TABLE OF CONTENTS", chapter_title_style))
story.append(Spacer(1, 0.3*inch))

toc_data = [['Chapter', 'Title']]
for ch in book_data['chapters']:
    toc_data.append([f"Chapter {ch['number']}", ch['title']])

toc_table = Table(toc_data, colWidths=[1.5*inch, 4*inch])
toc_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), GOLD_COLOR),
    ('TEXTCOLOR', (0, 0), (-1, 0), BLACK_COLOR),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 12),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 11),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey]),
]))
story.append(toc_table)
story.append(PageBreak())

# ===== CHAPTERS =====
for chapter in book_data['chapters']:
    # Chapter Header
    story.append(Paragraph(f"CHAPTER {chapter['number']}", chapter_title_style))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph(chapter['title'], subtitle_style))
    story.append(Spacer(1, 0.3*inch))
    
    # Chapter Hook/Quote
    story.append(Paragraph(f'"{chapter["hook"]}"', hook_style))
    story.append(Spacer(1, 0.3*inch))
    
    # Chapter Content
    # Split content into paragraphs
    paragraphs = chapter['content'].split('\n\n')
    for para in paragraphs:
        if para.strip():
            story.append(Paragraph(para.strip(), body_style))
            story.append(Spacer(1, 0.2*inch))
    
    story.append(PageBreak())

# ===== CONCLUSION =====
story.append(Paragraph("CONCLUSION", chapter_title_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph(book_data['conclusion'], body_style))
story.append(PageBreak())

# ===== ABOUT THE AUTHOR =====
story.append(Paragraph("ABOUT THE AUTHOR", chapter_title_style))
story.append(Spacer(1, 0.3*inch))
about_text = f"""
{book_data['metadata']['author']} is the Lead Pastor of {book_data['metadata']['church']}, Lagos, Nigeria. 
A preacher, teacher, and technology professional, he writes at the intersection of faith, leadership, and practical life.

"I wrote this book for the person I used to be—and sometimes still am."

This book was forged in a furnace of personal struggle and divine encounter. He writes not as someone who has arrived, 
but as someone who has learned one thing clearly: sitting is not a strategy. Movement is.
"""
story.append(Paragraph(about_text, body_style))

# Build PDF
doc.build(story)
print(f"✅ Professional PDF generated: {PDF_FILE}")
print(f"   - International Standard: A4 (210 x 297 mm)")
print(f"   - Font Size: 14pt (body text)")
print(f"   - Font: Helvetica (professional standard)")
print(f"   - Color Scheme: Gold (#c9a84c), Cream (#f5f0e8), Black (#0a0a0a)")
print(f"   - Content: Full book with all chapters")
print(f"   - Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
