# ✅ Bài 29: Đáp Án – Iterator

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án để việc học hiệu quả nhất.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Duyệt danh sách bằng `next()`

**Phân tích:** Bài tập làm quen `iter()` và `next()` — hai hàm điều khiển duyệt thủ công.

**Ý tưởng:** `iter(danh_sach)` tạo iterator; mỗi `next(it)` trả một phần tử.

**Thuật toán:**
1. Tạo danh sách.
2. Gọi `iter()` lấy iterator.
3. Gọi `next()` ba lần, in mỗi lần.

**Code:**

```python
# Danh sách cần duyệt
danh_sach = ["hoc", "tap", "vui"]

# Lấy iterator từ danh sách
it = iter(danh_sach)

# Xin từng giá trị một bằng next()
print(next(it))
print(next(it))
print(next(it))
```

**Giải thích code:**
* `iter(danh_sach)` — biến danh sách (iterable) thành iterator.
* Mỗi lần `next(it)` — lấy giá trị kế tiếp và nhích vị trí.
* Lần `next` thứ 4 sẽ ném `StopIteration` vì đã hết.

**Độ phức tạp:** O(1) mỗi lần next.

---

### Bài 2: Duyệt chuỗi ký tự

**Phân tích:** Chuỗi cũng là iterable — mỗi ký tự là một phần tử.

**Ý tưởng:** Áp dụng đúng cách duyệt của bài 1 cho chuỗi.

**Thuật toán:**
1. `it = iter("Py")`.
2. Gọi `next()` hai lần.

**Code:**

```python
# Chuỗi là iterable — duyệt từng ký tự
it = iter("Py")

print(next(it))   # ký tự đầu tiên
print(next(it))   # ký tự thứ hai
```

**Giải thích code:**
* `iter("Py")` tạo iterator duyệt chuỗi ký tự.
* `next(it)` lần lượt trả về `"P"` rồi `"y"`.

**Độ phức tạp:** O(1).

---

### Bài 3: Nhận diện iterator

**Phân tích:** Cần một cách kiểm tra khách quan xem đối tượng có phải iterator hay không.

**Ý tưởng:** Iterator bắt buộc có phương thức `__next__` — kiểm tra bằng `hasattr`.

**Thuật toán:**
1. Tạo danh sách và iterator của nó.
2. Kiểm tra `__next__` cho cả hai.

**Code:**

```python
# Danh sách và iterator của nó
danh_sach = [1, 2, 3]
it = iter(danh_sach)

# Iterator phải có phương thức __next__
print("danh_sach:", hasattr(danh_sach, "__next__"))
print("it:", hasattr(it, "__next__"))
```

**Giải thích code:**
* `hasattr(x, "__next__")` — trả `True` nếu đối tượng có phương thức `__next__`.
* List không có `__next__` → `False`; iterator có → `True`.

**Độ phức tạp:** O(1).

---

### Bài 4: Bắt `StopIteration`

**Phân tích:** `StopIteration` là ngoại lệ — có thể bắt bằng `try/except` như mọi ngoại lệ khác.

**Ý tưởng:** Gọi `next()` trong `try`; khi hết dữ liệu, `except StopIteration` in thông báo.

**Thuật toán:**
1. Tạo iterator từ `[7]`.
2. `next()` lần 1 — in `7`.
3. `next()` lần 2 — bắt `StopIteration`.

**Code:**

```python
# Iterator chỉ có 1 phần tử
it = iter([7])

print(next(it))   # lấy phần tử duy nhất

try:
    next(it)      # đã hết dữ liệu
except StopIteration:
    print("Het du lieu!")
```

**Giải thích code:**
* Lần `next` thứ hai không còn giá trị → Python ném `StopIteration`.
* `except StopIteration` bắt tín hiệu và in thông báo — vòng lặp `for` cũng làm y hệt vậy để thoát.

**Độ phức tạp:** O(1).

---

### Bài 5: `__iter__` trả về gì?

**Phân tích:** Class vừa là iterable vừa là iterator khi `__iter__` trả `self`.

**Ý tưởng:** Giữ biến đếm trong `self`, tăng dần; dừng khi vượt giới hạn.

