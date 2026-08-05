# ✅ Bài 16: Đáp Án – Set (Tập Hợp)

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án để việc học hiệu quả nhất.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Tạo set đầu tiên

**Phân tích:** Tạo set 3 phần tử và đếm số phần tử.

**Ý tưởng:** `len()` đếm phần tử của set như của list/tuple.

**Thuật toán:**
1. Tạo set `trai_cay`.
2. In `len(trai_cay)`.

**Code:**

```python
# Set 3 loại trái cây
trai_cay = {"tao", "chuoi", "cam"}
# Số phần tử trong set
print(len(trai_cay))
```

**Giải thích code:**
* `{"tao", "chuoi", "cam"}` — set tạo bằng ngoặc nhọn.
* `len(trai_cay)` → 3.
* Lưu ý: dấu `{}` khi chứa dữ liệu tạo **set**, nhưng `{}` rỗng là dictionary.

**Độ phức tạp:** O(1).

---

### Bài 2: Kiểm tra phần tử

**Phân tích:** Kiểm tra sự tồn tại của hai giá trị.

**Ý tưởng:** Toán tử `in` trả `True`/`False` — với set hoạt động **rất nhanh**.

**Thuật toán:**
1. Tạo set `mon`.
2. In `"Toan" in mon`.
3. In `"Ly" in mon`.

**Code:**

```python
# Set các môn học
mon = {"Toan", "Van", "Anh"}
# "Toan" có trong set không?
print("Toan" in mon)
# "Ly" có trong set không?
print("Ly" in mon)
```

**Giải thích code:**
* `"Toan" in mon` → `True`.
* `"Ly" in mon` → `False`.
* Khác list (phải duyệt từng phần), set dùng bảng băm nên kiểm tra gần như tức thời.

**Độ phức tạp:** O(1) trung bình.

---

### Bài 3: Loại phần tử trùng

**Phân tích:** Cần "nén" các giá trị trùng trong list thành set duy nhất.

**Ý tưởng:** `set(ds)` tự động loại bỏ trùng — tính duy nhất là đặc tính của set.

**Thuật toán:**
1. Tạo list `ds` có trùng.
2. `s = set(ds)`.
3. In set và số phần tử.

**Code:**

```python
# List có nhiều giá trị trùng
ds = [1, 2, 2, 3, 3, 3, 4]
# Chuyển sang set — tự loại bỏ phần tử trùng
s = set(ds)
# In set và số phần tử duy nhất
print(s)
print(len(s))
```

**Giải thích code:**
* `set(ds)` → `{1, 2, 3, 4}` — các số 2, 3 trùng bị "nuốt" gọn.
* `len(s)` → 4.
* Đây là cách ngắn nhất để đếm giá trị khác nhau trong danh sách.

**Độ phức tạp:** O(n) — duyệt toàn list để dựng set.

---

### Bài 4: Thêm phần tử

**Phân tích:** Set rỗng được thêm dần; phần tử trùng không làm tăng kích thước.

**Ý tưởng:** `set()` tạo set rỗng (không phải `{}`); `add` thêm một phần tử.

**Thuật toán:**
1. Tạo `thanh_vien = set()`.
2. `add("An")`, `add("Binh")`, `add("An")`.
3. In set và `len`.

**Code:**

```python
# Set rỗng — bắt buộc dùng set(), không dùng {}
thanh_vien = set()
# Thêm từng thành viên
thanh_vien.add("An")
thanh_vien.add("Binh")
# Thêm "An" lần nữa — không làm tăng phần tử vì đã có
thanh_vien.add("An")
# In kết quả
print(thanh_vien)
print(len(thanh_vien))
```

**Giải thích code:**
* `set()` — cách duy nhất để tạo set rỗng.
* `add("An")` lần hai không đổi gì — tính duy nhất của set.
* Kết quả `{'An', 'Binh'}` với số lượng 2.

**Độ phức tạp:** O(1) mỗi lần `add`.

---

