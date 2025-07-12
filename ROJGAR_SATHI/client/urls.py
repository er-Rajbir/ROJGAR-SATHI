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
    path('requests/history/', views.request_history, name='request_history'),
    path('requests/', views.request_status, name='request_status'),
    path('request/<int:request_id>/cancel/', views.cancel_request, name='cancel_request'),
    path('request/<int:pk>/reschedule/', views.reschedule_request, name='reschedule_request'),
    path('mark-completed/<int:request_id>/', views.mark_as_completed, name='mark_completed'),
    path('requests/<int:request_id>/complete/', views.mark_as_completed, name='mark_as_completed'),


]
