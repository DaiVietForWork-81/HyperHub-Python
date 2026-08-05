# 📝 Bài 41: Bài Tập – Dự Án Cuối Khóa: Ứng Dụng Quản Lý Thư Viện

> 🎓 **Bài tập cuối cùng của khóa học!** 20 bài tập này sẽ dẫn bạn **xây từng viên gạch** của chương trình `quan_ly_thu_vien.py`: từ class `Sach` nhỏ xíu đến toàn bộ ứng dụng hoàn chỉnh chạy bằng SQLite.
>
> ⚠️ **Lưu ý:** hãy tự làm trước, gặp bí mới xem **[Đáp án](./dap_an.md)**. Các bài từ Bài 5 trở đi thao tác với file `thu_vien.db` — file này **tự động được tạo tại thư mục đang chạy chương trình**.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Tạo lớp `Sach` cơ bản

* **Đề bài:** Định nghĩa class `Sach` có phương thức `__init__(ten, tac_gia, nam, so_luong=1)` lưu 4 thuộc tính, và `__str__` trả về chuỗi dạng `Ten sach - Tac gia (nam), X cuon`. Tạo 2 đối tượng và in ra bằng `print()`.
* **Input:** Không có — dùng trực tiếp 2 đầu sách mẫu: "De Men Phieu Luu Ky"/"To Hoai"/1941/10 và "Tuoi tho du doi"/"Nguyen Nhat Anh"/2008/5.
* **Output:** Hai chuỗi mô tả sách, mỗi cái một dòng.
* **Ví dụ:**
  ```
  De Men Phieu Luu Ky - To Hoai (1941), 10 cuon
  Tuoi tho du doi - Nguyen Nhat Anh (2008), 5 cuon
  ```
* **Gợi ý:** `__str__` phải `return` chuỗi (không được `print` bên trong); dùng f-string; nhớ từ khóa `self` cho mọi thuộc tính.

### Bài 2: Nâng cấp lớp `Sach` — mã sách, số đang mượn, số còn lại

* **Đề bài:** Nâng cấp `Sach` từ bài 1: thêm tham số `dang_muon=0` và `ma=None`; thêm `@property con_lai` trả về `so_luong - dang_muon`; cập nhật `__str__` hiển thị thêm trạng thái `con` (còn) hoặc `het` (hết).
* **Input:** Tạo sách: ma=1, ten="De Men Phieu Luu Ky", tac_gia="To Hoai", nam=1941, so_luong=10, dang_muon=3.
* **Output:**
  ```
  [1] De Men Phieu Luu Ky - To Hoai (1941) | con 7/10 cuon [con]
  Con lai: 7
  ```
* **Ví dụ:**
  ```
  # Tạo sách có 10 cuốn, đã mượn 3 -> còn 7
  ```
* **Gợi ý:** `@property` biến phương thức thành thuộc tính đọc được như biến; `con_lai > 0` thì trạng thái là `con`.

### Bài 3: Kết nối cơ sở dữ liệu SQLite

* **Đề bài:** Viết chương trình mở kết nối tới file `thu_vien.db` (file sẽ tự tạo), in ra phiên bản SQLite bằng câu lệnh `SELECT sqlite_version()`, rồi đóng kết nối.
* **Input:** Không có.
* **Output:** Một dòng dạng `Phien ban SQLite: 3.x.y` (con số tùy máy).
* **Ví dụ:**
  ```
  Phien ban SQLite: 3.45.1
  ```
* **Gợi ý:** `import sqlite3`; `sqlite3.connect("thu_vien.db")`; dùng `ket_noi.execute(...).fetchone()[0]` để lấy giá trị; đừng quên `ket_noi.close()`.

### Bài 4: Tạo bảng `Sach` trong database

* **Đề bài:** Mở kết nối `thu_vien.db`, tạo bảng `Sach` với 6 cột (`id` PRIMARY KEY AUTOINCREMENT, `ten` TEXT NOT NULL, `tac_gia` TEXT NOT NULL, `nam` INTEGER, `so_luong` INTEGER NOT NULL, `dang_muon` INTEGER NOT NULL DEFAULT 0), rồi in cấu trúc bảng bằng `PRAGMA table_info(Sach)`.
* **Input:** Không có.
* **Output:** Danh sách các cột (mỗi cột một tuple với id, tên, kiểu dữ liệu...).
* **Ví dụ:**
  ```
  (0, 'id', 'INTEGER', 0, None, 1)
  (1, 'ten', 'TEXT', 1, None, 0)
  ...
  ```
