# 📥 Bài 7: Nhập và Xuất Dữ Liệu

> 🎓 **Chương 2 – Nền tảng lập trình**

---

## 🎯 Mục tiêu

Sau bài học này, học viên sẽ:

* ✅ Hiểu rõ vai trò của **nhập (input)** và **xuất (output)** trong mọi chương trình.
* ✅ Dùng thành thạo `print()` nâng cao với tham số `sep` và `end`.
* ✅ Dùng `input()` để nhận dữ liệu từ bàn phím, biết rằng nó **luôn trả về chuỗi** `str`.
* ✅ Ép kiểu dữ liệu bằng `int()`, `float()`, `str()` để tính toán đúng.
* ✅ Viết được **f-string** cơ bản để in kết quả đẹp và gọn.
* ✅ Xây dựng chương trình hoàn chỉnh theo luồng: **nhập → xử lý → xuất** (chào hỏi, tính tuổi, diện tích, BMI, đổi tiền...).

---

## 📖 Kiến thức

### 1. Nhìn lại bài 6

Ở bài 6, mọi con số trong chương trình đều được **gán cứng** vào biến:

```python
a = 5      # số 5 "khắc" sẵn trong code
b = 3
print(a + b)
```

Điều này bất tiện: muốn tính với số khác thì phải **sửa code rồi chạy lại**. Bài 7 giúp bạn "trao quyền" cho người dùng — họ nhập số liệu từ bàn phím, chương trình tính và trả lời. Đó chính là lúc chương trình trở nên **tương tác** như phần mềm thật.

```mermaid
flowchart LR
    A[Người dùng nhập liệu<br/>input()] --> B[Chương trình xử lý<br/>biến + toán tử]
    B --> C[Kết quả hiển thị<br/>print()]
```

### 2. `print()` nâng cao: `sep` và `end`

Ở bài 1, bạn biết `print()` in dữ liệu ra màn hình và tự **xuống dòng**. Thực ra `print()` có 2 tham số ẩn:

| Tham số | Giá trị mặc định | Ý nghĩa |
|---|---|---|
| `sep` | dấu cách `" "` | Ký tự chèn **giữa** các đối số |
| `end` | ký tự xuống dòng `"\n"` | Ký tự chèn **cuối** dòng |

**Ví dụ đời thực:** Cột cờ khi in danh sách, các mục ngăn cách bằng dấu `|` như bảng điểm; hoặc đếm ngược không xuống dòng để gây hồi hộp.

```python
# sep: thay dấu cách mặc định bằng dấu gạch
print("Toan", "Van", "Anh", sep=" | ")   # Toan | Van | Anh

# end: không xuống dòng, in liền tiếp
print("3", end=" ")
print("2", end=" ")
print("1")                                # 3 2 1
```

> 💡 `end=""` (chuỗi rỗng) nghĩa là **không** in thêm gì cuối dòng — câu lệnh in tiếp theo sẽ nối liền ngay.

### 3. `input()` — lắng nghe bàn phím

Cú pháp:

```python
ten = input("Bạn tên gì? ")
```

Khi chạy, Python hiện câu hỏi, **dừng lại** chờ người dùng gõ rồi nhấn `Enter`, sau đó mới lưu câu trả lời vào biến.

> ⚠️ **QUY TẮC SỐ 1 CỦA `input()`:** dù người dùng gõ gì — chữ, số, dấu thập phân — `input()` **luôn trả về chuỗi `str`**.

```python
tuoi = input("Bạn bao nhiêu tuổi? ")   # người dùng gõ 15
print(type(tuoi))   # <class 'str'>  - KHÔNG phải số!
```

Vì vậy `tuoi` lúc này là chuỗi `"15"`, chưa thể dùng phép cộng số học với nó. Đây là "cạm bẫy" mà hầu hết người mới đều vấp phải.

### 4. Ép kiểu (type casting) — biến chữ thành số

Vì `input()` trả về `str`, ta phải **ép kiểu** trước khi tính toán:

| Hàm ép kiểu | Công dụng | Ví dụ | Kết quả |
|---|---|---|---|
| `int(x)` | Ép về **số nguyên** | `int("15")` | `15` |
| `float(x)` | Ép về **số thực** | `float("1.6")` | `1.6` |
| `str(x)` | Ép về **chuỗi** | `str(2026)` | `"2026"` |

