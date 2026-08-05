# ⚡ Bài 25: Lambda – Hàm Vô Danh Siêu Ngắn Gọn

> 🎓 **Chương 5 – Lập trình hướng đối tượng & các công cụ nâng cao**

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

Ở [Bài 12 – Hàm](../12_Ham/bai_giang.md), ta định nghĩa hàm bằng `def`:

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

## 🏁 Kết thúc bài

🎉 **Tuyệt vời!** Bạn đã nắm được công cụ lambda "tiện dụng có giới hạn" — sắp xếp, lọc, biến đổi dữ liệu chỉ trong một dòng.

Bạn có thấy cách viết `list(map(lambda x: x * x, so))` đôi khi hơi rối mắt? Bài sau sẽ giới thiệu một cách viết **đẹp hơn, dễ đọc hơn** cho chính những combo này:

👉 **[Bài 26: List Comprehension](../26_List_Comprehension/bai_giang.md)**
