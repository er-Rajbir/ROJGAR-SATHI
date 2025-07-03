from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('register_client/', views.register_view, name='register_view'),
    path('dashboard/', views.client_dashboard, name='client_dashboard'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('request/create/', views.create_work_request, name='create_request'),
    path('all/', views.hunarbaaz_list, name='all_profiles'),
    path('hunarbaaz/<int:id>/', views.hunarbaaz_detail_view, name='hunarbaaz_details'),
    # client/urls.py
#path('hunarbaaz/<int:pk>/', views.hunarbaaz_details, name='hunarbaaz_details'),


]
