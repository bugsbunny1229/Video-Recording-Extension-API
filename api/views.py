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

@csrf_exempt
def upload_video(request):
    if request.method == 'POST':
        video_file = request.FILES.get('video_file')
        if video_file:
            # Check if the uploaded file is a video
            allowed_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv']
            file_extension = os.path.splitext(video_file.name)[1].lower()
            if file_extension not in allowed_extensions:
                return JsonResponse({'error': 'Invalid file type. Only video files are allowed.'}, status=400)

            try:
                Video.objects.create(video_file=video_file)
                return JsonResponse({'message': 'Video uploaded successfully.'})
            except ValidationError:
                return JsonResponse({'error': 'Invalid file format.'}, status=400)
    return JsonResponse({'error': 'Invalid request'})

def play_video(request, video_id):
    try:
        video = Video.objects.get(pk=video_id)
        return render(request, 'play_video.html', {'video': video})
    except Video.DoesNotExist:
        return JsonResponse({'error': 'Video not found'}, status=404)

@api_view(['GET'])
def list_videos(request):
    if request.method == 'GET':
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)