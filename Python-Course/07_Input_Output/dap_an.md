# ✅ Bài 7: Đáp Án – Nhập và Xuất Dữ Liệu

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án để việc học hiệu quả nhất.
>
> 📌 Các chương trình dưới đây dùng `input()` — khi chạy thử, hãy nhập đúng giá trị mẫu ở dòng chú thích `# Nhập: ...`.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Máy chào hỏi

**Phân tích:** Nhận tên từ bàn phím rồi in lời chào có chứa tên.

**Ý tưởng:** Lưu kết quả `input()` vào biến, dùng f-string chèn tên vào câu chào.

**Thuật toán:**
1. Hỏi và nhận tên.
2. In câu chào với tên vừa nhận.

**Code:**

```python
# Nhập: Mai
# Hỏi tên người dùng
ten = input("Bạn tên gì? ")
# In lời chào có chèn tên
print(f"Xin chào {ten}!")
```

**Giải thích code:**
* `input("Bạn tên gì? ")` — hiện câu hỏi, chờ nhập, trả về chuỗi `"Mai"`.
* `f"Xin chào {ten}!"` — thay `{ten}` bằng giá trị biến → `Xin chào Mai!`.
* Tên là chuỗi nên không cần ép kiểu.

**Độ phức tạp:** O(1).

---

### Bài 2: Hỏi và in lại câu trả lời

**Phân tích:** Hỏi món ăn yêu thích và in lại trong một câu hoàn chỉnh.

**Ý tưởng:** Gán kết quả nhập vào biến, dùng f-string.

**Thuật toán:**
1. Hỏi món ăn.
2. In câu nhắc lại món ăn.

**Code:**

```python
# Nhập: Phở
# Hỏi món ăn yêu thích
mon_an = input("Bạn thích ăn gì? ")
# In câu nhắc lại món ăn
print(f"Hôm nay bạn sẽ ăn {mon_an} nhé!")
```

**Giải thích code:**
* Giá trị nhập `"Phở"` được lưu vào `mon_an`.
* f-string đưa biến vào đúng vị trí giữa câu: `Hôm nay bạn sẽ ăn Phở nhé!`.

**Độ phức tạp:** O(1).

---

### Bài 3: Cộng hai số

**Phân tích:** Nhập hai số nguyên, tính tổng và in kèm các số đã nhập.

**Ý tưởng:** Ép kiểu `int()` ngay trong lệnh nhập, tính tổng rồi in bằng f-string.

**Thuật toán:**
1. Nhập và ép kiểu `a`, `b`.
2. Tính `tong = a + b`.
3. In tổng.

**Code:**

```python
# Nhập: 7, 5
# Nhập hai số nguyên (ép kiểu ngay khi nhập)
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
# Tính tổng
tong = a + b
# In kết quả bằng f-string
print(f"Tổng của {a} và {b} là {tong}")
```

**Giải thích code:**
* Nếu không có `int()`, `"7" + "5"` sẽ nối chuỗi thành `"75"` — kết quả sai ngầm.
* `int(input(...))` — xử lý từ trong ra: `input` lấy chuỗi trước, `int` ép số sau.
* `{tong}` chèn kết quả phép cộng vào câu in.

**Độ phức tạp:** O(1).

---

### Bài 4: In liền một dòng với `end`

**Phân tích:** In cùng một chuỗi 3 lần trên một dòng, cách nhau bởi dấu cách.

**Ý tưởng:** Dùng `end=" "` để hai lần in đầu không xuống dòng.

**Thuật toán:**
1. Nhập chuỗi.
2. In lần 1 với `end=" "`.
3. In lần 2 với `end=" "`.
4. In lần 3 bình thường để kết thúc dòng.

**Code:**

```python
# Nhập: hoc
# Nhập chuỗi cần lặp lại
tu = input("Nhập từ cần lặp: ")
# In 3 lần trên cùng một dòng, cách nhau dấu cách
print(tu, end=" ")
print(tu, end=" ")
print(tu)
```

