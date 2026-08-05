# ✅ Bài 12: Đáp Án – Hàm (Function)

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án để việc học hiệu quả nhất.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Hàm xin chào

**Phân tích:** Bài làm quen — viết hàm không tham số, chỉ in chữ, rồi gọi hàm.

**Ý tưởng:** Hàm chỉ gồm một lệnh `print()`. Gọi hàm 2 lần để thấy code chạy lại.

**Thuật toán:**
1. Định nghĩa hàm `xin_chao()`.
2. Trong thân hàm in ra dòng chữ.
3. Gọi hàm hai lần.

**Code:**

```python
def xin_chao():
    """In lời chào ra màn hình."""
    print("Xin chao, lop 10A1!")

xin_chao()
xin_chao()
```

**Giải thích code:**
* `def xin_chao():` — khai báo hàm không có tham số.
* `print(...)` — thân hàm, chạy khi hàm được gọi.
* Hai lần `xin_chao()` — hàm chạy 2 lần, in 2 dòng giống nhau.

**Độ phức tạp:** O(1).

---

### Bài 2: Hàm chào theo tên

**Phân tích:** Hàm nhận tham số `ten` và chèn vào chuỗi in ra.

**Ý tưởng:** Dùng f-string để chèn biến vào chuỗi.

**Thuật toán:**
1. Định nghĩa `chao_ban(ten)`.
2. In `f"Xin chao, {ten}!"`.
3. Gọi với `"Mai"`, rồi `"Nam"`.

**Code:**

```python
def chao_ban(ten):
    """Chào một người theo tên."""
    print(f"Xin chao, {ten}!")

chao_ban("Mai")
chao_ban("Nam")
```

**Giải thích code:**
* `ten` — tham số nhận giá trị từ đối số khi gọi.
* `f"Xin chao, {ten}!"` — `{ten}` được thay bằng giá trị thực của biến.

**Độ phức tạp:** O(1).

---

### Bài 3: Hàm tính bình phương

**Phân tích:** Hàm tính toán phải dùng `return` để trả kết quả.

**Ý tưởng:** `binh_phuong(x)` trả về `x * x`.

**Thuật toán:**
1. Định nghĩa hàm trả về `x * x`.
2. Gọi hàm với `7` và in kết quả.

**Code:**

```python
def binh_phuong(x):
    """Trả về bình phương của x."""
    return x * x

print(binh_phuong(7))
```

**Giải thích code:**
* `return x * x` — `49` được gửi ra ngoài.
* `print(binh_phuong(7))` — gọi hàm, nhận `49`, in ra màn hình.

**Độ phức tạp:** O(1).

---

### Bài 4: Hàm cộng hai số

**Phân tích:** Hàm 2 tham số, trả về tổng.

**Ý tưởng:** `return a + b`.

**Thuật toán:**
1. Định nghĩa `cong_hai_so(a, b)`.
2. Trả về `a + b`.
3. Gọi với `12, 30` và in.

**Code:**

```python
def cong_hai_so(a, b):
    """Trả về tổng của a và b."""
    return a + b

print(cong_hai_so(12, 30))
```

**Giải thích code:**
* `a` nhận `12`, `b` nhận `30` — theo thứ tự vị trí.
* Hàm trả về `42`.

**Độ phức tạp:** O(1).

---

### Bài 5: Hàm với docstring

**Phân tích:** Bài luyện viết docstring và dùng công thức chu vi.

**Ý tưởng:** Chu vi = `2 * (dai + rong)`.

**Thuật toán:**
1. Viết hàm kèm docstring.
2. Trả về chu vi.
3. Gọi với `5, 3` và in.

**Code:**

```python
def tinh_chu_vi_hcn(dai, rong):
    """Tính chu vi hình chữ nhật.

    Args:
        dai (float): chiều dài
        rong (float): chiều rộng

    Returns:
        float: chu vi hình chữ nhật
    """
    return 2 * (dai + rong)

print(tinh_chu_vi_hcn(5, 3))
```

