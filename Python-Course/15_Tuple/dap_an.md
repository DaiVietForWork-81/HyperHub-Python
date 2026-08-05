# ✅ Bài 15: Đáp Án – Tuple (Bộ Dữ Liệu)

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án để việc học hiệu quả nhất.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Tạo tuple đầu tiên

**Phân tích:** Tạo tuple 3 số, in phần tử đầu và cuối.

**Ý tưởng:** Truy cập bằng index dương `0` và index âm `-1`.

**Thuật toán:**
1. Tạo tuple `so`.
2. In `so[0]`.
3. In `so[-1]`.

**Code:**

```python
# Tuple chứa 3 số nguyên
so = (10, 20, 30)
# Phần tử đầu tiên
print(so[0])
# Phần tử cuối cùng — dùng index âm
print(so[-1])
```

**Giải thích code:**
* `(10, 20, 30)` — tuple có index 0, 1, 2.
* `so[0]` → 10, `so[-1]` → 30.
* Index âm tiện vì không cần biết độ dài tuple.

**Độ phức tạp:** O(1).

---

### Bài 2: In toàn bộ tuple

**Phân tích:** Duyệt toàn bộ tuple và in từng phần tử.

**Ý tưởng:** Vòng lặp `for` duyệt tuple y hệt list — vì cả hai đều là dãy (sequence).

**Thuật toán:**
1. Tạo tuple `mon`.
2. Lặp qua từng môn và in.

**Code:**

```python
# Tuple các môn học
mon = ("Toan", "Van", "Anh")
# Duyệt từng phần tử và in ra
for m in mon:
    print(m)
```

**Giải thích code:**
* `for m in mon:` — lần lượt gán `m = "Toan"`, `"Van"`, `"Anh"`.
* `print(m)` — in từng môn lên một dòng riêng.

**Độ phức tạp:** O(n).

---

### Bài 3: Tuple một phần tử

**Phân tích:** Cần tạo tuple đúng 1 phần tử — dễ nhầm thành số thường.

**Ý tưởng:** Thêm **dấu phẩy đuôi** sau giá trị: `(7,)`.

**Thuật toán:**
1. Tạo `tp = (7,)`.
2. In `type(tp)` để kiểm chứng.

**Code:**

```python
# Dấu phẩy đuôi là yếu tố quyết định để tạo tuple 1 phần tử
tp = (7,)
# type() in ra loại dữ liệu của biến
print(type(tp))
```

**Giải thích code:**
* `(7)` — ngoặc tròn chỉ nhóm biểu thức → kết quả là **số 7**.
* `(7,)` — có dấu phẩy → Python hiểu đây là **tuple 1 phần tử**.
* `type(tp)` → `<class 'tuple'>`.

**Độ phức tạp:** O(1).

---

### Bài 4: Đếm và tìm vị trí

**Phân tích:** Đếm số lần xuất hiện và vị trí đầu tiên của giá trị trong tuple.

**Ý tưởng:** `count()` đếm; `index()` trả vị trí đầu tiên.

**Thuật toán:**
1. Tạo tuple `diem`.
2. In `diem.count(9)`.
3. In `diem.index(8)`.

**Code:**

```python
# Điểm thi — giá trị 9 xuất hiện nhiều lần
diem = (9, 7, 9, 8, 9)
# Đếm số lần xuất hiện của 9
print(diem.count(9))
# Vị trí đầu tiên của 8
print(diem.index(8))
```

**Giải thích code:**
* `diem.count(9)` → 3 (ba lần xuất hiện).
* `diem.index(8)` → 3 (index bắt đầu từ 0: 9→0, 7→1, 9→2, 8→3).
* Lưu ý: `index` báo `ValueError` nếu giá trị không tồn tại.

**Độ phức tạp:** O(n).

---

### Bài 5: Kiểm tra phần tử

**Phân tích:** Kiểm tra sự tồn tại của hai giá trị trong tuple.

**Ý tưởng:** Toán tử `in` trả về `True`/`False`.

