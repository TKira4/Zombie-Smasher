import json
import os

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

def add_point(points):
    data = load_data()
    data["point"] += points
    save_data(data)
    print(f"New point Saved: {data['point']}")  

def upgrade_gun():
    global data

    if(data is None):
        data = load_data()
    
    gun_level = data.get("gun_level", 1)
    point = data.get("point", 0)

    upgrade_cost = gun_level * 100
    if point >= upgrade_cost:
        data["point"] -= upgrade_cost  
        data["gun_level"] += 1  
        save_data(data)  
        return f"Gun upgraded to level {data['gun_level']}!"
    else:
        return "Not enough points to upgrade!"

def get_gun_level():
    if(data is not None):
        return data["gun_level"]
    
    return load_data().get("gun_level", 1)
