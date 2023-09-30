"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
schema_view = get_schema_view(
    openapi.Info(
        title = "Chrome Extension API", 
        default_version = "v1",
        description = "A Chrome extension API that provides the capability for individuals to stream binary data and seamlessly append it to an ongoing video recording process. Afterward, it saves the video and employs OpenAI Whisper to accurately transcribe the contents of these saved videos.",
        contact = openapi.Contact(email="johndbizz@gmail.com"),
        license = openapi.License(name="MIT License") 
        ),
        public = True,
        # permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
