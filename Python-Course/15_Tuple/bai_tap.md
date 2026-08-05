# 📝 Bài 15: Bài Tập – Tuple (Bộ Dữ Liệu)

> 🎯 **Chủ đề:** Tạo tuple, tính bất biến, truy cập, duyệt, unpacking (hoán đổi biến), count/index và so sánh với list.

---

## 📌 Hướng dẫn làm bài

* Mỗi bài tập cần **tự viết code** rồi chạy thử trước khi xem đáp án.
* Nếu chưa nhớ lý thuyết, hãy xem lại [bài giảng 15](bai_giang.md).
* Đáp án chi tiết 20 bài: 👉 [xem file dap_an.md](dap_an.md)

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Tạo tuple đầu tiên

* **Đề bài:** Tạo tuple `so` chứa `(10, 20, 30)` và in ra: phần tử đầu tiên và phần tử cuối cùng.
* **Input:** Không có.
* **Output:**
  ```
  10
  30
  ```
* **Gợi ý:** Truy cập bằng `so[0]` và `so[-1]`.

### Bài 2: In toàn bộ tuple

* **Đề bài:** Cho `mon = ("Toan", "Van", "Anh")`. Dùng vòng lặp in từng môn trên một dòng.
* **Input:** Không có.
* **Output:**
  ```
  Toan
  Van
  Anh
  ```
* **Gợi ý:** `for m in mon: print(m)`.

### Bài 3: Tuple một phần tử

* **Đề bài:** Tạo một **tuple** chứa đúng 1 phần tử là số `7` (không được tạo thành số `7`), rồi in `type()` của nó ra màn hình.
* **Input:** Không có.
* **Output:**
  ```
  <class 'tuple'>
  ```
* **Gợi ý:** Nhớ dấu phẩy đuôi: `(7,)`.

### Bài 4: Đếm và tìm vị trí

* **Đề bài:** Cho `diem = (9, 7, 9, 8, 9)`. In ra số lần xuất hiện của `9` và vị trí đầu tiên của `8`.
* **Input:** Không có.
* **Output:**
  ```
  3
  3
  ```
* **Gợi ý:** `diem.count(9)` và `diem.index(8)`.

### Bài 5: Kiểm tra phần tử

* **Đề bài:** Cho `trai_cay = ("tao", "chuoi", "cam")`. Kiểm tra xem `"tao"` có trong tuple không và `"xoai"` có trong tuple không, in cả hai kết quả.
* **Input:** Không có.
* **Output:**
  ```
  True
  False
  ```
* **Gợi ý:** Dùng toán tử `in`.

### Bài 6: Độ dài và tổng

* **Đề bài:** Cho `so = (4, 8, 15, 16, 23, 42)`. In ra số phần tử và tổng của tuple.
* **Input:** Không có.
* **Output:**
  ```
  6
  108
  ```
* **Gợi ý:** `len(so)` và `sum(so)`.

### Bài 7: Truy cập ngược từ cuối

* **Đề bài:** Cho `ngay = ("T2", "T3", "T4", "T5", "T6")`. In ra phần tử ở chỉ số âm `-2` và `-1`.
* **Input:** Không có.
* **Output:**
  ```
  T5
  T6
  ```
* **Gợi ý:** Index âm đếm từ cuối lên, `-1` là phần tử cuối.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Hoán đổi hai biến

* **Đề bài:** Cho `a = 5`, `b = 10`. Dùng kỹ thuật **unpacking tuple** để hoán đổi giá trị hai biến rồi in ra.
* **Input:** Không có.
* **Output:**
  ```
  a = 10, b = 5
  ```
* **Gợi ý:** `a, b = b, a`.

### Bài 9: Giải nén tọa độ

* **Đề bài:** Cho tuple `toa_do = (21.03, 105.85)`. Giải nén vào hai biến `vi_do` và `kinh_do` rồi in ra.
* **Input:** Không có.
* **Output:**
  ```
  Vi do: 21.03
  Kinh do: 105.85
  ```
* **Gợi ý:** `vi_do, kinh_do = toa_do`.

### Bài 10: Unpacking trong vòng lặp

* **Đề bài:** Cho list chứa các tuple 2 phần tử `ds = [("An", 8), ("Binh", 9)]`. Dùng vòng lặp giải nén để in ra `"An: 8 diem"` dạng tương tự.
* **Input:** Không có.
* **Output:**
  ```
  An: 8 diem
  Binh: 9 diem
  ```
* **Gợi ý:** `for ten, diem in ds:`.

### Bài 11: Cắt slice tuple

* **Đề bài:** Cho `so = (10, 20, 30, 40, 50, 60)`. In ra 3 phần tử đầu và đảo ngược toàn bộ tuple bằng slice.
* **Input:** Không có.
* **Output:**
  ```
  (10, 20, 30)
  (60, 50, 40, 30, 20, 10)
  ```
* **Gợi ý:** `so[:3]` và `so[::-1]`.

### Bài 12: Chuyển đổi list ↔ tuple

* **Đề bài:** Cho `tu = ("trung", "sua", "banh")`. Chuyển tuple thành list, thêm `"pho mai"` vào list, rồi chuyển lại thành tuple và in ra.
* **Input:** Không có.
* **Output:**
  ```
  ('trung', 'sua', 'banh', 'pho mai')
  ```
* **Gợi ý:** `list(tu)`, `append`, rồi `tuple(...)`.

### Bài 13: Trả về nhiều giá trị từ hàm

