# 📝 Bài 16: Bài Tập – Set (Tập Hợp)

> 🎯 **Chủ đề:** Tạo set, tính duy nhất, add/remove/discard/clear, membership `in`, phép toán tập hợp và khi nào dùng set.

---

## 📌 Hướng dẫn làm bài

* Mỗi bài tập cần **tự viết code** rồi chạy thử trước khi xem đáp án.
* Nếu chưa nhớ lý thuyết, hãy xem lại [bài giảng 16](bai_giang.md).
* Đáp án chi tiết 20 bài: 👉 [xem file dap_an.md](dap_an.md)

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Tạo set đầu tiên

* **Đề bài:** Tạo set `trai_cay = {"tao", "chuoi", "cam"}` và in ra `len()` của nó.
* **Input:** Không có.
* **Output:**
  ```
  3
  ```
* **Gợi ý:** `len(set)` đếm số phần tử.

### Bài 2: Kiểm tra phần tử

* **Đề bài:** Cho `mon = {"Toan", "Van", "Anh"}`. Kiểm tra `"Toan"` và `"Ly"` có trong set không, in hai kết quả.
* **Input:** Không có.
* **Output:**
  ```
  True
  False
  ```
* **Gợi ý:** Dùng toán tử `in`.

### Bài 3: Loại phần tử trùng

* **Đề bài:** Cho list `ds = [1, 2, 2, 3, 3, 3, 4]`. Chuyển sang set để loại trùng rồi in ra set và số phần tử duy nhất.
* **Input:** Không có.
* **Output:**
  ```
  {1, 2, 3, 4}
  4
  ```
* **Gợi ý:** `set(ds)` và `len(set(ds))`.

### Bài 4: Thêm phần tử

* **Đề bài:** Tạo set rỗng `thanh_vien = set()`. Thêm lần lượt `"An"`, `"Binh"`, `"An"` bằng `add`. In ra set và số thành viên.
* **Input:** Không có.
* **Output:**
  ```
  {'An', 'Binh'}
  2
  ```
* **Gợi ý:** Thêm `"An"` lần 2 không làm tăng số phần tử.

### Bài 5: Thêm nhiều phần tử

* **Đề bài:** Cho `s = {1, 2}`. Dùng `update([3, 4])` để thêm hai số nữa rồi in ra set.
* **Input:** Không có.
* **Output:**
  ```
  {1, 2, 3, 4}
  ```
* **Gợi ý:** `s.update([3, 4])`.

### Bài 6: Xóa với discard

* **Đề bài:** Cho `s = {"An", "Binh", "Chi"}`. Xóa `"Binh"` bằng `discard`, rồi `discard("Dung")` (không có — thử xem có lỗi không). In set kết quả.
* **Input:** Không có.
* **Output:**
  ```
  {'An', 'Chi'}
  ```
* **Gợi ý:** `discard` không báo lỗi khi phần tử không tồn tại.

### Bài 7: Hợp hai set

* **Đề bài:** Cho `a = {1, 2}` và `b = {2, 3}`. In ra phép hợp `a | b` và số phần tử của nó.
* **Input:** Không có.
* **Output:**
  ```
  {1, 2, 3}
  3
  ```
* **Gợi ý:** Dùng toán tử `|`.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Giao, hiệu, đối xứng

* **Đề bài:** Cho `a = {1, 2, 3, 4}` và `b = {3, 4, 5, 6}`. In ra lần lượt: `a & b`, `a - b`, `a ^ b`.
* **Input:** Không có.
* **Output:**
  ```
  {3, 4}
  {1, 2}
  {1, 2, 5, 6}
  ```
* **Gợi ý:** Nhớ `&` là giao, `-` là hiệu, `^` là đối xứng.

### Bài 9: Đếm ký tự khác nhau

* **Đề bài:** Cho chuỗi `cau = "abracadabra"`. Đếm và in ra số ký tự **khác nhau** xuất hiện trong chuỗi.
* **Input:** Không có.
* **Output:**
  ```
  5
  ```
