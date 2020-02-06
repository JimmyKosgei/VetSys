"""VetSys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,  include, re_path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/login/', obtain_jwt_token),
    path('auth/refresh-token/', refresh_jwt_token),
    path('api-auth/', include('rest_framework.urls')),
    re_path('', include('cases.urls')),
    re_path('', include('costs.urls')),
    re_path('', include('diagnosis.urls')),
    re_path('', include('lab_exam.urls')),
    re_path('', include('physycal_exam.urls')),
    re_path('', include('vets.urls'))
]
