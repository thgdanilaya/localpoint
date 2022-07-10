"""localpoint URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.template.defaulttags import url
from django.urls import path

from registration import views
from registration.views import home, LoginUser
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('registration/', views.Registration.as_view(), name='registration'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('reg_success/', views.reg_success, name="reg_success"),
    path('log_success/', views.log_success, name="log_success"),
    path('profile/', views.profile, name="profile"),
    path('map/', views.map, name="map")

]
