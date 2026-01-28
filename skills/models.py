"""
Skills app models.
Contains the Skill model for storing technical and soft skills.
"""
from django.db import models


class Skill(models.Model):
    """
    Model to store skills and their proficiency levels.
    """
    LEVEL_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Expert', 'Expert'),
    ]
    
    name = models.CharField(max_length=100, help_text="Skill name (e.g., Python, Django)")
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='Intermediate', help_text="Proficiency level")
    description = models.TextField(blank=True, null=True, help_text="Additional details about this skill")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} ({self.level})"
