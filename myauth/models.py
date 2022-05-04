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
    favorite_artist = models.CharField(max_length=20, null=True)
    favorite_song = models.CharField(max_length=20, null=True)
    favorite_podcast = models.CharField(max_length=20, null=True)
    favorite_genre = models.CharField(max_length=20, null=True)
    instagram_url = models.URLField(max_length=255, null=True)
    facebook_url = models.URLField(max_length=255, null=True)
    twitter_url = models.URLField(max_length=255, null=True)
    city = models.CharField(max_length=20, null=True)
    friends = models.ManyToManyField('Friendship')
    likes = models.ManyToManyField('Like')


class Like(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    song_name = models.CharField(max_length=255)
    song_url = models.URLField(max_length=255)
    given_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='given_by', unique=False)
    given_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='given_to', unique=False)


class Friendship(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, related_name="friendship_creator_set", on_delete=models.CASCADE)
    friend = models.ForeignKey(User, related_name="friend_set", on_delete=models.CASCADE)
