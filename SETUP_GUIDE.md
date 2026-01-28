# 🚀 Complete Setup Guide - Django Portfolio Project

## ⚡ Quick Start (5 Minutes)

### Step 1: Navigate to Project Directory
```bash
cd portfolio
```

### Step 2: Install Django & Pillow
```bash
pip install django pillow
```

### Step 3: Create Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 4: Create Admin Account
```bash
python manage.py createsuperuser
```
Enter:
- Username: admin
- Email: admin@example.com
- Password: admin123 (or your choice)

### Step 5: Start Server
```bash
python manage.py runserver
```

### Step 6: Open in Browser
- Homepage: http://127.0.0.1:8000/
- Admin Panel: http://127.0.0.1:8000/admin/

---

## 📝 Detailed Setup Instructions

### Prerequisites Check
Before starting, make sure you have:
- ✅ Python 3.8 or higher installed
- ✅ pip (Python package manager)
- ✅ Text editor or IDE (VS Code, PyCharm, etc.)

To check Python version:
```bash
python --version
```

### Installation Process

#### 1. Install Required Packages
```bash
pip install -r requirements.txt
```

This installs:
- Django 4.2+ (Web framework)
- Pillow 10.0+ (Image handling)

#### 2. Initialize Database

**Make migrations for all apps:**
```bash
python manage.py makemigrations bio
python manage.py makemigrations education
python manage.py makemigrations skills
python manage.py makemigrations experience
python manage.py makemigrations projects
```

**Apply migrations:**
```bash
python manage.py migrate
```

This creates the SQLite database (`db.sqlite3`) with all necessary tables.

#### 3. Create Superuser Account
```bash
python manage.py createsuperuser
```

Follow the prompts:
```
Username: admin
Email address: your@email.com
Password: ********
Password (again): ********
```

**Note**: Password won't be visible while typing (security feature).

#### 4. Run Development Server
```bash
python manage.py runserver
```

You should see:
```
Django version X.X, using settings 'portfolio.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

---

## 🎯 Adding Content

### Using Admin Panel

1. **Open Admin Panel**
   ```
   http://127.0.0.1:8000/admin/
   ```

2. **Login** with your superuser credentials

3. **Add Bio Information**
   - Click on "Bio" under "BIO" section
   - Click "Add Bio" button
   - Fill in:
     * Name: Your Full Name
     * Job Title: Your Role/Title
     * Profile Image: Upload your photo
     * Description: Brief about yourself
   - Click "Save"

4. **Add Education Entries**
   - Click on "Education Entries" under "EDUCATION"
   - Click "Add Education"
   - Fill in degree, institute, year, description
   - Click "Save"
   - Add more entries as needed

5. **Add Skills**
   - Click on "Skills" under "SKILLS"
   - Click "Add Skill"
   - Enter skill name (e.g., Python, Django)
   - Select proficiency level
   - Click "Save"
   - Add multiple skills

6. **Add Experience**
   - Click on "Experience Entries" under "EXPERIENCE"
   - Click "Add Experience"
   - Fill in role, organization, duration, description
   - Click "Save"
   - Add all work experiences

7. **Add Projects**
   - Click on "Projects" under "PROJECTS"
   - Click "Add Project"
   - Fill in:
     * Title: Project name
     * Description: Project details
     * Image: Upload screenshot
     * Project Link: GitHub or live URL
     * Technologies: Tech stack used
   - Click "Save"
   - Add all your projects

### View Your Portfolio
After adding content, visit:
```
http://127.0.0.1:8000/
```

---

## 🏗️ Project Architecture Explanation

### Apps Structure
```
portfolio/              # Main project
├── bio/               # Personal information
├── education/         # Academic background
├── skills/            # Technical & soft skills
├── experience/        # Work history
└── projects/          # Portfolio projects
```

### MVT Flow
```
User Request
    ↓
URLs (urls.py) → Routes to correct view
    ↓
View (views.py) → Fetches data from database using ORM
    ↓
Model (models.py) → Database structure
    ↓
View → Passes data to template
    ↓
Template (HTML) → Renders final HTML
    ↓
Response to User
```

### File Purposes

**models.py**: Define database structure
```python
class Bio(models.Model):
    name = models.CharField(max_length=100)
    # ... more fields
```

**views.py**: Handle requests and fetch data
```python
def home(request):
    bio = Bio.objects.first()
    return render(request, 'index.html', {'bio': bio})
