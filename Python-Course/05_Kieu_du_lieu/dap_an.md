# ✅ Bài 5: Đáp Án – Kiểu Dữ Liệu Cơ Bản

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án để việc học hiệu quả nhất.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Nhận diện kiểu dữ liệu

**Phân tích:** Cần in kiểu của 4 giá trị thuộc 4 kiểu khác nhau.

**Ý tưởng:** `type()` cho từng giá trị; chú ý `7.0` có dấu chấm là `float`, `"7"` có nháy là `str`.

**Thuật toán:**
1. In `type(7)`.
2. In `type(7.0)`.
3. In `type("7")`.
4. In `type(True)`.

**Code:**

```python
print(type(7))       # int
print(type(7.0))     # float
print(type("7"))     # str
print(type(True))    # bool
```

**Giải thích code:**

* `7` — không dấu chấm, không nháy → `int`.
* `7.0` — có dấu chấm → `float`.
* `"7"` — nằm trong dấu nháy → `str`, kể cả khi nội dung là chữ số.
* `True` — viết hoa, không nháy → `bool`.

**Độ phức tạp:** O(1).

---

### Bài 2: Khai báo đủ 4 loại

**Phân tích:** Khai báo biến 4 kiểu và in đồng loạt.

**Ý tưởng:** Gán giá trị phù hợp từng kiểu; `print` nhiều đối số.

**Thuật toán:**
1. Gán 4 biến.
2. In cả 4.

**Code:**

```python
nam = 2026          # int
diem = 8.5          # float
mon_hoc = "Python"  # str
da_hoc = True       # bool
print(nam, diem, mon_hoc, da_hoc)
```

**Giải thích code:**

* Mỗi biến mang đúng kiểu của giá trị được gán.
* `print` với dấu phẩy in các giá trị cách nhau khoảng trắng trên một dòng.

**Độ phức tạp:** O(1).

---

### Bài 3: Số hay chữ?

**Phân tích:** Phân biệt phép cộng số và phép nối chuỗi.

**Ý tưởng:** `5 + 3` là cộng số → `8`; `"5" + "3"` là nối chữ → `"53"`.

**Thuật toán:**
1. In `5 + 3`.
2. In `"5" + "3"`.

**Code:**

```python
print(5 + 3)       # số cộng số
print("5" + "3")   # chữ nối chữ
```

**Giải thích code:**

* Dấu `+` với hai số → phép cộng.
* Dấu `+` với hai chuỗi → phép nối chuỗi.
* Kết quả khác hẳn nhau: `8` và `53` — đây là lý do phải phân biệt kiểu dữ liệu.

**Độ phức tạp:** O(1).

---

### Bài 4: Đếm ký tự

**Phân tích:** `len()` trả về số nguyên dù nguồn là chuỗi.

**Ý tưởng:** `so_ky_tu = len("Python")` — `"Python"` có 6 ký tự.

**Thuật toán:**
1. Gán `so_ky_tu = len("Python")`.
2. In giá trị và kiểu.

**Code:**

```python
so_ky_tu = len("Python")
print(so_ky_tu)
print(type(so_ky_tu))
```

**Giải thích code:**

* `len()` đếm ký tự: `P-y-t-h-o-n` → 6.
* Kết quả là số nguyên nên `type()` cho `<class 'int'>`.

**Độ phức tạp:** O(1).

---

### Bài 5: Nối chuỗi và số

**Phân tích:** Nối chuỗi chữ với biến chuỗi bằng `+`.

**Ý tưởng:** `"Chao ban " + ten` — chú ý khoảng trắng cuối chuỗi đầu.

**Thuật toán:**
1. Gán `ten = "Mai"`.
2. Nối và in.

**Code:**

```python
ten = "Mai"
print("Chao ban " + ten)
```

**Giải thích code:**

* Chuỗi `"Chao ban "` có sẵn một khoảng trắng ở cuối nên câu in ra là `Chao ban Mai` đẹp mắt.
* Cả hai vế đều là `str` nên phép `+` là nối chuỗi.

**Độ phức tạp:** O(1).

---

### Bài 6: Ép chuỗi thành số

**Phân tích:** `"10"` là chuỗi — phải ép `int` mới cộng được với số.

**Ý tưởng:** `int("10")` → `10`; cộng `5` → `15`.

**Thuật toán:**
1. Gán `so = "10"`.
2. Ép kiểu rồi cộng và in.

**Code:**

```python
so = "10"
print(int(so) + 5)
```

**Giải thích code:**

* `int(so)` biến chuỗi `"10"` thành số `10`.
* `10 + 5 = 15`.
* Nếu quên ép kiểu, `"10" + 5` sẽ báo `TypeError`.

