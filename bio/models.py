"""
Bio app models.
Contains the Bio model for storing personal information.
"""
from django.db import models


class Bio(models.Model):
    """
    Model to store personal bio information.
    Should only have one entry in the database.
    """
    name = models.CharField(max_length=100, help_text="Your full name")
    job_title = models.CharField(max_length=100, help_text="Your current job title or role")
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True, help_text="Your profile picture")
    description = models.TextField(help_text="A brief description about yourself")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Bio"
        verbose_name_plural = "Bio"
    
    def __str__(self):
        return self.name
