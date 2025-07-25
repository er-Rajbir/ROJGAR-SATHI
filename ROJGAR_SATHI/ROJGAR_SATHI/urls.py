"""
URL configuration for ROJGAR_SATHI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',include('hunarbaaz.urls')),
    path('',include('base.urls')),
    path('client/', include(('client.urls', 'client'), namespace='client')),
     path('hunarbaaz/', include(('hunarbaaz.urls', 'hunarbaaz'), namespace='hunarbaaz')),
    path('client/', include(('client.urls', 'client'), namespace='client')),
    path('reviews/', include(('reviews.urls', 'reviews'), namespace='reviews')),
    

    # path('client/', include('client.urls')),
    # path('hunarbaaz/', include(('hunarbaaz.urls', 'hunarbaaz'), namespace='hunarbaaz')),
    path('', include(('base.urls', 'base'), namespace='base')),  # Optional, if base has URLs



    


    # other urls...

    # Password reset views:
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

