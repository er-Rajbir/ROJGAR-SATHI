from django.contrib import admin
from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView



urlpatterns = [
    
    path('', views.home, name='home'),
   
    
    path('about/', views.about_view, name='about'),
    path('privacy-terms/', views.privacy_terms_view, name='privacy_terms'),
    
    path('login/', auth_views.LoginView.as_view(template_name='base/login.html'), name='login'),
    path('logout/',LogoutView.as_view(next_page='home'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),



]