**Độ phức tạp:** O(1).

---

### Bài 7: Ép số thành chuỗi

**Phân tích:** Cần nối số vào chuỗi — phải `str()` số đó trước.

**Ý tưởng:** `"Nam " + str(nam) + " la nam moi"`.

**Thuật toán:**
1. Gán `nam = 2026`.
2. Ép `str` và nối rồi in.

**Code:**

```python
nam = 2026
print("Nam " + str(nam) + " la nam moi")
```

**Giải thích code:**

* `str(nam)` biến số 2026 thành chuỗi `"2026"` để có thể `+` với chuỗi khác.
* Thiếu bước này sẽ báo `TypeError`.

**Độ phức tạp:** O(1).

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Toàn cảnh kiểu dữ liệu

**Phân tích:** Kiểm tra kiểu của kết quả phép so sánh và các phép ép kiểu.

**Ý tưởng:** Đặt từng biểu thức vào `type()`.

**Thuật toán:**
1. `type(10 > 3)` → bool.
2. `type(float(7))` → float.
3. `type(int("9"))` → int.
4. `type(str(3.14))` → str.

**Code:**

```python
print(type(10 > 3))    # kết quả so sánh là bool
print(type(float(7)))  # ép số nguyên thành số thực
print(type(int("9")))  # ép chuỗi thành số nguyên
print(type(str(3.14))) # ép số thực thành chuỗi
```

**Giải thích code:**

* `10 > 3` là `True` — phép so sánh luôn cho `bool`.
* `float(7)` → `7.0` (`float`); `int("9")` → `9` (`int`); `str(3.14)` → `"3.14"` (`str`).

**Độ phức tạp:** O(1).

---

### Bài 9: Điểm mới của học sinh

**Phân tích:** Điểm dạng chuỗi `"8.5"` chứa dấu chấm → ép `float`, không ép `int`.

**Ý tưởng:** `float("8.5")` → `8.5`; cộng `0.5` → `9.0`.

**Thuật toán:**
1. Gán `diem_so = "8.5"`.
2. Ép float, cộng thưởng.
3. In kết quả.

**Code:**

```python
diem_so = "8.5"
# Chuỗi thập phân phải ép float
diem_moi = float(diem_so) + 0.5
print("Diem moi:", diem_moi)
```

**Giải thích code:**

* Nếu ép `int("8.5")` sẽ báo `ValueError` vì chuỗi không phải dạng số nguyên.
* `8.5 + 0.5 = 9.0` — kiểu float.

**Độ phức tạp:** O(1).

---

### Bài 10: Cắt phần thập phân

**Phân tích:** Lấy phần nguyên của giá trị thập phân.

**Ý tưởng:** `int(19.99)` cắt phần lẻ → `19` (không làm tròn).

**Thuật toán:**
1. Gán `gia = 19.99`.
2. `int(gia)` và in.

**Code:**

```python
gia = 19.99
print("Gia nguyen:", int(gia))
```

**Giải thích code:**

* `int(19.99)` → `19`: hàm `int` với số thực sẽ **cắt bỏ** phần thập phân.
* Để làm tròn lên 20 phải dùng `round(19.99)` — nhưng bài này yêu cầu cắt.

**Độ phức tạp:** O(1).

---

### Bài 11: Kiểm tra hàm `bool`

**Phân tích:** `bool()` trả về `True`/`False` theo quy tắc: giá trị "rỗng" và 0 → `False`.

**Ý tưởng:** In từng trường hợp với nhãn.

**Thuật toán:**
1. In `bool(0)`.
2. In `bool(1)`.
3. In `bool("")`.
4. In `bool("Python")`.
5. In `bool(0.0)`.

**Code:**

```python
print("bool(0) =", bool(0))
print("bool(1) =", bool(1))
print('bool("") =', bool(""))
print('bool("Python") =', bool("Python"))
print("bool(0.0) =", bool(0.0))
```

**Giải thích code:**

* `0`, `0.0`, `""` (chuỗi rỗng) → `False`.
* `1`, chuỗi khác rỗng → `True`.
* Lưu ý: `""` là chuỗi rỗng (không ký tự nào) — khác với `" "` (một khoảng trắng, vẫn là `True`).

**Độ phức tạp:** O(1).

---

### Bài 12: Ghép chuỗi số tuổi

**Phân tích:** Nối nhiều biến số vào câu chữ — cần ép `str` từng số.

**Ý tưởng:** `"Toi " + str(tuoi) + " tuoi, hoc lop " + str(lop)`.

