# ✅ Bài 40: Đáp Án – Mini Project Quản Lý Cửa Hàng Sách

> 🎯 **Hướng dẫn:** Mỗi bài giải gồm **Phân tích → Ý tưởng → Thuật toán → Code → Giải thích → Độ phức tạp**. Toàn bộ code chạy được với **Python 3.9+**. Cuối file là **chương trình hoàn chỉnh** `quan_ly_sach.py` ghép toàn bộ 20 bài.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Tạo dữ liệu sách

**Phân tích:** Mỗi cuốn sách là một dict với 6 khóa cố định; hàm `tao_sach` chuẩn hóa việc tạo dict.

**Ý tưởng:** Hàm nhận 6 tham số và trả `{...}` — tập trung cấu trúc dữ liệu vào một chỗ duy nhất.

**Thuật toán:**
1. Import `Dict, List` từ `typing`.
2. Hàm `tao_sach(...)` trả dict.
3. Tạo 2 cuốn, in `kho[0]["ten"]`.

**Code:**

```python
from typing import Dict, List

def tao_sach(ma: int, ten: str, tac_gia: str, the_loai: str,
             gia: float, so_luong: int) -> Dict[str, object]:
    """Trả về dict đại diện một cuốn sách."""
    return {
        "ma": ma,
        "ten": ten,
        "tac_gia": tac_gia,
        "the_loai": the_loai,
        "gia": gia,
        "so_luong": so_luong,
    }

kho: List[Dict[str, object]] = [
    tao_sach(1, "De Men Phieu Luu Ky", "To Hoai", "Truyen", 65000.0, 12),
    tao_sach(2, "Tuoi tho du doi", "Nguyen Nhat Anh", "Van hoc", 58000.0, 8),
]

print("Cuon dau:", kho[0]["ten"])
```

**Giải thích code:**
* `Dict[str, object]` nói "dict mà khóa là chuỗi, giá trị bất kỳ" — đủ cho cấu trúc đa kiểu này.
* `kho` là list các dict — dữ liệu chính của ứng dụng.

**Độ phức tạp:** O(1) — tạo 2 phần tử.

---

### Bài 2: Hiển thị kho rỗng

**Phân tích:** Hàm hiển thị phải an toàn với danh sách rỗng — đây là thông lệ của mọi ứng dụng CRUD.

**Ý tưởng:** List rỗng có giá trị truthy là `False`, nên `if not danh_sach:` bắt được trường hợp rỗng.

**Thuật toán:**
1. Tham số `danh_sach: List[Dict[str, object]]`.
2. Nếu rỗng → in `"Kho dang rong."` và `return`.
3. Ngược lại sẽ in từng sách (đã làm ở bài 3).

**Code:**

```python
from typing import Dict, List

def hien_thi_danh_sach(danh_sach: List[Dict[str, object]]) -> None:
    """In toàn bộ sách trong kho."""
    if not danh_sach:
        print("Kho dang rong.")
        return
    for s in danh_sach:
        print(f"{s['ma']}  {s['ten']}")

hien_thi_danh_sach([])   # Kho dang rong.
```

**Giải thích:** `if not danh_sach` — list rỗng coi là `False` → rẽ nhánh sớm (early return) tránh vòng lặp thừa.

**Độ phức tạp:** O(1) khi rỗng.

---

### 3: Hiển thị 2 cuốn sách

**Phân tích:** Hiển thị có thông tin đầy đủ. Dùng f-string với căn lề để bảng thẳng cột.

**Ý tưởng:** Mỗi dòng in ra các trường cách nhau; thường kèm tiêu đề bảng.

**Code:**

```python
from typing import Dict, List

def hien_thi_danh_sach(danh_sach: List[Dict[str, object]]) -> None:
    if not danh_sach:
        print("Kho dang rong.")
        return
    print(f"{'Ma':<4}{'Ten':<26}{'Tac gia':<16}{'The loai':<12}"
          f"{'Gia':<10}{'SL':<5}")
    print("-" * 72)
    for s in danh_sach:
        print(f"{s['ma']:<4}{s['ten']:<26}{s['tac_gia']:<16}"
              f"{s['the_loai']:<12}{s['gia']:<10}{s['so_luong']:<6}")

kho = [
    {"ma": 1, "ten": "De Men Phieu Luu Ky", "tac_gia": "To Hoai",
     "the_loai": "Truyen", "gia": 65000.0, "so_luong": 12},
    {"ma": 2, "ten": "Tuoi tho du doi", "tac_gia": "Nguyen Nhat Anh",
     "the_loai": "Van hoc", "gia": 58000.0, "so_luong": 8},
]
hien_thi_danh_sach(kho)
```

