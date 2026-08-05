# ✅ Bài 21: Đáp Án – Package Trong Python

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án để việc học hiệu quả nhất.

> 📁 Với các bài tạo package: phần Code gồm **các file cần tạo** và **`main.py` để chạy kiểm chứng** — hãy tạo đúng cấu trúc thư mục rồi chạy `main.py`.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Tạo package đầu tiên

**Phân tích:** Package chỉ cần một thư mục + file `__init__.py`; kiểm chứng bằng cách import được.

**Ý tưởng:** Tạo thư mục `quanly`, đặt `__init__.py` trống, viết `main.py` import và in `__name__`.

**Thuật toán:**
1. Tạo thư mục `quanly`, trong đó tạo file `__init__.py` (trống).
2. Tạo `main.py` cùng cấp với `quanly`.
3. Import và in `quanly.__name__`.

**Code:**

Tạo `quanly/__init__.py` — để trống (mỗi `#` đều được):

```python
# __init__.py — đánh dấu thư mục quanly là package
```

Tạo `main.py`:

```python
# main.py — kiểm chứng package được import thành công
import quanly

print(quanly.__name__)
```

**Giải thích code:**
* `import quanly` — nạp package; nhờ có `__init__.py`, Python nhận diện thư mục là package.
* `quanly.__name__` — biến đặc biệt của mọi module/package, in ra tên `quanly`.

**Độ phức tạp:** O(1).

---

### Bài 2: Module đầu tiên trong package

**Phân tích:** Cần một module con trong package và gọi qua cú pháp chấm đầy đủ.

**Ý tưởng:** Viết hàm trong `hoc_sinh.py`; `main.py` import `quanly.hoc_sinh` rồi gọi.

**Thuật toán:**
1. Tạo `hoc_sinh.py` với hàm `chao_hoc_sinh(ten)`.
2. `main.py`: `import quanly.hoc_sinh`.
3. Gọi `quanly.hoc_sinh.chao_hoc_sinh("An")`.

**Code:**

Tạo `quanly/hoc_sinh.py`:

```python
# hoc_sinh.py — module quản lý học sinh

def chao_hoc_sinh(ten):
    """In lời chào đến một học sinh."""
    print(f"Xin chao ban {ten}!")
```

Tạo `main.py`:

```python
# main.py — dùng module trong package
import quanly.hoc_sinh

quanly.hoc_sinh.chao_hoc_sinh("An")
```

**Giải thích code:**
* `import quanly.hoc_sinh` — nạp module con; để gọi hàm phải đi qua **từng cấp**: `quanly` → `hoc_sinh` → hàm.
* f-string `f"Xin chao ban {ten}!"` — chèn giá trị `ten` vào chuỗi.

**Độ phức tạp:** O(1).

---

### Bài 3: Module thứ hai – điểm số

**Phân tích:** Hàm tính trung bình cộng list; xử lý cả trường hợp list rỗng.

**Ý tưởng:** `sum()` cộng toàn bộ, `len()` đếm số lượng; chia lấy trung bình.

**Thuật toán:**
1. Nếu list rỗng → trả về 0.0.
2. Trả về `sum(danh_sach) / len(danh_sach)`.

**Code:**

Tạo `quanly/diem.py`:

```python
# diem.py — module xử lý điểm số

def trung_binh(danh_sach):
    """Tính điểm trung bình của một list điểm."""
    if len(danh_sach) == 0:
        return 0.0
    return sum(danh_sach) / len(danh_sach)
```

Tạo `main.py`:

```python
# main.py — tính điểm trung bình
import quanly.diem

tb = quanly.diem.trung_binh([8, 7, 9])
print("Diem trung binh:", tb)
```

**Giải thích code:**
* `sum(danh_sach)` — tổng list `[8, 7, 9]` = 24.
* `24 / 3` = `8.0` — phép chia luôn trả về số thực.
* Kiểm tra `len == 0` tránh lỗi chia cho 0.

**Độ phức tạp:** O(n) với n là số phần tử list.

---

### Bài 4: Import kiểu 1 – `import quanly.hoc_sinh`

**Phân tích:** Dùng đúng cú pháp import module con và truy cập qua đầy đủ tên.

**Ý tưởng:** `tao_hoc_sinh` trả về dict; in `hs["ten"]`.

**Thuật toán:**
1. Import `quanly.hoc_sinh`.
2. Gọi `tao_hoc_sinh("Mai", "10A1")`.
3. In giá trị `ten` của dict.

**Code:**

Tạo `quanly/hoc_sinh.py`:

