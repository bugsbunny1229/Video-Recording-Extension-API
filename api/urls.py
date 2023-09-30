from django.urls import path
from .views import CreateVideoRecording, AddDataToRecording, CompleteRecording

urlpatterns = [
    path('create/', CreateVideoRecording.as_view(), name='create-video-recording'),
    path('add-data/<uuid:uuid>/', AddDataToRecording.as_view(), name='add-data-to-recording'),
    path('complete/<uuid:uuid>/', CompleteRecording.as_view(), name='complete-recording'),
]
