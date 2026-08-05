# 📝 Bài 6: Bài Tập – Toán Tử Trong Python

> 🎯 **Chủ đề:** Toán tử số học, gán kết hợp, so sánh, logic; thứ tự ưu tiên; tính tiền, chia đều, kiểm tra chẵn lẻ.

---

## 📌 Hướng dẫn làm bài

* Mỗi bài tập cần **tự viết code** rồi chạy thử trước khi xem đáp án.
* Sử dụng kiến thức bài 6 cùng biến và kiểu dữ liệu từ bài 4–5. Chưa cần `input()` — gán giá trị trực tiếp.
* Đáp án chi tiết 20 bài: 👉 [xem file dap_an.md](dap_an.md)

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Năm phép tính cơ bản

* **Đề bài:** In kết quả `8 + 2`, `8 - 2`, `8 * 2`, `8 / 2`, `8 ** 2`.
* **Input:** Không có.
* **Output:**
  ```
  10
  6
  16
  4.0
  64
  ```
* **Gợi ý:** `8 / 2` ra `4.0` — phép chia luôn cho số thực.

### Bài 2: Chia nguyên và chia dư

* **Đề bài:** In kết quả `17 // 5` và `17 % 5`.
* **Input:** Không có.
* **Output:**
  ```
  3
  2
  ```
* **Gợi ý:** `//` lấy phần nguyên, `%` lấy phần dư.

### Bài 3: Chia bánh cho bạn

* **Đề bài:** Có `banh = 30` chiếc bánh chia cho `10` học sinh. In mỗi bạn được bao nhiêu và còn thừa bao nhiêu.
* **Input:** Không có.
* **Output:**
  ```
  Moi ban: 3
  Con du: 0
  ```
* **Gợi ý:** `so_ban = banh // hoc_sinh`, `con_du = banh % hoc_sinh`.

### Bài 4: Bình phương và lập phương

* **Đề bài:** Biến `x = 5`. In ra `x²` và `x³`.
* **Input:** Không có.
* **Output:**
  ```
  25
  125
  ```
* **Gợi ý:** `print(x ** 2)` và `print(x ** 3)`.

### Bài 5: Cộng dồn bằng `+=`

* **Đề bài:** Biến `tong = 0`. Cộng dần `5`, `8`, `3` vào `tong` bằng toán tử `+=`. In kết quả cuối.
* **Input:** Không có.
* **Output:**
  ```
  16
  ```
* **Gợi ý:** `tong += 5`, rồi `tong += 8`, rồi `tong += 3`.

### Bài 6: Kiểm tra số lớn hơn

* **Đề bài:** `a = 15`, `b = 6`. In kết quả `a > b` và `a < b`.
* **Input:** Không có.
* **Output:**
  ```
  True
  False
  ```
* **Gợi ý:** Hai phép so sánh đơn — kết quả thuộc kiểu `bool`.

### Bài 7: Đại hay sai?

* **Đề bài:** In kết quả `5 == 5`, `5 == "5"`, `5 != 4`.
* **Input:** Không có.
* **Output:**
  ```
  True
  False
  True
  ```
* **Gợi ý:** `"5"` là chuỗi nên không bằng số 5.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Thứ tự ưu tiên

* **Đề bài:** In kết quả `2 + 3 * 4`, `(2 + 3) * 4`, `10 // 2 + 2`.
* **Input:** Không có.
* **Output:**
  ```
  14
  20
  7
  ```
* **Gợi ý:** Nhân chia trước, dấu ngoặc tính đầu tiên.

### Bài 9: Đổi nhiệt độ C sang F

* **Đề bài:** `do_c = 20.5`. Đổi sang độ F bằng công thức `F = C * 9 / 5 + 32`, in kết quả làm tròn 1 chữ số.
* **Input:** Không có.
* **Output:**
  ```
  68.9
  ```
* **Gợi ý:** `round(do_c * 9 / 5 + 32, 1)`.

### Bài 10: Sấp giảm giá quần áo

* **Đề bài:** Áo giá `gia_goc = 200000`, giảm 40%. Tính số tiền được giảm và giá phải trả, in hai dòng.
* **Input:** Không có.
* **Output:**
  ```
  Duoc giam: 80000.0
  Gia moi: 120000.0
  ```
* **Gợi ý:** `tien_giam = gia_goc * 0.4`; `gia_moi = gia_goc - tien_giam`.

### Bài 11: Tuổi teen không?

* **Đề bài:** `tuoi = 14`. Dùng `and` kiểm tra tuổi trong khoảng 13–19, in tên kết quả.
* **Input:** Không có.
* **Output:**
  ```
  La tuoi teen: True
  ```
* **Gợi ý:** `tuoi >= 13 and tuoi <= 19`.

### Bài 12: Điểm thưởng hay nhắc nhở?

* **Đề bài:** `diem = 7`. Kiểm tra: "được thưởng" khi `diem >= 8` **hoặc** `diem == 10`; "bị nhắc" khi `not (diem >= 5)`. In cả hai.
* **Input:** Không có.
* **Output:**
  ```
  Duoc thuong: False
  Bi nhac: False
  ```
