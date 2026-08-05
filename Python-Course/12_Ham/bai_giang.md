# 🐍 Bài 12: Hàm (Function) Trong Python

> 🎓 **Chương 4 – Tự động hóa công việc lặp lại**

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

## 🏁 Kết thúc bài

🎉 Bạn đã biết cách đóng gói code vào hàm — chương trình giờ gọn gàng và tái sử dụng được. Câu hỏi tiếp theo rất tự nhiên: **biến bên trong hàm và biến ngoài chương trình có quan hệ gì? Viết trùng tên có sao không?** Đó chính là nội dung bài sau — hãy sang:

👉 **[Bài 13: Phạm Vi Biến (Scope)](../13_Scope/bai_giang.md)**
