# 📝 Bài 11: Bài Tập – Vòng Lặp While

> 🎯 **Chủ đề:** `while`, vòng lặp vô hạn và cách tránh, `break`, `continue`, `else` với while, `while True`, menu vòng lặp, kiểm tra nhập liệu.

---

## 📌 Hướng dẫn làm bài

* Mỗi bài tập cần **tự viết code** rồi chạy thử trước khi xem đáp án.
* Nhớ "bộ ba bất tử": **khởi tạo → kiểm tra → cập nhật** — quên một chân là vòng lặp vô hạn!
* Bị treo thì nhấn `Ctrl + C` trong Terminal.
* Đáp án chi tiết 20 bài: 👉 [xem file dap_an.md](dap_an.md)

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Đếm từ 1 đến 10 bằng while

* **Đề bài:** Dùng `while` in các số từ 1 đến 10.
* **Input:** Không có.
* **Output:**
  ```
  1
  2
  ...
  10
  ```
* **Gợi ý:** `i = 1`; điều kiện `i <= 10`; cuối khối lệnh có `i = i + 1`.

### Bài 2: Đếm ngược từ 10 về 1

* **Đề bài:** Dùng `while` đếm ngược từ 10 về 1.
* **Input:** Không có.
* **Output:**
  ```
  10
  9
  ...
  1
  ```
* **Gợi ý:** Khởi tạo `i = 10`, điều kiện `i >= 1`, cập nhật `i = i - 1`.

### Bài 3: Tổng 1 đến n bằng while

* **Đề bài:** Nhập n, tính tổng `1 + 2 + ... + n` **bằng vòng lặp while**.
* **Input:** Số nguyên dương n.
* **Output:** Tổng.
* **Ví dụ:**
  ```
  Nhập n: 5
  Tổng: 15
  ```
* **Gợi ý:** Biến `i = 1`, biến `tong = 0`; vòng lặp cộng dồn rồi tăng i.

### Bài 4: In "Python" 5 lần bằng while

* **Đề bài:** Dùng `while` in dòng chữ `Python` đúng 5 lần, mỗi lần kèm số thứ tự: `Lan 1: Python`.
* **Input:** Không có.
* **Output:**
  ```
  Lan 1: Python
  Lan 2: Python
  ...
  Lan 5: Python
  ```
* **Gợi ý:** `dem = 1`; `while dem <= 5:`; đừng quên `dem = dem + 1`!

### Bài 5: Các số chẵn từ 2 đến 20

* **Đề bài:** Dùng `while` in các số chẵn từ 2 đến 20.
* **Input:** Không có.
* **Output:**
  ```
  2
  4
  ...
  20
  ```
* **Gợi ý:** Cập nhật `i = i + 2` mỗi lượt — bước nhảy 2.

### Bài 6: Bảng nhân 7 bằng while

* **Đề bài:** Dùng `while` in bảng nhân 7: từ `7 x 1 = 7` đến `7 x 10 = 70`.
* **Input:** Không có.
* **Output:** 10 dòng phép nhân.
* **Gợi ý:** `i = 1`; `while i <= 10:`; in `f"7 x {i} = {7 * i}"`; tăng i.

### Bài 7: Nhập số dương

* **Đề bài:** Nhập một số nguyên; nếu số ≤ 0 thì báo `So phai lon hon 0!` và **yêu cầu nhập lại** cho đến khi hợp lệ, rồi in số đã nhận.
* **Input:** Một hoặc nhiều số nguyên.
* **Output:** Số dương đã nhận.
* **Ví dụ:**
  ```
  Nhập số: -3
  So phai lon hon 0!
  Nhập số: 5
  Số đã nhận: 5
  ```
* **Gợi ý:** `while so <= 0:` — điều kiện "còn sai thì lặp lại".

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Cộng dồn đến khi nhập 0

* **Đề bài:** Nhập liên tục các số, cộng dồn lại; nhập **0** thì dừng và in tổng.
* **Input:** Nhiều số thực, kết thúc bằng 0.
* **Output:** Tổng các số đã nhập.
* **Ví dụ:**
  ```
  Nhập số (0 để dừng): 5
  Nhập số (0 để dừng): 3
  Nhập số (0 để dừng): 0
  Tổng: 8.0
  ```
* **Gợi ý:** `while True:` + `if so == 0: break`.

### Bài 9: Đếm ngược có hồi chuông

* **Đề bài:** Đếm ngược từ n về 1 (n nhập từ bàn phím), sau đó in `Het gio!`. Nếu n ≤ 0 thì in `So khong hop le!` mà không đếm.
* **Input:** Số nguyên n.
* **Output:** Dãy đếm ngược + dòng kết thúc.
* **Ví dụ:**
  ```
  Nhập n: 3
  3
  2
  1
  Het gio!
  ```
