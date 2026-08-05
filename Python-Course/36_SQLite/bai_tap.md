# 📝 Bài 36: Bài Tập – SQLite

> 🎯 **Chủ đề:** Làm quen cơ sở dữ liệu SQLite với module `sqlite3` — tạo bảng, thêm, sửa, xóa, tìm kiếm dữ liệu.
>
> 📌 **Lưu ý:** Tất cả bài tập dùng **file `.db` tạm** đặt ngay trong thư mục chạy (ví dụ `bai_tap_36.db`). Muốn chạy lại từ đầu, bạn có thể xóa file `.db` cũ. Nếu chưa làm được, hãy xem lại bài giảng rồi quay lại — **đáp án chi tiết ở [dap_an.md](dap_an.md)**.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Tạo cơ sở dữ liệu và bảng học sinh

* **Đề bài:** Viết chương trình kết nối file `bai_tap_36.db` và tạo bảng `hoc_sinh` gồm các cột: `id` (số nguyên, khóa chính, tự tăng), `ten` (chữ, không để trống), `toan`, `van` (số thực).
* **Input:** Không có.
* **Output:** Không in gì (hoặc in "Đã tạo bảng hoc_sinh."). Sau khi chạy, trong thư mục có file `bai_tap_36.db`.
* **Ví dụ:**
  ```
  Đã tạo bảng hoc_sinh.
  ```
* **Gợi ý:** `sqlite3.connect("bai_tap_36.db")`, dùng `cur.execute("""CREATE TABLE IF NOT EXISTS ...""")`.

### Bài 2: Thêm ba học sinh đầu tiên

* **Đề bài:** Dùng lại bảng `hoc_sinh` ở bài 1, thêm 3 học sinh: An (Toán 8.5, Văn 7.0), Bình (Toán 9.0, Văn 8.5), Cường (Toán 6.5, Văn 7.5). Chạy chương trình **2 lần** và quan sát kết quả đếm dòng.
* **Input:** Không có.
* **Output:**
  ```
  Đã thêm học sinh Nguyễn Văn An (mã số 1).
  Đã thêm học sinh Trần Thị Bình (mã số 2).
  Đã thêm học sinh Lê Văn Cường (mã số 3).
  ```
* **Gợi ý:** `INSERT INTO hoc_sinh (ten, toan, van) VALUES (?, ?, ?)` và đừng quên `conn.commit()`; in `cur.lastrowid`.

### Bài 3: Xem toàn bộ danh sách học sinh

* **Đề bài:** Viết chương trình đọc và in ra **tất cả** học sinh trong bảng `hoc_sinh` dạng `Mã X: Tên - Toán Y - Văn Z`.
* **Input:** Không có (dùng dữ liệu đã thêm ở bài 2).
* **Output:**
  ```
  Mã 1: Nguyễn Văn An - Toán 8.5 - Văn 7.0
  Mã 2: Trần Thị Bình - Toán 9.0 - Văn 8.5
  Mã 3: Lê Văn Cường - Toán 6.5 - Văn 7.5
  ```
* **Gợi ý:** `SELECT * FROM hoc_sinh` rồi `fetchall()` và duyệt bằng `for`.

### Bài 4: Lọc học sinh có điểm Văn trên 7.0

* **Đề bài:** Viết chương trình in ra tên các học sinh có điểm Văn **lớn hơn 7.0**, kèm điểm Văn.
* **Input:** Không có (dùng dữ liệu ở bài 2).
* **Output:**
  ```
  Trần Thị Bình - Van 8.5
  Lê Văn Cường - Van 7.5
  ```
* **Gợi ý:** `SELECT ten, van FROM hoc_sinh WHERE van > 7.0`.

### Bài 5: Cập nhật điểm Toán

* **Đề bài:** Cập nhật điểm Toán của học sinh mã số 1 lên `10.0`, rồi in ra số dòng đã sửa.
* **Input:** Không có.
* **Output:**
  ```
  So dong da sua: 1
  ```
* **Gợi ý:** `UPDATE hoc_sinh SET toan = ? WHERE id = ?`, in `cur.rowcount`, nhớ `commit()`.

### Bài 6: Xóa một học sinh

* **Đề bài:** Xóa học sinh có `id = 3` khỏi bảng, in ra số dòng đã xóa, sau đó in lại toàn bộ danh sách để kiểm tra.
* **Input:** Không có.
* **Output:**
  ```
  So dong da xoa: 1
  Mã 1: Nguyễn Văn An - Toán 10.0 - Văn 7.0
  Mã 2: Trần Thị Bình - Toán 9.0 - Văn 8.5
  ```
* **Gợi ý:** `DELETE FROM hoc_sinh WHERE id = ?` + `commit()`.

### Bài 7: Đếm số lượng học sinh

* **Đề bài:** Viết chương trình đếm và in ra **tổng số học sinh** hiện có trong bảng (dùng câu lệnh SQL `COUNT`).
* **Input:** Không có.
* **Output:**
  ```
  Tong so hoc sinh: 2
  ```
