from django.contrib import admin
from django.urls import path, include
from .views import UserDetailView, UsersView, LogoutView, LikeView, LoginView, AuthURL
app_name = 'myauth'
urlpatterns = [
    path('login/', include('rest_social_auth.urls_token')),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('my-login/', LoginView.as_view(), name="my-login"),
    path('authurl/', AuthURL.as_view(), name='auth_url'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user'),
    path('users/', UsersView.as_view(), name='users'),
    # path('current-song/', CurrentSong.as_view(), name='current_song'),
    # path('update-coords/', UpdateCoords.as_view(), name='update'),
    path('likes/', LikeView.as_view(), name='like'),
]
