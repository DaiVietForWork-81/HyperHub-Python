# 📝 Bài 12: Bài Tập – Hàm (Function)

> 🎯 **Chủ đề:** Định nghĩa hàm `def`, gọi hàm, tham số – đối số, `return`, tham số mặc định, keyword arguments, `*args`, `**kwargs`, docstring.

---

## 📌 Hướng dẫn làm bài

* Mỗi bài tập cần **tự viết code** rồi chạy thử trước khi xem đáp án.
* Nhớ **gọi hàm** sau khi định nghĩa — nếu không chương trình sẽ không in gì.
* Đáp án chi tiết 20 bài: 👉 [xem file dap_an.md](dap_an.md)

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Hàm xin chào

* **Đề bài:** Viết hàm `xin_chao()` in ra màn hình dòng chữ `Xin chao, lop 10A1!` rồi gọi hàm đó 2 lần.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Xin chao, lop 10A1!
  Xin chao, lop 10A1!
  ```
* **Gợi ý:** Hàm không cần tham số cũng không cần `return`; chỉ cần `def` + `print` + gọi hàm.

### Bài 2: Hàm chào theo tên

* **Đề bài:** Viết hàm `chao_ban(ten)` in ra câu `Xin chao, <ten>!` với tên được truyền vào. Gọi hàm với tên `Mai` và `Nam`.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Xin chao, Mai!
  Xin chao, Nam!
  ```
* **Gợi ý:** Dùng f-string `f"Xin chao, {ten}!"` bên trong `print`.

### Bài 3: Hàm tính bình phương

* **Đề bài:** Viết hàm `binh_phuong(x)` trả về `x * x`. Gọi hàm với số `7` và in kết quả ra màn hình.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  49
  ```
* **Gợi ý:** Dùng `return x * x`, rồi `print(binh_phuong(7))`.

### Bài 4: Hàm cộng hai số

* **Đề bài:** Viết hàm `cong_hai_so(a, b)` trả về tổng của `a` và `b`. In kết quả của `cong_hai_so(12, 30)`.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  42
  ```
* **Gợi ý:** `return a + b` — nhớ đủ 2 đối số khi gọi.

### Bài 5: Hàm với docstring

* **Đề bài:** Viết hàm `tinh_chu_vi_hcn(dai, rong)` có **docstring** mô tả, trả về chu vi hình chữ nhật (2 × (dai + rong)). Gọi hàm với `5, 3` và in kết quả.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  16
  ```
* **Gợi ý:** Docstring viết trong `"""..."""` ngay sau dòng `def`; không bắt buộc in docstring ra.

### Bài 6: Hàm trả về lời chào

* **Đề bài:** Viết hàm `tao_loi_chao(ten)` **trả về** chuỗi `Chao buoi sang, <ten>!` (không in bên trong hàm). Gọi hàm rồi in kết quả trả về.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Chao buoi sang, An!
  ```
* **Gợi ý:** `return f"Chao buoi sang, {ten}!"` — giá trị trả về mới được in ở ngoài.

### Bài 7: Hàm kiểm tra chẵn lẻ

* **Đề bài:** Viết hàm `la_so_chan(n)` trả về `True` nếu `n` chia hết cho 2, ngược lại trả về `False`. Kiểm tra với `10` và `7`, in ra kết quả.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  True
  False
  ```
* **Gợi ý:** Dùng toán tử `%`: `n % 2 == 0`.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Hàm tính diện tích tam giác

* **Đề bài:** Viết hàm `dien_tich_tam_giac(day, cao)` trả về diện tích tam giác = `day * cao / 2`. Gọi hàm với `day = 10, cao = 4` và in kết quả với 2 chữ số thập phân.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Dien tich tam giac: 20.0
  ```
* **Gợi ý:** Chú ý phép chia `/` luôn cho số thực; có thể dùng `f"{ket_qua:.2f}"`.

### Bài 9: Hàm xếp loại học sinh