**Thuật toán:**
1. `__init__` đặt `gia_tri = 1`.
2. `__iter__` trả `self`.
3. `__next__` trả giá trị, tăng lên; nếu `> 3` thì `raise StopIteration`.

**Code:**

```python
class So1:
    """Iterator trả về 1, 2, 3 rồi dừng."""

    def __init__(self):
        self.gia_tri = 1   # giá trị bắt đầu

    def __iter__(self):
        return self        # chính nó là iterator

    def __next__(self):
        if self.gia_tri > 3:      # đã phát hết 3 số?
            raise StopIteration
        ket_qua = self.gia_tri
        self.gia_tri += 1         # chuẩn bị số kế tiếp
        return ket_qua

for so in So1():
    print(so)
```

**Giải thích code:**
* `__iter__` trả `self` — vòng `for` gọi `iter(So1())` và nhận chính đối tượng đó.
* `__next__` kiểm tra điều kiện hết, trả giá trị rồi tăng biến đếm.

**Độ phức tạp:** O(1) mỗi lần next.

---

### Bài 6: Iterator dùng một lần

**Phân tích:** Chứng minh iterator "tiêu hao" — dữ liệu đã lấy không quay lại được.

**Ý tưởng:** `list(it)` gom toàn bộ phần còn lại của iterator.

**Thuật toán:**
1. Tạo iterator từ `[5, 6]`.
2. Gọi `next(it)` một lần (lấy `5`).
3. `list(it)` — chỉ còn `6`.

**Code:**

```python
# Iterator từ danh sách
it = iter([5, 6])

# Lấy mất 1 phần tử
next(it)

# list(it) gom phần CÒN LẠI
print(list(it))
```

**Giải thích code:**
* Sau khi `next(it)` lấy `5`, iterator chỉ còn `6`.
* `list(it)` đọc nốt phần còn lại → `[6]`.
* Nếu muốn cả `[5, 6]` thì phải tạo iterator mới.

**Độ phức tạp:** O(n) với n là số phần tử còn lại.

---

### Bài 7: Duyệt từ điển theo khóa

**Phân tích:** Dict là iterable nhưng iterator của nó duyệt qua **các khóa**.

**Ý tưởng:** `iter(dict)` rồi `next()` liên tiếp.

**Thuật toán:**
1. Tạo dict.
2. `iter(diem)` lấy iterator khóa.
3. Gọi `next()` hai lần.

**Code:**

```python
# Từ điển điểm của học sinh
diem = {"An": 8, "Binh": 9}

# iter(dict) duyệt qua các KHÓA
it = iter(diem)

print(next(it))   # An
print(next(it))   # Binh
```

**Giải thích code:**
* `iter(diem)` duyệt khóa, không duyệt giá trị.
* Muốn duyệt giá trị thì dùng `iter(diem.values())` — kỹ thuật tương tự.

**Độ phức tạp:** O(1) mỗi lần next.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Class `DemNguoc`

**Phân tích:** Iterator có trạng thái giảm dần — mỗi lần `next()` trả số nhỏ hơn 1.

**Ý tưởng:** Giữ `hien_tai` khởi đầu bằng `n`; trả rồi giảm; dừng khi dưới 1.

**Thuật toán:**
1. `__init__` nhận `n`, đặt `hien_tai = n`.
2. `__iter__` trả `self`.
3. `__next__`: nếu `hien_tai < 1` → `StopIteration`; ngược lại trả rồi giảm.

**Code:**

```python
class DemNguoc:
    """Iterator đếm ngược từ n về 1."""

    def __init__(self, n):
        self.hien_tai = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.hien_tai < 1:
            raise StopIteration
        ket_qua = self.hien_tai
        self.hien_tai -= 1
        return ket_qua

for so in DemNguoc(4):
    print(so)
```

**Giải thích code:**
* `hien_tai` chính là "vị trí" của iterator — đặc điểm chỉ iterator mới có.
* Vòng `for` tự gọi `next()` cho tới khi gặp `StopIteration`.

**Độ phức tạp:** O(1) mỗi lần next; tổng O(n).

---

### Bài 9: Class `SoChan` — số chẵn vô hạn

**Phân tích:** Dãy vô hạn — KHÔNG có `StopIteration`, chỉ dùng `next()` có kiểm soát.