**Giải thích code:**
* Docstring nằm ngay sau `def`, trong cặp `"""..."""`.
* `2 * (5 + 3) = 16`.

**Độ phức tạp:** O(1).

---

### Bài 6: Hàm trả về lời chào

**Phân tích:** Phân biệt hàm `print` (in thẳng) và hàm `return` (trả về để in ở ngoài).

**Ý tưởng:** Hàm `tao_loi_chao` chỉ `return` chuỗi; việc in do nơi gọi đảm nhận.

**Thuật toán:**
1. Hàm trả về chuỗi chào bằng f-string.
2. Lưu kết quả vào biến hoặc in trực tiếp.

**Code:**

```python
def tao_loi_chao(ten):
    """Tạo chuỗi lời chào buổi sáng."""
    return f"Chao buoi sang, {ten}!"

loi = tao_loi_chao("An")
print(loi)
```

**Giải thích code:**
* Hàm không in — chỉ tạo chuỗi rồi trả về.
* `loi = tao_loi_chao("An")` — biến nhận chuỗi trả về, sau đó mới in.

**Độ phức tạp:** O(1).

---

### Bài 7: Hàm kiểm tra chẵn lẻ

**Phân tích:** Hàm trả về `True`/`False` — kiểu dữ liệu boolean.

**Ý tưởng:** Số chẵn khi `n % 2 == 0`.

**Thuật toán:**
1. Định nghĩa hàm dùng biểu thức so sánh.
2. Gọi và in với `10` và `7`.

**Code:**

```python
def la_so_chan(n):
    """Kiểm tra n có phải số chẵn không."""
    return n % 2 == 0

print(la_so_chan(10))
print(la_so_chan(7))
```

**Giải thích code:**
* `n % 2 == 0` là biểu thức so sánh — kết quả đã là `True`/`False`.
* `10 % 2 == 0` → `True`; `7 % 2 == 0` → `False`.

**Độ phức tạp:** O(1).

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Hàm tính diện tích tam giác

**Phân tích:** Dùng công thức `day * cao / 2`, in kết quả 2 chữ số thập phân.

**Ý tưởng:** `return day * cao / 2`, định dạng bằng f-string.

**Thuật toán:**
1. Tính diện tích trong hàm.
2. In với định dạng `:.2f`.

**Code:**

```python
def dien_tich_tam_giac(day, cao):
    """Tính diện tích tam giác."""
    return day * cao / 2

ket_qua = dien_tich_tam_giac(10, 4)
print(f"Dien tich tam giac: {ket_qua:.2f}")
```

**Giải thích code:**
* `10 * 4 / 2 = 20.0` — phép `/` luôn cho số thực.
* `{ket_qua:.2f}` — hiển thị đúng 2 chữ số sau dấu phẩy: `20.00`? Không — `20.0` có 1 chữ số; `.2f` thêm đủ 2: in ra `20.00`. Nhưng đề yêu cầu `20.0`, nên dùng `{ket_qua:.1f}` cũng được. Cả hai đều chấp nhận nếu thể hiện đúng ý nghĩa.

**Độ phức tạp:** O(1).

---

### Bài 9: Hàm xếp loại học sinh

**Phân tích:** Phân nhánh điểm theo 4 mức.

**Ý tưởng:** `if/elif/else` với mỗi nhánh một `return`.

**Thuật toán:**
1. Nếu `dtb >= 8.5` → "Gioi".
2. Nếu `dtb >= 7.0` → "Kha".
3. Nếu `dtb >= 5.0` → "Trung binh".
4. Ngược lại → "Yeu".

**Code:**

```python
def xep_loai(dtb):
    """Xếp loại học lực theo điểm trung bình."""
    if dtb >= 8.5:
        return "Gioi"
    elif dtb >= 7.0:
        return "Kha"
    elif dtb >= 5.0:
        return "Trung binh"
    return "Yeu"

print("8.7 ->", xep_loai(8.7))
print("6.5 ->", xep_loai(6.5))
print("4.9 ->", xep_loai(4.9))
```