**Giải thích code:**
* `end=" "` thay ký tự xuống dòng mặc định bằng một dấu cách.
* Lần in cuối không chỉ định `end` nên tự xuống dòng — đầu ra gọn đẹp: `hoc hoc hoc`.

**Độ phức tạp:** O(1).

---

### Bài 5: Ngăn cách bằng `sep`

**Phân tích:** Nhập ba thông tin và in trên một dòng, ngăn cách bởi ` - `.

**Ý tưởng:** Truyền ba biến cho `print()` với `sep=" - "`.

**Thuật toán:**
1. Nhập tên, lớp, trường.
2. In ba biến với `sep=" - "`.

**Code:**

```python
# Nhập: Mai, 10A1, THPT Python
# Nhập ba thông tin cá nhân
ten = input("Nhập tên: ")
lop = input("Nhập lớp: ")
truong = input("Nhập trường: ")
# In trên một dòng, ngăn cách bởi " - "
print(ten, lop, truong, sep=" - ")
```

**Giải thích code:**
* Mặc định `print(a, b, c)` chèn dấu cách; `sep=" - "` thay dấu cách đó bằng ` - `.
* Kết quả: `Mai - 10A1 - THPT Python`.

**Độ phức tạp:** O(1).

---

### Bài 6: Diện tích hình chữ nhật

**Phân tích:** Nhập chiều dài, chiều rộng (số thực) và tính diện tích.

**Ý tưởng:** Ép `float` vì kích thước có thể là số thập phân; diện tích = dài × rộng.

**Thuật toán:**
1. Nhập chiều dài, chiều rộng dạng `float`.
2. Tính diện tích.
3. In kết quả.

**Code:**

```python
# Nhập: 5, 10
# Nhập hai cạnh hình chữ nhật (số thực)
chieu_dai = float(input("Nhập chiều dài: "))
chieu_rong = float(input("Nhập chiều rộng: "))
# Diện tích hình chữ nhật
dien_tich = chieu_dai * chieu_rong
# In kết quả
print(f"Diện tích hình chữ nhật là: {dien_tich}")
```

**Giải thích code:**
* `float(input(...))` — nếu nhập `5.5` mà dùng `int()` sẽ báo `ValueError`.
* `5 * 10 = 50.0` — kết quả số thực vì các biến đều là `float`.

**Độ phức tạp:** O(1).

---

### Bài 7: Trung bình cộng ba số

**Phân tích:** Nhập ba số thực, tính trung bình cộng `(a + b + c) / 3`.

**Ý tưởng:** Ép `float`, cộng ba số trong ngoặc rồi chia cho 3.

**Thuật toán:**
1. Nhập `a`, `b`, `c` dạng `float`.
2. Tính `(a + b + c) / 3`.
3. In kết quả.

**Code:**

```python
# Nhập: 4, 5, 7
# Nhập ba số thực
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
# Trung bình cộng: tổng chia số lượng
trung_binh = (a + b + c) / 3
print(f"Trung bình cộng của a, b, c: {trung_binh}")
```

**Giải thích code:**
* Ngoặc `(a + b + c)` bắt buộc phải có — thiếu ngoặc thì chỉ `c` bị chia 3.
* `16 / 3 = 5.333...` — phép `/` luôn trả số thực.

**Độ phức tạp:** O(1).

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Tính tuổi

**Phân tích:** Lấy năm 2026 trừ đi năm sinh để có tuổi.

**Ý tưởng:** Ép `int` cho năm sinh rồi trừ; in bằng f-string.

**Thuật toán:**
1. Nhập năm sinh (số nguyên).
2. Tính `tuoi = 2026 - nam_sinh`.
3. In tuổi.

**Code:**

```python
# Nhập: 2010
# Nhập năm sinh
nam_sinh = int(input("Bạn sinh năm bao nhiêu? "))
# Tính tuổi so với năm hiện tại
tuoi = 2026 - nam_sinh
print(f"Bạn {tuoi} tuổi.")
```

**Giải thích code:**
* `int(input(...))` bắt buộc — trừ số với chuỗi sẽ báo `TypeError`.
* `2026 - 2010 = 16` — số nguyên, không có phần thập phân.

