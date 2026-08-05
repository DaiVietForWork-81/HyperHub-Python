# 📝 Bài 37: Bài Tập – Logging

> 🎯 **Chủ đề:** Ghi nhật ký hoạt động chương trình bằng module `logging` — 5 mức độ, `basicConfig`, format, ghi file, log trong module.
>
> 📌 **Lưu ý:** Các bài tập dùng `logging` không cần thư viện ngoài. Với bài ghi ra file, hãy mở file `.log` tạo ra để quan sát kết quả; có thể xóa file cũ trước mỗi lần chạy (hoặc dùng `filemode="w"`). Nếu chưa làm được, hãy xem lại bài giảng — **đáp án chi tiết ở [dap_an.md](dap_an.md)**.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Dòng log đầu tiên

* **Đề bài:** Viết chương trình ghi một log mức INFO: `Chao mung ban den voi Python logging.` (không cần cấu hình gì thêm).
* **Input:** Không có.
* **Output:** Mặc định chỉ hiện từ WARNING — quan sát xem có gì được in ra không.
* **Gợi ý:** `import logging` rồi `logging.info("...")`.

### Bài 2: Ghi cả năm mức

* **Đề bài:** Ghi lần lượt cả 5 mức: DEBUG, INFO, WARNING, ERROR, CRITICAL với nội dung tự đặt (ví dụ `Day la dong DEBUG`...). Chạy **không cấu hình** rồi chạy **có** `level=logging.DEBUG` và so sánh.
* **Input:** Không có.
* **Output:** Khi đã cấu hình DEBUG, hiện đủ 5 dòng; chưa cấu hình chỉ hiện 3 dòng cuối.
* **Gợi ý:** `logging.basicConfig(level=logging.DEBUG)` đặt trước khi ghi.

### Bài 3: Cấu hình hiển thị từ INFO

* **Đề bài:** Cấu hình `basicConfig` với `level=logging.INFO`, ghi một dòng DEBUG và một dòng INFO. In ra màn hình `Xong!`.
* **Input:** Không có.
* **Output:**
  ```
  2026-08-05 20:00:00,000 - INFO - Chuong trinh bat dau
  Xong!
  ```
* **Gợi ý:** Đặt `level=logging.INFO` — DEBUG sẽ bị chặn.

### Bài 4: Thêm thời gian vào log

* **Đề bài:** Cấu hình format gồm `%(asctime)s - %(levelname)s - %(message)s` và `datefmt="%d/%m/%Y %H:%M:%S"`. Ghi log WARNING `Truy cap thanh cong.`.
* **Input:** Không có.
* **Output:**
  ```
  05/08/2026 20:05:00 - WARNING - Truy cap thanh cong.
  ```
* **Gợi ý:** `format=` và `datefmt=` nằm trong `basicConfig`.

### Bài 5: Ghi log ra file

* **Đề bài:** Cấu hình ghi log vào file `bai_tap.log` (định dạng `%(asctime)s - %(levelname)s - %(message)s`), ghi 2 log INFO. Sau khi chạy, mở file `bai_tap.log` kiểm tra.
* **Input:** Không có.
* **Output:** Màn hình **không** in gì; nội dung trong file `bai_tap.log` có 2 dòng.
* **Gợi ý:** Thêm `filename="bai_tap.log"` và `filemode="a"`.

### Bài 6: Log chào mừng người dùng ATM

* **Đề bài:** Viết chương trình giả lập bước đầu của máy ATM: in ra màn hình `Chao mung ban den voi ATM!`, ghi log INFO `Nguoi dung bat dau su dung ATM.`, ghi log DEBUG `Hien menu chinh.`.
* **Input:** Không có.
* **Output:**
  ```
  Chao mung ban den voi ATM!
  ```
  (kèm 2 dòng log trên màn hình nếu level đủ thấp)
* **Gợi ý:** Cấu hình `level=logging.DEBUG` để thấy cả DEBUG; `print()` cho dòng chào người dùng.

### Bài 7: Tên module trong log

* **Đề bài:** Tạo logger bằng `logging.getLogger("may_giat")` và ghi log INFO `Bat dau giat.` với format có `%(name)s`.
* **Input:** Không có.
* **Output:**
  ```
  2026-08-05 20:10:00,000 - INFO - may_giat - Bat dau giat.
  ```
* **Gợi ý:** Format: `"%(asctime)s - %(levelname)s - %(name)s - %(message)s"`.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Format đầy đủ và ghi đè file

