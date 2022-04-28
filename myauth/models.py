from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    profile_picture = models.URLField(max_length=255, null=True, blank=True)
    current_song_name = models.CharField(max_length=255, null=True)
    current_song_url = models.URLField(max_length=255, null=True)
    spotify_profile_url = models.URLField(max_length=255, null=True)


class Like(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    song_name = models.CharField(max_length=255)
    song_url = models.URLField(max_length=255)
    given_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='given_by', unique=False)
    given_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='given_to', unique=False)
