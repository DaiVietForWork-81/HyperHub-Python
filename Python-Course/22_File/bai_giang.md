# 💾 Bài 22: Đọc Và Ghi File Trong Python

> 🎓 **Chương 6 – Tổ chức mã nguồn: Module, Package và File**

---

## 🎯 Mục tiêu

Sau bài học này, học viên sẽ:

* ✅ Hiểu **vì sao cần lưu dữ liệu ra file** thay vì chỉ giữ trong bộ nhớ.
* ✅ Sử dụng thành thạo **`open()`** với các mode `r`, `w`, `a` và đối số `encoding='utf-8'`.
* ✅ Đọc file bằng **`read()`**, **`readline()`**, **`readlines()`**.
* ✅ Ghi file bằng **`write()`**, **`writelines()`**.
* ✅ Dùng **`with` statement** để mở file an toàn, tự đóng.
* ✅ **Xử lý lỗi** `FileNotFoundError` khi file không tồn tại.
* ✅ Viết được chương trình **đọc điểm từ file**, **ghi danh sách học sinh**, **lưu nhật ký**.

---

## 📖 Kiến thức

### 1. Nhắc lại Bài 21 — và vấn đề lớn nhất hiện tại

Ở **Bài 21**, dữ liệu (học sinh, điểm số) nằm trong biến, list, dict — tất cả đều **trong bộ nhớ RAM**. Tắt máy là **mất sạch**! Cũng giống như bạn học thuộc lòng thời khóa biểu nhưng không ghi vào sổ — tối nay ngủ dậy là quên.

> 💬 **Nói đơn giản:** File giống **cuốn sổ tay** của chương trình: mọi thứ ghi vào sổ sẽ còn nguyên trên đĩa cứng kể cả khi tắt máy.

### 2. Hàm `open()` — mở "cánh cửa" vào file

Muốn đọc hay ghi file, trước hết phải **mở file** bằng `open()`:

```python
f = open("ten_file.txt", "r", encoding="utf-8")
```

Ba "mảnh ghép" quan trọng:

| Tham số | Ý nghĩa |
|---|---|
| `"ten_file.txt"` | Tên file (nếu muốn đường dẫn thư mục: `"thumuc/ten.txt"`) |
| `"r"` | **Mode** — chế độ mở file |
| `encoding="utf-8"` | Bảng mã ký tự — **bắt buộc có** khi xử lý tiếng Việt |

### 3. Các mode mở file

| Mode | Tên đầy đủ | Tác dụng | File chưa tồn tại |
|---|---|---|---|
| `"r"` | read | Chỉ **đọc** | ❌ Báo lỗi `FileNotFoundError` |
| `"w"` | write | **Ghi đè** từ đầu — dữ liệu cũ bị xóa | ✅ Tự tạo file mới |
| `"a"` | append | **Ghi thêm** vào cuối — giữ dữ liệu cũ | ✅ Tự tạo file mới |
| `"r+"` | read + write | Đọc và ghi (không xóa) | ❌ Báo lỗi nếu chưa có |
| `"w+"` | write + read | Ghi và đọc | ✅ Tự tạo |
| `"a+"` | append + read | Thêm và đọc | ✅ Tự tạo |
| `"x"` | exclusive | Chỉ tạo **file mới**; đã có sẵn thì lỗi | ✅ Tạo mới |

> ⚠️ **Nguy hiểm nhất là mode `"w"`:** nó "quét sạch" nội dung cũ trước khi ghi. Mở nhầm `"w"` khi muốn `"a"` là mất dữ liệu!

### 4. Vòng đời của một file

Mọi thao tác file đều theo 3 bước: **Mở → Xử lý → Đóng** — như mở tủ, lấy đồ, rồi đóng tủ:

```mermaid
flowchart LR
    A[Mở file<br/>open()] --> B[Đọc hoặc ghi<br/>read / write] --> C[Đóng file<br/>close()]
```

