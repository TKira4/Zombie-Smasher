def open():
    import threading
    from ..service.sso import open_sso
    threading.Thread(target=open_sso).start()

def ui():
    import sys
    from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
    from PyQt5.QtCore import Qt
    from PyQt5.QtGui import QColor, QPalette
    

    def on_button_click():
        label.setText("Button Clicked!") 

    app = QApplication(sys.argv)

    # Tạo cửa sổ chính
    window = QWidget()
    window.setWindowTitle("Giao diện PyQt5")

    # Lấy thông tin màn hình
    screen = app.primaryScreen()
    screen_geometry = screen.geometry()

    # Kích thước cửa sổ
    window_width = 800
    window_height = 600

    # Tính toán vị trí cửa sổ sao cho nó ở giữa màn hình
    x = (screen_geometry.width() - window_width) // 2
    y = (screen_geometry.height() - window_height) // 3

    # Đặt vị trí và kích thước cửa sổ
    window.setGeometry(x, y, window_width, window_height)

    # Tạo layout để sắp xếp các widget
    layout = QVBoxLayout()

    # Thêm label hiển thị chữ "Hello", căn giữa và thay đổi font
    label = QLabel("Mẹ Mày Béo", window)
    label.setAlignment(Qt.AlignCenter)  # Căn giữa chữ
    layout.addWidget(label)

    # Thêm nút, căn giữa và thêm trang trí
    button = QPushButton("Click me", window)
    button.setStyleSheet("background-color: #4CAF50; color: white; font-size: 16px; border-radius: 10px; padding: 10px;")
    button.clicked.connect(open)  # Kết nối nút với hàm on_button_click
    layout.addWidget(button)

    # Thiết lập layout cho cửa sổ và căn giữa mọi thứ
    window.setLayout(layout)

    # Thiết lập màu nền cho cửa sổ
    palette = QPalette()
    palette.setColor(QPalette.Background, QColor(240, 240, 240))  # Màu nền sáng
    window.setPalette(palette)

    # Hiển thị cửa sổ
    window.show()

    sys.exit(app.exec_())
