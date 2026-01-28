"""
Experience app models.
Contains the Experience model for storing work experience.
"""
from django.db import models


class Experience(models.Model):
    """
    Model to store work experience information.
    """
    role = models.CharField(max_length=200, help_text="Job title or role")
    organization = models.CharField(max_length=200, help_text="Company or organization name")
    description = models.TextField(help_text="Description of responsibilities and achievements")
    duration = models.CharField(max_length=100, blank=True, null=True, help_text="Duration (e.g., Jan 2022 - Present)")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experience Entries"
        ordering = ['-id']
    
    def __str__(self):
        return f"{self.role} at {self.organization}"
