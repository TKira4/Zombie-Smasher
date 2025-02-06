import json
from pathlib import Path

'''
server_port: import server_port để lấy server_port
'''

json_file_path = Path('data/config.json')

with open(json_file_path, 'r') as file:
    data = json.load(file)

    server_port = int(data["server_port"])