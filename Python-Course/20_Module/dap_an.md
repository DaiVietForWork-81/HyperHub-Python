# ✅ Bài 20: Đáp Án – Module Trong Python

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án để việc học hiệu quả nhất.

> 🛠️ **Lưu ý chung:** Với bài cần tạo module, code đáp án sẽ **tự tạo file module bằng lệnh ghi file** ngay trong chương trình (kỹ thuật `open(...).write(...)` — bạn sẽ học sâu ở Bài 22) để **mọi thứ chạy được ngay** khi copy vào một file `.py`. Sau đó gọi `import`.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Căn bậc hai với math

**Phân tích:** Dùng hàm `sqrt` trong module `math` — thư viện chuẩn, không cần cài thêm.

**Ý tưởng:** `import math` rồi gọi `math.sqrt(81)`.

**Thuật toán:**
1. Import module `math`.
2. In kết quả `math.sqrt(81)`.

**Code:**

```python
import math

print(math.sqrt(81))
```

**Giải thích code:**
* `import math` — nạp module toán học.
* `math.sqrt(81)` — căn bậc hai của 81, kết quả `9.0` (số thực).

**Độ phức tạp:** O(1).

---

### Bài 2: Tung xúc xắc

**Phân tích:** Mô phỏng con xúc xắc 6 mặt bằng cách sinh số nguyên ngẫu nhiên 1–6.

**Ý tưởng:** Dùng `random.randint(1, 6)`.

**Thuật toán:**
1. `import random`.
2. Gán `ket_qua = random.randint(1, 6)`.
3. In kết quả.

**Code:**

```python
import random

# Tung xúc xắc: số ngẫu nhiên từ 1 đến 6
ket_qua = random.randint(1, 6)
print(ket_qua)
```

**Giải thích code:**
* `randint(a, b)` — trả về số nguyên ngẫu nhiên nằm giữa `a` và `b`, **bao gồm cả hai đầu mút**.
* Mỗi lần chạy, kết quả khác nhau.

**Độ phức tạp:** O(1).

---

### Bài 3: Bí danh cho math

**Phân tích:** Luyện cú pháp `as` — đặt tên ngắn cho module.

**Ý tưởng:** `import math as m` rồi dùng `m.pi`, `m.ceil`.

**Thuật toán:**
1. Import math với bí danh `m`.
2. In `m.pi`.
3. In `m.ceil(4.2)`.

**Code:**

```python
import math as m

print(m.pi)
print(m.ceil(4.2))
```

**Giải thích code:**
* `import math as m` — từ nay gọi `m.` thay vì `math.`.
* `m.pi` — hằng số pi.
* `m.ceil(4.2)` — làm tròn lên, ra `5`.

**Độ phức tạp:** O(1).

---

### Bài 4: Chỉ lấy một hàm

**Phân tích:** Luyện `from ... import ...` để gọi hàm trực tiếp.

**Ý tưởng:** `from random import randint` rồi gọi `randint(1, 100)`.

**Thuật toán:**
1. Nhập riêng hàm `randint`.
2. In kết quả ngẫu nhiên.

**Code:**

```python
from random import randint

print(randint(1, 100))
```

**Giải thích code:**
* `from random import randint` — chỉ lấy hàm `randint`, không cần tiền tố `random.`.
* Kết quả là số nguyên trong khoảng 1 – 100.

**Độ phức tạp:** O(1).

---

### Bài 5: Bốc thăm món ăn

**Phân tích:** `random.choice` chọn ngẫu nhiên một phần tử từ một chuỗi/list.

**Ý tưởng:** Tạo list món ăn, gọi `random.choice`.

**Thuật toán:**
1. `import random`.
2. Tạo list `mon_an`.
3. Chọn ngẫu nhiên và in.

**Code:**

```python
import random

# Danh sách món ăn trong căng tin
mon_an = ["phở", "bún", "cơm", "bánh mì"]

# Bốc thăm ngẫu nhiên một món
chon = random.choice(mon_an)
print(chon)
```