```python
# hoc_sinh.py — tạo và xử lý học sinh

def tao_hoc_sinh(ten, lop):
    """Tạo học sinh dạng dict."""
    return {"ten": ten, "lop": lop}
```

Tạo `main.py`:

```python
# main.py — import module con qua dấu chấm
import quanly.hoc_sinh

hs = quanly.hoc_sinh.tao_hoc_sinh("Mai", "10A1")
print(hs["ten"])
```

**Giải thích code:**
* `quanly.hoc_sinh.tao_hoc_sinh("Mai", "10A1")` — gọi qua đầy đủ 2 cấp; kết quả là dict `{"ten": "Mai", "lop": "10A1"}`.
* `hs["ten"]` — lấy giá trị theo khóa.

**Độ phức tạp:** O(1).

---

### Bài 5: Import kiểu 2 – `from quanly import diem`

**Phân tích:** Import module con bằng `from`, gọi ngắn gọn hơn.

**Ý tưởng:** `from quanly import diem` cho phép gọi `diem.trung_binh(...)`.

**Thuật toán:**
1. Import module `diem` từ package `quanly`.
2. Gọi hàm và in kết quả.

**Code:**

Tạo `quanly/diem.py` (như bài 3):

```python
# diem.py — module xử lý điểm số

def trung_binh(danh_sach):
    """Tính điểm trung bình của một list điểm."""
    if len(danh_sach) == 0:
        return 0.0
    return sum(danh_sach) / len(danh_sach)
```

Tạo `main.py`:

```python
# main.py — import module con bằng from
from quanly import diem

tb = diem.trung_binh([10, 10, 10])
print("Trung binh:", tb)
```

**Giải thích code:**
* `from quanly import diem` — lấy module `diem` ra, gọi thẳng `diem.trung_binh(...)` mà không cần tiền tố `quanly.`.
* `[10, 10, 10]` → tổng 30, chia 3 = `10.0`.

**Độ phức tạp:** O(n).

---

### Bài 6: Import kiểu 3 – lấy thẳng hàm

**Phân tích:** Import trực tiếp tên hàm giúp code ngắn nhất.

**Ý tưởng:** `from quanly.diem import trung_binh, xep_loai`; viết `xep_loai` theo thang điểm.

**Thuật toán:**
1. Viết `xep_loai(tb)` với các mốc 8.0 / 6.5 / 5.0.
2. Import thẳng hai hàm.
3. In xếp loại của 6.8.

**Code:**

Tạo `quanly/diem.py`:

```python
# diem.py — điểm số và xếp loại

def trung_binh(danh_sach):
    """Tính điểm trung bình của một list điểm."""
    if len(danh_sach) == 0:
        return 0.0
    return sum(danh_sach) / len(danh_sach)

def xep_loai(tb):
    """Xếp loại theo điểm trung bình (thang 10)."""
    if tb >= 8.0:
        return "Gioi"
    if tb >= 6.5:
        return "Kha"
    if tb >= 5.0:
        return "Trung binh"
    return "Yeu"
```

Tạo `main.py`:

```python
# main.py — import thẳng tên hàm
from quanly.diem import trung_binh, xep_loai

print("Diem 6.8 ->", xep_loai(6.8))
```

**Giải thích code:**
* Import thẳng tên → gọi `xep_loai(6.8)` không cần tiền tố.
* `6.8 >= 6.5` nên rơi vào nhánh "Kha" (thứ tự kiểm tra từ cao xuống thấp).

**Độ phức tạp:** O(1).

---

### Bài 7: Import kiểu 4 – bí danh `as`

**Phân tích:** Đặt bí danh ngắn giúp gõ nhanh; hành vi không đổi.

**Ý tưởng:** `import quanly.hoc_sinh as hs` và `import quanly.diem as d`.

**Thuật toán:**
1. Import hai module với bí danh.
2. Gọi hàm qua bí danh, in kết quả.

**Code:**

Tạo `quanly/hoc_sinh.py`:

```python
# hoc_sinh.py
def chao_hoc_sinh(ten):
    """In lời chào đến một học sinh."""
    print(f"Xin chao ban {ten}!")
```

Tạo `quanly/diem.py`:

```python
# diem.py
def trung_binh(danh_sach):
    """Tính điểm trung bình của một list điểm."""
    if len(danh_sach) == 0:
        return 0.0
    return sum(danh_sach) / len(danh_sach)
```

Tạo `main.py`:

```python
# main.py — bí danh as giúp code ngắn gọn
import quanly.hoc_sinh as hs
import quanly.diem as d

hs.chao_hoc_sinh("Binh")
print("Diem trung binh:", d.trung_binh([5, 6]))
```

