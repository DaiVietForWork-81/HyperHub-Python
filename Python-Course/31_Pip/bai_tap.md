# 📝 Bài 31: Bài Tập – Pip

> 🎯 **Chủ đề:** `pip install`, `pip uninstall`, `pip list`, `pip show`, `pip freeze`, `requirements.txt`, phiên bản thư viện, nâng cấp pip.
> 🖥️ Đây là bài tập **lý thuyết + thao tác thực hành** — mở terminal, kích hoạt venv rồi thực hiện!

---

## 📌 Hướng dẫn làm bài

* Bài **lý thuyết**: ghi câu trả lời ngắn gọn.
* Bài **thao tác**: gõ lệnh trong terminal (trong venv), ghi lại kết quả.
* Nên tạo thư mục `bai_tap_pip` và venv riêng cho bài này.
* Đáp án chi tiết 20 bài: 👉 [xem file dap_an.md](dap_an.md)

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Pip là gì?

* **Đề bài:** Nêu vai trò của pip trong 1-2 câu. Thư viện Python được tải từ trang nào?
* **Input:** Không có
* **Output:** 1-2 câu trả lời.
* **Gợi ý:** pip = trình quản lý thư viện; nguồn chính thức là PyPI.

### Bài 2: Kiểm tra pip

* **Đề bài:** Chạy `python -m pip --version` và ghi lại kết quả (phiên bản pip và đường dẫn).
* **Input:** Thao tác thật.
* **Output:** Dòng kết quả của lệnh.
* **Gợi ý:** Nên chạy trong venv đã kích hoạt.

### Bài 3: Lệnh cài thư viện

* **Đề bài:** Ghi lệnh cài thư viện `requests` (bản mới nhất).
* **Input:** Không có
* **Output:** Một dòng lệnh.
* **Gợi ý:** `pip install` + tên thư viện.

### Bài 4: Cài đúng phiên bản

* **Đề bài:** Ghi lệnh cài `requests` **đúng phiên bản 2.31.0**.
* **Input:** Không có
* **Output:** Một dòng lệnh.
* **Gợi ý:** Thêm `==` và số phiên bản.

### Bài 5: Xem danh sách thư viện

* **Đề bài:** Chạy `pip list` trong venv (sau khi đã cài requests). Ghi lại **tên và phiên bản của 3 thư viện bất kỳ** trong danh sách.
* **Input:** Thao tác thật.
* **Output:** 3 dòng dạng `ten    phien_ban`.
* **Gợi ý:** Chú ý các thư viện phụ thuộc như certifi, charset-normalizer.

### Bài 6: Xem chi tiết thư viện

* **Đề bài:** Chạy `pip show requests` và ghi lại: **Version**, **Summary**, **Requires**.
* **Input:** Thao tác thật.
* **Output:** 3 dòng thông tin.
* **Gợi ý:** `Requires` cho biết thư viện phụ thuộc.

### Bài 7: Lệnh gỡ thư viện

* **Đề bài:** Ghi lệnh gỡ `requests` **không cần xác nhận** (tự động chọn y).
* **Input:** Không có
* **Output:** Một dòng lệnh.
* **Gợi ý:** Dùng cờ `-y`.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Cài nhiều thư viện cùng lúc

* **Đề bài:** Ghi lệnh cài cùng lúc hai thư viện `requests` và `flask`.
* **Input:** Không có
* **Output:** Một dòng lệnh.
* **Gợi ý:** Liệt kê tên cách nhau dấu cách.

### Bài 9: Thực hành trọn vòng đời

* **Đề bài:** Trong venv: cài `flask` → `pip list` → gỡ `flask -y` → `pip list` lần nữa. Ghi lại **số thư viện trước** và **sau** khi gỡ flask.
* **Input:** Thao tác thật.
* **Output:** 2 con số + nhận xét.
* **Gợi ý:** Đếm số dòng trong bảng `pip list` (trừ dòng tiêu đề).

### Bài 10: Xuất requirements.txt

* **Đề bài:** Sau khi cài `requests`, chạy `pip freeze > requirements.txt` rồi mở file ghi lại **toàn bộ nội dung**.
* **Input:** Thao tác thật.
* **Output:** Nội dung file (4-6 dòng).
* **Gợi ý:** Xem file bằng `type requirements.txt` (Windows) hoặc `cat requirements.txt`.

### Bài 11: Khôi phục từ requirements.txt

* **Đề bài:** Tạo venv **mới** tên `venv2` (trong cùng thư mục), kích hoạt, chạy `pip install -r requirements.txt`, rồi `pip list`. Kết luận: danh sách có giống venv ban đầu không?
* **Input:** Thao tác thật.
* **Output:** Kết luận + 3 dòng đầu `pip list` của venv2.
* **Gợi ý:** Các bước giống bài 30 (tạo venv + kích hoạt).

