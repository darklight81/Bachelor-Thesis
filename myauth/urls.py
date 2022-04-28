from django.contrib import admin
from django.urls import path, include
from .views import UserView, DashboardUsersView, LogoutView, LikeView, LoginView
app_name = 'myauth'
urlpatterns = [
    path('login/', include('rest_social_auth.urls_token')),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('my-login/', LoginView.as_view(), name="my-login"),
    # ('authurl/', AuthURL.as_view(), name='auth_url'),
    path('user/', UserView.as_view(), name='user'),
    path('users/', DashboardUsersView.as_view(), name='users'),
    # path('current-song/', CurrentSong.as_view(), name='current_song'),
    # path('update-coords/', UpdateCoords.as_view(), name='update'),
    path('like/', LikeView.as_view(), name='like'),
]
