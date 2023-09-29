from django.shortcuts import render
from rest_framework import viewsets
from .models import Video
from .serializers import VideoSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ValidationError
import os
from django.urls import reverse

@csrf_exempt
def upload_video(request):
    """Upload video."""
    if request.method == 'POST':
        video_file = request.FILES.get('video_file')
        if video_file:
            # Check if the uploaded file is a video
            allowed_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv']
            file_extension = os.path.splitext(video_file.name)[1].lower()
            if file_extension not in allowed_extensions:
                return JsonResponse({'error': 'Invalid file type. Only video files are allowed.'}, status=400)

            try:
                # Save the video and reverse the url
                video = Video.objects.create(video_file=video_file)
                video_url = request.build_absolute_uri(video.video_file.url)
                return JsonResponse({'message': 'Video uploaded successfully.', 'video_url': video_url})
            except ValidationError:
                return JsonResponse({'error': 'Invalid file format.'}, status=400)
    return JsonResponse({'error': 'Invalid request'})

@api_view(['GET'])
def list_videos(request):
    """List all videos."""
    if request.method == 'GET':
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)