```python
# Cách 1: mở rồi phải tự đóng
f = open("nhat_ky.txt", "a", encoding="utf-8")
f.write("Hom nay hoc Python\n")
f.close()   # quên đóng = nguy cơ mất dữ liệu

# Cách 2: dùng with — tự đóng, kể cả khi gặp lỗi (nên dùng!)
with open("nhat_ky.txt", "a", encoding="utf-8") as f:
    f.write("Hom nay hoc Python\n")
```

### 5. `with` statement — "trợ lý" đóng file hộ bạn

```python
with open("hello.txt", "r", encoding="utf-8") as f:
    noi_dung = f.read()
# Ra khỏi khối with, file ĐÃ TỰ ĐÓNG — không cần f.close()
```

**Vì sao `with` là chuẩn mực?**
* ✅ Tự động đóng file dù code chạy xong hay gặp lỗi giữa chừng.
* ✅ Code ngắn gọn, không sợ quên `close()`.
* ✅ Từ nay **mọi ví dụ** của bài này đều dùng `with`.

### 6. Đọc file — 3 "vũ khí" cơ bản

Giả sử file `hoc_sinh.txt` có nội dung:

```
Nguyen Van An,10A1
Tran Thi Mai,10A1
Le Quang Binh,10A2
```

| Hàm | Trả về | Dùng khi |
|---|---|---|
| `f.read()` | **Toàn bộ** nội dung dưới dạng **một chuỗi** | File nhỏ, muốn đọc hết |
| `f.readline()` | **Một dòng** (kèm `\n` ở cuối) | Đọc lần lượt từng dòng |
| `f.readlines()` | **List** các dòng | Muốn duyệt/xử lý từng dòng |

```python
with open("hoc_sinh.txt", "r", encoding="utf-8") as f:
    noi_dung = f.read()          # "Nguyen Van An,10A1\nTran Thi Mai,10A1\n..."
```

> 💡 Cách duyệt phổ biến nhất: `for dong in f:` — Python đọc từng dòng một, tiết kiệm bộ nhớ ngay cả với file cực lớn.

### 7. Ghi file — `write()` và `writelines()`

| Hàm | Ghi gì |
|---|---|
| `f.write(chuoi)` | Ghi **một chuỗi** — không tự thêm `\n`! |
| `f.writelines(list)` | Ghi **một list chuỗi** liền mạch — vẫn phải tự thêm `\n` |

```python
danh_sach = ["Toan\n", "Van\n", "Anh\n"]
with open("mon_hoc.txt", "w", encoding="utf-8") as f:
    f.writelines(danh_sach)
```

> ⚠️ `write` **không tự xuống dòng**: phải tự thêm `"\n"`. Đây là lỗi khiến nhiều người ngạc nhiên nhất!

### 8. `encoding="utf-8"` — bảo bối chống lỗi tiếng Việt

File chỉ lưu được **số nhị phân** — phải có "bảng dịch" (encoding) giữa ký tự và số. Bảng mã mặc định của Windows là `cp1252` — **không chứa** chữ "ă, â, đ, ê..." nên ghi tiếng Việt sẽ báo lỗi:

```
UnicodeEncodeError: 'charmap' codec can't encode character '\u0103'...
```

**Giải pháp:** luôn ghi `encoding="utf-8"` khi mở file:

```python
with open("ghi_chu.txt", "w", encoding="utf-8") as f:
    f.write("Hôm nay học Python rất vui!")   # ✅ không lỗi
```

> 💡 Quy tắc vàng: **mọi lúc mở file có chữ tiếng Việt → kèm `encoding="utf-8"`**, cả khi đọc lẫn khi ghi.

### 9. Xử lý lỗi khi mở file — `FileNotFoundError`

Đọc file **không tồn tại** với mode `"r"` → chương trình sập ngay:

```python
with open("khong_co.txt", "r", encoding="utf-8") as f:   # ❌ FileNotFoundError
    print(f.read())
```

