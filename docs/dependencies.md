# Dependencies

## Overview
This document lists all Python and JavaScript dependencies required for the Kenyan Events & Lifestyle Blog website. Dependencies are organized by category and environment.

## Python Dependencies

### Base Dependencies (`requirements/base.txt`)
These dependencies are required for all environments.

```txt
Django>=4.2,<5.0
django-environ>=0.10.0
psycopg2-binary>=2.9.0  # PostgreSQL driver
Pillow>=9.0.0  # Image processing
django-ckeditor>=6.5.0  # Rich text editor for articles
django-taggit>=3.0.0  # Tagging functionality
django-filter>=22.1  # Filtering for API views
djangorestframework>=3.14.0  # API framework
markdown>=3.4.0  # Markdown support
bleach>=5.0.0  # HTML sanitization for comments
django-cors-headers>=3.13.0  # CORS headers for API
django-redis>=5.2.0  # Redis integration for caching
celery>=5.2.0  # Task queue for background processing
```

### Development Dependencies (`requirements/development.txt`)
These dependencies are only needed during development.

```txt
-r base.txt
django-debug-toolbar>=3.2.0  # Debugging tools
django-extensions>=3.1.0  # Useful Django extensions
coverage>=6.5.0  # Code coverage analysis
pytest>=7.2.0  # Testing framework
pytest-django>=4.5.0  # Django integration for pytest
factory-boy>=3.2.0  # Test data generation
black>=22.0.0  # Code formatting
flake8>=5.0.0  # Code linting
pre-commit>=2.20.0  # Git pre-commit hooks
```

### Production Dependencies (`requirements/production.txt`)
These dependencies are needed in production environments.

```txt
-r base.txt
gunicorn>=20.1.0  # WSGI server
whitenoise>=6.2.0  # Static file serving
django-storages>=1.13.0  # Cloud storage integration (S3, etc.)
boto3>=1.24.0  # AWS SDK for S3 integration
sentry-sdk>=1.9.0  # Error tracking and monitoring
newrelic>=7.0.0  # Application performance monitoring
```

### Detailed Dependency Descriptions

#### Core Framework
- **Django**: The main web framework providing the foundation for the blog
- **django-environ**: For managing environment variables and settings

#### Database
- **psycopg2-binary**: PostgreSQL database adapter for Python
- **Pillow**: Python Imaging Library for handling images

#### Content Management
- **django-ckeditor**: Rich text editor for creating articles with formatting
- **django-taggit**: Tagging system for articles
- **markdown**: Markdown parsing for article content
- **bleach**: Sanitization of user-generated content (comments)

#### API and Data Handling
- **django-filter**: Filtering capabilities for API endpoints
- **djangorestframework**: REST API framework for exposing data
- **django-cors-headers**: Handling Cross-Origin Resource Sharing

#### Performance and Caching
- **django-redis**: Redis integration for caching and session storage
- **celery**: Distributed task queue for background processing

#### Development Tools
- **django-debug-toolbar**: Debugging and profiling tools
- **django-extensions**: Additional Django management commands
- **coverage**: Code coverage measurement
- **pytest**: Testing framework with pytest-django integration
- **factory-boy**: Test data generation
- **black**: Code formatting tool
- **flake8**: Code linting tool
- **pre-commit**: Git pre-commit hooks for code quality

#### Production Tools
- **gunicorn**: Production WSGI server
- **whitenoise**: Efficient static file serving
- **django-storages**: Cloud storage integration for media files
- **boto3**: AWS SDK for S3 integration
- **sentry-sdk**: Error tracking and monitoring
- **newrelic**: Application performance monitoring

## JavaScript Dependencies

### Frontend Libraries
These are the core frontend libraries used in the project.

```txt
bootstrap@5.2.3  # CSS framework for responsive design
@popperjs/core@2.11.6  # Required for Bootstrap tooltips and popovers
jquery@3.6.1  # Required for some Bootstrap components
```

### Development Tools
These tools are used during development for building and optimizing assets.

```txt
sass@1.54.0  # CSS preprocessor
autoprefixer@10.4.8  # CSS vendor prefixing
webpack@5.74.0  # Module bundler
webpack-cli@4.10.0  # Webpack command line interface
webpack-dev-server@4.10.0  # Development server with live reloading
```

### Package Management
```txt
npm@8.0.0  # Node package manager (version depends on Node.js installation)
```

### Custom JavaScript Files
The project will include several custom JavaScript files:

1. **dark-mode.js**: Handles dark mode toggle functionality
2. **main.js**: Main application JavaScript
3. **article-gallery.js**: Image gallery functionality
4. **comment-system.js**: Comment submission and management
5. **newsletter.js**: Newsletter subscription handling
6. **search.js**: Search functionality enhancements

### CDN Dependencies
For faster loading and caching, some dependencies will be loaded via CDN:

```html
<!-- Bootstrap CSS -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet">

<!-- Bootstrap JS -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>

<!-- jQuery (if needed for specific components) -->
<script src="https://cdn.jsdelivr.net/npm/jquery@3.6.1/dist/jquery.min.js"></script>
```

## Version Compatibility

### Python Versions
- **Python 3.8+**: The project requires Python 3.8 or higher

### Django Compatibility
- **Django 4.2**: The project is built on Django 4.2 LTS for long-term support

### Database Compatibility
- **PostgreSQL 12+**: Recommended for production
- **SQLite 3.9+**: Suitable for development

### Browser Support
The frontend is designed to support:
- **Chrome**: Latest 2 versions
- **Firefox**: Latest 2 versions
- **Safari**: Latest 2 versions
- **Edge**: Latest 2 versions
- **Mobile Safari**: Latest 2 versions
- **Chrome for Android**: Latest version

## Installation Instructions

### Python Dependencies
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install base dependencies
pip install -r requirements/base.txt

# For development:
pip install -r requirements/development.txt

# For production:
pip install -r requirements/production.txt
```

### JavaScript Dependencies
```bash
# Install Node.js dependencies
npm install

# For development build
npm run build:dev

# For production build
npm run build:prod
```

## Dependency Update Strategy

### Python Dependencies
- Regular security updates using `pip-audit` or similar tools
- Monthly review of dependency updates
- Automated dependency update checks via GitHub Dependabot

### JavaScript Dependencies
- Regular security audits using `npm audit`
- Quarterly review of major version updates
- Testing of updates in staging environment before production deployment

## Security Considerations

### Dependency Security
- All dependencies are regularly checked for known vulnerabilities
- Only maintained and actively developed packages are used
- Minimal dependency set to reduce attack surface
- Regular security scanning as part of CI/CD pipeline

### Version Pinning
- Specific versions are pinned in requirements files to ensure reproducible builds
- Semantic versioning is respected for compatible updates
- Major version updates are carefully tested before implementation