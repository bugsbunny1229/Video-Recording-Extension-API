from django.urls import path
from .views import upload_video, list_videos

urlpatterns = [
    path('api', upload_video, name='upload_video'),
    path('api/list', list_videos, name='video-list'),
]
