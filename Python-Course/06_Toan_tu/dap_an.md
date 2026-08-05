# ✅ Bài 6: Đáp Án – Toán Tử Trong Python

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án để việc học hiệu quả nhất.
>
> 📌 Trong các đáp án của bài này, giá trị được **gán trực tiếp vào biến** (chưa dùng `input()`) — kỹ năng nhập liệu sẽ học ở bài 7.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Năm phép tính cơ bản

**Phân tích:** Cần in kết quả 5 phép toán khác nhau của `8` và `2`.

**Ý tưởng:** Mỗi phép toán truyền trực tiếp vào `print()`; Python tự tính rồi in.

**Thuật toán:**
1. In `8 + 2`.
2. In `8 - 2`.
3. In `8 * 2`.
4. In `8 / 2`.
5. In `8 ** 2`.

**Code:**

```python
print(8 + 2)    # Cộng: 10
print(8 - 2)    # Trừ: 6
print(8 * 2)    # Nhân: 16
print(8 / 2)    # Chia: 4.0 (luôn ra số thực)
print(8 ** 2)   # Lũy thừa: 64
```

**Giải thích code:**
* `8 / 2` → `4.0` — phép `/` luôn cho kết quả số thực (`float`), kể cả khi chia hết.
* `8 ** 2` → đọc là "8 mũ 2", kết quả `64`.
* Mỗi lệnh `print()` in từng kết quả trên một dòng riêng.

**Độ phức tạp:** O(1).

---

### Bài 2: Chia nguyên và chia dư

**Phân tích:** Hai phép toán `//` (lấy phần nguyên) và `%` (lấy phần dư) khi chia 17 cho 5.

**Ý tưởng:** `17 = 5 * 3 + 2` nên phần nguyên là `3`, phần dư là `2`.

**Thuật toán:**
1. In `17 // 5`.
2. In `17 % 5`.

**Code:**

```python
# Chia lấy phần nguyên: 17 : 5 được 3 (dư 2)
print(17 // 5)   # 3
# Chia lấy phần dư
print(17 % 5)    # 2
```

**Giải thích code:**
* `//` — bỏ phần dư, chỉ giữ phần nguyên của thương.
* `%` — giữ đúng phần dư của phép chia.
* Hai toán tử này luôn đi cặp: `17 = (17 // 5) * 5 + (17 % 5)`.

**Độ phức tạp:** O(1).

---

### Bài 3: Chia bánh cho bạn

**Phân tích:** 30 chiếc bánh chia đều cho 10 học sinh — mỗi bạn 3 chiếc, không dư.

**Ý tưởng:** Dùng biến lưu số bánh và số học sinh, rồi áp dụng `//` và `%`.

**Thuật toán:**
1. Gán `banh = 30`, `hoc_sinh = 10`.
2. Tính `so_ban = banh // hoc_sinh`.
3. Tính `con_du = banh % hoc_sinh`.
4. In hai kết quả kèm nhãn.

**Code:**

```python
# Số bánh và số học sinh
banh = 30
hoc_sinh = 10
# Mỗi bạn được bao nhiêu chiếc (phần nguyên)
so_ban = banh // hoc_sinh
# Còn thừa bao nhiêu chiếc (phần dư)
con_du = banh % hoc_sinh
print("Moi ban:", so_ban)
print("Con du:", con_du)
```

**Giải thích code:**
* `30 // 10 = 3` — mỗi bạn 3 chiếc.
* `30 % 10 = 0` — chia hết nên không dư.
* Dùng biến trung gian giúp code dễ đọc hơn so với gộp phép tính vào `print()`.

**Độ phức tạp:** O(1).

---

### Bài 4: Bình phương và lập phương

**Phân tích:** Tính `x²` và `x³` khi `x = 5`.

**Ý tưởng:** Dùng toán tử lũy thừa `**` với số mũ 2 và 3.

**Thuật toán:**
1. Gán `x = 5`.
2. In `x ** 2`.
3. In `x ** 3`.

**Code:**

```python
# Biến cần tính lũy thừa
x = 5
# Bình phương (x mũ 2)
print(x ** 2)   # 25
# Lập phương (x mũ 3)
print(x ** 3)   # 125
```

**Giải thích code:**
* `x ** 2` ↔ `5 * 5 = 25`.
* `x ** 3` ↔ `5 * 5 * 5 = 125`.
* Toán tử `**` tiện hơn viết lặp nhiều phép nhân khi số mũ lớn.

