from rest_framework import serializers
from .models import User, Like


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'current_song_name', 'current_song_url', 'profile_picture',
                  'latitude', 'longitude', 'spotify_profile_url']


class LikeSerializer(serializers.ModelSerializer):
    given_to = UserSerializer()
    given_by = UserSerializer()

    class Meta:
        model = Like
        fields = ['id', 'created_at', 'song_name', 'song_url', 'given_by', 'given_to']
