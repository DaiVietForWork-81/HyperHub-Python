# ✅ Bài 23: Đáp Án – Lập Trình Hướng Đối Tượng

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án để việc học hiệu quả nhất.

> 📌 Mỗi lời giải gồm: định nghĩa class → tạo đối tượng → gọi phương thức để kiểm chứng.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Class đầu tiên

**Phân tích:** Bài làm quen: khai báo class với `__init__` gán thuộc tính; tạo nhiều đối tượng độc lập.

**Ý tưởng:** `__init__` nhận `ten`, `lop`; mỗi đối tượng lưu giá trị riêng của mình qua `self`.

**Thuật toán:**
1. Khai báo class `HocSinh` với `__init__(self, ten, lop)`.
2. Tạo 2 đối tượng.
3. In thuộc tính của từng đối tượng.

**Code:**

```python
class HocSinh:
    """Bản thiết kế của một học sinh."""

    def __init__(self, ten, lop):
        self.ten = ten      # thuộc tính gắn với từng đối tượng
        self.lop = lop

# Tạo hai đối tượng từ cùng một class
an = HocSinh("An", "10A1")
mai = HocSinh("Mai", "11B2")

print(f"{an.ten} hoc lop {an.lop}")
print(f"{mai.ten} hoc lop {mai.lop}")
```

**Giải thích code:**
* `class HocSinh:` — khai báo class; tên class viết hoa chữ đầu.
* `self.ten = ten` — gán tham số vào thuộc tính của **đối tượng đang được tạo**.
* `an` và `mai` là 2 đối tượng riêng biệt: `an.ten = "An"`, `mai.ten = "Mai"`.

**Độ phức tạp:** O(1).

---

### Bài 2: Xếp loại điểm

**Phân tích:** Phương thức đọc thuộc tính `self.diem_tb` và trả về xếp loại theo thang điểm.

**Ý tưởng:** `if/elif` từ mốc cao xuống thấp; `return` chuỗi loại.

**Thuật toán:**
1. `__init__` gán `ten`, `diem_tb`.
2. `xep_loai()`: ≥8 Gioi, ≥6.5 Kha, ≥5 Trung binh, còn lại Yeu.
3. Tạo đối tượng An (8.5) và in.

**Code:**

```python
class HocSinh:
    """Học sinh có điểm trung bình."""

    def __init__(self, ten, diem_tb):
        self.ten = ten
        self.diem_tb = diem_tb

    def xep_loai(self):
        """Trả về xếp loại dựa trên điểm trung bình."""
        if self.diem_tb >= 8.0:
            return "Gioi"
        if self.diem_tb >= 6.5:
            return "Kha"
        if self.diem_tb >= 5.0:
            return "Trung binh"
        return "Yeu"

an = HocSinh("An", 8.5)
print(f"{an.ten}: {an.xep_loai()}")
```

**Giải thích code:**
* `xep_loai` không cần tham số điểm — tự đọc `self.diem_tb`.
* `8.5 >= 8.0` → nhánh đầu tiên → `"Gioi"`.
* Thứ tự kiểm tra từ cao xuống thấp là bắt buộc (nếu đảo thứ tự sẽ xếp loại sai).

**Độ phức tạp:** O(1).

---

### Bài 3: Constructor với giá trị biến thiên

**Phân tích:** Hình chữ nhật có 2 thuộc tính; diện tích và chu vi tính từ chúng.

**Ý tưởng:** Hai phương thức `dien_tich()` và `chu_vi()` dùng `self.dai`, `self.rong`.

**Thuật toán:**
1. `__init__(self, dai, rong)`.
2. `dien_tich()` → `self.dai * self.rong`.
3. `chu_vi()` → `2 * (self.dai + self.rong)`.
4. Tạo hình 6×4 và in kết quả.

**Code:**

```python
class HinhChuNhat:
    """Hình chữ nhật với chiều dài, chiều rộng."""

    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def dien_tich(self):
        """Diện tích = dài x rộng."""
        return self.dai * self.rong

    def chu_vi(self):
        """Chu vi = 2 x (dài + rộng)."""
        return 2 * (self.dai + self.rong)

hinh = HinhChuNhat(6, 4)
print("Dien tich:", hinh.dien_tich())
print("Chu vi:", hinh.chu_vi())
```

**Giải thích code:**
* Tham số `dai`, `rong` của `__init__` chuyển thành thuộc tính để dùng lại ở mọi phương thức.
* `6 * 4 = 24`; `2 * (6 + 4) = 20`.

**Độ phức tạp:** O(1).

---

### Bài 4: ATM Mini

**Phân tích:** Số dư thay đổi qua phương thức; `rut` phải kiểm tra điều kiện trước khi trừ.

**Ý tưởng:** `nap` cộng; `rut` kiểm tra đủ tiền rồi trừ, trả về `True/False`; `xem` trả về số dư.

**Thuật toán:**
1. Khởi tạo `so_du = 1000000`.
2. `nap(50000)` → 1.050.000.
3. `rut(200000)` → 850.000.
4. In số dư.

**Code:**

