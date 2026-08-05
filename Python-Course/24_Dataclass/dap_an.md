# ✅ Bài 24: Đáp Án – Dataclass

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án để việc học hiệu quả nhất.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Dataclass Sản phẩm đầu tiên

**Phân tích:** Cần một class chỉ chứa 2 trường dữ liệu — đây là trường hợp dùng `@dataclass` hoàn hảo.

**Ý tưởng:** Khai báo `@dataclass` với 2 trường kèm kiểu; Python tự sinh `__init__` và `__repr__`.

**Thuật toán:**
1. Import `dataclass`.
2. Khai báo class với 2 trường.
3. Tạo đối tượng và in.

**Code:**

```python
from dataclasses import dataclass

@dataclass
class SanPham:
    ten: str
    gia: float

sp = SanPham("Bút bi", 5000)
print(sp)
```

**Giải thích code:**
* `@dataclass` — Python tự sinh `__init__` (nhận `ten`, `gia`) và `__repr__` (in đẹp).
* `SanPham("Bút bi", 5000)` — gọi `__init__` tự sinh.
* `print(sp)` — hiển thị `SanPham(ten='Bút bi', gia=5000.0)`.

**Độ phức tạp:** O(1).

---

### Bài 2: Học sinh và lớp

**Phân tích:** Tạo nhiều đối tượng cùng class rồi in từng cái.

**Ý tưởng:** Hai lần gọi tạo đối tượng với đối số khác nhau; mỗi `print()` in một đối tượng.

**Thuật toán:**
1. Khai báo dataclass `HocSinh`.
2. Tạo `hs1`, `hs2`.
3. In lần lượt.

**Code:**

```python
from dataclasses import dataclass

@dataclass
class HocSinh:
    ten: str
    lop: str

hs1 = HocSinh("An", "10A1")
hs2 = HocSinh("Bình", "10A2")
print(hs1)
print(hs2)
```

**Giải thích code:**
* `HocSinh("An", "10A1")` — đối số theo đúng thứ tự khai báo: tên trước, lớp sau.
* Hai `print()` tạo hai dòng riêng biệt.

**Độ phức tạp:** O(1).

---

### Bài 3: Truy cập thuộc tính sách

**Phân tích:** Sau khi tạo đối tượng, cần lấy từng thuộc tính riêng lẻ.

**Ý tưởng:** Dùng cú pháp chấm `đối_tượng.thuộc_tính` như class thường.

**Thuật toán:**
1. Khai báo dataclass `Sach`.
2. Tạo sách.
3. In tên và tác giả riêng.

**Code:**

```python
from dataclasses import dataclass

@dataclass
class Sach:
    tua: str
    tac_gia: str

s = Sach("Đắc Nhân Tâm", "Dale Carnegie")
print("Tua:", s.tua)
print("Tac gia:", s.tac_gia)
```

**Giải thích code:**
* `s.tua` — lấy giá trị trường `tua` của đối tượng `s`.
* Dataclass không khác gì class thường khi **truy cập** thuộc tính — chỉ khác ở phần tự sinh.

**Độ phức tạp:** O(1).

---

### Bài 4: Xe có màu mặc định

**Phân tích:** Trường `mau` có mặc định nên khi tạo xe thứ nhất không cần truyền.

**Ý tưởng:** Khai báo `mau: str = "Trắng"` — trường mặc định đứng sau trường bắt buộc.

**Thuật toán:**
1. Khai báo class với trường mặc định.
2. Tạo xe không truyền màu và xe truyền màu.
3. In cả hai.

**Code:**

```python
from dataclasses import dataclass

@dataclass
class Xe:
    ten: str
    mau: str = "Trắng"

xe1 = Xe("Honda Vision")
xe2 = Xe("Sirius", "Đỏ")
print(xe1)
print(xe2)
```

**Giải thích code:**
* `mau: str = "Trắng"` — nếu bỏ qua đối số, Python dùng `"Trắng"`.
* `Xe("Sirius", "Đỏ")` — truyền rõ màu sẽ thay thế mặc định.

**Độ phức tạp:** O(1).

---

### Bài 5: Điểm thi hai môn

**Phân tích:** Cần tính tổng hai trường số thực của đối tượng.

**Ý tưởng:** Truy cập `toan`, `van` rồi cộng, đưa vào `print`.

**Thuật toán:**
1. Khai báo dataclass `Diem`.
2. Tạo đối tượng.
3. In tổng.

**Code:**

```python
from dataclasses import dataclass

@dataclass
class Diem:
    toan: float
    van: float

d = Diem(9.0, 8.0)
print("Tong diem:", d.toan + d.van)
```

