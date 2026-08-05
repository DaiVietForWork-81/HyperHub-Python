# ✅ Bài 2: Đáp Án – Cài Đặt Python

> 💡 **Lưu ý:** Các bài ở chương này chủ yếu là **thao tác máy** — đáp án dưới đây mô tả đầy đủ lệnh và kết quả mong đợi.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Kiểm tra Python đã cài chưa

**Phân tích:** Cách nhanh nhất để biết Python có hoạt động là gõ lệnh kiểm tra phiên bản.

**Ý tưởng:** Dùng lệnh `python --version`.

**Thuật toán:**
1. Mở Command Prompt.
2. Gõ lệnh kiểm tra.

**Code:**

```bash
python --version
```

**Kết quả mong đợi:**

```
Python 3.14.2
```

**Giải thích code:**
* `python` — gọi chương trình Python đã cài.
* `--version` — yêu cầu Python in số phiên bản ra màn hình.
* Nếu báo `'python' is not recognized`, xem lại phần PATH (bài giảng).

**Độ phức tạp:** O(1).

---

### Bài 2: Kiểm tra thư mục chứa Python

**Phân tích:** Cần biết máy đang dùng file `python.exe` ở đâu.

**Ý tưởng:** Lệnh `where` trả về đường dẫn tuyệt đối của chương trình.

**Thuật toán:**
1. Gõ lệnh `where python`.
2. Đọc đường dẫn trả về.

**Code:**

```bash
where python
```

**Kết quả mong đợi (ví dụ):**

```
C:\Users\An\AppData\Local\Programs\Python\Python314\python.exe
```

**Giải thích code:**
* `where` — lệnh Windows tìm vị trí chương trình.
* Kết quả cho biết Python nằm trong thư mục `...\Programs\Python\Python314\`.

**Độ phức tạp:** O(1).

---

### Bài 3: Kiểm tra pip

**Phân tích:** Pip cần hoạt động vì hầu hết thư viện sẽ cài qua pip ở các bài sau.

**Ý tưởng:** Gọi pip thông qua Python để chắc chắn dùng đúng phiên bản.

**Thuật toán:**
1. Chạy `python -m pip --version`.

**Code:**

```bash
python -m pip --version
```

**Kết quả mong đợi:**

```
pip 26.1.2 from C:\Python314\Lib\site-packages\pip (python 3.14)
```

**Giải thích code:**
* `-m` — chạy pip như một module của Python.
* Biết dùng `python -m pip` thay vì gõ `pip` trực tiếp để tránh lệnh nhầm phiên bản.

**Độ phức tạp:** O(1).

---

### Bài 4: Vào chế độ tương tác

**Phân tích:** REPL cho phép gõ lệnh và xem kết quả tức thì.

**Ý tưởng:** Gõ lệnh `python` để vào REPL, rồi gõ `print(...)`.

**Code:**

```bash
python
```

```python
>>> print("Chao mung")
Chao mung
>>> exit()
```

**Giải thích code:**
* `python` — mở trình phiên dịch tương tác, dấu nhắc đổi thành `>>>`.
* `print("Chao mung")` — in ngay dòng chữ.
* `exit()` — thoát khỏi REPL.

**Độ phức tạp:** O(1).

---

### Bài 5: Tính toán trong REPL

**Phân tích:** REPL như chiếc máy tính cầm tay — gõ phép tính và Enter ngay kết quả.

**Ý tưởng:** Gõ trực tiếp biểu thức.

**Code:**

```python
>>> 15 * 4
60
>>> 100 // 7
14
```

**Giải thích code:**
* `*` — phép nhân: `15 * 4 = 60`.
* `//` — chia lấy phần nguyên: `100 // 7 = 14` (100 chia 7 được 14 dư 2).

**Độ phức tạp:** O(1).

---

### Bài 6: Tạo file đầu tiên

**Phân tích:** Viết chương trình bằng file giúp lưu trữ và chạy lại nhiều lần.

**Ý tưởng:** Dùng Notepad tạo `hello.py` với 2 lệnh `print()`.

