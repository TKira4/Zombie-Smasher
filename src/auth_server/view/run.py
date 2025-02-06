import os
import signal
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPalette
from ..service.sso import open_sso
from src.auth_server.service.store_reader import email_reader
import time

def stop_server():
    os.kill(os.getpid(), signal.SIGINT)
    
class UI:
    ''' self:
        app
        window
        layout

        greeting_label
        enter_game_button
        exit_button

        player_name
    '''

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = QWidget()
        self.layout = QVBoxLayout()

        self.__private_window_config()

        try:
            self.player_name = email_reader().split("@")[0]

            self.greeting_label = QLabel(f"Chào, {self.player_name}!", self.window)
            self.greeting_label.setAlignment(Qt.AlignCenter) 
            self.greeting_label.setStyleSheet("font-size: 70px; font-weight: bold; color: #333;")
            self.layout.addWidget(self.greeting_label)
        except:
            self.player_name = None
            self.greeting_label = QLabel(f"Chưa đăng nhập", self.window)
            self.greeting_label.setAlignment(Qt.AlignCenter) 
            self.greeting_label.setStyleSheet("font-size: 70px; font-weight: bold; color: #333;")
            self.layout.addWidget(self.greeting_label)

        self.__private_button_load()

        # Thiết lập layout cho cửa sổ và căn giữa mọi thứ
        self.window.setLayout(self.layout)

        # Thiết lập màu nền cho cửa sổ
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(240, 240, 240))  # Màu nền sáng
        self.window.setPalette(palette)

        # Hiển thị cửa sổ
        self.window.show()

        threading.Thread(target=self.__private_check).start()

        sys.exit(self.app.exec_())

    def __private_window_config(self):
        self.window.setWindowTitle("Giao diện PyQt5")
        self.window.setWindowFlags(self.window.windowFlags() & ~Qt.WindowCloseButtonHint)

        screen = self.app.primaryScreen()
        screen_geometry = screen.geometry()

        window_width = 1600
        window_height = 1200

        x = (screen_geometry.width() - window_width) // 2
        y = (screen_geometry.height() - window_height) // 3

        self.window.setGeometry(x, y, window_width, window_height)

    def __private_button_load(self):
        self.enter_game_button = QPushButton("Vào game", self.window)
        self.enter_game_button.setStyleSheet("""
            background-color: #0000FF; 
            color: white; 
            font-size: 36px; 
            border-radius: 10px; 
            padding: 10px; 
            margin-bottom: 20px;
        """)
        self.enter_game_button.clicked.connect(self.__private_open_game) 
        self.layout.addWidget(self.enter_game_button)
        self.enter_game_button.setCursor(Qt.PointingHandCursor)

        # Thêm nút Đăng nhập
        self.login_button = QPushButton("Đăng nhập", self.window)
        self.login_button.setStyleSheet("""
            background-color: #4CAF50; 
            color: white; 
            font-size: 36px; 
            border-radius: 10px; 
            padding: 10px; 
            margin-bottom: 20px;
        """)
        self.login_button.clicked.connect(open_sso)  
        self.layout.addWidget(self.login_button)
        self.login_button.setCursor(Qt.PointingHandCursor)

        # Đăng xuất
        self.logout_button = QPushButton("Đăng xuất", self.window)
        self.logout_button.setStyleSheet("""
            background-color: #f44336; 
            color: white; 
            font-size: 36px; 
            border-radius: 10px; 
            padding: 10px; 
        """)
        self.logout_button.clicked.connect(self.__private_logout)  
        self.layout.addWidget(self.logout_button)
        self.logout_button.setCursor(Qt.PointingHandCursor)

        # Thoát
        self.exit_button = QPushButton("Thoát", self.window)
        self.exit_button.setStyleSheet("""
            background-color: #f44336; 
            color: white; 
            font-size: 36px; 
            border-radius: 10px; 
            padding: 10px; 
        """)
        self.exit_button.clicked.connect(stop_server)  
        self.layout.addWidget(self.exit_button)
        self.exit_button.setCursor(Qt.PointingHandCursor)
    
        self.enter_game_button.setVisible(False)
        self.logout_button.setVisible(False)
        self.login_button.setVisible(False)
        self.exit_button.setVisible(False)

        if(self.player_name is not None):
            self.enter_game_button.setVisible(True)
            self.logout_button.setVisible(True)
        else:
            self.exit_button.setVisible(True)
            self.login_button.setVisible(True)

    def __private_logout(self):
        import os
        os.remove("data/auth/store.json")
        self.greeting_label.setText("Chưa đăng nhập")

        self.__private_hide_button(self.logout_button)
        self.__private_hide_button(self.enter_game_button)
        self.__private_show_button(self.exit_button)
        self.__private_show_button(self.login_button)

    def __private_hide_button(self, button):
        button.setVisible(False)

    def __private_show_button(self, button):
        button.setVisible(True)

    def __private_change_greet(self):
        self.player_name = email_reader().split("@")[0]
        self.greeting_label.setText(f"Chào {self.player_name}")

    def __private_open_game(self):
        from src.game.run import game
        threading.Thread(target=game).start()

    def __private_check(self):
        while True:
            try:
                self.__private_change_greet()
                self.__private_show_button(self.enter_game_button)
                self.__private_show_button(self.logout_button)
            except Exception as e:
                print(str(e))
                pass
            finally:
                time.sleep(5)

def ui():
    ui = UI()