**Thuật toán:**
1. Tạo tuple `trai_cay`.
2. In `"tao" in trai_cay`.
3. In `"xoai" in trai_cay`.

**Code:**

```python
# Tuple các loại trái cây
trai_cay = ("tao", "chuoi", "cam")
# "tao" có tồn tại không?
print("tao" in trai_cay)
# "xoai" có tồn tại không?
print("xoai" in trai_cay)
```

**Giải thích code:**
* `"tao" in trai_cay` → `True`.
* `"xoai" in trai_cay` → `False`.
* `in` dùng được cho cả list, tuple, set, dict (bài 16, 17 sẽ gặp lại).

**Độ phức tạp:** O(n) — duyệt qua tuple.

---

### Bài 6: Độ dài và tổng

**Phân tích:** Lấy số phần tử và tổng giá trị của tuple số.

**Ý tưởng:** `len()` và `sum()` hoạt động với tuple như list.

**Thuật toán:**
1. Tạo tuple `so`.
2. In `len(so)`.
3. In `sum(so)`.

**Code:**

```python
# Tuple 6 số
so = (4, 8, 15, 16, 23, 42)
# Số lượng phần tử
print(len(so))
# Tổng các giá trị
print(sum(so))
```

**Giải thích code:**
* `len(so)` → 6.
* `sum(so)` → 4 + 8 + 15 + 16 + 23 + 42 = 108.
* `sum` yêu cầu tuple toàn số.

**Độ phức tạp:** O(1) cho `len`, O(n) cho `sum`.

---

### Bài 7: Truy cập ngược từ cuối

**Phân tích:** Lấy phần tử bằng index âm.

**Ý tưởng:** Index âm đếm từ cuối: `-1` là cuối, `-2` là kế cuối.

**Thuật toán:**
1. Tạo tuple `ngay`.
2. In `ngay[-2]`.
3. In `ngay[-1]`.

**Code:**

```python
# Các ngày trong tuần làm việc
ngay = ("T2", "T3", "T4", "T5", "T6")
# Kế cuối — index âm -2
print(ngay[-2])
# Cuối cùng — index âm -1
print(ngay[-1])
```

**Giải thích code:**
* `ngay[-1]` → `"T6"` (phần tử cuối).
* `ngay[-2]` → `"T5"`.
* Index âm giúp lấy phần tử cuối mà không cần biết độ dài.

**Độ phức tạp:** O(1).

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Hoán đổi hai biến

**Phân tích:** Hoán đổi giá trị 2 biến không cần biến trung gian.

**Ý tưởng:** Vế phải `b, a` tạo **tuple tạm** rồi được giải nén ngược vào `a`, `b`.

**Thuật toán:**
1. Gán `a = 5`, `b = 10`.
2. `a, b = b, a`.
3. In kết quả.

**Code:**

```python
# Hai biến ban đầu
a = 5
b = 10
# Hoán đổi bằng unpacking tuple — không cần biến trung gian
a, b = b, a
# In kết quả
print(f"a = {a}, b = {b}")
```

**Giải thích code:**
* `b, a` ở vế phải tạo tuple tạm `(10, 5)`.
* Unpacking gán `a = 10`, `b = 5`.
* Cách truyền thống cần biến `temp` — Python làm gọn hơn hẳn.

**Độ phức tạp:** O(1).

---

### Bài 9: Giải nén tọa độ

**Phân tích:** Tuple 2 phần tử được gán vào 2 biến riêng biệt.

**Ý tưởng:** Unpacking: `vi_do, kinh_do = toa_do`.

**Thuật toán:**
1. Tạo tuple `toa_do`.
2. Giải nén vào 2 biến.
3. In từng biến.

**Code:**

```python
# Tọa độ một điểm: (vĩ độ, kinh độ)
toa_do = (21.03, 105.85)
# Giải nén tuple vào hai biến — số biến phải khớp số phần tử
vi_do, kinh_do = toa_do
# In kết quả
print("Vi do:", vi_do)
print("Kinh do:", kinh_do)
```