```python
class ATM:
    """Máy ATM đơn giản."""

    def __init__(self, so_du):
        self.so_du = so_du

    def nap(self, tien):
        """Nạp tiền vào tài khoản."""
        self.so_du += tien

    def rut(self, tien):
        """Rút tiền; trả về True nếu thành công."""
        if tien > self.so_du:
            print("Khong du tien!")
            return False
        self.so_du -= tien
        return True

    def xem(self):
        """Trả về số dư hiện tại."""
        return self.so_du

may = ATM(1000000)
may.nap(50000)
may.rut(200000)
print("So du:", may.xem())
```

**Giải thích code:**
* `may.rut(200000)` — 200.000 ≤ 1.050.000 nên thành công.
* Nếu rút quá số dư, phương thức in cảnh báo và trả `False` — không trừ nhầm tiền.
* `xem()` chỉ trả về, không in — tách "lấy dữ liệu" khỏi "hiển thị".

**Độ phức tạp:** O(1).

---

### Bài 5: `__str__` đẹp

**Phân tích:** In trực tiếp đối tượng cần `__str__` — phương thức quy định chuỗi hiển thị.

**Ý tưởng:** `__str__` trả về f-string; `print(doi_tuong)` tự gọi nó.

**Thuật toán:**
1. `__init__` gán `ma_so`, `ho_ten`.
2. `__str__` trả về chuỗi định dạng.
3. Tạo 2 sinh viên và in.

**Code:**

```python
class SinhVien:
    """Sinh viên với mã số và họ tên."""

    def __init__(self, ma_so, ho_ten):
        self.ma_so = ma_so
        self.ho_ten = ho_ten

    def __str__(self):
        """Python gọi hàm này khi in đối tượng."""
        return f"Ma so: {self.ma_so} - Ho ten: {self.ho_ten}"

sv1 = SinhVien("SV001", "Nguyen Van An")
sv2 = SinhVien("SV002", "Tran Thi Mai")

print(sv1)
print(sv2)
```

**Giải thích code:**
* Không có `__str__`, `print(sv1)` in ra địa chỉ bộ nhớ xấu xí.
* `__str__` **trả về** chuỗi (không `print` bên trong) — đúng chuẩn.
* `print(sv1)` → tự động gọi `sv1.__str__()`.

**Độ phức tạp:** O(1).

---

### Bài 6: Danh sách điểm

**Phân tích:** Thuộc tính `mon_hoc` là list; phương thức thêm phần tử và in ra.

**Ý tưởng:** `self.mon_hoc = []` trong `__init__`; `them_mon` dùng `append`; in dùng `join`.

**Thuật toán:**
1. `__init__` tạo list rỗng.
2. `them_mon(ten)` append.
3. `in_mon_hoc()` nối list thành chuỗi bằng `", "`.
4. Thêm 3 môn và in.

**Code:**

```python
class SinhVien:
    """Sinh viên theo dõi các môn học."""

    def __init__(self, ten):
        self.ten = ten
        self.mon_hoc = []          # list rỗng — chưa có môn nào

    def them_mon(self, mon):
        """Thêm một môn học vào danh sách."""
        self.mon_hoc.append(mon)

    def in_mon_hoc(self):
        """In danh sách các môn đã đăng ký."""
        print(f"Mon hoc cua {self.ten}: {', '.join(self.mon_hoc)}")

an = SinhVien("An")
an.them_mon("Toan")
an.them_mon("Van")
an.them_mon("Anh")
an.in_mon_hoc()
```

**Giải thích code:**
* Thuộc tính list phải khởi tạo trong `__init__` — nếu khai báo ngoài, mọi đối tượng sẽ **dùng chung** một list (lỗi ngầm nguy hiểm).
* `', '.join(self.mon_hoc)` — nối list chuỗi bằng dấu phẩy + khoảng trắng.

**Độ phức tạp:** O(1) mỗi lần thêm; O(n) khi in.

---

### Bài 7: Tính điểm trung bình

**Phân tích:** Điểm là list 3 môn; TB = tổng chia số lượng.

**Ý tưởng:** `sum(self.diem) / len(self.diem)`; in làm tròn 2 chữ số.

**Thuật toán:**
1. `__init__` nhận list `diem`.
2. `tinh_tb()` trả về trung bình.
3. In `8.00`.

**Code:**

```python
class HocSinh:
    """Học sinh có danh sách điểm."""

    def __init__(self, ten, diem):
        self.ten = ten
        self.diem = diem          # list điểm các môn

    def tinh_tb(self):
        """Điểm trung bình = tổng / số môn."""
        return sum(self.diem) / len(self.diem)

an = HocSinh("An", [8, 7, 9])
print(f"Diem trung binh: {an.tinh_tb():.2f}")
```

**Giải thích code:**
* `[8, 7, 9]` → tổng 24, chia 3 → `8.0`.
* `:.2f` — định dạng 2 chữ số thập phân: `8.00`.

**Độ phức tạp:** O(m) với m số môn.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Đóng gói tài khoản

**Phân tích:** Số dư đặt sau `_` (quy ước nội bộ); chỉ thay đổi qua phương thức kiểm tra.

