import json
import os
import threading

data = None

def load_data():
    global data

    from src.data.data_handler import data_load

    data = data_load()
    return data

def save_data(data):
    from src.data.data_handler import insert_data
    insert_data(data)

def get_point():
    if(data is not None):
        return data["point"]
    
    return load_data().get("point", 0)

def insert_point_to_table(score):
    from src.data.score_query import scoreDB
    score_db = scoreDB()
    score_db.update_score(score)
    
def rankings():
    from src.data.score_query import scoreDB
    score_db = scoreDB()
    return score_db.get_score()

def add_point(points):
    global data

    if(data is None):
        data = load_data()

    data["point"] += points

    threading.Thread(target=save_data(data)).start()
    print(f"New point Saved: {data['point']}")  

def upgrade_gun():
    global data

    if(data is None):
        data = load_data()
    
    gun_level = data["gun_level"]
    point = data["point"]

    upgrade_cost = gun_level * 100
    if point >= upgrade_cost:
        data["point"] -= upgrade_cost  
        data["gun_level"] += 1  
        threading.Thread(target=save_data(data)).start()
        return f"Gun upgraded to level {data['gun_level']}!"
    else:
        return "Not enough points to upgrade!"

def get_gun_level():
    if(data is not None):
        return data["gun_level"]
    
    return load_data()["gun_level"]
