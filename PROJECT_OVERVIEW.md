# 📊 Django Portfolio Project - Complete Overview

## 🎯 Project Details
**Name**: Dynamic Portfolio Website
**Framework**: Django 4.2+
**Architecture**: MVT (Model-View-Template)
**Database**: SQLite3
**Purpose**: University Term Project

---

## 📁 Complete File Structure

```
portfolio/
│
├── 📂 portfolio/                        # MAIN PROJECT FOLDER
│   ├── __init__.py                     # Package initializer
│   ├── settings.py                     # ⚙️ Project settings & configuration
│   ├── urls.py                         # 🔗 Main URL routing
│   ├── views.py                        # 👁️ Combined home view (fetches all data)
│   ├── wsgi.py                         # Web server gateway
│   └── asgi.py                         # Async server gateway
│
├── 📂 bio/                              # BIO APP
│   ├── 📂 migrations/                  
│   │   └── __init__.py
│   ├── 📂 templates/bio/
│   │   └── bio_detail.html             # Bio template
│   ├── __init__.py
│   ├── admin.py                        # ⚙️ Bio admin configuration
│   ├── apps.py                         # App configuration
│   ├── models.py                       # 📊 Bio model (name, job_title, image, description)
│   ├── urls.py                         # 🔗 Bio URL patterns
│   └── views.py                        # 👁️ Bio views
│
├── 📂 education/                        # EDUCATION APP
│   ├── 📂 migrations/
│   │   └── __init__.py
│   ├── 📂 templates/education/
│   │   └── education_list.html         # Education template
│   ├── __init__.py
│   ├── admin.py                        # ⚙️ Education admin
│   ├── apps.py
│   ├── models.py                       # 📊 Education model (degree, institute, year)
│   ├── urls.py                         # 🔗 Education URLs
│   └── views.py                        # 👁️ Education views
│
├── 📂 skills/                           # SKILLS APP
│   ├── 📂 migrations/
│   │   └── __init__.py
│   ├── 📂 templates/skills/
│   │   └── skills_list.html            # Skills template
│   ├── __init__.py
│   ├── admin.py                        # ⚙️ Skills admin
│   ├── apps.py
│   ├── models.py                       # 📊 Skill model (name, level)
│   ├── urls.py                         # 🔗 Skills URLs
│   └── views.py                        # 👁️ Skills views
│
├── 📂 experience/                       # EXPERIENCE APP
│   ├── 📂 migrations/
│   │   └── __init__.py
│   ├── 📂 templates/experience/
│   │   └── experience_list.html        # Experience template
│   ├── __init__.py
│   ├── admin.py                        # ⚙️ Experience admin
│   ├── apps.py
│   ├── models.py                       # 📊 Experience model (role, org, description)
│   ├── urls.py                         # 🔗 Experience URLs
│   └── views.py                        # 👁️ Experience views
│
├── 📂 projects/                         # PROJECTS APP
│   ├── 📂 migrations/
│   │   └── __init__.py
│   ├── 📂 templates/projects/
│   │   └── projects_list.html          # Projects template
│   ├── __init__.py
│   ├── admin.py                        # ⚙️ Projects admin
│   ├── apps.py
│   ├── models.py                       # 📊 Project model (title, description, image, link)
│   ├── urls.py                         # 🔗 Projects URLs
│   └── views.py                        # 👁️ Projects views
│
├── 📂 templates/                        # GLOBAL TEMPLATES
│   ├── base.html                       # 📄 Base template (inherited by all)
│   └── index.html                      # 📄 Home page (shows all sections)
│
├── 📂 media/                            # MEDIA FILES (user uploads)
│   ├── profile/                        # Profile pictures
│   └── projects/                       # Project images
│
├── 📂 static/                           # STATIC FILES (CSS, JS, images)
│
├── manage.py                            # 🔧 Django management script
├── requirements.txt                     # 📦 Python dependencies
├── README.md                            # 📖 Complete documentation
├── SETUP_GUIDE.md                       # 🚀 Step-by-step setup instructions
├── COMMANDS.md                          # 💻 Command cheatsheet
└── .gitignore                           # Git ignore file
```

