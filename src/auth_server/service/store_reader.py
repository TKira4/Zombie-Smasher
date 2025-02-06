import json
from pathlib import Path

json_file_path = Path('src/auth_server/data/store.json')

def token_reader():
    with open(json_file_path, 'r') as file:
        data = json.load(file)

        return data["token"]
    
def email_reader():
    with open(json_file_path, 'r') as file:
        data = json.load(file)

        return data["email"]

def insert_token(email:str, token: str):
    data = {"token": token, "email": email}

    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)  