**Giải thích code:**
* `vi_do, kinh_do = toa_do` — một dòng gán cả hai giá trị.
* Nếu số biến không khớp → `ValueError: too many values to unpack`.
* Unpacking là kỹ thuật nền cho nhiều mẫu code sau này.

**Độ phức tạp:** O(1).

---

### Bài 10: Unpacking trong vòng lặp

**Phân tích:** List chứa các tuple 2 phần tử; cần in từng cặp.

**Ý tưởng:** `for ten, diem in ds:` — mỗi vòng lặp tự động giải nén tuple.

**Thuật toán:**
1. Tạo list `ds` chứa các tuple.
2. Duyệt với `for ten, diem in ds`.
3. In chuỗi.

**Code:**

```python
# Danh sách học sinh: (tên, điểm)
ds = [("An", 8), ("Binh", 9)]
# Mỗi vòng lặp, tuple được giải nén vào ten và diem
for ten, diem in ds:
    print(f"{ten}: {diem} diem")
```

**Giải thích code:**
* Phần tử đầu tiên `("An", 8)` được gán `ten = "An"`, `diem = 8`.
* `f"{ten}: {diem} diem"` — f-string chèn biến vào chuỗi.
* Mẫu này gặp rất nhiều khi làm việc với danh sách dữ liệu.

**Độ phức tạp:** O(n).

---

### Bài 11: Cắt slice tuple

**Phân tích:** Lấy đoạn đầu và đảo ngược tuple bằng slice.

**Ý tưởng:** `[:3]` lấy 3 phần tử đầu; `[::-1]` đảo ngược — cả hai trả **tuple mới**.

**Thuật toán:**
1. Tạo tuple `so`.
2. In `so[:3]`.
3. In `so[::-1]`.

**Code:**

```python
# Tuple 6 số
so = (10, 20, 30, 40, 50, 60)
# Ba phần tử đầu — từ đầu tới trước index 3
print(so[:3])
# Đảo ngược toàn bộ — bước nhảy -1
print(so[::-1])
```

**Giải thích code:**
* `so[:3]` → `(10, 20, 30)`.
* `so[::-1]` → `(60, 50, 40, 30, 20, 10)`.
* Slice trả **tuple mới**, tuple gốc không đổi — phù hợp tính bất biến.

**Độ phức tạp:** O(k) với k là độ dài đoạn cắt.

---

### Bài 12: Chuyển đổi list ↔ tuple

**Phân tích:** Cần thêm phần tử vào tuple — bất biến nên phải "vòng qua" list.

**Ý tưởng:** `list(tu)` chuyển sang list → `append` → `tuple(...)` chuyển về.

**Thuật toán:**
1. Tạo tuple `tu`.
2. Chuyển sang list.
3. Thêm `"pho mai"`.
4. Chuyển ngược lại tuple và in.

**Code:**

```python
# Tuple ban đầu
tu = ("trung", "sua", "banh")
# Chuyển tuple sang list để có thể thêm phần tử
tam = list(tu)
# Thêm món mới vào list
tam.append("pho mai")
# Chuyển ngược lại tuple — bất biến nhưng có thể tạo tuple mới
tu_moi = tuple(tam)
# In kết quả
print(tu_moi)
```

**Giải thích code:**
* Tuple không có `append` — phải đi qua list tạm.
* `tuple(tam)` tạo **tuple mới** từ list đã cập nhật.
* Đây là cách "thêm phần tử" vào tuple một cách an toàn.

**Độ phức tạp:** O(n) — chuyển đổi duyệt toàn bộ.

---

### Bài 13: Trả về nhiều giá trị từ hàm

**Phân tích:** Hàm chỉ trả về "một giá trị" — nhưng giá trị đó có thể là tuple chứa nhiều kết quả.

**Ý tưởng:** `return (dien_tich, chu_vi)`; bên ngoài dùng unpacking nhận cả hai.

**Thuật toán:**
1. Định nghĩa hàm trả về tuple.
2. Gọi hàm với `dai = 5, rong = 3`.
3. Unpacking và in.

**Code:**