* **Đề bài:** Viết hàm `xep_loai(dtb)` nhận điểm trung bình và trả về `"Gioi"` nếu `dtb >= 8.5`, `"Kha"` nếu `dtb >= 7.0`, `"Trung binh"` nếu `dtb >= 5.0`, ngược lại `"Yeu"`. In kết quả cho `dtb = 8.7`, `dtb = 6.5`, `dtb = 4.9`.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  8.7 -> Gioi
  6.5 -> Kha
  4.9 -> Yeu
  ```
* **Gợi ý:** Dùng `if / elif / else` bên trong hàm, mỗi nhánh một `return`.

### Bài 10: Hàm tính điểm trung bình 3 môn

* **Đề bài:** Viết hàm `tinh_trung_binh(toan, van, anh)` trả về điểm trung bình 3 môn. An có điểm `8, 7.5, 9`, Bình có điểm `5, 6, 6.5`. In điểm trung bình của từng bạn.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  An: 8.2
  Binh: 5.8
  ```
* **Gợi ý:** `(toan + van + anh) / 3`; làm tròn 1 chữ số thập phân bằng `round(..., 1)`.

### Bài 11: Hàm có tham số mặc định

* **Đề bài:** Viết hàm `dat_truoc(mon, so_luong=1)` in ra câu `Ban da dat <so_luong> phan <mon>.` Gọi hàm với: `dat_truoc("pho")` và `dat_truoc("bun bo", 3)`.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Ban da dat 1 phan pho.
  Ban da dat 3 phan bun bo.
  ```
* **Gợi ý:** Tham số mặc định `so_luong=1` được dùng khi gọi không truyền đối số thứ hai.

### Bài 12: Gọi hàm bằng keyword arguments

* **Đề bài:** Viết hàm `ghi_ho_so(ten, tuoi, lop)` in ra `Ten: <ten> | Tuoi: <tuoi> | Lop: <lop>`. Gọi hàm **một lần duy nhất** bằng keyword arguments với thứ tự trộn lẫn: `lop="10A1", ten="Mai", tuoi=15`.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Ten: Mai | Tuoi: 15 | Lop: 10A1
  ```
* **Gợi ý:** Gọi `ghi_ho_so(lop="10A1", ten="Mai", tuoi=15)` — thứ tự không quan trọng.

### Bài 13: Hàm cộng nhiều số bằng `*args`

* **Đề bài:** Viết hàm `tinh_tong(*cac_so)` trả về tổng của tất cả các số truyền vào. In kết quả của `tinh_tong(1, 2, 3)` và `tinh_tong(10, 20, 30, 40)`.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  6
  100
  ```
* **Gợi ý:** Bên trong hàm, `cac_so` là một tuple — dùng `sum(cac_so)`.

### Bài 14: Menu máy tính bằng hàm

* **Đề bài:** Viết hàm `hien_menu()` in ra 4 dòng menu (1. Cong, 2. Tru, 3. Nhan, 4. Chia) và hàm `may_tinh(a, b, phep_tinh)` trả về kết quả theo phép tính được chọn (xử lý cả trường hợp `b = 0` khi chia). Gọi `may_tinh(10, 2, "4")` và `may_tinh(8, 0, "4")`.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  5.0
  Khong the chia cho 0!
  ```
* **Gợi ý:** Trong `may_tinh` dùng `if` so sánh `phep_tinh` với chuỗi `"1"`, `"2"`, `"3"`, `"4"`.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Hàm in ra tên viết tắt

* **Đề bài:** Viết hàm `viet_tat(ho_ten)` nhận chuỗi họ tên đầy đủ (ví dụ `"Nguyen Van An"`), tách các từ bằng `split()` và trả về chuỗi gồm **chữ cái đầu mỗi từ, viết hoa, không dấu cách** (ví dụ `"NVA"`).
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Nguyen Van An -> NVA
  Tran Thi Binh -> TTB
  ```
* **Gợi ý:** `ho_ten.split()` cho danh sách các từ; lấy từng từ `[0]`; nối bằng `"".join(...)` hoặc `+`.

### Bài 16: Hàm kiểm tra số nguyên tố

* **Đề bài:** Viết hàm `la_so_nguyen_to(n)` trả về `True` nếu `n > 1` và chỉ chia hết cho 1 và chính nó, ngược lại `False`. Kiểm tra các số `2, 9, 17, 1` và in kết quả từng số.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  2: True
  9: False
  17: True
  1: False
  ```
