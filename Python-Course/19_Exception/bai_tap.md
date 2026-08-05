# 📝 Bài 19: Bài Tập – Ngoại Lệ (Exception)

> 🎯 **Chủ đề:** Error vs Exception, try/except, except cụ thể, else, finally, raise, ngoại lệ tùy chỉnh.

---

## 📌 Hướng dẫn làm bài

* Mỗi bài tập cần **tự viết code** rồi chạy thử trước khi xem đáp án.
* Đáp án chi tiết 20 bài: 👉 [xem file dap_an.md](dap_an.md)

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Bắt lỗi chia cho 0

* **Đề bài:** Đặt phép tính `10 / 0` trong `try`, bắt lỗi `ZeroDivisionError` và in ra `Khong the chia cho 0!`. Sau đó in thêm `Chuong trinh van chay tiep`.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Khong the chia cho 0!
  Chuong trinh van chay tiep
  ```
* **Gợi ý:** `except ZeroDivisionError:` ngay sau khối `try`.

### Bài 2: Bắt lỗi nhập sai kiểu

* **Đề bài:** Dùng `int("abc")` trong `try`, bắt `ValueError` và in `Khong phai so nguyen!`.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Khong phai so nguyen!
  ```
* **Gợi ý:** `int("abc")` luôn ném `ValueError`.

### Bài 3: Bắt lỗi chỉ số ngoài phạm vi

* **Đề bài:** Truy cập `ds[5]` với `ds = [10, 20, 30]` trong `try`, bắt `IndexError` và in `Chi so nam ngoai danh sach!`.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Chi so nam ngoai danh sach!
  ```
* **Gợi ý:** `except IndexError:`.

### Bài 4: Bắt lỗi khóa không tồn tại

* **Đề bài:** Truy cập `diem["Ly"]` với `diem = {"Toan": 8}` trong `try`, bắt `KeyError` và in `Mon nay chua co diem!`.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Mon nay chua co diem!
  ```
* **Gợi ý:** `except KeyError:` — ôn lại bài 17.

### Bài 5: finally luôn chạy

* **Đề bài:** Viết chương trình: `try` thực hiện `10 / 0` (sẽ lỗi), `except` in `Da bat duoc loi!`, `finally` in `Dang don dep tai nguyen...`. In thêm dòng `Ket thuc chuong trinh`.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Da bat duoc loi!
  Dang don dep tai nguyen...
  Ket thuc chuong trinh
  ```
* **Gợi ý:** Khối `finally` chạy dù có lỗi hay không.

### Bài 6: else chạy khi không lỗi

* **Đề bài:** `try` thực hiện `x = 10 / 2` (không lỗi); `except` in `Co loi!`; `else` in `Khong co loi gi!`. Quan sát kết quả.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Khong co loi gi!
  ```
* **Gợi ý:** `else` chỉ chạy khi khối `try` hoàn thành không lỗi.

### Bài 7: Sử dụng biến lỗi

* **Đề bài:** `try` gọi `int("abc")`, `except ValueError as e:` in nội dung lỗi ra màn hình.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Loi: invalid literal for int() with base 10: 'abc'
  ```
* **Gợi ý:** `as e` gán ngoại lệ vào biến; in bằng `print("Loi:", e)`.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Nhập số nguyên cho tới khi đúng

* **Đề bài:** Dùng vòng lặp `while` nhập một số nguyên; nếu nhập sai thì báo `Sai roi, nhap lai!` và cho nhập lại tới khi đúng thì in `So da nhap: <so>`.
* **Input:**
  ```
  Nhap so nguyen: abc
  Sai roi, nhap lai!
  Nhap so nguyen: 15
  ```
* **Output:**
  ```
  So da nhap: 15
  ```
* **Gợi ý:** `while True` + `try/except ValueError` + `break` khi thành công.

### Bài 9: Bắt nhiều loại lỗi cùng lúc

* **Đề bài:** Viết chương trình tính `100 / so` với `so` nhập từ bàn phím. Bắt cả `ValueError` (nhập sai) và `ZeroDivisionError` (chia 0) — mỗi lỗi in thông báo riêng. Không lỗi thì in kết quả.
* **Input:**
  ```
  Nhap so: 0
  ```
* **Output:**
  ```
  Khong duoc chia cho 0!
  ```
* **Gợi ý:** Hai khối `except` riêng biệt, viết liên tiếp.

### Bài 10: Chương trình chia an toàn

* **Đề bài:** Nhập hai số `a`, `b`, in thương `a / b`. Nếu lỗi thì báo lại và cho **nhập lại từ đầu** cho tới khi thành công. Dùng cả `else` để in `Tinh xong!`.
* **Input:**
  ```
  Nhap a: 10
  Nhap b: 0
  Nhap a: 10
  Nhap b: 4
  ```
* **Output:**
  ```
  Khong chia duoc cho 0!
  Thuong: 2.5
  Tinh xong!
  ```
* **Gợi ý:** Vòng lặp bảo vệ: `try` + `except` + `else` với `break` trong `else`.

### Bài 11: Nhập tuổi hợp lệ bằng raise

* **Đề bài:** Viết hàm `kiem_tra_tuoi(tuoi)`: nếu tuổi < 0 hoặc > 150 thì `raise ValueError`. Gọi thử với `-5` trong `try/except` và in thông báo lỗi.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Loi: Tuoi phai tu 0 den 150!
  ```
