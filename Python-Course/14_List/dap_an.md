# ✅ Bài 14: Đáp Án – Danh Sách (List)

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án để việc học hiệu quả nhất.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Tạo danh sách trái cây

**Phân tích:** Cần tạo list 4 phần tử, in phần tử đầu (index 0) và cuối (index -1).

**Ý tưởng:** Truy cập trực tiếp bằng chỉ số dương `0` và chỉ số âm `-1`.

**Thuật toán:**
1. Tạo list `trai_cay`.
2. In `trai_cay[0]`.
3. In `trai_cay[-1]`.

**Code:**

```python
# Tạo list 4 loại trái cây
trai_cay = ["tao", "chuoi", "cam", "xoai"]
# Phần tử đầu tiên — index dương 0
print(trai_cay[0])
# Phần tử cuối cùng — index âm -1
print(trai_cay[-1])
```

**Giải thích code:**
* `["tao", "chuoi", "cam", "xoai"]` — list có index 0, 1, 2, 3.
* `trai_cay[0]` → `"tao"` (đầu tiên).
* `trai_cay[-1]` → `"xoai"` (đếm ngược từ cuối, nhanh hơn nhớ độ dài).

**Độ phức tạp:** O(1) — truy cập theo index luôn tức thời.

---

### Bài 2: In toàn bộ danh sách

**Phân tích:** In từng phần tử của list lên từng dòng.

**Ý tưởng:** Dùng vòng lặp `for` duyệt qua từng giá trị — Python tự gán biến `x` cho mỗi phần tử.

**Thuật toán:**
1. Khởi tạo list `so`.
2. Lặp qua từng phần tử và in ra.

**Code:**

```python
# Danh sách 5 số
so = [10, 20, 30, 40, 50]
# Duyệt từng phần tử và in ra màn hình
for x in so:
    print(x)
```

**Giải thích code:**
* `for x in so:` — lần lượt gán `x = 10`, `x = 20`, ..., `x = 50`.
* `print(x)` — in ra giá trị hiện tại, xuống dòng tự động.

**Độ phức tạp:** O(n) — duyệt n phần tử.

---

### Bài 3: Độ dài và tổng

**Phân tích:** Cần số lượng phần tử và tổng giá trị của list số.

**Ý tưởng:** `len(diem)` cho số phần tử; `sum(diem)` cho tổng.

**Thuật toán:**
1. Khởi tạo list `diem`.
2. In `len(diem)`.
3. In `sum(diem)`.

**Code:**

```python
# Điểm 4 môn học
diem = [8, 9, 10, 7]
# Số lượng phần tử
print("So phan tu:", len(diem))
# Tổng giá trị các phần tử
print("Tong diem:", sum(diem))
```

**Giải thích code:**
* `len(diem)` → 4 (đếm phần tử).
* `sum(diem)` → 8 + 9 + 10 + 7 = 34.
* Hai hàm này chỉ hoạt động đúng với list chứa toàn số (đối với `sum`).

**Độ phức tạp:** O(1) cho `len`, O(n) cho `sum`.

---

### Bài 4: Thêm phần tử vào cuối

**Phân tích:** Bắt đầu từ list rỗng rồi thêm dần 3 giá trị.

**Ý tưởng:** Dùng `append()` — mỗi lần thêm 1 phần tử vào cuối list.

**Thuật toán:**
1. Tạo list rỗng `gio_hang`.
2. Gọi `append` 3 lần với từng món.
3. In list.

**Code:**

```python
# Giỏ hàng ban đầu rỗng
gio_hang = []
# Lần lượt thêm từng món vào cuối giỏ
gio_hang.append("sua")
gio_hang.append("trung")
gio_hang.append("banh mi")
# In toàn bộ giỏ hàng
print(gio_hang)
```

**Giải thích code:**
* `[]` — list rỗng, chưa có ngăn nào.
* Mỗi `append` mở thêm một "ngăn" ở cuối và đặt giá trị vào.
* Kết quả in ra `['sua', 'trung', 'banh mi']` theo đúng thứ tự thêm.

**Độ phức tạp:** O(1) mỗi lần `append`.

---

### Bài 5: Tìm vị trí phần tử

**Phân tích:** Cần vị trí của `"com"` và kiểm tra sự tồn tại của `"banh"`.

