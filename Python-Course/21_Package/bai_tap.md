# 📝 Bài 21: Bài Tập – Package Trong Python

> 🎯 **Chủ đề:** Tạo package `quanly`, tổ chức module vào package, import từ package, sử dụng package trong `main.py`.

---

## 📌 Hướng dẫn làm bài

* ✅ Mỗi bài tập yêu cầu **tự tạo thư mục và file** theo hướng dẫn, rồi chạy `main.py` để kiểm tra.
* ✅ Cấu trúc chuẩn dùng cho nhiều bài:

  ```
  du_an/
  ├── main.py
  └── quanly/
      ├── __init__.py
      ├── hoc_sinh.py
      └── diem.py
  ```

* ✅ Nhớ luôn tạo file `__init__.py` trong mỗi thư mục package.
* ✅ Đáp án chi tiết 20 bài: 👉 [xem file dap_an.md](dap_an.md)

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Tạo package đầu tiên

* **Đề bài:** Tạo thư mục `quanly` chứa file `__init__.py` (để trống). Viết `main.py` cùng cấp, chạy thử `import quanly` và in ra `quanly.__name__`.
* **Input:** Không có.
* **Output:**
  ```
  quanly
  ```
* **Gợi ý:** `print(quanly.__name__)` cho ra tên package.

### Bài 2: Module đầu tiên trong package

* **Đề bài:** Trong `quanly`, tạo file `hoc_sinh.py` chứa hàm `chao_hoc_sinh(ten)` in lời chào: `Xin chao ban {ten}!`. Viết `main.py` import `quanly.hoc_sinh` và gọi hàm với tên "An".
* **Input:** Không có.
* **Output:**
  ```
  Xin chao ban An!
  ```
* **Gợi ý:** Gọi hàm bằng cú pháp `quanly.hoc_sinh.chao_hoc_sinh("An")`.

### Bài 3: Module thứ hai – điểm số

* **Đề bài:** Trong `quanly`, tạo file `diem.py` chứa hàm `trung_binh(danh_sach)` trả về trung bình cộng của list điểm (danh sách rỗng thì trả về 0.0). Viết `main.py` in kết quả của `[8, 7, 9]`.
* **Input:** Không có.
* **Output:**
  ```
  Diem trung binh: 8.0
  ```
* **Gợi ý:** Dùng `sum(danh_sach) / len(danh_sach)`.

### Bài 4: Import kiểu 1 – `import quanly.hoc_sinh`

* **Đề bài:** Dùng cấu trúc bài 2, viết `main.py` chỉ dùng lệnh `import quanly.hoc_sinh` (không dùng `from`), tạo học sinh bằng hàm `tao_hoc_sinh("Mai", "10A1")` trả về dict `{"ten": ..., "lop": ...}` rồi in ra tên.
* **Input:** Không có.
* **Output:**
  ```
  Mai
  ```
* **Gợi ý:** `hs = quanly.hoc_sinh.tao_hoc_sinh(...)` rồi `print(hs["ten"])`.

### Bài 5: Import kiểu 2 – `from quanly import diem`

* **Đề bài:** Viết `main.py` dùng `from quanly import diem` để gọi `diem.trung_binh([10, 10, 10])` và in kết quả.
* **Input:** Không có.
* **Output:**
  ```
  Trung binh: 10.0
  ```
* **Gợi ý:** Khác bài 3 là lệnh import, còn cách gọi tương tự nhau.

### Bài 6: Import kiểu 3 – lấy thẳng hàm

* **Đề bài:** Viết `main.py` dùng `from quanly.diem import trung_binh, xep_loai` (viết thêm hàm `xep_loai(tb)` theo thang: ≥8 Giỏi, ≥6.5 Khá, ≥5 Trung bình, còn lại Yếu). In xếp loại của điểm 6.8.
* **Input:** Không có.
* **Output:**
  ```
  Diem 6.8 -> Kha
  ```
* **Gợi ý:** Khi import thẳng tên thì gọi không cần tiền tố.

### Bài 7: Import kiểu 4 – bí danh `as`

* **Đề bài:** Viết `main.py` dùng `import quanly.hoc_sinh as hs` và `import quanly.diem as d`. Gọi `hs.chao_hoc_sinh("Binh")` và `d.trung_binh([5, 6])`, in cả hai kết quả.
* **Input:** Không có.
* **Output:**
  ```
  Xin chao ban Binh!
  Diem trung binh: 5.5
  ```
* **Gợi ý:** `as` chỉ đặt bí danh ngắn, cách dùng y như tên thật.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Học sinh dạng dict

