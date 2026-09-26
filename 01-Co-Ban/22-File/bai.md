# Bài 22 — Đọc Và Ghi File Trong Python

> 🎓 **Chương 6 – Tổ chức mã nguồn: Module, Package và File**

## 🧠 Điều kiện tiên quyết

- [Bài 20 — Module Trong Python](../20-Module/bai.md)
- [Bài 21 — Package Trong Python](../21-Package/bai.md)

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

---

## 🧩 Bài tập

> 📝 🎯 **Chủ đề:** `open()` với các mode `r/w/a`, `read/readline/readlines`, `write/writelines`, `with` statement, `encoding="utf-8"`, xử lý lỗi file.

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Ghi rồi đọc lại

* **Đề bài:** Ghi chuỗi `Xin chao the gioi Python!` vào file `hello.txt` (mode `"w"`), sau đó đọc lại toàn bộ bằng `read()` và in ra màn hình.
* **Input:** Không có.
* **Output:**
  ```
  Xin chao the gioi Python!
  ```
* **Gợi ý:** `with open("hello.txt", "w", encoding="utf-8") as f: f.write(...)`.

### Bài 2: Ghi nhiều dòng

* **Đề bài:** Ghi 3 dòng `Toan`, `Van`, `Anh` vào file `mon_hoc.txt` (mỗi dòng là một lệnh `write` kèm `\n`), rồi đọc lại và in.
* **Input:** Không có.
* **Output:**
  ```
  Mon: Toan
  Mon: Van
  Mon: Anh
  ```
* **Gợi ý:** Đọc bằng vòng lặp `for dong in f` và `dong.strip()`.

### Bài 3: Đọc toàn bộ bằng `read()`

* **Đề bài:** Tạo file `tho.txt` gồm 2 câu thơ, đọc bằng `read()` và in ra — kèm in số ký tự trong file.
* **Input:** Không có.
* **Output:**
  ```
  Rung xanh la biec
  Chim hot trong cay
  So ky tu: 37
  ```
* **Gợi ý:** `len(noi_dung)` đếm ký tự; nhớ đếm cả dấu xuống dòng `\n`.

### Bài 4: Mode `"a"` — ghi thêm

* **Đề bài:** Ghi 2 dòng vào `nhat_ky.txt`, đóng lại. Mở lại với mode `"a"` ghi thêm 1 dòng. Đọc lại và in toàn bộ để chứng minh dữ liệu cũ vẫn còn.
* **Input:** Không có.
* **Output:**
  ```
  Buoi sang: hoc Python
  Buoi chieu: lam bai tap
  Buoi toi: on lai bai
  ```
* **Gợi ý:** Mode `"a"` không xóa dữ liệu cũ; đọc bằng `read()` sau khi ghi xong.

### Bài 5: `readlines()` và đếm dòng

* **Đề bài:** Tạo file `hs.txt` gồm 4 dòng tên học sinh. Dùng `readlines()` đọc list các dòng, in số dòng và từng dòng đã bỏ khoảng trắng.
* **Input:** Không có.
* **Output:**
  ```
  So dong: 4
  An
  Binh
  Cuong
  Dung
  ```
* **Gợi ý:** `len(danh_sach_dong)`; mỗi dòng dùng `.strip()`.

### Bài 6: Ghi danh sách học sinh

* **Đề bài:** Có list 3 tuple `("Ten", "Lop")`. Ghi vào file `hoc_sinh.txt` dạng `Ten,Lop` (mỗi học sinh một dòng), rồi đọc lại in ra màn hình.
* **Input:** Không có.
* **Output:**
  ```
  Nguyen Van An,10A1
  Tran Thi Mai,10A1
  Le Quang Binh,10A2
  ```
* **Gợi ý:** Vòng lặp `for ten, lop in danh_sach:` + `f.write(f"{ten},{lop}\n")`.

### Bài 7: `readline()` lần lượt

* **Đề bài:** Tạo file `tinh.txt` 3 dòng. Dùng `readline()` đọc đúng 2 dòng đầu, in ra dòng 1 và dòng 2.
* **Input:** Không có.
* **Output:**
  ```
  Dong 1: Python
  Dong 2: la
  ```
* **Gợi ý:** Mỗi lần gọi `readline()` đọc một dòng theo thứ tự.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Đọc điểm từ file

* **Đề bài:** Tạo file `diem.txt` dạng `Ten,Toan,Van,Anh` cho 3 học sinh. Đọc file, tính điểm trung bình mỗi bạn và in ra `Ten: TB` (2 chữ số thập phân).
* **Input:** Không có.
* **Output:**
  ```
  Nguyen Van An: 8.17
  Tran Thi Mai: 6.50
  Le Quang Binh: 5.00
  ```
* **Gợi ý:** `phan = dong.split(",")`; chuyển điểm bằng `float(...)`.

### Bài 9: Bắt lỗi file không tồn tại

* **Đề bài:** Viết chương trình đọc file `khong_co.txt` (chưa từng được tạo) bằng `try/except`, bắt `FileNotFoundError` và in thông báo thân thiện, chương trình **không sập**.
* **Input:** Không có.
* **Output:**
  ```
  File khong ton tai! Hay kiem tra lai ten file.
  ```
* **Gợi ý:** Đặt `with open(...)` bên trong `try`, bắt lỗi trong `except FileNotFoundError`.

### Bài 10: Nhật ký đơn giản

* **Đề bài:** Viết hàm `ghi_log(thong_diep)` dùng mode `"a"`, mỗi dòng có dạng `[gio_hien_tai] thong_diep` (dùng `datetime.now().strftime("%H:%M:%S")`). Gọi hàm 3 lần với 3 sự kiện mẫu, rồi đọc lại và in.
* **Input:** Không có.
* **Output (thời gian có thể khác):**
  ```
  [10:15:22] Chuong trinh khoi dong
  [10:15:22] Xu ly du lieu
  [10:15:22] Ket thuc
  ```
