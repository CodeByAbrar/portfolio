"""
Projects app URL configuration.
"""
from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.projects_list, name='list'),
]
