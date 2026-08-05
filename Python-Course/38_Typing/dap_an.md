# ✅ Bài 38: Đáp Án – Type Hints

> 🎯 **Hướng dẫn:** Mỗi bài giải gồm các mục **Phân tích → Ý tưởng → Thuật toán → Code → Giải thích → Độ phức tạp**. Toàn bộ code chạy được với **Python 3.9+**, tuân theo **PEP 8**, có comment tiếng Việt. Hãy tự làm trước khi xem đáp án!

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Khai báo biến có chú thích

**Phân tích:** Cần khai báo 4 biến với 4 kiểu khác nhau (`str`, `int`, `float`, `bool`) rồi in chúng trên cùng một dòng.

**Ý tưởng:** Dùng cú pháp `tên: kiểu = giá_trị` cho từng biến; `print()` nhận nhiều đối số, tự động nối bằng dấu cách.

**Thuật toán:**
1. Khai báo `ten`, `tuoi`, `diem_tb`, `da_tot_nghiep` kèm chú thích kiểu.
2. Gọi `print(ten, tuoi, diem_tb, da_tot_nghiep)`.

**Code:**

```python
ten: str = "An"              # biến tên — phải là chuỗi
tuoi: int = 15               # biến tuổi — phải là số nguyên
diem_tb: float = 8.5         # điểm trung bình — phải là số thực
da_tot_nghiep: bool = True   # đã tốt nghiệp hay chưa — đúng/sai

print(ten, tuoi, diem_tb, da_tot_nghiep)
```

**Giải thích code:**
* Ký hiệu `: str`, `: int`, `: float`, `: bool` là **type hint** — ghi chú "biến này nên chứa kiểu gì".
* `print(a, b, c, d)` in liền 4 giá trị, giữa chúng có một khoảng trắng.
* Chú thích chỉ là ghi chú: dù bạn gán `tuoi = "mười lăm"` chương trình vẫn chạy, nhưng IDE sẽ cảnh báo.

**Độ phức tạp:** O(1) — chỉ khai báo và in 4 biến.

---

### Bài 2: Hàm chào có chú thích

**Phân tích:** Viết hàm nhận chuỗi `ten` và trả về câu chào có **tiền tố hậu tố** xung quanh tên.

**Ý tưởng:** Nối chuỗi bằng toán tử `+`; chú thích tham số `ten: str` và giá trị trả về `-> str`.

**Thuật toán:**
1. Định nghĩa hàm `chao(ten: str) -> str`.
2. Trả về `"Xin chao, " + ten + "!"`.
3. Gọi với `"Mai"` và in ra.

**Code:**

```python
def chao(ten: str) -> str:
    """Tạo câu chào lịch sự cho một cái tên."""
    return "Xin chao, " + ten + "!"

print(chao("Mai"))
```

**Giải thích code:**
* `ten: str` — tham số phải là chuỗi.
* `-> str` — hàm cam kết trả về một chuỗi (nối 3 xâu lại với nhau).
* Dấu `+` với chuỗi sẽ **ghép** (concatenate) chứ không cộng số.

**Độ phức tạp:** O(n) với n là độ dài chuỗi (do phép nối chuỗi).

---

### Bài 3: Hàm cộng hai số

**Phân tích:** Hàm nhận 2 số nguyên, trả về tổng — dạng bài đơn giản nhất của type hint.

**Ý tưởng:** Dùng `a + b`; đây là phép cộng số nguyên vì cả hai tham số khai báo `int`.

**Thuật toán:**
1. Định nghĩa `cong(a: int, b: int) -> int`.
2. `return a + b`.
3. Gọi `cong(3, 4)` và in.

**Code:**

```python
def cong(a: int, b: int) -> int:
    """Trả về tổng của hai số nguyên."""
    return a + b

print(cong(3, 4))
```

