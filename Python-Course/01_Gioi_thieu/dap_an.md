# ✅ Bài 1: Đáp Án – Giới Thiệu Python

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án để việc học hiệu quả nhất.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Xin chào thế giới

**Phân tích:** Bài tập làm quen đơn giản nhất — in một dòng chữ ra màn hình.

**Ý tưởng:** Dùng lệnh `print()` với chuỗi ký tự bên trong dấu ngoặc kép.

**Thuật toán:**
1. Gọi lệnh `print()`.
2. Truyền vào chuỗi cần in.

**Code:**

```python
print("Xin chao the gioi Python")
```

**Giải thích code:**
* `print(...)` — lệnh in dữ liệu ra màn hình.
* `"Xin chao the gioi Python"` — chuỗi ký tự cần hiển thị, nằm trong dấu ngoặc kép thẳng.

**Độ phức tạp:** O(1).

---

### Bài 2: Giới thiệu bản thân

**Phân tích:** Cần in 3 dòng thông tin khác nhau.

**Ý tưởng:** Mỗi dòng là một lệnh `print()` riêng biệt — Python in lần lượt từng dòng.

**Thuật toán:**
1. In dòng họ tên.
2. In dòng tuổi.
3. In dòng môn học yêu thích.

**Code:**

```python
# In dòng họ tên
print("Ten: Nguyen Van A")
# In dòng tuổi
print("Tuoi: 15")
# In dòng môn học yêu thích
print("Mon yeu thich: Tin hoc")
```

**Giải thích code:**
* Ba lệnh `print()` chạy lần lượt từ trên xuống dưới.
* Mỗi lệnh kết thúc sẽ **xuống dòng** tự động — đó là hành vi mặc định của `print()`.

**Độ phức tạp:** O(1).

---

### Bài 3: Phép tính nhanh

**Phân tích:** Python tính toán được phép toán số học ngay bên trong `print()`.

**Ý tưởng:** Truyền biểu thức số học vào `print()`; Python tính ra kết quả rồi mới in.

**Thuật toán:**
1. In kết quả `25 + 17`.
2. In kết quả `100 - 45`.

**Code:**

```python
print(25 + 17)
print(100 - 45)
```

**Giải thích code:**
* `25 + 17` — phép cộng, Python tính ra `42`.
* `100 - 45` — phép trừ, Python tính ra `55`.
* Lưu ý: không cần dấu ngoặc kép vì đây là **số**, không phải **chữ**.

**Độ phức tạp:** O(1).

---

### Bài 4: Ngày và tháng

**Phân tích:** In nhiều dòng thông tin về ngày giờ tùy theo mốc thời gian bạn chọn.

**Ý tưởng:** Dùng `print()` cho từng dòng.

**Thuật toán:**
1. In dòng thứ trong tuần.
2. In dòng ngày – tháng.

**Code:**

```python
print("Hom nay la thu Hai")
print("Ngay 5 thang 8")
```

**Giải thích code:**
* Dòng 1: in ra thứ trong tuần.
* Dòng 2: in ra ngày và tháng.
* Mỗi `print()` xuống dòng tự động nên hai dòng hiển thị riêng biệt.

**Độ phức tạp:** O(1).

---

### Bài 5: Vẽ hình chữ nhật bằng dấu `*`

**Phân tích:** Hình chữ nhật 4 hàng × 6 cột, mỗi hàng giống hệt nhau.

**Ý tưởng:** In 4 lần chuỗi 6 dấu `*` giống nhau.

**Thuật toán:**
1. In hàng thứ nhất: 6 dấu `*`.
2. Lặp lại cho đến hàng thứ tư.

**Code:**

```python
print("******")
print("******")
print("******")
print("******")
```

**Giải thích code:**
* Mỗi dòng `print("******")` in đúng 6 dấu `*`.
* Bốn lệnh tạo ra 4 hàng — đủ hình chữ nhật 4×6.

**Độ phức tạp:** O(1).

---

### Bài 6: Vẽ tam giác đơn giản

**Phân tích:** Tam giác 3 tầng: tầng 1 có 1 dấu `*`, tầng 2 có 2, tầng 3 có 3.

**Ý tưởng:** Số dấu `*` tăng dần theo từng hàng.

**Thuật toán:**
1. In hàng 1 dấu `*`.
2. In hàng 2 dấu `*`.
3. In hàng 3 dấu `*`.

**Code:**

```python
print("*")
print("**")
print("***")
```

