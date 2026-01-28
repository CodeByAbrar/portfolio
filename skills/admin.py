"""
Skills app admin configuration.
"""
from django.contrib import admin
from .models import Skill


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """
    Admin interface for Skill model.
    """
    list_display = ('name', 'level', 'created_at')
    search_fields = ('name',)
    list_filter = ('level', 'created_at')
    ordering = ('name',)
