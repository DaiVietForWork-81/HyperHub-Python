# 📝 Bài 3: Bài Tập – Visual Studio Code

> 🎯 **Chủ đề:** Cài đặt VSCode, cài Extension Python, tạo file, chạy chương trình.

---

## 📌 Hướng dẫn

* Các bài tập chủ yếu là **thao tác thực hành trên VSCode**.
* Hoàn thành từng bước rồi ghi nhận kết quả.
* Đáp án chi tiết: 👉 [xem file dap_an.md](dap_an.md)

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Cài đặt VSCode

* **Đề bài:** Tải và cài Visual Studio Code từ trang chính thức.
* **Input:** 🖱️ Thực hành cài đặt tại máy.
* **Output:** Biểu tượng VSCode xuất hiện trên Desktop / Start Menu.
* **Gợi ý:** Vào https://code.visualstudio.com/download → Download for Windows.

### Bài 2: Mở VSCode và tạo thư mục học tập

* **Đề bài:** Dùng VSCode tạo thư mục `HocPython`, sau đó mở thư mục này bằng Open Folder.
* **Input:** 🖱️ Trong VSCode: File → Open Folder → tạo mới `HocPython`.
* **Output:** Explorer hiển thị thư mục `HocPython` rỗng ở phía trái.
* **Gợi ý:** Nhớ nguyên tắc **mở thư mục, không mở file lẻ**.

### Bài 3: Cài Extension Python

* **Đề bài:** Cài Extension Python (publisher Microsoft) trong VSCode.
* **Input:** `Ctrl + Shift + X` → gõ `Python` → Install.
* **Output:** Extension Python xuất hiện trong danh sách Installed.
* **Gợi ý:** Nhận diện bản chuẩn bằng tên publisher **Microsoft**.

### Bài 4: Tạo file hello_vscode.py

* **Đề bài:** Tạo file `hello_vscode.py` trong thư mục đang mở, ghi dòng `Chao ban den voi VSCode`.
* **Input:** Tạo file mới (`Ctrl + N`), lưu bằng `Ctrl + S`, đặt tên đuôi `.py`.
* **Output:** File nằm trong **Explorer** (thanh bên trái).
* **Gợi ý:** File phải có đuôi `.py` mới kích hoạt hỗ trợ Python.

### Bài 5: Chạy chương trình bằng nút Run

* **Đề bài:** Chạy `hello_vscode.py` bằng nút ▶️ **Run Python File**.
* **Input:** Giữ tab `hello_vscode.py` → bấm nút Run.
* **Output:** Dòng `Chao ban den voi VSCode` hiện trong **Terminal** phía dưới.
* **Gợi ý:** Nếu không thấy nút Run, kiểm tra đã cài Extension Python chưa.

### Bài 6: Mở Terminal và chạy bằng lệnh

* **Đề bài:** Mở Terminal trong VSCode và chạy file bằng lệnh `python`.
* **Input:** `Ctrl + ~` → gõ `python hello_vscode.py`.
* **Output:** Kết quả in ra giống khi bấm nút Run.
* **Gợi ý:** Dùng phím mũi tên ↑ để gọi lại lệnh cũ.

### Bài 7: Lưu file nhanh

* **Đề bài:** Sửa nội dung `hello_vscode.py` thành in thêm dòng thứ 2 `Chuc ban hoc tot nhe!` và lưu bằng shortcut.
* **Input:** Sửa code → `Ctrl + S`.
* **Output:** Dấu chấm tròn trên tab không còn (báo hiệu đã lưu).
* **Gợi ý:** Ghi nhớ `Ctrl + S` — phím tắt quan trọng nhất của lập trình viên.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Tạo menu thực hành

* **Đề bài:** Tạo file `menu.py` in ra 3 dòng: `1. Xem bai giang`, `2. Lam bai tap`, `3. Xem dap an`. Chạy thử.
* **Input:** Code 3 lệnh `print()`.
* **Output:**
  ```
  1. Xem bai giang
  2. Lam bai tap
  3. Xem dap an
  ```
* **Gợi ý:** Mỗi dòng là một `print()`.

### Bài 9: Bật Auto Save

* **Đề bài:** Bật tính năng Auto Save bằng Command Palette.
* **Input:** `Ctrl + Shift + P` → gõ `auto save` → chọn bật.
* **Output:** Thanh trạng thái hiển thị trạng thái Auto Save đã bật.
* **Gợi ý:** Command Palette cho phép gõ tìm lệnh mà không cần tìm trong menu.

### Bài 10: Tìm lỗi bằng gạch chân đỏ

* **Đề bài:** Viết một dòng code sai (ví dụ thiếu dấu nháy) để xem VSCode gợi ý lỗi. Ghi lại dòng code sai và dòng sửa đúng.
* **Input:** Gõ `print("Thieu nhay)` → quan sát.
* **Output:** Ghi lại 2 dòng: sai và đúng.
* **Gợi ý:** VSCode **gạch chân sóng đỏ** ở chỗ lỗi cú pháp.

### Bài 11: Chọn Interpreter đúng

* **Điều kiện trước:** Đang mở file `.py`.
* **Đề bài:** Chọn đúng bản Python đã cài cho VSCode.
* **Input:** `Ctrl + Shift + P` → `Python: Select Interpreter`.
* **Output:** Góc dưới cửa sổ hiển thị tên phiên bản Python.
* **Gợi ý:** Chọn phiên bản trùng với kết quả `python --version` (bài 2).

