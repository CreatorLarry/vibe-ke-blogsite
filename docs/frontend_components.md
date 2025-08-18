# Frontend Components and Features

## Overview
This document describes the frontend components and features for the Kenyan Events & Lifestyle Blog website. The frontend is built with HTML5, CSS3, JavaScript, and Bootstrap 5 for a responsive, mobile-first design.

## Page Templates

### Base Template (`base.html`)
The foundation template that all other pages extend.

**Components:**
- DOCTYPE and meta tags for responsive design
- CSS includes (Bootstrap, custom styles, dark mode)
- Navigation bar with dropdown menus
- Main content block
- Footer with social links and newsletter signup
- JavaScript includes (Bootstrap, custom scripts, dark mode)

### Homepage (`index.html`)
The main landing page showcasing featured content.

**Components:**
- Hero section with featured article
- Category navigation tabs
- Article grid/cards (3-column layout on desktop, 1-column on mobile)
- Search bar
- Newsletter signup form
- Pagination controls

### Article Page (`article_detail.html`)
Individual blog post page.

**Components:**
- Full-width header with featured image
- Article metadata (author, date, category)
- Article content with embedded media
- Social sharing buttons
- Author bio card
- Related posts section
- Comment system
- Newsletter signup CTA

### Category Page (`category_detail.html`)
Category-specific article listings.

**Components:**
- Category header with description and icon
- Article grid/cards filtered by category
- Pagination controls

### Author Profile Page (`author_detail.html`)
Author information and their published articles.

**Components:**
- Author profile header with image and bio
- Article grid/cards by this author
- Pagination controls

### Search Results Page (`search_results.html`)
Articles matching search criteria.

**Components:**
- Search results header with query information
- Article grid/cards matching search
- Pagination controls

## UI Components

### Navigation Bar (`navigation.html`)
Sticky navigation bar with responsive menu.

**Features:**
- Brand/logo area
- Category dropdown menu
- Search icon/form toggle
- Dark mode toggle switch
- Mobile hamburger menu

### Article Cards (`article_card.html`)
Reusable component for article previews.

**Features:**
- Featured image with aspect ratio
- Category badge
- Title with truncation
- Excerpt with read more link
- Author and date information
- View count

### Featured Article Banner (`featured_article.html`)
Prominent display for featured articles.

**Features:**
- Large background image
- Overlay text content
- Category badge
- Title and excerpt
- Author and date information

### Author Bio Card (`author_bio.html`)
Compact author information component.

**Features:**
- Circular profile image
- Name and bio excerpt
- Social links
- Article count

### Comment System (`comments.html`)
Interactive comment display and submission.

**Features:**
- Comment list with nested replies
- Comment submission form
- Moderation notice for pending comments
- Pagination for comments

### Newsletter Signup (`newsletter_signup.html`)
Reusable newsletter subscription component.

**Features:**
- Email input field
- Name fields (optional)
- Preference checkboxes
- Submit button
- Success/error messaging

### Footer (`footer.html`)
Site-wide footer with additional navigation.

**Features:**
- Site description
- Quick links to categories
- Social media icons
- Newsletter signup form
- Copyright information

## Interactive Features

### Dark Mode Toggle
**Implementation:**
- CSS custom properties for color theming
- JavaScript to toggle between light/dark themes
- Local storage to remember user preference
- System preference detection as default

**Components:**
- Toggle switch in navigation bar
- Theme-specific CSS classes
- JavaScript theme manager

### Responsive Design
**Features:**
- Mobile-first approach using Bootstrap 5 grid
- Flexible image handling with `img-fluid` class
- Responsive navigation with collapse behavior
- Adaptive typography scaling
- Touch-friendly interactive elements

### Search Functionality
**Features:**
- Live search suggestions (optional)
- Search results page
- Highlighting of search terms in results
- Filtering by category/author/date

### Media Handling
**Features:**
- Responsive image galleries
- Video embedding (YouTube, Vimeo)
- Lightbox for image viewing
- Lazy loading for improved performance
- Accessible alt text for all images

## JavaScript Components

### Article Gallery
**Features:**
- Thumbnail navigation
- Full-size image display
- Keyboard navigation support
- Touch swipe gestures
- Caption display

### Comment System
**Features:**
- AJAX form submission
- Real-time validation
- Comment preview
- Reply functionality
- Spam protection

### Newsletter Signup
**Features:**
- Form validation
- AJAX submission
- Success/error feedback
- Preference management

### Social Sharing
**Features:**
- Share buttons for major platforms
- Dynamic URL generation
- Share count display (optional)

## CSS Architecture

### Bootstrap Customization
- Custom theme colors for Kenyan aesthetic
- Typography hierarchy for readability
- Spacing system for consistent layouts
- Component overrides for brand styling

### Custom CSS Modules
1. **Base Styles**
   - Typography
   - Color palette
   - Spacing system

2. **Layout Components**
   - Grid modifications
   - Section styling
   - Container variations

3. **UI Components**
   - Card styling
   - Button variations
   - Form elements

4. **Utilities**
   - Helper classes
   - Responsive utilities
   - Dark mode utilities

### Dark Mode Implementation
- CSS custom properties for theme colors
- Separate dark mode stylesheet
- JavaScript theme toggle
- System preference detection

## Responsive Breakpoints

The design follows Bootstrap 5's responsive breakpoints:

- **Extra small (xs)**: <576px (Mobile portrait)
- **Small (sm)**: ≥576px (Mobile landscape)
- **Medium (md)**: ≥768px (Tablet)
- **Large (lg)**: ≥992px (Desktop)
- **Extra large (xl)**: ≥1200px (Large desktop)
- **Extra extra large (xxl)**: ≥1400px (Extra large desktop)

## Accessibility Features

- Semantic HTML structure
- ARIA labels for interactive elements
- Keyboard navigation support
- Sufficient color contrast
- Focus indicators for interactive elements
- Alt text for all images
- Skip navigation link

## Performance Considerations

- Minified CSS and JavaScript
- Image optimization and compression
- Lazy loading for images and videos
- Efficient CSS selectors
- Critical CSS for above-the-fold content
- Caching strategies