**Giải thích code:**
* `d.toan + d.van` — `9.0 + 8.0 = 17.0`, kết quả kiểu `float` nên có `.0`.

**Độ phức tạp:** O(1).

---

### Bài 6: So sánh hai sản phẩm

**Phân tích:** Dataclass tự sinh `__eq__` so từng trường.

**Ý tưởng:** Tạo 3 đối tượng; `sp1 == sp2` so 2 trường bằng nhau, `sp1 == sp3` khác nhau.

**Thuật toán:**
1. Khai báo dataclass.
2. Tạo 3 sản phẩm.
3. In kết quả so sánh.

**Code:**

```python
from dataclasses import dataclass

@dataclass
class SanPham:
    ten: str
    gia: float

sp1 = SanPham("Chuột", 200000)
sp2 = SanPham("Chuột", 200000)
sp3 = SanPham("Bàn phím", 350000)

print(sp1 == sp2)
print(sp1 == sp3)
```

**Giải thích code:**
* `sp1 == sp2` — cùng tên và cùng giá → `True`.
* `sp1 == sp3` — khác tên, khác giá → `False`.
* Với class thường, kết quả sẽ luôn là `False` vì Python so địa chỉ ô nhớ.

**Độ phức tạp:** O(1).

---

### Bài 7: Danh sách môn học trống

**Phân tích:** Trường list phải dùng `field(default_factory=list)` — không được gán `= []` trực tiếp.

**Ý tưởng:** Khai báo đúng factory; khi tạo đối tượng, list tự động là `[]`.

**Thuật toán:**
1. Import cả `field`.
2. Khai báo trường list với `default_factory=list`.
3. Tạo và in.

**Code:**

```python
from dataclasses import dataclass, field

@dataclass
class HocSinh:
    ten: str
    mon_hoc: list = field(default_factory=list)

hs = HocSinh("An")
print(hs)
```

**Giải thích code:**
* `field(default_factory=list)` — mỗi lần tạo đối tượng, Python gọi `list()` tạo danh sách mới.
* `mon_hoc` in ra `[]` — danh sách trống chưa có môn nào.

**Độ phức tạp:** O(1).

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Danh sách học sinh trong lớp

**Phân tích:** Cần "chứa trong chứa" — class `LopHoc` có một list đối tượng/danh sách tên.

**Ý tưởng:** Dùng `field(default_factory=list)` rồi `append` từng học sinh.

**Thuật toán:**
1. Khai báo dataclass với trường list.
2. Tạo lớp và thêm 3 tên.
3. In lớp.

**Code:**

```python
from dataclasses import dataclass, field

@dataclass
class LopHoc:
    ten: str
    hoc_sinh: list = field(default_factory=list)

lop = LopHoc("10A1")
lop.hoc_sinh.append("An")
lop.hoc_sinh.append("Bình")
lop.hoc_sinh.append("Cường")
print(lop)
```

**Giải thích code:**
* `lop.hoc_sinh.append(...)` — thêm tên vào danh sách riêng của lớp.
* `print(lop)` — `__repr__` tự sinh hiển thị cả danh sách bên trong.

**Độ phức tạp:** O(n) với n là số học sinh thêm vào.

---

### Bài 9: In toàn bộ sản phẩm

**Phân tích:** Kết hợp dataclass với vòng lặp `for` để in danh sách đối tượng.

**Ý tưởng:** Dựng list literal chứa các đối tượng, duyệt và in từng cái.

**Thuật toán:**
1. Khai báo dataclass.
2. Tạo danh sách 3 sản phẩm.
3. Vòng lặp in.

**Code:**

```python
from dataclasses import dataclass

@dataclass
class SanPham:
    ten: str
    gia: float

danh_sach = [
    SanPham("Laptop", 15000000),
    SanPham("Chuột", 200000),
    SanPham("Bàn phím", 350000),
]

for sp in danh_sach:
    print(sp)
```

**Giải thích code:**
* List literal chứa trực tiếp các đối tượng `SanPham`.
* `print(sp)` — mỗi dòng một sản phẩm nhờ `__repr__` tự sinh.

**Độ phức tạp:** O(n).

---

### Bài 10: Sản phẩm đắt nhất

**Phân tích:** Tìm phần tử lớn nhất theo tiêu chí `gia`.

**Ý tưởng:** Dùng `max(danh_sach, key=lambda sp: sp.gia)` — `key` cho biết "so sánh theo giá trị nào".

**Thuật toán:**
1. Tạo danh sách sản phẩm.
2. Gọi `max` với `key`.
3. In kết quả.

