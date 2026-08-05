# ✅ Bài 4: Đáp Án – Biến Trong Python

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án để việc học hiệu quả nhất.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Chiếc hộp đầu tiên

**Phân tích:** Khai báo biến và in giá trị ra màn hình.

**Ý tưởng:** Gán chuỗi vào biến `lop`, rồi dùng `print()`.

**Thuật toán:**
1. Gán `"10A1"` cho biến `lop`.
2. In biến `lop`.

**Code:**

```python
# Gán chuỗi cho biến lop
lop = "10A1"
# In giá trị trong biến lop
print(lop)
```

**Giải thích code:**

* `lop = "10A1"` — tạo hộp `lop`, bỏ chuỗi `"10A1"` vào.
* `print(lop)` — in giá trị bên trong hộp nên kết quả là `10A1` (không có dấu nháy).

**Độ phức tạp:** O(1).

---

### Bài 2: Điểm môn học

**Phân tích:** In nhãn chữ kèm giá trị biến số thực.

**Ý tưởng:** `print()` với hai đối số cách nhau dấu phẩy.

**Thuật toán:**
1. Gán `8.5` cho `diem`.
2. In nhãn và giá trị.

**Code:**

```python
# Gán điểm cho biến diem
diem = 8.5
# In nhãn rồi in giá trị biến
print("Diem cua toi la:", diem)
```

**Giải thích code:**

* `diem = 8.5` — số thực (`float`), viết dấu chấm chứ không phải dấu phẩy.
* Dấu phẩy trong `print()` giúp in chuỗi nhãn và giá trị biến trên cùng dòng, có khoảng trắng giữa chúng.

**Độ phức tạp:** O(1).

---

### Bài 3: Đổi nội dung hộp

**Phân tích:** Biến được gán hai lần — giá trị sau ghi đè giá trị trước.

**Ý tưởng:** Gán `5` cho `so`, rồi gán lại `10`; in ra giá trị mới nhất.

**Thuật toán:**
1. Gán `so = 5`.
2. Gán lại `so = 10`.
3. In `so`.

**Code:**

```python
so = 5       # lần gán thứ nhất
so = 10      # lần gán thứ hai - ghi đè giá trị cũ
print(so)    # in giá trị mới nhất
```

**Giải thích code:**

* Sau lệnh thứ hai, hộp `so` chứa `10`, giá trị `5` bị thay thế hoàn toàn.
* Python in ra giá trị **hiện tại cuối cùng** của biến.

**Độ phức tạp:** O(1).

---

### Bài 4: Đặt tên đúng hay sai

**Phân tích:** Tên biến bắt đầu bằng chữ số nên bị `SyntaxError`.

**Ý tưởng:** Đưa chữ số về cuối tên hoặc dùng gạch dưới.

**Thuật toán:**
1. Đổi `1ten` thành `ten1`.
2. Sửa cả ở lệnh `print`.

**Code:**

```python
ten1 = "An"      # tên biến tận cùng bằng số là hợp lệ
print(ten1)
```

**Giải thích code:**

* `ten1` — chữ số đứng sau chữ cái nên hợp lệ.
* Cả khai báo và in phải dùng cùng một tên, cùng kiểu viết hoa – thường.

**Độ phức tạp:** O(1).

---

### Bài 5: Ba biến, ba món quà

**Phân tích:** Gán nhiều biến cùng lúc trên một dòng.

**Ý tưởng:** Dùng cú pháp `a, b, c = 1, 2, 3`.

**Thuật toán:**
1. Gán ba biến.
2. In cả ba.

**Code:**

```python
# Gán 3 biến cùng lúc
a, b, c = 1, 2, 3
# In cả ba giá trị
print(a, b, c)
```

**Giải thích code:**

* `a, b, c = 1, 2, 3` — Python gán lần lượt theo thứ tự: `a=1`, `b=2`, `c=3`.
* `print(a, b, c)` in ba số trên một dòng, ngăn cách bởi khoảng trắng.

**Độ phức tạp:** O(1).

---