**Giải thích code:**
* `as hs` — từ đây `hs` chính là `quanly.hoc_sinh`.
* `d.trung_binh([5, 6])` → tổng 11 / 2 = `5.5`.

**Độ phức tạp:** O(n).

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Học sinh dạng dict

**Phân tích:** Mỗi học sinh là một dict; hàm `hien_thi` đọc khóa và in đẹp.

**Ý tưởng:** `tao_hoc_sinh` trả dict; `hien_thi` dùng f-string.

**Thuật toán:**
1. Tạo dict `{"ten": ..., "lop": ...}`.
2. Duyệt danh sách 2 học sinh, in từng bạn.

**Code:**

Tạo `quanly/hoc_sinh.py`:

```python
# hoc_sinh.py — tạo và hiển thị học sinh

def tao_hoc_sinh(ten, lop):
    """Tạo học sinh dạng dict."""
    return {"ten": ten, "lop": lop}

def hien_thi(hs):
    """In thông tin một học sinh."""
    print(f"- {hs['ten']} (lop {hs['lop']})")
```

Tạo `main.py`:

```python
# main.py — hiển thị danh sách học sinh
from quanly import hoc_sinh

danh_sach = [
    hoc_sinh.tao_hoc_sinh("Nguyen Van An", "10A1"),
    hoc_sinh.tao_hoc_sinh("Tran Thi Mai", "11B2"),
]

for hs in danh_sach:
    hoc_sinh.hien_thi(hs)
```

**Giải thích code:**
* `hoc_sinh.tao_hoc_sinh(...)` — tạo từng dict trong list.
* Vòng `for` duyệt list, mỗi lượt gọi `hien_thi` với một học sinh.
* f-string `{hs['ten']}` — truy cập khóa trong dict ngay trong chuỗi.

**Độ phức tạp:** O(n) với n số học sinh.

---

### Bài 9: Xếp loại học sinh

**Phân tích:** Áp dụng hàm `xep_loai` cho 5 giá trị mẫu, in cặp "diem -> loai".

**Ý tưởng:** Duyệt list điểm, gọi `xep_loai` từng phần tử.

**Thuật toán:**
1. Có list 5 điểm mẫu.
2. Với mỗi điểm, in `diem -> xep_loai(diem)`.

**Code:**

Tạo `quanly/diem.py`:

```python
# diem.py — điểm số và xếp loại

def trung_binh(danh_sach):
    """Tính điểm trung bình của một list điểm."""
    if len(danh_sach) == 0:
        return 0.0
    return sum(danh_sach) / len(danh_sach)

def xep_loai(tb):
    """Xếp loại theo điểm trung bình (thang 10)."""
    if tb >= 8.0:
        return "Gioi"
    if tb >= 6.5:
        return "Kha"
    if tb >= 5.0:
        return "Trung binh"
    return "Yeu"
```

Tạo `main.py`:

```python
# main.py — xếp loại hàng loạt điểm mẫu
from quanly.diem import xep_loai

diem_mau = [9.5, 7.0, 5.2, 4.0, 8.0]

for d in diem_mau:
    print(f"{d} -> {xep_loai(d)}")
```

**Giải thích code:**
* `9.5` ≥ 8 → "Gioi"; `7.0` ≥ 6.5 → "Kha"; `5.2` ≥ 5 → "Trung binh"; `4.0` → "Yeu"; `8.0` ≥ 8 → "Gioi".
* Thứ tự `if` quan trọng: kiểm tra mốc cao trước.

**Độ phức tạp:** O(n).

---

### Bài 10: Kết hợp hai module

**Phân tích:** Dữ liệu mỗi học sinh gồm tên, lớp, list 3 điểm; cần tính TB và xếp loại.

**Ý tưởng:** Dùng `trung_binh` từ `diem.py`, in f-string canh lề.

**Thuật toán:**
1. Tạo list dict 3 học sinh kèm điểm.
2. Với mỗi học sinh: tính TB, xếp loại, in.

**Code:**

Tạo `quanly/hoc_sinh.py` và `quanly/diem.py` như bài 9 (có `tao_hoc_sinh`, `trung_binh`, `xep_loai`).

Tạo `main.py`:

```python
# main.py — kết hợp module học sinh và điểm
from quanly import hoc_sinh, diem

danh_sach = [
    {"ten": "Nguyen Van An", "lop": "10A1", "diem": [8.5, 7.0, 9.0]},
    {"ten": "Tran Thi Mai", "lop": "10A1", "diem": [6.0, 6.5, 7.0]},
    {"ten": "Le Quang Binh", "lop": "10A2", "diem": [4.5, 5.0, 5.5]},
]

for hs in danh_sach:
    tb = diem.trung_binh(hs["diem"])
    print(f"{hs['ten']}: {tb:.2f} - {diem.xep_loai(tb)}")
```