**Giải thích:** Căn lề `:<n` giúp cột thẳng hàng; kiểu dữ liệu lặp — tương đương output đề bài.

**Độ phức tạp:** O(n) với n là số sách.

---

### 4: Tìm sách theo mã

**Phân tích:** Hàm tìm theo mã trả về **vị trí** (index) — tiện cho sửa/xóa về sau — hoặc `None`.

**Ý tưởng:** `enumerate` vừa lấy chỉ số vừa lấy phần tử; `return` ngay khi khớp (early return).

**Code:**

```python
from typing import Dict, List, Optional

def tim_theo_ma(danh_sach: List[Dict[str, object]], ma: int) -> Optional[int]:
    """Trả về vị trí của sách có mã cho trước; None nếu không có."""
    for i, s in enumerate(danh_sach):
        if s["ma"] == ma:
            return i
    return None

kho = [
    {"ma": 1, "ten": "De Men Phieu Luu Ky"},
    {"ma": 2, "ten": "Tuoi tho du doi"},
]

print("Vi tri ma 1:", tim_theo_ma(kho, 1))
print("Vi tri ma 99:", tim_theo_ma(kho, 99))
```

**Giải thích:** `Optional[int]` truyền tải "có thể không tìm thấy" — người gọi kiểm tra trước khuchaeo dùng.

**Độ phức tạp:** O(n) — tuyến tuyến qua n sách.

---

### 5: Tìm sách theo tên (không phân biệt hoa thường)

**Phân tích:** Cần tìm kiếm mềm dẻo: cho phép người dùng gõ sai hoa thường. Kỹ thuật đưa cả hai về chữ thường bằng `.lower()`.

**Ý tưởng:** Kiểm tra `ten_can_tim` là **chuỗi con** (nằm trong) tên sách, cả hai đều `.lower()`.

**Code:**

```python
from typing import Dict, List, Optional

def tim_theo_ten(danh_sach: List[Dict[str, object]],
                 ten_can_tim: str) -> Optional[Dict[str, object]]:
    """Trả sách đầu tiên có tên chứa chuỗi (không phân biệt hoa thường)."""
    ten_can_tim = ten_can_tim.lower()
    for s in danh_sach:
        if ten_can_tim in str(s["ten"]).lower():
            return s
    return None

kho = [{"ma": 1, "ten": "De Men Phieu Luu Ky"}]

sach = tim_theo_ten(kho, "DE")
print("Tim thay:", sach["ten"] if sach else "Khong tim thay.")
```

**Giải thích:** `in` kiểm tra chuỗi con; câu in dùng biểu thức điều kiện — tìm thấy in tên, không thấy in thông báo.

**Độ phức tạp:** O(n×m) với m độ dài tên (do so khớp con).

---

### 6: Đếm số đầu sách

**Phân tích:** Số đầu sách = số phần tử trong list.

**Ý tưởng:** `len(danh_sach)` là hàm đếm nhanh nhất.

**Code:**

```python
def dem_dau_sach(danh_sach) -> int:
    """Trả về số lượng sách đang có trong kho."""
    return len(danh_sach)

kho = [{"ma": 1}, {"ma": 2}]
print("So dau sach:", dem_dau_sach(kho))
```

**Giải thích:** Chỉ cần biết length — không cần vòng lặp.

**Độ phức tạp:** O(1).

---

### 7: Tổng số cuốn trong kho

**Phân tích:** Cộng dồn trường `so_luong` của mọi sách.

**Ý tưởng:** Generator expression `sum(...)` là cách gọn nhất.

**Code:**

```python
from typing import Dict, List

def lai_noi_4_tong_so(danh_sach: List[Dict[str, object]]) -> int:
    """Trả về tổng số cuốn sách trong kho."""
    return sum(int(s["so_luong"]) for s in danh_sach)

kho = [{"ma": 1, "so_luong": 12}, {"ma": 2, "so_luong": 8}]

print("Tong so cuon:", tong_so_cuon(kho))
```

