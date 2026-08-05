# 📝 Bài 23: Bài Tập – Lập Trình Hướng Đối Tượng

> 🎯 **Chủ đề:** class, thuộc tính, phương thức, `__init__`, `self`, `__str__`, kế thừa (`super`), ghi đè, đóng gói, `@classmethod` / `@staticmethod`.

---

## 📌 Hướng dẫn làm bài

* ✅ Mỗi bài tự viết class rồi tạo đối tượng và gọi phương thức để kiểm chứng.
* ✅ Nhớ: phương thức luôn có tham số `self` đầu tiên; gọi phương thức phải có dấu ngoặc `()`.
* ✅ `__init__` chỉ nên gán thuộc tính; `__str__` trả về chuỗi (không dùng `print` trong đó).
* ✅ Đáp án chi tiết 20 bài: 👉 [xem file dap_an.md](dap_an.md)

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Class đầu tiên

* **Đề bài:** Tạo class `HocSinh` có thuộc tính `ten`, `lop` gán trong `__init__`. Tạo 2 đối tượng "Nguyen Van An" (10A1) và "Tran Thi Mai" (11B2), in tên của từng bạn.
* **Input:** Không có.
* **Output:**
  ```
  An hoc lop 10A1
  Mai hoc lop 11B2
  ```
* **Gợi ý:** `print(f"{hs.ten} hoc lop {hs.lop}")`.

### Bài 2: Xếp loại điểm

* **Đề bài:** Class `HocSinh` có `__init__(ten, diem_tb)`. Phương thức `xep_loai()` trả về loại: ≥8 Gioi, ≥6.5 Kha, ≥5 Trung binh, còn lại Yeu. Tạo bạn "An" điểm 8.5, in kết quả.
* **Input:** Không có.
* **Output:**
  ```
  An: Gioi
  ```
* **Gợi ý:** Dùng `if/elif` đọc `self.diem_tb`.

### Bài 3: Constructor với giá trị biến thiên

* **Đề bài:** Class `HinhChuNhat` với `dai`, `rong`. Phương thức `dien_tich()` và `chu_vi()`. Tạo hình 6×4, in diện tích và chu vi.
* **Input:** Không có.
* **Output:**
  ```
  Dien tich: 24
  Chu vi: 20
  ```
* **Gợi ý:** `dien_tich = dai * rong`; `chu_vi = 2 * (dai + rong)`.

### Bài 4: ATM Mini

* **Đề bài:** Class `ATM` với `so_du`; phương thức `nap(tien)` cộng vào số dư; `rut(tien)` kiểm tra đủ tiền rồi trừ, trả về `True/False`; `xem()` trả về số dư. Mô phỏng: khởi tạo 1000000, nạp 50000, rút 200000, in số dư.
* **Input:** Không có.
* **Output:**
  ```
  So du: 850000
  ```
* **Gợi ý:** Nếu `tien > self.so_du` → in thông báo và trả về `False`.

### Bài 5: `__str__` đẹp

* **Đề bài:** Class `SinhVien` với `ma_so`, `ho_ten`. Viết `__str__` trả về chuỗi dạng `Ma so: SV001 - Ho ten: Nguyen Van An`. Tạo 2 sinh viên và in từng đối tượng.
* **Input:** Không có.
* **Output:**
  ```
  Ma so: SV001 - Ho ten: Nguyen Van An
  Ma so: SV002 - Ho ten: Tran Thi Mai
  ```
* **Gợi ý:** `def __str__(self): return f"Ma so: {self.ma_so} - Ho ten: {self.ho_ten}"`.

### Bài 6: Danh sách điểm

* **Đề bài:** Class `SinhVien` thêm thuộc tính `mon_hoc` (list rỗng), phương thức `them_mon(ten)` thêm môn, `in_mon_hoc()` in danh sách. Tạo sinh viên, thêm 3 môn, in ra.
* **Input:** Không có.
* **Output:**
  ```
  Mon hoc cua An: Toan, Van, Anh
  ```
* **Gợi ý:** `self.mon_hoc.append(ten)`; nối list bằng `", ".join(self.mon_hoc)`.

### Bài 7: Tính điểm trung bình

* **Đề bài:** Class `HocSinh` có `diem` là list 3 môn. Phương thức `tinh_tb()` trả về điểm trung bình. Tạo sinh viên điểm `[8, 7, 9]`, in TB 2 chữ số thập phân.
* **Input:** Không có.
* **Output:**
  ```
  Diem trung binh: 8.00
  ```
* **Gợi ý:** `sum(self.diem) / len(self.diem)`.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Đóng gói tài khoản

* **Đề bài:** Class `BankAccount` với `_so_du` protected; `nap_tien(tien)`, `rut_tien(tien)` (kiểm tra đủ tiền), `xem_so_du()`. Mô phỏng: 1.000.000 → nạp 200.000 → rút 1.500.000 (thất bại) → rút 100.000 → in số dư.
* **Input:** Không có.
* **Output:**
  ```
  Rut that bai: khong du so du
  So du cuoi: 1100000
  ```