**Giải thích code:**
* `random.choice(mon_an)` — trả về ngẫu nhiên một phần tử của list.
* `random.choice` còn dùng được cho cả chuỗi, tuple.

**Độ phức tạp:** O(1).

---

### Bài 6: Module chào hỏi của tôi

**Phân tích:** Bài đầu tiên "tự tạo module" — chứng minh file `.py` chính là module.

**Ý tưởng:** Tạo `chao_hon.py` chứa hàm, rồi import từ `main` cùng thư mục. Để file chạy được ngay khi copy, code dưới đây **tự tạo** module trước khi import.

**Thuật toán:**
1. Ghi nội dung hàm `xin_chao` vào file `chao_hon.py`.
2. Import hàm từ `chao_hon`.
3. Gọi hàm với tên `"Mai"`.

**Code:**

```python
# Tự tạo module chao_hon.py ngay trong code để đáp án chạy được
with open("chao_hon.py", "w", encoding="utf-8") as f:
    f.write(
        'def xin_chao(ten):\n'
        '    return f"Xin chao {ten}!"\n'
    )

# Nhập hàm từ module vừa tạo
from chao_hon import xin_chao

# Dùng hàm
print(xin_chao("Mai"))
```

**Giải thích code:**
* `open("chao_hon.py", "w", encoding="utf-8")` — tạo file mới (chế độ `w`) và ghi nội dung hàm.
* `from chao_hon import xin_chao` — import hàm từ module cùng thư mục.
* `xin_chao("Mai")` — trả về chuỗi `"Xin chao Mai!"`.

> 📝 **Cách làm "thật" trong dự án:** tạo hai file `chao_hon.py` và `main.py` như bài tập mô tả.

**Độ phức tạp:** O(1).

---

### Bài 7: Số thực ngẫu nhiên

**Phân tích:** `random.random()` sinh số thực trong `[0.0, 1.0)` — cần làm tròn để hiển thị đẹp.

**Ý tưởng:** Lấy `random.random()`, làm tròn 4 chữ số.

**Thuật toán:**
1. Import random.
2. Sinh số thực ngẫu nhiên.
3. Làm tròn và in.

**Code:**

```python
import random

so = random.random()
print(round(so, 4))
```

**Giải thích code:**
* `random.random()` — số thực ngẫu nhiên lớn hơn hoặc bằng 0, nhỏ hơn 1.
* `round(so, 4)` — giữ 4 chữ số thập phân.

**Độ phức tạp:** O(1).

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Module tiện ích hình tròn

**Phân tích:** Module chứa hằng số `PI` và hai hàm; `main.py` chỉ nhập và tính toán.

**Ý tưởng:** Ghi module `tien_ich.py` bằng code, import 2 hàm cần thiết, in kết quả.

**Thuật toán:**
1. Tạo `tien_ich.py` với `PI` và 2 hàm.
2. Import 2 hàm từ module.
3. Tính toán và in.

**Code:**

```python
# Tự tạo module tien_ich.py
with open("tien_ich.py", "w", encoding="utf-8") as f:
    f.write(
        'PI = 3.14159\n'
        '\n'
        'def dien_tich_hinh_tron(r):\n'
        '    return PI * r * r\n'
        '\n'
        'def chu_vi_hinh_tron(r):\n'
        '    return 2 * PI * r\n'
    )

from tien_ich import dien_tich_hinh_tron, chu_vi_hinh_tron

# Bán kính mẫu
ban_kinh = 5

print("Dien tich:", round(dien_tich_hinh_tron(ban_kinh), 5))
print("Chu vi:", round(chu_vi_hinh_tron(ban_kinh), 4))
```

**Giải thích code:**
* `open(...).write(...)` — tạo file module chứa hằng số và hàm.
* `from tien_ich import ...` — chỉ lấy 2 hàm cần dùng.
* `round(..., 5)` và `round(..., 4)` — làm tròn theo số chữ số mong muốn.