* **Gợi ý:** dùng `with ket_noi:` để câu lệnh `CREATE` được tự động COMMIT; `CREATE TABLE IF NOT EXISTS` an toàn khi chạy lại nhiều lần.

### Bài 5: Phương thức `them_sach` cho lớp `ThuVien`

* **Đề bài:** Tạo class `ThuVien` với `__init__(duong_dan_db="thu_vien.db")` (kết nối, đặt `row_factory = sqlite3.Row`, gọi tạo bảng) và phương thức `them_sach(sach)` dùng `INSERT INTO Sach (ten, tac_gia, nam, so_luong, dang_muon) VALUES (?, ?, ?, ?, ?)` — trả về mã sách mới tạo (`lastrowid`).
* **Input:** Tạo 2 đối tượng `Sach` rồi thêm vào thư viện.
* **Output:** Hai dòng `Da them sach co ma X` (mã tự tăng 1, 2...).
* **Ví dụ:**
  ```
  Da them sach co ma 1
  Da them sach co ma 2
  ```
* **Gợi ý:** dùng `with self.ket_noi:` bọc `execute` để tự COMMIT; `con_tro.lastrowid` lấy mã vừa tạo; truyền giá trị qua `?` — không ghép chuỗi.

### Bài 6: Phương thức `xem_danh_sach`

* **Đề bài:** Thêm vào `ThuVien` phương thức `xem_danh_sach()` chạy `SELECT * FROM Sach ORDER BY id` và trả về **list các dict** (mỗi dòng là `dict(dong)`). In kết quả ra màn hình sau khi thêm 2 sách.
* **Input:** Database có 2 sách (từ bài 5 — chạy lại bài 5 nếu chưa có).
* **Output:** Danh sách dict của 2 sách.
* **Ví dụ:**
  ```
  [{'id': 1, 'ten': 'De Men Phieu Luu Ky', 'tac_gia': 'To Hoai', 'nam': 1941, 'so_luong': 10, 'dang_muon': 0}, ...]
  ```
* **Gợi ý:** `fetchall()` trả list các `Row`; `dict(dong)` biến từng dòng thành từ điển nhờ `row_factory` đã đặt ở bài 5.

### Bài 7: Phương thức `_lay_sach` — lấy sách theo mã

* **Đề bài:** Thêm vào `ThuVien` phương thức `_lay_sach(ma)` dùng `SELECT * FROM Sach WHERE id = ?`, trả về dict của sách nếu có, **`None` nếu không có**. Kiểm thử với mã có thật và mã không tồn tại (ví dụ 999).
* **Input:** Database có sách mã 1.
* **Output:**
  ```
  Sach ma 1: {'id': 1, ...}
  Sach ma 999: None
  ```
* **Ví dụ:**
  ```
  # _lay_sach(1)  -> dict sách
  # _lay_sach(999) -> None
  ```
* **Gợi ý:** `fetchone()` trả `None` khi hết dòng; viết gọn: `return dict(dong) if dong else None`.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Tìm sách theo tên

* **Đề bài:** Thêm vào `ThuVien` phương thức `tim_theo_ten(ten_can_tim)` dùng `WHERE ten LIKE ?` với mẫu `%chuoi%` (bỏ khoảng trắng đầu/cuối bằng `strip()`), trả về list dict. Tìm chữ "de men".
* **Input:** Database có sách "De Men Phieu Luu Ky".
* **Output:** List chứa sách tìm thấy (rỗng nếu không có).
* **Ví dụ:**
  ```
  Tim 'de men': [{'id': 1, 'ten': 'De Men Phieu Luu Ky', ...}]
  ```
* **Gợi ý:** tham số truyền là `(f"%{ten_can_tim.strip()}%",)` — nhớ dấu phẩy để thành tuple; `LIKE` tìm "chứa", không cần nhập đúng cả tên.

### Bài 9: Tìm sách theo tác giả

* **Đề bài:** Thêm phương thức `tim_theo_tac_gia(tac_gia_can_tim)` tương tự bài 8 nhưng trên cột `tac_gia`. Tìm "hoai".
* **Input:** Database có sách tác giả "To Hoai".
* **Output:** List chứa sách của tác giả đó.
* **Ví dụ:**
  ```
  Tim 'hoai': [{'ten': 'De Men Phieu Luu Ky', 'tac_gia': 'To Hoai', ...}]
  ```
* **Gợi ý:** chỉ khác bài 8 ở tên cột trong `WHERE`; nên `ORDER BY id` cho kết quả ổn định.