**Code:**

```python
from dataclasses import dataclass

@dataclass
class SanPham:
    ten: str
    gia: float

danh_sach = [
    SanPham("Chuột", 200000),
    SanPham("Bàn phím", 350000),
    SanPham("Laptop", 15000000),
    SanPham("Tai nghe", 500000),
]

sp_dat_nhat = max(danh_sach, key=lambda sp: sp.gia)
print("Sản phẩm đắt nhất:", sp_dat_nhat)
```

**Giải thích code:**
* `key=lambda sp: sp.gia` — mỗi sản phẩm quy về giá để so sánh (lambda học chi tiết bài 25).
* `max` trả về chính đối tượng có giá lớn nhất.

**Độ phức tạp:** O(n).

---

### Bài 11: Học sinh đạt học bổng

**Phân tích:** Lọc danh sách theo điều kiện điểm.

**Ý tưởng:** Duyệt từng học sinh, kiểm tra `diem >= 8` rồi in.

**Thuật toán:**
1. Tạo danh sách học sinh.
2. Duyệt và kiểm tra điều kiện.
3. In học sinh đạt.

**Code:**

```python
from dataclasses import dataclass

@dataclass
class HocSinh:
    ten: str
    diem: float

lop = [
    HocSinh("An", 8.5),
    HocSinh("Bình", 6.0),
    HocSinh("Cường", 9.0),
    HocSinh("Dung", 7.5),
    HocSinh("Em", 8.0),
]

for hs in lop:
    if hs.diem >= 8:
        print(hs.ten, hs.diem)
```

**Giải thích code:**
* `if hs.diem >= 8` — điều kiện học bổng.
* Chỉ những học sinh thỏa mãn mới được in.

**Độ phức tạp:** O(n).

---

### Bài 12: Phương thức tính trung bình

**Phân tích:** Dataclass vẫn viết phương thức như class thường.

**Ý tưởng:** Định nghĩa `trung_binh()` trong class, dùng `self` để truy cập dữ liệu.

**Thuật toán:**
1. Khai báo class với 3 trường.
2. Viết phương thức `trung_binh()`.
3. Tạo đối tượng và in kết quả.

**Code:**

```python
from dataclasses import dataclass

@dataclass
class HocSinh:
    ten: str
    diem_toan: float
    diem_van: float

    def trung_binh(self):
        return (self.diem_toan + self.diem_van) / 2

hs = HocSinh("An", 9.0, 7.0)
print(f"{hs.ten} co diem trung binh: {hs.trung_binh()}")
```

**Giải thích code:**
* `def trung_binh(self)` — phương thức thường, đối số đầu tiên là `self`.
* `(self.diem_toan + self.diem_van) / 2` — `(9.0 + 7.0) / 2 = 8.0`.
* f-string nhúng kết quả trực tiếp vào chuỗi in.

**Độ phức tạp:** O(1).

---

### Bài 13: Thống kê sản phẩm rẻ

**Phân tích:** Đếm số phần tử thỏa điều kiện giá.

**Ý tưởng:** Biến đếm khởi tạo 0, tăng khi gặp sản phẩm giá dưới 100.000.

**Thuật toán:**
1. Tạo danh sách 5 sản phẩm.
2. Khởi tạo `dem = 0`.
3. Duyệt, tăng `dem` khi thỏa điều kiện.
4. In kết quả.

**Code:**

```python
from dataclasses import dataclass

@dataclass
class SanPham:
    ten: str
    gia: float

danh_sach = [
    SanPham("Bút bi", 5000),
    SanPham("Vở", 15000),
    SanPham("Thước", 8000),
    SanPham("Balô", 250000),
    SanPham("Bình nước", 90000),
]

dem = 0
for sp in danh_sach:
    if sp.gia < 100000:
        dem += 1

print(f"So san pham re (duoi 100000): {dem}")
```

**Giải thích code:**
* `dem = 0` — khởi tạo bộ đếm.
* `dem += 1` — tăng đếm mỗi lần gặp sản phẩm rẻ.
* Bút bi, Vở, Thước, Bình nước (4 sản phẩm) đều dưới 100k.

**Độ phức tạp:** O(n).

---

### Bài 14: Sắp xếp sản phẩm theo giá

**Phân tích:** Cần sắp xếp danh sách đối tượng theo một thuộc tính.

**Ý tưởng:** `sorted(danh_sach, key=lambda sp: sp.gia)` trả về danh sách mới đã sắp xếp.

**Thuật toán:**
1. Tạo danh sách.
2. Sắp xếp bằng `sorted` với `key`.
3. Duyệt in.

