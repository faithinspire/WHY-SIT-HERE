# Chapter Template - For Iterative Development

## HTML Template for Adding Chapters

```html
<!-- CHAPTER X -->
<div class="page page-content">
    <div class="page-content-inner">
        <div class="chapter-number">CHAPTER X</div>
        <h2 class="chapter-title">Chapter Title Here</h2>
        <p>Opening paragraph - hook the reader with a real-life scenario or powerful statement.</p>
        <p>Continue with the main content. Each paragraph should be meaningful and engaging.</p>
    </div>
    <div class="page-number">XX</div>
</div>

<!-- CHAPTER X CONTINUED (if needed) -->
<div class="page page-content">
    <div class="page-content-inner">
        <p>Continue the chapter content here.</p>
        <p>Add more paragraphs as needed.</p>
        <h3>Subheading (if needed)</h3>
        <p>Additional content with subheadings for structure.</p>
    </div>
    <div class="page-number">XX</div>
</div>
```

## Chapter Structure

Each chapter should include:

1. **Cold Open** (1-2 paragraphs)
   - Real-life scenario
   - Dramatic hook
   - Relatable situation

2. **The Gate Question** (1 paragraph)
   - Uncomfortable question
   - Exposes passivity
   - Challenges reader

3. **Bible Mirror** (2-3 paragraphs)
   - 2 Kings 7 insight
   - Related Bible story
   - Connection to theme

4. **The Life Tool** (2-3 paragraphs)
   - Practical framework
   - Actionable steps
   - Real-world application

5. **Movement Assignment** (1 paragraph)
   - Specific action
   - 24-72 hour timeframe
   - Measurable outcome

6. **Closing Line** (1 sentence)
   - Powerful summary
   - Echoes the title
   - Memorable takeaway

## Chapters to Add (Iteration 2.1)

### Chapter 2: Name the Famine
- Scripture: 2 Kings 6:25
- Hook: You can't break what you refuse to describe
- Life Areas: Finances, academics, career clarity
- Key Takeaway: Scarcity is real—but denial is optional

### Chapter 3: When Rejection Becomes a Teacher
- Scripture: 2 Kings 7:3
- Hook: Some people weren't invited into comfort, so they discovered purpose
- Life Areas: Human development, self-worth, resilience
- Key Takeaway: Don't let pain name you. Let it train you

### Chapter 4: The Conversation That Changed Everything
- Scripture: "they said one to another…" (2 Kings 7:3)
- Hook: Your next level often begins with a hard conversation
- Life Areas: Leadership, relationships, teamwork
- Key Takeaway: Breakthrough starts when someone speaks truth in the group

## Page Numbering

- Continue from previous chapter
- Each page gets a unique number
- Use absolute positioning (already in CSS)
- Format: centered at bottom

## Testing Checklist

- [ ] HTML validates (W3C)
- [ ] CSS applies correctly
- [ ] Text fits on pages
- [ ] No overflow
- [ ] Page numbers visible
- [ ] Print preview looks good
- [ ] Mobile responsive
- [ ] Links work (if any)

## Commit Message Template

```
feat: Add Chapters X-Y to book

- Added Chapter X: [Title]
- Added Chapter Y: [Title]
- Added Chapter Z: [Title]
- Updated page numbering
- Tested layout consistency
- Verified print output

Iteration: 2.1
Status: Ready for review
```

## Deployment Steps

1. Add chapters to book-v2.html
2. Test thoroughly
3. Commit to Git
4. Push to GitHub
5. Vercel auto-deploys
6. Test live deployment
7. Gather feedback

## Performance Optimization

- Keep file size reasonable
- Optimize images (if added)
- Minimize CSS
- Use web fonts efficiently
- Test load times

## Accessibility

- Semantic HTML
- Proper heading hierarchy
- Alt text for images
- Color contrast
- Keyboard navigation

## Next Iteration

After completing Iteration 2.1:
1. Review feedback
2. Make improvements
3. Plan Iteration 2.2
4. Add Chapters 5-8
5. Repeat process
