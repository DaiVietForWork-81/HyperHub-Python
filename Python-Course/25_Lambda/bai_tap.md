# 📝 Bài 25: Bài Tập – Lambda

> 🎯 **Chủ đề:** Hàm vô danh `lambda` với `sorted(key=...)`, `filter`, `map`.

---

## 📌 Hướng dẫn làm bài

* Mỗi bài tập cần **tự viết code** rồi chạy thử trước khi xem đáp án.
* Nhớ `list(...)` quanh kết quả `filter`/`map` khi in danh sách.
* Đáp án chi tiết 20 bài: 👉 [xem file dap_an.md](dap_an.md)

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Lambda cộng hai số

* **Đề bài:** Viết lambda nhận 2 số `a`, `b` trả về tổng. Gán vào biến `cong` rồi in kết quả `cong(3, 7)`.
* **Input:** Không có.
* **Output:**
  ```
  10
  ```
* **Gợi ý:** `cong = lambda a, b: a + b`; gọi `print(cong(3, 7))`.

### Bài 2: Lambda bình phương

* **Đề bài:** Viết lambda nhận `x` trả về `x * x`. Gán vào biến `bp` và in `bp(6)`.
* **Input:** Không có.
* **Output:**
  ```
  36
  ```
* **Gợi ý:** `bp = lambda x: x * x`.

### Bài 3: Lambda nhân đôi

* **Đề bài:** Viết lambda nhận `x` trả về `x * 2`, dùng `map` để nhân đôi danh sách `[1, 2, 3, 4]` và in kết quả.
* **Input:** Không có.
* **Output:**
  ```
  [2, 4, 6, 8]
  ```
* **Gợi ý:** `list(map(lambda x: x * 2, [1, 2, 3, 4]))`.

### Bài 4: Lambda trả về số lớn hơn

* **Đề bài:** Dùng `max` với `key=lambda` để tìm chuỗi **dài nhất** trong `["an", "binh", "cuong"]` rồi in ra.
* **Input:** Không có.
* **Output:**
  ```
  cuong
  ```
* **Gợi ý:** `max(danh_sach, key=lambda s: len(s))`.

### Bài 5: Sắp xếp số tăng dần

* **Đề bài:** Dùng `sorted` với `key=lambda x: x` để sắp xếp `[5, 2, 8, 1, 9]` tăng dần và in kết quả.
* **Input:** Không có.
* **Output:**
  ```
  [1, 2, 5, 8, 9]
  ```
* **Gợi ý:** `sorted(so, key=lambda x: x)` — key trả về chính giá trị so sánh.

### Bài 6: Sắp xếp theo độ dài

* **Đề bài:** Danh sách tên `["An", "Binh", "Cuong", "D"]`. Dùng `sorted` với `key=lambda ten: len(ten)` để sắp theo độ dài tăng dần và in ra.
* **Input:** Không có.
* **Output:**
  ```
  ['D', 'An', 'Binh', 'Cuong']
  ```
* **Gợi ý:** `sorted(ten, key=lambda s: len(s))`.

### Bài 7: Lọc số chẵn bằng filter

* **Đề bài:** Dùng `filter` + lambda lọc từng số chẵn trong `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` và in danh sách kết quả.
* **Input:** Không có.
* **Output:**
  ```
  [2, 4, 6, 8, 10]
  ```
* **Gợi ý:** `list(filter(lambda x: x % 2 == 0, so))`.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Sắp xếp học sinh theo điểm (tuplet)

* **Đề bài:** Danh sách `[("An", 8.5), ("Binh", 5.0), ("Cuong", 9.5)]`. Sắp giảm dần theo điểm và in danh sách kết quả.
* **Input:** Không có.
* **Output:**
  ```
  [('Cuong', 9.5), ('An', 8.5), ('Binh', 5.0)]
  ```
* **Gợi ý:** `sorted(ten, key=lambda hs: hs[1], reverse=True)` — điểm ở vị trí số 1.

### Bài 9: Lọc người trên 18 tuổi

* **Đề bài:** Danh sách `[("An", 17), ("Binh", 19), ("Cuong", 20), ("Dung", 15)]`. Dùng `filter` lọc những người từ 18 tuổi trở lên và in kết quả.
* **Input:** Không có.
* **Output:**
  ```
  [('Binh', 19), ('Cuong', 20)]
  ```
* **Gợi ý:** `list(filter(lambda ng: ng[1] >= 18, nguoi))`.

### Bài 10: Map đổi khối lượng.

* **Đề bài:** Danh sách giá USD `[10, 25, 50]`. Dùng `map` + lambda đổi sang VND (1 USD = 25000 VND) và in.
* **Input:** Không có.
* **Output:**
  ```
  [250000, 625000, 1250000]
  ```
* **Gợi ý:** `list(map(lambda usd: usd * 25000, gia_usd))`.

### Bài 11: Tên viết hoa toàn bộ

* **Đề bài:** Danh sách `["an", "binh", "cuong"]`. Dùng `map` + lambda viết hoa tất cả ký tự của mỗi tên và in.
* **Input:** Không có.
* **Output:**
  ```
  ['AN', 'BINH', 'CUONG']
  ```
* **Gợi ý:** `list(map(lambda s: s.upper(), ten))`.

### Bài 12: Tìm sinh viên điểm cao nhất

