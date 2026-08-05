# 📝 Bài 13: Bài Tập – Phạm Vi Biến (Scope)

> 🎯 **Chủ đề:** Biến local – global, từ khóa `global`, `nonlocal`, quy tắc LEGB, tránh lạm dụng biến toàn cục.

---

## 📌 Hướng dẫn làm bài

* Mỗi bài tập cần **tự viết code** rồi chạy thử trước khi xem đáp án.
* Nhiều bài yêu cầu **đoán kết quả** — hãy viết chương trình chạy để kiểm chứng, đừng chỉ đoán mò.
* Đáp án chi tiết 20 bài: 👉 [xem file dap_an.md](dap_an.md)

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Biến trong hàm là local

* **Đề bài:** Viết hàm `in_so()` bên trong tạo biến `so = 42` rồi in ra. Ở ngoài hàm, gọi `in_so()`. Giải thích: biến `so` có dùng được ngoài hàm không? In `so` ngoài hàm xem điều gì xảy ra.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  So trong ham: 42
  Traceback ... NameError: name 'so' is not defined
  ```
* **Gợi ý:** Biến tạo trong hàm chỉ tồn tại trong hàm — dùng ngoài sẽ lỗi `NameError`. Ghi chú bằng comment thay vì bắt buộc chạy lỗi.

### Bài 2: Đọc biến global trong hàm

* **Đề bài:** Khai báo biến global `phi_phuc_vu = 5000`. Viết hàm `tong_tien(mon)` trả về `mon * 30000 + phi_phuc_vu`. In kết quả cho `mon = 2`.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  65000
  ```
* **Gợi ý:** Hàm chỉ **đọc** biến global nên không cần từ khóa `global`.

### Bài 3: Hàm gán biến — có sửa global không?

* **Đề bài:** Khai báo `x = 10` ngoài hàm. Viết hàm `doi_x()` bên trong gán `x = 99` (không dùng `global`). Gọi hàm rồi in `x` ở ngoài. Kết quả là bao nhiêu?
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  10
  ```
* **Gợi ý:** Gán trong hàm tạo biến **local mới** — biến global giữ nguyên.

### Bài 4: Dùng từ khóa `global`

* **Đề bài:** Khai báo `so_lan = 0`. Viết hàm `lap_mot_lan()` dùng `global so_lan` để tăng biến lên 1 và in ra `Lan lap: <so_lan>`. Gọi hàm 3 lần.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Lan lap: 1
  Lan lap: 2
  Lan lap: 3
  ```
* **Gợi ý:** Nhớ khai báo `global` **trước** khi sửa biến.

### Bài 5: Trả về thay vì global

* **Đề bài:** Viết hàm `cong_mot(so)` trả về `so + 1` (không dùng `global`). Gọi hàm 3 lần, mỗi lần gán kết quả trở lại cho cùng biến `n`, rồi in `n`.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  3
  ```
* **Gợi ý:** `n = cong_mot(n)` — giá trị trả về "chảy ngược" về biến ngoài.

### Bài 6: Tìm mức LEGB

* **Đề bài:** Cho code:

  ```python
  ten = "G"
  def ham_ngoai():
      ten = "E"
      def ham_trong():
          ten = "L"
          print(ten)
      ham_trong()
  ham_ngoai()
  ```
  Viết chương trình này vào file và chạy. Kết quả in ra là gì?
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  L
  ```
* **Gợi ý:** Python tìm theo LEGB — biến local tồn tại nên được dùng ngay, không nhìn ra ngoài.

### Bài 7: Hàm đọc biến global làm việc bình thường

* **Đề bài:** Khai báo `giam_gia = 0.2`. Viết hàm `gia_sau_giam(gia)` trả về `gia * (1 - giam_gia)`. In kết quả cho `gia = 100000`.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  80000.0
  ```
* **Gợi ý:** Đọc biến global không cần khai báo gì thêm.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Trước hay sau? Không thay đổi được

* **Đề bài:** Viết hàm `kho_dam(x)` có tham số tên `x`, bên trong gán `x = 999` rồi trả về `x`. Gọi `kho_dam(5)` và in kết quả. In giá trị của `x` ngoài hàm (nếu khai báo `x = 5` ngoài) — giá trị ngoài có đổi không?
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  999
  5
  ```
