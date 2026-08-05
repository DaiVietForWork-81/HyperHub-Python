# 📝 Bài 24: Bài Tập – Dataclass

> 🎯 **Chủ đề:** Tạo class chứa dữ liệu tự động với `@dataclass` — giá trị mặc định, `field(default_factory=list)`, `frozen=True`.

---

## 📌 Hướng dẫn làm bài

* Mỗi bài tập cần **tự viết code** rồi chạy thử trước khi xem đáp án.
* Nhớ import: `from dataclasses import dataclass` (và `field` khi cần).
* Đáp án chi tiết 20 bài: 👉 [xem file dap_an.md](dap_an.md)

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Dataclass Sản phẩm đầu tiên

* **Đề bài:** Tạo dataclass `SanPham` có 2 trường `ten` (str) và `gia` (float). Tạo sản phẩm `"Bút bi"` giá `5000` rồi in đối tượng ra màn hình.
* **Input:** Không có.
* **Output:**
  ```
  SanPham(ten='Bút bi', gia=5000.0)
  ```
* **Gợi ý:** Dùng `@dataclass` + khai báo trường kèm kiểu; `print(sp)` hiển thị nhờ `__repr__` tự sinh.

### Bài 2: Học sinh và lớp

* **Đề bài:** Tạo dataclass `HocSinh` có trường `ten` (str) và `lop` (str). Tạo 2 học sinh `"An"` lớp `"10A1"`, `"Bình"` lớp `"10A2"` và in lần lượt từng học sinh.
* **Input:** Không có.
* **Output:**
  ```
  HocSinh(ten='An', lop='10A1')
  HocSinh(ten='Bình', lop='10A2')
  ```
* **Gợi ý:** Mỗi đối tượng một `print()`, thứ tự tham số đúng thứ tự khai báo.

### Bài 3: Truy cập thuộc tính sách

* **Đề bài:** Tạo dataclass `Sach` gồm `tua` (str) và `tac_gia` (str). Tạo sách `"Đắc Nhân Tâm"` của `"Dale Carnegie"`, sau đó in riêng tên sách và tác giả bằng cách truy cập thuộc tính.
* **Input:** Không có.
* **Output:**
  ```
  Tua: Đắc Nhân Tâm
  Tac gia: Dale Carnegie
  ```
* **Gợi ý:** Dùng `s.tua`, `s.tac_gia` như thuộc tính class thường.

### Bài 4: Xe có màu mặc định

* **Đề bài:** Tạo dataclass `Xe` gồm `ten` (str) và `mau` (str, **mặc định** `"Trắng"`). Tạo xe `"Honda Vision"` không truyền màu, in ra; rồi tạo xe `"Sirius"` màu `"Đỏ"`, in ra.
* **Input:** Không có.
* **Output:**
  ```
  Xe(ten='Honda Vision', mau='Trắng')
  Xe(ten='Sirius', mau='Đỏ')
  ```
* **Gợi ý:** Trường có mặc định đứng sau trường bắt buộc; không truyền thì lấy mặc định.

### Bài 5: Điểm thi hai môn

* **Đề bài:** Tạo dataclass `Diem` có 2 trường `toan` (float), `van` (float). Tạo đối tượng `Diem(9.0, 8.0)` và in tổng điểm ra màn hình dạng: `Tong diem: 17.0`.
* **Input:** Không có.
* **Output:**
  ```
  Tong diem: 17.0
  ```
* **Gợi ý:** `d.toan + d.van` — truy cập như thuộc tính bình thường.

### Bài 6: So sánh hai sản phẩm

* **Đề bài:** Tạo dataclass `SanPham` (ten, gia). Tạo `sp1 = SanPham("Chuột", 200000)` và `sp2 = SanPham("Chuột", 200000)`, `sp3 = SanPham("Bàn phím", 350000)`. In kết quả `sp1 == sp2` và `sp1 == sp3`.
* **Input:** Không có.
* **Output:**
  ```
  True
  False
  ```
* **Gợi ý:** Dataclass tự sinh `__eq__` — so giá trị từng trường.

### Bài 7: Danh sách môn học trống

* **Đề bài:** Tạo dataclass `HocSinh` gồm `ten` (str) và `mon_hoc` (list) với `field(default_factory=list)`. Tạo học sinh `"An"` và in ra.
* **Input:** Không có.
* **Output:**
  ```
  HocSinh(ten='An', mon_hoc=[])
  ```