**Giải thích code:**
* Toàn bộ "hợp đồng" của hàm nằm ở **dòng khai báo**: nhận 2 số nguyên, trả 1 số nguyên — đọc là hiểu ngay.
* Gọi `cong("3", "4")` vẫn chạy nhưng trả `"34"` (nối chuỗi) — type hint không chặn chạy, chỉ để IDE/mypy cảnh báo.

**Độ phức tạp:** O(1).

---

### Bài 4: Hàm gấp đôi chuỗi

**Phân tích:** Dùng toán tử `*` trên chuỗi để lặp lại chuỗi 2 lần (học từ bài 18).

**Ý tưởng:** `chuoi * 2` tạo chuỗi mới = chuỗi gốc viết liền 2 lần.

**Thuật toán:**
1. Định nghĩa `gap_doi(chuoi: str) -> str`.
2. `return chuoi * 2`.
3. Gọi với `"abc"`.

**Code:**

```python
def gap_doi(chuoi: str) -> str:
    """Trả về chuỗi lặp lại hai lần liên tiếp."""
    return chuoi * 2

print(gap_doi("abc"))   # abc + abc = abcabc
```

**Giải thích code:**
* Toán tử `*` với số nguyên n trên chuỗi = lặp lại chuỗi n lần: `"abc" * 2` → `"abcabc"`.
* Kiểu trả về là `str` nên khi gọi hàm này gán cho biến khác, IDE vẫn biết đó là chuỗi.

**Độ phức tạp:** O(n) với n là độ dài chuỗi kết quả.

---

### Bài 5: Danh sách điểm

**Phân tích:** Sử dụng `List[float]` từ module `typing` — kiểu "danh sách chứa số thực". Cần **import trước khi dùng**.

**Ý tưởng:** In từng điểm bằng vòng lặp `for`, tính tổng bằng hàm chuẩn `sum()`.

**Thuật toán:**
1. `from typing import List`.
2. Khai báo `diem: List[float] = [...]`.
3. Vòng lặp in từng điểm; có dòng cuối in tổng.

**Code:**

```python
from typing import List

diem: List[float] = [8.5, 9.0, 7.5]   # danh sách các số thực

for d in diem:
    print(d)

print("Tong:", sum(diem))
```

**Giải thích code:**
* `List[float]` là kiểu tổng quát (generic): không chỉ nói "đây là list" mà còn nói rõ "**list chứa float**".
* `sum(diem)` cộng tất cả phần tử: `8.5 + 9.0 + 7.5 = 25.0`.
* Quên `from typing import List` sẽ báo `NameError: name 'List' is not defined`.

**Độ phức tạp:** O(n) — một vòng lặp duyệt hết danh sách.

---

### Bài 6: Từ điển tên – điểm

**Phân tích:** Dùng `Dict[str, float]`: khóa là tên học sinh (chuỗi), giá trị là điểm (số thực).

**Ý tưởng:** Truy cập điểm của An qua cặp ngoặc vuông `bang_diem["An"]`.

**Thuật toán:**
1. `from typing import Dict`.
2. Khai báo từ điển 2 cặp `"An": 8.5`, `"Binh": 9.0`.
3. In `bang_diem["An"]`.

**Code:**

```python
from typing import Dict

bang_diem: Dict[str, float] = {"An": 8.5, "Binh": 9.0}

print("Diem cua An:", bang_diem["An"])
```

**Giải thích code:**
* `Dict[str, float]` diễn giải: "từ điển ÁNH XẠ tên (str) → điểm (float)".
* `bang_diem["An"]` trả giá trị gắn với khóa `"An"` là `8.5`.
* Nếu khóa không tồn tại, `bang_diem["X"]` báo `KeyError` — bài 8 sẽ xử lý an toàn với `.get()`.

**Độ phức tạp:** O(1) — truy cập từ điển theo khóa.

---

### Bài 7: Tuple thông tin