* **Gợi ý:** `from datetime import datetime`; thời gian lấy trong lúc gọi hàm.

### Bài 11: Đếm dòng và chữ

* **Đề bài:** Tạo file `van_ban.txt` gồm 3 câu ngắn. Đọc file, in ra số dòng và tổng số từ (mỗi từ ngăn cách bởi khoảng trắng).
* **Input:** Không có.
* **Output:**
  ```
  So dong: 3
  So tu: 6
  ```
* **Gợi ý:** `len(dong.split())` đếm từ trong một dòng.

### Bài 12: Bảng cửu chương ra file

* **Đề bài:** Ghi bảng cửu chương nhân 5 (từ 1 đến 10) vào file `bang_5.txt` bằng vòng lặp `for` + `write`, rồi đọc lại in ra màn hình.
* **Input:** Không có.
* **Output:**
  ```
  5 x 1 = 5
  5 x 2 = 10
  ...
  5 x 10 = 50
  ```
* **Gợi ý:** `f.write(f"5 x {i} = {5 * i}\n")` trong vòng lặp `range(1, 11)`.

### Bài 13: Tìm kiếm trong file

* **Đề bài:** Tạo file `lop.txt` gồm 4 tên học sinh. Đọc từng dòng và in ra những bạn có tên **chứa chữ "An"**.
* **Input:** Không có.
* **Output:**
  ```
  Tim thay: Nguyen Van An
  Tim thay: Pham Thi Anh
  ```
* **Gợi ý:** Điều kiện `if "An" in dong`.

### Bài 14: Xóa dòng trống

* **Đề bài:** Tạo file `lo_xinh.txt` gồm 4 dòng, trong đó có 1 dòng trống ở giữa. Đọc file, ghi các dòng **có nội dung** vào file mới `sach.txt`, rồi in nội dung file mới.
* **Input:** Không có.
* **Output:**
  ```
  Dong 1
  Dong 2
  Dong 4
  ```
* **Gợi ý:** Sau khi `strip()`, nếu chuỗi rỗng thì `continue`.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Nâng điểm cho học sinh

* **Đề bài:** File `diem.txt` dạng `Ten,Toan` cho 4 bạn (tự tạo). Đọc file, bạn nào điểm Toán **nhỏ hơn 9.0** thì cộng thêm 2 (không quá 10), ghi **lại toàn bộ** vào file (mode `"w"`), rồi đọc lại in kết quả.
* **Input:** Không có.
* **Output:**
  ```
  Sau khi nang diem:
  An,7.5
  Binh,5.0
  Cuong,10.0
  Dung,6.0
  ```
* **Gợi ý:** Đọc vào list, chỉnh sửa trong list, ghi lại từ đầu bằng `"w"`.

### Bài 16: Ghép hai file

* **Đề bài:** Tạo 2 file `hs_10a.txt` và `hs_10b.txt`, mỗi file 2 tên học sinh. Đọc cả hai và gộp vào file `hs_ca_khoi.txt`, in ra tổng số học sinh và nội dung file gộp.
* **Input:** Không có.
* **Output:**
  ```
  Tong so hoc sinh: 4
  An
  Binh
  Cuong
  Dung
  ```
* **Gợi ý:** Ghi bằng mode `"a"` cho lần thứ hai, hoặc gom list rồi ghi một lần.

### Bài 17: Phân loại và ghi kết quả

* **Đề bài:** File `diem.txt` dạng `Ten,Toan,Van,Anh` (3 bạn, tự tạo). Đọc, tính điểm TB, xếp loại (≥8 Giỏi, ≥6.5 Khá, ≥5 Trung bình, còn lại Yếu), ghi vào file `xep_loai.txt` dạng `Ten: Loai`, rồi in nội dung file kết quả.
* **Input:** Không có.
* **Output:**
  ```
  Nguyen Van An: Gioi
  Tran Thi Mai: Kha
  Le Quang Binh: Yeu
  ```
* **Gợi ý:** Ghi file kết quả bằng `"w"`; từng bước: đọc → tính → ghi → in.

### Bài 18: Sổ tay ghi chú

* **Đề bài:** Viết chương trình: list ghi chú mẫu gồm 3 chuỗi, ghi toàn bộ vào `so_tay.txt` (mỗi ghi chú một dòng, có dấu `-` đầu dòng). Mở lại file, in số ghi chú và từng ghi chú.
* **Input:** Không có.
* **Output:**
  ```
  So ghi chu: 3
  - Mua sach Python
  - Lam bai tap bai 22
  - On lai bai 21
  ```
* **Gợi ý:** Dùng `writelines` với list đã có sẵn dấu `-` và `\n`.

### Bài 19: Nhật ký lỗi

* **Đề bài:** Viết hàm `ghi_log(thong_diep)` dùng `with` + `"a"` + `encoding`. Mô phỏng 3 sự kiện: 2 sự kiện bình thường, 1 sự kiện dạng `LOI: ...`. Đọc lại file và chỉ in ra các dòng chứa chữ `LOI`.
* **Input:** Không có.
* **Output:**
  ```
  LOI: File diem.txt khong doc duoc
  ```
* **Gợi ý:** Khi đọc lại, dùng `if "LOI" in dong` để lọc.

### Bài 20: Quản lý điểm lưu file (tiểu dự án)

* **Đề bài:** Xây dựng chương trình hoàn chỉnh:
  1. Tạo file `quan_ly_diem.txt` với 4 học sinh, mỗi dòng `Ten,Toan,Van,Anh`.
  2. Đọc file (có `try/except` bắt `FileNotFoundError`), tính TB và xếp loại từng bạn.
  3. Ghi bảng tổng kết `Ten - TB - Loai` vào file `tong_ket.txt`.
  4. In cả bảng tổng kết ra màn hình và in dòng chữ `Da ghi ket qua vao tong_ket.txt`.
