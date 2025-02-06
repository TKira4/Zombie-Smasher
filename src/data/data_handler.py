import json
import os

# Internal api do not call
def check_data_exist(email:str):
    file_path = f'src/data/{email.split("@")[0]}.json'
    return os.path.exists(file_path)

def data_init(email:str):
    data = {
        "score": 0,
        "gun_level": 0
    }

    with open(f'src/data/{email.split("@")[0]}.json', 'w') as file:
        json.dump(data, file, indent=4)  

# External api
def data_load(email:str):
    with open(f'src/data/{email.split("@")[0]}.json', 'r') as file:
        data = json.load(file)

    return data

def insert_data(email:str, data):
    with open(f'src/data/{email.split("@")[0]}.json', 'w') as file:
        json.dump(data, file, indent=4)  

if __name__ == "__main__":
    # # Nạp dữ liệu lần đầu:
    # data_init("qscvdefb@gmail.com")


    # # Lấy dữ liệu:
    # print(data_load("qscvdefb@gmail.com"))
    # print(data_load("khang.tran@gmail.com"))
    pass