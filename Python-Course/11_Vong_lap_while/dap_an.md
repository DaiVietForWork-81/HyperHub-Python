# ✅ Bài 11: Đáp Án – Vòng Lặp While

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án để việc học hiệu quả nhất.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Đếm từ 1 đến 10 bằng while

**Phân tích:** Lặp đếm với số lần biết trước nhưng yêu cầu dùng `while` để làm quen "bộ ba".

**Ý tưởng:** Khởi tạo `i = 1`; kiểm tra `i <= 10`; cập nhật `i = i + 1`.

**Thuật toán:**
1. `i = 1`.
2. Trong khi `i <= 10`: in i, tăng i lên 1.

**Code:**

```python
# Khởi tạo biến đếm
i = 1

# Lặp khi điều kiện còn đúng
while i <= 10:
    print(i)
    i = i + 1   # Cập nhật — thiếu dòng này là vô hạn!
```

**Giải thích code:**
* `i = 1` — khởi tạo trước vòng lặp.
* `while i <= 10:` — kiểm tra trước mỗi lượt.
* `i = i + 1` — biến đếm tiến dần về 11 → điều kiện sai → dừng.

**Độ phức tạp:** O(n).

---

### Bài 2: Đếm ngược từ 10 về 1

**Phân tích:** Đếm lùi — cập nhật bằng phép trừ.

**Ý tưởng:** Khởi tạo 10, điều kiện `>= 1`, cập nhật trừ 1.

**Thuật toán:**
1. `i = 10`.
2. Trong khi `i >= 1`: in i, giảm i xuống 1.

**Code:**

```python
# Khởi tạo từ 10
i = 10

# Lặp khi i còn lớn hơn hoặc bằng 1
while i >= 1:
    print(i)
    i = i - 1   # Giảm dần — hướng tới điều kiện sai
```

**Giải thích code:**
* Điều kiện `i >= 1` — khi i = 0 thì sai, vòng lặp dừng đúng lúc.
* `i = i - 1` — mỗi lượt giảm 1, ngược với bài 1.

**Độ phức tạp:** O(n).

---

### Bài 3: Tổng 1 đến n bằng while

**Phân tích:** Biến tích lũy (bài 10) kết hợp while.

**Ý tưởng:** `tong = 0`, `i = 1`; cộng dồn rồi tăng i tới khi i > n.

**Thuật toán:**
1. Nhập n.
2. `tong = 0`, `i = 1`.
3. Trong khi `i <= n`: `tong = tong + i`, `i = i + 1`.
4. In tổng.

**Code:**

```python
# Nhập n (ví dụ nhập: 5)
n = int(input("Nhập n: "))

tong = 0
i = 1

# Cộng dồn từ 1 đến n
while i <= n:
    tong = tong + i
    i = i + 1

print(f"Tổng: {tong}")
```

**Giải thích code:**
* Vòng lặp vừa cộng dồn `tong` vừa cập nhật `i` — hai lệnh cập nhật đi kèm nhau.
* Với n = 5: tổng = 1+2+3+4+5 = **15**.

**Độ phức tạp:** O(n).

---

### Bài 4: In "Python" 5 lần bằng while

**Phân tích:** Lặp đúng 5 lần kèm số thứ tự — kiểm tra kỹ năng cập nhật biến đếm.

**Ý tưởng:** `dem` chạy 1..5, in f-string.

**Thuật toán:**
1. `dem = 1`.
2. Trong khi `dem <= 5`: in `Lan {dem}: Python`, tăng dem.

**Code:**

```python
dem = 1

# In đúng 5 lần
while dem <= 5:
    print(f"Lan {dem}: Python")
    dem = dem + 1
```

**Giải thích code:**
* `dem = dem + 1` — đừng quên: thiếu là chương trình in "Lan 1" mãi mãi.
* f-string chèn số thứ tự vào dòng chữ.

**Độ phức tạp:** O(1) — số lần cố định 5.

---

### Bài 5: Các số chẵn từ 2 đến 20

**Phân tích:** Dãy cách quãng — cập nhật bước nhảy 2.

