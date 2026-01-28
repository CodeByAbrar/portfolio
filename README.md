# Dynamic Portfolio Website - Django Project

## 🎯 Project Overview
A fully dynamic personal portfolio website built with Django, following the MVT (Model-View-Template) architecture. All content is fetched from the database with no hardcoded HTML content.

## 📋 Project Requirements Met

### ✅ Project Structure
- **Project Name**: `portfolio`
- **Separate Apps**: bio, education, skills, experience, projects
- **MVT Architecture**: Proper separation of Models, Views, and Templates
- **Database-Driven**: All content is dynamic and fetched from SQLite database

### ✅ Features Implemented
1. **Bio Section**: Personal information with profile image
2. **Education Section**: Academic background
3. **Skills Section**: Technical and soft skills with proficiency levels
4. **Experience Section**: Work history
5. **Projects Section**: Portfolio projects with images and links
6. **Admin Panel**: Fully configured for content management
7. **Media Handling**: Profile pictures and project images
8. **Responsive Design**: Clean, professional styling

## 📁 Project Structure

```
portfolio/
│
├── portfolio/                  # Main project directory
│   ├── __init__.py
│   ├── settings.py            # Project settings
│   ├── urls.py                # Main URL configuration
│   ├── views.py               # Combined home view
│   ├── wsgi.py
│   └── asgi.py
│
├── bio/                       # Bio app
│   ├── migrations/
│   ├── templates/bio/
│   ├── __init__.py
│   ├── admin.py              # Bio admin configuration
│   ├── apps.py
│   ├── models.py             # Bio model
│   ├── urls.py
│   └── views.py              # Bio views
│
├── education/                 # Education app
│   ├── migrations/
│   ├── templates/education/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── skills/                    # Skills app
│   ├── migrations/
│   ├── templates/skills/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── experience/                # Experience app
│   ├── migrations/
│   ├── templates/experience/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── projects/                  # Projects app
│   ├── migrations/
│   ├── templates/projects/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── templates/                 # Global templates
│   ├── base.html             # Base template
│   └── index.html            # Home page (combined view)
│
├── media/                     # Media files directory
│   ├── profile/              # Profile images
│   └── projects/             # Project images
│
├── static/                    # Static files directory
│
├── manage.py                  # Django management script
└── requirements.txt           # Python dependencies
```

## 🔧 Installation & Setup

### Step 1: Prerequisites
Make sure you have Python installed (Python 3.8 or higher recommended).

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

**Required packages:**
- Django (4.2+)
- Pillow (for image handling)

### Step 3: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

This will create all necessary database tables for:
- Bio
- Education
- Skills
- Experience
- Projects

