import uuid
from django.db import models

class VideoRecording(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    video_file = models.FileField(upload_to='videos/', blank=True)
    is_complete = models.BooleanField(default=False)
    video_url = models.CharField(max_length=255, blank=True)  # Add this line to store the video URL

    def save(self, *args, **kwargs):
        # Generate the video URL based on the video_file path
        if self.video_file:
            self.video_url = self.video_file.url
        super().save(*args, **kwargs)
