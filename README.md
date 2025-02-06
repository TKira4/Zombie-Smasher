# Các lệnh:
- **Xóa dữ liệu**: python -B -m src.run --clear_db
- **Chạy chương trình**: python -B -m src.run 

# Zombie Smasher
- **Thể loại**: Game Arcade.
- **Mô tả**: Zombie Smasher là game giải trí, người chơi phải bắn hạ các Zombie xuất hiện từ những chiếc bình bí ẩn. Với thao tác chính là click chuột, người chơi cần nhanh chóng bắn trúng các Zombie để ghi điểm, giữ chuỗi combo, và tránh bị mất máu. Súng sẽ có giới hạn về đạn, vì thế phải tính toán kĩ lưỡng trước khi bắn.
# Tính năng chính:
- **Xác thực người dùng**: Xác thực qua sso và mỗi player có dữ liệu riêng.
- **Lựa chọn độ khó**: Người chơi chọn kích thước kệ (NxN).
- **Chơi Game**:
    - Zombie sẽ ngẫu nhiên xuất hiện từ những chiếc bình bí ẩn và tấn công người chơi.
    - Bắn trúng Zombie để tích điểm và giữ chuỗi combo. Nếu bắn hụt hoặc để lâu quá sẽ mất combo và có thể bị Zombie tấn công.
- **Súng có giới hạn đạn**: Tự động nạp lại đạn khi hết.
- **Optional**: Lưu điểm cao vào bảng xếp hạng.
- **Cửa hàng**: Người chơi có thể lựa chọn nâng cấp súng tại cửa hàng.
# Hướng dẫn cài đặt
**1. Yêu cầu hệ thống**
- Python 3.9 hoặc cao hơn (Tôi đang sử dụng Python 3.11.9).
- Thư viện pygame (2.6.0).
- Visual Studio Code (hoặc các IDE tương tự).

**2. Clone dự án từ Github**
```basg
git clone https://github.com/<username>/Zombie-Smasher.git
cd Zombie-Smasher
```
**3. Tạo và kích hoạt môi trường ảo**
*Đối với Windows:*
```basg
python -m venv venv
.\venv\Scripts\activate
```
*Đối với macOS/Linux:*
```basg
python3 -m venv venv
source venv/bin/activate
```
**4. Cài đặt thư viện cần thiết**
```basg
pip install -r requirement.txt     
```

# Hướng dẫn chạy
```basg
.\venv\Scripts\activate
python -B -m .\src\main.py
```
# Cấu trúc dự án
```plaintext
Zombie-Smasher/
│
├── assets/                 # Thư mục chứa tài nguyên của game
│   ├── sprites/            # Chứa hình ảnh
│   └── sound/              # Chứa âm thanh
│
│── screen/                 # Chứa các screen của game (menu, shop, game)
│
│── logic/                  # Chứa logic chính của game
│
│
│── game_objects/           # Chứa object
│
├── main.py                 # Điểm bắt đầu của game
├── setting.py              # File chứa cài đặt game
└── renderer.py             # Dùng riêng để vẽ UI
```