* **Gợi ý:** `set(cau)` tách từng ký tự và loại trùng; đếm bằng `len`.

### Bài 10: So sánh remove và discard

* **Đề bài:** Cho `s = {"An", "Binh"}`. Viết chương trình dùng `try...except` để gọi `s.remove("Dung")` và bắt lỗi, sau đó dùng `s.discard("Dung")` và in thông báo kiểu lỗi. In ra set cuối cùng.
* **Input:** Không có.
* **Output:**
  ```
  Loi: KeyError
  Duoc discrim bo qua 'Dung'
  {'An', 'Binh'}
  ```
* **Gợi ý:** `remove` ném `KeyError`; bắt bằng `except KeyError`. `discard` không ném lỗi.

### Bài 11: Lọc tên trùng trong danh sách đăng ký

* **Đề bài:** Danh sách đăng ký dự thi lớp 10: `["An", "Binh", "An", "Chi", "Dung", "Chi"]`. Tạo set từ danh sách rồi in ra các tên duy nhất (mỗi tên một lần) và số thí sinh duy nhất.
* **Input:** Không có.
* **Output:**
  ```
  {'An', 'Binh', 'Chi', 'Dung'}
  4
  ```
* **Gợi ý:** `set(danh_sach)` rồi `sorted()` nếu muốn in có thứ tự (tùy chọn).

### Bài 12: Kiểm tra môn đã đăng ký

* **Đề bài:** Cho `da_dang_ky = {"Toan", "Anh"}`. Kiểm tra nếu `"Van"` chưa đăng ký thì thêm vào; nếu `"Toan"` đã đăng ký thì in `"Da co"`. In set cuối cùng.
* **Input:** Không có.
* **Output:**
  ```
  Da co
  {'Toan', 'Anh', 'Van'}
  ```
* **Gợi ý:** `x in set` để kiểm tra, `add` để thêm.

### Bài 13: Học sinh giỏi cả hai môn

* **Đề bài:** Cho `gioi_toan = {"An", "Binh", "Chi"}` và `gioi_van = {"Binh", "Chi", "Dung"}`. In ra học sinh giỏi **cả hai môn** và học sinh giỏi **ít nhất một môn**.
* **Input:** Không có.
* **Output:**
  ```
  Gioi ca hai: {'Binh', 'Chi'}
  Gioi it nhat 1 mon: {'An', 'Binh', 'Chi', 'Dung'}
  ```
* **Gợi ý:** Giao `&` và hợp `|`.

### Bài 14: Bạn chung của hai người

* **Đề bài:** Cho `ban_an = {"Binh", "Chi", "Dung"}` và `ban_binh = {"An", "Chi", "Dung", "Em"}`. In ra bạn chung và số bạn **chỉ quen đúng một người** trong hai người.
* **Input:** Không có.
* **Output:**
  ```
  Ban chung: {'Chi', 'Dung'}
  Ban chi quen 1 nguoi: 3
  ```
* **Gợi ý:** Giao `&`; đối xứng `^` rồi `len`.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Kiểm tra tập con

* **Đề bài:** Cho `lop_10A = {"An", "Binh", "Chi"}` và `toan_truong = {"An", "Binh", "Chi", "Dung", "Em"}`. Viết chương trình kiểm tra xem `lop_10A` có phải là **tập con** của `toan_truong` không và in `True`.
* **Input:** Không có.
* **Output:**
  ```
  True
  ```
* **Gợi ý:** Dùng phương thức `issubset()` — tìm hiểu thêm từ bài giảng/đọc thêm.

### Bài 16: Từ khóa xuất hiện trong cả hai bài viết

* **Đề bài:** Hai bài viết (dạng chuỗi) có nội dung:
  * `bai_1 = "python lap trinh la de hoc va dong dao"`
  * `bai_2 = "python dung de phan tich du lieu dong dao"`
  Tách thành set các từ, rồi in ra các **từ khóa chung** của hai bài và **số từ khóa duy nhất** toàn bộ.
