"""
Bio app views.
"""
from django.shortcuts import render
from .models import Bio


def bio_detail(request):
    """
    View to display bio information.
    """
    bio = Bio.objects.first()
    context = {
        'bio': bio,
    }
    return render(request, 'bio/bio_detail.html', context)
