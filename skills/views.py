"""
Skills app views.
"""
from django.shortcuts import render
from .models import Skill


def skills_list(request):
    """
    View to display all skills.
    """
    skills = Skill.objects.all()
    context = {
        'skills': skills,
    }
    return render(request, 'skills/skills_list.html', context)
