# HTML Structure Guide — Professional Book Layout

## PROPER HTML STRUCTURE FOR BOOK PAGES

### Page Container
```html
<div id="book-wrapper">
  <!-- All pages go here -->
</div>
```

### Standard Page Structure
```html
<div class="page page-inner">
  <div class="page-content">
    <!-- Page content goes here -->
  </div>
  <div class="page-footer">
    <span class="footer-title">Book Title</span>
    <span class="footer-number">1</span>
  </div>
</div>
```

### Cover Page
```html
<div class="page page-cover">
  <div class="cover-content">
    <div class="cover-title">Book Title</div>
    <div class="cover-subtitle">Subtitle text</div>
    <div class="cover-divider"></div>
    <div class="cover-author">Author Name</div>
    <div class="cover-church">Organization</div>
  </div>
</div>
```

### Chapter Page
```html
<div class="page page-inner">
  <div class="page-content">
    <span class="chapter-label">Part One · Chapter One</span>
    <div class="chapter-number">01</div>
    <h2 class="chapter-title">Chapter Title</h2>
    <div class="chapter-hook">Hook text that introduces the chapter theme.</div>
    
    <div class="ch-body">
      <p class="drop-cap">First paragraph with drop cap...</p>
      <p>Regular paragraph...</p>
      
      <h3 class="section-heading">Section Heading</h3>
      <p>Section content...</p>
      
      <div class="scripture-pull">
        "Scripture text here..."
        <cite>Reference (Version)</cite>
      </div>
      
      <ul class="bullet-list">
        <li>List item one</li>
        <li>List item two</li>
      </ul>
      
      <div class="movement-box">
        <div class="movement-box-title">Movement Assignment</div>
        <p>Assignment text...</p>
      </div>
      
      <div class="prayer-box">
        <div class="prayer-box-title">Prayer</div>
        <p>Prayer text...</p>
      </div>
      
      <p class="closing-line">Closing line of chapter...</p>
    </div>
  </div>
  
  <div class="page-footer">
    <span class="footer-title">Book Title</span>
    <span class="footer-number">25</span>
  </div>
</div>
```

## ELEMENT REFERENCE

### Typography Elements

#### Chapter Label
```html
<span class="chapter-label">Part One · Chapter One</span>
```
- Font size: 0.75rem
- Color: Gold
- Uppercase
- Spacing: 0.2em letter-spacing

#### Chapter Number
```html
<div class="chapter-number">01</div>
```
- Font size: 3.5rem
- Color: Light gold (10% opacity)
- Font weight: 900
- Line height: 0.9

#### Chapter Title
```html
<h2 class="chapter-title">Chapter Title</h2>
```
- Font size: 1.8rem
- Font weight: 700
- Line height: 1.2
- Color: Dark text
- Page break after: avoid

#### Chapter Hook
```html
<div class="chapter-hook">Hook text here</div>
```
- Font size: 0.95rem
- Font style: Italic
- Border left: 2px gold
- Padding left: 1rem
- Color: Muted
- Page break inside: avoid

#### Section Heading
```html
<h3 class="section-heading">Section Title</h3>
```
- Font size: 1.05rem
- Font weight: 700
- Border bottom: 1px gold
- Margin: 1.5rem top, 0.6rem bottom
- Page break after: avoid

### Content Elements

#### Body Paragraph
```html
<p>Paragraph text here...</p>
```
- Font size: 11pt
- Line height: 1.8
- Text align: Justify
- Hyphens: Auto
- Orphans: 3
- Widows: 3
- Margin bottom: 0.9rem

#### Drop Cap Paragraph
```html
<p class="drop-cap">First letter will be large...</p>
```
- First letter: 3.5rem, gold, float left
- Proper line height and margin

#### Scripture Pull
```html
<div class="scripture-pull">
  "Scripture text..."
  <cite>Reference (Version)</cite>
</div>
```
- Background: Light gold (6% opacity)
- Border left: 3px gold
- Padding: 1rem 1.2rem
- Font style: Italic
- Page break inside: avoid

#### Bullet List
```html
<ul class="bullet-list">
  <li>Item one</li>
  <li>Item two</li>
  <li>Item three</li>
</ul>
```
- Padding left: 1.5rem
- Font size: 0.95rem
- Line height: 1.7
- Margin bottom per item: 0.5rem

### Box Elements