Giải pháp: bọc trong `try/except` (kiến thức **Bài 19**):

```python
try:
    with open("khong_co.txt", "r", encoding="utf-8") as f:
        noi_dung = f.read()
except FileNotFoundError:
    print("File khong ton tai! Hay tao file truoc.")
```

### 10. Cách ổn định khi đọc điểm từ file

File `diem.txt` mỗi dòng một học sinh:

```
Nguyen Van An,8.5,7.0,9.0
Tran Thi Mai,6.0,6.5,7.0
```

Quy trình "chuẩn không cần chỉnh":

```mermaid
flowchart TD
    A[Mở file với with + utf-8] --> B[Duyệt từng dòng bằng for]
    B --> C[dòng.strip bỏ khoảng trắng + xuống dòng]
    C --> D{split theo dấu phẩy]
    D --> E[Chuyển điểm sang float]
    E --> F[Tính trung bình và xử lý]
```

```python
with open("diem.txt", "r", encoding="utf-8") as f:
    for dong in f:
        dong = dong.strip()            # 1) bỏ ký tự xuống dòng
        if not dong:                   # 2) bỏ qua dòng trống
            continue
        phan = dong.split(",")         # 3) tách theo dấu phẩy
        ten = phan[0]
        diem = [float(x) for x in phan[1:]]   # 4) chuyển sang số thực
        tb = sum(diem) / len(diem)
        print(f"{ten}: {tb:.2f}")
```

> 💡 `float(x)` có thể gây `ValueError` nếu dữ liệu lỗi — kết hợp `try/except` (Bài 19) khi dữ liệu không tin cậy.

---

## 💡 Ví dụ minh họa

### Ví dụ 1: Ghi một chuỗi, rồi đọc lại

```python
# Bước 1: ghi file (mode "w" tự tạo file nếu chưa có)
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("Xin chao cac ban!\n")
    f.write("Day la file dau tien cua toi.\n")

# Bước 2: đọc lại toàn bộ
with open("hello.txt", "r", encoding="utf-8") as f:
    noi_dung = f.read()

print(noi_dung)
```

Kết quả:

```
Xin chao cac ban!
Day la file dau tien cua toi.
```

**Giải thích từng dòng:**

| Dòng code | Ý nghĩa |
|---|---|
| `open("hello.txt", "w", encoding="utf-8")` | Mở mode ghi đè; file chưa có thì Python tự tạo |
| `f.write("...\n")` | Ghi một dòng; `\n` chính là ký tự xuống dòng |
| `f.read()` | Đọc toàn bộ nội dung thành chuỗi |
| `with ... as f:` | Tự động đóng file khi thoát khối lệnh |

### Ví dụ 2: Đọc từng dòng bằng `readline()` và vòng lặp

```python
# Tạo file 3 dòng trước
with open("mon_hoc.txt", "w", encoding="utf-8") as f:
    f.writelines(["Toan\n", "Van\n", "Anh\n"])

# Cách A: readline() đọc lần lượt
with open("mon_hoc.txt", "r", encoding="utf-8") as f:
    d1 = f.readline()   # "Toan\n"
    d2 = f.readline()   # "Van\n"
print("2 dong dau:", d1.strip(), "-", d2.strip())

# Cách B: for duyệt từng dòng (được khuyên dùng)
with open("mon_hoc.txt", "r", encoding="utf-8") as f:
    for dong in f:
        print("Mon:", dong.strip())
```

Kết quả:

```
2 dong dau: Toan - Van
Mon: Toan
Mon: Van
Mon: Anh
```

**Giải thích từng dòng:**

| Dòng code | Ý nghĩa |
|---|---|
| `f.readline()` | Đọc đúng 1 dòng, con trỏ nhảy xuống dòng kế |
| `dong.strip()` | Bỏ ký tự xuống dòng `\n` và khoảng trắng thừa |
| `for dong in f` | Duyệt hết file, mỗi lượt gán `dong` = một dòng |