---

## 🏗️ MVT Architecture Flow

```
┌─────────────────────────────────────────────────────────────┐
│                         USER REQUEST                         │
│                    (http://localhost:8000/)                  │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ↓
┌─────────────────────────────────────────────────────────────┐
│                    URLs (portfolio/urls.py)                  │
│              Maps URL to corresponding view                  │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ↓
┌─────────────────────────────────────────────────────────────┐
│                 VIEW (portfolio/views.py)                    │
│              def home(request):                              │
│                  bio = Bio.objects.first()                   │
│                  educations = Education.objects.all()        │
│                  ... (fetches data using ORM)                │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ↓
┌─────────────────────────────────────────────────────────────┐
│                   MODELS (*/models.py)                       │
│              Database structure definitions                  │
│              - Bio model                                     │
│              - Education model                               │
│              - Skills model                                  │
│              - Experience model                              │
│              - Projects model                                │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ↓
┌─────────────────────────────────────────────────────────────┐
│                    DATABASE (SQLite3)                        │
│              Stores all portfolio data                       │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ↓ (Data returned to view)
┌─────────────────────────────────────────────────────────────┐
│               VIEW passes data to TEMPLATE                   │
│              context = {'bio': bio, ...}                     │
│              return render(request, 'index.html', context)   │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ↓
┌─────────────────────────────────────────────────────────────┐
│                TEMPLATE (templates/index.html)               │
│              Renders HTML with data                          │
│              {% for education in educations %}               │
│                  <h3>{{ education.degree }}</h3>             │
│              {% endfor %}                                    │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ↓
┌─────────────────────────────────────────────────────────────┐
│                      HTML RESPONSE                           │
│              Sent back to user's browser                     │
└─────────────────────────────────────────────────────────────┘
```

---

## 📊 Database Models

### 1. Bio Model
```python
class Bio(models.Model):
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile/')
    description = models.TextField()
```
**Purpose**: Store personal information
**Instances**: 1 (single bio entry)

### 2. Education Model
```python
class Education(models.Model):
    degree = models.CharField(max_length=200)
    institute = models.CharField(max_length=200)
    year = models.CharField(max_length=50)
    description = models.TextField()
```
**Purpose**: Store academic background
**Instances**: Multiple (all degrees)

### 3. Skill Model
```python
class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=20)  # Choices: Beginner/Intermediate/Advanced/Expert
    description = models.TextField()
```
**Purpose**: Store technical and soft skills
**Instances**: Multiple (all skills)

### 4. Experience Model
```python
class Experience(models.Model):
    role = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.CharField(max_length=100)
```
**Purpose**: Store work experience
**Instances**: Multiple (all jobs)

### 5. Project Model
```python
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    project_link = models.URLField()
    technologies = models.CharField(max_length=300)
```
**Purpose**: Store portfolio projects
**Instances**: Multiple (all projects)

---

## 🔗 URL Routing Structure

```
http://127.0.0.1:8000/                  → home view → index.html
http://127.0.0.1:8000/admin/            → Django admin panel
http://127.0.0.1:8000/bio/              → bio_detail view → bio_detail.html
http://127.0.0.1:8000/education/        → education_list view → education_list.html
http://127.0.0.1:8000/skills/           → skills_list view → skills_list.html
http://127.0.0.1:8000/experience/       → experience_list view → experience_list.html
http://127.0.0.1:8000/projects/         → projects_list view → projects_list.html
http://127.0.0.1:8000/media/            → Serves uploaded images
```

---

## 🎨 Template Structure

```
base.html (Parent Template)
│
├── Header (Name, Title)
├── Navigation Menu
├── {% block content %} ← Child templates insert content here
└── Footer
```

