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


if not os.path.exists("wordlist.json"):
    wordlist = pull_wordlist()
else:
    local_json_file = open("wordlist.json", "r").read()
    local_wordlist = json.loads(local_json_file)
    local_version = float(local_wordlist["version"])
    online_json_file = requests.get("https://raw.githubusercontent.com/TheBiemGamer/TheHangmanWordlist/refs/heads/main/wordlist.json")
    online_wordlist = json.loads(online_json_file.text)
    online_version = float(local_wordlist["version"])
    print(online_version, local_version)
    if online_version > local_version:
        wordlist = pull_wordlist()
    else:
        wordlist = local_wordlist

difficulty = input("What difficulty do you want? (easy/medium/hard): ")
word = random.choice(wordlist[difficulty])
print(word)