**Ý tưởng:** `rut_tien` trả `False` khi không đủ; `xem_so_du()` là "cửa sổ" hợp lệ để đọc.

**Thuật toán:**
1. `_so_du = 1000000`.
2. `nap_tien(200000)` → 1.200.000.
3. `rut_tien(1500000)` → thất bại (1.500.000 > 1.200.000).
4. `rut_tien(100000)` → 1.100.000.
5. In số dư cuối.

**Code:**

```python
class BankAccount:
    """Tài khoản ngân hàng với số dư được bảo vệ."""

    def __init__(self, so_du_ban_dau):
        self._so_du = so_du_ban_dau      # quy ước: thuộc tính nội bộ

    def nap_tien(self, tien):
        """Nạp tiền, chỉ nhận số dương."""
        if tien > 0:
            self._so_du += tien

    def rut_tien(self, tien):
        """Rút tiền; trả về True nếu thành công."""
        if tien > self._so_du:
            return False
        self._so_du -= tien
        return True

    def xem_so_du(self):
        """Cách hợp lệ để đọc số dư."""
        return self._so_du

tk = BankAccount(1000000)
tk.nap_tien(200000)
if not tk.rut_tien(1500000):               # rút quá số dư
    print("Rut that bai: khong du so du")
tk.rut_tien(100000)
print("So du cuoi:", tk.xem_so_du())
```

**Giải thích code:**
* `_so_du` (một gạch) là lời nhắn "nội bộ — đừng đụng vào"; muốn thay đổi phải qua `nap_tien`/`rut_tien`.
* `rut_tien(1500000)` trả `False` nên in thông báo; không trừ tiền.
* Cuối cùng: 1.000.000 + 200.000 − 100.000 = 1.100.000.

**Độ phức tạp:** O(1).

---

### Bài 9: Kế thừa đơn giản

**Phân tích:** `HocSinhNangKhieu` là một `HocSinh` nhưng có thêm năng khiếu — dùng kế thừa.

**Ý tưởng:** Class con không viết lại `__init__` mà gọi `super().__init__`, thêm thuộc tính mới, ghi đè `gioi_thieu`.

**Thuật toán:**
1. `HocSinh`: `__init__` + `gioi_thieu()`.
2. `HocSinhNangKhieu(HocSinh)`: `super().__init__` + thêm `nang_khieu` + ghi đè `gioi_thieu`.
3. Tạo 2 đối tượng, gọi `gioi_thieu()`.

**Code:**

```python
class HocSinh:
    """Học sinh cơ bản."""

    def __init__(self, ten, lop):
        self.ten = ten
        self.lop = lop

    def gioi_thieu(self):
        return f"Toi la {self.ten} hoc lop {self.lop}"

class HocSinhNangKhieu(HocSinh):
    """Học sinh năng khiếu — kế thừa HocSinh."""

    def __init__(self, ten, lop, nang_khieu):
        super().__init__(ten, lop)        # gán ten, lop giống cha
        self.nang_khieu = nang_khieu      # thêm thuộc tính riêng

    def gioi_thieu(self):                 # ghi đè phương thức cha
        return f"Toi la {self.ten} hoc lop {self.lop}, voi nang khieu ve {self.nang_khieu}"

hs1 = HocSinh("An", "10A1")
hs2 = HocSinhNangKhieu("Minh", "10A1", "hoi hoa")
print(hs1.gioi_thieu())
print(hs2.gioi_thieu())
```

**Giải thích code:**
* `class HocSinhNangKhieu(HocSinh)` — kế thừa: có ngay `ten`, `lop`.
* `super().__init__(ten, lop)` — dùng lại hàm khởi tạo của cha, không gõ lại.
* Ghi đè: cùng tên `gioi_thieu` nhưng nội dung khác — đối tượng mỗi loại tự "nói" theo cách của mình.

**Độ phức tạp:** O(1).

---

### Bài 10: `super().__init__`

**Phân tích:** Tầng kế thừa 1 cấp: `GiaoVien` là `NhanVien` + thêm môn dạy.

**Ý tưởng:** `super().__init__(ten, ma_so)` ở dòng đầu của `__init__` con.

**Thuật toán:**
1. `NhanVien`: `ten`, `ma_so`.
2. `GiaoVien(NhanVien)`: `super().__init__` + `mon_day`.
3. `mo_ta()` in đầy đủ.
4. Tạo đối tượng và in.

**Code:**

```python
class NhanVien:
    """Nhân viên cơ bản."""

    def __init__(self, ten, ma_so):
        self.ten = ten
        self.ma_so = ma_so

class GiaoVien(NhanVien):
    """Giáo viên — là một nhân viên, thêm môn dạy."""

    def __init__(self, ten, ma_so, mon_day):
        super().__init__(ten, ma_so)      # gọi __init__ của NhanVien
        self.mon_day = mon_day            # thuộc tính riêng

    def mo_ta(self):
        return f"Giao vien: {self.ten}, MS: {self.ma_so}, day mon {self.mon_day}"

gv = GiaoVien("Nguyen Van An", "NV01", "Toan")
print(gv.mo_ta())
```

