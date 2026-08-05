# ✅ Bài 3: Đáp Án – Visual Studio Code

> 💡 **Lưu ý:** Đây là các bài thực hành — đáp án mô tả đầy đủ thao tác và kết quả mong đợi.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Cài đặt VSCode

**Phân tích:** Cài phần mềm miễn phí, chính thức từ trang chủ.

**Các bước:**

1. Mở trình duyệt → https://code.visualstudio.com/download
2. Bấm **Download for Windows** (hoặc đúng hệ điều hành).
3. Mở file cài đặt → chọn **I accept the agreement** → **Next** → **Install**.
4. Bấm **Finish** — VSCode tự mở.

**Kiểm tra:** Biểu tượng VSCode xuất hiện trên Desktop / Start Menu. ✅

---

### Bài 2: Mở VSCode và tạo thư mục học tập

**Các bước:**

1. Mở VSCode.
2. Menu **File → Open Folder** (`Ctrl + K, Ctrl + O`).
3. Trong hộp thoại, tạo thư mục mới tên `HocPython` (nút New Folder).
4. Chọn `HocPython` → **Select Folder**.

**Kiểm tra:** Thanh **Explorer** bên trái hiển thị thư mục rỗng. ✅

> 📌 Nhớ: luôn **mở thư mục**, không mở file lẻ.

---

### Bài 3: Cài Extension Python

**Các bước:**

1. Nhấn `Ctrl + Shift + X` → mở Extensions.
2. Gõ `Python` vào ô tìm kiếm.
3. Chọn gói **Python** của **Microsoft** (có hàng trăm triệu lượt cài).
4. Bấm **Install**, đợi hoàn tất.

**Kiểm tra:** Mục **Installed** trong Extensions có tên Python. ✅

---

### Bài 4: Tạo file hello_vscode.py

**Các bước:**

1. Bấm biểu tượng **New File** (hoặc `Ctrl + N`).
2. Gõ nội dung:

```python
print("Chao ban den voi VSCode")
```

3. `Ctrl + S` → đặt tên `hello_vscode.py` → Save.

**Kiểm tra:** File xuất hiện trong Explorer, code tự **tô màu** (nhờ đuôi `.py`). ✅

---

### Bài 5: Chạy chương trình bằng nút Run

**Các bước:**

1. Chắc chắn tab `hello_vscode.py` đang mở.
2. Bấm nút ▶️ **Run Python File** ở góc phải trên cửa sổ.

**Kết quả:** Terminal phía dưới hiện:

```
Chao ban den voi VSCode
```

> ⚠️ Không thấy nút ▶️? → Chưa cài Extension Python (làm lại bài 3).

---

### Bài 6: Mở Terminal và chạy bằng lệnh

**Các bước:**