**Ý tưởng:** `index()` trả vị trí đầu tiên; toán tử `in` trả `True`/`False`.

**Thuật toán:**
1. Khởi tạo list `mon`.
2. In `mon.index("com")`.
3. In `"banh" in mon`.

**Code:**

```python
# Danh sách món ăn
mon = ["pho", "bun", "com", "mi"]
# Vị trí đầu tiên của "com"
print(mon.index("com"))
# Kiểm tra "banh" có trong list không
print("banh" in mon)
```

**Giải thích code:**
* `mon.index("com")` → 2 (vị trí bắt đầu đếm từ 0).
* `"banh" in mon` → `False` vì list không chứa `"banh"`.
* Lưu ý: nếu dùng `index` với phần tử không tồn tại sẽ báo `ValueError`.

**Độ phức tạp:** O(n) — phải duyệt để tìm.

---

### Bài 6: Xóa phần tử

**Phân tích:** Xóa theo **giá trị** (số 5 đầu tiên) rồi xóa theo **vị trí** (phần tử cuối).

**Ý tưởng:** `remove(5)` tìm giá trị đầu tiên; `pop()` xóa phần tử cuối.

**Thuật toán:**
1. Khởi tạo `diem = [5, 8, 7, 5]`.
2. `diem.remove(5)` rồi in.
3. `diem.pop()` rồi in.

**Code:**

```python
# Danh sách điểm
diem = [5, 8, 7, 5]
# Xóa giá trị 5 ĐẦU TIÊN — list còn [8, 7, 5]
diem.remove(5)
print(diem)
# Xóa phần tử cuối (pop trả về giá trị bị xóa nhưng ta không cần dùng)
diem.pop()
print(diem)
```

**Giải thích code:**
* `remove(5)` — xóa đúng **một** phần tử đầu tiên có giá trị 5.
* `pop()` — xóa phần tử cuối (giá trị 5 còn lại) và trả về nó.
* Kết quả: `[8, 7, 5]` rồi `[8, 7]`.

**Độ phức tạp:** O(n) cho `remove` (phải dò), O(1) cho `pop` cuối.

---

### Bài 7: Sắp xếp tăng dần

**Phân tích:** Cần sắp xếp list số theo thứ tự tăng dần.

**Ý tưởng:** `sort()` sắp xếp **ngay trên list gốc**.

**Thuật toán:**
1. Khởi tạo list `so`.
2. Gọi `so.sort()`.
3. In list.

**Code:**

```python
# Danh sách chưa sắp xếp
so = [9, 1, 7, 3]
# Sắp xếp tăng dần — sửa ngay list gốc
so.sort()
# In kết quả
print(so)
```

**Giải thích code:**
* `so.sort()` — sắp xếp và **thay đổi list gốc**, trả về `None`.
* Kết quả: `[1, 3, 7, 9]`.
* Nếu muốn giữ list gốc, phải dùng `sorted(so)`.

**Độ phức tạp:** O(n log n).

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Điểm trung bình của lớp

**Phân tích:** Với list số, trung bình = `sum / len`; cần thêm `max` và `min`.

**Ý tưởng:** Tính từng giá trị rồi làm tròn 2 chữ số với `round`.

**Thuật toán:**
1. Khởi tạo list điểm.
2. Tính `tong = sum(diem)`, `so_mon = len(diem)`.
3. Tính trung bình và làm tròn.
4. In trung bình, cao nhất, thấp nhất.

**Code:**

```python
# Danh sách điểm của 5 học sinh
diem = [6.5, 8.0, 9.5, 5.0, 7.5]
# Tổng điểm
tong = sum(diem)
# Số môn
so_mon = len(diem)
# Trung bình, làm tròn 2 chữ số
trung_binh = round(tong / so_mon, 2)
# In kết quả
print("Trung binh:", trung_binh)
print("Cao nhat:", max(diem))
print("Thap nhat:", min(diem))
```

**Giải thích code:**
* `tong / so_mon` → 36.5 / 5 = 7.3.
* `round(7.3, 2)` → 7.3 (giữ 2 chữ số thập phân).
* `max`/`min` duyệt toàn list để tìm giá trị lớn/nhỏ nhất.

**Độ phức tạp:** O(n) — 3 lần duyệt qua list.

