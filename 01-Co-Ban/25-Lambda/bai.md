# Bài 25 — Lambda – Hàm Vô Danh Siêu Ngắn Gọn

> 🎓 **Chương 5 – Lập trình hướng đối tượng & các công cụ nâng cao**

## 🧠 Điều kiện tiên quyết

- [Bài 12 — Hàm (Function) Trong Python](../12-Ham/bai.md)

---

## 🎯 Mục tiêu

Sau bài học này, học viên sẽ:

* ✅ Hiểu **lambda là gì** — "hàm vô danh" chỉ một dòng, không cần `def` và tên hàm.
* ✅ Viết được cú pháp `lambda thamso: bieuthuc` thành thạo.
* ✅ Biết dùng lambda với **`sorted(key=...)`** để sắp xếp theo tiêu chí riêng.
* ✅ Biết dùng lambda với **`filter`** và **`map`** để lọc và biến đổi dữ liệu.
* ✅ Nắm được **hạn chế** của lambda (chỉ một biểu thức, khó đọc khi quá phức tạp).
* ✅ Lập được **bảng so sánh** `def` vs `lambda` để chọn đúng công cụ.

---

## 📖 Kiến thức

### 1. Hàm thường đã có `def`, vì sao cần lambda?

Ở [Bài 12 – Hàm](../12-Ham/bai.md), ta định nghĩa hàm bằng `def`:

```python
def binh_phuong(x):
    return x * x

print(binh_phuong(5))   # 25
```

Vấn đề nảy sinh khi ta chỉ cần một **hàm dùng một lần** — ví dụ truyền vào `sorted()` để sắp xếp. Viết hẳn một hàm `def` có tên thì tốn 2-3 dòng, mà dùng xong rồi cũng chẳng ai gọi lại. Giống như bạn chỉ cần gọi taxi **một lần** — đâu cần mua hẳn một chiếc xe!

> 💬 **Nói đơn giản:** Lambda là "chiếc taxi" — tạo ra để dùng ngay, dùng xong không cần nhớ tên. Nó là **hàm vô danh** (anonymous function).

### 2. Cú pháp lambda

```python
lambda thamso1, thamso2: bieuthuc_tra_ve
```

| Thành phần | Ý nghĩa |
|---|---|
| `lambda` | Từ khóa khai báo hàm vô danh |
| `thamso1, thamso2` | Danh sách tham số (có thể 0, 1 hoặc nhiều) |
| `:` | Ngăn cách phần tham số và phần thân |
| `bieuthuc_tra_ve` | **Một biểu thức duy nhất** — giá trị của nó chính là kết quả trả về |

**Ví dụ so sánh hai cách viết:**

```python
# Cách 1: hàm thường
def binh_phuong(x):
    return x * x

# Cách 2: lambda — một dòng
binh_phuong = lambda x: x * x

print(binh_phuong(5))   # 25
```

> ⚠️ **Luật vàng:** lambda **chỉ chứa một biểu thức** — không có lệnh `if...else` nhiều nhánh, không có vòng lặp, không có nhiều dòng. Cần phức tạp hơn → dùng `def`.

### 3. Dùng lambda với sorted(key=...)

Hàm `sorted()` sắp xếp danh sách. Tham số `key` quy định **lấy giá trị nào để so sánh**:

```python
hoc_sinh = [("An", 8.5), ("Bình", 6.0), ("Cường", 9.0)]

# Sắp theo điểm (phần tử thứ 1 của tuple) — tăng dần
sx = sorted(hoc_sinh, key=lambda hs: hs[1])
print(sx)   # [('Bình', 6.0), ('An', 8.5), ('Cường', 9.0)]
```

* Nếu không có `key`, Python sắp theo cả tuple: ưu tiên tên trước.
* Với `key=lambda hs: hs[1]`, Python "hỏi" mỗi phần tử: "giá trị so sánh của mày là gì?" → là điểm số.

```mermaid
flowchart LR
    A[Danh sách học sinh] --> B[key = lambda hs: hs[1]]
    B -->|mỗi phần tử trả về điểm| C[sorted so sánh theo điểm]
    C --> D[Danh sách đã sắp xếp]
```

> 💡 `sorted` **không sửa** danh sách gốc, trả về danh sách mới. Muốn sửa ngay danh sách cũ thì dùng `list.sort(key=...)`.

### 4. Dùng lambda với filter()

`filter(hàm, danh_sach)` **giữ lại** những phần tử mà hàm trả về `True`:

```python
so = [1, 2, 3, 4, 5, 6]

# Lọc số chẵn: phần tử nào x % 2 == 0 thì giữ
so_chan = list(filter(lambda x: x % 2 == 0, so))
print(so_chan)   # [2, 4, 6]
```

> 📌 `filter` trả về **đối tượng filter** (kiểu iterable), cần bọc `list(...)` để xem dưới dạng danh sách.

**Ví dụ đời thực — lọc người trên 18 tuổi:**

```python
nguoi = [("An", 17), ("Bình", 19), ("Cường", 20), ("Dung", 15)]

truong_thanh = list(filter(lambda ng: ng[1] >= 18, nguoi))
print(truong_thanh)   # [('Bình', 19), ('Cường', 20)]
```

### 5. Dùng lambda với map()

`map(hàm, danh_sach)` **áp dụng hàm lên từng phần tử** và trả danh sách kết quả:

```python
so = [1, 2, 3, 4, 5]

# Nhân đôi từng số
nhan_doi = list(map(lambda x: x * 2, so))
print(nhan_doi)   # [2, 4, 6, 8, 10]
```