**Child Templates:**
- `index.html` - Extends base.html, shows all sections
- `bio/bio_detail.html` - Shows bio only
- `education/education_list.html` - Shows education only
- `skills/skills_list.html` - Shows skills only
- `experience/experience_list.html` - Shows experience only
- `projects/projects_list.html` - Shows projects only

---

## 🔧 Admin Panel Configuration

Each app has admin.py with:
```python
@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2', 'field3')  # Columns to show
    search_fields = ('field1',)                     # Enable search
    list_filter = ('field2',)                       # Add filters
    ordering = ('-created_at',)                     # Default ordering
```

**Access**: http://127.0.0.1:8000/admin/

---

## 📦 Dependencies

**requirements.txt:**
```
Django>=4.2,<5.0    # Web framework
Pillow>=10.0.0      # Image processing
```

---

## 🚀 Quick Start Commands

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Create database
python manage.py makemigrations
python manage.py migrate

# 3. Create admin user
python manage.py createsuperuser

# 4. Run server
python manage.py runserver

# 5. Open browser
http://127.0.0.1:8000/
```

---

## ✅ Key Features Implemented

### ✓ MVT Architecture
- Models defined in each app
- Views fetch data using ORM
- Templates render dynamic content

### ✓ Separate Apps
- bio - Personal info
- education - Academic background
- skills - Technical skills
- experience - Work history
- projects - Portfolio projects

### ✓ Django ORM
```python
Bio.objects.first()              # Get single object
Education.objects.all()          # Get all objects
Skill.objects.filter(level='Expert')  # Filter objects
```

### ✓ Admin Panel
- All models registered
- list_display configured
- Search and filter enabled

### ✓ Media Handling
- Profile images in media/profile/
- Project images in media/projects/
- Served correctly in development

### ✓ Template Inheritance
- base.html as parent
- All pages extend base
- Consistent navigation

### ✓ Dynamic Content
- Zero hardcoded content
- All data from database
- Easy to update via admin

---

## 🎓 Viva Key Points

### 1. Project Structure
- Explain each folder's purpose
- Show separation of concerns
- Demonstrate modularity

### 2. MVT Flow
- Request → URL → View → Model → Template → Response
- Show example with actual code

### 3. Django ORM
- Show ORM queries in views.py
- Explain object-oriented approach
- Compare with raw SQL

### 4. Admin Panel
- Demonstrate adding content
- Show list_display feature
- Explain automatic generation

### 5. Templates
- Show template inheritance
- Explain DTL syntax
- Demonstrate loops and conditionals

---

## 📈 Project Statistics

- **Total Apps**: 5 (bio, education, skills, experience, projects)
- **Total Models**: 5 (one per app)
- **Total Views**: 6 (home + 5 app views)
- **Total Templates**: 6 (base + index + 5 app templates)
- **Total URL Patterns**: 7+ (home + admin + 5 apps)
- **Lines of Code**: ~1000+
- **Database Tables**: 5 main tables + Django's built-in tables

---

## 🎯 Achievement Summary

✅ Complete Django project with proper structure
✅ Five separate functional apps
✅ MVT architecture properly implemented
✅ Database-driven dynamic content
✅ Fully functional admin panel
✅ Responsive professional design
✅ Media file handling configured
✅ Template inheritance implemented
✅ Django ORM used throughout
✅ Ready for viva demonstration

---

## 📚 Documentation Files

1. **README.md** - Complete project documentation
2. **SETUP_GUIDE.md** - Step-by-step setup instructions
3. **COMMANDS.md** - Command reference and cheatsheet
4. **PROJECT_OVERVIEW.md** - This file (visual overview)

---

**🎉 Your Django Portfolio Project is Complete and Ready!**

**Total Development Time**: Professional-grade project
**Complexity Level**: University term project standard
**Viva Readiness**: 100% ✓

Good luck with your presentation! 🚀
