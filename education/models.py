"""
Education app models.
Contains the Education model for storing educational background.
"""
from django.db import models


class Education(models.Model):
    """
    Model to store education information.
    """
    degree = models.CharField(max_length=200, help_text="Degree or certification name")
    institute = models.CharField(max_length=200, help_text="Name of educational institution")
    year = models.CharField(max_length=50, help_text="Year or duration (e.g., 2020-2024)")
    description = models.TextField(blank=True, null=True, help_text="Additional details about this education")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Education Entries"
        ordering = ['-year']
    
    def __str__(self):
        return f"{self.degree} - {self.institute}"
