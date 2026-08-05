# 📝 Bài 10: Bài Tập – Vòng Lặp For

> 🎯 **Chủ đề:** `for`, `range(start, stop, step)`, duyệt chuỗi/list, `enumerate`, `break`, `continue`, vòng lặp lồng nhau.

---

## 📌 Hướng dẫn làm bài

* Mỗi bài tập cần **tự viết code** rồi chạy thử trước khi xem đáp án.
* Nhớ: `range(1, n + 1)` mới đếm đủ tới n — "một cộng"!
* Đáp án chi tiết 20 bài: 👉 [xem file dap_an.md](dap_an.md)

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Đếm từ 1 đến 10

* **Đề bài:** Dùng vòng lặp `for` in các số từ 1 đến 10, mỗi số một dòng.
* **Input:** Không có.
* **Output:**
  ```
  1
  2
  ...
  10
  ```
* **Gợi ý:** `for i in range(1, 11): print(i)`.

### Bài 2: Các số lẻ từ 1 đến 20

* **Đề bài:** In các số lẻ từ 1 đến 20, mỗi số một dòng.
* **Input:** Không có.
* **Output:**
  ```
  1
  3
  5
  ...
  19
  ```
* **Gợi ý:** Dùng step 2: `range(1, 21, 2)`.

### Bài 3: Tổng từ 1 đến n

* **Đề bài:** Nhập số nguyên dương n, tính và in tổng `1 + 2 + ... + n`.
* **Input:** Một số nguyên dương n.
* **Output:** Tổng.
* **Ví dụ:**
  ```
  Nhập n: 5
  Tổng 1 + 2 + ... + 5 = 15
  ```
* **Gợi ý:** Biến `tong = 0` rồi cộng dồn từng i trong vòng lặp.

### Bài 4: In chữ 5 lần

* **Đề bài:** In dòng chữ `Xin chao Python!` đúng 5 lần, mỗi lần kèm số thứ tự: `Lan 1: Xin chao Python!`.
* **Input:** Không có.
* **Output:**
  ```
  Lan 1: Xin chao Python!
  Lan 2: Xin chao Python!
  ...
  Lan 5: Xin chao Python!
  ```
* **Gợi ý:** `for i in range(1, 6): print(f"Lan {i}: ...")`.

### Bài 5: Bảng nhân của n

* **Đề bài:** Nhập số nguyên n (1–9), in bảng nhân n từ `n x 1 = ...` đến `n x 10 = ...`.
* **Input:** Một số nguyên.
* **Output:** 10 dòng phép nhân.
* **Ví dụ:**
  ```
  Nhập n: 5
  5 x 1 = 5
  5 x 2 = 10
  ...
  5 x 10 = 50
  ```
* **Gợi ý:** `for i in range(1, 11): print(f"{n} x {i} = {n * i}")`.

### Bài 6: Số chẵn giảm dần

* **Đề bài:** In các số chẵn **giảm dần** từ 20 về 0, mỗi số một dòng.
* **Input:** Không có.
* **Output:**
  ```
  20
  18
  ...
  0
  ```
* **Gợi ý:** `range(20, -1, -2)` — step âm và nhớ `stop` là `-1` để có số 0.

### Bài 7: Tên của bạn từng chữ

* **Đề bài:** Nhập họ tên của bạn, in **từng chữ cái** trên một dòng.
* **Input:** Một chuỗi họ tên.
* **Output:** Từng ký tự trên từng dòng.
* **Ví dụ:**
  ```
  Nhập họ tên: An
  A
  n
  ```
* **Gợi ý:** `for chu in ho_ten:` — chuỗi duyệt được từng ký tự.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Giai thừa n!

* **Đề bài:** Nhập số nguyên dương n, tính và in `n! = 1 * 2 * ... * n`.
* **Input:** Một số nguyên dương.
* **Output:** Giá trị giai thừa.
* **Ví dụ:**
  ```
  Nhập n: 5
  5! = 120
  ```
