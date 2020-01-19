"""MedApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.urls import path
from . import settings
from MedWebApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(), name="index"),
    path('token_validator/',views.activate_user_by_token,name="token_validator"),
    path('signup/',views.SignUp.as_view(),name="signup"),
    path('login/', views.Login.as_view(), name="login"),
    path('directory/', views.Directory.as_view(), name="directory"),
    path('clinics/', views.Clinic.as_view(), name='clinic'),
    path('clinics/appointments', views.Clinic_appointment.as_view(), name='clinic_appointment'),
    path('clinics/financial', views.Clinic_financial.as_view(), name='clinic_financial'),
    path('clinics/visits', views.Clinic_visits.as_view(), name='clinic_visits')
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)  # MEDIA_URL, MEDIA_ROOT