**Ý tưởng:** Khởi tạo 2, cập nhật `i = i + 2`.

**Thuật toán:**
1. `i = 2`.
2. Trong khi `i <= 20`: in i, tăng i thêm 2.

**Code:**

```python
i = 2

# Mỗi lượt tăng 2 → luôn là số chẵn
while i <= 20:
    print(i)
    i = i + 2
```

**Giải thích code:**
* Khởi tạo 2 (chẵn) và bước nhảy 2 (chẵn) → mọi giá trị i đều chẵn.
* In đến 20 rồi i = 22 → dừng.

**Độ phức tạp:** O(n).

---

### Bài 6: Bảng nhân 7 bằng while

**Phân tích:** Giống bài 5 (bài 10) nhưng bằng while.

**Ý tưởng:** i chạy 1..10, in `7 x i = 7*i`.

**Thuật toán:**
1. `i = 1`.
2. Trong khi `i <= 10`: in phép nhân, tăng i.

**Code:**

```python
i = 1

# In bảng nhân 7 từ 1 đến 10
while i <= 10:
    print(f"7 x {i} = {7 * i}")
    i = i + 1
```

**Giải thích code:**
* `7 * i` — Python tính tích ngay trong f-string.
* Sau lượt i = 10, i = 11 → dừng.

**Độ phức tạp:** O(10) → hằng số.

---

### Bài 7: Nhập số dương

**Phân tích:** Kiểm tra đầu vào — "còn sai thì hỏi lại".

**Ý tưởng:** Điều kiện lặp chính là điều kiện "chưa hợp lệ".

**Thuật toán:**
1. `so = 0` (khởi tạo để chắc chắn vào vòng lặp).
2. Trong khi `so <= 0`: nhập số; nếu ≤ 0 báo lỗi.
3. In số đã nhận.

**Code:**

```python
# Khởi tạo giá trị không hợp lệ để vòng lặp chạy ít nhất 1 lần
so = 0

# Còn không hợp lệ thì cứ hỏi lại
while so <= 0:
    so = int(input("Nhập số: "))
    if so <= 0:
        print("So phai lon hon 0!")

print(f"Số đã nhận: {so}")
```

**Giải thích code:**
* `so = 0` — điều kiện `so <= 0` đúng ngay lần đầu → vòng lặp chắc chắn chạy.
* Sau vòng lặp, `so` **chắc chắn** là số dương — phần sau yên tâm xử lý.

**Độ phức tạp:** O(1) trung bình (số lần phụ thuộc người nhập).

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Cộng dồn đến khi nhập 0

**Phân tích:** Số lần lặp không biết trước — `while True` + `break` là lựa chọn chuẩn.

**Ý tưởng:** Nhập liên tục; số 0 là tín hiệu dừng.

**Thuật toán:**
1. `tong = 0`.
2. Vòng lặp: nhập số; nếu 0 → break; ngược lại cộng dồn.
3. In tổng.

**Code:**

```python
tong = 0

# Vòng lặp vô hạn có chủ đích, thoát khi nhập 0
while True:
    so = float(input("Nhập số (0 để dừng): "))
    if so == 0:
        break          # Lối thoát duy nhất
    tong = tong + so

print(f"Tổng: {tong}")
```

**Giải thích code:**
* `while True:` — người dùng quyết định khi nào dừng, chương trình không thể đoán trước.
* `break` nằm trước lệnh cộng dồn — số 0 chỉ làm tín hiệu dừng, không bị cộng vào tổng.
* Ví dụ: 5 + 3 + 0 → tổng **8.0**.

**Độ phức tạp:** O(k) với k là số lượng số nhập vào.

---

### Bài 9: Đếm ngược có hồi chuông

**Phân tích:** Chỉ đếm khi n hợp lệ — `else` của while báo "hết giờ" khi đếm xong thật sự.

**Ý tưởng:** `i = n`; while `i >= 1` đếm lùi; `else` in "Het gio!".

**Thuật toán:**
1. Nhập n.
2. `i = n`.
3. Trong khi `i >= 1`: in i, giảm i.
4. `else`: in "Het gio!" (chỉ khi không bị break).
5. Nếu n ≤ 0: in "So khong hop le!" và không đếm.

