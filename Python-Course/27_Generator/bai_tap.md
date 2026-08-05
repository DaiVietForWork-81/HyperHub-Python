# 📝 Bài 27: Bài Tập – Generator

> 🎯 **Chủ đề:** Generator function với `yield`, `next()`, generator expression, Fibonacci, đọc file từng dòng, tiết kiệm bộ nhớ.

---

## 📌 Hướng dẫn làm bài

* Mỗi bài tập cần **tự viết code** rồi chạy thử trước khi xem đáp án.
* Nhớ: hàm có `yield` trở thành generator — cần duyệt hoặc `next()` mới có giá trị.
* Đáp án chi tiết 20 bài: 👉 [xem file dap_an.md](dap_an.md)

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Generator in 5 số đầu

* **Đề bài:** Viết generator `dem_den(n)` sinh các số từ 0 đến n-1. Gọi với n = 5 và in từng số bằng vòng lặp `for`.
* **Input:** Không có.
* **Output:**
  ```
  0 1 2 3 4
  ```
* **Gợi ý:** `for x in range(n): yield x`, sau đó `for so in dem_den(5): print(so, end=" ")`.

### Bài 2: Generator bình phương

* **Đề bài:** Viết generator `binh_phuong(n)` sinh bình phương các số 0..n-1. Gọi với n = 6, in từng giá trị.
* **Input:** Không có.
* **Output:**
  ```
  0 1 4 9 16 25
  ```
* **Gợi ý:** `yield x * x`.

### Bài 3: Chuyển generator thành list

* **Đề bài:** Viết generator `chan(n)` sinh các số chẵn 0, 2, 4... nhỏ hơn n. Gọi với n = 10, chuyển kết quả thành list bằng `list()` và in.
* **Input:** Không có.
* **Output:**
  ```
  [0, 2, 4, 6, 8]
  ```
* **Gợi ý:** `[0, 2, 4, 6, 8] = list(chan(10))`.

### Bài 4: Dùng next() lấy từng phần tử

* **Đề bài:** Viết generator `doi(x)` trả `x * 2`. Gọi và lấy 3 phần tử đầu bằng `next()` rồi in chúng.
* **Input:** Không có.
* **Output:**
  ```
  0
  2
  4
  ```
* **Gợi ý:** `g = doi(3)` rồi `print(next(g))` ba lần.

### Bài 5: Generator đếm ngược

* **Đề bài:** Viết generator `dem_nguoc(n)` sinh n, n-1, ..., 1. Gọi với n = 5 và in các giá trị trên một dòng.
* **Input:** Không có.
* **Output:**
  ```
  5 4 3 2 1
  ```
* **Gợi ý:** `while n > 0: yield n; n -= 1`.

### Bài 6: Generator bảng cửu chương

* **Đề bài:** Viết generator `bang_nhan(k)` sinh các chuỗi `"k x i = k*i"` cho i = 1..10. Gọi với k = 3 và in từng dòng.
* **Input:** Không có.
* **Output:**
  ```
  3 x 1 = 3
  3 x 2 = 6
  ...
  3 x 10 = 30
  ```
* **Gợi ý:** `yield f"{k} x {i} = {k * i}"`.

### Bài 7: Generator expression nhỏ

* **Đề bài:** Dùng generator expression `(x * 3 for x in range(1, 6))` rồi in tổng các giá trị.
* **Input:** Không có.
* **Output:**
  ```
  45
  ```
* **Gợi ý:** `sum(x * 3 for x in range(1, 6))` — 3+6+9+12+15.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Generator Fibonacci 10 số

* **Đề bài:** Viết generator `fibonacci(n)` sinh n số Fibonacci đầu tiên (0, 1, 1, 2, 3, 5...). Gọi với n = 10, in dãy.
* **Input:** Không có.
* **Output:**
  ```
  0 1 1 2 3 5 8 13 21 34
  ```
* **Gợi ý:** `a, b = 0, 1; yield a; a, b = b, a + b` trong vòng lặp.

### Bài 9: Generator số chẵn đến n

* **Đề bài:** Viết generator `so_chan(n)` sinh các số chẵn từ 0 đến n. Gọi với n = 20, tính tổng bằng `sum()`.
* **Input:** Không có.
* **Output:**
  ```
  110
  ```
* **Gợi ý:** `yield x` khi `x % 2 == 0`; 0+2+...+20 = 110.

### Bài 10: Đọc file từng dòng

* **Đề bài:** Tạo file `nhat_ky.txt` với 3 dòng nội dung bất kỳ (dùng `open(..., "w")`). Viết generator `doc_file(ten)` đọc và trả từng dòng đã bỏ ký tự xuống dòng. In 3 dòng ra màn hình.
* **Input:** Không có.
* **Output:** Ví dụ:
  ```
  Dong 1: Chao buoi sang
  Dong 2: Toi dang hoc Python
  Dong 3: Generator rat hay
  ```
* **Gợi ý:** `with open(ten, encoding="utf-8") as f: for dong in f: yield dong.strip()`.

### Bài 11: Lọc dòng chứa từ khóa

