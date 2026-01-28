"""
Projects app admin configuration.
"""
from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    Admin interface for Project model.
    """
    list_display = ('title', 'technologies', 'project_link', 'created_at')
    search_fields = ('title', 'description', 'technologies')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