**Phân tích:** Tuple `("Mai", 16)` bất biến, cố định 2 phần: tên chuỗi, tuổi nguyên. Dùng `Tuple[str, int]`.

**Ý tưởng:** **Giải nén (unpack)** tuple thành 2 biến rồi in theo định dạng.

**Thuật toán:**
1. `from typing import Tuple`.
2. Khai báo `thong_tin: Tuple[str, int] = ("Mai", 16)`.
3. Giải nén `ten, tuoi = thong_tin`.
4. In bằng f-string.

**Code:**

```python
from typing import Tuple

thong_tin: Tuple[str, int] = ("Mai", 16)   # cố định: tên + tuổi

ten, tuoi = thong_tin                      # giải nén tuple
print(f"Ten: {ten} - Tuoi: {tuoi}")
```

**Giải thích code:**
* `Tuple[str, int]` nói rõ **vị trí 0 là str, vị trí 1 là int** — số phần tử và thứ tự là hợp đồng bất thành văn.
* Dòng `ten, tuoi = thong_tin` gán `ten = "Mai"`, `tuoi = 16`.
* f-string `f"...{ten}..."` chèn biến vào chuỗi.

**Độ phức tạp:** O(1).

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Hàm tìm điểm — Optional

**Phân tích:** Đây là bản chất của mọi hàm tìm kiếm: hoặc tìm thấy (có điểm) hoặc không (trả `None`). Kiểu phù hợp: `Optional[float]` = `float` **hoặc** `None`.

**Ý tưởng:** Dùng `.get(ten)` của từ điển — nó trả về giá trị nếu có khóa, ngược lại trả `None` mà không gây lỗi.

**Thuật toán:**
1. Định nghĩa hàm nhận tên và từ điển `Dict[str, float]`.
2. `return bang_diem.get(ten)`.
3. Gọi với tên có (`"An"`) và tên không có (`"X"`).

**Code:**

```python
from typing import Dict, Optional

def tim_diem(ten: str, bang_diem: Dict[str, float]) -> Optional[float]:
    """Trả về điểm của tên; None nếu không có trong bảng."""
    return bang_diem.get(ten)

bang = {"An": 8.5, "Binh": 9.0}

print("Diem An:", tim_diem("An", bang))
print("Diem X:", tim_diem("X", bang))
```

**Giải thích code:**
* `-> Optional[float]` truyền tải ý định: "**có thể không tìm thấy**" — người gọi biết phải xử lý trường hợp `None`.
* `bang_diem.get(ten)` an toàn hơn `bang_diem[ten]` (vốn báo `KeyError` khi thiếu khóa).
* Kết quả: `Diem An: 8.5` và `Diem X: None`.

**Độ phức tạp:** O(1) cho truy cập từ điển.

---

### Bài 9: Union hai kiểu số

**Phân tích:** Hàm vẫn dùng được cho cả số nguyên lẫn số thực — `Union[int, float]` nói rõ điều đó; Python 3.10+ có thể viết `int | float`.

**Ý tưởng:** Chỉ cần `so * 2` — Python tự giữ kiểu: int × 2 = int, float × 2 = float.

**Thuật toán:**
1. Import `Union`.
2. Định nghĩa hàm với tham số `Union[int, float]`.
3. Gọi với `5` và `2.5`.

**Code:**

```python
from typing import Union

def nhan_doi(so: Union[int, float]) -> Union[int, float]:
    """Trả về hai lần giá trị nhận vào."""
    return so * 2

print(nhan_doi(5))     # 5 * 2 = 10  (số nguyên)
print(nhan_doi(2.5))   # 2.5 * 2 = 5.0  (số thực)
```

**Giải thích code:**
* `Union[int, float]` = "chấp nhận một trong hai kiểu".
* Lưu ý `Union` **không** bao gồm `None`; muốn thêm `None` phải dùng `Optional` hoặc `Union[int, float, None]`.
* Kết quả in ra `10` và `5.0` — dấu `.0` cho thấy kiểu được giữ nguyên.

