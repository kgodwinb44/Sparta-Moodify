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


# Mapping answers to moods
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
    },
    3: {
        'a': "relaxed",
        'b': "energetic",
        'c': "romantic",
        'd': "sad",
        'e': "active",
        'f': "rebellious",
        'g': "sophisticated"
    }
}

# Ask questions and keep count of answers
def ask_questions():
    # For each mood, count a score
    mood_scores = {"relaxed": 0, "energetic": 0, "romantic": 0, "sad": 0, "active": 0, "rebellious": 0, "sophisticated": 0}

    questions = {
        1: "1. How are you feeling?\n   a. Relaxed\n   b. Energetic\n   c. Romantic\n   d. Sad\n   e. Active\n   f. Rebellious",
        2: "2. What kind of weather do you like?\n   a. Rainy\n   b. Sunny\n   c. Snowy\n   d. Cloudy\n   e.Shinny\n   f.Stormy",
        3: "3. Pick a color:\n   a. Blue\n   b. Yellow\n   c. Red\n   d. Grey\n   e.Green\n   f.Black\n"
    }

    # Iterate through the question items
    for q_num, question in questions.items():
        # Check if elements in questions.items
        while True:
            print(question)
            answer = input("Choose a, b, c, d, e or f: ").lower()
            if answer in ['a', 'b', 'c', 'd', 'e', 'f']:
                mood = answer_map[q_num][answer]
                mood_scores[mood] += 1
                break

    # Get the mood with the highest score
    final_mood = max(mood_scores, key=mood_scores.get)
    return final_mood

# Request mood feature from api
def get_deezer_song(mood):
    response = requests.get("https://api.deezer.com/search", params={"q": mood, "limit": 1})
    if response.status_code == 200:
        data = response.json().get("data", [])
        if data:
            song = data[0]
            return {
                "title": song['title'],
                "artist": song['artist']['name'],
                "link": song['link']
            }
    return None

def main():
    mood = ask_questions()

    song = get_deezer_song(mood)
    print("Recommended Song: ")
    print(f"\n Song: {song['title']}")
    print(f" Artist: {song['artist']}")
    print(f" Listen: {song['link']}")


if __name__ == "__main__":
    main()