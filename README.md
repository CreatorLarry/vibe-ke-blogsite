# Kenyan Events & Lifestyle Blog

A modern Django blog website focused on Kenyan events, restaurants, and new spots with Bootstrap 5 frontend.

## Features

- Beautiful, responsive blog homepage with featured articles carousel
- Individual article pages with support for embedded images
- Categories: Events, Food & Restaurants, New Spots, Lifestyle
- Author profiles with bio and list of their published articles
- Admin dashboard (Django Admin) for posting, editing, and managing articles
- Comment system for readers (moderated)
- SEO-friendly structure and meta tags
- Related posts section on each article page
- Newsletter subscription (email capture)
- Mobile-first responsive design with Bootstrap 5
- Dark mode toggle

## Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Backend**: Python Django
- **Database**: SQLite (local dev), PostgreSQL (production)
- **Media storage**: Local for dev, scalable to S3 or similar in production

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment tool (venv or virtualenv)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd blog-website
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (admin) account**
   ```bash
   python manage.py createsuperuser
   ```

7. **Load sample data (optional)**
   ```bash
   python manage.py loaddata sample_data.json
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   - Website: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

### Project Structure

```
blog-website/
├── blog/                 # Main Django project settings
├── articles/             # Articles management
├── authors/              # Author profiles
├── categories/           # Article categories
├── comments/             # Comment system
├── newsletter/           # Newsletter subscription
├── templates/            # HTML templates
├── static/               # CSS, JavaScript, images
├── media/                # User-uploaded content
├── requirements.txt      # Python dependencies
└── manage.py             # Django management script
```

### Admin Features

As an admin, you can:
- Create, edit, and publish articles
- Manage authors and their profiles
- Organize content with categories
- Moderate comments
- Manage newsletter subscribers
- Customize site settings

### Customization

To customize the blog for your needs:

1. **Update site information**: Modify templates/base.html to change site name, description, etc.
2. **Add new categories**: Use the Django admin panel to add new categories
3. **Modify styling**: Update CSS files in static/css/custom/
4. **Add new features**: Extend Django apps or create new ones

### Deployment

For production deployment:

1. **Set environment variables**:
   - SECRET_KEY
   - DEBUG (set to False)
   - ALLOWED_HOSTS
   - DATABASE_URL (for PostgreSQL)

2. **Configure production settings**:
   Update blog/settings/production.py with your production database settings

3. **Collect static files**:
   ```bash
   python manage.py collectstatic
   ```

4. **Use a production web server**:
   - Gunicorn with Nginx
   - Apache with mod_wsgi
   - Other WSGI servers

### Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

### License

This project is licensed under the MIT License - see the LICENSE file for details.

### Support

For support, please open an issue on the repository or contact the maintainers.