---

### Bài 9: Lọc số chẵn

**Phân tích:** Thu thập các số chia hết cho 2 vào list riêng.

**Ý tưởng:** Mẫu hình "collect": duyệt → kiểm tra điều kiện → `append` vào list kết quả.

**Thuật toán:**
1. Khởi tạo list rỗng `so_chan`.
2. Với mỗi `x` trong `so`: nếu `x % 2 == 0` thì `append`.
3. In `so_chan`.

**Code:**

```python
# Danh sách gốc
so = [1, 4, 7, 8, 10, 13]
# List kết quả — thu thập số chẵn
so_chan = []
# Duyệt từng phần tử
for x in so:
    # Kiểm tra số chẵn: chia hết cho 2
    if x % 2 == 0:
        so_chan.append(x)
# In kết quả
print(so_chan)
```

**Giải thích code:**
* `x % 2 == 0` — phép chia lấy dư: chẵn khi dư 0.
* `append` chỉ được gọi khi điều kiện đúng → list chỉ chứa số chẵn.
* Kết quả: `[4, 8, 10]`.

**Độ phức tạp:** O(n).

---

### Bài 10: Chia danh sách thành 3 phần

**Phân tích:** List 9 phần tử cần chia thành 3 đoạn bằng nhau.

**Ý tưởng:** Dùng slice với `stop` tương ứng: 3, 6, hết.

**Thuật toán:**
1. Khởi tạo list.
2. In `so[:3]`, `so[3:6]`, `so[6:]`.

**Code:**

```python
# Danh sách 9 số
so = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Ba số đầu — từ đầu tới trước index 3
print(so[:3])
# Ba số giữa — từ index 3 tới trước index 6
print(so[3:6])
# Ba số cuối — từ index 6 tới hết
print(so[6:])
```

**Giải thích code:**
* Slice `[start:stop]` lấy từ `start` tới **trước** `stop`.
* `so[:3]` → `[1, 2, 3]`; `so[3:6]` → `[4, 5, 6]`; `so[6:]` → `[7, 8, 9]`.
* Mỗi slice trả về **list mới**, list gốc không đổi.

**Độ phức tạp:** O(k) với k là độ dài đoạn cắt.

---

### Bài 11: Đếm số lần xuất hiện

**Phân tích:** Cần đếm từ `"python"` trong một câu; câu cần được tách thành list từ.

**Ý tưởng:** `str.split()` tách chuỗi theo khoảng trắng thành list; `list.count()` đếm số lần xuất hiện.

**Thuật toán:**
1. Tách câu bằng `cau.split()`.
2. In `tu.split().count("python")`.

**Code:**

```python
# Câu văn cần phân tích
cau = "toi thich hoc python vi python don gian"
# Tách thành list các từ (theo khoảng trắng)
tu = cau.split()
# Đếm số lần từ "python" xuất hiện
print(tu.count("python"))
```

**Giải thích code:**
* `cau.split()` → `["toi", "thich", "hoc", "python", "vi", "python", "don", "gian"]`.
* `tu.count("python")` → 2 (duyệt toàn list đếm các phần tử khớp).

**Độ phức tạp:** O(n).

---

### Bài 12: Hoán đổi vị trí

**Phân tích:** Đổi chỗ phần tử đầu và cuối.

**Ý tưởng:** Python cho phép gán nhiều giá trị cùng lúc — hoán đổi trong **một dòng**.

**Thuật toán:**
1. Khởi tạo list.
2. `ds[0], ds[-1] = ds[-1], ds[0]`.
3. In list.

**Code:**

```python
# Danh sách ban đầu
ds = [1, 2, 3, 4]
# Hoán đổi phần tử đầu và cuối trong một dòng
ds[0], ds[-1] = ds[-1], ds[0]
# In kết quả
print(ds)
```

**Giải thích code:**
* Vế phải `ds[-1], ds[0]` được **đọc trước** (= 4, 1).
* Sau đó mới gán lần lượt: `ds[0] = 4`, `ds[-1] = 1`.
* Kết quả: `[4, 2, 3, 1]`.

**Độ phức tạp:** O(1).

---

### Bài 13: Kiểm tra tăng dần