Hãy thử đoán kết quả của dòng sau — đây là lý do bài học này tồn tại:

```python
print("5" + "3")   # "53" - nối chuỗi, KHÔNG phải 8!
```

```python
# So sánh hai cách viết
a = int("5")   # ép chuỗi "5" thành số 5
b = int("3")   # ép chuỗi "3" thành số 3
print(a + b)   # 8 - giờ là phép cộng số học thật sự
```

**Mẹo viết gọn:** ép kiểu **ngay trong câu lệnh nhập**:

```python
so = int(input("Nhập một số nguyên: "))
chieu_cao = float(input("Nhập chiều cao (m): "))
```

Đây là phong cách chuẩn, được dùng trong hầu hết chương trình thực tế.

> ⚠️ Nếu người dùng gõ thứ không thể ép kiểu (ví dụ `int("abc")`), chương trình báo lỗi **`ValueError`** và dừng — cách xử lý lỗi sẽ học ở bài 19.

### 5. Ép kiểu `int` với số thực — cắt hay làm tròn?

Một chi tiết hay nhầm: `int(3.7)` cho `3` — `int` **cắt bỏ phần thập phân**, không làm tròn. Còn `float("3.5")` cho `3.5`.

> ⚠️ `int("3.5")` báo lỗi `ValueError` — không thể ép chuỗi có dấu chấm thẳng thành số nguyên; phải ép qua `float` trước: `int(float("3.5"))` → `3`.

### 6. f-string — in kết quả đẹp như in báo

Trước đây muốn in "Tổng là 8" phải dùng dấu phẩy:

```python
tong = 8
print("Tổng là", tong)   # được, nhưng cần cẩn thận khoảng trắng
```

**f-string** (f = format) cho phép **chèn biến hoặc biểu thức thẳng vào chuỗi**:

```python
tong = 8
print(f"Tổng là {tong}")             # Tổng là 8
print(f"5 + 3 = {5 + 3}")            # chèn cả biểu thức: 5 + 3 = 8
```

Cú pháp: chữ `f` ngay trước dấu nháy, phần chèn nằm trong cặp `{}`.

**Định dạng số thập phân:** dùng `{biến:.2f}` để giữ 2 chữ số sau dấu phẩy:

```python
so_usd = 94.0
print(f"Số USD: {so_usd:.2f}")   # Số USD: 94.00
```

| Cú pháp | Ý nghĩa | Ví dụ (x = 3.14159) |
|---|---|---|
| `f"{x}"` | In nguyên giá trị | `3.14159` |
| `f"{x:.2f}"` | 2 chữ số thập phân | `3.14` |
| `f"{x:.1f}"` | 1 chữ số thập phân | `3.1` |
| `f"{x:.0f}"` | Số tròn (làm tròn) | `3` |

> 💬 **Ví dụ đời thực:** f-string như việc điền vào **mẫu giấy có sẵn chỗ trống** — phần chữ cố định có sẵn, phần `{...}` là chỗ điền số liệu. Tiện ơi là tiện!

---

## 💡 Ví dụ minh họa

### Ví dụ 1: Máy chào hỏi

```python
# Hỏi tên người dùng và lưu vào biến ten
ten = input("Bạn tên gì? ")
# Chào lại với f-string
print(f"Chào mừng {ten} đến với khóa học Python!")
```

**Giải thích từng dòng:**

| Dòng code | Ý nghĩa |
|---|---|
| `input("Bạn tên gì? ")` | Hiện câu hỏi, dừng chờ người gõ, trả về chuỗi tên |
| `ten = ...` | Lưu câu trả lời vào biến `ten` |
| `f"Chào mừng {ten}..."` | Chèn biến `ten` vào vị trí `{}` của chuỗi |

Kết quả chạy:

```
Bạn tên gì? Mai
Chào mừng Mai đến với khóa học Python!
```

### Ví dụ 2: Cộng hai số (có ép kiểu)

```python
# Nhập hai số nguyên từ bàn phím (ép kiểu ngay khi nhập)
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
# Tính tổng rồi in bằng f-string
print(f"Tổng của {a} và {b} là {a + b}")
```