* **Gợi ý:** Tham số cũng là biến local của hàm.

### Bài 9: Đếm lượt mở ứng dụng

* **Đề bài:** Khai báo `so_luot_mo = 0`. Viết hàm `mo_ung_dung()` dùng `global` để tăng số lượt và trả về chuỗi `Da mo ung dung lan thu <n>`. Gọi hàm 2 lần, in kết quả từng lần, rồi in `so_luot_mo`.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Da mo ung dung lan thu 1
  Da mo ung dung lan thu 2
  Tong so luot mo: 2
  ```
* **Gợi ý:** Kết hợp `global` và `f-string`.

### Bài 10: Sửa lỗi UnboundLocalError

* **Đề bài:** Code sau bị lỗi `UnboundLocalError`. Hãy sửa để chạy đúng:

  ```python
  diem = 10
  def tang_diem():
      diem += 1
  tang_diem()
  print(diem)
  ```
* **Output mong đợi:**
  ```
  11
  ```
* **Gợi ý:** Có 2 cách sửa: thêm `global diem`, hoặc bỏ lệnh tăng và dùng `return diem + 1`.

### Bài 11: Vì sao lỗi? Giải thích bằng comment

* **Đề bài:** Viết hàm `ham_lu(flag)` với code sau và chạy với `flag = False`:

  ```python
  def ham_lu(flag):
      if flag:
          gia_tri = 1
      return gia_tri
  ```
* **Output:**
  ```
  Traceback ... UnboundLocalError: local variable 'gia_tri' referenced before assignment
  ```
* **Gợi ý:** `gia_tri` chỉ được gán khi `flag` đúng — khi sai, biến chưa từng tồn tại. Ghi chú giải thích trong comment.

### Bài 12: Hàm lồng nhau không dùng nonlocal

* **Đề bài:** Viết hàm `dem_ngoai()`: khai báo `n = 0`, bên trong định nghĩa `dem_trong()` thực hiện `n = n + 1` (KHÔNG có `nonlocal`) rồi gọi nó. Chạy thử — lỗi gì xảy ra? Sửa lại bằng `nonlocal` để chạy đúng, in `n` sau khi gọi 2 lần.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  2
  ```
* **Gợi ý:** Gán biến của hàm ngoài từ hàm trong bắt buộc khai báo `nonlocal`.

### Bài 13: Tách biến global — đặt tên khác

* **Đề bài:** Biến global `tong` đang dùng ở ngoài. Viết hàm `tinh_tong_cuc_bo(a, b)` dùng biến **local tên khác** `tong_local` và trả về kết quả. Gọi hàm với `7, 8` rồi in cả kết quả và `tong` global (khai báo `tong = 100` ngoài).
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  15
  100
  ```
* **Gợi ý:** Đặt tên khác để tránh nhầm lẫn — không cần `global` lúc nào cũng có thể.

### Bài 14: Hóa đơn cửa hàng — tổng hợp scope

* **Đề bài:** Khai báo global `thue = 0.1`. Viết hàm `thanh_toan(gia_goc)`:
  * Nếu `gia_goc >= 100000` thì giảm thêm `giam_them = 0.05` (biến local), ngược lại `giam_them = 0`.
  * Trả về `gia_goc * (1 - giam_them) * (1 + thue)`.
  In kết quả cho `thanh_toan(120000)` và `thanh_toan(50000)` (làm tròn 0 chữ số thập phân).
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  125400
  55000
  ```
* **Gợi ý:** `120000 * 0.95 * 1.1 = 125400`; `50000 * 1.1 = 55000`.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Máy rút tiền — lỗi kinh điển

* **Đề bài:** Chạy code sau:

  ```python
  so_du = 100000
  def rut(tien):
      so_du -= tien
      return so_du
  rut(20000)
  print(so_du)
  ```
  Dự đoán kết quả trước khi chạy, chạy thử để kiểm tra. Sửa bằng `global` để hàm cập nhật được số dư, sau đó in số dư.
