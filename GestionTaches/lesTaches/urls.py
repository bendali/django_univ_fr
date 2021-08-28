from . import views
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('home/<name>', views.home ,name='home'),
    path('listing/', views.task_listing, name='listing'),
]