**Giải thích từng dòng:**

* `int(input(...))` — trước tiên `input()` lấy chuỗi, sau đó `int()` ép thành số nguyên. Nhớ xử lý từ trong ra ngoài: `input` chạy trước, `int` chạy sau.
* `f"... {a + b} ..."` — biểu thức `a + b` được tính **trước** rồi chèn kết quả vào chuỗi.

Kết quả chạy:

```
Nhập số thứ nhất: 7
Nhập số thứ hai: 5
Tổng của 7 và 5 là 12
```

### Ví dụ 3: Diện tích hình chữ nhật

```python
# Nhập chiều dài và chiều rộng dạng số thực
chieu_dai = float(input("Nhập chiều dài: "))
chieu_rong = float(input("Nhập chiều rộng: "))
# Công thức diện tích
dien_tich = chieu_dai * chieu_rong
# In kết quả
print(f"Diện tích hình chữ nhật là: {dien_tich}")
```

**Giải thích từng dòng:**

* `float(input(...))` — vì chiều dài có thể là `5.5`, ta ép sang `float`, không phải `int`.
* `chieu_dai * chieu_rong` — nhân hai số thực, kết quả là số thực.

Kết quả chạy:

```
Nhập chiều dài: 5
Nhập chiều rộng: 10
Diện tích hình chữ nhật là: 50.0
```

### Ví dụ 4: `sep` và `end` trong thực tế

```python
# In 3 môn học ngăn cách bởi dấu |
print("Toán", "Văn", "Anh", sep=" | ")

# Đếm ngược trên cùng một dòng
print("3", end="... ")
print("2", end="... ")
print("1")
print("Phóng!")
```

**Giải thích từng dòng:**

* `sep=" | "` — các môn học in trên một dòng, cách nhau bởi ` | `.
* `end="... "` — mỗi số in xong **không xuống dòng** mà in tiếp chuỗi `... `.
* `print("1")` — không chỉ định `end` nên cuối dòng tự động xuống dòng mới.

Kết quả chạy:

```
Toán | Văn | Anh
3... 2... 1
Phóng!
```

---

## 🔬 Ví dụ nâng cao

### Ví dụ 1: Chương trình tính BMI

> 💡 Bài toán thực tế từ giáo trình: nhập cân nặng (kg) và chiều cao (m), tính `BMI = kg / (cao * cao)`.

```python
# Nhập cân nặng và chiều cao
kg = float(input("Hãy nhập số kg: "))
chieu_cao = float(input("Hãy nhập chiều cao (m): "))
# Công thức BMI
bmi = kg / (chieu_cao * chieu_cao)
# In kết quả làm tròn 2 chữ số thập phân
print(f"BMI của bạn là: {bmi:.2f}")
```

Kết quả chạy:

```
Hãy nhập số kg: 80
Hãy nhập chiều cao (m): 1.6
BMI của bạn là: 31.25
```

> 💡 Với chiều cao 1.6 m, phải ép kiểu `float` nếu không chương trình lỗi ngay khi nhập `1.6`. Và nhớ `{bmi:.2f}` giúp kết quả gọn đẹp thay vì `31.249999999999993`.

### Ví dụ 2: Tính tuổi từ năm sinh

```python
# Năm hiện tại
nam_hien_tai = 2026
# Nhập năm sinh
nam_sinh = int(input("Bạn sinh năm bao nhiêu? "))
# Tính tuổi
tuoi = nam_hien_tai - nam_sinh
# In kết quả
print(f"Năm nay bạn {tuoi} tuổi.")
```

Kết quả chạy:

```
Bạn sinh năm bao nhiêu? 2010
Năm nay bạn 16 tuổi.
```

> 💡 Nếu quên `int()`, phép trừ `2026 - "2010"` sẽ báo lỗi `TypeError` — máy không biết trừ số với chữ.

### Ví dụ 3: Đổi tiền VND sang USD

