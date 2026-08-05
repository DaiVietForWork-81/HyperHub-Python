# ✅ Bài 31: Đáp Án – Pip

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án. Các bài thao tác: mô tả từng lệnh để bạn tự kiểm chứng trên máy.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Pip là gì?

**Đáp án mẫu:**

> pip là **trình quản lý thư viện** của Python — công cụ cài đặt, gỡ bỏ, cập nhật và liệt kê các thư viện trong môi trường Python. Thư viện được tải từ **PyPI** (Python Package Index) tại https://pypi.org/ — "chợ thư viện" chính thức của cộng đồng Python.

---

### Bài 2: Kiểm tra pip

**Các lệnh:**

```bash
python -m pip --version
```

**Kết quả mẫu (số phiên bản có thể khác máy):**

```
pip 26.1.2 from C:\Users\An\bai_tap_pip\venv\Lib\site-packages\pip (python 3.14)
```

**Giải thích:** dòng kết quả cho biết phiên bản pip (`26.1.2`), vị trí đặt pip (đang nằm **trong venv** — chứng tỏ đã kích hoạt đúng môi trường) và phiên bản Python đi kèm.

---

### Bài 3: Lệnh cài thư viện

**Đáp án:**

```bash
pip install requests
```

Không ghi phiên bản → pip cài **bản mới nhất** của `requests` (kèm các thư viện phụ thuộc tự động).

---

### Bài 4: Cài đúng phiên bản

**Đáp án:**

```bash
pip install requests==2.31.0
```

Ký hiệu `==` nghĩa là "đúng phiên bản này". pip sẽ gỡ phiên bản khác (nếu có) và cài 2.31.0.

---

### Bài 5: Xem danh sách thư viện

**Lệnh:**

```bash
pip list
```

**Kết quả mẫu (3 thư viện bất kỳ):**

```
Package            Version
------------------ ----------
certifi            2025.5.15
charset-normalizer 3.4.1
idna               3.10
```

**Giải thích:** ngoài `requests`, pip tự cài các **thư viện phụ thuộc** (certifi, charset-normalizer, idna, urllib3) — bạn thấy chúng trong `pip list`.

---

### Bài 6: Xem chi tiết thư viện

**Lệnh:**

```bash
pip show requests
```

**Kết quả mẫu (3 dòng quan trọng):**

```
Name: requests
Version: 2.32.3
Summary: Python HTTP for Humans.
Requires: certifi, charset-normalizer, idna, urllib3
```

**Giải thích:** `Version` — phiên bản đang dùng; `Summary` — mô tả ngắn; `Requires` — danh sách thư viện mà requests cần (mục này rất hữu ích khi gỡ cài).

---

### Bài 7: Lệnh gỡ thư viện

**Đáp án:**

```bash
pip uninstall requests -y
```

Cờ `-y` tự trả lời "y" cho câu hỏi xác nhận → gỡ ngay không hỏi.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Cài nhiều thư viện cùng lúc

**Đáp án:**

```bash
pip install requests flask
```

Một lệnh cài cả hai — pip xử lý lần lượt từng thư viện và tự giải quyết phụ thuộc chung.

---

### Bài 9: Thực hành trọn vòng đời

**Các lệnh:**

```bash
pip install flask
pip list | findstr /C:"flask"      # Windows (kiểm tra có flask)
pip uninstall flask -y
pip list
```

**Nhận xét mẫu:** trước khi gỡ flask, `pip list` có thêm `flask` và các phụ thuộc như `click`, `itsdangerous`, `jinja2`, `markupsafe`, `werkzeug`; sau khi `pip uninstall flask -y`, **flask biến mất** nhưng các phụ thuộc có thể vẫn còn (pip không tự gỡ chúng). Số thư viện sau ít hơn trước đúng 1 (nếu không cài thứ khác xen vào).

---

### Bài 10: Xuất requirements.txt

**Các lệnh:**

```bash
pip freeze > requirements.txt
type requirements.txt
```

**Nội dung mẫu của file:**

```
certifi==2025.5.15
charset-normalizer==3.4.1
idna==3.10
requests==2.32.3
urllib3==2.3.0
```

**Giải thích:** định dạng `ten_thu_vien==phien_ban`, mỗi thư viện một dòng — đây là "thực đơn" để dựng lại môi trường.

---

### Bài 11: Khôi phục từ requirements.txt

**Các lệnh (từ thư mục dự án):**

```bash
python -m venv venv2
venv2\Scripts\activate            # macOS/Linux: source venv2/bin/activate
pip install -r requirements.txt
pip list
```

**Kết luận:** `pip list` của `venv2` giống hệt venv ban đầu (cùng tên thư viện và phiên bản) → chứng minh `requirements.txt` tái tạo môi trường chính xác.

---

### Bài 12: Nâng cấp pip

**Lệnh:**

```bash
python -m pip install --upgrade pip
```

**Kết quả mẫu:** nếu pip chưa mới, lệnh tải phiên bản mới và in phiên bản mới, ví dụ `pip 26.1.2`. Nếu đã mới: `Requirement already satisfied: pip ...` — nghĩa là đã là bản mới nhất, không cần nâng cấp.

---

### Bài 13: Kiểm tra thư viện cũ

**Lệnh:**

```bash
pip list --outdated
```

**Giải thích:** lệnh kết nối PyPI để so sánh; nếu có thư viện nào trên máy có bản mới hơn thì hiện ra kèm cột `Latest`. Nếu không có gì (hoặc không hiện thư viện nào), nghĩa là mọi thư viện đang dùng đều là bản mới nhất trên PyPI tại thời điểm kiểm tra.