**Độ phức tạp:** O(1).

---

### Bài 10: Any — nhận bất kỳ

**Phân tích:** Khi một hàm thật sự xử lý mọi kiểu dữ liệu (in ra màn hình), ta dùng `Any` — "không hứa gì về kiểu". Kết hợp `-> None` vì hàm chỉ in, không trả về giá trị.

**Ý tưởng:** `type(x)` trả về đối tượng kiểu; nối chuỗi với f-string để in ra loại và giá trị.

**Thuật toán:**
1. Import `Any`.
2. Định nghĩa `in_du_lieu(du_lieu: Any) -> None`.
3. In `type(du_lieu)` và `du_lieu`.
4. Gọi với số, chuỗi và list.

**Code:**

```python
from typing import Any

def in_du_lieu(du_lieu: Any) -> None:
    """In ra loại dữ liệu và giá trị nhận được."""
    print(f"Loai: {type(du_lieu)} - Gia tri: {du_lieu}")

in_du_lieu(10)
in_du_lieu("chao")
in_du_lieu([1, 2])
```

**Giải thích code:**
* `Any` phá vỡ kiểm tra kiểu — chỉ dùng khi thật sự cần (ví dụ in log).
* `type(du_lieu)` in ra `<class 'int'>`, `<class 'str'>`, `<class 'list'>`.
* `-> None` là cách khai báo chuẩn cho hàm **chỉ thực hiện hành động, không trả về** (như `print`).

**Độ phức tạp:** O(1).

---

### Bài 11: Type alias đầu tiên

**Phân tích:** Kiểu `List[float]` xuất hiện nhiều lần trong chương trình → đặt **bí danh** `Diem` để code ngắn và thống nhất.

**Ý tưởng:** Gán `Diem = List[float]` ngay đầu file; dùng `Diem` trong mọi chú thích.

**Thuật toán:**
1. Import `List`.
2. Tạo alias `Diem = List[float]`.
3. Định nghĩa hàm `tong_diem(diem: Diem) -> float`.
4. Gọi với `[1.5, 2.5, 3.0]`.

**Code:**

```python
from typing import List

# Alias: "Diem" là rút gọn của "danh sách các số thực"
Diem = List[float]

def tong_diem(diem: Diem) -> float:
    """Trả về tổng các điểm trong danh sách."""
    return sum(diem)

print("Tong:", tong_diem([1.5, 2.5, 3.0]))
```

**Giải thích code:**
* Alias thường **viết hoa chữ cái đầu** để phân biệt với biến thường.
* Lợi ích lớn nhất: đổi định nghĩa **một chỗ** là tự động áp dụng cho mọi hàm — ví dụ đổi thành `Tuple[float, ...]` mà không cần sửa từng hàm.
* Tổng `1.5 + 2.5 + 3.0 = 7.0`.

**Độ phức tạp:** O(n) với n là số phần tử.

---

### Bài 12: Hàm trả về danh sách

**Phân tích:** Hàm không chỉ nhận kiểu phức tạp mà còn **trả về** kiểu phức tạp — ở đây là `List[int]`.

**Ý tưởng:** `range(1, n + 1)` sinh dãy số từ 1 đến n, `list(...)` biến thành danh sách.

**Thuật toán:**
1. Import `List`.
2. Định nghĩa `tao_danh_sach_so(n: int) -> List[int]`.
3. `return list(range(1, n + 1))`.
4. Gọi với `n = 5`.

**Code:**

```python
from typing import List

def tao_danh_sach_so(n: int) -> List[int]:
    """Trả về danh sách các số nguyên từ 1 đến n."""
    return list(range(1, n + 1))

print(tao_danh_sach_so(5))
```

**Giải thích code:**
* `range(1, 5 + 1)` = `range(1, 6)` sinh `1, 2, 3, 4, 5` — cần `+1` vì `range` dừng **trước** giá trị cuối.
* `-> List[int]` cho phép IDE gợi ý ngay các phương thức của list khi nhận kết quả hàm này.

