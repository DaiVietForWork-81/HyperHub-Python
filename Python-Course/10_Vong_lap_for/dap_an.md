# ✅ Bài 10: Đáp Án – Vòng Lặp For

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án để việc học hiệu quả nhất.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Đếm từ 1 đến 10

**Phân tích:** Đếm đều tay từ 1 đến 10 — bài làm quen vòng lặp.

**Ý tưởng:** `range(1, 11)` sinh dãy 1..10; in từng giá trị.

**Thuật toán:**
1. Duyệt `i` từ 1 đến 10.
2. In `i`.

**Code:**

```python
# In các số từ 1 đến 10
for i in range(1, 11):
    print(i)
```

**Giải thích code:**
* `range(1, 11)` — sinh `1, 2, ..., 10` (không bao gồm 11).
* `print(i)` — in từng số, mỗi `print` tự xuống dòng.

**Độ phức tạp:** O(n) với n = 10 số in.

---

### Bài 2: Các số lẻ từ 1 đến 20

**Phân tích:** Dãy số lẻ cách đều 2 đơn vị — dùng step của range.

**Ý tưởng:** `range(1, 21, 2)` sinh thẳng dãy số lẻ.

**Thuật toán:**
1. Duyệt `i` trong dãy 1, 3, 5, ..., 19.
2. In từng số.

**Code:**

```python
# In các số lẻ từ 1 đến 20
for i in range(1, 21, 2):
    print(i)
```

**Giải thích code:**
* `range(1, 21, 2)` — bắt đầu 1, mỗi bước cộng 2 → `1, 3, 5, ..., 19`.
* Điểm dừng `21` đảm bảo số cuối là 19 (lẻ lớn nhất ≤ 20).

**Độ phức tạp:** O(n) — 10 số.

---

### Bài 3: Tổng từ 1 đến n

**Phân tích:** Cộng dồn — bài toán kinh điển của biến tích lũy.

**Ý tưởng:** Khởi tạo `tong = 0`, mỗi lượt cộng i vào.

**Thuật toán:**
1. Nhập n.
2. `tong = 0`.
3. Lặp i từ 1 đến n: `tong = tong + i`.
4. In kết quả.

**Code:**

```python
# Nhập n (ví dụ nhập: 5)
n = int(input("Nhập n: "))

tong = 0  # Biến tích lũy bắt đầu bằng 0

# Cộng dồn từng số từ 1 đến n
for i in range(1, n + 1):
    tong = tong + i

print(f"Tổng 1 + 2 + ... + {n} = {tong}")
```

**Giải thích code:**
* `range(1, n + 1)` — quy tắc "một cộng": muốn đủ đến n thì ghi `n + 1`.
* `tong = tong + i` — hộp tích lũy: lấy giá trị cũ, cộng thêm i, bỏ lại.
* Với n = 5: 0→1→3→6→10→15.

**Độ phức tạp:** O(n).

---

### Bài 4: In chữ 5 lần

**Phân tích:** Lặp đúng 5 lần, cần số lần để hiển thị.

**Ý tưởng:** `range(1, 6)` cho số lần 1..5; f-string ghép vào dòng chữ.

**Thuật toán:**
1. Duyệt i từ 1 đến 5.
2. In `Lan i: Xin chao Python!`.

**Code:**

```python
# In dòng chữ 5 lần kèm số thứ tự
for i in range(1, 6):
    print(f"Lan {i}: Xin chao Python!")
```

**Giải thích code:**
* `range(1, 6)` — 5 lượt với i = 1, 2, 3, 4, 5.
* `f"Lan {i}: ..."` — f-string chèn số i vào giữa câu.

**Độ phức tạp:** O(1) — số lần cố định 5.

---

### Bài 5: Bảng nhân của n

**Phân tích:** Một bảng nhân gồm 10 phép tính với số cố định n.

**Ý tưởng:** i chạy 1..10, in `n x i = n*i`.

