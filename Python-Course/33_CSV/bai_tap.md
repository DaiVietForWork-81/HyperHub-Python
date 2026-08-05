# 📝 Bài 33: Bài Tập – CSV

> 📋 **Chương 10 – Dữ liệu và mạng**
> Bạn đã học cách đọc/ghi file CSV bằng `csv.reader`, `csv.writer`, `csv.DictReader`, `csv.DictWriter`. Giờ hãy thực hành với các tình huống thực tế: danh sách học viên, bảng điểm, xuất dữ liệu ra file.
>
> 💡 **Lưu ý:** Hãy tự làm trước, chỉ xem đáp án sau khi đã thử hết sức. Đáp án nằm ở file `dap_an.md` cùng thư mục.
>
> ⚠️ **Mẹo chung:** Khi chạy đáp án, mỗi bài tự tạo file dữ liệu mẫu rồi xử lý — chương trình sẽ chạy được ngay trên máy bạn.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Ghi danh sách môn học

* **Đề bài:** Dùng `csv.writer` ghi danh sách các môn học của trường ra file `mon_hoc.csv`. Mỗi môn một dòng, cột đầu là mã môn, cột sau là tên môn.
* **Input:** Danh sách mã môn: `"TOAN", "VAN", "TIN"` kèm tên: `"Toán", "Ngữ văn", "Tin học"`.
* **Output:** File `mon_hoc.csv` với 3 dòng dữ liệu (không cần tiêu đề).
* **Ví dụ:**
  ```
  TOAN,Toán
  VAN,Ngữ văn
  TIN,Tin học
  ```
* **Gợi ý:** Tạo danh sách các dòng, mỗi dòng là một list hai phần tử; dùng `with open(...)` với `newline=""`.

### Bài 2: Đọc file và in từng dòng

* **Đề bài:** Đọc file `mon_hoc.csv` (tạo ở bài 1) bằng `csv.reader` và in từng dòng ra màn hình dưới dạng list.
* **Input:** File `mon_hoc.csv` có sẵn.
* **Output:**
  ```
  ['TOAN', 'Toán']
  ['VAN', 'Ngữ văn']
  ['TIN', 'Tin học']
  ```
* **Gợi ý:** Mở file với `encoding="utf-8"`, tạo `csv.reader(f)` rồi `for dong in doc: print(dong)`.

### Bài 3: Ghi danh sách học viên

* **Đề bài:** Dùng `csv.writer` ghi danh sách 3 học viên (tên, lớp) ra file `hoc_vien.csv`.
* **Input:** `"An"` – `"10A1"`, `"Binh"` – `"10A2"`, `"Chi"` – `"10A1"`.
* **Output:** File `hoc_vien.csv` có dòng tiêu đề `ten,lop` và 3 dòng dữ liệu.
* **Gợi ý:** Dòng đầu tiên là tiêu đề cột, sau đó mới đến dữ liệu; mỗi lần ghi một dòng bằng `writerow(...)`.

### Bài 4: In tên và điểm bằng DictReader

* **Đề bài:** Đọc file `bang_diem.csv` (có tiêu đề `ten,diem`) bằng `csv.DictReader`, in ra mỗi dòng dạng `ten - diem`.
* **Input:**
  ```csv
  ten,diem
  An,8
  Binh,7
  Chi,9
  ```
* **Output:**
  ```
  An - 8
  Binh - 7
  Chi - 9
  ```
* **Gợi ý:** Truy cập cột bằng tên khóa: `dong["ten"]`, `dong["diem"]`.

### Bài 5: Xuất bảng điểm bằng DictWriter

* **Đề bài:** Dùng `csv.DictWriter` ghi danh sách học viên dạng dict (tên, lớp, điểm) ra file `bang_diem_moi.csv`, có dòng tiêu đề.
* **Input:** Danh sách dict: `{"ten": "An", "lop": "10A1", "diem": 8}`, `{"ten": "Binh", "lop": "10A2", "diem": 7}`.
* **Output:** File `bang_diem_moi.csv` với tiêu đề `ten,lop,diem` và 2 dòng dữ liệu.
* **Gợi ý:** `fieldnames=["ten", "lop", "diem"]`, gọi `writeheader()` trước khi `writerow()`.

### Bài 6: Đọc file dấu chấm phẩy

* **Đề bài:** Đọc file `du_lieu_vn.csv` dùng dấu `;` làm phân cách, in từng dòng ra màn hình.
* **Input:**
  ```csv
  ten;lop
  An;10A1
  Binh;10A2
  ```
* **Output:** Các list tương ứng với từng dòng.
* **Gợi ý:** Truyền tham số `delimiter=";"` cho `csv.reader`.

### Bài 7: Đếm số học viên

* **Đề bài:** Đọc file `hoc_vien.csv` (bài 3) bằng `csv.reader`, đếm xem có bao nhiêu học viên (không tính dòng tiêu đề).
* **Input:** File `hoc_vien.csv` có tiêu đề `ten,lop` + 3 dòng dữ liệu.
* **Output:** `So hoc vien: 3`
* **Gợi ý:** Dùng `next(doc)` để bỏ qua dòng tiêu đề, đếm các dòng còn lại trong vòng `for`.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Tính điểm trung bình từng học viên