* **Gợi ý:** Duyệt từ `2` đến `n // 2 + 1`; nếu thấy ước thì trả về `False` ngay. Số `n <= 1` không phải nguyên tố.

### Bài 17: Hàm gộp nhiều thông tin bằng `**kwargs`

* **Đề bài:** Viết hàm `tong_ket(**mon_hoc)` nhận các cặp tên môn và điểm (dạng `toan=8, van=7`), in ra từng môn kèm điểm, đồng thời trả về điểm trung bình. Gọi với `toan=8, van=7, anh=9` và in điểm trung bình.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  toan: 8
  van: 7
  anh: 9
  Diem trung binh: 8.0
  ```
* **Gợi ý:** `mon_hoc` là dictionary; `sum(mon_hoc.values()) / len(mon_hoc)` cho điểm trung bình.

### Bài 18: Trò chơi đoán số — chia thành hàm

* **Đề bài:** Viết 3 hàm: `sinh_so_bi_mat()` trả về số ngẫu nhiên trong 1–100, `doan_so(so_bi_mat, so_doan)` trả về `"lon hon"`, `"nho hon"` hoặc `"chinh xac"`, và `choi_game()` dùng vòng lặp `while` cho người chơi đoán tối đa 7 lần, in kết quả sau mỗi lần đoán.
* **Input:** Mô phỏng lần lượt các số đoán: `50`, `25`, `40` (giả sử số bí mật là `40`)
* **Output:**
  ```
  Ban doan so 50: so bi mat nho hon
  Ban doan so 25: so bi mat lon hon
  Ban doan so 40: chinh xac! Xin chuc mung!
  ```
* **Gợi ý:** Dùng `import random; random.randint(1, 100)`. Hàm `doan_so` chỉ so sánh và trả về chuỗi.

### Bài 19: Tiền lương nhân viên

* **Đề bài:** Viết hàm `tinh_luong(so_gio, luong_mot_gio=20000)` trả về tiền lương; nếu `so_gio > 40` thì số giờ vượt được tính gấp rưỡi (×1.5). Viết thêm hàm `in_phieu_luong(ten, so_gio)` in ra tên và tiền lương. Gọi cho An (`45` giờ) và Bình (`30` giờ).
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  An lam 45 gio -> 950000 dong
  Binh lam 30 gio -> 600000 dong
  ```
* **Gợi ý:** `gio_vuot = so_gio - 40`; lương = `40 * luong_mot_gio + gio_vuot * luong_mot_gio * 1.5`.

### Bài 20: Quản lý menu quán phở — tổng hợp hàm

* **Đề bài:** Viết các hàm: `gia_mon()` trả về dictionary giá `{"pho": 35000, "bun bo": 40000, "com": 25000}`, `thanh_tien(mon, so_luong, phu_thu=0)` trả về tổng tiền, và `in_hoa_don(don_hang)` nhận danh sách món đã đặt dạng `[("pho", 2), ("com", 1)]`, in từng món, thành tiền từng món và tổng tiền toàn bộ.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  pho x2 = 70000 dong
  com x1 = 25000 dong
  Tong: 95000 dong
  ```
* **Gợi ý:** Trong `in_hoa_don`, dùng vòng lặp `for mon, sl in don_hang`; tích lũy tổng bằng biến `tong = 0`.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Định nghĩa và gọi hàm thành thạo, biết khi nào hàm cần `return`.
* ✅ Dùng tham số mặc định, keyword arguments, `*args`, `**kwargs` linh hoạt.
* ✅ Tách chương trình lớn thành các hàm nhỏ rõ ràng (menu máy tính, game đoán số, hóa đơn).
* ✅ Viết docstring và đọc hiểu hàm do người khác viết.

> 💪 Nếu bài nào chưa tự làm được, hãy đọc lại bài giảng phần tương ứng rồi thử lại. **Chương trình tốt = chương trình nhiều hàm nhỏ!**

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 13: Phạm Vi Biến](../13_Scope/bai_giang.md)**
