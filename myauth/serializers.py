from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'current_song_name', 'current_song_url', 'profile_picture',
                  'latitude', 'longitude', 'spotify_profile_url']
