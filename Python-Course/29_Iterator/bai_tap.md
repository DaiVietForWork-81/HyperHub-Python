# 📝 Bài 29: Bài Tập – Iterator

> 🎯 **Chủ đề:** Iterable vs iterator, `iter()` / `next()`, `StopIteration`, tự tạo class Iterator (`__iter__` / `__next__`), iterator vô hạn, đọc file theo dòng.
> 📘 Hãy **tự viết code và chạy thử** trước khi xem đáp án.

---

## 📌 Hướng dẫn làm bài

* Mỗi bài tập hãy **tự gõ code** vào file `.py` rồi chạy bằng `python ten_file.py`.
* Đọc kỹ phần "Input/Output" — dữ liệu ví dụ chỉ để kiểm tra.
* Đáp án chi tiết 20 bài: 👉 [xem file dap_an.md](dap_an.md)

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Duyệt danh sách bằng `next()`

* **Đề bài:** Tạo danh sách `["hoc", "tap", "vui"]`. Dùng `iter()` và `next()` in ra từng phần tử, mỗi phần tử một dòng.
* **Input:** Không có
* **Output:**
  ```
  hoc
  tap
  vui
  ```
* **Gợi ý:** `it = iter(danh_sach)` rồi gọi `next(it)` ba lần.

### Bài 2: Duyệt chuỗi ký tự

* **Đề bài:** Dùng `iter()` và `next()` in ra từng ký tự của chuỗi `"Py"` — mỗi ký tự một dòng.
* **Input:** Không có
* **Output:**
  ```
  P
  y
  ```
* **Gợi ý:** Chuỗi cũng là iterable.

### Bài 3: Nhận diện iterator

* **Đề bài:** Viết chương trình kiểm tra và in ra: `danh_sach = [1, 2, 3]` có phải iterator không; `it = iter(danh_sach)` có phải iterator không.
* **Input:** Không có
* **Output:**
  ```
  danh_sach: False
  it: True
  ```
* **Gợi ý:** Dùng `hasattr(x, "__next__")` để kiểm tra.

### Bài 4: Bắt `StopIteration`

* **Đề bài:** Tạo iterator từ `[7]`, gọi `next()` hai lần trong `try/except`, in `"Het du lieu!"` khi bắt được `StopIteration`.
* **Input:** Không có
* **Output:**
  ```
  7
  Het du lieu!
  ```
* **Gợi ý:** `except StopIteration:` — đã học ở bài 19.

### Bài 5: `__iter__` trả về gì?

* **Đề bài:** Tạo class `So1` — iterator trả về lần lượt `1, 2, 3` rồi dừng. Trong `__iter__` trả về `self`. Chạy `for` in ra 3 số.
* **Input:** Không có
* **Output:**
  ```
  1
  2
  3
  ```
* **Gợi ý:** Dùng biến `self.gia_tri` tăng dần, `raise StopIteration` khi `> 3`.

### Bài 6: Iterator dùng một lần

* **Đề bài:** Tạo `it = iter([5, 6])`. Gọi `next(it)` một lần rồi dùng `list(it)` và in ra. Giải thích kết quả.
* **Input:** Không có
* **Output:**
  ```
  [6]
  ```
* **Gợi ý:** `list(it)` gom các giá trị CÒN LẠI trong iterator.

### Bài 7: Duyệt từ điển theo khóa

* **Đề bài:** Tạo dict `diem = {"An": 8, "Binh": 9}`. Dùng `iter()` trên dict và `next()` in ra khóa của từng phần tử.
* **Input:** Không có
* **Output:**
  ```
  An
  Binh
  ```
* **Gợi ý:** `iter(dict)` trả iterator duyệt qua các **khóa**.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Class `DemNguoc`

* **Đề bài:** Viết class `DemNguoc(n)` đếm ngược từ `n` về `1`. Tạo đối tượng `DemNguoc(4)` và dùng `for` in ra.
* **Input:** Không có
* **Output:**
  ```
  4
  3
  2
  1
  ```
* **Gợi ý:** Giảm dần `self.hien_tai`, `raise StopIteration` khi nhỏ hơn 1.

### Bài 9: Class `SoChan` — số chẵn vô hạn

* **Đề bài:** Viết class `SoChan` sinh số chẵn: `0, 2, 4, 6...`. Dùng `next()` in ra **4 số đầu tiên** (KHÔNG dùng vòng lặp không giới hạn).
* **Input:** Không có
* **Output:**
  ```
  0
  2
  4
  6
  ```
* **Gợi ý:** `self.so += 2` mỗi lần gọi; chỉ gọi `next()` đúng 4 lần.

### Bài 10: Class `SoLe` có giới hạn

* **Đề bài:** Viết class `SoLe(so_luong)` sinh ra `so_luong` số lẻ đầu tiên: `1, 3, 5, 7, 9`. Tạo `SoLe(5)` duyệt bằng `for`.
* **Input:** Không có
* **Output:**
  ```
  1
  3
  5
  7
  9
  ```
* **Gợi ý:** Đếm số lần đã sinh; khi đủ thì `raise StopIteration`.

### Bài 11: Tạo iterator bằng `iter(ham, sentinel)`

* **Đề bài:** Viết hàm `sinh_so()` trả về lần lượt `1, 2, 3, 99`. Dùng `iter(sinh_so, 99)` để duyệt và in ra các số **trước khi gặp 99**.
* **Input:** Không có
* **Output:**
  ```
  1
  2
  3
  ```
