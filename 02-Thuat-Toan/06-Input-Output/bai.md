<!-- TỰ ĐỘNG ĐỒNG BỘ từ 01-Co-Ban/07-Input-Output/bai.md — đừng sửa trực tiếp, sửa bản chính rồi chạy tools/sync_tracks.py -->

# Bài 6 — Nhập và Xuất Dữ Liệu

> 🎓 **Chương 2 – Nền tảng lập trình**

## 🧠 Điều kiện tiên quyết

- [Bài 1 — Giới Thiệu Python](../01-Gioi-Thieu/bai.md)
- [Bài 3 — Biến Trong Python](../03-Bien/bai.md)

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

Điều này bất tiện: muốn tính với số khác thì phải **sửa code rồi chạy lại**. Bài 6 giúp bạn "trao quyền" cho người dùng — họ nhập số liệu từ bàn phím, chương trình tính và trả lời. Đó chính là lúc chương trình trở nên **tương tác** như phần mềm thật.

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

---

## 🧩 Bài tập

> 📝 🎯 **Chủ đề:** `print()` với `sep`/`end`, `input()` trả về chuỗi, ép kiểu `int`/`float`/`str`, f-string cơ bản. Tất cả bài đều có nhập liệu từ bàn phím.

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Máy chào hỏi

* **Đề bài:** Nhập tên của bạn rồi in ra lời chào `Xin chào <tên>!`
* **Input:** Một dòng là tên.
* **Output:** Dòng chào có chứa tên.
* **Ví dụ:**
  ```
  Bạn tên gì? Mai
  Xin chào Mai!
  ```
* **Gợi ý:** `ten = input("Bạn tên gì? ")` rồi in với f-string.

### Bài 2: Hỏi và in lại câu trả lời

* **Đề bài:** Hỏi người dùng "Bạn thích ăn gì?" rồi in lại câu `Hôm nay bạn sẽ ăn <món> nhé!`
* **Input:** Một dòng là tên món ăn.
* **Output:** Dòng nhắc lại món ăn.
* **Ví dụ:**
  ```
  Bạn thích ăn gì? Phở
  Hôm nay bạn sẽ ăn Phở nhé!
  ```
* **Gợi ý:** Kết quả `input()` lưu vào biến rồi mới dùng.

### Bài 3: Cộng hai số

* **Đề bài:** Nhập hai số nguyên từ bàn phím, in ra tổng của chúng.
* **Input:** Hai dòng, mỗi dòng một số nguyên.
* **Output:** `Tổng của <a> và <b> là <tổng>`
* **Ví dụ:**
  ```
  Nhập số thứ nhất: 7
  Nhập số thứ hai: 5
  Tổng của 7 và 5 là 12
  ```
* **Gợi ý:** Quên ép kiểu `int()` thì `"7" + "5"` sẽ thành `"75"` — nhớ ép kiểu ngay khi nhập.

### Bài 4: In liền một dòng với `end`

* **Đề bài:** Nhập một chuỗi bất kỳ rồi in nó 3 lần **trên cùng một dòng**, cách nhau một dấu cách, dùng tham số `end`.
* **Input:** Một dòng là chuỗi (ví dụ `hoc`).
* **Output:** Chuỗi đó lặp lại 3 lần trên một dòng.
* **Ví dụ:**
  ```
  Nhập từ cần lặp: hoc
  hoc hoc hoc
  ```
* **Gợi ý:** `print(tu, end=" ")` hai lần rồi lần cuối in bình thường để xuống dòng.

### Bài 5: Ngăn cách bằng `sep`

* **Đề bài:** Nhập tên, lớp và trường rồi in cả ba trên một dòng, ngăn cách bởi dấu ` - `.
* **Input:** Ba dòng dữ liệu.
* **Output:** Một dòng có dạng `Tên - Lớp - Trường`.
* **Ví dụ:**
  ```
  Nhập tên: Mai
  Nhập lớp: 10A1
  Nhập trường: THPT Python
  Mai - 10A1 - THPT Python
  ```
* **Gợi ý:** `print(ten, lop, truong, sep=" - ")`.

### Bài 6: Diện tích hình chữ nhật

* **Đề bài:** Nhập chiều dài và chiều rộng (số thực), in ra diện tích hình chữ nhật.
* **Input:** Hai dòng số thực.
* **Output:** `Diện tích hình chữ nhật là: <kết quả>`
* **Ví dụ:**
  ```
  Nhập chiều dài: 5
  Nhập chiều rộng: 10
  Diện tích hình chữ nhật là: 50.0
  ```
* **Gợi ý:** Diện tích = dài × rộng; chiều dài có thể là số thập phân nên dùng `float`.

### Bài 7: Trung bình cộng ba số