**Giải thích code:**
* `"*"` — 1 ký tự.
* `"**"` — 2 ký tự.
* `"***"` — 3 ký tự.
* Ba hàng chồng lên nhau tạo hình tam giác hướng trái.

**Độ phức tạp:** O(1).

---

### Bài 7: In ra con số 2026

**Phân tích:** Đây là bài phân biệt in **số** và in **chuỗi chữ**.

**Ý tưởng:** In số trực tiếp, không bọc trong dấu nháy.

**Thuật toán:**
1. Gọi `print()` với đối số là số nguyên.

**Code:**

```python
print(2026)
```

**Giải thích code:**
* `2026` — số nguyên (`int`), không cần dấu ngoặc kép.
* Nếu viết `"2026"` thì máy in chữ "2026" — nhìn giống nhau nhưng về bản chất khác: một cái là số để tính toán, một cái chỉ là ký tự.

**Độ phức tạp:** O(1).

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Chương trình tính điểm

**Phân tích:** In chuỗi chữ kèm kết quả phép tính.

**Ý tưởng:** Dùng `print()` với nhiều đối số cách nhau dấu phẩy; Python tự thêm khoảng trắng giữa các đối số.

**Thuật toán:**
1. In nhãn "Tong diem 3 mon la:".
2. In kết quả `10 + 8 + 7` ngay sau đó.

**Code:**

```python
print("Tong diem 3 mon la:", 10 + 8 + 7)
```

**Giải thích code:**
* `"Tong diem 3 mon la:"` — phần chữ.
* `10 + 8 + 7` — Python tính ra `25`.
* Dấu phẩy ngăn cách hai đối số, Python tự chèn một khoảng trắng giữa chúng.

**Độ phức tạp:** O(1).

---

### Bài 9: Tính trung bình cộng

**Phân tích:** Tính tổng rồi chia cho số lượng phần tử.

**Ý tưởng:** Tổng = `12 + 15 + 18`, trung bình = tổng / 3. Phép chia luôn cho kết quả số thực (`float`).

**Thuật toán:**
1. In tổng số kẹo.
2. In trung bình cộng.

**Code:**

```python
print("Tong keo:", 12 + 15 + 18)
print("Trung binh:", (12 + 15 + 18) / 3)
```

**Giải thích code:**
* Dòng 1: `12 + 15 + 18 = 45`.
* Dòng 2: `45 / 3 = 15.0` — có dấu `.0` vì phép chia `/` luôn trả về số thực.
* Dấu ngoặc `( )` giúp Python tính tổng trước khi chia.

**Độ phức tạp:** O(1).

---

### Bài 10: Bảng cửu chương nhân 5

**Phân tích:** In 3 dòng dạng `5 x k = kết quả`.

**Ý tưởng:** Đối số thứ ba của `print()` là phép nhân `5 * k` — Python tính rồi in.

**Thuật toán:**
1. In `5 x 1 = 5`.
2. In `5 x 2 = 10`.
3. In `5 x 3 = 15`.

**Code:**

```python
print("5 x 1 =", 5 * 1)
print("5 x 2 =", 5 * 2)
print("5 x 3 =", 5 * 3)
```

**Giải thích code:**
* `5 * 1` → `5`, `5 * 2` → `10`, `5 * 3` → `15`.
* Dấu `*` là phép **nhân** trong Python (không phải `x` như toán học thông thường).

**Độ phức tạp:** O(1).

---

### Bài 11: In cách nhau bởi dấu phẩy

**Phân tích:** In nhiều chuỗi trên cùng một dòng.

**Ý tưởng:** Truyền nhiều đối số cho `print()`, ngăn cách bằng dấu phẩy.

**Thuật toán:**
1. Gọi `print()` với 3 chuỗi.

**Code:**

```python
print("Python", "Java", "C++")
```

**Giải thích code:**
* Ba chuỗi cách nhau bằng dấu phẩy — Python in chúng liền một dòng.
* Python tự thêm **một khoảng trắng** giữa các đối số.

**Độ phức tạp:** O(1).

---

### Bài 12: Đếm ngược

**Phân tích:** In 4 dòng: 3 số và một dòng chữ.

**Ý tưởng:** Bốn lệnh `print()` tuần tự.

**Thuật toán:**
1. In `3`.
2. In `2`.
3. In `1`.
4. In `Chay!`.

**Code:**

```python
print(3)
print(2)
print(1)
print("Chay!")
```

**Giải thích code:**
* Các số in ra không cần dấu nháy; dòng chữ cần dấu nháy.
* Thứ tự lệnh chạy từ trên xuống tạo cảm giác đếm ngược.