### Bài 6: Tổng hai số

**Phân tích:** Tính tổng hai biến rồi lưu vào biến thứ ba.

**Ý tưởng:** `tong = x + y` — Python tính `12 + 30` trước, rồi gán `42` cho `tong`.

**Thuật toán:**
1. Gán `x`, `y`.
2. Tính và gán `tong`.
3. In câu kết quả.

**Code:**

```python
x = 12
y = 30
# Tính tổng và gán cho biến tong
tong = x + y
print("Tong la:", tong)
```

**Giải thích code:**

* `tong = x + y` — vế phải được tính trước (`42`), sau đó mới gán vào biến `tong`.
* Nhờ biến `tong`, giá trị tổng được lưu lại để dùng ở lệnh in.

**Độ phức tạp:** O(1).

---

### Bài 7: Tên biến viết thường

**Phân tích:** Luyện chuẩn `snake_case` — chữ thường và dấu gạch dưới.

**Ý tưởng:** `TenTruong` → `ten_truong`.

**Thuật toán:**
1. Gán giá trị cho `ten_truong`.
2. In biến.

**Code:**

```python
# Tên biến theo chuẩn snake_case
ten_truong = "THPT Python"
print(ten_truong)
```

**Giải thích code:**

* `snake_case`: chữ thường, nhiều từ nối bằng `_`.
* Giá trị chuỗi giữ nguyên chữ hoa trong nội dung — chỉ tên biến mới viết thường.

**Độ phức tạp:** O(1).

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Hoán đổi bằng biến tạm

**Phân tích:** Đổi giá trị hai biến cần "cốc thứ ba" để không mất dữ liệu.

**Ý tưởng:** Sao chép `a` sang `tam`, đổ `b` vào `a`, đổ `tam` vào `b`.

**Thuật toán:**
1. `tam = a` — giữ giá trị cũ của `a`.
2. `a = b` — `a` nhận giá trị của `b`.
3. `b = tam` — `b` nhận giá trị cũ của `a`.

**Code:**

```python
a = 3
b = 7
# Dùng biến tạm để hoán đổi
tam = a
a = b
b = tam
print(a, b)
```

**Giải thích code:**

* Nếu viết `a = b` trước thì giá trị `a = 3` sẽ biến mất — nên phải giữ ở `tam`.
* Sau ba lệnh gán, `a = 7`, `b = 3`.

**Độ phức tạp:** O(1).

---

### Bài 9: Hoán đổi kiểu Python

**Phân tích:** Hoán đổi hai biến trong một dòng duy nhất.

**Ý tưởng:** `x, y = y, x` — Python tự xử lý việc "mượn cốc" bên trong.

**Thuật toán:**
1. Gán `x`, `y`.
2. Hoán đổi bằng `x, y = y, x`.
3. In kết quả.

**Code:**

```python
x = "banh mi"
y = "pho"
# Hoán đổi hai biến - một dòng duy nhất
x, y = y, x
print(x, y)
```

**Giải thích code:**

* `x, y = y, x` — vế phải được đánh giá trước (`"pho", "banh mi"`), sau đó mới gán lần lượt cho `x`, `y`.
* Kết quả in ra: `pho banh mi`.

**Độ phức tạp:** O(1).

---

### Bài 10: Ví tiền trong một ngày

**Phân tích:** Cập nhật biến liên tục theo các sự kiện trong ngày.

**Ý tưởng:** Mỗi lần chi tiêu hoặc nhận tiền, gán lại `tien = tien ± số tiền`.

**Thuật toán:**
1. `tien = 200000` — khởi tạo.
2. Trừ tiền mua cơm.
3. Trừ tiền mua sách.
4. Cộng tiền mẹ cho.
5. In kết quả.

**Code:**

```python
tien = 200000              # sáng có 200.000 đồng
tien = tien - 45000        # mua cơm trưa
tien = tien - 80000        # mua sách chiều
tien = tien + 100000       # mẹ cho thêm buổi tối
print("So tien con lai:", tien)
```

**Giải thích code:**