**Giải thích code:**
* Các nhánh kiểm tra từ cao xuống thấp — không cần viết `dtb < 8.5` vì nhánh trước đã loại.
* `return` trong `if` đã kết thúc hàm nên nhánh cuối `return "Yeu"` không cần `else`.

**Độ phức tạp:** O(1).

---

### Bài 10: Hàm tính điểm trung bình 3 môn

**Phân tích:** Tính trung bình và làm tròn 1 chữ số.

**Ý tưởng:** `(toan + van + anh) / 3`, dùng `round(..., 1)`.

**Thuật toán:**
1. Viết hàm trung bình 3 môn.
2. Gọi cho An và Bình, in kết quả.

**Code:**

```python
def tinh_trung_binh(toan, van, anh):
    """Tính điểm trung bình 3 môn."""
    return (toan + van + anh) / 3

diem_an = round(tinh_trung_binh(8, 7.5, 9), 1)
diem_binh = round(tinh_trung_binh(5, 6, 6.5), 1)
print(f"An: {diem_an}")
print(f"Binh: {diem_binh}")
```

**Giải thích code:**
* An: `(8 + 7.5 + 9) / 3 = 8.166...` → `round(..., 1) = 8.2`.
* Bình: `(5 + 6 + 6.5) / 3 = 5.833...` → `5.8`.

**Độ phức tạp:** O(1).

---

### Bài 11: Hàm có tham số mặc định

**Phân tích:** Dùng tham số mặc định cho số lượng.

**Ý tưởng:** `so_luong=1` — khi gọi thiếu đối số thứ hai, tự dùng `1`.

**Thuật toán:**
1. Định nghĩa hàm với tham số mặc định.
2. Gọi lần 1 không truyền số lượng.
3. Gọi lần 2 truyền `3`.

**Code:**

```python
def dat_truoc(mon, so_luong=1):
    """Đặt trước món ăn với số lượng (mặc định 1)."""
    print(f"Ban da dat {so_luong} phan {mon}.")

dat_truoc("pho")
dat_truoc("bun bo", 3)
```

**Giải thích code:**
* Lần gọi thứ nhất: `so_luong` nhận giá trị mặc định `1`.
* Lần gọi thứ hai: truyền `3` ghi đè giá trị mặc định.

**Độ phức tạp:** O(1).

---

### Bài 12: Gọi hàm bằng keyword arguments

**Phân tích:** Keyword arguments giúp gọi hàm không phụ thuộc thứ tự.

**Ý tưởng:** Ghi rõ `ten=`, `tuoi=`, `lop=` khi gọi.

**Thuật toán:**
1. Định nghĩa hàm 3 tham số.
2. Gọi với keyword arguments thứ tự trộn lẫn.

**Code:**

```python
def ghi_ho_so(ten, tuoi, lop):
    """In thông tin hồ sơ học sinh."""
    print(f"Ten: {ten} | Tuoi: {tuoi} | Lop: {lop}")

ghi_ho_so(lop="10A1", ten="Mai", tuoi=15)
```

**Giải thích code:**
* Thứ tự đối số không quan trọng khi đã ghi rõ tên tham số.
* Python khớp `lop="10A1"` vào tham số `lop` dù nó đứng đầu.

**Độ phức tạp:** O(1).

---

### Bài 13: Hàm cộng nhiều số bằng `*args`

**Phân tích:** Số lượng đối số không cố định — dùng `*args`.

**Ý tưởng:** `*cac_so` gói mọi đối số thành tuple, `sum()` tính tổng.

**Thuật toán:**
1. Định nghĩa `tinh_tong(*cac_so)`.
2. Trả về `sum(cac_so)`.
3. Gọi với 3 và 4 đối số.

**Code:**