* **Đề bài:** Nhập ba số thực, in ra trung bình cộng của chúng.
* **Input:** Ba dòng số thực.
* **Output:** `Trung bình cộng của a, b, c: <kết quả>`
* **Ví dụ:**
  ```
  Nhập số a: 4
  Nhập số b: 5
  Nhập số c: 7
  Trung bình cộng của a, b, c: 5.333333333333333
  ```
* **Gợi ý:** Trung bình = (a + b + c) / 3 — nhớ ngoặc bao tử số.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Tính tuổi

* **Đề bài:** Nhập năm sinh (số nguyên), tính và in tuổi tính đến năm 2026.
* **Input:** Một dòng là năm sinh.
* **Output:** `Bạn <tuổi> tuổi.`
* **Ví dụ:**
  ```
  Bạn sinh năm bao nhiêu? 2010
  Bạn 16 tuổi.
  ```
* **Gợi ý:** `tuoi = 2026 - nam_sinh`; năm sinh phải ép `int`.

### Bài 9: Chu vi và diện tích hình tròn

* **Đề bài:** Nhập bán kính (số thực), in chu vi và diện tích hình tròn với `pi = 3.14`, làm tròn 2 chữ số thập phân.
* **Input:** Một dòng là bán kính.
* **Output:** Hai dòng `Chu vi: <kết quả>` và `Diện tích: <kết quả>` (2 chữ số thập phân).
* **Ví dụ:**
  ```
  Nhập bán kính: 5
  Chu vi: 31.40
  Diện tích: 78.50
  ```
* **Gợi ý:** `chu_vi = 2 * 3.14 * r`, `dien_tich = 3.14 * r * r`; dùng `{:.2f}` trong f-string.

### Bài 10: Đổi tiền VND sang USD

* **Đề bài:** Nhập số tiền VND, đổi sang USD theo tỉ giá `1 USD = 25000 VND`, in kết quả 2 chữ số thập phân.
* **Input:** Một dòng số tiền VND.
* **Output:** `<số VND> VND được đổi thành <số USD> USD`
* **Ví dụ:**
  ```
  Hãy nhập số tiền VND muốn quy đổi thành USD: 2350000
  2350000 VND được đổi thành 94.00 USD
  ```
* **Gợi ý:** `so_usd = so_vnd / 25000`; tiền là số thực, dùng `{:.2f}`.

### Bài 11: Vận tốc trung bình

* **Đề bài:** Nhập quãng đường (km) và thời gian (giờ), tính vận tốc theo công thức `v = s / t` và in kết quả.
* **Input:** Hai dòng số thực (quãng đường, thời gian).
* **Output:** `Vận tốc = <vận tốc> km/h` (1 chữ số thập phân).
* **Ví dụ:**
  ```
  Nhập số km: 120
  Nhập thời gian (h): 2.5
  Vận tốc = 48.0 km/h
  ```
* **Gợi ý:** `v = s / t`; nhớ ép `float` cho cả hai.

### Bài 12: Chương trình tính BMI

* **Đề bài:** Nhập cân nặng (kg) và chiều cao (m), tính BMI theo công thức `BMI = kg / (cao * cao)`, in 2 chữ số thập phân.
* **Input:** Hai dòng số thực (kg, chiều cao).
* **Output:** `BMI của bạn là: <kết quả>`
* **Ví dụ:**
  ```
  Hãy nhập số kg: 80
  Hãy nhập chiều cao (m): 1.6
  BMI của bạn là: 31.25
  ```
* **Gợi ý:** Chiều cao là số thực → `float`; đừng quên ngoặc quanh `cao * cao`.

### Bài 13: Đổi độ C sang độ F

* **Đề bài:** Nhập nhiệt độ theo độ C, đổi sang độ F theo công thức `F = C * 9 / 5 + 32`, in kết quả 1 chữ số thập phân.
* **Input:** Một dòng nhiệt độ C (số thực).
* **Output:** `C độ C = <kết quả> độ F`
* **Ví dụ:**
  ```
  Nhập nhiệt độ (°C): 20.5
  20.5 độ C = 68.9 độ F
  ```
* **Gợi ý:** Lưu cả giá trị gốc vào biến để in lại trong f-string; dùng `{:.1f}`.

### Bài 14: Giới thiệu bản thân bằng f-string

* **Đề bài:** Nhập tên, tuổi, lớp học. In một câu giới thiệu duy nhất: `Tôi tên là <tên>, <tuổi> tuổi, học lớp <lớp>.`
* **Input:** Ba dòng: tên, tuổi, lớp.
* **Output:** Một dòng giới thiệu như trên.
* **Ví dụ:**
  ```
  Nhập tên: An
  Nhập tuổi: 15
  Nhập lớp: 10A1
  Tôi tên là An, 15 tuổi, học lớp 10A1.
  ```