**Giải thích code:**
* `hs["diem"]` — list điểm của từng học sinh.
* `{tb:.2f}` — làm tròn 2 chữ số thập phân khi in.
* Kết quả: An TB `8.17` → Gioi; Mai `6.50` → Kha; Binh `5.00` → Trung binh.

**Độ phức tạp:** O(n × m) với n học sinh, m điểm mỗi học sinh.

---

### Bài 11: Package con

**Phân tích:** Package con nằm lồng bên trong package cha; import qua nhiều cấp chấm.

**Ý tưởng:** Tạo `quanly/giaovu/` là package con; `main.py` import `from quanly.giaovu import lop_hoc`.

**Thuật toán:**
1. Tạo `quanly/giaovu/__init__.py` (trống).
2. Tạo `quanly/giaovu/lop_hoc.py` với hàm trả list lớp.
3. `main.py` duyệt list và in.

**Code:**

Tạo `quanly/giaovu/__init__.py` (trống):

```python
# __init__.py — package con giaovu
```

Tạo `quanly/giaovu/lop_hoc.py`:

```python
# lop_hoc.py — danh sách lớp học

def danh_sach_lop():
    """Trả về danh sách các lớp của trường."""
    return ["10A1", "10A2", "11B1"]
```

Tạo `main.py`:

```python
# main.py — dùng package con
from quanly.giaovu import lop_hoc

for ten_lop in lop_hoc.danh_sach_lop():
    print("Lop:", ten_lop)
```

**Giải thích code:**
* `from quanly.giaovu import lop_hoc` — đi qua 2 cấp: `quanly` → `giaovu` → module `lop_hoc`.
* Vòng `for` in lần lượt 3 lớp.

**Độ phức tạp:** O(n) với n số lớp.

---

### Bài 12: `__init__.py` làm mặt tiền

**Phân tích:** Xuất sẵn hàm trong `__init__.py` để `import quanly` là dùng được ngay.

**Ý tưởng:** Dùng import tương đối `from .ten_file import ...` trong `__init__.py`.

**Thuật toán:**
1. `__init__.py`: import các hàm từ module con + khai báo `TEN_PHAN_MEM`.
2. `main.py`: `import quanly`, dùng thẳng hàm và biến.

**Code:**

Tạo `quanly/__init__.py`:

```python
# __init__.py — mặt tiền của package
from .hoc_sinh import tao_hoc_sinh
from .diem import trung_binh, xep_loai

TEN_PHAN_MEM = "QuanLy v1.0"
```

Tạo `quanly/hoc_sinh.py` và `quanly/diem.py` (như bài 9).

Tạo `main.py`:

```python
# main.py — import gọn từ chính package
import quanly

print(quanly.TEN_PHAN_MEM)
print("Trung binh:", quanly.trung_binh([7.0, 7.0, 7.0]))
```

**Giải thích code:**
* `from .hoc_sinh import ...` — dấu `.` = "chính package đang xét" (import tương đối).
* Sau khi xuất ra, `quanly.trung_binh(...)` dùng thẳng mà không cần tên module con.
* `[7.0, 7.0, 7.0]` → TB `7.0`.

**Độ phức tạp:** O(n).

---

### Bài 13: Package tiện ích tự đặt

**Phân tích:** Package `tien_ich` gồm hai module độc lập: toán học và chuỗi.

**Ý tưởng:** `giai_thua` dùng vòng lặp nhân dồn; `dao_nguoc` dùng cắt chuỗi.

**Thuật toán:**
1. `tinh_toan.py`: vòng lặp từ 1 → n nhân dồn vào biến.
2. `chuoi.py`: trả về `s[::-1]`.
3. `main.py` gọi và in.

**Code:**

Tạo `tien_ich/__init__.py` (trống):

```python
# __init__.py — package tien_ich
```

Tạo `tien_ich/tinh_toan.py`:

```python
# tinh_toan.py — các hàm toán học

def giai_thua(n):
    """Tính n! = 1 * 2 * ... * n."""
    ket_qua = 1
    for i in range(1, n + 1):
        ket_qua *= i
    return ket_qua
```

Tạo `tien_ich/chuoi.py`:

```python
# chuoi.py — các hàm xử lý chuỗi

def dao_nguoc(s):
    """Đảo ngược chuỗi."""
    return s[::-1]
```