* **Gợi ý:** Biến nhân dồn khởi tạo **1** (không phải 0!), nhân dồn từ 1 đến n.

### Bài 9: Tổng số chẵn từ 0 đến n

* **Đề bài:** Nhập số nguyên dương n, tính tổng các số chẵn từ 0 đến n.
* **Input:** Một số nguyên dương.
* **Output:** Tổng.
* **Ví dụ:**
  ```
  Nhập n: 10
  Tổng các số chẵn từ 0 đến 10 là: 30
  ```
* **Gợi ý:** Cách 1: `if i % 2 == 0` để lọc; Cách 2 (gọn hơn): `range(0, n + 1, 2)`.

### Bài 10: Bỏ qua số chia hết cho 3

* **Đề bài:** In các số từ 1 đến 30, nhưng **bỏ qua** các số chia hết cho 3.
* **Input:** Không có.
* **Output:**
  ```
  1
  2
  4
  5
  7
  ...
  29
  ```
* **Gợi ý:** Dùng `if i % 3 == 0: continue` trong vòng lặp.

### Bài 11: Bảng cửu chương 2 đến 5

* **Đề bài:** In các bảng nhân từ 2 đến 5, mỗi bảng đủ 10 phép tính, trước mỗi bảng in dòng `=== BANG NHAN {so} ===`.
* **Input:** Không có.
* **Output:**
  ```
  === BANG NHAN 2 ===
  2 x 1 = 2
  ...
  === BANG NHAN 3 ===
  ...
  ```
* **Gợi ý:** Hai vòng lặp lồng nhau: vòng ngoài chọn bảng, vòng trong in phép tính.

### Bài 12: Trung bình cộng n số

* **Đề bài:** Nhập số lượng môn học n, rồi nhập điểm của từng môn; in trung bình cộng (làm tròn 2 chữ số thập phân).
* **Input:** n và n điểm (số thực).
* **Output:** Điểm trung bình.
* **Ví dụ:**
  ```
  Nhập số môn: 3
  Nhập điểm môn 1: 7
  Nhập điểm môn 2: 8
  Nhập điểm môn 3: 9
  Điểm trung bình: 8.0
  ```
* **Gợi ý:** Cộng dồn trong vòng lặp `range(n)`, sau đó chia cho n.

### Bài 13: Hóa đơn siêu thị

* **Đề bài:** Nhập số món hàng n, rồi nhập giá từng món (nghìn đồng); in từng món đã mua và tổng tiền phải trả.
* **Input:** n và n giá tiền.
* **Output:** Tổng tiền hóa đơn.
* **Ví dụ:**
  ```
  Nhập số món hàng: 3
  Nhập giá món 1: 15
  Nhập giá món 2: 25
  Nhập giá món 3: 10
  Tổng hóa đơn: 50 nghìn đồng
  ```
* **Gợi ý:** Biến tích lũy cộng dồn giá từng món ngay khi nhập.

### Bài 14: Vị trí đầu tiên của ký tự

* **Đề bài:** Nhập một chuỗi và một ký tự, in vị trí **đầu tiên** ký tự đó xuất hiện (vị trí đếm từ 0). Nếu không có → in `Khong tim thay!`.
* **Input:** Một chuỗi và một ký tự.
* **Output:** Vị trí đầu tiên hoặc thông báo.
* **Ví dụ:**
  ```
  Nhập chuỗi: python
  Nhập ký tự: t
  Vị trí đầu tiên: 2
  ```
* **Gợi ý:** `for vi_tri, ky_tu in enumerate(chuoi):` và dùng `break` khi tìm thấy; dùng biến cờ `tim_thay` để biết có tìm thấy hay không.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Toàn bộ bảng cửu chương

* **Đề bài:** In bảng cửu chương từ 2 đến 9, mỗi bảng đủ 10 phép tính, có dòng tiêu đề và **dòng trống** ngăn cách giữa các bảng.
* **Input:** Không có.
* **Output:** 8 bảng cửu chương hoàn chỉnh.
* **Gợi ý:** Vòng lặp lồng nhau; `print()` không đối số sẽ xuống dòng tạo khoảng cách.