* **Đề bài:** Trong `hoc_sinh.py`, viết hàm `tao_hoc_sinh(ten, lop)` trả về dict và hàm `hien_thi(hs)` in ra `- Ten (lop Lop)`. Viết `main.py` tạo 2 học sinh và hiển thị cả hai.
* **Input:** Không có.
* **Output:**
  ```
  - Nguyen Van An (lop 10A1)
  - Tran Thi Mai (lop 11B2)
  ```
* **Gợi ý:** Dùng f-string: `f"- {hs['ten']} (lop {hs['lop']})"`.

### Bài 9: Xếp loại học sinh

* **Đề bài:** Hoàn thiện `diem.py` với hàm `xep_loai(tb)` như bài 6. Viết `main.py` có list 5 điểm trung bình mẫu `[9.5, 7.0, 5.2, 4.0, 8.0]`, in từng cặp `diem -> loai`.
* **Input:** Không có.
* **Output:**
  ```
  9.5 -> Gioi
  7.0 -> Kha
  5.2 -> Trung binh
  4.0 -> Yeu
  8.0 -> Gioi
  ```
* **Gợi ý:** Dùng vòng lặp `for` duyệt list (kiến thức Bài 14).

### Bài 10: Kết hợp hai module

* **Đề bài:** Viết `main.py` kết hợp `hoc_sinh.py` và `diem.py`: tạo 3 học sinh, mỗi bạn gắn list điểm 3 môn, in ra `Ten: diem TB - Xep loai` cho từng bạn.
* **Input:** Không có.
* **Output:**
  ```
  Nguyen Van An: 8.17 - Gioi
  Tran Thi Mai: 6.50 - Kha
  Le Quang Binh: 5.00 - Trung binh
  ```
* **Gợi ý:** Tổ chức dữ liệu dạng list chứa dict: `{"ten": ..., "lop": ..., "diem": [...]}`.

### Bài 11: Package con

* **Đề bài:** Tạo package con `quanly/giaovu/` gồm `__init__.py` và `lop_hoc.py` chứa hàm `danh_sach_lop()` trả về `["10A1", "10A2", "11B1"]`. Viết `main.py` in từng lớp trong danh sách.
* **Input:** Không có.
* **Output:**
  ```
  Lop: 10A1
  Lop: 10A2
  Lop: 11B1
  ```
* **Gợi ý:** Import qua hai cấp: `from quanly.giaovu import lop_hoc`.

### Bài 12: `__init__.py` làm mặt tiền

* **Đề bài:** Sửa `__init__.py` để xuất sẵn `tao_hoc_sinh`, `trung_binh`, `xep_loai` (dùng import tương đối `from .ten_file import ...`), thêm biến `TEN_PHAN_MEM = "QuanLy v1.0"`. Viết `main.py` chỉ cần `import quanly` rồi dùng thẳng các hàm và in `quanly.TEN_PHAN_MEM`.
* **Input:** Không có.
* **Output:**
  ```
  QuanLy v1.0
  Trung binh: 7.0
  ```
* **Gợi ý:** Trong `__init__.py` dùng `from .hoc_sinh import tao_hoc_sinh`.

### Bài 13: Package tiện ích tự đặt

* **Đề bài:** Tạo package `tien_ich` gồm `__init__.py`, `tinh_toan.py` (hàm `giai_thua(n)`) và `chuoi.py` (hàm `dao_nguoc(s)`). Viết `main.py` in `giai_thua(5)` và `dao_nguoc("Python")`.
* **Input:** Không có.
* **Output:**
  ```
  Giai thua 5: 120
  Dao nguoc: nohtyP
  ```
* **Gợi ý:** `giai_thua` dùng vòng lặp `for` hoặc `while`; `dao_nguoc` dùng `s[::-1]`.

### Bài 14: Hai package, không đụng nhau

* **Đề bài:** Tạo 2 package độc lập: `diem` (hàm `xep_loai(tb)` thang 10) và `danh_gia` (hàm `xep_loai(tb)` thang 100: ≥80 "Tot", còn lại "Chua tot"). Viết `main.py` gọi cả hai và in kết quả của `8.0` và `80`.
* **Input:** Không có.
* **Output:**
  ```
  Diem 8.0 -> Gioi
  Danh gia 80 -> Tot
  ```
* **Gợi ý:** Dùng `as` cho một trong hai lệnh import để phân biệt.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Thống kê học sinh theo lớp

* **Đề bài:** Thêm vào `hoc_sinh.py` hàm `thong_ke(danh_sach)` nhận list học sinh dict, trả về dict `{lop: so_luong}`. Viết `main.py` với 4 học sinh (2 lớp khác nhau) và in kết quả thống kê.
* **Input:** Không có.
* **Output:**
  ```
  Thong ke theo lop:
  10A1: 2 hoc sinh
  10A2: 2 hoc sinh
  ```
* **Gợi ý:** Duyệt danh sách, nếu lớp chưa có trong dict thì khởi tạo 0, rồi `+1`.

