<!-- TỰ ĐỘNG ĐỒNG BỘ từ 01-Co-Ban/12-Ham/bai.md — đừng sửa trực tiếp, sửa bản chính rồi chạy tools/sync_tracks.py -->

# Bài 12 — Hàm (Function) Trong Python

> 🎓 **Chương 4 – Tự động hóa công việc lặp lại**

## 🧠 Điều kiện tiên quyết

- [Bài 8 — Câu Lệnh If – Cấu Trúc Rẽ Nhánh](../08-Cau-Lenh-If/bai.md)
- [Bài 10 — Vòng Lặp For – Lặp Lại Một Số Lần Biết Trước](../10-Vong-Lap-For/bai.md)
- [Bài 11 — Vòng Lặp While – Lặp Cho Đến Khi Điều Kiện Sai](../11-Vong-Lap-While/bai.md)

---

## 🎯 Mục tiêu

Sau bài học này, học viên sẽ:

* ✅ Hiểu **hàm là gì** và vì sao phải dùng hàm — tránh viết code lặp lại.
* ✅ Định nghĩa được hàm bằng từ khóa `def` và **gọi hàm** đúng cách.
* ✅ Nắm vững khái niệm **tham số (parameter)** và **đối số (argument)**.
* ✅ Dùng được `return` để trả về kết quả; biết hàm không `return` sẽ trả về `None`.
* ✅ Sử dụng thành thạo **tham số mặc định**, **keyword arguments**, `*args`, `**kwargs`.
* ✅ Viết được **docstring** và các hàm tính diện tích, điểm trung bình, menu máy tính.

---

## 📖 Kiến thức

### 1. Hàm là gì? Vì sao phải dùng hàm?

> 💬 **Nói đơn giản:** Hàm là **một cụm code có tên**, bạn viết một lần rồi **gọi lại nhiều lần** mỗi khi cần.

**Ví dụ đời thực:** Hàm giống như **công thức nấu phở** của mẹ bạn. Mẹ viết công thức **một lần** trên giấy, nhưng mỗi khi khách đến thì **mở ra làm theo** — không cần nghĩ lại từ đầu. Bạn chỉ cần đưa vào **nguyên liệu** (thịt, phở, hành...) và nhận về **bát phở nóng**.

Trong lập trình:

* **Đầu vào** — nguyên liệu gọi là **tham số / đối số**.
* **Đầu ra** — bát phở thành phẩm gọi là **giá trị trả về** (`return`).

**Nhìn lại bài 11 (vòng lặp while):** khi phải viết code đếm ngược nhiều lần, bạn phải viết lại từng khối lặp. Với hàm, bạn chỉ cần viết **một lần** và gọi bất cứ khi nào muốn.

**Lợi ích của hàm:**

| Lợi ích | Giải thích |
|---|---|
| 🔁 **Tái sử dụng** | Viết 1 lần, dùng nhiều nơi — không sao chép code |
| 🧩 **Chia nhỏ** | Chương trình dài được tách thành các khối nhỏ dễ hiểu |
| 🐞 **Dễ sửa lỗi** | Lỗi chỉ nằm trong một hàm, sửa một chỗ là xong |
| 📖 **Dễ đọc** | Tên hàm mô tả công việc: `tinh_diem_trung_binh()` rõ nghĩa hơn 30 dòng code |

### 2. Cấu trúc một hàm — từ khóa `def`

```python
def ten_ham(tham_so1, tham_so2):
    """Docstring: mô tả ngắn gọn hàm làm gì"""
    # Thân hàm: các lệnh
    ket_qua = tham_so1 + tham_so2
    return ket_qua
```

| Thành phần | Ý nghĩa |
|---|---|
| `def` | Từ khóa khai báo hàm (viết tắt của *define* — định nghĩa) |
| `ten_ham` | Tên hàm — đặt theo quy tắc biến: chữ thường, gạch dưới |
| `(tham_so1, ...)` | Danh sách **tham số** — các giá trị đầu vào (có thể không có) |
| `:` | Kết thúc dòng khai báo — bắt buộc |
| `"""..."""` | **Docstring** — tài liệu mô tả hàm |
| Thân hàm | Các lệnh được **thụt vào (indent)** — thường 4 khoảng trắng |
| `return ...` | Trả kết quả về cho nơi gọi (có thể không có) |

### 3. Gọi hàm

Định nghĩa hàm **chưa làm gì cả** — phải **gọi** nó thì code mới chạy:

```python
def xin_chao():
    print("Xin chào!")

xin_chao()   # Gọi hàm — in ra: Xin chào!
xin_chao()   # Gọi lại lần nữa — in thêm một dòng nữa
```

> ⚠️ **Lỗi kinh điển của người mới:** định nghĩa hàm rồi quên gọi → chương trình chạy **im lặng không ra gì**. Hàm như công thức nấu ăn: ghi trong sổ thì chưa có món nào cả, phải đọc ra thực hiện.

### 4. Tham số và đối số

* **Tham số (parameter):** tên biến trong `( )` lúc **định nghĩa** hàm — như "chỗ trống" chờ nhận giá trị.
* **Đối số (argument):** giá trị thật sự truyền vào lúc **gọi** hàm.

```python
def cong_hai_so(a, b):      # a, b là THAM SỐ
    return a + b

print(cong_hai_so(3, 5))    # 3, 5 là ĐỐI SỐ → in ra 8
```

**Quy tắc:** số lượng đối số phải **khớp** số lượng tham số, không thì báo `TypeError`.

### 5. `return` — trả về kết quả

Từ khóa `return` làm hai việc:

1. **Gửi kết quả** ra ngoài cho nơi gọi dùng.
2. **Kết thúc hàm ngay** — các lệnh sau `return` không bao giờ chạy.

```python
def binh_phuong(x):
    return x * x
    print("Dòng này KHÔNG bao giờ chạy!")

kq = binh_phuong(5)
print(kq)    # 25 — hàm đã "đưa" 25 ra ngoài cho biến kq
```

### 6. Hàm không trả về → `None`

Nếu hàm không có `return` (hoặc `return` không kèm giá trị), Python tự trả về **`None`** — nghĩa là "không có gì".

```python
def in_thong_bao():
    print("Đã xong!")

kq = in_thong_bao()
print(kq)    # None
```

> 💡 Hàm kiểu "in ra màn hình" và hàm kiểu "trả về kết quả" là hai loại khác nhau. **Hàm tính toán nên dùng `return`** để giá trị còn tái sử dụng được; hàm chỉ hiển thị thì cứ `print`.

### 7. Tham số mặc định (Default Parameter)

```python
def chao(ten, loi_chao="Xin chào"):
    print(loi_chao, ten)

chao("Mai")                # Xin chào Mai — dùng giá trị mặc định
chao("Mai", "Chào buổi sáng")  # Chào buổi sáng Mai — ghi đè giá trị mặc định
```

* Tham số mặc định cho phép **bỏ qua đối số** khi gọi.
* ⚠️ **Quy tắc vàng:** tham số mặc định phải nằm **SAU** tham số thường — `def f(a, b=1)` đúng, `def f(a=1, b)` sai (báo `SyntaxError`).

