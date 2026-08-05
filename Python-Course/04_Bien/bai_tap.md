# 📝 Bài 4: Bài Tập – Biến Trong Python

> 🎯 **Chủ đề:** Khai báo biến, gán và gán lại giá trị, quy tắc đặt tên, gán nhiều biến, hoán đổi giá trị.

---

## 📌 Hướng dẫn làm bài

* Mỗi bài tập cần **tự viết code** rồi chạy thử trước khi xem đáp án.
* Vì bài 4 chưa học `input()`, các bài tập dùng **giá trị gán trực tiếp** — dữ liệu "chỉ định sẵn".
* Đáp án chi tiết 20 bài: 👉 [xem file dap_an.md](dap_an.md)

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Chiếc hộp đầu tiên

* **Đề bài:** Tạo biến `lop` chứa chuỗi `"10A1"` và in giá trị của nó ra màn hình.
* **Input:** Không có.
* **Output:**
  ```
  10A1
  ```
* **Gợi ý:** Gán `lop = "10A1"` rồi `print(lop)`.

### Bài 2: Điểm môn học

* **Đề bài:** Tạo biến `diem` có giá trị `8.5`, rồi in ra câu `Diem cua toi la: 8.5`.
* **Input:** Không có.
* **Output:**
  ```
  Diem cua toi la: 8.5
  ```
* **Gợi ý:** `print("Diem cua toi la:", diem)`.

### Bài 3: Đổi nội dung hộp

* **Đề bài:** Biến `so` đầu tiên được gán `5`, sau đó gán lại `10`. In ra giá trị cuối cùng của `so`.
* **Input:** Không có.
* **Output:**
  ```
  10
  ```
* **Gợi ý:** Lệnh gán sau sẽ ghi đè lệnh gán trước.

### Bài 4: Đặt tên đúng hay sai

* **Đề bài:** Chương trình sau bị lỗi. Hãy sửa để chạy được:

  ```python
  1ten = "An"
  print(1ten)
  ```
* **Output mong đợi:**
  ```
  An
  ```
* **Gợi ý:** Tên biến không được bắt đầu bằng chữ số.

### Bài 5: Ba biến, ba món quà

* **Đề bài:** Dùng một dòng lệnh gán 3 biến `a`, `b`, `c` lần lượt cho `1`, `2`, `3`, rồi in cả ba giá trị.
* **Input:** Không có.
* **Output:**
  ```
  1 2 3
  ```
* **Gợi ý:** `a, b, c = 1, 2, 3`.

### Bài 6: Tổng hai số

* **Đề bài:** Tạo hai biến `x = 12` và `y = 30`, tính tổng lưu vào biến `tong`, in ra câu `Tong la: 42`.
* **Input:** Không có.
* **Output:**
  ```
  Tong la: 42
  ```
* **Gợi ý:** `tong = x + y` rồi in.

### Bài 7: Tên biến viết thường

* **Đề bài:** Tạo biến `TenTruong` chứa `"THPT Python"`. Viết lại bằng chuẩn snake_case rồi in giá trị.
* **Input:** Không có.
* **Output:**
  ```
  THPT Python
  ```
* **Gợi ý:** Tên đẹp là `ten_truong`, tất cả chữ thường, dùng dấu `_`.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Hoán đổi bằng biến tạm

* **Đề bài:** Cho `a = 3` và `b = 7`. Dùng **một biến tạm** để đổi giá trị hai biến cho nhau, in kết quả.
* **Input:** Không có.
* **Output:**
  ```
  7 3
  ```
* **Gợi ý:** Mượn "cốc thứ ba" để rót: `tam = a`, `a = b`, `b = tam`.

### Bài 9: Hoán đổi kiểu Python

* **Đề bài:** Cho `x = "banh mi"` và `y = "pho"`. Đổi giá trị hai biến **không dùng biến tạm**, in kết quả.
* **Input:** Không có.
* **Output:**
  ```
  pho banh mi
  ```
* **Gợi ý:** `x, y = y, x` — một dòng duy nhất.

### Bài 10: Ví tiền trong một ngày

* **Đề bài:** Sáng có `tien = 200000`. Buổi trưa mua cơm hết `45000`, chiều mua sách hết `80000`, tối mẹ cho thêm `100000`. Dùng biến `tien` cập nhật liên tiếp, in số tiền cuối ngày.
* **Input:** Không có.
* **Output:**
  ```
  So tien con lai: 175000
  ```
* **Gợi ý:** `tien = tien - 45000`, rồi `tien = tien - 80000`, rồi `tien = tien + 100000`.

### Bài 11: Điểm trung bình hai môn

* **Đề bài:** Biến `diem_toan = 9`, `diem_van = 7`. Tính trung bình cộng hai môn lưu vào biến `trung_binh`, in ra câu `Trung binh: 8.0`.
* **Input:** Không có.
* **Output:**
  ```
  Trung binh: 8.0
  ```
* **Gợi ý:** `trung_binh = (diem_toan + diem_van) / 2`.

### Bài 12: Chỉnh sửa chỗ sai

* **Đề bài:** Tìm và sửa lỗi trong chương trình:

  ```python
  so qua = 5
  print(so_qua)
  ```
* **Output mong đợi:**
  ```
  5
  ```
* **Gợi ý:** Tên biến không được chứa dấu cách; còn có một lỗi in không khớp tên.

### Bài 13: Tìm ra con số lớn hơn

* **Đề bài:** Cho hai biến `m = 15`, `n = 9`. Dùng hàm `max(m, n)` gán cho biến `lon_nhat`, in câu `So lon hon: 15`.
* **Input:** Không có.
* **Output:**
  ```
  So lon hon: 15
  ```
