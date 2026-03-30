# Quick Reference — Professional Book Layout

## 🚀 START HERE

Your book is now professionally redesigned and ready to use.

**Main File:** `book-professional.html`

---

## 📖 WHAT'S FIXED

✅ Perfect page layout (A5: 148mm × 210mm)
✅ Consistent margins (20mm top/bottom, 18mm left, 16mm right)
✅ All content fits within page boundaries
✅ Professional typography hierarchy
✅ No broken or cut-off text
✅ Proper page numbering and footers
✅ Print-ready format
✅ Responsive design (mobile, tablet, desktop)

---

## 💻 HOW TO USE

### View in Browser
1. Open `book-professional.html` in any web browser
2. Scroll through pages
3. Responsive design adapts automatically

### Print to PDF
1. Open `book-professional.html` in browser
2. Press `Ctrl+P` (Windows) or `Cmd+P` (Mac)
3. Select "Print to PDF"
4. Page size: A5 (148mm × 210mm)
5. Save and distribute

### Print to Physical Book
1. Open `book-professional.html` in browser
2. Press `Ctrl+P` or `Cmd+P`
3. Select your printer
4. Page size: A5
5. Print settings: Color, exact colors

---

## 📝 EDITING CONTENT

### Add New Pages
Copy this structure and paste after any page:

```html
<div class="page page-inner">
  <div class="page-content">
    <!-- Your content here -->
  </div>
  <div class="page-footer">
    <span class="footer-title">Why Sit Here and Die?</span>
    <span class="footer-number">X</span>
  </div>
</div>
```

### Change Colors
Edit the CSS variables at the top:

```css
:root {
  --gold: #c9a84c;      /* Accent color */
  --dark: #0a0a0a;      /* Dark backgrounds */
  --cream: #faf7f2;     /* Page background */
  --text: #1a1a1a;      /* Body text */
  --muted: #5a5a5a;     /* Secondary text */
}
```

### Adjust Margins
Edit the CSS variables:

```css
:root {
  --margin-top: 20mm;
  --margin-bottom: 20mm;
  --margin-left: 18mm;
  --margin-right: 16mm;
}
```

---

## 🎨 STYLING CLASSES

### Headings
- `.chapter-label` - Small uppercase label (0.75rem, gold)
- `.chapter-number` - Large chapter number (3.5rem, light gold)
- `.chapter-title` - Main chapter heading (1.8rem, bold)
- `.section-heading` - Section break (1.05rem, with underline)

### Text Elements
- `.drop-cap` - First letter styled large (3.5rem, gold)
- `.scripture-pull` - Quoted scripture (italic, gold border)
- `.chapter-hook` - Chapter introduction (italic, gold border)
- `.closing-line` - Closing statement (italic, with border)

### Boxes
- `.movement-box` - Action box (cream background, gold border)
- `.prayer-box` - Prayer box (burgundy accent)
- `.bullet-list` - Bulleted list (proper indentation)

### Footer
- `.page-footer` - Footer container (absolute positioning)
- `.footer-title` - Left side text (italic, gold)
- `.footer-number` - Right side page number (bold)

---

## 📐 PAGE STRUCTURE

Every page follows this structure:

```html
<div class="page page-inner">
  <div class="page-content">
    <!-- Your content goes here -->
    <!-- Automatically respects margins -->
  </div>
  <div class="page-footer">
    <span class="footer-title">Book Title</span>
    <span class="footer-number">Page #</span>
  </div>
</div>
```

---

## 🎯 PROFESSIONAL STANDARDS

### Typography
- **Headings:** Playfair Display (serif)
- **Body:** EB Garamond (serif)
- **Line Height:** 1.8 (optimal readability)
- **Text Alignment:** Justified with hyphenation

### Spacing
- **Paragraph:** 0.9rem margin-bottom
- **Section Heading:** 1.5rem top, 0.6rem bottom
- **Box Padding:** 1.2rem
- **Footer:** 15mm from bottom

### Colors
- **Gold Accent:** #c9a84c
- **Dark:** #0a0a0a
- **Cream Background:** #faf7f2
- **Text:** #1a1a1a
- **Muted:** #5a5a5a

---

## 📱 RESPONSIVE BREAKPOINTS

### Desktop (Full Size)
- Page width: 148mm (A5)
- Margins: 20mm top/bottom, 18mm left/right
- Font sizes: Full

### Tablet (≤768px)
- Page width: 100%
- Margins: 15mm
- Font sizes: Reduced

### Mobile (≤480px)
- Page width: 100%
- Margins: 12mm
- Font sizes: Further reduced

---

## 🖨️ PRINT SETTINGS

### For PDF Export
- Page size: A5 (148mm × 210mm)
- Margins: 0 (handled by page layout)
- Color: Exact (preserve colors)
- Orientation: Portrait

### For Physical Printing
- Paper size: A5
- Color mode: CMYK or RGB
- Quality: High (300 DPI minimum)
- Binding: Left margin (18mm) for binding

---

## ✨ COMMON CUSTOMIZATIONS

### Change Book Title
Find and replace "Why Sit Here and Die?" with your title

### Change Author Name
Find and replace "Olushola Odunuga Paul" with your name

### Change Church/Organization
Find and replace "Ruach Apostolic Center · Lagos, Nigeria" with your info

### Add Chapter Content
Copy the preface page structure and modify the content

### Change Font
Replace font names in CSS (keep serif fonts for professional look)

---

## 🔍 TROUBLESHOOTING

**Q: Content is cut off at page edges**
A: Check margins in CSS variables. Should be 20mm top/bottom, 18mm left/right.

**Q: Text is too small on mobile**
A: Responsive design handles this automatically. Check media queries.

**Q: Colors don't print correctly**
A: In print dialog, enable "Exact colors" or "Print backgrounds".

**Q: Page breaks are awkward**
A: Add `page-break-after: avoid;` to headings or `page-break-inside: avoid;` to boxes.

**Q: Footer is misaligned**
A: Footer uses absolute positioning at 15mm from bottom. Adjust if needed.

---

## 📚 FILE STRUCTURE

```
book-professional.html          ← Main file (use this!)
PROFESSIONAL_REDESIGN_COMPLETE.md  ← Full documentation
QUICK_REFERENCE.md              ← This file
LAYOUT_FIXES.md                 ← Previous fixes (reference)
```

---

## 🎓 BEST PRACTICES

1. **Always use semantic HTML** - Use proper heading tags (h1, h2, h3)
2. **Maintain consistent spacing** - Use the defined CSS classes
3. **Test on multiple devices** - Check mobile, tablet, desktop
4. **Print preview before publishing** - Ensure layout looks correct
5. **Use the color palette** - Stick to defined colors for consistency
6. **Keep margins consistent** - Don't override margin variables
7. **Use page-break classes** - Prevent awkward page breaks

---

## 📞 SUPPORT

For detailed information, see:
- `PROFESSIONAL_REDESIGN_COMPLETE.md` - Full technical guide
- `LAYOUT_FIXES.md` - Previous fixes and improvements
- `HTML_STRUCTURE_GUIDE.md` - HTML structure details

---

## ✅ READY TO GO

Your book is now:
- ✅ Professionally formatted
- ✅ Print-ready
- ✅ Responsive
- ✅ Publication-quality

**Open `book-professional.html` and start using it!**

