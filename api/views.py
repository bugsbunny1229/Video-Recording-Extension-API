from django.shortcuts import render
from rest_framework import viewsets
from .models import Video
from .serializers import VideoSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload_video(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        video_file = request.FILES.get('video_file')
        if title and video_file:
            Video.objects.create(title=title, video_file=video_file)
            return JsonResponse({'message': 'Video uploaded successfully'})
    return JsonResponse({'error': 'Invalid request'})

def play_video(request, video_id):
    try:
        video = Video.objects.get(pk=video_id)
        return render(request, 'play_video.html', {'video': video})
    except Video.DoesNotExist:
        return JsonResponse({'error': 'Video not found'}, status=404)