### Bài 16: Kiểm tra số nguyên tố

* **Đề bài:** Nhập số nguyên dương n, kiểm tra n có phải số nguyên tố không (chia hết cho 1 và chính nó; 2 là số nguyên tố nhỏ nhất). In `La so nguyen to` hoặc `Khong phai so nguyen to`.
* **Input:** Một số nguyên dương.
* **Output:** Kết luận.
* **Ví dụ:**
  ```
  Nhập n: 17
  La so nguyen to
  ```
* **Gợi ý:** Đếm số ước trong khoảng `range(2, n)` — nếu có ước nào chia hết thì không phải nguyên tố; dùng biến cờ hoặc `break`.

### Bài 17: Tam giác sao

* **Đề bài:** Nhập chiều cao h, vẽ tam giác vuông cân bằng dấu `*`, hàng thứ i có i dấu `*` (i từ 1 đến h).
* **Input:** Một số nguyên dương.
* **Output:** Hình tam giác.
* **Ví dụ:**
  ```
  Nhập chiều cao: 4
  *
  **
  ***
  ****
  ```
* **Gợi ý:** Vòng ngoài in từng hàng; nhân chuỗi: `"*" * i` tạo i dấu `*`.

### Bài 18: Tổng dãy phân số

* **Đề bài:** Nhập n, tính `S = 1 + 1/2 + 1/3 + ... + 1/n` và in kết quả làm tròn 2 chữ số thập phân.
* **Input:** Số nguyên dương n.
* **Output:** Tổng (2 chữ số thập phân).
* **Ví dụ:**
  ```
  Nhập n: 4
  S = 2.08
  ```
* **Gợi ý:** Cộng dồn `tong = tong + 1 / i`; lưu ý `1/i` trong Python 3 là phép chia thực.

### Bài 19: Dãy Fibonacci

* **Đề bài:** Nhập n, in **n số đầu tiên** của dãy Fibonacci (0, 1, 1, 2, 3, 5, 8, ... — mỗi số bằng tổng hai số trước).
* **Input:** Số nguyên dương n.
* **Output:** n số Fibonacci.
* **Ví dụ:**
  ```
  Nhập n: 7
  0 1 1 2 3 5 8
  ```
* **Gợi ý:** Hai biến `a, b` bắt đầu là 0, 1; mỗi lượt in `a` rồi gán đồng thời `a, b = b, a + b`.

### Bài 20: Lãi kép tiết kiệm

* **Đề bài:** Gửi tiết kiệm số tiền S (triệu đồng), lãi suất r% **mỗi tháng**, lãi được nhập vào gốc hằng tháng (lãi kép). Nhập S, r và số tháng n; tính số tiền sau n tháng (làm tròn 2 chữ số thập phân).
* **Input:** S (float), r (float), n (int).
* **Output:** Số tiền sau n tháng.
* **Ví dụ:**
  ```
  Nhập số tiền gửi (triệu): 100
  Nhập lãi suất %/tháng: 1
  Nhập số tháng: 12
  Số tiền sau 12 tháng: 112.68 triệu đồng
  ```
* **Gợi ý:** Mỗi tháng: `tien = tien + tien * r / 100` — lặp n lần, in kết quả bằng `round(..., 2)`.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Thành thạo `for` với `range(start, stop, step)` — kể cả đếm ngược.
* ✅ Duyệt chuỗi và danh sách, dùng `enumerate` lấy vị trí.
* ✅ Điều khiển vòng lặp với `break` và `continue`.
* ✅ Viết vòng lặp lồng nhau cho bảng cửu chương, hình vẽ.
* ✅ Giải các bài toán thực tế: giai thừa, tổng, hóa đơn, lãi suất.

> 💪 Chưa tự làm được bài nào thì đừng lo — hãy xem lại bài giảng rồi quay lại. **Lập trình là luyện tập!**

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 11: Vòng Lặp While](../11_Vong_lap_while/bai_giang.md)**