* **Gợi ý:** `SELECT COUNT(*) FROM hoc_sinh`, kết quả là `rows[0][0]`.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Tìm học sinh theo đúng tên

* **Đề bài:** Viết chương trình tìm học sinh có tên `Trần Thị Bình` và in ra đầy đủ thông tin. Nếu không tìm thấy, in `Khong tim thay.` Dùng tham số `?` cho tên.
* **Input:** Không có (gán trực tiếp `ten_can_tim = "Trần Thị Bình"`).
* **Output:**
  ```
  Tim thay: Mã 2 - Trần Thị Bình - Toán 9.0 - Văn 8.5
  ```
* **Gợi ý:** `SELECT * FROM hoc_sinh WHERE ten = ?`; dùng `fetchone()` vì chỉ cần 1 dòng.

### Bài 9: Tìm học sinh theo từ khóa trong tên

* **Đề bài:** Viết chương trình tìm tất cả học sinh có tên **chứa chữ** `An` (ví dụ "Nguyễn Văn An", "Anh") và in ra danh sách.
* **Input:** Không có.
* **Output:**
  ```
  Mã 1: Nguyễn Văn An
  ```
* **Gợi ý:** Dùng `WHERE ten LIKE ?` với tham số `"%An%"`.

### Bài 10: Sắp xếp theo điểm Toán giảm dần

* **Đề bài:** In danh sách học sinh (mã, tên, điểm Toán) **sắp xếp theo điểm Toán giảm dần** — học sinh giỏi Toán đứng đầu.
* **Input:** Không có.
* **Output:**
  ```
  1: Nguyễn Văn An - 10.0
  2: Trần Thị Bình - 9.0
  ```
* **Gợi ý:** `ORDER BY toan DESC`.

### Bài 11: Trung bình cộng hai môn của từng học sinh

* **Đề bài:** In ra tên và **điểm trung bình** của từng học sinh (tính trung bình Toán – Văn ngay trong Python), làm tròn 2 chữ số.
* **Input:** Không có.
* **Output:**
  ```
  Nguyễn Văn An - 8.5
  Trần Thị Bình - 8.75
  ```
* **Gợi ý:** Tính `(row[2] + row[3]) / 2` rồi `round(x, 2)`.

### Bài 12: Điểm trung bình toàn lớp

* **Đề bài:** Dùng câu lệnh SQL để tính **điểm Toán trung bình** của cả lớp và in ra kết quả làm tròn 2 chữ số.
* **Input:** Không có.
* **Output:**
  ```
  Diem toan trung binh: 9.5
  ```
* **Gợi ý:** `SELECT AVG(toan) FROM hoc_sinh`.

### Bài 13: Lọc theo khoảng điểm

* **Đề bài:** In ra danh sách học sinh có điểm Văn **từ 7.0 đến 8.5** (bao gồm cả hai giá trị), mỗi dòng: tên và điểm Văn.
* **Input:** Không có.
* **Output:**
  ```
  Nguyễn Văn An - Van 7.0
  Trần Thị Bình - Van 8.5
  ```
* **Gợi ý:** Dùng `BETWEEN ? AND ?` hoặc `van >= ? AND van <= ?`.

### Bài 14: Cập nhật nhiều bản ghi cùng lúc

* **Đề bài:** Tăng điểm Văn lên `1.0` cho **tất cả** học sinh có điểm Văn dưới 8.0, in số dòng đã sửa, rồi in lại danh sách.
* **Input:** Không có.
* **Output:**
  ```
  So dong da sua: 1
  Mã 1: Nguyễn Văn An - Văn 8.0
  Mã 2: Trần Thị Bình - Văn 8.5
  ```
* **Gợi ý:** `UPDATE hoc_sinh SET van = van + ? WHERE van < ?`.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Bảng sản phẩm với CRUD đầy đủ

* **Đề bài:** Tạo bảng `san_pham` (id, ten, gia REAL) trong file `cua_hang.db`. Thêm 4 sản phẩm, in danh sách, sửa giá sản phẩm mã 2 thành 15.000, xóa sản phẩm giá dưới 20.000, in danh sách lần cuối.
* **Input:** Không có (gán dữ liệu trực tiếp).
* **Output:**
  ```
  --- Sau khi thêm ---
  1: Sách Python - 120000.0
  2: Bút bi - 5000.0
  3: Vở ô ly - 8000.0
  4: Balo - 250000.0
  --- Sau khi sửa và xóa ---
  1: Sách Python - 120000.0
  4: Balo - 250000.0
  ```
* **Gợi ý:** Viết các hàm `them_san_pham`, `hien_thi`, `sua_gia`, `xoa_duoi_gia`.

### Bài 16: Chương trình menu quản lý học sinh