```python
def tinh_tong(*cac_so):
    """Tính tổng một danh sách số bất kỳ."""
    return sum(cac_so)

print(tinh_tong(1, 2, 3))
print(tinh_tong(10, 20, 30, 40))
```

**Giải thích code:**
* `*cac_so` → `(1, 2, 3)` là một tuple.
* `sum()` cộng toàn bộ phần tử trong tuple.

**Độ phức tạp:** O(n) với n là số lượng đối số.

---

### Bài 14: Menu máy tính bằng hàm

**Phân tích:** Kết hợp hàm hiển thị menu và hàm thực hiện phép tính.

**Ý tưởng:** `may_tinh` kiểm tra chuỗi `phep_tinh` rồi gọi phép toán tương ứng.

**Thuật toán:**
1. `hien_menu()` in 4 dòng lựa chọn.
2. `may_tinh(a, b, phep_tinh)`:
   - `"1"` → `a + b`
   - `"2"` → `a - b`
   - `"3"` → `a * b`
   - `"4"` → chia, kiểm tra `b == 0`.

**Code:**

```python
def hien_menu():
    """Hiển thị menu máy tính."""
    print("1. Cong | 2. Tru | 3. Nhan | 4. Chia")

def may_tinh(a, b, phep_tinh):
    """Thực hiện phép tính theo lựa chọn."""
    if phep_tinh == "1":
        return a + b
    elif phep_tinh == "2":
        return a - b
    elif phep_tinh == "3":
        return a * b
    elif phep_tinh == "4":
        if b == 0:
            return "Khong the chia cho 0!"
        return a / b
    return "Lua chon khong hop le!"

hien_menu()
print(may_tinh(10, 2, "4"))
print(may_tinh(8, 0, "4"))
```

**Giải thích code:**
* So sánh chuỗi vì `input()` luôn trả về chuỗi — trong bài này gọi trực tiếp với `"4"`.
* Nhánh chia kiểm tra `b == 0` để không gây `ZeroDivisionError`.

**Độ phức tạp:** O(1).

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Hàm in ra tên viết tắt

**Phân tích:** Xử lý chuỗi: tách từ, lấy chữ cái đầu, viết hoa, nối lại.

**Ý tưởng:** `split()` tạo danh sách từ; lấy ký tự `[0]` mỗi từ; nối bằng `"".join()`.

**Thuật toán:**
1. Tách họ tên thành danh sách các từ.
2. Lấy ký tự đầu mỗi từ và viết hoa.
3. Nối các ký tự thành chuỗi viết tắt.

**Code:**

```python
def viet_tat(ho_ten):
    """Tạo chuỗi viết tắt từ họ tên."""
    cac_tu = ho_ten.split()
    chu_cai_dau = [tu[0].upper() for tu in cac_tu]
    return "".join(chu_cai_dau)

print(f"Nguyen Van An -> {viet_tat('Nguyen Van An')}")
print(f"Tran Thi Binh -> {viet_tat('Tran Thi Binh')}")
```

**Giải thích code:**
* `"Nguyen Van An".split()` → `["Nguyen", "Van", "An"]`.
* `tu[0]` lấy chữ cái đầu, `.upper()` viết hoa.
* `"".join(...)` nối không có khoảng trắng → `"NVA"`.

**Độ phức tạp:** O(n) với n là độ dài chuỗi.

---

### Bài 16: Hàm kiểm tra số nguyên tố

**Phân tích:** Số nguyên tố chỉ chia hết cho 1 và chính nó.

**Ý tưởng:** Duyệt ước từ 2 đến `n // 2`; nếu có ước → không nguyên tố.

**Thuật toán:**
1. `n <= 1` → `False`.
2. Duyệt `i` từ 2 đến `n // 2` (đủ vì mọi ước > `n/2` đều kèm ước < `n/2`).
3. Nếu `n % i == 0` → `False`.
4. Hết vòng → `True`.

**Code:**