**Độ phức tạp:** O(1).

---

### Bài 5: Cộng dồn bằng `+=`

**Phân tích:** Bắt đầu `tong = 0`, cộng dần 5, 8, 3 — kết quả cuối là 16.

**Ý tưởng:** Dùng toán tử gán kết hợp `+=` — ngắn gọn thay cho `tong = tong + ...`.

**Thuật toán:**
1. Khởi tạo `tong = 0`.
2. `tong += 5`.
3. `tong += 8`.
4. `tong += 3`.
5. In `tong`.

**Code:**

```python
# Khởi tạo tổng bằng 0
tong = 0
# Cộng dồn từng số vào biến tong
tong += 5   # tong = 0 + 5 = 5
tong += 8   # tong = 5 + 8 = 13
tong += 3   # tong = 13 + 3 = 16
print(tong)   # 16
```

**Giải thích code:**
* `tong += 5` tương đương `tong = tong + 5` — lấy giá trị hiện tại cộng thêm 5 rồi gán lại.
* `+=` giúp code gọn và ít lỗi hơn khi cần ghi biến nhiều lần.
* Đây là mẫu câu **tích lũy (accumulator)** — xuất hiện khắp nơi trong lập trình.

**Độ phức tạp:** O(1).

---

### Bài 6: Kiểm tra số lớn hơn

**Phân tích:** So sánh `a = 15` với `b = 6` bằng hai toán tử `>` và `<`.

**Ý tưởng:** Kết quả so sánh là kiểu `bool` — `True` hoặc `False`, in trực tiếp.

**Thuật toán:**
1. Gán `a = 15`, `b = 6`.
2. In `a > b`.
3. In `a < b`.

**Code:**

```python
# Hai số cần so sánh
a = 15
b = 6
print(a > b)   # 15 > 6 → True
print(a < b)   # 15 < 6 → False
```

**Giải thích code:**
* `>` hỏi "có lớn hơn không?" — kết quả `True`.
* `<` hỏi "có nhỏ hơn không?" — kết quả `False`.
* Mọi phép so sánh đều trả về kiểu `bool`, không phải số.

**Độ phức tạp:** O(1).

---

### Bài 7: Đại hay sai?

**Phân tích:** Kiểm tra ba biểu thức: `5 == 5`, `5 == "5"`, `5 != 4`.

**Ý tưởng:** Dùng `==` (bằng) và `!=` (khác nhau); chú ý `"5"` là chuỗi nên không bằng số `5`.

**Thuật toán:**
1. In `5 == 5`.
2. In `5 == "5"`.
3. In `5 != 4`.

**Code:**

```python
print(5 == 5)    # True - cùng là số 5
print(5 == "5")  # False - số khác chuỗi ký tự
print(5 != 4)    # True - khác nhau
```

**Giải thích code:**
* `==` — so sánh **giá trị** kèm kiểu: `5` (int) và `"5"` (str) không bao giờ bằng nhau.
* `!=` — phủ định của `==`: đúng khi hai giá trị khác nhau.
* Đây là lý do phải **ép kiểu** dữ liệu khi so sánh — kỹ năng sẽ học ở bài 7.

**Độ phức tạp:** O(1).

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Thứ tự ưu tiên

**Phân tích:** Ba biểu thức kiểm tra thứ tự tính toán: nhân chia trước cộng trừ, ngoặc tính đầu tiên.

**Ý tưởng:** Viết trực tiếp ba biểu thức, so sánh kết quả với nhau.

**Thuật toán:**
1. In `2 + 3 * 4`.
2. In `(2 + 3) * 4`.
3. In `10 // 2 + 2`.

**Code:**

```python
print(2 + 3 * 4)   # 14 - nhân (3*4=12) trước, rồi cộng (2+12)
print((2 + 3) * 4) # 20 - ngoặc tính trước: (5)*4
print(10 // 2 + 2) # 7 - chia nguyên (5) trước, rồi cộng (5+2)
```

**Giải thích code:**
* Bước 1 → 3: nhân chia có **độ ưu tiên cao hơn** cộng trừ.
* Dấu ngoặc `( )` luôn được tính **đầu tiên**, đổi được thứ tự mặc định.
* `10 // 2 = 5` — chia nguyên vẫn thuộc nhóm nhân chia, tính trước `+`.

