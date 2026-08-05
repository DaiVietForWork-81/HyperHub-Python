# 📝 Bài 17: Bài Tập – Dictionary (Từ Điển)

> 🎯 **Chủ đề:** Tạo, truy cập, thêm, sửa, xóa, duyệt dictionary; kiểm tra khóa; dict comprehension cơ bản.

---

## 📌 Hướng dẫn làm bài

* Mỗi bài tập cần **tự viết code** rồi chạy thử trước khi xem đáp án.
* Đáp án chi tiết 20 bài: 👉 [xem file dap_an.md](dap_an.md)

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Tạo từ điển điểm môn học

* **Đề bài:** Tạo từ điển `diem` gồm 3 môn: `Toan: 8.5`, `Van: 7.0`, `Anh: 9.0` rồi in ra màn hình.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  {'Toan': 8.5, 'Van': 7.0, 'Anh': 9.0}
  ```
* **Gợi ý:** Dùng cặp ngoặc nhọn `{}` với cú pháp `{khóa: giá_trị, ...}`.

### Bài 2: Tra cứu điểm

* **Đề bài:** Với từ điển `diem` (Toan, Van, Anh), in ra điểm môn Toán và điểm môn Anh.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Diem Toan: 8.5
  Diem Anh: 9.0
  ```
* **Gợi ý:** Truy cập bằng cú pháp `diem["Toan"]`.

### Bài 3: Tra cứu an toàn với get()

* **Đề bài:** Với menu món ăn `{"Pho": 45, "Bun": 30}`, in giá của món `Pho` và món `Ga ran` (không có trong menu) — món không có phải trả về giá mặc định `0`.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Pho: 45
  Ga ran: 0
  ```
* **Gợi ý:** Dùng `menu.get(món, 0)`.

### Bài 4: Thêm môn học mới

* **Đề bài:** Bắt đầu với `diem = {"Toan": 8.5}`, thêm môn `Van: 7.0` và `Anh: 9.0` rồi in kết quả.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  {'Toan': 8.5, 'Van': 7.0, 'Anh': 9.0}
  ```
* **Gợi ý:** Gán `diem["Van"] = 7.0` — khóa chưa có nên được thêm mới.

### Bài 5: Sửa điểm

* **Đề bài:** `diem = {"Toan": 8.5, "Van": 7.0}` — cô giáo sửa điểm Toán thành `9.0`. In lại từ điển.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  {'Toan': 9.0, 'Van': 7.0}
  ```
* **Gợi ý:** Gán `diem["Toan"] = 9.0` — khóa đã tồn tại nên giá trị được thay thế.

### Bài 6: Xóa món khỏi menu bằng pop()

* **Đề bài:** `menu = {"Pho": 45, "Bun": 30, "Com": 25}` — món Cơm hết nên xóa khỏi menu. In giá vừa xóa và menu còn lại.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Da xoa: 25
  {'Pho': 45, 'Bun': 30}
  ```
* **Gợi ý:** `gia = menu.pop("Com")` — vừa xóa vừa lấy giá trị.

### Bài 7: Kiểm tra khóa tồn tại

* **Đề bài:** `diem = {"Toan": 8.5, "Anh": 9.0}` — kiểm tra xem môn `Toan` và môn `Ly` có trong từ điển không, in `True`/`False`.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Toan: True
  Ly: False
  ```
* **Gợi ý:** Dùng toán tử `"Toan" in diem`.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Duyệt khóa và in từng môn

* **Đề bài:** Với `diem = {"Toan": 8.5, "Van": 7.0, "Anh": 9.0}`, dùng vòng lặp in ra tên từng môn học.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Toan
  Van
  Anh
  ```
* **Gợi ý:** `for mon in diem:` — vòng lặp tự duyệt qua các khóa.

### Bài 9: Tính tổng và trung bình điểm

* **Đề bài:** Với `diem` 3 môn, in tổng điểm và điểm trung bình (làm tròn 2 chữ số).
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Tong: 24.5
  Trung binh: 8.17
  ```
* **Gợi ý:** `sum(diem.values())` cộng toàn bộ giá trị; trung bình = tổng chia `len(diem)`.

### Bài 10: Duyệt cặp khóa – giá trị

* **Đề bài:** In bảng điểm dạng `Mon: Diem` cho từng môn bằng `items()`.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Toan: 8.5
  Van: 7.0
  Anh: 9.0
  ```
* **Gợi ý:** `for mon, d in diem.items():`.

### Bài 11: Đếm số phần tử

* **Đề bài:** Sổ tay từ vựng `tu_vung = {"apple": "qua tao", "book": "quyen sach", "pen": "cay but"}` — in ra số từ đang học.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  So tu dang hoc: 3
  ```
* **Gợi ý:** Dùng `len(tu_vung)`.

### Bài 12: Bảng tuổi của bạn bè

* **Đề bài:** `ban_be = {"An": 15, "Binh": 16, "Chi": 15}` — in ra bảng dạng `Ten: tuoi tuoi` đẹp mắt bằng f-string.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  An 15 tuoi
  Binh 16 tuoi
  Chi 15 tuoi
  ```
