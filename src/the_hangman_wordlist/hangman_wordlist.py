"""
The Hangman Wordlist
By Noah Bozkurt and Jurriaan Portier
"""
import requests
import json
import random
import os
from importlib_metadata import version as ver, PackageNotFoundError

class HangmanWordlist:
    def __init__(self) -> None:
        self.online_list: str = "https://raw.githubusercontent.com/TheBiemGamer/TheHangmanWordlist/refs/heads/main/src/the_hangman_wordlist/wordlist.json"
        self.local_file: str = "wordlist.json"
        self.wordlist: dict = self.load_wordlist()
        self.difficulties: list[str] = ["easy", "medium", "hard"]
        self.current_version: str = self.get_version()
        self.word: str = ""

    def fetch_online_wordlist(self) -> dict:
        response = requests.get(self.online_list)
        return response.json()

    def load_wordlist(self) -> dict:
        local_wordlist: dict = {}
        if os.path.exists(self.local_file):
            try:
                with open(self.local_file, "r") as local_file:
                    local_wordlist = json.load(local_file)
            except json.JSONDecodeError:
                print("Local wordlist file is corrupted or empty. Re-downloading...")
                local_wordlist = {}

        if local_wordlist is None or "version" not in local_wordlist:
            try:
                wordlist: dict = self.fetch_online_wordlist()
                self.save_wordlist(wordlist)
                print("Downloaded and saved new wordlist")
                return wordlist
            except requests.RequestException:
                raise Exception("Failed to fetch online wordlist, and no valid local wordlist found.")

        try:
            online_wordlist: dict = self.fetch_online_wordlist()
            if float(online_wordlist["version"]) > float(local_wordlist["version"]):
                self.save_wordlist(online_wordlist)
                print("Downloaded and saved new wordlist")
                return online_wordlist
            else:
                return local_wordlist
        except requests.RequestException:
            print("Failed to fetch online wordlist, using local version.")
            return local_wordlist

    def save_wordlist(self, wordlist: dict) -> None:
        with open(self.local_file, "w") as output_file:
            json.dump(wordlist, output_file, indent=4)

    def pull_word(self, diff: str = None) -> str:
        if diff is None or diff not in self.difficulties:
            diff = random.choice(self.difficulties)

        while True:
            new_word = random.choice(self.wordlist[diff])
            if new_word != self.word:
                break

        self.word = new_word
        return self.word

    @staticmethod #https://stackoverflow.com/questions/23554872/why-does-pycharm-propose-to-change-method-to-static
    def get_version() -> str:
        try:
            version = ver("the_hangman_wordlist")
        except PackageNotFoundError:
            version = "-unknown"
        return version
    
    def version(self) -> tuple[str, str]:
        return self.current_version, self.wordlist["version"]
"""
Example Usage:
from the_hangman_wordlist import HangmanWordlist
"""
if __name__ == "__main__":
    wordlist = HangmanWordlist()
    print("This is the example script for The Hangman Wordlist")
    difficulty: str = ""
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