* **Gợi ý:** `raise ValueError("Tuoi phai tu 0 den 150!")`.

### Bài 12: Đọc file không tồn tại

* **Đề bài:** Dùng `open("khong_co.txt", "r")` trong `try`, bắt `FileNotFoundError` và in `Khong tim thay file!`. `finally` in `Da ket thuc xu ly file`.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Khong tim thay file!
  Da ket thuc xu ly file
  ```
* **Gợi ý:** `except FileNotFoundError` + `finally` luôn chạy.

### Bài 13: Tránh lỗi ngoài try

* **Đề bài:** Đoạn code sau bị lỗi ở dòng ngoài `try`. Hãy sửa để chương trình bắt được cả lỗi nhập sai lẫn lỗi chia 0:

  ```python
  a = int(input("Nhap so: "))
  try:
      print(10 / a)
  except ZeroDivisionError:
      print("Khong chia 0!")
  ```
* **Input:**
  ```
  Nhap so: abc
  ```
* **Output mong đợi:**
  ```
  Phai nhap so nguyen!
  ```
* **Gợi ý:** Đưa `int(input(...))` vào trong `try` và thêm `except ValueError`.

### Bài 14: Bộ đủ try – except – else – finally

* **Đề bài:** Nhập một số nguyên `n`, in `Binh phuong: n*n`. Dùng đủ 4 khối: `except ValueError` in `Nhap sai!`; `else` in bình phương; `finally` in `Ket thuc chuong trinh`.
* **Input:**
  ```
  Nhap n: 6
  ```
* **Output:**
  ```
  Binh phuong: 36
  Ket thuc chuong trinh
  ```
* **Gợi ý:** Theo đúng thứ tự `try` → `except` → `else` → `finally`.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Nhập điểm hợp lệ (0–10)

* **Đề bài:** Nhập điểm từ bàn phím, chấp nhận cả số thập phân. Yêu cầu: phải là số (bắt `ValueError`), phải nằm trong khoảng 0–10 (dùng `raise ValueError`). Lặp tới khi hợp lệ, in `Diem hop le: <diem>`.
* **Input:**
  ```
  Nhap diem (0-10): abc
  Sai roi, nhap lai!
  Nhap diem (0-10): 12
  Sai roi, nhap lai!
  Nhap diem (0-10): 8.5
  ```
* **Output:**
  ```
  Diem hop le: 8.5
  ```
* **Gợi ý:** `float(input(...))` + kiểm tra khoảng + `raise` + `while True`/`break`.

### Bài 16: Máy tính 4 phép tính không bao giờ "sập"

* **Đề bài:** Viết máy tính cộng, trừ, nhân, chia với vòng lặp. Nhập phép tính dạng `a op b` (cách nhau khoảng trắng), ví dụ `10 / 3`. Bắt mọi lỗi nhập (sai định dạng, chia 0) và cho nhập lại. Gõ `thoat` để kết thúc.
* **Input:**
  ```
  Nhap phep tinh: 10 / 0
  Nhap phep tinh: abc
  Nhap phep tinh: 10 / 3
  Nhap phep tinh: thoat
  ```
* **Output:**
  ```
  Loi: khong chia duoc cho 0!
  Loi: phep tinh khong hop le!
  Ket qua: 3.3333333333333335
  Tam biet!
  ```
* **Gợi ý:** `split()` lấy 3 phần tử; `try/except` bao quanh toàn bộ phép tính; dùng `if` để chọn phép toán.

### Bài 17: Ngoại lệ tùy chỉnh — tuổi

* **Đề bài:** Định nghĩa `class TuoiKhongHopLe(Exception)`. Viết hàm `kiem_tra_tuoi` ném lỗi này khi tuổi < 0 (thông điệp `Tuoi khong the la so am!`) hoặc > 150 (`Tuoi qua lon!`). Gọi thử với `-5` và `200` trong `try/except` rồi in kết quả.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Loi: Tuoi khong the la so am!
  Loi: Tuoi qua lon!
  ```
