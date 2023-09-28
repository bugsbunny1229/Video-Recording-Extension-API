from django.urls import path
from .views import upload_video, play_video

urlpatterns = [
    path('upload/', upload_video, name='upload_video'),
    path('play/<int:video_id>/', play_video, name='play_video'),
]
