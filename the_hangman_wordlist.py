"""
The Hangman Wordlist v0.4
By Noah Bozkurt and Jurriaan Portier

Example usage:
from the_hangman_wordlist import HangmanWordlist

if __name__ == "__main__":
    wordlist = HangmanWordlist()
    difficulty = input("What difficulty do you want? (easy/medium/hard): ")
    word, version = wordlist.pull_word(difficulty)
    print(f"\nThe {difficulty} word is: '{word}'")
    print(f"Wordlist v{version}")
    input("\nPress Enter to exit...")
"""
import requests
import json
import random
import os

class HangmanWordlist:
    def __init__(self):
        self.online_list = "https://raw.githubusercontent.com/TheBiemGamer/TheHangmanWordlist/refs/heads/main/wordlist.json"
        self.wordlist = HangmanWordlist.pull_wordlist(self)

    def pull_wordlist(self):
        json_file = requests.get(self.online_list)
        wordlist = json_file.json()
        with open("wordlist.json", 'w') as input_file:
            input_file.seek(0)
            json.dump(wordlist, input_file, indent=4)
        print("Updated wordlist")
        return json.loads(json_file.text)

    def pull_word(self, diff):
        if not os.path.exists("wordlist.json"):
            wordlist = HangmanWordlist.pull_wordlist(diff)
        else:
            local_json_file = open("wordlist.json", "r").read()
            local_wordlist = json.loads(local_json_file)
            local_version = float(local_wordlist["version"])
            online_json_file = requests.get(self.online_list)
            online_wordlist = json.loads(online_json_file.text)
            online_version = float(online_wordlist["version"])
            if online_version > local_version:
                wordlist = HangmanWordlist.pull_wordlist(diff)
            else:
                wordlist = local_wordlist
        word = random.choice(wordlist[diff])
        return word, wordlist["version"]