* **Gợi ý:** Điều kiện `i >= 1`; sau vòng lặp in "Het gio!" — dùng `else` của while để chỉ in khi đếm thật.

### Bài 10: Nhập điểm hợp lệ (0–10)

* **Đề bài:** Nhập điểm môn học; nếu điểm ngoài khoảng 0–10 thì báo lỗi và nhập lại; khi hợp lệ thì in `Điểm đã nhận: X` và xếp loại (>= 9 Xuất sắc, >= 8 Giỏi, >= 6.5 Khá, >= 5 Trung bình, còn lại Yếu).
* **Input:** Một hoặc nhiều số thực.
* **Output:** Điểm đã nhận và xếp loại.
* **Ví dụ:**
  ```
  Nhập điểm (0-10): 12
  Điểm không hợp lệ!
  Nhập điểm (0-10): 8.5
  Điểm đã nhận: 8.5
  Xếp loại: Gioi
  ```
* **Gợi ý:** `while True:` hỏi lại; `if 0 <= diem <= 10: break`. Xếp loại bằng if-elif sau vòng lặp.

### Bài 11: Đếm chữ số của n

* **Đề bài:** Nhập số nguyên dương n, đếm xem n có bao nhiêu chữ số (ví dụ 2026 có 4 chữ số).
* **Input:** Số nguyên dương.
* **Output:** Số lượng chữ số.
* **Ví dụ:**
  ```
  Nhập n: 2026
  Số chữ số: 4
  ```
* **Gợi ý:** Lặp phép chia `n = n // 10` cho tới khi n = 0, mỗi lần tăng biến đếm lên 1.

### Bài 12: Tổng các chữ số của n

* **Đề bài:** Nhập số nguyên dương n, tính tổng các chữ số của n (ví dụ 2026 → 2+0+2+6 = 10).
* **Input:** Số nguyên dương.
* **Output:** Tổng các chữ số.
* **Ví dụ:**
  ```
  Nhập n: 2026
  Tổng các chữ số: 10
  ```
* **Gợi ý:** Chữ số cuối là `n % 10`; bỏ chữ số cuối bằng `n = n // 10`; cộng dồn đến khi hết.

### Bài 13: Đảo ngược số

* **Đề bài:** Nhập số nguyên dương n, in ra số đảo ngược (ví dụ 2026 → 6202; lưu ý chữ số 0 đầu kết quả bị mất là chấp nhận).
* **Input:** Số nguyên dương.
* **Output:** Số đảo ngược.
* **Ví dụ:**
  ```
  Nhập n: 2026
  Số đảo ngược: 6202
  ```
* **Gợi ý:** Xây dựng `so_dao = so_dao * 10 + (n % 10)` rồi `n = n // 10`.

### Bài 14: Tìm ước chung lớn nhất

* **Đề bài:** Nhập hai số nguyên dương a, b; tìm **ước chung lớn nhất** bằng phương pháp trừ liên tiếp: lặp tới khi a == b; nếu a > b thì a = a - b, ngược lại b = b - a. Kết quả là a (hoặc b).
* **Input:** Hai số nguyên dương.
* **Output:** ƯCLN.
* **Ví dụ:**
  ```
  Nhập a: 12
  Nhập b: 8
  ƯCLN(12, 8) = 4
  ```
* **Gợi ý:** Điều kiện lặp `while a != b:`; in kết quả sau vòng lặp.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Game đoán số

* **Đề bài:** Máy nghĩ số bí mật từ 1 đến 10 (cố định là 7 để dễ kiểm tra). Người chơi đoán liên tục; mỗi lần sai, máy gợi ý `Nho hon so bi mat!` hoặc `Lon hon so bi mat!`. Đoán đúng thì in `Chuc mung! Ban doan dung sau X lan.` rồi kết thúc.
* **Input:** Nhiều số nguyên (lần đoán).
* **Output:** Gợi ý và kết quả.
* **Ví dụ:**
  ```
  Lần đoán 1: 5
  Nho hon so bi mat!
  Lần đoán 2: 8
  Lon hon so bi mat!
  Lần đoán 3: 7
  Chuc mung! Ban doan dung sau 3 lan.
  ```
* **Gợi ý:** `so_bi_mat = 7`; `while True:` với biến đếm `so_lan`; `break` khi đúng.

### Bài 16: Kiểm tra số đối xứng

* **Đề bài:** Nhập số nguyên dương n, kiểm tra n có phải **số đối xứng** (đọc xuôi, ngược giống nhau — ví dụ 1221, 585) hay không. In `La so doi xung` hoặc `Khong phai so doi xung`.
* **Input:** Số nguyên dương.
* **Output:** Kết luận.
* **Ví dụ:**
  ```
  Nhập n: 1221
  La so doi xung
  ```
