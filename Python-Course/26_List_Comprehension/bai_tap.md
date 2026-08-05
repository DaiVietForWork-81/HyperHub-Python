# 📝 Bài 26: Bài Tập – List Comprehension

> 🎯 **Chủ đề:** Vòng lặp sinh danh sách một dòng: cú pháp cơ bản, bộ lọc `if`, `if/else`, lồng nhau, set/dict comprehension.

---

## 📌 Hướng dẫn làm bài

* Mỗi bài tập cần **tự viết code** rồi chạy thử trước khi xem đáp án.
* Nhớ phân biệt "if cuối" (lọc) và "if/else đầu" (chọn giá trị).
* Đáp án chi tiết 20 bài: 👉 [xem file dap_an.md](dap_an.md)

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Bình phương các số 0–9

* **Đề bài:** Dùng list comprehension tạo danh sách bình phương của các số `0, 1, 2, ..., 9` và in ra.
* **Input:** Không có.
* **Output:**
  ```
  [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
  ```
* **Gợi ý:** `[x * x for x in range(10)]`.

### Bài 2: Danh sách số chẵn 1–20

* **Đề bài:** Dùng comprehension lấy các số chẵn từ 1 đến 20 và in.
* **Input:** Không có.
* **Output:**
  ```
  [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
  ```
* **Gợi ý:** `[x for x in range(1, 21) if x % 2 == 0]`.

### Bài 3: Viết hoa tên học sinh

* **Đề bài:** Cho `ten = ["an", "binh", "cuong"]`. Dùng comprehension tạo danh sách các tên **viết hoa** và in.
* **Input:** Không có.
* **Output:**
  ```
  ['AN', 'BINH', 'CUONG']
  ```
* **Gợi ý:** `[t.upper() for t in ten]`.

### Bài 4: Nhân đôi và cộng thêm 1

* **Đề bài:** Cho `so = [1, 2, 3, 4]`. Tạo list mới mỗi phần tử bằng `x * 2 + 1` và in.
* **Input:** Không có.
* **Output:**
  ```
  [3, 5, 7, 9]
  ```
* **Gợi ý:** `[x * 2 + 1 for x in so]`.

### Bài 5: Chữ cái của một chuỗi

* **Đề bài:** Cho `tu = "python"`. Dùng comprehension tạo danh sách từng ký tự của chuỗi và in.
* **Input:** Không có.
* **Output:**
  ```
  ['p', 'y', 't', 'h', 'o', 'n']
  ```
* **Gợi ý:** duyệt `for c in tu` — chuỗi cũng là iterable.

### Bài 6: Số lớn hơn 10

* **Đề bài:** Cho `data = [3, 12, 7, 20, 1, 15]`. Lọc các số **lớn hơn 10** và in.
* **Input:** Không có.
* **Output:**
  ```
  [12, 20, 15]
  ```
* **Gợi ý:** `[x for x in data if x > 10]`.

### Bài 7: Độ dài từng tên

* **Đề bài:** Cho `ten = ["An", "Binh", "Cuong"]`. Tạo list chứa **độ dài** của mỗi tên và in.
* **Input:** Không có.
* **Output:**
  ```
  [2, 4, 5]
  ```
* **Gợi ý:** `[len(t) for t in ten]`.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Lọc chẵn rồi bình phương

* **Đề bài:** Cho `so = list(range(1, 11))`. Dùng comprehension lọc số chẵn rồi **bình phương** chúng, in kết quả.
* **Input:** Không có.
* **Output:**
  ```
  [4, 16, 36, 64, 100]
  ```
* **Gợi ý:** `[x * x for x in so if x % 2 == 0]`.

### Bài 9: Nhãn chẵn/lẻ (if/else)

* **Đề bài:** Cho `so = [1, 2, 3, 4, 5]`. Dùng if/else trong comprehension tạo list các chuỗi `"E"` (chẵn) hoặc `"O"` (lẻ) và in.
* **Input:** Không có.
* **Output:**
  ```
  ['O', 'E', 'O', 'E', 'O']
  ```
* **Gợi ý:** `["E" if x % 2 == 0 else "O" for x in so]`.

### Bài 10: Set comprehension – bình phương tập số

* **Đề bài:** Cho `so = [1, 2, 2, 3, 3, 4]`. Dùng set comprehension tạo tập bình phương của các số (không trùng) và in.
* **Input:** Không có.
* **Output:**
  ```
  {16, 1, 9, 4}
  ```
* **Gợi ý:** `{x * x for x in so}` — set tự loại trùng.

### Bài 11: Dict comprehension – khóa và bình phương

* **Đề bài:** Dùng dict comprehension tạo từ điển `{số: bình phương}` cho các số 1..5 và in.
* **Input:** Không có.
* **Output:**
  ```
  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
  ```
* **Gợi ý:** `{x: x * x for x in range(1, 6)}`.

### Bài 12: Bảng cửu chương nhân 5

* **Đề bài:** Dùng comprehension tạo danh sách các chuỗi `"5 x k = kq"` cho k = 1..10, in mỗi dòng một phép tính.
* **Input:** Không có.
* **Output:**
  ```
  5 x 1 = 5
  5 x 2 = 10
  ...
  5 x 10 = 50
  ```