```python
def la_so_nguyen_to(n):
    """Kiểm tra n có phải số nguyên tố không."""
    if n <= 1:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

for so in [2, 9, 17, 1]:
    print(f"{so}: {la_so_nguyen_to(so)}")
```

**Giải thích code:**
* `2`: không chia hết cho số nào trong `range(2, 2)` (rỗng) → `True`.
* `9`: `9 % 3 == 0` → `False`.
* `17`: không có ước → `True`.
* `1`: bị loại ngay vì `n <= 1`.

**Độ phức tạp:** O(n) cho một số `n`.

---

### Bài 17: Hàm gộp nhiều thông tin bằng `**kwargs`

**Phân tích:** `**kwargs` gom các cặp tên–giá trị thành dictionary.

**Ý tưởng:** Duyệt `mon_hoc.items()` để in; trung bình = tổng điểm chia số môn.

**Thuật toán:**
1. In từng cặp môn – điểm.
2. Tính trung bình bằng `sum(...) / len(...)`.
3. Trả về điểm trung bình.

**Code:**

```python
def tong_ket(**mon_hoc):
    """In điểm từng môn và trả về điểm trung bình."""
    for mon, diem in mon_hoc.items():
        print(f"{mon}: {diem}")
    diem_trung_binh = sum(mon_hoc.values()) / len(mon_hoc)
    return diem_trung_binh

dtb = tong_ket(toan=8, van=7, anh=9)
print(f"Diem trung binh: {dtb}")
```

**Giải thích code:**
* `mon_hoc` = `{"toan": 8, "van": 7, "anh": 9}`.
* `sum(...)` = 24, `len(...)` = 3 → trung bình 8.0.

**Độ phức tạp:** O(m) với m là số môn.

---

### Bài 18: Trò chơi đoán số — chia thành hàm

**Phân tích:** Tách chương trình game thành 3 hàm nhỏ, mỗi hàm một nhiệm vụ.

**Ý tưởng:** `choi_game()` quản lý vòng lặp; hai hàm còn lại chỉ xử lý một việc.

**Thuật toán:**
1. `sinh_so_bi_mat()`: `random.randint(1, 100)`.
2. `doan_so(so_bi_mat, so_doan)`: so sánh và trả về chuỗi kết quả.
3. `choi_game()`: vòng `while` tối đa 7 lượt, in kết quả, thoát khi đoán đúng.

**Code:**

```python
import random

def sinh_so_bi_mat():
    """Tạo số bí mật ngẫu nhiên từ 1 đến 100."""
    return random.randint(1, 100)

def doan_so(so_bi_mat, so_doan):
    """So sánh số đoán với số bí mật."""
    if so_doan > so_bi_mat:
        return "so bi mat nho hon"
    elif so_doan < so_bi_mat:
        return "so bi mat lon hon"
    return "chinh xac! Xin chuc mung!"

def choi_game():
    """Điều khiển toàn bộ trò chơi đoán số."""
    so_bi_mat = sinh_so_bi_mat()
    luot = 0
    while luot < 7:
        so_doan = int(input("Ban doan so: "))  # Nhập: 50, 25, 40 ...
        luot += 1
        ket_qua = doan_so(so_bi_mat, so_doan)
        print(f"Ban doan so {so_doan}: {ket_qua}")
        if ket_qua == "chinh xac! Xin chuc mung!":
            return
    print("Het luot! So bi mat la", so_bi_mat)

choi_game()
```

**Giải thích code:**
* Với số bí mật là `40` và lần đoán `50, 25, 40`:
  - `50 > 40` → "so bi mat nho hon".
  - `25 < 40` → "so bi mat lon hon".
  - `40 == 40` → chính xác, kết thúc.
* `input()` dùng vì đây là game tương tác thật — khi chạy thử hãy nhập lần lượt các số.

**Độ phức tạp:** O(1) cho mỗi lượt đoán; tối đa 7 lượt.

---

### Bài 19: Tiền lương nhân viên

**Phân tích:** Tính lương có giờ tăng ca gấp rưỡi.

