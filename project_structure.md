# Blog Website Project Structure

## Root Directory Structure
```
blog-website/
├── blog/                     # Main Django project directory
│   ├── __init__.py
│   ├── settings/             # Settings package for different environments
│   │   ├── __init__.py
│   │   ├── base.py           # Base settings
│   │   ├── development.py    # Development-specific settings
│   │   └── production.py     # Production-specific settings
│   ├── urls.py               # Main URL configuration
│   ├── wsgi.py               # WSGI deployment configuration
│   └── asgi.py               # ASGI deployment configuration
├── articles/                 # Django app for articles management
│   ├── migrations/           # Database migrations
│   ├── templates/            # App-specific templates
│   ├── static/               # App-specific static files
│   ├── __init__.py
│   ├── admin.py              # Admin interface configuration
│   ├── apps.py               # App configuration
│   ├── models.py             # Data models
│   ├── views.py              # View functions
│   ├── urls.py               # App URL configuration
│   ├── forms.py              # Form definitions
│   └── tests.py              # Unit tests
├── authors/                  # Django app for author profiles
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
├── categories/               # Django app for article categories
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
├── comments/                 # Django app for comment system
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
├── newsletter/               # Django app for newsletter subscription
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
├── templates/                # Base templates directory
│   ├── base.html             # Base template with common structure
│   ├── includes/             # Reusable template components
│   │   ├── header.html
│   │   ├── footer.html
│   │   ├── navigation.html
│   │   └── sidebar.html
│   └── partials/             # Small template snippets
├── static/                   # Global static files
│   ├── css/
│   │   ├── bootstrap/        # Bootstrap CSS files
│   │   ├── custom/           # Custom CSS files
│   │   └── dark-mode.css     # Dark mode styles
│   ├── js/
│   │   ├── bootstrap/        # Bootstrap JS files
│   │   ├── custom/           # Custom JavaScript files
│   │   └── dark-mode.js      # Dark mode toggle functionality
│   ├── images/               # Global images
│   └── fonts/                # Custom fonts
├── media/                    # User-uploaded media files (in .gitignore)
├── docs/                     # Project documentation
│   ├── architecture.md       # Architecture decisions
│   ├── database_schema.md    # Database schema documentation
│   └── api_documentation.md  # API documentation
├── requirements/             # Python dependency files
│   ├── base.txt              # Common dependencies
│   ├── development.txt       # Development dependencies
│   └── production.txt       # Production dependencies
├── .env                      # Environment variables (in .gitignore)
├── .gitignore                # Git ignore file
├── manage.py                 # Django management script
├── README.md                 # Project overview and setup instructions
└── Dockerfile               # Docker configuration (optional)
```

## Detailed Explanation

### Django Project Structure (`blog/`)
- Contains the main Django project configuration
- Settings are organized by environment for better security and flexibility
- Separates development and production configurations

### Articles App (`articles/`)
- Core functionality for managing blog posts
- Handles article creation, editing, and display
- Includes support for featured articles and related posts

### Authors App (`authors/`)
- Manages author profiles and their associated articles
- Handles author bio information and article listings

### Categories App (`categories/`)
- Implements the categorization system (Events, Food & Restaurants, etc.)
- Provides category-based navigation and filtering

### Comments App (`comments/`)
- Implements the moderated comment system
- Handles comment submission, approval, and display

### Newsletter App (`newsletter/`)
- Manages email subscriptions and newsletter functionality
- Handles subscriber data and preferences

### Templates Directory (`templates/`)
- Contains base templates and reusable components
- Organized for maintainability and reuse

### Static Files (`static/`)
- Organized by file type for easy management
- Separates third-party libraries from custom code
- Includes dark mode specific assets

### Media Files (`media/`)
- Stores user-uploaded content (images, videos)
- Excluded from version control for security

### Documentation (`docs/`)
- Centralized location for project documentation
- Includes architecture and database schema documentation

### Requirements (`requirements/`)
- Organized dependency management for different environments
- Separates base, development, and production dependencies