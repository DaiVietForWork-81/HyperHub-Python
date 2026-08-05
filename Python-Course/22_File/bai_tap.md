# 📝 Bài 22: Bài Tập – Đọc Và Ghi File

> 🎯 **Chủ đề:** `open()` với các mode `r/w/a`, `read/readline/readlines`, `write/writelines`, `with` statement, `encoding="utf-8"`, xử lý lỗi file.

---

## 📌 Hướng dẫn làm bài

* ✅ **Mọi bài tập phải mở file bằng `with open(...)` và kèm `encoding="utf-8"`.**
* ✅ Nếu bài đọc một file dữ liệu, hãy **tự tạo file dữ liệu đó trước** trong code (dùng mode `"w"`) — vừa tránh lỗi `FileNotFoundError`, vừa dễ kiểm tra.
* ✅ Đọc từng dòng nhớ dùng `dong.strip()` để bỏ ký tự xuống dòng.
* ✅ Đáp án chi tiết 20 bài: 👉 [xem file dap_an.md](dap_an.md)

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Ghi rồi đọc lại

* **Đề bài:** Ghi chuỗi `Xin chao the gioi Python!` vào file `hello.txt` (mode `"w"`), sau đó đọc lại toàn bộ bằng `read()` và in ra màn hình.
* **Input:** Không có.
* **Output:**
  ```
  Xin chao the gioi Python!
  ```
* **Gợi ý:** `with open("hello.txt", "w", encoding="utf-8") as f: f.write(...)`.

### Bài 2: Ghi nhiều dòng

* **Đề bài:** Ghi 3 dòng `Toan`, `Van`, `Anh` vào file `mon_hoc.txt` (mỗi dòng là một lệnh `write` kèm `\n`), rồi đọc lại và in.
* **Input:** Không có.
* **Output:**
  ```
  Mon: Toan
  Mon: Van
  Mon: Anh
  ```
* **Gợi ý:** Đọc bằng vòng lặp `for dong in f` và `dong.strip()`.

### Bài 3: Đọc toàn bộ bằng `read()`

* **Đề bài:** Tạo file `tho.txt` gồm 2 câu thơ, đọc bằng `read()` và in ra — kèm in số ký tự trong file.
* **Input:** Không có.
* **Output:**
  ```
  Rung xanh la biec
  Chim hot trong cay
  So ky tu: 37
  ```
* **Gợi ý:** `len(noi_dung)` đếm ký tự; nhớ đếm cả dấu xuống dòng `\n`.

### Bài 4: Mode `"a"` — ghi thêm

* **Đề bài:** Ghi 2 dòng vào `nhat_ky.txt`, đóng lại. Mở lại với mode `"a"` ghi thêm 1 dòng. Đọc lại và in toàn bộ để chứng minh dữ liệu cũ vẫn còn.
* **Input:** Không có.
* **Output:**
  ```
  Buoi sang: hoc Python
  Buoi chieu: lam bai tap
  Buoi toi: on lai bai
  ```
* **Gợi ý:** Mode `"a"` không xóa dữ liệu cũ; đọc bằng `read()` sau khi ghi xong.

### Bài 5: `readlines()` và đếm dòng

* **Đề bài:** Tạo file `hs.txt` gồm 4 dòng tên học sinh. Dùng `readlines()` đọc list các dòng, in số dòng và từng dòng đã bỏ khoảng trắng.
* **Input:** Không có.
* **Output:**
  ```
  So dong: 4
  An
  Binh
  Cuong
  Dung
  ```
* **Gợi ý:** `len(danh_sach_dong)`; mỗi dòng dùng `.strip()`.

### Bài 6: Ghi danh sách học sinh

* **Đề bài:** Có list 3 tuple `("Ten", "Lop")`. Ghi vào file `hoc_sinh.txt` dạng `Ten,Lop` (mỗi học sinh một dòng), rồi đọc lại in ra màn hình.
* **Input:** Không có.
* **Output:**
  ```
  Nguyen Van An,10A1
  Tran Thi Mai,10A1
  Le Quang Binh,10A2
  ```
* **Gợi ý:** Vòng lặp `for ten, lop in danh_sach:` + `f.write(f"{ten},{lop}\n")`.

### Bài 7: `readline()` lần lượt

* **Đề bài:** Tạo file `tinh.txt` 3 dòng. Dùng `readline()` đọc đúng 2 dòng đầu, in ra dòng 1 và dòng 2.
* **Input:** Không có.
* **Output:**
  ```
  Dong 1: Python
  Dong 2: la
  ```
