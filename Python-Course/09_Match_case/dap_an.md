# ✅ Bài 9: Đáp Án – Câu Lệnh Match – Case

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án để việc học hiệu quả nhất.
>
> ⚠️ Tất cả code yêu cầu **Python 3.10+**.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Thứ trong tuần

**Phân tích:** Nhập số 1–7 và ánh xạ sang tên thứ — bài toán "so khớp giá trị cố định" kinh điển, rất hợp với match-case.

**Ý tưởng:** Một `match` với 7 case; case ngoài 1–7 rơi vào `case _`.

**Thuật toán:**
1. Nhập và ép kiểu số nguyên.
2. Match số với từng case.
3. Case cuối là `case _` báo lỗi.

**Code:**

```python
# Nhập số thứ trong tuần (ví dụ nhập: 3)
so = int(input("Nhập số (1-7): "))

# So khớp số với tên thứ tương ứng
match so:
    case 1:
        print("Chủ nhật")
    case 2:
        print("Thứ Hai")
    case 3:
        print("Thứ Ba")
    case 4:
        print("Thứ Tư")
    case 5:
        print("Thứ Năm")
    case 6:
        print("Thứ Sáu")
    case 7:
        print("Thứ Bảy")
    case _:
        print("So khong hop le!")
```

**Giải thích code:**
* `int(input(...))` — đổi chữ nhập vào thành số nguyên để so sánh.
* Các `case 1: ... case 7:` — mỗi mẫu là một hằng số; khớp cái nào chạy cái đó rồi thoát.
* `case _:` — bắt mọi số còn lại (0, 8, -3...) — giống `else`.

**Độ phức tạp:** O(1).

---

### Bài 2: Số ngày trong tháng

**Phân tích:** 12 tháng nhưng chỉ 3 nhóm số ngày (28, 30, 31) — tận dụng dấu `|` để gộp nhóm.

**Ý tưởng:** 3 case gộp nhóm + 1 case lỗi.

**Thuật toán:**
1. Nhập tháng.
2. Case 2 → 28 ngày.
3. Case `4 | 6 | 9 | 11` → 30 ngày.
4. Case các tháng còn lại (1, 3, 5, 7, 8, 10, 12) → 31 ngày.
5. `case _` → báo lỗi.

**Code:**

```python
# Nhập tháng (ví dụ nhập: 4)
thang = int(input("Nhập tháng: "))

# So khớp tháng với số ngày tương ứng
match thang:
    case 2:
        print(f"Tháng {thang} có 28 ngày")
    case 4 | 6 | 9 | 11:
        print(f"Tháng {thang} có 30 ngày")
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print(f"Tháng {thang} có 31 ngày")
    case _:
        print("Tháng không hợp lệ!")
```

**Giải thích code:**
* `case 4 | 6 | 9 | 11:` — dấu `|` cho phép một case khớp 4 giá trị khác nhau, giảm từ 12 case xuống còn 4.
* `f"Tháng {thang} có..."` — f-string chèn giá trị biến `thang` vào câu in.
* Thứ tự case không quan trọng ở bài này vì các nhóm không trùng nhau.

**Độ phức tạp:** O(1).

---

### Bài 3: Điểm chữ

**Phân tích:** Nhập chữ cái có thể thường/hoa — cần chuẩn hóa trước khi khớp.

**Ý tưởng:** Dùng `.upper()` chuyển về in hoa rồi match.

**Thuật toán:**
1. Nhập chữ cái, gọi `.upper()`.
2. Match chữ với 5 case.
3. `case _` cho ký tự khác.

**Code:**

```python
# Nhập điểm chữ, đổi về chữ hoa (ví dụ nhập: b)
chu = input("Nhập điểm chữ: ").upper()

# So khớp chữ cái với xếp loại
match chu:
    case "A":
        print("Xuat sac")
    case "B":
        print("Gioi")
    case "C":
        print("Kha")
    case "D":
        print("Trung binh")
    case "F":
        print("Khong dat")
    case _:
        print("Diem chu khong hop le!")
```

**Giải thích code:**
* `input(...).upper()` — ngay sau khi nhập, chữ được đổi sang in hoa: nhập `b` hay `B` đều thành `"B"`.
* 5 case tương ứng 5 mức xếp loại; `case _` bắt các ký tự như `E`, `G`, số...

**Độ phức tạp:** O(1).

---

### Bài 4: Menu món ăn trưa

**Phân tích:** Nhập số 1–4 để chọn món — mô hình menu đơn giản.

