#!/usr/bin/env python3
"""
Generate PDF for "Why Sit Here and Die?" book
Creates a professional PDF with all 18 chapters
"""

import json
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from datetime import datetime

# Load book data
with open('book-data-complete.js', 'r', encoding='utf-8') as f:
    content = f.read()
    # Extract the bookContent object
    start = content.find('{')
    end = content.rfind('}') + 1
    json_str = content[start:end]
    # Replace JavaScript syntax with JSON
    json_str = json_str.replace('const bookContent = ', '')
    json_str = json_str.replace("'", '"')
    json_str = json_str.replace('`', '"')
    
    # Parse manually since it's complex
    import re
    
# Alternative: Load from JSON file
with open('book-complete.json', 'r', encoding='utf-8') as f:
    book_data = json.load(f)

# Create PDF
pdf_filename = 'Why_Sit_Here_and_Die_Complete_Book.pdf'
doc = SimpleDocTemplate(pdf_filename, pagesize=letter,
                       rightMargin=0.75*inch, leftMargin=0.75*inch,
                       topMargin=0.75*inch, bottomMargin=0.75*inch)

# Container for PDF elements
elements = []

# Define styles
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=28,
    textColor=colors.HexColor('#c9a84c'),
    spaceAfter=12,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold'
)

subtitle_style = ParagraphStyle(
    'CustomSubtitle',
    parent=styles['Heading2'],
    fontSize=14,
    textColor=colors.HexColor('#3d0c11'),
    spaceAfter=24,
    alignment=TA_CENTER,
    fontName='Helvetica'
)

chapter_title_style = ParagraphStyle(
    'ChapterTitle',
    parent=styles['Heading2'],
    fontSize=16,
    textColor=colors.HexColor('#c9a84c'),
    spaceAfter=12,
    spaceBefore=12,
    fontName='Helvetica-Bold'
)

chapter_hook_style = ParagraphStyle(
    'ChapterHook',
    parent=styles['Normal'],
    fontSize=11,
    textColor=colors.HexColor('#3d0c11'),
    spaceAfter=12,
    alignment=TA_CENTER,
    fontName='Helvetica-Oblique',
    borderPadding=12,
    borderColor=colors.HexColor('#c9a84c'),
    borderWidth=1
)

body_style = ParagraphStyle(
    'BodyText',
    parent=styles['Normal'],
    fontSize=10,
    leading=14,
    alignment=TA_JUSTIFY,
    spaceAfter=12
)

# Title Page
elements.append(Spacer(1, 1.5*inch))
elements.append(Paragraph("WHY SIT HERE AND DIE?", title_style))
elements.append(Spacer(1, 0.3*inch))
elements.append(Paragraph(book_data['book']['metadata']['subtitle'], subtitle_style))
elements.append(Spacer(1, 0.5*inch))
elements.append(Paragraph(f"by {book_data['book']['metadata']['author']}", styles['Normal']))
elements.append(Spacer(1, 0.3*inch))
elements.append(Paragraph(book_data['book']['metadata']['church'], styles['Normal']))
elements.append(Spacer(1, 0.3*inch))
elements.append(Paragraph(str(book_data['book']['metadata']['year']), styles['Normal']))
elements.append(Spacer(1, 1*inch))
elements.append(Paragraph(book_data['book']['frontMatter']['titlePage']['copyright'], styles['Normal']))
elements.append(PageBreak())

# Dedication
elements.append(Paragraph("Dedication", chapter_title_style))
elements.append(Spacer(1, 0.2*inch))
elements.append(Paragraph(book_data['book']['frontMatter']['dedication'], body_style))
elements.append(PageBreak())

# Epigraph
elements.append(Spacer(1, 1*inch))
elements.append(Paragraph(book_data['book']['frontMatter']['epigraph'], chapter_hook_style))
elements.append(PageBreak())

# Foreword
elements.append(Paragraph("Foreword", chapter_title_style))
elements.append(Spacer(1, 0.2*inch))
foreword_text = book_data['book']['frontMatter']['foreword'].replace('\n', '<br/>')
elements.append(Paragraph(foreword_text, body_style))
elements.append(PageBreak())

# Endorsement
elements.append(Paragraph("Endorsement", chapter_title_style))
elements.append(Spacer(1, 0.2*inch))
endorsement_text = book_data['book']['frontMatter']['endorsement'].replace('\n', '<br/>')
elements.append(Paragraph(endorsement_text, body_style))
elements.append(PageBreak())

# Preface
elements.append(Paragraph("Preface", chapter_title_style))
elements.append(Spacer(1, 0.2*inch))
preface_text = book_data['book']['frontMatter']['preface'].replace('\n', '<br/>')
elements.append(Paragraph(preface_text, body_style))
elements.append(PageBreak())

# Table of Contents
elements.append(Paragraph("Table of Contents", chapter_title_style))
elements.append(Spacer(1, 0.3*inch))

for chapter in book_data['book']['chapters']:
    toc_entry = f"Chapter {chapter['number']}: {chapter['title']}"
    elements.append(Paragraph(toc_entry, body_style))

elements.append(PageBreak())

# Chapters
for chapter in book_data['book']['chapters']:
    elements.append(Paragraph(f"Chapter {chapter['number']}: {chapter['title']}", chapter_title_style))
    elements.append(Spacer(1, 0.1*inch))
    elements.append(Paragraph(chapter['hook'], chapter_hook_style))
    elements.append(Spacer(1, 0.2*inch))
    
    # Clean up content for PDF
    content_text = chapter['content'].replace('\n', '<br/>')
    elements.append(Paragraph(content_text, body_style))
    elements.append(PageBreak())

# Build PDF
try:
    doc.build(elements)
    print(f"✅ PDF created successfully: {pdf_filename}")
    print(f"📊 File size: {len(open(pdf_filename, 'rb').read()) / (1024*1024):.2f} MB")
except Exception as e:
    print(f"❌ Error creating PDF: {e}")
    import traceback
    traceback.print_exc()