**Code:**

```python
print("Ten toi la An")
print("Toi 15 tuoi")
```

**Kết quả khi chạy:**

```
Ten toi la An
Toi 15 tuoi
```

**Giải thích code:**
* File phải có phần mở rộng `.py`.
* Dấu nháy thẳng `"` — nếu dùng nháy cong sẽ báo `SyntaxError`.

**Độ phức tạp:** O(1).

---

### Bài 7: Chạy file hello.py

**Phân tích:** Lệnh chạy file là nền tảng cho toàn bộ khóa học.

**Ý tưởng:** Di chuyển đúng thư mục rồi gọi `python ten_file.py`.

**Code:**

```bash
cd D:\hoc_python
python hello.py
```

**Kết quả:**
```
Ten toi la An
Toi 15 tuoi
```

**Giải thích code:**
* `cd D:\hoc_python` — di chuyển tới thư mục chứa file.
* `python hello.py` — Python đọc file, chạy từng dòng rồi in ra.

**Độ phức tạp:** O(n) với n là số dòng trong file.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Di chuyển thư mục trong dòng lệnh

**Phân tích:** Hầu hết file sẽ nằm trong thư mục chứ không ở màn hình Command Prompt.

**Ý tưởng:** Dùng `cd` để vào đúng thư mục trước khi chạy.

**Code:**

```bash
cd D:\hoc_python
python hello.py
```

**Giải thích code:**
* `cd` (change directory) — đổi thư mục hiện tại.
* Sau khi vào đúng thư mục, lệnh `python hello.py` hoạt động vì đã tìm thấy file.

**Độ phức tạp:** O(1).

---

### Bài 9: Xem danh sách file trong thư mục

**Phân tích:** Muốn biết trong thư mục hiện tại có những file nào thì dùng `dir`.

**Code:**

```bash
dir
```

**Kết quả mong đợi (ví dụ):**

```
Directory of D:\hoc_python

hello.py            chao.py          ...
```

**Giải thích code:**
* `dir` — liệt kê file trong thư mục hiện tại (Windows).
* Trên macOS/Linux dùng `ls`.

**Độ phức tạp:** O(n) với n là số file.

---

### Bài 10: Kiểm tra cả python và pip cùng lúc

**Phân tích:** Khi nghi ngờ cấu hình máy, kiểm tra cả hai.

**Ý tưởng:** Chạy 2 lệnh liên tiếp.

**Code:**

```bash
python --version
python -m pip --version
```

**Kết quả mong đợi:**

```
Python 3.14.2
pip 26.1.2 ...
```

**Giải thích code:** cả hai lệnh đều dùng đối số `--version` để in phiên bản tương ứng.

**Độ phức tạp:** O(1).

---

### Bài 11: Gợi ý lệnh trong REPL

**Phân tích:** REPL hỗ trợ gõ Tab để gợi ý phương thức.

**Code:**

```python
>>> 5 +
       +  add  bitwise AND  ...  (danh sách phương thức hiện ra)
```

**Giải thích code:**
* Nhấn Tab sau toán tử sẽ mở bảng gợi ý **autocomplete**.
* Đây là tính năng khám phá thư viện cực hữu ích cho người mới.

---

### Bài 12: Xem tài liệu của hàm print

**Phân tích:** Python có tài liệu ngay trong máy — không cần internet.

**Code:**

```python
>>> help(print)
```

**Kết quả:** Màn hình hiện tài liệu mô tả `print(*args, sep=' ', end='\n')...`

**Giải thích code:**
* `help(đối tượng)` — hiển thị docstring của đối tượng.
* Nhấn `q` để thoát khỏi màn hình help.

---

### Bài 13: Sửa lỗi "not recognized"

**Thao tác:** Sửa biến môi trường PAT.

**Các bước:**

1. Mở Menu Start → gõ **"path"** → chọn **Edit the system environment variables**.
2. Bấm **Environment Variables**.
3. Tìm biến `Path` trong **System variables** → **Edit**.
4. Nhấn **New** và dán đường dẫn thư mục chứa `python.exe`.
5. Nhấn OK và **đóng/mở lại** Command Prompt.