**Ý tưởng:** Mỗi case in tên món tương ứng.

**Thuật toán:**
1. In menu lên màn hình cho người dùng biết.
2. Nhập lựa chọn.
3. Match với 4 case.

**Code:**

```python
# Hiển thị menu cho người dùng
print("=== MENU TRƯA ===")
print("1. Pho")
print("2. Bun")
print("3. Com")
print("4. My xao")
print("================")

# Nhập lựa chọn (ví dụ nhập: 2)
lua_chon = int(input("Nhập lựa chọn (1-4): "))

# So khớp số với món ăn
match lua_chon:
    case 1:
        print("Ban chon: Pho")
    case 2:
        print("Ban chon: Bun")
    case 3:
        print("Ban chon: Com")
    case 4:
        print("Ban chon: My xao")
    case _:
        print("Mon khong co trong menu!")
```

**Giải thích code:**
* Các lệnh `print` menu giúp người dùng biết cần nhập gì — chương trình thân thiện hơn.
* `case _` xử lý nhập 5, 0, -1... thay vì chương trình im lặng.

**Độ phức tạp:** O(1).

---

### Bài 5: Kích cỡ áo

**Phân tích:** Nhập kích cỡ (thường/hoa) và in số đo.

**Ý tưởng:** Chuẩn hóa bằng `.upper()` rồi match.

**Thuật toán:**
1. Nhập kích cỡ, đổi in hoa.
2. Match 4 case + case lỗi.

**Code:**

```python
# Nhập kích cỡ, đổi về in hoa (ví dụ nhập: l)
size = input("Nhập kích cỡ: ").upper()

# So khớp kích cỡ với số đo
match size:
    case "S":
        print("Kich co S - so do 36")
    case "M":
        print("Kich co M - so do 38")
    case "L":
        print("Kich co L - so do 40")
    case "XL":
        print("Kich co XL - so do 42")
    case _:
        print("Khong co kich co nay")
```

**Giải thích code:**
* Nhập `l` → `.upper()` → `"L"` → khớp case L — người dùng không bị phiền vì quên viết hoa.
* Nếu không có `.upper()` thì phải viết thêm 4 case cho chữ thường, code dài gấp đôi.

**Độ phức tạp:** O(1).

---

### Bài 6: Chào hỏi bằng nhiều ngôn ngữ

**Phân tích:** Ánh xạ tên ngôn ngữ sang lời chào.

**Ý tưởng:** Match chuỗi ngôn ngữ, mỗi case in lời chào.

**Thuật toán:**
1. Nhập tên ngôn ngữ.
2. Match với 4 case + case mặc định.

**Code:**

```python
# Nhập tên ngôn ngữ (ví dụ nhập: anh)
ngon_ngu = input("Nhập ngôn ngữ (viet/anh/phap/nhat): ")

# So khớp ngôn ngữ với lời chào
match ngon_ngu:
    case "viet":
        print("Xin chào!")
    case "anh":
        print("Hello!")
    case "phap":
        print("Bonjour!")
    case "nhat":
        print("Konnichiwa!")
    case _:
        print("Chua ho tro ngon ngu nay!")
```

**Giải thích code:**
* Match-case làm việc tốt với chuỗi ký tự — mỗi case là một chuỗi cần khớp.
* `case _` thông báo khi nhập `han`, `trung`... — chương trình không "chết" vì đầu vào lạ.

**Độ phức tạp:** O(1).

---

### Bài 7: Mùa trong năm

**Phân tích:** 12 tháng gộp thành 4 mùa — mỗi mùa 3 tháng.

**Ý tưởng:** Dùng dấu `|` gộp 3 tháng cho mỗi mùa.

**Thuật toán:**
1. Nhập tháng.
2. Match: 4 case mùa + 1 case lỗi.

**Code:**

```python
# Nhập tháng (ví dụ nhập: 6)
thang = int(input("Nhập tháng: "))

# So khớp tháng với mùa trong năm
match thang:
    case 12 | 1 | 2:
        print("Mùa đông")
    case 3 | 4 | 5:
        print("Mùa xuân")
    case 6 | 7 | 8:
        print("Mùa hè")
    case 9 | 10 | 11:
        print("Mùa thu")
    case _:
        print("Thang khong hop le!")
```

**Giải thích code:**
* Thứ tự các case không quan trọng vì các nhóm tháng rời nhau.
* `case 12 | 1 | 2:` — đáng chú ý: tháng 12 nằm cùng nhóm với 1, 2 (mùa đông ở Bắc bán cầu).

