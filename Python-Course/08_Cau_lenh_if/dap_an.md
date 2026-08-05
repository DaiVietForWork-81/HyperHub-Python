# ✅ Bài 8: Đáp Án – Câu Lệnh If (Cấu Trúc Rẽ Nhánh)

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án để việc học hiệu quả nhất.
>
> 📌 Khi chạy thử, hãy nhập đúng giá trị mẫu ở dòng chú thích `# Nhập: ...`.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Chẵn hay lẻ?

**Phân tích:** Số chẵn chia hết cho 2 — phần dư khi chia cho 2 bằng 0.

**Ý tưởng:** Dùng `so % 2 == 0` làm điều kiện cho `if - else`.

**Thuật toán:**
1. Nhập số nguyên.
2. Nếu `so % 2 == 0` → in `Chan`, ngược lại in `Le`.

**Code:**

```python
# Nhập: 42
# Nhập số nguyên cần kiểm tra
so = int(input("Nhập một số nguyên: "))
# Số chẵn khi phần dư chia cho 2 bằng 0
if so % 2 == 0:
    print("Chan")
else:
    print("Le")
```

**Giải thích code:**
* `so % 2` cho phần dư: 0 (chẵn) hoặc 1 (lẻ).
* `so % 2 == 0` — biểu thức so sánh trả về `True`/`False` điều khiển nhánh rẽ.
* `42 % 2 = 0` → điều kiện đúng → in `Chan`.

**Độ phức tạp:** O(1).

---

### Bài 2: Số dương hay số âm?

**Phân tích:** Ba trường hợp: lớn hơn 0, nhỏ hơn 0, bằng 0.

**Ý tưởng:** Xét dương/âm bằng `if - elif`, trường hợp còn lại (bằng 0) nằm trong `else`.

**Thuật toán:**
1. Nhập số thực.
2. Nếu `x > 0` → in `So duong`.
3. Ngược lại nếu `x < 0` → in `So am`.
4. Ngược lại (bằng 0) → in `So khong`.

**Code:**

```python
# Nhập: -3.5
# Nhập số cần phân loại
x = float(input("Nhập một số: "))
if x > 0:
    print("So duong")
elif x < 0:
    print("So am")
else:
    print("So khong")
```

**Giải thích code:**
* `-3.5 > 0` sai → chuyển sang `elif x < 0` → `-3.5 < 0` đúng → in `So am`.
* `else` chỉ nhận các giá trị còn lại — chính là số 0.
* Thứ tự dương → âm → không quan trọng ở bài này vì ba trường hợp rời nhau.

**Độ phức tạp:** O(1).

---

### Bài 3: Kiểm tra tuổi xem phim

**Phân tích:** Hai trường hợp ngược nhau: đủ 18 tuổi và chưa đủ.

**Ý tưởng:** `if - else` với điều kiện `tuoi >= 18`.

**Thuật toán:**
1. Nhập tuổi (số nguyên).
2. Nếu `tuoi >= 18` → in câu thứ nhất, ngược lại in câu thứ hai.

**Code:**

```python
# Nhập: 16
# Nhập tuổi người xem
tuoi = int(input("Nhập tuổi: "))
if tuoi >= 18:
    print("Duoc xem phim nguoi lon")
else:
    print("Can nguoi lon di kem")
```

**Giải thích code:**
* `16 >= 18` sai → chạy nhánh `else`.
* Mỗi lần chạy chỉ **một** nhánh được chọn — không bao giờ cả hai.

**Độ phức tạp:** O(1).

---

### Bài 4: Đậu hay rớt?

**Phân tích:** Điểm từ 5 trở lên là đậu — điểm có thể là số thập phân.

**Ý tưởng:** Ép `float` cho điểm, so sánh với 5.

**Thuật toán:**
1. Nhập điểm dạng số thực.
2. Nếu `diem >= 5` → `Dau`, ngược lại → `Rot`.

**Code:**

```python
# Nhập: 4.5
# Nhập điểm trung bình
diem = float(input("Nhập điểm: "))
if diem >= 5:
    print("Dau")
else:
    print("Rot")
```

