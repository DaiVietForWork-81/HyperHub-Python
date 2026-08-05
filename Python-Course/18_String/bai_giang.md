# 🔤 Bài 18: Chuỗi (String) Trong Python

> 🎓 **Chương 6 – Làm việc với văn bản**

Ở bài 17, bạn học cách lưu dữ liệu có nhãn bằng dictionary. Nhưng đa số dữ liệu hằng ngày — tên, địa chỉ, tin nhắn, mật khẩu — đều là **văn bản**. Hôm nay khám phá trọn vẹn kiểu dữ liệu `str`: tạo, nối, cắt, biến đổi và kiểm tra chuỗi.

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

## 🏁 Kết thúc bài

🎉 Bạn đã làm chủ kiểu dữ liệu **str** — tạo, cắt, biến đổi, kiểm tra và định dạng văn bản. Nhưng bạn có để ý: gõ nhầm chữ vào chỗ cần số là chương trình **sập ngay lập tức**? Đừng lo — bài sau dạy bạn cách **bắt và xử lý lỗi** để chương trình không bao giờ "đứng hình":

👉 **[Bài 19: Ngoại lệ (Exception)](../19_Exception/bai_giang.md)**
