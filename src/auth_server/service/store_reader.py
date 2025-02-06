import json
from pathlib import Path

json_file_path = Path('data/auth/store.json')

def token_reader():
    with open(json_file_path, 'r') as file:
        data = json.load(file)

        return data["token"]
    
def email_reader():
    import requests
    url = "https://sso.hcmutssps.id.vn/api/verifyToken.php"

    with open(json_file_path, 'r') as file:
        data = json.load(file)

        token = data["token"]

        return requests.get(f"{url}?token={token}").json()["message"]["sub"]

def insert_token(token: str):
    data = {"token": token}

    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)  