**Độ phức tạp:** O(1).

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Máy tính hai số

**Phân tích:** Chọn phép toán từ bàn phím và thực hiện — kết hợp match-case với `if` chống chia 0.

**Ý tưởng:** Match ký tự phép toán; trong `case "/"` kiểm tra mẫu số.

**Thuật toán:**
1. Nhập hai số và phép toán.
2. Match phép toán với 4 case.
3. Trong case chia: nếu `b == 0` báo lỗi.

**Code:**

```python
# Nhập hai số (ví dụ: 10 và 4)
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))

# Nhập phép toán (ví dụ nhập: /)
phep_toan = input("Nhập phép toán (+, -, *, /): ")

# So khớp ký tự phép toán
match phep_toan:
    case "+":
        print(f"{a} + {b} = {a + b}")
    case "-":
        print(f"{a} - {b} = {a - b}")
    case "*":
        print(f"{a} * {b} = {a * b}")
    case "/":
        # Kiểm tra mẫu số bằng 0 trước khi chia
        if b == 0:
            print("Khong the chia cho 0!")
        else:
            print(f"{a} / {b} = {a / b}")
    case _:
        print("Phep toan khong hop le!")
```

**Giải thích code:**
* Mỗi case thực hiện đúng một phép tính và in kết quả kèm f-string.
* `case "/":` chứa `if b == 0` — match-case không cấm dùng `if` bên trong khối lệnh; ngược lại đây là cách kết hợp đúng chỗ.
* `case _` bắt các ký tự lạ như `^`, `x`, chữ...

**Độ phức tạp:** O(1).

---

### Bài 9: Xếp loại điểm trung bình

**Phân tích:** Điểm là khoảng giá trị liên tục — dùng guard `case _ if ...` để match-case xử lý được.

**Ý tưởng:** Xét các case từ cao xuống thấp; case đầu tiên có guard đúng sẽ chạy.

**Thuật toán:**
1. Nhập điểm.
2. Guard theo thứ tự: >= 9, >= 8, >= 6.5, >= 5, >= 0.
3. `case _` cuối cùng bắt điểm âm/trên 10.

**Code:**

```python
# Nhập điểm trung bình (ví dụ nhập: 8.2)
diem = float(input("Nhập điểm trung bình: "))

# Dùng guard để xử lý khoảng giá trị
match diem:
    case _ if diem >= 9:
        print("Xuat sac")
    case _ if diem >= 8:
        print("Gioi")
    case _ if diem >= 6.5:
        print("Kha")
    case _ if diem >= 5:
        print("Trung binh")
    case _ if diem >= 0:
        print("Yeu")
    case _:
        print("Diem khong hop le!")
```

**Giải thích code:**
* `case _ if diem >= 8:` — mẫu `_` khớp mọi giá trị, guard `if diem >= 8` kiểm tra thêm.
* Các case xét **từ trên xuống**: điểm 8.2 không qua guard `>= 9`, rơi xuống `>= 8` → "Gioi".
* Điểm 11 hoặc -3 không qua guard nào (kể cả `>= 0`) → rơi vào `case _` cuối.

**Độ phức tạp:** O(1).

---

### Bài 10: Số ngày trong tháng (có năm nhuận)

**Phân tích:** Chỉ tháng 2 thay đổi theo năm nhuận — các tháng khác giữ nguyên như bài 2.

**Ý tưởng:** Match tháng; trong `case 2:` dùng `if` kiểm tra năm nhuận.

**Thuật toán:**
1. Nhập tháng và năm.
2. Match tháng như bài 2.
3. Trong case 2: năm nhuận (`% 400 == 0` hoặc `% 4 == 0` và `% 100 != 0`) → 29 ngày, ngược lại 28.

**Code:**

```python
# Nhập tháng và năm (ví dụ: 2 và 2024)
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

# Kiểm tra năm nhuận cho tháng 2
nam_nhuan = (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)

# So khớp tháng với số ngày
match thang:
    case 2:
        # Tháng 2 phụ thuộc vào năm nhuận
        if nam_nhuan:
            print(f"Tháng 2 năm {nam} có 29 ngày")
        else:
            print(f"Tháng 2 năm {nam} có 28 ngày")
    case 4 | 6 | 9 | 11:
        print(f"Tháng {thang} năm {nam} có 30 ngày")
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print(f"Tháng {thang} năm {nam} có 31 ngày")
    case _:
        print("Tháng không hợp lệ!")
```