* **Đề bài:** File `log.txt` có 4 dòng (2 dòng bắt đầu bằng `LOI`, 2 dòng khác). Viết generator lọc và in ra những dòng bắt đầu bằng `LOI`.
* **Input:** Không có.
* **Output:** Ví dụ:
  ```
  LOI ket noi mang
  LOI tai lieu khong ton tai
  ```
* **Gợi ý:** `if dong.startswith("LOI"): yield dong`.

### Bài 12: Tổng bằng generator expression có điều kiện

* **Đề bài:** Dùng generator expression tính tổng **bình phương các số lẻ** từ 1 đến 10.
* **Input:** Không có.
* **Output:**
  ```
  165
  ```
* **Gợi ý:** `sum(x * x for x in range(1, 11) if x % 2 == 1)` — 1+9+25+49+81 = 165.

### Bài 13: Generator phân tách chữ số

* **Đề bài:** Viết generator `chu_so(so)` sinh từng chữ số của một số nguyên dương (từ trái sang phải). Gọi với 2026 và in các chữ số.
* **Input:** Không có.
* **Output:**
  ```
  2 0 2 6
  ```
* **Gợi ý:** đổi sang chuỗi `str(so)` rồi duyệt từng ký tự, `yield int(c)`.

### Bài 14: Generator xoay vòng ba môn học

* **Đề bài:** Viết generator `lich_hoc()` lặp vô hạn qua 3 môn `["Toan", "Ly", "Hoa"]` theo thứ tự. Dùng `islice` lấy 7 phần tử đầu và in.
* **Input:** Không có.
* **Output:**
  ```
  Toan Ly Hoa Toan Ly Hoa Toan
  ```
* **Gợi ý:** `while True:` duyệt danh sách rồi `yield mon`; `from itertools import islice`.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Generator số nguyên tố

* **Đề bài:** Viết generator `so_nguyen_to(n)` sinh các số nguyên tố nhỏ hơn n. Gọi với n = 30, in các số nguyên tố.
* **Input:** Không có.
* **Output:**
  ```
  2 3 5 7 11 13 17 19 23 29
  ```
* **Gợi ý:** hàm phụ `la_nguyen_to(x)` kiểm tra ước từ 2 đến `x - 1` (hoặc đến `int(x**0.5)`).

### Bài 16: So sánh bộ nhớ list vs generator

* **Đề bài:** Viết chương trình so sánh `sys.getsizeof` của list `[x for x in range(50000)]` và generator `(x for x in range(50000))`, in ra hai con số.
* **Input:** Không có.
* **Output:** Ví dụ:
  ```
  Kich thuoc list: 406632 byte
  Kich thuoc generator: 112 byte
  ```
* **Gợi ý:** `import sys; print(sys.getsizeof(lst)); print(sys.getsizeof(gen))`.

### Bài 17: Đếm dòng trong file lớn (giả lập)

* **Đề bài:** Tạo file `du_lieu.txt` có 5 dòng số. Dùng generator + `sum(1 for ...)` để đếm số dòng **không rỗng** và in ra.
* **Input:** Không có.
* **Output:**
  ```
  So dong khong rong: 5
  ```
* **Gợi ý:** `sum(1 for dong in f if dong.strip() != "")`.

### Bài 18: Generator ghép đôi hai danh sách

* **Đề bài:** Viết generator `ghep_doi(a, b)` sinh lần lượt phần tử a[0], b[0], a[1], b[1], ... Cho `a = ["A1","A2"]`, `b = ["B1","B2"]`, in kết quả.
* **Input:** Không có.
* **Output:**
  ```
  A1 B1 A2 B2
  ```
* **Gợi ý:** duyệt `range(len(a))` rồi `yield a[i]` và `yield b[i]`.

### Bài 19: Tổng Fibonacci 50 số (chứng minh tiết kiệm nhớ)

* **Đề bài:** Dùng generator `fibonacci(n)` (bài 8) tính tổng 50 số Fibonacci đầu tiên bằng `sum()` và in kết quả (số chẵn).
* **Input:** Không có.
* **Output:**
  ```
  Tong 50 so Fibonacci dau: 12586269024
  ```
* **Gợi ý:** `sum(fibonacci(50))` — chỉ cần generator, không cần list.

### Bài 20: Đọc log + thống kê lỗi (tổng hợp)

* **Đề bài:** Tạo file `he_thong.log` gồm các dòng dạng `OK ...` hoặc `LOI ...` (tự viết 6 dòng). Viết chương trình dùng generator đọc file, đếm số dòng `LOI` và in ra tổng.
* **Input:** Không có.
* **Output:** Ví dụ:
  ```
  So loi phan hien: 3
  ```
* **Gợi ý:** generator `doc_file` (bài 10) kết hợp `sum(1 for dong in doc_file(...) if dong.startswith("LOI"))`.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Viết generator function với `yield`, dùng `next()` và vòng lặp.
* ✅ Dùng generator expression tiết kiệm bộ nhớ.
* ✅ Dựng Fibonacci, số nguyên tố, dãy vô hạn.
* ✅ Xử lý file lớn từng dòng và đếm/thống kê bằng generator.

> 💪 Chưa tự làm được bài nào thì đừng lo — hãy xem lại bài giảng rồi quay lại. **Lập trình là luyện tập!**

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 28: Decorator](../28_Decorator/bai_giang.md)**