* **Gợi ý:** Nhớ `from dataclasses import field`; không gán `= []` trực tiếp.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Danh sách học sinh trong lớp

* **Đề bài:** Tạo dataclass `LopHoc` gồm `ten` (str) và `hoc_sinh` (list, `field(default_factory=list)`). Tạo lớp `"10A1"`, thêm `"An"`, `"Bình"`, `"Cường"` vào `hoc_sinh` rồi in lớp ra.
* **Input:** Không có.
* **Output:**
  ```
  LopHoc(ten='10A1', hoc_sinh=['An', 'Bình', 'Cường'])
  ```
* **Gợi ý:** Dùng `lop.hoc_sinh.append(...)` để thêm từng người.

### Bài 9: In toàn bộ sản phẩm

* **Đề bài:** Tạo dataclass `SanPham` (ten, gia). Tạo danh sách 3 sản phẩm (Laptop 15 triệu, Chuột 200k, Bàn phím 350k) rồi dùng vòng lặp `for` in từng sản phẩm.
* **Input:** Không có.
* **Output:**
  ```
  SanPham(ten='Laptop', gia=15000000.0)
  SanPham(ten='Chuột', gia=200000.0)
  SanPham(ten='Bàn phím', gia=350000.0)
  ```
* **Gợi ý:** `for sp in danh_sach: print(sp)`.

### Bài 10: Sản phẩm đắt nhất

* **Đề bài:** Dùng dataclass `SanPham` (ten, gia) với danh sách 4 sản phẩm bất kỳ. Tìm và in sản phẩm **có giá cao nhất**.
* **Input:** Không có.
* **Output:**
  ```
  Sản phẩm đắt nhất: SanPham(ten='Laptop', gia=15000000.0)
  ```
* **Gợi ý:** Dùng `max(danh_sach, key=lambda sp: sp.gia)` — lambda học ở bài 25, hoặc tự duyệt so sánh.

### Bài 11: Học sinh đạt học bổng

* **Đề bài:** Tạo dataclass `HocSinh` gồm `ten` (str) và `diem` (float). Cho danh sách 5 học sinh, in ra những học sinh có **điểm từ 8.0 trở lên** (đủ điều kiện học bổng).
* **Input:** Không có.
* **Output:** Ví dụ:
  ```
  An 8.5
  Cường 9.0
  ```
* **Gợi ý:** Duyệt `for`, kiểm tra `if hs.diem >= 8`.

### Bài 12: Phương thức tính trung bình

* **Đề bài:** Tạo dataclass `HocSinh` gồm `ten` (str), `diem_toan` (float), `diem_van` (float) kèm phương thức `trung_binh()` trả về trung bình cộng 2 môn. Tạo học sinh `"An"` (9.0, 7.0) và in kết quả `An co diem trung binh: 8.0`.
* **Input:** Không có.
* **Output:**
  ```
  An co diem trung binh: 8.0
  ```
* **Gợi ý:** Phương thức viết trong class như bình thường: `return (self.diem_toan + self.diem_van) / 2`.

### Bài 13: Thống kê sản phẩm rẻ

* **Đề bài:** Dataclass `SanPham` (ten, gia). Cho danh sách 5 sản phẩm, đếm xem có **bao nhiêu sản phẩm giá dưới 100.000 đồng** và in kết quả.
* **Input:** Không có.
* **Output:** Ví dụ:
  ```
  So san pham re (duoi 100000): 3
  ```
* **Gợi ý:** Đếm bằng biến `dem`, tăng khi `sp.gia < 100000`.

### Bài 14: Sắp xếp sản phẩm theo giá

* **Đề bài:** Dataclass `SanPham` (ten, gia). Cho danh sách 4 sản phẩm, in danh sách **sau khi sắp xếp tăng dần theo giá** (mỗi sản phẩm một dòng).
* **Input:** Không có.
* **Output:** Ví dụ:
  ```
  SanPham(ten='Chuột', gia=200000.0)
  SanPham(ten='Bàn phím', gia=350000.0)
  ```
* **Gợi ý:** `sorted(danh_sach, key=lambda sp: sp.gia)` rồi duyệt in.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Điểm thi bất biến