* **Output mong đợi sau khi sửa:**
  ```
  80000
  ```
* **Gợi ý:** Phép `so_du -= tien` chính là `so_du = so_du - tien` — một phép gán.

### Bài 16: So sánh 2 cách cộng dồn

* **Đề bài:** Viết 2 phiên bản đếm: (a) dùng biến global + `global`, (b) dùng tham số + `return`. Cả hai in kết quả sau khi gọi 3 lần với `+2`. Chỉ rõ bằng comment cách nào dễ đọc hơn.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Cach global: 6
  Cach return: 6
  ```
* **Gợi ý:** Phiên bản (b): `n = cong(n, 2)` lặp lại 3 lần.

### Bài 17: Đếm số lần gọi hàm — dùng nonlocal

* **Đề bài:** Viết hàm `tao_bo_dem()`: bên trong có biến `lan = 0` và hàm `goi()` dùng `nonlocal lan` để tăng và in `Lan goi thu: <n>`, trả về `lan`. Gán `bo_dem = tao_bo_dem()` và gọi `bo_dem()` 3 lần.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Lan goi thu: 1
  Lan goi thu: 2
  Lan goi thu: 3
  ```
* **Gợi ý:** Biến `lan` "đóng gói" bên trong `tao_bo_dem` — nơi duy nhất sửa được là hàm `goi`.

### Bài 18: Game đoán số — tổng hợp global

* **Đề bài:** Khai báo global `diem = 0`. Viết hàm `choi_mot_van(dung_sai)` cộng 10 điểm nếu đúng, trừ 5 nếu sai (dùng `global`), trả về thông báo `Dung! +10 diem` hoặc `Sai! -5 diem`. Mô phỏng 1 ván đúng, 1 ván sai, 1 ván đúng và in điểm cuối.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Dung! +10 diem
  Sai! -5 diem
  Dung! +10 diem
  Diem cuoi: 15
  ```
* **Gợi ý:** Điểm cuối = 10 - 5 + 10 = 15.

### Bài 19: Nhiều hàm cùng chia sẻ biến — cảnh giác

* **Đề bài:** Khai báo `quy = 1000`. Viết hàm `nap(tien)` cộng vào quỹ và hàm `tieu(tien)` trừ khỏi quỹ (cả hai dùng `global`, `tieu` chặn khi tiền không đủ, trả về chuỗi báo lỗi). Gọi: `nap(500)`, `tieu(200)`, `tieu(2000)`. In `quy` sau mỗi lần.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Quy: 1500
  Quy: 1300
  Khong du tien!
  ```
* **Gợi ý:** Hai hàm cùng sửa một biến global — chú ý kiểm tra đủ tiền trước khi trừ.

### Bài 20: Dự đoán kết quả chương trình

* **Đề bài:** Đoán kết quả in ra của chương trình sau **trước khi chạy**, sau đó chạy để kiểm tra, ghi chú giải thích từng dòng bằng comment:

  ```python
  x = 1
  def f():
      y = 2
      def g():
          nonlocal y
          y += 1
          return y
      return g() + x
  print(f())
  print(x)
  ```
* **Output mong đợi:**
  ```
  4
  1
  ```
* **Gợi ý:** `g()` trả về `2 + 1 = 3`, `f()` trả về `3 + x(global) = 4`; `x` không bao giờ bị sửa nên vẫn `1`.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Phân biệt rõ biến local – global và cơ chế "gán trong hàm = tạo local".
* ✅ Dùng `global`, `nonlocal` đúng chỗ, hiểu vì sao hạn chế lạm dụng.
* ✅ Vận dụng LEGB để dự đoán chính xác kết quả chương trình.
* ✅ Viết hàm "sạch" theo nguyên tắc tham số vào – `return` ra.

> 💪 Chưa tự làm được bài nào thì đừng lo — hãy đọc lại bài giảng phần tương ứng rồi quay lại. **Phạm vi biến là kiến thức nền cho mọi bài sau!**

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 14: List](../14_List/bai_giang.md)**