> 💬 **Phân biệt:** `filter` = "ai đủ điều kiện thì **giữ**", `map` = "ai cũng bị **biến đổi**". Lọc làm danh sách ngắn lại; map giữ nguyên độ dài, chỉ đổi giá trị.

### 6. Hạn chế của lambda

| Hạn chế | Giải thích | Khi đó làm gì |
|---|---|---|
| Chỉ 1 biểu thức | Không viết được nhiều câu lệnh, vòng lặp | Dùng `def` |
| Khó gỡ lỗi | Lỗi bên trong lambda không có tên hàm để trace | Tách ra hàm `def` có tên |
| Khó đọc khi dài | Lambda dài 3-4 dòng làm code rối | Dùng `def` cho rõ ràng |
| Không dùng được `return` | Giá trị trả về là chính biểu thức | Hiểu rõ quy tắc này |

**Quy tắc thực hành:** lambda hợp lý khi **biểu thức ngắn, dùng 1 lần** (thường trong `sorted`, `filter`, `map`). Từ 2 thao tác trở lên → `def`.

### 7. Bảng so sánh: def vs lambda

| Tiêu chí | 🐍 `def` | ⚡ `lambda` |
|---|---|---|
| Cú pháp | `def ten(thamso): ...` | `lambda thamso: bieuthuc` |
| Tên hàm | Bắt buộc phải đặt | Không có tên (vô danh) |
| Số dòng | Nhiều dòng, nhiều lệnh | Đúng 1 biểu thức |
| `return` | Dùng tường minh | Không cần — biểu thức tự là kết quả |
| Vòng lặp / nhiều nhánh | ✅ Có | ❌ Không |
| Khi nào dùng | Hàm tái sử dụng, logic dài | Hàm ngắn dùng một lần, truyền vào hàm khác |
| Ví dụ tiêu biểu | Hàm tính lương, xử lý dữ liệu | `key=lambda`, `filter(lambda...)` |

---

## 💡 Ví dụ minh họa

### Ví dụ 1: Sắp xếp học sinh theo điểm (bảng điểm thực tế)

```python
# Danh sách học sinh dạng tuple: (tên, điểm)
hoc_sinh = [("An", 8.5), ("Bình", 6.0), ("Cường", 9.0), ("Dung", 7.5)]

# key=lambda hs: hs[1] -> lấy phần tử vị trí 1 (điểm) để so sánh
sx_tang = sorted(hoc_sinh, key=lambda hs: hs[1])
sx_giam = sorted(hoc_sinh, key=lambda hs: hs[1], reverse=True)

print("Tang dan:", sx_tang)
print("Giam dan:", sx_giam)
```

Kết quả:

```
Tang dan: [('Bình', 6.0), ('Dung', 7.5), ('An', 8.5), ('Cường', 9.0)]
Giam dan: [('Cường', 9.0), ('An', 8.5), ('Dung', 7.5), ('Bình', 6.0)]
```

**Giải thích từng dòng:**

| Dòng code | Ý nghĩa |
|---|---|
| `hoc_sinh = [...]` | Danh sách tuple — mỗi học sinh gồm tên (vị trí 0) và điểm (vị trí 1) |
| `key=lambda hs: hs[1]` | Với mỗi tuple `hs`, trả về `hs[1]` (điểm) làm chìa khóa so sánh |
| `sorted(..., reverse=True)` | Đảo chiều: giảm dần |
| `print(sx_tang)` | Hiển thị danh sách mới đã sắp xếp — danh sách gốc không đổi |

### Ví dụ 2: Lọc người đủ tuổi đi làm

```python
nguoi = [("An", 17), ("Bình", 19), ("Cường", 20), ("Dung", 15), ("Em", 18)]

# Lọc người từ 18 tuổi trở lên
du_tuoi = list(filter(lambda ng: ng[1] >= 18, nguoi))
print("Du tuoi:", du_tuoi)

# In tên những người đủ tuổi
for ten, tuoi in du_tuoi:
    print(ten, "co", tuoi, "tuoi")
```

Kết quả:

```
Du tuoi: [('Bình', 19), ('Cường', 20), ('Em', 18)]
Bình co 19 tuoi
Cường co 20 tuoi
Em co 18 tuoi
```

**Giải thích từng dòng:**

| Dòng code | Ý nghĩa |
|---|---|
| `filter(lambda ng: ng[1] >= 18, nguoi)` | Giữ lại tuple nào có tuổi ≥ 18 |
| `list(...)` | Chuyển đối tượng filter thành danh sách để in/dùng |
| `for ten, tuoi in du_tuoi` | Giải nén (unpack) từng tuple thành 2 biến |
| `print(ten, "co", tuoi, "tuoi")` | In tên và tuổi người đủ điều kiện |

### Ví dụ 3: Map — đổi tiền từ USD sang VND

```python
gia_usd = [10, 25, 50, 100]          # giá các món đồ (USD)
TY_GIA = 25000                       # 1 USD = 25.000 VND

# map: biến đổi từng giá trị USD thành VND
gia_vnd = list(map(lambda usd: usd * TY_GIA, gia_usd))
print("Gia VND:", gia_vnd)
```

Kết quả:

```
Gia VND: [250000, 625000, 1250000, 2500000]
```

**Giải thích từng dòng:**

| Dòng code | Ý nghĩa |
|---|---|
| `lambda usd: usd * TY_GIA` | Hàm vô danh: nhận giá USD, trả giá VND |
| `map(lambda..., gia_usd)` | Áp dụng lambda lên từng phần tử danh sách |
| `list(...)` | Gói kết quả map thành list |
| `TY_GIA` | Hằng số đặt tên hoa — quy ước PEP 8 cho giá trị không đổi |

---

## 🔬 Ví dụ nâng cao