* **Gợi ý:** Mỗi lần gọi `readline()` đọc một dòng theo thứ tự.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Đọc điểm từ file

* **Đề bài:** Tạo file `diem.txt` dạng `Ten,Toan,Van,Anh` cho 3 học sinh. Đọc file, tính điểm trung bình mỗi bạn và in ra `Ten: TB` (2 chữ số thập phân).
* **Input:** Không có.
* **Output:**
  ```
  Nguyen Van An: 8.17
  Tran Thi Mai: 6.50
  Le Quang Binh: 5.00
  ```
* **Gợi ý:** `phan = dong.split(",")`; chuyển điểm bằng `float(...)`.

### Bài 9: Bắt lỗi file không tồn tại

* **Đề bài:** Viết chương trình đọc file `khong_co.txt` (chưa từng được tạo) bằng `try/except`, bắt `FileNotFoundError` và in thông báo thân thiện, chương trình **không sập**.
* **Input:** Không có.
* **Output:**
  ```
  File khong ton tai! Hay kiem tra lai ten file.
  ```
* **Gợi ý:** Đặt `with open(...)` bên trong `try`, bắt lỗi trong `except FileNotFoundError`.

### Bài 10: Nhật ký đơn giản

* **Đề bài:** Viết hàm `ghi_log(thong_diep)` dùng mode `"a"`, mỗi dòng có dạng `[gio_hien_tai] thong_diep` (dùng `datetime.now().strftime("%H:%M:%S")`). Gọi hàm 3 lần với 3 sự kiện mẫu, rồi đọc lại và in.
* **Input:** Không có.
* **Output (thời gian có thể khác):**
  ```
  [10:15:22] Chuong trinh khoi dong
  [10:15:22] Xu ly du lieu
  [10:15:22] Ket thuc
  ```
* **Gợi ý:** `from datetime import datetime`; thời gian lấy trong lúc gọi hàm.

### Bài 11: Đếm dòng và chữ

* **Đề bài:** Tạo file `van_ban.txt` gồm 3 câu ngắn. Đọc file, in ra số dòng và tổng số từ (mỗi từ ngăn cách bởi khoảng trắng).
* **Input:** Không có.
* **Output:**
  ```
  So dong: 3
  So tu: 6
  ```
* **Gợi ý:** `len(dong.split())` đếm từ trong một dòng.

### Bài 12: Bảng cửu chương ra file

* **Đề bài:** Ghi bảng cửu chương nhân 5 (từ 1 đến 10) vào file `bang_5.txt` bằng vòng lặp `for` + `write`, rồi đọc lại in ra màn hình.
* **Input:** Không có.
* **Output:**
  ```
  5 x 1 = 5
  5 x 2 = 10
  ...
  5 x 10 = 50
  ```
* **Gợi ý:** `f.write(f"5 x {i} = {5 * i}\n")` trong vòng lặp `range(1, 11)`.

### Bài 13: Tìm kiếm trong file

* **Đề bài:** Tạo file `lop.txt` gồm 4 tên học sinh. Đọc từng dòng và in ra những bạn có tên **chứa chữ "An"**.
* **Input:** Không có.
* **Output:**
  ```
  Tim thay: Nguyen Van An
  Tim thay: Pham Thi Anh
  ```
* **Gợi ý:** Điều kiện `if "An" in dong`.

### Bài 14: Xóa dòng trống

* **Đề bài:** Tạo file `lo_xinh.txt` gồm 4 dòng, trong đó có 1 dòng trống ở giữa. Đọc file, ghi các dòng **có nội dung** vào file mới `sach.txt`, rồi in nội dung file mới.
* **Input:** Không có.
* **Output:**
  ```
  Dong 1
  Dong 2
  Dong 4
  ```
* **Gợi ý:** Sau khi `strip()`, nếu chuỗi rỗng thì `continue`.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Nâng điểm cho học sinh

* **Đề bài:** File `diem.txt` dạng `Ten,Toan` cho 4 bạn (tự tạo). Đọc file, bạn nào điểm Toán **nhỏ hơn 9.0** thì cộng thêm 2 (không quá 10), ghi **lại toàn bộ** vào file (mode `"w"`), rồi đọc lại in kết quả.
* **Input:** Không có.
* **Output:**
  ```
  Sau khi nang diem:
  An,7.5
  Binh,5.0
  Cuong,10.0
  Dung,6.0
  ```