**Độ phức tạp:** O(1).

---

### Bài 9: Chu vi và diện tích hình tròn

**Phân tích:** Với `pi = 3.14`, chu vi `2 * pi * r`, diện tích `pi * r * r`, in 2 chữ số thập phân.

**Ý tưởng:** Dùng `{:.2f}` trong f-string để định dạng số thực.

**Thuật toán:**
1. Nhập bán kính (float).
2. Tính chu vi và diện tích.
3. In hai dòng với 2 chữ số thập phân.

**Code:**

```python
# Nhập: 5
# Nhập bán kính hình tròn
r = float(input("Nhập bán kính: "))
# Hằng số pi
pi = 3.14
# Chu vi hình tròn
chu_vi = 2 * pi * r
# Diện tích hình tròn
dien_tich = pi * r * r
# In kết quả, giữ 2 chữ số thập phân
print(f"Chu vi: {chu_vi:.2f}")
print(f"Diện tích: {dien_tich:.2f}")
```

**Giải thích code:**
* `2 * 3.14 * 5 = 31.4` → `{:.2f}` in thành `31.40`.
* `3.14 * 25 = 78.5` → `78.50`.
* `:.2f` giữ đúng 2 chữ số sau dấu phẩy, kể cả khi số tròn.

**Độ phức tạp:** O(1).

---

### Bài 10: Đổi tiền VND sang USD

**Phân tích:** Chia số VND cho tỉ giá 25.000 để ra số USD.

**Ý tưởng:** Ép `float` cho số tiền, chia, in kết quả với 2 chữ số thập phân.

**Thuật toán:**
1. Nhập số tiền VND.
2. Chia cho tỉ giá.
3. In kết quả.

**Code:**

```python
# Nhập: 2350000
# Tỉ giá quy đổi
ti_gia = 25000
# Nhập số tiền VND cần đổi
so_vnd = float(input("Hãy nhập số tiền VND muốn quy đổi thành USD: "))
# Quy đổi sang USD
so_usd = so_vnd / ti_gia
# In kết quả với 2 chữ số thập phân
print(f"{so_vnd:.0f} VND được đổi thành {so_usd:.2f} USD")
```

**Giải thích code:**
* `2350000 / 25000 = 94.0` → `{:.2f}` in `94.00`.
* `{so_vnd:.0f}` — làm tròn số VND về số nguyên cho gọn trong câu in.

**Độ phức tạp:** O(1).

---

### Bài 11: Vận tốc trung bình

**Phân tích:** Vận tốc = quãng đường / thời gian.

**Ý tưởng:** Ép `float` cả hai đại lượng, chia rồi in 1 chữ số thập phân.

**Thuật toán:**
1. Nhập quãng đường và thời gian.
2. Tính `v = s / t`.
3. In vận tốc.

**Code:**

```python
# Nhập: 120, 2.5
# Nhập quãng đường (km) và thời gian (giờ)
s = float(input("Nhập số km: "))
t = float(input("Nhập thời gian (h): "))
# Vận tốc trung bình
v = s / t
# In kết quả với 1 chữ số thập phân
print(f"Vận tốc = {v:.1f} km/h")
```

**Giải thích code:**
* `120 / 2.5 = 48.0` → `{:.1f}` in `48.0`.
* Nếu quên ép kiểu, `"120" / "2.5"` sẽ báo `TypeError` ngay.

**Độ phức tạp:** O(1).

---

### Bài 12: Chương trình tính BMI

**Phân tích:** `BMI = kg / (cao * cao)` — kiểm tra sức khỏe từ cân nặng và chiều cao.

**Ý tưởng:** Ép `float`, tính bình phương chiều cao rồi chia; in 2 chữ số thập phân.

**Thuật toán:**
1. Nhập cân nặng và chiều cao.
2. Tính `bmi = kg / (cao * cao)`.
3. In kết quả.

**Code:**

