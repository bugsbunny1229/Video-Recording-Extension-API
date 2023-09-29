from django.db import models
from django.utils import timezone

class Video(models.Model):
    video_file = models.FileField(upload_to='videos/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
