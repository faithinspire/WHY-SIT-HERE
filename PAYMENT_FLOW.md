# Payment Flow & Book Access

## How Users Access the Book After Payment

### Step 1: Landing Page
- User visits: https://why-sit-here-and-die.vercel.app
- Sees book description, features, and pricing (₦5,000)
- Two payment options: PayPal or Card Payment

### Step 2: Payment Processing
After successful payment, payment processor redirects to:
```
https://why-sit-here-and-die.vercel.app/online-reader.html?access=March31
```

### Step 3: Automatic Access
- URL parameter `?access=March31` is detected
- System automatically:
  - Sets `localStorage.bookAccess = 'true'`
  - Removes access code from URL (for security)
  - Loads the online reader
  - Displays the complete manuscript

### Step 4: Read Book
- User can read all 18 chapters online
- Download as PDF using browser print function
- Logout when finished

## Implementation Details

### Landing Page (index.html)
- Book description and features
- Pricing display
- Payment method buttons
- Direct access link for existing customers

### Online Reader (online-reader.html)
- Password login (fallback method)
- URL parameter auto-login (post-payment)
- Session persistence with localStorage
- Complete manuscript display
- PDF export capability

### URL Parameter Method
```javascript
// After payment, redirect to:
online-reader.html?access=March31

// System automatically:
1. Detects access parameter
2. Sets localStorage.bookAccess = 'true'
3. Removes parameter from URL
4. Loads reader with content
```

### Fallback: Manual Password Entry
If user loses session or visits directly:
- Can enter password "March31" manually
- Gets same access to complete book

## Payment Integration (To Be Configured)

### PayPal Integration
- Redirect URL: `online-reader.html?access=March31`
- Amount: ₦5,000
- Currency: NGN

### Stripe Integration
- Redirect URL: `online-reader.html?access=March31`
- Amount: 500000 (in kobo)
- Currency: NGN

## Security Notes

1. Access code is removed from URL after use
2. Session stored in localStorage (browser-specific)
3. Password "March31" is the fallback
4. No sensitive data in URL after initial redirect

## User Experience Flow

```
Landing Page (index.html)
    ↓
[Choose Payment Method]
    ↓
[Process Payment]
    ↓
Redirect: online-reader.html?access=March31
    ↓
Auto-login & Load Book
    ↓
Read Complete Manuscript
    ↓
[Download PDF or Logout]
```

## Testing

To test the flow:
1. Visit: `https://why-sit-here-and-die.vercel.app/online-reader.html?access=March31`
2. Should automatically load the reader with book content
3. URL should change to just `online-reader.html` (parameter removed)
4. Session should persist on page refresh