### Bài 5: Thêm nhiều phần tử

**Phân tích:** Thêm cả một nhóm phần tử vào set trong một lần.

**Ý tưởng:** `update([...])` nhận một dãy (list/tuple/chuỗi) và thêm từng phần tử.

**Thuật toán:**
1. Tạo set `s = {1, 2}`.
2. `s.update([3, 4])`.
3. In set.

**Code:**

```python
# Set ban đầu
s = {1, 2}
# Thêm nhiều phần tử cùng lúc bằng update
s.update([3, 4])
# In kết quả
print(s)
```

**Giải thích code:**
* `update([3, 4])` — thêm cả 3 và 4 vào set.
* Nếu thêm trùng, tự động bỏ qua.
* `add` chỉ thêm **một** phần tử; `update` thêm **nhiều**.

**Độ phức tạp:** O(k) với k là số phần tử thêm.

---

### Bài 6: Xóa với discard

**Phân tích:** Xóa phần tử có thể **không tồn tại** mà không sợ lỗi.

**Ý tưởng:** `discard` im lặng bỏ qua khi phần tử không có — an toàn hơn `remove`.

**Thuật toán:**
1. Tạo set `s`.
2. `s.discard("Binh")`.
3. `s.discard("Dung")` — không có, không lỗi.
4. In set.

**Code:**

```python
# Set thành viên
s = {"An", "Binh", "Chi"}
# Xóa "Binh" — có trong set nên xóa được
s.discard("Binh")
# Xóa "Dung" — KHÔNG có trong set, discard im lặng bỏ qua
s.discard("Dung")
# In kết quả — chương trình chạy bình thường
print(s)
```

**Giải thích code:**
* `discard` không báo lỗi dù phần tử vắng mặt.
* Nếu dùng `remove("Dung")` ở vị trí này sẽ báo `KeyError`.
* Kết quả: `{'An', 'Chi'}`.

**Độ phức tạp:** O(1) trung bình.

---

### Bài 7: Hợp hai set

**Phân tích:** Phép hợp gom mọi phần tử của cả hai set.

**Ý tưởng:** Toán tử `|` — mỗi phần tử chỉ xuất hiện một lần.

**Thuật toán:**
1. Tạo hai set `a`, `b`.
2. `hop = a | b`.
3. In set và `len`.

**Code:**

```python
# Hai tập hợp
a = {1, 2}
b = {2, 3}
# Phép hợp — gom mọi phần tử, không trùng
hop = a | b
# In kết quả và số phần tử
print(hop)
print(len(hop))
```

**Giải thích code:**
* `a | b` → `{1, 2, 3}` — số 2 chung chỉ xuất hiện một lần.
* `len(hop)` → 3.
* Tương đương `a.union(b)`.

**Độ phức tạp:** O(n + m).

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Giao, hiệu, đối xứng

**Phân tích:** Thực hiện ba phép toán tập hợp trên hai set.

**Ý tưởng:** `&` giao, `-` hiệu, `^` đối xứng — kết quả là set mới.

**Thuật toán:**
1. Tạo `a`, `b`.
2. In `a & b`, `a - b`, `a ^ b`.

**Code:**

```python
# Hai tập hợp
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
# Giao: phần tử chung
print(a & b)
# Hiệu: phần tử của a nhưng không thuộc b
print(a - b)
# Hiệu đối xứng: chỉ thuộc đúng một trong hai
print(a ^ b)
```

**Giải thích code:**
* `a & b` → `{3, 4}` (chung).
* `a - b` → `{1, 2}` (chỉ của a).
* `a ^ b` → `{1, 2, 5, 6}` (mỗi phần tử chỉ thuộc một set).

**Độ phức tạp:** O(n + m) mỗi phép.

---

### Bài 9: Đếm ký tự khác nhau

**Phân tích:** Chuỗi có ký tự lặp; cần đếm loại ký tự khác nhau.

**Ý tưởng:** `set(chuỗi)` tách chuỗi thành set **từng ký tự** và loại trùng.

