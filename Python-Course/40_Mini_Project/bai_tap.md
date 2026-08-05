# 📝 Bài 40: Bài Tập – Mini Project Quản Lý Cửa Hàng Sách

> 🎯 **Chủ đề:** Xây dựng từng phần của ứng dụng "Quản lý cửa hàng sách": dữ liệu, CRUD, tìm kiếm, thống kê, menu, lưu/đọc file JSON.
>
> 📌 **Lưu ý:** Các bài từ 1 đến 14 là **hàm độc lập** (thử bằng lời gọi mẫu). Các bài từ 15 đến 20 là **ghép vào chương trình menu** (có `input()` — hãy gõ giá trị mẫu). Nếu chưa làm được, hãy xem lại bài giảng — **đáp án chi tiết ở [dap_an.md](dap_an.md)**.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Tạo dữ liệu sách

* **Đề bài:** Viết hàm `tao_sach(ma: int, ten: str, tac_gia: str, the_loai: str, gia: float, so_luong: int) -> Dict[str, object]` trả dict sách. Tạo 2 cuốn (mã 1, 2) và in `"Cuon dau: <ten>"`.
* **Input:** Không có.
* **Output:**
  ```
  Cuon dau: De Men Phieu Luu Ky
  ```
* **Gợi ý:** `return {"ma": ma, "ten": ten, ...}` (ôn bài 17).

### Bài 2: Hiển thị kho rỗng

* **Đề bài:** Viết hàm `hien_thi_danh_sach(danh_sach: List[Dict[str, object]]) -> None` in `"Kho dang rong."` nếu danh sách rỗng.
* **Input:** Không có.
* **Output:**
  ```
  Kho dang rong.
  ```
* **Gợi ý:** `if not danh_sach:` (list rỗng là `False`).

### Bài 3: Hiển thị 2 cuốn sách

* **Đề bài:** Mở rộng `hien_thi_danh_sach` để in bảng 2 sách mẫu (mã, tên, tác giả, thể loại, giá, số lượng).
* **Input:** Không có.
* **Output:**
  ```
  1  De Men Phieu Luu Ky       To Hoai      Truyen    65000.0  12
  2  Tuoi tho du doi           Nguyen Nhat Anh  Van hoc  58000.0  8
  ```
* **Gợi ý:** Vòng lặp `for s in danh_sach:` rồi `print(s["ma"], s["ten"], ...)`.

### Bài 4: Tìm sách theo mã

* **Đề bài:** Viết hàm `tim_theo_ma(danh_sach: List[Dict[str, object]], ma: int) -> Optional[int]` trả **vị trí** (index) của sách trong list, `None` nếu không có. Thử với mã 1 và mã 99.
* **Input:** Không có.
* **Output:**
  ```
  Vi tri ma 1: 0
  Vi tri ma 99: None
  ```
* **Gợi ý:** `for i, s in enumerate(danh_sach): if s["ma"] == ma: return i`.

### Bài 5: Tìm sách theo tên (không phân biệt hoa thường)

* **Đề bài:** Viết hàm `tim_theo_ten(danh_sach, ten_can_tim: str) -> Optional[dict]` tìm cuốn đầu tiên có tên **chứa** chuỗi (không phân biệt chữ hoa/thường). Thử `"de"` với tên `"De Men Phieu Luu Ky"`.
* **Input:** Không có.
* **Output:**
  ```
  Tim thay: De Men Phieu Luu Ky
  ```
* **Gợi ý:** đưa cả hai về `lower()`: `ten_can_tim.lower() in str(s["ten"]).lower()`.

### Bài 6: Đếm số đầu sách

* **Đề bài:** Viết hàm `dem_dau_sach(danh_sach) -> int` trả số lượng sách trong kho.
* **Input:** Không có.
* **Output:**
  ```
  So dau sach: 2
  ```
* **Gợi ý:** `return len(danh_sach)`.

### Bài 7: Tổng số cuốn trong kho

* **Đề bài:** Viết hàm `tong_so_cuon(danh_sach) -> int` cộng trường `so_luong` của mọi sách.
* **Input:** Không có.
* **Output:**
  ```
  Tong so cuon: 20
  ```
* **Gợi ý:** `sum(s["so_luong"] for s in danh_sach)`.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Thêm sách với mã tự tăng

