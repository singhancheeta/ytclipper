from django.db import models
from django.contrib.auth.models import User

class Clip(models.Model):
    url = models.URLField()
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class ClippedVideo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name