**Phân tích:** List "tăng dần" khi mọi phần tử đứng sau đều lớn hơn phần tử liền trước.

**Ý tưởng:** So sánh `ds` với phiên bản đã sắp xếp `sorted(ds)` — nếu bằng nhau thì đã tăng dần.

**Thuật toán:**
1. Khởi tạo list.
2. So sánh `ds == sorted(ds)`.
3. In kết quả.

**Code:**

```python
# Danh sách cần kiểm tra
ds = [1, 3, 5, 7]
# sorted(ds) tạo list đã sắp xếp; so sánh với list gốc
ket_qua = ds == sorted(ds)
# In ra True nếu đúng là tăng dần
print(ket_qua)
```

**Giải thích code:**
* `sorted(ds)` → `[1, 3, 5, 7]` — list mới, không sửa `ds`.
* So sánh `==` giữa hai list so từng phần tử từng vị trí.
* Vì giống hệt nhau → `True`.
* Nếu đổi `ds = [1, 3, 2]` thì `sorted` cho `[1, 2, 3]` → `False`.

**Độ phức tạp:** O(n log n) — chi phí của `sorted`.

---

### Bài 14: Sinh viên mới

**Phân tích:** Vừa chèn vào vị trí giữa, vừa xóa phần tử — thứ tự thao tác quyết định kết quả.

**Ý tưởng:** `insert(2, "Dung")` chèn sau "Binh" (index 1 → chèn tại 2); sau đó `remove("An")`.

**Thuật toán:**
1. Khởi tạo list ban đầu.
2. `insert(2, "Dung")` — chèn vào vị trí index 2.
3. `remove("An")` — xóa phần tử theo giá trị.
4. In list.

**Code:**

```python
# Danh sách lớp ban đầu
lop = ["An", "Binh", "Chi"]
# Chèn "Dung" vào vị trí index 2 — sau "Binh"
lop.insert(2, "Dung")
# "An" chuyển trường — xóa theo giá trị
lop.remove("An")
# In list cuối cùng
print(lop)
```

**Giải thích code:**
* Sau `insert(2, "Dung")`: `["An", "Binh", "Dung", "Chi"]`.
* Sau `remove("An")`: `["Binh", "Dung", "Chi"]`.
* Nếu làm ngược (xóa trước, chèn sau) vẫn ra kết quả đúng trong bài này, nhưng hãy tập suy nghĩ theo thứ tự dữ kiện thực tế.

**Độ phức tạp:** O(n) — insert/remove đều phải dịch chuyển phần tử.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Bảng điểm học sinh (list lồng nhau)

**Phân tích:** Mỗi hàng là `[tên, toán, văn]`; cần tổng điểm từng bạn và tìm bạn cao nhất.

**Ý tưởng:** Duyệt từng hàng, cộng điểm; dùng biến `diem_max` và `ten_max` cập nhật khi gặp tổng lớn hơn.

**Thuật toán:**
1. Khởi tạo `bang_diem`.
2. Với mỗi hàng: tính `tong = hang[1] + hang[2]`, in ra.
3. Nếu `tong > diem_max`: cập nhật `diem_max`, `ten_max`.
4. In tên cao nhất.

**Code:**

```python
# Bảng điểm: [tên, điểm Toán, điểm Văn]
bang_diem = [
    ["An", 8, 9],
    ["Binh", 7, 8],
    ["Chi", 9, 10],
]
# Biến theo dõi bạn có tổng cao nhất
diem_max = -1
ten_max = ""
# Duyệt từng hàng của bảng
for hang in bang_diem:
    # Tổng điểm Toán + Văn
    tong = hang[1] + hang[2]
    print(f"{hang[0]}: {tong}")
    # Cập nhật người dẫn đầu nếu tổng lớn hơn
    if tong > diem_max:
        diem_max = tong
        ten_max = hang[0]
# In người có tổng cao nhất
print("Cao nhat:", ten_max)
```

**Giải thích code:**
* `hang[0]` là tên, `hang[1]` và `hang[2]` là hai cột điểm.
* Khởi tạo `diem_max = -1` đảm bảo mọi tổng dương đều lớn hơn.
* Cuối vòng lặp, `ten_max` giữ tên bạn đứng đầu.

**Độ phức tạp:** O(n) với n là số hàng.

---