* **Gợi ý:** `rut_tien` trả về `False` khi không đủ; chỉ trừ khi đủ.

### Bài 9: Kế thừa đơn giản

* **Đề bài:** Class `HocSinh` (`ten`, `lop`, `gioi_thieu()`). Class `HocSinhNangKhieu(HocSinh)` thêm `nang_khieu`, ghi đè `gioi_thieu()` thêm "voi nang khieu ...". Tạo đối tượng, gọi phương thức.
* **Input:** Không có.
* **Output:**
  ```
  Toi la An hoc lop 10A1
  Toi la Minh hoc lop 10A1, voi nang khieu ve hoi hoa
  ```
* **Gợi ý:** Phương thức của con gọi `super()` hoặc viết lại hoàn toàn.

### Bài 10: `super().__init__`

* **Đề bài:** Class `NhanVien` (`ten`, `ma_so`). Class `GiaoVien(NhanVien)` thêm `mon_day`, dùng `super().__init__`. Phương thức `mo_ta()` in thông tin đầy đủ.
* **Input:** Không có.
* **Output:**
  ```
  Giao vien: Nguyen Van An, MS: NV01, day mon Toan
  ```
* **Gợi ý:** `self.mon_day` thêm sau khi `super().__init__`.

### Bài 11: Lớp học quản lý học sinh

* **Đề bài:** Class `HocSinh` (`ten`, `diem_tb`). Class `LopHoc` với `them(hs)` và `trung_binh_ca_lop()` tính TB cả lớp (list rỗng thì 0.0). Thêm 3 bạn, in TB cả lớp 2 chữ số.
* **Input:** Không có.
* **Output:**
  ```
  Diem trung binh ca lop: 7.50
  ```
* **Gợi ý:** Duyệt `self.danh_sach`, cộng `hs.diem_tb` rồi chia `len`.

### Bài 12: Ghi đè `__str__`

* **Đề bài:** Class `Xe` (`ten`, `gia`) `__str__`; Class `XeMay(Xe)` ghi đè `__str__` thêm tiền tố `[Xe may]`; class `OTo(Xe)` ghi đè thêm `[O to]`. Tạo đối tượng và in cả 3.
* **Input:** Không có.
* **Output:**
  ```
  Xe chung: Xe Cub, gia 30
  Xe may: [Xe may] Xemay, gia 30
  O to: [Oto] Kia, gia 500
  ```
* **Gợi ý:** Mỗi class con định nghĩa lại `__str__` với nội dung riêng (có thể dùng `super().__str__()`).

### Bài 13: Đóng gói với `__so_du`

* **Đề bài:** Class `ViDienTu` dùng `self.__so_du` (2 gạch dưới) `nap(tien)`, `tra_so_du()`. Truy cập `vi.__so_du` ngoài class. In lỗi `AttributeError` và ghi nhận chương trình đã dùng đúng `tra_so_du()`.
* **Input:** Không có.
* **Output:**
  ```
  So du hop le: 100000
  `vi.__so_du` gay AttributeError (dang bao mat)
  ```
* **Gợi ý:** Dùng `try/except` để bắt lỗi truy cập trực tiếp (kiến thức Bài 19).

### Bài 14: `@staticmethod` và `@classmethod`

* **Đề bài:** Class `SanPham` với `THUE = 0.1`; `@classmethod doi_thue(cls, thue)`; `@staticmethod tinh_gia_sau_thue(gia)`. Ban đầu in `tinh_gia_sau_thue(100000)`, sau khi `doi_thue(0.05)` in tiếp.
* **Input:** Không có.
* **Output:**
  ```
  110000.0
  105000.0
  ```
* **Gợi ý:** Đầu tiên = `100000 * 1.1`; sau khi đổi = `100000 * 1.05`.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Quản lý điểm cá nhân

* **Đề bài:** Class `HocSinh` (`ten`, `lop`, `diem` list 3 môn). Phương thức: `tinh_tb()`, `xep_loai()` (≥8 Gioi, ≥6.5 Kha, ≥5 Trung binh, else Yeu), `__str__` dạng `Ten - TB - Loai`. Tạo 3 học sinh, in danh sách trình bày đẹp.
* **Input:** Không có.
* **Output:**
  ```
  Nguyen Van An     TB: 8.17 - Gioi
  Tran Thi Mai      TB: 6.50 - Kha
  Le Quang Binh     TB: 5.00 - Trung binh
  ```
* **Gợi ý:** F-string canh cột `:<20` + `:.2f`; `diem = [8.5, 7.0, 9.0]`.

### Bài 16: Thư viện mini