**Thuật toán:**
1. Nhập n.
2. Lặp i từ 1 đến 10.
3. In phép tính.

**Code:**

```python
# Nhập số cần làm bảng nhân (ví dụ nhập: 5)
n = int(input("Nhập n: "))

# In bảng nhân từ n x 1 đến n x 10
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```

**Giải thích code:**
* `range(1, 11)` — i = 1..10.
* `{n * i}` — Python tính sẵn tích ngay trong f-string.
* Nhập 5 → 10 dòng từ `5 x 1 = 5` đến `5 x 10 = 50`.

**Độ phức tạp:** O(10) → hằng số.

---

### Bài 6: Số chẵn giảm dần

**Phân tích:** Đếm lùi cách quãng 2 — step âm của range.

**Ý tưởng:** `range(20, -1, -2)` sinh 20, 18, ..., 0.

**Thuật toán:**
1. Duyệt i trong dãy 20 → 0 (bước −2).
2. In i.

**Code:**

```python
# In các số chẵn giảm dần từ 20 về 0
for i in range(20, -1, -2):
    print(i)
```

**Giải thích code:**
* `range(20, -1, -2)` — bắt đầu 20, mỗi bước trừ 2.
* Điểm dừng `-1` (không phải 0!) vì range không bao gồm stop — muốn in cả 0 thì stop phải nhỏ hơn 0.

**Độ phức tạp:** O(n) — 11 số.

---

### Bài 7: Tên của bạn từng chữ

**Phân tích:** Chuỗi là một dãy ký tự — duyệt trực tiếp bằng for.

**Ý tưởng:** `for chu in ho_ten:` in từng ký tự.

**Thuật toán:**
1. Nhập họ tên.
2. Duyệt từng ký tự và in.

**Code:**

```python
# Nhập họ tên (ví dụ nhập: An)
ho_ten = input("Nhập họ tên: ")

# In từng chữ cái của tên
for chu in ho_ten:
    print(chu)
```

**Giải thích code:**
* `for chu in ho_ten:` — Python cho phép duyệt trực tiếp chuỗi, mỗi lượt gán `chu` một ký tự.
* Với "An" → in `A` rồi `n`.

**Độ phức tạp:** O(len(ho_ten)).

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Giai thừa n!

**Phân tích:** Nhân dồn các số 1..n — cần phân biệt khởi tạo với cộng dồn.

**Ý tưởng:** `giai_thua = 1` rồi nhân dồn từng i.

**Thuật toán:**
1. Nhập n.
2. `giai_thua = 1` (nhân dồn khởi tạo bằng 1).
3. Lặp i từ 1 đến n: `giai_thua = giai_thua * i`.
4. In kết quả.

**Code:**

```python
# Nhập n (ví dụ nhập: 5)
n = int(input("Nhập n: "))

giai_thua = 1  # Nhân dồn nên khởi tạo bằng 1, không phải 0!

# Nhân dồn từ 1 đến n
for i in range(1, n + 1):
    giai_thua = giai_thua * i

print(f"{n}! = {giai_thua}")
```

**Giải thích code:**
* `giai_thua = 1` — nếu khởi tạo 0, mọi phép nhân với 0 ra 0.
* Các bước với n = 5: 1×1=1 → ×2=2 → ×3=6 → ×4=24 → ×5=**120**.

**Độ phức tạp:** O(n).

---

### Bài 9: Tổng số chẵn từ 0 đến n

**Phân tích:** Lọc số chẵn — có hai cách: lọc bằng `if` hoặc sinh thẳng bằng step.

**Ý tưởng:** Dùng `range(0, n + 1, 2)` sinh thẳng dãy số chẵn.

**Thuật toán:**
1. Nhập n.
2. `tong = 0`.
3. Cộng dồn i trong dãy 0, 2, 4, ..., n.
4. In kết quả.

**Code:**

