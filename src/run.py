import threading
import argparse
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Quản lý database")
    parser.add_argument("--clear_db", action="store_true", help="Xóa toàn bộ dữ liệu trong database")
    args = parser.parse_args()

    if args.clear_db:
        from .data.score_query import scoreDB
        score_db = scoreDB()

        score_db.clear()    
        
        folder_path ="src/data/player"

        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)

            if os.path.isfile(file_path): 
                os.remove(file_path)
                print(f"Đã xóa: {file_path}")
        
        os.remove("src/auth_server/data/store.json")

        print("Đã xóa tất cả dữ liều người dùng!")

    else:
        try:
            from src.auth_server.view.run import ui
            from src.auth_server.controller.token_receive import host

            threading.Thread(target=ui).start()
            host()
        except Exception as e:
            print(str(e))