#### Movement Box
```html
<div class="movement-box">
  <div class="movement-box-title">Movement Assignment</div>
  <p>Assignment instructions...</p>
  <p>More details...</p>
</div>
```
- Background: Cream (#f0ebe0)
- Border: 1px gold
- Padding: 1.2rem 1.4rem
- Page break inside: avoid

#### Prayer Box
```html
<div class="prayer-box">
  <div class="prayer-box-title">Prayer</div>
  <p>Prayer text...</p>
</div>
```
- Background: Light burgundy (4% opacity)
- Border left: 3px burgundy
- Padding: 1rem 1.2rem
- Page break inside: avoid

#### Closing Line
```html
<p class="closing-line">Final thought...</p>
```
- Font style: Italic
- Color: Muted
- Border top: 1px gold
- Padding top: 1rem
- Margin top: 1.5rem

### Footer
```html
<div class="page-footer">
  <span class="footer-title">Book Title</span>
  <span class="footer-number">25</span>
</div>
```
- Position: Absolute, bottom 15mm
- Font size: 0.75rem
- Border top: 0.5px gold
- Padding top: 0.6rem

## COMPLETE PAGE EXAMPLE

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Why Sit Here and Die?</title>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400;1,700&family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="book-styles-optimized.css">
</head>
<body>

<div id="book-wrapper">

  <!-- COVER PAGE -->
  <div class="page page-cover">
    <div class="cover-content">
      <div class="cover-title">Why Sit Here<br>and Die?</div>
      <div class="cover-subtitle">Breaking the trap of stagnation — spiritually, financially, and personally — from 2 Kings 7</div>
      <div class="cover-divider"></div>
      <div class="cover-author">Olushola Odunuga Paul</div>
      <div class="cover-church">Lead Pastor · Ruach Apostolic Center · Lagos, Nigeria</div>
    </div>
  </div>

  <!-- CHAPTER 1 -->
  <div class="page page-inner">
    <div class="page-content">
      <span class="chapter-label">Part One · Chapter One</span>
      <div class="chapter-number">01</div>
      <h2 class="chapter-title">The Gate Mentality</h2>
      <div class="chapter-hook">The most dangerous place is not the battlefield — it's the place you learned to survive without hope.</div>
      
      <div class="ch-body">
        <p class="drop-cap">There is a kind of death that doesn't need a coffin...</p>
        
        <h3 class="section-heading">A Cold Open: The Clean-Looking Cage</h3>
        <p>He had a good chair...</p>
        
        <div class="scripture-pull">
          "And there were four leprous men at the entering in of the gate..."
          <cite>2 Kings 7:3 (KJV)</cite>
        </div>
        
        <h3 class="section-heading">Three Doors, One Decision</h3>
        <p>Look at their logic...</p>
        
        <ul class="bullet-list">
          <li>First point</li>
          <li>Second point</li>
        </ul>
        
        <div class="movement-box">
          <div class="movement-box-title">Movement Assignment</div>
          <p>Write the heading: MY GATES...</p>
        </div>
        
        <div class="prayer-box">
          <div class="prayer-box-title">Prayer</div>
          <p>Lord, expose every gate...</p>
        </div>
        
        <p class="closing-line">A gate is a passage, not a residence.</p>
      </div>
    </div>
    
    <div class="page-footer">
      <span class="footer-title">Why Sit Here and Die?</span>
      <span class="footer-number">25</span>
    </div>
  </div>

</div><!-- END BOOK WRAPPER -->

</body>
</html>
```

## BEST PRACTICES

### 1. Semantic HTML
- Use `<h2>` for chapter titles
- Use `<h3>` for section headings
- Use `<p>` for paragraphs
- Use `<ul>` for lists
- Use `<div>` for containers

### 2. Proper Nesting
```html
<!-- CORRECT -->
<div class="page">
  <div class="page-content">
    <h2>Title</h2>
    <p>Content</p>
  </div>
  <div class="page-footer">Footer</div>
</div>

<!-- INCORRECT -->
<div class="page">
  <h2>Title</h2>
  <p>Content</p>
  <div class="page-footer">Footer</div>
</div>
```

### 3. Class Naming
- Use descriptive class names
- Use kebab-case (not camelCase)
- Avoid generic names like "box" or "text"
- Be consistent across pages

### 4. Accessibility
- Use proper heading hierarchy
- Include alt text for images
- Use semantic HTML elements
- Ensure sufficient color contrast

### 5. Performance
- Minimize inline styles
- Use CSS classes instead
- Avoid unnecessary divs
- Optimize images

## COMMON MISTAKES TO AVOID

❌ **Don't:** Use `<br>` for spacing
✅ **Do:** Use CSS margins and padding

❌ **Don't:** Use inline styles
✅ **Do:** Use CSS classes

❌ **Don't:** Nest pages inside pages
✅ **Do:** Keep pages as siblings

❌ **Don't:** Use `<span>` for block elements
✅ **Do:** Use `<div>` for block elements

❌ **Don't:** Skip the page-footer
✅ **Do:** Include footer on every page

## VALIDATION CHECKLIST

- [ ] All pages have `.page` class
- [ ] All pages have `.page-content` div
- [ ] All pages have `.page-footer` div
- [ ] Chapter pages have `.chapter-label`
- [ ] Chapter pages have `.chapter-number`
- [ ] Chapter pages have `.chapter-title`
- [ ] Chapter pages have `.chapter-hook`
- [ ] All boxes have `page-break-inside: avoid`
- [ ] All headings have `page-break-after: avoid`
- [ ] All paragraphs have proper margins
- [ ] All lists use `<ul>` and `<li>`
- [ ] All scripture uses `.scripture-pull`
- [ ] All assignments use `.movement-box`
- [ ] All prayers use `.prayer-box`

---

**Ready to implement?** Follow the IMPLEMENTATION_GUIDE.md for step-by-step instructions.