**Độ phức tạp:** O(n).

---

### Bài 13: Dict chứa List

**Phân tích:** Kiểu **lồng nhau** `Dict[str, List[float]]`: khóa là tên học sinh, giá trị là một danh sách điểm. Bài này luyện kiểu lồng và vòng lặp trên items.

**Ý tưởng:** Vòng lặp `for ten, diem in lop.items()` lấy đồng thời khóa và giá trị; in bằng f-string.

**Thuật toán:**
1. Import `Dict`, `List`.
2. Định nghĩa `in_lop`.
3. Khai báo từ điển 2 học sinh.
4. Gọi và in.

**Code:**

```python
from typing import Dict, List

def in_lop(lop: Dict[str, List[float]]) -> None:
    """In tên từng học sinh kèm danh sách điểm của họ."""
    for ten, diem in lop.items():
        print(f"{ten}: {diem}")

lop: Dict[str, List[float]] = {
    "An":   [8.5, 9.0, 7.0],
    "Binh": [9.0, 8.0, 9.5],
}

in_lop(lop)
```

**Giải thích code:**
* `Dict[str, List[float]]` đọc từ ngoài vào: "một từ điển mà giá trị của mỗi khóa là một **danh sách** số thực".
* `.items()` trả từng cặp (khóa, giá trị); vòng lặp giải nén trực tiếp thành `ten, diem`.
* Kết quả in ra đúng 2 dòng như đề bài.

**Độ phức tạp:** O(n × m) với n học sinh, m điểm mỗi em.

---

### Bài 14: Hàm kiểm tra chuỗi

**Phân tích:** Hàm trả về `bool`. Điều kiện gồm 2 vế: độ dài ≥ 3 **và** không chứa chữ số nào.

**Ý tưởng:** `len(ten) >= 3` kiểm tra độ dài; `any(c.isdigit() for c in ten)` trả `True` nếu **có ít nhất một** ký tự là số → phủ định bằng `not` để "không chứa số".

**Thuật toán:**
1. Định nghĩa hàm với `ten: str -> bool`.
2. Trả về biểu thức logic kết hợp `and`.
3. Gọi với `"An"`, `"Mai"`, `"A1"`.

**Code:**

```python
def kiem_tra_ten(ten: str) -> bool:
    """Trả True nếu tên dài ít nhất 3 ký tự và không chứa chữ số."""
    du_dai = len(ten) >= 3
    khong_so = not any(c.isdigit() for c in ten)
    return du_dai and khong_so

print("An:", kiem_tra_ten("An"))
print("Mai:", kiem_tra_ten("Mai"))
print("A1:", kiem_tra_ten("A1"))
```

**Giải thích code:**
* Tách từng điều kiện ra biến giúp code tự chú thích được mình.
* `"An"` đủ điều kiện? `len = 2` → không đạt → `False`.
* `"A1"` dài 2, lại chứa `"1"` → `False`.
* Chỉ `"Mai"` thỏa mãn cả hai → `True`.

**Độ phức tạp:** O(n) với n là độ dài chuỗi (duyệt các ký tự).

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Optional với giá trị mặc định

**Phân tích:** Khóa từ điển giờ là **số nguyên** (`ma` sinh viên), giá trị là tên chuỗi: `Dict[int, str]`. Bài luyện xử lý rẽ nhánh trước khi trả `Optional`.

**Ý tưởng:** Kiểm tra `if ma in danh_sach:` — tồn tại thì trả tên, ngược lại trả `None`; bên ngoài xử lý khi nhận được `None`.

**Thuật toán:**
1. Định nghĩa hàm với tham số `Dict[int, str]`, trả `Optional[str]`.
2. Rẽ nhánh theo sự tồn tại của khóa.
3. Gọi với mã `1` (có) và mã `99` (không); in thông báo khi `None`.