* **Đề bài:** Viết hàm `them_sach(danh_sach, ten, tac_gia, the_loai, gia, so_luong) -> None` thêm sách vào cuối kho với mã = **mã lớn nhất + 1**. Thêm 1 cuốn vào kho có 2 cuốn (mã 1, 2) rồi in mã cuối.
* **Input:** Không có.
* **Output:**
  ```
  Ma moi: 3
  ```
* **Gợi ý:** `ma = max((s["ma"] for s in danh_sach), default=0) + 1`.

### Bài 9: Sửa giá theo mã

* **Đề bài:** Viết hàm `sua_gia(danh_sach, ma: int, gia_moi: float) -> bool` đổi giá sách, trả `True` nếu sửa được. Thử sửa mã 2 thành 70000 và in giá mới.
* **Input:** Không có.
* **Output:**
  ```
  Da sua. Gia moi: 70000.0
  ```
* **Gợi ý:** dùng `tim_theo_ma` để lấy vị trí.

### Bài 10: Xóa sách theo mã

* **Đề bài:** Viết hàm `xoa_sach(danh_sach, ma: int) -> bool` xóa sách có mã, trả `True` nếu xóa được. Xóa mã 1 rồi in số sách còn lại.
* **Input:** Không có.
* **Output:**
  ```
  Con lai: 1
  ```
* **Gợi ý:** `danh_sach.pop(vi_tri)`.

### Bài 11: Thống kê cơ bản

* **Đề bài:** Viết hàm `thong_ke(danh_sach) -> None` in: số đầu sách, tổng số cuốn, tổng giá trị kho (`gia * so_luong`).
* **Input:** Không có.
* **Output:**
  ```
  So dau sach: 2
  Tong so cuon: 20
  Tong gia tri: 1,244,000 dong
  ```
* **Gợi ý:** `sum(float(s["gia"]) * s["so_luong"] for s in danh_sach)`; in với `f"{x:,.0f}"`.

### Bài 12: Tìm sách đắt nhất

* **Đề bài:** Viết hàm `sach_dat_nhat(danh_sach) -> dict` trả sách có `gia` lớn nhất. In tên + giá.
* **Input:** Không có.
* **Output:**
  ```
  Dat nhat: De Men Phieu Luu Ky - 65000.0
  ```
* **Gợi ý:** `max(danh_sach, key=lambda s: s["gia"])`.

### Bài 13: Lưu danh sách ra JSON

* **Đề bài:** Viết hàm `luu_file(danh_sach: List[dict], ten_file: str) -> None` ghi toàn bộ ra file JSON (tiếng Việt đúng, chỉ thụt 2 mức). Chạy với tên `"kho_test.json"` rồi in `"Da luu 2 cuon sach."`.
* **Input:** Không có.
* **Output:**
  ```
  Da luu 2 cuon sach.
  ```
* **Gợi ý:** `open(ten_file, "w", encoding="utf-8")` + `json.dump(..., ensure_ascii=False, indent=2)`.

### Bài 14: Nạp danh sách từ JSON

* **Đề bài:** Viết hàm `nap_file(ten_file: str) -> List[dict]` đọc file JSON thành list; nếu file không tồn tại trả `[]`. Đọc file đã lưu ở bài 13 và in số phần tử; đọc file không tồn tại in `0`.
* **Input:** Không có.
* **Output:**
  ```
  Doc duoc: 2
  File khong co: 0
  ```
* **Gợi ý:** `try: json.load(f)` / `except FileNotFoundError: return []`.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Menu đơn giản (Thêm / Xem / Thoát)

* **Đề bài:** Viết `in_menu()` in 3 lựa chọn (1. Thêm, 2. Xem, 0. Thoát) và `main()` chạy vòng lặp menu liên tục; chọn `1` thì gọi `them_sach` (nhập qua `input()`), chọn `2` gọi `hien_thi_danh_sach`, chọn `0` in `"Tam biet!"` và thoát.
* **Input:** Nhập `1`, tên `De Men`, tác giả `To Hoai`, thể loại `Truyen`, giá `65000`, SL `10`, rồi `2`, rồi `0`.
* **Output:**
  ```
  De Men  To Hoai  Truyen  65000.0  10
  Tam biet!
  ```
* **Gợi ý:** `while True:` + rẽ nhánh `if chon == ...`; nhớ `from typing import ...`.

