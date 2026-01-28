"""
Projects app models.
Contains the Project model for storing portfolio projects.
"""
from django.db import models


class Project(models.Model):
    """
    Model to store project information.
    """
    title = models.CharField(max_length=200, help_text="Project title")
    description = models.TextField(help_text="Project description and details")
    image = models.ImageField(upload_to='projects/', blank=True, null=True, help_text="Project screenshot or image")
    project_link = models.URLField(max_length=500, blank=True, null=True, help_text="Link to live project or repository")
    technologies = models.CharField(max_length=300, blank=True, null=True, help_text="Technologies used (comma-separated)")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