* **Đề bài:** Đọc file `bang_diem.csv` (tiêu đề `ten,van,toan`), tính trung bình 2 môn của từng học viên và in ra.
* **Input:**
  ```csv
  ten,van,toan
  An,8,9
  Binh,7,6
  Chi,9,10
  ```
* **Output:**
  ```
  An: 8.5
  Binh: 6.5
  Chi: 9.5
  ```
* **Gợi ý:** Giá trị đọc từ CSV là chuỗi — nhớ ép kiểu `float()` trước khi cộng.

### Bài 9: Lọc học viên điểm cao

* **Đề bài:** Đọc file `bang_diem.csv` (tiêu đề `ten,diem`), in ra tên các học viên có điểm từ 8 trở lên.
* **Input:**
  ```csv
  ten,diem
  An,8
  Binh,7
  Chi,9
  Duong,6
  ```
* **Output:**
  ```
  An
  Chi
  ```
* **Gợi ý:** Dùng `csv.DictReader` + điều kiện `float(dong["diem"]) >= 8`.

### Bài 10: Tìm học viên điểm cao nhất

* **Đề bài:** Đọc file `bang_diem.csv` (tiêu đề `ten,diem`), tìm và in tên học viên có điểm cao nhất kèm số điểm.
* **Input:**
  ```csv
  ten,diem
  An,8
  Binh,7
  Chi,9
  ```
* **Output:** `Chi dat diem cao nhat: 9`
* **Gợi ý:** Lưu biến `ten_max` và `diem_max`, cập nhật khi gặp điểm lớn hơn.

### Bài 11: Xuất CSV thêm cột tổng và trung bình

* **Đề bài:** Đọc file `bang_diem.csv` (tiêu đề `ten,van,toan`), thêm cột `tong` (tổng 2 môn) và `tb` (trung bình) rồi ghi ra file `bang_diem_tong.csv`.
* **Input:**
  ```csv
  ten,van,toan
  An,8,9
  Binh,7,6
  ```
* **Output:** File `bang_diem_tong.csv` với tiêu đề `ten,van,toan,tong,tb`.
* **Gợi ý:** Đọc hết vào list dict, tính toán thêm khóa mới, rồi `csv.DictWriter` với `fieldnames` đầy đủ.

### Bài 12: Xếp loại học lực

* **Đề bài:** Đọc file `bang_diem_tong.csv` (bài 11), xếp loại theo điểm TB: `>= 8` là "Gioi", `>= 6.5` là "Kha", còn lại là "TB". Xuất ra file `xep_loai.csv` thêm cột `loai`.
* **Input:** File `bang_diem_tong.csv` từ bài 11.
* **Output:** File `xep_loai.csv` có cột `loai` tương ứng.
* **Gợi ý:** Dùng câu lệnh `if/elif/else` trên `float(hs["tb"])`.

### Bài 13: Chuyển JSON sang CSV

* **Đề bài:** Bạn có danh sách sản phẩm dạng JSON (list dict với các trường `ten`, `gia`, `so_luong`). Dùng `json.loads` (bài 32) để đọc, rồi ghi ra file `san_pham.csv` bằng `csv.DictWriter`.
* **Input:** Chuỗi JSON: `[{"ten": "Vo", "gia": 5000, "so_luong": 10}, {"ten": "But", "gia": 3000, "so_luong": 15}]`.
* **Output:** File `san_pham.csv` với tiêu đề `ten,gia,so_luong`.
* **Gợi ý:** `json.loads(chuoi)` trả list dict; ghi bằng `csv.DictWriter(f, fieldnames=["ten", "gia", "so_luong"])`.

### Bài 14: Cộng điểm hai file CSV

* **Đề bài:** File `diem_van.csv` (tiêu đề `ten,diem`) và file `diem_toan.csv` (tiêu đề `ten,diem`) của cùng danh sách học viên. Đọc cả hai, ghép theo tên và ghi file `diem_tong.csv` với tiêu đề `ten,van,toan,tb`.
* **Input:** Hai file có cùng các tên học viên (có thể khác thứ tự).
* **Output:** File `diem_tong.csv` gồm đủ 3 học viên.
* **Gợi ý:** Đọc từng file thành dict `{ten: diem}`, lặp qua danh sách tên của file thứ nhất.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Thống kê theo lớp

* **Đề bài:** Đọc file `hoc_sinh.csv` (tiêu đề `ten,lop,diem`), tính số lượng học viên và điểm trung bình của từng lớp. In kết quả.
* **Input:**
  ```csv
  ten,lop,diem
  An,10A1,8
  Binh,10A2,7
  Chi,10A1,9
  Dung,10A2,5
  Em,10A1,6
  ```
* **Output:**
  ```
  10A1: 3 hoc vien, diem TB 7.67
  10A2: 2 hoc vien, diem TB 6.00
  ```
* **Gợi ý:** Dùng dict với khóa là tên lớp, giá trị là [tổng điểm, số lượng]; làm tròn 2 chữ số bằng `round(x, 2)`.