**Độ phức tạp:** O(1).

---

### Bài 9: Đổi nhiệt độ C sang F

**Phân tích:** Từ `do_c = 20.5`, áp dụng công thức `F = C * 9 / 5 + 32` → 68.9°F.

**Ý tưởng:** Tính liền biểu thức rồi dùng `round(x, 1)` giữ 1 chữ số thập phân.

**Thuật toán:**
1. Gán `do_c = 20.5`.
2. Tính `do_f = do_c * 9 / 5 + 32`.
3. Làm tròn 1 chữ số và in.

**Code:**

```python
# Nhiệt độ đầu vào theo độ C
do_c = 20.5
# Công thức chuyển đổi sang độ F
do_f = do_c * 9 / 5 + 32
# Làm tròn 1 chữ số thập phân rồi in
print(round(do_f, 1))
```

**Giải thích code:**
* `20.5 * 9 / 5 + 32` → nhân chia trước: `184.5 / 5 = 36.9`, cộng `32` → `68.9`.
* `round(do_f, 1)` — giữ đúng 1 chữ số sau dấu phẩy, kết quả `68.9`.
* Thứ tự phép tính của Python luôn tuân theo ưu tiên toán học.

**Độ phức tạp:** O(1).

---

### Bài 10: Sấp giảm giá quần áo

**Phân tích:** Giá gốc 200.000đ giảm 40% — số tiền giảm 80.000đ, phải trả 120.000đ.

**Ý tưởng:** Viết tỉ lệ giảm dưới dạng số thập phân `0.4`, tính tiền giảm rồi trừ đi.

**Thuật toán:**
1. Gán `gia_goc = 200000`.
2. Tính `tien_giam = gia_goc * 0.4`.
3. Tính `gia_moi = gia_goc - tien_giam`.
4. In hai dòng kết quả.

**Code:**

```python
# Giá gốc của sản phẩm
gia_goc = 200000
# Số tiền được giảm: 40% của giá gốc
tien_giam = gia_goc * 0.4
# Giá mới sau khi trừ tiền giảm
gia_moi = gia_goc - tien_giam
print("Duoc giam:", tien_giam)
print("Gia moi:", gia_moi)
```

**Giải thích code:**
* `200000 * 0.4 = 80000.0` — nhân số nguyên với số thực cho kết quả `float`.
* `200000 - 80000 = 120000.0`.
* Nhờ lưu biến trung gian, ta in được cả "được giảm" và "giá mới" mà không tính lại.

**Độ phức tạp:** O(1).

---

### Bài 11: Tuổi teen không?

**Phân tích:** `tuoi = 14` có nằm trong khoảng 13–19 hay không.

**Ý tưởng:** Dùng toán tử logic `and` để kết hợp hai điều kiện số học `>=` và `<=`.

**Thuật toán:**
1. Gán `tuoi = 14`.
2. Viết biểu thức `tuoi >= 13 and tuoi <= 19`.
3. In kết quả có nhãn.

**Code:**

```python
# Tuổi cần kiểm tra
tuoi = 14
# Cả hai điều kiện đều phải đúng (and)
la_teen = tuoi >= 13 and tuoi <= 19
print("La tuoi teen:", la_teen)   # True
```

**Giải thích code:**
* `14 >= 13` → `True`; `14 <= 19` → `True`.
* `and` yêu cầu **cả hai** đúng: `True and True = True`.
* Nếu chỉ một vế sai thì kết quả là `False`.

**Độ phức tạp:** O(1).

---

### Bài 12: Điểm thưởng hay nhắc nhở?

**Phân tích:** Với `diem = 7`: biểu thức "được thưởng" dùng `or`, biểu thức "bị nhắc" dùng `not`.

**Ý tưởng:** `diem >= 8 or diem == 10` → một trong hai đúng là đủ; `not (diem >= 5)` → phủ định.

**Thuật toán:**
1. Gán `diem = 7`.
2. Tính `duoc_thuong = diem >= 8 or diem == 10`.
3. Tính `bi_nhac = not (diem >= 5)`.
4. In hai kết quả.

**Code:**