**Giải thích code:**
* `nam_nhuan` — biểu thức logic: chia hết 400 **hoặc** (chia hết 4 **và không** chia hết 100) — đúng quy tắc lịch Gregory.
* Điều kiện năm nhuận tính **một lần** trước match — code case sạch hơn.
* Năm 2024 chia hết cho 4, không chia hết 100 → nhuận → 29 ngày. Năm 2100 không nhuận (chia hết 100 nhưng không chia hết 400).

**Độ phức tạp:** O(1).

---

### Bài 11: Đổi ngoại tệ

**Phân tích:** Mỗi mã tiền tệ có một tỉ giá riêng — match mã rồi nhân số tiền.

**Ý tưởng:** Chuẩn hóa mã bằng `.upper()`, mỗi case gán tỉ giá, sau đó in phép nhân.

**Thuật toán:**
1. Nhập mã tiền tệ (đổi in hoa) và số tiền.
2. Match mã: gán tỉ giá tương ứng.
3. In số VND = số tiền × tỉ giá.

**Code:**

```python
# Nhập mã tiền tệ và số tiền (ví dụ: usd và 2)
ma = input("Nhập mã tiền tệ: ").upper()
so_tien = float(input("Nhập số tiền: "))

# So khớp mã tiền tệ với tỉ giá (VND)
match ma:
    case "USD":
        ti_gia = 25000
    case "EUR":
        ti_gia = 27000
    case "JPY":
        ti_gia = 170
    case _:
        ti_gia = 0   # Mã không hợp lệ → tỉ giá 0 để phát hiện

# Nếu tỉ giá hợp lệ thì tính toán, ngược lại báo lỗi
if ti_gia > 0:
    print(f"{so_tien} {ma} = {so_tien * ti_gia} VND")
else:
    print("Ma tien te khong hop le!")
```

**Giải thích code:**
* Nhập `usd` → `.upper()` → `"USD"` → khớp case đầu.
* Mỗi case chỉ **gán tỉ giá** vào biến `ti_gia` — cách tổ chức gọn: match dùng để "tra bảng".
* Mã lạ → `ti_gia = 0` → `if ti_gia > 0` báo lỗi. Không cần đặt câu in lặp lại trong từng case.

**Độ phức tạp:** O(1).

---

### Bài 12: Xếp loại học lực (điểm + hạnh kiểm)

**Phân tích:** Kết quả phụ thuộc **hai** yếu tố — đúng lúc dùng so khớp bộ giá trị `match (diem, hanh_kiem):`.

**Ý tưởng:** Khớp cặp (điểm, hạnh kiểm); dùng `_` trong bộ giá trị cho "bất kể điểm".

**Thuật toán:**
1. Nhập điểm và hạnh kiểm (chuẩn hóa viết hoa chữ đầu).
2. Match bộ giá trị theo các quy tắc.
3. Case cuối là mặc định "Trung binh".

**Code:**

```python
# Nhập điểm và hạnh kiểm (ví dụ: 8.5 và Tot)
diem = float(input("Nhập điểm: "))
hanh_kiem = input("Nhập hạnh kiểm (Tot/Kha/Yeu): ").capitalize()

# So khớp bộ giá trị (điểm, hạnh kiểm)
match (diem, hanh_kiem):
    case (_, "Yeu"):
        print("Khen thuong: Khong")
    case (_, "Tot") if diem >= 8:
        print("Khen thuong: Gioi")
    case (_, "Kha") if diem >= 8:
        print("Khen thuong: Kha")
    case _:
        print("Khen thuong: Trung binh")
```

**Giải thích code:**
* `match (diem, hanh_kiem):` — Python ghép hai giá trị thành một cặp rồi so mẫu với cặp.
* `case (_, "Yeu"):` — `_` khớp **bất kỳ** điểm nào; chỉ cần hạnh kiểm là "Yeu" → không khen.
* `case (_, "Tot") if diem >= 8:` — guard xét thêm điểm >= 8.
* `case _` — mọi trường hợp còn lại (hạnh kiểm Tốt/Khá mà điểm < 8, hoặc hạnh kiểm không đúng chuẩn) → Trung binh.

**Độ phức tạp:** O(1).

---

### Bài 13: Vé máy bay

**Phân tích:** Hạng vé quyết định giá; tổng tiền = giá × số lượng.

**Ý tưởng:** Match hạng vé gán giá, rồi nhân với số lượng.

**Thuật toán:**
1. Nhập hạng vé (đổi thường) và số lượng.
2. Match hạng: gán giá.
3. Hạng lạ → báo lỗi; ngược lại in tổng tiền.

