from django.db.models.functions import Now
from django.http import Http404
from requests import Request
from rest_framework.parsers import JSONParser

from bachelorthesis_v2.settings import SOCIAL_AUTH_SPOTIFY_SCOPE, SOCIAL_AUTH_SPOTIFY_KEY
from .models import User, Like, Friendship
from social_django.models import UserSocialAuth
from social_django.utils import load_strategy
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import spotipy

from .serializers import UserSerializer, LikeSerializer, FriendshipSerializer
from .utils import *


class UserDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return User.objects.get(id=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        # Update current song
        user = self.get_object(pk)
        serializer = UserSerializer(user)

        if request.user.id is user.id:
            content = {
                'user': serializer.data,
                'token': str(request.auth),  # None
            }
        else:
            content = {
                'user': serializer.data,
            }
        return Response(content, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)

        if user.id is not request.user.id:
            return Response({"detail": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)

        UserSocialAuth.objects.get_social_auth(uid=user, provider='spotify').refresh_token(load_strategy())
        access_token = user.social_auth.get(provider='spotify').get_access_token(load_strategy())

        current_song = spotipy.Spotify(auth=access_token).currently_playing()
        current_song_deserialized = currentSongToString(current_song)
        data = JSONParser().parse(request)

        data['username'] = request.user.username
        if current_song is not None:
            data['current_song_name'] = current_song_deserialized[0]
            data['current_song_url'] = current_song_deserialized[1]
        serializer = UserSerializer(request.user, data=data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Get all users
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        # Get closest users
        filtered_users = closestUsers(request.user, serializer.data)
        content = {
            'users': filtered_users
        }
        return Response(content, status=status.HTTP_200_OK)


class UserFriendsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return User.objects.get(id=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)

        serializer = FriendshipSerializer(user.friends, many=True)
        print(serializer.data)
        content = {
            'friends': serializer.data
        }
        return Response(content, status=status.HTTP_200_OK)

    def post(self, request, pk, format=None):
        user = self.get_object(pk)

        if user.id is not request.user.id:
            return Response({"detail": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)

        data = JSONParser().parse(request)
        try:
            friend = self.get_object(data['friend_id'])
        except KeyError:
            return Response({'error': 'Missing parameter friend_id in body.'}, status=status.HTTP_400_BAD_REQUEST)

        if Friendship.objects.filter(friend_id=data['friend_id'], creator_id=pk).exists():
            return Response({'error': 'Friendship already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        friendship = Friendship.objects.create(creator=user, friend=friend)
        creator = User.objects.get(id=request.user.id)
        creator.friends.add(friendship)

        serializer = FriendshipSerializer(friendship)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        try:
            given_by = User.objects.filter(id=request.data['user_id']).first()
            friend = User.objects.filter(id=request.data['friend_id']).first()
            given_by.friends.filter(friend_id=friend.id).delete()
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)


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


class UserLikesView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return User.objects.get(id=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)

        serializer = LikeSerializer(user.likes.order_by('-created_at'), many=True)
        print(serializer.data)
        content = {
            'likes': serializer.data
        }
        return Response(content, status=status.HTTP_200_OK)

    def post(self, request, pk, format=None):
        given_to = self.get_object(pk)

        data = JSONParser().parse(request)
        try:
            given_by = self.get_object(data['given_by'])
            songName = data['song_name']
            songUrl = data['song_url']
        except (KeyError, ValueError):
            return Response({'error': 'Invalid request.'}, status=status.HTTP_400_BAD_REQUEST)

        if Like.objects.filter(given_by=given_by, given_to=given_to, song_name=songName, song_url=songUrl).exists():
            return Response({'error': 'Song already liked.'}, status=status.HTTP_400_BAD_REQUEST)

        like = Like.objects.create(given_by=given_by, given_to=given_to, song_name=songName, song_url=songUrl)
        given_to.likes.add(like)

        serializer = LikeSerializer(like)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        try:
            given_to = self.get_object(pk)
            given_by = self.get_object(request.data['given_by'])
            song_name = request.data['song_name']
            song_url = request.data['song_url']
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        like = given_to.likes.get(given_by=given_by, song_name=song_name, song_url=song_url)
        try:
            like.delete()
        except Exception as e:
            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_200_OK)


class AuthURL(APIView):
    def get(self, request):
        url = Request('GET', 'https://accounts.spotify.com/authorize', params={
            'scope': SOCIAL_AUTH_SPOTIFY_SCOPE,
            'response_type': 'code',
            'redirect_uri': 'https://igor.uhlik.ml/',
            'client_id': SOCIAL_AUTH_SPOTIFY_KEY,
        }).prepare().url

        return Response({'url': url}, status=status.HTTP_200_OK)
