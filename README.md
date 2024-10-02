# The Hangman Wordlist
A simple json wordlist for use with hangman with easy, medium and hard words!

### Example usage in python (see [main.py](main.py))
```py
import requests
import json
import random
import os

online_list = "https://raw.githubusercontent.com/TheBiemGamer/TheHangmanWordlist/refs/heads/main/wordlist.json"

def pull_wordlist():
    json_file = requests.get(online_list)
    wordlist = json_file.json()
    with open("wordlist.json", 'w') as input_file:
        input_file.seek(0)
        json.dump(wordlist, input_file, indent=4)
    print("Updated wordlist")
    return json.loads(json_file.text)


def pull_word(diff):
    if not os.path.exists("wordlist.json"):
        wordlist = pull_wordlist()
    else:
        local_json_file = open("wordlist.json", "r").read()
        local_wordlist = json.loads(local_json_file)
        local_version = float(local_wordlist["version"])
        online_json_file = requests.get(online_list)
        online_wordlist = json.loads(online_json_file.text)
        online_version = float(online_wordlist["version"])
        if online_version > local_version:
            wordlist = pull_wordlist()
        else:
            wordlist = local_wordlist

    word = random.choice(wordlist[diff])
    return word, wordlist["version"]

difficulty = input("What difficulty do you want? (easy/medium/hard): ")
word, version = pull_word(difficulty)
print(f"\nThe {difficulty} word is: '{word}'")
print(f"Wordlist v{version}")
input("\nPress Enter to exit...")
```

### Credits
- [Jurriaaaantje](https://github.com/Jurriaaaantje) (Wordlist words and update wordlist functionality)
- [TheBiemGamer](https://github.com/TheBiemGamer) (Version check and json functionality)
