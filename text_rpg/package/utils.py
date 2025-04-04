import json
import os.path

from package.moodels import Player


def load_game():
    if os.path.exists("./save.json"):
        with open("./save.json", "r", encoding="utf-8") as file:
            date = json.load(file)
            return Player.from_dict(date)
    return None

def save_game(player):
    with open("./save.json", "w", encoding="utf-8") as file:
        json.dump(player.to_dict(), file, indent=4)