### 8. Keyword Arguments

Khi gọi hàm, bạn có thể chỉ rõ **tên tham số = giá trị** — thứ tự không còn quan trọng:

```python
def gioi_thieu(ten, tuoi, lop):
    print(f"{ten} - {tuoi} tuổi - lớp {lop}")

gioi_thieu(tuoi=15, lop="10A1", ten="Mai")   # Mai - 15 tuổi - lớp 10A1
```

### 9. `*args` — số lượng đối số không xác định

Dấu `*` trước tham số gói **toàn bộ đối số** thành một **tuple**:

```python
def tinh_tong(*cac_so):
    return sum(cac_so)

print(tinh_tong(1, 2, 3))        # 6
print(tinh_tong(1, 2, 3, 4, 5))  # 15
```

### 10. `**kwargs` — đối số dạng tên

Hai dấu `**` gói toàn bộ keyword arguments thành một **dictionary**:

```python
def in_thong_tin(**thong_tin):
    for khoa, gia_tri in thong_tin.items():
        print(khoa, "=", gia_tri)

in_thong_tin(ten="An", tuoi=15, lop="10A1")
```

### 11. Docstring

**Docstring** là chuỗi `"""..."""` đặt ngay sau dòng `def`, dùng để **tài liệu hóa** hàm:

```python
def dien_tich_hcn(dai, rong):
    """Tính diện tích hình chữ nhật.

    Args:
        dai (float): chiều dài
        rong (float): chiều rộng

    Returns:
        float: diện tích = dai * rong
    """
    return dai * rong
```

Xem tài liệu hàm bằng `help(dien_tich_hcn)` hoặc `dien_tich_hcn.__doc__`.

---

## 💡 Ví dụ minh họa

### Ví dụ 1: Hàm chào hỏi đơn giản

```python
def xin_chao(ten):            # Hàm nhận tên người được chào
    """In lời chào kèm tên."""
    print(f"Xin chào {ten}, chúc bạn một ngày tốt lành!")

xin_chao("Mai")
xin_chao("Nam")
```

Kết quả:

```
Xin chào Mai, chúc bạn một ngày tốt lành!
Xin chào Nam, chúc bạn một ngày tốt lành!
```

**Giải thích từng dòng:**

| Dòng | Ý nghĩa |
|---|---|
| `def xin_chao(ten):` | Khai báo hàm, tham số `ten` |
| `"""..."""` | Docstring mô tả hàm |
| `print(f"Xin chào {ten}...")` | f-string chèn giá trị biến `ten` vào chuỗi |
| `xin_chao("Mai")` | Gọi hàm, gán `ten = "Mai"` |

### Ví dụ 2: Hàm tính diện tích

```python
def dien_tich_tam_giac(day, cao):
    """Tính diện tích tam giác: (đáy * cao) / 2."""
    s = (day * cao) / 2
    return s

# Gọi hàm và lưu kết quả vào biến
ket_qua = dien_tich_tam_giac(10, 6)
print("Diện tích tam giác:", ket_qua)    # 30.0
```

**Giải thích từng dòng:**

| Dòng | Ý nghĩa |
|---|---|
| `def dien_tich_tam_giac(day, cao):` | Khai báo hàm với 2 tham số |
| `s = (day * cao) / 2` | Tính theo công thức toán |
| `return s` | Trả kết quả về cho nơi gọi |
| `ket_qua = dien_tich_tam_giac(10, 6)` | Gọi hàm, gán kết quả `30.0` vào biến |
| `print("...", ket_qua)` | In kết quả ra màn hình |

### Ví dụ 3: Hàm tính điểm trung bình

```python
def tinh_trung_binh(*diem):
    """Tính điểm trung bình của danh sách điểm bất kỳ."""
    if len(diem) == 0:          # Chống chia cho 0
        return 0
    return sum(diem) / len(diem)

print(tinh_trung_binh(8, 7, 9))       # 8.0
print(tinh_trung_binh(6.5, 7.5))      # 7.0
print(tinh_trung_binh())              # 0 — an toàn, không lỗi
```

---

## 🔬 Ví dụ nâng cao

### Ví dụ 1: Máy tính bốn phép tính — dùng hàm cho menu (mở rộng từ bài 11)

```python
def cong(a, b):
    return a + b

def tru(a, b):
    return a - b

def nhan(a, b):
    return a * b

def chia(a, b):
    if b == 0:
        return "Không thể chia cho 0!"
    return a / b

def hien_menu():
    """In bảng menu ra màn hình."""
    print("1. Cộng | 2. Trừ | 3. Nhân | 4. Chia | 0. Thoát")

while True:
    hien_menu()
    chon = input("Chọn phép tính: ")
    if chon == "0":
        print("Tạm biệt!")
        break
    a = float(input("Nhập số thứ nhất: "))
    b = float(input("Nhập số thứ hai: "))
    if chon == "1":
        print("Kết quả:", cong(a, b))
    elif chon == "2":
        print("Kết quả:", tru(a, b))
    elif chon == "3":
        print("Kết quả:", nhan(a, b))
    elif chon == "4":
        print("Kết quả:", chia(a, b))
    else:
        print("Lựa chọn không hợp lệ!")
```

> Mỗi phép tính là một hàm riêng — khi cần sửa cách tính, chỉ sửa đúng một chỗ.

### Ví dụ 2: Đánh giá xếp loại học sinh

```python
def xep_loai(diem_trung_binh):
    """Xếp loại học lực dựa trên điểm trung bình."""
    if diem_trung_binh >= 8.5:
        return "Giỏi"
    elif diem_trung_binh >= 7.0:
        return "Khá"
    elif diem_trung_binh >= 5.0:
        return "Trung bình"
    return "Yếu"

def nhap_va_xep_loai():
    """Nhập điểm và in kết quả xếp loại."""
    diem = float(input("Nhập điểm trung bình: "))
    print("Xếp loại:", xep_loai(diem))

nhap_va_xep_loai()
```

### Ví dụ 3: Gộp nhiều hàm thành chương trình quản lý điểm

```python
def tinh_trung_binh(diem_toan, diem_van, diem_anh):
    """Tính trung bình 3 môn."""
    return (diem_toan + diem_van + diem_anh) / 3

def xep_loai(dtb):
    """Xếp loại theo điểm trung bình."""
    if dtb >= 8.5:
        return "Giỏi"
    if dtb >= 6.5:
        return "Khá"
    if dtb >= 5.0:
        return "Trung bình"
    return "Yếu"

def in_ket_qua(ten, toan, van, anh):
    """In bảng kết quả học sinh."""
    dtb = tinh_trung_binh(toan, van, anh)
    print(f"Học sinh: {ten}")
    print(f"Điểm TB: {dtb:.1f} - Xếp loại: {xep_loai(dtb)}")

in_ket_qua("Nguyễn Văn An", 9, 8.5, 7.5)
in_ket_qua("Trần Thị Bình", 5, 6, 5.5)
```