**Độ phức tạp:** O(1).

---

### Bài 13: Tìm chỗ sai (Debug)

**Phân tích:** Chương trình có 2 lỗi cú pháp.

**Ý tưởng:** Xác định từng lỗi:
1. `Print` — sai vì Python phân biệt hoa – thường, phải là `print`.
2. `print(Toi 15 tuoi")` — thiếu dấu mở nháy, dấu nháy đặt sai vị trí.

**Thuật toán:**
1. Sửa `Print` thành `print`.
2. Đặt dấu nháy đúng cho chuỗi.

**Code:**

```python
print("Ten toi la An")
print("Toi 15 tuoi")
```

**Giải thích code:**
* Lỗi 1: `Print("...")` → `print("...")` — lệnh Python viết thường.
* Lỗi 2: `print(Toi 15 tuoi")` → `print("Toi 15 tuoi")` — chuỗi phải nằm trọn trong cặp dấu nháy.

**Độ phức tạp:** O(1).

---

### Bài 14: In ra thông tin trường học

**Phân tích:** In 4 dòng thông tin dạng nhãn: giá trị.

**Ý tưởng:** Mỗi dòng là một `print("Nhan:", "gia tri")`.

**Thuật toán:**
1. In tên trường.
2. In địa chỉ.
3. In lớp.
4. In số điện thoại.

**Code:**

```python
print("Truong:", "THPT Python")
print("Dia chi:", "123 Nguyen Hue, TP HCM")
print("Lop:", "10A1")
print("So dien thoai:", "0901 234 567")
```

**Giải thích code:**
* Mỗi `print()` có hai đối số: nhãn và giá trị, ngăn cách bởi dấu phẩy.
* Địa chỉ và số điện thoại là chữ nên phải đặt trong dấu nháy.

**Độ phức tạp:** O(1).

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: In ra số đã làm tròn

**Phân tích:** Chu vi hình tròn = `2 * pi * r` với pi ≈ 3.14. Kết quả `31.400000...` cần làm tròn về 31.4.

**Ý tưởng:** Lưu kết quả vào biến, dùng hàm `round(x, 2)` làm tròn 2 chữ số thập phân.

**Thuật toán:**
1. Tính chu vi: `chu_vi = 2 * 3.14 * 5`.
2. Làm tròn: `round(chu_vi, 2)`.
3. In kết quả.

**Code:**

```python
# Bán kính hình tròn
r = 5
# Tính chu vi: 2 * pi * r
chu_vi = 2 * 3.14 * r
# Làm tròn tới 2 chữ số thập phân rồi in
print("Chu vi:", round(chu_vi, 2))
```

**Giải thích code:**
* `r = 5` — biến lưu bán kính.
* `2 * 3.14 * r` — phép tính cho ra `31.4`.
* `round(chu_vi, 2)` — giữ 2 chữ số sau dấu phẩy, kết quả `31.4`.

**Độ phức tạp:** O(1).

---

### Bài 16: Bảng thông báo trường học

**Phân tích:** Cần in viền trên/dưới và các dòng nội dung có lề.

**Ý tưởng:** Mỗi dòng là một `print()`. Dùng dấu phẩy để Python tự căn khoảng trắng giữa `|` và nội dung.

**Thuật toán:**
1. In dòng viền trên.
2. In từng dòng nội dung kèm dấu `|`.
3. In dòng viền dưới.

**Code:**

```python
# Vẽ bảng thông báo
print("==============================")
print("|", "TRUONG THPT PYTHON", "|")
print("|", "Khai giang: 05/09/2026", "|")
print("|", "Chuan bi giay to can thiet", "|")
print("==============================")
```

**Giải thích code:**
* `print("==...")` — dòng viền trên và dưới giống nhau.
* `print("|", "TRUONG THPT PYTHON", "|")` — dấu phẩy tạo khoảng trắng đều hai bên nội dung.
* Nếu muốn căn chính xác từng cột, có thể cộng chuỗi bằng `+` và tự thêm khoảng trắng.

**Độ phức tạp:** O(1).

---

### Bài 17: Tách số thành chữ số

**Phân tích:** Cần lấy từng chữ số của số 12345. Vì đây là chữ số nên cách đơn giản nhất là đổi thành chuỗi rồi truy cập từng vị trí.

**Ý tưởng:** `str(12345)` cho chuỗi `"12345"`; lấy ký tự thứ `i` bằng cú pháp `chuoi[i]` với vị trí bắt đầu từ 0.