**Giải thích code:**
* `super().__init__(ten, ma_so)` — nạp "tài sản" chung từ cha, chỉ cần viết 1 lần.
* Quên `super()` sẽ báo `AttributeError` khi truy cập `self.ten`.
* Lợi ích: sau này thêm thuộc tính cho `NhanVien`, mọi class con tự có.

**Độ phức tạp:** O(1).

---

### Bài 11: Lớp học quản lý học sinh

**Phân tích:** `LopHoc` chứa list **đối tượng** `HocSinh` — hợp thành ("có một/một lớp").

**Ý tưởng:** `them(hs)` append; `trung_binh_ca_lop()` cộng dồn `hs.diem_tb`.

**Thuật toán:**
1. `LopHoc.__init__` tạo list rỗng.
2. `them(hs)` — nhận cả đối tượng.
3. `trung_binh_ca_lop()` — duyệt list, cộng dồn, chia số lượng; rỗng → 0.0.
4. Thêm 3 bạn và in.

**Code:**

```python
class HocSinh:
    """Học sinh với điểm trung bình."""

    def __init__(self, ten, diem_tb):
        self.ten = ten
        self.diem_tb = diem_tb

class LopHoc:
    """Lớp học quản lý nhiều học sinh."""

    def __init__(self, ten_lop):
        self.ten_lop = ten_lop
        self.danh_sach = []              # list chứa đối tượng HocSinh

    def them(self, hs):
        """Thêm một học sinh vào lớp."""
        self.danh_sach.append(hs)

    def trung_binh_ca_lop(self):
        """Điểm trung bình của cả lớp."""
        if len(self.danh_sach) == 0:
            return 0.0
        tong = 0.0
        for hs in self.danh_sach:
            tong += hs.diem_tb
        return tong / len(self.danh_sach)

lop = LopHoc("10A1")
lop.them(HocSinh("An", 8.5))
lop.them(HocSinh("Binh", 7.0))
lop.them(HocSinh("Cuong", 7.0))

print(f"Diem trung binh ca lop: {lop.trung_binh_ca_lop():.2f}")
```

**Giải thích code:**
* `lop.them(HocSinh("An", 8.5))` — tạo đối tượng ngay khi truyền (đối tượng "vô danh").
* `hs.diem_tb` — duyệt list và đọc thuộc tính từng đối tượng.
* (8.5 + 7.0 + 7.0) / 3 = 7.5.

**Độ phức tạp:** O(n) với n học sinh.

---

### Bài 12: Ghi đè `__str__`

**Phân tích:** Ba class cùng tên `__str__` nhưng mỗi class hiển thị theo kiểu riêng.

**Ý tưởng:** Class con định nghĩa lại `__str__`; có thể tận dụng `super().__str__()`.

**Thuật toán:**
1. `Xe.__str__` → `f"Xe {ten}, gia {gia}"`.
2. `XeMay.__str__` → thêm tiền tố `[Xe may]`.
3. `OTo.__str__` → thêm tiền tố `[Oto]`.
4. In 3 đối tượng với nhãn.

**Code:**

```python
class Xe:
    """Xe nói chung."""

    def __init__(self, ten, gia):
        self.ten = ten
        self.gia = gia

    def __str__(self):
        return f"Xe {self.ten}, gia {self.gia}"

class XeMay(Xe):
    """Xe máy — ghi đè __str__."""

    def __str__(self):
        return f"[Xe may] {self.ten}, gia {self.gia}"

class OTo(Xe):
    """Ô tô — ghi đè __str__."""

    def __str__(self):
        return f"[Oto] {self.ten}, gia {self.gia}"

xe = Xe("Cub", 30)
xemay = XeMay("Xemay", 30)
oto = OTo("Kia", 500)

print("Xe chung:", xe)
print("Xe may:", xemay)
print("O to:", oto)
```

**Giải thích code:**
* Ba class có cùng phương thức `__str__` nhưng hành vi khác nhau — đây là **đa hình** (polymorphism).
* `print(xemay)` gọi đúng `__str__` của `XeMay` chứ không phải của `Xe`.
* Có thể dùng `super().__str__()` nếu muốn lấy phần chuỗi của cha rồi thêm tiếp.

**Độ phức tạp:** O(1).

---

### Bài 13: Đóng gói với `__so_du`

**Phân tích:** Hai gạch dưới khiến Python **bẻ tên** (name mangling) — truy cập trực tiếp từ ngoài gây lỗi.

**Ý tưởng:** Chỉ thay đổi/đọc qua phương thức; dùng `try/except` để chứng minh truy cập trực tiếp lỗi.

**Thuật toán:**
1. `self.__so_du` trong `__init__`.
2. `nap(tien)` cộng; `tra_so_du()` trả về.
3. Thử `vi.__so_du` trong `try/except AttributeError`.
4. In kết quả hợp lệ.

**Code:**