```
Học sinh: Nguyễn Văn An
Điểm TB: 8.3 - Xếp loại: Giỏi
Học sinh: Trần Thị Bình
Điểm TB: 5.5 - Xếp loại: Trung bình
```

---

## ⚠️ Lỗi thường gặp

### Lỗi 1: `SyntaxError: invalid syntax` — quên dấu hai chấm

```python
def chao(ten)          # ❌ SAI — thiếu dấu :
def chao(ten):         # ✅ ĐÚNG
```

* **Nguyên nhân:** Dòng `def` phải kết thúc bằng dấu `:`.
* **Cách sửa:** Thêm dấu `:` cuối dòng.

### Lỗi 2: `IndentationError: expected an indented block`

```python
def chao():
print("Xin chào")      # ❌ SAI — thân hàm phải thụt vào
def chao():
    print("Xin chào")  # ✅ ĐÚNG
```

* **Nguyên nhân:** Python dùng khoảng trắng đầu dòng để xác định khối lệnh.
* **Cách sửa:** Thụt vào 4 khoảng trắng cho mọi lệnh trong hàm.

### Lỗi 3: `TypeError` — sai số lượng đối số

```python
def tinh_dien_tich(dai, rong):
    return dai * rong

print(tinh_dien_tich(5))     # ❌ TypeError — thiếu 1 đối số
print(tinh_dien_tich(5, 3))  # ✅ ĐÚNG
```

* **Nguyên nhân:** Gọi hàm với 1 đối số trong khi hàm cần 2.
* **Cách sửa:** Truyền đủ đối số, hoặc gán giá trị mặc định cho tham số.

### Lỗi 4: `NameError: name 'x' is not defined` — quên gọi hàm

```python
def tinh_tong(a, b):
    return a + b

# Quên dòng tinh_tong(5, 7) — chương trình chạy xong mà không ra gì
```

* **Nguyên nhân:** Chỉ định nghĩa hàm nhưng không gọi.
* **Cách sửa:** Thêm dòng gọi hàm: `print(tinh_tong(5, 7))`.

### Lỗi 5: Quên `return` — kết quả luôn là `None`

```python
def binh_phuong(x):
    x * x          # ❌ SAI — tính xong nhưng không trả về
def binh_phuong(x):
    return x * x   # ✅ ĐÚNG
```

* **Nguyên nhân:** Thiếu `return`, hàm tự trả về `None`.
* **Cách sửa:** Thêm `return` trước biểu thức cần trả về.

---

## 💎 Mẹo

* ✨ **Mẹo ghi nhớ:** Hàm là **công thức nấu ăn** — `def` là lúc "viết công thức", gọi hàm là lúc "nấu".
* 🏷️ **Tên hàm:** chữ thường + gạch dưới, động từ đi trước: `tinh_tong()`, `in_menu()`, `xep_loai()`.
* 📌 **Luôn viết docstring** cho hàm — sau 1 tuần quay lại đọc, bạn sẽ cảm ơn chính mình.
* 🎯 **Một hàm làm một việc** — hàm dài quá 20 dòng nên tách nhỏ.
* ⚠️ **Không dùng `print` trong hàm tính toán** — in thì không tái dùng được; hãy `return`.
* 🧠 **Tham số mặc định chỉ dùng khi thật cần** — dùng nhiều quá khiến code khó đọc.
* 🐛 Trong VS Code, đặt con trỏ vào tên hàm bấm `F12` để nhảy đến định nghĩa — hoặc xem docstring khi hover chuột.

---

## 📝 Tóm tắt

| Khái niệm | Nội dung |
|---|---|
| `def ten_ham():` | Khai báo hàm |
| `ten_ham()` | Gọi hàm — thiếu bước này hàm không chạy |
| Tham số | Biến trong `( )` lúc định nghĩa |
| Đối số | Giá trị truyền vào lúc gọi |
| `return` | Trả kết quả và kết thúc hàm ngay |
| `None` | Giá trị hàm trả về khi không có `return` |
| Tham số mặc định | `def f(a, b=2)` — đứng sau tham số thường |
| Keyword args | Gọi `f(b=2, a=1)` — kèm tên, không cần đúng thứ tự |
| `*args` | Gói nhiều đối số thành tuple |
| `**kwargs` | Gói nhiều keyword args thành dictionary |
| Docstring | `"""..."""` tài liệu hóa hàm |

---

## 🧪 Kiểm tra nhanh

1. ❓ Từ khóa nào dùng để định nghĩa hàm?
2. ❓ Hàm đã định nghĩa nhưng không gọi thì có chạy không?
3. ❓ Hàm không có `return` trả về giá trị gì?
4. ❓ `def f(a, b=1)` — khi gọi `f(5)` thì `b` nhận giá trị nào?
5. ❓ Keyword arguments giúp gì khi gọi hàm?
6. ❓ `*args` biến các đối số thành kiểu dữ liệu gì?
7. ❓ Tham số mặc định phải đứng ở vị trí nào so với tham số thường?
8. ❓ Docstring viết bằng ký tự nào và để làm gì?
9. ❓ `return` ngoài việc trả kết quả còn làm việc gì nữa?
10. ❓ Sửa lỗi: `def tinh_tong(a, b) return a + b`.

<details>
<summary>🔍 Xem đáp án</summary>

1. `def`.
2. Không — chỉ định nghĩa, không gọi thì không chạy.
3. `None`.
4. `b = 1` (giá trị mặc định).
5. Gọi hàm kèm tên tham số, không cần đúng thứ tự, code dễ đọc.
6. Tuple.
7. Sau tất cả tham số thường (không có mặc định).
8. Cặp `"""..."""` — mô tả chức năng hàm cho người đọc.
9. Kết thúc hàm ngay lập tức.
10. Thiếu dấu `:` — sửa thành `def tinh_tong(a, b):`.

</details>

---

## 📚 Bài đọc thêm