* **Input:** Không có.
* **Output:**
  ```
  Nguyen Van An - 8.17 - Gioi
  Tran Thi Mai - 6.50 - Kha
  Le Quang Binh - 5.00 - Trung binh
  Pham Thu Ha - 8.50 - Gioi
  Da ghi ket qua vao tong_ket.txt
  ```
* **Gợi ý:** Gộp toàn bộ kiến thức bài: tạo file, đọc, tính, ghi kết quả, bắt lỗi.

---

## 🎯 Tổng kết sau khi làm bài

* ✅ Viết được chương trình ghi và đọc file với `with` + `encoding="utf-8"`.
* ✅ Phân biệt rõ `"r"`, `"w"`, `"a"` và chọn đúng mode cho từng việc.
* ✅ Xử lý được `FileNotFoundError` không cho chương trình sập.
* ✅ Xây dựng được ứng dụng nhỏ lưu dữ liệu (điểm, log, ghi chú) ra file.

> 💪 Khi dữ liệu đã "sống lâu dài" trên đĩa, đã đến lúc tổ chức nó đẹp đẽ hơn bằng **lớp (class)**!

---

## ✅ Đáp án

> 💡 **Hãy tự làm bài tập trước** rồi mới mở đáp án.

## 🟢 Dễ (Bài 1 – 7)


<details>
<summary>✅ Bài 1: Ghi rồi đọc lại</summary>


**Phân tích:** Hai thao tác ngược nhau: ghi bằng `write`, đọc bằng `read`.

**Ý tưởng:** Mở file mode `"w"` ghi chuỗi; mở lại mode `"r"` đọc toàn bộ và in.

**Thuật toán:**
1. `open("hello.txt", "w", encoding="utf-8")` → `write("Xin chao the gioi Python!")`.
2. `open("hello.txt", "r", encoding="utf-8")` → `read()`.
3. In nội dung đọc được.

**Code:**

```python
# Bước 1: ghi chuỗi vào file (mode "w" tự tạo file nếu chưa có)
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("Xin chao the gioi Python!")

# Bước 2: đọc lại toàn bộ nội dung
with open("hello.txt", "r", encoding="utf-8") as f:
    noi_dung = f.read()

print(noi_dung)
```

**Giải thích code:**
* Mode `"w"` — ghi đè từ đầu; file chưa tồn tại thì Python tự tạo.
* `read()` trả về toàn bộ nội dung dạng chuỗi.
* Hai `with` riêng biệt: mở để ghi xong đóng, rồi mở lại để đọc.

**Độ phức tạp:** O(n) với n là số ký tự file.

---

</details>

<details>
<summary>✅ Bài 2: Ghi nhiều dòng</summary>


**Phân tích:** Mỗi dòng là một lần `write`; phải tự thêm `\n`.

**Ý tưởng:** Ghi 3 lần với `\n`, đọc bằng vòng lặp `for dong in f`.

**Thuật toán:**
1. Mở `"w"`, `write` 3 dòng mỗi dòng kèm `"\n"`.
2. Mở `"r"`, vòng `for` in từng dòng đã `strip()`.

**Code:**

```python
# Ghi 3 dòng vào file
with open("mon_hoc.txt", "w", encoding="utf-8") as f:
    f.write("Toan\n")
    f.write("Van\n")
    f.write("Anh\n")

# Đọc lại từng dòng và in
with open("mon_hoc.txt", "r", encoding="utf-8") as f:
    for dong in f:
        print("Mon:", dong.strip())
```

**Giải thích code:**
* `write("Toan\n")` — `\n` là ký tự xuống dòng; thiếu nó mọi dòng sẽ dính làm một.
* `for dong in f` — Python duyệt file từng dòng một, tiết kiệm bộ nhớ.
* `dong.strip()` — bỏ `\n` và khoảng trắng thừa.

**Độ phức tạp:** O(n) với n tổng số ký tự.

---

</details>

<details>
<summary>✅ Bài 3: Đọc toàn bộ bằng `read()`</summary>


**Phân tích:** `read()` đọc cả file thành một chuỗi; `len()` đếm ký tự kèm cả `\n`.

**Ý tưởng:** Ghi 2 câu thơ, đọc lại, in nội dung và độ dài.

**Thuật toán:**
1. Ghi `"Rung xanh la biec\n"` và `"Chim hot trong cay\n"`.
2. `read()` → in nội dung.
3. `len(noi_dung)` → in số ký tự.

**Code:**

```python
# Tạo file thơ
with open("tho.txt", "w", encoding="utf-8") as f:
    f.write("Rung xanh la biec\n")
    f.write("Chim hot trong cay\n")

# Đọc toàn bộ
with open("tho.txt", "r", encoding="utf-8") as f:
    noi_dung = f.read()

print(noi_dung, end="")          # end="" để không in thêm xuống dòng
print("So ky tu:", len(noi_dung))
```

**Giải thích code:**
* Chuỗi đọc được là `"Rung xanh la biec\nChim hot trong cay\n"`.
* Đếm: `17 + 1 + 18 + 1 = 37` ký tự — hai dấu `\n` cũng được đếm.
* `print(noi_dung, end="")` — nội dung đã có sẵn `\n`, tránh in thêm dòng trống.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 4: Mode `"a"` — ghi thêm</summary>


**Phân tích:** Mode `"a"` (append) không xóa dữ liệu cũ — kiểm chứng bằng cách ghi 2 lần.

**Ý tưởng:** Lần 1 mode `"w"` ghi 2 dòng; lần 2 mode `"a"` ghi thêm 1 dòng; đọc lại toàn bộ.

**Thuật toán:**
1. Mở `"w"` ghi `Buoi sang`, `Buoi chieu`.
2. Mở `"a"` ghi `Buoi toi`.
3. Mở `"r"` in toàn bộ.