**Code:**

```python
from typing import Dict, Optional

def tim_sinh_vien(ma: int, danh_sach: Dict[int, str]) -> Optional[str]:
    """Trả tên sinh viên theo mã; None nếu không có mã đó."""
    if ma in danh_sach:
        return danh_sach[ma]
    return None

ds = {1: "An", 2: "Mai"}

print("Ma 1:", tim_sinh_vien(1, ds))

ket_qua = tim_sinh_vien(99, ds)
if ket_qua is None:
    print("Khong tim thay sinh vien ma 99.")
```

**Giải thích code:**
* `if ma in danh_sach:` kiểm tra khóa tồn tại mà không gây `KeyError`.
* Người gọi **bắt buộc** xử lý `None` vì chữ ký hàm đã hứa "có thể không tìm thấy".
* Nếu không kiểm tra `if`, code vẫn chạy nhưng in ra `None` một cách vô nghĩa.

**Độ phức tạp:** O(1) — kiểm tra sự tồn tại trong từ điển.

---

### Bài 16: Alias tuple hồ sơ

**Phân tích:** Tạo alias mô tả một **bản ghi bất biến**: tên + năm sinh + điểm. `HoSo = Tuple[str, int, float]`.

**Ý tưởng:** Giải nén tuple ra 3 biến rồi in theo định dạng chuẩn.

**Thuật toán:**
1. Import `Tuple`.
2. Tạo alias `HoSo`.
3. Định nghĩa hàm `hien_ho_so(ho_so: HoSo) -> None`.
4. Gọi với `("Mai", 2008, 8.75)`.

**Code:**

```python
from typing import Tuple

# Alias: một hồ sơ gồm (tên, năm sinh, điểm trung bình)
HoSo = Tuple[str, int, float]

def hien_ho_so(ho_so: HoSo) -> None:
    """In hồ sơ theo định dạng Ten - NamSinh - Diem."""
    ten, nam, diem = ho_so          # giải nén 3 phần tử
    print(f"{ten} - {nam} - {diem}")

hien_ho_so(("Mai", 2008, 8.75))
```

**Giải thích code:**
* Alias đóng vai trò "khuôn mẫu" — bất kỳ ai đọc `def f(ho_so: HoSo)` đều biết `ho_so` có 3 phần theo đúng thứ tự.
* Giải nén thẳng trong hàm làm code ngắn; vị trí khớp đúng với khai báo tuple.
* Kết quả: `Mai - 2008 - 8.75`.

**Độ phức tạp:** O(1).

---

### Bài 17: Thống kê lớp với Dict

**Phân tích:** Chuyển đổi kiểu dữ liệu: từ `Dict[str, List[float]]` (tên → các điểm) sang `Dict[str, float]` (tên → điểm trung bình). Đây chính là bài toán "biến đổi dữ liệu" quen thuộc trong báo cáo.

**Ý tưởng:** Duyệt từng học sinh, tính tổng/chia số lượng rồi làm tròn 2 chữ số bằng `round(x, 2)`; ghi vào từ điển kết quả.

**Thuật toán:**
1. Định nghĩa hàm với 2 kiểu `Dict[...]` ở đầu vào và trả về.
2. Khởi tạo từ điển kết quả rỗng.
3. Vòng lặp `items()`, tính trung bình, lưu vào kết quả.
4. Gọi với lớp 2 học sinh.

**Code:**

```python
from typing import Dict, List

def thong_ke(bang_diem: Dict[str, List[float]]) -> Dict[str, float]:
    """Trả về từ điển ten -> diem trung binh (làm tròn 2 chữ số)."""
    ket_qua: Dict[str, float] = {}
    for ten, diem in bang_diem.items():
        ket_qua[ten] = round(sum(diem) / len(diem), 2)
    return ket_qua

lop = {
    "An":   [8.5, 9.0, 7.0],
    "Binh": [9.0, 8.0, 9.5],
}

print(thong_ke(lop))
```

