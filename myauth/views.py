from django.db.models.functions import Now
from requests import Request
from rest_framework.parsers import JSONParser

from bachelorthesis_v2.settings import SOCIAL_AUTH_SPOTIFY_SCOPE, SOCIAL_AUTH_SPOTIFY_KEY
from .models import User, Like
from social_django.models import UserSocialAuth
from social_django.utils import load_strategy
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import spotipy

from .serializers import UserSerializer, LikeSerializer
from .utils import *


class UserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        # Update current song
        UserSocialAuth.objects.get_social_auth(uid=request.user, provider='spotify').refresh_token(load_strategy())
        access_token = request.user.social_auth.get(provider='spotify').get_access_token(load_strategy())

        current_song = spotipy.Spotify(auth=access_token).currently_playing()

        current_song_deserialized = currentSongToString(current_song)
        request.user.current_song_name = current_song_deserialized[0]
        request.user.current_song_url = current_song_deserialized[1]
        request.user.save()

        serializer = UserSerializer(request.user)
        content = {
            'user': serializer.data,
            'token': str(request.auth),  # None
        }
        return Response(content, status=status.HTTP_200_OK)

    def put(self, request):
        data = JSONParser().parse(request)
        serializer = UserSerializer(request.user, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DashboardUsersView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Todo: use User.object.all() instead of .values()
        # Get all users
        users = User.objects.values()
        filtered_users = closestUsers(request.user, users)
        # Get closest users
        content = {
            'users': filtered_users
        }
        return Response(content, status=status.HTTP_200_OK)


# Fetch default data about user from spotify after logging in
class LoginView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        UserSocialAuth.objects.get_social_auth(uid=request.user, provider='spotify').refresh_token(load_strategy())
        access_token = request.user.social_auth.get(provider='spotify').get_access_token(load_strategy())
        sp = spotipy.Spotify(auth=access_token)
        me = sp.me()
        try:
            request.user.profile_picture = me['images'][0]['url']
        except IndexError:
            request.user.profile_picture = ''

        request.user.spotify_profile_url = me['external_urls']['spotify']

        request.user.last_login = Now()
        request.user.save()
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Deletes auth token after Logout
class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class LikeView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        likes = Like.objects.filter(given_to=request.user)
        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            given_by = User.objects.filter(id=request.data['given_by']).first()
            given_to = User.objects.filter(id=request.data['given_to']).first()
            like = Like.objects.create(
                given_to=given_to,
                given_by=given_by,
                song_name=request.data['song_name'],
                song_url=request.data['song_url']
            )
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        serializer = LikeSerializer(like)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        try:
            given_by = User.objects.filter(id=request.data['given_by']).first()
            given_to = User.objects.filter(id=request.data['given_to']).first()
            like = Like.objects.filter(given_by=given_by,
                                       given_to=given_to,
                                       song_name=request.data['song_name'],
                                       song_url=request.data['song_url']).first()
            like.delete()
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)


'''
class CurrentSong(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        UserSocialAuth.objects.get_social_auth(uid=request.user, provider='spotify').refresh_token(load_strategy())
        access_token = request.user.social_auth.get(provider='spotify').get_access_token(load_strategy())

        sp = spotipy.Spotify(auth=access_token)
        current_song = sp.currently_playing()
        try:
            request.user.profile_picture = sp.me()['images'][0]['url']
        except IndexError:
            request.user.profile_picture = ''

        current_song_deserialized = currentSongToString(current_song)
        request.user.current_song_name = current_song_deserialized[0]
        request.user.current_song_url = current_song_deserialized[1]
        request.user.save()

        content = {
            'currently_playing': current_song
        }
        return Response(content)
'''

"""
class UpdateCoords(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if not request.data["latitude"] or not request.data["longitude"]:
            return Response(status.HTTP_400_BAD_REQUEST)

        request.user.latitude = request.data["latitude"]
        request.user.longitude = request.data["longitude"]
        request.user.save()
        return Response(status.HTTP_200_OK)
"""


class AuthURL(APIView):
    def get(self, request):
        url = Request('GET', 'https://accounts.spotify.com/authorize', params={
            'scope': SOCIAL_AUTH_SPOTIFY_SCOPE,
            'response_type': 'code',
            'redirect_uri': 'http://localhost:8080/',
            'client_id': SOCIAL_AUTH_SPOTIFY_KEY,
        }).prepare().url

        return Response({'url': url}, status=status.HTTP_200_OK)