### Bài 10: Sửa thông tin sách

* **Đề bài:** Thêm vào `ThuVien`:
  * Hằng số lớp `COT_HOP_LE = ("ten", "tac_gia", "nam", "so_luong")`.
  * Phương thức `sua_sach(ma, cot, gia_tri)`: nếu `cot` không nằm trong `COT_HOP_LE` thì `raise ValueError`; nếu sách không tồn tại trả `False`; ngược lại chạy `UPDATE Sach SET {cot} = ? WHERE id = ?` và trả `True`.
* **Input:** Sửa tên sách mã 1 thành "De Men Phieu Luu Ky (bia cung)".
* **Output:** `True`; sau đó `xem_danh_sach` thấy tên mới.
* **Ví dụ:**
  ```
  Sua thanh cong: True
  ```
* **Gợi ý:** cột chỉ được phép lấy từ danh sách hằng (chống SQL Injection vào tên cột); kiểm tra `_lay_sach(ma)` trước khi UPDATE.

### Bài 11: Xóa sách

* **Đề bài:** Thêm phương thức `xoa_sach(ma)` dùng `DELETE FROM Sach WHERE id = ?`: trả `True` nếu xóa được, `False` nếu mã không tồn tại. Kiểm thử xóa một sách rồi xem danh sách.
* **Input:** Database có sách mã 2.
* **Output:**
  ```
  Xoa sach 2: True
  Danh sach sau khi xoa chi con sach ma 1
  ```
* **Ví dụ:**
  ```
  Xoa sach 999: False
  ```
* **Gợi ý:** tương tự bài 10: kiểm tra tồn tại trước; dùng `with self.ket_noi:` cho lệnh DELETE.

### Bài 12: Mượn sách

* **Đề bài:** Thêm phương thức `muon_sach(ma)`:
  * Sách không tồn tại → trả `False`.
  * `dang_muon >= so_luong` (hết sách) → `raise ValueError("Sach nay da duoc muon het")`.
  * Còn sách → `UPDATE Sach SET dang_muon = dang_muon + 1 WHERE id = ?`, trả `True`.
  Kiểm thử mượn nhiều lần một sách có 2 cuốn.
* **Input:** Sách mã 1 có so_luong=2, dang_muon=0.
* **Output:**
  ```
  Lan 1: True
  Lan 2: True
  Lan 3: Loi: Sach nay da duoc muon het
  ```
* **Ví dụ:**
  ```
  Muon sach khong ton tai: False
  ```
* **Gợi ý:** dùng `_lay_sach(ma)` đọc kiểm tra trước, rồi mới UPDATE — đừng bỏ qua bước kiểm tra.

### Bài 13: Trả sách

* **Đề bài:** Thêm phương thức `tra_sach(ma)` ngược với bài 12:
  * Không tồn tại → `False`.
  * `dang_muon <= 0` → `raise ValueError("Khong co cuon nao dang muon de tra")`.
  * Ngược lại `UPDATE ... SET dang_muon = dang_muon - 1`, trả `True`.
  Kiểm thử trả khi chưa mượn và khi đang mượn.
* **Input:** Sách mã 1 đang có dang_muon=1 (vừa mượn ở bài 12).
* **Output:**
  ```
  Tra lan 1: True
  Tra lan 2: Loi: Khong co cuon nao dang muon de tra
  ```
* **Ví dụ:**
  ```
  Tra sach khong ton tai: False
  ```
* **Gợi ý:** đảo dấu của bài 12; kiểm tra `dang_muon <= 0` trước khi giảm để không ra số âm.

### Bài 14: Thống kê thư viện

* **Đề bài:** Thêm phương thức `thong_ke()` chạy `SELECT COUNT(*) AS so_dau, COALESCE(SUM(so_luong), 0) AS tong_cuon, COALESCE(SUM(dang_muon), 0) AS dang_muon FROM Sach` rồi thêm khóa `con_lai = tong_cuon - dang_muon`; trả về dict. Kiểm thử cả khi bảng trống.
* **Input:** Database có 2 sách: (3 cuốn, mượn 1) + (2 cuốn, mượn 0).
* **Output:**
  ```
  {'so_dau': 2, 'tong_cuon': 5, 'dang_muon': 1, 'con_lai': 4}
  ```
* **Ví dụ:**
  ```
  # Bảng trống -> {'so_dau': 0, 'tong_cuon': 0, 'dang_muon': 0, 'con_lai': 0}
  ```
