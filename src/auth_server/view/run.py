def ui():
    import sys
    from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
    from PyQt5.QtCore import Qt
    from PyQt5.QtGui import QColor, QPalette
    from ..service.sso import open_sso

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
    label = QLabel("Xin lỗi em, Amanai. Anh không giận gì em đâu. Anh cũng chả hận thù gì người trên cõi đời này. Anh thấy, thế gian giờ thật tươi đẹp biết bao. Cảnh chim bay bướm lượn, hoa lá nở xum xuê 'Thiên thượng thiên hạ. Duy ngã độc tôn.'\nCái lợi của thuật thức di truyền đó là đã được biết và giảng giải tường tận. Nhưng đi kèm theo đó cũng là bất lợi khi thông tin thuật thức dễ dàng bị tuồng ra ngoài.\nXem ra ngươi chí ít đã từng sống cùng tộc nhân Zen'in một thời gian nên mới hiểu rõ cách Vô Hạ Hạn hoạt động.\nNhưng kể cả có là tộc nhân nhà Gojo cũng chỉ lác đác vài kẻ biết đến \"thứ này\". Thuận và đảo, xuôi và nghịch, hai thứ năng lượng trái dấu xung khắc nhau đến vô tận tạo ra luồng uy lực cực hạn từ hư không.\nHư Thức: Tử\" 🫸🏻🔴🔵🫷🏻🤌🏻🫴🏻🟣\"", window)
    label.setAlignment(Qt.AlignCenter)  # Căn giữa chữ
    layout.addWidget(label)

    # Thêm nút, căn giữa và thêm trang trí
    button = QPushButton("Click me", window)
    button.setStyleSheet("background-color: #4CAF50; color: white; font-size: 16px; border-radius: 10px; padding: 10px;")
    button.clicked.connect(open_sso)  # Kết nối nút với hàm on_button_click
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