### Bài 16: Thêm chức năng Tìm kiếm vào menu

* **Đề bài:** Bổ sung vào menu lựa chọn `3. Tim theo ten`. Khi chọn 3, nhập tên, gọi `tim_theo_ten`; tìm thấy thì in `sach["ten"] + " - " + str(sach["gia"])`, không thấy in `"Khong tim thay"`.
* **Input:** Thêm 1 sách, chọn 3, nhập `de`, rồi `0`.
* **Output:**
  ```
  De Men Phieu Luu Ky - 65000.0
  Tam biet!
  ```
* **Gợi ý:** Kết quả tìm có thể là `None` — nhớ kiểm tra.

### Bài 17: Thêm chức năng Sửa và Xóa

* **Đề bài:** Bổ sung `4. Sua sach` và `5. Xoa sach`. Chọn 4: nhập mã → nhập giá mới → `sua_gia`. Chọn 5: nhập mã → `xoa_sach`. Sau đó in số đầu sách còn lại.
* **Input:** Thêm 2 sách, chọn 4 (mã 1, giá 70000), chọn 5 (mã 2), chọn 2.
* **Output:**
  ```
  Da sua ma 1.
  Da xoa ma 2.
  Con 1 dau sach.
  ```
* **Gợi ý:** Tận dụng `sua_gia` và `xoa_sach` đã viết ở bài 9, 10.

### Bài 18: Thêm chức năng Thống kê và Lưu file

* **Đề bài:** Bổ sung `6. Thong ke` (gọi `thong_ke`) và `7. Luu file` (gọi `luu_file(kho, "kho_chinh.json")`). Chạy 1 lượt: thêm 2 sách → 7 → 6 → 0.
* **Input:** Nhập 2 sách, chọn 7, chọn 6, chọn 0.
* **Output:**
  ```
  Da luu 2 cuon sach.
  So dau sach: 2
  Tong so cuon: 20
  Tong gia tri: 1,244,000 dong
  Tam biet!
  ```
* **Gợi ý:** Lưu vào một tên file cố định.

### Bài 19: Tự động lưu khi thoát

* **Đề bài:** Sửa `main()` sao cho khi chọn `0. Thoat`, chương trình **tự gọi `luu_file`** rồi in `"Da tu dong luu truoc khi thoat."` rồi `"Tam biet!"`.
* **Input:** Thêm 1 sách, chọn 0.
* **Output:**
  ```
  Da tu dong luu truoc khi thoat.
  Tam biet!
  ```
* **Gợi ý:** Đặt `luu_file(...)` ngay trước `break`.

### Bài 20: Chương trình hoàn chỉnh

* **Đề bài:** Ghép toàn bộ: khi khởi động `main()` gọi `nap_file("kho_sach.json")` để nạp dữ liệu cũ; menu đầy đủ 8 mục (Thêm 1, Xem 2, Tìm 3, Sửa 4, Xóa 5, Thống kê 6, Lưu 7, Thoát 0); khi thoát tự lưu.
* **Input:** Khởi động (kho đã có 1 sách), xem → thêm 1 sách → lưu → thống kê → thoát → khởi động lại xem dữ liệu còn không.
* **Output:**
  ```
  So dau sach khi nap: 1
  Da them sach co ma 2.
  Da luu 2 cuon sach.
  So dau sach: 2
  Da tu dong luu truoc khi thoat.
  So dau sach khi nap lai: 2
  ```
* **Gợi ý:** Mỗi bước là một hàm đã có; chỉ cần lắp chúng vào `main()` đúng thứ tự.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Xây dựng từng hàm riêng biệt rồi **ghép thành chương trình hoàn chỉnh**.
* ✅ Thành thạo CRUD trên danh sách sách và tìm kiếm an toàn (`Optional`).
* ✅ Thống kê kho bằng generator expression.
* ✅ Lưu / đọc dữ liệu JSON bền vững qua nhiều lần chạy.

> 💪 **Mẹo học:** hãy chạy đi chạy lại toàn bộ quy trình (thêm → xem → sửa → xóa → lưu → mở lại) cho tới khi thuộc như nằm lòng — đó chính là cách lập trình viên kiểm thử ứng dụng của mình.

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 41: Dự Án Cuối Khóa](../41_Du_an_Cuoi_Khoa/bai_giang.md)**