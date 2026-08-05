# 📝 Bài 14: Bài Tập – Danh Sách (List)

> 🎯 **Chủ đề:** Tạo list, truy cập, cắt slice, thêm/xóa, tìm kiếm, sắp xếp, đảo, duyệt, list lồng nhau và copy list an toàn.

---

## 📌 Hướng dẫn làm bài

* Mỗi bài tập cần **tự viết code** rồi chạy thử trước khi xem đáp án.
* Nếu chưa nhớ lý thuyết, hãy xem lại [bài giảng 14](bai_giang.md).
* Đáp án chi tiết 20 bài: 👉 [xem file dap_an.md](dap_an.md)

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Tạo danh sách trái cây

* **Đề bài:** Tạo list `trai_cay` chứa 4 loại quả: `"tao"`, `"chuoi"`, `"cam"`, `"xoai"`. In ra phần tử đầu tiên và phần tử cuối cùng.
* **Input:** Không có.
* **Output:**
  ```
  tao
  xoai
  ```
* **Gợi ý:** Index đầu tiên là `0`, index cuối có thể dùng `-1`.

### Bài 2: In toàn bộ danh sách

* **Đề bài:** Cho list `so = [10, 20, 30, 40, 50]`. Viết chương trình in ra từng số trên một dòng.
* **Input:** Không có.
* **Output:**
  ```
  10
  20
  30
  40
  50
  ```
* **Gợi ý:** Dùng vòng lặp `for x in so:`.

### Bài 3: Độ dài và tổng

* **Đề bài:** Cho `diem = [8, 9, 10, 7]`. In ra số lượng phần tử và tổng điểm.
* **Input:** Không có.
* **Output:**
  ```
  So phan tu: 4
  Tong diem: 34
  ```
* **Gợi ý:** Dùng `len()` và `sum()`.

### Bài 4: Thêm phần tử vào cuối

* **Đề bài:** Tạo list rỗng `gio_hang`, rồi lần lượt thêm `"sua"`, `"trung"`, `"banh mi"` bằng `append`. In list kết quả.
* **Input:** Không có.
* **Output:**
  ```
  ['sua', 'trung', 'banh mi']
  ```
* **Gợi ý:** `gio_hang = []` rồi gọi `gio_hang.append(...)` ba lần.

### Bài 5: Tìm vị trí phần tử

* **Đề bài:** Cho `mon = ["pho", "bun", "com", "mi"]`. In ra vị trí (index) của `"com"` và kiểm tra xem `"banh"` có trong list không.
* **Input:** Không có.
* **Output:**
  ```
  2
  False
  ```
* **Gợi ý:** `mon.index("com")` và `"banh" in mon`.

### Bài 6: Xóa phần tử

* **Đề bài:** Cho `diem = [5, 8, 7, 5]`. Xóa giá trị `5` đầu tiên rồi in list; sau đó xóa phần tử cuối bằng `pop()` và in ra list.
* **Input:** Không có.
* **Output:**
  ```
  [8, 7, 5]
  [8, 7]
  ```
* **Gợi ý:** `diem.remove(5)` xóa theo giá trị; `diem.pop()` xóa phần tử cuối.

### Bài 7: Sắp xếp tăng dần

* **Đề bài:** Cho `so = [9, 1, 7, 3]`. Sắp xếp list theo thứ tự tăng dần rồi in ra.
* **Input:** Không có.
* **Output:**
  ```
  [1, 3, 7, 9]
  ```
* **Gợi ý:** `so.sort()` sẽ sửa ngay list gốc.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Điểm trung bình của lớp

* **Đề bài:** Cho danh sách điểm `[6.5, 8.0, 9.5, 5.0, 7.5]`. Tính và in ra điểm trung bình (làm tròn 2 chữ số), điểm cao nhất và thấp nhất.
* **Input:** Không có.
* **Output:**
  ```
  Trung binh: 7.3
  Cao nhat: 9.5
  Thap nhat: 5.0
  ```
* **Gợi ý:** Kết hợp `sum`, `len`, `max`, `min` và `round`.

### Bài 9: Lọc số chẵn

* **Đề bài:** Cho `so = [1, 4, 7, 8, 10, 13]`. Tạo list mới `so_chan` chỉ chứa các số chẵn rồi in ra.
* **Input:** Không có.
* **Output:**
  ```
  [4, 8, 10]
  ```
* **Gợi ý:** Duyệt list, kiểm tra `x % 2 == 0`, rồi `append` vào list kết quả.

### Bài 10: Chia danh sách thành 3 phần

* **Đề bài:** Cho `so = [1, 2, 3, 4, 5, 6, 7, 8, 9]`. In ra: 3 số đầu, 3 số giữa, 3 số cuối bằng cách cắt slice.
* **Input:** Không có.
* **Output:**
  ```
  [1, 2, 3]
  [4, 5, 6]
  [7, 8, 9]
  ```
* **Gợi ý:** Dùng `so[:3]`, `so[3:6]`, `so[6:]`.

### Bài 11: Đếm số lần xuất hiện

* **Đề bài:** Cho chuỗi chữ: `"toi thich hoc python vi python don gian"` (lưu dưới dạng list các từ). Đếm xem từ `"python"` xuất hiện mấy lần và in ra.
* **Input:** Không có.
* **Output:**
  ```
  2
  ```
* **Gợi ý:** Tách chuỗi thành list bằng `cau.split()` rồi dùng `list.count("python")`.

### Bài 12: Hoán đổi vị trí

* **Đề bài:** Cho `ds = [1, 2, 3, 4]`. Viết chương trình hoán đổi phần tử đầu và phần tử cuối cho nhau, rồi in ra.
* **Input:** Không có.
* **Output:**
  ```
  [4, 2, 3, 1]
  ```
