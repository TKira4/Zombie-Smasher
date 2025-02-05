import webbrowser

url = "https://sso.hcmutssps.id.vn/login?redirect=http%3A%2F%2Flocalhost%3A8000%2Freceive"

def sso():
    webbrowser.open(url)