```python
# Nhập: 80, 1.6
# Nhập cân nặng (kg) và chiều cao (m)
kg = float(input("Hãy nhập số kg: "))
chieu_cao = float(input("Hãy nhập chiều cao (m): "))
# Công thức BMI
bmi = kg / (chieu_cao * chieu_cao)
# In kết quả làm tròn 2 chữ số thập phân
print(f"BMI của bạn là: {bmi:.2f}")
```

**Giải thích code:**
* `1.6 * 1.6 = 2.56`; `80 / 2.56 = 31.25`.
* Nếu không ép `float`, nhập `1.6` sẽ gây `ValueError` khi ép `int`.
* `{:.2f}` xóa bỏ các số thập phân "rác" như `31.249999999999993`.

**Độ phức tạp:** O(1).

---

### Bài 13: Đổi độ C sang độ F

**Phân tích:** Công thức `F = C * 9 / 5 + 32`.

**Ý tưởng:** Giữ giá trị C trong biến để in lại, tính F, định dạng 1 chữ số thập phân.

**Thuật toán:**
1. Nhập nhiệt độ C.
2. Tính F.
3. In cả hai.

**Code:**

```python
# Nhập: 20.5
# Nhập nhiệt độ theo độ C
do_c = float(input("Nhập nhiệt độ (°C): "))
# Công thức chuyển đổi
do_f = do_c * 9 / 5 + 32
# In kết quả với 1 chữ số thập phân
print(f"{do_c:.1f} độ C = {do_f:.1f} độ F")
```

**Giải thích code:**
* `20.5 * 9 / 5 + 32 = 68.9` → in `68.9`.
* `{do_c:.1f}` đảm bảo số nhập `20.5` in lại đúng dạng `20.5`.

**Độ phức tạp:** O(1).

---

### Bài 14: Giới thiệu bản thân bằng f-string

**Phân tích:** Nhập tên, tuổi, lớp và gộp vào một câu giới thiệu.

**Ý tưởng:** Tuổi ép `int`, tên và lớp là chuỗi; chèn cả ba vào một f-string.

**Thuật toán:**
1. Nhập tên (str), tuổi (int), lớp (str).
2. In một câu f-string tổng hợp.

**Code:**

```python
# Nhập: An, 15, 10A1
# Nhập thông tin cá nhân
ten = input("Nhập tên: ")
tuoi = int(input("Nhập tuổi: "))
lop = input("Nhập lớp: ")
# In câu giới thiệu bằng f-string
print(f"Tôi tên là {ten}, {tuoi} tuổi, học lớp {lop}.")
```

**Giải thích code:**
* `tuoi` là số nguyên (đã ép kiểu) nên in ra `15` không có dấu nháy.
* Một f-string duy nhất thay cho nhiều `print()` ghép nối — dễ đọc, khó lỗi.

**Độ phức tạp:** O(1).

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Đổi giây ra giờ:phút:giây

**Phân tích:** 3725 giây = 1 giờ 2 phút 5 giây — cần chia tách bằng `//` và `%`.

**Ý tưởng:** Lấy phần nguyên giờ, phần dư còn lại đổi tiếp ra phút, phần dư cuối là giây.

**Thuật toán:**
1. Nhập số giây `s`.
2. `gio = s // 3600`.
3. `phut = (s % 3600) // 60`.
4. `giay = s % 60`.
5. In ba thành phần.

**Code:**

```python
# Nhập: 3725
# Nhập tổng số giây
s = int(input("Nhập số giây: "))
# Mỗi giờ có 3600 giây - lấy phần nguyên
gio = s // 3600
# Phần dư sau giờ, đổi tiếp ra phút (60 giây/phút)
phut = (s % 3600) // 60
# Phần dư cuối cùng chính là số giây
giay = s % 60
# In kết quả
print(f"{gio} giờ {phut} phút {giay} giây")
```

**Giải thích code:**
* `3725 // 3600 = 1` (giờ); `3725 % 3600 = 125` (giây còn lại).
* `125 // 60 = 2` (phút); `125 % 60 = 5` (giây).
* Đây là mẫu tách đơn vị kinh điển của `//` và `%` — dùng rất nhiều trong lập trình.

