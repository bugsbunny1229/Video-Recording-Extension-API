import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import VideoRecording
from .serializers import VideoRecordingSerializer
import openai

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
            # Transcribe the video using OpenAI Whisper
            try:
                openai.api_key = settings.OPENAI_API_KEY
                transcription = openai.Transcription.create(
                    audio_url=video_url,
                    model="whisper",
                    language="en-US",
                )
                transcription_text = transcription['text']
            except Exception as e:
                return Response({'error': 'Transcription failed.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response({
                'message': 'Recording marked as complete.',
                'video_url': video_url,
                'transcription_text': transcription_text,
            }, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Recording marked as complete.'}, status=status.HTTP_200_OK)
