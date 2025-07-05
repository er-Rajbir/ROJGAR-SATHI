from django.contrib import admin
from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('dashboard/', views.hunarbaaz_dashboard, name='hunarbaaz_dashboard'),
    path('register/', views.register_hunarbaaz, name='register_hunarbaaz'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('requests/', views.view_requests, name='view_requests'),

    
    path('request/<int:request_id>/accept/', views.accept_request, name='accept_request'),
path('request/<int:request_id>/reject/', views.reject_request, name='reject_request'),
path('mark-completed/<int:request_id>/', views.mark_as_completed, name='mark_completed'),
path('work-history/', views.work_history, name='work_history'),


    
]