```python
# Điểm của học sinh
diem = 7
# Được thưởng khi đạt 8 trở lên HOẶC đúng 10 điểm
duoc_thuong = diem >= 8 or diem == 10
# Bị nhắc khi KHÔNG đạt từ 5 điểm trở lên
bi_nhac = not (diem >= 5)
print("Duoc thuong:", duoc_thuong)   # False
print("Bi nhac:", bi_nhac)           # False
```

**Giải thích code:**
* `or` — chỉ cần **một** điều kiện đúng là đủ: `7 >= 8` (False) `or 7 == 10` (False) → `False`.
* `not (7 >= 5)` → `not True` → `False`.
* Hai kết quả cùng `False` nghĩa là: điểm 7 không đủ thưởng nhưng cũng không tới mức bị nhắc.

**Độ phức tạp:** O(1).

---

### Bài 13: Kiểm tra tính chia hết

**Phân tích:** Số 24 chia hết cho 3 (đúng) nhưng không chia hết cho 5 (sai).

**Ý tưởng:** Số chia hết khi phần dư bằng 0: `so % 3 == 0`.

**Thuật toán:**
1. Gán `so = 24`.
2. Kiểm tra `so % 3 == 0`.
3. Kiểm tra `so % 5 == 0`.
4. In hai kết quả kèm nhãn.

**Code:**

```python
# Số cần kiểm tra
so = 24
# Chia hết cho 3 khi phần dư = 0
print("Chia het cho 3:", so % 3 == 0)   # True
# Chia hết cho 5 khi phần dư = 0
print("Chia het cho 5:", so % 5 == 0)   # False
```

**Giải thích code:**
* `24 % 3 = 0` → biểu thức `0 == 0` đúng → `True`.
* `24 % 5 = 4` → biểu thức `4 == 0` sai → `False`.
* Nhớ quy tắc: **chia hết ⇔ phần dư bằng 0** — viết đủ `so % k == 0`, đừng bỏ sót `== 0`.

**Độ phức tạp:** O(1).

---

### Bài 14: So sánh chuỗi ký tự

**Phân tích:** `"abc" < "abd"` so theo thứ tự từ điển (True); `"An" == "an"` khác hoa-thường (False).

**Ý tưởng:** Chuỗi so sánh lần lượt từng ký tự; chữ hoa và chữ thường là khác nhau.

**Thuật toán:**
1. In `"abc" < "abd"`.
2. In `"An" == "an"`.

**Code:**

```python
print("abc" < "abd")   # True - so từng ký tự: abc... abd...
print("An" == "an")    # False - chữ hoa A khác chữ thường a
```

**Giải thích code:**
* Vị trí đầu `a` bằng nhau; so đến ký tự thứ ba: `c < d` → `True`.
* `"An"` và `"an"` khác nhau ở ký tự đầu (A hoa, a thường) → `False`.
* Python phân biệt chữ hoa – chữ thường nên chuỗi nhập vào cũng được so khớp chính xác.

**Độ phức tạp:** O(n) với n là độ dài chuỗi (ở đây rất ngắn nên xem như O(1)).

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Hóa đơn quán ăn

**Phân tích:** Ba món 50.000 + 15.000 + 20.000 = 85.000đ; cộng 10% phí dịch vụ → 93.500đ.

**Ý tưởng:** Cộng dồn từng món bằng `+=`, sau đó nhân thêm 10% toàn đơn.

**Thuật toán:**
1. Khởi tạo `tong = 0`.
2. Cộng dồn `pho`, `tra`, `banh` bằng `+=`.
3. Tính `tong_phi = tong + tong * 0.1`.
4. In hai dòng kết quả.

**Code:**

```python
# Giá từng món trong đơn
pho = 50000
tra = 15000
banh = 20000
# Cộng dồn các món vào biến tong
tong = 0
tong += pho    # 50000
tong += tra    # 65000
tong += banh   # 85000
# Phí dịch vụ 10% của tổng đơn
tong_phi = tong + tong * 0.1
print("Tong:", tong)
print("Tong co phi dich vu:", tong_phi)
```

**Giải thích code:**
* `+=` giúp cộng dồn gọn; dễ thêm bớt món mà không phải sửa nhiều.
* `tong * 0.1` = 8.500đ phí dịch vụ.
* `85000 + 8500 = 93500.0` — kết quả số thực vì phép nhân với `0.1`.

**Độ phức tạp:** O(1).

---

### Bài 16: Đổi tiền USD