**Ý tưởng:** `self.so` bắt đầu 0, mỗi lần trả rồi `+= 2`.

**Thuật toán:**
1. `__init__` đặt `so = 0`.
2. `__next__` trả `so` rồi tăng 2.

**Code:**

```python
class SoChan:
    """Iterator sinh số chẵn: 0, 2, 4, 6..."""

    def __init__(self):
        self.so = 0

    def __iter__(self):
        return self

    def __next__(self):
        ket_qua = self.so
        self.so += 2
        return ket_qua

it = SoChan()
print(next(it))
print(next(it))
print(next(it))
print(next(it))
```

**Giải thích code:**
* Không có `raise StopIteration` → không thể dùng `for` vô hạn trên class này!
* Gọi `next()` đúng 4 lần để lấy 4 số chẵn đầu.

**Độ phức tạp:** O(1) mỗi lần next.

---

### Bài 10: Class `SoLe` có giới hạn

**Phân tích:** Biến thể có giới hạn: cần biến đếm số lượng đã phát.

**Ý tưởng:** `so_hien_tai` chạy `1, 3, 5...`; `dem` đếm số đã phát; dừng khi đủ.

**Thuật toán:**
1. `__init__` đặt `so = 1`, `dem = 0`, `so_luong = so_luong`.
2. `__next__`: nếu `dem == so_luong` → `StopIteration`; trả `so`, tăng cả `so` và `dem`.

**Code:**

```python
class SoLe:
    """Iterator sinh so_luong số lẻ đầu tiên."""

    def __init__(self, so_luong):
        self.so = 1
        self.dem = 0
        self.so_luong = so_luong

    def __iter__(self):
        return self

    def __next__(self):
        if self.dem == self.so_luong:
            raise StopIteration
        ket_qua = self.so
        self.so += 2        # số lẻ kế tiếp
        self.dem += 1       # đã phát thêm 1 số
        return ket_qua

for so in SoLe(5):
    print(so)
```

**Giải thích code:**
* `dem` đảm bảo dừng đúng sau 5 số — tránh vô hạn.
* `so += 2` nhảy qua các số lẻ.

**Độ phức tạp:** O(1) mỗi lần next.

---

### Bài 11: Tạo iterator bằng `iter(ham, sentinel)`

**Phân tích:** Cú pháp `iter(ham, sentinel)` gọi hàm liên tục đến khi kết quả bằng sentinel.

**Ý tưởng:** Hàm `sinh_so` trả `1, 2, 3, 99`; sentinel là `99` — vòng dừng trước `99`.

**Thuật toán:**
1. Viết hàm `sinh_so` với biến đếm ngoài.
2. `for x in iter(sinh_so, 99):` in `x`.

**Code:**

```python
# Biến đếm nằm ngoài hàm
dem = 0

def sinh_so():
    """Trả số tăng dần, kết thúc bằng 99."""
    global dem
    dem += 1
    return [1, 2, 3, 99][dem - 1]

# iter(ham, 99): gọi ham() tới khi gặp 99 rồi dừng (không in 99)
for so in iter(sinh_so, 99):
    print(so)
```

**Giải thích code:**
* `iter(sinh_so, 99)` — gọi `sinh_so()` từng lần; nếu kết quả bằng `99` thì dừng mà không trả về `99`.
* Đây là cách gọn để đọc theo "khối" đến khi gặp dấu kết thúc.

**Độ phức tạp:** O(1) mỗi lần gọi.

---

### Bài 12: Class `BinhPhuong`

**Phân tích:** Iterator tính toán giá trị khi được hỏi — không cần lưu sẵn.

**Ý tưởng:** `index` từ 1 đến n; trả `index * index`.

**Thuật toán:**
1. `__init__`: `index = 1`, `n = n`.
2. `__next__`: nếu `index > n` → dừng; trả `index²`, tăng index.

**Code:**

```python
class BinhPhuong:
    """Iterator trả về bình phương của 1..n."""

    def __init__(self, n):
        self.n = n
        self.index = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > self.n:
            raise StopIteration
        ket_qua = self.index * self.index
        self.index += 1
        return ket_qua

for so in BinhPhuong(4):
    print(so)
```