**Code:**

```python
# Nhập hạng vé và số lượng (ví dụ: business và 2)
hang_ve = input("Nhập hạng vé: ").lower()
so_luong = int(input("Nhập số lượng vé: "))

# So khớp hạng vé với đơn giá (ngàn đồng)
match hang_ve:
    case "economy":
        don_gia = 1000
    case "business":
        don_gia = 3500
    case "first":
        don_gia = 8000
    case _:
        don_gia = 0   # Hạng không hợp lệ

# Tính và in tổng tiền nếu giá hợp lệ
if don_gia > 0:
    print(f"Tổng tiền: {don_gia * so_luong} ngàn đồng")
else:
    print("Hang ve khong hop le!")
```

**Giải thích code:**
* `.lower()` giúp nhập `BUSINESS` hay `Business` đều khớp.
* Match chỉ gán giá; phép nhân `don_gia * so_luong` nằm sau match — tách bạch "tra bảng" và "tính toán".
* `don_gia = 0` làm cờ báo hiệu hạng không hợp lệ.

**Độ phức tạp:** O(1).

---

### Bài 14: Cung hoàng đạo (theo tháng)

**Phân tích:** 12 tháng → 12 cung — bài tập "bảng tra cứu" thuần túy.

**Ý tưởng:** 12 case đơn giản, mỗi case in một cung.

**Thuật toán:**
1. Nhập tháng.
2. Match với 12 case.
3. `case _` báo lỗi.

**Code:**

```python
# Nhập tháng sinh (ví dụ nhập: 9)
thang = int(input("Nhập tháng sinh: "))

# So khớp tháng với cung hoàng đạo
match thang:
    case 1:
        print("Cung của bạn: Bao Binh")
    case 2:
        print("Cung của bạn: Song Ngu")
    case 3:
        print("Cung của bạn: Bach Duong")
    case 4:
        print("Cung của bạn: Kim Nguu")
    case 5:
        print("Cung của bạn: Song Tu")
    case 6:
        print("Cung của bạn: Cu Giai")
    case 7:
        print("Cung của bạn: Su Tu")
    case 8:
        print("Cung của bạn: Xu Nu")
    case 9:
        print("Cung của bạn: Thien Binh")
    case 10:
        print("Cung của bạn: Thien Yet")
    case 11:
        print("Cung của bạn: Nhan Ma")
    case 12:
        print("Cung của bạn: Ma Ket")
    case _:
        print("Tháng sinh không hợp lệ!")
```

**Giải thích code:**
* Đây là dạng "bảng tra cứu" mà match-case xử lý gọn nhất — viết 12 lệnh `elif` cũng được nhưng dài và khó nhìn hơn.
* `case _` bắt tháng 0, 13... với câu thông báo rõ ràng.

**Độ phức tạp:** O(1).

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Oẳn tù tì

**Phân tích:** 9 tổ hợp (3×3) nhưng chỉ 3 kết quả — dùng bộ giá trị + dấu `|` gom gọn.

**Ý tưởng:** Khớp cặp (người, máy); máy cố định "búa" nên chỉ cần liệt kê cặp người.

**Thuật toán:**
1. Nhập lựa chọn của người chơi.
2. Match cặp `(nguoi, "búa")` với các nhóm thắng/thua/hòa.
3. `case _` cho đầu vào không đúng.

**Code:**

```python
# Người chơi nhập (ví dụ nhập: bao)
nguoi = input("Bạn chọn (kéo/búa/bao): ").lower()
may = "búa"

print(f"Máy chọn: {may}")

# So khớp cặp (người, máy) để phân định thắng thua
match (nguoi, may):
    case ("kéo", "búa") | ("búa", "bao") | ("bao", "kéo"):
        print("Bạn thua!")
    case ("kéo", "bao") | ("búa", "kéo") | ("bao", "búa"):
        print("Bạn thắng!")
    case ("kéo", "kéo") | ("búa", "búa") | ("bao", "bao"):
        print("Hòa nhau!")
    case _:
        print("Nhap khong dung!")
```

**Giải thích code:**
* `match (nguoi, may):` — ghép hai lựa chọn thành một cặp để khớp.
* Nhóm thua gồm 3 cặp: kéo thua búa, búa thua bao, bao thua kéo — gộp bằng `|`.
* Mỗi case liệt kê đủ 3 cặp → tổng 9 khả năng được phủ hết bởi 4 case.
* `case _` bắt chuỗi không đúng như `keo` (thiếu dấu) hoặc chữ khác.