**Code:**

```python
from dataclasses import dataclass

@dataclass
class SanPham:
    ten: str
    gia: float

danh_sach = [
    SanPham("Laptop", 15000000),
    SanPham("Chuột", 200000),
    SanPham("Bàn phím", 350000),
    SanPham("Tai nghe", 500000),
]

danh_sach_sx = sorted(danh_sach, key=lambda sp: sp.gia)

for sp in danh_sach_sx:
    print(sp)
```

**Giải thích code:**
* `sorted` **không sửa** danh sách gốc mà trả về danh sách mới.
* `key=lambda sp: sp.gia` — lấy giá làm chìa khóa so sánh.
* Thứ tự in: Chuột → Bàn phím → Tai nghe → Laptop.

**Độ phức tạp:** O(n log n).

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Điểm thi bất biến

**Phân tích:** `frozen=True` chặn mọi thay đổi thuộc tính; lỗi phát sinh là `FrozenInstanceError`.

**Ý tưởng:** Khai báo `@dataclass(frozen=True)`, bọc phép gán sai trong `try...except`.

**Thuật toán:**
1. Import `FrozenInstanceError`.
2. Khai báo dataclass frozen.
3. In đối tượng, thử sửa và bắt lỗi.

**Code:**

```python
from dataclasses import dataclass, FrozenInstanceError

@dataclass(frozen=True)
class DiemThi:
    mon: str
    diem: float

d = DiemThi("Toan", 9.5)
print(d)

try:
    d.diem = 10
except FrozenInstanceError:
    print("Khong the sua diem thi!")
```

**Giải thích code:**
* `@dataclass(frozen=True)` — mọi trường trở thành "đóng băng".
* `d.diem = 10` — ném `FrozenInstanceError`.
* `except FrozenInstanceError` — bắt đúng lỗi và in thông báo thân thiện.

**Độ phức tạp:** O(1).

---

### Bài 16: Quản lý cửa hàng mini

**Phân tích:** Cần phương thức tính giá trị theo số lượng, sau đó cộng dồn cả kho.

**Ý tưởng:** Phương thức `gia_tri()` trả `gia * so_luong`; vòng lặp cộng dồn.

**Thuật toán:**
1. Khai báo class có phương thức `gia_tri()`.
2. Tạo 3 sản phẩm với số lượng.
3. Cộng dồn và in tổng.

**Code:**

```python
from dataclasses import dataclass

@dataclass
class SanPham:
    ten: str
    gia: float
    so_luong: int = 0

    def gia_tri(self):
        return self.gia * self.so_luong

kho = [
    SanPham("Laptop", 15000000, 3),
    SanPham("Chuột", 200000, 20),
    SanPham("Bàn phím", 350000, 10),
]

tong = 0
for sp in kho:
    tong += sp.gia_tri()

print(f"Tong gia tri kho: {tong}")
```

**Giải thích code:**
* `so_luong: int = 0` — trường mặc định đứng sau trường bắt buộc.
* `sp.gia_tri()` — `15000000*3 + 200000*20 + 350000*10 = 12300000.0`.
* `tong += ...` — cộng dồn giá trị từng sản phẩm.

**Độ phức tạp:** O(n).

---

### Bài 17: Học sinh và danh sách điểm

**Phân tích:** Mỗi học sinh sở hữu một list điểm riêng — dùng `default_factory=list`.

**Ý tưởng:** Phương thức `trung_binh()` tính `sum(diem) / len(diem)`.

**Thuật toán:**
1. Khai báo class với trường list.
2. Viết phương thức trung bình.
3. Tạo học sinh, thêm điểm, in kết quả.

**Code:**

```python
from dataclasses import dataclass, field

@dataclass
class HocSinh:
    ten: str
    diem: list = field(default_factory=list)

    def trung_binh(self):
        return sum(self.diem) / len(self.diem)

hs = HocSinh("An")
hs.diem = [8, 9, 10]
print(f"Trung binh cua {hs.ten}: {hs.trung_binh()}")
```

**Giải thích code:**
* `sum(self.diem)` — `8 + 9 + 10 = 27`.
* `len(self.diem)` — `3`.
* `27 / 3 = 9.0` — trung bình của An.

**Độ phức tạp:** O(k) với k là số môn học.

---

### Bài 18: Bảng xếp hạng học sinh

**Phân tích:** Sắp xếp giảm dần rồi đánh số thứ hạng.

**Ý tưởng:** `sorted(..., reverse=True)` + `enumerate(danh_sach, start=1)` để có thứ hạng.

