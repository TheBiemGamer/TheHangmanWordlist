"""
The Hangman Wordlist
By Noah Bozkurt and Jurriaan Portier
"""

import requests
import json
import random
import os
from importlib_metadata import version

class HangmanWordlist:
    def __init__(self):
        self.online_list = "https://raw.githubusercontent.com/TheBiemGamer/TheHangmanWordlist/refs/heads/main/src/the_hangman_wordlist/wordlist.json"
        self.local_file = "wordlist.json"
        self.wordlist = self.load_wordlist()
        self.difficulties = ["easy", "medium", "hard"]
        self.current_version = version("the_hangman_wordlist")
        self.word = None

    def fetch_online_wordlist(self):
        response = requests.get(self.online_list)
        return response.json()

    def load_wordlist(self):
        local_wordlist = None
        if os.path.exists(self.local_file):
            with open(self.local_file, "r") as local_file:
                local_wordlist = json.load(local_file)
        if local_wordlist is None or "version" not in local_wordlist:
            wordlist = self.fetch_online_wordlist()
            self.save_wordlist(wordlist)
            print("Downloaded and saved new wordlist")
            return wordlist
        try:
            online_wordlist = self.fetch_online_wordlist()
            if float(online_wordlist["version"]) > float(local_wordlist["version"]):
                self.save_wordlist(online_wordlist)
                print("Downloaded and saved new wordlist")
                return online_wordlist
            else:
                return local_wordlist
        except requests.RequestException:
            print("Failed to fetch online wordlist, using local version.")
            return local_wordlist

    def save_wordlist(self, wordlist):
        with open(self.local_file, "w") as output_file:
            json.dump(wordlist, output_file, indent=4)

    def pull_word(self, diff = None):
        if diff is None or diff not in self.difficulties:
            diff = random.choice(self.difficulties)
        while True:
            new_word = random.choice(self.wordlist[diff])
            if new_word != self.word:
                break
        self.word = new_word
        return self.word

    def version(self):
        return self.current_version, self.wordlist["version"]

"""
Example Usage:
from the_hangman_wordlist import HangmanWordlist
"""
if __name__ == "__main__":
    wordlist = HangmanWordlist()
    print("This is the example script for The Hangman Wordlist")
    difficulty = ""
    while difficulty not in {"easy", "medium", "hard", "random"}:
        difficulty = input("What difficulty do you want? (easy/medium/hard/random): ").lower()
        difficulty = {
            "e": "easy",
            "m": "medium",
            "h": "hard",
            "r": "random"
        }.get(difficulty, difficulty)

    script_version, wordlist_version = wordlist.version()
    print(f"Library v{script_version} and wordlist v{wordlist_version}.")

    while True:
        print(f"\n{difficulty.capitalize()} difficulty word: '{wordlist.pull_word(difficulty)}'\n")
        if input("Press Enter to generate a word or type 'exit' to quit... ").lower() == "exit":
            break