**Độ phức tạp:** O(1).

---

### Bài 16: Cung hoàng đạo (theo ngày + tháng)

**Phân tích:** Ranh giới cung nằm giữa tháng — cần khớp cặp (tháng, ngày) kèm guard so sánh ngày.

**Ý tưởng:** Mỗi tháng có 1–2 case: ngày >= ranh giới thuộc cung sau, ngược lại cung trước.

**Thuật toán:**
1. Nhập ngày và tháng.
2. Match cặp (tháng, ngày) với guard.
3. Tháng nào không chia ranh giới thì một case duy nhất.

**Code:**

```python
# Nhập ngày và tháng sinh (ví dụ: 15 và 8)
ngay = int(input("Nhập ngày sinh: "))
thang = int(input("Nhập tháng sinh: "))

# So khớp cặp (tháng, ngày) với guard cho ranh giới ngày
match (thang, ngay):
    case (1, _) if ngay >= 20:
        print("Cung của bạn: Bao Binh")
    case (2, _) if ngay <= 18:
        print("Cung của bạn: Bao Binh")
    case (2, _):
        print("Cung của bạn: Song Ngu")
    case (3, _) if ngay <= 20:
        print("Cung của bạn: Song Ngu")
    case (3, _):
        print("Cung của bạn: Bach Duong")
    case (4, _) if ngay <= 19:
        print("Cung của bạn: Bach Duong")
    case (4, _):
        print("Cung của bạn: Kim Nguu")
    case (5, _) if ngay <= 20:
        print("Cung của bạn: Kim Nguu")
    case (5, _):
        print("Cung của bạn: Song Tu")
    case (6, _) if ngay <= 21:
        print("Cung của bạn: Song Tu")
    case (6, _):
        print("Cung của bạn: Cu Giai")
    case (7, _) if ngay <= 22:
        print("Cung của bạn: Cu Giai")
    case (7, _):
        print("Cung của bạn: Su Tu")
    case (8, _) if ngay <= 22:
        print("Cung của bạn: Su Tu")
    case (8, _):
        print("Cung của bạn: Xu Nu")
    case (9, _) if ngay <= 22:
        print("Cung của bạn: Xu Nu")
    case (9, _):
        print("Cung của bạn: Thien Binh")
    case (10, _) if ngay <= 22:
        print("Cung của bạn: Thien Binh")
    case (10, _):
        print("Cung của bạn: Thien Yet")
    case (11, _) if ngay <= 21:
        print("Cung của bạn: Thien Yet")
    case (11, _):
        print("Cung của bạn: Nhan Ma")
    case (12, _) if ngay <= 21:
        print("Cung của bạn: Nhan Ma")
    case (12, _):
        print("Cung của bạn: Ma Ket")
    case (1, _):
        print("Cung của bạn: Ma Ket")
```

**Giải thích code:**
* `case (1, _) if ngay >= 20:` — tháng 1 từ ngày 20 trở đi là Bảo Bình; `_` khớp mọi ngày.
* Thứ tự case **quan trọng**: case có guard đặt trước, case thường đặt sau (tháng 2 ngày <= 18 → Bảo Bình, còn lại → Song Ngư).
* Ngày sinh giả định hợp lệ theo đề bài nên không cần case lỗi.

**Độ phức tạp:** O(1).

---

### Bài 17: Tiền điện bậc thang

**Phân tích:** Giá tiền theo bậc — với 3 bậc chỉ cần guard + công thức cộng dồn.

**Ý tưởng:** Chia 3 khoảng bằng guard; mỗi khoảng tính số kWh ở bậc cao nhất.

**Thuật toán:**
1. Nhập số kWh.
2. Guard theo khoảng: <= 50; <= 100; > 100.
3. Tính tiền theo công thức từng bậc; số âm → case cuối báo lỗi.

**Code:**

```python
# Nhập số điện tiêu thụ (ví dụ nhập: 65)
so_kwh = float(input("Nhập số điện tiêu thụ (kWh): "))

# Giá áp đồng loạt theo bậc của tổng số kWh (theo giáo trình)
match so_kwh:
    case _ if so_kwh <= 50:
        # Bậc 1: 2000 đồng/kWh
        tien = so_kwh * 2000
        print(f"Số tiền phải trả: {tien} đồng")
    case _ if so_kwh <= 100:
        # Bậc 2: 2500 đồng/kWh cho toàn bộ lượng điện
        tien = so_kwh * 2500
        print(f"Số tiền phải trả: {tien} đồng")
    case _ if so_kwh >= 0:
        # Bậc 3: 3000 đồng/kWh cho toàn bộ lượng điện
        tien = so_kwh * 3000
        print(f"Số tiền phải trả: {tien} đồng")
    case _:
        print("So lieu khong hop le!")
```