* **Gợi ý:** `class TuoiKhongHopLe(Exception): pass` rồi `raise TuoiKhongHopLe("...")`.

### Bài 18: Ngoại lệ tùy chỉnh — tiền rút ATM

* **Đề bài:** Định nghĩa `class SoDuKhongDu(Exception)`. Hàm `rut_tien(so_du, so_tien)` ném lỗi khi `so_tien > so_du`, ngược lại trả về số dư mới. Gọi với `so_du = 50000, so_tien = 100000`; bắt lỗi và in `Loi: So du khong du!`.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Loi: So du khong du!
  ```
* **Gợi ý:** Dùng `as e` để in thông điệp đã ném.

### Bài 19: Điểm danh bằng get() và KeyError

* **Đề bài:** Cho `diem = {"An": 8, "Binh": 7}`. Viết hàm `lay_diem(ten)` dùng `diem[ten]`. Trong `main`, hỏi nhập tên học sinh (cho tới khi gõ `thoat`), in điểm; bắt `KeyError` in `Hoc sinh nay khong co diem!` rồi tiếp tục nhập tên khác.
* **Input:**
  ```
  Nhap ten hoc sinh: An
  Nhap ten hoc sinh: Chi
  Nhap ten hoc sinh: thoat
  ```
* **Output:**
  ```
  Diem cua An: 8
  Hoc sinh nay khong co diem!
  ```
* **Gợi ý:** Vòng lặp `while`, `try/except KeyError` bên trong.

### Bài 20: Quản lý điểm học sinh hoàn chỉnh

* **Đề bài:** Viết chương trình nhập điểm của 3 môn Toán, Văn, Anh (mỗi môn dùng vòng lặp bảo vệ: phải là số, phải trong 0–10, nếu không thì báo lỗi và nhập lại). Sau đó tính và in trung bình (2 chữ số) và xếp loại: ≥ 8.0 → `Gioi`, ≥ 6.5 → `Kha`, ≥ 5.0 → `Trung binh`, còn lại → `Yeu`. Nếu tổng cộng có lỗi bất ngờ, bắt `Exception` in `Co loi khong mong doi!`.
* **Input:**
  ```
  Nhap diem Toan: abc
  Nhap diem Toan: 8.5
  Nhap diem Van: 7
  Nhap diem Anh: 9
  ```
* **Output:**
  ```
  Diem khong hop le, nhap lai!
  Trung binh: 8.17
  Xep loai: Gioi
  ```
* **Gợi ý:** Tạo hàm `nhap_diem(mon)` dùng vòng lặp bảo vệ; `try/except Exception` bao quanh phần tính toán.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Phân biệt error và exception; dùng `try/except` bắt lỗi không cho chương trình "sập".
* ✅ Dùng `else`, `finally`, `raise` và bắt các ngoại lệ cụ thể.
* ✅ Tự định nghĩa ngoại lệ riêng bằng `class ... (Exception)`.
* ✅ Xây dựng máy tính và chương trình nhập điểm an toàn — mẫu của mọi ứng dụng thực tế.

> 💪 Chưa tự làm được bài nào thì đừng lo — xem lại bài giảng rồi quay lại. **Lập trình là luyện tập!**

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 20: Module](../20_Module/bai_giang.md)**