```python
# Hàm trả về tuple chứa diện tích và chu vi
def tinh_hcn(dai, rong):
    # Tính diện tích
    dien_tich = dai * rong
    # Tính chu vi
    chu_vi = (dai + rong) * 2
    # Trả về tuple 2 phần tử
    return (dien_tich, chu_vi)

# Nhận cả hai giá trị từ hàm bằng unpacking
dien_tich, chu_vi = tinh_hcn(5, 3)
# In kết quả
print("Dien tich:", dien_tich)
print("Chu vi:", chu_vi)
```

**Giải thích code:**
* `return (dien_tich, chu_vi)` — gói kết quả vào tuple.
* `dien_tich, chu_vi = tinh_hcn(5, 3)` — nhận trực tiếp từng giá trị.
* Dien tích = 15, chu vi = (5+3)*2 = 16.

**Độ phức tạp:** O(1).

---

### Bài 14: Điểm trung bình của tuple

**Phân tích:** Tính trung bình, max, min của tuple số.

**Ý tưởng:** `sum`/`len` cho trung bình; `max`/`min` cho cực trị — tất cả dùng được với tuple.

**Thuật toán:**
1. Tạo tuple `diem`.
2. Tính trung bình, làm tròn.
3. In trung bình, max, min.

**Code:**

```python
# Điểm 4 môn
diem = (8, 9, 7, 6)
# Trung bình cộng, làm tròn 2 chữ số
trung_binh = round(sum(diem) / len(diem), 2)
# In kết quả
print("Trung binh:", trung_binh)
print("Cao nhat:", max(diem))
print("Thap nhat:", min(diem))
```

**Giải thích code:**
* `sum(diem)` = 30, `len(diem)` = 4 → 7.5.
* `max(diem)` → 9, `min(diem)` → 6.
* Nhận xét: mọi hàm tính toán của list đều tương thích với tuple.

**Độ phức tạp:** O(n).

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Bảo vệ dữ liệu khỏi sửa đổi

**Phân tích:** Tuple bất biến nên việc gán `cau_hinh[0] = "user"` sẽ báo `TypeError`; cần bắt lỗi để chương trình không dừng.

**Ý tưởng:** Đặt lệnh gán sai trong `try`, bắt `TypeError` trong `except`.

**Thuật toán:**
1. Tạo tuple `cau_hinh`.
2. `try`: gán `cau_hinh[0] = "user"`.
3. `except TypeError`: in thông báo.

**Code:**

```python
# Cấu hình cố định — không được sửa đổi
cau_hinh = ("admin", 8080, "localhost")
# Thử sửa tuple — sẽ báo TypeError
try:
    cau_hinh[0] = "user"
except TypeError:
    # Bắt lỗi để chương trình vẫn chạy tiếp
    print("Loi: khong the sua doi tuple")
```

**Giải thích code:**
* `cau_hinh[0] = "user"` — gán vào tuple → Python ném `TypeError`.
* `try...except TypeError` — bắt đúng loại lỗi, in thông báo thay vì dừng chương trình.
* Đây chính là "tấm khiên" mà tính bất biến mang lại.

**Độ phức tạp:** O(1).

---

### Bài 16: Tìm phần tử lớn nhất (không dùng max)

**Phân tích:** Cần tìm max và vị trí của nó bằng vòng lặp thủ công.

**Ý tưởng:** Duyệt `enumerate`; mỗi khi gặp giá trị lớn hơn, cập nhật cả giá trị lẫn vị trí.

**Thuật toán:**
1. Khởi tạo `gia_tri_max` bằng phần tử đầu tiên, `vi_tri = 0`.
2. Duyệt từng (index, giá trị).
3. Nếu giá trị lớn hơn max → cập nhật.
4. In kết quả.

**Code:**

```python
# Tuple số cần tìm
so = (12, 5, 27, 8, 19)
# Khởi tạo với phần tử đầu tiên
gia_tri_max = so[0]
vi_tri = 0
# Duyệt toàn bộ kèm vị trí
for i, gia_tri in enumerate(so):
    # Tìm thấy giá trị lớn hơn → cập nhật
    if gia_tri > gia_tri_max:
        gia_tri_max = gia_tri
        vi_tri = i
# In kết quả
print("Lon nhat:", gia_tri_max)
print("Vi tri:", vi_tri)
```