* **Gợi ý:** Tuổi nên ép `int` (và in lại số 15, không có dấu nháy); dùng một câu f-string.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Đổi giây ra giờ:phút:giây

* **Đề bài:** Nhập một số giây (số nguyên), đổi ra giờ, phút, giây. Biết `1 giờ = 3600 giây`, `1 phút = 60 giây`.
* **Input:** Một dòng số nguyên.
* **Output:** `<giờ> giờ <phút> phút <giây> giây`
* **Ví dụ:**
  ```
  Nhập số giây: 3725
  1 giờ 2 phút 5 giây
  ```
* **Gợi ý:** `gio = s // 3600`; `phut = (s % 3600) // 60`; `giay = s % 60` — kết hợp `//` và `%` từ bài 6.

### Bài 16: Hóa đơn quán cà phê

* **Đề bài:** Nhập giá một ly cà phê và số ly. Nếu tổng từ 100.000đ trở lên thì giảm 10%. In tiền phải trả 2 chữ số thập phân. *(Chưa học `if` — hãy tận dụng kỹ thuật `int(điều kiện)` ở bài 6.)*
* **Input:** Hai dòng: giá ly (số thực), số ly (số nguyên).
* **Output:** `Tổng tiền: <tổng>` và `Tiền phải trả: <kết quả>` (2 chữ số thập phân).
* **Ví dụ:**
  ```
  Nhập giá một ly: 35000
  Nhập số ly: 3
  Tổng tiền: 105000.00
  Tiền phải trả: 94500.00
  ```
* **Gợi ý:** `tong = gia * so_ly`; `khuyen_mai = tong >= 100000`; `tien = tong - tong * 0.1 * int(khuyen_mai)`.

### Bài 17: Tiền lãi tiết kiệm một năm

* **Đề bài:** Nhập số tiền gửi (số thực). Với lãi suất `6.5%/năm`, tính số tiền lãi sau 1 năm và tổng tiền (gốc + lãi). In cả hai, 2 chữ số thập phân.
* **Input:** Một dòng số tiền gửi.
* **Output:** Hai dòng `Tiền lãi: <kết quả>` và `Tổng tiền nhận được: <kết quả>`
* **Ví dụ:**
  ```
  Nhập số tiền gửi: 10000000
  Tiền lãi: 650000.00
  Tổng tiền nhận được: 10650000.00
  ```
* **Gợi ý:** `lai = tien * 0.065`; tổng = gốc + lãi; nhớ `{:.2f}`.

### Bài 18: Điểm trung bình có trọng số

* **Đề bài:** Nhập điểm Toán, Văn, Anh (thang 10, số thực). Điểm trung bình = `(Toán * 2 + Văn * 1 + Anh * 1) / 4`. In kết quả 2 chữ số thập phân.
* **Input:** Ba dòng điểm từng môn.
* **Output:** `Điểm trung bình: <kết quả>`
* **Ví dụ:**
  ```
  Nhập điểm Toán: 8
  Nhập điểm Văn: 7
  Nhập điểm Anh: 9
  Điểm trung bình: 8.00
  ```
* **Gợi ý:** Điểm có thể là 8.5 nên dùng `float`; ngoặc quanh tổng trước khi chia.

### Bài 19: Chia tiền sau bữa ăn

* **Đề bài:** Nhập tổng hóa đơn (số thực) và số người cùng chia. Mỗi người trả phần bằng nhau (làm tròn 2 chữ số thập phân), in kết quả.
* **Input:** Hai dòng: tổng hóa đơn, số người (số nguyên).
* **Output:** `Mỗi người phải trả: <kết quả> VND`
* **Ví dụ:**
  ```
  Nhập tổng hóa đơn: 850000
  Nhập số người: 4
  Mỗi người phải trả: 212500.00 VND
  ```
* **Gợi ý:** `moi_nguoi = tong / so_nguoi`; số người dùng `int`, hóa đơn dùng `float`.

### Bài 20: Hồ sơ học sinh hoàn chỉnh

* **Đề bài:** Nhập: họ tên, tuổi, trường, môn học yêu thích. In ra một **hồ sơ 3 dòng** dùng f-string, ngăn cách các thông tin trong mỗi dòng bằng dấu ` | ` (dùng `sep`).
  * Dòng 1: Hồ sơ cá nhân
  * Dòng 2: Tên, tuổi, trường
  * Dòng 3: Môn yêu thích