* **Đề bài:** Danh sách `[("An", 8.5), ("Binh", 5.0), ("Cuong", 9.5)]`. Dùng `max` + `key=lambda` in tên sinh viên có điểm cao nhất.
* **Input:** Không có.
* **Output:**
  ```
  Cuong 9.5
  ```
* **Gợi ý:** `max(danh_sach, key=lambda sv: sv[1])` rồi in tên và điểm.

### Bài 13: Lọc số chia hết cho 3

* **Đề bài:** Dùng `filter` + lambda lọc các số **chia hết cho 3** trong `[1, 2, 3, ..., 20]` và in.
* **Input:** Không có.
* **Output:**
  ```
  [3, 6, 9, 12, 15, 18]
  ```
* **Gợi ý:** `list(filter(lambda x: x % 3 == 0, so))`.

### Bài 14: Sắp xếp tên theo ký tự cuối

* **Đề bài:** Danh sách `["banana", "apple", "cherry", "date"]`. Sắp xếp theo **ký tự cuối** của mỗi chuỗi (dùng lambda lấy `s[-1]`) và in.
* **Input:** Không có.
* **Output:**
  ```
  ['banana', 'apple', 'cherry', 'date']
  ```
  (chỉ cần đúng thứ tự theo chữ cái cuối: a → e → y, hãy tự kiểm tra)
* **Gợi ý:** `sorted(qua, key=lambda s: s[-1])`.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Lọc chẵn rồi bình phương

* **Đề bài:** Danh sách `[1..10]`. Dùng `filter` lấy số chẵn, rồi `map` bình phương chúng vào `list` và in.
* **Input:** Không có.
* **Output:**
  ```
  [4, 16, 36, 64, 100]
  ```
* **Gợi ý:** `list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, so)))`.

### Bài 16: Điểm chuẩn thí sinh

* **Đề bài:** Danh sách thí sinh `[("An", 9.0), ("Binh", 4.5), ("Cuong", 7.0), ("Dung", 6.0)]`. Với điểm chuẩn 6.0: lọc những người đậu rồi sắp giảm dần thei theo điểm. In danh sách kết quả.
* **Input:** Không có.
* **Output:**
  ```
  [('An', 9.0), ('Cuong', 7.0), ('Dung', 6.0)]
  ```
* **Gợi ý:** filter `ts[1] >= 6` rồi `sorted(..., reverse=True)` theo điểm.

### Bài 17: Giá sau giảm giá

* **Đề bài:** Danh sách giá sản phẩm `[100000, 200000, 500000]`. Dùng `map` + lambda tính giá sau khi **giảm 20%** (tức giữ 80%) và in.
* **Input:** Không có.
* **Output:**
  ```
  [80000.0, 160000.0, 400000.0]
  ```
* **Gợi ý:** `lambda gia: gia * 0.8`.

### Bài 18: Sắp xếp thời khóa biểu theo giờ

* **Đề bài:** Danh sách `[("Toan", 7), ("Van", 10), ("Ly", 8), ("Anh", 9)]` — (môn, giờ bắt đầu). Sắp liệt kê theo thứ tự giờ tăng dần và in danh sách kết quả.
* **Input:** Không có.
* **Output:**
  ```
  [('Toan', 7), ('Ly', 8), ('Anh', 9), ('Van', 10)]
  ```
* **Gợi ý:** `sorted(lich, key=lambda mon: mon[1])` — lấy phần tử vị trí 1 (giờ) làm chìa khóa.

### Bài 19: Lọc + tìm max chia hết cho 5

* **Đề bài:** Danh sách số `[12, 7, 25, 33, 40, 15]`. Dùng lambda để tìm **số lớn nhất chia hết cho 5** trong danh sách và in kết quả.
* **Input:** Không có.
* **Output:**
  ```
  40
  ```
* **Gợi ý:** `filter(lambda x: x % 5 == 0, so)` lọc các số chia hết cho 5, rồi `max(...)` trong đó để tìm lớn nhất.

### Bài 20: Xếp hạng giảm dần + tổng lương

* **Đề bài:** Có 2 việc: (1) Danh sách học sinh `[("An", 8.5), ("Binh", 6.0), ("Cuong", 9.0)]` — sắp giảm dần theo điểm và in mỗi người kèm thứ hạng `1. Cuong - 9.0`. (2) Danh sách nhân viên `[("Minh", 5000), ("Lan", 8000), ("Thai", 6000)]` — in tổng lương cả công ty.
* **Input:** Không có.
* **Output:**
  ```
  1. Cuong - 9.0
  2. An - 8.5
  3. Binh - 6.0
  Tong luong: 19000
  ```
* **Gợi ý:** `sorted(..., reverse=True)` + `enumerate(..., start=1)` cho phần 1; `sum(map(lambda nv: nv[1], nhan_vien))` cho phần 2.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Viết thành thạo `lambda tham_so: biểu_thức`.
* ✅ Sắp xếp dữ liệu với `sorted(key=lambda ...)`.
* ✅ Lọc và biến đổi dữ liệu với `filter` + `map`.
* ✅ Kết hợp nhiều lambda để giải bài toán thực tế (điểm, thời khóa biểu, lương).

> 💪 Chưa tự làm được bài nào thì đừng lo — hãy xem lại bài giảng rồi quay lại. **Lập trình là luyện tập!**

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 26: List Comprehension](../26_List_Comprehension/bai_giang.md)**