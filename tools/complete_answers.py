# -*- coding: utf-8 -*-
"""Bổ sung đáp án thiếu cho 3 bài mà file dap_an.md gốc không đầy đủ:
- Bài 20 (Module): thiếu đáp án 15-20
- Bài 27 (Generator): thiếu đáp án 8-20
- Bài 40 (Mini Project): thiếu đáp án 15-20
Nội dung viết theo đúng format đáp án sẵn có của khóa học.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


# ---------- Bài 20: đáp án 15-20 ----------

B20 = r'''
<details>
<summary>✅ Bài 15: Bộ tiện ích hình học hoàn chỉnh</summary>

**Phân tích:** Cần tách rõ "định nghĩa" (trong module `hinh_hoc.py`) và "dùng thử"
(trong `main.py`); chỉ import 2 hàm hình tròn và 2 hàm hình chữ nhật — đúng luật
"dùng gì, nhập nấy".

**Ý tưởng:** Module chứa công thức thuần túy (không `input`/`print` bên trong);
`main.py` quyết định dữ liệu mẫu và cách in đẹp mắt.

**Thuật toán:**
1. Module: 4 hàm nhận số, trả số (`math.pi` cho hình tròn).
2. `main.py`: import 4 hàm (riêng biệt, không import *).
3. Gọi với dữ liệu mẫu, in kết quả làm tròn 2 chữ số.

**Code:**

```python
# hinh_hoc.py
import math


def dien_tich_hinh_tron(r):
    return math.pi * r * r


def chu_vi_hinh_tron(r):
    return 2 * math.pi * r


def dien_tich_tam_giac(a, h):
    return a * h / 2


def dien_tich_chu_nhat(a, b):
    return a * b
```

```python
# main.py
from hinh_hoc import (dien_tich_hinh_tron, chu_vi_hinh_tron,
                      dien_tich_chu_nhat)

dien_tich = round(dien_tich_hinh_tron(5), 2)
chu_vi = round(chu_vi_hinh_tron(5), 2)
print("Hinh tron r=5: Dien tich", dien_tich, end=", ")
print("Chu vi", chu_vi)
print("Hinh chu nhat 4x6: Dien tich", dien_tich_chu_nhat(4, 6))
```

**Giải thích code:**
* `math.pi` — hằng số π chuẩn xác từ thư viện, không cần ghi 3.14 thủ công.
* `dien_tich_tam_giac` nằm trong module nhưng `main.py` không import —
  đó là ý nghĩa của import chọn lọc: dùng gì, lấy đúng cái đó.
* `round(x, 2)` để in 78.54 và 31.42 — khớp output yêu cầu.

**Độ phức tạp:** O(1) — toàn phép tính số học, không vòng lặp.

</details>

<details>
<summary>✅ Bài 16: Đoán số nhiều lượt</summary>

**Phân tích:** Ba yêu cầu cùng lúc: lặp nhiều lượt (`while`), xử lý nhập sai
(`try/except ValueError`), số ngẫu nhiên (`random.randint`). Lượt nhập sai
không được tính — phải `continue` kịp thời.

**Ý tưởng:** Vòng lặp vô hạn + `break` khi đoán đúng; `try/except` bao quanh
chỗ chuyển `int()`; chỉ tăng đếm `luot` sau khi có số hợp lệ.

**Thuật toán:**
1. `so_bi_mat = random.randint(1, 100)`, `luot = 0`.
2. Lặp: đọc `input`, `try: doan = int(...)` — lỗi thì in cảnh báo, `continue`.
3. So sánh: nhỏ hơn → "Lon hon", lớn hơn → "Be hon", bằng → in kết quả + `break`.

**Code:**

```python
import random

so_bi_mat = random.randint(1, 100)
luot = 0

while True:
    try:
        doan = int(input("Doan so 1-100: "))
    except ValueError:
        print("Vui long nhap so nguyen!")
        continue
    luot += 1
    if doan < so_bi_mat:
        print("Lon hon")
    elif doan > so_bi_mat:
        print("Be hon")
    else:
        print(f"Dung roi! So bi mat la {so_bi_mat}. Ban doan {luot} luot.")
        break
```

**Giải thích code:**
* `continue` trong `except` — bỏ qua phần còn lại của vòng lặp, không cộng `luot`.
  Với input mẫu (`50, abc, 75, 62` khi số bí mật là 62): lần 1 "Be hon",
  `abc` → cảnh báo (không tính lượt), 75 → "Lon hon", 62 → đúng với 3 lượt. ✔
* `while True + break` dùng khi chưa biết trước số vòng lặp — đúng hoàn cảnh
  trò chơi "đoán đến khi đúng".

**Độ phức tạp:** O(k) với k = số lượt đoán hợp lệ; bộ nhớ O(1).

</details>

<details>
<summary>✅ Bài 17: Sinh mật khẩu ngẫu nhiên</summary>

**Phân tích:** Mật khẩu = chuỗi 6 ký tự, mỗi ký tự bốc ngẫu nhiên từ bảng
chữ cái gồm chữ thường + chữ hoa + chữ số (62 ký tự). `random.choice` là công
cụ đúng — nó chọn 1 phần tử từ dãy, cần thì gọi lại nhiều lần.

**Ý tưởng:** Cộng chuỗi rỗng với từng ký tự bốc được trong vòng lặp 6 lần;
có thể viết gọn bằng `join` sau khi hiểu kỹ.

**Thuật toán:**
1. Gộp 3 nhóm ký tự thành chuỗi `ky_tu`.
2. `mat_khau = ""`, lặp 6 lần: `mat_khau += random.choice(ky_tu)`.
3. In ra.

**Code:**

```python
# Cách 1 — vòng lặp, rõ ý nhất
import random

ky_tu = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
mat_khau = ""
for i in range(6):
    mat_khau += random.choice(ky_tu)
print(mat_khau)
```

```python
# Cách 2 — join + generator expression (khi đã thành thạo)
mat_khau = "".join(random.choice(ky_tu) for i in range(6))
print(mat_khau)
```

**Giải thích code:**
* `random.choice(ky_tu)` — bốc 1 ký tự bất kỳ trong 62 ký tự, mỗi lần độc lập
  nên ký tự có thể lặp (đúng như mật khẩu thật).
* Cách 2 dùng `"".join(...)` nối 6 ký tự thành chuỗi — ngắn gọn, hiệu năng tốt
  hơn cộng chuỗi nhiều lần (với 6 ký tự thì khác biệt không đáng kể).

**Độ phức tạp:** O(6) ≈ O(1); bộ nhớ O(1).

</details>

<details>
<summary>✅ Bài 18: Module thống kê</summary>

**Phân tích:** Module gồm 4 hàm thuần túy; `main.py` import cả 4 hàm và dùng
cho danh sách điểm cụ thể. Gợi ý yêu cầu viết thủ công bằng vòng lặp (không
dùng `sum`/`max`/`min`) — luyện tay và hiểu sâu.

**Ý tưởng:** `tong` là nền cho `trung_binh`; tìm lớn/nhỏ nhất bằng kỹ thuật
"gán ứng viên đầu tiên, duyệt so sánh và thay thế".

**Thuật toán:**
1. `tong(ds)`: cộng dồn từ 0.
2. `trung_binh(ds)`: `tong(ds) / len(ds)`.
3. `lon_nhat(ds)` / `nho_nhat(ds)`: ứng viên = `ds[0]`, duyệt so sánh.
4. `main.py`: import 4 hàm, gọi cho `[7, 8.5, 6, 9, 7.5]`, làm tròn 2 chữ số.

**Code:**

```python
# thong_ke.py
def tong(ds):
    kq = 0
    for x in ds:
        kq += x
    return kq


def trung_binh(ds):
    return tong(ds) / len(ds)


def lon_nhat(ds):
    kq = ds[0]
    for x in ds:
        if x > kq:
            kq = x
    return kq


def nho_nhat(ds):
    kq = ds[0]
    for x in ds:
        if x < kq:
            kq = x
    return kq
```

```python
# main.py
from thong_ke import tong, trung_binh, lon_nhat, nho_nhat

diem = [7, 8.5, 6, 9, 7.5]
print("Tong:", tong(diem))
print("Trung binh:", round(trung_binh(diem), 2))
print("Lon nhat:", lon_nhat(diem))
print("Nho nhat:", nho_nhat(diem))
```

**Giải thích code:**
* Tái sử dụng `tong()` bên trong `trung_binh()` — đúng tinh thần module:
  viết một lần, dùng nhiều chỗ.
* Tổng = 7 + 8.5 + 6 + 9 + 7.5 = 38.0; trung bình = 38.0 / 5 = 7.6. ✔

**Độ phức tạp:** O(n) thời gian, O(1) bộ nhớ phụ.

</details>

<details>
<summary>✅ Bài 19: Module hai vai — chạy thử và bị import</summary>

**Phân tích:** Điểm mấu chốt là `if __name__ == "__main__"` — khối kiểm thử chỉ
chạy khi thực thi trực tiếp file `thoi_tiet.py`, không chạy khi `main.py`
import nó. Đây là mẫu "module hai vai" chuẩn trong mọi dự án Python.

**Ý tưởng:** Hàm `mo_ta(t)` dùng rẽ nhánh ngưỡng; khối test in 3 giá trị;
`main.py` đọc nhiệt độ từ người dùng và gọi hàm.

**Thuật toán:**
1. `mo_ta(t)`: `t >= 30` → "Nong"; `t >= 20` → "Mat"; còn lại → "Lanh".
2. Khối `if __name__ == "__main__"` in test 35, 25, 10.
3. `main.py`: import hàm, `input` nhiệt độ (đổi sang `int`), in mô tả.

**Code:**

```python
# thoi_tiet.py
def mo_ta(t):
    if t >= 30:
        return "Nong"
    elif t >= 20:
        return "Mat"
    return "Lanh"


if __name__ == "__main__":
    print("Test 35 ->", mo_ta(35))
    print("Test 25 ->", mo_ta(25))
    print("Test 10 ->", mo_ta(10))
```

```python
# main.py
from thoi_tiet import mo_ta

t = int(input("Nhiet do hom nay: "))
print("Thoi tiet hom nay:", mo_ta(t))
```

**Giải thích code:**
* Chạy `python thoi_tiet.py` → `__name__` là `"__main__"` → khối test chạy,
  in đúng 3 dòng yêu cầu.
* Chạy `python main.py` → module được import, `__name__` là `"thoi_tiet"` →
  khối test **không** chạy; người dùng nhập 32 → "Thoi tiet hom nay: Nong". ✔
* Lỗi thường gặp: quên khối `if __name__...` thì khi `main.py` import, 3 dòng
  test bị in ra — "rác" trong chương trình chính.

**Độ phức tạp:** O(1).

</details>

<details>
<summary>✅ Bài 20: Trò chơi Oẳn tù tì</summary>

**Phân tích:** Máy chọn ngẫu nhiên 1 trong 3; người chơi nhập 1 trong 3; phán
thắng/thua/hòa theo vòng tròn Búa → Kéo → Bao → Búa. Viết cả đống `if/elif`
dễ sai; dùng từ điển `thang` ánh xạ "X thắng Y" là cách gọn và ít lỗi nhất.

**Ý tưởng:** `thang = {"bua": "keo", "keo": "bao", "bao": "bua"}` — chữ đọc
là "bua thắng keo"... Nếu hai bên bằng nhau → hòa; nếu `thang[ban] == may`
→ người thắng; còn lại → máy thắng.

**Thuật toán:**
1. `may = random.choice(["bua", "keo", "bao"])`.
2. `ban = input(...)`, in lựa chọn của máy.
3. Hòa → bằng nhau; thắng → tra từ điển; ngược lại thua.

**Code:**

```python
import random

thang = {
    "bua": "keo",   # Búa thắng Kéo
    "keo": "bao",   # Kéo thắng Bao
    "bao": "bua",   # Bao thắng Búa
}

may = random.choice(["bua", "keo", "bao"])
ban = input("Ban chon (bua/keo/bao): ")
print("May chon:", may)

if ban == may:
    print("Hoa!")
elif thang[ban] == may:
    print("Ban thang!")
else:
    print("May thang!")
```

**Giải thích code:**
* Ví dụ: bạn chọn `bua`, máy `keo` → `thang["bua"]` là `"keo"` bằng `may` →
  "Ban thang!". ✔
* Nếu bạn nhập chữ không có trong từ điển (ví dụ `da`) → `KeyError`. Muốn
  chương trình chắc chắn, thêm vòng kiểm tra `while ban not in thang` —
  kỹ thuật học ở bài `while` và `Exception`.

**Độ phức tạp:** O(1).

</details>
'''.strip()


# ---------- Bài 27: đáp án 8-14 (trung bình) ----------

B27_MEDIUM = r'''
<details>
<summary>✅ Bài 8: Generator Fibonacci 10 số</summary>

**Phân tích:** Dãy Fibonacci: số sau = tổng hai số trước (bắt đầu 0, 1).
Cần "sinh n số đầu" — không lưu list, chỉ `yield` từng số.

**Ý tưởng:** Giữ cặp `(a, b)`; mỗi vòng lặp `yield a` rồi trượt cặp
`a, b = b, a + b` — mẫu "trượt cửa sổ 2 số" rất hay gặp khi làm việc với dãy số.

**Thuật toán:**
1. `a, b = 0, 1`.
2. Lặp n lần: `yield a`; cập nhật `a, b = b, a + b`.
3. In bằng vòng lặp, cách nhau bằng dấu cách.

**Code:**

```python
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


for so in fibonacci(10):
    print(so, end=" ")
```

**Giải thích code:**
* `fibonacci(10)` sinh đúng 10 số: 0 1 1 2 3 5 8 13 21 34. ✔
* Nếu viết `return a` thay vì `yield a` thì hàm chỉ trả đúng 1 số đầu rồi dừng —
  đó là sự khác biệt cốt lõi giữa hàm thường và generator.

**Độ phức tạp:** O(n) thời gian, O(1) bộ nhớ (không lưu dãy).

</details>

<details>
<summary>✅ Bài 9: Generator số chẵn đến n</summary>

**Phân tích:** Sinh các số chẵn từ 0 đến n (bao gồm n nếu n chẵn), rồi tính
tổng bằng `sum()` — kết hợp generator với hàm tổng hợp sẵn có.

**Ý tưởng:** Duyệt `range(0, n + 1)`, `yield x` khi `x % 2 == 0`;
`sum()` tự "kéo" generator đến hết — không cần list trung gian.

**Thuật toán:**
1. `so_chan(n)`: lặp 0..n, yield số chẵn.
2. `print(sum(so_chan(20)))`.

**Code:**

```python
def so_chan(n):
    for x in range(0, n + 1):
        if x % 2 == 0:
            yield x


print(sum(so_chan(20)))
```

**Giải thích code:**
* 0 + 2 + 4 + ... + 20 = 110. ✔
* `range(0, n + 1)` chứ không phải `range(n)` — vì phải **bao gồm** n;
  lỗi "thiếu số cuối" khi quên `+ 1` là lỗi rất phổ biến.
* So sánh với list comprehension `[x for x in range(21) if x % 2 == 0]`:
  cho cùng kết quả nhưng tốn bộ nhớ lưu cả dãy.

**Độ phức tạp:** O(n) thời gian, O(1) bộ nhớ phụ.

</details>

<details>
<summary>✅ Bài 10: Đọc file từng dòng</summary>

**Phân tích:** Hai việc: (1) tạo file `nhat_ky.txt` 3 dòng bằng chế độ `"w"`,
(2) generator `doc_file(ten)` đọc file và trả từng dòng đã `.strip()`.

**Ý tưởng:** `with open(...)` tự đóng file; trong generator, `for dong in f`
duyệt file từng dòng **mà không cần đọc cả file vào RAM** — đây chính là lý do
generator ra đời (xử lý file lớn).

**Thuật toán:**
1. Ghi 3 dòng nội dung vào file (chế độ `"w"`, `encoding="utf-8"`).
2. `doc_file(ten)`: mở file, `yield dong.strip()` cho mỗi dòng.
3. Đánh số thứ tự khi in.

**Code:**

```python
# Bước 1 — tạo file mẫu
with open("nhat_ky.txt", "w", encoding="utf-8") as f:
    f.write("Chao buoi sang\n")
    f.write("Toi dang hoc Python\n")
    f.write("Generator rat hay\n")


# Bước 2 — generator đọc file
def doc_file(ten):
    with open(ten, encoding="utf-8") as f:
        for dong in f:
            yield dong.strip()


# Bước 3 — dùng
i = 1
for dong in doc_file("nhat_ky.txt"):
    print(f"Dong {i}: {dong}")
    i += 1
```

**Giải thích code:**
* `.strip()` bỏ ký tự xuống dòng `\n` ở cuối — không có nó, mỗi dòng in ra sẽ
  cách nhau một dòng trống (vì `print` tự thêm `\n`).
* Chế độ `"w"` ghi đè file nếu đã tồn tại — muốn giữ nội dung cũ thì dùng `"a"`.
* Mẫu này dùng lại nguyên vẹn ở bài 11, 17, 20 — học một lần, dùng nhiều lần.

**Độ phức tạp:** O(số dòng) thời gian, O(1) bộ nhớ (đọc lười từng dòng).

</details>

<details>
<summary>✅ Bài 11: Lọc dòng chứa từ khóa</summary>

**Phân tích:** Đọc file `log.txt` 4 dòng, chỉ giữ dòng bắt đầu bằng `LOI`.
Tái sử dụng đúng mẫu `doc_file` của bài 10 + thêm điều kiện lọc trong generator.

**Ý tưởng:** `str.startswith("LOI")` kiểm tra tiền tố; đặt điều kiện ngay trong
generator để phía dùng không phải lọc lại — generator "vừa đọc vừa lọc".

**Thuật toán:**
1. Tạo file `log.txt` với 2 dòng `LOI` và 2 dòng khác.
2. Generator duyệt từng dòng, `yield` dòng đã strip nếu bắt đầu bằng `LOI`.
3. In kết quả.

**Code:**

```python
# Tạo file mẫu
with open("log.txt", "w", encoding="utf-8") as f:
    f.write("LOI ket noi mang\n")
    f.write("OK chay thanh cong\n")
    f.write("LOI tai lieu khong ton tai\n")
    f.write("OK ket thuc\n")


def loc_loi(ten):
    with open(ten, encoding="utf-8") as f:
        for dong in f:
            if dong.startswith("LOI"):
                yield dong.strip()


for dong in loc_loi("log.txt"):
    print(dong)
```

**Giải thích code:**
* In ra đúng 2 dòng `LOI...`. ✔
* `startswith` phân biệt chữ hoa/thường: dòng `loi ...` (thường) sẽ bị bỏ qua —
  nếu muốn "không phân biệt", cần `dong.upper().startswith("LOI")`.
* Cùng một kỹ thuật áp dụng cho lọc email, lọc số điện thoại, lọc dòng CSV...

**Độ phức tạp:** O(số dòng) thời gian, O(1) bộ nhớ.

</details>

<details>
<summary>✅ Bài 12: Tổng bằng generator expression có điều kiện</summary>

**Phân tích:** Tính 1² + 3² + 5² + 7² + 9² = 165 bằng **một biểu thức duy nhất** —
không vòng lặp, không biến tạm. Dạng `( ... for ... if ... )` gọi là generator
expression có điều kiện.

**Ý tưởng:** `sum(X for x in range(1, 11) if LẺ)` — `sum` kéo từng giá trị,
cộng dồn, không tạo list trung gian.

**Thuật toán:** Một dòng: lọc số lẻ trong 1..10, bình phương, cộng dồn.

**Code:**

```python
tong = sum(x * x for x in range(1, 11) if x % 2 == 1)
print(tong)
```

**Giải thích code:**
* 1 + 9 + 25 + 49 + 81 = 165. ✔
* So sánh 3 cách viết cùng kết quả:
  * List comprehension: `sum([x*x for x in range(1,11) if x%2==1])` — tạo list
    trung gian trong RAM rồi mới cộng.
  * Generator expression (cách trên) — không tạo list, tiết kiệm nhớ.
  * Vòng lặp + biến cộng dồn — dài dòng nhưng dễ đọc nhất cho người mới.

**Độ phức tạp:** O(n) thời gian, O(1) bộ nhớ.

</details>

<details>
<summary>✅ Bài 13: Generator phân tách chữ số</summary>

**Phân tích:** Từ số nguyên 2026 sinh ra các chữ số 2, 0, 2, 6 theo thứ tự từ
trái sang phải. Phép chia lấy dư (`%`, `//`) cho ra chữ số từ **phải sang trái**
(khó hơn); cách đơn giản và trực quan là đổi số thành chuỗi rồi duyệt ký tự.

**Ý tưởng:** `str(so)` biến 2026 thành "2026"; mỗi ký tự là một chữ số —
`yield int(c)` để trả về số nguyên chứ không phải ký tự.

**Thuật toán:**
1. Đổi số thành chuỗi.
2. Duyệt từng ký tự, `yield int(ký tự)`.
3. In cách nhau bằng dấu cách.

**Code:**

```python
def chu_so(so):
    for c in str(so):
        yield int(c)


for c in chu_so(2026):
    print(c, end=" ")
```

**Giải thích code:**
* In ra: 2 0 2 6. ✔
* Số 0 ở giữa được giữ đúng vị trí — cách chia lấy dư cũng làm được nhưng phải
  xử lý khéo léo; cách chuỗi tự nhiên bảo toàn thứ tự và số 0 đứng giữa.
* `str(so)` với số âm (ví dụ -123) sẽ có ký tự `'-'` đầu — `int('-')` báo lỗi;
  muốn chắc chắn, dùng `abs(so)` trước.

**Độ phức tạp:** O(số chữ số) thời gian, O(1) bộ nhớ phụ.

</details>

<details>
<summary>✅ Bài 14: Generator xoay vòng ba môn học</summary>

**Phân tích:** Cần "lặp vô hạn" qua 3 môn theo thứ tự, rồi lấy 7 phần tử đầu.
Hai công cụ: `while True` (vòng lặp vô hạn) và `itertools.islice` (cắt lát một
dãy vô hạn mà không treo máy).

**Ý tưởng:** Generator `lich_hoc()` không bao giờ dừng (`while True` + lặp danh
sách); phía dùng quyết định lấy bao nhiêu bằng `islice` — tách bạch "sinh vô
hạn" và "lấy hữu hạn".

**Thuật toán:**
1. `lich_hoc()`: lặp vô tận, `yield` từng môn theo thứ tự.
2. `from itertools import islice`; `islice(lich_hoc(), 7)` lấy 7 phần tử.
3. In cách nhau bằng dấu cách.

**Code:**

```python
from itertools import islice


def lich_hoc():
    mon_hoc = ["Toan", "Ly", "Hoa"]
    while True:              # lặp vô hạn
        for mon in mon_hoc:
            yield mon


for mon in islice(lich_hoc(), 7):
    print(mon, end=" ")
```

**Giải thích code:**
* In ra: Toan Ly Hoa Toan Ly Hoa Toan. ✔
* `islice` kéo generator đúng 7 lần rồi dừng — generator vẫn "sống" nhưng không
  bị gọi tiếp; không dùng `islice` mà `list(lich_hoc())` sẽ **treo máy** vì cố
  biến dãy vô hạn thành list — lỗi nguy hiểm nhất khi làm việc với generator
  vô hạn.
* Ứng dụng thật: lịch xoay ca, vòng quay nhiệm vụ, sinh ID tuần hoàn...

**Độ phức tạp:** O(k) với k = số phần tử lấy ra; O(1) bộ nhớ.

</details>
'''.strip()


# ---------- Bài 27: đáp án 15-20 (khó) ----------

B27_HARD = r'''
<details>
<summary>✅ Bài 15: Generator số nguyên tố</summary>

**Phân tích:** Sinh các số nguyên tố nhỏ hơn n. Cần hàm phụ `la_nguyen_to(x)`
và generator lọc. Kiểm tra đến `√x` thay vì `x - 1` là tối ưu quan trọng
(n giảm từ O(x) xuống O(√x) mỗi số).

**Ý tưởng:** Duyệt 2..n-1, `yield x` khi `x` nguyên tố; `la_nguyen_to` loại
ngay số < 2 và thử ước từ 2 đến `int(x**0.5)`.

**Thuật toán:**
1. `la_nguyen_to(x)`: < 2 → False; ước nào chia hết → False; còn lại True.
2. `so_nguyen_to(n)`: duyệt 2..n-1, yield số thỏa mãn.
3. In cách nhau bằng dấu cách.

**Code:**

```python
def la_nguyen_to(x):
    if x < 2:
        return False
    for u in range(2, int(x ** 0.5) + 1):
        if x % u == 0:
            return False
    return True


def so_nguyen_to(n):
    for x in range(2, n):
        if la_nguyen_to(x):
            yield x


for so in so_nguyen_to(30):
    print(so, end=" ")
```

**Giải thích code:**
* In ra: 2 3 5 7 11 13 17 19 23 29. ✔
* `int(x ** 0.5) + 1` — cộng 1 để `range` bao gồm chính căn bậc hai
  (ví dụ x = 9, không có +1 sẽ bỏ sót ước 3 — lỗi tinh vi hay gặp!).
* Số 2 là số chẵn nguyên tố duy nhất; hàm xử lý đúng vì vòng `range(2, 2)`
  rỗng → trả True.

**Độ phức tạp:** O(n√n) thời gian, O(1) bộ nhớ phụ.

</details>

<details>
<summary>✅ Bài 16: So sánh bộ nhớ list vs generator</summary>

**Phân tích:** Chứng minh bằng số liệu: list 50.000 số tốn bao nhiêu byte,
generator tương ứng tốn bao nhiêu. `sys.getsizeof` đo kích thước đối tượng.

**Ý tưởng:** Tạo cả hai, in `getsizeof` từng cái; chênh lệch lớn là đáp án
cho câu hỏi "vì sao cần generator".

**Thuật toán:**
1. `import sys`.
2. List comprehension 50.000 số; generator expression tương ứng.
3. In hai con số.

**Code:**

```python
import sys

lst = [x for x in range(50000)]
gen = (x for x in range(50000))

print("Kich thuoc list:", sys.getsizeof(lst), "byte")
print("Kich thuoc generator:", sys.getsizeof(gen), "byte")
```

**Giải thích code:**
* Kết quả mẫu: list ~400.000+ byte, generator chỉ ~100 byte — chênh lệch
  hàng nghìn lần, và khoảng cách càng nới rộng khi dữ liệu càng lớn.
* `getsizeof(lst)` đo cả vùng chứa 50.000 số; `getsizeof(gen)` chỉ đo "bộ máy"
  sinh số (trạng thái + con trỏ), không chứa số nào.
* Lưu ý: `getsizeof` không đo sâu (đối tượng lồng trong list) — nhưng để so
  sánh tương đối hai cách lưu cùng dữ liệu thì hoàn toàn đủ.

**Độ phức tạp:** đo trong O(1) — hàm hệ thống trả kích thước đã biết sẵn.

</details>

<details>
<summary>✅ Bài 17: Đếm dòng trong file lớn (giả lập)</summary>

**Phân tích:** Đếm số dòng không rỗng trong file chỉ bằng generator +
`sum(1 for ...)`, không đọc cả file vào RAM. Với file thật hàng GB, đây là
cách duy nhất khả thi; ở đây giả lập bằng file 5 dòng.

**Ý tưởng:** Mỗi dòng không rỗng đóng góp `1` vào tổng; dòng rỗng (chỉ có
`\n` hoặc khoảng trắng) bị loại bởi `dong.strip() != ""`.

**Thuật toán:**
1. Tạo `du_lieu.txt` gồm 5 dòng số.
2. Reuse generator `doc_file` (bài 10).
3. `sum(1 for dong in doc_file(...) if dong.strip() != "")`.

**Code:**

```python
# Tạo file giả lập
with open("du_lieu.txt", "w", encoding="utf-8") as f:
    f.write("10\n20\n30\n40\n50\n")


def doc_file(ten):
    with open(ten, encoding="utf-8") as f:
        for dong in f:
            yield dong


so_dong = sum(1 for dong in doc_file("du_lieu.txt")
              if dong.strip() != "")
print("So dong khong rong:", so_dong)
```

**Giải thích code:**
* In ra: So dong khong rong: 5. ✔
* `sum(1 for ...)` là idiom đếm chuẩn Python: tổng của toàn số 1 = số dòng
  thỏa điều kiện; đọc cực nhanh sau khi đã quen mắt.
* Lỗi thường gặp: `sum(dong for ...)` — cộng chuỗi với số → `TypeError`.
  Phải là `sum(1 for ...)` (đếm) hoặc `sum(int(dong) ...)` (cộng giá trị).

**Độ phức tạp:** O(số dòng) thời gian, O(1) bộ nhớ — không phụ thuộc kích
thước file.

</details>

<details>
<summary>✅ Bài 18: Generator ghép đôi hai danh sách</summary>

**Phân tích:** Từ `a = ["A1","A2"]`, `b = ["B1","B2"]` sinh ra
A1, B1, A2, B2 — xen kẽ theo chỉ số. Giả định hai danh sách cùng độ dài
(đề bài ghi rõ), duyệt theo `range(len(a))`.

**Ý tưởng:** Mỗi vòng lặp `yield` hai lần: `a[i]` rồi `b[i]` — thứ tự yield
quyết định thứ tự xuất hiện trong kết quả.

**Thuật toán:**
1. Duyệt `i` từ 0 đến `len(a) - 1`.
2. `yield a[i]`, rồi `yield b[i]`.
3. In cách nhau bằng dấu cách.

**Code:**

```python
def ghep_doi(a, b):
    for i in range(len(a)):
        yield a[i]
        yield b[i]


a = ["A1", "A2"]
b = ["B1", "B2"]
for x in ghep_doi(a, b):
    print(x, end=" ")
```

**Giải thích code:**
* In ra: A1 B1 A2 B2. ✔
* Kỹ thuật "yield nhiều lần trong một vòng lặp" — một generator có thể sinh
  ra nhiều giá trị mỗi lần lặp, không giới hạn 1 yield / 1 vòng.
* Nếu hai danh sách khác độ dài: dùng `zip(a, b)` an toàn hơn
  (`for x, y in zip(a, b): yield x; yield y`) — dừng ở danh sách ngắn hơn,
  tránh `IndexError`.

**Độ phức tạp:** O(n) thời gian, O(1) bộ nhớ phụ.

</details>

<details>
<summary>✅ Bài 19: Tổng Fibonacci 50 số (chứng minh tiết kiệm nhớ)</summary>

**Phân tích:** Tính tổng 50 số Fibonacci đầu bằng `sum(fibonacci(50))` — không
list trung gian. Đáp án này còn **sửa một lỗi trong đề bài gốc**: đề ghi kết
quả `12586269024`, nhưng tổng 50 số đầu (F₀..F₄₉) đúng phải là `20365011073`
(đã kiểm chứng bằng cách chạy code).

**Ý tưởng:** Reuse generator `fibonacci(n)` (bài 8); `sum()` kéo toàn bộ;
chứng minh: với 50 số thì list vẫn ổn, nhưng với 5.000.000 số thì chỉ
generator mới sống sót.

**Thuật toán:**
1. Dùng nguyên generator `fibonacci(n)` đã viết.
2. `print("Tong 50 so Fibonacci dau:", sum(fibonacci(50)))`.

**Code:**

```python
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


print("Tong 50 so Fibonacci dau:", sum(fibonacci(50)))
```

**Giải thích code:**
* Chạy thật cho kết quả: `Tong 50 so Fibonacci dau: 20365011073`. ✔
* Vì sao đề gốc sai? `12586269024 = F₅₀ − 1` — đó là tổng 50 số **bắt đầu từ 1**
  (F₁..F₅₀), không phải dãy "0, 1, 1, 2..." như đề bài 8 định nghĩa. Bài học:
  **luôn chạy code để kiểm chứng**, đừng tin con số ghi sẵn — kể cả trong giáo
  trình này.
* Thử `sum(fibonacci(500000))` — vẫn chạy mượt vì generator; còn list 500.000
  số Fibonacci (số khổng lồ hàng trăm nghìn chữ số) sẽ nuốt RAM.

**Độ phức tạp:** O(n) thời gian, O(1) bộ nhớ (ngoài số nguyên lớn dần).

</details>

<details>
<summary>✅ Bài 20: Đọc log + thống kê lỗi (tổng hợp)</summary>

**Phân tích:** Bài tổng hợp: tạo file log 6 dòng (dạng `OK ...` / `LOI ...`),
reuse generator `doc_file` (bài 10), kết hợp idiom đếm `sum(1 for ...)`
(bài 17) và lọc tiền tố `startswith` (bài 11). Cả khóa Generator dồn vào một bài.

**Ý tưởng:** Generator đọc từng dòng; biểu thức đếm chỉ giữ dòng `LOI`;
kết quả duy nhất là một con số.

**Thuật toán:**
1. Tạo `he_thong.log` gồm 6 dòng, trong đó 3 dòng `LOI`.
2. `doc_file(ten_file)`: yield từng dòng đã strip.
3. `sum(1 for dong in doc_file(...) if dong.startswith("LOI"))`.

**Code:**

```python
# Tạo file log giả lập
with open("he_thong.log", "w", encoding="utf-8") as f:
    f.write("OK khoi dong\n")
    f.write("LOI ket noi database\n")
    f.write("OK tai du lieu\n")
    f.write("LOI ghi file that bai\n")
    f.write("OK gui bao cao\n")
    f.write("LOI email khong gui duoc\n")


def doc_file(ten):
    with open(ten, encoding="utf-8") as f:
        for dong in f:
            yield dong.strip()


so_loi = sum(1 for dong in doc_file("he_thong.log")
             if dong.startswith("LOI"))
print("So loi phat hien:", so_loi)
```

**Giải thích code:**
* In ra: So loi phat hien: 3. ✔
* Công thức "đọc lười + lọc + đếm trong một dòng" xử lý được log hàng GB —
  đúng cách các hệ thống thật thống kê lỗi mỗi ngày.

**Độ phức tạp:** O(số dòng) thời gian, O(1) bộ nhớ.

</details>
'''.strip()


# ---------- Bài 40: đáp án 15-20 ----------

B40 = r'''
<details>
<summary>✅ Bài 15: Menu đơn giản (Thêm / Xem / Thoát)</summary>

**Phân tích:** Dựng khung chương trình menu: `in_menu()` chỉ lo in,
`main()` lo vòng lặp, còn nghiệp vụ (thêm/xem) reuse hàm `them_sach`,
`hien_thi_danh_sach` đã viết ở các bài trước. Chưa có tìm/sửa/xóa —
menu chỉ 3 mục.

**Ý tưởng:** `while True` + rẽ nhánh theo chuỗi lựa chọn; `break` khi chọn
`"0"`. So sánh với **chuỗi** (`chon == "1"`) chứ không đổi sang `int` —
tránh crash khi người dùng gõ chữ.

**Thuật toán:**
1. `kho = []`.
2. Lặp: in menu → đọc lựa chọn → `"1"`: nhập 6 trường, gọi `them_sach`;
   `"2"`: gọi `hien_thi_danh_sach`; `"0"`: chào tạm biệt + `break`;
   còn lại: báo không có lựa chọn này.

**Code:**

```python
from typing import Dict, List


def tao_sach(ma, ten, tac_gia, the_loai, gia, so_luong):
    return {"ma": ma, "ten": ten, "tac_gia": tac_gia,
            "the_loai": the_loai, "gia": gia, "so_luong": so_luong}


def them_sach(kho, sach):
    kho.append(sach)
    print("Da them sach co ma", sach["ma"])


def hien_thi_danh_sach(kho):
    if len(kho) == 0:
        print("Kho trong!")
        return
    for sach in kho:
        print(sach["ten"], sach["tac_gia"], sach["the_loai"],
              sach["gia"], sach["so_luong"])


def in_menu():
    print("1. Them sach")
    print("2. Xem kho")
    print("0. Thoat")


def main():
    kho = []
    while True:
        in_menu()
        chon = input("Chon: ")
        if chon == "1":
            ma = int(input("Ma: "))
            ten = input("Ten: ")
            tac_gia = input("Tac gia: ")
            the_loai = input("The loai: ")
            gia = float(input("Gia: "))
            so_luong = int(input("So luong: "))
            them_sach(kho, tao_sach(ma, ten, tac_gia, the_loai,
                                    gia, so_luong))
        elif chon == "2":
            hien_thi_danh_sach(kho)
        elif chon == "0":
            print("Tam biet!")
            break
        else:
            print("Khong co lua chon nay!")


main()
```

**Giải thích code:**
* Nhập theo đề bài (Thêm "De Men"/"To Hoai"/"Truyen"/65000/10 → Xem → Thoát)
  in ra đúng: `De Men  To Hoai  Truyen  65000.0  10` rồi `Tam biet!`. ✔
* Nhánh `else` cuối là "lưới an toàn" cho lựa chọn lạ — menu không bao giờ
  treo hay crash vì nhập sai.

**Độ phức tạp:** mỗi lượt menu O(số sách) khi Xem, O(1) khi Thêm/Thoát.

</details>

<details>
<summary>✅ Bài 16: Thêm chức năng Tìm kiếm vào menu</summary>

**Phân tích:** Thêm mục `3. Tim theo ten` vào menu và nhánh xử lý trong
`main()`. Kết quả `tim_theo_ten` có thể là `None` — bắt buộc kiểm tra trước
khi truy cập `sach["ten"]`, nếu không sẽ `TypeError`.

**Ý tưởng:** `tim_theo_ten` so sánh không phân biệt hoa/thường bằng `.lower()`
cả hai phía; `main()` chỉ thêm 1 nhánh `elif`, không sửa code cũ.

**Thuật toán:**
1. Bổ sung dòng in menu: `3. Tim theo ten`.
2. Nhánh `"3"`: nhập tên → gọi `tim_theo_ten` → tìm thấy in
   `ten + " - " + str(gia)`, không thấy in `"Khong tim thay"`.

**Code:**

```python
def tim_theo_ten(kho, ten_can_tim):
    for sach in kho:
        if sach["ten"].lower() == ten_can_tim.lower():
            return sach
    return None


# --- Bổ sung vào in_menu() ---
# print("3. Tim theo ten")

# --- Bổ sung vào main(), sau nhánh "2" ---
# elif chon == "3":
#     ten = input("Nhap ten can tim: ")
#     sach = tim_theo_ten(kho, ten)
#     if sach is not None:
#         print(sach["ten"] + " - " + str(sach["gia"]))
#     else:
#         print("Khong tim thay")
```

**Giải thích code:**
* Thêm sách "De Men Phieu Luu Ky" giá 65000, chọn 3, nhập `de` → tìm thấy
  (vì đề bài 5 dùng tìm "chứa", ở đây dùng khớp toàn bộ không phân biệt hoa
  thường — với input mẫu cả hai cách đều ra `De Men Phieu Luu Ky - 65000.0`). ✔
* `str(sach["gia"])` bắt buộc vì không cộng chuỗi với số được (`"..." + 65000`
  → `TypeError`) — lỗi kinh điển của người mới.

**Độ phức tạp:** O(số sách) mỗi lần tìm.

</details>

<details>
<summary>✅ Bài 17: Thêm chức năng Sửa và Xóa</summary>

**Phân tích:** Thêm mục 4 (Sửa giá theo mã) và 5 (Xóa theo mã). Reuse nguyên
`su gia` (bài 9) và `xoa_sach` (bài 10) — menu chỉ là "lớp vỏ" gọi hàm đã có.

**Ý tưởng:** Mỗi nhánh menu làm đúng 3 việc: đọc mã (và giá mới) → gọi hàm
nghiệp vụ → hàm tự in thông báo kết quả. Sau chuỗi thao tác, in số đầu sách
còn lại để kiểm chứng.

**Thuật toán:**
1. Bổ sung 2 dòng menu: `4. Sua sach`, `5. Xoa sach`.
2. Nhánh `"4"`: nhập mã, nhập giá mới, gọi `sua_gia`.
3. Nhánh `"5"`: nhập mã, gọi `xoa_sach`.
4. In `len(kho)`.

**Code:**

```python
def sua_gia(kho, ma, gia_moi):
    for sach in kho:
        if sach["ma"] == ma:
            sach["gia"] = gia_moi
            print("Da sua ma", ma)
            return
    print("Khong tim thay ma", ma)


def xoa_sach(kho, ma):
    for sach in kho:
        if sach["ma"] == ma:
            kho.remove(sach)
            print("Da xoa ma", ma)
            return
    print("Khong tim thay ma", ma)


# --- Bổ sung vào in_menu() ---
# print("4. Sua sach")
# print("5. Xoa sach")

# --- Bổ sung vào main() ---
# elif chon == "4":
#     ma = int(input("Ma can sua: "))
#     gia_moi = float(input("Gia moi: "))
#     sua_gia(kho, ma, gia_moi)
# elif chon == "5":
#     ma = int(input("Ma can xoa: "))
#     xoa_sach(kho, ma)
```

**Giải thích code:**
* Thêm 2 sách → sửa mã 1 thành 70000 → xóa mã 2 → còn 1 đầu sách:
  in ra đúng `Da sua ma 1.` / `Da xoa ma 2.` / `Con 1 dau sach.`. ✔
* `return` ngay sau khi sửa/xóa xong — không duyệt tiếp cho tốn thời gian,
  và tránh lỗi "xóa trong lúc duyệt" khi có mã trùng.

**Độ phức tạp:** O(số sách) mỗi thao tác sửa/xóa.

</details>

<details>
<summary>✅ Bài 18: Thêm chức năng Thống kê và Lưu file</summary>

**Phân tích:** Thêm mục 6 (Thống kê) và 7 (Lưu file). Cả hai reuse hàm đã có
(bài 11, 13). Lưu vào tên file cố định `"kho_chinh.json"` để lần chạy sau
còn biết đường nạp lại.

**Ý tưởng:** `thong_ke` tính 3 con số: số đầu sách, tổng số cuốn
(`sum` số lượng), tổng giá trị (`sum` giá × số lượng, in có dấu phẩy ngăn
nghìn). `luu_file` dùng `json.dump` với `ensure_ascii=False` để giữ tiếng Việt.

**Thuật toán:**
1. Bổ sung 2 dòng menu: `6. Thong ke`, `7. Luu file`.
2. Nhánh `"6"` gọi `thong_ke(kho)`; nhánh `"7"` gọi
   `luu_file(kho, "kho_chinh.json")`.

**Code:**

```python
import json


def thong_ke(kho):
    so_dau = len(kho)
    tong_cuon = sum(s["so_luong"] for s in kho)
    tong_gia_tri = sum(s["gia"] * s["so_luong"] for s in kho)
    print("So dau sach:", so_dau)
    print("Tong so cuon:", tong_cuon)
    print("Tong gia tri:", f"{tong_gia_tri:,}", "dong")


def luu_file(kho, ten_file):
    with open(ten_file, "w", encoding="utf-8") as f:
        json.dump(kho, f, ensure_ascii=False, indent=2)
    print("Da luu", len(kho), "cuon sach.")


# --- Bổ sung vào in_menu() ---
# print("6. Thong ke")
# print("7. Luu file")

# --- Bổ sung vào main() ---
# elif chon == "6":
#     thong_ke(kho)
# elif chon == "7":
#     luu_file(kho, "kho_chinh.json")
```

**Giải thích code:**
* Thêm 2 sách (mỗi cuốn SL 10, giá 65000 và 59400) → Lưu → Thống kê → Thoát
  in đúng: `Da luu 2 cuon sach.` / `So dau sach: 2` / `Tong so cuon: 20` /
  `Tong gia tri: 1,244,000 dong` / `Tam biet!`. ✔
* `f"{tong_gia_tri:,}"` — dấu phẩy trong f-string tự thêm dấu ngăn nghìn,
  mẹo nhỏ nhưng làm output "chuyên nghiệp" hẳn.

**Độ phức tạp:** O(số sách) cho thống kê; O(số sách) cho ghi file.

</details>

<details>
<summary>✅ Bài 19: Tự động lưu khi thoát</summary>

**Phân tích:** Chống mất dữ liệu khi người dùng quên bấm Lưu: đặt `luu_file`
ngay trước `break` trong nhánh `"0"`. Một dòng code, cứu cả buổi nhập liệu.

**Ý tưởng:** Nhánh thoát làm 3 việc theo đúng thứ tự: lưu → báo đã lưu →
chào tạm biệt → thoát. Thứ tự quan trọng: báo "đã lưu" chỉ sau khi lưu xong.

**Thuật toán:** Trong nhánh `chon == "0"`: gọi `luu_file(kho, "kho_sach.json")`,
in xác nhận, in tạm biệt, `break`.

**Code:**

```python
# --- Thay thế nhánh "0" cũ trong main() bằng: ---
# elif chon == "0":
#     luu_file(kho, "kho_sach.json")
#     print("Da tu dong luu truoc khi thoat.")
#     print("Tam biet!")
#     break
```

**Giải thích code:**
* Thêm 1 sách → chọn 0 → in đúng: `Da luu 1 cuon sach.` (từ trong `luu_file`),
  `Da tu dong luu truoc khi thoat.`, `Tam biet!`. ✔
* Vì lưu tự động rồi, mục 7 trong menu trở thành "lưu thủ công giữa chừng" —
  vẫn hữu ích khi muốn checkpoint mà chưa thoát.

**Độ phức tạp:** O(số sách) cho lần ghi file cuối.

</details>

<details>
<summary>✅ Bài 20: Chương trình hoàn chỉnh</summary>

**Phân tích:** Ghép toàn bộ mảnh ghép: khởi động nạp dữ liệu cũ (`nap_file`
với `try/except FileNotFoundError` cho lần chạy đầu tiên chưa có file),
menu đủ 8 mục, thoát tự lưu. Đây là "dự án thật" thu nhỏ: mở app → dữ liệu
cũ còn đó → làm việc → đóng app → không mất gì.

**Ý tưởng:** `main()` lắp các hàm đã có đúng thứ tự: nạp trước vòng lặp,
menu trong vòng lặp, lưu trong nhánh thoát. Không viết lại logic nào —
chỉ "đấu nối".

**Thuật toán:**
1. `nap_file(ten_file)`: đọc JSON; chưa có file → kho rỗng + thông báo.
2. `main()`: `kho = nap_file("kho_sach.json")` trước vòng lặp.
3. Menu 8 mục (1 Thêm, 2 Xem, 3 Tìm, 4 Sửa, 5 Xóa, 6 Thống kê, 7 Lưu, 0 Thoát).
4. Nhánh `"0"`: tự lưu + chào + `break`.

**Code:**

```python
import json


def nap_file(ten_file):
    try:
        with open(ten_file, encoding="utf-8") as f:
            kho = json.load(f)
        print("So dau sach khi nap:", len(kho))
        return kho
    except FileNotFoundError:
        print("Chua co du lieu cu - bat dau voi kho trong.")
        return []


def main():
    kho = nap_file("kho_sach.json")
    while True:
        in_menu()   # in đủ 8 mục: 1 2 3 4 5 6 7 0
        chon = input("Chon: ")
        if chon == "1":
            ma = int(input("Ma: "))
            ten = input("Ten: ")
            tac_gia = input("Tac gia: ")
            the_loai = input("The loai: ")
            gia = float(input("Gia: "))
            so_luong = int(input("So luong: "))
            them_sach(kho, tao_sach(ma, ten, tac_gia, the_loai,
                                    gia, so_luong))
        elif chon == "2":
            hien_thi_danh_sach(kho)
        elif chon == "3":
            ten = input("Nhap ten can tim: ")
            sach = tim_theo_ten(kho, ten)
            if sach is not None:
                print(sach["ten"] + " - " + str(sach["gia"]))
            else:
                print("Khong tim thay")
        elif chon == "4":
            ma = int(input("Ma can sua: "))
            gia_moi = float(input("Gia moi: "))
            sua_gia(kho, ma, gia_moi)
        elif chon == "5":
            ma = int(input("Ma can xoa: "))
            xoa_sach(kho, ma)
        elif chon == "6":
            thong_ke(kho)
        elif chon == "7":
            luu_file(kho, "kho_sach.json")
        elif chon == "0":
            luu_file(kho, "kho_sach.json")
            print("Da tu dong luu truoc khi thoat.")
            print("Tam biet!")
            break
        else:
            print("Khong co lua chon nay!")
```

**Giải thích code:**
* Kịch bản đề bài (khởi động với 1 sách → xem → thêm 1 → lưu → thống kê →
  thoát → khởi động lại) in đúng chuỗi output mẫu, kết thúc bằng
  `So dau sach khi nap lai: 2` — chứng minh dữ liệu "sống sót" qua lần thoát. ✔
* `try/except FileNotFoundError` trong `nap_file` xử lý lần chạy đầu tiên:
  chưa có file là chuyện bình thường, không phải lỗi — chương trình bắt đầu
  với kho trống thay vì crash.

**Độ phức tạp:** khởi động O(số sách đã lưu); mỗi thao tác menu như các bài trước.

</details>
'''.strip()


def insert_after_last_details(lines, start_idx, end_idx, blocks):
    """Chèn blocks ngay sau </details> cuối cùng trong [start_idx, end_idx).
    Nếu không có </details> nào, chèn ngay sau dòng start_idx."""
    last = None
    for i in range(start_idx, end_idx):
        if lines[i].strip() == "</details>":
            last = i
    pos = (last + 1) if last is not None else (start_idx + 1)
    new_lines = [""] + blocks.split("\n") + [""]
    return lines[:pos] + new_lines + lines[pos:]


def insert_into_group(path, group_marker, blocks):
    """Chèn đáp án mới vào đúng nhóm mức độ của phần Đáp án."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    # 1. phần Đáp án bắt đầu ở đâu
    ans_start = next(i for i, ln in enumerate(lines)
                     if ln.strip() == "## ✅ Đáp án")
    # 2. nhóm mong muốn (nếu có)
    grp = None
    if group_marker:
        for i in range(ans_start, len(lines)):
            if lines[i].strip() == group_marker:
                grp = i
                break
    if grp is not None:
        # cuối nhóm = dòng '## ' tiếp theo (sau header nhóm)
        end = len(lines)
        for i in range(grp + 1, len(lines)):
            if lines[i].startswith("## "):
                end = i
                break
        lines = insert_after_last_details(lines, grp, end, blocks)
    else:
        # không có nhóm: cuối phần Đáp án = '---' ngay trước '## ➡️'
        end = len(lines)
        for i in range(ans_start, len(lines)):
            if lines[i].strip() == "## ➡️ Điều hướng":
                j = i - 1
                while j > ans_start and lines[j].strip() == "":
                    j -= 1
                end = j if lines[j].strip() == "---" else i
                break
        lines = insert_after_last_details(lines, ans_start, end, blocks)

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("Đã bổ sung:", path.relative_to(ROOT))


def main():
    insert_into_group(ROOT / "01-Co-Ban" / "20-Module" / "bai.md",
                       "## 🔴 Khó (Bài 15 – 20)", B20)
    insert_into_group(ROOT / "01-Co-Ban" / "27-Generator" / "bai.md",
                       "## 🟡 Trung bình (Bài 8 – 14)", B27_MEDIUM)
    insert_into_group(ROOT / "01-Co-Ban" / "27-Generator" / "bai.md",
                       "## 🔴 Khó (Bài 15 – 20)", B27_HARD)
    insert_into_group(ROOT / "03-Thuc-Chien" / "11-Mini-Project" / "bai.md",
                       None, B40)


if __name__ == "__main__":
    main()