### Ví dụ 3: Ghi danh sách học sinh từ list

```python
# Danh sách học sinh trong chương trình
danh_sach = [
    ("Nguyen Van An", "10A1"),
    ("Tran Thi Mai", "10A1"),
    ("Le Quang Binh", "10A2"),
]

# Ghi toàn bộ vào file
with open("hoc_sinh.txt", "w", encoding="utf-8") as f:
    for ten, lop in danh_sach:
        f.write(f"{ten},{lop}\n")

# Đọc lại và in ra màn hình
with open("hoc_sinh.txt", "r", encoding="utf-8") as f:
    print(f.read())
```

Kết quả:

```
Nguyen Van An,10A1
Tran Thi Mai,10A1
Le Quang Binh,10A2
```

**Giải thích từng dòng:**

| Dòng code | Ý nghĩa |
|---|---|
| `for ten, lop in danh_sach` | Giải nén từng cặp (ten, lop) từ list tuple |
| `f.write(f"{ten},{lop}\n")` | Mỗi học sinh thành một dòng, các cột ngăn bằng dấu phẩy |
| `print(f.read())` | Đọc lại cả file và in — dữ liệu đã "sống" trên đĩa |

---

## 🔬 Ví dụ nâng cao

### Ví dụ 1: Đọc điểm từ file và xếp loại

```python
# File diem.txt: Ten,Toan,Van,Anh
with open("diem.txt", "w", encoding="utf-8") as f:
    f.write("Nguyen Van An,8.5,7.0,9.0\n")
    f.write("Tran Thi Mai,6.0,6.5,7.0\n")
    f.write("Le Quang Binh,4.5,5.0,5.5\n")

with open("diem.txt", "r", encoding="utf-8") as f:
    for dong in f:
        dong = dong.strip()
        if not dong:
            continue
        ten, *diem = dong.split(",")          # ten = cột 1, diem = các cột còn lại
        diem = [float(x) for x in diem]       # chuyển chuỗi -> số thực
        tb = sum(diem) / len(diem)
        loai = "Gioi" if tb >= 8 else "Kha" if tb >= 6.5 else "Trung binh" if tb >= 5 else "Yeu"
        print(f"{ten:<20} TB: {tb:.2f} - {loai}")
```

Kết quả:

```
Nguyen Van An       TB: 8.17 - Gioi
Tran Thi Mai        TB: 6.50 - Kha
Le Quang Binh       TB: 5.00 - Trung binh
```

### Ví dụ 2: Nhật ký (log) đơn giản

Ghi mỗi sự kiện thành một dòng, **mode "a"** giúp không bao giờ xóa log cũ:

```python
from datetime import datetime   # Bài 20: lấy thời gian hiện tại

def ghi_log(thong_diep):
    """Ghi một dòng nhật ký kèm thời gian."""
    thoi_gian = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("nhat_ky.txt", "a", encoding="utf-8") as f:
        f.write(f"[{thoi_gian}] {thong_diep}\n")

# Mô phỏng một phiên làm việc
ghi_log("Chuong trinh khoi dong")
ghi_log("Nguoi dung dang nhap: An")
ghi_log("Chuong trinh ket thuc")
```

Kết quả trong file `nhat_ky.txt`:

```
[2026-08-05 10:15:22] Chuong trinh khoi dong
[2026-08-05 10:15:22] Nguoi dung dang nhap: An
[2026-08-05 10:15:22] Chuong trinh ket thuc
```

### Ví dụ 3: Chương trình quản lý học sinh lưu vào file

