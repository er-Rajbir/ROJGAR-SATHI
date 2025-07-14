from django.contrib import admin
from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView



urlpatterns = [
    
    path('', views.home, name='home'),    
    path('about/', views.about_view, name='about'),
    path('privacy-terms/', views.privacy_terms_view, name='privacy_terms'),
    path('logout/',LogoutView.as_view(next_page='home'), name='logout'),
    path('login/', views.login_view, name='login'),
    path('access_denied/', views.access_denied, name='access_denied'),
    path('mail/',views.send_mail_page,name='mail')
    
]
