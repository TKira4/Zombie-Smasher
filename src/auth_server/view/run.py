import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QScreen

app = QApplication(sys.argv)

# Tạo cửa sổ chính
window = QWidget()
window.setWindowTitle("Giao diện PyQt5")

# Lấy thông tin màn hình
screen = app.primaryScreen()
screen_geometry = screen.geometry()

# Kích thước cửa sổ
window_width = 400
window_height = 300

# Tính toán vị trí cửa sổ sao cho nó ở giữa màn hình
x = (screen_geometry.width() - window_width) // 2
y = (screen_geometry.height() - window_height) // 3

# Đặt vị trí và kích thước cửa sổ
window.setGeometry(x, y, window_width, window_height)

# Hiển thị cửa sổ
window.show()

sys.exit(app.exec_())