**Code:**

```python
# Nhập n (ví dụ nhập: 3)
n = int(input("Nhập n: "))

# Kiểm tra n hợp lệ trước khi đếm
if n <= 0:
    print("So khong hop le!")
else:
    i = n
    # Đếm ngược từ n về 1
    while i >= 1:
        print(i)
        i = i - 1
    else:
        # Chạy khi vòng lặp kết thúc tự nhiên (không break)
        print("Het gio!")
```

**Giải thích code:**
* `while ... else:` — khối `else` chạy khi điều kiện tự sai (i < 1) — đúng lúc in "Het gio!".
* Nếu n ≤ 0, nhánh `else` ngoài cùng báo lỗi, không đếm — "Het gio!" không bị in nhầm.

**Độ phức tạp:** O(n).

---

### Bài 10: Nhập điểm hợp lệ (0–10)

**Phân tích:** Kiểm soát đầu vào rồi mới xử lý — kết hợp while với if-elif (bài 8).

**Ý tưởng:** `while True` hỏi lại tới khi `0 <= diem <= 10`; sau đó xếp loại.

**Thuật toán:**
1. Vòng lặp nhập điểm; hợp lệ thì break.
2. Xếp loại bằng if-elif.
3. In kết quả.

**Code:**

```python
# Nhập điểm cho tới khi hợp lệ (ví dụ nhập: 12 rồi 8.5)
while True:
    diem = float(input("Nhập điểm (0-10): "))
    if 0 <= diem <= 10:
        break          # Điểm hợp lệ → chấp nhận
    print("Điểm không hợp lệ!")

print(f"Điểm đã nhận: {diem}")

# Xếp loại (kiến thức bài 8)
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

print(f"Xếp loại: {loai}")
```

**Giải thích code:**
* `0 <= diem <= 10` — so sánh kép của Python: diem ≥ 0 **và** diem ≤ 10.
* Vòng lặp đảm bảo sau break, `diem` luôn hợp lệ → phần xếp loại không cần kiểm tra lại.
* Điểm 8.5 → "Gioi" — đúng ví dụ.

**Độ phức tạp:** O(1) trung bình.

---

### Bài 11: Đếm chữ số của n

**Phân tích:** Mỗi lượt "bóc" một chữ số bằng `// 10` — vòng lặp tự dừng khi n = 0.

**Ý tưởng:** `dem = 0`; lặp `while n > 0:` — đếm 1, `n = n // 10`.

**Thuật toán:**
1. Nhập n.
2. `dem = 0`.
3. Trong khi `n > 0`: `dem = dem + 1`; `n = n // 10`.
4. In số chữ số.

**Code:**

```python
# Nhập n (ví dụ nhập: 2026)
n = int(input("Nhập n: "))

dem = 0

# Bóc từng chữ số: 2026 → 202 → 20 → 2 → 0
while n > 0:
    dem = dem + 1
    n = n // 10      # Bỏ chữ số cuối

print(f"Số chữ số: {dem}")
```

**Giải thích code:**
* `n // 10` — chia lấy phần nguyên: 2026 // 10 = 202 (bỏ chữ số 6).
* Lượt đi: 2026 (đếm 1) → 202 (2) → 20 (3) → 2 (4) → 0 → dừng → **4 chữ số**.
* Lưu ý: với n = 0 kết quả là 0 — nếu muốn 0 có 1 chữ số, xử lý riêng (thực tế đề bài dùng n dương).

**Độ phức tạp:** O(số chữ số của n) = O(log n).

---

### Bài 12: Tổng các chữ số của n

**Phân tích:** Lấy chữ số cuối bằng `% 10`, bỏ chữ số cuối bằng `// 10`.

**Ý tưởng:** Cộng dồn `n % 10` mỗi lượt.

**Thuật toán:**
1. Nhập n.
2. `tong = 0`.
3. Trong khi `n > 0`: `tong = tong + n % 10`; `n = n // 10`.
4. In tổng.

**Code:**