**Giải thích code:**
* `enumerate(so)` trả về cặp (index, giá trị).
* Khởi tạo bằng phần tử đầu đảm bảo luôn có giá trị so sánh.
* Kết quả: max = 27 tại vị trí 2.

**Độ phức tạp:** O(n).

---

### Bài 17: Đếm số ngày trong các tháng

**Phân tích:** Số ngày mỗi tháng là dữ liệu **cố định** — dùng tuple để bảo vệ khỏi sửa đổi.

**Ý tưởng:** Số ngày tháng `m` nằm ở `so_ngay[m - 1]` vì index bắt đầu từ 0.

**Thuật toán:**
1. Tạo tuple `so_ngay`.
2. Với mỗi tháng trong `[2, 4, 6]`: lấy số ngày theo index.
3. In tên tháng và số ngày.

**Code:**

```python
# Số ngày của 12 tháng — dữ liệu cố định dùng tuple
so_ngay = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# Các tháng cần kiểm tra
cac_thang = [2, 4, 6]
# Duyệt từng tháng
for thang in cac_thang:
    # Index của tháng = thang - 1 (vì index bắt đầu từ 0)
    ngay = so_ngay[thang - 1]
    print(f"Thang {thang}: {ngay} ngay")
```

**Giải thích code:**
* `so_ngay[2 - 1]` = `so_ngay[1]` = 28 (tháng 2).
* `so_ngay[4 - 1]` = 30, `so_ngay[6 - 1]` = 30.
* Tuple phù hợp vì số ngày các tháng không thay đổi (trừ năm nhuận — xử lý thêm bằng điều kiện).

**Độ phức tạp:** O(n) với n là số tháng cần kiểm tra.

---

### Bài 18: Điểm của 3 giám khảo — bỏ điểm cao, thấp nhất

**Phân tích:** Quy tắc chấm nghệ thuật: loại 1 điểm cao nhất và 1 thấp nhất rồi trung bình số còn lại.

**Ý tưởng:** Tuple không `sort` được → chuyển sang list, sắp xếp, bỏ đầu – cuối, tính trung bình.

**Thuật toán:**
1. Tạo tuple điểm.
2. `list(diem)` → `sort()`.
3. Cắt bỏ phần tử đầu và cuối: `diem_sau_khi_loai = tam[1:-1]`.
4. Trung bình phần còn lại, làm tròn 2 chữ số.

**Code:**

```python
# Điểm 5 giám khảo
diem = (8.0, 9.5, 7.0, 9.5, 8.5)
# Chuyển sang list để sắp xếp được
tam = list(diem)
# Sắp xếp tăng dần
tam.sort()
# Bỏ điểm thấp nhất (đầu) và cao nhất (cuối)
tam = tam[1:-1]
# Trung bình 3 điểm còn lại
diem_chung = round(sum(tam) / len(tam), 2)
# In kết quả
print("Diem chung:", diem_chung)
```

**Giải thích code:**
* Sau `sort()`: `[7.0, 8.0, 8.5, 9.5, 9.5]`.
* `tam[1:-1]` → `[8.0, 8.5, 9.5]`.
* Trung bình: 26.0 / 3 ≈ 8.67.
* Chỉ có 5 giám khảo trở lên quy tắc này mới có ý nghĩa — với 3 giám khảo sẽ chỉ còn 1 điểm.

**Độ phức tạp:** O(n log n) — chi phí của `sort`.

---

### Bài 19: Sắp xếp tuple bằng vòng lặp (bubble sort)

**Phân tích:** Bài toán yêu cầu hiểu bản chất sắp xếp, không dùng `sorted`.

**Ý tưởng:** **Bubble sort**: lặp nhiều lượt, mỗi lượt "nổi" phần tử lớn nhất về cuối bằng cách hoán đổi các cặp liền kề sai thứ tự.