* `tien = tien - 45000` — lấy giá trị hiện tại (200000) trừ 45000, gán kết quả (155000) ngược về hộp `tien`.
* Qua mỗi lần gán, hộp `tien` được cập nhật: 200000 → 155000 → 75000 → 175000.

**Độ phức tạp:** O(1).

---

### Bài 11: Điểm trung bình hai môn

**Phân tích:** Trung bình cộng hai số = tổng chia 2.

**Ý tưởng:** `(diem_toan + diem_van) / 2` — dấu ngoặc đảm bảo tính tổng trước.

**Thuật toán:**
1. Gán hai điểm.
2. Tính trung bình.
3. In kết quả.

**Code:**

```python
diem_toan = 9
diem_van = 7
# Trung bình cộng hai môn
trung_binh = (diem_toan + diem_van) / 2
print("Trung binh:", trung_binh)
```

**Giải thích code:**

* `(9 + 7) / 2 = 16 / 2 = 8.0`.
* Phép chia `/` luôn cho số thực nên kết quả in ra là `8.0`.

**Độ phức tạp:** O(1).

---

### Bài 12: Chỉnh sửa chỗ sai

**Phân tích:** Hai lỗi: tên biến chứa dấu cách và lệnh `print` dùng sai tên.

**Ý tưởng:** Chuẩn hóa tên theo `snake_case` cho cả khai báo và in.

**Thuật toán:**
1. Đổi `so qua` thành `so_qua`.
2. Sửa `print` dùng đúng `so_qua`.

**Code:**

```python
so_qua = 5        # tên biến không chứa dấu cách
print(so_qua)
```

**Giải thích code:**

* `so_qua` — dấu gạch dưới thay cho dấu cách.
* Code gốc viết `print(so_qua)` nhưng khai báo `so qua` (có dấu cách) nên Python báo `SyntaxError` ngay ở dòng khai báo; sau khi sửa, in ra `5`.

**Độ phức tạp:** O(1).

---

### Bài 13: Tìm ra con số lớn hơn

**Phân tích:** Dùng hàm có sẵn `max()` để chọn giá trị lớn nhất.

**Ý tưởng:** `lon_nhat = max(m, n)`.

**Thuật toán:**
1. Gán `m`, `n`.
2. Gán `lon_nhat = max(m, n)`.
3. In câu kết quả.

**Code:**

```python
m = 15
n = 9
# max() trả về giá trị lớn nhất giữa hai số
lon_nhat = max(m, n)
print("So lon hon:", lon_nhat)
```

**Giải thích code:**

* `max(15, 9)` trả về `15`.
* Kết quả lưu vào biến `lon_nhat` rồi mới in — tách bạch tính toán và hiển thị.

**Độ phức tạp:** O(1).

---

### Bài 14: Đổi đơn vị giờ – phút

**Phân tích:** 135 phút = số giờ nguyên + phút thừa. Dùng phép chia lấy nguyên `//` và lấy dư `%`.

**Ý tưởng:** `gio = phut // 60`, `phut_con = phut % 60`.

**Thuật toán:**
1. Khởi tạo `phut = 135`.
2. Tính số giờ.
3. Tính số phút thừa.
4. In kết quả.

**Code:**

```python
phut = 135
# 1 giờ = 60 phút: chia lấy nguyên để ra số giờ
gio = phut // 60
# Phần dư là số phút còn thừa
phut_con = phut % 60
print("135 phut =", gio, "gio", phut_con, "phut")
```

**Giải thích code:**

* `135 // 60 = 2` (bỏ phần lẻ).
* `135 % 60 = 15` (phần dư).
* `print` với nhiều đối số tạo dòng kết quả hoàn chỉnh.

**Độ phức tạp:** O(1).

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Hoán đổi không cần biến tạm (phiên bản tay đôi)

**Phân tích:** Dùng phép cộng – trừ để hoán đổi hai số mà không cần biến phụ.

**Ý tưởng:** Gộp hai giá trị vào `a`, sau đó khôi phục lần lượt từng biến.