```python
# Nhập n (ví dụ nhập: 2026)
n = int(input("Nhập n: "))

tong = 0

# Tách từng chữ số và cộng dồn
while n > 0:
    tong = tong + (n % 10)   # Chữ số cuối cùng của n
    n = n // 10              # Bỏ chữ số cuối

print(f"Tổng các chữ số: {tong}")
```

**Giải thích code:**
* `n % 10` — lấy chữ số hàng đơn vị: 2026 % 10 = 6.
* Lượt đi: +6 → +2 → +0 → +2 = **10** — khớp ví dụ 2026 → 10.
* Kỹ thuật "bóc chữ số" (`% 10` lấy, `// 10` bỏ) xuất hiện lại ở bài 13, 16 — ghi nhớ!

**Độ phức tạp:** O(log n).

---

### Bài 13: Đảo ngược số

**Phân tích:** Dựng số mới bằng cách "đẩy" từng chữ số: `so_dao = so_dao * 10 + chu_so`.

**Ý tưởng:** Với mỗi chữ số cuối của n, nhân số đảo đang dựng lên 10 rồi cộng thêm chữ số đó.

**Thuật toán:**
1. Nhập n.
2. `so_dao = 0`.
3. Trong khi `n > 0`: `so_dao = so_dao * 10 + (n % 10)`; `n = n // 10`.
4. In số đảo ngược.

**Code:**

```python
# Nhập n (ví dụ nhập: 2026)
n = int(input("Nhập n: "))

so_dao = 0

# Dựng số đảo ngược từng chữ số một
while n > 0:
    so_dao = so_dao * 10 + (n % 10)   # Đẩy chữ số cuối vào số đảo
    n = n // 10                       # Bỏ chữ số cuối

print(f"Số đảo ngược: {so_dao}")
```

**Giải thích code:**
* Với 2026: so_dao = 0×10+6 = 6 → 6×10+2 = 62 → 62×10+0 = 620 → 620×10+2 = **6202**.
* Số 0 ở đầu kết quả bị "nuốt" tự nhiên (ví dụ 120 → 21) — chấp nhận theo đề bài.
* Phép `* 10 + chữ số` là kỹ thuật trung tâm của bài toán đảo số — cũng dùng ở bài 16.

**Độ phức tạp:** O(log n).

---

### Bài 14: Tìm ước chung lớn nhất

**Phân tích:** Phương pháp trừ liên tiếp: hai số bằng nhau là dừng — số đó chính là ƯCLN.

**Ý tưởng:** `while a != b:` — trừ số lớn cho số nhỏ đến khi bằng nhau.

**Thuật toán:**
1. Nhập a, b.
2. Trong khi `a != b`: nếu a > b → `a = a - b`; ngược lại → `b = b - a`.
3. In a (bằng b).

**Code:**

```python
# Nhập hai số (ví dụ: 12 và 8)
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

# Lưu bản gốc — a, b sẽ bị thay đổi trong vòng lặp
a_goc, b_goc = a, b

# Trừ liên tiếp cho tới khi hai số bằng nhau
while a != b:
    if a > b:
        a = a - b   # Giảm số lớn bên trái
    else:
        b = b - a   # Giảm số lớn bên phải

print(f"ƯCLN({a_goc}, {b_goc}) = {a}")
```

**Giải thích code:**
* 12 vs 8 → a = 4; 4 vs 8 → b = 4; 4 vs 4 → dừng → **ƯCLN = 4**.
* `a_goc, b_goc = a, b` — sao lưu trước khi lặp vì a, b bị đổi; dùng lại để in kết quả đúng dạng `ƯCLN(12, 8) = 4` với mọi cặp số nhập vào.

**Độ phức tạp:** O(a + b) trong trường hợp xấu (phương pháp trừ); nhanh hơn nhiều với số nhỏ.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Game đoán số

**Phân tích:** Số lần đoán không biết trước — tình huống chuẩn của `while True` + `break`.

**Ý tưởng:** Số bí mật cố định 7; mỗi lượt đoán, so sánh và gợi ý; đúng thì break.