**Giải thích code:**
* Dùng `float` vì điểm như `4.5`, `7.25` rất phổ biến.
* `4.5 >= 5` sai → in `Rot`.

**Độ phức tạp:** O(1).

---

### Bài 5: Số nào lớn hơn?

**Phân tích:** So sánh hai số `a` và `b`, in kết quả theo từng trường hợp.

**Ý tưởng:** `if a > b`; trường hợp còn lại là `a <= b`.

**Thuật toán:**
1. Nhập `a`, `b`.
2. Nếu `a > b` → in `a lon hon b`, ngược lại in `b lon hon hoac bang a`.

**Code:**

```python
# Nhập: 10, 3
# Nhập hai số nguyên
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
if a > b:
    print("a lon hon b")
else:
    print("b lon hon hoac bang a")
```

**Giải thích code:**
* `10 > 3` đúng → in nhánh `if`.
* Vì đề bài chỉ hỏi `a > b` hay không, nhánh `else` đại diện toàn bộ trường hợp còn lại (`a <= b`).

**Độ phức tạp:** O(1).

---

### Bài 6: Số chia hết cho 3?

**Phân tích:** Kiểm tra tính chia hết bằng phép `%`.

**Ý tưởng:** Điều kiện `so % 3 == 0`.

**Thuật toán:**
1. Nhập số nguyên.
2. Nếu `so % 3 == 0` → in `Chia het cho 3`, ngược lại in `Khong chia het cho 3`.

**Code:**

```python
# Nhập: 15
# Nhập số cần kiểm tra
so = int(input("Nhập một số: "))
if so % 3 == 0:
    print("Chia het cho 3")
else:
    print("Khong chia het cho 3")
```

**Giải thích code:**
* `15 % 3 = 0` → điều kiện `0 == 0` đúng → in `Chia het cho 3`.
* Mẫu câu này dùng được cho mọi ước số: đổi `3` thành `5`, `7`...

**Độ phức tạp:** O(1).

---

### Bài 7: Chào theo buổi

**Phân tích:** Dựa vào giờ (0–23) quyết định câu chào.

**Ý tưởng:** `gio < 12` là buổi sáng, còn lại là buổi chiều.

**Thuật toán:**
1. Nhập giờ (số nguyên).
2. Nếu `gio < 12` → `Chao buoi sang`, ngược lại → `Chao buoi chieu`.

**Code:**

```python
# Nhập: 9
# Nhập giờ hiện tại
gio = int(input("Nhập giờ: "))
if gio < 12:
    print("Chao buoi sang")
else:
    print("Chao buoi chieu")
```

**Giải thích code:**
* `9 < 12` đúng → in `Chao buoi sang`.
* Nếu muốn thêm buổi tối, thêm `elif gio >= 18` — bài 9 sẽ là nơi thử điều đó với `match`.

**Độ phức tạp:** O(1).

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Số lớn nhất trong ba số

**Phân tích:** Tìm số lớn nhất giữa `a`, `b`, `c` bằng so sánh, không dùng hàm `max()`.

**Ý tưởng:** `a` lớn nhất khi `a >= b and a >= c`; tương tự cho `b`, `c`; trường hợp còn lại thì `c` lớn nhất.

**Thuật toán:**
1. Nhập `a`, `b`, `c` dạng số thực.
2. Nếu `a >= b and a >= c` → in `a`.
3. Ngược lại nếu `b >= a and b >= c` → in `b`.
4. Ngược lại → in `c`.

**Code:**

```python
# Nhập: 5, 9.5, 3
# Nhập ba số thực
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
# a lớn nhất khi lớn hơn hoặc bằng cả b và c
if a >= b and a >= c:
    print(a)
# b lớn nhất khi lớn hơn hoặc bằng cả a và c
elif b >= a and b >= c:
    print(b)
# trường hợp còn lại c chính là số lớn nhất
else:
    print(c)
```

