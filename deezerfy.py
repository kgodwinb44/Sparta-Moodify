# Import to make HTTP requests
import requests

# Map moods to Deezer genre IDs
mood_to_genre = {
    "relaxed": 152,    # Chill
    "energetic": 113,  # Dance
    "romantic": 85,    # Love
    "sad": 129,        # Acoustic
    "active": 107,     # Workout
    "rebellious": 464,  # Metal
    "sophisticated": 98 # Classical
}

# Question answer to mood mapping
answer_map = {
    1: {
        'a': "relaxed",
        'b': "energetic",
        'c': "romantic",
        'd': "sad",
        'e': "active",
        'f': "rebellious",
        'g': "sophisticated"
    },
    2: {
        'a': "romantic",
        'b': "energetic",
        'c': "relaxed",
        'd': "sad",
        'e': "active",
        'f': "rebellious",
        'g': "sophisticated"
    }
}

# Ask questions and keep count of answers
def ask_questions():
    # Keep count of scores
    mood_scores = {"relaxed": 0, "energetic": 0, "romantic": 0, "sad": 0, "active": 0, "rebellious": 0, "sophisticated": 0}

    # Answers mapped in the answer_map
    questions = {
        1: "1. How are you feeling?\n   a. Relaxed\n   b. Energetic\n   c. Romantic\n   d. Sad\n   e. Active\n   f. Rebellious",
        2: "2. What kind of weather do you like?\n   a. Rainy\n   b. Sunny\n   c. Snowy\n   d. Cloudy\n   e.Shinny\n   f.Stormy",
    }

    # Count selected answer_map and map to mood_scores
    # Iterate through the question.items qnum = a,b,c
    for q_num, question in questions.items():
        # Check if elements in questions.items
        while True:
            print(question)
            # Make all answers lowercase .lower()
            answer = input("Choose a, b, c, d, e or f: ").lower()
            if answer in ['a', 'b', 'c', 'd', 'e', 'f']:
                mood = answer_map[q_num][answer]
                print(mood)
                mood_scores[mood] += 1
                break

    # Get the mood with the highest score
    final_mood = max(mood_scores, key=mood_scores.get)
    return final_mood

# Request song from selected mood
def get_deezer_song(mood):
    genre_id = mood_to_genre.get(mood)
    if genre_id is None:
        return None

    # Fetch top songs from the genre's editorial chart
    url = f"https://api.deezer.com/editorial/{genre_id}/charts"
    response = requests.get(url)

    # Check response code
    if response.status_code == 200:
        tracks = response.json().get("tracks", {}).get("data", [])
        if tracks:
            # Recommend the top track
            song = tracks[0]
            # Return dict
            return {
                "title": song['title'],
                "artist": song['artist']['name'],
                "link": song['link'],
                "album": song['album']
            }

    return None

def main():
    # Call questions function and assign the return value to mood
    mood = ask_questions()
    # Call deezer_song function and use the mood to find the song
    song = get_deezer_song(mood)
    album = requests.get(f"https://api.deezer.com/album/{song['album']['id']}").json()
    print("Recommended Song: ")
    print(f"\n Song: {song['title']}")
    print(f" Artist: {song['artist']}")
    print(f" Listen: {song['link']}")
    print(f" Release Date: {album['release_date']}")


if __name__ == "__main__":
    main()