**Giải thích code:**
* `1*1 = 1`, `2*2 = 4`, `3*3 = 9`, `4*4 = 16`.
* Giá trị được **tính khi cần** — tiết kiệm bộ nhớ so với tạo list sẵn.

**Độ phức tạp:** O(1) mỗi lần next.

---

### Bài 13: Đọc file từng dòng

**Phân tích:** File là iterable; `readline()` trả `""` khi hết — dùng làm điều kiện dừng.

**Ý tưởng:** Class giữ đối tượng file; `__next__` đọc một dòng, xử lý rỗng.

**Thuật toán:**
1. `__init__` mở file.
2. `__next__`: `readline()`; nếu `""` → đóng file, `StopIteration`; trả dòng đã bỏ `\n`.

**Code:**

```python
class DocFile:
    """Iterator đọc từng dòng của file."""

    def __init__(self, ten_file):
        self.f = open(ten_file, "r", encoding="utf-8")

    def __iter__(self):
        return self

    def __next__(self):
        dong = self.f.readline()
        if dong == "":
            self.f.close()          # dọn dẹp khi hết
            raise StopIteration
        return dong.rstrip("\n")

# Tạo file mẫu
with open("lop.txt", "w", encoding="utf-8") as f:
    f.write("An\nBinh\nChi\n")

for ten in DocFile("lop.txt"):
    print(ten)
```

**Giải thích code:**
* `readline()` trả `""` ở cuối file — tín hiệu dừng.
* `rstrip("\n")` xóa ký tự xuống dòng để in sạch.
* Class này giống hệt cách file Python hoạt động trong vòng `for`!

**Độ phức tạp:** O(1) mỗi dòng (tổng O(số dòng)).

---

### Bài 14: Iterator cộng dồn

**Phân tích:** Mỗi `next()` trả tổng tích lũy — trạng thái nằm trong iterator.

**Ý tưởng:** `tong` cộng dần từng phần tử; `index` duyệt danh sách.

**Thuật toán:**
1. `__init__` nhận danh sách, đặt `index = 0`, `tong = 0`.
2. `__next__`: nếu hết → dừng; `tong += ds[index]`; trả `tong`; tăng index.

**Code:**

```python
class CongDon:
    """Iterator trả tổng cộng dồn đến phần tử hiện tại."""

    def __init__(self, danh_sach):
        self.danh_sach = danh_sach
        self.index = 0
        self.tong = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.danh_sach):
            raise StopIteration
        self.tong += self.danh_sach[self.index]
        ket_qua = self.tong
        self.index += 1
        return ket_qua

for so in CongDon([2, 3, 4]):
    print(so)
```

**Giải thích code:**
* `tong` giữ giá trị cộng dồn: `2`, `2+3=5`, `5+4=9`.
* Kỹ thuật này hữu ích khi xử lý dữ liệu lớn từng phần (ví dụ điểm số tích lũy).

**Độ phức tạp:** O(1) mỗi lần next.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Dãy Fibonacci bằng iterator

**Phân tích:** Dãy Fibonacci: số sau = tổng hai số trước. Iterator giữ hai biến trạng thái.

**Ý tưởng:** `a, b = 0, 1`; mỗi lần trả `a` rồi cập nhật `a, b = b, a + b`.

**Thuật toán:**
1. `__init__`: `a = 0`, `b = 1`.
2. `__next__`: trả `a`, cập nhật cặp `a, b`.

**Code:**

```python
class Fibonacci:
    """Iterator sinh dãy Fibonacci vô hạn."""

    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        ket_qua = self.a
        self.a, self.b = self.b, self.a + self.b
        return ket_qua

it = Fibonacci()
for _ in range(7):
    print(next(it))
```

**Giải thích code:**
* Lượt 1: trả `0`, cập nhật `a, b = 1, 1`.
* Lượt 2: trả `1`, cập nhật `a, b = 1, 2`... đúng dãy `0, 1, 1, 2, 3, 5, 8`.
* Vô hạn nên phải dùng `next()` có số lần — giống bài 9.

**Độ phức tạp:** O(1) mỗi lần next.

---

### Bài 16: Iterator lọc số nguyên tố

