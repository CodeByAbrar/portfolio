"""
Education app views.
"""
from django.shortcuts import render
from .models import Education


def education_list(request):
    """
    View to display all education entries.
    """
    educations = Education.objects.all().order_by('-year')
    context = {
        'educations': educations,
    }
    return render(request, 'education/education_list.html', context)