* **Gợi ý:** Đọc vào list, chỉnh sửa trong list, ghi lại từ đầu bằng `"w"`.

### Bài 16: Ghép hai file

* **Đề bài:** Tạo 2 file `hs_10a.txt` và `hs_10b.txt`, mỗi file 2 tên học sinh. Đọc cả hai và gộp vào file `hs_ca_khoi.txt`, in ra tổng số học sinh và nội dung file gộp.
* **Input:** Không có.
* **Output:**
  ```
  Tong so hoc sinh: 4
  An
  Binh
  Cuong
  Dung
  ```
* **Gợi ý:** Ghi bằng mode `"a"` cho lần thứ hai, hoặc gom list rồi ghi một lần.

### Bài 17: Phân loại và ghi kết quả

* **Đề bài:** File `diem.txt` dạng `Ten,Toan,Van,Anh` (3 bạn, tự tạo). Đọc, tính điểm TB, xếp loại (≥8 Giỏi, ≥6.5 Khá, ≥5 Trung bình, còn lại Yếu), ghi vào file `xep_loai.txt` dạng `Ten: Loai`, rồi in nội dung file kết quả.
* **Input:** Không có.
* **Output:**
  ```
  Nguyen Van An: Gioi
  Tran Thi Mai: Kha
  Le Quang Binh: Yeu
  ```
* **Gợi ý:** Ghi file kết quả bằng `"w"`; từng bước: đọc → tính → ghi → in.

### Bài 18: Sổ tay ghi chú

* **Đề bài:** Viết chương trình: list ghi chú mẫu gồm 3 chuỗi, ghi toàn bộ vào `so_tay.txt` (mỗi ghi chú một dòng, có dấu `-` đầu dòng). Mở lại file, in số ghi chú và từng ghi chú.
* **Input:** Không có.
* **Output:**
  ```
  So ghi chu: 3
  - Mua sach Python
  - Lam bai tap bai 22
  - On lai bai 21
  ```
* **Gợi ý:** Dùng `writelines` với list đã có sẵn dấu `-` và `\n`.

### Bài 19: Nhật ký lỗi

* **Đề bài:** Viết hàm `ghi_log(thong_diep)` dùng `with` + `"a"` + `encoding`. Mô phỏng 3 sự kiện: 2 sự kiện bình thường, 1 sự kiện dạng `LOI: ...`. Đọc lại file và chỉ in ra các dòng chứa chữ `LOI`.
* **Input:** Không có.
* **Output:**
  ```
  LOI: File diem.txt khong doc duoc
  ```
* **Gợi ý:** Khi đọc lại, dùng `if "LOI" in dong` để lọc.

### Bài 20: Quản lý điểm lưu file (tiểu dự án)

* **Đề bài:** Xây dựng chương trình hoàn chỉnh:
  1. Tạo file `quan_ly_diem.txt` với 4 học sinh, mỗi dòng `Ten,Toan,Van,Anh`.
  2. Đọc file (có `try/except` bắt `FileNotFoundError`), tính TB và xếp loại từng bạn.
  3. Ghi bảng tổng kết `Ten - TB - Loai` vào file `tong_ket.txt`.
  4. In cả bảng tổng kết ra màn hình và in dòng chữ `Da ghi ket qua vao tong_ket.txt`.
* **Input:** Không có.
* **Output:**
  ```
  Nguyen Van An - 8.17 - Gioi
  Tran Thi Mai - 6.50 - Kha
  Le Quang Binh - 5.00 - Trung binh
  Pham Thu Ha - 8.50 - Gioi
  Da ghi ket qua vao tong_ket.txt
  ```
* **Gợi ý:** Gộp toàn bộ kiến thức bài: tạo file, đọc, tính, ghi kết quả, bắt lỗi.

---

## 🎯 Tổng kết sau khi làm bài

* ✅ Viết được chương trình ghi và đọc file với `with` + `encoding="utf-8"`.
* ✅ Phân biệt rõ `"r"`, `"w"`, `"a"` và chọn đúng mode cho từng việc.
* ✅ Xử lý được `FileNotFoundError` không cho chương trình sập.
* ✅ Xây dựng được ứng dụng nhỏ lưu dữ liệu (điểm, log, ghi chú) ra file.

> 💪 Khi dữ liệu đã "sống lâu dài" trên đĩa, đã đến lúc tổ chức nó đẹp đẽ hơn bằng **lớp (class)**!

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 23: Lập Trình Hướng Đối Tượng](../23_OOP/bai_giang.md)**