Tạo `main.py`:

```python
# main.py — dùng package tien_ich
from tien_ich import tinh_toan, chuoi

print("Giai thua 5:", tinh_toan.giai_thua(5))
print("Dao nguoc:", chuoi.dao_nguoc("Python"))
```

**Giải thích code:**
* `range(1, 6)` tạo `1,2,3,4,5`; `ket_qua` nhân dồn = 120.
* `s[::-1]` — cắt chuỗi bước -1 cho ra `nohtyP`.

**Độ phức tạp:** O(n) cho giai thừa, O(n) cho đảo chuỗi.

---

### Bài 14: Hai package, không đụng nhau

**Phân tích:** Hai package cùng tên hàm nhưng độc lập; dùng `as` để phân biệt.

**Ý tưởng:** Mỗi package có hàm `xep_loai`; vì file `xep_loai.py` trùng tên với hàm, cần **xuất hàm ra ở `__init__.py`** để `from diem import xep_loai` lấy đúng hàm (nếu không sẽ lấy nhầm *module*, gây lỗi khi gọi).

**Thuật toán:**
1. Tạo package `diem` với hàm `xep_loai` thang 10, xuất ra ở `__init__.py`.
2. Tạo package `danh_gia` với hàm `xep_loai` thang 100, xuất ra ở `__init__.py`.
3. `main.py` import cả hai với `as`, gọi và in.

**Code:**

Tạo `diem/__init__.py`:

```python
# __init__.py — xuất hàm xep_loai ra "mặt tiền" của package diem
from .xep_loai import xep_loai
```

Tạo `diem/xep_loai.py`:

```python
# xep_loai.py trong package diem — thang điểm 10

def xep_loai(tb):
    """Xếp loại theo thang điểm 10."""
    if tb >= 8.0:
        return "Gioi"
    if tb >= 6.5:
        return "Kha"
    if tb >= 5.0:
        return "Trung binh"
    return "Yeu"
```

Tạo `danh_gia/__init__.py`:

```python
# __init__.py — xuất hàm xep_loai ra "mặt tiền" của package danh_gia
from .xep_loai import xep_loai
```

Tạo `danh_gia/xep_loai.py`:

```python
# xep_loai.py trong package danh_gia — thang điểm 100

def xep_loai(tb):
    """Đánh giá theo thang điểm 100."""
    if tb >= 80:
        return "Tot"
    return "Chua tot"
```

Tạo `main.py`:

```python
# main.py — hai package cùng tên hàm, không xung đột
from diem import xep_loai as xep_loai_diem
from danh_gia import xep_loai as xep_loai_danh_gia

print("Diem 8.0 ->", xep_loai_diem(8.0))
print("Danh gia 80 ->", xep_loai_danh_gia(80))
```

**Giải thích code:**
* Vì trong package đã có module `xep_loai.py`, nếu `__init__.py` không xuất hàm, lệnh `from diem import xep_loai` sẽ lấy **nhầm module** (gọi sẽ báo `TypeError`). Nhờ `from .xep_loai import xep_loai` trong `__init__.py`, package "mặt tiền" trả đúng **hàm**.
* `as xep_loai_diem` — bí danh riêng cho hàm của package `diem`.
* Không có `as` thì hàm sau sẽ ghi đè hàm trước; có `as` thì cả hai sống chung.

**Độ phức tạp:** O(1).

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Thống kê học sinh theo lớp

**Phân tích:** Đếm số học sinh mỗi lớp, lưu vào dict `{lop: so_luong}`.

**Ý tưởng:** Duyệt danh sách; lớp chưa có trong dict thì gán 0 rồi +1.

**Thuật toán:**
1. Khởi tạo dict rỗng.
2. Với mỗi học sinh: `lop = hs["lop"]`, nếu chưa có → `0`, rồi `+1`.
3. In từng cặp lớp – số lượng.

**Code:**

Tạo `quanly/hoc_sinh.py`:

```python
# hoc_sinh.py — tạo, hiển thị, thống kê học sinh

def tao_hoc_sinh(ten, lop):
    """Tạo học sinh dạng dict."""
    return {"ten": ten, "lop": lop}

def thong_ke(danh_sach):
    """Đếm số học sinh theo từng lớp."""
    ket_qua = {}
    for hs in danh_sach:
        lop = hs["lop"]
        if lop not in ket_qua:      # lớp gặp lần đầu
            ket_qua[lop] = 0
        ket_qua[lop] += 1
    return ket_qua
```

Tạo `main.py`:

