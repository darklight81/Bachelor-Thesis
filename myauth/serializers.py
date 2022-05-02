from rest_framework import serializers
from .models import User, Like, Friendship


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


class FriendshipSerializer(serializers.ModelSerializer):
    creator = UserSerializer()
    friend = UserSerializer()

    class Meta:
        model = Friendship
        fields = ['id', 'created_at', 'creator', 'friend']