### Bài 16: Tìm học sinh điểm cao nhất

* **Đề bài:** Dùng `quanly` (hoc_sinh + diem): tạo 3 học sinh kèm điểm 3 môn, tính điểm TB từng bạn, tìm và in tên bạn có điểm TB **cao nhất**.
* **Input:** Không có.
* **Output:**
  ```
  Hoc sinh cao diem nhat: Nguyen Van An (8.17)
  ```
* **Gợi ý:** Lưu `(ten, tb)` vào list, duyệt so sánh `max`, hoặc dùng hàm `max` với `key`.

### Bài 17: Module con sử dụng lẫn nhau

* **Đề bài:** Thêm file `bang_diem.py` vào `quanly`, bên trong **import từ chính package** (`from . import diem`) và có hàm `in_bang(danh_sach)` in bảng điểm 3 môn + TB của từng học sinh. Viết `main.py` gọi `in_bang`.
* **Input:** Không có.
* **Output:**
  ```
  Ten                Toan  Van  Anh   TB
  Nguyen Van An        8.5  7.0  9.0  8.17
  Tran Thi Mai         6.0  6.5  7.0  6.50
  ```
* **Gợi ý:** F-string canh cột: `f"{ten:<20} {t:<5} {v:<5} {a:<5} {tb:.2f}"`.

### Bài 18: Package mô phỏng ngân hàng

* **Đề bài:** Tạo package `ngan_hang` gồm `tai_khoan.py` (hàm `tao_tai_khoan(so_du)`, `nap(tk, tien)`, `rut(tk, tien)` trả về `True/False`) và `giao_dich.py` (hàm `ghi_giao_dich(lich_su, mo_ta)` thêm chuỗi vào list). Viết `main.py`: tạo tài khoản 500000, nạp 200000, rút 100000, in lịch sử giao dịch.
* **Input:** Không có.
* **Output:**
  ```
  So du: 600000
  Lich su giao dich:
  - Nap 200000
  - Rut 100000
  ```
* **Gợi ý:** `rut` cần kiểm tra `tien <= so_du`; `tk["so_du"]` cập nhật sau mỗi lệnh.

### Bài 19: Tái cấu trúc từ Bài 20

* **Đề bài:** Ở Bài 20 bạn có module `tien_ich.py` với `dien_tich_hinh_tron(r)` và `chu_vi_hinh_tron(r)`. Hãy chuyển thành package `tien_ich` gồm `hinh_tron.py` (2 hàm trên) và `hinh_chu_nhat.py` (`dien_tich(dai, rong)`, `chu_vi(dai, rong)`). Viết `main.py` mới dùng package, in kết quả cho `r = 5` và `dai = 4, rong = 3`.
* **Input:** Không có.
* **Output:**
  ```
  Hinh tron r=5: dien tich 78.54, chu vi 31.42
  Hinh chu nhat 4x3: dien tich 12, chu vi 14
  ```
* **Gợi ý:** `main.py` nằm cùng cấp với package `tien_ich`; gọi qua `tien_ich.hinh_tron.dien_tich_hinh_tron(5)`.

### Bài 20: Tiểu dự án – hệ thống quản lý điểm

* **Đề bài:** Hoàn thiện package `quanly` thành "hệ thống": `__init__.py` chứa `__version__ = "1.0"` và xuất sẵn các hàm chính; `hoc_sinh.py` có `tao_hoc_sinh`, `hien_thi`, `thong_ke`; `diem.py` có `trung_binh`, `xep_loai`. Viết `main.py`: tạo 4 học sinh (2 lớp), tính TB và xếp loại từng bạn, in bảng tổng hợp, in thống kê theo lớp và in `quanly.__version__`.
* **Input:** Không có.
* **Output:**
  ```
  Quan ly hoc sinh v1.0
  === BANG DIEM ===
  Nguyen Van An       TB: 8.17 - Gioi
  ...
  === THONG KE ===
  10A1: 2 hoc sinh
  10A2: 2 hoc sinh
  ```
* **Gợi ý:** Chia chương trình thành các khối rõ ràng; mọi hàm lấy từ package `quanly`.

---

## 🎯 Tổng kết sau khi làm bài

* ✅ Tự tạo được package gồm `__init__.py` và nhiều module.
* ✅ Thành thạo 4 kiểu import và biết khi nào dùng kiểu nào.
* ✅ Biết tổ chức package con, import tương đối, "mặt tiền" `__init__.py`.
* ✅ Hiểu vì sao package giúp dự án lớn vẫn gọn gàng.

> 💪 Làm xong 20 bài, bạn đã sẵn sàng cho **Bài 22: đọc/ghi file** để lưu dữ liệu lâu dài!

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 22: Đọc Và Ghi File](../22_File/bai_giang.md)**