* **Gợi ý:** Dùng biến tạm hoặc hoán đổi trực tiếp `ds[0], ds[-1] = ds[-1], ds[0]`.

### Bài 13: Kiểm tra tăng dần

* **Đề bài:** Cho `ds = [1, 3, 5, 7]`. Viết chương trình kiểm tra list này có được sắp xếp tăng dần hay không và in ra `True`/`False`.
* **Input:** Không có.
* **Output:**
  ```
  True
  ```
* **Gợi ý:** So sánh từng cặp phần tử liền kề trong vòng lặp; hoặc so sánh `ds` với `sorted(ds)`.

### Bài 14: Sinh viên mới

* **Đề bài:** Lớp có danh sách `["An", "Binh", "Chi"]`. Bạn "Dung" chuyển đến, cần xếp **đúng vị trí giữa list** (sau "Binh"); sau đó bạn "An" chuyển trường phải xóa. In list cuối cùng.
* **Input:** Không có.
* **Output:**
  ```
  ['Binh', 'Dung', 'Chi']
  ```
* **Gợi ý:** `insert(index, "Dung")` với index hợp lý, rồi `remove("An")`. Lưu ý thứ tự thao tác.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Bảng điểm học sinh (list lồng nhau)

* **Đề bài:** Cho `bang_diem = [["An", 8, 9], ["Binh", 7, 8], ["Chi", 9, 10]]` (tên, điểm Toán, điểm Văn). In ra tên và **tổng điểm** của từng bạn, rồi in tên bạn có tổng điểm cao nhất.
* **Input:** Không có.
* **Output:**
  ```
  An: 17
  Binh: 15
  Chi: 19
  Cao nhat: Chi
  ```
* **Gợi ý:** Duyệt từng hàng, cộng `hang[1] + hang[2]`; dùng biến `max` để lưu bạn đang dẫn đầu.

### Bài 16: Bảng cửu chương từ danh sách

* **Đề bài:** Cho list `nhan = [2, 3, 4, 5]`. In ra bảng nhân `x * 1`, `x * 2`, `x * 3` cho từng giá trị `x` trong list (mỗi giá trị một dòng, các phép tính cách nhau dấu `, `).
* **Input:** Không có.
* **Output:**
  ```
  2x1=2, 2x2=4, 2x3=6
  3x1=3, 3x2=6, 3x3=9
  4x1=4, 4x2=8, 4x3=12
  5x1=5, 5x2=10, 5x3=15
  ```
* **Gợi ý:** Hai vòng lặp lồng nhau: vòng ngoài duyệt `nhan`, vòng trong chạy 1 → 3; gom chuỗi rồi in một lần.

### Bài 17: Xóa các phần tử trùng lặp liên tiếp

* **Đề bài:** Cho `ds = [1, 1, 2, 2, 2, 3, 4, 4, 5]`. Viết chương trình tạo list mới chỉ giữ lại **một** bản của mỗi phần tử đứng **liền kề nhau** (các phần tử trùng nhưng tách rời thì vẫn giữ). In list kết quả.
* **Input:** Không có.
* **Output:**
  ```
  [1, 2, 3, 4, 5]
  ```
* **Gợi ý:** Duyệt list, chỉ thêm phần tử vào list kết quả nếu nó **khác phần tử đứng trước** trong list kết quả.

### Bài 18: Ghép danh sách lệch thứ tự

* **Đề bài:** Cho hai list đã sắp tăng dần `a = [1, 3, 5]` và `b = [2, 4, 6]`. Viết chương trình **trộn (merge)** chúng thành một list duy nhất vẫn **tăng dần** và in ra.
* **Input:** Không có.
* **Output:**
  ```
  [1, 2, 3, 4, 5, 6]
  ```
* **Gợi ý:** Không dùng `sorted(a + b)`. Dùng hai biến chỉ số `i`, `j` so sánh lần lượt: phần tử nhỏ hơn được đưa vào kết quả trước (kỹ thuật **two-pointer**).

### Bài 19: Dịch chuyển vòng (rotate)

* **Đề bài:** Cho `ds = [1, 2, 3, 4, 5]`. Viết chương trình **dịch phải vòng tròn** 2 lần: mỗi lần phần tử cuối nhảy lên đầu, các phần tử còn lại lùi xuống. In list kết quả.
* **Input:** Không có.
* **Output:**
  ```
  [4, 5, 1, 2, 3]
  ```
* **Gợi ý:** Mỗi lần dịch: `ds.insert(0, ds.pop())`. Lặp đúng 2 lần.

### Bài 20: Copy an toàn — ứng dụng chấm điểm

* **Đề bài:** Cho `goc = [7, 9, 8, 6]`. Viết chương trình **sao chép an toàn** `goc` sang list `sao` (không được để thay đổi `sao` ảnh hưởng `goc`). Sau đó `sao` cộng thêm 1 điểm cho mỗi phần tử, in ra cả hai list để thấy `goc` không đổi.
* **Input:** Không có.
* **Output:**
  ```
  Sao (sau khi +1): [8, 10, 9, 7]
  Goc (khong doi): [7, 9, 8, 6]
  ```
* **Gợi ý:** Đừng gán bằng `=`. Dùng `copy()`, `list()`, hoặc `[:]`. Cộng điểm bằng vòng lặp duyệt theo index.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Tạo, truy cập và cắt list thành thạo.
* ✅ Thêm/xóa/sắp xếp/đảo list đúng cách.
* ✅ Duyệt list, xử lý list lồng nhau và copy an toàn.

> 💪 Nếu bài nào chưa tự làm được, hãy xem lại [bài giảng 14](bai_giang.md) rồi thử lại. **Lập trình là luyện tập!**

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 15: Tuple (Bộ dữ liệu)](../15_Tuple/bai_giang.md)**