* **Input:** Không có.
* **Output:**
  ```
  Tu chung: {'python', 'de', 'dong', 'dao'}
  Tong tu duy nhat: 14
  ```
* **Gợi ý:** `cau.split()` → `set(...)`; giao `&` cho từ chung; hợp `|` rồi `len` cho tổng duy nhất.

### Bài 17: Tìm phần tử lạc (xuất hiện một lần)

* **Đề bài:** Cho list `so = [1, 2, 3, 4, 2, 3, 4]` — mọi số đều xuất hiện đúng 2 lần **ngoại trừ một số** xuất hiện 1 lần. Viết chương trình in ra "số lạc" đó.
* **Input:** Không có.
* **Output:**
  ```
  1
  ```
* **Gợi ý:** Dùng set duy nhất đi với `count`: với mỗi phần tử trong `set(so)`, kiểm tra `so.count(x) == 1`.

### Bài 18: Hiệu chỉnh danh sách trùng

* **Đề bài:** Có 2 danh sách mã sản phẩm: `a = ["SP1", "SP2", "SP3"]` và `b = ["SP2", "SP4", "SP5"]`. Sản phẩm trùng giữa hai list phải bị **loại khỏi danh sách a** (chỉ còn ở một chỗ). Tính và in ra: mã trùng, mã chỉ có trong `a` sau khi loại trùng.
* **Input:** Không có.
* **Output:**
  ```
  Ma trung: {'SP2'}
  Con lai trong a: {'SP1', 'SP3'}
  ```
* **Gợi ý:** Giao `&` tìm trùng; hiệu `-` để biết mã chỉ thuộc a.

### Bài 19: Hệ thống quét thẻ sinh viên

* **Đề bài:** Khi điểm danh, mỗi sinh viên có thể bị quét thẻ **nhiều lần**. Viết chương trình từ một list thẻ `the = ["SV1", "SV2", "SV1", "SV3", "SV2", "SV4"]`, in ra danh sách sinh viên **có mặt** (mỗi người một lần, sắp xếp theo mã) và **số sinh viên có mặt**.
* **Input:** Không có.
* **Output:**
  ```
  Co mat: ['SV1', 'SV2', 'SV3', 'SV4']
  So luong: 4
  ```
* **Gợi ý:** `set(the)` loại trùng rồi `sorted()` cho thứ tự.

### Bài 20: Bầu chọn ứng viên đa năng

* **Đề bài:** Mỗi ứng viên được chấm điểm theo các **kỹ năng**. Cho:
  * `an_ky_nang = {"python", "thuyet_trinh", "phan_tich"}`
  * `binh_ky_nang = {"python", "thiet_ke", "thuyet_trinh"}`
  * `chi_ky_nang = {"python", "quan_ly", "marketing"}`
  Viết chương trình in ra: kỹ năng chung của cả ba người; kỹ năng chỉ An có (không ai khác có); tổng kỹ năng duy nhất của cả nhóm.
* **Input:** Không có.
* **Output:**
  ```
  Ky nang chung: {'python'}
  Chi An co: {'phan_tich'}
  Tong ky nang duy nhat: 6
  ```
* **Gợi ý:** Giao **nhiều** set bằng `a & b & c`; hiệu `an - binh - chi`; hợp `a | b | c` rồi `len`.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Tạo set, loại trùng và thao tác thêm/xóa thành thạo.
* ✅ Kiểm tra phần tử nhanh bằng `in`.
* ✅ Vận dụng 4 phép toán tập hợp vào bài toán thực tế.

> 💪 Nếu bài nào chưa tự làm được, hãy xem lại [bài giảng 16](bai_giang.md) rồi thử lại. **Lập trình là luyện tập!**

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 17: Dictionary (Từ điển)](../17_Dictionary/bai_giang.md)**