### Ví dụ 1: Sắp xếp sản phẩm theo giá (kết hợp dataclass bài 24)

```python
from dataclasses import dataclass

@dataclass
class SanPham:
    ten: str
    gia: float

kho = [
    SanPham("Laptop", 15000000),
    SanPham("Chuột", 200000),
    SanPham("Bàn phím", 350000),
    SanPham("Tai nghe", 500000),
]

# Sắp xếp giảm dần theo giá
kho_sx = sorted(kho, key=lambda sp: sp.gia, reverse=True)

for sp in kho_sx:
    print(sp)
```

Kết quả:

```
SanPham(ten='Laptop', gia=15000000.0)
SanPham(ten='Tai nghe', gia=500000.0)
SanPham(ten='Bàn phím', gia=350000.0)
SanPham(ten='Chuột', gia=200000.0)
```

> 💡 Lambda và dataclass "sinh ra cho nhau" — lambda lấy thuộc tính (`sp.gia`), dataclass cung cấp thuộc tính có tổ chức.

### Ví dụ 2: Bảng xếp hạng & lọc thí sinh đậu

```python
thi_sinh = [
    ("An", 8.5), ("Bình", 5.0), ("Cường", 9.5),
    ("Dung", 6.5), ("Em", 4.0),
]

# Lọc thí sinh đậu: điểm >= 5.0
dau = list(filter(lambda ts: ts[1] >= 5, thi_sinh))

# Sắp giảm dần theo điểm
dau_sx = sorted(dau, key=lambda ts: ts[1], reverse=True)

print("Thi sinh dau:")
for ten, diem in dau_sx:
    print(f"  {ten} - {diem}")

print(f"So thi sinh dau: {len(dau)}")
```

Kết quả:

```
Thi sinh dau:
  Cường - 9.5
  An - 8.5
  Dung - 6.5
So thi sinh dau: 4
```

> 🔎 Lưu ý: `Em` (4.0) bị `filter` loại trước khi sắp xếp — đúng quy trình "lọc trước, xếp sau".

### Ví dụ 3: map + filter kết hợp

```python
so = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Bước 1: lọc số chẵn; Bước 2: bình phương các số còn lại
ket_qua = list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, so)))
print(ket_qua)   # [4, 16, 36, 64, 100]
```

> 🧠 Đọc từ **trong ra ngoài**: `filter` lọc số chẵn (2, 4, 6, 8, 10), rồi `map` bình phương → [4, 16, 36, 64, 100].

### Ví dụ 4: max/min với key

```python
san_pham = [("Laptop", 15000000), ("Chuột", 200000), ("Màn hình", 3000000)]

# Sản phẩm đắt nhất
dat_nhat = max(san_pham, key=lambda sp: sp[1])
# Sản phẩm rẻ nhất
re_nhat = min(san_pham, key=lambda sp: sp[1])

print("Đắt nhất:", dat_nhat)
print("Rẻ nhất:", re_nhat)
```

Kết quả:

```
Đắt nhất: ('Laptop', 15000000)
Rẻ nhất: ('Chuột', 200000)
```

---

## ⚠️ Lỗi thường gặp

### Lỗi 1: Sai chính tả từ khóa

```python
lamda x: x * x   # ❌ SAI — viết thiếu chữ 'm'
lambda x: x * x  # ✅ ĐÚNG
```

* **Kết quả báo:** `SyntaxError: invalid syntax`
* **Nguyên nhân:** từ khóa đúng là `lambda` (viết liền `lambda`).
* **Cách sửa:** gõ đúng `lambda`.

### Lỗi 2: Viết nhiều lệnh trong lambda

```python
f = lambda x: x = x + 1; return x   # ❌ SAI — lambda không có lệnh gán và return
```

* **Kết quả báo:** `SyntaxError`
* **Nguyên nhân:** lambda chỉ chứa **một biểu thức**, không có phép gán, không có `return`.
* **Cách sửa:** nếu cần phức tạp → dùng `def`.

### Lỗi 3: Quên bọc list() quanh filter/map

```python
so_chan = filter(lambda x: x % 2 == 0, so)
print(so_chan)   # <filter object at 0x...> — không phải danh sách!
```

* **Kết quả báo:** không lỗi nhưng in ra `filter object`.
* **Nguyên nhân:** `filter`/`map` trả về iterable "lười biếng", cần gọi mới sinh giá trị.
* **Cách sửa:** `list(filter(...))` để lấy danh sách ngay.

### Lỗi 4: Lambda quá dài làm code khó đọc

```python
# ❌ Quá rối — lambda lồng nhiều thao tác
kq = sorted(list(filter(lambda x: x % 2 == 0, so)),
            key=lambda x: (x % 10), reverse=False)
```

* **Nguyên nhân:** lambda dùng liên tiếp, không tên, làm code khó hiểu.
* **Cách sửa:** tách ra hàm `def` đặt tên rõ ràng: `def so_chan(x): return x % 2 == 0`.

### Lỗi 5: Nhầm thứ tự tham số của sorted key

```python
sx = sorted(hoc_sinh, key=lambda hs: hs[1], reverse=True)  # ✅ đúng
sx = sorted(hoc_sinh, lambda hs: hs[1], reverse=True)       # ❌ SAI — thiếu key=
```

* **Kết quả báo:** `TypeError: sorted() takes no keyword arguments...`
* **Cách sửa:** viết đúng từ khóa: `key=lambda ...`.

---

## 💎 Mẹo

