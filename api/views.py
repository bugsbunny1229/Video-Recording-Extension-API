import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import VideoRecording
from .serializers import VideoRecordingSerializer

class CreateVideoRecording(APIView):
    def post(self, request):
        video_recording = VideoRecording.objects.create()
        return Response({'uuid': str(video_recording.uuid)}, status=status.HTTP_201_CREATED)

class AddDataToRecording(APIView):
    def patch(self, request, uuid):
        try:
            video_recording = VideoRecording.objects.get(uuid=uuid)
        except VideoRecording.DoesNotExist:
            return Response({'error': 'Video recording not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Append the received binary data to the existing video file.
        binary_data = request.data.get('binary_data', b'')
        if not video_recording.is_complete:
            video_recording.video_file.file.write(binary_data)
            video_recording.video_file.file.close()
            video_recording.save()
            return Response({'message': 'Data appended successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Recording is already complete.'}, status=status.HTTP_400_BAD_REQUEST)

class CompleteRecording(APIView):
    def patch(self, request, uuid):
        try:
            video_recording = VideoRecording.objects.get(uuid=uuid)
        except VideoRecording.DoesNotExist:
            return Response({'error': 'Video recording not found.'}, status=status.HTTP_404_NOT_FOUND)

        video_recording.is_complete = True
        video_recording.save()

        video_url = video_recording.video_url

        if video_url:
            return Response({'message': 'Recording marked as complete.', 'video_url': video_url}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Recording marked as complete.'}, status=status.HTTP_200_OK)