**Giải thích code:**
* `and` kết hợp hai điều kiện: `a >= b` **và** `a >= c`.
* Nếu `a` và `b` bằng nhau và đều lớn nhất, nhánh `a` được chọn trước — kết quả vẫn đúng (in `a`).
* Với `5, 9.5, 3`: nhánh `a` sai, nhánh `b` đúng → in `9.5`.

**Độ phức tạp:** O(1).

---

### Bài 9: Xếp loại điểm 4 mức

**Phân tích:** Bốn mức theo thang điểm 8 / 6.5 / 5.

**Ý tưởng:** Xét **từ cao xuống thấp** — nhánh nào đúng trước thì thắng.

**Thuật toán:**
1. Nhập điểm (float).
2. Nếu `>= 8` → `Gioi`; `elif >= 6.5` → `Kha`; `elif >= 5` → `Trung binh`; còn lại → `Yeu`.
3. In kết quả.

**Code:**

```python
# Nhập: 7.2
# Nhập điểm trung bình
diem = float(input("Nhập điểm: "))
# Xét từ cao xuống thấp - nhánh đầu tiên đúng sẽ được chọn
if diem >= 8:
    loai = "Gioi"
elif diem >= 6.5:
    loai = "Kha"
elif diem >= 5:
    loai = "Trung binh"
else:
    loai = "Yeu"
print(loai)
```

**Giải thích code:**
* `7.2 >= 8` sai → `7.2 >= 6.5` đúng → `Kha`.
* Lọt tới `elif diem >= 6.5` nghĩa là `diem < 8` — không cần viết lại điều kiện này.
* Nếu đảo thứ tự (để `>= 5` lên trước) thì mọi điểm đều ra `Trung binh` — sai ngầm khó phát hiện.

**Độ phức tạp:** O(1).

---

### Bài 10: Tiền điện bậc thang

**Phân tích:** 65 kWh thuộc bậc 2 (51–100) → đơn giá 2500đ → 162.500đ.

**Ý tưởng:** Xác định `don_gia` theo bậc rồi nhân với số kWh.

**Thuật toán:**
1. Nhập số kWh (float).
2. Nếu `<= 50` → giá 2000; `elif <= 100` → 2500; còn lại → 3000.
3. Tính và in tiền.

**Code:**

```python
# Nhập: 65
# Nhập số kWh tiêu thụ
kwh = float(input("Nhập số điện tiêu thụ (kWh): "))
# Xác định đơn giá theo bậc
if kwh <= 50:
    don_gia = 2000      # bậc 1: 0 - 50 kWh
elif kwh <= 100:
    don_gia = 2500      # bậc 2: 51 - 100 kWh
else:
    don_gia = 3000      # bậc 3: trên 100 kWh
# Số tiền phải trả
tien = kwh * don_gia
print(f"So tien phai tra la: {tien} VND")
```

**Giải thích code:**
* `65 <= 50` sai → `65 <= 100` đúng → `don_gia = 2500`.
* `65 * 2500 = 162500.0` — kết quả số thực vì `kwh` là `float`.
* Đây là bảng giá **đơn giản** (toàn bộ số kWh tính cùng giá); bảng giá lũy tiến từng phần sẽ khó hơn, chờ vòng lặp ở bài 10–11.

**Độ phức tạp:** O(1).

---

### Bài 11: Năm nhuận

**Phân tích:** Năm nhuận: chia hết cho 4, không chia hết cho 100, trừ khi chia hết cho 400.

**Ý tưởng:** Dùng đúng biểu thức từ bài 6: `nam % 4 == 0 and (nam % 100 != 0 or nam % 400 == 0)`.

**Thuật toán:**
1. Nhập năm (int).
2. Kiểm tra biểu thức năm nhuận.
3. In kết quả tương ứng.

**Code:**

```python
# Nhập: 2024
# Nhập năm cần kiểm tra
nam = int(input("Nhập năm: "))
# Quy tắc năm nhuận
if nam % 4 == 0 and (nam % 100 != 0 or nam % 400 == 0):
    print("Nam nhuan")
else:
    print("Khong phai nam nhuan")
```