* **Đề bài:** Tạo dataclass `DiemThi` với `frozen=True`, gồm `mon` (str) và `diem` (float). Tạo điểm thi Toán 9.5, in ra; cố gắng sửa `diem` thành 10 và **bắt lỗi** để in ra thông báo `Khong the sua diem thi!`.
* **Input:** Không có.
* **Output:**
  ```
  DiemThi(mon='Toan', diem=9.5)
  Khong the sua diem thi!
  ```
* **Gợi ý:** Bọc phép gán trong `try...except FrozenInstanceError` (nhập từ `dataclasses`).

### Bài 16: Quản lý cửa hàng mini

* **Đề bài:** Tạo dataclass `SanPham` (ten, gia, `so_luong` int = 0) có phương thức `gia_tri()` trả về `gia * so_luong`. Tạo 3 sản phẩm với số lượng khác nhau, in tổng giá trị kho.
* **Input:** Không có.
* **Output:**
  ```
  Tong gia tri kho: 12300000.0
  ```
* **Gợi ý:** Cộng dồn `sp.gia_tri()` trong vòng lặp.

### Bài 17: Học sinh và danh sách điểm

* **Đề bài:** Tạo dataclass `HocSinh` gồm `ten` (str) và `diem` (list, `field(default_factory=list)`) kèm phương thức `trung_binh()` tính trung bình các điểm trong list. Học sinh `"An"` có điểm `[8, 9, 10]` — in ra trung bình 2 chữ số thập phân.
* **Input:** Không có.
* **Output:**
  ```
  Trung binh cua An: 9.0
  ```
* **Gợi ý:** `sum(self.diem) / len(self.diem)`; dùng `round(..., 2)` nếu cần.

### Bài 18: Bảng xếp hạng học sinh

* **Đề bài:** Dataclass `HocSinh` (ten, diem). Cho danh sách 5 học sinh, in **bảng xếp hạng giảm dần theo điểm** kèm thứ hạng (1, 2, 3...). Ví dụ: `1. An - 9.0`.
* **Input:** Không có.
* **Output:** Ví dụ:
  ```
  1. Cường - 9.0
  2. An - 8.5
  3. Bình - 6.0
  ```
* **Gợi ý:** Sắp xếp `reverse=True` rồi dùng vòng lặp `enumerate(danh_sach, start=1)`.

### Bài 19: Giảm giá thông minh

* **Đề bài:** Dataclass `SanPham` (ten, gia) có phương thức `giam_gia(phan_tram)` làm giảm `gia` đi `phan_tram`%. Tạo sản phẩm `"Áo thun"` giá 200000, giảm 25%, in giá mới và in đối tượng sau khi giảm.
* **Input:** Không có.
* **Output:**
  ```
  Gia moi: 150000.0
  SanPham(ten='Áo thun', gia=150000.0)
  ```
* **Gợi ý:** `self.gia = self.gia * (1 - phan_tram / 100)`; phương thức không cần trả về gì.

### Bài 20: Chương trình thống kê kho hàng

* **Đề bài:** Tạo dataclass `SanPham` (ten, gia, `ton_kho` int = 0). Viết hàm `thong_ke(danh_sach)` in ra: (1) tổng số mặt hàng, (2) tổng giá trị kho (tổng `gia * ton_kho`), (3) mặt hàng có số lượng tồn ít nhất. Cho 4 sản phẩm mẫu và gọi hàm.
* **Input:** Không có.
* **Output:**
  ```
  Tong so mat hang: 4
  Tong gia tri kho: 15550000.0
  Hang ton it nhat: SanPham(ten='Tai nghe', gia=500000.0, ton_kho=2)
  ```
* **Gợi ý:** Dùng `len()`, vòng lặp cộng dồn, và `min(danh_sach, key=lambda sp: sp.ton_kho)`.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Tạo dataclass tự động có `__init__`, `__repr__`, `__eq__`.
* ✅ Dùng giá trị mặc định và `field(default_factory=list)` đúng cách.
* ✅ Bảo vệ dữ liệu bằng `frozen=True`.
* ✅ Viết phương thức và xử lý danh sách đối tượng (sắp xếp, thống kê, tìm kiếm).

> 💪 Chưa tự làm được bài nào thì đừng lo — hãy xem lại bài giảng rồi quay lại. **Lập trình là luyện tập!**

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 25: Lambda](../25_Lambda/bai_giang.md)**