### Bài 16: Gộp nhiều file CSV

* **Đề bài:** Có 3 file `lop_a.csv`, `lop_b.csv`, `lop_c.csv` (cùng tiêu đề `ten,diem`). Gộp toàn bộ dữ liệu vào một file `tat_ca.csv` (chỉ một dòng tiêu đề duy nhất).
* **Input:** 3 file với mỗi file 2–3 học viên.
* **Output:** File `tat_ca.csv` có đầy đủ học viên của 3 lớp.
* **Gợi ý:** Mở file đích ở chế độ `"w"` một lần, ghi tiêu đề rồi mở từng file nguồn bằng `csv.reader`; dùng `next(doc)` để bỏ tiêu đề của file nguồn.

### Bài 17: Cập nhật điểm trong CSV

* **Đề bài:** Đọc file `bang_diem.csv` (tiêu đề `ten,diem`), học viên nào điểm dưới 7 được cộng thêm 1 điểm (không vượt quá 10). Ghi kết quả đè lại chính file đó.
* **Input:**
  ```csv
  ten,diem
  An,8
  Binh,6
  Chi,9
  Duong,5
  ```
* **Output:** Trong file: Binh thành 7, Duong thành 6; An, Chi giữ nguyên.
* **Gợi ý:** Đọc hết vào list, sửa giá trị rồi ghi lại với `newline=""`; dùng `min(diem + 1, 10)`.

### Bài 18: Kiểm tra file CSV hợp lệ

* **Đề bài:** File `du_lieu.txt` có các dòng, dòng nào có đúng 3 cột là hợp lệ, dòng nào khác số cột là lỗi. Viết chương trình đọc (dùng `csv.reader`) và in kết quả kiểm tra từng dòng.
* **Input:**
  ```
  ten,lop,diem
  An,10A1,8
  Binh,10A2
  Chi,10A1,9
  Dung,10A2,7
  ```
* **Output:**
  ```
  Dong 1 (tieu de): 3 cot - OK
  Dong 2: 3 cot - OK
  Dong 3: 2 cot - LOI
  Dong 4: 3 cot - OK
  Dong 5: 3 cot - OK
  ```
* **Gợi ý:** `len(dong)` chính là số cột của dòng đó; đếm số thứ tự dòng bằng biến đếm trong vòng lặp.

### Bài 19: Chuyển đổi mã hóa và dấu phân cách

* **Đề bài:** File `excel_vn.csv` do Excel tiếng Việt xuất ra: mã hóa `utf-8-sig`, dấu phân cách `;`, tiêu đề `ho_ten;lop;diem`. Đọc đúng file này và ghi ra file `chuan.csv` chuẩn hóa: mã hóa `utf-8`, dấu phân cách `,`.
* **Input:**
  ```csv
  ho_ten;lop;diem
  Nguyễn Văn An;10A1;8
  Trần Thị Bình;10A2;7
  ```
* **Output:** File `chuan.csv` với dấu `,`, mở bằng Excel không loạn dấu.
* **Gợi ý:** Đọc với `encoding="utf-8-sig"` + `delimiter=";"`, ghi với `encoding="utf-8"` + `newline=""` (dấu `,` là mặc định).

### Bài 20: Hệ thống quản lý điểm (Mini Project)

* **Đề bài:** Xây dựng chương trình quản lý điểm một lớp học:
  1. Tạo danh sách 5 học viên (tên, lớp, điểm 3 môn Toán – Văn – Anh).
  2. Ghi file `bang_diem_day_du.csv` gồm cột `ten,lop,toan,van,anh,tong,tb,xep_loai`.
  3. Đọc lại file, xếp hạng học viên theo điểm TB từ cao xuống thấp, in bảng xếp hạng kèm hạng `1, 2, 3...`.
* **Input:** Danh sách học viên tự chọn (5 bạn).
* **Output:** File CSV đầy đủ + bảng xếp hạng in ra màn hình.
* **Gợi ý:** Sắp xếp bằng `sorted(danh_sach, key=lambda hs: float(hs["tb"]), reverse=True)`; dùng `enumerate` để gán thứ hạng.

---

## 🎯 Tổng kết

Chúc mừng bạn đã hoàn thành 20 bài tập về CSV! Bạn đã luyện:

* ✅ Đọc/ghi CSV cơ bản (`reader`, `writer`) và theo tên cột (`DictReader`, `DictWriter`).
* ✅ Xử lý dấu phân cách `;`, mã hóa tiếng Việt `utf-8-sig`, `cp1258`.
* ✅ Các tình huống thực tế: bảng điểm, danh sách học viên, xếp loại, xếp hạng, gộp và chuyển đổi file.

👉 Kiểm tra đáp án tại **[dap_an.md](dap_an.md)**.

Tiếp theo, bạn sẽ ra ngoài "thế giới mạng" — học về **API** để lấy dữ liệu từ các dịch vụ trực tuyến:

👉 **[Bài 34: API – Giao Tiếp Giữa Các Chương Trình](../34_API/bai_giang.md)**