```python
# Nhập n (ví dụ nhập: 10)
n = int(input("Nhập n: "))

tong = 0
# Dãy số chẵn: 0, 2, 4, ... (bước nhảy 2)
for i in range(0, n + 1, 2):
    tong = tong + i

print(f"Tổng các số chẵn từ 0 đến {n} là: {tong}")
```

**Giải thích code:**
* `range(0, n + 1, 2)` — sinh thẳng dãy số chẵn, không cần `if i % 2 == 0`.
* Với n = 10: 0+2+4+6+8+10 = **30** — khớp ví dụ giáo trình.
* Nếu n lẻ (n = 7): dãy 0,2,4,6 → tổng 12 — vẫn đúng vì chỉ tính số chẵn.

**Độ phức tạp:** O(n).

---

### Bài 10: Bỏ qua số chia hết cho 3

**Phân tích:** "Bỏ qua lượt" đúng nghĩa của `continue`.

**Ý tưởng:** Trong vòng lặp, nếu `i % 3 == 0` thì `continue` (không in).

**Thuật toán:**
1. Duyệt i từ 1 đến 30.
2. Nếu i chia hết cho 3 → `continue`.
3. Ngược lại in i.

**Code:**

```python
# In số từ 1 đến 30, bỏ qua số chia hết cho 3
for i in range(1, 31):
    if i % 3 == 0:
        continue  # Bỏ qua lượt này, sang số kế tiếp
    print(i)
```

**Giải thích code:**
* `continue` — khi gặp, Python bỏ qua phần còn lại của lượt và chuyển ngay đến i kế tiếp.
* Số 3, 6, 9... không được in; các số khác in bình thường.

**Độ phức tạp:** O(n).

---

### Bài 11: Bảng cửu chương 2 đến 5

**Phân tích:** Nhiều bảng nhân — vòng lặp lồng nhau: vòng ngoài chọn bảng, vòng trong in phép tính.

**Ý tưởng:** Hai `for` lồng nhau, mỗi lượt vòng ngoài đổi bảng.

**Thuật toán:**
1. Vòng ngoài `so` từ 2 đến 5: in tiêu đề.
2. Vòng trong `i` từ 1 đến 10: in phép tính.

**Code:**

```python
# In các bảng nhân từ 2 đến 5
for so in range(2, 6):            # Vòng ngoài: chọn bảng
    print(f"=== BANG NHAN {so} ===")
    for i in range(1, 11):        # Vòng trong: 10 phép tính
        print(f"{so} x {i} = {so * i}")
```

**Giải thích code:**
* Với `so = 2`, vòng trong in đủ 10 phép tính rồi mới sang `so = 3`.
* `range(2, 6)` — 2, 3, 4, 5 (4 bảng).
* Tổng cộng 4 tiêu đề + 40 phép tính.

**Độ phức tạp:** O(4 × 10) → hằng số.

---

### Bài 12: Trung bình cộng n số

**Phân tích:** Nhập n lần trong vòng lặp, cộng dồn rồi chia — mô hình nhập liệu hàng loạt.

**Ý tưởng:** Vòng lặp `range(n)`; mỗi lượt nhập một số và cộng dồn.

**Thuật toán:**
1. Nhập số môn n.
2. `tong = 0`.
3. Lặp i từ 1 đến n: nhập điểm môn i, cộng vào tong.
4. Trung bình = tong / n; in làm tròn 2 chữ số.

**Code:**

```python
# Nhập số môn (ví dụ nhập: 3)
n = int(input("Nhập số môn: "))

tong = 0

# Nhập và cộng dồn điểm từng môn
for i in range(1, n + 1):
    diem = float(input(f"Nhập điểm môn {i}: "))  # Ví dụ: 7, 8, 9
    tong = tong + diem

# Trung bình = tổng chia số môn
trung_binh = tong / n
print(f"Điểm trung bình: {round(trung_binh, 2)}")
```

**Giải thích code:**
* `input(f"Nhập điểm môn {i}: ")` — nhãn thay đổi theo i nhờ f-string.
* `tong / n` — với 7, 8, 9 → `24 / 3 = 8.0`.
* `round(trung_binh, 2)` — làm tròn 2 chữ số thập phân (bài 4 đã làm quen).