### Bài 12: Hai file, hai lần chạy

* **Đề bài:** Tạo thêm `tinh.py` in ra phép nhân `25 * 4 = 100` (dùng phép nhân của Python). Chạy cả 2 file bằng lệnh Terminal.
* **Input:** `python hello_vscode.py` rồi `python tinh.py`.
* **Output:** Kết quả 2 chương trình hiện ở 2 dòng liên tiếp.
* **Gợi ý:** `print("25 x 4 =", 25 * 4)`.

### Bài 13: So sánh nhanh

* **Đề bài:** Viết bảng so sánh giữa Notepad và VSCode với 5 tiêu chí đã học: tô màu cú pháp, gợi ý code, chạy code, sửa lỗi, giá tiền.
* **Input:** Không có.
* **Output:** Bảng so sánh đầy đủ 5 tiêu chí.
* **Gợi ý:** Tham khảo bảng "So sánh nhanh" trong bài giảng.

### Bài 14: Sửa lỗi thiếu dấu ngoặc

* **Đề bài:** Chương trình sau bị lỗi, hãy sửa để chạy được:
  ```python
  print"Thieu dau ngoac"
  ```
* **Output mong đợi:**
  ```
  Thieu dau ngoac
  ```
* **Gợi ý:** `print` cần cặp dấu ngoặc tròn `( )`.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Bảng cửu chương trong VSCode

* **Đề bài:** Tạo file `bang_cuu_chuong.py` in ra các phép nhân từ `7 x 1 = 7` đến `7 x 5 = 35` (mỗi dòng một phép). Chạy file.
* **Input:** Code 5 dòng `print()`.
* **Output:**
  ```
  7 x 1 = 7
  7 x 2 = 14
  7 x 3 = 21
  7 x 4 = 28
  7 x 5 = 35
  ```
* **Gợi ý:** Mỗi dòng chứa phép tính `7 * k`.

### Bài 16: Tính trung bình cộng

* **Đề bài:** Tạo file `diem.py` in ra trung bình cộng của 3 môn (tự chọn 3 điểm), làm tròn 2 chữ số thập phân.
* **Input:** Code với 3 biến số và `print()`.
* **Output:**
  ```
  Diem trung binh: 8.0
  ```
* **Gợi ý:** `round((a + b + c) / 3, 2)`.

### Bài 17: Vẽ tam giác trong file

* **Đề bài:** Tạo `tamgiac.py` vẽ tam giác 5 tầng bằng dấu `*`, chạy bằng cả nút ▶️ và Terminal. Ghi nhận: kết quả hai cách giống nhau.
* **Input:** Code 5 lệnh `print()`.
* **Output:**
  ```
  *
  **
  ***
  ****
  *****
  ```
* **Gợi ý:** Đã từng vẽ 3 tầng ở bài 1 — tăng lên 5 tầng.

### Bài 18: Vẽ bản đồ game 3x3

* **Đề bài:** Tạo file `ban_do.py` vẽ một "bản đồ" 3x3 bằng dấu `.` (3 hàng, mỗi hàng 3 dấu).
* **Input:** 3 lệnh `print()`.
* **Output:**
  ```
  ...
  ...
  ...
  ```
* **Gợi ý:** Mỗi hàng là 3 dấu `.` liền nhau.

### Bài 19: Chạy nhiều file một dòng lệnh

* **Đề bài:** Tạo ba file: `a.py` in `A`, `b.py` in `B`, `c.py` in `C`. Chạy cả ba bằng một dòng lệnh nối nhau bằng `&&` trong Terminal.
* **Input:**
  ```
  python a.py && python b.py && python c.py
  ```
* **Output:**
  ```
  A
  B
  C
  ```
* **Gợi ý:** Ký tự `&&` chạy lệnh tiếp theo khi lệnh trước đó thành công.

### Bài 20: Tự kiểm tra tổng hợp

* **Đề bài:** Viết ra **checklist 10 mục** kiểm tra mức độ sẵn sàng, đánh dấu ✔️ hoặc ❌ cho từng mục:
  1. VSCode đã cài đặt và mở được.
  2. Đã mở đúng thư mục `HocPython`.
  3. Extension Python (Microsoft) đã cài.
  4. Tạo được file `.py`.
  5. Chạy được code bằng nút ▶️.
  6. Chạy được code bằng Terminal.
  7. Đã bật Auto Save.
  8. Đã chọn đúng Interpreter.
  9. Tự sửa được ít nhất 1 lỗi cú pháp.
  10. Đã chạy thử ít nhất 2 chương trình khác nhau.
* **Gợi ý:** Mục nào chưa ✔️ thì quay lại làm đúng phần đó trước khi sang bài 4.

---

## 🎯 Tổng kết sau khi làm bài

* ✅ Cài và làm chủ VSCode cho Python.
* ✅ Chạy code bằng nút Run và Terminal.
* ✅ Dùng Command Palette, Auto Save, Select Interpreter.
* ✅ Sẵn sàng bước vào **Bài 4 – Biến** để khởi đầu lập trình thực thụ.

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 4: Biến trong Python](../04_Bien/bai_giang.md)**