**Thuật toán:**
1. Đổi số sang chuỗi.
2. Lấy lần lượt vị trí 0 → 4 và in ra.

**Code:**

```python
# Đổi số sang chuỗi để lấy từng chữ số
so = str(12345)
# Lấy từng ký tự theo vị trí (bắt đầu từ 0)
print(so[0])
print(so[1])
print(so[2])
print(so[3])
print(so[4])
```

**Giải thích code:**
* `str(12345)` → `"12345"`.
* `so[0]` → `"1"`, `so[1]` → `"2"`, ... `so[4]` → `"5"`.
* Vị trí chuỗi bắt đầu từ **0**, không phải 1 — đây là quy tắc quan trọng trong lập trình.

**Độ phức tạp:** O(1).

---

### Bài 18: Vẽ ngôi nhà

**Phân tích:** Ngôi nhà gồm mái tam giác 4 tầng (mỗi tầng thêm 2 dấu `*` và bớt 1 dấu cách) và thân hình chữ nhật 4×7.

**Ý tưởng:** Tự đếm khoảng trắng cho mái; thân nhà đơn giản là 4 dòng 7 dấu `*`.

**Thuật toán:**
1. Vẽ mái: từ 3 dấu cách + 1 `*`, giảm dần cách, tăng dần `*`.
2. Vẽ thân: 4 dòng `*******`.

**Code:**

```python
# Mái nhà - tam giác
print("   *")
print("  ***")
print(" *****")
print("*******")
# Thân nhà - hình chữ nhật
print("*******")
print("*******")
print("*******")
print("*******")
```

**Giải thích code:**
* Mái: hàng 1 có 3 dấu cách + 1 `*`; hàng 4 có 0 dấu cách + 7 `*`.
* Thân: 4 hàng giống nhau, mỗi hàng 7 dấu `*` — khớp đáy mái.

**Độ phức tạp:** O(1).

---

### Bài 19: In tên viết tắt

**Phân tích:** Tên "Nguyen Van An" viết tắt thành "NVA" — lấy chữ cái đầu mỗi từ.

**Ý tưởng:** Lấy ký tự vị trí 0 của mỗi từ rồi nối bằng `+`.

**Thuật toán:**
1. Lấy `"Nguyen"[0]` = `"N"`.
2. Lấy `"Van"[0]` = `"V"`.
3. Lấy `"An"[0]` = `"A"`.
4. Nối ba ký tự và in.

**Code:**

```python
# Lấy chữ cái đầu của mỗi từ rồi nối lại
viet_tat = "Nguyen"[0] + "Van"[0] + "An"[0]
print(viet_tat)
```

**Giải thích code:**
* `"Nguyen"[0]` — vị trí 0 là ký tự đầu tiên.
* `+` — phép **nối chuỗi** (không phải phép cộng số).
* Kết quả: `"N" + "V" + "A" = "NVA"`.

**Độ phức tạp:** O(1).

---

### Bài 20: Thiết kế khung giờ tự học

**Phân tích:** Cần in viền trên/dưới và các dòng buổi – môn học với cột thẳng hàng.

**Ý tưởng:** Dùng `print()` nhiều lần; thêm khoảng trắng để căn cột môn học thẳng lề.

**Thuật toán:**
1. In viền trên.
2. In từng dòng buổi – môn.
3. In viền dưới.

**Code:**

```python
# Khung giờ tự học
print("------------------------------")
print("| Sang | Toan                |")
print("| Trua | Van                 |")
print("| Chieu| Tin hoc             |")
print("------------------------------")
```

**Giải thích code:**
* Dấu `|` tạo cột; khoảng trắng thủ công để cột môn học thẳng hàng.
* Viền trên và dưới giống hệt nhau tạo khung đóng kín.
* Chú ý: `"| Chieu|"` — muốn thẳng cột phải canh độ dài của từng buổi trong dấu `|`.

**Độ phức tạp:** O(1).

---

## 📌 Lời khuyên cuối

* Mọi lệnh `print()` phải có dấu ngoặc tròn.
* Chuỗi chữ cần dấu nháy thẳng `"` hoặc `'`; số thì không cần.
* Python phân biệt hoa – thường: `print` đúng, `Print` sai.
* Luyện viết **biến** (đã thấy ở bài 15, 17, 19) — bài sau sẽ học kỹ hơn về biến!

👉 Tiếp theo: **[Bài 2: Cài đặt Python](../02_Cai_dat_Python/bai_giang.md)**