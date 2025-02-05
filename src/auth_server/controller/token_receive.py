from multiprocessing import Process
import threading

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

                from src.game.run import game
                threading.Thread(target=game).start()

                return {"message": "Xác thực thành công, đang mở ứng dụng"}
            else:
                return {"message": "Không thể xác thực :v"}

        uvicorn.run(app, host="127.0.0.1", port=server_port)
    except Exception as e:
        pass