**Độ phức tạp:** O(n).

---

### Bài 13: Hóa đơn siêu thị

**Phân tích:** Tính tiền thực tế: nhập giá từng món, cộng dồn tổng.

**Ý tưởng:** Giống bài 12 nhưng chỉ cộng dồn, không chia.

**Thuật toán:**
1. Nhập số món n.
2. `tong = 0`.
3. Lặp i từ 1 đến n: nhập giá món i, cộng dồn.
4. In tổng.

**Code:**

```python
# Nhập số món hàng (ví dụ nhập: 3)
n = int(input("Nhập số món hàng: "))

tong = 0

# Nhập giá từng món và cộng dồn
for i in range(1, n + 1):
    gia = float(input(f"Nhập giá món {i}: "))  # Ví dụ: 15, 25, 10
    tong = tong + gia

print(f"Tổng hóa đơn: {tong} nghìn đồng")
```

**Giải thích code:**
* Mỗi lượt vòng lặp nhập một giá và cộng ngay vào hóa đơn.
* Ví dụ: 15 + 25 + 10 = **50** nghìn đồng.
* Nếu siêu thị có 1000 món, chỉ cần đổi n — code không đổi dòng nào.

**Độ phức tạp:** O(n).

---

### Bài 14: Vị trí đầu tiên của ký tự

**Phân tích:** Tìm kiếm trong chuỗi — dùng `enumerate` lấy vị trí và `break` để dừng ngay khi tìm thấy.

**Ý tưởng:** Duyệt cặp (vị trí, ký tự); tìm thấy thì ghi lại vị trí và `break`; biến cờ cho biết có tìm thấy.

**Thuật toán:**
1. Nhập chuỗi và ký tự cần tìm.
2. `tim_thay = False`, `vi_tri = -1`.
3. Duyệt `enumerate(chuoi)`: nếu ký tự khớp → lưu vị trí, `tim_thay = True`, `break`.
4. In kết quả theo cờ.

**Code:**

```python
# Nhập chuỗi và ký tự (ví dụ: "python" và "t")
chuoi = input("Nhập chuỗi: ")
ky_tu = input("Nhập ký tự: ")

tim_thay = False
vi_tri = -1

# Duyệt từng vị trí kèm ký tự
for vi_tri, c in enumerate(chuoi):
    if c == ky_tu:
        tim_thay = True
        break  # Tìm thấy rồi thì dừng ngay, không duyệt tiếp

# In kết quả dựa vào biến cờ
if tim_thay:
    print(f"Vị trí đầu tiên: {vi_tri}")
else:
    print("Khong tim thay!")
```

**Giải thích code:**
* `enumerate(chuoi)` — trả về cặp `(vị trí, ký tự)`.
* `break` — với chuỗi "python", chữ 't' ở vị trí 2; break giúp dừng ngay, không in các vị trí sau.
* Biến cờ `tim_thay` — cách chuẩn để kiểm tra "có tìm thấy không" sau vòng lặp; nếu chỉ dựa vào `vi_tri` thì không biết phân biệt vị trí 0 thật với "chưa tìm".

**Độ phức tạp:** O(len(chuoi)) — trong trường hợp xấu nhất duyệt hết chuỗi.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Toàn bộ bảng cửu chương

**Phân tích:** Mở rộng bài 11 cho 8 bảng với khoảng cách giữa các bảng.

**Ý tưởng:** Vòng ngoài 2..9, vòng trong 1..10, thêm `print()` trống.

**Thuật toán:**
1. Vòng ngoài `so` từ 2 đến 9: in tiêu đề.
2. Vòng trong in 10 phép tính.
3. In dòng trống ngăn cách.

**Code:**

```python
# In toàn bộ bảng cửu chương từ 2 đến 9
for so in range(2, 10):
    print(f"=== BANG NHAN {so} ===")
    for i in range(1, 11):
        print(f"{so} x {i} = {so * i}")
    print()  # Dòng trống ngăn cách các bảng
```

