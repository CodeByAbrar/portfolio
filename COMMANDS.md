# Django Portfolio - Command Cheatsheet

## 🚀 Quick Start Commands

### 1. Initial Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Create database tables
python manage.py makemigrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Run server
python manage.py runserver
```

### 2. Running the Project
```bash
# Start development server
python manage.py runserver

# Start on specific port
python manage.py runserver 8080

# Start on all interfaces
python manage.py runserver 0.0.0.0:8000
```

### 3. Database Commands
```bash
# Create migrations for all apps
python manage.py makemigrations

# Create migrations for specific app
python manage.py makemigrations bio

# Apply migrations
python manage.py migrate

# Show all migrations
python manage.py showmigrations

# Rollback migration
python manage.py migrate bio 0001

# Reset database (delete db.sqlite3 and run migrations again)
rm db.sqlite3
python manage.py migrate
```

### 4. Admin Commands
```bash
# Create superuser
python manage.py createsuperuser

# Change user password
python manage.py changepassword username
```

### 5. Shell Commands
```bash
# Open Django shell
python manage.py shell

# Example: Add data via shell
python manage.py shell
>>> from bio.models import Bio
>>> bio = Bio.objects.create(
...     name="John Doe",
...     job_title="Django Developer",
...     description="Passionate about web development"
... )
>>> bio.save()
>>> exit()
```

### 6. Static Files
```bash
# Collect static files (for production)
python manage.py collectstatic
```

### 7. Utility Commands
```bash
# Check for problems
python manage.py check

# Show installed apps
python manage.py showmigrations

# Clear database cache
python manage.py flush
```

## 📊 URL Structure

```
Home Page (Combined View):
http://127.0.0.1:8000/

Admin Panel:
http://127.0.0.1:8000/admin/

Individual Sections:
http://127.0.0.1:8000/bio/
http://127.0.0.1:8000/education/
http://127.0.0.1:8000/skills/
http://127.0.0.1:8000/experience/
http://127.0.0.1:8000/projects/
```

## 🗂️ File Locations

```
Models:        bio/models.py, education/models.py, etc.
Views:         bio/views.py, portfolio/views.py (home view)
URLs:          bio/urls.py, portfolio/urls.py (main)
Templates:     templates/index.html, bio/templates/bio/
Admin:         bio/admin.py
Settings:      portfolio/settings.py
Database:      db.sqlite3
Media Files:   media/profile/, media/projects/
```

## 💡 Viva Demo Flow

1. Show project structure
2. Open settings.py - explain INSTALLED_APPS
3. Show models.py in any app - explain fields
4. Show admin.py - explain list_display
5. Run: python manage.py runserver
6. Open admin panel, add sample data
7. Show homepage with dynamic content
8. Show individual section pages
9. Explain views.py - show ORM queries
10. Show templates - explain template tags

## 🐛 Quick Fixes

### Problem: Module not found
```bash
pip install -r requirements.txt
```

### Problem: No such table
```bash
python manage.py migrate
```

### Problem: Images not showing
- Check MEDIA_URL in settings.py
- Verify media URLs in main urls.py
- Ensure DEBUG=True for development

### Problem: Admin panel shows "Not Found"
```bash
python manage.py createsuperuser
```

## 📝 Sample Data for Testing

### Bio
- Name: John Doe
- Job Title: Full Stack Developer
- Description: Experienced developer with 5+ years in web development

### Education
- Degree: BS Computer Science
- Institute: University of Technology
- Year: 2020-2024

### Skills
- Python (Advanced)
- Django (Expert)
- JavaScript (Intermediate)
- SQL (Advanced)

### Experience
- Role: Backend Developer
- Organization: Tech Company
- Duration: 2023-Present
- Description: Developed REST APIs using Django

### Projects
- Title: E-Commerce Platform
- Description: Full-featured online shopping system
- Technologies: Django, PostgreSQL, Bootstrap
- Link: https://github.com/username/project

## 🎯 Important Notes

1. Always run migrations after model changes
2. Restart server after settings.py changes
3. Use admin panel to add content
4. Check terminal for error messages
5. Use DEBUG=True only in development

## 📚 Django ORM Examples

```python
# Get all objects
Bio.objects.all()

# Get first object
Bio.objects.first()

# Filter objects
Education.objects.filter(year='2024')

# Order objects
Education.objects.all().order_by('-year')

# Create object
skill = Skill(name='Python', level='Expert')
skill.save()

# Update object
bio = Bio.objects.first()
bio.name = 'Jane Doe'
bio.save()

# Delete object
skill.delete()
```

---
Keep this file handy during your viva! 🎓
