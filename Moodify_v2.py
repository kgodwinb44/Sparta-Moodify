# App for Deezer API
import requests

# By artist name
artist_name = "sab"
resultByArtist = requests.get("https://api.deezer.com/search", params={"q": artist_name})
song = resultByArtist.json()["data"][0]
print("\nSong by Artist")
print("Artist:", song["artist"]["name"])
print("Song:", song["title"])
print("Link:", song["link"])


# By mood and year (figure out year part)
# Set mood and year
mood = "happy"
year = "2025"
resultByMood = requests.get("https://api.deezer.com/search", params={"q": mood, "limit": 1})
song = resultByMood.json()["data"][0]

print("\n🎵 Song by Mood and Year")
print("Song:", song["title"])
print("Artist:", song["artist"]["name"])
print("Album:", song["album"]["title"])
print("Link:", song["link"])