---

### Bài 14: Tìm hiểu `pip check`

**Lệnh:**

```bash
pip check
```

**Kết quả mẫu:**

```
No broken requirements found.
```

**Giải thích:** pip rà soát mọi thư viện đã cài xem có thư viện nào thiếu phụ thuộc hoặc có yêu cầu phiên bản bị vi phạm không. Kết quả trên nghĩa là môi trường **lành mạnh, không thiếu sót**.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Kịch bản xung đột phiên bản

**Đáp án mẫu:**

> Dự án của tôi cần `numpy==1.24.0` vì toàn bộ code tính toán dựa trên hành vi phiên bản cũ. Tôi lơ đãng gõ `pip install numpy` — pip cài phiên bản **mới nhất là 2.1.0** và gỡ bản 1.24 cũ. Khi chạy dự án, các hàm dùng cú pháp cũ bắt đầu báo lỗi hoặc cho kết quả khác, chương trình trục trặc. Kiểm tra bằng `pip show numpy` tôi phát hiện phiên bản đã nhảy lên 2.1.0. Giải pháp: gõ lại `pip install numpy==1.24.0` để hạ về đúng phiên bản cần thiết. Rút kinh nghiệm: luôn ghi phiên bản rõ ràng trong `requirements.txt` và kiểm tra `pip list` sau mỗi lần cài. Về lâu dài, mỗi dự án dùng một venv riêng để không bao giờ đụng phiên bản của dự án khác.

---

### Bài 16: Script cài tự động theo file

**Nội dung file `cai_het.bat` (Windows):**

```bat
@echo off
venv\Scripts\activate
pip install -r requirements.txt
pip check
pause
```

**Giải thích:**
* `@echo off` — tắt in lệnh thừa.
* `venv\Scripts\activate` — kích hoạt môi trường.
* `pip install -r requirements.txt` — cài toàn bộ theo danh sách.
* `pip check` — kiểm tra môi trường lành mạnh.
* `pause` — giữ cửa sổ mở để đọc kết quả.

---

### Bài 17: Báo cáo môi trường

**Các lệnh:**

```bash
python -m venv venv_sach
venv_sach\Scripts\activate
pip list
```

**Kết quả mẫu:**

```
Package    Version
---------- -------
pip        26.1.2
```

**Giải thích:** môi trường mới chỉ có `pip` (và vài công cụ nền tảng) — **không có `requests`** vì chưa ai cài. Môi trường ảo khởi đầu "sạch bong"; bạn cài thư viện nào mới có thư viện đó. Đây chính là điểm mạnh của venv: không "nhiễm" sẵn thứ gì từ hệ thống.

---

### Bài 18: Cài thư viện và xem "ai dựa vào ai"

**Các lệnh:**

```bash
pip install flask
pip show flask
pip show werkzeug
pip show jinja2
```

**Kết quả mẫu:**

```
Requires của flask: click, itsdangerous, jinja2, markupsafe, werkzeug

Name: werkzeug
Summary: The comprehensive WSGI web application library.

Name: jinja2
Summary: A very fast and expressive template engine.
```

**Giải thích:** `Requires` của flask liệt kê "gia đình" thư viện con; mỗi thư viện con có chức năng riêng (werkzeug lo HTTP, jinja2 lo template...). Hiểu được "cây phụ thuộc" giúp bạn biết môi trường mình đang nắm giữ những gì.

---

### Bài 19: Gỡ một thư viện phụ thuộc

**Các lệnh:**

```bash
pip uninstall urllib3 -y
python -c "import requests"
```

**Kết quả mẫu (lỗi):**

```
ModuleNotFoundError: No module named 'urllib3'
```

**Giải thích:** `requests` bên trong dùng `urllib3` để gửi yêu cầu HTTP. Khi gỡ `urllib3`, lệnh `import requests` vẫn nạp được requests nhưng khi dùng mới vỡ lở — thậm chí bản requests mới báo lỗi ngay khi import. Bài học: **không tùy tiện gỡ thư viện phụ thuộc**; muốn gỡ requests thì gỡ cả cụm, hoặc xem `Requires` trước khi quyết định.

---

### Bài 20: Dự án "checklist pip" hoàn chỉnh

**Nội dung file `huong_dan_cai_dat.md` mẫu:**

```markdown
# 📌 Hướng dẫn cài đặt môi trường cho người mới

1. Tạo môi trường ảo: `python -m venv venv`
2. Kích hoạt: `venv\Scripts\activate` (Windows) / `source venv/bin/activate` (macOS/Linux)
3. Cài thư viện theo danh sách: `pip install -r requirements.txt`
4. Kiểm tra danh sách: `pip list` (so sánh với requirements.txt)
5. Kiểm tra môi trường lành mạnh: `pip check`
6. Chạy thử chương trình: `python main.py`
```

**Giải thích:** checklist 6 bước giúp người mới (và chính bạn sau này) dựng môi trường đúng và nhanh, tránh lỗi "chạy không được do thiếu thư viện".

---

## 📌 Lời khuyên cuối

* Luôn **kích hoạt venv** trước khi dùng pip — kiểm tra dấu `(venv)`.
* Ưu tiên `python -m pip` để dùng đúng pip của Python hiện hành.
* Mỗi dự án nên có `requirements.txt` ở gốc — đó là "giấy khai sinh" môi trường.
* Đọc `Requires` trước khi gỡ thư viện để tránh phá phụ thuộc.
* Cài đúng phiên bản bằng `==` khi dự án yêu cầu khắt khe.

👉 Tiếp theo: **[Bài 32: JSON](../32_JSON/bai_giang.md)**