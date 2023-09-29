from django.urls import path
from .views import upload_video, play_video, list_videos

urlpatterns = [
    path('upload/', upload_video, name='upload_video'),
    path('play/<int:video_id>/', play_video, name='play_video'),
    # path('videos/', VideoListAPIView.as_view(), name='video-list'),
    path('videos/', list_videos, name='video-list'),
]
