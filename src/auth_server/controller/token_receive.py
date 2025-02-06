from multiprocessing import Process
import threading
import requests

url = "https://sso.hcmutssps.id.vn/api/verifyToken.php"

def host():
    try:
        from fastapi import FastAPI
        import uvicorn
        from ..service.config_reader import server_port
            
        app = FastAPI()

        @app.get("/receive")
        def read_items(token: str = None):
            if token:
                from ..service.store_reader import insert_token
                insert_token(token)

                email = requests.get(f"{url}?token={token}").json()["message"]["sub"]
                from src.data.data_handler import check_data_exist, data_init

                if(not check_data_exist(email)):
                    data_init(email)

                from src.game.run import game
                threading.Thread(target=game).start()

                return {"message": "Xác thực thành công, đang mở ứng dụng"}
            else:
                return {"message": "Không thể xác thực :v"}

        uvicorn.run(app, host="127.0.0.1", port=server_port)
    except Exception as e:
        pass

if __name__ == "__main__":
    email = requests.get(f"{url}?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJleHAiOjE3Mzg4NDIyNzIsInN1YiI6InFzY3ZkZWZiQGdtYWlsLmNvbSIsImtleSI6IiQyeSQxMCRSeHJsLzJDYW43MkV6U2dNdnk2VGFPNk5OZ2NXTXZzVmxXekQvQjFDYTVld250Lld3QS9idSJ9.5APdNnZ-3ZoYxXlxEvr0FGUJ-VwjoVvY7XwxNrG3WRdV2FD-pSv6K7WluzMqmkgKiOvgFuMRZKvtfEq3EPVFTg").json()["message"]["sub"]