```python
class ViDienTu:
    """Ví điện tử — số dư bị che giấu bằng hai gạch dưới."""

    def __init__(self, so_du):
        self.__so_du = so_du       # name mangling: thành _ViDienTu__so_du

    def nap(self, tien):
        """Nạp tiền."""
        self.__so_du += tien

    def tra_so_du(self):
        """Trả về số dư — cách hợp lệ duy nhất."""
        return self.__so_du

vi = ViDienTu(50000)
vi.nap(50000)
print("So du hop le:", vi.tra_so_du())

# Chứng minh không thể đọc trực tiếp từ bên ngoài
try:
    print(vi.__so_du)                     # ❌ AttributeError
except AttributeError:
    print("`vi.__so_du` gay AttributeError (dang bao mat)")
```

**Giải thích code:**
* `self.__so_du` bị Python đổi tên thành `_ViDienTu__so_du` — tên gốc không còn tồn tại.
* `vi.__so_du` ngoài class → `AttributeError` — đây chính là lớp bảo vệ.
* Bên trong class vẫn gọi bình thường; ngoài class phải qua `tra_so_du()`.

**Độ phức tạp:** O(1).

---

### Bài 14: `@staticmethod` và `@classmethod`

**Phân tích:** `staticmethod` không cần đối tượng/class; `classmethod` nhận `cls` để đổi thuộc tính chung.

**Ý tưởng:** `THUE` là thuộc tính lớp; `doi_thue(cls, ...)` thay đổi cho toàn class; `tinh_gia_sau_thue(gia)` là tiện ích độc lập.

**Thuật toán:**
1. `THUE = 0.1` (thuộc tính của class, chung mọi đối tượng).
2. `@staticmethod tinh_gia_sau_thue(gia)` → `gia * (1 + THUE)`.
3. `@classmethod doi_thue(cls, thue)` → `cls.THUE = thue`.
4. In giá trị trước và sau khi đổi thuế.

**Code:**

```python
class SanPham:
    """Sản phẩm với thuế chung cho cả class."""

    THUE = 0.1                            # thuộc tính class: ai cũng dùng chung

    def __init__(self, ten, gia):
        self.ten = ten
        self.gia = gia

    @staticmethod
    def tinh_gia_sau_thue(gia):
        """Tiện ích: cộng thuế vào giá. Không cần đối tượng."""
        return round(gia * (1 + SanPham.THUE), 2)

    @classmethod
    def doi_thue(cls, thue_moi):
        """Đổi thuế cho TOÀN BỘ class."""
        cls.THUE = thue_moi

print(SanPham.tinh_gia_sau_thue(100000))   # gọi qua class, không cần đối tượng
SanPham.doi_thue(0.05)
print(SanPham.tinh_gia_sau_thue(100000))
```

**Giải thích code:**
* `SanPham.tinh_gia_sau_thue(100000)` — gọi staticmethod thẳng qua class.
* `doi_thue(0.05)` — `cls` chính là `SanPham`; đổi `THUE` ai cũng thấy.
* `round(..., 2)` — làm tròn tránh lỗi số thực (`100000 * 1.1` có thể in ra `110000.00000000001`). Kết quả: 110.000.0; sau khi đổi thuế: 105.000.0.

**Độ phức tạp:** O(1).

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Quản lý điểm cá nhân

**Phân tích:** Gói trọn dữ liệu điểm + hành vi tính/xếp loại/in vào một class.

**Ý tưởng:** `tinh_tb()` phục vụ cả `xep_loai()` lẫn `__str__` — tránh lặp code.

**Thuật toán:**
1. `__init__` nhận `ten`, `lop`, list `diem`.
2. `tinh_tb()` → trung bình.
3. `xep_loai()` → dựa trên `tinh_tb()`.
4. `__str__` → chuỗi canh cột.
5. Tạo 3 học sinh, in danh sách.

**Code:**

```python
class HocSinh:
    """Học sinh với điểm 3 môn."""

    def __init__(self, ten, lop, diem):
        self.ten = ten
        self.lop = lop
        self.diem = diem                # list 3 điểm

    def tinh_tb(self):
        """Điểm trung bình."""
        return sum(self.diem) / len(self.diem)

    def xep_loai(self):
        """Xếp loại theo điểm trung bình."""
        tb = self.tinh_tb()
        if tb >= 8.0:
            return "Gioi"
        if tb >= 6.5:
            return "Kha"
        if tb >= 5.0:
            return "Trung binh"
        return "Yeu"

    def __str__(self):
        return f"{self.ten:<20} TB: {self.tinh_tb():.2f} - {self.xep_loai()}"

danh_sach = [
    HocSinh("Nguyen Van An", "10A1", [8.5, 7.0, 9.0]),
    HocSinh("Tran Thi Mai", "10A1", [6.0, 6.5, 7.0]),
    HocSinh("Le Quang Binh", "10A1", [4.5, 5.0, 5.5]),
]

for hs in danh_sach:
    print(hs)
```

**Giải thích code:**
* `xep_loai()` gọi `self.tinh_tb()` — tái sử dụng, sửa ở một nơi là đổi khắp nơi.
* `:<20` căn trái 20 ký tự cho cột tên thẳng hàng; `:.2f` làm tròn điểm.
* `print(hs)` — nhờ `__str__`, in ra đúng chuỗi định dạng.

**Độ phức tạp:** O(m) mỗi học sinh với m số môn.

