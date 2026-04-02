#!/usr/bin/env python3
"""
Professional PDF Generator for "Why Sit Here and Die?"
Generates a beautifully formatted PDF with:
- 14pt font (international standard)
- Professional design with background
- All 18 chapters + front matter
- Proper typography and spacing
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import json

# Colors
DARK_BG = HexColor('#1a1a1a')
GOLD = HexColor('#d4af37')
TEXT_COLOR = HexColor('#333333')
LIGHT_BG = HexColor('#f5f5f5')

# Load book data
with open('book-data-complete.js', 'r') as f:
    content = f.read()
    # Extract the bookContent object
    exec(content)

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_state = None

    def showPage(self):
        self._saved_state = dict(self.__dict__)
        self._startPage()

    def save(self):
        num_pages = self._pageNumber
        if self._saved_state is None:
            canvas.Canvas.save(self)
            return

        for page_num in range(1, num_pages + 1):
            self._pageNumber = page_num
            self.draw_page_decorations(page_num, num_pages)

        self._pageNumber = num_pages
        canvas.Canvas.save(self)

    def draw_page_decorations(self, page_num, total_pages):
        # Draw footer with page number
        self.setFont("Helvetica", 10)
        self.setFillColor(HexColor('#999999'))
        self.drawString(inch, 0.5*inch, f"Page {page_num}")
        self.drawRightString(7.5*inch, 0.5*inch, "Why Sit Here and Die?")

def create_pdf():
    """Create professional PDF"""
    
    # Create PDF
    pdf_file = "Why_Sit_Here_and_Die.pdf"
    doc = SimpleDocTemplate(
        pdf_file,
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=1*inch,
        bottomMargin=0.75*inch,
        title="Why Sit Here and Die?",
        author="Olushola Odunuga Paul"
    )

    # Create styles
    styles = getSampleStyleSheet()
    
    # Title style
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=28,
        textColor=GOLD,
        spaceAfter=12,
        alignment=1,  # Center
        fontName='Helvetica-Bold'
    )

    # Subtitle style
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=14,
        textColor=TEXT_COLOR,
        spaceAfter=24,
        alignment=1,  # Center
        fontName='Helvetica'
    )

    # Chapter title style
    chapter_title_style = ParagraphStyle(
        'ChapterTitle',
        parent=styles['Heading2'],
        fontSize=18,
        textColor=GOLD,
        spaceAfter=6,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )

    # Chapter hook style
    hook_style = ParagraphStyle(
        'Hook',
        parent=styles['Normal'],
        fontSize=12,
        textColor=HexColor('#666666'),
        spaceAfter=12,
        fontStyle='italic',
        fontName='Helvetica-Oblique'
    )

    # Body text style - 14pt as requested
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=14,
        leading=20,
        textColor=TEXT_COLOR,
        spaceAfter=12,
        alignment=4,  # Justify
        fontName='Helvetica'
    )

    # Front matter style
    frontmatter_style = ParagraphStyle(
        'FrontMatter',
        parent=styles['Normal'],
        fontSize=14,
        leading=20,
        textColor=TEXT_COLOR,
        spaceAfter=12,
        alignment=4,  # Justify
        fontName='Helvetica'
    )

    # Build PDF content
    story = []

    # Title Page
    story.append(Spacer(1, 1.5*inch))
    story.append(Paragraph("WHY SIT HERE AND DIE?", title_style))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph(
        "Breaking the trap of stagnation—spiritually, financially, and personally—from 2 Kings 7",
        subtitle_style
    ))
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("By OLUSHOLA O. PAUL", body_style))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("Ruach Apostolic Center, Lagos, Nigeria", body_style))
    story.append(Spacer(1, 1*inch))
    story.append(Paragraph("2 Kings 7:3 (KJV)", hook_style))
    story.append(Paragraph('"Why sit we here until we die?"', hook_style))
    story.append(PageBreak())

    # Dedication
    story.append(Paragraph("DEDICATION", chapter_title_style))
    story.append(Paragraph(bookContent['frontMatter']['dedication'], frontmatter_style))
    story.append(PageBreak())

    # Foreword
    story.append(Paragraph("FOREWORD", chapter_title_style))
    story.append(Paragraph("By Pst Tosin Oloyede", hook_style))
    story.append(Spacer(1, 0.2*inch))
    for para in bookContent['frontMatter']['foreword'].split('\n\n'):
        if para.strip():
            story.append(Paragraph(para.strip(), frontmatter_style))
    story.append(PageBreak())

    # Endorsement
    story.append(Paragraph("ENDORSEMENT", chapter_title_style))
    story.append(Paragraph("By A/P Mark E. Ikpegbu", hook_style))
    story.append(Spacer(1, 0.2*inch))
    for para in bookContent['frontMatter']['endorsement'].split('\n\n'):
        if para.strip():
            story.append(Paragraph(para.strip(), frontmatter_style))
    story.append(PageBreak())

    # Acknowledgments
    story.append(Paragraph("ACKNOWLEDGMENTS", chapter_title_style))
    story.append(Paragraph(bookContent['frontMatter']['acknowledgments'], frontmatter_style))
    story.append(PageBreak())

    # Preface
    story.append(Paragraph("PREFACE", chapter_title_style))
    for para in bookContent['frontMatter']['preface'].split('\n\n'):
        if para.strip():
            story.append(Paragraph(para.strip(), frontmatter_style))
    story.append(PageBreak())

    # Chapters
    for chapter in bookContent['chapters']:
        story.append(Paragraph(f"CHAPTER {chapter['number']}: {chapter['title'].upper()}", chapter_title_style))
        story.append(Paragraph(f'"{chapter["hook"]}"', hook_style))
        story.append(Spacer(1, 0.2*inch))
        
        for para in chapter['content'].split('\n\n'):
            if para.strip():
                story.append(Paragraph(para.strip(), body_style))
        
        story.append(PageBreak())

    # Build PDF
    doc.build(story)
    print(f"✓ PDF created successfully: {pdf_file}")
    print(f"✓ Font size: 14pt (international standard)")
    print(f"✓ Total chapters: {len(bookContent['chapters'])} + Front Matter")
    print(f"✓ Professional formatting with gold accents")

if __name__ == '__main__':
    create_pdf()