**Độ phức tạp:** O(1).

---

### Bài 9: Giải phương trình bậc hai

**Phân tích:** Công thức nghiệm cần căn bậc hai của biệt thức (delta).

**Ý tưởng:** Tính `delta = b*b - 4*a*c`, `sqrt_delta = math.sqrt(delta)`, rồi hai nghiệm.

**Thuật toán:**
1. Gán `a, b, c = 1, -5, 6`.
2. Tính delta.
3. Tính hai nghiệm và in.

**Code:**

```python
import math

# Hệ số phương trình x^2 - 5x + 6 = 0
a, b, c = 1, -5, 6

# Biệt thức delta
delta = b * b - 4 * a * c

# Căn bậc hai của delta
sqrt_delta = math.sqrt(delta)

# Hai nghiệm
x1 = (-b + sqrt_delta) / (2 * a)
x2 = (-b - sqrt_delta) / (2 * a)

print("Nghiem x1 =", x1)
print("Nghiem x2 =", x2)
```

**Giải thích code:**
* `math.sqrt(delta)` — căn bậc hai để giải phương trình thay vì nhẩm tay.
* Với `a=1, b=-5, c=6`, delta = 1 → nghiệm `3.0` và `2.0`.

> ⚠️ Nếu `delta < 0` chương trình sẽ báo `ValueError` — xử lý bằng `if` là bài nâng cao đáng thử.

**Độ phức tạp:** O(1).

---

### Bài 10: Sinh 5 số và tìm số lớn nhất

**Phân tích:** Gom số ngẫu nhiên vào list rồi tìm phần tử lớn nhất.

**Ý tưởng:** Vòng lặp `for` sinh 5 số, dùng `max()`.

**Thuật toán:**
1. Tạo list rỗng.
2. Lặp 5 lần thêm số ngẫu nhiên.
3. In list và `max(danh_sach)`.

**Code:**

```python
import random

danh_sach = []

# Sinh 5 số nguyên ngẫu nhiên từ 1 đến 99
for i in range(5):
    danh_sach.append(random.randint(1, 99))

print("Cac so:", danh_sach)
print("So lon nhat:", max(danh_sach))
```

**Giải thích code:**
* `append(...)` — thêm từng số vào cuối list.
* `max(danh_sach)` — hàm sẵn có tìm giá trị lớn nhất.
* Trong dự án thật, bạn sẽ gom dữ liệu theo cách này trước khi thống kê.

**Độ phức tạp:** O(n) với n = 5 lượt sinh + duyệt tìm max (thực chất rất nhỏ).

---

### Bài 11: Đồng hồ thông minh

**Phân tích:** Định dạng thời điểm hiện tại theo mẫu `HH:MM:SS DD/MM/YYYY`.

**Ý tưởng:** `datetime.now()` sau đó `strftime(...)`.

**Thuật toán:**
1. `from datetime import datetime`.
2. Lấy thời điểm hiện tại.
3. In theo định dạng.

**Code:**

```python
from datetime import datetime

# Thời điểm hiện tại
bay_gio = datetime.now()

# Định dạng: giờ:phút:giây ngày/tháng/năm
print(bay_gio.strftime("%H:%M:%S %d/%m/%Y"))
```

**Giải thích code:**
* `datetime.now()` — thời điểm hiện tại (ngày giờ của máy).
* `strftime(...)` — đổi `datetime` thành chuỗi theo mã: `%H` giờ (00–23), `%M` phút, `%S` giây, `%d` ngày, `%m` tháng, `%Y` năm.

**Độ phức tạp:** O(1).

---

### Bài 12: Khám phá thư mục

**Phân tích:** Đếm file Python trong thư mục hiện tại bằng `os`.

**Ý tưởng:** `os.getcwd()` lấy thư mục; lặp `os.listdir()`, đếm tên kết thúc bằng `.py`.

