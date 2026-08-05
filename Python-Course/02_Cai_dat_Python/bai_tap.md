# 📝 Bài 2: Bài Tập – Cài Đặt Python

> 🎯 **Chủ đề:** Cài đặt Python, kiểm tra phiên bản, chạy chương trình từ dòng lệnh.

---

## 📌 Hướng dẫn

* Các bài tập phần lớn là **thao tác thực hành trên máy** — làm đủ từng bước.
* Mỗi bài đều ghi rõ **lệnh cần gõ** và **kết quả mong đợi**.
* Đáp án chi tiết: 👉 [xem file dap_an.md](dap_an.md)

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Kiểm tra Python đã cài chưa

* **Đề bài:** Mở cửa sổ dòng lệnh (Command Prompt) và kiểm tra Python đã cài chưa.
* **Input:** Gõ lệnh `python --version`.
* **Output:** Chương trình hiện ra phiên bản, ví dụ `Python 3.14.2`.
* **Gợi ý:** Nhấn `Windows + R`, gõ `cmd`, Enter rồi gõ lệnh.

### Bài 2: Kiểm tra thư mục chứa Python

* **Đề bài:** Tìm đường dẫn chính xác nơi `python.exe` đang được cài.
* **Input:** Gõ lệnh `where python`.
* **Output:** Một hoặc nhiều đường dẫn tới `python.exe`.
* **Gợi ý:** Lệnh này chỉ hoạt động khi PATH đã được thiết lập đúng.

### Bài 3: Kiểm tra pip

* **Đề bài:** Kiểm tra công cụ cài thư viện pip đã sẵn sàng chưa.
* **Input:** Gõ `python -m pip --version`.
* **Output:** Dòng chữ bắt đầu bằng `pip 2x.x.x`.
* **Gợi ý:** Pip đi kèm Python khi cài đặt.

### Bài 4: Vào chế độ tương tác

* **Đề bài:** Mở chế độ REPL (dấu nhắc `>>>`) và in ra dòng chữ `Chao mung`.
* **Input:** Gõ `python` rồi gõ `print("Chao mung")`.
* **Output:**
  ```
  >>> print("Chao mung")
  Chao mung
  ```
* **Gợi ý:** Sau đó gõ `exit()` để thoát.

### Bài 5: Tính toán trong REPL

* **Đề bài:** Trong chế độ `>>>`, tính `15 * 4` và `100 // 7`.
* **Input:** Lần lượt gõ hai phép tính.
* **Output:**
  ```
  >>> 15 * 4
  60
  >>> 100 // 7
  14
  ```
* **Gợi ý:** `//` là phép chia lấy phần nguyên.

### Bài 6: Tạo file đầu tiên

* **Đề bài:** Tạo file `hello.py` (dùng Notepad hoặc trình soạn thảo) chứa đúng 2 dòng: in tên bạn và in tuổi bạn.
* **Input:** Nội dung file `hello.py`.
* **Output khi chạy:**
  ```
  Ten toi la An
  Toi 15 tuoi
  ```
* **Gợi ý:** Nhớ lưu file với phần mở rộng `.py`, dấu nháy thẳng `"`.

### Bài 7: Chạy file hello.py

* **Đề bài:** Dùng Command Prompt chạy file `hello.py` vừa tạo.
* **Input:** Lệnh `python hello.py`.
* **Output:** In ra 2 dòng trong file.
* **Gợi ý:** Nếu báo "not recognized", hãy `cd` vào thư mục chứa file.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Di chuyển thư mục trong dòng lệnh

* **Đề bài:** Giả sử file `hello.py` nằm ở `D:\hoc_python`. Hãy gõ các lệnh để di chuyển tới thư mục đó và chạy file.
* **Input:**
  ```bash
  cd D:\hoc_python
  python hello.py
  ```
* **Output:** Nội dung in ra từ file.
* **Gợi ý:** Lệnh `cd` = change directory (đổi thư mục).

### Bài 9: Xem danh sách file trong thư mục

* **Đề bài:** Trong Command Prompt, gõ lệnh xem danh sách file.
* **Input:** Gõ `dir`.
* **Output:** Danh sách file/thư mục trong thư mục hiện tại.
* **Gợi ý:** Trên Linux gõ `ls`.

### Bài 10: Kiểm tra cả python và pip cùng lúc

* **Đề bài:** Viết ra giấy (hoặc gõ) lệnh kiểm tra phiên bản của **cả Python và pip** — tức 2 lệnh riêng.
* **Input:** 2 lệnh `python --version` và `python -m pip --version`.
* **Output:** 2 dòng kết quả.
* **Gợi ý:** Lệnh `python -m pip` đảm bảo dùng pip của đúng phiên bản Python.

### Bài 11: Gợi ý lệnh trong REPL