```python
# main.py — thống kê học sinh theo lớp
from quanly.hoc_sinh import tao_hoc_sinh, thong_ke

danh_sach = [
    tao_hoc_sinh("Nguyen Van An", "10A1"),
    tao_hoc_sinh("Tran Thi Mai", "10A1"),
    tao_hoc_sinh("Le Quang Binh", "10A2"),
    tao_hoc_sinh("Pham Thu Ha", "10A2"),
]

print("Thong ke theo lop:")
for lop, so_luong in thong_ke(danh_sach).items():
    print(f"{lop}: {so_luong} hoc sinh")
```

**Giải thích code:**
* `if lop not in ket_qua` — kiểm tra khóa đã tồn tại chưa (kiến thức Bài 17).
* `dict.items()` — duyệt cặp (khóa, giá trị) để in.

**Độ phức tạp:** O(n) với n học sinh.

---

### Bài 16: Tìm học sinh điểm cao nhất

**Phân tích:** Cần tính TB từng học sinh rồi chọn bạn cao nhất.

**Ý tưởng:** Lưu cặp `(ten, tb)` vào list; duyệt so sánh lưu giá trị lớn nhất.

**Thuật toán:**
1. Với mỗi học sinh: tính TB bằng `trung_binh`.
2. So sánh và lưu `(ten, tb)` cao nhất.
3. In kết quả làm tròn 2 chữ số.

**Code:**

Tạo `quanly/diem.py` (hàm `trung_binh` như bài 9).

Tạo `main.py`:

```python
# main.py — tìm học sinh điểm trung bình cao nhất
from quanly.diem import trung_binh

danh_sach = [
    {"ten": "Nguyen Van An", "diem": [8.5, 7.0, 9.0]},
    {"ten": "Tran Thi Mai", "diem": [6.0, 6.5, 7.0]},
    {"ten": "Le Quang Binh", "diem": [9.0, 9.5, 8.5]},
]

ten_tot_nhat = ""
tb_tot_nhat = -1.0

for hs in danh_sach:
    tb = trung_binh(hs["diem"])
    if tb > tb_tot_nhat:        # tìm thấy bạn có điểm TB cao hơn
        tb_tot_nhat = tb
        ten_tot_nhat = hs["ten"]

print(f"Hoc sinh cao diem nhat: {ten_tot_nhat} ({tb_tot_nhat:.2f})")
```

**Giải thích code:**
* `tb_tot_nhat = -1.0` — khởi tạo nhỏ hơn mọi điểm hợp lệ để vòng lặp so sánh đúng.
* Mỗi lượt nếu TB lớn hơn thì cập nhật cả tên và TB.

**Độ phức tạp:** O(n × m) với n học sinh, m điểm mỗi học sinh.

---

### Bài 17: Module con sử dụng lẫn nhau

**Phân tích:** Module `bang_diem` dùng chính hàm của module `diem` trong cùng package.

**Ý tưởng:** Trong `bang_diem.py` dùng import tương đối `from . import diem`.

**Thuật toán:**
1. `bang_diem.py`: `from . import diem`, viết `in_bang(danh_sach)`.
2. In tiêu đề cột, mỗi hàng canh lề bằng f-string.
3. `main.py` gọi `in_bang`.

**Code:**

Tạo `quanly/bang_diem.py`:

```python
# bang_diem.py — in bảng điểm, dùng lại module diem

from . import diem      # import tương đối: module diem cùng package

def in_bang(danh_sach):
    """In bảng điểm 3 môn và điểm trung bình."""
    print(f"{'Ten':<20} {'Toan':<5} {'Van':<5} {'Anh':<5} {'TB':<6}")
    for hs in danh_sach:
        t, v, a = hs["diem"]            # gán ba môn
        tb = diem.trung_binh(hs["diem"])
        print(f"{hs['ten']:<20} {t:<5} {v:<5} {a:<5} {tb:.2f}")
```

Tạo `main.py`:

```python
# main.py — in bảng điểm qua module bang_diem
from quanly.bang_diem import in_bang

danh_sach = [
    {"ten": "Nguyen Van An", "diem": [8.5, 7.0, 9.0]},
    {"ten": "Tran Thi Mai", "diem": [6.0, 6.5, 7.0]},
]

in_bang(danh_sach)
```

**Giải thích code:**
* `from . import diem` — nạp module `diem` ngay trong package (không cần `quanly.`).
* `t, v, a = hs["diem"]` — giải nén list 3 phần tử vào 3 biến (kiến thức Bài 15).
* `:<20` căn trái với độ rộng 20 ký tự, giúp cột thẳng hàng.

**Độ phức tạp:** O(n) với n học sinh.

---

