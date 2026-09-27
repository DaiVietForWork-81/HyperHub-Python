<!-- TỰ ĐỘNG ĐỒNG BỘ từ 01-Co-Ban/18-String/bai.md — đừng sửa trực tiếp, sửa bản chính rồi chạy tools/sync_tracks.py -->

# Bài 16 — Chuỗi (String) Trong Python

> 🎓 **Chương 6 – Làm việc với văn bản**

## 🧠 Điều kiện tiên quyết

- [Bài 4 — Kiểu Dữ Liệu Cơ Bản](../04-Kieu-Du-Lieu/bai.md)
- [Bài 12 — Danh Sách (List) Trong Python](../12-List/bai.md)

---

## 🎯 Mục tiêu

Sau bài học này, học viên sẽ:

* ✅ Hiểu **chuỗi (string)** là gì và cách **tạo** chuỗi.
* ✅ **Nối** chuỗi bằng `+` và **lặp** bằng `*`.
* ✅ **Truy cập** từng ký tự và **cắt** chuỗi `[start:stop:step]`.
* ✅ Sử dụng các phương thức: `upper`, `lower`, `strip`, `split`, `join`, `replace`.
* ✅ Tìm kiếm và đếm: `find`, `startswith`, `endswith`, `count`.
* ✅ Kiểm tra nội dung: `isalpha`, `isdigit`, `isalnum`, `isspace`.
* ✅ Viết văn bản động bằng **f-string**.

---

## 📖 Kiến thức

### 1. Chuỗi là gì?

> 💬 **Nói đơn giản:** Chuỗi (string) là **một dãy ký tự** — chữ, số, dấu câu — được bọc trong dấu nháy. Mọi thứ bạn gõ trên bàn phím đều có thể là chuỗi.

**Ví dụ đời thực:** 🏷️ tên người, 📱 số điện thoại, 💬 tin nhắn.

**Tạo chuỗi — 3 cách:**

```python
s1 = "Xin chao"          # dấu nháy kép
s2 = 'Xin chao'          # dấu nháy đơn — giống hệt nhau
s3 = """Nhieu
dong"""                  # 3 dấu nháy — chuỗi nhiều dòng
```

> 💡 Dùng `'...'` khi chuỗi có chứa dấu `"`, và ngược lại: `"Anh ay noi 'xin chao'"`.

### 2. Nối và lặp chuỗi

```python
ho = "Nguyen"
ten = "An"
ho_ten = ho + " " + ten      # "Nguyen An" — nhớ thêm khoảng trắng
print(ho_ten)

vien = "-" * 30              # 30 dấu gạch ngang
print(vien)                  # ------------------------------
```

> ⚠️ Không cộng được chuỗi với số: `"Toi " + 15` báo `TypeError`. Phải đổi số thành chuỗi: `"Toi " + str(15)`.

### 3. Truy cập ký tự

Chuỗi giống một **dãy ô ký tự** đánh số từ **0**:

```python
s = "Python"
print(s[0])   # P — ký tự đầu tiên
print(s[5])   # n — ký tự cuối cùng
print(s[-1])  # n — chỉ số ÂM đếm từ cuối
print(len(s)) # 6 — số ký tự
```

| Chỉ số | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| Ký tự | P | y | t | h | o | n |
| Chỉ số âm | -6 | -5 | -4 | -3 | -2 | -1 |

> ⚠️ Truy cập vượt quá độ dài báo `IndexError: string index out of range`.

### 4. Cắt chuỗi (slicing)

Cú pháp `chuoi[start:stop:step]` — lấy từ `start` đến **trước** `stop`:

```python
s = "Python la rat de hoc"
print(s[0:6])    # Python  — 6 ký tự đầu
print(s[:6])     # Python  — bỏ trống start = bắt đầu từ 0
print(s[-3:])    # hoc     — 3 ký tự cuối
print(s[::2])    # Pto artd o — cách 1 ký tự lấy 1
print(s[::-1])   # coh ed tar al nohtyP — đảo ngược chuỗi
```

> 💡 Quy tắc vàng: `stop` **không được tính** — `s[0:6]` lấy vị trí 0..5. Và `[::-1]` là cách đảo chuỗi nhanh nhất.

### 5. Các phương thức biến đổi chính

Phương thức là "hàm đi kèm" với chuỗi, gọi bằng dấu chấm: `chuoi.phuong_thuc()`.

| Phương thức | Công dụng | Ví dụ | Kết quả |
|---|---|---|---|
| `upper()` | In hoa toàn bộ | `"python".upper()` | `PYTHON` |
| `lower()` | In thường toàn bộ | `"PYTHON".lower()` | `python` |
| `title()` | In hoa đầu mỗi từ | `"nguyen van an".title()` | `Nguyen Van An` |
| `strip()` | Xóa khoảng trắng 2 đầu | `"  py  ".strip()` | `py` |
| `replace(a, b)` | Thay `a` bằng `b` | `"ha noi".replace("ha", "HA")` | `HA noi` |

> ⚠️ **Quan trọng:** chuỗi là kiểu **bất biến** — mọi phương thức **trả về chuỗi mới**, không sửa chuỗi gốc:

```python
s = "python"
s.upper()        # ❌ bỏ quên kết quả — s vẫn là "python"
s = s.upper()    # ✅ phải gán lại
```

### 6. Tách và nối — split và join

**`split(sep)`** — cắt chuỗi thành danh sách:

```python
cac_tu = "Toi dang hoc Python".split()   # mặc định tách theo khoảng trắng
print(cac_tu)                            # ['Toi', 'dang', 'hoc', 'Python']
print(len(cac_tu))                       # 4 — số từ
print("2026-08-05".split("-"))           # ['2026', '08', '05']
```