**Độ phức tạp:** O(1).

---

### Bài 16: Hóa đơn quán cà phê

**Phân tích:** Tổng 105.000đ ≥ 100.000đ nên được giảm 10% → trả 94.500đ.

**Ý tưởng:** Dùng kỹ thuật `int(điều kiện)` của bài 6: điều kiện đúng (True→1) thì trừ 10%, sai (False→0) thì không.

**Thuật toán:**
1. Nhập giá ly và số ly.
2. Tính `tong = gia * so_ly`.
3. Kiểm tra điều kiện giảm giá.
4. Tính tiền phải trả và in.

**Code:**

```python
# Nhập: 35000, 3
# Nhập giá và số lượng
gia = float(input("Nhập giá một ly: "))
so_ly = int(input("Nhập số ly: "))
# Tổng tiền trước khi giảm
tong = gia * so_ly
# Có khuyến mãi khi tổng >= 100000 (kết quả True/False)
khuyen_mai = tong >= 100000
# int(True) = 1 -> trừ 10%; int(False) = 0 -> không trừ
tien_phai_tra = tong - tong * 0.1 * int(khuyen_mai)
# In kết quả
print(f"Tổng tiền: {tong:.2f}")
print(f"Tiền phải trả: {tien_phai_tra:.2f}")
```

**Giải thích code:**
* `105000 * 0.1 = 10500`; `105000 - 10500 = 94500.00`.
* `tong >= 100000` trả về `True` → `int(...)` biến thành `1`.
* Kỹ thuật này gọn nhưng sẽ được thay thế bằng `if` rõ ràng hơn ở bài 8.

**Độ phức tạp:** O(1).

---

### Bài 17: Tiền lãi tiết kiệm một năm

**Phân tích:** Với lãi suất 6.5%/năm, gửi 10 triệu được 650.000đ lãi.

**Ý tưởng:** `lai = tien * 0.065`; tổng = gốc + lãi; in 2 chữ số thập phân.

**Thuật toán:**
1. Nhập số tiền gửi.
2. Tính tiền lãi.
3. Tính tổng tiền.
4. In hai dòng kết quả.

**Code:**

```python
# Nhập: 10000000
# Lãi suất một năm
lai_suat = 0.065
# Nhập số tiền gửi
tien_gui = float(input("Nhập số tiền gửi: "))
# Tiền lãi sau 1 năm
tien_lai = tien_gui * lai_suat
# Tổng gốc và lãi
tong_nhan = tien_gui + tien_lai
# In kết quả
print(f"Tiền lãi: {tien_lai:.2f}")
print(f"Tổng tiền nhận được: {tong_nhan:.2f}")
```

**Giải thích code:**
* `10000000 * 0.065 = 650000.0`; tổng = `10650000.0`.
* Để tránh sai số, viết lãi suất dưới dạng `0.065` thay vì `6.5` rồi chia 100.
* `:.2f` cho đầu ra đúng định dạng tiền tệ.

**Độ phức tạp:** O(1).

---

### Bài 18: Điểm trung bình có trọng số

**Phân tích:** `(Toán*2 + Văn + Anh) / 4` với Toán hệ số 2.

**Ý tưởng:** Ép `float` cho điểm, cộng theo hệ số, chia tổng hệ số, in 2 chữ số.

**Thuật toán:**
1. Nhập ba môn.
2. Tính `(t*2 + v + a) / 4`.
3. In kết quả.

**Code:**

```python
# Nhập: 8, 7, 9
# Nhập điểm từng môn (thang 10)
diem_toan = float(input("Nhập điểm Toán: "))
diem_van = float(input("Nhập điểm Văn: "))
diem_anh = float(input("Nhập điểm Anh: "))
# Toán hệ số 2, Văn và Anh hệ số 1 -> chia cho 4
trung_binh = (diem_toan * 2 + diem_van + diem_anh) / 4
# In kết quả làm tròn 2 chữ số thập phân
print(f"Điểm trung bình: {trung_binh:.2f}")
```

