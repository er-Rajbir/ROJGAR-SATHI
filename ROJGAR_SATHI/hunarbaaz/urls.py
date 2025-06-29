from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('karigars/', views.karigar_list, name='karigar_list'),
    path('employer/register/', views.employer_register, name='employer_register'),
    path('login/', views.login_view, name='login'),
]