**Thuật toán:**
1. `so_bi_mat = 7`, `so_lan = 0`.
2. Vòng lặp: tăng so_lan, nhập dự đoán.
3. Nếu đúng → chúc mừng, break. Nếu nhỏ → gợi ý nhỏ hơn. Ngược lại → lớn hơn.

**Code:**

```python
# Số bí mật (cố định để dễ kiểm tra)
so_bi_mat = 7
so_lan = 0

print("Máy đã nghĩ một số từ 1 đến 10...")

# Người chơi đoán cho tới khi đúng
while True:
    so_lan = so_lan + 1
    doan = int(input(f"Lần đoán {so_lan}: "))
    if doan == so_bi_mat:
        print(f"Chuc mung! Ban doan dung sau {so_lan} lan.")
        break
    elif doan < so_bi_mat:
        print("Nho hon so bi mat!")
    else:
        print("Lon hon so bi mat!")
```

**Giải thích code:**
* `so_lan = so_lan + 1` ở **đầu** mỗi lượt — đếm trước khi hỏi.
* `break` — lối thoát duy nhất của vòng lặp vô hạn có chủ đích.
* Gợi ý "nhỏ hơn/lớn hơn" thu hẹp dần phạm vi đoán — với số bí mật 7, mọi dãy đoán đều hội tụ nhanh.

**Độ phức tạp:** O(k) với k là số lần đoán.

---

### Bài 16: Kiểm tra số đối xứng

**Phân tích:** Đảo ngược n (bài 13) rồi so sánh với bản gốc — nhớ lưu bản gốc trước khi phá hủy n.

**Ý tưởng:** `n_goc = n`; dựng `so_dao`; so sánh.

**Thuật toán:**
1. Nhập n, lưu `n_goc = n`.
2. Dựng `so_dao` bằng kỹ thuật `* 10 + chữ số`.
3. So sánh `so_dao` với `n_goc`.

**Code:**

```python
# Nhập n (ví dụ nhập: 1221)
n = int(input("Nhập n: "))

n_goc = n      # Lưu bản gốc — n sẽ bị phá hủy trong vòng lặp!
so_dao = 0

# Dựng số đảo ngược
while n > 0:
    so_dao = so_dao * 10 + (n % 10)
    n = n // 10

# So sánh số đảo với số gốc
if so_dao == n_goc:
    print("La so doi xung")
else:
    print("Khong phai so doi xung")
```

**Giải thích code:**
* `n_goc = n` trước vòng lặp — sau vòng lặp n = 0 nên phải so sánh với bản gốc.
* 1221 đảo thành 1221 → bằng nhau → "La so doi xung". 123 đảo thành 321 → không.

**Độ phức tạp:** O(log n).

---

### Bài 17: Kiểm tra số nguyên tố bằng while

**Phân tích:** Tìm ước từ 2 đến n−1; `else` của while kết luận "nguyên tố" khi không tìm thấy ước (không break).

**Ý tưởng:** `i = 2`; `while i < n:`; thấy ước thì break; else → nguyên tố.

**Thuật toán:**
1. Nhập n; nếu n < 2 → không nguyên tố.
2. `i = 2`.
3. Trong khi `i < n`: nếu `n % i == 0` → break; tăng i.
4. `else`: n là số nguyên tố.

**Code:**

```python
# Nhập n (ví dụ nhập: 29)
n = int(input("Nhập n: "))

# Số nhỏ hơn 2 không phải số nguyên tố
if n < 2:
    print("Khong phai so nguyen to")
else:
    i = 2
    # Tìm ước trong khoảng từ 2 đến n - 1
    while i < n:
        if n % i == 0:
            print("Khong phai so nguyen to")
            break            # Tìm thấy ước → thoát
        i = i + 1
    else:
        # Vòng lặp kết thúc tự nhiên — không tìm thấy ước nào
        print("La so nguyen to")
```

**Giải thích code:**
* Khối `else` của while chạy **chỉ khi không có `break`** — chính là "duyệt hết mà không thấy ước" → nguyên tố.
* Với n = 29: thử i = 2..28 không số nào chia hết → hết vòng lặp → "La so nguyen to".
* Với n = 10: gặp i = 2 (10 % 2 == 0) → break → else không chạy → "Khong phai...".
* n = 2: i = 2 không nhỏ hơn 2 → vòng lặp không chạy → else chạy → nguyên tố ✅ (2 là nguyên tố nhỏ nhất).

