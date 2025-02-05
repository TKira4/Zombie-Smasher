import threading

try:
    from .controller.token_receive import host
    from .service.sso_open import sso

    fastapi_thread = threading.Thread(target=host)
    fastapi_thread.start()

    sso()
    
except Exception as e:
    print("Lỗi xác thực người dùng")
    print(str(e))