**Phân tích:** Cần hàm kiểm tra nguyên tố (đã học bài 10) kết hợp với iterator.

**Ý tưởng:** Thử từng số từ 2; nếu là nguyên tố thì trả; dừng khi đủ số lượng.

**Thuật toán:**
1. Hàm phụ `la_nguyen_to(n)`.
2. `__next__`: tìm số nguyên tố kế tiếp từ `self.so`; trả về; tăng `dem`.

**Code:**

```python
def la_nguyen_to(n):
    """Trả True nếu n là số nguyên tố."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


class SoNguyenTo:
    """Iterator sinh so_luong số nguyên tố đầu tiên."""

    def __init__(self, so_luong):
        self.so_luong = so_luong
        self.so = 2
        self.dem = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.dem < self.so_luong:
            if la_nguyen_to(self.so):
                ket_qua = self.so
                self.so += 1
                self.dem += 1
                return ket_qua
            self.so += 1
        raise StopIteration

for so in SoNguyenTo(4):
    print(so)
```

**Giải thích code:**
* `la_nguyen_to` kiểm tra đến `√n` — đủ và nhanh.
* `__next__` quét `while` tới số nguyên tố kế tiếp rồi trả về.
* Dừng khi `dem` đủ `so_luong`.

**Độ phức tạp:** O(√n) mỗi số, với n là số đang kiểm tra.

---

### Bài 17: Đọc file — bỏ dòng trống

**Phân tích:** Mở rộng bài 13: lọc dòng rỗng ngay trong `__next__`.

**Ý tưởng:** Vòng lặp `while` bên trong `__next__` bỏ qua dòng `strip() == ""`.

**Thuật toán:**
1. Mở file trong `__init__`.
2. `__next__`: đọc dòng; nếu hết → đóng file, dừng; nếu rỗng → đọc tiếp; ngược lại trả dòng.

**Code:**

```python
class DocDongKhongTrong:
    """Iterator chỉ trả dòng không rỗng của file."""

    def __init__(self, ten_file):
        self.f = open(ten_file, "r", encoding="utf-8")

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            dong = self.f.readline()
            if dong == "":                  # hết file
                self.f.close()
                raise StopIteration
            noi_dung = dong.strip()
            if noi_dung != "":              # không rỗng → trả về
                return noi_dung

# Tạo file mẫu có dòng trống
with open("tho.txt", "w", encoding="utf-8") as f:
    f.write("Mua thu\n\nla dep\n")

for dong in DocDongKhongTrong("tho.txt"):
    print(dong)
```

**Giải thích code:**
* `strip()` xóa khoảng trắng hai đầu; nếu kết quả `""` thì dòng đó coi như trống.
* `while True` bên trong `__next__` giúp "nuốt" các dòng trống cho tới khi có dòng thật hoặc hết file.

**Độ phức tạp:** O(1) mỗi dòng thật (cộng số dòng trống phía trước).

---

### Bài 18: Iterator đảo ngược danh sách

**Phân tích:** Đảo hướng duyệt: bắt đầu từ chỉ số cuối, giảm dần.

**Ý tưởng:** `index = len(ds) - 1`; trả `ds[index]`; giảm index; dừng khi `< 0`.

**Thuật toán:**
1. `__init__` nhận danh sách, đặt `index` = vị trí cuối.
2. `__next__`: nếu `index < 0` → dừng; trả phần tử; giảm index.

**Code:**

```python
class DaoNguoc:
    """Iterator duyệt danh sách từ cuối về đầu."""

    def __init__(self, danh_sach):
        self.danh_sach = danh_sach
        self.index = len(danh_sach) - 1   # vị trí cuối cùng

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        ket_qua = self.danh_sach[self.index]
        self.index -= 1
        return ket_qua

for so in DaoNguoc([1, 2, 3]):
    print(so)
```

**Giải thích code:**
* `index` đi từ 2 → 1 → 0 → -1 (dừng).
* Giá trị trả về: `3, 2, 1` — duyệt ngược hoàn toàn.
* Không cần tạo bản sao đảo `[::-1]` — tiết kiệm bộ nhớ với list lớn.

**Độ phức tạp:** O(1) mỗi lần next.