**Giải thích code:**
* `range(2, 10)` — 8 bảng: 2..9.
* `print()` không đối số — in một dòng trống sau mỗi bảng, nhìn gọn gàng.
* Vòng trong chạy đủ 10 lượt cho mỗi giá trị của vòng ngoài — 80 dòng phép tính.

**Độ phức tạp:** O(8 × 10) → hằng số.

---

### Bài 16: Kiểm tra số nguyên tố

**Phân tích:** Số nguyên tố không có ước nào ngoài 1 và chính nó — kiểm tra từ 2 đến n-1.

**Ý tưởng:** Biến cờ `nguyen_to`; nếu tìm thấy ước thì gán False và `break`.

**Thuật toán:**
1. Nhập n.
2. Nếu n < 2 → không phải nguyên tố (2 là nguyên tố nhỏ nhất).
3. Duyệt i từ 2 đến n-1: nếu n chia hết cho i → cờ sai, break.
4. In kết luận theo cờ.

**Code:**

```python
# Nhập n (ví dụ nhập: 17)
n = int(input("Nhập n: "))

nguyen_to = True  # Giả định n là số nguyên tố

# 1 và số nhỏ hơn 2 không phải số nguyên tố
if n < 2:
    nguyen_to = False

# Kiểm tra từ 2 đến n - 1
for i in range(2, n):
    if n % i == 0:   # Có ước khác 1 và n
        nguyen_to = False
        break        # Đã chắc chắn không phải, dừng sớm

# In kết luận
if nguyen_to:
    print("La so nguyen to")
else:
    print("Khong phai so nguyen to")
```

**Giải thích code:**
* `range(2, n)` — các ước ứng viên của n.
* `break` — gặp ước đầu tiên là đủ kết luận, không cần kiểm tra tiếp (tiết kiệm thời gian với số lớn).
* n = 17: thử 2..16 không số nào chia hết → vẫn True → "La so nguyen to".

**Độ phức tạp:** O(n) — duyệt tối đa n−2 số; có thể tối ưu thành O(√n) (sẽ học ở bài sau).

---

### Bài 17: Tam giác sao

**Phân tích:** Hàng i có i dấu `*` — nhân chuỗi bằng toán tử `*`.

**Ý tưởng:** Vòng ngoài điều khiển hàng; `"*" * i` tạo đủ số dấu sao.

**Thuật toán:**
1. Nhập chiều cao h.
2. Duyệt i từ 1 đến h.
3. In `"*" * i`.

**Code:**

```python
# Nhập chiều cao (ví dụ nhập: 4)
h = int(input("Nhập chiều cao: "))

# Vẽ từng hàng: hàng i có i dấu sao
for i in range(1, h + 1):
    print("*" * i)
```

**Giải thích code:**
* `"*" * i` — toán tử `*` với chuỗi lặp lại chuỗi i lần: `"*" * 3` = `"***"`.
* `range(1, h + 1)` — i = 1..h; hàng 1 có 1 sao, hàng h có h sao.

**Độ phức tạp:** O(h²) ký tự in ra.

---

### Bài 18: Tổng dãy phân số

**Phân tích:** Mỗi số hạng là `1/i` — cộng dồn số thực.

**Ý tưởng:** `tong = tong + 1 / i` cho i = 1..n.

**Thuật toán:**
1. Nhập n.
2. `tong = 0`.
3. Lặp i từ 1 đến n: cộng `1 / i`.
4. In làm tròn 2 chữ số.

**Code:**

```python
# Nhập n (ví dụ nhập: 4)
n = int(input("Nhập n: "))

tong = 0.0

# Cộng dồn các phân số 1/i
for i in range(1, n + 1):
    tong = tong + 1 / i

print(f"S = {round(tong, 2)}")
```