### Bài 16: Bảng cửu chương từ danh sách

**Phân tích:** Với mỗi giá trị `x`, cần in 3 phép tính `x * 1`, `x * 2`, `x * 3` trên cùng dòng.

**Ý tưởng:** Vòng lặp ngoài duyệt `nhan`; vòng trong xây chuỗi phép tính; dùng `", ".join(...)` nối chuỗi.

**Thuật toán:**
1. Khởi tạo list `nhan`.
2. Với mỗi `x`: tạo list các chuỗi `f"{x}x{i}={x*i}"` cho i từ 1 đến 3.
3. Nối bằng dấu `, ` và in.

**Code:**

```python
# Các số cần in bảng nhân
nhan = [2, 3, 4, 5]
# Duyệt từng giá trị
for x in nhan:
    # Tạo list các phép tính x*1, x*2, x*3 dưới dạng chuỗi
    cac_phep = [f"{x}x{i}={x * i}" for i in range(1, 4)]
    # Nối các chuỗi bằng dấu ", " và in
    print(", ".join(cac_phep))
```

**Giải thích code:**
* `range(1, 4)` sinh ra 1, 2, 3.
* List comprehension tạo chuỗi như `"2x1=2"`, `"2x2=4"`, `"2x3=6"`.
* `", ".join(...)` nối thành `2x1=2, 2x2=4, 2x3=6`.

**Độ phức tạp:** O(n × 3) = O(n).

---

### Bài 17: Xóa các phần tử trùng lặp liên tiếp

**Phân tích:** Chỉ giữ một bản cho nhóm phần tử giống nhau đứng liền nhau.

**Ý tưởng:** Xây list kết quả; thêm phần tử mới **chỉ khi khác phần tử cuối** của list kết quả.

**Thuật toán:**
1. Khởi tạo list rỗng `ket_qua`.
2. Với mỗi `x` trong `ds`: nếu `ket_qua` rỗng hoặc `ket_qua[-1] != x` thì `append`.
3. In `ket_qua`.

**Code:**

```python
# Danh sách có các cụm trùng liên tiếp
ds = [1, 1, 2, 2, 2, 3, 4, 4, 5]
# List kết quả sau khi nén các cụm trùng
ket_qua = []
# Duyệt từng phần tử
for x in ds:
    # Chỉ thêm khi khác phần tử đứng liền trước trong kết quả
    if not ket_qua or ket_qua[-1] != x:
        ket_qua.append(x)
# In kết quả
print(ket_qua)
```

**Giải thích code:**
* `ket_qua[-1]` — phần tử vừa thêm vào cuối list kết quả.
* `not ket_qua` — kiểm tra list rỗng để thêm phần tử đầu tiên.
* Các giá trị trùng liền kề bị "nuốt" vì bằng `ket_qua[-1]`.

**Độ phức tạp:** O(n).

---

### Bài 18: Ghép danh sách lệch thứ tự

**Phân tích:** Hai list đã tăng dần; cần trộn thành một list tăng dần mà **không** dùng `sorted(a + b)`.

**Ý tưởng:** Kỹ thuật **two-pointer**: hai biến `i`, `j` lần lượt trỏ vào hai list; so sánh, đưa phần tử nhỏ hơn vào kết quả, tăng con trỏ tương ứng.

**Thuật toán:**
1. Khởi tạo `i = 0`, `j = 0`, list rỗng `ket_qua`.
2. Trong khi cả hai con trỏ còn trong phạm vi: so sánh `a[i]` và `b[j]`, thêm giá trị nhỏ hơn.
3. Sao chép nốt phần dư của list còn lại.
4. In kết quả.

**Code:**

```python
# Hai list đã sắp xếp tăng dần
a = [1, 3, 5]
b = [2, 4, 6]
# Hai con trỏ chỉ số và list kết quả
i = 0
j = 0
ket_qua = []
# Trộn khi cả hai còn phần tử
while i < len(a) and j < len(b):
    # Lấy phần tử nhỏ hơn ở hai đầu
    if a[i] < b[j]:
        ket_qua.append(a[i])
        i += 1
    else:
        ket_qua.append(b[j])
        j += 1
# Dồn nốt phần còn lại của list a (nếu có)
while i < len(a):
    ket_qua.append(a[i])
    i += 1
# Dồn nốt phần còn lại của list b (nếu có)
while j < len(b):
    ket_qua.append(b[j])
    j += 1
# In kết quả
print(ket_qua)
```

