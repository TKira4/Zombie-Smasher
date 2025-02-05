from .store_reader import token_reader
import requests

url = "https://sso.hcmutssps.id.vn/api/verifyToken.php?token="

def verify():
    res = requests.get(f"{url}{token_reader()}")

