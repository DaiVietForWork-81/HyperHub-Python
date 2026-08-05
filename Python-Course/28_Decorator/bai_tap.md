# 📝 Bài 28: Bài Tập – Decorator

> 🎯 **Chủ đề:** Hàm bậc cao, closure, cú pháp `@`, `functools.wraps`, decorator có đối số, `*args/**kwargs`, kết hợp nhiều decorator.
> 📘 Muốn đạt kết quả tốt nhất, hãy **tự viết code và chạy thử** trước khi xem đáp án.

---

## 📌 Hướng dẫn làm bài

* Mỗi bài tập hãy **tự gõ code** vào file `.py` rồi chạy bằng `python ten_file.py`.
* Kiểm tra kỹ output có khớp với "Output" của đề hay không.
* Toàn bộ bài tập dùng kiến thức đã học từ bài 25 → 28.
* Đáp án chi tiết 20 bài: 👉 [xem file dap_an.md](dap_an.md)

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Hàm trong biến

* **Đề bài:** Tạo hàm `chao(ten)` trả về chuỗi `"Xin chào " + ten`. Gán hàm này cho biến `ham` rồi gọi qua biến `ham` để in lời chào dành cho "Mai".
* **Input:** Không có.
* **Output:**
  ```
  Xin chào Mai
  ```
* **Gợi ý:** Trong Python hàm là đối tượng — `ham = chao` rồi gọi `ham("Mai")`.

### Bài 2: Truyền hàm vào hàm

* **Đề bài:** Viết hàm `ban_sao(loai, du_lieu)` nhận một hàm `loai` (ví dụ `len` hoặc `str`) và dữ liệu, rồi gọi `loai(du_lieu)` và trả về kết quả. In ra kết quả khi `loai` là `len`, `du_lieu` là `[1, 2, 3, 4]`.
* **Input:** Không có
* **Output:**
  ```
  4
  ```
* **Gợi ý:** Gọi `ban_sao(len, [1, 2, 3, 4])`.

### Bài 3: Hàm trả về hàm

* **Đề bài:** Viết hàm `tao_nhac_nho(loi)` trả về một **closure** mà khi gọi (không đối số) sẽ in ra `loi` hai lần, mỗi lần một dòng.
* **Input:** Không có
* **Output:**
  ```
  Hãy cố gắng!
  Hãy cố gắng!
  ```
* **Gợi ý:** Định nghĩa hàm con trong hàm cha, hàm cha `return` hàm con.

### Bài 4: Decorator in dấu hoa thị

* **Đề bài:** Dùng cú pháp `@` tạo decorator `dong_khung` — in 2 dấu `*`, gọi hàm gốc `in_ten()` in `"An"`, rồi in tiếp 2 dấu `*`.
* **Input:** Không có
* **Output:**
  ```
  *
  *
  An
  *
  *
  ```
* **Gợi ý:** Decorator chạy thân hàm gốc giữa các phần "trang trí".

### Bài 5: `__name__` sau khi trang trí

* **Đề bài:** Trang trí hàm `tong(a, b)` bằng decorator `trang_tri` KHÔNG dùng `@wraps`. In ra `tong.__name__` sau khi trang trí. **Viết chương trình để chứng minh** kết quả.
* **Input:** Không có
* **Output (dòng đầu có thể khác — chỉ cần đúng bản chất):**
  ```
  ham_moi
  ```
* **Gợi ý:** Hàm mới thay thế hàm cũ nên mang tên của hàm bên trong.

### Bài 6: Decorator gọi hàm nhiều lần

* **Đề bài:** Viết decorator `chao_py(so_lan)` — decorator **có đối số** — gọi hàm gốc đúng `so_lan` lần. Áp dụng `@chao_py(2)` cho hàm `in_polo()` in `"Polo!"`.
* **Input:** Không có
* **Output:**
  ```
  Polo!
  Polo!
  ```
* **Gợi ý:** Decorator có đối số gồm BA tầng hàm lồng nhau.

### Bài 7: Dùng `@wraps`

* **Đề bài:** Trang trí hàm `in_ten()` bằng decorator `giu_ten()` CÓ `@wraps`. In ra `in_ten.__name__` và `in_ten.__doc__` (tài liệu).
* **Input:** Không có
* **Output:**
  ```
  in_ten
  Hàm in tên.
  ```
* **Gợi ý:** `from functools import wraps`; ghi docstring `"""Hàm in tên."""` trong thân hàm.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Decorator đo thời gian