* **Đề bài:** Viết chương trình menu vòng lặp cho phép người dùng chọn: `1. Thêm`, `2. Xem`, `3. Sửa điểm`, `4. Xóa`, `5. Thoát`. Mỗi thao tác là một hàm. Dữ liệu lưu vào `ql_hs.db`. Tự chạy thử với các thao tác mẫu.
* **Input:** Số chọn menu và dữ liệu từ `input()`.
* **Output:** Ví dụ chạy với lựa chọn `1`, `2`, `5`:
  ```
  ===== QUAN LY HOC SINH =====
  1. Them hoc sinh
  2. Xem danh sach
  3. Sua diem
  4. Xoa hoc sinh
  5. Thoat
  Chon: 1
  Ten: An
  Diem toan: 8.5
  Diem van: 7.0
  Da them hoc sinh An (ma 1).
  Chon: 2
  Ma 1: An - Toan 8.5 - Van 7.0
  Chon: 5
  Tam biet!
  ```
* **Gợi ý:** Dùng `while True`, `if/elif` cho menu; mỗi chức năng tách hàm riêng.

### Bài 17: Chống SQL injection

* **Đề bài:** Viết chương trình hỏi tên học sinh qua `input()`, thêm vào bảng `hoc_sinh` **bằng tham số `?`**, rồi tự kiểm tra: nhập thử giá trị `x'); DROP TABLE hoc_sinh; --` và in ra xem bảng còn tồn tại không.
* **Input:** `x'); DROP TABLE hoc_sinh; --` (nhập làm thử nghiệm).
* **Output:**
  ```
  Da them hoc sinh co ten la: x'); DROP TABLE hoc_sinh; --
  So dong hien co: 3
  ```
  (Bảng vẫn còn nguyên — dữ liệu chưa bị xóa.)
* **Gợi ý:** `cur.execute("INSERT INTO hoc_sinh (ten) VALUES (?)", (ten,))` — tham số `?` biến chuỗi đó thành giá trị thuần túy.

### Bài 18: Thống kê toàn diện lớp học

* **Đề bài:** Viết chương trình in báo cáo lớp: số học sinh, điểm Toán cao nhất, thấp nhất, trung bình. Dùng các hàm SQL `COUNT`, `MAX`, `MIN`, `AVG`.
* **Input:** Không có.
* **Output:**
  ```
  So hoc sinh: 2
  Toan cao nhat: 10.0
  Toan thap nhat: 9.0
  Toan trung binh: 9.5
  ```
* **Gợi ý:** Mỗi thống kê là một `SELECT` riêng, đọc `fetchone()[0]`.

### Bài 19: Thêm cột và cập nhật dữ liệu cũ

* **Đề bài:** Bảng `hoc_sinh` hiện chưa có cột `email`. Viết chương trình: thêm cột `email TEXT`, cập nhật email cho từng học sinh theo mã số, rồi in bảng `id | ten | email`.
* **Input:** Không có.
* **Output:**
  ```
  1 | Nguyễn Văn An | an.nguyen@gmail.com
  2 | Trần Thị Bình | binh.tran@gmail.com
  ```
* **Gợi ý:** `ALTER TABLE hoc_sinh ADD COLUMN email TEXT` (chạy 1 lần; nếu chạy lại báo lỗi, có thể bỏ qua bằng try/except).

### Bài 20: Chương trình quản lý thư viện mini

* **Đề bài:** Tạo bảng `sach` (id, ten_sach, tac_gia, nam, so_luong) trong `thu_vien.db`. Viết chương trình menu: `1. Thêm sách`, `2. Xem sách`, `3. Tìm theo tên`, `4. Mượn sách` (giảm `so_luong` đi 1, nếu còn 0 thì báo "Hết sách"), `5. Thoát`. Mỗi chức năng là một hàm.
* **Input:** Số menu và dữ liệu từ `input()`.
* **Output:** Ví dụ: thêm "Python cơ bản", mượn sách đó:
  ```
  1. Them sach
  2. Xem sach
  3. Tim sach
  4. Muon sach
  5. Thoat
  Chon: 1
  Ten sach: Python co ban
  Tac gia: Nguyen Van A
  Nam: 2024
  So luong: 2
  Da them sach Python co ban.
  Chon: 4
  Ten sach can muon: Python co ban
  Da muon thanh cong. Con 1 quyen.
  Chon: 5
  Tam biet!
  ```
* **Gợi ý:** Mượn sách = `UPDATE sach SET so_luong = so_luong - 1 WHERE ten_sach = ? AND so_luong > 0`; kiểm tra `rowcount` để báo kết quả.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Tạo cơ sở dữ liệu, tạo bảng, thêm sửa xóa dữ liệu bằng SQL.
* ✅ Truy vấn với `WHERE`, `LIKE`, `ORDER BY`, `BETWEEN`, hàm `COUNT/AVG/MAX/MIN`.
* ✅ Dùng tham số `?` an toàn, `commit()`, `with` statement, `rowcount`, `lastrowid`.
* ✅ Xây dựng chương trình menu CRUD hoàn chỉnh.

> 💪 **Lập trình là luyện tập!** Chạy lại các chương trình nhiều lần, xóa file `.db` và thử lại từ đầu để hiểu sâu.

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 37: Logging](../37_Logging/bai_giang.md)**