**Giải thích code:**
* Với 65 kWh → `65 * 2500 = 162500` — khớp ví dụ trong giáo trình (giá áp theo bậc của tổng lượng điện, không lũy tiến theo phần vượt).
* Các case xét theo thứ tự: `<= 50` → `<= 100` → `>= 0`; số âm không qua guard `>= 0` nên rơi xuống `case _` → báo `So lieu khong hop le!`.
* Nếu bạn muốn kiểu **lũy tiến** (bậc cao chỉ tính phần vượt), chỉ cần đổi công thức bậc 2 thành `50 * 2000 + (so_kwh - 50) * 2500` — tùy quy định áp dụng.

**Độ phức tạp:** O(1).

---

### Bài 18: Máy tính nâng cao

**Phân tích:** Mở rộng máy tính cơ bản với chia nguyên, chia dư, lũy thừa và chống chia 0.

**Ý tưởng:** Match chuỗi phép toán; các case chứa phép chia kiểm tra `b == 0`.

**Thuật toán:**
1. Nhập hai số và phép toán.
2. Match 7 phép toán.
3. Chia (cả `/`, `//`, `%`) kiểm tra mẫu số 0.

**Code:**

```python
# Nhập hai số (ví dụ: 7 và 3)
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))

# Nhập phép toán (ví dụ nhập: //)
phep_toan = input("Nhập phép toán: ")

# So khớp phép toán
match phep_toan:
    case "+":
        print(f"{a} + {b} = {a + b}")
    case "-":
        print(f"{a} - {b} = {a - b}")
    case "*":
        print(f"{a} * {b} = {a * b}")
    case "/":
        if b == 0:
            print("Khong the chia cho 0!")
        else:
            print(f"{a} / {b} = {a / b}")
    case "//":
        if b == 0:
            print("Khong the chia cho 0!")
        else:
            print(f"{a} // {b} = {a // b}")
    case "%":
        if b == 0:
            print("Khong the chia cho 0!")
        else:
            print(f"{a} % {b} = {a % b}")
    case "**":
        print(f"{a} ** {b} = {a ** b}")
    case _:
        print("Phep toan khong hop le!")
```

**Giải thích code:**
* `//` chia lấy phần nguyên: `7 // 3 = 2`; `%` chia lấy dư: `7 % 3 = 1`; `**` lũy thừa: `7 ** 3 = 343`.
* `b == 0` được kiểm tra ở cả ba case có chia — lũy thừa với số mũ âm/0 vẫn hợp lệ nên không cần kiểm tra.
* `a`, `b` là `float` nên `//` trả về `2.0`; muốn kết quả nguyên hãy nhập `int` — tùy yêu cầu.

**Độ phức tạp:** O(1).

---

### Bài 19: Đặt món tại nhà hàng

**Phân tích:** Hóa đơn gồm 3 lựa chọn độc lập — ba khối `match` liên tiếp, mỗi khối gán giá vào một biến.

**Ý tưởng:** Tính giá món chính (theo size), giá đồ uống, rồi cộng tổng.

**Thuật toán:**
1. In menu, nhập món chính, size, đồ uống.
2. Match món chính → giá cơ bản.
3. Match size → nhân hệ số 1 hoặc 1.5.
4. Match đồ uống → giá.
5. In tổng = (giá món × hệ số) + giá uống.

**Code:**

```python
# Hiển thị menu
print("=== NHÀ HÀNG ===")
print("Món chính: 1. Phở 35k | 2. Cơm gà 40k | 3. Bún 30k")
print("Size: S = 1 lần | L = 1.5 lần giá")
print("Đồ uống: 1. Trà đá 5k | 2. Nước ngọt 10k | 3. Cà phê 15k")

# Nhập lựa chọn (ví dụ: 2, L, 3)
mon = int(input("Món chính (1-3): "))
size = input("Size (S/L): ").upper()
do_uong = int(input("Đồ uống (1-3): "))

# Khối match 1: giá món chính
match mon:
    case 1:
        gia_mon = 35
    case 2:
        gia_mon = 40
    case 3:
        gia_mon = 30
    case _:
        gia_mon = 0   # Món không hợp lệ

# Khối match 2: hệ số size
match size:
    case "S":
        he_so = 1
    case "L":
        he_so = 1.5
    case _:
        he_so = 0   # Size không hợp lệ

# Khối match 3: giá đồ uống
match do_uong:
    case 1:
        gia_uong = 5
    case 2:
        gia_uong = 10
    case 3:
        gia_uong = 15
    case _:
        gia_uong = 0   # Đồ uống không hợp lệ

# Tính tổng tiền nếu mọi lựa chọn hợp lệ
if gia_mon > 0 and he_so > 0 and gia_uong > 0:
    tong = gia_mon * he_so + gia_uong
    print(f"Tổng tiền: {tong} ngàn đồng")
else:
    print("Lựa chọn không hợp lệ!")
```