---

### Bài 16: Thư viện mini

**Phân tích:** Hai class hợp tác: `Sach` là dữ liệu, `ThuVien` quản lý list sách và tìm kiếm.

**Ý tưởng:** `tim` duyệt list, lọc theo chuỗi con trong `sach.ten`.

**Thuật toán:**
1. `Sach`: `ten`, `tac_gia`, `nam`; `__str__` = `"ten - tac_gia"`.
2. `ThuVien`: list rỗng, `them`, `tim(tu_khoa)`, `ton_danh_sach()`.
3. Thêm 3 sách, tìm "Python", in kết quả.

**Code:**

```python
class Sach:
    """Quyển sách."""

    def __init__(self, ten, tac_gia, nam):
        self.ten = ten
        self.tac_gia = tac_gia
        self.nam = nam

    def __str__(self):
        return f"{self.ten} - {self.tac_gia}"

class ThuVien:
    """Thư viện quản lý các quyển sách."""

    def __init__(self):
        self.kho_sach = []

    def them(self, sach):
        """Thêm sách vào kho."""
        self.kho_sach.append(sach)

    def tim(self, tu_khoa):
        """Trả về list sách có tên chứa từ khóa."""
        ket_qua = []
        for sach in self.kho_sach:
            if tu_khoa in sach.ten:
                ket_qua.append(sach)
        return ket_qua

    def ton_danh_sach(self):
        """Số sách hiện có."""
        return len(self.kho_sach)

thu_vien = ThuVien()
thu_vien.them(Sach("Python Co Ban", "Nguyen Van An", 2024))
thu_vien.them(Sach("Toan Cao Cap", "Le B", 2023))
thu_vien.them(Sach("Python Nang Cao", "Tran B", 2025))

tim_thay = thu_vien.tim("Python")
print(f"Tim thay {len(tim_thay)} quyen:")
for sach in tim_thay:
    print("-", sach)
```

**Giải thích code:**
* `thu_vien.tim("Python")` — kiểm tra `"Python" in "Python Co Ban"` → `True`.
* List kết quả chứa **đối tượng Sach**; khi in tự gọi `__str__` của từng sách.
* `len(tim_thay)` = 2.

**Độ phức tạp:** O(n) cho `tim`, O(1) cho `them`.

---

### Bài 17: ATM hoàn chỉnh

**Phân tích:** Mọi thao tác phải kiểm tra điều kiện trước — chặn số âm và rút quá số dư.

**Ý tưởng:** Mỗi phương thức in kết quả thành công/thất bại; chỉ cập nhật `_so_du` khi hợp lệ.

**Thuật toán:**
1. `_so_du = 500000`.
2. `nap(-100)` → thất bại (số âm).
3. `rut(600000)` → thất bại (vượt số dư 500.000).
4. `nap(300000)` → 800.000.
5. `rut(400000)` → 400.000.
6. In số dư cuối.

**Code:**

```python
class ATM:
    """Máy ATM với kiểm tra chặt chẽ."""

    def __init__(self, so_du):
        self._so_du = so_du

    def nap(self, tien):
        """Nạp tiền — chỉ nhận số dương."""
        if tien <= 0:
            print("Nap that bai: so tien phai lon hon 0")
            return False
        self._so_du += tien
        print(f"Nap {tien} thanh cong")
        return True

    def rut(self, tien):
        """Rút tiền — không vượt số dư, không rút số âm."""
        if tien <= 0:
            print("Rut that bai: so tien phai lon hon 0")
            return False
        if tien > self._so_du:
            print("Rut that bai: khong du so du")
            return False
        self._so_du -= tien
        print(f"Rut {tien} thanh cong")
        return True

    def xem_so_du(self):
        """Số dư hiện tại."""
        return self._so_du

may = ATM(500000)
may.nap(-100)          # ❌ số âm
may.rut(600000)        # ❌ vượt số dư
may.nap(300000)        # ✅ 800.000
may.rut(400000)        # ✅ 400.000
print("So du cuoi:", may.xem_so_du())
```

**Giải thích code:**
* Mỗi phương thức kiểm tra 2 loại lỗi: số tiền không hợp lệ và số dư không đủ.
* `return False` giúp chỗ gọi biết kết quả — "ATM" luôn báo rõ trạng thái.
* 500.000 + 300.000 − 400.000 = 400.000.

**Độ phức tạp:** O(1).

---

### Bài 18: Kế thừa ba tầng

**Phân tích:** Chuỗi kế thừa `NhanVien → GiaoVien → GiaoVienChuNhiem`; mỗi tầng thêm thuộc tính và ghi đè `mo_ta()`.

**Ý tưởng:** Tầng con gọi `super().__init__` của tầng cha; `mo_ta()` tầng con có thể dựa trên `super().mo_ta()`.

**Thuật toán:**
1. `NhanVien.mo_ta()` → `"NV: ten (ma_so)"`.
2. `GiaoVien` thêm `mon_day`; `mo_ta()` → `"GV: ten day mon mon (ma_so)"`.
3. `GiaoVienChuNhiem` thêm `lop_cn`; `mo_ta()` → `"GVCN: ... chu nhiem lop lop_cn (ma_so)"`.
4. Tạo đối tượng tầng cuối, in cả 3 dạng.

