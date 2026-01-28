"""
Projects app views.
"""
from django.shortcuts import render
from .models import Project


def projects_list(request):
    """
    View to display all projects.
    """
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'projects/projects_list.html', context)