**Giải thích:** `sum(generator)` cộng tất cả; `int(...)` bảo đảm tính số.

**Độ phức tạp:** O(n).

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Thêm sách với mã tự tăng

**Phân tích:** Mã mới phải **khác mọi mã cũ**, kể cả sau khi xóa một số sách → dùng mã lớn nhất cộng 1.

**Ý tưởng:** `max((s["ma"] for s in danh_sach), default=0)` — generator lấy mọi `ma`; `default=0` giữ an toàn khi list rỗng.

**Code:**

```python
from typing import Dict, List

def them_sach(danh_sach: List[Dict[str, object]],
              ten: str, tac_gia: str, the_loai: str,
              gia: int, so_luong: int) -> None:
    """Thêm sách mới với mã tự tăng."""
    ma = max((s["ma"] for s in danh_sach), default=0) + 1   # mã mới
    danh_sach.append({
        "ma": ma, "ten": ten, "tac_gia": tac_gia,
        "the_loai": the_loai, "gia": gia, "so_luong": so_luong,
    })
    print("Ma moi:", ma)

kho: List[Dict[str, object]] = [{"ma": 2}]
them_sach(kho, "Cho toi mot ve", "Nguyen Nhat Anh", "Van hoc", 50000, 5)
```

**Giải thích:** `max(... generator ...)` chạy qua mọi `ma`, `default` giữ không lỗi khi khôông có phần tử nào.

**Độ phức tạp:** O(n) — duyệt list để tìm mã max.

---

### 9: Sửa giá theo mã

**Phân tích:** Sửa một trường của sách đã có. Dùng lại `tim_theo_ma` (bài 4) để có vị trí.

**Ý tưởng:** Nếu có vị trí → đổi `s["gia"]`; trả code thành công/thất bại.

**Code:**

```python
from typing import Dict, List, Optional

def tim_theo_ma(danh_sach: List[Dict[str, object]], ma: int) -> Optional[int]:
    for i, s in enumerate(danh_sach):
        if s["ma"] == ma:
            return i
    return None

def sua_gia(danh_sach: List[Dict[str, object]], ma: int, gia_moi: float) -> bool:
    """Đổi giá sách có mã; trả True nếu thực hiện được."""
    vitri = tim_theo_ma(danh_sach, ma)
    if vitri is None:
        return False
    danh_sach[vitri]["gia"] = gia_moi
    return True

kho = [{"ma": 1, "gia": 50000.0}, {"ma": 2, "gia": 40000.0}]
if sua_gia(kho, 2, 70000.0):
    print("Da sua. Gia moi:", kho[1]["gia"])
```

**Giải thích cấu trúc:** tách hàm "tìm" khỏi hàm "sửa" — `sua_gia` gọi lại `tim_theo_ma`, tái sử dụng (không trùng code).

**Độ phức tạp:** O(n) cho tìm + O(1) cho đổi.

---

### 10: Xóa sách theo mã

**Phân tích:** Xóa bằng vị trí qua phương thức `pop`; trả `True`/`False` cho người gọi biết kết quả.

**Ý tưởng:** Nếu có vị trí → `danh_sach.pop(vitri)`.

**Code:**

```python
from typing import Dict, List, Optional

def tim_theo_ma(danh_sach: List[Dict[str, object]], ma: int) -> Optional[int]:
    for i, s in enumerate(danh_sach):
        if s["ma"] == ma:
            return i
    return None

def xoa_sach(danh_sach: List[Dict[str, object]], ma: int) -> bool:
    """Xóa sách có mã; trả True nếu xóa được."""
    vitri = tim_theo_ma(danh_sach, ma)
    if vitri is None:
        return False
    danh_sach.pop(vitri)
    return True

danh_sach = [{"ma": 1, "ten": "A"}, {"ma": 2, "ten": "B"}]
xoa_sach(danh_sach, 1)
print("Con lai:", len(danh_sach))
```

**Giải thích:** `pop(index)` vừa lấy vừa xóa phần tử tại vị trí; list tự dịch lại về sau.

**Độ phức tạp:** O(n) tìm + O(n) pop (dịch phần tử phía sau).

---

### 11: Thống kê cơ bản

**Phân tích:** Ba con số: số đầu sách, tổng cuốn, tổng giá trị. Đây là báo cáo thường gặp.