* **Đề bài:** Viết decorator `do_gio` in ra `"{tên hàm} mất {x:.4f} giây"` khi chạy `tinh_tong(10_000_000)` (tính tổng các số từ 0 đến n).
* **Input:** Không có
* **Output (số giây thay đổi tùy máy):**
  ```
  tinh_tong mất 0.6000 giây
  ```
* **Gợi ý:** `import time`, lấy `time.time()` trước và sau khi gọi hàm gốc.

### Bài 9: Yêu cầu đăng nhập

* **Đề bài:** Tạo biến toàn cục `co_phien_moi = True`. Decorator `can_dang_nhap()` nếu `not co_phien_moi` in `"Cần đăng nhập"` và trả về `None`; ngược lại chạy hàm gốc. Áp dụng cho hàm `xem_ho_so()` in thông tin hồ sơ.
* **Input:** Không có
* **Output:**
  ```
  Ho so: An - lop 10A1
  ```
* **Gợi ý:** `if not co_phien_moi: print("Cần đăng nhập"); return None`.

### Bài 10: Đếm số lần gọi hàm

* **Đề bài:** Decorator `dem_lan` đếm số lần gọi và in `"Số lần: {n}"`. Gọi hàm `@dem_lan gioi_thieu()` 3 lần.
* **Input:** Không có
* **Output:**
  ```
  Số lần: 1
  Số lần: 2
  Số lần: 3
  ```
* **Gợi ý:** Gắn biến đếm lên chính hàm: khởi tạo `ham_moi.so_lan = 0` rồi tăng mỗi lần gọi.

### Bài 11: Bọc kết quả thành chữ in hoa

* **Đề bài:** Viết decorator `in_hoa()` trang trí hàm `cau_hoi()` (trả về chuỗi `"Do you want to quit?"` viết thường) sao cho khi gọi, kết quả được in HOA toàn bộ.
* **Input:** Không có
* **Output:**
  ```
  DO YOU WANT TO QUIT?
  ```
* **Gợi ý:** `ket_qua = ham(); return ket_qua.upper()` — chú ý hàm gốc phải `return` chuỗi.

### Bài 12: Kiểm tra số âm

* **Đề bài:** Hàm `tinh_binh_phuong(x)` trả về `x * x`. Decorator `kiem_tra_am()` — nếu `x` âm in `"Số âm không hợp lệ"` và trả về `None`; ngược lại chạy hàm gốc. Gọi với `-3` và với `4`.
* **Input:** Không có
* **Output:**
  ```
  Số âm không hợp lệ
  16
  ```
* **Gợi ý:** Trong decorator kiểm tra `args[0] < 0`.

### Bài 13: Log tên hàm đang chạy

* **Đề bài:** Viết decorator `ghi_ten()` in `"Đang chạy: {tên hàm}"` trước khi gọi hàm gốc. Áp dụng cho hai hàm `foo()` (in `"foo đang chạy"`) và `bar()` (in `"bar đang chạy"`).
* **Input:** Không có
* **Output:**
  ```
  Đang chạy: foo
  foo đang chạy
  Đang chạy: bar
  bar đang chạy
  ```
* **Gợi ý:** Dùng `ham.__name__` lấy tên hàm; dùng `@ghi_ten` lên cả hai hàm.

### Bài 14: Decorator xử lý chia cho 0

* **Đề bài:** Hàm `chia(a, b)` trả về `a / b`. Viết decorator `an_toan_chia()` — nếu `b == 0` in `"Lỗi chia cho 0!"` và trả về `None`; ngược lại chạy hàm gốc. Gọi `chia(10, 2)` và `chia(10, 0)`.
* **Input:** Không có
* **Output:**
  ```
  5.0
  Lỗi chia cho 0!
  ```
* **Gợi ý:** Kiểm tra `args[1] == 0` trước khi `return ham(*args, **kwargs)`.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Decorator báo cáo có tên sự kiện

* **Đề bài:** Viết decorator `bao_cao(ten_su_kien)` — **có đối số** — in `"Bắt đầu {tên_sự_kiện}"`, chạy hàm gốc, rồi in `"Kết thúc {tên_sự_kiện}"`. Áp dụng `@bao_cao("xử lý")` cho hàm `xu_ly()` in `"Đang xử lý..."`.
* **Input:** Không có
* **Output:**
  ```
  Bắt đầu xử lý
  Đang xử lý...
  Kết thúc xử lý
  ```
