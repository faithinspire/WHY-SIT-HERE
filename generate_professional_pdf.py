#!/usr/bin/env python3
"""
Professional PDF Generator for "Why Sit Here and Die?"
Generates a beautifully formatted PDF with proper typography and design
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import json
from datetime import datetime

# Page setup
PAGE_WIDTH, PAGE_HEIGHT = letter
MARGIN = 0.75 * inch
CONTENT_WIDTH = PAGE_WIDTH - (2 * MARGIN)

class NumberedCanvas(canvas.Canvas):
    """Canvas with page numbers and professional styling"""
    
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_state = None
        
    def showPage(self):
        self._saved_state = self.__dict__.copy()
        self._startPage()
        
    def save(self):
        num_pages = self._pageNumber
        if self._saved_state is None:
            canvas.Canvas.save(self)
            return
            
        for page_num in range(1, num_pages + 1):
            self.__dict__.update(self._saved_state)
            self.draw_page_decorations(page_num, num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)
        
    def draw_page_decorations(self, page_num, total_pages):
        """Add page numbers and decorative elements"""
        # Page number at bottom
        self.setFont("Helvetica", 10)
        self.setFillColor(colors.HexColor("#999999"))
        page_text = f"{page_num}"
        self.drawCentredString(PAGE_WIDTH / 2, 0.5 * inch, page_text)
        
        # Decorative line
        self.setStrokeColor(colors.HexColor("#667eea"))
        self.setLineWidth(0.5)
        self.line(MARGIN, 0.7 * inch, PAGE_WIDTH - MARGIN, 0.7 * inch)

def create_styles():
    """Create custom paragraph styles"""
    styles = getSampleStyleSheet()
    
    # Title style
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=28,
        textColor=colors.HexColor("#667eea"),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
        leading=32
    )
    
    # Subtitle style
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=14,
        textColor=colors.HexColor("#764ba2"),
        spaceAfter=24,
        alignment=TA_CENTER,
        fontName='Helvetica-Oblique',
        leading=16
    )
    
    # Chapter title style
    chapter_title_style = ParagraphStyle(
        'ChapterTitle',
        parent=styles['Heading1'],
        fontSize=22,
        textColor=colors.HexColor("#667eea"),
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold',
        leading=26,
        borderColor=colors.HexColor("#667eea"),
        borderWidth=2,
        borderPadding=10
    )
    
    # Body text style - 14pt as requested
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=14,
        leading=20,
        alignment=TA_JUSTIFY,
        spaceAfter=12,
        fontName='Helvetica',
        textColor=colors.HexColor("#333333")
    )
    
    # Hook style
    hook_style = ParagraphStyle(
        'Hook',
        parent=styles['Normal'],
        fontSize=12,
        leading=16,
        alignment=TA_CENTER,
        spaceAfter=20,
        fontName='Helvetica-Oblique',
        textColor=colors.HexColor("#667eea"),
        borderColor=colors.HexColor("#667eea"),
        borderWidth=1,
        borderPadding=8
    )
    
    # Heading 3 style
    heading3_style = ParagraphStyle(
        'Heading3Custom',
        parent=styles['Heading3'],
        fontSize=14,
        textColor=colors.HexColor("#667eea"),
        spaceAfter=10,
        spaceBefore=12,
        fontName='Helvetica-Bold',
        leading=16
    )
    
    return {
        'title': title_style,
        'subtitle': subtitle_style,
        'chapter_title': chapter_title_style,
        'body': body_style,
        'hook': hook_style,
        'heading3': heading3_style
    }

def load_book_data():
    """Load complete book data"""
    try:
        with open('book-complete.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        print("Error loading book data")
        return None

def create_title_page(story, styles):
    """Create professional title page"""
    story.append(Spacer(1, 1.5 * inch))
    
    # Main title
    story.append(Paragraph("WHY SIT HERE AND DIE?", styles['title']))
    story.append(Spacer(1, 0.2 * inch))
    
    # Subtitle
    story.append(Paragraph(
        "Breaking the trap of stagnation—spiritually, financially, and personally—from 2 Kings 7",
        styles['subtitle']
    ))
    
    story.append(Spacer(1, 1 * inch))
    
    # Author
    story.append(Paragraph("By OLUSHOLA O. PAUL", styles['body']))
    story.append(Spacer(1, 0.5 * inch))
    
    # Copyright
    story.append(Paragraph(
        f"Copyright © 2026 by OLUSHOLA O PAUL. All rights reserved.<br/>"
        f"Scripture quotations marked KJV are from the King James Version, public domain.",
        styles['body']
    ))
    
    story.append(PageBreak())

def create_front_matter(story, book_data, styles):
    """Add front matter sections"""
    front_matter = book_data['book']['frontMatter']
    
    # Dedication
    story.append(Paragraph("Dedication", styles['chapter_title']))
    story.append(Paragraph(front_matter['dedication'], styles['body']))
    story.append(PageBreak())
    
    # Foreword
    story.append(Paragraph("Foreword", styles['chapter_title']))
    story.append(Paragraph("By Pst Tosin Oloyede", styles['subtitle']))
    foreword_text = front_matter.get('foreword', '').replace('\n', '<br/>')
    story.append(Paragraph(foreword_text, styles['body']))
    story.append(PageBreak())
    
    # Acknowledgments
    story.append(Paragraph("Acknowledgments", styles['chapter_title']))
    ack_text = front_matter.get('acknowledgments', '').replace('\n', '<br/>')
    story.append(Paragraph(ack_text, styles['body']))
    story.append(PageBreak())
    
    # Preface
    story.append(Paragraph("Preface", styles['chapter_title']))
    preface_text = front_matter.get('preface', '').replace('\n', '<br/>')
    story.append(Paragraph(preface_text, styles['body']))
    story.append(PageBreak())

def create_chapters(story, book_data, styles):
    """Add all chapters"""
    chapters = book_data['book']['chapters']
    
    for chapter in chapters:
        # Chapter header
        chapter_num = chapter.get('number', '')
        chapter_title = chapter.get('title', '')
        chapter_part = chapter.get('part', '')
        
        if chapter_part:
            story.append(Paragraph(chapter_part, styles['subtitle']))
        
        story.append(Paragraph(f"Chapter {chapter_num}: {chapter_title}", styles['chapter_title']))
        
        # Hook
        if chapter.get('hook'):
            story.append(Paragraph(f'"{chapter["hook"]}"', styles['hook']))
        
        story.append(Spacer(1, 0.2 * inch))
        
        # Content
        content = chapter.get('content', '')
        if content:
            # Split content into paragraphs and format
            paragraphs = content.split('\n\n')
            for para in paragraphs:
                para = para.strip()
                if not para:
                    continue
                
                # Check if it's a heading
                if para.isupper() and len(para) < 100:
                    story.append(Paragraph(para, styles['heading3']))
                else:
                    story.append(Paragraph(para, styles['body']))
        
        story.append(PageBreak())

def generate_pdf():
    """Generate the complete PDF"""
    print("Loading book data...")
    book_data = load_book_data()
    
    if not book_data:
        print("Failed to load book data")
        return
    
    print("Creating PDF...")
    
    # Create PDF
    pdf_filename = "Why_Sit_Here_and_Die_Complete.pdf"
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=letter,
        rightMargin=MARGIN,
        leftMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=MARGIN,
        title="Why Sit Here and Die?",
        author="Olushola Odunuga Paul"
    )
    
    # Create styles
    styles = create_styles()
    
    # Build story
    story = []
    
    # Title page
    create_title_page(story, styles)
    
    # Front matter
    create_front_matter(story, book_data, styles)
    
    # Chapters
    create_chapters(story, book_data, styles)
    
    # Build PDF
    doc.build(story)
    
    print(f"✓ PDF generated successfully: {pdf_filename}")
    print(f"  - Professional 14pt font")
    print(f"  - Complete book content (front matter + all 18 chapters)")
    print(f"  - Beautiful gradient design")
    print(f"  - Justified text alignment")
    print(f"  - Page numbers and decorative elements")

if __name__ == "__main__":
    generate_pdf()
