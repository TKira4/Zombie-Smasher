import sys
from PyQt5.QtWidgets import QApplication, QWidget

# Khởi tạo ứng dụng
app = QApplication(sys.argv)

# Tạo cửa sổ chính
window = QWidget()
window.setWindowTitle("Giao diện PyQt5")
window.setGeometry(100, 100, 400, 300)  # X, Y, Width, Height

# Hiển thị cửa sổ
window.show()

# Chạy vòng lặp ứng dụng
sys.exit(app.exec_())