### Step 4: Create Superuser
```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### Step 5: Run Development Server
```bash
python manage.py runserver
```

The website will be available at: **http://127.0.0.1:8000/**

### Step 6: Access Admin Panel
Go to: **http://127.0.0.1:8000/admin/**

Login with your superuser credentials and start adding content!

## 📊 Database Models

### Bio Model
- `name` (CharField) - Your full name
- `job_title` (CharField) - Your current job title
- `profile_image` (ImageField) - Profile picture
- `description` (TextField) - About yourself

### Education Model
- `degree` (CharField) - Degree name
- `institute` (CharField) - Institution name
- `year` (CharField) - Year or duration
- `description` (TextField) - Additional details

### Skill Model
- `name` (CharField) - Skill name
- `level` (CharField) - Proficiency level (Beginner/Intermediate/Advanced/Expert)
- `description` (TextField) - Additional details

### Experience Model
- `role` (CharField) - Job title
- `organization` (CharField) - Company name
- `description` (TextField) - Job responsibilities
- `duration` (CharField) - Work duration

### Project Model
- `title` (CharField) - Project name
- `description` (TextField) - Project details
- `image` (ImageField) - Project screenshot
- `project_link` (URLField) - Live project or repo link
- `technologies` (CharField) - Technologies used

## 🎨 Features

### Admin Panel Features
- All models registered with `list_display`
- Search functionality
- Filtering options
- User-friendly interface

### Template Features
- **Base Template**: Reusable layout with navigation
- **Home Page**: Combined view showing all sections
- **Individual Pages**: Separate pages for each section
- **Django Template Language**: Proper use of loops, conditionals, and variables
- **Responsive Design**: Works on all devices

### URL Configuration
- Clean URL patterns
- Named URLs for easy navigation
- Proper URL namespacing for each app

## 🚀 How to Use

### Adding Content via Admin Panel

1. **Add Bio Information**
   - Go to Admin Panel → Bio
   - Click "Add Bio"
   - Fill in your details and upload profile image
   - Save

2. **Add Education**
   - Go to Admin Panel → Education
   - Click "Add Education"
   - Add your degrees and institutions
   - Save

3. **Add Skills**
   - Go to Admin Panel → Skills
   - Click "Add Skill"
   - Enter skill name and select proficiency level
   - Save

4. **Add Experience**
   - Go to Admin Panel → Experience
   - Click "Add Experience"
   - Fill in job details
   - Save

5. **Add Projects**
   - Go to Admin Panel → Projects
   - Click "Add Project"
   - Upload project image and add details
   - Save

### Viewing the Portfolio
- **Home Page**: http://127.0.0.1:8000/ (Shows all sections combined)
- **Bio Page**: http://127.0.0.1:8000/bio/
- **Education Page**: http://127.0.0.1:8000/education/
- **Skills Page**: http://127.0.0.1:8000/skills/
- **Experience Page**: http://127.0.0.1:8000/experience/
- **Projects Page**: http://127.0.0.1:8000/projects/

## 📝 Technical Implementation

### MVT Architecture
1. **Models**: Define data structure in each app's `models.py`
2. **Views**: Fetch data from models and pass to templates in `views.py`
3. **Templates**: Display data using Django template language

### Django ORM Usage
```python
# Example from portfolio/views.py
bio = Bio.objects.first()
educations = Education.objects.all().order_by('-year')
skills = Skill.objects.all()
experiences = Experience.objects.all()
projects = Project.objects.all()
```

### Media Configuration
```python
# In settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

## 🎓 Viva Preparation Tips

### Key Concepts to Explain
1. **MVT Architecture**: Explain how Django separates concerns
2. **ORM**: Demonstrate database queries without SQL
3. **Admin Panel**: Show how Django provides built-in admin interface
4. **Template Inheritance**: Explain base.html and extending templates
5. **URL Routing**: Demonstrate URL patterns and namespacing
6. **Media Handling**: Explain how images are uploaded and served

### Common Viva Questions
1. **Q: What is MVT?**
   - A: Model-View-Template - Django's architectural pattern

2. **Q: How is data fetched from database?**
   - A: Using Django ORM (e.g., `Model.objects.all()`)

3. **Q: Why separate apps?**
   - A: For modularity, reusability, and better organization

4. **Q: How are templates rendered?**
   - A: Using `render()` function with context data

5. **Q: What is the purpose of migrations?**
   - A: To create/update database schema based on models

## 🛠️ Troubleshooting

### Issue: Images not showing
**Solution**: Make sure `MEDIA_URL` and `MEDIA_ROOT` are configured in settings.py and URLs are set up correctly.

### Issue: Admin panel not accessible
**Solution**: Run `python manage.py createsuperuser` to create an admin account.

### Issue: Page not found error
**Solution**: Check your URL patterns and make sure they're included in the main `urls.py`.

## 📚 Resources
- [Django Documentation](https://docs.djangoproject.com/)
- [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- [Django MVT Architecture](https://docs.djangoproject.com/en/stable/faq/general/#django-appears-to-be-a-mvc-framework-but-you-call-the-controller-the-view-and-the-view-the-template-how-come-you-don-t-use-the-standard-names)

## 👨‍💻 Author
Term Project - Django Portfolio Website

## 📄 License
This project is created for educational purposes as part of a university term project.

---

**Note**: This is a complete, working Django project ready for demonstration and viva. All requirements have been implemented according to the project specifications.