**Code:**

```python
# Lần 1: tạo file với 2 dòng
with open("nhat_ky.txt", "w", encoding="utf-8") as f:
    f.write("Buoi sang: hoc Python\n")
    f.write("Buoi chieu: lam bai tap\n")

# Lần 2: mode "a" chỉ thêm vào cuối, không xóa gì
with open("nhat_ky.txt", "a", encoding="utf-8") as f:
    f.write("Buoi toi: on lai bai\n")

# Đọc lại và in toàn bộ 3 dòng
with open("nhat_ky.txt", "r", encoding="utf-8") as f:
    print(f.read())
```

**Giải thích code:**
* Lần 1 dùng `"w"` vì cần tạo file mới; lần 2 phải dùng `"a"` để giữ 2 dòng cũ.
* Nếu lần 2 dùng `"w"` thì file chỉ còn 1 dòng — dữ liệu cũ biến mất.
* `read()` in cả 3 dòng, chứng minh mode `"a"` giữ nguyên dữ liệu.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 5: `readlines()` và đếm dòng</summary>


**Phân tích:** `readlines()` trả về list — đếm bằng `len()`, duyệt bằng vòng lặp.

**Ý tưởng:** Tạo file 4 tên, đọc thành list, in số dòng và từng tên sau `strip()`.

**Thuật toán:**
1. Ghi 4 tên học sinh (4 dòng).
2. `readlines()` → list.
3. In `len(list)` và từng phần tử đã `strip()`.

**Code:**

```python
# Tạo file 4 tên học sinh
with open("hs.txt", "w", encoding="utf-8") as f:
    f.writelines(["An\n", "Binh\n", "Cuong\n", "Dung\n"])

# Đọc thành list các dòng
with open("hs.txt", "r", encoding="utf-8") as f:
    danh_sach_dong = f.readlines()

print("So dong:", len(danh_sach_dong))
for dong in danh_sach_dong:
    print(dong.strip())
```

**Giải thích code:**
* `writelines(list)` — ghi cả list chuỗi liền mạch; vẫn phải có `\n` trong từng phần tử.
* `readlines()` trả về `["An\n", "Binh\n", "Cuong\n", "Dung\n"]` → 4 phần tử.
* `.strip()` xóa `\n` trước khi in.

**Độ phức tạp:** O(n) với n tổng ký tự.

---

</details>

<details>
<summary>✅ Bài 6: Ghi danh sách học sinh</summary>


**Phân tích:** Chuyển dữ liệu trong bộ nhớ (list tuple) thành dòng chữ trên file.

**Ý tưởng:** Duyệt list, ghi từng cặp `Ten,Lop` thành một dòng.

**Thuật toán:**
1. Khai báo list 3 tuple `("Ten", "Lop")`.
2. Mode `"w"`: mỗi cặp ghi `f"{ten},{lop}\n"`.
3. Đọc lại và in toàn bộ.

**Code:**

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

# Đọc lại và in
with open("hoc_sinh.txt", "r", encoding="utf-8") as f:
    print(f.read(), end="")
```

**Giải thích code:**
* `for ten, lop in danh_sach` — giải nén tuple thành 2 biến.
* Định dạng `Ten,Lop` (dấu phẩy) là "quy ước" giúp bài sau tách cột bằng `split(",")`.
* Mỗi dòng kết thúc bằng `\n` để từng học sinh ở một dòng.

**Độ phức tạp:** O(n) với n học sinh.

---

</details>

<details>
<summary>✅ Bài 7: `readline()` lần lượt</summary>


**Phân tích:** Mỗi lần gọi `readline()` đọc đúng một dòng và con trỏ tự nhảy xuống dòng kế.

**Ý tưởng:** Tạo file 3 dòng, gọi `readline()` 2 lần, in với nhãn.

**Thuật toán:**
1. Ghi `"Python\n"`, `"la\n"`, `"ngon ngu\n"`.
2. `d1 = f.readline()`; `d2 = f.readline()`.
3. In `d1`, `d2` sau khi `strip()`.

**Code:**

```python
# Tạo file 3 dòng
with open("tinh.txt", "w", encoding="utf-8") as f:
    f.write("Python\n")
    f.write("la\n")
    f.write("ngon ngu\n")

# Đọc lần lượt 2 dòng đầu
with open("tinh.txt", "r", encoding="utf-8") as f:
    d1 = f.readline()
    d2 = f.readline()

print("Dong 1:", d1.strip())
print("Dong 2:", d2.strip())
```

**Giải thích code:**
* `readline()` thứ nhất trả `"Python\n"`, con trỏ xuống dòng 2.
* `readline()` thứ hai trả `"la\n"`.
* `.strip()` bỏ `\n` để in gọn đẹp.

**Độ phức tạp:** O(1) — chỉ đọc 2 dòng.

---

</details>

## 🟡 Trung bình (Bài 8 – 14)


<details>
<summary>✅ Bài 8: Đọc điểm từ file</summary>


**Phân tích:** Mỗi dòng là một bản ghi; cần tách cột, đổi kiểu dữ liệu, tính toán.

**Ý tưởng:** `strip()` → `split(",")` → `float()` từng điểm → trung bình.

**Thuật toán:**
1. Tạo `diem.txt` với 3 dòng `Ten,Toan,Van,Anh`.
2. Với mỗi dòng: bỏ `\n`, bỏ dòng trống, tách cột.
3. Tính TB = `sum(diem)/len(diem)`, in 2 chữ số thập phân.

**Code:**

```python
# Tạo file điểm mẫu (4 cột: tên + 3 điểm)
with open("diem.txt", "w", encoding="utf-8") as f:
    f.write("Nguyen Van An,8.5,7.0,9.0\n")
    f.write("Tran Thi Mai,6.0,6.5,7.0\n")
    f.write("Le Quang Binh,4.5,5.0,5.5\n")

