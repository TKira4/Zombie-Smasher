import json
import os

DATA_FILE = "data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        data = {"score": 0, "gun_level": 1}
        save_data(data)  
        return data

    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def get_score():
    return load_data().get("score", 0)

def add_score(scores):
    data = load_data()
    data["score"] += scores
    save_data(data)
    print(f"New Score Saved: {data['score']}")  

def upgrade_gun():
    data = load_data()
    gun_level = data.get("gun_level", 1)
    score = data.get("score", 0)

    upgrade_cost = gun_level * 100
    if score >= upgrade_cost:
        data["score"] -= upgrade_cost  
        data["gun_level"] += 1  
        save_data(data)  
        return f"Gun upgraded to level {data['gun_level']}!"
    else:
        return "Not enough points to upgrade!"

def get_gun_level():
    return load_data().get("gun_level", 1)