* 🎯 **Đọc lambda "từ trong ra":** `lambda tham_so: biểu_thức` — bên trái là "đưa vào gì", bên phải là "trả về gì".
* 🧮 **Dùng lambda cho `max`/`min`** khi cần tìm "người nhất" theo một tiêu chí: `max(lst, key=...)`.
* 🏷️ **Đặt tên biến ngắn:** trong hàm dùng 1 lần, tham số lambda nên đặt 1-2 ký tự: `x`, `i`, `sp`, `hs`.
* 🔁 **Kết hợp filter → map là chuỗi "lọc rồi biến đổi"** rất phổ biến trong xử lý dữ liệu.
* 📏 **Nếu lambda dài hơn 1 dòng → tự đặt câu hỏi** có nên dùng `def` không? Câu trả lời thường là có.
* ⏱️ **Lambda không nhanh hơn def** — lợi ích là ngắn gọn, không phải tốc độ.
* 🧪 **Bài sau (26) sẽ so sánh lambda + map/filter với cách viết gọn hơn** — cùng vị trí thân quen.

---

## 📝 Tóm tắt

| Khái niệm | Nội dung chính |
|---|---|
| ✍️ Cú pháp | `lambda tham_so1, tham_so2: biểu_thức` |
| 🎭 Bản chất | Hàm vô danh, không tên, dùng một lần |
| 🔑 `sorted(key=lambda)` | Sắp xếp theo giá trị do lambda trả về |
| 🧹 `filter` | Giữ phần tử mà lambda trả về `True` |
| 🔄 `map` | Biến đổi từng phần tử bằng lambda |
| ⛔ Hạn chế | Chỉ 1 biểu thức, không lệnh, không vòng lặp |
| ⚖️ def vs lambda | Phức tạp/tái sử dụng → `def`; ngắn/1 lần → `lambda` |

---

## 🧪 Kiểm tra nhanh

1. ❓ Lambda thường được gọi là "hàm gì"? Vì sao có tên gọi đó?
2. ❓ Cú pháp đầy đủ của một lambda nhận 2 tham số `a`, `b` trả về `a + b` là gì?
3. ❓ Lambda có dùng được vòng lặp `for` bên trong không?
4. ❓ `sorted(so, key=lambda x: x)` sắp xếp theo gì?
5. ❓ `filter` và `map` khác nhau ở điểm nào?
6. ❓ Vì sao phải `list(filter(...))` thay vì `print(filter(...))`?
7. ❓ Khi nào nên chọn `def` thay vì `lambda`?
8. ❓ Viết lambda nhận `x`, trả về bình phương của x.

<details>
<summary>🔍 Xem đáp án</summary>

1. "Hàm vô danh" (anonymous function) — không cần đặt tên.
2. `lambda a, b: a + b`.
3. Không — lambda chỉ chứa một biểu thức.
4. Sắp theo giá trị của biểu thức `x` — tức sắp theo chính giá trị các phần tử (có `key` hay không kết quả giống nhau ở đây).
5. `filter` **giữ/loại bỏ** phần tử, `map` **biến đổi** từng phần tử. Filter làm danh sách ngắn lại, map giữ nguyên độ dài.
6. `filter`/`map` trả đối tượng iterable "lười", cần `list()` để lấy giá trị ngay.
7. Khi hàm phức tạp, nhiều lệnh, hoặc cần tái sử dụng nhiều nơi.
8. `lambda x: x * x`.

</details>

---

## 📚 Bài đọc thêm