* **Gợi ý:** `iter(sinh_so, 99)` dừng khi kết quả bằng `99`; giá trị `99` không được in.

### Bài 12: Class `BinhPhuong` — bình phương liên tiếp

* **Đề bài:** Viết class `BinhPhuong(n)` trả về `1², 2², ..., n²`. Duyệt `BinhPhuong(4)` in ra.
* **Input:** Không có
* **Output:**
  ```
  1
  4
  9
  16
  ```
* **Gợi ý:** `self.index` chạy từ 1 đến n, trả về `index * index`.

### Bài 13: Đọc file từng dòng

* **Đề bài:** Tạo file `lop.txt` chứa 3 dòng `An, Binh, Chi`. Viết class `DocFile` — mỗi lần `next()` trả một dòng (bỏ ký tự xuống dòng). Duyệt và in ra.
* **Input:** Tạo file trước khi chạy chương trình.
* **Output:**
  ```
  An
  Binh
  Chi
  ```
* **Gợi ý:** Dùng `readline()`, kiểm tra `""` để dừng.

### Bài 14: Iterator cộng dồn

* **Đề bài:** Viết class `CongDon` nhận danh sách số; `next()` trả về **tổng cộng dồn** đến phần tử hiện tại. Ví dụ `[2, 3, 4]` → `2, 5, 9`.
* **Input:** Không có
* **Output:**
  ```
  2
  5
  9
  ```
* **Gợi ý:** Biến `self.tong` cộng dồn từng phần tử; duyệt hết thì `raise StopIteration`.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Dãy Fibonacci bằng iterator

* **Đề bài:** Viết class `Fibonacci` sinh dãy `0, 1, 1, 2, 3, 5, 8...` (vô hạn). Dùng `next()` in ra **7 số đầu tiên**.
* **Input:** Không có
* **Output:**
  ```
  0
  1
  1
  2
  3
  5
  8
  ```
* **Gợi ý:** Giữ hai biến `a, b`; mỗi lần trả `a` rồi cập nhật `a, b = b, a + b`.

### Bài 16: Iterator lọc số nguyên tố

* **Đề bài:** Viết class `SoNguyenTo(so_luong)` sinh ra `so_luong` số nguyên tố đầu tiên: `2, 3, 5, 7, 11...`. Tạo `SoNguyenTo(4)` duyệt in ra.
* **Input:** Không có
* **Output:**
  ```
  2
  3
  5
  7
  ```
* **Gợi ý:** Viết hàm phụ `la_nguyen_to(n)`; thử từng số từ 2 trở đi.

### Bài 17: Đọc file — bỏ dòng trống

* **Đề bài:** Tạo file `tho.txt` có cả dòng trống. Viết class `DocDongKhongTrong` — chỉ trả về các dòng KHÔNG rỗng (đã bỏ khoảng trắng thừa).
* **Input:** File mẫu:
  ```
  Mua thu

  la dep
  ```
* **Output:**
  ```
  Mua thu
  la dep
  ```
* **Gợi ý:** `dong.strip()` bỏ khoảng trắng; bỏ qua khi `dong.strip() == ""`.

### Bài 18: Iterator đảo ngược danh sách

* **Đề bài:** Viết class `DaoNguoc` nhận một danh sách, duyệt từ **cuối về đầu**. Kiểm tra với `[1, 2, 3]`.
* **Input:** Không có
* **Output:**
  ```
  3
  2
  1
  ```
* **Gợi ý:** Khởi tạo chỉ số `len(danh_sach) - 1` rồi giảm dần.

### Bài 19: Iterator ghép hai danh sách (zigzag)

* **Đề bài:** Viết class `ZicZac` nhận hai danh sách, trả về luân phiên: phần tử 1 của list A, phần tử 1 của list B, phần tử 2 của A... Ví dụ `[1, 2]` và `["a", "b"]` → `1, "a", 2, "b"`. Dừng khi cả hai hết.
* **Input:** Không có
* **Output:**
  ```
  1
  a
  2
  b
  ```
* **Gợi ý:** Dùng `zip` đã học hoặc hai chỉ số `self.i, self.j`.

### Bài 20: Đồng hồ đếm ngược với thông báo

* **Đề bài:** Viết class `DongHoDemNguoc(n)`: mỗi lần `next()` in ra số còn lại kèm dòng `"Còn lại: x"`, khi hết số thì in `"Het gio!"` (dòng này chỉ in trong `__next__` khi hết) và ném `StopIteration`. Dùng `for` để duyệt `DongHoDemNguoc(3)`.
* **Input:** Không có
* **Output:**
  ```
  Còn lại: 3
  Còn lại: 2
  Còn lại: 1
  Het gio!
  ```
* **Gợi ý:** Khi `hien_tai < 1`: in `"Het gio!"` rồi `raise StopIteration`.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Phân biệt iterable và iterator, dùng thành thạo `iter()` / `next()`.
* ✅ Hiểu vòng lặp `for` dùng `StopIteration` để thoát.
* ✅ Tự xây class iterator với `__iter__` / `__next__` — kể cả dãy vô hạn!
* ✅ Ứng dụng iterator vào đọc file, lọc dữ liệu, dãy Fibonacci, đảo danh sách...

> 💪 Chưa tự làm được bài nào thì đừng lo — đọc lại bài giảng, vẽ lại sơ đồ vòng lặp, rồi thử lại. **Lập trình là luyện tập.**

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 30: Virtual Environment](../30_Virtual_Environment/bai_giang.md)**