**Các lý do kiểm tra:**
* PATH chưa có Python.
* Window App execution aliases đang ưu tiên store.
* Cửa sổ dòng lệnh chưa được mở lại sau khi sửa PATH.

---

### Bài 14: Chạy nhiều file trong cùng một ngày

**Ý tưởng:** Mở Command Prompt một lần, chạy lần lượt nhiều file.

**Code:**

```bash
python hello.py
python chao.py
```

**Kết quả mong đợi:**

```
Ten toi la An
Toi 15 tuoi
Chao ban den voi Python
```

**Giải thích code:** mỗi lệnh là một lần khởi động Python riêng phan — không cần thoát giữa chừng.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Tạo báo cáo cấu hình máy

**Ý tưởng:** Dùng module `sys` đi kèm Python để có thông tin chi tiết.

**Code:**

```python
import sys
sys.version
```

Kết quả dạng: `'3.14.2 (tags/v3.14.2:...)[MSC v.1940 64 bit (AMD64)]'`

**Giải thích code:**
* `import sys` — nạp module hệ thống.
* `sys.version` — chuỗi mô tả chi tiết phiên bản và thông tin trình dịch..

---

### Bài 16: Vòng tránh lỗi khi cài đặt

**Quy trình sửa:**

1. Bấm Start → gõ "path".
2. Chọn **Edit the system environment variables**.
3. Trong **System variables** chọn `Path` → **Edit**.
4. Nhấn **New**, dán đường dẫn `python.exe`, bấm OK.

---

### Bài 17: Chạy chương trình với đối số dòng lệnh

**Code file `tinhtuoi.py`:**

```python
# Tính tuổi vào năm 2030
tuoi = 2030 - 2010
print("Nam 2030 ban se", tuoi, "tuoi")
```

**Cách chạy:**

```bash
python tinhtuoi.py
```

**Kết quả:**

```
Nam 2030 ban se 20 tuoi
```

**Giải thích code:**
* `2030 - 2010` → `20`, lưu vào biến `tuoi`.
* `print("...", tuoi, "tuoi")` — in kết hợp chữ và số.

---

### Bài 18: Kiểm tra phiên bản bị trùng

**Thao tác:**

```bash
where python
```

**Kết quả (ví dụ 2 dòng):**

```
C:\Program Files\Python312\python.exe
C:\Users\An\AppData\Local\...\Python313\python.exe
```

**Giải thích:**
* Danh sách trên → xuống: mục đầu tiên được dùng trước.
* Nếu disable bản không mong muốn, đổi thứ tự `Path` hoặc xóa bản cũ.

---

### Bài 19: Tạo menu chạy thử

**Code:**

```python
print("1) Chay REPL")
print("2) Tao file .py")
print("3) Chay file .py")
print("4) Xem help")
```

**Kết quả khi chạy `python thuc_hanh.py` như đề bài.**

---

### Bài 20: Tự kiểm tra toàn bộ

**Checklist mẫu:**

- [x] `python --version` → ra số phiên bản
- [x] `python -m pip --version` → pip hoạt động
- [x] REPL in được chữ
- [x] Tạo được file `.py`
- [x] Chạy được file `.py`
- [ ] Di chuyển thư mục bằng `cd`

**Giải thích:** nếu mục nào chưa tick, quay lại làm đúng phần đó rồi mới chuyển sang bài 3.

---

## 📌 Lời khuyên cuối

* Luôn luôn nhớ lệnh `python ten_file.py` — sẽ dùng suốt khóa học.
* Ghi nhớ cách sửa PATH — lỗi kinh điển của người mới.
* Đừng lo nếu thấy nhiều lệnh mới: chúng sẽ lặp lại và bạn sớm nhớ thôi!

👉 Tiếp theo: **[Bài 3: Visual Studio Code](../03_VSCode/bai_giang.md)**