**Ý tưởng:** Tách phần tính lương và phần in ra; công thức tăng ca ×1.5.

**Thuật toán:**
1. `tinh_luong(so_gio, luong_mot_gio=20000)`:
   - Nếu `so_gio <= 40`: `so_gio * luong_mot_gio`.
   - Ngược lại: `40 * luong_mot_gio + (so_gio - 40) * luong_mot_gio * 1.5`.
2. `in_phieu_luong(ten, so_gio)` in kết quả.

**Code:**

```python
def tinh_luong(so_gio, luong_mot_gio=20000):
    """Tính lương, giờ vượt 40 được tính gấp rưỡi."""
    if so_gio <= 40:
        return so_gio * luong_mot_gio
    gio_vuot = so_gio - 40
    return 40 * luong_mot_gio + gio_vuot * luong_mot_gio * 1.5

def in_phieu_luong(ten, so_gio):
    """In phiếu lương của nhân viên."""
    tien = tinh_luong(so_gio)
    print(f"{ten} lam {so_gio} gio -> {int(tien)} dong")

in_phieu_luong("An", 45)
in_phieu_luong("Binh", 30)
```

**Giải thích code:**
* An 45 giờ: `40*20000 + 5*20000*1.5 = 800000 + 150000 = 950000`.
* Bình 30 giờ: `30 * 20000 = 600000`.
* `int(tien)` bỏ phần `.0` cho hiển thị gọn (vì phép nhân với `1.5` cho float).

**Độ phức tạp:** O(1).

---

### Bài 20: Quản lý menu quán phở — tổng hợp hàm

**Phân tích:** Tổng hợp đầy đủ kiến thức: dictionary, tham số mặc định, vòng lặp trong hàm, tích lũy tổng.

**Ý tưởng:** Mỗi nhiệm vụ một hàm; `in_hoa_don` duyệt danh sách đơn hàng.

**Thuật toán:**
1. `gia_mon()` trả về dictionary giá.
2. `thanh_tien(mon, so_luong, phu_thu=0)` = giá × số lượng + phụ thu.
3. `in_hoa_don(don_hang)`: duyệt từng `(mon, sl)`, cộng dồn tổng, in ra.

**Code:**

```python
def gia_mon():
    """Trả về bảng giá các món."""
    return {"pho": 35000, "bun bo": 40000, "com": 25000}

def thanh_tien(mon, so_luong, phu_thu=0):
    """Tính tiền cho một món đã chọn."""
    return gia_mon()[mon] * so_luong + phu_thu

def in_hoa_don(don_hang):
    """In hóa đơn chi tiết cho danh sách món đã đặt."""
    tong = 0
    for mon, so_luong in don_hang:
        tien_mon = thanh_tien(mon, so_luong)
        tong += tien_mon
        print(f"{mon} x{so_luong} = {tien_mon} dong")
    print(f"Tong: {tong} dong")

don = [("pho", 2), ("com", 1)]
in_hoa_don(don)
```

**Giải thích code:**
* `don_hang` là danh sách các tuple `(tên món, số lượng)`.
* `pho x2 = 35000 * 2 = 70000`; `com x1 = 25000`.
* Biến `tong` cộng dồn qua từng vòng lặp, in ra `95000`.

**Độ phức tạp:** O(m) với m là số món trong hóa đơn.

---

## 📌 Lời khuyên cuối

* **Viết hàm nhỏ, mỗi hàm một việc** — chương trình dễ đọc, dễ sửa.
* **Tính toán thì `return`, hiển thị thì `print`** — đừng trộn lẫn.
* **Đặt tên hàm có nghĩa** bằng tiếng Việt không dấu hoặc tiếng Anh đơn giản.
* Nhớ **gọi hàm** — định nghĩa mà không gọi thì chương trình im lặng.

👉 Tiếp theo: **[Bài 13: Phạm Vi Biến](../13_Scope/bai_giang.md)**
