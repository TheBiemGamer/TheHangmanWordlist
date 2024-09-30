import requests
import json
import random

wordlist = "https://raw.githubusercontent.com/TheBiemGamer/TheHangmanWordlist/refs/heads/main/wordlist.json"
response = requests.get(wordlist)

data = json.loads(response.text)
difficulty = input("What difficulty do you want? (easy/medium/hard): ")
word = random.choice(data[difficulty])
print(word)