* **Gợi ý:** Đây là decorator CÓ đối số — gồm ba tầng hàm lồng nhau.

### Bài 16: Xếp chồng hai decorator

* **Đề bài:** Tạo `f1` in `"F1 trước"` và `"F1 sau"` quanh hàm gốc; `f2` in `"F2 trước"` và `"F2 sau"`. Áp dụng:
  ```python
  @f2
  @f1
  def hang():
      print("Thân hàm")
  ```
* **Input:** Không có
* **Output:**
  ```
  F2 trước
  F1 trước
  Thân hàm
  F1 sau
  F2 sau
  ```
* **Gợi ý:** Decorator ở dưới (gần hàm nhất) áp dụng trước → `f1` bọc trong `f2`.

### Bài 17: Bộ nhớ đệm (cache) kết quả

* **Đề bài:** Viết decorator `bo_nho_dem()` lưu kết quả vào dictionary theo từng tham số. Hàm `binh_phuong(n)` trả về `n * n`. Gọi hai lần với `n = 5`: lần đầu phải tính toán (in `"Tính toán"`), lần thứ hai lấy từ cache (in `"Lấy từ cache"`).
* **Input:** Không có
* **Output:**
  ```
  Tính toán
  25
  Lấy từ cache
  25
  ```
* **Gợi ý:** Dùng dict nằm ngoài closure; nếu tham số đã có trong dict thì trả luôn, không gọi hàm gốc.

### Bài 18: Kiểm tra kiểu dữ liệu tham số

* **Đề bài:** Viết decorator `kiem_tra_kieu()` — trước khi chạy kiểm tra `isinstance(args[0], int)`, nếu không phải in `"Cần số nguyên"` và trả về `None`. Áp dụng cho hàm `tong_tu_0(n)` trả về tổng `0 + 1 + ... + n`. Gọi với `3` và với `"abc"`.
* **Input:** Không có
* **Output:**
  ```
  6
  Cần số nguyên
  ```
* **Gợi ý:** `sum(range(n + 1))` tính tổng từ 0 đến n.

### Bài 19: Log đầy đủ tham số và kết quả

* **Đề bài:** Viết decorator `ghi_log()` in một dòng: `"gọi {tên} args={args} kwargs={kwargs} -> {kết quả}"`. Áp dụng cho hàm `mua_hang(loai, so_tien=100000)` trả về chuỗi xác nhận. Gọi `mua_hang("trà", so_tien=500000)`.
* **Input:** Không có
* **Output (dạng log):**
  ```
  gọi mua_hang args=('trà',) kwargs={'so_tien': 500000} -> Đã mua trà
  Đã mua trà
  ```
* **Gợi ý:** Gọi `ket_qua = ham(*args, **kwargs)` rồi in trước khi `return ket_qua`.

### Bài 20: Kết hợp đếm lần gọi và đo thời gian

* **Đề bài:** Tạo hai decorator: `dem_lan()` (in `"Lần gọi thứ {n}"`) và `do_gio()` (in `"Đang chạy {tên}, tốn {x:.4f} giây"`). Xếp chồng để mỗi lần gọi hàm `hoc_tap()` (in `"Học bài"`) đều hiện đủ: dòng đo thời gian, dòng số lần gọi, rồi dòng nội dung. Gọi hàm 2 lần.
* **Input:** Không có
* **Output (dạng — giây thay đổi tùy máy):**
  ```
  Đang chạy hoc_tap, tốn 0.0000 giây
  Lần gọi thứ 1
  Học bài
  Đang chạy hoc_tap, tốn 0.0000 giây
  Lần gọi thứ 2
  Học bài
  ```
* **Gợi ý:** Thử thứ tự `@do_gio` và `@dem_lan` xem thứ tự nào cho kết quả trên — decorator gần hàm nhất áp dụng trước.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Thành thạo hàm bậc cao, closure và decorator cú pháp `@`.
* ✅ Phân biệt decorator không đối số và có đối số.
* ✅ Giữ danh tính hàm bằng `@wraps`, truyền tham số linh hoạt bằng `*args/**kwargs`.
* ✅ Áp dụng decorator cho log, đếm, cache, kiểm tra dữ liệu — đúng kiểu "trang trí" mà các framework web (Flask, Django) dùng!

> 💪 Chưa tự làm được bài nào thì đừng lo — đọc lại bài giảng, xem từng dòng code chậm lại, rồi thử lại. **Lập trình là luyện tập.**

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 29: Iterator](../29_Iterator/bai_giang.md)**