**Thuật toán:**
1. Khởi tạo chuỗi.
2. `s = set(cau)`.
3. In `len(s)`.

**Code:**

```python
# Chuỗi cần đếm ký tự
cau = "abracadabra"
# set(chuỗi) tách thành các ký tự và loại trùng
s = set(cau)
# Số ký tự khác nhau
print(len(s))
```

**Giải thích code:**
* `set("abracadabra")` → `{'a', 'b', 'c', 'd', 'r'}`.
* `len(s)` → 5.
* Cách đếm ký tự phân biệt ngắn gọn nhất trong Python.

**Độ phức tạp:** O(n) với n là độ dài chuỗi.

---

### Bài 10: So sánh remove và discard

**Phân tích:** Cần chứng minh `remove` báo `KeyError`, `discard` thì không.

**Ý tưởng:** Bắt lỗi bằng `try...except KeyError` rồi chuyển sang `discard`.

**Thuật toán:**
1. Tạo set `s`.
2. `try: s.remove("Dung")` → `except KeyError: in thông báo`.
3. `s.discard("Dung")` → in thông báo.
4. In set.

**Code:**

```python
# Set thành viên
s = {"An", "Binh"}
# remove sẽ ném KeyError vì "Dung" không tồn tại
try:
    s.remove("Dung")
except KeyError:
    # Bắt lỗi và in tên loại lỗi
    print("Loi: KeyError")
# discard không ném lỗi — im lặng bỏ qua
s.discard("Dung")
print("Duoc discard bo qua 'Dung'")
# In set cuối cùng — không đổi
print(s)
```

**Giải thích code:**
* `s.remove("Dung")` — phần tử vắng mặt → Python ném `KeyError`.
* `except KeyError` — bắt đúng lỗi, chương trình không dừng.
* `s.discard("Dung")` — không lỗi, set giữ nguyên `{'An', 'Binh'}`.

**Độ phức tạp:** O(1) trung bình.

---

### Bài 11: Lọc tên trùng trong danh sách đăng ký

**Phân tích:** Danh sách thí sinh bị ghi trùng; cần danh sách tên duy nhất.

**Ý tưởng:** `set(danh_sach)` loại trùng; `sorted()` để in có thứ tự dễ đọc.

**Thuật toán:**
1. Khởi tạo list.
2. `s = set(danh_sach)`.
3. In set và `len`.

**Code:**

```python
# Danh sách đăng ký — có tên trùng
danh_sach = ["An", "Binh", "An", "Chi", "Dung", "Chi"]
# Loại trùng bằng set
s = set(danh_sach)
# In set và số thí sinh duy nhất
print(s)
print(len(s))
```

**Giải thích code:**
* `set(danh_sach)` → `{'An', 'Binh', 'Chi', 'Dung'}`.
* `len(s)` → 4 (thay vì 6 lượt đăng ký).
* Muốn in có thứ tự, dùng `sorted(s)`.

**Độ phức tạp:** O(n).

---

### Bài 12: Kiểm tra môn đã đăng ký

**Phân tích:** Vừa kiểm tra vừa thêm môn chưa có vào set.

**Ý tưởng:** `in` để kiểm tra; `add` để thêm — kết hợp thành quy tắc "thêm nếu chưa có".

**Thuật toán:**
1. Tạo set `da_dang_ky`.
2. Nếu `"Van" not in da_dang_ky`: thêm.
3. Nếu `"Toan" in da_dang_ky`: in `"Da co"`.
4. In set.

**Code:**

```python
# Các môn đã đăng ký
da_dang_ky = {"Toan", "Anh"}
# "Van" chưa có → thêm vào
if "Van" not in da_dang_ky:
    da_dang_ky.add("Van")
# "Toan" đã có → thông báo
if "Toan" in da_dang_ky:
    print("Da co")
# In set cuối cùng
print(da_dang_ky)
```

