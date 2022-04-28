from django.contrib import admin
from django.urls import path, include
from .views import AuthURL, UserView, DashboardUsersView, CurrentSong, UpdateCoords, Logout, LikeSong
app_name = 'myauth'
urlpatterns = [
    path('login/', include('rest_social_auth.urls_token')),
    path('logout/', Logout.as_view(), name='logout'),
    path('authurl/', AuthURL.as_view(), name='auth_url'),
    path('user/', UserView.as_view(), name='user'),
    path('users/', DashboardUsersView.as_view(), name='users'),
    path('current-song/', CurrentSong.as_view(), name='current_song'),
    path('update-coords/', UpdateCoords.as_view(), name='update'),
    path('like-song/', LikeSong.as_view(), name='like_song'),
]
