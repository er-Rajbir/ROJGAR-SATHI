from django.contrib import admin
from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('dashboard/', views.hunarbaaz_dashboard, name='hunarbaaz_dashboard'),
    path('register/', views.register_hunarbaaz, name='register_hunarbaaz'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]
