from multiprocessing import Process
import threading
import requests
from fastapi.responses import HTMLResponse

url = "https://sso.hcmutssps.id.vn/api/verifyToken.php"

def host():
    try:
        from fastapi import FastAPI
        import uvicorn
        from ..service.config_reader import server_port
            
        app = FastAPI()

        @app.get("/receive", response_class=HTMLResponse)
        def read_items(token: str = None):
            if token:
                email = requests.get(f"{url}?token={token}").json()["message"]["sub"]
                from src.data.data_handler import check_data_exist, data_init

                from ..service.store_reader import insert_token
                insert_token(token)

                if(not check_data_exist(email)):
                    data_init(email)

                from src.game.run import game
                threading.Thread(target=game).start()

                return """
                    <html>
                    <head>
                        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
                        <style>
                            body {
                                background-color: #f8f9fa;
                                display: flex;
                                justify-content: center;
                                align-items: center;
                                height: 100vh;
                                margin: 0;
                            }
                            .container {
                                text-align: center;
                                background-color: #ffffff;
                                padding: 20px;
                                border-radius: 8px;
                                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                                width: 90%;
                                max-width: 500px;
                            }
                            h2 {
                                color: #28a745;
                            }
                            p {
                                font-size: 1.2rem;
                                color: #333;
                            }
                        </style>
                    </head>
                    <body>
                        <div class="container">
                            <h2>Xác thực thành công, đang mở ứng dụng...</h2>
                        </div>
                    </body>
                    </html>
                """
            else:
                return {"message": "Không thể xác thực :v"}

        uvicorn.run(app, host="127.0.0.1", port=server_port)
    except Exception as e:
        pass

if __name__ == "__main__":
    email = requests.get(f"{url}?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJleHAiOjE3Mzg4NDIyNzIsInN1YiI6InFzY3ZkZWZiQGdtYWlsLmNvbSIsImtleSI6IiQyeSQxMCRSeHJsLzJDYW43MkV6U2dNdnk2VGFPNk5OZ2NXTXZzVmxXekQvQjFDYTVld250Lld3QS9idSJ9.5APdNnZ-3ZoYxXlxEvr0FGUJ-VwjoVvY7XwxNrG3WRdV2FD-pSv6K7WluzMqmkgKiOvgFuMRZKvtfEq3EPVFTg").json()["message"]["sub"]