* **Đề bài:** Class `Sach` (`ten`, `tac_gia`, `nam`). Class `ThuVien` có list rỗng, `them(sach)`, `tim(ten_tu_khoa)` trả về list sách có tên chứa từ khóa, `ton_danh_sach()`. Thêm 3 sách, tìm sách có "Python".
* **Input:** Không có.
* **Output:**
  ```
  Tim thay 2 quyen:
  - Python Co Ban - Nguyen Van An
  - Python Nang Cao - Tran B
  ```
* **Gợi ý:** Duyệt list; `if tu_khoa in sach.ten`; `__str__` của `Sach` trả về `f"{ten} - {tac_gia}"`.

### Bài 17: ATM hoàn chỉnh

* **Đề bài:** Class `ATM` với `_so_du`, `nap(tien)`, `rut(tien)` (chặn rút 0 đủ số dư, chặn số âm), `xem_so_du()`. Mô phỏng các thao tác: tạo 500000; nạp -100 (lỗi); rút 600000 (lỗi); nạp 300000; rút 400000; in từng kết quả và số dư cuối.
* **Input:** Không có.
* **Output:**
  ```
  Nap that bai: so tien phai lon hon 0
  Rut that bai: khong du so du
  Nap 300000 thanh cong
  Rut 400000 thanh cong
  So du cuoi: 400000
  ```
* **Gợi ý:** Kiểm tra điều kiện trước khi cập nhật; mỗi phương thức in trạng thái hoặc trả về `True/False`.

### Bài 18: Kế thừa ba tầng

* **Đề bài:** `NhanVien` → `GiaoVien` (thêm `mon_day`) → `GiaoVienChuNhiem` (thêm `lop_cn`). Mỗi tầng gọi `super().__init__` và ghi đè `mo_ta()`. Tạo đối tượng 3 tầng, in `mo_ta()` của cả 3 và so sánh.
* **Input:** Không có.
* **Output:**
  ```
  NV: An (NV01)
  GV: An day mon Toan (NV01)
  GVCN: An day mon Toan, chu nhiem lop 10A1 (NV01)
  ```
* **Gợi ý:** Mỗi tầng `mo_ta()` xây trên kết quả của cha bằng `super().mo_ta()` hoặc viết lại.

### Bài 19: Game đoán số bằng OOP

* **Đề bài:** Class `NguoiChoi` (`ten`, `diem`). `Class TroChoi` với `so_bi_mat` ngẫu nhiên (dùng `random.randint` Bài 20), `doan(so)` trả về `-1` nếu nhỏ, `1` nếu lớn, `0` nếu đúng và tăng `số_lan`. Mô phỏng dùng `while` đoán số 7 để máy phản hồi từng lượt.
* **Input:** Không có.
* **Output (ví dụ):**
  ```
  So ban doan 5 nho hon
  So ban doan 8 lon hon
  Chinh xac! So bi mat la 7 sau 3 luot
  ```
* **Gợi ý:** `random.randint(1, 10)`; trong `TroChoi` dùng `self.so_bi_mat` so sánh.

### Bài 20: Quản lý trường học (tiểu dự án)

* **Đề bài:** Xây 5 class:
  * `Nguoi` (`ten`, `__str__` trả về tên)
  * `HocSinh(Nguoi)` thêm `lop`, `diem_tb`, `xep_loai()`
  * `GiaoVien(Nguoi)` thêm `mon_day`
  * `LopHoc` (`ten_lop`, list học sinh, `them(hs)`, `so_hoc_sinh()`)
  * `Truong` (`ten`, load list `lop_hoc` và `giao_vien`, `them_lop`, `tong_so_hoc_sinh()` với `@staticmethod` đếm, hoặc `@classmethod` in báo cáo)
* Chương trình: tạo 1 trường, 2 lớp (mỗi lớp 2 HS), 1 giáo viên; in báo cáo: tổng HS, từng lớp, từng giáo viên.
* **Input:** Không có.
* **Output:**
  ```
  Truong THPT Python
  Tong so hoc sinh: 4
  Lop 10A1: 2 hoc sinh
  Lop 10A2: 2 hoc sinh
  Giao vien: Co Mai day mon Toan
  ```
* **Gợi ý:** `@staticmethod` đếm hỗ trợ lớp `Truong`; dùng `__str__` lớp con hợp lại trong báo cáo.

---

## 🎯 Tổng kết sau khi làm bài

* ✅ Tự viết class với thuộc tính, phương thức, `__init__`, `self`, `__str__`.
* ✅ Dùng kế thừa + `super()` + ghi đè để tái sử dụng và mở rộng.
* ✅ Bảo vệ dữ liệu bằng đóng gói `_` / `__` và phương thức truy cập.
* ✅ Áp dụng OOP vào hệ thống nhỏ: trường học, ATM, thư viện, game.

> 💪 OOP là "chân trời mới" — Bài tiếp theo **Dataclass** sẽ giúp viết class ngắn gọn hơn hẳn!

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 24: Dataclass](../24_Dataclass/bai_giang.md)**