### Bài 18: Package mô phỏng ngân hàng

**Phân tích:** Hai module: tài khoản (số dư, nạp, rút) và lịch sử giao dịch.

**Ý tưởng:** Tài khoản là dict `{"so_du": ...}`; `rut` kiểm tra đủ tiền rồi mới trừ.

**Thuật toán:**
1. `tao_tai_khoan(so_du)` trả dict.
2. `nap`/`rut` cập nhật số dư; `rut` chặn khi thiếu tiền.
3. `ghi_giao_dich` thêm chuỗi mô tả vào list.
4. `main.py` chạy kịch bản và in lịch sử.

**Code:**

Tạo `ngan_hang/__init__.py` (trống).

Tạo `ngan_hang/tai_khoan.py`:

```python
# tai_khoan.py — thao tác số dư tài khoản

def tao_tai_khoan(so_du):
    """Tạo tài khoản với số dư ban đầu."""
    return {"so_du": so_du}

def nap(tk, tien):
    """Nạp tiền, cập nhật số dư."""
    tk["so_du"] += tien

def rut(tk, tien):
    """Rút tiền; trả về True nếu thành công, False nếu thiếu tiền."""
    if tien > tk["so_du"]:
        return False
    tk["so_du"] -= tien
    return True
```

Tạo `ngan_hang/giao_dich.py`:

```python
# giao_dich.py — lịch sử giao dịch

def ghi_giao_dich(lich_su, mo_ta):
    """Thêm một giao dịch vào lịch sử."""
    lich_su.append(mo_ta)
```

Tạo `main.py`:

```python
# main.py — mô phỏng giao dịch ngân hàng
from ngan_hang import tai_khoan, giao_dich

tk = tai_khoan.tao_tai_khoan(500000)
lich_su = []

giao_dich.ghi_giao_dich(lich_su, "Nap 200000")
tai_khoan.nap(tk, 200000)

giao_dich.ghi_giao_dich(lich_su, "Rut 100000")
tai_khoan.rut(tk, 100000)

print("So du:", tk["so_du"])
print("Lich su giao dich:")
for gd in lich_su:
    print("-", gd)
```

**Giải thích code:**
* `tk["so_du"] += tien` — cộng dồn vào khóa `so_du` của dict.
* Lịch sử là list chứa chuỗi mô tả — mỗi thao tác thêm một dòng.
* Số dư: 500000 + 200000 − 100000 = 600000.

**Độ phức tạp:** O(1) mỗi thao tác; O(k) khi in k giao dịch.

---

### Bài 19: Tái cấu trúc từ Bài 20

**Phân tích:** Chuyển module `tien_ich.py` (Bài 20) thành package gồm 2 module chuyên biệt.

**Ý tưởng:** Tách hàm hình tròn và hình chữ nhật thành 2 file; `main.py` dùng lại như cũ.

**Thuật toán:**
1. Tạo package `tien_ich` với `hinh_tron.py` và `hinh_chu_nhat.py`.
2. `main.py` import và in 4 kết quả (làm tròn hình tròn 2 chữ số).

**Code:**

Tạo `tien_ich/__init__.py` (trống).

Tạo `tien_ich/hinh_tron.py`:

```python
# hinh_tron.py — công thức hình tròn

PI = 3.14159

def dien_tich_hinh_tron(r):
    """Diện tích hình tròn: pi * r^2."""
    return PI * r * r

def chu_vi_hinh_tron(r):
    """Chu vi hình tròn: 2 * pi * r."""
    return 2 * PI * r
```

Tạo `tien_ich/hinh_chu_nhat.py`:

```python
# hinh_chu_nhat.py — công thức hình chữ nhật

def dien_tich(dai, rong):
    """Diện tích hình chữ nhật."""
    return dai * rong

def chu_vi(dai, rong):
    """Chu vi hình chữ nhật."""
    return 2 * (dai + rong)
```

Tạo `main.py`:

```python
# main.py — dùng package tien_ich tách từ Bài 20
from tien_ich import hinh_tron, hinh_chu_nhat

r = 5
dai, rong = 4, 3

print(f"Hinh tron r={r}: dien tich {hinh_tron.dien_tich_hinh_tron(r):.2f}, "
      f"chu vi {hinh_tron.chu_vi_hinh_tron(r):.2f}")
print(f"Hinh chu nhat {dai}x{rong}: dien tich {hinh_chu_nhat.dien_tich(dai, rong)}, "
      f"chu vi {hinh_chu_nhat.chu_vi(dai, rong)}")
```