* **Đề bài:** Cấu hình format `%(asctime)s | %(levelname)s | %(lineno)d | %(message)s` ghi ra file `dai_han.log` với `filemode="w"`. Ghi 2 log rồi chạy lại 2 lần và kiểm tra file chỉ có 2 dòng.
* **Input:** Không có.
* **Output:** Sau 2 lần chạy, file `dai_han.log` chỉ chứa 2 dòng (lần chạy sau xóa nội dung cũ).
* **Gợi ý:** `%(lineno)d` in số dòng code; `"w"` = write (ghi đè).

### Bài 9: Log tên hàm đang chạy

* **Đề bài:** Viết 2 hàm `tinh_tien(so_luong, don_gia)` và `in_hoa_don()`; mỗi hàm ghi log INFO với format có `%(funcName)s`. Gọi cả 2 hàm và quan sát.
* **Input:** Không có.
* **Output:** Mỗi dòng log có tên hàm tương ứng: `tinh_tien`, `in_hoa_don`.
* **Gợi ý:** `format="%(asctime)s - %(funcName)s - %(message)s"`.

### Bài 10: Chia số bắt lỗi ghi ERROR

* **Đề bài:** Viết hàm `chia(a, b)` trả về thương; nếu `b == 0`, ghi log ERROR `Khong the chia cho 0` và trả về `None`. Gọi với `(10, 2)` và `(10, 0)`.
* **Input:** Không có.
* **Output:**
  ```
  Ket qua 10 / 2 = 5.0
  2026-08-05 20:15:00,000 - ERROR - Khong the chia cho 0
  Ket qua 10 / 0 = None
  ```
* **Gợi ý:** Dùng `if b == 0` để ghi log; `print(f"Ket qua {a} / {b} = {ket_qua}")`.

### Bài 11: Đọc file không tồn tại

* **Đề bài:** Viết chương trình mở file `khong_co_file.txt` bằng `try/except`; nếu `FileNotFoundError` thì ghi log ERROR kèm tên file. Ghi ra file `loi_file.log`.
* **Input:** Không có.
* **Output:** Màn hình in `Khong mo duoc file.`; trong `loi_file.log` có 1 dòng ERROR.
* **Gợi ý:** `logging.error("Khong mo duoc file: %s", ten_file)`.

### Bài 12: Logger riêng trong module

* **Đề bài:** Tạo file `dich_vu.py` chứa hàm `kiem_tra_ngay(ngay)` ghi INFO/WARNING, sử dụng `logger = logging.getLogger(__name__)`. Tạo file `main.py` cấu hình `basicConfig` rồi gọi hàm. (Có thể làm gọn: dùng `getLogger("dich_vu")`.)
* **Input:** Không có.
* **Output:** Log từ hàm có tên `dich_vu` trong cột `%(name)s`.
* **Gợi ý:** Trong module con chỉ dùng `logger.xxx(...)`, không gọi `basicConfig`.

### Bài 13: Đếm số lần nhập mật khẩu sai

* **Đề bài:** Giả lập đăng nhập: mật khẩu đúng là `python123`. Cho người dùng nhập mật khẩu (lặp tối đa 3 lần). Mỗi lần sai ghi WARNING `Sai mat khau lan thu N`; đúng ghi INFO `Dang nhap thanh cong`.
* **Input:** Nhập 2 lần sai rồi 1 lần đúng: `abc`, `xyz`, `python123`.
* **Output:**
  ```
  WARNING - Sai mat khau lan thu 1
  WARNING - Sai mat khau lan thu 2
  INFO - Dang nhap thanh cong
  ```
* **Gợi ý:** Vòng lặp `for lan in range(1, 4)`; `if` so sánh với mật khẩu đúng.

### Bài 14: Kiểm tra tuổi truy cập

* **Đề bài:** Viết hàm `kiem_tra_do_tuoi(tuoi)`: tuổi từ 18 trở lên ghi INFO `Cho phep truy cap`; dưới 18 ghi WARNING `Do tuoi chua du (N tuoi)`. Gọi với tuổi 15 và 20.
* **Input:** Không có.
* **Output:**
  ```
  INFO - Do tuoi 20: cho phep truy cap
  WARNING - Do tuoi 15: chua du dieu kien
  ```
* **Gợi ý:** `logging.warning("Do tuoi chua du (%d tuoi)", tuoi)`.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Chương trình ATM hoàn chỉnh có log

* **Đề bài:** Viết chương trình ATM với menu (Rút tiền, Nạp tiền, Xem số dư, Thoát). Số dư ban đầu 500.000. Ghi log: INFO khi nạp/rút thành công, WARNING khi rút quá số dư, CRITICAL khi người dùng nhập sai chức năng quá 3 lần. Ghi ra file `atm.log`.
* **Input:** Chọn `1` (rút) nhập `700000`, chọn `1` rút `100000`, chọn `4` (thoát).
* **Output:** Trên màn hình thông báo kết quả; file `atm.log` chứa các dòng WARNING/INFO tương ứng.
* **Gợi ý:** Mỗi chức năng một hàm; đếm lựa chọn sai bằng biến đếm.