**Phân tích:** 2.350.000 VND với tỉ giá 1 USD = 25.000 VND → 94 USD.

**Ý tưởng:** Chia `so_vnd / 25000`; in với 2 chữ số thập phân (f-string) và phần nguyên (`int`).

**Thuật toán:**
1. Gán `so_vnd = 2350000`.
2. Tính `so_usd = so_vnd / 25000`.
3. In số USD với 2 chữ số thập phân.
4. In phần nguyên của nó.

**Code:**

```python
# Số tiền VND muốn đổi và tỉ giá
so_vnd = 2350000
ti_gia = 25000
# Quy đổi sang USD
so_usd = so_vnd / ti_gia
# In 2 chữ số thập phân bằng f-string (sẽ đọc kỹ ở bài 7)
print(f"So USD: {so_usd:.2f}")   # 94.00
# Phần nguyên của số USD
print("Phan nguyen:", int(so_usd))   # 94
```

**Giải thích code:**
* `2350000 / 25000 = 94.0`.
* `f"{so_usd:.2f}"` — định dạng đúng 2 chữ số thập phân: `"94.00"`.
* `int(so_usd)` — bỏ phần thập phân, giữ nguyên thương nguyên là `94`.

**Độ phức tạp:** O(1).

---

### Bài 17: Kiểm tra năm nhuận

**Phân tích:** Quy tắc năm nhuận: chia hết cho 4, **nhưng** không chia hết cho 100, trừ khi chia hết cho 400. Năm 2024 nhuận, 2025 không.

**Ý tưởng:** Viết gọn quy tắc thành một biểu thức `and`/`or`: `nam % 4 == 0 and (nam % 100 != 0 or nam % 400 == 0)`.

**Thuật toán:**
1. Kiểm tra năm 2024 (kết quả True).
2. Kiểm tra năm 2025 (kết quả False).
3. In hai kết quả kèm nhãn.

**Code:**

```python
# Quy tắc: chia hết cho 4 VÀ (không chia hết cho 100 HOẶC chia hết cho 400)
nam_2024 = 2024 % 4 == 0 and (2024 % 100 != 0 or 2024 % 400 == 0)
nam_2025 = 2025 % 4 == 0 and (2025 % 100 != 0 or 2025 % 400 == 0)
print("2024:", nam_2024)   # True
print("2025:", nam_2025)   # False
```

**Giải thích code:**
* Năm 2024: `2024 % 4 == 0` (True) `and` `2024 % 100 != 0` (True) → `True`.
* Năm 2025: `2025 % 4 = 1` → vế đầu sai, `and` cần cả hai nên → `False`.
* Dấu ngoặc quan trọng: nó gom nhóm "trừ khi..." trước khi kết hợp với `and`.

**Độ phức tạp:** O(1).

---

### Bài 18: Điểm trung bình có trọng số

**Phân tích:** Toán hệ số 2, Văn hệ số 1: `(8*2 + 7) / 3 = 23 / 3 = 7.666...` → 7.67.

**Ý tưởng:** Nhân hệ số, cộng tổng, rồi chia cho tổng hệ số; làm tròn 2 chữ số.

**Thuật toán:**
1. Gán `diem_toan = 8`, `diem_van = 7`.
2. Tính trung bình theo công thức `(diem_toan * 2 + diem_van) / 3`.
3. Làm tròn 2 chữ số và in.

**Code:**

```python
# Điểm từng môn
diem_toan = 8
diem_van = 7
# Toán hệ số 2, Văn hệ số 1 -> chia cho tổng hệ số (3)
tb = (diem_toan * 2 + diem_van) / 3
# Làm tròn 2 chữ số thập phân
print(round(tb, 2))   # 7.67
```

**Giải thích code:**
* `(8 * 2 + 7) / 3 = 23 / 3 = 7.6666666...`.
* `round(7.666..., 2) = 7.67` — làm tròn 2 chữ số sau dấu phẩy.
* Dấu ngoặc bao hết tử số: nếu thiếu ngoặc, Python sẽ tính `8 * 2 + 7 / 3` sai hoàn toàn.

**Độ phức tạp:** O(1).

---

### Bài 19: Tiền lãi kép 3 tháng

**Phân tích:** Gửi 1.000.000đ, mỗi tháng số dư tăng thêm 1,2% — lãi cộng dồn vào gốc (lãi kép).

