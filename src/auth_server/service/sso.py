import webbrowser
from ..service.config_reader import server_port

url = f"https://sso.hcmutssps.id.vn/login?redirect=http%3A%2F%2Flocalhost%3A{server_port}%2Freceive"

def open_sso():
    webbrowser.open(url)

def verify_token():
    pass