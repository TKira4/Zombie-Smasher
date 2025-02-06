import json
import os



def load_data():
    from src.data.data_handler import data_load
    return data_load()

def save_data(data):
    from src.data.data_handler import insert_data
    insert_data(data)

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