**Thuật toán:**
1. `import os`.
2. In `os.getcwd()`.
3. Lặp danh sách file, đếm `endswith(".py")`.

**Code:**

```python
import os

# Thư mục đang làm việc
print("Thu muc hien tai:", os.getcwd())

# Đếm file Python
so_file_py = 0
for ten in os.listdir():
    if ten.endswith(".py"):
        print("File Python:", ten)
        so_file_py = so_file_py + 1

print("So file .py:", so_file_py)
```

**Giải thích code:**
* `os.listdir()` — danh sách tên các tệp/thư mục trong thư mục hiện tại.
* `ten.endswith(".py")` — kiểm tra kiểu file bằng đuôi.
* Kết quả phụ thuộc vào thư mục bạn đang chạy — giá trị in ra có thể khác ví dụ.

**Độ phức tạp:** O(n) với n = số phần tử trong thư mục.

---

### Bài 13: Đoán số một lượt

**Phân tích:** Kết hợp `input` (Bài 7), `random` và `if` để đoán số.

**Ý tưởng:** Máy chọn số 1–10; so sánh với nhập của người chơi.

**Thuật toán:**
1. Máy chọn `so_bi_mat = random.randint(1, 10)`.
2. Người chơi nhập số.
3. So sánh và in thông báo.

**Code:**

```python
import random

# Máy nghĩ số từ 1 đến 10
so_bi_mat = random.randint(1, 10)

# Người chơi nhập dự đoán (# Nhập: 7)
du_doan = int(input("Nhap so ban doan (1-10): "))

if du_doan == so_bi_mat:
    print("Dung roi!")
else:
    print("Sai roi! So bi mat la", so_bi_mat)
```

**Giải thích code:**
* `input(...)` trả về chuỗi nên phải `int(...)` để so sánh số.
* `if/else` quyết định thông báo thắng – thua.
* Lời khuyên: bọc `int(input(...))` trong `try/except` (Bài 19) để an toàn.

**Độ phức tạp:** O(1).

---

### Bài 14: Module có chạy thử

**Phân tích:** Luyện `if __name__ == "__main__"` — file vừa chạy thử trực tiếp vừa được import.

**Ý tưởng:** Module `tien_ich.py` chứa hàm `tong(*cac_so)` + khối chạy thử; `main.py` chỉ import hàm.

**Thuật toán:**
1. Tạo `tien_ich.py` với hàm `tong` và khối `if __name__`.
2. Import từ `main` và in tổng ba số.

**Code:**

```python
# Tự tạo module tien_ich.py có cả phần chạy thử
with open("tien_ich.py", "w", encoding="utf-8") as f:
    f.write(
        'def tong(*cac_so):\n'
        '    """Tính tổng nhiều số."""\n'
        '    ket_qua = 0\n'
        '    for so in cac_so:\n'
        '        ket_qua += so\n'
        '    return ket_qua\n'
        '\n'
        'if __name__ == "__main__":\n'
        '    print("Tong thu nghiem:", tong(1, 2, 3))\n'
    )

# Chạy thử trực tiếp module
import tien_ich

# Đọc phần main: import hàm rồi dùng
from tien_ich import tong
print("Tong:", tong(10, 20, 30))
```

**Giải thích code:**
* `def tong(*cac_so):` — `*` cho phép truyền bao nhiêu số cũng được, gom vào tuple.
* `if __name__ == "__main__":` — câu lệnh này chỉ chạy thử khi gõ `python tien_ich.py`, không chạy khi bị import.
* Chạy toàn file này: dòng `import tien_ich` đã chạy module (không in dòng test vì khi import `__name__` khác `"__main__"`), sau đó dòng `from tien_ich import tong` và `print` hiển thị `Tong: 60`.

**Độ phức tạp:** O(n) với n = số lượng đối số.

---

<!--P-DAPAN-P3-->