**Giải thích code:**
* `An`: `(8.5 + 9.0 + 7.0) / 3 = 8.166...` → `round(..., 2) = 8.17`.
* `Binh`: `26.5 / 3 = 8.833...` → `8.83`.
* `ket_qua: Dict[str, float]` chú thích biến cục bộ — đây là thói quen tốt cho biến chứa dữ liệu tổng hợp.

**Độ phức tạp:** O(n × m) với n học sinh, m điểm mỗi em.

---

### Bài 18: Danh sách Optional

**Phân tích:** Dữ liệu thực tế có "ô trống": học sinh bỏ thi nên điểm là `None`. Kiểu `List[Optional[float]]` phản ánh đúng thực tế. Cần tách hai nhóm và tính trung bình chỉ trên nhóm có điểm.

**Ý tưởng:** Dùng list comprehension lọc `None`: `[d for d in diem_thi if d is not None]`. Số người bỏ thi = tổng − số người thi.

**Thuật toán:**
1. Khai báo `diem_thi: List[Optional[float]]`.
2. Lọc danh sách người thi (bỏ `None`).
3. Tính số thi, số bỏ thi.
4. Tính và in trung bình.

**Code:**

```python
from typing import List, Optional

diem_thi: List[Optional[float]] = [8.5, None, 7.0, None]

# Lọc ra những người thật sự đi thi (giá trị khác None)
diem_hop_le = [d for d in diem_thi if d is not None]

so_thi = len(diem_hop_le)
so_bo_thi = len(diem_thi) - so_thi

trung_binh = round(sum(diem_hop_le) / so_thi, 2)

print("So nguoi thi:", so_thi)
print("So nguoi bo thi:", so_bo_thi)
print("Diem trung binh:", trung_binh)
```

**Giải thích code:**
* `d is not None` nhận diện người đi thi; so sánh với `None` phải dùng `is` (không phải `==`).
* `sum(diem_hop_le) / so_thi = (8.5 + 7.0) / 2 = 7.75`.
* Nếu dùng lọc trực tiếp trên `diem_thi` (không tách), `sum()` sẽ báo `TypeError` vì không cộng được `None`.

**Độ phức tạp:** O(n).

---

### Bài 19: Tìm sinh viên với Optional

**Phân tích:** Danh sách gồm các tuple `(ma, ten)`: `List[Tuple[int, str]]`. Cần trả về **mã** của sinh viên **đầu tiên** khớp tên — hoặc `None`.

**Ý tưởng:** Vòng lặp `for ma, ten_sv in danh_sach:` và **return ngay** khi tên khớp — kiểu vòng lặp "tìm và dừng".

**Thuật toán:**
1. Định nghĩa hàm với `List[Tuple[int, str]]`, trả `Optional[int]`.
2. Duyệt từng cặp; khi `ten_sv == ten` thì `return ma`.
3. Hết vòng lặp không tìm thấy → `return None`.
4. Gọi với tên có và tên không có.

**Code:**

```python
from typing import List, Optional, Tuple

def tim_sv_theo_ten(ten: str, danh_sach: List[Tuple[int, str]]) -> Optional[int]:
    """Trả về mã sinh viên đầu tiên khớp tên; None nếu không có."""
    for ma, ten_sv in danh_sach:
        if ten_sv == ten:
            return ma          # dừng ngay khi tìm thấy
    return None

ds = [(1, "An"), (2, "Mai"), (3, "An")]

print("Ma cua Mai:", tim_sv_theo_ten("Mai", ds))

ket_qua = tim_sv_theo_ten("X", ds)
if ket_qua is None:
    print("Khong tim thay X.")
```