* **Input:** Bốn dòng dữ liệu (họ tên, tuổi, trường, môn học).
* **Output:** Ba dòng như mô tả.
* **Ví dụ:**
  ```
  Nhập họ tên: Nguyễn Văn An
  Nhập tuổi: 16
  Nhập trường: THPT Python
  Nhập môn yêu thích: Tin học
  ===== HỒ SƠ CÁ NHÂN =====
  Nguyễn Văn An | 16 tuổi | THPT Python
  Môn yêu thích: Tin học
  ```
* **Gợi ý:** Kết hợp f-string (dòng 2) và `print(..., sep=" | ")`; nhớ tuổi ép `int` rồi chèn vào f-string.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Dùng `input()` nhận dữ liệu và luôn nhớ nó trả về chuỗi.
* ✅ Ép kiểu `int`/`float` đúng lúc, đúng chỗ để tính toán chuẩn xác.
* ✅ Làm chủ `print()` với `sep` và `end` để trang trí dòng in.
* ✅ Viết f-string với `{:.2f}` để in tiền, điểm, kết quả đẹp như phần mềm thật.

> 💪 Từ giờ chương trình của bạn đã biết "nghe" người dùng! Hãy chắc chắn mọi bài đều chạy thử với **nhiều giá trị nhập khác nhau**.

---

## ✅ Đáp án

> 💡 **Hãy tự làm bài tập trước** rồi mới mở đáp án.

## 🟢 Dễ (Bài 1 – 7)


<details>
<summary>✅ Bài 1: Máy chào hỏi</summary>


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

</details>

<details>
<summary>✅ Bài 2: Hỏi và in lại câu trả lời</summary>


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

</details>

<details>
<summary>✅ Bài 3: Cộng hai số</summary>


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

</details>

<details>
<summary>✅ Bài 4: In liền một dòng với `end`</summary>


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

</details>

<details>
<summary>✅ Bài 5: Ngăn cách bằng `sep`</summary>


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

</details>

<details>
<summary>✅ Bài 6: Diện tích hình chữ nhật</summary>


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

</details>

<details>
<summary>✅ Bài 7: Trung bình cộng ba số</summary>


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

</details>

## 🟡 Trung bình (Bài 8 – 14)


<details>
<summary>✅ Bài 8: Tính tuổi</summary>


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

</details>

<details>
<summary>✅ Bài 9: Chu vi và diện tích hình tròn</summary>


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

</details>

<details>
<summary>✅ Bài 10: Đổi tiền VND sang USD</summary>


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

</details>

<details>
<summary>✅ Bài 11: Vận tốc trung bình</summary>


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

</details>

<details>
<summary>✅ Bài 12: Chương trình tính BMI</summary>


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

</details>

<details>
<summary>✅ Bài 13: Đổi độ C sang độ F</summary>


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

</details>

<details>
<summary>✅ Bài 14: Giới thiệu bản thân bằng f-string</summary>


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

</details>

## 🔴 Khó (Bài 15 – 20)


<details>
<summary>✅ Bài 15: Đổi giây ra giờ:phút:giây</summary>


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

</details>

<details>
<summary>✅ Bài 16: Hóa đơn quán cà phê</summary>


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

</details>

<details>
<summary>✅ Bài 17: Tiền lãi tiết kiệm một năm</summary>


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

</details>

<details>
<summary>✅ Bài 18: Điểm trung bình có trọng số</summary>


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

</details>

<details>
<summary>✅ Bài 19: Chia tiền sau bữa ăn</summary>


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

</details>

<details>
<summary>✅ Bài 20: Hồ sơ học sinh hoàn chỉnh</summary>


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

</details>

## 📌 Lời khuyên cuối


* 📥 **Nhớ luôn:** `input()` trả về chuỗi — cứ nhập số là phải ép kiểu.
* 🔄 **Đọc lỗi theo chiều kim đồng hồ:** `int(input(...))` — `input` chạy trước, ép kiểu chạy sau.
* 🎨 **f-string là "chân ái"** của việc in ấn: vừa gọn, vừa định dạng được số `:.2f`.
* 🧪 **Chạy thử nhiều lần** với giá trị khác nhau (số âm, số thập phân, chữ cái) để hiểu chương trình phản ứng thế nào.
* Bài sau bạn sẽ học `if` — lúc đó chương trình biết **tự đưa ra quyết định** dựa trên dữ liệu vừa nhập!

👉 Tiếp theo: **[Bài 7: Câu Lệnh If – Cấu Trúc Rẽ Nhánh](../07-Cau-Lenh-If/bai.md)**

---

## ➡️ Điều hướng

**Vị trí:** `02-Thuat-Toan/06-Input-Output/bai.md`

**Bài tiếp theo:** [Bài 7 — Câu Lệnh If – Cấu Trúc Rẽ Nhánh](../07-Cau-Lenh-If/bai.md)