**Giải thích code:**
* `1 / i` — trong Python 3, `/` luôn là phép chia thực (ra số thập phân) — không phải `int(i)` như Python 2.
* Với n = 4: 1 + 0.5 + 0.3333 + 0.25 = 2.0833... → làm tròn **2.08**.

**Độ phức tạp:** O(n).

---

### Bài 19: Dãy Fibonacci

**Phân tích:** Mỗi số bằng tổng hai số trước — dùng hai biến trượt.

**Ý tưởng:** `a, b = 0, 1`; mỗi lượt in `a` rồi trượt: `a, b = b, a + b`.

**Thuật toán:**
1. Nhập n.
2. `a, b = 0, 1`.
3. Lặp n lần: in a; cập nhật a, b.
4. Xuống dòng khi kết thúc.

**Code:**

```python
# Nhập n (ví dụ nhập: 7)
n = int(input("Nhập n: "))

a, b = 0, 1  # Hai số đầu của dãy

# In n số Fibonacci đầu tiên
for _ in range(n):
    print(a, end=" ")   # In a kèm khoảng trắng, không xuống dòng
    a, b = b, a + b     # Trượt: a nhận b, b nhận tổng hai số trước

print()  # Xuống dòng sau cùng
```

**Giải thích code:**
* `a, b = b, a + b` — **gán đồng thời**: Python tính `b` và `a + b` từ giá trị cũ rồi mới gán — không cần biến phụ.
* Các bước: in 0 → (1,1); in 1 → (1,2); in 1 → (2,3); in 2 → (3,5); in 3 → (5,8); in 5 → (8,13); in 8 → dừng.
* Kết quả: `0 1 1 2 3 5 8` — đúng n = 7 số.
* `end=" "` — thay ký tự xuống dòng mặc định bằng khoảng trắng (in trên một dòng).

**Độ phức tạp:** O(n).

---

### Bài 20: Lãi kép tiết kiệm

**Phân tích:** Mỗi tháng số tiền tăng thêm `tien * r / 100` — lặp lại n lần.

**Ý tưởng:** Vòng lặp n lần, mỗi lần cập nhật `tien = tien + tien * r / 100`.

**Thuật toán:**
1. Nhập S, r, n.
2. `tien = S`.
3. Lặp n lần: `tien = tien + tien * r / 100`.
4. In kết quả làm tròn 2 chữ số.

**Code:**

```python
# Nhập dữ liệu (ví dụ: 100 triệu, 1% / tháng, 12 tháng)
s = float(input("Nhập số tiền gửi (triệu): "))
r = float(input("Nhập lãi suất %/tháng: "))
n = int(input("Nhập số tháng: "))

tien = s

# Cộng lãi từng tháng (lãi kép: lãi nhập vào gốc)
for _ in range(n):
    tien = tien + tien * r / 100

print(f"Số tiền sau {n} tháng: {round(tien, 2)} triệu đồng")
```

**Giải thích code:**
* `tien = tien + tien * r / 100` — lãi tháng này tính trên **gốc mới** (đã cộng lãi tháng trước) — đó chính là lãi kép.
* Tháng 1: 100 + 1 = 101; tháng 2: 101 + 1.01 = 102.01... — lãi ngày càng lớn dần.
* Sau 12 tháng: **112.68** triệu — khớp ví dụ đề bài.

**Độ phức tạp:** O(n).

---

## 📌 Lời khuyên cuối

* 🔢 Ghi nhớ bộ ba: `range(start, stop, step)` — và **"một cộng"** cho đếm tới n.
* 🧮 Phân biệt: cộng dồn khởi tạo `0`, nhân dồn khởi tạo `1`.
* 🏁 Tìm kiếm → `break`; lọc bỏ → `continue`; tích lũy → biến đặt trước vòng lặp.
* 🧪 Chạy thử với n nhỏ và tự kiểm tra bằng tay trước khi tin kết quả.

👉 Tiếp theo: **[Bài 11: Vòng Lặp While](../11_Vong_lap_while/bai_giang.md)**