**Độ phức tạp:** O(n) — có thể tối ưu O(√n) ở bài sau.

---

### Bài 18: Lãi kép — bao giờ đạt mục tiêu?

**Phân tích:** Số tháng không biết trước — `while tien < M:` đúng chất while.

**Ý tưởng:** Mỗi tháng cộng lãi và tăng biến đếm; dừng khi đạt mục tiêu.

**Thuật toán:**
1. Nhập S, r, M.
2. `tien = S`, `thang = 0`.
3. Trong khi `tien < M`: `tien = tien + tien * r / 100`; `thang = thang + 1`.
4. In số tháng.

**Code:**

```python
# Nhập dữ liệu (ví dụ: 100 triệu, 1%/tháng, mục tiêu 150 triệu)
s = float(input("Nhập tiền gửi (triệu): "))
r = float(input("Nhập lãi suất %/tháng: "))
muc_tieu = float(input("Nhập mục tiêu (triệu): "))

tien = s
thang = 0

# Cộng lãi mỗi tháng cho tới khi đạt mục tiêu
while tien < muc_tieu:
    tien = tien + tien * r / 100   # Lãi kép
    thang = thang + 1

print(f"Cần {thang} tháng để đạt mục tiêu")
```

**Giải thích code:**
* `tien = tien + tien * r / 100` — lãi tính trên gốc mới (đã gồm lãi tháng trước).
* 100 → 101 → 102.01 → ... chạm 150 sau **41 tháng** (100 × 1.01⁴¹ ≈ 150.6) — khớp ví dụ.
* Lưu ý: nếu r = 0 và mục tiêu > tiền gửi thì vòng lặp **vô hạn** — có thể thêm kiểm tra `if r <= 0` để tránh; với r > 0 mọi mục tiêu đều đạt được.

**Độ phức tạp:** O(tháng cần gửi).

---

### Bài 19: Game đoán số ngẫu nhiên (có giới hạn lượt)

**Phân tích:** Số bí mật ngẫu nhiên 1–100 (thư viện chuẩn `random`), giới hạn 7 lượt — `else` của while in thông báo thua khi hết lượt không break.

**Ý tưởng:** `while so_lan < 7:`; đúng thì break; else → thua.

**Thuật toán:**
1. `import random`; `so_bi_mat = random.randint(1, 100)`.
2. `so_lan = 0`.
3. Trong khi `so_lan < 7`: tăng so_lan, nhập đoán, gợi ý; đúng → break.
4. `else`: in thông báo thua kèm số bí mật.

**Code:**

```python
import random  # Thư viện chuẩn — tạo số ngẫu nhiên

# Máy nghĩ số ngẫu nhiên từ 1 đến 100
so_bi_mat = random.randint(1, 100)
so_lan = 0

print("Máy đã nghĩ một số từ 1 đến 100. Bạn có 7 lượt đoán!")

# Người chơi có tối đa 7 lượt
while so_lan < 7:
    so_lan = so_lan + 1
    doan = int(input(f"Lần {so_lan}/7: "))
    if doan == so_bi_mat:
        print(f"Chuc mung! Ban doan dung sau {so_lan} lan.")
        break
    elif doan < so_bi_mat:
        print("Lon hon so bi mat!")   # Gợi ý: số cần đoán lớn hơn
    else:
        print("Nho hon so bi mat!")   # Gợi ý: số cần đoán nhỏ hơn
else:
    # Hết 7 lượt mà không đoán đúng (không có break)
    print(f"Ban da thua! So bi mat la: {so_bi_mat}")
```

**Giải thích code:**
* `random.randint(1, 100)` — sinh số nguyên ngẫu nhiên trong khoảng 1..100 (đã học cách cài `import` ở bài 2, chi tiết bài 20).
* `while so_lan < 7:` — vòng lặp bị **giới hạn lượt** bởi điều kiện; không cần `while True`.
* Khối `else` chạy khi vòng lặp kết thúc vì so_lan = 7 (không break) → thông báo thua. Đúng thì break → else bị bỏ qua.
* Mẹo chơi: chọn 50, rồi thu hẹp nửa phạm vi mỗi lượt — tối đa ~7 lượt đủ thắng (thuật toán tìm kiếm nhị phân, sẽ học ở bài sau).