**Giải thích code:**
* 2024: `2024 % 4 == 0` (True) `and` `2024 % 100 != 0` (True) → `True` → năm nhuận.
* 1900: chia hết cho 4 và 100 nhưng không chia hết cho 400 → không nhuận — biểu thức xử lý đúng quy tắc "trừ khi".
* 2000: chia hết cho 400 → nhánh `or` đúng → nhuận.

**Độ phức tạp:** O(1).

---

### Bài 12: Máy ATM rút tiền

**Phân tích:** Kiểm tra số tiền rút có vượt quá số dư không trước khi trừ.

**Ý tưởng:** `if so_rut <= so_du` → trừ và in kết quả; ngược lại báo lỗi.

**Thuật toán:**
1. Khởi tạo `so_du = 1000000`.
2. Nhập số tiền rút.
3. Nếu đủ tiền → trừ, in số dư mới; ngược lại in thông báo.

**Code:**

```python
# Nhập: 500000
# Số dư khởi tạo
so_du = 1000000
# Nhập số tiền muốn rút
so_rut = float(input("Nhập số tiền muốn rút: "))
# Kiểm tra số dư đủ hay không
if so_rut <= so_du:
    so_du -= so_rut          # trừ tiền vào số dư
    print(f"Rut thanh cong. So du con lai: {so_du} VND")
else:
    print("So du khong du!")
```

**Giải thích code:**
* `500000 <= 1000000` đúng → thực hiện rút: `so_du = 1000000 - 500000 = 500000.0`.
* `so_du -= so_rut` là toán tử gán kết hợp của bài 6 — ngắn gọn cho "cập nhật số dư".
* Nếu nhập `2000000`, điều kiện sai → không trừ tiền, in `So du khong du!`.

**Độ phức tạp:** O(1).

---

### Bài 13: Phân loại tam giác

**Phân tích:** Phân biệt tam giác đều (3 cạnh bằng), cân (2 cạnh bằng), thường.

**Ý tưởng:** Kiểm tra đều trước (điều kiện hẹp nhất), rồi cân, còn lại là thường.

**Thuật toán:**
1. Nhập ba cạnh.
2. Nếu `a == b and b == c` → đều.
3. Ngược lại nếu có hai cạnh bằng → cân.
4. Ngược lại → thường.

**Code:**

```python
# Nhập: 5, 5, 3
# Nhập ba cạnh của tam giác
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
# Tam giác đều: cả ba cạnh bằng nhau (kiểm tra trước)
if a == b and b == c:
    print("Tam giac deu")
# Tam giác cân: ít nhất hai cạnh bằng nhau
elif a == b or b == c or a == c:
    print("Tam giac can")
else:
    print("Tam giac thuong")
```

**Giải thích code:**
* `5 == 5 and 5 == 3` sai (vế sau) → chuyển `elif`.
* `a == b` đúng → in `Tam giac can`.
* Quan trọng: kiểm tra **đều trước** — nếu để nhánh cân trước, tam giác đều cũng rơi vào nhánh cân, kết quả sai.

**Độ phức tạp:** O(1).

---

### Bài 14: Tiền vé tham quan

**Phân tích:** Bốn nhóm tuổi với bốn mức giá, xét từ trẻ nhất.

**Ý tưởng:** Xét `tuoi < 6` → 0đ; `tuoi <= 12` → 20.000đ; `tuoi <= 17` → 40.000đ; còn lại 60.000đ.

**Thuật toán:**
1. Nhập tuổi (int).
2. Xét lần lượt các khoảng tuổi.
3. In tiền vé.

**Code:**

```python
# Nhập: 14
# Nhập tuổi khách
tuoi = int(input("Nhập tuổi: "))
# Xét các mức giá từ thấp tuổi nhất
if tuoi < 6:
    tien_ve = 0          # trẻ em dưới 6 tuổi miễn phí
elif tuoi <= 12:
    tien_ve = 20000      # 6 - 12 tuổi
elif tuoi <= 17:
    tien_ve = 40000      # 13 - 17 tuổi
else:
    tien_ve = 60000      # từ 18 tuổi
print(f"Tien ve: {tien_ve} VND")
```

