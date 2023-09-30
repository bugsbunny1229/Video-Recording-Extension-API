from rest_framework import serializers
from .models import VideoRecording

class VideoRecordingSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoRecording
        fields = '__all__'