* [Python.org – Lambda expressions (tài liệu chính thức)](https://docs.python.org/3/reference/expressions.html#lambda)
* [Real Python – How to Use Python Lambda Functions](https://realpython.com/python-lambda/)
* [W3Schools – Python Lambda](https://www.w3schools.com/python/python_lambda.asp)

---

---

## 🧩 Bài tập

> 📝 🎯 **Chủ đề:** Hàm vô danh `lambda` với `sorted(key=...)`, `filter`, `map`.

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Lambda cộng hai số

* **Đề bài:** Viết lambda nhận 2 số `a`, `b` trả về tổng. Gán vào biến `cong` rồi in kết quả `cong(3, 7)`.
* **Input:** Không có.
* **Output:**
  ```
  10
  ```
* **Gợi ý:** `cong = lambda a, b: a + b`; gọi `print(cong(3, 7))`.

### Bài 2: Lambda bình phương

* **Đề bài:** Viết lambda nhận `x` trả về `x * x`. Gán vào biến `bp` và in `bp(6)`.
* **Input:** Không có.
* **Output:**
  ```
  36
  ```
* **Gợi ý:** `bp = lambda x: x * x`.

### Bài 3: Lambda nhân đôi

* **Đề bài:** Viết lambda nhận `x` trả về `x * 2`, dùng `map` để nhân đôi danh sách `[1, 2, 3, 4]` và in kết quả.
* **Input:** Không có.
* **Output:**
  ```
  [2, 4, 6, 8]
  ```
* **Gợi ý:** `list(map(lambda x: x * 2, [1, 2, 3, 4]))`.

### Bài 4: Lambda trả về số lớn hơn

* **Đề bài:** Dùng `max` với `key=lambda` để tìm chuỗi **dài nhất** trong `["an", "binh", "cuong"]` rồi in ra.
* **Input:** Không có.
* **Output:**
  ```
  cuong
  ```
* **Gợi ý:** `max(danh_sach, key=lambda s: len(s))`.

### Bài 5: Sắp xếp số tăng dần

* **Đề bài:** Dùng `sorted` với `key=lambda x: x` để sắp xếp `[5, 2, 8, 1, 9]` tăng dần và in kết quả.
* **Input:** Không có.
* **Output:**
  ```
  [1, 2, 5, 8, 9]
  ```
* **Gợi ý:** `sorted(so, key=lambda x: x)` — key trả về chính giá trị so sánh.

### Bài 6: Sắp xếp theo độ dài

* **Đề bài:** Danh sách tên `["An", "Binh", "Cuong", "D"]`. Dùng `sorted` với `key=lambda ten: len(ten)` để sắp theo độ dài tăng dần và in ra.
* **Input:** Không có.
* **Output:**
  ```
  ['D', 'An', 'Binh', 'Cuong']
  ```
* **Gợi ý:** `sorted(ten, key=lambda s: len(s))`.

### Bài 7: Lọc số chẵn bằng filter

* **Đề bài:** Dùng `filter` + lambda lọc từng số chẵn trong `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` và in danh sách kết quả.
* **Input:** Không có.
* **Output:**
  ```
  [2, 4, 6, 8, 10]
  ```
* **Gợi ý:** `list(filter(lambda x: x % 2 == 0, so))`.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Sắp xếp học sinh theo điểm (tuplet)

* **Đề bài:** Danh sách `[("An", 8.5), ("Binh", 5.0), ("Cuong", 9.5)]`. Sắp giảm dần theo điểm và in danh sách kết quả.
* **Input:** Không có.
* **Output:**
  ```
  [('Cuong', 9.5), ('An', 8.5), ('Binh', 5.0)]
  ```
* **Gợi ý:** `sorted(ten, key=lambda hs: hs[1], reverse=True)` — điểm ở vị trí số 1.

### Bài 9: Lọc người trên 18 tuổi

* **Đề bài:** Danh sách `[("An", 17), ("Binh", 19), ("Cuong", 20), ("Dung", 15)]`. Dùng `filter` lọc những người từ 18 tuổi trở lên và in kết quả.
* **Input:** Không có.
* **Output:**
  ```
  [('Binh', 19), ('Cuong', 20)]
  ```
* **Gợi ý:** `list(filter(lambda ng: ng[1] >= 18, nguoi))`.

### Bài 10: Map đổi khối lượng.

* **Đề bài:** Danh sách giá USD `[10, 25, 50]`. Dùng `map` + lambda đổi sang VND (1 USD = 25000 VND) và in.
* **Input:** Không có.
* **Output:**
  ```
  [250000, 625000, 1250000]
  ```
* **Gợi ý:** `list(map(lambda usd: usd * 25000, gia_usd))`.

### Bài 11: Tên viết hoa toàn bộ

* **Đề bài:** Danh sách `["an", "binh", "cuong"]`. Dùng `map` + lambda viết hoa tất cả ký tự của mỗi tên và in.
* **Input:** Không có.
* **Output:**
  ```
  ['AN', 'BINH', 'CUONG']
  ```
* **Gợi ý:** `list(map(lambda s: s.upper(), ten))`.

### Bài 12: Tìm sinh viên điểm cao nhất

* **Đề bài:** Danh sách `[("An", 8.5), ("Binh", 5.0), ("Cuong", 9.5)]`. Dùng `max` + `key=lambda` in tên sinh viên có điểm cao nhất.
* **Input:** Không có.
* **Output:**
  ```
  Cuong 9.5
  ```
* **Gợi ý:** `max(danh_sach, key=lambda sv: sv[1])` rồi in tên và điểm.

### Bài 13: Lọc số chia hết cho 3

* **Đề bài:** Dùng `filter` + lambda lọc các số **chia hết cho 3** trong `[1, 2, 3, ..., 20]` và in.
* **Input:** Không có.
* **Output:**
  ```
  [3, 6, 9, 12, 15, 18]
  ```
* **Gợi ý:** `list(filter(lambda x: x % 3 == 0, so))`.

### Bài 14: Sắp xếp tên theo ký tự cuối

* **Đề bài:** Danh sách `["banana", "apple", "cherry", "date"]`. Sắp xếp theo **ký tự cuối** của mỗi chuỗi (dùng lambda lấy `s[-1]`) và in.
* **Input:** Không có.
* **Output:**
  ```
  ['banana', 'apple', 'cherry', 'date']
  ```
  (chỉ cần đúng thứ tự theo chữ cái cuối: a → e → y, hãy tự kiểm tra)
* **Gợi ý:** `sorted(qua, key=lambda s: s[-1])`.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Lọc chẵn rồi bình phương

* **Đề bài:** Danh sách `[1..10]`. Dùng `filter` lấy số chẵn, rồi `map` bình phương chúng vào `list` và in.
* **Input:** Không có.
* **Output:**
  ```
  [4, 16, 36, 64, 100]
  ```
* **Gợi ý:** `list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, so)))`.

### Bài 16: Điểm chuẩn thí sinh

* **Đề bài:** Danh sách thí sinh `[("An", 9.0), ("Binh", 4.5), ("Cuong", 7.0), ("Dung", 6.0)]`. Với điểm chuẩn 6.0: lọc những người đậu rồi sắp giảm dần thei theo điểm. In danh sách kết quả.
* **Input:** Không có.
* **Output:**
  ```
  [('An', 9.0), ('Cuong', 7.0), ('Dung', 6.0)]
  ```
* **Gợi ý:** filter `ts[1] >= 6` rồi `sorted(..., reverse=True)` theo điểm.

### Bài 17: Giá sau giảm giá

* **Đề bài:** Danh sách giá sản phẩm `[100000, 200000, 500000]`. Dùng `map` + lambda tính giá sau khi **giảm 20%** (tức giữ 80%) và in.
* **Input:** Không có.
* **Output:**
  ```
  [80000.0, 160000.0, 400000.0]
  ```
* **Gợi ý:** `lambda gia: gia * 0.8`.

### Bài 18: Sắp xếp thời khóa biểu theo giờ

* **Đề bài:** Danh sách `[("Toan", 7), ("Van", 10), ("Ly", 8), ("Anh", 9)]` — (môn, giờ bắt đầu). Sắp liệt kê theo thứ tự giờ tăng dần và in danh sách kết quả.
* **Input:** Không có.
* **Output:**
  ```
  [('Toan', 7), ('Ly', 8), ('Anh', 9), ('Van', 10)]
  ```
* **Gợi ý:** `sorted(lich, key=lambda mon: mon[1])` — lấy phần tử vị trí 1 (giờ) làm chìa khóa.

### Bài 19: Lọc + tìm max chia hết cho 5

* **Đề bài:** Danh sách số `[12, 7, 25, 33, 40, 15]`. Dùng lambda để tìm **số lớn nhất chia hết cho 5** trong danh sách và in kết quả.
* **Input:** Không có.
* **Output:**
  ```
  40
  ```
* **Gợi ý:** `filter(lambda x: x % 5 == 0, so)` lọc các số chia hết cho 5, rồi `max(...)` trong đó để tìm lớn nhất.

### Bài 20: Xếp hạng giảm dần + tổng lương

* **Đề bài:** Có 2 việc: (1) Danh sách học sinh `[("An", 8.5), ("Binh", 6.0), ("Cuong", 9.0)]` — sắp giảm dần theo điểm và in mỗi người kèm thứ hạng `1. Cuong - 9.0`. (2) Danh sách nhân viên `[("Minh", 5000), ("Lan", 8000), ("Thai", 6000)]` — in tổng lương cả công ty.
* **Input:** Không có.
* **Output:**
  ```
  1. Cuong - 9.0
  2. An - 8.5
  3. Binh - 6.0
  Tong luong: 19000
  ```
* **Gợi ý:** `sorted(..., reverse=True)` + `enumerate(..., start=1)` cho phần 1; `sum(map(lambda nv: nv[1], nhan_vien))` cho phần 2.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Viết thành thạo `lambda tham_so: biểu_thức`.
* ✅ Sắp xếp dữ liệu với `sorted(key=lambda ...)`.
* ✅ Lọc và biến đổi dữ liệu với `filter` + `map`.
* ✅ Kết hợp nhiều lambda để giải bài toán thực tế (điểm, thời khóa biểu, lương).

> 💪 Chưa tự làm được bài nào thì đừng lo — hãy xem lại bài giảng rồi quay lại. **Lập trình là luyện tập!**

---

## ✅ Đáp án

> 💡 **Hãy tự làm bài tập trước** rồi mới mở đáp án.

## 🟢 Dễ (Bài 1 – 7)


<details>
<summary>✅ Bài 1: Lambda cộng hai số</summary>


**Phân tích:** Bài làm quen cú pháp `lambda thamso: bieuthuc`.

**Ý tưởng:** Gán lambda vào biến rồi gọi như hàm thường.

**Thuật toán:**
1. Tạo lambda nhận `a`, `b` trả `a + b`.
2. Gọi với `(3, 7)` và in.

**Code:**

```python
# Lambda nhận 2 tham số, trả về tổng
cong = lambda a, b: a + b
print(cong(3, 7))
```

**Giải thích code:**
* `lambda a, b: a + b` — hàm vô danh: 2 tham số, biểu thức `a + b` là kết quả.
* `cong(3, 7)` — gọi như hàm thường, trả `10`.

**Độ phức tạp:** O(1).

---

</details>

<details>
<summary>✅ Bài 2: Lambda bình phương</summary>


**Phân tích:** Lambda đơn tham số, một biểu thức số học.

**Ý tưởng:** `lambda x: x * x` gán cho biến `bp`.

**Thuật toán:**
1. Tạo lambda `bp`.
2. In `bp(6)`.

**Code:**

```python
bp = lambda x: x * x
print(bp(6))
```

**Giải thích code:** `x * x = 36`; không cần từ khóa `return` — biểu thức tự là kết quả.

**Độ phức tạp:** O(1).

---

</details>

<details>
<summary>✅ Bài 3: Lambda nhân đôi</summary>


**Phân tích:** Áp dụng lambda lên từng phần tử bằng `map`.

**Ý tưởng:** `map(lambda x: x * 2, danh_sach)` rồi bọc `list()`.

**Code:**

```python
so = [1, 2, 3, 4]
nhan_doi = list(map(lambda x: x * 2, so))
print(nhan_doi)
```

**Giải thích code:**
* `map` chạy lambda với từng giá trị: 1→2, 2→4, 3→6, 4→8.
* `list(...)` chuyển đối tượng map thành danh sách.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 4: Lambda trả về chuỗi dài nhất</summary>


**Phân tích:** `max` cần biết so sánh "dài nhất" theo tiêu chí gì → `key`.

**Ý tưởng:** `key=lambda s: len(s)` — so theo độ dài chuỗi.

**Code:**

```python
ten = ["an", "binh", "cuong"]
dai_nhat = max(ten, key=lambda s: len(s))
print(dai_nhat)
```

**Giải thích code:** `len("cuong") = 6` lớn nhất nên `max` trả về `"cuong"`.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 5: Sắp xếp số tăng dần</summary>


**Phân tích:** `sorted` với key trả về chính giá trị để so sánh.

**Ý tưởng:** `sorted(so, key=lambda x: x)` — sắp tăng dần.

**Code:**

```python
so = [5, 2, 8, 1, 9]
sx = sorted(so, key=lambda x: x)
print(sx)
```

**Giải thích code:** `key` trả về `x` → Python so sánh các giá trị gốc → `[1, 2, 5, 8, 9]`. `sorted` không sửa `so`.

**Độ phức tạp:** O(n log n).

---

</details>

<details>
<summary>✅ Bài 6: Sắp xếp theo độ dài</summary>


**Phân tích:** Sắp chuỗi theo số ký tự.

**Ý tưởng:** `key=lambda s: len(s)`.

**Code:**

```python
ten = ["An", "Binh", "Cuong", "D"]
sx = sorted(ten, key=lambda s: len(s))
print(sx)
```

**Giải thích code:** Độ dài: An=2, Binh=4, Cuong=5, D=1 → thứ tự `["D", "An", "Binh", "Cuong"]`.

**Độ phức tạp:** O(n log n).

---

</details>

<details>
<summary>✅ Bài 7: Lọc số chẵn bằng filter</summary>


**Phân tích:** Giữ các phần tử thỏa điều kiện `x % 2 == 0`.

**Ý tưởng:** `filter(lambda x: x % 2 == 0, so)` + `list()`.

**Code:**

```python
so = list(range(1, 11))
so_chan = list(filter(lambda x: x % 2 == 0, so))
print(so_chan)
```

**Giải thích code:**
* `range(1, 11)` tạo 1→10 (không gồm 11).
* `lambda` trả `True` cho số chẵn — `filter` giữ lại chúng.
* Kết quả `[2, 4, 6, 8, 10]`.

**Độ phức tạp:** O(n).

---

</details>

## 🟡 Trung bình (Bài 8 – 14)


<details>
<summary>✅ Bài 8: Sắp xếp học sinh theo điểm (tuple)</summary>


**Phân tích:** Mỗi học sinh là tuple `(tên, điểm)` — cần sắp theo phần tử số 1.

**Ý tưởng:** `key=lambda hs: hs[1]`, giảm dần với `reverse=True`.

**Thuật toán:**
1. Tạo danh sách tuple.
2. Sắp theo điểm giảm dần.
3. In.

**Code:**

```python
hoc_sinh = [("An", 8.5), ("Binh", 5.0), ("Cuong", 9.5)]

sx = sorted(hoc_sinh, key=lambda hs: hs[1], reverse=True)
print(sx)
```

**Giải thích code:**
* `hs[1]` — vị trí 1 của tuple là điểm.
* `reverse=True` — từ cao xuống thấp.

**Độ phức tạp:** O(n log n).

---

</details>

<details>
<summary>✅ Bài 9: Lọc người trên 18 tuổi</summary>


**Phân tích:** Giữ những tuple có tuổi ≥ 18.

**Ý tưởng:** `filter(lambda ng: ng[1] >= 18, nguoi)`.

**Code:**

```python
nguoi = [("An", 17), ("Binh", 19), ("Cuong", 20), ("Dung", 15)]

du_tuoi = list(filter(lambda ng: ng[1] >= 18, nguoi))
print(du_tuoi)
```

**Giải thích code:** An (17) và Dung (15) bị loại; Binh, Cuong được giữ.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 10: Map đổi USD sang VND</summary>


**Phân tích:** Biến đổi từng giá trị theo tỉ giá.

**Ý tưởng:** Nhân mỗi giá trị với `25000` bằng lambda trong `map`.

**Code:**

```python
gia_usd = [10, 25, 50]
TY_GIA = 25000

gia_vnd = list(map(lambda usd: usd * TY_GIA, gia_usd))
print(gia_vnd)
```

**Giải thích code:** `10*25000=250000`, `25*25000=625000`, `50*25000=1250000`.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 11: Tên viết hoa toàn bộ</summary>


**Phân tích:** `upper()` viết hoa toàn chuỗi — dùng lambda để gọi lên từng phần tử.

**Ý tưởng:** `map(lambda s: s.upper(), ten)`.

**Code:**

```python
ten = ["an", "binh", "cuong"]
hoa = list(map(lambda s: s.upper(), ten))
print(hoa)
```

**Giải thích code:** `"an".upper()` → `"AN"`, tương tự cho các tên còn lại.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 12: Tìm sinh viên điểm cao nhất</summary>


**Phân tích:** Cần "sinh viên có điểm cao nhất" — dùng `max` với `key`.

**Ý tưởng:** `max(danh_sach, key=lambda sv: sv[1])`.

**Code:**

```python
danh_sach = [("An", 8.5), ("Binh", 5.0), ("Cuong", 9.5)]

sv_tot = max(danh_sach, key=lambda sv: sv[1])
print(sv_tot[0], sv_tot[1])
```

**Giải thích code:**
* `max(..., key=...)` trả về tuple có điểm lớn nhất `("Cuong", 9.5)`.
* `sv_tot[0]`, `sv_tot[1]` — lấy tên và điểm để in.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 13: Lọc số chia hết cho 3</summary>


**Phân tích:** Điều kiện `x % 3 == 0`.

**Ý tưởng:** `filter` với lambda kiểm tra phép chia dư.

**Code:**

```python
so = list(range(1, 21))
boi_3 = list(filter(lambda x: x % 3 == 0, so))
print(boi_3)
```

**Giải thích code:** range 1→20; số nào chia 3 dư 0 thì giữ lại.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 14: Sắp xếp tên theo ký tự cuối</summary>


**Độ phức tạp:** O(n log n).

---

</details>

## 🔴 Khó (Bài 15 – 20)


<details>
<summary>✅ Bài 15: Lọc chẵn rồi bình phương</summary>


**Phân tích:** Hai bước: lọc → biến đổi; ghép `filter` trong `map`.

**Ý tưởng:** `map(lambda x: x*x, filter(lambda x: x%2==0, so))` — đọc từ trong ra.

**Thuật toán:**
1. Xây danh sách 1–10.
2. `filter` số chẵn.
3. `map` bình phương.
4. Bọc `list` và in.

**Code:**

```python
so = list(range(1, 11))

# filter lấy số chẵn, map bình phương → bọc list
ket_qua = list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, so)))
print(ket_qua)
```

**Giải thích code:**
* Trong: `filter(...)` → [2, 4, 6, 8, 10].
* Ngoài: `map(x*x)` → [4, 16, 36, 64, 100].

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 16: Điểm chuẩn thí sinh</summary>


**Phân tích:** Lọc thí sinh điểm ≥ 6.0 rồi sắp giảm dần.

**Ý tưởng:** `filter` → `sorted` ngược.

**Thuật toán:**
1. Lọc giữ thí sinh có `ts[1] >= 6`.
2. Sắp giảm dần theo điểm.
3. In.

**Code:**

```python
thi = [("An", 9.0), ("Binh", 4.5), ("Cuong", 7.0), ("Dung", 6.0)]

# Lọc đậu rồi sắp giảm dần
dau = list(filter(lambda ts: ts[1] >= 6, thi))
ket_qua = sorted(dau, key=lambda ts: ts[1], reverse=True)
print(ket_qua)
```

**Giải thích code:** Binh (4.5) bị loại; còn lại sắp giảm: An 9.0, Cuong 7.0, Dung 6.0.

**Độ phức tạp:** O(n log n).

---

</details>

<details>
<summary>✅ Bài 17: Giá sau giảm giá</summary>


**Phân tích:** Giữ lại 80% giá → nhân `0.8`.

**Ý tưởng:** `map(lambda g: g * 0.8, danh_sach)`.

**Code:**

```python
gia = [100000, 200000, 500000]

sau_giam = list(map(lambda g: g * 0.8, gia))
print(sau_giam)
```

**Giải thích code:** `100000*0.8 = 80000.0`, `200000*0.8 = 160000.0`, `500000*0.8 = 400000.0`.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 18: Sắp xếp thời khóa biểu theo giờ</summary>


**Phân tích:** Phần tử vị trí 1 của tuple là giờ — sắp tăng dần theo đó.

**Ý tưởng:** `sorted(lich, key=lambda mon: mon[1])`.

**Code:**

```python
lich = [("Toan", 7), ("Van", 10), ("Ly", 8), ("Anh", 9)]

sx = sorted(lich, key=lambda mon: mon[1])
print(sx)
```

**Giải thích code:** Giờ tăng dần: 7 (Toan), 8 (Ly), 9 (Anh), 10 (Van).

**Độ phức tạp:** O(n log n).

---

</details>

<details>
<summary>✅ Bài 19: Lọc + tìm max chia hết cho 5</summary>


**Phân tích:** Kết hợp điều kiện (chia hết cho 5) và tìm cực trị.

**Ý tưởng:** `filter` lọc số thỏa `x % 5 == 0`, `max` chọn lớn nhất.

**Code:**

```python
so = [12, 7, 25, 33, 40, 15]

boi_5 = list(filter(lambda x: x % 5 == 0, so))
lon_nhat = max(boi_5, key=lambda x: x)
print(lon_nhat)
```

**Giải thích code:**
* `filter` → [25, 40, 15].
* `max` → 40 (dùng `key=lambda x: x` để minh họa — với số thì key không bắt buộc).

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 20: Xếp hạng giảm dần + tổng lương</summary>


**Phân tích:** Tổng hợp: sắp xếp + đánh thứ hạng; tính tổng bằng lambda qua `map`/`sum`.

**Ý tưởng:** Phần 1 dùng `sorted(reverse=True)` + `enumerate`; phần 2 dùng `sum(map(lambda nv: nv[1], ...))`.

**Thuật toán:**
1. Sắp học giảm dần theo điểm.
2. In vòng lặp với thứ hạng.
3. Tính tổng lương bằng `sum(map(...))`.

**Code:**

```python
hoc_sinh = [("An", 8.5), ("Binh", 6.0), ("Cuong", 9.0)]
nhan_vien = [("Minh", 5000), ("Lan", 8000), ("Thai", 6000)]

# Phần 1: xếp hạng học sinh giảm dần theo điểm
bang = sorted(hoc_sinh, key=lambda hs: hs[1], reverse=True)
for thu_hang, hs in enumerate(bang, start=1):
    print(f"{thu_hang}. {hs[0]} - {hs[1]}")

# Phần 2: tổng lương công ty
tong_luong = sum(map(lambda nv: nv[1], nhan_vien))
print("Tong luong:", tong_luong)
```

**Giải thích code:**
* `enumerate(bang, start=1)` — cặp (thứ hạng, học sinh).
* `map(lambda nv: nv[1], ...)` — lấy lương từng nhân viên; `sum` gộp: 5000+8000+6000 = 19000.

**Độ phức tạp:** O(n log n).

---

</details>

## 📌 Lời khuyên cuối


* Luôn nhớ lambda chỉ có **một biểu thức** — phức tạp hãy dùng `def`.
* `filter` **giữ/lọc**, `map` **biến đổi** — đều trả iterable, đừng quên `list()`.
* `sorted(key=...)` sẽ xuất hiện ở nhiều bài sau (danh sách dataclass, JSON).
* Khi cùng một lambda dùng nhiều nơi, hãy đặt tên + `def` cho dễ bảo trì.

👉 Tiếp theo: **[Bài 26: List Comprehension](../26-List-Comprehension/bai.md)**

---

## ➡️ Điều hướng

**Vị trí:** `01-Co-Ban/25-Lambda/bai.md`

**Bài tiếp theo:** [Bài 26 — List Comprehension – Vòng Lặp "Viết Trong Một Dòng"](../26-List-Comprehension/bai.md)