**Giải thích code:**
* `"Van" not in da_dang_ky` → `True` nên `add("Van")`.
* `"Toan" in da_dang_ky` → `True` nên in `Da co`.
* Kết quả set: `{'Toan', 'Anh', 'Van'}`.

**Độ phức tạp:** O(1) trung bình.

---

### Bài 13: Học sinh giỏi cả hai môn

**Phân tích:** Tìm học sinh giỏi cả hai môn (giao) và giỏi ít nhất một môn (hợp).

**Ý tưởng:** `&` và `|`.

**Thuật toán:**
1. Tạo hai set.
2. `ca_hai = gioi_toan & gioi_van`.
3. `it_nhat_mot = gioi_toan | gioi_van`.
4. In kết quả.

**Code:**

```python
# Học sinh giỏi từng môn
gioi_toan = {"An", "Binh", "Chi"}
gioi_van = {"Binh", "Chi", "Dung"}
# Giỏi CẢ HAI môn → giao
gioi_ca_hai = gioi_toan & gioi_van
print("Gioi ca hai:", gioi_ca_hai)
# Giỏi ÍT NHẤT MỘT môn → hợp
gioi_it_nhat_mot = gioi_toan | gioi_van
print("Gioi it nhat 1 mon:", gioi_it_nhat_mot)
```

**Giải thích code:**
* Giao → `{'Binh', 'Chi'}`.
* Hợp → `{'An', 'Binh', 'Chi', 'Dung'}`.
* Không cần vòng lặp nào — sức mạnh của phép toán tập hợp.

**Độ phức tạp:** O(n + m).

---

### Bài 14: Bạn chung của hai người

**Phân tích:** Tìm bạn chung và đếm bạn "riêng" (chỉ quen một người).

**Ý tưởng:** Giao `&` cho bạn chung; hiệu đối xứng `^` cho bạn riêng.

**Thuật toán:**
1. Tạo hai set bạn.
2. `ban_chung = ban_an & ban_binh`.
3. `ban_rieng = ban_an ^ ban_binh` và đếm `len`.
4. In kết quả.

**Code:**

```python
# Bạn của An và bạn của Binh
ban_an = {"Binh", "Chi", "Dung"}
ban_binh = {"An", "Chi", "Dung", "Em"}
# Bạn CHUNG của cả hai → giao
ban_chung = ban_an & ban_binh
print("Ban chung:", ban_chung)
# Bạn chỉ quen ĐÚNG một người → hiệu đối xứng
ban_rieng = ban_an ^ ban_binh
print("Ban chi quen 1 nguoi:", len(ban_rieng))
```

**Giải thích code:**
* `ban_chung` → `{'Chi', 'Dung'}`.
* `ban_an ^ ban_binh` → `{'An', 'Binh', 'Em'}` — 3 người.
* Hiệu đối xứng loại các phần tử chung, giữ phần tử chỉ thuộc một set.

**Độ phức tạp:** O(n + m).

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Kiểm tra tập con

**Phân tích:** Cần kiểm tra mọi phần tử của set này đều nằm trong set kia.

**Ý tưởng:** Phương thức `issubset()` — trả `True` nếu là tập con.

**Thuật toán:**
1. Tạo hai set.
2. In `lop_10A.issubset(toan_truong)`.

**Code:**

```python
# Lớp 10A và toàn trường
lop_10A = {"An", "Binh", "Chi"}
toan_truong = {"An", "Binh", "Chi", "Dung", "Em"}
# Kiểm tra mọi học sinh 10A có trong toàn trường không
print(lop_10A.issubset(toan_truong))
```

**Giải thích code:**
* Mọi phần tử của `lop_10A` đều nằm trong `toan_truong` → `True`.
* Ngược lại: `toan_truong.issuperset(lop_10A)` cũng trả `True` (superset = tập chứa).
* Nếu đổi thành `{"An", "Xuan"}` thì trả `False`.

**Độ phức tạp:** O(n) với n là kích thước set con.

---

### Bài 16: Từ khóa xuất hiện trong cả hai bài viết

