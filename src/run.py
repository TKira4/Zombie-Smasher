import threading

try:
    from src.auth_server.view.run import ui
    from src.auth_server.controller.token_receive import host

    threading.Thread(target=ui).start()
    host()
except Exception as e:
    print(str(e))