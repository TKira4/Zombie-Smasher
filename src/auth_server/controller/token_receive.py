def host():
    from fastapi import FastAPI
    import uvicorn

    app = FastAPI()

    @app.get("/receive")
    def read_items(token: str = None):
        if token:
            return {"token": f"{token}"}
        else:
            return {"message": "No token provided"}

    # Khởi động FastAPI từ trong Python
    uvicorn.run(app, host="127.0.0.1", port=8000)
