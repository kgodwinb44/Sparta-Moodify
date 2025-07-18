#Start if API Mini-Project
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id="88814e4970aa486b925f12e71c99b858",
    client_secret="8c02517f55354fa5b86aaca95b4c7e48"
))

