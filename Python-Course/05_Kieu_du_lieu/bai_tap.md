# 📝 Bài 5: Bài Tập – Kiểu Dữ Liệu Cơ Bản

> 🎯 **Chủ đề:** Nhận biết `int`, `float`, `str`, `bool`; dùng `type()`; ép kiểu và phân biệt số với chuỗi.

---

## 📌 Hướng dẫn làm bài

* Mỗi bài tập cần **tự viết code** rồi chạy thử trước khi xem đáp án.
* Vì bài 5 chưa học `input()`, các bài tập dùng **giá trị gán trực tiếp**.
* Đáp án chi tiết 20 bài: 👉 [xem file dap_an.md](dap_an.md)

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Nhận diện kiểu dữ liệu

* **Đề bài:** Viết chương trình in ra kiểu dữ liệu của các giá trị: `7`, `7.0`, `"7"`, `True`.
* **Input:** Không có.
* **Output:**
  ```
  <class 'int'>
  <class 'float'>
  <class 'str'>
  <class 'bool'>
  ```
* **Gợi ý:** Dùng `print(type(gia_tri))` cho từng giá trị.

### Bài 2: Khai báo đủ 4 loại

* **Đề bài:** Tạo 4 biến thuộc 4 kiểu `int`, `float`, `str`, `bool` (tự chọn giá trị), rồi in cả 4 ra màn hình.
* **Input:** Không có.
* **Output:**
  ```
  2026 8.5 Python True
  ```
* **Gợi ý:** `print(bien_int, bien_float, bien_str, bien_bool)`.

### Bài 3: Số hay chữ?

* **Đề bài:** In ra hai kết quả: `5 + 3` và `"5" + "3"`.
* **Input:** Không có.
* **Output:**
  ```
  8
  53
  ```
* **Gợi ý:** `print(5 + 3)`; `print("5" + "3")`.

### Bài 4: Đếm ký tự

* **Đề bài:** Đếm số ký tự của chuỗi `"Python"` bằng `len()` (kể từ bài trước đã dùng) và in ra kèm kiểu dữ liệu của kết quả.
* **Input:** Không có.
* **Output:**
  ```
  6
  <class 'int'>
  ```
* **Gợi ý:** `so_ky_tu = len("Python")`; in `so_ky_tu` và `type(so_ky_tu)`.

### Bài 5: Nối chuỗi và số

* **Đề bài:** Biến `ten = "Mai"`. In câu `Chao ban Mai` bằng cách nối chuỗi với biến `ten`.
* **Input:** Không có.
* **Output:**
  ```
  Chao ban Mai
  ```
* **Gợi ý:** `print("Chao ban " + ten)` — Chuỗi có sẵn dấu cách cuối.

### Bài 6: Ép chuỗi thành số

* **Đề bài:** Biến `so = "10"`. Dùng `int()` ép thành số rồi tính `so + 5`, in kết quả.
* **Input:** Không có.
* **Output:**
  ```
  15
  ```
* **Gợi ý:** `print(int(so) + 5)`.

### Bài 7: Ép số thành chuỗi

* **Đề bài:** Biến `nam = 2026`. Nối `nam` vào câu `Nam 2026 la nam moi` bằng `str()`.
* **Input:** Không có.
* **Output:**
  ```
  Nam 2026 la nam moi
  ```
* **Gợi ý:** `print("Nam " + str(nam) + ". Nam moi")`.

---

## 🟨 Trung bình (Bài 8 – 14)

### Bài 8: Toàn cảnh kiểu dữ liệu

* **Đề bài:** Với mỗi giá trị sau, in ra kiểu bằng `type()`: `10 > 3`, `float(7)`, `int("9")`, `str(3.14)`.
* **Input:** Không có.
* **Output:**
  ```
  <class 'bool'>
  <class 'float'>
  <class 'int'>
  <class 'str'>
  ```
* **Gợi ý:** Gõ trực tiếp giá trị trong `type()`; chú ý `10 > 3` là phép so sánh trả về `bool`.

### Bài 9: Bmis sai của học sinh

* **Đề bài:** Hai bạn `diem_so = "8.5"` (dạng chuỗi) và muốn cộng thêm `0.5` (điểm thưởng). Ép kiểu đúng rồi in: `Diem moi: 9.0`.
* **Input:** Không có.
* **Output:**
  ```
  Diem moi: 9.0
  ```
* **Gợi ý:** `float(diem_so) + 0.5` — chuỗi thập phân nên ép `float` chứ không phải `int`.

### Bài 10: Cắt phần thập phân

* **Đề bài:** Biến `gia = 19.99` (đơn vị nghìn đồng). In ra phần nguyên của giá bằng `int()`: `Gia nguyen: 19`.
* **Input:** Không có.
* **Output:**
  ```
  Gia nguyen: 19
  ```
* **Gợi ý:** `print("Gia nguyen:", int(gia))`.

### Bài 11: Kiểm tra hàm `bool`

* **Đề bài:** In ra kết quả `bool()` của các giá trị: `0`, `1`, `""`, `"Python"`, `0.0` kèm nhãn từng dòng.
* **Input:** Không có.
* **Output:**
  ```
  bool(0) = False
  bool(1) = True
  bool("") = False
  bool("Python") = True
  bool(0.0) = False
  ```
* **Gợi ý:** `print("bool(0) =", bool(0))` … viết đủ 5 dòng.

### Bài 12: Ghép chuỗi số tuổi

* **Đề bài:** Biến `tuoi = 15`. Viết chương trình in dòng `Toi 15 tuoi, hoc lop 10` — mỗi con số phải xuất phát từ biến (ép `str` để nối).
* **Input:** Không có.
* **Output:**
  ```
  Toi 15 tuoi, hoc lop 10
  ```