* **Gợi ý:** `COALESCE` biến `NULL` (bảng trống) thành `0` — nếu bỏ nó, kết quả sẽ là `None`; `AS` đặt tên lại cho cột tính toán.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: In danh sách sách dạng bảng

* **Đề bài:** Viết hàm `in_bang_sach(danh_sach)` (không thuộc class nào) in bảng với 6 cột: `Ma`, `Ten`, `Tac gia`, `Nam`, `SL`, `Dang muon` — căn trái bằng f-string `:<N`, có dòng tiêu đề và đường gạch ngang. Nếu danh sách rỗng in "Khong co sach nao.".
* **Input:** Kết quả của `xem_danh_sach()` sau khi thêm 2 sách.
* **Output:**
  ```
  Ma  Ten                          Tac gia            Nam   SL   Dang muon
  ----------------------------------------------------------------------
  1   De Men Phieu Luu Ky          To Hoai            1941  3    1
  ```
* **Ví dụ:**
  ```
  # in_bang_sach([]) -> Khong co sach nao.
  ```
* **Gợi ý:** đặt độ rộng cho từng cột: `{'Ma':<4}`, `{'Ten':<28}`, `{'Tac gia':<18}`, `{'Nam':<6}`, `{'SL':<4}`, `{'Dang muon':<10}`; kẻ gạch bằng `"-" * len(tieu_de)`.

### Bài 16: Nhập liệu an toàn — không bao giờ cho phép gõ sai

* **Đề bài:** Viết 2 hàm (tầng `App`):
  * `nhap_so_nguyen(loi_nhan)`: lặp đến khi người dùng gõ đúng số nguyên (bắt `ValueError`).
  * `nhap_sach_moi()`: nhập tên/tác giả **không được rỗng** (hỏi lại nếu rỗng), năm và số lượng là số nguyên, `so_luong` phải `>= 0`; trả về đối tượng `Sach`.
* **Input:** Người dùng gõ: tên rỗng (Enter), rồi "De Men", tác giả "To Hoai", năm "abc" rồi "1941", số lượng "3".
* **Output:** Chương trình hỏi lại mỗi lần gõ sai và cuối cùng tạo được `Sach` hợp lệ.
* **Ví dụ:**
  ```
  Ten sach:                (gõ Enter -> hỏi lại)
  Ten sach khong duoc rong, nhap lai: De Men
  Nam xuat ban: abc        (gõ chữ -> hỏi lại)
  Vui long nhap mot so nguyen hop le.
  Nam xuat ban: 1941
  ```
* **Gợi ý:** kết hợp `while True` + `try/except ValueError`; với chuỗi rỗng dùng `while not ten: ten = input(...)`. Chưa cần đưa vào `App`, viết dưới dạng hàm độc lập cũng được.

### Bài 17: Xử lý lỗi toàn diện cho mượn/trả

* **Đề bài:** Viết hàm `xu_ly_muon_tra(thu_vien, ma, loai)` trong đó `loai` là `"muon"` hoặc `"tra"`: gọi phương thức tương ứng trong `try/except`, bắt `ValueError` để in `"Loi: ..."`; `False` thì in "Khong tim thay sach". Kiểm thử: mượn sách không tồn tại, mượn đến khi hết sách, trả sách khi không có gì để trả — chương trình **không được gãy**.
* **Input:** Sách mã 1 có 1 cuốn.
* **Output:**
  ```
  Muon: Thanh cong.
  Muon: Loi: Sach nay da duoc muon het
  Tra: Thanh cong.
  Tra: Loi: Khong co cuon nao dang muon de tra
  Muon sach 999: Khong tim thay sach
  ```
* **Ví dụ:**
  ```
  # Cả 5 tình huống trên đều kết thúc bằng lệnh print, không có traceback
  ```
* **Gợi ý:** `except ValueError as loi: print("Loi:", loi)`; phân biệt hai tầng: `return False` (không tồn tại) và `raise ValueError` (vi phạm nghiệp vụ).

### Bài 18: Menu hoàn chỉnh

* **Đề bài:** Xây dựng class `App` với:
  * `__init__` tạo `self.thu_vien = ThuVien()`.
  * `in_menu()` in menu 9 chức năng + thoát.
  * `chay()`: vòng `while True` đọc lựa chọn, dùng `if/elif` gọi đúng phương thức (tích hợp `nhap_so_nguyen`, `nhap_sach_moi`, `in_bang_sach`, `xu_ly_muon_tra`); chọn "0" thì đóng kết nối và `break`; lựa chọn khác in "Lua chon khong hop le.".
  * `if __name__ == "__main__": App().chay()`.