**Ý tưởng:** `len`, `sum(so_luong)`, `sum(gia * so_luong)` — đều bằng generator toán.

**Code:**

```python
from typing import Dict, List

def thong_ke(danh_sach: List[Dict[str, object]]) -> None:
    """In báo cáo tổng hợp kho."""
    if not danh_sach:
        print("Kho rong.")
        return
    so_dau = len(danh_sach)
    tong_cuon = sum(int(s["so_luong"]) for s in danh_sach)
    tong_gia_tri = sum(float(s["gia"]) * int(s["so_luong"]) for s in danh_sach)
    print(f"So dau sach: {so_dau}")
    print(f"Tong so cuon: {tong_cuong}")
    print(f"Tong gia tri: {tong_gia_tri:,.0f} dong")

kho = [
    {"ma": 1, "gia": 65000.0, "so_luong": 12},
    {"ma": 2, "gia": 58000.0, "so_luong": 8},
]
thong_ke(kho)
```

**Giải thích:** `f"{x:,.0f}"` chèn dấu phẩy cho dễ đọc (`1,244,000`).

**Độ phức tạp:** O(n).

---

### 12: Tìm sách đắt nhất

**Phân tích:** Cần cuốn có `gia` lớn nhất → hàm có sẵn `max` với `key`.

**Ý tưởng:** `max(danh_sach, key=lambda s: s["gia"])`.

**Code:**

```python
from typing import Dict, List

def dat_nhat(danh_sach: List[Dict[str, object]]) -> Dict[str, object]:
    """Trả về sách có giá cao nhất."""
    return max(danh_sach, key=lambda s: s["gia"])

kho = [
    {"ma": 1, "ten": "De Men Phieu Luu Ky", "gia": 65000.0},
    {"ma": 2, "ten": "Tuoi tho du doi", "gia": 58000.0},
]
x = dat_nhat(kho)
print("Dat nhat:", x["ten"], "-", x["gia"])
```

**Giải thích:** `key` quyết định tiêu chí so sánh (lấy trường `gia`).

**Độ phức tạp:** O(n).

---

### 13: Lưu danh sách ra JSON

**Phân tích:** Khi dữ liệu chỉ trong RAM, đóng máy là mất. Lưu JSON giữ dữ liệu giữa các phiên chạy.

**Ý tưởng:** `json.dump` toàn khối list; nhớ `ensure_ascii=False` và `indent=2` cho đẹp và đúng tiếng Việt.

**Code:**

```python
import json
from typing import Dict, List

def luu_file(danh_sach: List[Dict[str, object]], ten_file: str) -> None:
    """Ghi toàn bộ danh sách ra file JSON."""
    with open(ten_file, "w", encoding="utf-8") as f:
        json.dump(danh_sach, f, ensure_ascii=False, indent=2)
    print(f"Da luu {len(danh_sach)} cuon sach.")

kho = [{"ma": 1, "ten": "De Men", "gia": 65000.0}]
luu_file(kho, "kho_test.json")
```

**Giải thích:** `open(..., "w")` mở ghi; mở trong `with` tự đóng. File sinh ra có nội dung có dấccc.

**Độ phức tạp:** O(n) — tuần tự ghi toàn list.

---

### 14: Nạp danh sách từ JSON

**Phân tích:** Khi máy không có file (lần chạy đầu), chương trình không được nổ crash → bắt ngoại lệ, trả `[]`.

**Ý tưởng:** `try: json.load`; `except FileNotFoundError: return []`.

**Code:**

```python
import json
from typing import Dict, List

def nap_file(ten_file: str) -> List[Dict[str, object]]:
    """Đọc file JSON thành list; file không tồn tại trả list rỗng."""
    try:
        with open(ten_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

du_lieu = nap_file("kho_test.json")       # đã lưu ở bài 13
print("Doc duoc:", len(du_lieu))

rong = nap_file("khong_co.json")
print("File khong co:", len(rong))
```

**Giải thích:** `except FileNotFoundError` là cách "dung túng" thiếu sót file — dữ liệu mặc định rỗng.

**Độ phức tạp:** O(n) đọc; O(1) khi không có file.

<!-- PHAN_2 -->

> 🎯 **Hướng dẫn:** Tiếp theo là **🔴 Khó (Bài 15 – 20)** và **chương trình hoàn chỉnh**.