**Thuật toán:**
1. Tạo danh sách học sinh.
2. Sắp xếp giảm dần theo điểm.
3. Duyệt với `enumerate` và in thứ hạng.

**Code:**

```python
from dataclasses import dataclass

@dataclass
class HocSinh:
    ten: str
    diem: float

lop = [
    HocSinh("An", 8.5),
    HocSinh("Bình", 6.0),
    HocSinh("Cường", 9.0),
    HocSinh("Dung", 7.5),
    HocSinh("Em", 8.0),
]

bang_xep_hang = sorted(lop, key=lambda hs: hs.diem, reverse=True)

for thu_hang, hs in enumerate(bang_xep_hang, start=1):
    print(f"{thu_hang}. {hs.ten} - {hs.diem}")
```

**Giải thích code:**
* `reverse=True` — từ cao xuống thấp.
* `enumerate(danh_sach, start=1)` — trả cặp (thứ hạng, học sinh), bắt đầu từ 1.
* f-string định dạng `1. Cường - 9.0`.

**Độ phức tạp:** O(n log n).

---

### Bài 19: Giảm giá thông minh

**Phân tích:** Phương thức thay đổi chính thuộc tính `gia` của đối tượng.

**Ý tưởng:** `self.gia = self.gia * (1 - phan_tram / 100)` — giảm phần trăm.

**Thuật toán:**
1. Khai báo class với phương thức `giam_gia`.
2. Tạo áo thun 200.000.
3. Giảm 25%, in giá mới và đối tượng.

**Code:**

```python
from dataclasses import dataclass

@dataclass
class SanPham:
    ten: str
    gia: float

    def giam_gia(self, phan_tram):
        self.gia = self.gia * (1 - phan_tram / 100)

ao = SanPham("Áo thun", 200000)
ao.giam_gia(25)
print("Gia moi:", ao.gia)
print(ao)
```

**Giải thích code:**
* `1 - 25 / 100 = 0.75` — giữ lại 75% giá.
* `200000 * 0.75 = 150000.0`.
* `print(ao)` — `__repr__` tự sinh cập nhật đúng giá mới.

**Độ phức tạp:** O(1).

---

### Bài 20: Chương trình thống kê kho hàng

**Phân tích:** Bài tổng hợp: đếm, cộng dồn, tìm cực trị trên danh sách đối tượng.

**Ý tưởng:** Viết hàm `thong_ke()` nhận danh sách; dùng `len`, vòng lặp, `min` với `key`.

**Thuật toán:**
1. Khai báo dataclass `SanPham` có `ton_kho`.
2. Viết hàm thống kê (đếm, tổng giá trị, tìm tồn ít nhất).
3. Tạo 4 sản phẩm và gọi hàm.

**Code:**

```python
from dataclasses import dataclass

@dataclass
class SanPham:
    ten: str
    gia: float
    ton_kho: int = 0


def thong_ke(danh_sach):
    tong_gia_tri = 0
    for sp in danh_sach:
        tong_gia_tri += sp.gia * sp.ton_kho

    it_nhat = min(danh_sach, key=lambda sp: sp.ton_kho)

    print(f"Tong so mat hang: {len(danh_sach)}")
    print(f"Tong gia tri kho: {tong_gia_tri}")
    print(f"Hang ton it nhat: {it_nhat}")


kho = [
    SanPham("Laptop", 15000000, 3),
    SanPham("Chuột", 200000, 20),
    SanPham("Bàn phím", 350000, 5),
    SanPham("Tai nghe", 500000, 2),
]

thong_ke(kho)
```

**Giải thích code:**
* `tong_gia_tri += sp.gia * sp.ton_kho` — giá trị từng mặt hàng.
* `min(..., key=lambda sp: sp.ton_kho)` — mặt hàng tồn ít nhất (Tai nghe, 2 cái).
* `len(danh_sach)` — tổng số mặt hàng là 4.
* Hàm `thong_ke` giúp tái sử dụng cho bất kỳ kho nào.

**Độ phức tạp:** O(n).

---

## 📌 Lời khuyên cuối

* Luôn nhớ `from dataclasses import dataclass` — thiếu là `NameError`.
* Trường kiểu list/dict bắt buộc dùng `field(default_factory=...)`.
* `frozen=True` cho dữ liệu "sự thật" (điểm thi, hóa đơn), dataclass thường cho dữ liệu hay thay đổi.
* Kết hợp dataclass với `sorted`, `max`, `min` + `key=lambda` sẽ cực kỳ hiệu quả — chuẩn bị tinh thần học **lambda**!

👉 Tiếp theo: **[Bài 25: Lambda](../25_Lambda/bai_giang.md)**

