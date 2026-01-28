"""
Experience app URL configuration.
"""
from django.urls import path
from . import views

app_name = 'experience'

urlpatterns = [
    path('', views.experience_list, name='list'),
]