**Thuật toán:**
1. `a = a + b` → `a = 13`.
2. `b = a - b` → `b = 13 - 9 = 4` (giá trị cũ của b đã được lưu trong `a`).
3. `a = a - b` → `a = 13 - 4 = 9`.

**Code:**

```python
a = 4
b = 9
# Hoán đổi bằng phép cộng và trừ
a = a + b    # a = 4 + 9 = 13
b = a - b    # b = 13 - 9 = 4
a = a - b    # a = 13 - 4 = 9
print("a =", a, ", b =", b)
```

**Giải thích code:**

* Ở bước 2, `b` vẫn giữ giá trị gốc `9` khi được dùng trong phép trừ, vì phép tính lấy giá trị trước khi gán.
* Kết quả: `a = 9, b = 4`.
* ⚠️ Hạn chế: cách này chỉ đúng với **số**; với chuỗi ký tự thì phép `+ -` không dùng được — vì vậy cách an toàn nhất vẫn là `a, b = b, a` hoặc biến tạm.

**Độ phức tạp:** O(1).

---

### Bài 16: Kiểm tra `id()` của biến

**Phân tích:** `id(bien)` trả về địa chỉ vùng nhớ. `y = x` sao chép giá trị nên hai biến trỏ tới cùng đối tượng ban đầu.

**Ý tưởng:** So sánh `id(x)` và `id(y)` trước và sau khi đổi giá trị `y`.

**Thuật toán:**
1. Gán `x = 1000`, `y = x`.
2. In `id` của cả hai và so sánh.
3. Gán `y = 2000`, in lại.

**Code:**

```python
x = 1000
y = x                 # y sao chép giá trị của x
print("id(x) =", id(x))
print("id(y) =", id(y))
print("id(x) == id(y):", id(x) == id(y))
# Đổi giá trị y
y = 2000
print("Sau khi y doi gia tri:")
print("id(y) =", id(y))
print("id(x) == id(y):", id(x) == id(y))
```

**Giải thích code:**

* Ban đầu `x` và `y` cùng trỏ tới đối tượng `1000` nên `id` bằng nhau.
* Sau khi `y` nhận giá trị mới `2000`, Python tạo đối tượng khác cho `y` — địa chỉ thay đổi, `x` vẫn như cũ. Điều này chứng minh `b = a` là **sao chép giá trị**, không phải "kết nối" hai biến.

**Độ phức tạp:** O(1).

---

### Bài 17: Hóa đơn mua kẹo

**Phân tích:** Mua 4 gói, sau đó mua thêm 1 gói — tổng 5 gói, mỗi gói 12000.

**Ý tưởng:** Cập nhật số gói trước khi tính tiền, hoặc cộng trực tiếp vào số lượng.

**Thuật toán:**
1. Khởi tạo `so_goi_keo = 4`, `gia_goi = 12000`.
2. Cập nhật `so_goi_keo = so_goi_keo + 1`.
3. Tính `tong_tien = so_goi_keo * gia_goi`.
4. In kết quả.

**Code:**

```python
so_goi_keo = 4
gia_goi = 12000
# Mua thêm 1 gói nữa
so_goi_keo = so_goi_keo + 1
# Tính tổng tiền
tong_tien = so_goi_keo * gia_goi
print("Tong tien:", tong_tien)
```

**Giải thích code:**

* `so_goi_keo + 1` → `5`, gán lại vào biến.
* `5 * 12000 = 60000`.
* Nếu không cập nhật biến mà vẫn dùng giá trị cũ thì kết quả sẽ nhầm (40000).

**Độ phức tạp:** O(1).

---

### Bài 18: Thời khóa biểu dùng biến

**Phân tích:** Hoán đổi `mon1` và `mon3`, giữ nguyên `mon2`.

**Ý tưởng:** `mon1, mon3 = mon3, mon1`.

**Thuật toán:**
1. Khởi tạo 3 biến.
2. Hoán đổi `mon1` và `mon3`.
3. In cả ba.

**Code:**