```python
# 1) Ghi danh sách học sinh vào file
danh_sach = [
    {"ten": "Nguyen Van An", "lop": "10A1"},
    {"ten": "Tran Thi Mai", "lop": "10A1"},
]
with open("hs.txt", "w", encoding="utf-8") as f:
    for hs in danh_sach:
        f.write(f"{hs['ten']},{hs['lop']}\n")

# 2) Đọc lại từ file vào list dict (dữ liệu "hồi sinh")
hs_doc_lai = []
try:
    with open("hs.txt", "r", encoding="utf-8") as f:
        for dong in f:
            dong = dong.strip()
            if not dong:
                continue
            ten, lop = dong.split(",")
            hs_doc_lai.append({"ten": ten, "lop": lop})
except FileNotFoundError:
    print("File chua ton tai!")

# 3) Hiển thị
for hs in hs_doc_lai:
    print(f"- {hs['ten']} (lop {hs['lop']})")
```

Kết quả:

```
- Nguyen Van An (lop 10A1)
- Tran Thi Mai (lop 10A1)
```

> 💡 Đây chính là **"lưu trữ" thô sơ** — Bài 32 (JSON) và Bài 33 (CSV) sẽ dạy định dạng lưu trữ chuẩn hơn.

---

## ⚠️ Lỗi thường gặp

### Lỗi 1: `FileNotFoundError: [Errno 2] No such file or directory`

```python
with open("diem.txt", "r", encoding="utf-8") as f:   # ❌ file chưa tồn tại
    print(f.read())
```

* **Nguyên nhân:** Mở mode `"r"` với file chưa được tạo.
* **Cách sửa:** Chắc chắn file đã tồn tại; hoặc bọc `try/except FileNotFoundError`; hoặc tạo file trước bằng mode `"w"`.

### Lỗi 2: `UnicodeEncodeError` khi ghi tiếng Việt

```python
with open("ghi_chu.txt", "w") as f:          # ❌ thiếu encoding trên Windows
    f.write("Hôm nay vui quá!")
```

* **Nguyên nhân:** Bảng mã mặc định của Windows (`cp1252`) không chứa chữ có dấu.
* **Cách sửa:** Luôn mở file với `encoding="utf-8"` — cả khi đọc lẫn khi ghi.

### Lỗi 3: Quên `close()` hoặc không dùng `with`

```python
f = open("nhat_ky.txt", "a", encoding="utf-8")
f.write("du lieu")
# ❌ quên f.close() — dữ liệu có thể chưa được ghi ra đĩa
```

* **Nguyên nhân:** Nội dung còn nằm trong "vùng đệm", chưa chắc đã xuống đĩa.
* **Cách sửa:** Dùng `with open(...) as f:` — Python tự đóng và ghi đầy đủ khi thoát khối.

### Lỗi 4: Nhầm `"w"` với `"a"` — mất dữ liệu

```python
with open("diem.txt", "w", encoding="utf-8") as f:   # ❌ xóa sạch dữ liệu cũ!
    f.write("chi co 1 dong moi")
```

* **Nguyên nhân:** `"w"` luôn **quét sạch** file trước khi ghi.
* **Cách sửa:** Muốn **giữ dữ liệu cũ và thêm vào cuối** → dùng `"a"`.

### Lỗi 5: Đọc xong thấy "file trống" dù rõ ràng có nội dung

```python
f = open("hs.txt", "r", encoding="utf-8")
noi_dung = f.read()
noi_dung_2 = f.read()   # ❌ kết quả là chuỗi rỗng
f.close()
```

* **Nguyên nhân:** Sau khi đọc hết, con trỏ đọc nằm ở **cuối file**; đọc tiếp chỉ nhận rỗng.
* **Cách sửa:** Đọc một lần và lưu vào biến, hoặc mở lại file nếu muốn đọc lần hai.

---

## 💎 Mẹo