**Code:**

```python
class NhanVien:
    """Tầng 1: nhân viên."""

    def __init__(self, ten, ma_so):
        self.ten = ten
        self.ma_so = ma_so

    def mo_ta(self):
        return f"NV: {self.ten} ({self.ma_so})"

class GiaoVien(NhanVien):
    """Tầng 2: giáo viên."""

    def __init__(self, ten, ma_so, mon_day):
        super().__init__(ten, ma_so)
        self.mon_day = mon_day

    def mo_ta(self):                     # ghi đè tầng 1
        return f"GV: {self.ten} day mon {self.mon_day} ({self.ma_so})"

class GiaoVienChuNhiem(GiaoVien):
    """Tầng 3: giáo viên chủ nhiệm."""

    def __init__(self, ten, ma_so, mon_day, lop_cn):
        super().__init__(ten, ma_so, mon_day)
        self.lop_cn = lop_cn

    def mo_ta(self):                     # ghi đè tầng 2
        return (f"GVCN: {self.ten} day mon {self.mon_day}, "
                f"chu nhiem lop {self.lop_cn} ({self.ma_so})")

gv = GiaoVienChuNhiem("An", "NV01", "Toan", "10A1")
print(gv.mo_ta())
```

**Giải thích code:**
* Chuỗi `super().__init__` chạy "cầu thang": `GiaoVienChuNhiem` → `GiaoVien` → `NhanVien`.
* Đối tượng tầng cuối có đủ 4 thuộc tính: `ten`, `ma_so`, `mon_day`, `lop_cn`.
* Gọi `gv.mo_ta()` chạy đúng phiên bản **cuối cùng** trong chuỗi kế thừa.

**Độ phức tạp:** O(1).

---

### Bài 19: Game đoán số bằng OOP

**Phân tích:** Gói trạng thái game (số bí mật, số lần đoán) vào class; người chơi là class riêng.

**Ý tưởng:** `TroChoi.doan(so)` so sánh với `self.so_bi_mat`, trả về -1/1/0 và tăng `so_lan`.

**Thuật toán:**
1. `NguoiChoi`: `ten`, `diem`.
2. `TroChoi`: `so_bi_mat` (ngẫu nhiên hoặc cố định để dễ kiểm thử), `so_lan = 0`.
3. `doan(so)`: so sánh; trả về kết quả; đúng thì `diem` người chơi +1.
4. Vòng lặp `while` đoán `5, 8, 7` đến khi đúng.

**Code:**

```python
import random

class NguoiChoi:
    """Người chơi của trò chơi."""

    def __init__(self, ten):
        self.ten = ten
        self.diem = 0

class TroChoi:
    """Trò chơi đoán số."""

    def __init__(self, so_bi_mat=None):
        # Nếu không truyền số, máy tự chọn ngẫu nhiên từ 1 đến 10
        if so_bi_mat is None:
            so_bi_mat = random.randint(1, 10)
        self.so_bi_mat = so_bi_mat
        self.so_lan = 0

    def doan(self, so):
        """So sánh số đoán với số bí mật."""
        self.so_lan += 1
        if so < self.so_bi_mat:
            return -1        # đoán nhỏ hơn
        if so > self.so_bi_mat:
            return 1         # đoán lớn hơn
        return 0             # đúng rồi

# Dùng số cố định 7 để kết quả chạy ổn định khi demo
nguoi_choi = NguoiChoi("An")
tro_choi = TroChoi(so_bi_mat=7)

cac_so_doan = [5, 8, 7]     # kịch bản đoán mẫu
ket_qua = ""

for so in cac_so_doan:
    ket_qua = tro_choi.doan(so)
    if ket_qua == -1:
        print(f"So ban doan {so} nho hon")
    elif ket_qua == 1:
        print(f"So ban doan {so} lon hon")
    else:
        print(f"Chinh xac! So bi mat la {so} sau {tro_choi.so_lan} luot")
        nguoi_choi.diem += 1
        break
```

**Giải thích code:**
* `TroChoi(so_bi_mat=7)` — tham số mặc định giúp vừa chơi ngẫu nhiên vừa kiểm thử được.
* `doan()` trả về -1/1/0 thay vì in trực tiếp — "bộ não" tách khỏi "màn hình".
* Lần 1: 5 < 7 → "nho hon"; lần 2: 8 > 7 → "lon hon"; lần 3: 7 = 7 → chiến thắng sau 3 lượt.

**Độ phức tạp:** O(1) mỗi lượt đoán.

---

### Bài 20: Quản lý trường học (tiểu dự án)

**Phân tích:** Áp dụng toàn bộ OOP: kế thừa (`HocSinh`, `GiaoVien` là `Nguoi`), hợp thành (`Truong` chứa lớp và giáo viên), `__str__`, `@staticmethod`/`@classmethod`.

**Ý tưởng:** Mỗi cấp quản lý một tầng; `Truong` tổng hợp báo cáo; `@classmethod` tạo trường mẫu, `@staticmethod` in đường phân cách.