**Giải thích code:**
* `(8*2 + 7 + 9) / 4 = 32 / 4 = 8.0` → in `8.00`.
* Ngoặc bao trọn tử số — nếu thiếu, `anh / 4` bị tách ra ngoài, kết quả sai.

**Độ phức tạp:** O(1).

---

### Bài 19: Chia tiền sau bữa ăn

**Phân tích:** 850.000đ chia 4 người, mỗi người 212.500đ.

**Ý tưởng:** Chia tổng cho số người, định dạng 2 chữ số thập phân.

**Thuật toán:**
1. Nhập tổng hóa đơn và số người.
2. Tính phần mỗi người.
3. In kết quả.

**Code:**

```python
# Nhập: 850000, 4
# Nhập tổng hóa đơn và số người chia
tong = float(input("Nhập tổng hóa đơn: "))
so_nguoi = int(input("Nhập số người: "))
# Mỗi người trả phần bằng nhau
moi_nguoi = tong / so_nguoi
# In kết quả
print(f"Mỗi người phải trả: {moi_nguoi:.2f} VND")
```

**Giải thích code:**
* `850000 / 4 = 212500.0` → in `212500.00`.
* Số người là số nguyên (`int`), tiền là số thực (`float`) — mỗi đại lượng một kiểu đúng nghĩa.

**Độ phức tạp:** O(1).

---

### Bài 20: Hồ sơ học sinh hoàn chỉnh

**Phân tích:** Kết hợp tất cả kiến thức bài 7: nhập nhiều kiểu dữ liệu, f-string, `sep`, trang trí khung.

**Ý tưởng:** Nhập 4 thông tin, in 3 dòng: dòng viền, dòng thông tin chính (f-string + `sep`), dòng môn học.

**Thuật toán:**
1. Nhập họ tên (str), tuổi (int), trường (str), môn học (str).
2. In dòng viền tiêu đề.
3. In dòng thông tin chính ngăn cách bởi ` | `.
4. In dòng môn yêu thích.

**Code:**

```python
# Nhập: Nguyễn Văn An, 16, THPT Python, Tin học
# Nhập thông tin hồ sơ
ho_ten = input("Nhập họ tên: ")
tuoi = int(input("Nhập tuổi: "))
truong = input("Nhập trường: ")
mon_hoc = input("Nhập môn yêu thích: ")
# Dòng viền tiêu đề
print("===== HỒ SƠ CÁ NHÂN =====")
# Dòng thông tin chính: f-string chèn tên, tuổi, trường
print(f"{ho_ten} | {tuoi} tuổi | {truong}")
# Dòng môn học yêu thích
print(f"Môn yêu thích: {mon_hoc}")
```

**Giải thích code:**
* `{tuoi} tuổi` — tuổi đã ép `int` nên in đúng số `16` giữa hai chuỗi.
* Dòng thông tin chính có thể viết bằng `print(ho_ten, f"{tuoi} tuổi", truong, sep=" | ")` — cả hai cách đều hợp lệ.
* Đây chính là kiểu chương trình "mẫu hồ sơ" có thể nhập lại mỗi lần chạy cho người dùng khác.

**Độ phức tạp:** O(1).

---

## 📌 Lời khuyên cuối

* 📥 **Nhớ luôn:** `input()` trả về chuỗi — cứ nhập số là phải ép kiểu.
* 🔄 **Đọc lỗi theo chiều kim đồng hồ:** `int(input(...))` — `input` chạy trước, ép kiểu chạy sau.
* 🎨 **f-string là "chân ái"** của việc in ấn: vừa gọn, vừa định dạng được số `:.2f`.
* 🧪 **Chạy thử nhiều lần** với giá trị khác nhau (số âm, số thập phân, chữ cái) để hiểu chương trình phản ứng thế nào.
* Bài sau bạn sẽ học `if` — lúc đó chương trình biết **tự đưa ra quyết định** dựa trên dữ liệu vừa nhập!

👉 Tiếp theo: **[Bài 8: Câu Lệnh If – Cấu Trúc Rẽ Nhánh](../08_Cau_lenh_if/bai_giang.md)**