**`join(iterable)`** — nối danh sách thành chuỗi (ngược với split):

```python
print(" ".join(["Toi", "dang", "hoc"]))  # Toi dang hoc
print("/".join(["05", "08", "2026"]))    # 05/08/2026
```

### 7. Tìm kiếm và đếm

```python
cau = "Python la ngon ngu tuyen voi"
print(cau.find("ngon"))       # 10 — vị trí tìm thấy (không có thì -1)
print(cau.count("n"))         # 5 — số lần xuất hiện
print(cau.startswith("Py"))   # True — bắt đầu bằng "Py"?
print(cau.endswith("voi"))    # True — kết thúc bằng "voi"?
```

### 8. Kiểm tra nội dung chuỗi

```python
print("12345".isdigit())      # True  — toàn chữ số
print("abc".isalpha())        # True  — toàn chữ cái
print("abc123".isalnum())     # True  — chữ + số, không ký tự đặc biệt
print("   ".isspace())        # True  — toàn khoảng trắng
print("ABC".isupper())        # True  — toàn in hoa
print("abc".islower())        # True  — toàn in thường
```

> 💡 Dùng để **kiểm tra đầu vào** trước khi xử lý: biển số, số điện thoại, mật khẩu...

### 9. F-string — chèn biến vào chuỗi

```python
ten = "An"
tuoi = 15
print(f"Xin chao {ten}, nam nay ban {tuoi} tuoi")

diem = 7.56789
print(f"Diem: {diem:.2f}")   # Diem: 7.57 — giữ 2 chữ số thập phân
print(f"{'Python':^20}")     # chữ căn giữa trong 20 ô
```

---

## 💡 Ví dụ minh họa

### Ví dụ 1: Tạo, nối và lặp chuỗi

```python
# Bước 1: tạo các chuỗi
ten = "An"
mon = "Python"
# Bước 2: nối chuỗi bằng +
thong_bao = "Ban " + ten + " dang hoc " + mon
print(thong_bao)             # Ban An dang hoc Python
# Bước 3: lặp chuỗi tạo đường viền
print("-" * 25)              # -------------------------
```

| Dòng code | Ý nghĩa |
|---|---|
| `"Ban " + ten + ...` | Nối 4 chuỗi thành 1 |
| `"-" * 25` | Tạo chuỗi 25 dấu gạch |

### Ví dụ 2: Cắt chuỗi lấy thông tin

```python
s = "Ho ten: Nguyen Van An"
print(s[8:])                 # Nguyen Van An — từ vị trí 8 đến hết
print(s[:3])                 # Ho
print("Python"[::2])         # Pto — cách quãng
```

### Ví dụ 3: Chuẩn hóa chuỗi nhập vào

```python
du_lieu = "  NGUYEN VAN AN  "
# strip bỏ khoảng trắng 2 đầu, title viết hoa đầu từ
sach = du_lieu.strip().title()
print(sach)                  # Nguyen Van An
```

> 💡 Chuỗi phương thức theo chuỗi gọi là **method chaining** — xử lý từ trái qua phải.

---

## 🔬 Ví dụ nâng cao

### Ví dụ 1: Thu nhỏ họ tên 📛

```python
ho_ten = "nguyen van an"
cac_tu = ho_ten.split()          # ['nguyen', 'van', 'an']

viet_tat = ""
for tu in cac_tu:
    viet_tat += tu[0].upper()    # cộng dồn chữ cái đầu mỗi từ

print("Viet tat:", viet_tat)     # Viet tat: NVA
```

### Ví dụ 2: Đếm số từ và tìm từ dài nhất 🔢

```python
cau = "  Python la ngon ngu tuyen voi  "
danh_sach_tu = cau.strip().split()        # strip + split gom khoảng trắng
print("So tu:", len(danh_sach_tu))        # So tu: 6
print("Tu dai nhat:", max(danh_sach_tu, key=len))   # Tu dai nhat: Python
```

### Ví dụ 3: Kiểm tra mật khẩu mạnh 🔐

```python
mat_khau = "An123@xyz"

# Kiểm tra từng điều kiện bằng hàm is... và đếm
du_dai = len(mat_khau) >= 8
co_chu = any(c.isalpha() for c in mat_khau)          # có ít nhất 1 chữ cái
co_so = any(c.isdigit() for c in mat_khau)           # có ít nhất 1 chữ số
co_dac_biet = any(not c.isalnum() for c in mat_khau) # có ký tự đặc biệt

if du_dai and co_chu and co_so and co_dac_biet:
    print("Mat khau MANH")       # đủ 4 điều kiện
else:
    print("Mat khau YEU")
```

### Ví dụ 4: Kiểm tra chuỗi đối xứng 🔄

```python
chuoi = "Race car"
sach = chuoi.replace(" ", "").lower()     # bỏ trắng, hạ thường: "racecar"
print(sach == sach[::-1])                 # True — đọc ngược giống nhau
```

> 💡 Bài tập 19 của bài này sẽ yêu cầu bạn tự hoàn thiện kiểm tra palindrome này!

---

## ⚠️ Lỗi thường gặp

### Lỗi 1: Cộng chuỗi với số — TypeError

```python
tuoi = 15
print("Toi " + tuoi + " tuoi")   # ❌ SAI — TypeError
print(f"Toi {tuoi} tuoi")        # ✅ SAI => đúng: dùng f-string
```

* **Kết quả báo:** `TypeError: can only concatenate str (not "int") to str`.

### Lỗi 2: Truy cập vị trí không tồn tại — IndexError