# Đọc và tính trung bình từng bạn
with open("diem.txt", "r", encoding="utf-8") as f:
    for dong in f:
        dong = dong.strip()                # bỏ ký tự xuống dòng
        if not dong:                       # bỏ qua dòng trống
            continue
        phan = dong.split(",")             # tách cột
        ten = phan[0]                      # cột 1: tên
        diem = [float(x) for x in phan[1:]]  # các cột còn lại: điểm
        tb = sum(diem) / len(diem)
        print(f"{ten}: {tb:.2f}")
```

**Giải thích code:**
* `phan[1:]` — lấy từ cột 2 đến hết (3 điểm).
* `float(x)` — chuyển chuỗi `"8.5"` thành số 8.5; thiếu bước này sẽ lỗi phép tính.
* `{tb:.2f}` — in làm tròn 2 chữ số thập phân.

**Độ phức tạp:** O(n) với n học sinh.

---

</details>

<details>
<summary>✅ Bài 9: Bắt lỗi file không tồn tại</summary>


**Phân tích:** Đọc file chưa tồn tại sẽ ném `FileNotFoundError` — cần chặn để chương trình không sập.

**Ý tưởng:** Bọc thao tác mở file trong `try`, bắt lỗi trong `except FileNotFoundError`.

**Thuật toán:**
1. `try:` mở `"khong_co.txt"` mode `"r"`.
2. Nếu mở được: đọc và in.
3. `except FileNotFoundError:` in thông báo thân thiện.

**Code:**

```python
try:
    # File này KHÔNG tồn tại trong thư mục — thử đọc sẽ lỗi
    with open("khong_co.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("File khong ton tai! Hay kiem tra lai ten file.")

print("Chuong trinh van chay tiep binh thuong.")   # minh chứng không sập
```

**Giải thích code:**
* Khi mở thất bại, `with` cũng chưa kịp chạy — lỗi bị `except` hứng ngay.
* Không có `try/except`, chương trình in lỗi đỏ và dừng đột ngột.

**Độ phức tạp:** O(1).

---

</details>

<details>
<summary>✅ Bài 10: Nhật ký đơn giản</summary>


**Phân tích:** Nhật ký phải giữ lịch sử → mode `"a"`; mỗi dòng kèm thời gian.

**Ý tưởng:** Hàm `ghi_log` dùng `datetime.now()` lấy giờ, ghi dòng `[giờ] sự kiện`.

**Thuật toán:**
1. `from datetime import datetime`.
2. Hàm `ghi_log`: lấy giờ hiện tại, `with` + `"a"` ghi một dòng.
3. Gọi 3 lần, đọc lại và in.

**Code:**

```python
from datetime import datetime

def ghi_log(thong_diep):
    """Ghi một dòng nhật ký kèm thời gian."""
    gio = datetime.now().strftime("%H:%M:%S")
    with open("nhat_ky.txt", "a", encoding="utf-8") as f:
        f.write(f"[{gio}] {thong_diep}\n")

# Gọi hàm 3 lần với các sự kiện mẫu
ghi_log("Chuong trinh khoi dong")
ghi_log("Xu ly du lieu")
ghi_log("Ket thuc")

# Đọc lại và in
with open("nhat_ky.txt", "r", encoding="utf-8") as f:
    print(f.read(), end="")
```

**Giải thích code:**
* `strftime("%H:%M:%S")` — định dạng giờ:phút:giây (kiến thức Bài 20).
* Mode `"a"` — mỗi lần chạy lại, log cũ vẫn còn, dòng mới thêm vào cuối.
* Tách hàm `ghi_log` giúp gọi lại nhiều nơi trong chương trình.

**Độ phức tạp:** O(1) mỗi lần ghi.

---

</details>

<details>
<summary>✅ Bài 11: Đếm dòng và chữ</summary>


**Phân tích:** Dòng đếm bằng vòng lặp; từ trong mỗi dòng đếm bằng `split()`.

**Ý tưởng:** Đếm biến chạy; `len(dong.split())` = số từ của một dòng.

**Thuật toán:**
1. Tạo file 3 câu ngắn (tổng 6 từ).
2. Với mỗi dòng: `so_dong += 1`; `so_tu += len(dong.split())`.
3. In kết quả.

**Code:**

```python
# Tạo file văn bản mẫu: 3 dòng, mỗi dòng 2 từ → tổng 6 từ
with open("van_ban.txt", "w", encoding="utf-8") as f:
    f.write("Python la\n")
    f.write("ngon ngu\n")
    f.write("de hoc\n")

so_dong = 0
so_tu = 0

with open("van_ban.txt", "r", encoding="utf-8") as f:
    for dong in f:
        dong = dong.strip()
        if not dong:            # dòng trống không tính
            continue
        so_dong += 1
        so_tu += len(dong.split())

print("So dong:", so_dong)
print("So tu:", so_tu)
```

**Giải thích code:**
* `dong.split()` — tách chuỗi theo khoảng trắng: `"Python la"` → `["Python", "la"]` = 2 từ.
* Ba dòng × 2 từ = 6 từ; ba dòng = 3 dòng.
* Biến đếm phải khai báo **trước** vòng lặp, nếu không sẽ báo `NameError`.

**Độ phức tạp:** O(n) với n ký tự file.

---

</details>

<details>
<summary>✅ Bài 12: Bảng cửu chương ra file</summary>


**Phân tích:** Sinh 10 dòng bằng vòng lặp rồi ghi file; đọc lại để kiểm chứng.

**Ý tưởng:** `for i in range(1, 11)` + `write(f"5 x {i} = {5*i}\n")`.

**Thuật toán:**
1. Mở `"w"`, vòng lặp ghi 10 dòng.
2. Mở `"r"`, in toàn bộ.

**Code:**

```python
# Ghi bảng cửu chương nhân 5 vào file
with open("bang_5.txt", "w", encoding="utf-8") as f:
    for i in range(1, 11):
        f.write(f"5 x {i} = {5 * i}\n")

# Đọc lại và in
with open("bang_5.txt", "r", encoding="utf-8") as f:
    print(f.read(), end="")
```

**Giải thích code:**
* `range(1, 11)` — 10 lần lặp từ 1 đến 10.
* `f"5 x {i} = {5 * i}"` — Python tính sẵn `5 * i` rồi chèn vào chuỗi.
* Kết quả dòng cuối: `5 x 10 = 50`.

**Độ phức tạp:** O(1) — số dòng cố định 10.

---

</details>

<details>
<summary>✅ Bài 13: Tìm kiếm trong file</summary>


**Phân tích:** Đọc từng dòng và lọc theo điều kiện chứa chuỗi con.

**Ý tưởng:** `if "An" in dong` — kiểm tra chuỗi con (kiến thức Bài 18).

**Thuật toán:**
1. Tạo file 4 tên, trong đó 2 tên chứa "An".
2. Duyệt từng dòng; nếu chứa `"An"` thì in ra.
3. Bỏ qua `\n` khi in.

**Code:**

```python
# Tạo danh sách lớp
with open("lop.txt", "w", encoding="utf-8") as f:
    f.write("Nguyen Van An\n")
    f.write("Tran Binh\n")
    f.write("Pham Thi Anh\n")
    f.write("Le Cuong\n")

# Tìm các bạn có tên chứa "An"
with open("lop.txt", "r", encoding="utf-8") as f:
    for dong in f:
        if "An" in dong:                 # kiểm tra chuỗi con
            print("Tim thay:", dong.strip())
```

**Giải thích code:**
* `"An" in "Pham Thi Anh"` → `True` vì chuỗi con "An" xuất hiện trong tên.
* `"An" in "Tran Binh"` → `False` (chữ "An" không khớp giữa chữ "Binh").
* `.strip()` xóa `\n` thừa khi in.

**Độ phức tạp:** O(n × m) với n dòng, m độ dài chuỗi trung bình.

---

</details>

<details>
<summary>✅ Bài 14: Xóa dòng trống</summary>


**Phân tích:** File có dòng trống; khi ghi file mới chỉ giữ dòng có nội dung.

**Ý tưởng:** Sau `strip()`, chuỗi rỗng nghĩa là dòng trống → `continue`.

**Thuật toán:**
1. Tạo file `lo_xinh.txt`: "Dong 1", "Dong 2", "" (trống), "Dong 4".
2. Đọc từng dòng; dòng sau `strip()` rỗng thì bỏ qua.
3. Ghi các dòng hợp lệ vào `sach.txt` (mode `"w"`).
4. Đọc lại và in.

**Code:**

```python
# Tạo file có chứa một dòng trống ở giữa
with open("lo_xinh.txt", "w", encoding="utf-8") as f:
    f.write("Dong 1\n")
    f.write("Dong 2\n")
    f.write("\n")                     # dòng trống
    f.write("Dong 4\n")

# Đọc và chỉ ghi những dòng có nội dung
with open("lo_xinh.txt", "r", encoding="utf-8") as f_doc, \
     open("sach.txt", "w", encoding="utf-8") as f_ghi:
    for dong in f_doc:
        dong = dong.strip()
        if not dong:                  # dòng trống -> bỏ qua
            continue
        f_ghi.write(dong + "\n")

# In nội dung file đã làm sạch
with open("sach.txt", "r", encoding="utf-8") as f:
    print(f.read(), end="")
```

**Giải thích code:**
* Mở **2 file cùng lúc** trong một `with` (ngăn cách bằng dấu phẩy) — đọc file nguồn, ghi file đích.
* `if not dong` — chuỗi rỗng mang giá trị `False`, dòng trống bị bỏ.
* Dấu `\` cuối dòng giúp tách câu lệnh dài sang dòng mới.

**Độ phức tạp:** O(n) với n ký tự file.

---

</details>

## 🔴 Khó (Bài 15 – 20)


<details>
<summary>✅ Bài 15: Nâng điểm cho học sinh</summary>


**Phân tích:** Quy trình "đọc → sửa → ghi lại" là cách phổ biến để cập nhật file.

**Ý tưởng:** Đọc vào list, điều chỉnh điểm, mở lại với `"w"` ghi toàn bộ.

**Thuật toán:**
1. Tạo `diem.txt` 4 dòng `Ten,Toan`.
2. Đọc vào list các chuỗi; tách điểm, nếu < 9.0 thì +2 (tối đa 10).
3. Ghi lại toàn bộ với `"w"`.
4. Đọc lại và in.

**Code:**

```python
# Tạo file điểm mẫu
with open("diem.txt", "w", encoding="utf-8") as f:
    f.write("An,5.5\n")
    f.write("Binh,3.0\n")
    f.write("Cuong,8.5\n")
    f.write("Dung,4.0\n")

# Bước 1: đọc toàn bộ vào list
danh_sach = []
with open("diem.txt", "r", encoding="utf-8") as f:
    for dong in f:
        danh_sach.append(dong.strip())

# Bước 2: sửa điểm trong list
for i in range(len(danh_sach)):
    ten, diem = danh_sach[i].split(",")
    diem = float(diem)
    if diem < 9.0:                     # nâng điểm cho mọi bạn dưới 9
        diem = min(diem + 2, 10.0)     # cộng 2 nhưng không quá 10
    danh_sach[i] = f"{ten},{diem:.1f}"

# Bước 3: ghi lại toàn bộ (mode "w" — ghi đè file cũ)
with open("diem.txt", "w", encoding="utf-8") as f:
    for dong in danh_sach:
        f.write(dong + "\n")

# Bước 4: đọc lại kiểm chứng
print("Sau khi nang diem:")
with open("diem.txt", "r", encoding="utf-8") as f:
    print(f.read(), end="")
```

**Giải thích code:**
* `diem = min(diem + 2, 10.0)` — cộng 2 nhưng giới hạn ở 10 (hàm `min` lấy giá trị nhỏ hơn).
* `{diem:.1f}` — luôn in 1 chữ số thập phân (`5.0`, `10.0`) cho cột điểm đều đẹp.
* Ghi lại bằng `"w"` — nội dung mới thay thế hoàn toàn nội dung cũ.
* Kết quả: An 5.5→7.5, Binh 3.0→5.0, Cuong 8.5→10.0, Dung 4.0→6.0.

**Độ phức tạp:** O(n) với n học sinh.

---

</details>

<details>
<summary>✅ Bài 16: Ghép hai file</summary>


**Phân tích:** Ghép nội dung 2 file thành 1; đếm tổng số dòng.

**Ý tưởng:** Đọc từng file vào list, gộp list, ghi một lần.

**Thuật toán:**
1. Tạo 2 file, mỗi file 2 tên.
2. Đọc cả hai vào 1 list.
3. Ghi list gộp vào `hs_ca_khoi.txt`.
4. In số lượng và nội dung.

**Code:**

```python
# Tạo 2 file lớp
with open("hs_10a.txt", "w", encoding="utf-8") as f:
    f.write("An\n")
    f.write("Binh\n")

with open("hs_10b.txt", "w", encoding="utf-8") as f:
    f.write("Cuong\n")
    f.write("Dung\n")

# Đọc cả hai file vào một list
danh_sach = []
for ten_file in ["hs_10a.txt", "hs_10b.txt"]:
    with open(ten_file, "r", encoding="utf-8") as f:
        for dong in f:
            if dong.strip():
                danh_sach.append(dong.strip())

# Ghi gộp vào file mới
with open("hs_ca_khoi.txt", "w", encoding="utf-8") as f:
    for ten in danh_sach:
        f.write(ten + "\n")

# Báo cáo kết quả
print("Tong so hoc sinh:", len(danh_sach))
with open("hs_ca_khoi.txt", "r", encoding="utf-8") as f:
    print(f.read(), end="")
```

**Giải thích code:**
* Vòng lặp `for ten_file in [...]` — xử lý nhiều file với cùng đoạn code, không lặp lại 2 lần.
* `if dong.strip()` — lọc luôn dòng trống khi đọc.
* Số học sinh = `len(danh_sach)` = 4.

**Độ phức tạp:** O(n) với n tổng số dòng hai file.

---

</details>

<details>
<summary>✅ Bài 17: Phân loại và ghi kết quả</summary>


**Phân tích:** Chuỗi xử lý khép kín: tạo dữ liệu → đọc → tính → ghi kết quả → in.

**Ý tưởng:** Tách riêng 2 file: file nguồn (điểm) và file kết quả (xếp loại).

**Thuật toán:**
1. Tạo `diem.txt` 3 học sinh, 4 cột.
2. Với mỗi dòng: tính TB, xếp loại theo 4 mốc.
3. Ghi `Ten: Loai` vào `xep_loai.txt` (`"w"`).
4. Đọc file kết quả và in.

**Code:**

```python
# Tạo file điểm mẫu
with open("diem.txt", "w", encoding="utf-8") as f:
    f.write("Nguyen Van An,8.5,7.0,9.0\n")
    f.write("Tran Thi Mai,6.0,6.5,7.0\n")
    f.write("Le Quang Binh,4.0,4.5,5.0\n")

def xep_loai(tb):
    """Xếp loại theo điểm trung bình."""
    if tb >= 8.0:
        return "Gioi"
    if tb >= 6.5:
        return "Kha"
    if tb >= 5.0:
        return "Trung binh"
    return "Yeu"

# Đọc, tính, ghi kết quả
with open("diem.txt", "r", encoding="utf-8") as f_doc, \
     open("xep_loai.txt", "w", encoding="utf-8") as f_ghi:
    for dong in f_doc:
        dong = dong.strip()
        if not dong:
            continue
        phan = dong.split(",")
        ten = phan[0]
        diem = [float(x) for x in phan[1:]]
        tb = sum(diem) / len(diem)
        f_ghi.write(f"{ten}: {xep_loai(tb)}\n")

# In kết quả
with open("xep_loai.txt", "r", encoding="utf-8") as f:
    print(f.read(), end="")
```

**Giải thích code:**
* Hàm `xep_loai` tách riêng giúp code dễ đọc, dễ kiểm tra.
* An TB 8.17 → Gioi; Mai TB 6.50 → Kha; Binh TB 4.50 → Yeu.
* Ghi và đọc dùng 2 `with` riêng: ghi xong đóng, rồi mới đọc lại.

**Độ phức tạp:** O(n) với n học sinh.

---

</details>

<details>
<summary>✅ Bài 18: Sổ tay ghi chú</summary>


**Phân tích:** List ghi chú được ghi nguyên khối bằng `writelines`, đọc lại để báo cáo.

**Ý tưởng:** Chuẩn bị sẵn list chuỗi có dấu `-` và `\n`, ghi 1 lần.

**Thuật toán:**
1. Tạo list 3 ghi chú dạng `"- ...\n"`.
2. `writelines` ghi vào `so_tay.txt`.
3. Đọc lại, in số ghi chú và từng ghi chú.

**Code:**

```python
# Danh sách ghi chú trong chương trình
ghi_chu = [
    "- Mua sach Python\n",
    "- Lam bai tap bai 22\n",
    "- On lai bai 21\n",
]

# Ghi toàn bộ vào file
with open("so_tay.txt", "w", encoding="utf-8") as f:
    f.writelines(ghi_chu)

# Đọc lại và báo cáo
with open("so_tay.txt", "r", encoding="utf-8") as f:
    danh_sach = f.readlines()

print("So ghi chu:", len(danh_sach))
for dong in danh_sach:
    print(dong.strip())
```

**Giải thích code:**
* `writelines` ghi cả list liền mạch — mỗi phần tử đã sẵn `\n` nên tự tách dòng.
* `readlines()` đọc lại đúng thành list 3 phần tử.
* `.strip()` bỏ `\n` khi in.

**Độ phức tạp:** O(n) với n ký tự.

---

</details>

<details>
<summary>✅ Bài 19: Nhật ký lỗi</summary>


**Phân tích:** Vừa ghi log, vừa lọc log — hai kỹ năng kết hợp trong một bài.

**Ý tưởng:** Hàm `ghi_log` ghi mọi sự kiện; khi đọc lại, lọc dòng chứa `"LOI"`.

**Thuật toán:**
1. Hàm `ghi_log` dùng `"a"` + encoding.
2. Ghi 3 sự kiện: 2 thường + 1 lỗi.
3. Đọc lại, chỉ in dòng chứa `"LOI"`.

**Code:**

```python
from datetime import datetime

def ghi_log(thong_diep):
    """Ghi một dòng nhật ký kèm thời gian."""
    gio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("nhat_ky.txt", "a", encoding="utf-8") as f:
        f.write(f"[{gio}] {thong_diep}\n")

# Mô phỏng 3 sự kiện
ghi_log("Mo file thanh cong")
ghi_log("LOI: File diem.txt khong doc duoc")
ghi_log("Ket thuc chuong trinh")

# Đọc lại và chỉ in các dòng lỗi
with open("nhat_ky.txt", "r", encoding="utf-8") as f:
    for dong in f:
        if "LOI" in dong:
            print(dong.strip())
```

**Giải thích code:**
* Mọi sự kiện đều được ghi đầy đủ vào nhật ký — chỉ khi đọc mới lọc.
* `if "LOI" in dong` — lọc dòng có chuỗi con "LOI".
* Cách này giúp log đầy đủ mà báo cáo lỗi vẫn gọn gàng.

**Độ phức tạp:** O(1) mỗi lần ghi; O(n) khi quét toàn file.

---

</details>

<details>
<summary>✅ Bài 20: Quản lý điểm lưu file (tiểu dự án)</summary>


**Phân tích:** Bài tổng hợp toàn bộ: tạo file, đọc an toàn (bắt lỗi), tính toán, ghi kết quả, báo cáo.

**Ý tưởng:** Chia 4 bước rõ ràng, mỗi bước một khối `with` riêng.

**Thuật toán:**
1. Tạo `quan_ly_diem.txt` với 4 học sinh.
2. Đọc file trong `try/except` → tính TB và xếp loại.
3. Ghi bảng tổng kết vào `tong_ket.txt`.
4. In bảng tổng kết + dòng xác nhận.

**Code:**

```python
def xep_loai(tb):
    """Xếp loại theo điểm trung bình."""
    if tb >= 8.0:
        return "Gioi"
    if tb >= 6.5:
        return "Kha"
    if tb >= 5.0:
        return "Trung binh"
    return "Yeu"

# Bước 1: tạo dữ liệu mẫu
with open("quan_ly_diem.txt", "w", encoding="utf-8") as f:
    f.write("Nguyen Van An,8.5,7.0,9.0\n")
    f.write("Tran Thi Mai,6.0,6.5,7.0\n")
    f.write("Le Quang Binh,4.5,5.0,5.5\n")
    f.write("Pham Thu Ha,9.0,8.5,8.0\n")

# Bước 2: đọc file an toàn và tính điểm
ket_qua = []
try:
    with open("quan_ly_diem.txt", "r", encoding="utf-8") as f:
        for dong in f:
            dong = dong.strip()
            if not dong:
                continue
            phan = dong.split(",")
            ten = phan[0]
            diem = [float(x) for x in phan[1:]]
            tb = sum(diem) / len(diem)
            ket_qua.append(f"{ten} - {tb:.2f} - {xep_loai(tb)}")
except FileNotFoundError:
    print("File quan_ly_diem.txt khong ton tai!")

# Bước 3: ghi bảng tổng kết
with open("tong_ket.txt", "w", encoding="utf-8") as f:
    for dong in ket_qua:
        f.write(dong + "\n")

# Bước 4: in ra màn hình
for dong in ket_qua:
    print(dong)
print("Da ghi ket qua vao tong_ket.txt")
```

**Giải thích code:**
* Bước 2 nằm trong `try/except` — nếu file bị xóa mất, chương trình báo lỗi mà không sập.
* `ket_qua` là list chuỗi đã định dạng sẵn — vừa để ghi file, vừa để in ra.
* Mỗi bước một `with` riêng: tạo → đọc → ghi → in, trình tự rõ ràng.

**Độ phức tạp:** O(n) với n học sinh.

---

</details>

## 📌 Lời khuyên cuối


* Công thức bất biến: `with open(ten, mode, encoding="utf-8") as f:` — đủ 3 thành phần mới chuẩn.
* Muốn giữ dữ liệu cũ → `"a"`; muốn thay mới → `"w"`; chỉ đọc → `"r"`.
* File do người dùng đặt tên → luôn bọc trong `try/except FileNotFoundError`.
* Đọc từng dòng nhớ `.strip()` và bỏ qua dòng trống.
* Bài sau đã sẵn sàng: gói dữ liệu học sinh, điểm số thành **class** với lập trình hướng đối tượng!

👉 Tiếp theo: **[Bài 23: Lập Trình Hướng Đối Tượng](../23-OOP/bai.md)**

---

## ➡️ Điều hướng

**Vị trí:** `01-Co-Ban/22-File/bai.md`

**Bài tiếp theo:** [Bài 23 — Lập Trình Hướng Đối Tượng (OOP)](../23-OOP/bai.md)