```python
# Tỉ giá 1 USD = 25000 VND
ti_gia = 25000
# Nhập số tiền VND
so_vnd = float(input("Hãy nhập số tiền VND muốn quy đổi thành USD: "))
# Quy đổi
so_usd = so_vnd / ti_gia
# In kết quả với 2 chữ số thập phân
print(f"{so_vnd:,.0f} VND được đổi thành {so_usd:.2f} USD")
```

Kết quả chạy:

```
Hãy nhập số tiền VND muốn quy đổi thành USD: 2350000
2,350,000 VND được đổi thành 94.00 USD
```

> 💡 `{so_vnd:,.0f}` — dấu phẩy trong định dạng giúp **tách hàng nghìn** cho số lớn dễ đọc.

### Ví dụ 4: Trung bình cộng ba số

```python
# Nhập ba số nguyên
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
# Trung bình cộng - phép chia luôn cho số thực
trung_binh = (a + b + c) / 3
# In kết quả
print(f"Trung bình cộng của {a}, {b}, {c}: {trung_binh}")
```

Kết quả chạy:

```
Nhập số a: 4
Nhập số b: 5
Nhập số c: 7
Trung bình cộng của 4, 5, 7: 5.333333333333333
```

---

## ⚠️ Lỗi thường gặp

### Lỗi 1: Quên ép kiểu — kết quả sai ngầm (không báo lỗi!)

```python
a = input("Nhập số a: ")   # người dùng gõ 5 -> "5" (chuỗi)
b = input("Nhập số b: ")   # người dùng gõ 3 -> "3"
print(a + b)               # "53" chứ không phải 8
```

* **Nguyên nhân:** `input()` trả về `str`; dấu `+` với hai chuỗi là **nối chuỗi**.
* **Nguy hiểm:** chương trình chạy "trơn tru" nhưng kết quả sai — khó phát hiện nhất.
* **Cách sửa:** `a = int(input("Nhập số a: "))`.

### Lỗi 2: TypeError khi trộn số với chuỗi

```python
tuoi = input("Bạn bao nhiêu tuổi? ")   # "16"
print("Năm sau bạn", tuoi + 1, "tuổi")   # ❌ TypeError
```

* **Kết quả báo:** `TypeError: can only concatenate str (not "int") to str`.
* **Nguyên nhân:** cộng chuỗi `"16"` với số `1` — hai kiểu khác nhau.
* **Cách sửa:** ép kiểu: `tuoi = int(input("Bạn bao nhiêu tuổi? "))` rồi mới tính.

### Lỗi 3: ValueError khi ép kiểu sai dữ liệu

```python
so = int(input("Nhập một số: "))   # người dùng gõ "3.5" hoặc "abc"
```

* **Kết quả báo:** `ValueError: invalid literal for int() with base 10: '3.5'`.
* **Nguyên nhân:** `int()` không nhận chuỗi có dấu chấm; `int("abc")` cũng lỗi.
* **Cách sửa:** số thập phân thì ép `float("3.5")`; muốn số nguyên từ `3.5` thì `int(float("3.5"))`.

### Lỗi 4: Nhầm `int` với `float` khi nhập số thực

```python
chieu_cao = int(input("Nhập chiều cao (m): "))   # gõ 1.6 -> lỗi!
```

* **Nguyên nhân:** chiều cao là số thực, không thể ép thẳng bằng `int()`.
* **Cách sửa:** dùng `float()`; chỉ dùng `int()` khi chắc chắn dữ liệu là số nguyên (tuổi, số lượng...).

### Lỗi 5: Quên gán kết quả `input()`

```python
input("Bạn tên gì? ")     # hỏi xong... biến mất!
print("Chào", ten)        # ❌ NameError: name 'ten' is not defined
```

* **Nguyên nhân:** `input()` trả về dữ liệu, nhưng không gán vào biến thì dữ liệu "bay hơi" ngay.
* **Cách sửa:** luôn gán: `ten = input("Bạn tên gì? ")`.

---

## 💎 Mẹo

