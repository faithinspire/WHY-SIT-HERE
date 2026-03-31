#!/usr/bin/env python3
"""
Generate PDF for "Why Sit Here and Die?" book
Requires: pip install reportlab pypdf
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from datetime import datetime
import json

# Load book data
with open('book-complete.json', 'r', encoding='utf-8') as f:
    book_data = json.load(f)['book']

# Create PDF
pdf_filename = "Why_Sit_Here_and_Die_Complete_Book.pdf"
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
    spaceAfter=6,
    alignment=TA_CENTER,
    fontName='Helvetica'
)

author_style = ParagraphStyle(
    'Author',
    parent=styles['Normal'],
    fontSize=12,
    textColor=colors.black,
    spaceAfter=24,
    alignment=TA_CENTER,
    fontName='Helvetica'
)

chapter_title_style = ParagraphStyle(
    'ChapterTitle',
    parent=styles['Heading1'],
    fontSize=18,
    textColor=colors.HexColor('#c9a84c'),
    spaceAfter=6,
    spaceBefore=12,
    fontName='Helvetica-Bold'
)

chapter_hook_style = ParagraphStyle(
    'ChapterHook',
    parent=styles['Italic'],
    fontSize=11,
    textColor=colors.HexColor('#3d0c11'),
    spaceAfter=12,
    fontName='Helvetica-Oblique'
)

body_style = ParagraphStyle(
    'BodyText',
    parent=styles['BodyText'],
    fontSize=10,
    alignment=TA_JUSTIFY,
    spaceAfter=6,
    leading=14
)

# TITLE PAGE
elements.append(Spacer(1, 1.5*inch))
elements.append(Paragraph(book_data['metadata']['title'], title_style))
elements.append(Spacer(1, 0.3*inch))
elements.append(Paragraph(book_data['metadata']['subtitle'], subtitle_style))
elements.append(Spacer(1, 0.5*inch))
elements.append(Paragraph(f"By {book_data['metadata']['author']}", author_style))
elements.append(Spacer(1, 0.3*inch))
elements.append(Paragraph(book_data['metadata']['church'], author_style))
elements.append(Spacer(1, 1*inch))
elements.append(Paragraph(book_data['metadata']['coreScripture'], author_style))
elements.append(PageBreak())

# DEDICATION
elements.append(Paragraph("Dedication", chapter_title_style))
elements.append(Spacer(1, 0.2*inch))
elements.append(Paragraph(book_data['frontMatter']['dedication'], body_style))
elements.append(PageBreak())

# EPIGRAPH
elements.append(Paragraph("Epigraph", chapter_title_style))
elements.append(Spacer(1, 0.2*inch))
elements.append(Paragraph(book_data['frontMatter']['epigraph'], body_style))
elements.append(PageBreak())

# ACKNOWLEDGMENTS
elements.append(Paragraph("Acknowledgments", chapter_title_style))
elements.append(Spacer(1, 0.2*inch))
elements.append(Paragraph(book_data['frontMatter']['acknowledgments'], body_style))
elements.append(PageBreak())

# TABLE OF CONTENTS
elements.append(Paragraph("Table of Contents", chapter_title_style))
elements.append(Spacer(1, 0.2*inch))

for part_key, part_data in book_data['structure'].items():
    if part_key.startswith('PART_'):
        elements.append(Paragraph(f"<b>{part_data['title']}</b>", body_style))
        for ch_num in part_data['chapters']:
            chapter = next((c for c in book_data['chapters'] if c['number'] == ch_num), None)
            if chapter:
                elements.append(Paragraph(
                    f"Chapter {ch_num}: {chapter['title']}", 
                    ParagraphStyle('TOC', parent=styles['Normal'], fontSize=9, leftIndent=20)
                ))
        elements.append(Spacer(1, 0.1*inch))

elements.append(PageBreak())

# CHAPTERS
for chapter in book_data['chapters']:
    elements.append(Paragraph(f"Chapter {chapter['number']}", chapter_title_style))
    elements.append(Paragraph(chapter['title'], subtitle_style))
    elements.append(Spacer(1, 0.1*inch))
    elements.append(Paragraph(f"<i>{chapter['hook']}</i>", chapter_hook_style))
    elements.append(Spacer(1, 0.2*inch))
    
    # Add chapter content (truncated for demo - full content would be added here)
    elements.append(Paragraph(
        f"[Chapter {chapter['number']} content - Full text available in book-data-complete.js]",
        body_style
    ))
    elements.append(Spacer(1, 0.3*inch))
    elements.append(PageBreak())

# BACK MATTER
elements.append(Paragraph("About the Author", chapter_title_style))
elements.append(Spacer(1, 0.2*inch))
elements.append(Paragraph(
    f"Olushola Odunuga Paul is the Lead Pastor of Ruach Apostolic Center in Lagos, Nigeria. "
    f"He is dedicated to helping believers move from stagnation to significance through biblical principles "
    f"and practical application. This book represents his journey and his passion to see others rise from their gates.",
    body_style
))
elements.append(Spacer(1, 0.3*inch))
elements.append(Paragraph("Connect with the Author", chapter_title_style))
elements.append(Spacer(1, 0.2*inch))
elements.append(Paragraph(
    f"Church: Ruach Apostolic Center, Lagos, Nigeria<br/>"
    f"Website: https://why-sit-here.vercel.app<br/>"
    f"For speaking engagements and workshops, contact through the website.",
    body_style
))

# Build PDF
doc.build(elements)
print(f"✅ PDF generated successfully: {pdf_filename}")
print(f"📄 File size: {len(open(pdf_filename, 'rb').read()) / 1024:.2f} KB")
print(f"📍 Location: {pdf_filename}")