**Giải thích code:**
* Hàm cũ không đổi — chỉ đổi "nơi ở": từ 1 file thành package 2 file.
* `:.2f` làm tròn diện tích 78.54 và chu vi 31.42.
* Tách module giúp sau này thêm `hinh_tam_giac.py` mà không đụng code cũ.

**Độ phức tạp:** O(1).

---

### Bài 20: Tiểu dự án – hệ thống quản lý điểm

**Phân tích:** Gói toàn bộ kiến thức: package chuẩn, mặt tiền `__init__.py`, thống kê, xếp loại.

**Ý tưởng:** Xây dựng `quanly` hoàn chỉnh rồi viết `main.py` dùng mọi thứ một lần.

**Thuật toán:**
1. `__init__.py`: xuất hàm chính + `__version__`.
2. `hoc_sinh.py`: `tao_hoc_sinh`, `hien_thi`, `thong_ke`.
3. `diem.py`: `trung_binh`, `xep_loai`.
4. `main.py`: tạo 4 học sinh → bảng điểm → thống kê → in phiên bản.

**Code:**

Tạo `quanly/__init__.py`:

```python
# __init__.py — mặt tiền của hệ thống
from .hoc_sinh import tao_hoc_sinh, hien_thi, thong_ke
from .diem import trung_binh, xep_loai

__version__ = "1.0"
```

Tạo `quanly/hoc_sinh.py`:

```python
# hoc_sinh.py — học sinh

def tao_hoc_sinh(ten, lop):
    """Tạo học sinh dạng dict."""
    return {"ten": ten, "lop": lop}

def hien_thi(hs):
    """In thông tin một học sinh."""
    print(f"- {hs['ten']} (lop {hs['lop']})")

def thong_ke(danh_sach):
    """Đếm số học sinh theo từng lớp."""
    ket_qua = {}
    for hs in danh_sach:
        lop = hs["lop"]
        if lop not in ket_qua:
            ket_qua[lop] = 0
        ket_qua[lop] += 1
    return ket_qua
```

Tạo `quanly/diem.py`:

```python
# diem.py — điểm số

def trung_binh(danh_sach):
    """Tính điểm trung bình của một list điểm."""
    if len(danh_sach) == 0:
        return 0.0
    return sum(danh_sach) / len(danh_sach)

def xep_loai(tb):
    """Xếp loại theo điểm trung bình (thang 10)."""
    if tb >= 8.0:
        return "Gioi"
    if tb >= 6.5:
        return "Kha"
    if tb >= 5.0:
        return "Trung binh"
    return "Yeu"
```

Tạo `main.py`:

```python
# main.py — chương trình chính của hệ thống quản lý điểm
import quanly

print("Quan ly hoc sinh v" + quanly.__version__)
print("=== BANG DIEM ===")

danh_sach = [
    {"ten": "Nguyen Van An", "lop": "10A1", "diem": [8.5, 7.0, 9.0]},
    {"ten": "Tran Thi Mai", "lop": "10A1", "diem": [6.0, 6.5, 7.0]},
    {"ten": "Le Quang Binh", "lop": "10A2", "diem": [4.5, 5.0, 5.5]},
    {"ten": "Pham Thu Ha", "lop": "10A2", "diem": [9.0, 8.5, 8.0]},
]

for hs in danh_sach:
    tb = quanly.trung_binh(hs["diem"])
    print(f"{hs['ten']:<20} TB: {tb:.2f} - {quanly.xep_loai(tb)}")

print("=== THONG KE ===")
for lop, so_luong in quanly.thong_ke(danh_sach).items():
    print(f"{lop}: {so_luong} hoc sinh")
```

**Giải thích code:**
* Chỉ cần `import quanly` — mọi hàm đã được xuất qua mặt tiền `__init__.py`.
* `quanly.__version__` — đọc phiên bản từ chính package.
* Mỗi khối in rõ ràng: bảng điểm → thống kê, dùng đúng hàm đã xây.

**Độ phức tạp:** O(n) cho bảng điểm, O(n) cho thống kê (n học sinh).

---

## 📌 Lời khuyên cuối

* Package giúp dự án "lớn mà không loạn" — hãy luôn đặt `__init__.py` và import đúng cấp.
* Khi gặp `ModuleNotFoundError`, kiểm tra **vị trí file** trước tiên, rồi mới kiểm tra tên.
* `import quanly` không nạp module con — đây là lỗi phổ biến nhất của người mới.
* Bài sau là **Đọc/Ghi file** — lưu dữ liệu ra đĩa để tắt máy không mất!

👉 Tiếp theo: **[Bài 22: Đọc Và Ghi File](../22_File/bai_giang.md)**