```python
print("Python"[6])   # ❌ SAI — vị trí tối đa là 5
```

* **Kết quả báo:** `IndexError: string index out of range`.

### Lỗi 3: Quên gán kết quả phương thức

```python
s = "python"
s.upper()     # ❌ SAI — kết quả bị vứt đi
print(s)      # python — không đổi
```

* **Nguyên nhân:** chuỗi **bất biến**; phải gán lại: `s = s.upper()`.

### Lỗi 4: Hiểu nhầm `isdigit` và `split`

```python
print("1.5".isdigit())     # False — có dấu chấm
print("  a   b  ".split(" "))   # ['', 'a', '', '', 'b', ''] — phần tử rỗng
print("  a   b  ".split())      # ['a', 'b'] — mặc định gom nhiều khoảng trắng
```

* **Cách sửa:** kiểm tra số thực bằng `float()` trong khối bắt lỗi (bài 19); tách chuỗi dùng `split()` không tham số.

---

## 💎 Mẹo

* 🧱 **`"+".join(list)` nhanh hơn nhiều** so với `+` trong vòng lặp khi nối nhiều chuỗi.
* 🔄 **`s[::-1]`** — đảo ngược chuỗi chỉ với 1 dòng.
* ✂️ **Cắt chuỗi không bao giờ lỗi khi vượt biên** — `"abc"[0:99]` trả về `"abc"`.
* 🎯 **`.strip()` trước khi phân tích** dữ liệu nhập — tránh khoảng trắng ẩn.
* 📏 `len()` đếm **ký tự**; `len(s.split())` đếm **từ**.
* ✨ F-string với `:.2f` làm tròn số đẹp khi in bảng giá, điểm số.
* 🔎 Kiểm tra bằng `isdigit()` trước khi `int()` — bài 19 sẽ học cách chuẩn hơn.

---

## 📝 Tóm tắt

| Nhóm | Phương thức / Cú pháp | Công dụng |
|---|---|---|
| Tạo | `"..."`, `'...'`, `"""..."""` | Tạo chuỗi |
| Nối – lặp | `+`, `*` | Nối chuỗi, lặp ký tự |
| Truy cập | `s[i]`, `s[-1]` | Lấy ký tự theo vị trí |
| Cắt | `s[a:b:c]` | Lấy đoạn con, đảo chuỗi |
| Biến đổi | `upper()`, `lower()`, `title()`, `strip()`, `replace()` | Trả về chuỗi mới |
| Tách – nối | `split()`, `join()` | Chuỗi ↔ danh sách |
| Tìm – đếm | `find()`, `count()`, `startswith()`, `endswith()` | Vị trí, số lần, kiểm tra đầu/cuối |
| Kiểm tra | `isalpha()`, `isdigit()`, `isalnum()`, `isspace()` | Kiểm tra nội dung |
| F-string | `f"...{bien}..."` | Chèn biến vào chuỗi |

---

## 🧪 Kiểm tra nhanh

1. ❓ Viết 2 cách tạo chuỗi giống hệt nhau.
2. ❓ `"A" + "B" * 3` cho kết quả gì?
3. ❓ Chỉ số của ký tự đầu tiên và cuối cùng trong `"Python"` là bao nhiêu?
4. ❓ `"Python la de"[0:6]` trả về gì? Vì sao không lấy ký tự ở vị trí 6?
5. ❓ Chuỗi có bị thay đổi khi gọi `upper()` không?
6. ❓ `split()` dùng để làm gì? `join()` thì sao?
7. ❓ Làm thế nào để đảo ngược chuỗi `"abc"`?
8. ❓ Hàm nào kiểm tra chuỗi toàn chữ số?
9. ❓ Viết f-string in ra `Toi 15 tuoi` với biến `tuoi = 15`.
10. ❓ `"Nguyen Van An".title()` cho kết quả gì?

<details>
<summary>🔍 Xem đáp án</summary>

1. `"Xin chao"` và `'Xin chao'`.
2. `"ABBB"` — `*` nhân trước, `+` nối sau.
3. Đầu tiên: 0; cuối cùng: 5.
4. `"Python"` — quy tắc cắt: vị trí `stop` không được tính.
5. Không — chuỗi bất biến; phương thức trả về chuỗi mới, phải gán lại.
6. `split()` cắt chuỗi thành danh sách; `join()` nối danh sách thành chuỗi.
7. `"abc"[::-1]`.
8. `isdigit()`.
9. `print(f"Toi {tuoi} tuoi")`.
10. `"Nguyen Van An"`.

</details>

---

## 📚 Bài đọc thêm