**Thuật toán:**
1. Chuyển tuple sang list `ds`.
2. Vòng ngoài: `n - 1` lượt.
3. Vòng trong: so sánh `ds[j]` và `ds[j+1]`, hoán đổi nếu sai thứ tự (dùng tuple hoán đổi).
4. In kết quả.

**Code:**

```python
# Tuple chưa sắp xếp
so = (5, 2, 9, 1, 7)
# Chuyển sang list để sửa được
ds = list(so)
# Số phần tử
n = len(ds)
# Bubble sort: n-1 lượt
for i in range(n - 1):
    # Mỗi lượt đẩy phần tử lớn nhất về cuối
    for j in range(n - 1 - i):
        # Hai phần tử liền kề sai thứ tự → hoán đổi bằng tuple
        if ds[j] > ds[j + 1]:
            ds[j], ds[j + 1] = ds[j + 1], ds[j]
# In list đã sắp xếp
print(ds)
```

**Giải thích code:**
* Vòng ngoài chạy `n - 1` lượt; sau lượt `i`, `i + 1` phần tử cuối đã đúng chỗ.
* Vòng trong chỉ cần xét tới `n - 1 - i` — phần đuôi đã sắp xong.
* `ds[j], ds[j+1] = ds[j+1], ds[j]` — hoán đổi bằng unpacking tuple (kiến thức chính bài này).
* Kết quả: `[1, 2, 5, 7, 9]`.

**Độ phức tạp:** O(n²) trong trường hợp xấu — thuật toán đơn giản nhưng chậm với list lớn.

---

### Bài 20: Quản lý kho cố định

**Phân tích:** Tuple lồng nhau: mỗi phần tử là tuple `(tên, số lượng)`; cần tổng mặt hàng, tổng hàng và phát hiện mặt hàng sắp hết.

**Ý tưởng:** Duyệt `for ten, sl in kho:` (unpacking cặp), cộng dồn `sl`, kiểm tra ngưỡng `< 40`.

**Thuật toán:**
1. Tạo tuple `kho` lồng nhau.
2. Đếm `len(kho)` → số mặt hàng.
3. Vòng lặp: cộng dồn tổng, kiểm tra sắp hết.
4. In kết quả.

**Code:**

```python
# Kho hàng: mỗi phần tử là tuple (tên, số lượng)
kho = (("gao", 100), ("trung", 50), ("sua", 30))
# Số mặt hàng
print("So mat hang:", len(kho))
# Tổng số lượng hàng
tong = 0
# Duyệt và giải nén từng cặp (ten, so_luong)
for ten, so_luong in kho:
    tong += so_luong
print("Tong so luong:", tong)
# Kiểm tra mặt hàng sắp hết (dưới 40)
sap_het = ""
for ten, so_luong in kho:
    if so_luong < 40:
        sap_het = ten
# In trạng thái kho
if sap_het:
    print("SAP HET", f"({sap_het})")
else:
    print("DU HANG")
```

**Giải thích code:**
* `len(kho)` → 3 (số cặp = số mặt hàng).
* `for ten, so_luong in kho:` — tuple lồng được giải nén tự động.
* `sap_het` lưu tên mặt hàng đầu tiên dưới ngưỡng — ở đây `"sua"` (30 < 40).
* Nếu không có mặt hàng nào dưới ngưỡng, in `DU HANG`.

**Độ phức tạp:** O(n) với n là số mặt hàng.

---

## 📌 Lời khuyên cuối

* 🔗 Nhớ: tuple **bất biến** — đừng cố `append`/`sort`/gán phần tử, sẽ gặp `TypeError`/`AttributeError`.
* 🔄 **Unpacking** (`a, b = b, a`) là kỹ năng sống — dùng khắp nơi trong các bài sau.
* 📦 Muốn "thêm" vào tuple: đi qua list hoặc tạo tuple mới.
* 🧮 Trung bình cộng, max, min, sum đều dùng được cho tuple như list.

👉 Tiếp theo: **[Bài 16: Set (Tập hợp)](../16_Set/bai_giang.md)**