* **Gợi ý:** Kết hợp `items()` với f-string: `print(f"{ten} {tuoi} tuoi")`.

### Bài 13: get() với giá trị mặc định khi điểm danh

* **Đề bài:** Lớp có điểm `{"An": 8, "Binh": 7}`. Tra điểm của `An`, `Chi` (chưa có → mặc định 0) và in ra.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  An: 8
  Chi: 0
  ```
* **Gợi ý:** `diem.get("Chi", 0)`.

### Bài 14: Xóa bằng del và clear()

* **Đề bài:** Bắt đầu với `menu = {"Pho": 45, "Bun": 30, "Com": 25, "My xao": 35}`. Xóa món `Bun` bằng `del`, sau đó dùng `clear()` xóa hết và in kết quả từng bước.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Sau khi del: {'Pho': 45, 'Com': 25, 'My xao': 35}
  Sau khi clear: {}
  ```
* **Gợi ý:** `del menu["Bun"]` xóa 1 phần tử; `menu.clear()` xóa sạch.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Đếm tần suất chữ cái

* **Đề bài:** Cho câu `"python la ngon ngu tuyen voi"`. Đếm mỗi chữ cái (không tính dấu cách) xuất hiện bao nhiêu lần và in kết quả dạng `chu: so_lan`.
* **Input:** (không cần nhập gì)
* **Output (một phần ví dụ):**
  ```
  p: 1
  y: 2
  t: 2
  ...
  ```
* **Gợi ý:** Từ điển rỗng, mỗi chữ: `dem[chu] = dem.get(chu, 0) + 1`.

### Bài 16: Máy tính tiền quán ăn

* **Đề bài:** Menu `{"Pho": 45, "Bun": 30, "Com": 25, "My xao": 35}`. Nhập tên món ăn khách gọi (có thể nhiều món, nhập `xong` để dừng), in giá từng món và tổng tiền. Món không có trong menu thì báo `Khong co mon nay!`.
* **Input:**
  ```
  Nhap mon (xong de dung): Pho
  Nhap mon (xong de dung): Bun
  Nhap mon (xong de dung): xong
  ```
* **Output:**
  ```
  Pho: 45k
  Bun: 30k
  Tong tien: 75k
  ```
* **Gợi ý:** Vòng lặp `while`, kiểm tra `mon in menu` hoặc dùng `get()`.

### Bài 17: Quản lý điểm — thêm, sửa, xóa

* **Đề bài:** Bắt đầu `diem = {"Toan": 8.5, "Van": 7.0}`. Thực hiện lần lượt: thêm `Anh: 9.0`, sửa `Toan` thành `9.5`, xóa `Van`, rồi in bảng điểm cuối cùng dạng `Mon: Diem`.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Toan: 9.5
  Anh: 9.0
  ```
* **Gợi ý:** Lần lượt gán và `pop`; in bằng `items()`.

### Bài 18: Tìm môn điểm cao nhất

* **Đề bài:** `diem = {"Toan": 7.5, "Van": 9.0, "Anh": 8.0, "Ly": 9.0}`. Tìm và in môn có điểm cao nhất cùng điểm số đó.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Mon cao nhat: Van, diem: 9.0
  ```
* **Gợi ý:** Duyệt `items()` để so sánh; nếu điểm bằng nhau, chọn môn gặp trước. (Môn `Van` gặp trước `Ly`.)

### Bài 19: Dict comprehension nhân đôi điểm

* **Đề bài:** `diem = {"Toan": 4, "Van": 5, "Anh": 6}`. Dùng dict comprehension tạo từ điển mới với điểm gấp đôi, in kết quả.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  {'Toan': 8, 'Van': 10, 'Anh': 12}
  ```
* **Gợi ý:** `{mon: d * 2 for mon, d in diem.items()}`.

### Bài 20: Tổng hợp — xếp loại học sinh

* **Đề bài:** Cho `diem = {"Toan": 8.5, "Van": 7.0, "Anh": 9.0, "Ly": 6.5}`. Viết chương trình:
  1. In bảng điểm từng môn.
  2. Tính điểm trung bình (làm tròn 2 chữ số).
  3. Xếp loại: ≥ 8.0 → `Gioi`, ≥ 6.5 → `Kha`, ≥ 5.0 → `Trung binh`, còn lại → `Yeu`.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Toan: 8.5
  Van: 7.0
  Anh: 9.0
  Ly: 6.5
  Trung binh: 7.75
  Xep loai: Kha
  ```
* **Gợi ý:** Kết hợp `items()`, `sum()`/`len()` và chuỗi `if...elif...else`.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Thành thạo tạo, truy cập (kể cả `get()` an toàn), thêm, sửa, xóa dictionary.
* ✅ Duyệt từ điển bằng `keys()`, `values()`, `items()` và dùng `in`, `len()`.
* ✅ Xây dựng các chương trình thực tế: điểm học, menu, đếm tần suất, dict comprehension.

> 💪 Chưa tự làm được bài nào thì đừng lo — xem lại bài giảng rồi quay lại. **Lập trình là luyện tập!**

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 18: Chuỗi](../18_String/bai_giang.md)**