**Phân tích:** Cần tách chuỗi thành các từ, so sánh hai tập từ.

**Ý tưởng:** `split()` tách từ; `set(...)` dựng tập từ; `&` cho từ chung, `|` + `len` cho tổng duy nhất.

**Thuật toán:**
1. Tạo hai chuỗi.
2. `s1 = set(bai_1.split())`, `s2 = set(bai_2.split())`.
3. `tu_chung = s1 & s2`.
4. `len(s1 | s2)`.
5. In kết quả.

**Code:**

```python
# Hai bài viết
bai_1 = "python lap trinh la de hoc va dong dao"
bai_2 = "python dung de phan tich du lieu dong dao"
# Tách chuỗi thành set các từ
s1 = set(bai_1.split())
s2 = set(bai_2.split())
# Từ xuất hiện trong CẢ HAI bài → giao
tu_chung = s1 & s2
print("Tu chung:", tu_chung)
# Tổng từ duy nhất của cả hai bài → hợp
tong_tu = len(s1 | s2)
print("Tong tu duy nhat:", tong_tu)
```

**Giải thích code:**
* `bai_1.split()` tách theo khoảng trắng thành list các từ.
* Giao → `{'python', 'de', 'dong', 'dao'}`.
* Hợp: mỗi bài 9 từ, chung 4 → tổng duy nhất 9 + 9 − 4 = 14.

**Độ phức tạp:** O(n + m) với n, m là số từ hai bài.

---

### Bài 17: Tìm phần tử lạc (xuất hiện một lần)

**Phân tích:** Mọi số xuất hiện 2 lần trừ một số — cần tìm số "lạc".

**Ý tưởng:** Duyệt các giá trị duy nhất (từ `set(so)`), đếm số lần xuất hiện trong list gốc bằng `count`.

**Thuật toán:**
1. Tạo list `so`.
2. `for x in set(so):` kiểm tra `so.count(x) == 1`.
3. In số tìm được.

**Code:**

```python
# Mọi số xuất hiện 2 lần, một số chỉ 1 lần
so = [1, 2, 3, 4, 2, 3, 4]
# Duyệt các giá trị duy nhất
for x in set(so):
    # Số lạc là số chỉ xuất hiện đúng 1 lần
    if so.count(x) == 1:
        print(x)
        break
```

**Giải thích code:**
* `set(so)` → `{1, 2, 3, 4}` — chỉ xét mỗi giá trị một lần.
* `so.count(1)` = 1 → in ra `1` và dừng.
* Các số khác đếm ra 2 nên bỏ qua.

**Độ phức tạp:** O(n²) với cách `count` lặp lại; cải tiến được bằng dict đếm (bài 17).

---

### Bài 18: Hiệu chỉnh danh sách trùng

**Phân tích:** Mã sản phẩm trùng giữa hai list phải bị loại khỏi list a.

**Ý tưởng:** Giao `&` tìm mã trùng; hiệu `-` tìm mã chỉ có trong a (đã loại trùng tự động).

**Thuật toán:**
1. Tạo hai list.
2. `sa = set(a)`, `sb = set(b)`.
3. `ma_trung = sa & sb`.
4. `con_lai = sa - sb`.
5. In kết quả.

**Code:**

```python
# Hai danh sách mã sản phẩm
a = ["SP1", "SP2", "SP3"]
b = ["SP2", "SP4", "SP5"]
# Chuyển sang set để so sánh
sa = set(a)
sb = set(b)
# Mã có ở CẢ HAI nơi → giao
ma_trung = sa & sb
print("Ma trung:", ma_trung)
# Mã chỉ có trong a (đã loại phần trùng) → hiệu
con_lai = sa - sb
print("Con lai trong a:", con_lai)
```

**Giải thích code:**
* `ma_trung` → `{'SP2'}`.
* `sa - sb` → `{'SP1', 'SP3'}` — hiệu tự loại SP2 vì nó thuộc cả `sb`.
* Hai dòng toán tập hợp thay cho cả vòng lặp dài dòng.