* **Gợi ý:** `[f"5 x {k} = {5 * k}" for k in range(1, 11)]` rồi vòng lặp in.

### Bài 13: Đếm số chẵn bằng comprehension

* **Đề bài:** Cho `so = [3, 8, 12, 7, 20, 1, 24]`. Dùng comprehension + `len()` để **đếm số chẵn** và in ra số đếm.
* **Input:** Không có.
* **Output:**
  ```
  4
  ```
* **Gợi ý:** `len([x for x in so if x % 2 == 0])`.

### Bài 14: Làm phẳng ma trận (nested cơ bản)

* **Đề bài:** Cho `ma_tran = [[1, 2], [3, 4], [5, 6]]`. Dùng comprehension lồng nhau để gom tất cả phần tử thành **một list phẳng** và in.
* **Input:** Không có.
* **Output:**
  ```
  [1, 2, 3, 4, 5, 6]
  ```
* **Gợi ý:** `[x for hang in ma_tran for x in hang]` — vòng ngoài duyệt hàng, vòng trong duyệt phần tử.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Điểm trung bình lớp bằng comprehension

* **Đề bài:** Cho `diem = [8.5, 6.0, 9.0, 7.5]`. Dùng comprehension + `sum()` để tính trung bình cộng và in kết quả 2 chữ số thập phân.
* **Input:** Không có.
* **Output:**
  ```
  7.75
  ```
* **Gợi ý:** `sum([d for d in diem]) / len(diem)` — đơn giản hóa: `sum(diem) / len(diem)`, rồi `round(..., 2)`.

### Bài 16: Đếm tần suất chữ cái (dict comprehension)

* **Đề bài:** Cho `cau = "hoc hoc nua hoc mai"`. Dùng dict comprehension tạo từ điển đếm **số lần xuất hiện** mỗi chữ cái (bỏ khoảng trắng) và in từ điển.
* **Input:** Không có.
* **Output:** Ví dụ:
  ```
  {'h': 4, 'o': 4, 'c': 3, 'n': 1, 'u': 1, 'a': 2, 'm': 1, 'i': 1}
  ```
* **Gợi ý:** `{c: cau.count(c) for c in set(cau) if c != " "}`.

### Bài 17: Số chính phương nhỏ hơn 50

* **Đề bài:** Tìm tất cả **số chính phương** (n = x² với x nguyên) nhỏ hơn 50 bằng comprehension lồng nhau (duyệt x từ 0 đến 7) và in.
* **Input:** Không có.
* **Output:**
  ```
  [0, 1, 4, 9, 16, 25, 36, 49]
  ```
* **Gợi ý:** `[x * x for x in range(8) if x * x < 50]`.

### Bài 18: Phân loại điểm học sinh (if/else phức tạp)

* **Đề bài:** Cho `diem = [9.0, 5.5, 7.0, 3.5, 8.0]`. Dùng if/else trong comprehension tạo list nhãn: `"Gioi"` (≥8), `"Kha"` (≥6.5), `"TB"` (còn lại) và in.
* **Input:** Không có.
* **Output:**
  ```
  ['Gioi', 'TB', 'Kha', 'TB', 'Gioi']
  ```
* **Gợi ý:** cần if/elif/else — viết bằng cách **lồng**: `"Gioi" if d >= 8 else ("Kha" if d >= 6.5 else "TB")`.

### Bài 19: Lọc sản phẩm theo giá + tổng

* **Đề bài:** Cho giá sản phẩm `gia = [50000, 120000, 30000, 250000, 80000]`. Dùng comprehension lọc những sản phẩm **giá trên 60000**, tính tổng chúng và in tổng.
* **Input:** Không có.
* **Output:**
  ```
  450000
  ```
* **Gợi ý:** `sum([g for g in gia if g > 60000])` → 120000 + 250000 + 80000.

### Bài 20: Bảng điểm chi tiết (tổng hợp)

* **Đề bài:** Cho danh sách tuple `(tên, điểm)`: `[("An", 8.5), ("Binh", 4.0), ("Cuong", 9.0), ("Dung", 6.5)]`. Viết chương trình: (1) danh sách tên học sinh đậu (điểm ≥ 5) bằng comprehension, (2) điểm cao nhất bằng `max`, (3) in kết quả.
* **Input:** Không có.
* **Output:**
  ```
  Hoc sinh dau: ['An', 'Cuong', 'Dung']
  Diem cao nhat: 9.0
  ```
* **Gợi ý:** `[hs[0] for hs in lop if hs[1] >= 5]` và `max(lop, key=lambda hs: hs[1])[1]`.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Viết thành thạo comprehension cơ bản, bộ lọc `if`, `if/else`.
* ✅ Làm quen set/dict comprehension và nested.
* ✅ Kết hợp comprehension với `sum`, `len`, `max` để xử lý dữ liệu thực tế.

> 💪 Chưa tự làm được bài nào thì đừng lo — hãy xem lại bài giảng rồi quay lại. **Lập trình là luyện tập!**

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 27: Generator](../27_Generator/bai_giang.md)**