### Bài 16: Hàm xử lý nhiều ngoại lệ

* **Đề bài:** Viết hàm `xu_ly_du_lieu(du_lieu)`: nếu không phải số → ERROR; nếu là số âm → WARNING; nếu là số dương → INFO. Gọi với chuỗi `"abc"`, số `-5`, số `10`. Ghi ra file `xu_ly.log`.
* **Input:** Không có.
* **Output:** 3 dòng log với 3 mức khác nhau trong file `xu_ly.log`.
* **Gợi ý:** Kiểm tra bằng `isinstance(du_lieu, (int, float))` (học ở bài 38) hoặc `str(du_lieu).replace(".", "").replace("-", "").isdigit()`.

### Bài 17: Máy tính cầm tay có nhật ký

* **Đề bài:** Viết hàm `tinh(a, b, phep_toan)` nhận `+`, `-`, `*`, `/`. Mỗi lần tính ghi DEBUG kèm phép tính; phép chia cho 0 ghi ERROR. Gọi thử 3 phép tính, ghi ra file `may_tinh.log`.
* **Input:** Không có.
* **Output:** File `may_tinh.log` có 3-4 dòng, trong đó phép chia 0 là ERROR.
* **Gợi ý:** `logging.debug("%d %s %d = %s", a, phep_toan, b, ket_qua)`.

### Bài 18: Xử lý danh sách số từ file

* **Đề bài:** Tạo file `so.txt` chứa 3 dòng: `10`, `abc`, `20`. Viết chương trình đọc từng dòng, chuyển thành số: thành công ghi DEBUG `Dong N = gia tri`; thất bại ghi ERROR `Dong N khong phai so: abc`. Cuối cùng in tổng các số hợp lệ.
* **Input:** Không có (file `so.txt` đã có).
* **Output:**
  ```
  Tong cac so hop le: 30
  ```
  (kèm 3 dòng log trên màn hình nếu level DEBUG)
* **Gợi ý:** `try: int(dong.strip()) except ValueError:` (bài 19 về exception).

### Bài 19: Chặn log dữ liệu nhạy cảm

* **Đề bài:** Viết hàm `dang_nhap(ten_dang_nhap, mat_khau)` ghi INFO `Nguoi dung abc dang nhap.` **không được chứa mật khẩu**. Sau đó gọi với `("admin", "bi_mat_123")` và kiểm tra file `bao_mat.log` không chứa chuỗi `bi_mat_123`.
* **Input:** Không có.
* **Output:** File `bao_mat.log` chứa 1 dòng INFO có tên đăng nhập nhưng không có mật khẩu.
* **Gợi ý:** Chỉ đưa `ten_dang_nhap` vào message; thử đọc lại file và `assert "bi_mat_123" not in noi_dung`.

### Bài 20: Hệ thống quản lý lớp học có log

* **Đề bài:** Viết chương trình quản lý lớp học (menu: Thêm học sinh, Xóa học sinh, Xem danh sách, Thoát). Ghi log: INFO khi thêm/xóa thành công, WARNING khi xóa học sinh không có trong lớp, ERROR khi người dùng nhập tên trống. Ghi ra file `lop_hoc.log`.
* **Input:** Chọn `1` nhập `An`, chọn `2` nhập `An`, chọn `2` nhập `Binh` (không có), chọn `4`.
* **Output:** File `lop_hoc.log` có: 1 INFO thêm, 1 INFO xóa, 1 WARNING không tìm thấy.
* **Gợi ý:** Lưu danh sách học sinh trong list; kiểm tra `if ten.strip() == ""` để ghi ERROR; `if ten in lop` trước khi xóa.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Ghi log đủ 5 mức độ và hiểu ngưỡng hiển thị mặc định.
* ✅ Cấu hình `basicConfig`: level, format, ghi file, ghi đè.
* ✅ Dùng `%(asctime)s`, `%(name)s`, `%(funcName)s`, `%(lineno)d` trong format.
* ✅ Kết hợp log với `try/except` để ghi lỗi đọc file.
* ✅ Xây dựng chương trình thực tế (ATM, máy tính, quản lý lớp) có nhật ký đầy đủ.

> 💪 **Chạy lại nhiều lần và mở file `.log`** để xem "nhật ký" tích lũy như thế nào — đó chính là cách lập trình viên dò lỗi trong thực tế.

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 38: Type Hints](../38_Typing/bai_giang.md)**