* 📌 **Công thức chuẩn:** `with open("ten.txt", "r", encoding="utf-8") as f:` — nhớ đủ ba thành phần.
* 🧹 Luôn gọi `.strip()` khi đọc từng dòng để bỏ `\n` và khoảng trắng thừa.
* 📝 Ghi log bằng mode `"a"` để giữ lịch sử; đừng dùng `"w"` cho nhật ký.
* 🛡️ Bọc `open` trong `try/except` khi file có thể không tồn tại (file do người dùng đặt tên).
* 📊 Mỗi dòng file = một bản ghi; các cột ngăn cách bằng dấu phẩy — đơn giản, dễ đọc, dễ xử lý.
* 🔁 Đọc xong muốn đọc lại lần nữa → mở lại file hoặc lưu nội dung vào biến.

---

## 📝 Tóm tắt

| Khái niệm | Nội dung |
|---|---|
| `open(ten, mode, encoding)` | Mở file; `"r"` đọc, `"w"` ghi đè, `"a"` ghi thêm |
| `with open(...) as f` | Mở và tự đóng file an toàn — luôn nên dùng |
| `read()` / `readline()` / `readlines()` | Đọc toàn bộ / một dòng / list các dòng |
| `write()` / `writelines()` | Ghi chuỗi / ghi list chuỗi (nhớ thêm `\n`) |
| `encoding="utf-8"` | Bắt buộc với tiếng Việt để tránh `UnicodeEncodeError` |
| `FileNotFoundError` | Bắt bằng `try/except` khi file có thể chưa tồn tại |
| ⚠️ `"w"` vs `"a"` | `"w"` xóa dữ liệu cũ, `"a"` giữ dữ liệu cũ |

---

## 🧪 Kiểm tra nhanh

1. ❓ Mode nào xóa sạch nội dung file trước khi ghi?
2. ❓ Mode nào cho phép ghi thêm vào cuối file mà không xóa dữ liệu cũ?
3. ❓ Mở file chưa tồn tại với mode `"r"` sẽ gặp lỗi gì?
4. ❓ Vì sao phải dùng `encoding="utf-8"`?
5. ❓ `write()` có tự xuống dòng không?
6. ❓ `readlines()` trả về dữ liệu kiểu gì?
7. ❓ `with open(...) as f` có lợi ích gì nổi bật nhất?
8. ❓ Đọc file điểm dạng `An,8.5,7.0` cần hàm nào để tách các cột?
9. ❓ Làm sao bỏ ký tự xuống dòng khi đọc từng dòng?
10. ❓ Muốn ghi nhật ký lâu dài nên chọn mode `"w"` hay `"a"`? Vì sao?

<details>
<summary>🔍 Xem đáp án</summary>

1. Mode `"w"` (write — ghi đè).
2. Mode `"a"` (append — ghi thêm).
3. `FileNotFoundError`.
4. Bảng mã mặc định trên Windows không chứa chữ tiếng Việt, gây `UnicodeEncodeError`.
5. Không — phải tự thêm `"\n"`.
6. List các chuỗi (mỗi chuỗi là một dòng).
7. Tự động đóng file dù có lỗi hay không.
8. `dong.split(",")`.
9. `dong.strip()`.
10. Mode `"a"` — vì nó giữ dữ liệu cũ và thêm dòng mới vào cuối.

</details>

---

## 📚 Bài đọc thêm

* [Python.org – Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
* [Python.org – open() documentation](https://docs.python.org/3/library/functions.html#open)
* [Real Python – Reading and Writing Files in Python](https://realpython.com/read-write-files-python/)
* [Python.org – Unicode HOWTO (hiểu về encoding)](https://docs.python.org/3/howto/unicode.html)

---

## 🏁 Kết thúc bài

🎉 Bạn đã biết lưu dữ liệu vào file và đọc lại — "cuốn sổ tay" của chương trình đã có! Nhưng dữ liệu học sinh, điểm số giờ vẫn nằm rải rác trong dict. **Bài kế tiếp** sẽ dạy cách đóng gói dữ liệu và hành vi thành **lớp (class)** — nền tảng của lập trình hướng đối tượng:

👉 **[Bài 23: Lập Trình Hướng Đối Tượng](../23_OOP/bai_giang.md)**