* **Gợi ý:** Tạo thêm biến `lop = 10`; dùng `str(tuoi)`, `str(lop)`.

### Bài 13: Hé lộ lỗi TypeError

* **Đề bài:** Chương trình sau bị lỗi. Đoán lỗi gì, sửa để in đúng:

  ```python
  diem = 8
  print("Diem cua toi: " + diem)
  ```
* **Output mong đợi:**
  ```
  Diem cua toi: 8
  ```
* **Gợi ý:** `diem` là `int`, chuỗi không thể `+` trực tiếp với `int` — phải `str(diem)`.

### Bài 14: Độ dài của số hay chữ?

* **Đề bài:** `len("2026")` là số mấy? `len(str(2026))` là số mấy? In cả hai kèm giải thích ngắn bằng dòng `print` thông báo.
* **Input:** Không có.
* **Output:**
  ```
  len("2026") = 4
  len(str(2026)) = 4
  ```
* **Gợi ý:** `len` đếm số ký tự trong chuỗi; `"2026"` có 4 ký tự, `str(2026)` cũng thành `"2026"`.

---

## 🟥 Khó (Bài 15 – 20)

### Bài 15: Chuyển đổi linh hoạt qua trung gian

* **Đề bài:** Biến `gia_tri = "7.8"` (chuỗi). File muốn giá trị nguyên (kiểu `int`) của nó. Ép qua 2 bước rồi in kết quả và kiểu.
* **Input:** Không có.
* **Output:**
  ```
  Gia tri: 7 - Kieu: <class 'int'>
  ```
* **Gợi ý:** `int(float("7.8"))` — qua `float` trung gian.

### Bài 16: Kiểm tra "True / False" của phép so sánh

* **Đề bài:** In ra kết quả và kiểu dữ liệu của biểu thức `(10 > 5) and (10 < 20)`. Nhớ `and` là toán tử logic (học ở bài 6) — lần này chỉ cần in kết quả và ghi chú.
* **Input:** Không có.
* **Output:**
  ```
  Ket qua: True
  Kieu: <class 'bool'>
  ```
* **Gợi ý:** `ket_qua = 10 > 5 and 10 < 20`; in `ket_qua` và `type(ket_qua)`. (Ghi chú: `and` sẽ học kỹ ở bài sau.)

### Bài 17: Máy tách phần nguyên – phần thập phân

* **Đề bài:** Biến `so_thuc = 12.68`. Dùng `int()` và phép trừ để tách thành `phan_nguyen = 12` và `phan_thap_phan = 0.68` (làm tròn 2 chữ số bằng `round`). In kết quả kèm kiểu.
* **Input:** Không có.
* **Output:**
  ```
  Phan nguyen: 12 (int)
  Phan thap phan: 0.68 (float)
  ```
* **Gợi ý:** `phan_nguyen = int(so_thuc)`; `phan_thap_phan = round(so_thuc - phan_nguyen, 2)`.

### Bài 18: Bảng tóm tắt — in và kiểu

* **Đề bài:** Từ `str(123)`, `int("45")`, `float("6.5")`, `bool("0")` — In từng kết quả và kiểu của nó dạng một bảng đẹp bằng `print` nhiều dòng.
* **Input:** Không có.
* **Output:**
  ```
  Gia tri: 123 - Kieu: <class 'str'>
  Gia tri: 45 - Kieu: <class 'int'>
  Gia tri: 6.5 - Kieu: <class 'float'>
  Gia tri: True - Kieu: <class 'bool'>
  ```
* **Gợi ý:** `bool("0")` — chuỗi "0" khác số `0`! Chuỗi không rỗng → `True`. In từng dòng với `str(...)` để nối được.

### Bài 19: Giá trị trung bình "trộn kiểu"

* **Đề bài:** Biến `diem1 = "7"`, `diem2 = "8.5"`, trung bình 2 môn. Ép kiểu phù hợp (một cái `int`, một cái `float`) rồi tính trung bình và in kết quả kèm kiểu dữ liệu đã ép.
* **Input:** Không có.
* **Output:**
  ```
  Trung binh: 7.75
  Kieu ket qua: <class 'float'>
  ```
* **Gợi ý:** `(int(diem1) + float(diem2)) / 2`.

### Bài 20: Chương trình "thay đồ" cho biến

* **Đề bài:** Biến `x` bắt đầu là `10`. Lần lượt: biến thành `"mot"`, thành `10.0`, thành `False`, thành `"10.0"`. Ở mỗi bước in giá trị và kiểu. Cuối cùng, thử ép `x` (đang là `"10.0"`) về `float` và in kết quả so sánh xem `float(x) == 10.0` hay không.
* **Input:** Không có.
* **Output:** giống dạng:
  ```
  10 <class 'int'>
  mot <class 'str'>
  10.0 <class 'float'>
  False <class 'bool'>
  10.0 <class 'str'>
  float(x) == 10.0: True
  ```
* **Gợi ý:** Gán và in `x` + `type(x)` sau mỗi dòng; phép so sánh `==` trả về `bool`.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Phân biệt rõ 4 kiểu dữ liệu và dùng `type()` thành thạo.
* ✅ Ép kiểu theo mọi hướng: số → chuỗi, chuỗi → số, boole.
* ✅ Hiểu vì sao `"5"` khác `5` và tránh lỗi `TypeError`, `ValueError`.

> 💪 Mẹo vàng: nghi ngờ kiểu gì thì cứ `print(type(...))` mà kiểm chứng. **Lập trình là luyện tập!**

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 6: Toán Tử](../06_Toan_tu/bai_giang.md)**