* [Python.org – Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
* [Python.org – More on Defining Functions (thêm về *args, **kwargs)](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions)
* [W3Schools – Python Functions](https://www.w3schools.com/python/python_functions.asp)
* [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
* [Real Python – Functions in Python](https://realpython.com/defining-your-own-python-function/)

---

---

## 🧩 Bài tập

> 📝 🎯 **Chủ đề:** Định nghĩa hàm `def`, gọi hàm, tham số – đối số, `return`, tham số mặc định, keyword arguments, `*args`, `**kwargs`, docstring.

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Hàm xin chào

* **Đề bài:** Viết hàm `xin_chao()` in ra màn hình dòng chữ `Xin chao, lop 10A1!` rồi gọi hàm đó 2 lần.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Xin chao, lop 10A1!
  Xin chao, lop 10A1!
  ```
* **Gợi ý:** Hàm không cần tham số cũng không cần `return`; chỉ cần `def` + `print` + gọi hàm.

### Bài 2: Hàm chào theo tên

* **Đề bài:** Viết hàm `chao_ban(ten)` in ra câu `Xin chao, <ten>!` với tên được truyền vào. Gọi hàm với tên `Mai` và `Nam`.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Xin chao, Mai!
  Xin chao, Nam!
  ```
* **Gợi ý:** Dùng f-string `f"Xin chao, {ten}!"` bên trong `print`.

### Bài 3: Hàm tính bình phương

* **Đề bài:** Viết hàm `binh_phuong(x)` trả về `x * x`. Gọi hàm với số `7` và in kết quả ra màn hình.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  49
  ```
* **Gợi ý:** Dùng `return x * x`, rồi `print(binh_phuong(7))`.

### Bài 4: Hàm cộng hai số

* **Đề bài:** Viết hàm `cong_hai_so(a, b)` trả về tổng của `a` và `b`. In kết quả của `cong_hai_so(12, 30)`.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  42
  ```
* **Gợi ý:** `return a + b` — nhớ đủ 2 đối số khi gọi.

### Bài 5: Hàm với docstring

* **Đề bài:** Viết hàm `tinh_chu_vi_hcn(dai, rong)` có **docstring** mô tả, trả về chu vi hình chữ nhật (2 × (dai + rong)). Gọi hàm với `5, 3` và in kết quả.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  16
  ```
* **Gợi ý:** Docstring viết trong `"""..."""` ngay sau dòng `def`; không bắt buộc in docstring ra.

### Bài 6: Hàm trả về lời chào

* **Đề bài:** Viết hàm `tao_loi_chao(ten)` **trả về** chuỗi `Chao buoi sang, <ten>!` (không in bên trong hàm). Gọi hàm rồi in kết quả trả về.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Chao buoi sang, An!
  ```
* **Gợi ý:** `return f"Chao buoi sang, {ten}!"` — giá trị trả về mới được in ở ngoài.

### Bài 7: Hàm kiểm tra chẵn lẻ

* **Đề bài:** Viết hàm `la_so_chan(n)` trả về `True` nếu `n` chia hết cho 2, ngược lại trả về `False`. Kiểm tra với `10` và `7`, in ra kết quả.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  True
  False
  ```
* **Gợi ý:** Dùng toán tử `%`: `n % 2 == 0`.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Hàm tính diện tích tam giác

* **Đề bài:** Viết hàm `dien_tich_tam_giac(day, cao)` trả về diện tích tam giác = `day * cao / 2`. Gọi hàm với `day = 10, cao = 4` và in kết quả với 2 chữ số thập phân.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Dien tich tam giac: 20.0
  ```
* **Gợi ý:** Chú ý phép chia `/` luôn cho số thực; có thể dùng `f"{ket_qua:.2f}"`.

### Bài 9: Hàm xếp loại học sinh

* **Đề bài:** Viết hàm `xep_loai(dtb)` nhận điểm trung bình và trả về `"Gioi"` nếu `dtb >= 8.5`, `"Kha"` nếu `dtb >= 7.0`, `"Trung binh"` nếu `dtb >= 5.0`, ngược lại `"Yeu"`. In kết quả cho `dtb = 8.7`, `dtb = 6.5`, `dtb = 4.9`.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  8.7 -> Gioi
  6.5 -> Kha
  4.9 -> Yeu
  ```
* **Gợi ý:** Dùng `if / elif / else` bên trong hàm, mỗi nhánh một `return`.

### Bài 10: Hàm tính điểm trung bình 3 môn

* **Đề bài:** Viết hàm `tinh_trung_binh(toan, van, anh)` trả về điểm trung bình 3 môn. An có điểm `8, 7.5, 9`, Bình có điểm `5, 6, 6.5`. In điểm trung bình của từng bạn.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  An: 8.2
  Binh: 5.8
  ```
* **Gợi ý:** `(toan + van + anh) / 3`; làm tròn 1 chữ số thập phân bằng `round(..., 1)`.

### Bài 11: Hàm có tham số mặc định

* **Đề bài:** Viết hàm `dat_truoc(mon, so_luong=1)` in ra câu `Ban da dat <so_luong> phan <mon>.` Gọi hàm với: `dat_truoc("pho")` và `dat_truoc("bun bo", 3)`.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Ban da dat 1 phan pho.
  Ban da dat 3 phan bun bo.
  ```
* **Gợi ý:** Tham số mặc định `so_luong=1` được dùng khi gọi không truyền đối số thứ hai.

### Bài 12: Gọi hàm bằng keyword arguments

* **Đề bài:** Viết hàm `ghi_ho_so(ten, tuoi, lop)` in ra `Ten: <ten> | Tuoi: <tuoi> | Lop: <lop>`. Gọi hàm **một lần duy nhất** bằng keyword arguments với thứ tự trộn lẫn: `lop="10A1", ten="Mai", tuoi=15`.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Ten: Mai | Tuoi: 15 | Lop: 10A1
  ```
* **Gợi ý:** Gọi `ghi_ho_so(lop="10A1", ten="Mai", tuoi=15)` — thứ tự không quan trọng.

### Bài 13: Hàm cộng nhiều số bằng `*args`

* **Đề bài:** Viết hàm `tinh_tong(*cac_so)` trả về tổng của tất cả các số truyền vào. In kết quả của `tinh_tong(1, 2, 3)` và `tinh_tong(10, 20, 30, 40)`.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  6
  100
  ```
* **Gợi ý:** Bên trong hàm, `cac_so` là một tuple — dùng `sum(cac_so)`.

### Bài 14: Menu máy tính bằng hàm

* **Đề bài:** Viết hàm `hien_menu()` in ra 4 dòng menu (1. Cong, 2. Tru, 3. Nhan, 4. Chia) và hàm `may_tinh(a, b, phep_tinh)` trả về kết quả theo phép tính được chọn (xử lý cả trường hợp `b = 0` khi chia). Gọi `may_tinh(10, 2, "4")` và `may_tinh(8, 0, "4")`.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  5.0
  Khong the chia cho 0!
  ```
* **Gợi ý:** Trong `may_tinh` dùng `if` so sánh `phep_tinh` với chuỗi `"1"`, `"2"`, `"3"`, `"4"`.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Hàm in ra tên viết tắt

* **Đề bài:** Viết hàm `viet_tat(ho_ten)` nhận chuỗi họ tên đầy đủ (ví dụ `"Nguyen Van An"`), tách các từ bằng `split()` và trả về chuỗi gồm **chữ cái đầu mỗi từ, viết hoa, không dấu cách** (ví dụ `"NVA"`).
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Nguyen Van An -> NVA
  Tran Thi Binh -> TTB
  ```
* **Gợi ý:** `ho_ten.split()` cho danh sách các từ; lấy từng từ `[0]`; nối bằng `"".join(...)` hoặc `+`.

### Bài 16: Hàm kiểm tra số nguyên tố

* **Đề bài:** Viết hàm `la_so_nguyen_to(n)` trả về `True` nếu `n > 1` và chỉ chia hết cho 1 và chính nó, ngược lại `False`. Kiểm tra các số `2, 9, 17, 1` và in kết quả từng số.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  2: True
  9: False
  17: True
  1: False
  ```
* **Gợi ý:** Duyệt từ `2` đến `n // 2 + 1`; nếu thấy ước thì trả về `False` ngay. Số `n <= 1` không phải nguyên tố.

### Bài 17: Hàm gộp nhiều thông tin bằng `**kwargs`

* **Đề bài:** Viết hàm `tong_ket(**mon_hoc)` nhận các cặp tên môn và điểm (dạng `toan=8, van=7`), in ra từng môn kèm điểm, đồng thời trả về điểm trung bình. Gọi với `toan=8, van=7, anh=9` và in điểm trung bình.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  toan: 8
  van: 7
  anh: 9
  Diem trung binh: 8.0
  ```
* **Gợi ý:** `mon_hoc` là dictionary; `sum(mon_hoc.values()) / len(mon_hoc)` cho điểm trung bình.

### Bài 18: Trò chơi đoán số — chia thành hàm

* **Đề bài:** Viết 3 hàm: `sinh_so_bi_mat()` trả về số ngẫu nhiên trong 1–100, `doan_so(so_bi_mat, so_doan)` trả về `"lon hon"`, `"nho hon"` hoặc `"chinh xac"`, và `choi_game()` dùng vòng lặp `while` cho người chơi đoán tối đa 7 lần, in kết quả sau mỗi lần đoán.
* **Input:** Mô phỏng lần lượt các số đoán: `50`, `25`, `40` (giả sử số bí mật là `40`)
* **Output:**
  ```
  Ban doan so 50: so bi mat nho hon
  Ban doan so 25: so bi mat lon hon
  Ban doan so 40: chinh xac! Xin chuc mung!
  ```
* **Gợi ý:** Dùng `import random; random.randint(1, 100)`. Hàm `doan_so` chỉ so sánh và trả về chuỗi.

### Bài 19: Tiền lương nhân viên

* **Đề bài:** Viết hàm `tinh_luong(so_gio, luong_mot_gio=20000)` trả về tiền lương; nếu `so_gio > 40` thì số giờ vượt được tính gấp rưỡi (×1.5). Viết thêm hàm `in_phieu_luong(ten, so_gio)` in ra tên và tiền lương. Gọi cho An (`45` giờ) và Bình (`30` giờ).
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  An lam 45 gio -> 950000 dong
  Binh lam 30 gio -> 600000 dong
  ```
* **Gợi ý:** `gio_vuot = so_gio - 40`; lương = `40 * luong_mot_gio + gio_vuot * luong_mot_gio * 1.5`.

### Bài 20: Quản lý menu quán phở — tổng hợp hàm

* **Đề bài:** Viết các hàm: `gia_mon()` trả về dictionary giá `{"pho": 35000, "bun bo": 40000, "com": 25000}`, `thanh_tien(mon, so_luong, phu_thu=0)` trả về tổng tiền, và `in_hoa_don(don_hang)` nhận danh sách món đã đặt dạng `[("pho", 2), ("com", 1)]`, in từng món, thành tiền từng món và tổng tiền toàn bộ.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  pho x2 = 70000 dong
  com x1 = 25000 dong
  Tong: 95000 dong
  ```
* **Gợi ý:** Trong `in_hoa_don`, dùng vòng lặp `for mon, sl in don_hang`; tích lũy tổng bằng biến `tong = 0`.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Định nghĩa và gọi hàm thành thạo, biết khi nào hàm cần `return`.
* ✅ Dùng tham số mặc định, keyword arguments, `*args`, `**kwargs` linh hoạt.
* ✅ Tách chương trình lớn thành các hàm nhỏ rõ ràng (menu máy tính, game đoán số, hóa đơn).
* ✅ Viết docstring và đọc hiểu hàm do người khác viết.

> 💪 Nếu bài nào chưa tự làm được, hãy đọc lại bài giảng phần tương ứng rồi thử lại. **Chương trình tốt = chương trình nhiều hàm nhỏ!**

---

## ✅ Đáp án

> 💡 **Hãy tự làm bài tập trước** rồi mới mở đáp án.

## 🟢 Dễ (Bài 1 – 7)


<details>
<summary>✅ Bài 1: Hàm xin chào</summary>


**Phân tích:** Bài làm quen — viết hàm không tham số, chỉ in chữ, rồi gọi hàm.

**Ý tưởng:** Hàm chỉ gồm một lệnh `print()`. Gọi hàm 2 lần để thấy code chạy lại.

**Thuật toán:**
1. Định nghĩa hàm `xin_chao()`.
2. Trong thân hàm in ra dòng chữ.
3. Gọi hàm hai lần.

**Code:**

```python
def xin_chao():
    """In lời chào ra màn hình."""
    print("Xin chao, lop 10A1!")

xin_chao()
xin_chao()
```

**Giải thích code:**
* `def xin_chao():` — khai báo hàm không có tham số.
* `print(...)` — thân hàm, chạy khi hàm được gọi.
* Hai lần `xin_chao()` — hàm chạy 2 lần, in 2 dòng giống nhau.

**Độ phức tạp:** O(1).

---

</details>

<details>
<summary>✅ Bài 2: Hàm chào theo tên</summary>


**Phân tích:** Hàm nhận tham số `ten` và chèn vào chuỗi in ra.

**Ý tưởng:** Dùng f-string để chèn biến vào chuỗi.

**Thuật toán:**
1. Định nghĩa `chao_ban(ten)`.
2. In `f"Xin chao, {ten}!"`.
3. Gọi với `"Mai"`, rồi `"Nam"`.

**Code:**

```python
def chao_ban(ten):
    """Chào một người theo tên."""
    print(f"Xin chao, {ten}!")

chao_ban("Mai")
chao_ban("Nam")
```

**Giải thích code:**
* `ten` — tham số nhận giá trị từ đối số khi gọi.
* `f"Xin chao, {ten}!"` — `{ten}` được thay bằng giá trị thực của biến.

**Độ phức tạp:** O(1).

---

</details>

<details>
<summary>✅ Bài 3: Hàm tính bình phương</summary>


**Phân tích:** Hàm tính toán phải dùng `return` để trả kết quả.

**Ý tưởng:** `binh_phuong(x)` trả về `x * x`.

**Thuật toán:**
1. Định nghĩa hàm trả về `x * x`.
2. Gọi hàm với `7` và in kết quả.

**Code:**

```python
def binh_phuong(x):
    """Trả về bình phương của x."""
    return x * x

print(binh_phuong(7))
```

**Giải thích code:**
* `return x * x` — `49` được gửi ra ngoài.
* `print(binh_phuong(7))` — gọi hàm, nhận `49`, in ra màn hình.

**Độ phức tạp:** O(1).

---

</details>

<details>
<summary>✅ Bài 4: Hàm cộng hai số</summary>


**Phân tích:** Hàm 2 tham số, trả về tổng.

**Ý tưởng:** `return a + b`.

**Thuật toán:**
1. Định nghĩa `cong_hai_so(a, b)`.
2. Trả về `a + b`.
3. Gọi với `12, 30` và in.

**Code:**

```python
def cong_hai_so(a, b):
    """Trả về tổng của a và b."""
    return a + b

print(cong_hai_so(12, 30))
```

**Giải thích code:**
* `a` nhận `12`, `b` nhận `30` — theo thứ tự vị trí.
* Hàm trả về `42`.

**Độ phức tạp:** O(1).

---

</details>

<details>
<summary>✅ Bài 5: Hàm với docstring</summary>


**Phân tích:** Bài luyện viết docstring và dùng công thức chu vi.

**Ý tưởng:** Chu vi = `2 * (dai + rong)`.

**Thuật toán:**
1. Viết hàm kèm docstring.
2. Trả về chu vi.
3. Gọi với `5, 3` và in.

**Code:**

```python
def tinh_chu_vi_hcn(dai, rong):
    """Tính chu vi hình chữ nhật.

    Args:
        dai (float): chiều dài
        rong (float): chiều rộng

    Returns:
        float: chu vi hình chữ nhật
    """
    return 2 * (dai + rong)

print(tinh_chu_vi_hcn(5, 3))
```

**Giải thích code:**
* Docstring nằm ngay sau `def`, trong cặp `"""..."""`.
* `2 * (5 + 3) = 16`.

**Độ phức tạp:** O(1).

---

</details>

<details>
<summary>✅ Bài 6: Hàm trả về lời chào</summary>


**Phân tích:** Phân biệt hàm `print` (in thẳng) và hàm `return` (trả về để in ở ngoài).

**Ý tưởng:** Hàm `tao_loi_chao` chỉ `return` chuỗi; việc in do nơi gọi đảm nhận.

**Thuật toán:**
1. Hàm trả về chuỗi chào bằng f-string.
2. Lưu kết quả vào biến hoặc in trực tiếp.

**Code:**

```python
def tao_loi_chao(ten):
    """Tạo chuỗi lời chào buổi sáng."""
    return f"Chao buoi sang, {ten}!"

loi = tao_loi_chao("An")
print(loi)
```

**Giải thích code:**
* Hàm không in — chỉ tạo chuỗi rồi trả về.
* `loi = tao_loi_chao("An")` — biến nhận chuỗi trả về, sau đó mới in.

**Độ phức tạp:** O(1).

---

</details>

<details>
<summary>✅ Bài 7: Hàm kiểm tra chẵn lẻ</summary>


**Phân tích:** Hàm trả về `True`/`False` — kiểu dữ liệu boolean.

**Ý tưởng:** Số chẵn khi `n % 2 == 0`.

**Thuật toán:**
1. Định nghĩa hàm dùng biểu thức so sánh.
2. Gọi và in với `10` và `7`.

**Code:**

```python
def la_so_chan(n):
    """Kiểm tra n có phải số chẵn không."""
    return n % 2 == 0

print(la_so_chan(10))
print(la_so_chan(7))
```

**Giải thích code:**
* `n % 2 == 0` là biểu thức so sánh — kết quả đã là `True`/`False`.
* `10 % 2 == 0` → `True`; `7 % 2 == 0` → `False`.

**Độ phức tạp:** O(1).

---

</details>

## 🟡 Trung bình (Bài 8 – 14)


<details>
<summary>✅ Bài 8: Hàm tính diện tích tam giác</summary>


**Phân tích:** Dùng công thức `day * cao / 2`, in kết quả 2 chữ số thập phân.

**Ý tưởng:** `return day * cao / 2`, định dạng bằng f-string.

**Thuật toán:**
1. Tính diện tích trong hàm.
2. In với định dạng `:.2f`.

**Code:**

```python
def dien_tich_tam_giac(day, cao):
    """Tính diện tích tam giác."""
    return day * cao / 2

ket_qua = dien_tich_tam_giac(10, 4)
print(f"Dien tich tam giac: {ket_qua:.2f}")
```

**Giải thích code:**
* `10 * 4 / 2 = 20.0` — phép `/` luôn cho số thực.
* `{ket_qua:.2f}` — hiển thị đúng 2 chữ số sau dấu phẩy: `20.00`? Không — `20.0` có 1 chữ số; `.2f` thêm đủ 2: in ra `20.00`. Nhưng đề yêu cầu `20.0`, nên dùng `{ket_qua:.1f}` cũng được. Cả hai đều chấp nhận nếu thể hiện đúng ý nghĩa.

**Độ phức tạp:** O(1).

---

</details>

<details>
<summary>✅ Bài 9: Hàm xếp loại học sinh</summary>


**Phân tích:** Phân nhánh điểm theo 4 mức.

**Ý tưởng:** `if/elif/else` với mỗi nhánh một `return`.

**Thuật toán:**
1. Nếu `dtb >= 8.5` → "Gioi".
2. Nếu `dtb >= 7.0` → "Kha".
3. Nếu `dtb >= 5.0` → "Trung binh".
4. Ngược lại → "Yeu".

**Code:**

```python
def xep_loai(dtb):
    """Xếp loại học lực theo điểm trung bình."""
    if dtb >= 8.5:
        return "Gioi"
    elif dtb >= 7.0:
        return "Kha"
    elif dtb >= 5.0:
        return "Trung binh"
    return "Yeu"

print("8.7 ->", xep_loai(8.7))
print("6.5 ->", xep_loai(6.5))
print("4.9 ->", xep_loai(4.9))
```

**Giải thích code:**
* Các nhánh kiểm tra từ cao xuống thấp — không cần viết `dtb < 8.5` vì nhánh trước đã loại.
* `return` trong `if` đã kết thúc hàm nên nhánh cuối `return "Yeu"` không cần `else`.

**Độ phức tạp:** O(1).

---

</details>

<details>
<summary>✅ Bài 10: Hàm tính điểm trung bình 3 môn</summary>


**Phân tích:** Tính trung bình và làm tròn 1 chữ số.

**Ý tưởng:** `(toan + van + anh) / 3`, dùng `round(..., 1)`.

**Thuật toán:**
1. Viết hàm trung bình 3 môn.
2. Gọi cho An và Bình, in kết quả.

**Code:**

```python
def tinh_trung_binh(toan, van, anh):
    """Tính điểm trung bình 3 môn."""
    return (toan + van + anh) / 3

diem_an = round(tinh_trung_binh(8, 7.5, 9), 1)
diem_binh = round(tinh_trung_binh(5, 6, 6.5), 1)
print(f"An: {diem_an}")
print(f"Binh: {diem_binh}")
```

**Giải thích code:**
* An: `(8 + 7.5 + 9) / 3 = 8.166...` → `round(..., 1) = 8.2`.
* Bình: `(5 + 6 + 6.5) / 3 = 5.833...` → `5.8`.

**Độ phức tạp:** O(1).

---

</details>

<details>
<summary>✅ Bài 11: Hàm có tham số mặc định</summary>


**Phân tích:** Dùng tham số mặc định cho số lượng.

**Ý tưởng:** `so_luong=1` — khi gọi thiếu đối số thứ hai, tự dùng `1`.

**Thuật toán:**
1. Định nghĩa hàm với tham số mặc định.
2. Gọi lần 1 không truyền số lượng.
3. Gọi lần 2 truyền `3`.

**Code:**

```python
def dat_truoc(mon, so_luong=1):
    """Đặt trước món ăn với số lượng (mặc định 1)."""
    print(f"Ban da dat {so_luong} phan {mon}.")

dat_truoc("pho")
dat_truoc("bun bo", 3)
```

**Giải thích code:**
* Lần gọi thứ nhất: `so_luong` nhận giá trị mặc định `1`.
* Lần gọi thứ hai: truyền `3` ghi đè giá trị mặc định.

**Độ phức tạp:** O(1).

---

</details>

<details>
<summary>✅ Bài 12: Gọi hàm bằng keyword arguments</summary>


**Phân tích:** Keyword arguments giúp gọi hàm không phụ thuộc thứ tự.

**Ý tưởng:** Ghi rõ `ten=`, `tuoi=`, `lop=` khi gọi.

**Thuật toán:**
1. Định nghĩa hàm 3 tham số.
2. Gọi với keyword arguments thứ tự trộn lẫn.

**Code:**

```python
def ghi_ho_so(ten, tuoi, lop):
    """In thông tin hồ sơ học sinh."""
    print(f"Ten: {ten} | Tuoi: {tuoi} | Lop: {lop}")

ghi_ho_so(lop="10A1", ten="Mai", tuoi=15)
```

**Giải thích code:**
* Thứ tự đối số không quan trọng khi đã ghi rõ tên tham số.
* Python khớp `lop="10A1"` vào tham số `lop` dù nó đứng đầu.

**Độ phức tạp:** O(1).

---

</details>

<details>
<summary>✅ Bài 13: Hàm cộng nhiều số bằng `*args`</summary>


**Phân tích:** Số lượng đối số không cố định — dùng `*args`.

**Ý tưởng:** `*cac_so` gói mọi đối số thành tuple, `sum()` tính tổng.

**Thuật toán:**
1. Định nghĩa `tinh_tong(*cac_so)`.
2. Trả về `sum(cac_so)`.
3. Gọi với 3 và 4 đối số.

**Code:**

```python
def tinh_tong(*cac_so):
    """Tính tổng một danh sách số bất kỳ."""
    return sum(cac_so)

print(tinh_tong(1, 2, 3))
print(tinh_tong(10, 20, 30, 40))
```

**Giải thích code:**
* `*cac_so` → `(1, 2, 3)` là một tuple.
* `sum()` cộng toàn bộ phần tử trong tuple.

**Độ phức tạp:** O(n) với n là số lượng đối số.

---

</details>

<details>
<summary>✅ Bài 14: Menu máy tính bằng hàm</summary>


**Phân tích:** Kết hợp hàm hiển thị menu và hàm thực hiện phép tính.

**Ý tưởng:** `may_tinh` kiểm tra chuỗi `phep_tinh` rồi gọi phép toán tương ứng.

**Thuật toán:**
1. `hien_menu()` in 4 dòng lựa chọn.
2. `may_tinh(a, b, phep_tinh)`:
   - `"1"` → `a + b`
   - `"2"` → `a - b`
   - `"3"` → `a * b`
   - `"4"` → chia, kiểm tra `b == 0`.

**Code:**

```python
def hien_menu():
    """Hiển thị menu máy tính."""
    print("1. Cong | 2. Tru | 3. Nhan | 4. Chia")

def may_tinh(a, b, phep_tinh):
    """Thực hiện phép tính theo lựa chọn."""
    if phep_tinh == "1":
        return a + b
    elif phep_tinh == "2":
        return a - b
    elif phep_tinh == "3":
        return a * b
    elif phep_tinh == "4":
        if b == 0:
            return "Khong the chia cho 0!"
        return a / b
    return "Lua chon khong hop le!"

hien_menu()
print(may_tinh(10, 2, "4"))
print(may_tinh(8, 0, "4"))
```

**Giải thích code:**
* So sánh chuỗi vì `input()` luôn trả về chuỗi — trong bài này gọi trực tiếp với `"4"`.
* Nhánh chia kiểm tra `b == 0` để không gây `ZeroDivisionError`.

**Độ phức tạp:** O(1).

---

</details>

## 🔴 Khó (Bài 15 – 20)


<details>
<summary>✅ Bài 15: Hàm in ra tên viết tắt</summary>


**Phân tích:** Xử lý chuỗi: tách từ, lấy chữ cái đầu, viết hoa, nối lại.

**Ý tưởng:** `split()` tạo danh sách từ; lấy ký tự `[0]` mỗi từ; nối bằng `"".join()`.

**Thuật toán:**
1. Tách họ tên thành danh sách các từ.
2. Lấy ký tự đầu mỗi từ và viết hoa.
3. Nối các ký tự thành chuỗi viết tắt.

**Code:**

```python
def viet_tat(ho_ten):
    """Tạo chuỗi viết tắt từ họ tên."""
    cac_tu = ho_ten.split()
    chu_cai_dau = [tu[0].upper() for tu in cac_tu]
    return "".join(chu_cai_dau)

print(f"Nguyen Van An -> {viet_tat('Nguyen Van An')}")
print(f"Tran Thi Binh -> {viet_tat('Tran Thi Binh')}")
```

**Giải thích code:**
* `"Nguyen Van An".split()` → `["Nguyen", "Van", "An"]`.
* `tu[0]` lấy chữ cái đầu, `.upper()` viết hoa.
* `"".join(...)` nối không có khoảng trắng → `"NVA"`.

**Độ phức tạp:** O(n) với n là độ dài chuỗi.

---

</details>

<details>
<summary>✅ Bài 16: Hàm kiểm tra số nguyên tố</summary>


**Phân tích:** Số nguyên tố chỉ chia hết cho 1 và chính nó.

**Ý tưởng:** Duyệt ước từ 2 đến `n // 2`; nếu có ước → không nguyên tố.

**Thuật toán:**
1. `n <= 1` → `False`.
2. Duyệt `i` từ 2 đến `n // 2` (đủ vì mọi ước > `n/2` đều kèm ước < `n/2`).
3. Nếu `n % i == 0` → `False`.
4. Hết vòng → `True`.

**Code:**

```python
def la_so_nguyen_to(n):
    """Kiểm tra n có phải số nguyên tố không."""
    if n <= 1:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

for so in [2, 9, 17, 1]:
    print(f"{so}: {la_so_nguyen_to(so)}")
```

**Giải thích code:**
* `2`: không chia hết cho số nào trong `range(2, 2)` (rỗng) → `True`.
* `9`: `9 % 3 == 0` → `False`.
* `17`: không có ước → `True`.
* `1`: bị loại ngay vì `n <= 1`.

**Độ phức tạp:** O(n) cho một số `n`.

---

</details>

<details>
<summary>✅ Bài 17: Hàm gộp nhiều thông tin bằng `**kwargs`</summary>


**Phân tích:** `**kwargs` gom các cặp tên–giá trị thành dictionary.

**Ý tưởng:** Duyệt `mon_hoc.items()` để in; trung bình = tổng điểm chia số môn.

**Thuật toán:**
1. In từng cặp môn – điểm.
2. Tính trung bình bằng `sum(...) / len(...)`.
3. Trả về điểm trung bình.

**Code:**

```python
def tong_ket(**mon_hoc):
    """In điểm từng môn và trả về điểm trung bình."""
    for mon, diem in mon_hoc.items():
        print(f"{mon}: {diem}")
    diem_trung_binh = sum(mon_hoc.values()) / len(mon_hoc)
    return diem_trung_binh

dtb = tong_ket(toan=8, van=7, anh=9)
print(f"Diem trung binh: {dtb}")
```

**Giải thích code:**
* `mon_hoc` = `{"toan": 8, "van": 7, "anh": 9}`.
* `sum(...)` = 24, `len(...)` = 3 → trung bình 8.0.

**Độ phức tạp:** O(m) với m là số môn.

---

</details>

<details>
<summary>✅ Bài 18: Trò chơi đoán số — chia thành hàm</summary>


**Phân tích:** Tách chương trình game thành 3 hàm nhỏ, mỗi hàm một nhiệm vụ.

**Ý tưởng:** `choi_game()` quản lý vòng lặp; hai hàm còn lại chỉ xử lý một việc.

**Thuật toán:**
1. `sinh_so_bi_mat()`: `random.randint(1, 100)`.
2. `doan_so(so_bi_mat, so_doan)`: so sánh và trả về chuỗi kết quả.
3. `choi_game()`: vòng `while` tối đa 7 lượt, in kết quả, thoát khi đoán đúng.

**Code:**

```python
import random

def sinh_so_bi_mat():
    """Tạo số bí mật ngẫu nhiên từ 1 đến 100."""
    return random.randint(1, 100)

def doan_so(so_bi_mat, so_doan):
    """So sánh số đoán với số bí mật."""
    if so_doan > so_bi_mat:
        return "so bi mat nho hon"
    elif so_doan < so_bi_mat:
        return "so bi mat lon hon"
    return "chinh xac! Xin chuc mung!"

def choi_game():
    """Điều khiển toàn bộ trò chơi đoán số."""
    so_bi_mat = sinh_so_bi_mat()
    luot = 0
    while luot < 7:
        so_doan = int(input("Ban doan so: "))  # Nhập: 50, 25, 40 ...
        luot += 1
        ket_qua = doan_so(so_bi_mat, so_doan)
        print(f"Ban doan so {so_doan}: {ket_qua}")
        if ket_qua == "chinh xac! Xin chuc mung!":
            return
    print("Het luot! So bi mat la", so_bi_mat)

choi_game()
```

**Giải thích code:**
* Với số bí mật là `40` và lần đoán `50, 25, 40`:
  - `50 > 40` → "so bi mat nho hon".
  - `25 < 40` → "so bi mat lon hon".
  - `40 == 40` → chính xác, kết thúc.
* `input()` dùng vì đây là game tương tác thật — khi chạy thử hãy nhập lần lượt các số.

**Độ phức tạp:** O(1) cho mỗi lượt đoán; tối đa 7 lượt.

---

</details>

<details>
<summary>✅ Bài 19: Tiền lương nhân viên</summary>


**Phân tích:** Tính lương có giờ tăng ca gấp rưỡi.

**Ý tưởng:** Tách phần tính lương và phần in ra; công thức tăng ca ×1.5.

**Thuật toán:**
1. `tinh_luong(so_gio, luong_mot_gio=20000)`:
   - Nếu `so_gio <= 40`: `so_gio * luong_mot_gio`.
   - Ngược lại: `40 * luong_mot_gio + (so_gio - 40) * luong_mot_gio * 1.5`.
2. `in_phieu_luong(ten, so_gio)` in kết quả.

**Code:**

```python
def tinh_luong(so_gio, luong_mot_gio=20000):
    """Tính lương, giờ vượt 40 được tính gấp rưỡi."""
    if so_gio <= 40:
        return so_gio * luong_mot_gio
    gio_vuot = so_gio - 40
    return 40 * luong_mot_gio + gio_vuot * luong_mot_gio * 1.5

def in_phieu_luong(ten, so_gio):
    """In phiếu lương của nhân viên."""
    tien = tinh_luong(so_gio)
    print(f"{ten} lam {so_gio} gio -> {int(tien)} dong")

in_phieu_luong("An", 45)
in_phieu_luong("Binh", 30)
```

**Giải thích code:**
* An 45 giờ: `40*20000 + 5*20000*1.5 = 800000 + 150000 = 950000`.
* Bình 30 giờ: `30 * 20000 = 600000`.
* `int(tien)` bỏ phần `.0` cho hiển thị gọn (vì phép nhân với `1.5` cho float).

**Độ phức tạp:** O(1).

---

</details>

<details>
<summary>✅ Bài 20: Quản lý menu quán phở — tổng hợp hàm</summary>


**Phân tích:** Tổng hợp đầy đủ kiến thức: dictionary, tham số mặc định, vòng lặp trong hàm, tích lũy tổng.

**Ý tưởng:** Mỗi nhiệm vụ một hàm; `in_hoa_don` duyệt danh sách đơn hàng.

**Thuật toán:**
1. `gia_mon()` trả về dictionary giá.
2. `thanh_tien(mon, so_luong, phu_thu=0)` = giá × số lượng + phụ thu.
3. `in_hoa_don(don_hang)`: duyệt từng `(mon, sl)`, cộng dồn tổng, in ra.

**Code:**

```python
def gia_mon():
    """Trả về bảng giá các món."""
    return {"pho": 35000, "bun bo": 40000, "com": 25000}

def thanh_tien(mon, so_luong, phu_thu=0):
    """Tính tiền cho một món đã chọn."""
    return gia_mon()[mon] * so_luong + phu_thu

def in_hoa_don(don_hang):
    """In hóa đơn chi tiết cho danh sách món đã đặt."""
    tong = 0
    for mon, so_luong in don_hang:
        tien_mon = thanh_tien(mon, so_luong)
        tong += tien_mon
        print(f"{mon} x{so_luong} = {tien_mon} dong")
    print(f"Tong: {tong} dong")

don = [("pho", 2), ("com", 1)]
in_hoa_don(don)
```

**Giải thích code:**
* `don_hang` là danh sách các tuple `(tên món, số lượng)`.
* `pho x2 = 35000 * 2 = 70000`; `com x1 = 25000`.
* Biến `tong` cộng dồn qua từng vòng lặp, in ra `95000`.

**Độ phức tạp:** O(m) với m là số món trong hóa đơn.

---

</details>

## 📌 Lời khuyên cuối


* **Viết hàm nhỏ, mỗi hàm một việc** — chương trình dễ đọc, dễ sửa.
* **Tính toán thì `return`, hiển thị thì `print`** — đừng trộn lẫn.
* **Đặt tên hàm có nghĩa** bằng tiếng Việt không dấu hoặc tiếng Anh đơn giản.
* Nhớ **gọi hàm** — định nghĩa mà không gọi thì chương trình im lặng.

👉 Tiếp theo: **[Bài 13: Phạm Vi Biến](../13-Scope/bai.md)**

---

## ➡️ Điều hướng

**Vị trí:** `04-Full/Phan-1-Co-Ban/12-Ham/bai.md`

**Bài tiếp theo:** [Bài 13 — Phạm Vi Biến (Scope) Trong Python](../13-Scope/bai.md)