---

### Bài 19: Iterator ghép hai danh sách (zigzag)

**Phân tích:** Luân phiên lấy phần tử hai danh sách; dừng khi cả hai hết.

**Ý tưởng:** Dùng `zip` — vốn đã hoạt động nhờ iterator của từng list.

**Thuật toán:**
1. `__init__` lưu hai danh sách, `i = 0`, `j = 0`.
2. `__next__`: luân phiên lấy; nếu hết cả hai → dừng.

**Code:**

```python
class ZicZac:
    """Iterator trả phần tử luân phiên của hai danh sách."""

    def __init__(self, ds_a, ds_b):
        self.ds_a = ds_a
        self.ds_b = ds_b
        self.i = 0
        self.j = 0

    def __iter__(self):
        return self

    def __next__(self):
        # Ưu tiên lấy từ A, rồi B, luân phiên
        if self.i < len(self.ds_a) and self.i <= self.j:
            ket_qua = self.ds_a[self.i]
            self.i += 1
            return ket_qua
        if self.j < len(self.ds_b):
            ket_qua = self.ds_b[self.j]
            self.j += 1
            return ket_qua
        raise StopIteration

for phan_tu in ZicZac([1, 2], ["a", "b"]):
    print(phan_tu)
```

**Giải thích code:**
* Điều kiện `self.i <= self.j` giữ nhịp luân phiên: A trước (0 ≤ 0), B (1 > 0), A (1 ≤ 1), B (2 > 1).
* Khi A hết, chỉ còn B chạy nốt; hết cả hai thì `StopIteration`.
* Trong thực tế, `zip` đã làm việc này sẵn — nhưng tự viết giúp hiểu cơ chế sâu hơn.

**Độ phức tạp:** O(1) mỗi lần next.

---

### Bài 20: Đồng hồ đếm ngược với thông báo

**Phân tích:** `__next__` vừa trả dữ liệu vừa có tác dụng phụ (in), và báo hiệu kết thúc bằng thông báo + `StopIteration`.

**Ý tưởng:** In `"Còn lại: x"` khi còn số; khi hết in `"Het gio!"` rồi ném `StopIteration`.

**Thuật toán:**
1. `__init__` đặt `hien_tai = n`.
2. `__next__`: nếu `hien_tai < 1` → in `"Het gio!"`, `raise StopIteration`; ngược lại in `"Còn lại: x"`, giảm, trả.

**Code:**

```python
class DongHoDemNguoc:
    """Đồng hồ đếm ngược kèm thông báo."""

    def __init__(self, n):
        self.hien_tai = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.hien_tai < 1:
            print("Het gio!")
            raise StopIteration
        print(f"Còn lại: {self.hien_tai}")
        ket_qua = self.hien_tai
        self.hien_tai -= 1
        return ket_qua

for giay in DongHoDemNguoc(3):
    pass   # thông báo đã in sẵn trong __next__
```

**Giải thích code:**
* Ở lần cuối, `hien_tai = 1` được in `"Còn lại: 1"`, giảm về 0.
* Lần gọi kế tiếp: `0 < 1` → in `"Het gio!"` và ném `StopIteration` — vòng `for` thoát đúng lúc.
* Đây là kiểu "iterator có tác dụng phụ" thường thấy trong game và hệ thống hẹn giờ.

**Độ phức tạp:** O(1) mỗi lần next.

---

## 📌 Lời khuyên cuối

* **Iterable** cung cấp iterator; **iterator** mới là kẻ thực sự duyệt dữ liệu.
* Cứ mở khung: `__iter__` trả `self`, `__next__` trả giá trị và `raise StopIteration` khi hết.
* Iterator vô hạn phải điều khiển bằng `next()` có số lần — đừng đưa vào `for` không giới hạn.
* Nếu class chỉ đơn thuần phát giá trị, generator (`yield`) sẽ ngắn hơn — bài 27 đã dạy.
* Kỹ năng tự tạo iterator chính là nền tảng để bạn đọc hiểu thư viện lớn (Pandas, SQLite...) trong các bài sau.

👉 Tiếp theo: **[Bài 30: Virtual Environment](../30_Virtual_Environment/bai_giang.md)**