* **Gợi ý:** `lon_nhat = max(m, n)` — `max` là hàm lấy giá trị lớn nhất.

### Bài 14: Đổi đơn vị giờ – phút

* **Đề bài:** Biến `phut = 135`. Tính xem 135 phút bằng bao nhiêu giờ và bao nhiêu phút còn thừa, lưu vào `gio` và `phut_con`, in kết quả.
* **Input:** Không có.
* **Output:**
  ```
  135 phut = 2 gio 15 phut
  ```
* **Gợi ý:** `gio = phut // 60`, `phut_con = phut % 60` — phép chia lấy nguyên và lấy dư (học kỹ ở Bài 6).

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Hoán đổi không cần biến tạm (phiên bản tay đôi)

* **Đề bài:** Cho `a = 4`, `b = 9`. Đổi giá trị cho nhau **chỉ dùng phép toán cộng/trừ, không dùng biến tạm, không dùng `a, b = b, a`**, in kết quả.
* **Input:** Không có.
* **Output:**
  ```
  a = 9, b = 4
  ```
* **Gợi ý:** Thử `a = a + b` (a trở thành 13), rồi `b = a - b`, rồi `a = a - b`. Giải thích vì sao cách này không nên dùng cho chuỗi.

### Bài 16: Kiểm tra `id()` của biến

* **Đề bài:** Tạo `x = 1000` và `y = x`. In `id(x)` và `id(y)`, so sánh xem chúng có bằng nhau không. Sau đó gán `y = 2000` và in lại `id(y)` kèm câu kết luận ngắn.
* **Input:** Không có.
* **Output:**
  ```
  id(x) = ... 
  id(y) = ...
  id(x) == id(y): True
  Sau khi y doi gia tri...
  ```
* **Gợi ý:** `id(x) == id(y)` so sánh hai địa chỉ. Khi `y` nhận giá trị mới, nó chuyển sang vùng nhớ khác.

### Bài 17: Hóa đơn mua kẹo

* **Đề bài:** Cửa hàng bán `so_goi_keo = 4` gói, mỗi gói `gia_goi = 12000`. Mua thêm 1 gói sau đó. Tính tổng tiền lưu vào biến `tong_tien` và in ra câu `Tong tien: 60000`.
* **Input:** Không có.
* **Output:**
  ```
  Tong tien: 60000
  ```
* **Gợi ý:** Cập nhật `so_goi_keo = so_goi_keo + 1` trước khi tính, hoặc tính `tong_tien = (so_goi_keo + 1) * gia_goi`.

### Bài 18: Thời khóa biểu dùng biến

* **Đề bài:** Tạo 3 biến `mon1`, `mon2`, `mon3` lần lượt chứa `"Toan"`, `"Van"`, `"Tin"`. Hoán đổi để `mon1` thành `"Tin"`, `mon3` thành `"Toan"` (chỉ đổi `mon1` và `mon3`), in cả ba.
* **Input:** Không có.
* **Output:**
  ```
  Tin Van Toan
  ```
* **Gợi ý:** Đổi hai biến bằng `mon1, mon3 = mon3, mon1`.

### Bài 19: Chương trình nhập điểm kiểu "sắp hàng"

* **Đề bài:** Biến `diem1 = 5`, `diem2 = 8`. Vì điểm 2 cao hơn, bạn muốn xếp `cao` chứa điểm lớn hơn và `thap` chứa điểm nhỏ hơn. Không dùng hàm `max/min`, hãy dùng biến tạm và phép so sánh `if` để gán đúng (có thể dùng `if` đơn giản).
* **Input:** Không có.
* **Output:**
  ```
  Cao: 8 - Thap: 5
  ```
* **Gợi ý:** Gán `cao = diem1`, `thap = diem2`; nếu `diem1 < diem2` thì đổi ngược lại bằng biến tạm.

### Bài 20: Mô phỏng "hộp số kẹo chia đôi"

* **Đề bài:** Bạn có `so_keo = 25` viên kẹo. Mỗi ngày bạn ăn hết 3 viên và nhận thêm 2 viên từ bạn bè. Mô phỏng 3 ngày bằng biến `so_keo` (cập nhật liên tiếp), mỗi ngày in số kẹo còn lại. Ngày nào số kẹo còn lại là số chẵn thì gán `so_le = False`, ngược lại `so_le = True` (chỉ cần gán ở ngày cuối).
* **Input:** Không có.
* **Output:**
  ```
  Ngay 1: 24
  Ngay 2: 23
  Ngay 3: 22
  So keo con lai la so chan: True
  ```
* **Gợi ý:** Mỗi ngày `so_keo = so_keo - 3 + 2`; số chẵn kiểm tra bằng `so_keo % 2 == 0` (học kỹ ở Bài 6).

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Khai báo, gán và gán lại biến thành thạo.
* ✅ Nắm vững quy tắc đặt tên biến và chuẩn `snake_case`.
* ✅ Gán nhiều biến cùng lúc, hoán đổi giá trị bằng nhiều cách.
* ✅ Biết kiểm tra vùng nhớ bằng `id()` và sao chép giá trị giữa các biến.

> 💪 Khi gặp `NameError`, hãy kiểm tra: biến đã được gán trước khi dùng chưa? Tên viết đúng hoa – thường chưa? **Lập trình là luyện tập!**

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 5: Kiểu Dữ Liệu Cơ Bản](../05_Kieu_du_lieu/bai_giang.md)**