* **Gợi ý:** dùng `or` cho câu thứ nhất, `not` cho câu thứ hai.

### Bài 13: Kiểm tra tính chia hết

* **Đề bài:** `so = 24`. Kiểm tra `so` có chia hết cho `3` và cho `5` không.
* **Input:** Không có.
* **Output:**
  ```
  Chia het cho 3: True
  Chia het cho 5: False
  ```
* **Gợi ý:** `so % 3 == 0` và `so % 5 == 0`.

### Bài 14: So sánh chuỗi ký tự

* **Đề bài:** In kết quả so sánh `"abc" < "abd"` và `"An" == "an"`.
* **Input:** Không có.
* **Output:**
  ```
  True
  False
  ```
* **Gợi ý:** chuỗi so theo thứ tự từ điển; phân biệt chữ hoa – chữ thường.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Hóa đơn quán ăn

* **Đề bài:** Đơn hàng gồm `pho = 50000`, `tra = 15000`, `banh = 20000`. Cộng dồn vào biến `tong` bằng `+=`. Thêm phí dịch vụ 10% của đơn. In tổng trước và sau phí.
* **Input:** Không có.
* **Output:**
  ```
  Tong: 85000
  Tong co phi dich vu: 93500.0
  ```
* **Gợi ý:** `tong += ...` từng món; rồi `tong + tong * 0.1` cho phần phí.

### Bài 16: Đổi tiền USD

* **Đề bài:** `so_vnd = 2350000`, `1 USD = 25000 VND`. Tính số USD: `so_usd = so_vnd / 25000`. In số USD (2 chữ số thập phân) và phần nguyên của nó.
* **Input:** Không có.
* **Output:**
  ```
  So USD: 94.00
  Phan nguyen: 94
  ```
* **Gợi ý:** `round(so_usd, 2)` và `int(so_usd)`.

### Bài 17: Kiểm tra năm nhuận

> **Quy tắc:** Năm nhuận khi chia hết cho 4, nhưng không chia hết cho 100 (trừ khi chia hết cho 400).

* **Đề bài:** Kiểm tra hai năm `2024` và `2025` có phải năm nhuận. Dùng công thức `nam % 4 == 0 and (nam % 100 != 0 or nam % 400 == 0)`.
* **Input:** Không có.
* **Output:**
  ```
  2024: True
  2025: False
  ```
* **Gợi ý:** Viết một hàm kiểm tra đơn giản hoặc lưu kết quả vào biến rồi in hai lần.

### Bài 18: Điểm trung bình có trọng số

* **Đề bài:** Toán hệ số 2, Văn hệ số 1: `diem_toan = 8`, `diem_van = 7`. Trung bình = `(diem_toan * 2 + diem_van) / 3`. In kết quả làm tròn 2 chữ số.
* **Input:** Không có.
* **Output:**
  ```
  7.67
  ```
* **Gợi ý:** Chú ý dấu ngoặc — cộng tất cả rồi mới chia.

### Bài 19: Tiền lãi kép 3 tháng

* **Đề bài:** Vay `tien = 1000000` với lãi suất `1.2%/tháng`. Mỗi tháng `tien` tăng thêm `tien * 0.012` (làm dần bằng toán tử `+=`). In số tiền sau từng tháng (không làm tròn).
* **Input:** Không có.
* **Output:**
  ```
  Sau thang 1: 1012000.0
  Sau thang 2: 1024144.0
  Sau thang 3: 1036433.728
  ```
* **Gợi ý:** Dùng vòng tính `tien += tien * 0.012` ba lần — hoặc lặp cập đầy đủ sau mỗi tháng (chưa cần vòng lặp, viết 3 lần).

### Bài 20: Kiểm tra con số "may mắn"

* **Đề bài:** `so = 28`. Viết và in kết quả 5 biểu thức (kèm nhãn), dùng kết hợp `and`/`or`/`not` và `%`:
  1. Là số chẵn **và** nhỏ hơn 30.
  2. Lớn hơn 20 **hoặc** chia hết cho 7.
  3. `not (so < 10)` — tức không nhỏ hơn 10.
  4. Chia hết cho 4.
  5. Chia hết cho 4 **và** (chia hết cho 2 **hoặc** lớn hơn 30).
* **Input:** Không có.
* **Output:**
  ```
  Cau 1: True
  Cau 2: True
  Cau 3: True
  Cau 4: True
  Cau 5: True
  ```
* **Gợi ý:** Viết từng biểu thức với dấu ngoặc đầy đủ; in nhãn "Cau i" trước mỗi kết quả.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Nắm trọn 7 toán tử số học, hiểu rõ `//`, `%`, `**`.
* ✅ Dùng **cấm `+=` để cộng dồn** gọn gàng.
* ✅ Kết hợp so sánh và logic `and`/`or`/`not`.
* ✅ Trả về `bool` từ mọi phép so sánh để giải bài toán thực tế.

> 💪 Toán tử là "nguyên liệu" của mọi tính toán. Càng luyện càng phản xạ. **Lập trình là luyện tập!**

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 7: Nhập Xuất Dữ Liệu](../07_Input_Output/bai_giang.md)**