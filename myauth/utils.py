from haversine import haversine
from sortedcontainers import SortedList
from .models import User


def closestUsers(user, users):
    queryset = []
    user_location = (user.latitude, user.longitude)
    for x in users:
        if x['latitude'] is None or x['longitude'] is None:
            pass
        else:
            pass
            x['distance'] = haversine(user_location, (x['latitude'], x['longitude']))
            queryset.append(x)
    srt = sorted(queryset, key=lambda i: i['distance'])
    return srt


def currentSongToString(current_song):
    current_song_str = ''
    current_song_url = ''
    if current_song is not None:
        current_song_str += current_song['item']['name']
        current_song_str += ' - '

        for i, artist in enumerate(current_song['item']['artists']):
            current_song_str += artist['name']
            if i != len(current_song['item']['artists']) - 1:
                current_song_str += ', '

        if current_song['item']['external_urls']['spotify']:
            current_song_url = current_song['item']['external_urls']['spotify']

    return current_song_str, current_song_url