**Giải thích code:**
* Ba khối `match` chạy tuần tự, mỗi khối **chỉ gán giá** vào biến — tách biệt "tra bảng" với "tính toán".
* Ví dụ: Cơm gà size L + cà phê → `40 * 1.5 + 15 = 75.0` ngàn đồng — khớp ví dụ đề bài.
* Các biến cờ `0` giúp `if` cuối cùng phát hiện lựa chọn sai — nếu dùng số âm làm cờ sẽ càng an toàn, nhưng 0 đủ dùng khi mọi giá > 0.

**Độ phức tạp:** O(1).

---

### Bài 20: Máy bán nước tự động

**Phân tích:** Giao dịch bán hàng: tra bảng sản phẩm, so sánh tiền nhận với giá, trả tiền thừa.

**Ý tưởng:** Match số sản phẩm → tên + giá; `case _` bắt sản phẩm sai; sau đó `if` xử lý tiền.

**Thuật toán:**
1. In danh sách sản phẩm.
2. Nhập số sản phẩm và số tiền.
3. Match sản phẩm: gán tên và giá.
4. Sản phẩm sai → báo lỗi; tiền thiếu → báo thiếu; đủ → in món, giá, tiền thừa.

**Code:**

```python
# In danh sách sản phẩm
print("=== MÁY BÁN NƯỚC ===")
print("1. Trà đá - 5000 đồng")
print("2. Coca - 10000 đồng")
print("3. Nước cam - 15000 đồng")
print("4. Cà phê - 12000 đồng")

# Nhập lựa chọn (ví dụ: 3 và 20000)
san_pham = int(input("Chọn sản phẩm (1-4): "))
tien = int(input("Nhập số tiền: "))

# So khớp sản phẩm với tên và giá
match san_pham:
    case 1:
        ten, gia = "Trà đá", 5000
    case 2:
        ten, gia = "Coca", 10000
    case 3:
        ten, gia = "Nước cam", 15000
    case 4:
        ten, gia = "Cà phê", 12000
    case _:
        ten, gia = "", 0   # Sản phẩm không tồn tại

# Xử lý giao dịch sau khi đã tra bảng
if gia == 0:
    print("San pham khong ton tai!")
elif tien < gia:
    print("Thieu tien!")
else:
    print(f"Ban mua: {ten} - {gia} đồng")
    print(f"Tiền thừa: {tien - gia} đồng")
```

**Giải thích code:**
* `ten, gia = "Trà đá", 5000` — gán **hai biến cùng lúc** từ cặp giá trị (giải nén tuple) — gọn hơn hai lệnh gán riêng.
* `case _:` gán cờ `gia = 0` → dòng `if gia == 0` phát hiện sản phẩm sai.
* Ví dụ: sản phẩm 3 giá 15000, đưa 20000 → thừa 5000 — đúng kết quả đề bài.
* Đây là mô hình thu nhỏ của máy bán hàng thật: tra bảng → kiểm tra tiền → trả hàng và tiền thừa.

**Độ phức tạp:** O(1).

---

## 📌 Lời khuyên cuối

* 🐍 Nhắc lại: mọi code bài này cần **Python 3.10+** — kiểm tra bằng `python --version`.
* 🔀 Hãy tự hỏi: "Mình có đang so một biến với nhiều giá trị cố định không?" → đúng thì match-case là lựa chọn gọn nhất.
* 📏 Nhớ thứ tự: các case đặc biệt (kèm guard) đặt **trước**, `case _` đặt **cuối cùng**.
* 🧪 Nếu kết quả phụ thuộc nhiều biến, thử `match (a, b):` — nó mạnh hơn bạn tưởng.

👉 Tiếp theo: **[Bài 10: Vòng Lặp For](../10_Vong_lap_for/bai_giang.md)**