```

**urls.py**: Map URLs to views
```python
urlpatterns = [
    path('', views.home, name='home'),
]
```

**admin.py**: Configure admin interface
```python
@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    list_display = ('name', 'job_title')
```

**templates/**: HTML files with Django template language
```html
<h1>{{ bio.name }}</h1>
<p>{{ bio.description }}</p>
```

---

## 🎓 Viva Preparation

### Key Points to Remember

1. **MVT Architecture**
   - Model: Database layer (models.py)
   - View: Business logic (views.py)
   - Template: Presentation layer (HTML)

2. **Django ORM**
   - Object-Relational Mapping
   - Python code instead of SQL
   - Example: `Bio.objects.all()`

3. **Admin Panel**
   - Built-in Django feature
   - Automatically generated
   - Configured in admin.py

4. **URL Routing**
   - URLconf in urls.py
   - Pattern matching
   - Named URLs for reverse lookup

5. **Template Inheritance**
   - base.html as parent
   - Child templates extend base
   - {% block %} tags for content sections

### Demo Flow for Viva

1. **Show Project Structure** (2 min)
   - Explain folder organization
   - Point out apps and their purposes

2. **Explain Settings** (2 min)
   - Open settings.py
   - Show INSTALLED_APPS
   - Explain MEDIA_URL and MEDIA_ROOT

3. **Show Models** (3 min)
   - Open any models.py
   - Explain field types
   - Show relationships

4. **Demonstrate Admin** (3 min)
   - Open admin panel
   - Add sample data
   - Show list_display feature

5. **Show Views** (3 min)
   - Open views.py
   - Explain ORM queries
   - Show context data passing

6. **Show Templates** (3 min)
   - Open index.html
   - Explain template tags
   - Show for loops and if conditions

7. **Run Project** (2 min)
   - Start server
   - Navigate through pages
   - Show dynamic content

### Common Viva Questions & Answers

**Q1: What is Django?**
A: Django is a high-level Python web framework that enables rapid development of secure and maintainable websites. It follows the MVT pattern.

**Q2: What is MVT?**
A: MVT stands for Model-View-Template:
- Model: Database structure
- View: Business logic
- Template: User interface

**Q3: What is Django ORM?**
A: Object-Relational Mapping allows you to interact with databases using Python code instead of SQL. Example: `Bio.objects.all()` instead of `SELECT * FROM bio`.

**Q4: Why separate apps?**
A: For modularity, reusability, easier maintenance, and better organization. Each app handles a specific functionality.

**Q5: How does Django handle media files?**
A: Through MEDIA_URL and MEDIA_ROOT settings. Files are uploaded to MEDIA_ROOT and served via MEDIA_URL in development.

**Q6: What are migrations?**
A: Migrations are Django's way of propagating changes you make to models into the database schema. They're version control for database structure.

**Q7: How do templates work?**
A: Templates receive context data from views and render HTML using Django Template Language (DTL) with tags like {{ variable }} and {% for %}.

**Q8: What is the purpose of admin.py?**
A: To customize how models appear in Django's admin interface. We can configure list_display, search_fields, filters, etc.

---

## 🐛 Troubleshooting

### Problem: "No module named 'django'"
**Solution:**
```bash
pip install django
```

### Problem: "No such table"
**Solution:**
```bash
python manage.py migrate
```

### Problem: Images not displaying
**Solution:**
1. Check MEDIA_URL in settings.py
2. Verify media URLs in main urls.py:
   ```python
   if settings.DEBUG:
       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```
3. Ensure DEBUG=True in settings.py

### Problem: Admin panel shows "Permission denied"
**Solution:**
Create superuser account:
```bash
python manage.py createsuperuser
```

### Problem: Port already in use
**Solution:**
Use a different port:
```bash
python manage.py runserver 8080
```

### Problem: Changes not reflecting
**Solution:**
1. Restart development server (Ctrl+C, then runserver again)
2. Clear browser cache (Ctrl+Shift+R)
3. Check if you're editing the correct file

---

## 📚 Additional Resources

### Django Documentation
- Official Docs: https://docs.djangoproject.com/
- Tutorial: https://docs.djangoproject.com/en/stable/intro/tutorial01/

### Learning Materials
- Django Girls Tutorial
- Mozilla Django Tutorial
- Real Python Django Tutorials

### Useful Commands Reference
See `COMMANDS.md` for comprehensive command list.

---

## ✅ Pre-Viva Checklist

Before your viva, make sure:
- [ ] Project runs without errors
- [ ] Database has sample data
- [ ] All pages are accessible
- [ ] Admin panel works
- [ ] You can explain each file's purpose
- [ ] You understand MVT architecture
- [ ] You can demonstrate ORM queries
- [ ] You know how migrations work
- [ ] You can explain URL routing
- [ ] You understand template inheritance

---

## 🎉 Success!

Your Django portfolio is ready! You now have:
- ✅ Complete working Django project
- ✅ Five separate functional apps
- ✅ Fully configured admin panel
- ✅ Dynamic content from database
- ✅ Professional responsive design
- ✅ Proper MVT architecture
- ✅ Media handling for images

**Good luck with your viva! 🚀**

---

## 📞 Need Help?

If you encounter issues:
1. Check error messages in terminal
2. Read the error traceback
3. Verify all files are in correct locations
4. Ensure all migrations are applied
5. Check Django documentation

Remember: Django has excellent error pages in DEBUG mode that help identify problems!
