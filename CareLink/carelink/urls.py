"""
URL configuration for carelink project.

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
from django.urls import path
from care import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('home', views.home, name='home'),
    path('admin_login',views.admin_login , name='admin_login'),
    path('patient_login', views.patient_login, name='patient_login'),
    path('physician_login', views.physician_login, name='physician_login'),
    path('forgotpass', views.forgotpass, name='forgotpass'),
    path('patient_registration', views.patient_registration, name='patient_registration'),
    path('phys_registration', views.phys_registration, name='phys_registration'),
    path('admin_registration', views.admin_registration, name='admin_registration'),
]
