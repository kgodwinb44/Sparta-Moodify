#Start if API Mini-Project
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id="88814e4970aa486b925f12e71c99b858",
    client_secret="8c02517f55354fa5b86aaca95b4c7e48"
))

results = sp.search(q='sabrinacarpenter', type='artist')
artist = results['artists']['items'][0]
print("\nSong by Artist")
print(f"Artist: {artist['name']}, Followers: {artist['followers']['total']}")

resultsForMood = sp.search(q='sad', type='track', limit=1)
track = resultsForMood["tracks"]["items"][0]
print("\nSong by Mood")
print("Song:", track["name"])
print("Artist:", track["artists"][0]["name"])
print("Link:", track["external_urls"]["spotify"])