import json
from pathlib import Path

json_file_path = Path('src/auth_server/data/store.json')

def token_reader():
    global token

    with open(json_file_path, 'r') as file:
        data = json.load(file)

        return data["token"]

def insert_token(token: str):
    data = {"token": token}

    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)  