**Giải thích code:**
* Lọt tới `elif tuoi <= 12` nghĩa là `tuoi >= 6` — không cần ghi lại chặn dưới.
* `14`: không < 6, không <= 12, `14 <= 17` đúng → `40000`.
* Mô hình "bảng giá theo tuổi" này dùng được cho vé máy bay, vé tàu, vé khu vui chơi...

**Độ phức tạp:** O(1).

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Xếp loại học lực 5 mức + kiểm tra điểm hợp lệ

**Phân tích:** Vừa kiểm tra dữ liệu hợp lệ (0–10), vừa xếp loại 5 mức theo PDF. (Thử thêm với `15` để xem nhánh báo lỗi.)

**Ý tưởng:** Chặn điểm rác trước bằng `or`; nếu hợp lệ mới xếp loại từ 9 → 8 → 6.5 → 5.

**Thuật toán:**
1. Nhập điểm (float).
2. Nếu điểm ngoài 0–10 → báo `Diem khong hop le`.
3. Ngược lại: xếp loại theo thang 9 / 8 / 6.5 / 5.
4. In xếp loại.

**Code:**

```python
# Nhập: 8.4
# Nhập điểm trung bình
diem = float(input("Nhập điểm trung bình (0 - 10): "))
# Bước 1: kiểm tra điểm có hợp lệ không
if diem < 0 or diem > 10:
    print("Diem khong hop le")
else:
    # Bước 2: điểm hợp lệ mới xếp loại (từ cao xuống thấp)
    if diem >= 9:
        loai = "Xuat sac"
    elif diem >= 8:
        loai = "Gioi"
    elif diem >= 6.5:
        loai = "Kha"
    elif diem >= 5:
        loai = "Trung binh"
    else:
        loai = "Yeu"
    print(loai)
```

**Giải thích code:**
* `8.4 < 0 or 8.4 > 10` đều sai → vào `else`; `8.4 >= 9` sai, `8.4 >= 8` đúng → `Gioi`.
* `15 > 10` đúng → in `Diem khong hop le`, không rơi vào xếp loại.
* Chú ý thứ tự: `>= 8` đứng trước `>= 6.5` để 8.4 không bị xếp nhầm thành `Kha`.

**Độ phức tạp:** O(1).

---

### Bài 16: Máy tính bốn phép tính

**Phân tích:** Điều khiển 4 phép toán bằng mã lựa chọn; phép chia cần xử lý thêm trường hợp `b = 0`.

**Ý tưởng:** `if - elif - else` cho lựa chọn; `if` lồng bên trong nhánh chia để kiểm tra mẫu số.

**Thuật toán:**
1. Nhập `a`, `b`, lựa chọn.
2. Nhánh 1: cộng; nhánh 2: trừ; nhánh 3: nhân; nhánh 4: chia (kiểm tra `b != 0`); còn lại báo lỗi chọn.

**Code:**

```python
# Nhập: 10, 3, 4
# Nhập hai số và lựa chọn phép tính
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
lua_chon = int(input("Chọn phép tính (1 cộng, 2 trừ, 3 nhân, 4 chia): "))

if lua_chon == 1:
    print(f"Ket qua: {a + b}")
elif lua_chon == 2:
    print(f"Ket qua: {a - b}")
elif lua_chon == 3:
    print(f"Ket qua: {a * b}")
elif lua_chon == 4:
    # if lồng: kiểm tra mẫu số trước khi chia
    if b != 0:
        print(f"Ket qua: {a / b}")
    else:
        print("Khong the chia cho 0")
else:
    print("Lua chon khong hop le")
```

**Giải thích code:**
* `lua_chon == 4` → nhánh chia; `b != 0` (3) đúng → `10 / 3 = 3.3333333333333335`.
* Nếu nhập `b = 0` và chọn phép chia → nhánh lồng sai → in `Khong the chia cho 0`, không gây lỗi chương trình.
* Nếu lựa chọn không nằm trong 1–4, `else` cuối cùng báo lỗi — mô hình này giống đúng menu của máy ATM.

**Độ phức tạp:** O(1).