**Độ phức tạp:** O(n + m).

---

### Bài 19: Hệ thống quét thẻ sinh viên

**Phân tích:** Thẻ bị quét nhiều lần — cần danh sách có mặt mỗi người một lần, có thứ tự.

**Ý tưởng:** `set(the)` loại trùng; `sorted()` sắp xếp mã.

**Thuật toán:**
1. Tạo list thẻ.
2. `co_mat = sorted(set(the))`.
3. In list và số lượng.

**Code:**

```python
# Danh sách thẻ quét — có lần trùng
the = ["SV1", "SV2", "SV1", "SV3", "SV2", "SV4"]
# Loại trùng và sắp xếp theo mã
co_mat = sorted(set(the))
# In danh sách có mặt
print("Co mat:", co_mat)
print("So luong:", len(co_mat))
```

**Giải thích code:**
* `set(the)` → `{'SV1', 'SV2', 'SV3', 'SV4'}`.
* `sorted(...)` → `['SV1', 'SV2', 'SV3', 'SV4']` — set không có thứ tự nên cần sắp xếp.
* `len` → 4.

**Độ phức tạp:** O(n log n) — chi phí sắp xếp.

---

### Bài 20: Bầu chọn ứng viên đa năng

**Phân tích:** So sánh kỹ năng của ba ứng viên: chung cả ba, chỉ một người có, tổng duy nhất.

**Ý tưởng:** Giao nhiều set `a & b & c`; hiệu liên tiếp `a - b - c`; hợp `a | b | c`.

**Thuật toán:**
1. Tạo ba set kỹ năng.
2. `chung = a & b & c`.
3. `chi_an = a - b - c`.
4. `tong = len(a | b | c)`.
5. In kết quả.

**Code:**

```python
# Kỹ năng của từng ứng viên
an_ky_nang = {"python", "thuyet_trinh", "phan_tich"}
binh_ky_nang = {"python", "thiet_ke", "thuyet_trinh"}
chi_ky_nang = {"python", "quan_ly", "marketing"}
# Kỹ năng chung của CẢ BA → giao nhiều set
chung = an_ky_nang & binh_ky_nang & chi_ky_nang
print("Ky nang chung:", chung)
# Kỹ năng CHỈ An có → trừ dần kỹ năng của hai người kia
chi_an = an_ky_nang - binh_ky_nang - chi_ky_nang
print("Chi An co:", chi_an)
# Tổng kỹ năng duy nhất của cả nhóm → hợp
tong = len(an_ky_nang | binh_ky_nang | chi_ky_nang)
print("Tong ky nang duy nhat:", tong)
```

**Giải thích code:**
* Giao 3 set: chỉ `'python'` có ở cả ba → `{'python'}`.
* `an - binh - chi` → `{'phan_tich'}` (bỏ thuyet_trinh vì Bình cũng có, bỏ python vì mọi người có).
* Hợp 3 set: mỗi người 3 kỹ năng, trùng `python` (3 lần → tính 1) và `thuyet_trinh` (An, Bình → tính 1) → tổng duy nhất = 9 − 2 (python) − 1 (thuyet_trinh) = 6.

**Độ phức tạp:** O(n + m + p).

---

## 📌 Lời khuyên cuối

* ⭐ Dùng `set(danh_sach)` để loại trùng — nhanh và ngắn hơn mọi vòng lặp.
* 🛡️ `discard` khi dữ liệu không chắc chắn; `remove` khi chắc chắn tồn tại.
* 🧮 Bốn phép toán `| & - ^` giải quyết mọi bài toán "chung/riêng/khác".
* ⚠️ Nhớ: `{}` là dictionary — muốn set rỗng phải dùng `set()`.
* 🔍 Duyệt set không đảm bảo thứ tự — dùng `sorted()` khi cần.

👉 Tiếp theo: **[Bài 17: Dictionary (Từ điển)](../17_Dictionary/bai_giang.md)**
