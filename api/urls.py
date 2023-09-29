from django.urls import path
from .views import upload_video, list_videos

urlpatterns = [
    path('upload/', upload_video, name='upload_video'),
    path('videos/', list_videos, name='video-list'),
]