**Ý tưởng:** Mỗi tháng thực hiện `tien += tien * 0.012`; gốc mới của tháng sau được tính trên gốc đã cộng lãi.

**Thuật toán:**
1. Khởi tạo `tien = 1000000`.
2. Tháng 1: `tien += tien * 0.012`, in.
3. Tháng 2: `tien += tien * 0.012`, in.
4. Tháng 3: `tien += tien * 0.012`, in.

**Code:**

```python
# Số tiền gửi ban đầu
tien = 1000000

# Tháng 1: cộng 1.2% của số dư hiện tại
tien += tien * 0.012
print("Sau thang 1:", tien)

# Tháng 2: lãi tính trên số dư đã tăng (lãi kép)
tien += tien * 0.012
print("Sau thang 2:", tien)

# Tháng 3
tien += tien * 0.012
print("Sau thang 3:", tien)
```

**Giải thích code:**
* Tháng 1: `1000000 + 12000 = 1012000.0`.
* Tháng 2: `1012000 + 12144 = 1024144.0`.
* Tháng 3: `1024144 + 12289.728 = 1036433.728`.
* Vì lãi tính trên **số dư mới** mỗi tháng nên số tiền tăng dần — đó chính là **lãi kép**, khác hẳn lãi đơn cố định 12.000đ/tháng.

**Độ phức tạp:** O(1).

---

### Bài 20: Kiểm tra con số "may mắn"

**Phân tích:** Số 28 cần kiểm tra qua 5 biểu thức kết hợp `and`/`or`/`not` và phép `%` — tất cả đều đúng (True).

**Ý tưởng:** Viết từng biểu thức vào biến riêng để dễ đọc, in kèm nhãn "Cau i".

**Thuật toán:**
1. Gán `so = 28`.
2. Tính và in lần lượt 5 biểu thức theo yêu cầu.

**Code:**

```python
# Con số cần kiểm tra
so = 28

# 1. Số chẵn VÀ nhỏ hơn 30
cau_1 = so % 2 == 0 and so < 30
# 2. Lớn hơn 20 HOẶC chia hết cho 7
cau_2 = so > 20 or so % 7 == 0
# 3. KHÔNG nhỏ hơn 10 (tức là lớn hơn hoặc bằng 10)
cau_3 = not (so < 10)
# 4. Chia hết cho 4
cau_4 = so % 4 == 0
# 5. Chia hết cho 4 VÀ (chia hết cho 2 HOẶC lớn hơn 30)
cau_5 = so % 4 == 0 and (so % 2 == 0 or so > 30)

print("Cau 1:", cau_1)
print("Cau 2:", cau_2)
print("Cau 3:", cau_3)
print("Cau 4:", cau_4)
print("Cau 5:", cau_5)
```

**Giải thích code:**
* Cau 1: `28 % 2 == 0` (True) `and 28 < 30` (True) → `True`.
* Cau 2: `28 > 20` (True) `or 28 % 7 == 0` (True) → `True`.
* Cau 3: `not (28 < 10)` → `not False` → `True`.
* Cau 4: `28 % 4 = 0` → `True`.
* Cau 5: trong ngoặc `28 % 2 == 0` (True) `or ...` (không cần xét) → `True`; `and` với `True` → `True`.
* Lưu ý thứ tự ưu tiên: `and` tính trước `or` nên dùng ngoặc để gom nhóm rõ ràng.

**Độ phức tạp:** O(1).

---

## 📌 Lời khuyên cuối

* **`//` và `%` là "cặp bài trùng":** cứ hỏi "bao nhiêu chẵn" thì `//`, "còn dư mấy" thì `%`.
* **`==` để hỏi, `=` để gán** — một trong những nhầm lẫn tốn thời gian nhất của người mới.
* **`and`/`or`/`not`** giúp gộp nhiều điều kiện; nhớ `and` yêu cầu tất cả, `or` chỉ cần một.
* **Khi biểu thức dài, hãy thêm ngoặc tròn** — vừa đúng, vừa dễ đọc, không cần học thuộc thứ tự ưu tiên.
* Bài tiếp theo bạn sẽ học **nhập dữ liệu** bằng `input()` — lúc đó mọi phép tính của bài này sẽ trở nên sống động hơn nhiều!

👉 Tiếp theo: **[Bài 7: Nhập Xuất Dữ Liệu](../07_Input_Output/bai_giang.md)**