import random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, PLAYLIST_ID

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
))

def get_random_song():
    results = sp.playlist_tracks(PLAYLIST_ID)
    tracks = [item['track'] for item in results['items'] if item['track']]

    track = random.choice(tracks)

    name = track['name']
    artist = track['artists'][0]['name']
    url = track['external_urls']['spotify']

    return f"🎵 **{name}** - {artist}\n{url}"