**Độ phức tạp:** O(1) — tối đa 7 lượt cố định.

---

### Bài 20: Máy ATM hoàn chỉnh

**Phân tích:** Menu vòng lặp chuẩn: in menu → nhận lựa chọn → xử lý → quay lại; thoát bằng lựa chọn 0.

**Ý tưởng:** `while True:`; số dư là biến cập nhật; kiểm tra số dư đủ khi rút; kiểm tra tiền dương khi nạp.

**Thuật toán:**
1. `so_du = 1000000.0`.
2. Vòng lặp: in menu, nhận lựa chọn (chuỗi).
3. `"0"` → tạm biệt, break.
4. `"1"` → in số dư. `"2"` → nhập tiền dương, cộng dồn. `"3"` → kiểm tra đủ tiền rồi trừ.
5. Khác → báo lỗi.

**Code:**

```python
# Số dư khởi tạo
so_du = 1000000.0

print("===== MÁY ATM =====")

# Menu chạy cho tới khi người dùng thoát
while True:
    # In menu mỗi lượt
    print("0. Thoát chương trình")
    print("1. Xem số dư hiện tại")
    print("2. Nạp tiền")
    print("3. Rút tiền")
    lua_chon = input("Nhập lựa chọn: ")

    # Xử lý từng lựa chọn
    if lua_chon == "0":
        print("Cảm ơn bạn đã sử dụng ATM!")
        break
    elif lua_chon == "1":
        print(f"Số dư hiện tại: {so_du} VND")
    elif lua_chon == "2":
        tien = float(input("Nhập số tiền muốn nạp: "))
        if tien <= 0:
            print("Số tiền nạp phải lớn hơn 0!")
        else:
            so_du = so_du + tien
            print(f"Nạp tiền thành công. Số dư mới: {so_du} VND")
    elif lua_chon == "3":
        tien = float(input("Nhập số tiền muốn rút: "))
        if tien <= 0:
            print("Số tiền rút phải lớn hơn 0!")
        elif tien > so_du:
            print("So du khong du!")
        else:
            so_du = so_du - tien
            print(f"Rút tiền thành công. Số dư mới: {so_du} VND")
    else:
        print("Lua chon khong hop le!")
```

**Giải thích code:**
* `lua_chon` là **chuỗi** (`"0"`...`"3"`) — so sánh trực tiếp với input, không cần ép kiểu.
* `so_du` được cập nhật trong vòng lặp và **giữ nguyên giá trị** giữa các lượt — đúng tính chất máy ATM thật.
* Nạp tiền kiểm tra `tien <= 0`; rút tiền kiểm tra cả `tien <= 0` lẫn `tien > so_du` — tài khoản không bao giờ âm.
* Sau mỗi thao tác, vòng lặp quay lại in menu; chỉ `lua_chon == "0"` (break) mới kết thúc.

**Độ phức tạp:** O(1) mỗi lượt; tổng phụ thuộc số thao tác người dùng.

---

## 📌 Lời khuyên cuối

* 🔁 Kiểm tra lại "bộ ba": khởi tạo? kiểm tra? cập nhật? — thiếu một là vô hạn.
* 🚪 `while True` phải có lối thoát — nếu không thấy `break` trong 5 giây, dừng lại đọc lại code.
* 🧮 Kỹ thuật "bóc chữ số" (`% 10` lấy, `// 10` bỏ) xuất hiện ở bài 11, 12, 13, 16 — thuộc lòng nó.
* 🔍 `else` của while rất hợp cho tìm kiếm: "không thấy thì báo" — gọn hơn biến cờ.
* 🧪 Chạy thử với số nhỏ và kiểm tra bằng tay trước khi tin kết quả.

👉 Tiếp theo: **[Bài 12: Hàm](../12_Ham/bai_giang.md)**