**Thuật toán:**
1. Gán `tuoi`, `lop`.
2. Ép `str` và nối.
3. In.

**Code:**

```python
tuoi = 15
lop = 10
# Ép cả hai số thành chuỗi rồi nối
cau = "Toi " + str(tuoi) + " tuoi, hoc lop " + str(lop)
print(cau)
```

**Giải thích code:**

* `str(tuoi)` → `"15"`, `str(lop)` → `"10"`.
* Toàn bộ vế phải là chuỗi nên `+` thực hiện nối thành câu hoàn chỉnh.

**Độ phức tạp:** O(1).

---

### Bài 13: Hé lộ lỗi TypeError

**Phân tích:** `"Diem cua toi: " + diem` nối chuỗi với `int` → `TypeError`.

**Ý tưởng:** Ép `str(diem)` trước khi nối.

**Thuật toán:**
1. Gán `diem = 8`.
2. Nối với `str(diem)`.
3. In.

**Code:**

```python
diem = 8
print("Diem cua toi: " + str(diem))
```

**Giải thích code:**

* Code gốc báo `TypeError: can only concatenate str (not "int") to str`.
* Sau khi ép `str(diem)`, hai vế cùng là chuỗi, phép `+` nối thành công.

**Độ phức tạp:** O(1).

---

### Bài 14: Độ dài của số hay chữ?

**Phân tích:** `len` chỉ đếm chuỗi. `"2026"` có 4 ký tự; `str(2026)` cũng ra `"2026"` nên cả hai cùng 4.

**Ý tưởng:** Tính hai lần và in so sánh.

**Thuật toán:**
1. In `len("2026")`.
2. In `len(str(2026))`.

**Code:**

```python
print('len("2026") =', len("2026"))
print("len(str(2026)) =", len(str(2026)))
```

**Giải thích code:**

* `len("2026")` → 4.
* `str(2026)` → `"2026"` → `len` = 4.
* Hai cách cho cùng kết quả vì cả hai đều đếm chuỗi 4 ký tự.

**Độ phức tạp:** O(1).

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Chuyển đổi linh hoạt qua trung gian

**Phân tích:** Chuỗi thập phân không ép thẳng sang `int` được — phải qua `float`.

**Ý tưởng:** `int(float("7.8"))` → `int(7.8)` → `7`.

**Thuật toán:**
1. Ép `"7.8"` thành `float`.
2. Ép `float` thành `int`.
3. In giá trị và kiểu.

**Code:**

```python
gia_tri = "7.8"
# Qua float trung gian rồi mới sang int
ket_qua = int(float(gia_tri))
print("Gia tri:", ket_qua, "- Kieu:", type(ket_qua))
```

**Giải thích code:**

* `float("7.8")` → `7.8`.
* `int(7.8)` → `7` (cắt phần lẻ).
* Nếu viết thẳng `int("7.8")` sẽ bị `ValueError`.

**Độ phức tạp:** O(1).

---

### Bài 16: Kiểm tra True/False của phép so sánh

**Phân tích:** Biểu thức kết hợp so sánh và logic `and` trả về `bool`.

**Ý tưởng:** Tính `10 > 5 and 10 < 20` — cả hai đều đúng nên kết quả `True`.

**Thuật toán:**
1. Gán `ket_qua`.
2. In giá trị và kiểu.

**Code:**

```python
# Cả hai vế đều đúng nên kết quả True
ket_qua = 10 > 5 and 10 < 20
print("Ket qua:", ket_qua)
print("Kieu:", type(ket_qua))
```

**Giải thích code:**

* `10 > 5` → `True`, `10 < 20` → `True`; `and` đúng khi cả hai đúng → `True`.
* Kết quả phép so sánh/logic luôn là `bool`.

**Độ phức tạp:** O(1).

---

### Bài 17: Máy tách phần nguyên – phần thập phân

**Phân tích:** Tách `12.68` thành `12` và `0.68` bằng phép ép kiểu và trừ.

**Ý tưởng:** Phần nguyên = `int(so_thuc)`; phần thập phân = số gốc trừ phần nguyên, làm tròn để tránh sai số máy tính.

**Thuật toán:**
1. Gán `so_thuc = 12.68`.
2. Tính `phan_nguyen = int(so_thuc)`.
3. Tính `phan_thap_phan = round(so_thuc - phan_nguyen, 2)`.
4. In kèm kiểu.

**Code:**