* **Đề bài:** Trong REPL, gõ `5 +` rồi nhấn Tab. Mô tả những gì xảy ra.
* **Input:** Gõ `5 +` + Tab trong REPL.
* **Output:** Python liệt kê các phương thức mà đối tượng số hỗ trợ.
* **Gợi ý:** Đây là tính năng **autocomplete** — gõ thử để trải nghiệm.

### Bài 12: Xem tài liệu của hàm print

* **Đề bài:** Trong REPL, gõ `help(print)` và quan sát.
* **Input:** Gõ `help(print)` trong REPL, sau đó gõ `q` để thoát.
* **Output:** Tài liệu mô tả chức năng của hàm `print`.
* **Gợi ý:** `help()` là công cụ xem tài liệu ngay trong Python.

### Bài 13: Sửa lỗi "not recognized"

* **Đề bài:** Bạn mở Command Prompt mới nhưng gõ `python` vẫn báo lỗi. Ghi ra **3 lý do có thể** và cách kiểm tra từng lý do.
* **Input:** Không có.
* **Output:** Liệt kê đủ 3 lý do + cách kiểm tra.
* **Gợi ý:** Nhớ lại: PATH, App execution aliases, cửa sổ chưa mở lại.

### Bài 14: Chạy nhiều file trong cùng một ngày

* **Đề bài:** Tạo thêm file `chao.py` in ra `Chao ban den voi Python`. Chạy lần lượt cả `hello.py` và `chao.py` trong cùng một phiên dòng lệnh.
* **Input:** 2 lệnh chạy file.
* **Output:** Kết quả của cả 2 file.
* **Gợi ý:** Hai lệnh gõ liên tiếp, cùng thư mục.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Tạo báo cáo cấu hình máy (script tự viết)

* **Đề bài:** Trong REPL, lần lượt gõ `import sys`, rồi gõ `sys.version` để xem thông tin phiên bản chi tiết. Viết lại kết quả nhận được.
* **Input:**
  ```python
  import sys
  sys.version
  ```
* **Output:** Một đoạn mô tả chi tiết phiên bản Python.
* **Gợi ý:** `sys` là module hệ thống đi kèm Python.

### Bài 16: Vòng tránh lỗi khi cài đặt

* **Đề bài:** Một bạn mới cài Python quên "Add to PATH". Viết ra **danh sách 4 bước sửa lỗi** bằng cách chỉnh biến môi trường `Path`.
* **Input:** Không có.
* **Output:** Danh sách đủ 4 bước.
* **Gợi ý:** Environment Variables → System variables → Path → Edit.

### Bài 17: Chạy chương trình với đối số dòng lệnh

* **Đề bài:** Tạo file `tinhtuoi.py` tính hiệu số giữa năm 2030 và năm sinh 2010, in kết quả ra màn hình, rồi chạy file đó.
* **Input:** Lệnh `python tinhtuoi.py`.
* **Output:**
  ```
  Nam 2030 ban se 20 tuoi
  ```
* **Gợi ý:** Dùng phép tính `2030 - 2010` trong lệnh `print()`.

### Bài 18: Kiểm tra phiên bản bị trùng

* **Đề bài:** Máy bạn có 2 phiên bản Python. Gõ `where python` để xem danh sách, rồi viết ra **cách xác định phiên bản nào được ưu tiên chạy**.
* **Input:** Lệnh `where python`.
* **Output:** Danh sách đường dẫn + giải thích ngắn (mục nào xuất hiện trước được ưu tiên).
* **Gợi ý:** Thứ tự trong PATH quyết định thứ tự ưu tiên.

### Bài 19: Tạo menu chạy thử

* **Đề bài:** Viết file `thuc_hanh.py` gồm 4 lệnh in ra: `1) Chay REPL`, `2) Tao file .py`, `3) Chay file .py`, `4) Xem help`. Chạy file và quan sát.
* **Input:** Lệnh `python thuc_hanh.py`.
* **Output:** 4 dòng chữ như trên.
* **Gợi ý:** Bốn lệnh `print()`.

### Bài 20: Tự kiểm tra toàn bộ kiến thức

* **Đề bài:** Viết ra một **bảng kiểm tra (checklist)** gồm 6 mục sau, mỗi mục đánh dấu ✔️ nếu bạn làm được: (1) `python --version` ra số; (2) pip hoạt động; (3) REPL in chữ; (4) tạo file `.py`; (5) chạy file `.py`; (6) di chuyển thư mục bằng `cd`.
* **Input:** Không có.
* **Output:** Checklist 6 mục với dấu ✔️.
* **Gợi ý:** Nếu thiếu mục nào, hãy làm lại đúng phần đó trước khi sang bài 3.

---

## 🎯 Tổng kết sau khi làm bài

* ✅ Kiểm tra được Python và pip đã cài đúng.
* ✅ Thao tác thành thạo REPL và chạy file `.py`.
* ✅ Tự sửa được lỗi PATH phổ biến.
* ✅ Sẵn sàng sử dụng công cụ viết code chuyên nghiệp.

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 3: VSCode](../03_VSCode/bai_giang.md)**