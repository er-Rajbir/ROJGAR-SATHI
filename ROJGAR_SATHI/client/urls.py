from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register_client/', views.register_view, name='register_view'),
        
    
     path('dashboard/', views.dashboard, name='client_dashboard'),
]