---

### Bài 17: Số ngày trong tháng

**Phân tích:** Tháng 2 phụ thuộc năm nhuận; tháng 4, 6, 9, 11 có 30 ngày; còn lại 31 ngày.

**Ý tưởng:** Xét `thang == 2` với `if` lồng kiểm tra nhuận; nhóm tháng 30 ngày bằng `or`.

**Thuật toán:**
1. Nhập tháng, năm.
2. Nếu tháng ngoài 1–12 → báo lỗi.
3. Nếu tháng 2 → kiểm tra nhuận: 29 hoặc 28 ngày.
4. Ngược lại nếu tháng thuộc nhóm 30 ngày → 30.
5. Còn lại → 31.
6. In kết quả.

**Code:**

```python
# Nhập: 2, 2024
# Nhập tháng và năm
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

# Tháng phải nằm trong khoảng 1 - 12
if thang < 1 or thang > 12:
    print("Thang khong hop le")
elif thang == 2:
    # Kiểm tra năm nhuận cho riêng tháng 2
    if nam % 4 == 0 and (nam % 100 != 0 or nam % 400 == 0):
        so_ngay = 29
    else:
        so_ngay = 28
    print(f"Thang {thang}/{nam} có {so_ngay} ngày")
elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
    print(f"Thang {thang}/{nam} có 30 ngày")
else:
    print(f"Thang {thang}/{nam} có 31 ngày")
```

**Giải thích code:**
* 2024 nhuận → `so_ngay = 29` — `if` lồng chỉ xét khi đã chắc chắn tháng 2.
* Nhóm `thang == 4 or 6 or 9 or 11` gộp bốn tháng 30 ngày vào một nhánh.
* Thứ tự quan trọng: kiểm tra tháng hợp lệ trước khi tính ngày.

**Độ phức tạp:** O(1).

---

### Bài 18: Tiền nước sinh hoạt (bậc thang + thuế)

**Phân tích:** 25 m³ thuộc bậc 21–30 (10000đ/m³) → tiền 250.000đ; cộng 10% VAT → 275.000đ.

**Ý tưởng:** Bốn bậc đơn giá bằng `if - elif - else`, nhân với m³, cộng thuế 10%.

**Thuật toán:**
1. Nhập số m³.
2. Xác định đơn giá theo bậc.
3. Tính tiền nước = m³ × đơn giá.
4. Cộng thuế 10% → in tổng.

**Code:**

```python
# Nhập: 25
# Nhập số mét khối nước tiêu thụ
m3 = float(input("Nhập số m3 nước tiêu thụ: "))
# Xác định đơn giá theo bậc
if m3 <= 10:
    don_gia = 6000       # bậc 1: 0 - 10 m3
elif m3 <= 20:
    don_gia = 8000       # bậc 2: 11 - 20 m3
elif m3 <= 30:
    don_gia = 10000      # bậc 3: 21 - 30 m3
else:
    don_gia = 12000      # bậc 4: trên 30 m3
# Tiền nước chưa thuế
tien_nuoc = m3 * don_gia
# Cộng thuế VAT 10%
tong_tien = tien_nuoc + tien_nuoc * 0.1
# In kết quả 2 chữ số thập phân
print(f"Tong tien nuoc: {tong_tien:.2f} VND")
```

**Giải thích code:**
* `25 <= 20` sai → `25 <= 30` đúng → `don_gia = 10000`.
* `25 * 10000 = 250000`; thuế `250000 * 0.1 = 25000`; tổng `275000.00`.
* `{:.2f}` đảm bảo hiển thị đúng định dạng tiền tệ như hóa đơn.

**Độ phức tạp:** O(1).

---

### Bài 19: Điểm trung bình có trọng số + xếp loại

**Phân tích:** Vừa tính trung bình theo hệ số (bài 7), vừa xếp loại 5 mức (bài này).

**Ý tưởng:** Tính `tb` trước, rồi `if - elif - else` xếp loại theo 8.5 / 7 / 5.5 / 4.