* **Input:** Người dùng chọn lần lượt: 1 (thêm sách), 2 (xem), 9 (thống kê), 0 (thoát).
* **Output:** Mỗi thao tác in kết quả đúng chức năng; chương trình thoát sạch sẽ khi chọn 0.
* **Ví dụ:**
  ```
  ===== QUAN LY THU VIEN =====
  1. Them sach        6. Tra sach
  ...
  0. Thoat
  Chon chuc nang: 2
  ```
* **Gợi ý:** mỗi nhánh `elif` chỉ nên dài 2-4 dòng — nếu dài hơn, tách hàm riêng (ví dụ `xu_ly_sua_sach`, `xu_ly_thong_ke`); đừng quên `self.thu_vien.dong_ket_noi()` sau vòng lặp.

### Bài 19: Tối ưu hóa + tìm kiếm tổng hợp

* **Đề bài:** Tối ưu lại chương trình:
  1. Đưa tên file DB vào hằng số `TEN_FILE_DB = "thu_vien.db"` và cho `ThuVien.__init__` dùng nó làm giá trị mặc định.
  2. Viết docstring đầy đủ cho mọi class và phương thức.
  3. Thêm phương thức `tim_tong_hop(chuoi)` dùng `WHERE ten LIKE ? OR tac_gia LIKE ?` — tìm sách theo cả tên lẫn tác giả.
  4. Kiểm tra mọi câu SQL đều dùng `?` placeholder.
* **Input:** Tìm "hoai" (là tác giả) và "de men" (là tên).
* **Output:** Cả hai đều tìm được sách — không cần biết người dùng nhớ tên hay tác giả.
* **Ví dụ:**
  ```
  Tim 'hoai' -> [{'ten': 'De Men Phieu Luu Ky', ...}]
  Tim 'de men' -> [{'ten': 'De Men Phieu Luu Ky', ...}]
  ```
* **Gợi ý:** `WHERE ten LIKE ? OR tac_gia LIKE ?` với cùng một tham số `f"%{chuoi.strip()}%"` truyền hai lần; hằng số giúp đổi tên DB ở đúng một chỗ.

### Bài 20: Dự án hoàn chỉnh + kịch bản kiểm thử tổng thể

* **Đề bài:** Ghép toàn bộ các bài 1–19 thành chương trình hoàn chỉnh `quan_ly_thu_vien.py` (class `Sach`, `ThuVien`, `App`), sau đó **chạy kịch bản kiểm thử** sau và ghi lại kết quả:
  1. Thêm 3 sách: "De Men Phieu Luu Ky" (3 cuốn), "Tuoi tho du doi" (2 cuốn), "Nha Gia Kim" (1 cuốn).
  2. Xem danh sách → đúng 3 sách.
  3. Mượn sách 1 ba lần → lần 4 báo hết sách nhưng không gãy.
4. Mượn sách 3 → xem lại → `dang_muon` của sách 1 và 3 tăng.
5. Trả sách 1 một lần.
6. Thống kê → kiểm tra số liệu khớp.
7. Xóa sách 2 → danh sách còn 2 sách.
8. Thoát → chạy lại chương trình → dữ liệu vẫn còn (SQLite bền vững).
* **Input:** Các bước theo kịch bản trên.
* **Output:** Toàn bộ màn hình phiên chạy 1 và phiên chạy 2 (để chứng minh dữ liệu bền vững).
* **Ví dụ:**
  ```
  ----- THONG KE THU VIEN -----
  So dau sach      : 3
  Tong so cuon     : 6
  Dang duoc muon   : 3
  Con lai tren ke  : 3
  ```
* **Gợi ý:** nếu còn bí ở bất kỳ phần nào, tham khảo **[CODE HOÀN CHỈNH](./dap_an.md)** ở cuối file đáp án — đối chiếu từng phần với bài làm của mình; đừng copy nguyên si khi chưa hiểu!

---

## 🎯 Tổng kết

Bạn vừa hoàn thành **bài tập cuối cùng** của khóa học — 20 bài tập dẫn bạn đi từ một class 20 dòng đến một ứng dụng quản lý thư viện hoàn chỉnh với OOP + SQLite. Đây chính là bài tổng hợp toàn diện nhất: nếu làm được hết, bạn đã sẵn sàng cho những dự án thật sự!

👉 Xem **[Đáp án và CODE HOÀN CHỈNH](./dap_an.md)** để đối chiếu bài làm của mình.