```python
mon1 = "Toan"
mon2 = "Van"
mon3 = "Tin"
# Hoán đổi môn thứ 1 và thứ 3
mon1, mon3 = mon3, mon1
print(mon1, mon2, mon3)
```

**Giải thích code:**

* Trước: `mon1="Toan"`, `mon3="Tin"`. Sau hoán đổi: `mon1="Tin"`, `mon3="Toan"`.
* `mon2` không đổi nên dòng in ra `Tin Van Toan`.

**Độ phức tạp:** O(1).

---

### Bài 19: Chương trình "sắp hàng" điểm số

**Phân tích:** Xếp hai điểm thành `cao` và `thap` bằng phép so sánh `if` đơn giản.

**Ý tưởng:** Giả định `cao = diem1`, nếu `diem1` nhỏ hơn `diem2` thì hoán đổi bằng biến tạm.

**Thuật toán:**
1. Gán `cao = diem1`, `thap = diem2`.
2. Nếu `diem1 < diem2` → dùng biến tạm hoán đổi hai biến.
3. In kết quả.

**Code:**

```python
diem1 = 5
diem2 = 8
cao = diem1
thap = diem2
# Nếu điểm 1 nhỏ hơn điểm 2 thì phải hoán đổi
if cao < thap:
    tam = cao
    cao = thap
    thap = tam
print("Cao:", cao, "- Thap:", thap)
```

**Giải thích code:**

* Câu lệnh `if cao < thap:` — nếu điều kiện đúng thì chạy khối phía dưới (thụt lề 4 dấu cách).
* Vì `5 < 8` nên hoán đổi: `cao = 8`, `thap = 5`.
* Đây là bước đệm cho Bài 8 – câu lệnh rẽ nhánh `if`.

**Độ phức tạp:** O(1).

---

### Bài 20: Mô phỏng "hộp số kẹo chia đôi"

**Phân tích:** Mỗi ngày số kẹo giảm 3 và tăng 2 → mạng lại lưới biết trước mỗi ngày.

**Ý tưởng:** Cập nhật `so_keo` liên tiếp 3 lần, mỗi lần in; cuối cùng kiểm tra số chẵn bằng `% 2 == 0`.

**Thuật toán:**
1. `so_keo = 25`.
2. Ngày 1: `so_keo = so_keo - 3 + 2` → 24, in.
3. Ngày 2: tiếp tục trừ 3 cộng 2 → 23, in.
4. Ngày 3: → 22, in và kiểm tra chẵn lẻ.

**Code:**

```python
so_keo = 25
# Ngày 1: ăn 3 viên, nhận thêm 2 viên
so_keo = so_keo - 3 + 2
print("Ngay 1:", so_keo)
# Ngày 2
so_keo = so_keo - 3 + 2
print("Ngay 2:", so_keo)
# Ngày 3
so_keo = so_keo - 3 + 2
print("Ngay 3:", so_keo)
# Kiểm tra số chẵn bằng phép chia lấy dư
so_le = not (so_keo % 2 == 0)
print("So keo con lai la so chan:", not so_le)
```

**Giải thích code:**

* `so_keo - 3 + 2` — Python tính trái sang phải: trừ trước rồi cộng (cũng tương đương `-1` mỗi ngày).
* `22 % 2 == 0` là `True` nên cờ số chẵn là `True`.
* Kết quả in ra lần lượt `24`, `23`, `22` và `True`.

**Độ phức tạp:** O(1).

---

## 📌 Lời khuyên cuối

* Mỗi biến nên có **một mục đích rõ ràng** và tên gọi dễ hiểu.
* Gặp `NameError` → kiểm tra đã gán biến chưa, tên có khớp hoa – thường không.
* Chuẩn `snake_case` là "nét chữ" của người viết Python chuyên nghiệp.
* `a, b = b, a` là câu thần chú hoán đổi — hãy dùng thoải mái.

👉 Tiếp theo: **[Bài 5: Kiểu Dữ Liệu Cơ Bản](../05_Kieu_du_lieu/bai_giang.md)**