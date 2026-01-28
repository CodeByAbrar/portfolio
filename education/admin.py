"""
Education app admin configuration.
"""
from django.contrib import admin
from .models import Education


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    """
    Admin interface for Education model.
    """
    list_display = ('degree', 'institute', 'year', 'created_at')
    search_fields = ('degree', 'institute')
    list_filter = ('year', 'created_at')
    ordering = ('-year',)