```python
so_thuc = 12.68
# Phần nguyên là phần bị cắt bởi int()
phan_nguyen = int(so_thuc)
# Phần thập phân = số gốc trừ phần nguyên
phan_thap_phan = round(so_thuc - phan_nguyen, 2)
print("Phan nguyen:", phan_nguyen, "(int)")
print("Phan thap phan:", phan_thap_phan, "(float)")
```

**Giải thích code:**

* `int(12.68)` → `12`.
* `12.68 - 12 = 0.679999...` — máy tính biểu diễn số thập phân không chính xác tuyệt đối, nên `round(..., 2)` cho lại `0.68`.

**Độ phức tạp:** O(1).

---

### Bài 18: Bảng tóm tắt — in và kiểu

**Phân tích:** Ép kiểu 4 hướng khác nhau, đặc biệt `bool("0")` — chuỗi khác số.

**Ý tưởng:** `"0"` là chuỗi không rỗng → `bool` là `True` dù nội dung là chữ số 0.

**Thuật toán:**
1. Tính và ép từng giá trị.
2. In từng dòng với `str()` và `type()`.

**Code:**

```python
g1 = str(123)          # chuỗi "123"
g2 = int("45")         # số 45
g3 = float("6.5")      # số 6.5
g4 = bool("0")         # chuỗi "0" khác rỗng -> True
print("Gia tri:", g1, "- Kieu:", type(g1))
print("Gia tri:", g2, "- Kieu:", type(g2))
print("Gia tri:", g3, "- Kieu:", type(g3))
print("Gia tri:", g4, "- Kieu:", type(g4))
```

**Giải thích code:**

* `str(123)` → `"123"` (`str`); `int("45")` → `45` (`int`); `float("6.5")` → `6.5` (`float`).
* `bool("0")` → `True`: chuỗi "0" không rỗng; chỉ chuỗi `""` mới là `False`. Đây là bẫy kinh điển dễ nhầm với `bool(0)`.

**Độ phức tạp:** O(1).

---

### Bài 19: Giá trị trung bình "trộn kiểu"

**Phân tích:** Hai điểm dạng chuỗi khác nhau — một cái ép `int`, một cái ép `float`.

**Ý tưởng:** `(int("7") + float("8.5")) / 2` → `(7 + 8.5) / 2` → `7.75`.

**Thuật toán:**
1. Gán hai điểm chuỗi.
2. Ép kiểu phù hợp từng biến.
3. Tính trung bình và in.

**Code:**

```python
diem1 = "7"
diem2 = "8.5"
# Ép từng chuỗi về đúng kiểu số
tong = int(diem1) + float(diem2)
trung_binh = tong / 2
print("Trung binh:", trung_binh)
print("Kieu ket qua:", type(trung_binh))
```

**Giải thích code:**

* `int("7")` → 7, `float("8.5")` → 8.5 — tổng là 15.5.
* Chia 2 → `7.75` kiểu `float` (phép `/` luôn cho float).

**Độ phức tạp:** O(1).

---

### Bài 20: Chương trình "thay đồ" cho biến

**Phân tích:** Một biến trải qua nhiều kiểu dữ liệu — minh họa định kiểu động của Python.

**Ý tưởng:** Gán và in từng bước; cuối cùng ép `"10.0"` về float và so sánh.

**Thuật toán:**
1. `x = 10`, in + type.
2. `x = "mot"`, in + type.
3. `x = 10.0`, in + type.
4. `x = False`, in + type.
5. `x = "10.0"`, in + type.
6. So sánh `float(x) == 10.0`.

**Code:**

```python
x = 10
print(x, type(x))
x = "mot"
print(x, type(x))
x = 10.0
print(x, type(x))
x = False
print(x, type(x))
x = "10.0"
print(x, type(x))
# Ép chuỗi "10.0" về số thực rồi so sánh
print("float(x) == 10.0:", float(x) == 10.0)
```

**Giải thích code:**

* Mỗi lần gán, biến `x` mang kiểu của giá trị mới — Python không khóa kiểu cho biến.
* `float("10.0")` → `10.0`, so sánh `==` với `10.0` → `True`.
* Đây là nền tảng để hiểu cơ chế "gán lại" mà chương trình thực tế thường dùng.

**Độ phức tạp:** O(1).

---

## 📌 Lời khuyên cuối

* Muốn biết biến mang kiểu gì → `print(type(bien))`.
* Muốn tính toán với dữ liệu nhập vào → **ép kiểu trước, tính sau**.
* `int()` cắt phần lẻ, không làm tròn — muốn làm tròn dùng `round()`.
* Chữ số trong dấu nháy vẫn là chữ: `"5"` ≠ `5`.

👉 Tiếp theo: **[Bài 6: Toán Tử](../06_Toan_tu/bai_giang.md)**