**Thuật toán:**
1. Nhập ba môn.
2. Tính `tb = (toan*2 + van + anh) / 4`.
3. Xếp loại từ cao xuống thấp.
4. In trung bình và loại.

**Code:**

```python
# Nhập: 8, 6, 9
# Nhập điểm ba môn
diem_toan = float(input("Nhập điểm Toán: "))
diem_van = float(input("Nhập điểm Văn: "))
diem_anh = float(input("Nhập điểm Anh: "))
# Điểm trung bình (Toán hệ số 2)
tb = (diem_toan * 2 + diem_van + diem_anh) / 4
# Xếp loại từ cao xuống thấp
if tb >= 8.5:
    loai = "Xuat sac"
elif tb >= 7:
    loai = "Gioi"
elif tb >= 5.5:
    loai = "Kha"
elif tb >= 4:
    loai = "Trung binh"
else:
    loai = "Yeu"
# In kết quả
print(f"Diem trung binh: {tb:.2f}")
print(f"Xep loai: {loai}")
```

**Giải thích code:**
* `(8*2 + 6 + 9) / 4 = 31 / 4 = 7.75` → in `7.75`.
* `7.75 >= 8.5` sai, `7.75 >= 7` đúng → `Gioi`.
* Cấu trúc "tính trước, phân loại sau" rất điển hình trong các ứng dụng quản lý điểm.

**Độ phức tạp:** O(1).

---

### Bài 20: Trò chơi đoán số bí mật

**Phân tích:** So khớp dự đoán với số bí mật 7: đúng / lớn hơn / nhỏ hơn.

**Ý tưởng:** Kiểm tra bằng trước; hai nhánh còn lại dùng `elif` rõ ràng cho cả hai chiều.

**Thuật toán:**
1. Nhập số dự đoán.
2. Nếu bằng 7 → chúc mừng.
3. Ngược lại nếu lớn hơn → gợi ý lớn hơn.
4. Ngược lại (nhỏ hơn) → gợi ý nhỏ hơn.

**Code:**

```python
# Nhập: 9
# Số bí mật do chương trình giữ
bi_mat = 7
# Nhập dự đoán của người chơi
n = int(input("Đoán con số bí mật (1 - 10): "))
# So sánh dự đoán với số bí mật
if n == bi_mat:
    print("Chuc mung! Ban da doan dung.")
elif n > bi_mat:
    print("So ban nhap lon hon dap an. Thu lai nhe!")
else:
    print("So ban nhap nho hon dap an. Thu lai nhe!")
```

**Giải thích code:**
* `9 == 7` sai → `9 > 7` đúng → in câu gợi ý "lớn hơn".
* Nếu `n < 7`, cả hai nhánh trước đều sai → `else` in gợi ý "nhỏ hơn".
* Khi học vòng lặp (bài 10, 11), thêm `while` quanh khối này là bạn có một trò chơi chơi được nhiều lượt — đây là khởi đầu của một mini game thực thụ!

**Độ phức tạp:** O(1).

---

## 📌 Lời khuyên cuối

* 🧠 **Đọc yêu cầu theo công thức:** "Nếu A → làm X, còn lại → làm Y" chính là `if - else`; "nhiều mức A, B, C" chính là `if - elif - else`.
* 📏 **Thứ tự `elif` từ chặt đến rộng** — sai thứ tự là sai kết quả dù code chạy trơn tru.
* 🛡️ **Luôn kiểm tra dữ liệu đầu vào** (điểm 0–10, tiền rút ≤ số dư, mẫu số ≠ 0) trước khi xử lý.
* 🧪 **Thử các giá trị biên:** 49/50/51 kWh, 7.99/8.0 điểm, năm 1900/2000 — đây là nơi các lỗi ẩn nấp.
* 🚦 `if` là nền tảng của mọi thuật toán ra quyết định — bài sau sẽ giới thiệu `match - case`, bản "nâng cấp" gọn gàng khi cần so khớp nhiều giá trị cố định.

👉 Tiếp theo: **[Bài 9: Match Case – Cấu Trúc Phân Rẽ Mẫu](../09_Match_case/bai_giang.md)**