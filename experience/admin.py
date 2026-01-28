"""
Experience app admin configuration.
"""
from django.contrib import admin
from .models import Experience


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    """
    Admin interface for Experience model.
    """
    list_display = ('role', 'organization', 'duration', 'created_at')
    search_fields = ('role', 'organization')
    list_filter = ('created_at',)
    ordering = ('-id',)