* 🎯 **Nhập và ép kiểu ngay một lần:** `so = int(input("..."))` — gọn, ít quên.
* 📐 **Chọn đúng loại ép kiểu:** số lượng, tuổi → `int`; tiền, chiều cao, điểm → `float`.
* ✨ **f-string thay cho phép nối chuỗi:** `f"Tổng: {tong}"` đẹp hơn `"Tổng: " + str(tong)`.
* 💵 **Tiền và tỉ giá:** luôn in dạng `:.2f` để có 2 chữ số thập phân như hóa đơn thật.
* 🧹 **Vệ sinh dữ liệu:** nếu người dùng gõ thừa khoảng trắng (ví dụ `" Mai "`), dùng `.strip()`: `input("Tên: ").strip()`.
* 🧪 **Thử các trường hợp biên:** chạy thử nhập số 0, số âm, chữ cái để biết chương trình phản ứng thế nào.
* 🔍 **`type()` là "kính lúp":** khi nghi ngờ dữ liệu thuộc kiểu gì, in thử `print(type(bien))`.

---

## 📝 Tóm tắt

| Khái niệm | Nội dung chính |
|---|---|
| 📤 `print(..., sep=, end=)` | In nhiều dữ liệu; `sep` đổi dấu phân cách, `end` đổi ký tự kết thúc dòng |
| 📥 `input("câu hỏi")` | Nhận dữ liệu từ bàn phím, **luôn trả về `str`** |
| 🔄 Ép kiểu | `int()` số nguyên, `float()` số thực, `str()` chuỗi |
| 🎨 f-string | `f"... {biến} ..."` chèn biến/biểu thức vào chuỗi; `{x:.2f}` định dạng số |
| 🔁 Luồng chương trình | Nhập → ép kiểu → xử lý (toán tử) → in kết quả |

---

## 🧪 Kiểm tra nhanh

1. ❓ `input()` luôn trả về kiểu dữ liệu nào?
2. ❓ Viết lệnh nhập một số nguyên từ bàn phím và ép kiểu ngay.
3. ❓ `print(1, 2, 3, sep="-")` in ra gì?
4. ❓ `print("A", end=""); print("B")` in ra gì?
5. ❓ `"5" + "3"` bằng bao nhiêu? Vì sao?
6. ❓ Viết câu lệnh in "Tổng là 8" bằng f-string khi biết `tong = 8`.
7. ❓ `f"{3.14159:.2f}"` cho kết quả gì?
8. ❓ Lỗi gì xảy ra khi gõ `int("3.5")`?
9. ❓ Khi nào dùng `int()`, khi nào dùng `float()` để ép kiểu?
10. ❓ Sắp xếp đúng thứ tự luồng dữ liệu: xử lý, xuất, nhập.

<details>
<summary>🔍 Xem đáp án</summary>

1. Chuỗi `str` — dù người dùng gõ số vẫn là chuỗi.
2. `so = int(input("Nhập một số nguyên: "))`.
3. `1-2-3`.
4. `AB` — không xuống dòng giữa hai lệnh.
5. `"53"` — nối hai chuỗi lại với nhau, không phải phép cộng số.
6. `print(f"Tổng là {tong}")`.
7. `3.14`.
8. `ValueError` — `int()` không ép được chuỗi có dấu chấm.
9. `int()` cho số nguyên (tuổi, số lượng); `float()` cho số thực (tiền, chiều cao, điểm).
10. Nhập → xử lý → xuất.

</details>

---

## 📚 Bài đọc thêm

* [Python.org – Hàm input()](https://docs.python.org/3/library/functions.html#input)
* [Python.org – Hàm print()](https://docs.python.org/3/library/functions.html#print)
* [Python.org – Formatted String Literals (f-string)](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals)
* [W3Schools – Python User Input](https://www.w3schools.com/python/python_user_input.asp)
* [Real Python – Python String Formatting](https://realpython.com/python-string-formatting/)

---

## 🏁 Kết thúc bài

🎉 Giờ đây chương trình của bạn đã biết **nghe và nói**: nhận dữ liệu từ bàn phím, tính toán và in kết quả đẹp mắt. Nhưng máy tính còn thiếu một khả năng quan trọng nhất — **tự quyết định**! Chẳng hạn "Nếu điểm >= 5 thì in Đậu, ngược lại in Rớt". Kiến thức đó nằm ở bài kế tiếp:

👉 **[Bài 8: Câu Lệnh If – Cấu Trúc Rẽ Nhánh](../08_Cau_lenh_if/bai_giang.md)**