* **Gợi ý:** Đảo ngược n (kỹ thuật bài 13) rồi so sánh với n ban đầu (nhớ lưu bản gốc trước khi phá hủy n).

### Bài 17: Kiểm tra số nguyên tố bằng while

* **Đề bài:** Nhập số nguyên dương n, kiểm tra n có phải số nguyên tố không (chỉ chia hết cho 1 và chính nó; 2 là nguyên tố nhỏ nhất). In `La so nguyen to` hoặc `Khong phai so nguyen to`.
* **Input:** Số nguyên dương.
* **Output:** Kết luận.
* **Ví dụ:**
  ```
  Nhập n: 29
  La so nguyen to
  ```
* **Gợi ý:** `i = 2`; `while i < n:`; nếu `n % i == 0` thì `break`; dùng `else` của while để kết luận "là nguyên tố".

### Bài 18: Lãi kép — bao giờ đạt mục tiêu?

* **Đề bài:** Gửi tiết kiệm S triệu đồng, lãi r% mỗi tháng (lãi kép). Nhập S, r và số tiền mục tiêu M. Hỏi sau **ít nhất bao nhiêu tháng** thì số tiền đạt hoặc vượt M?
* **Input:** S (float), r (float), M (float).
* **Output:** Số tháng cần gửi.
* **Ví dụ:**
  ```
  Nhập tiền gửi (triệu): 100
  Nhập lãi suất %/tháng: 1
  Nhập mục tiêu (triệu): 150
  Cần 41 tháng để đạt mục tiêu
  ```
* **Gợi ý:** `while tien < M:` — mỗi lượt cộng lãi và tăng biến đếm tháng; số tháng không biết trước nên phải dùng while.

### Bài 19: Game đoán số ngẫu nhiên (có giới hạn lượt)

* **Đề bài:** Dùng `import random` — máy nghĩ số ngẫu nhiên `random.randint(1, 100)`. Người chơi có tối đa **7 lượt** đoán; mỗi lần gợi ý lớn/nhỏ hơn. Đoán đúng → chúc mừng kèm số lượt; hết lượt → in `Ban da thua! So bi mat la: X`.
* **Input:** Nhiều số nguyên (tối đa 7 lượt).
* **Output:** Gợi ý và kết quả.
* **Ví dụ:**
  ```
  Lần 1/7: 50
  Lon hon so bi mat!
  ...
  ```
* **Gợi ý:** Biến `so_lan = 0`; điều kiện `while so_lan < 7:`; tăng `so_lan` mỗi lượt; `break` khi đúng; `else` của while in thông báo thua.

### Bài 20: Máy ATM hoàn chỉnh

* **Đề bài:** Viết chương trình máy ATM chạy vòng lặp với menu:
  * `0. Thoát` — in lời tạm biệt rồi kết thúc.
  * `1. Xem số dư` — in số dư hiện tại.
  * `2. Nạp tiền` — nhập số tiền dương, cộng vào số dư.
  * `3. Rút tiền` — nhập số tiền; nếu lớn hơn số dư → `So du khong du!`, ngược lại trừ vào số dư.
  * Số khác → `Lua chon khong hop le!`
  
  Số dư khởi tạo 1 000 000 VND. Sau mỗi thao tác quay lại menu.
* **Input:** Chuỗi lựa chọn và số tiền (khi nạp/rút).
* **Output:** Menu lặp lại và kết quả từng thao tác.
* **Ví dụ:**
  ```
  === MÁY ATM ===
  0. Thoát
  1. Xem số dư
  2. Nạp tiền
  3. Rút tiền
  Nhập lựa chọn: 2
  Nhập số tiền muốn nạp: 50000
  Nạp tiền thành công. Số dư mới: 1050000.0 VND
  ...
  Nhập lựa chọn: 0
  Cảm ơn bạn đã sử dụng ATM!
  ```
* **Gợi ý:** `while True:` bao quanh menu; `if lua_chon == "0": break`; số dư là biến cập nhật bên trong vòng lặp; kiểm tra tiền dương khi nạp.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Viết thành thạo `while` với "bộ ba: khởi tạo – kiểm tra – cập nhật".
* ✅ Tránh và xử lý được vòng lặp vô hạn.
* ✅ Dùng `break`, `continue`, `else` với while đúng tình huống.
* ✅ Xây dựng menu vòng lặp (máy ATM) và game tương tác (đoán số).
* ✅ Kiểm soát đầu vào hợp lệ — chương trình không "chết" vì dữ liệu xấu.

> 💪 Chưa tự làm được bài nào thì đừng lo — hãy xem lại bài giảng rồi quay lại. **Lập trình là luyện tập!**

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 12: Hàm](../12_Ham/bai_giang.md)**