1. Nhấn `` Ctrl + ` `` để mở Terminal.
2. Gõ lệnh:

```bash
python hello_vscode.py
```

**Kết quả:** Giống hệt khi bấm nút Run.

```
Chao ban den voi VSCode
```

> 💡 Phím **↑** gọi lại lệnh cũ — gõ nhanh hơn.

---

### Bài 7: Lưu file nhanh

**Các bước:**

1. Sửa file thành:

```python
print("Chao ban den voi VSCode")
print("Chuc ban hoc tot nhe!")
```

2. Nhấn `Ctrl + S`.

**Kiểm tra:** Dấu chấm tròn màu trắng trên tab biến mất → đã lưu. ✅

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Tạo menu thực hành

**Code `menu.py`:**

```python
print("1. Xem bai giang")
print("2. Lam bai tap")
print("3. Xem dap an")
```

**Kết quả khi chạy:**

```
1. Xem bai giang
2. Lam bai tap
3. Xem dap an
```

**Giải thích:** Ba lệnh `print()` tuần tự in 3 dòng menu; mỗi lệnh tự động xuống dòng.

---

### Bài 9: Bật Auto Save

**Các bước:**

1. Nhấn `Ctrl + Shift + P` → Command Palette.
2. Gõ `auto save`.
3. Chọn **File: Toggle Auto Save**.

**Kiểm tra:** Gõ thử 1 ký tự rồi dừng 1–2 giây — dấu tròn trên tab biến mất tự động. ✅

---

### Bài 10: Tìm lỗi bằng gạch chân đỏ

**Dòng sai:**

```python
print("Thieu nhay)
```

**Dòng đúng:**

```python
print("Thieu nhay")
```

**Giải thích:** Dòng sai thiếu dấu nháy đóng — VSCode gạch chân đỏ ở cuối chuỗi. Cần cặp nháy `" "` bao trọn chuỗi.

---

### Bài 11: Chọn Interpreter đúng

**Các bước:**

1. Mở file `.py`.
2. `Ctrl + Shift + P` → gõ `Python: Select Interpreter`.
3. Chọn phiên bản Python trùng với `python --version` đã kiểm tra ở bài 2.

**Kiểm tra:** Góc dưới trái hiện tên phiên bản (ví dụ `Python 3.14.2 64-bit`). ✅

---

### Bài 12: Hai file, hai lần chạy

**Code `tinh.py`:**

```python
print("25 x 4 =", 25 * 4)
```

**Chạy trong Terminal:**

```bash
python hello_vscode.py
python tinh.py
```

**Kết quả:**

```
Chao ban den voi VSCode
Chuc ban hoc tot nhe!
25 x 4 = 100
```

**Giải thích:** `25 * 4` — Python tính ra `100` rồi in kèm sau nhãn.

---

### Bài 13: So sánh nhanh

| Tiêu chí | Notepad | VSCode |
|---|---|---|
| Tô màu cú pháp | ❌ | ✅ |
| Gợi ý code (IntelliSense) | ❌ | ✅ |
| Chạy code | ❌ | ✅ |
| Sửa lỗi (debug) | ❌ | ✅ |
| Giá tiền | Miễn phí | Miễn phí |

**Kết luận:** VSCode vượt trội hoàn toàn cho việc học lập trình.

---

### Bài 14: Sửa lỗi thiếu dấu ngoặc

**Code sai:**

```python
print"Thieu dau ngoac"
```

**Code đúng:**

```python
print("Thieu dau ngoac")
```

**Giải thích:** Hàm `print` luôn cần cặp dấu ngoặc tròn chứa đối số. Thiếu dấu ngoặc → `SyntaxError`.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Bảng cửu chương trong VSCode

**Code `bang_cuu_chuong.py`:**

```python
print("7 x 1 =", 7 * 1)
print("7 x 2 =", 7 * 2)
print("7 x 3 =", 7 * 3)
print("7 x 4 =", 7 * 4)
print("7 x 5 =", 7 * 5)
```

**Kết quả:**

```
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
```

**Giải thích:** Mỗi dòng in nhãn `"7 x k ="` rồi Python tính `7 * k`. Dấu `*` là phép nhân.

---

### Bài 16: Tính trung bình cộng

**Code `diem.py`:**

```python
# Điểm ba môn
toan = 8
van = 7
anh = 9
# Trung bình cộng, làm tròn 2 chữ số
trung_binh = round((toan + van + anh) / 3, 2)
print("Diem trung binh:", trung_binh)
```

**Kết quả:**

```
Diem trung binh: 8.0
```

**Giải thích code:**
* `(8 + 7 + 9) / 3 = 8.0` — phép chia `/` trả về số thực.
* `round(..., 2)` giữ 2 chữ số sau dấu phẩy.
* Biến giúp code gọn, dễ thay điểm số.

---

### Bài 17: Vẽ tam giác trong file

**Code `tamgiac.py`:**

```python
print("*")
print("**")
print("***")
print("****")
print("*****")
```

**Kết quả:**

```
*
**
***
****
*****
```

**Ghi nhận:** Cách chạy bằng nút ▶️ và bằng Terminal cho **kết quả giống hệt nhau** — chỉ khác cách bấm.

---

### Bài 18: Vẽ bản đồ game 3x3

**Code `ban_do.py`:**

```python
print("...")
print("...")
print("...")
```

**Kết quả:**

```
...
...
...
```

**Giải thích:** Ba hàng giống nhau tạo lưới 3x3 — mô hình ban đầu cho trò chơi (cờ, mê cung...) sẽ học sau.

---

### Bài 19: Chạy nhiều file một dòng lệnh

**Code các file:**

* `a.py`: `print("A")`
* `b.py`: `print("B")`
* `c.py`: `print("C")`

**Lệnh chạy:**

```bash
python a.py && python b.py && python c.py
```

**Kết quả:**

```
A
B
C
```

**Giải thích:** `&&` chạy lệnh sau chỉ khi lệnh trước **thành công** — hữu ích khi cần chạy chuỗi công việc.

---

### Bài 20: Tự kiểm tra tổng hợp

**Checklist mẫu (tick ✔️ nếu làm được):**

- [x] VSCode đã cài đặt và mở được.
- [x] Đã mở đúng thư mục `HocPython`.
- [x] Extension Python (Microsoft) đã cài.
- [x] Tạo được file `.py`.
- [x] Chạy được code bằng nút ▶️.
- [x] Chạy được code bằng Terminal.
- [x] Đã bật Auto Save.
- [x] Đã chọn đúng Interpreter.
- [x] Tự sửa được ít nhất 1 lỗi cú pháp.
- [x] Đã chạy thử ít nhất 2 chương trình khác nhau.

> Nếu còn mục ❌ — quay lại ôn phần đó. Từ bài sau, mọi kiến thức đều dựa trên công cụ này.

---

## 📌 Lời khuyên cuối

* VSCode sẽ là "nhà" của bạn suốt khóa học — hãy ghi nhớ các phím tắt.
* Luyện chạy code cả 2 cách: nút ▶️ và Terminal.
* Đừng ngại bấm thử: sai lỗi cú pháp chỉ là lỗi gõ — sửa là chạy.

👉 Tiếp theo: **[Bài 4: Biến trong Python](../04_Bien/bai_giang.md)**