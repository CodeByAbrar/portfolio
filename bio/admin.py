"""
Bio app admin configuration.
"""
from django.contrib import admin
from .models import Bio


@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    """
    Admin interface for Bio model.
    """
    list_display = ('name', 'job_title', 'created_at', 'updated_at')
    search_fields = ('name', 'job_title')
    list_filter = ('created_at',)
    
    # Limit to only one bio entry
    def has_add_permission(self, request):
        # Allow adding only if no Bio exists
        if Bio.objects.count() >= 1:
            return False
        return super().has_add_permission(request)