### Bài 12: Nâng cấp pip

* **Đề bài:** Chạy `python -m pip install --upgrade pip` và ghi lại phiên bản pip **sau khi** nâng cấp (nếu chưa mới).
* **Input:** Thao tác thật.
* **Output:** Phiên bản pip mới.
* **Gợi ý:** Lệnh tự báo `already up to date` nếu pip đã mới nhất.

### Bài 13: Kiểm tra thư viện cũ

* **Đề bài:** Chạy `pip list --outdated` và giải thích kết quả bạn nhận được (có danh sách hay không, vì sao).
* **Input:** Thao tác thật.
* **Output:** Kết quả + lời giải thích.
* **Gợi ý:** Lệnh chỉ hiện thư viện có phiên bản mới hơn trên PyPI.

### Bài 14: Tìm hiểu `pip check`

* **Đề bài:** Chạy `pip check` trong venv. Ghi lại kết quả và giải thích ý nghĩa.
* **Input:** Thao tác thật.
* **Output:** Kết quả lệnh + giải thích.
* **Gợi ý:** Kết quả "No broken requirements found" = môi trường lành mạnh.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Kịch bản xung đột phiên bản

* **Đề bài:** Viết 5-7 câu mô tả tình huống: dự án cần `numpy==1.24` nhưng bạn gõ `pip install numpy` vô tình cài bản 2.1. Điều gì xảy ra và giải pháp thế nào?
* **Input:** Không có
* **Output:** Đoạn văn 5-7 câu.
* **Gợi ý:** Nhắc đến `pip list` để kiểm tra, `pip install numpy==1.24` để hạ phiên bản, venv để cách ly.

### Bài 16: Script cài tự động theo file

* **Đề bài:** Viết file `cai_het.bat` (Windows) làm: kích hoạt venv, cài theo `requirements.txt`, chạy `pip check`, rồi `pause`. Ghi nội dung file.
* **Input:** Không có
* **Output:** Nội dung file `.bat` (4 dòng).
* **Gợi ý:** `venv\Scripts\activate` → `pip install -r requirements.txt` → `pip check` → `pause`.

### Bài 17: Báo cáo môi trường

* **Đề bài:** Tạo venv sạch mới `venv_sach`, kích hoạt, gõ `pip list`. Ghi lại: có bao nhiêu thư viện? Gồm những gì? Giải thích vì sao có `pip` mà không có `requests`.
* **Input:** Thao tác thật.
* **Output:** Bảng pip list + giải thích.
* **Gợi ý:** Môi trường mới chỉ có pip (và các công cụ cơ bản); thư viện chưa được cài thủ công.

### Bài 18: Cài thư viện và xem "ai dựa vào ai"

* **Đề bài:** Cài `flask`, rồi `pip show flask` ghi lại `Requires`. Sau đó với từng thư viện trong Requires, chạy `pip show` và ghi lại `Summary` của 2 thư viện bất kỳ.
* **Input:** Thao tác thật.
* **Output:** Dòng Requires của flask + 2 dòng Summary.
* **Gợi ý:** Flask phụ thuộc werkzeug, jinja2, click... — bạn thấy "cây phụ thuộc".

### Bài 19: Gỡ một thư viện phụ thuộc

* **Đề bài:** Trong venv đã cài `requests`, thử `pip uninstall urllib3 -y` (urllib3 là phụ thuộc của requests), rồi `python -c "import requests"`. Ghi lại lỗi (nếu có) và giải thích vì sao.
* **Input:** Thao tác thật.
* **Output:** Thông báo lỗi + giải thích.
* **Gợi ý:** requests gọi urllib3 bên trong; gỡ urllib3 → import requests có thể báo lỗi module.

### Bài 20: Dự án "checklist pip" hoàn chỉnh

* **Đề bài:** Viết file `huong_dan_cai_dat.md` (checklist 6 mục) cho bạn mới vào nhóm, gồm: tạo venv, kích hoạt, cài theo requirements.txt, kiểm tra pip list, pip check, chạy thử chương trình.
* **Input:** Không có
* **Output:** File checklist 6 mục (ghi lại nội dung).
* **Gợi ý:** Mỗi mục kèm lệnh tương ứng trong dấu `` ` ``.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Thành thạo các lệnh pip cơ bản: install, uninstall, list, show.
* ✅ Xuất và khôi phục môi trường bằng `requirements.txt`.
* ✅ Cài đúng phiên bản thư viện, nâng cấp pip.
* ✅ Hiểu "cây phụ thuộc" và biết cách kiểm tra sức khỏe môi trường.

> 💪 Chưa tự làm được bài nào thì đừng lo — mở lại bài giảng, gõ từng lệnh trong terminal rồi quan sát kết quả. **Quen tay thì chẳng còn khó!**

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 32: JSON](../32_JSON/bai_giang.md)**