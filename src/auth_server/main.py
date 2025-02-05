import threading

try:
    from .view import run

    # from .controller.token_receive import host
    # from .service.sso import open_sso

    # threading.Thread(target=open_sso).start()
    # host()

except Exception as e:
    print("Lỗi xác thực người dùng")
    print(str(e))