**Thuật toán:**
1. `Nguoi` (cơ sở) + `__str__`.
2. `HocSinh(Nguoi)`: `lop`, `diem_tb`, `xep_loai()`.
3. `GiaoVien(Nguoi)`: `mon_day`.
4. `LopHoc`: list học sinh, `them`, `so_hoc_sinh()`.
5. `Truong`: `them_lop`, `them_giao_vien`, `tong_so_hoc_sinh()`, `@staticmethod` in phân cách, `@classmethod` tạo trường mẫu.
6. In báo cáo.

**Code:**

```python
class Nguoi:
    """Con người — lớp cơ sở."""

    def __init__(self, ten):
        self.ten = ten

    def __str__(self):
        return self.ten

class HocSinh(Nguoi):
    """Học sinh — là một người, thêm lớp và điểm."""

    def __init__(self, ten, lop, diem_tb):
        super().__init__(ten)
        self.lop = lop
        self.diem_tb = diem_tb

    def xep_loai(self):
        if self.diem_tb >= 8.0:
            return "Gioi"
        if self.diem_tb >= 6.5:
            return "Kha"
        return "Trung binh"

class GiaoVien(Nguoi):
    """Giáo viên — là một người, thêm môn dạy."""

    def __init__(self, ten, mon_day):
        super().__init__(ten)
        self.mon_day = mon_day

    def __str__(self):
        return f"{self.ten} day mon {self.mon_day}"

class LopHoc:
    """Lớp học gồm nhiều học sinh."""

    def __init__(self, ten_lop):
        self.ten_lop = ten_lop
        self.danh_sach = []

    def them(self, hs):
        self.danh_sach.append(hs)

    def so_hoc_sinh(self):
        return len(self.danh_sach)

class Truong:
    """Trường học — nơi hợp nhất lớp học và giáo viên."""

    def __init__(self, ten):
        self.ten = ten
        self.lop_hoc = []
        self.giao_vien = []

    def them_lop(self, lop):
        self.lop_hoc.append(lop)

    def them_giao_vien(self, gv):
        self.giao_vien.append(gv)

    def tong_so_hoc_sinh(self):
        """Tổng học sinh của mọi lớp."""
        tong = 0
        for lop in self.lop_hoc:
            tong += lop.so_hoc_sinh()
        return tong

    @staticmethod
    def in_phan_cach():
        """Static: tiện ích in đường phân cách — không cần đối tượng."""
        print("=" * 25)

    @classmethod
    def tao_truong_mau(cls):
        """Classmethod: tạo sẵn một trường có dữ liệu mẫu."""
        truong = cls("THPT Python")
        lop_a1 = LopHoc("10A1")
        lop_a1.them(HocSinh("Nguyen Van An", "10A1", 8.5))
        lop_a1.them(HocSinh("Tran Thi Mai", "10A1", 7.0))
        lop_a2 = LopHoc("10A2")
        lop_a2.them(HocSinh("Le Quang Binh", "10A2", 6.5))
        lop_a2.them(HocSinh("Pham Thu Ha", "10A2", 9.0))
        truong.them_lop(lop_a1)
        truong.them_lop(lop_a2)
        truong.them_giao_vien(GiaoVien("Co Mai", "Toan"))
        return truong

truong = Truong.tao_truong_mau()

truong.in_phan_cach()
print("Truong", truong.ten)
truong.in_phan_cach()
print("Tong so hoc sinh:", truong.tong_so_hoc_sinh())
for lop in truong.lop_hoc:
    print(f"Lop {lop.ten_lop}: {lop.so_hoc_sinh()} hoc sinh")
for gv in truong.giao_vien:
    print("Giao vien:", gv)
```

**Giải thích code:**
* Kế thừa: `HocSinh`, `GiaoVien` kế thừa `Nguoi` qua `super().__init__` — không lặp code tên.
* Hợp thành: `Truong` chứa list `LopHoc` và `GiaoVien`; `LopHoc` chứa list `HocSinh`.
* `@staticmethod` không cần `self` — gọi qua `truong.in_phan_cach()` hoặc `Truong.in_phan_cach()`.
* `@classmethod` nhận `cls` và tạo đối tượng `Truong` — dùng để "cung cấp trường mẫu".

**Độ phức tạp:** O(L + H) với L số lớp, H số học sinh.

---

## 📌 Lời khuyên cuối

* Luôn nhớ `self` đầu tiên trong phương thức, `()` khi gọi, và `super().__init__` trong class con.
* Viết `__str__` cho mọi class — cuộc sống dễ thở hơn hẳn khi in đối tượng.
* Kế thừa cho quan hệ "là một", hợp thành cho "có một" — đừng kế thừa bừa bãi.
* `_` là quy ước nội bộ, `__` là che giấu — hãy cho người dùng phương thức đúng thay vì sờ vào thuộc tính.
* Bài sau sẽ gọn nhẹ hơn hẳn với **dataclass** — Python tự sinh `__init__`, `__str__`... cho bạn!

👉 Tiếp theo: **[Bài 24: Dataclass](../24_Dataclass/bai_giang.md)**