**Giải thích code:**
* Vòng lặp **dừng sớm** (early return) — hiệu quả nhất khi phần tử cần tìm nằm gần đầu.
* Với tên trùng lặp (`"An"` xuất hiện 2 lần) chỉ trả mã **đầu tiên** = `1`.
* Kiểu trả về là mã số nguyên → `Optional[int]`, không phải `Optional[str]`.

**Độ phức tạp:** O(n) — trung bình O(n/2) nhờ dừng sớm.

---

### Bài 20: Chương trình tiện ích đầy đủ type hints

**Phân tích:** Tổng hợp toàn bộ bài: alias kiểu bản ghi `SanPham`, hàm thao tác danh sách, hàm tìm kiếm trả `Optional`, hàm tổng hợp. Đây là "hình mẫu" thu nhỏ của các chương trình quản lý sau này.

**Ý tưởng:** Mỗi sản phẩm là một tuple `(mã, tên, giá)`. Ba hàm độc lập: thêm (append), tìm (vòng lặp + return None), tổng (generator expression).

**Thuật toán:**
1. Tạo alias `SanPham = Tuple[int, str, float]`.
2. `them_san_pham`: `append((ma, ten, gia))` — trả `None`.
3. `tim_san_pham`: vòng lặp so sánh `sp[1] == ten`, nếu thấy trả cả tuple, không thấy trả `None`.
4. `tong_gia_tri`: `sum(sp[2] for sp in danh_sach)`.
5. Khởi tạo 2 sản phẩm, thêm 1, tìm 1, in tổng.

**Code:**

```python
from typing import List, Optional, Tuple

# Mỗi sản phẩm: (mã, tên, giá)
SanPham = Tuple[int, str, float]


def them_san_pham(danh_sach: List[SanPham], ma: int, ten: str, gia: float) -> None:
    """Thêm một sản phẩm mới vào cuối danh sách."""
    danh_sach.append((ma, ten, gia))


def tim_san_pham(danh_sach: List[SanPham], ten: str) -> Optional[SanPham]:
    """Trả về sản phẩm đầu tiên khớp tên; None nếu không có."""
    for sp in danh_sach:
        if sp[1] == ten:
            return sp
    return None


def tong_gia_tri(danh_sach: List[SanPham]) -> float:
    """Trả về tổng giá trị toàn bộ sản phẩm trong kho."""
    return sum(sp[2] for sp in danh_sach)


# --- Chương trình chính ---
kho: List[SanPham] = []
them_san_pham(kho, 1, "Ban phim", 350.0)
them_san_pham(kho, 2, "Chuot", 150.0)
them_san_pham(kho, 3, "Tai nghe", 200.0)

print("Tim thay:", tim_san_pham(kho, "Chuot"))
print("Tong gia tri:", tong_gia_tri(kho))
```

**Giải thích code:**
* `sp[1] == ten` so sánh vị trí tên trong tuple; vì tuple đã có alias nên theo thứ tự (mã, tên, giá).
* `sum(sp[2] for sp in danh_sach)` dùng generator — khai báo kiểu trả về `float` khớp với tổng của `350.0 + 150.0 + 200.0`.
* `tim_san_pham` trả `Optional[SanPham]` — đúng quy ước mọi hàm tìm kiếm.
* Kết quả: `Tim thay: (2, 'Chuot', 150.0)` và `Tong gia tri: 700.0`.

**Độ phức tạp:** thêm O(1); tìm O(n); tổng O(n).

---

## 🎯 Lời kết

Bạn đã hoàn thành **20 bài tập Type Hints** — từ khai báo biến đến viết cả một chương trình quản lý sản phẩm có chú thích đầy đủ. Từ bây giờ, hãy **tạo thói quen viết type hints cho mọi hàm**, nó sẽ giúp bạn đọc lại code của chính mình dễ dàng và khiến chương trình lớn ít lỗi hơn hẳn.

👉 Tiếp theo: **[Bài 39: Asyncio – Lập Trình Bất Đồng Bộ](../39_Asyncio/bai_giang.md)**