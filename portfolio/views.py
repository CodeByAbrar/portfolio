"""
Main views for portfolio project.
This file contains the combined home view that fetches data from all apps.
"""
from django.shortcuts import render
from bio.models import Bio
from education.models import Education
from skills.models import Skill
from experience.models import Experience
from projects.models import Project


def home(request):
    """
    Combined home view that displays all portfolio sections.
    Fetches data from all apps using Django ORM.
    """
    # Fetch data from all models
    bio = Bio.objects.first()  # Get the single bio entry
    educations = Education.objects.all().order_by('-year')
    skills = Skill.objects.all()
    experiences = Experience.objects.all().order_by('-id')
    projects_list = Project.objects.all().order_by('-id')
    
    context = {
        'bio': bio,
        'educations': educations,
        'skills': skills,
        'experiences': experiences,
        'projects': projects_list,
    }
    
    return render(request, 'index.html', context)
