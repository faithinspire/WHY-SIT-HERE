# Why Sit Here and Die? - Complete Book System

A professional, mobile-first web application for reading and distributing "Why Sit Here and Die?" by Olushola Odunuga Paul.

## 🎯 Features

### Professional Webapp (`app.html`)
- **Dark Theme with Gold Accents**: Professional mobile-first design
- **Full-Screen Click-to-Read Interface**: Click any chapter to read full-screen
- **Navigation Arrows**: Move between chapters with Previous/Next buttons
- **Bottom Navigation**: HOME, CHAPTERS, PAYMENT, ACCESS screens
- **Responsive Design**: Works perfectly on mobile, tablet, and desktop
- **All 18 Chapters**: Complete book content + front matter

### Complete Book Content
- **Introduction**: Gateway to the message
- **Foreword**: By Pst Tosin Oloyede
- **Endorsement**: By A/P Mark E. Ikpegbu
- **Acknowledgments**: Author's gratitude
- **Preface**: "Before You Read This Book"
- **18 Full Chapters**: All chapters with complete content
  - Part 1: The Diagnosis (Chapters 1-4)
  - Part 2: The Spiritual Dimension (Chapters 5-8)
  - Part 3: The Personal Dimension (Chapters 9-12)
  - Part 4: The Journey Continues (Chapters 13-18)

### PDF Generator (`pdf-generator.html`)
- **Professional PDF Output**: 14pt font (international standard)
- **Beautiful Formatting**: Gold accents and professional typography
- **Complete Content**: All 18 chapters + front matter
- **Browser-Based**: No installation required
- **One-Click Generation**: Click "Generate PDF" button

## 🚀 Quick Start

### Online Reading
1. Open `app.html` in your browser
2. Click "GET BOOK" on the home screen
3. Browse chapters in the CHAPTERS screen
4. Click any chapter to read full-screen
5. Use Previous/Next arrows to navigate

### Generate PDF
1. Open `pdf-generator.html` in your browser
2. Click "📥 Generate PDF" button
3. PDF downloads automatically as `Why_Sit_Here_and_Die.pdf`

## 📁 File Structure

```
├── app.html                      # Main webapp (dark theme + gold accents)
├── book-data-complete.js         # All 18 chapters + front matter
├── pdf-generator.html            # Browser-based PDF generator
├── generate_pdf_professional.py  # Python PDF generator (optional)
├── README.md                     # This file
└── Why_Sit_Here_and_Die.pdf     # Generated PDF (created by pdf-generator.html)
```

## 🎨 Design Specifications

### Color Scheme
- **Dark Background**: #1a1a1a
- **Gold Accent**: #d4af37
- **Light Text**: #f5f5f5
- **Muted Text**: #b0b0b0

### Typography
- **Font**: Segoe UI, Tahoma, Geneva, Verdana, sans-serif
- **Body Text**: 14pt (international standard)
- **Line Height**: 1.8 (optimal readability)
- **Alignment**: Justified text

### Responsive Breakpoints
- Mobile: < 480px
- Tablet: 480px - 768px
- Desktop: > 768px

## 🔧 Technical Details

### Technologies Used
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **PDF Generation**: html2pdf.js library
- **Data Format**: JavaScript object (book-data-complete.js)
- **Deployment**: Vercel (auto-deploy on git push)

### Browser Compatibility
- Chrome/Edge: ✓ Full support
- Firefox: ✓ Full support
- Safari: ✓ Full support
- Mobile browsers: ✓ Full support

## 📱 Screen Navigation

### HOME Screen
- Book preview with cover
- "GET BOOK" button to access chapters
- Professional welcome message

### CHAPTERS Screen
- List of all chapters
- Chapter numbers, titles, and hooks
- Click to read full-screen
- Organized by parts

### READER Screen
- Full-screen chapter reading
- Chapter title and metadata
- Previous/Next navigation
- Page indicator
- Keyboard navigation (← →)

### PAYMENT Screen
- Purchase information
- Payment processing
- Access management

### ACCESS Screen
- Account status
- Access confirmation
- User information

## 🌐 Deployment

### Live URL
https://why-sit-here.vercel.app/app.html

### Deploy Steps
1. Push to GitHub: `git push origin master`
2. Vercel auto-deploys on push
3. Check deployment status at vercel.com

### Local Testing
1. Open `app.html` in browser
2. Or use a local server: `python -m http.server 8000`
3. Visit `http://localhost:8000/app.html`

## 📖 Book Information

**Title**: Why Sit Here and Die?
**Subtitle**: Breaking the trap of stagnation — spiritually, financially, and personally — from 2 Kings 7
**Author**: Olushola Odunuga Paul
**Church**: Ruach Apostolic Center, Lagos, Nigeria
**Year**: 2026
**Core Scripture**: 2 Kings 7:3–4 (KJV)

## 🎯 Key Features Implemented

✓ Professional dark theme with gold accents
✓ Full-screen click-to-read interface (NOT side-by-side)
✓ All 18 chapters with complete content
✓ Front matter (Introduction, Foreword, Endorsement, Acknowledgments, Preface)
✓ Mobile-first responsive design
✓ Bottom navigation (HOME, CHAPTERS, PAYMENT, ACCESS)
✓ Professional PDF generator with 14pt font
✓ Keyboard navigation support
✓ Smooth transitions and animations
✓ Git version control
✓ Vercel deployment

## 🔄 Updates & Maintenance

### To Update Content
1. Edit `book-data-complete.js`
2. Commit changes: `git add . && git commit -m "Update content"`
3. Push to GitHub: `git push origin master`
4. Vercel auto-deploys

### To Modify Design
1. Edit CSS in `app.html` or `pdf-generator.html`
2. Test locally
3. Commit and push

## 📞 Support

For issues or questions:
1. Check the README
2. Review the code comments
3. Test in different browsers
4. Check Vercel deployment logs

## 📄 License

Copyright © 2026 by Olushola O Paul. All rights reserved.

---

**Last Updated**: April 2026
**Status**: ✓ Complete and Live
**Version**: 2.0 (Complete Rebuild)
