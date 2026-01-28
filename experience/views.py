"""
Experience app views.
"""
from django.shortcuts import render
from .models import Experience


def experience_list(request):
    """
    View to display all experience entries.
    """
    experiences = Experience.objects.all()
    context = {
        'experiences': experiences,
    }
    return render(request, 'experience/experience_list.html', context)