* [Python.org – Strings](https://docs.python.org/3/tutorial/introduction.html#strings)
* [Python.org – String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
* [W3Schools – Python Strings](https://www.w3schools.com/python/python_strings.asp)
* [Real Python – String Processing](https://realpython.com/python-strings/)

---

---

## 🧩 Bài tập

> 📝 🎯 **Chủ đề:** Tạo, nối, lặp, truy cập, cắt chuỗi; phương thức biến đổi; tìm kiếm; kiểm tra; f-string.

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Nối chuỗi chào hỏi

* **Đề bài:** Tạo biến `ten = "An"` và in ra câu `Xin chao An, chuc mot ngay tot lanh!` bằng cách nối chuỗi với `+`.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Xin chao An, chuc mot ngay tot lanh!
  ```
* **Gợi ý:** `"Xin chao " + ten + ", ..."` — nhớ thêm khoảng trắng khi nối.

### Bài 2: In hoa tên mình

* **Đề bài:** Tạo chuỗi `ten = "python"`, in ra chuỗi in hoa và chuỗi in thường của nó.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  PYTHON
  python
  ```
* **Gợi ý:** `ten.upper()` và `ten.lower()`.

### Bài 3: Độ dài chuỗi

* **Đề bài:** Cho chuỗi `thong_bao = "Hom nay troi dep"` — in ra độ dài của chuỗi.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Do dai: 16
  ```
* **Gợi ý:** Hàm `len()` đếm số ký tự (tính cả khoảng trắng).

### Bài 4: Lấy tên riêng từ họ tên

* **Đề bài:** Cho chuỗi `ho_ten = "Nguyen Van An"`. Dùng `split()` để lấy và in ra **tên riêng** (từ cuối cùng).
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Ten rieng: An
  ```
* **Gợi ý:** `ho_ten.split()` cho danh sách từ; tên riêng là phần tử cuối `[-1]`.

### Bài 5: Thay thế chữ

* **Đề bài:** Chuỗi `cau = "Toi thich an pho"` — dùng `replace()` thay `pho` thành `bun` và in kết quả.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Toi thich an bun
  ```
* **Gợi ý:** `cau.replace("pho", "bun")` — nhớ gán kết quả.

### Bài 6: Tìm vị trí chữ

* **Đề bài:** Chuỗi `cau = "Python la ngon ngu tuyen voi"` — in vị trí đầu tiên của từ `ngon` và vị trí của từ `khong` (không có).
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Vi tri 'ngon': 10
  Vi tri 'khong': -1
  ```
* **Gợi ý:** `cau.find("ngon")`; `find` trả về `-1` khi không tìm thấy.

### Bài 7: Xóa khoảng trắng thừa

* **Đề bài:** Chuỗi nhập lộn xộn `s = "   Xin chao Python   "` — dùng `strip()` in ra chuỗi sạch không còn khoảng trắng 2 đầu.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Xin chao Python
  ```
* **Gợi ý:** `s.strip()`.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Đếm số lần xuất hiện

* **Đề bài:** Chuỗi `cau = "Python la ngon ngu tuyen voi"` — đếm số lần ký tự `n` xuất hiện và in kết quả.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  So lan xuat hien cua 'n': 5
  ```
* **Gợi ý:** `cau.count("n")`.

### Bài 9: Kiểm tra đầu và cuối chuỗi

* **Đề bài:** Cho `ten_file = "baitho.docx"` — kiểm tra: file có bắt đầu bằng `bai` không? có kết thúc bằng `.txt` không? In `True`/`False`.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Bat dau bang 'bai': True
  Ket thuc bang '.txt': False
  ```
* **Gợi ý:** `startswith("bai")`, `endswith(".txt")`.

### Bài 10: Kiểm tra chuỗi toàn số

* **Đề bài:** Kiểm tra các chuỗi `"12345"`, `"12a45"`, `"1.5"` có phải toàn chữ số không, in kết quả từng dòng.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  12345: True
  12a45: False
  1.5: False
  ```
* **Gợi ý:** `isdigit()` — chỉ đúng khi **tất cả** ký tự là chữ số.

### Bài 11: Nối danh sách bằng join

* **Đề bài:** Danh sách `lop = ["10A1", "10A2", "10A3"]` — dùng `join` nối thành chuỗi cách nhau dấu `, ` và in ra.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  10A1, 10A2, 10A3
  ```
* **Gợi ý:** `", ".join(lop)`.

### Bài 12: Đếm số từ trong câu

* **Đề bài:** Câu `cau = "Hom nay toi di hoc tieng Anh"` — in ra số từ trong câu.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  So tu: 7
  ```
* **Gợi ý:** `split()` rồi `len()`.

### Bài 13: Kết hợp in hoa – in thường

* **Đề bài:** Cho `s = "ToiDangHocPython"` — in ra: chuỗi in hoa, chuỗi in thường, và kiểm tra xem chuỗi gốc có phải toàn in hoa không.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  TOIDANGHOCPYTHON
  toidanghocpython
  Toan in hoa? False
  ```
* **Gợi ý:** `upper()`, `lower()`, `isupper()`.

### Bài 14: Vẽ viền bằng phép nhân chuỗi

* **Đề bài:** In ra một tấm biển chào mừng gồm dòng viền `*` dài 20, dòng chữ `CHAO MUNG`, và dòng viền thứ hai.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  ********************
  CHAO MUNG
  ********************
  ```
* **Gợi ý:** `"*" * 20`.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Thu nhỏ họ tên

* **Đề bài:** Cho `ho_ten = "nguyen van an"`. Viết chương trình:
  1. Chuẩn hóa thành `Nguyen Van An` (in hoa đầu mỗi từ).
  2. Tạo viết tắt `NVA` (lấy chữ cái đầu mỗi từ, in hoa).
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Chuan hoa: Nguyen Van An
  Viet tat: NVA
  ```
* **Gợi ý:** Dùng `title()` cho việc 1; `split()` + vòng lặp + `upper()` cho việc 2.

### Bài 16: Đếm nguyên âm và phụ âm

* **Đề bài:** Câu `cau = "Python la ngon ngu tuyen voi"`. Đếm số **nguyên âm** (a, e, i, o, u) và số **phụ âm** (kí tự chữ cái còn lại, không tính khoảng trắng) rồi in ra.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Nguyen am: 8
  Phu am: 15
  ```
* **Gợi ý:** Vòng lặp qua từng ký tự; kiểm tra `chu in "aeiou"`; dùng `isalpha()` để loại khoảng trắng.

### Bài 17: Kiểm tra mật khẩu mạnh

* **Đề bài:** Nhập một mật khẩu. Kiểm tra và in `Manh` nếu có **đủ 4 điều kiện**: dài ≥ 8 ký tự, có chữ cái, có chữ số, có ký tự đặc biệt (không phải chữ và số). Ngược lại in `Yeu`.
* **Input:**
  ```
  Nhap mat khau: An123@xyz
  ```
* **Output:**
  ```
  Manh
  ```
* **Gợi ý:** Dùng `len()`, vòng lặp với `isalpha()`, `isdigit()`, `isalnum()`; `any()` có thể giúp kiểm tra nhanh.

### Bài 18: Chuẩn hóa họ tên

* **Đề bài:** Nhập họ tên có thể thừa nhiều khoảng trắng, ví dụ `"   nguyen   van   an   "`. In ra họ tên chuẩn: giữa các từ chỉ 1 khoảng trắng, đầu mỗi từ viết hoa.
* **Input:**
  ```
  Nhap ho ten:    nguyen   van   an   
  ```
* **Output:**
  ```
  Nguyen Van An
  ```
* **Gợi ý:** `strip()` + `split()` tự gom khoảng trắng thừa, sau đó `title()` hoặc tự viết hoa.

### Bài 19: Kiểm tra chuỗi đối xứng (Palindrome)

* **Đề bài:** Nhập một chuỗi, kiểm tra xem đọc xuôi và đọc ngược có giống nhau không (bỏ qua hoa/thường và khoảng trắng). In `Palindrome` hoặc `Khong phai palindrome`.
* **Input:**
  ```
  Nhap chuoi: Race car
  ```
* **Output:**
  ```
  Palindrome
  ```
* **Gợi ý:** Xóa khoảng trắng, hạ thường, rồi so sánh với bản đảo ngược `[::-1]`.

### Bài 20: Tạo tên đăng nhập từ họ tên

* **Đề bài:** Nhập họ tên, ví dụ `Nguyen Van An`. Tạo tên đăng nhập theo quy tắc: lấy **chữ cái đầu họ + tên riêng**, tất cả viết thường, thêm số `2026`. In ra tên đăng nhập.
* **Input:**
  ```
  Nhap ho ten: Nguyen Van An
  ```
* **Output:**
  ```
  nvan2026
  ```
* **Gợi ý:** `split()` → họ là phần tử `[0]`, tên riêng là `[-1]`; `lower()` toàn bộ; nối bằng `+`.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Thành thạo tạo, nối, lặp, truy cập và cắt chuỗi.
* ✅ Dùng được các phương thức biến đổi, tìm kiếm, kiểm tra và f-string.
* ✅ Xử lý văn bản thực tế: thu nhỏ tên, đếm từ, kiểm tra mật khẩu, palindrome.

> 💪 Chưa tự làm được bài nào thì đừng lo — xem lại bài giảng rồi quay lại. **Lập trình là luyện tập!**

---

## ✅ Đáp án

> 💡 **Hãy tự làm bài tập trước** rồi mới mở đáp án.

## 🟢 Dễ (Bài 1 – 7)


<details>
<summary>✅ Bài 1: Nối chuỗi chào hỏi</summary>


**Phân tích:** Cần ghép biến `ten` vào giữa câu văn.

**Ý tưởng:** Dùng toán tử `+` nối các chuỗi; phải thêm khoảng trắng thủ công.

**Thuật toán:**
1. Tạo biến `ten`.
2. Nối `"Xin chao " + ten + ", chuc mot ngay tot lanh!"`.
3. In kết quả.

**Code:**

```python
ten = "An"

# Nối chuỗi bằng dấu + (nhớ thêm khoảng trắng)
cau = "Xin chao " + ten + ", chuc mot ngay tot lanh!"
print(cau)
```

**Giải thích code:**
* `"Xin chao "` — có khoảng trắng cuối để tách với tên.
* `+ ten +` — chèn biến vào giữa.
* Kết quả: `Xin chao An, chuc mot ngay tot lanh!`.

**Độ phức tạp:** O(n) với n là độ dài chuỗi tạo ra.

---

</details>

<details>
<summary>✅ Bài 2: In hoa tên mình</summary>


**Phân tích:** Cần bản in hoa và in thường của cùng một chuỗi.

**Ý tưởng:** `upper()` và `lower()` — đều trả về chuỗi mới.

**Thuật toán:**
1. Tạo chuỗi `ten`.
2. In `ten.upper()`.
3. In `ten.lower()`.

**Code:**

```python
ten = "python"

# In hoa toàn bộ
print(ten.upper())
# In thường toàn bộ
print(ten.lower())
```

**Giải thích code:**
* `ten.upper()` → `PYTHON`.
* `ten.lower()` → `python` (giống chuỗi gốc).
* Chuỗi gốc không đổi — hai phương thức này trả về chuỗi mới.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 3: Độ dài chuỗi</summary>


**Phân tích:** Đếm số ký tự của chuỗi, tính cả khoảng trắng.

**Ý tưởng:** Dùng hàm `len()`.

**Thuật toán:**
1. Tạo chuỗi.
2. In `len(thong_bao)`.

**Code:**

```python
thong_bao = "Hom nay troi dep"

# len() đếm mọi ký tự, kể cả khoảng trắng
print("Do dai:", len(thong_bao))
```

**Giải thích code:**
* `"Hom nay troi dep"` gồm 13 chữ cái + 3 khoảng trắng = 16 ký tự.

**Độ phức tạp:** O(1).

---

</details>

<details>
<summary>✅ Bài 4: Lấy tên riêng từ họ tên</summary>


**Phân tích:** Tên riêng là từ cuối cùng của họ tên.

**Ý tưởng:** `split()` tách thành danh sách từ, lấy phần tử cuối bằng `[-1]`.

**Thuật toán:**
1. Tạo chuỗi họ tên.
2. `split()` → danh sách từ.
3. In `cac_tu[-1]`.

**Code:**

```python
ho_ten = "Nguyen Van An"

# split() mặc định tách theo khoảng trắng
cac_tu = ho_ten.split()
print("Ten rieng:", cac_tu[-1])
```

**Giải thích code:**
* `ho_ten.split()` → `['Nguyen', 'Van', 'An']`.
* `cac_tu[-1]` — chỉ số âm đếm từ cuối → `'An'`.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 5: Thay thế chữ</summary>


**Phân tích:** Thay một từ bằng từ khác trong chuỗi.

**Ý tưởng:** `replace(a, b)` thay toàn bộ `a` bằng `b`; phải gán lại kết quả.

**Thuật toán:**
1. Tạo chuỗi.
2. `cau.replace("pho", "bun")`.
3. Gán lại và in.

**Code:**

```python
cau = "Toi thich an pho"

# replace trả về chuỗi mới — cần gán lại
cau_moi = cau.replace("pho", "bun")
print(cau_moi)
```

**Giải thích code:**
* `replace("pho", "bun")` — tìm `"pho"` và thay bằng `"bun"`.
* Kết quả: `Toi thich an bun`.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 6: Tìm vị trí chữ</summary>


**Phân tích:** Cần vị trí xuất hiện đầu tiên của một từ; `-1` nếu không có.

**Ý tưởng:** Dùng `find()`.

**Thuật toán:**
1. Tạo chuỗi.
2. In `find("ngon")` và `find("khong")`.

**Code:**

```python
cau = "Python la ngon ngu tuyen voi"

# find trả về vị trí đầu tiên, hoặc -1 nếu không tìm thấy
print("Vi tri 'ngon':", cau.find("ngon"))
print("Vi tri 'khong':", cau.find("khong"))
```

**Giải thích code:**
* `cau.find("ngon")` — từ "ngon" bắt đầu ở vị trí 10.
* `cau.find("khong")` — không tồn tại → `-1`.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 7: Xóa khoảng trắng thừa</summary>


**Phân tích:** Chuỗi có khoảng trắng thừa ở hai đầu.

**Ý tưởng:** `strip()` xóa khoảng trắng đầu và cuối chuỗi.

**Thuật toán:**
1. Tạo chuỗi lộn xộn.
2. `s.strip()` và in.

**Code:**

```python
s = "   Xin chao Python   "

# strip xóa khoảng trắng ở cả 2 đầu
sach = s.strip()
print(sach)
```

**Giải thích code:**
* `"   Xin chao Python   ".strip()` → `"Xin chao Python"`.

**Độ phức tạp:** O(n).

---

</details>

## 🟡 Trung bình (Bài 8 – 14)


<details>
<summary>✅ Bài 8: Đếm số lần xuất hiện</summary>


**Phân tích:** Đếm số lần ký tự `n` xuất hiện trong chuỗi.

**Ý tưởng:** `count("n")` đếm toàn bộ.

**Thuật toán:**
1. Tạo chuỗi.
2. In `cau.count("n")`.

**Code:**

```python
cau = "Python la ngon ngu tuyen voi"

# count đếm số lần xuất hiện của ký tự/từ
print("So lan xuat hien cua 'n':", cau.count("n"))
```

**Giải thích code:**
* Đếm ký tự `n` trong câu: Python(1) + ngon(2) + ngu(1) + tuyen(1) = 5.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 9: Kiểm tra đầu và cuối chuỗi</summary>


**Phân tích:** Kiểm tra phần đầu và phần cuối của tên file.

**Ý tưởng:** `startswith()` và `endswith()` trả về `True`/`False`.

**Thuật toán:**
1. Tạo tên file.
2. In kết quả hai phép kiểm tra.

**Code:**

```python
ten_file = "baitho.docx"

# startswith: bắt đầu bằng?
print("Bat dau bang 'bai':", ten_file.startswith("bai"))
# endswith: kết thúc bằng?
print("Ket thuc bang '.txt':", ten_file.endswith(".txt"))
```

**Giải thích code:**
* `"baitho.docx".startswith("bai")` → True.
* `"baitho.docx".endswith(".txt")` → False (đuôi là `.docx`).

**Độ phức tạp:** O(k) với k là độ dài chuỗi kiểm tra.

---

</details>

<details>
<summary>✅ Bài 10: Kiểm tra chuỗi toàn số</summary>


**Phân tích:** Cần biết chuỗi có phải "toàn chữ số" hay không.

**Ý tưởng:** `isdigit()` chỉ trả `True` khi **mọi** ký tự đều là chữ số.

**Thuật toán:**
1. Lần lượt kiểm tra 3 chuỗi.
2. In kết quả.

**Code:**

```python
print("12345:", "12345".isdigit())   # toàn số -> True
print("12a45:", "12a45".isdigit())   # có chữ cái -> False
print("1.5:", "1.5".isdigit())       # có dấu chấm -> False
```

**Giải thích code:**
* `"12a45"` chứa chữ `a` → không phải toàn chữ số.
* `"1.5"` chứa dấu chấm → không phải chữ số.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 11: Nối danh sách bằng join</summary>


**Phân tích:** Cần nối các phần tử list thành chuỗi có dấu phân cách.

**Ý tưởng:** `", ".join(lop)` — nối bằng chuỗi `", "`.

**Thuật toán:**
1. Tạo danh sách.
2. `", ".join(lop)` và in.

**Code:**

```python
lop = ["10A1", "10A2", "10A3"]

# join nối danh sách thành chuỗi, xen dấu phẩy + khoảng trắng
chuoi = ", ".join(lop)
print(chuoi)
```

**Giải thích code:**
* `join` được gọi trên **chuỗi phân cách** `", "` và nhận danh sách làm đối số.
* Kết quả: `10A1, 10A2, 10A3`.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 12: Đếm số từ trong câu</summary>


**Phân tích:** Số từ = số phần tử sau khi tách theo khoảng trắng.

**Ý tưởng:** `cau.split()` → `len()`.

**Thuật toán:**
1. Tạo câu.
2. Tách thành danh sách từ.
3. In số phần tử.

**Code:**

```python
cau = "Hom nay toi di hoc tieng Anh"

# split tách theo khoảng trắng, len đếm số từ
so_tu = len(cau.split())
print("So tu:", so_tu)
```

**Giải thích code:**
* `"Hom nay toi di hoc tieng Anh".split()` → 6 từ.
* `len(...)` → 6.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 13: Kết hợp in hoa – in thường</summary>


**Phân tích:** Ba yêu cầu: in hoa, in thường, kiểm tra chuỗi gốc.

**Ý tưởng:** `upper()`, `lower()`, `isupper()`.

**Thuật toán:**
1. In bản in hoa.
2. In bản in thường.
3. In kết quả kiểm tra `isupper()`.

**Code:**

```python
s = "ToiDangHocPython"

# Ba thao tác trên cùng chuỗi gốc
print(s.upper())
print(s.lower())
print("Toan in hoa?", s.isupper())
```

**Giải thích code:**
* `s.upper()` → `TOIDANGHOCPYTHON`.
* `s.lower()` → `toidanghocpython`.
* `s.isupper()` → False vì chuỗi gốc có chữ thường.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 14: Vẽ viền bằng phép nhân chuỗi</summary>


**Phân tích:** Dòng viền lặp lại ký tự `*` 20 lần.

**Ý tưởng:** `"*" * 20` tạo chuỗi lặp.

**Thuật toán:**
1. In dòng viền trên.
2. In dòng chữ.
3. In dòng viền dưới.

**Code:**

```python
# Phép nhân chuỗi: lặp lại 20 lần
print("*" * 20)
print("CHAO MUNG")
print("*" * 20)
```

**Giải thích code:**
* `"*" * 20` — chuỗi gồm 20 dấu `*`.

**Độ phức tạp:** O(k) với k = 20.

---

</details>

## 🔴 Khó (Bài 15 – 20)


<details>
<summary>✅ Bài 15: Thu nhỏ họ tên</summary>


**Phân tích:** Hai việc: chuẩn hóa chữ hoa đầu từ, và lấy chữ cái đầu mỗi từ.

**Ý tưởng:** `title()` cho việc 1; `split()` + vòng lặp + `upper()` cho việc 2.

**Thuật toán:**
1. Tách tên thành danh sách từ.
2. Việc 1: nối các từ với `title()`.
3. Việc 2: gom chữ cái đầu mỗi từ, viết hoa.

**Code:**

```python
ho_ten = "nguyen van an"
cac_tu = ho_ten.split()          # ['nguyen', 'van', 'an']

# Việc 1: viết hoa đầu mỗi từ
chuan_hoa = " ".join(tu.title() for tu in cac_tu)
print("Chuan hoa:", chuan_hoa)   # Nguyen Van An

# Việc 2: lấy chữ cái đầu mỗi từ, viết hoa
viet_tat = ""
for tu in cac_tu:
    viet_tat += tu[0].upper()    # cộng dồn chữ cái đầu

print("Viet tat:", viet_tat)     # NVA
```

**Giải thích code:**
* `tu.title()` — viết hoa đầu mỗi từ; `" ".join(...)` nối lại.
* `tu[0]` — chữ cái đầu từ; `.upper()` — viết hoa; `+=` — cộng dồn.
* Kết quả: `Nguyen Van An` và `NVA`.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 16: Đếm nguyên âm và phụ âm</summary>


**Phân tích:** Duyệt từng ký tự, phân loại: nguyên âm, phụ âm, bỏ qua phần khác.

**Ý tưởng:** Vòng lặp kiểm tra `chu in "aeiou"` (đã hạ thường) và `chu.isalpha()`.

**Thuật toán:**
1. Hạ thường chuỗi để dễ so sánh.
2. Duyệt từng ký tự: nguyên âm nếu thuộc `"aeiou"`; phụ âm nếu là chữ cái còn lại.
3. In kết quả.

**Code:**

```python
cau = "Python la ngon ngu tuyen voi"
nguyen_am = 0
phu_am = 0

for chu in cau.lower():
    if chu in "aeiou":            # thuộc tập nguyên âm
        nguyen_am += 1
    elif chu.isalpha():           # còn là chữ cái -> phụ âm
        phu_am += 1

print("Nguyen am:", nguyen_am)
print("Phu am:", phu_am)
```

**Giải thích code:**
* `cau.lower()` — hạ thường để `"P"` và `"p"` đều so sánh được.
* `chu in "aeiou"` — kiểm tra ký tự có trong chuỗi nguyên âm không.
* `chu.isalpha()` — lọc chữ cái, loại khoảng trắng.
* Tổng: 8 nguyên âm, 15 phụ âm.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 17: Kiểm tra mật khẩu mạnh</summary>


**Phân tích:** Bốn điều kiện; cần kiểm tra "có ít nhất một" ký tự loại đó.

**Ý tưởng:** Dùng `any(... for chu in mat_khau)` — đúng nếu có ít nhất một ký tự thỏa mãn.

**Thuật toán:**
1. Nhập mật khẩu.
2. Kiểm tra 4 điều kiện bằng `len()` và `any()`.
3. In kết quả.

**Code:**

```python
mat_khau = input("Nhap mat khau: ")   # Nhập: An123@xyz

# 4 điều kiện
du_dai = len(mat_khau) >= 8
co_chu = any(c.isalpha() for c in mat_khau)   # có chữ cái
co_so = any(c.isdigit() for c in mat_khau)    # có chữ số
co_dac_biet = any(not c.isalnum() for c in mat_khau)  # có ký tự đặc biệt

if du_dai and co_chu and co_so and co_dac_biet:
    print("Manh")
else:
    print("Yeu")
```

**Giải thích code:**
* `any(...)` — trả về `True` nếu **ít nhất một** phần tử thỏa mãn.
* `not c.isalnum()` — ký tự không phải chữ và không phải số → ký tự đặc biệt (`@`).
* Mật khẩu `An123@xyz` đủ 4 điều kiện → `Manh`.

**Độ phức tạp:** O(n) với n là độ dài mật khẩu.

---

</details>

<details>
<summary>✅ Bài 18: Chuẩn hóa họ tên</summary>


**Phân tích:** Khoảng trắng thừa giữa các từ và hai đầu; chữ hoa lộn xộn.

**Ý tưởng:** `strip()` bỏ trắng hai đầu; `split()` mặc định tự gom nhiều khoảng trắng; `title()` viết hoa đầu từ.

**Thuật toán:**
1. Nhập họ tên.
2. `strip()` và `split()` để tách từ sạch.
3. Nối lại bằng `" "` với mỗi từ `title()`.

**Code:**

```python
ho_ten = input("Nhap ho ten: ")   # Nhập:    nguyen   van   an   

# split mặc định tự gom nhiều khoảng trắng; title viết hoa đầu từ
chuan = " ".join(tu.title() for tu in ho_ten.strip().split())
print(chuan)
```

**Giải thích code:**
* `ho_ten.strip()` — bỏ khoảng trắng hai đầu.
* `.split()` — tách theo bất kỳ khoảng trắng nào, nén nhiều trắng thành 1.
* `tu.title()` — mỗi từ viết hoa chữ đầu.
* `" ".join(...)` — nối lại với đúng 1 khoảng trắng.
* Kết quả: `Nguyen Van An`.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 19: Kiểm tra chuỗi đối xứng (Palindrome)</summary>


**Phân tích:** Cần so sánh chuỗi với bản đảo ngược, bỏ qua hoa/thường và khoảng trắng.

**Ý tưởng:** Lọc bỏ khoảng trắng, hạ thường, so sánh với `[::-1]`.

**Thuật toán:**
1. Nhập chuỗi.
2. Bỏ khoảng trắng bằng `replace(" ", "")`.
3. Hạ thường.
4. So sánh với chuỗi đảo ngược.

**Code:**

```python
chuoi = input("Nhap chuoi: ")   # Nhập: Race car

# Xóa khoảng trắng + hạ thường -> "racecar"
sach = chuoi.replace(" ", "").lower()

# So sánh với bản đảo ngược
if sach == sach[::-1]:
    print("Palindrome")
else:
    print("Khong phai palindrome")
```

**Giải thích code:**
* `chuoi.replace(" ", "")` — xóa mọi khoảng trắng.
* `.lower()` — đồng bộ chữ hoa/thường.
* `sach[::-1]` — đảo ngược chuỗi.
* `"racecar" == "racecar"` → `Palindrome`.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 20: Tạo tên đăng nhập từ họ tên</summary>


**Phân tích:** Quy tắc: chữ cái đầu họ + tên riêng + năm, toàn chữ thường.

**Ý tưởng:** `split()` lấy họ `[0]` và tên riêng `[-1]`; lấy `[0]` của họ; `lower()` toàn bộ.

**Thuật toán:**
1. Nhập họ tên.
2. Tách danh sách từ.
3. Họ = phần tử đầu, tên riêng = phần tử cuối.
4. Ghép: chữ đầu họ + tên riêng + "2026", hạ thường.

**Code:**

```python
ho_ten = input("Nhap ho ten: ")   # Nhập: Nguyen Van An
cac_tu = ho_ten.split()

# Họ là phần tử đầu, tên riêng là phần tử cuối
ho = cac_tu[0]
ten_rieng = cac_tu[-1]

# Chữ cái đầu họ + tên riêng + năm, tất cả viết thường
ten_dang_nhap = (ho[0] + ten_rieng + "2026").lower()
print(ten_dang_nhap)
```

**Giải thích code:**
* `ho[0]` — chữ `N` của "Nguyen".
* `"N" + "An" + "2026"` → `"NAn2026"`.
* `.lower()` → `nvan2026`.

**Độ phức tạp:** O(n).

---

</details>

## 📌 Lời khuyên cuối


* Khi nối nhiều chuỗi trong vòng lặp, hãy gom vào list rồi dùng `"".join()` — nhanh và sạch hơn.
* Chuỗi bất biến — mọi phương thức chỉ trả về chuỗi mới, đừng quên gán lại.
* Kiểm tra đầu vào bằng `isdigit()`, `isalpha()` trước khi xử lý để tránh lỗi bất ngờ (bài 19 sẽ học cách chuyên nghiệp hơn).

👉 Tiếp theo: **[Bài 17: Module Trong Python](../17-Module/bai.md)**

---

## ➡️ Điều hướng

**Vị trí:** `02-Thuat-Toan/16-String/bai.md`

**Bài tiếp theo:** [Bài 17 — Module Trong Python](../17-Module/bai.md)