* **Đề bài:** Viết hàm `tinh_hcn(dai, rong)` trả về **tuple** `(dien_tich, chu_vi)` của hình chữ nhật. Dùng hàm với `dai = 5, rong = 3` và in cả hai kết quả.
* **Input:** Không có.
* **Output:**
  ```
  Dien tich: 15
  Chu vi: 16
  ```
* **Gợi ý:** Hàm dùng `return (dai * rong, (dai + rong) * 2)` rồi gán `d, c = tinh_hcn(5, 3)`.

### Bài 14: Điểm trung bình của tuple

* **Đề bài:** Cho `diem = (8, 9, 7, 6)`. Tính trung bình cộng (làm tròn 2 chữ số), điểm cao nhất và thấp nhất.
* **Input:** Không có.
* **Output:**
  ```
  Trung binh: 7.5
  Cao nhat: 9
  Thap nhat: 6
  ```
* **Gợi ý:** `sum`, `len`, `max`, `min` đều dùng được với tuple.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Bảo vệ dữ liệu khỏi sửa đổi

* **Đề bài:** Tạo tuple `cau_hinh = ("admin", 8080, "localhost")`. Viết chương trình chứng minh rằng **không thể gán giá trị** `cau_hinh[0] = "user"` — hãy bắt lỗi `TypeError` bằng `try...except` và in ra dòng thông báo.
* **Input:** Không có.
* **Output:**
  ```
  Loi: khong the sua doi tuple
  ```
* **Gợi ý:** Nhớ kiến thức ngoại lệ cơ bản: `try: ... except TypeError: ...`. Chỗ gán sai phải nằm trong `try`.

### Bài 16: Tìm phần tử lớn nhất (không dùng max)

* **Đề bài:** Cho `so = (12, 5, 27, 8, 19)`. Viết chương trình tìm và in ra **phần tử lớn nhất** của tuple **không dùng hàm `max`**, cùng vị trí (index) của nó.
* **Input:** Không có.
* **Output:**
  ```
  Lon nhat: 27
  Vi tri: 2
  ```
* **Gợi ý:** Duyệt bằng `enumerate`, giữ lại `gia_tri_max` và vị trí mỗi khi gặp giá trị lớn hơn.

### Bài 17: Đếm số ngày trong các tháng

* **Đề bài:** Tạo tuple `so_ngay = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)` cho 12 tháng. Với một danh sách tháng cần kiểm tra `[2, 4, 6]`, in ra tên tháng (kiểu `"Thang 2"`) và số ngày tương ứng.
* **Input:** Không có.
* **Output:**
  ```
  Thang 2: 28 ngay
  Thang 4: 30 ngay
  Thang 6: 30 ngay
  ```
* **Gợi ý:** `so_ngay[thang - 1]` vì index bắt đầu từ 0.

### Bài 18: Điểm của 3 giám khảo — bỏ điểm cao, thấp nhất

* **Đề bài:** Cho tuple điểm `(8.0, 9.5, 7.0, 9.5, 8.5)` của 5 giám khảo. Tính **điểm chung** theo quy tắc thi về nghệ thuật: bỏ **1 điểm cao nhất và 1 điểm thấp nhất**, rồi lấy trung bình các điểm còn lại (làm tròn 2 chữ số).
* **Input:** Không có.
* **Output:**
  ```
  Diem chung: 8.67
  ```
* **Gợi ý:** Chuyển tuple sang list để dùng `sort`; bỏ phần tử đầu và cuối sau khi sắp xếp, rồi tính trung bình phần còn lại.

### Bài 19: Sắp xếp tuple bằng vòng lặp (bubble sort)

* **Đề bài:** Cho tuple `so = (5, 2, 9, 1, 7)`. Viết chương trình **sắp xếp tăng dần NHẤT THIẾT không dùng `sorted`**: chuyển tuple sang list, dùng thuật toán sắp xếp nổi bọt (lặp so sánh hai phần tử liền kề và hoán đổi bằng tuple), rồi in ra list đã sắp xếp.
* **Input:** Không có.
* **Output:**
  ```
  [1, 2, 5, 7, 9]
  ```
* **Gợi ý:** Vòng lặp lồng nhau: vòng ngoài `n-1` lượt, vòng trong so sánh `ds[j]` với `ds[j+1]`, hoán đổi bằng `ds[j], ds[j+1] = ds[j+1], ds[j]` khi sai thứ tự.

### Bài 20: Quản lý kho cố định

* **Đề bài:** Cho tuple `kho = (("gao", 100), ("trung", 50), ("sua", 30))` — mỗi phần tử là tuple `(ten, so_luong)`. Viết chương trình:
  1. In ra tổng số mặt hàng.
  2. In ra tổng số lượng hàng (cộng tất cả `so_luong`).
  3. Kiểm tra và in ra `"SAP HET"` nếu có mặt hàng nào `so_luong < 40`, ngược lại in `"DU HANG"`.
* **Input:** Không có.
* **Output:**
  ```
  So mat hang: 3
  Tong so luong: 180
  SAP HET (trung)
  ```
* **Gợi ý:** Duyệt bằng `for ten, sl in kho:` — unpacking tuple lồng. Cộng dồn `sl`; kiểm tra `sl < 40` để in cảnh báo.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Tạo và truy cập tuple thuần thục.
* ✅ Dùng unpacking — từ hoán đổi biến đến trả về nhiều giá trị.
* ✅ Nhận diện tính bất biến và bảo vệ dữ liệu với tuple.
* ✅ Biết khi nào chọn tuple thay vì list.

> 💪 Nếu bài nào chưa tự làm được, hãy xem lại [bài giảng 15](bai_giang.md) rồi thử lại. **Lập trình là luyện tập!**

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 16: Set (Tập hợp)](../16_Set/bai_giang.md)**