**Giải thích code:**
* Vì hai list đều tăng dần, phần tử nhỏ nhất "còn lại" luôn nằm ở một trong hai đầu `a[i]` hoặc `b[j]`.
* Vòng `while` thứ hai/thứ ba chỉ chạy cho list còn dư sau khi list kia hết.
* Kết quả: `[1, 2, 3, 4, 5, 6]`.

**Độ phức tạp:** O(n + m) — mỗi phần tử được xử lý đúng một lần.

---

### Bài 19: Dịch chuyển vòng (rotate)

**Phân tích:** Dịch phải vòng tròn 2 lần: phần tử cuối chuyển lên đầu.

**Ý tưởng:** Mỗi lần: `ds.pop()` lấy phần tử cuối, `ds.insert(0, ...)` chèn lên đầu. Lặp đúng 2 lần.

**Thuật toán:**
1. Khởi tạo list.
2. Lặp 2 lần: `ds.insert(0, ds.pop())`.
3. In list.

**Code:**

```python
# Danh sách ban đầu
ds = [1, 2, 3, 4, 5]
# Số lần dịch phải
so_lan = 2
# Dịch phải vòng tròn so_lan lần
for _ in range(so_lan):
    # pop lấy phần tử cuối, insert đưa lên đầu
    ds.insert(0, ds.pop())
# In kết quả
print(ds)
```

**Giải thích code:**
* Lần 1: `pop()` trả 5, `insert(0, 5)` → `[5, 1, 2, 3, 4]`.
* Lần 2: `pop()` trả 4, `insert(0, 4)` → `[4, 5, 1, 2, 3]`.
* Biến `_` chỉ dùng để đếm lần lặp, không dùng giá trị.

**Độ phức tạp:** O(k × n) — mỗi `insert(0, ...)` phải dịch cả list; với list lớn nên dùng `deque` (đọc thêm ở phần mở rộng).

---

### Bài 20: Copy an toàn — ứng dụng chấm điểm

**Phân tích:** Phải tạo **bản sao thực sự** để thay đổi bản sao không ảnh hưởng bản gốc — đây là bẫy tham chiếu `=` cần tránh.

**Ý tưởng:** Dùng `list()` (hoặc `copy()`/`[:]`) để copy; sau đó duyệt theo index để cộng điểm cho bản sao.

**Thuật toán:**
1. Khởi tạo `goc`.
2. `sao = goc.copy()` — copy an toàn.
3. Với mỗi index: `sao[i] += 1`.
4. In cả hai list.

**Code:**

```python
# Danh sách điểm gốc
goc = [7, 9, 8, 6]
# COPY AN TOÀN — không được dùng dấu "="!
sao = goc.copy()
# Cộng 1 điểm cho từng phần tử của bản sao
for i in range(len(sao)):
    sao[i] += 1
# In cả hai để kiểm chứng
print("Sao (sau khi +1):", sao)
print("Goc (khong doi):", goc)
```

**Giải thích code:**
* `goc.copy()` tạo list **mới độc lập** — khác hẳn `sao = goc` (chỉ trỏ chung).
* `for i in range(len(sao))` duyệt theo index để **sửa giá trị** — duyệt theo giá trị không sửa được.
* `sao[i] += 1` — mỗi phần tử của bản sao tăng 1.
* Kiểm chứng: `goc` vẫn là `[7, 9, 8, 6]`.

**Độ phức tạp:** O(n).

---

## 📌 Lời khuyên cuối

* ⛔ Nhớ kỹ **bẫy tham chiếu**: muốn copy list luôn dùng `copy()`, `list()` hay `[:]`.
* 🔍 Kiểm tra `x in ds` trước khi `remove`/`index` để tránh `ValueError`.
* 📦 Phân biệt `sort()` (sửa list gốc) và `sorted()` (trả list mới).
* 🧪 Khi gặp `IndexError`, hãy in `len(ds)` ra xem list thực sự có bao nhiêu phần tử.

👉 Tiếp theo: **[Bài 15: Tuple (Bộ dữ liệu)](../15_Tuple/bai_giang.md)**
