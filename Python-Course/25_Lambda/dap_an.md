# ✅ Bài 25: Đáp Án – Lambda

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án để việc học hiệu quả nhất.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Lambda cộng hai số

**Phân tích:** Bài làm quen cú pháp `lambda thamso: bieuthuc`.

**Ý tưởng:** Gán lambda vào biến rồi gọi như hàm thường.

**Thuật toán:**
1. Tạo lambda nhận `a`, `b` trả `a + b`.
2. Gọi với `(3, 7)` và in.

**Code:**

```python
# Lambda nhận 2 tham số, trả về tổng
cong = lambda a, b: a + b
print(cong(3, 7))
```

**Giải thích code:**
* `lambda a, b: a + b` — hàm vô danh: 2 tham số, biểu thức `a + b` là kết quả.
* `cong(3, 7)` — gọi như hàm thường, trả `10`.

**Độ phức tạp:** O(1).

---

### Bài 2: Lambda bình phương

**Phân tích:** Lambda đơn tham số, một biểu thức số học.

**Ý tưởng:** `lambda x: x * x` gán cho biến `bp`.

**Thuật toán:**
1. Tạo lambda `bp`.
2. In `bp(6)`.

**Code:**

```python
bp = lambda x: x * x
print(bp(6))
```

**Giải thích code:** `x * x = 36`; không cần từ khóa `return` — biểu thức tự là kết quả.

**Độ phức tạp:** O(1).

---

### Bài 3: Lambda nhân đôi

**Phân tích:** Áp dụng lambda lên từng phần tử bằng `map`.

**Ý tưởng:** `map(lambda x: x * 2, danh_sach)` rồi bọc `list()`.

**Code:**

```python
so = [1, 2, 3, 4]
nhan_doi = list(map(lambda x: x * 2, so))
print(nhan_doi)
```

**Giải thích code:**
* `map` chạy lambda với từng giá trị: 1→2, 2→4, 3→6, 4→8.
* `list(...)` chuyển đối tượng map thành danh sách.

**Độ phức tạp:** O(n).

---

### Bài 4: Lambda trả về chuỗi dài nhất

**Phân tích:** `max` cần biết so sánh "dài nhất" theo tiêu chí gì → `key`.

**Ý tưởng:** `key=lambda s: len(s)` — so theo độ dài chuỗi.

**Code:**

```python
ten = ["an", "binh", "cuong"]
dai_nhat = max(ten, key=lambda s: len(s))
print(dai_nhat)
```

**Giải thích code:** `len("cuong") = 6` lớn nhất nên `max` trả về `"cuong"`.

**Độ phức tạp:** O(n).

---

### Bài 5: Sắp xếp số tăng dần

**Phân tích:** `sorted` với key trả về chính giá trị để so sánh.

**Ý tưởng:** `sorted(so, key=lambda x: x)` — sắp tăng dần.

**Code:**

```python
so = [5, 2, 8, 1, 9]
sx = sorted(so, key=lambda x: x)
print(sx)
```

**Giải thích code:** `key` trả về `x` → Python so sánh các giá trị gốc → `[1, 2, 5, 8, 9]`. `sorted` không sửa `so`.

**Độ phức tạp:** O(n log n).

---

### Bài 6: Sắp xếp theo độ dài

**Phân tích:** Sắp chuỗi theo số ký tự.

**Ý tưởng:** `key=lambda s: len(s)`.

**Code:**

```python
ten = ["An", "Binh", "Cuong", "D"]
sx = sorted(ten, key=lambda s: len(s))
print(sx)
```

**Giải thích code:** Độ dài: An=2, Binh=4, Cuong=5, D=1 → thứ tự `["D", "An", "Binh", "Cuong"]`.

**Độ phức tạp:** O(n log n).

---

### Bài 7: Lọc số chẵn bằng filter

**Phân tích:** Giữ các phần tử thỏa điều kiện `x % 2 == 0`.

**Ý tưởng:** `filter(lambda x: x % 2 == 0, so)` + `list()`.

**Code:**

```python
so = list(range(1, 11))
so_chan = list(filter(lambda x: x % 2 == 0, so))
print(so_chan)
```

**Giải thích code:**
* `range(1, 11)` tạo 1→10 (không gồm 11).
* `lambda` trả `True` cho số chẵn — `filter` giữ lại chúng.
* Kết quả `[2, 4, 6, 8, 10]`.

**Độ phức tạp:** O(n).

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Sắp xếp học sinh theo điểm (tuple)

**Phân tích:** Mỗi học sinh là tuple `(tên, điểm)` — cần sắp theo phần tử số 1.

**Ý tưởng:** `key=lambda hs: hs[1]`, giảm dần với `reverse=True`.

**Thuật toán:**
1. Tạo danh sách tuple.
2. Sắp theo điểm giảm dần.
3. In.

**Code:**

```python
hoc_sinh = [("An", 8.5), ("Binh", 5.0), ("Cuong", 9.5)]

sx = sorted(hoc_sinh, key=lambda hs: hs[1], reverse=True)
print(sx)
```

**Giải thích code:**
* `hs[1]` — vị trí 1 của tuple là điểm.
* `reverse=True` — từ cao xuống thấp.

**Độ phức tạp:** O(n log n).

---

### Bài 9: Lọc người trên 18 tuổi

**Phân tích:** Giữ những tuple có tuổi ≥ 18.

**Ý tưởng:** `filter(lambda ng: ng[1] >= 18, nguoi)`.

**Code:**

```python
nguoi = [("An", 17), ("Binh", 19), ("Cuong", 20), ("Dung", 15)]

du_tuoi = list(filter(lambda ng: ng[1] >= 18, nguoi))
print(du_tuoi)
```

**Giải thích code:** An (17) và Dung (15) bị loại; Binh, Cuong được giữ.

**Độ phức tạp:** O(n).

---

### Bài 10: Map đổi USD sang VND

**Phân tích:** Biến đổi từng giá trị theo tỉ giá.

**Ý tưởng:** Nhân mỗi giá trị với `25000` bằng lambda trong `map`.

**Code:**

```python
gia_usd = [10, 25, 50]
TY_GIA = 25000

gia_vnd = list(map(lambda usd: usd * TY_GIA, gia_usd))
print(gia_vnd)
```

**Giải thích code:** `10*25000=250000`, `25*25000=625000`, `50*25000=1250000`.

**Độ phức tạp:** O(n).

---

### Bài 11: Tên viết hoa toàn bộ

**Phân tích:** `upper()` viết hoa toàn chuỗi — dùng lambda để gọi lên từng phần tử.

**Ý tưởng:** `map(lambda s: s.upper(), ten)`.

**Code:**

```python
ten = ["an", "binh", "cuong"]
hoa = list(map(lambda s: s.upper(), ten))
print(hoa)
```

**Giải thích code:** `"an".upper()` → `"AN"`, tương tự cho các tên còn lại.

**Độ phức tạp:** O(n).

---

### Bài 12: Tìm sinh viên điểm cao nhất

**Phân tích:** Cần "sinh viên có điểm cao nhất" — dùng `max` với `key`.

**Ý tưởng:** `max(danh_sach, key=lambda sv: sv[1])`.

**Code:**

```python
danh_sach = [("An", 8.5), ("Binh", 5.0), ("Cuong", 9.5)]

sv_tot = max(danh_sach, key=lambda sv: sv[1])
print(sv_tot[0], sv_tot[1])
```

**Giải thích code:**
* `max(..., key=...)` trả về tuple có điểm lớn nhất `("Cuong", 9.5)`.
* `sv_tot[0]`, `sv_tot[1]` — lấy tên và điểm để in.

**Độ phức tạp:** O(n).

---

### Bài 13: Lọc số chia hết cho 3

**Phân tích:** Điều kiện `x % 3 == 0`.

**Ý tưởng:** `filter` với lambda kiểm tra phép chia dư.

**Code:**

```python
so = list(range(1, 21))
boi_3 = list(filter(lambda x: x % 3 == 0, so))
print(boi_3)
```

**Giải thích code:** range 1→20; số nào chia 3 dư 0 thì giữ lại.

**Độ phức tạp:** O(n).

---

### Bài 14: Sắp xếp tên theo ký tự cuối

**Độ phức tạp:** O(n log n).

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Lọc chẵn rồi bình phương

**Phân tích:** Hai bước: lọc → biến đổi; ghép `filter` trong `map`.

**Ý tưởng:** `map(lambda x: x*x, filter(lambda x: x%2==0, so))` — đọc từ trong ra.

**Thuật toán:**
1. Xây danh sách 1–10.
2. `filter` số chẵn.
3. `map` bình phương.
4. Bọc `list` và in.

**Code:**

```python
so = list(range(1, 11))

# filter lấy số chẵn, map bình phương → bọc list
ket_qua = list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, so)))
print(ket_qua)
```

**Giải thích code:**
* Trong: `filter(...)` → [2, 4, 6, 8, 10].
* Ngoài: `map(x*x)` → [4, 16, 36, 64, 100].

**Độ phức tạp:** O(n).

---

### Bài 16: Điểm chuẩn thí sinh

**Phân tích:** Lọc thí sinh điểm ≥ 6.0 rồi sắp giảm dần.

**Ý tưởng:** `filter` → `sorted` ngược.

**Thuật toán:**
1. Lọc giữ thí sinh có `ts[1] >= 6`.
2. Sắp giảm dần theo điểm.
3. In.

**Code:**

```python
thi = [("An", 9.0), ("Binh", 4.5), ("Cuong", 7.0), ("Dung", 6.0)]

# Lọc đậu rồi sắp giảm dần
dau = list(filter(lambda ts: ts[1] >= 6, thi))
ket_qua = sorted(dau, key=lambda ts: ts[1], reverse=True)
print(ket_qua)
```

**Giải thích code:** Binh (4.5) bị loại; còn lại sắp giảm: An 9.0, Cuong 7.0, Dung 6.0.

**Độ phức tạp:** O(n log n).

---

### Bài 17: Giá sau giảm giá

**Phân tích:** Giữ lại 80% giá → nhân `0.8`.

**Ý tưởng:** `map(lambda g: g * 0.8, danh_sach)`.

**Code:**

```python
gia = [100000, 200000, 500000]

sau_giam = list(map(lambda g: g * 0.8, gia))
print(sau_giam)
```

**Giải thích code:** `100000*0.8 = 80000.0`, `200000*0.8 = 160000.0`, `500000*0.8 = 400000.0`.

**Độ phức tạp:** O(n).

---

### Bài 18: Sắp xếp thời khóa biểu theo giờ

**Phân tích:** Phần tử vị trí 1 của tuple là giờ — sắp tăng dần theo đó.

**Ý tưởng:** `sorted(lich, key=lambda mon: mon[1])`.

**Code:**

```python
lich = [("Toan", 7), ("Van", 10), ("Ly", 8), ("Anh", 9)]

sx = sorted(lich, key=lambda mon: mon[1])
print(sx)
```

**Giải thích code:** Giờ tăng dần: 7 (Toan), 8 (Ly), 9 (Anh), 10 (Van).

**Độ phức tạp:** O(n log n).

---

### Bài 19: Lọc + tìm max chia hết cho 5

**Phân tích:** Kết hợp điều kiện (chia hết cho 5) và tìm cực trị.

**Ý tưởng:** `filter` lọc số thỏa `x % 5 == 0`, `max` chọn lớn nhất.

**Code:**

```python
so = [12, 7, 25, 33, 40, 15]

boi_5 = list(filter(lambda x: x % 5 == 0, so))
lon_nhat = max(boi_5, key=lambda x: x)
print(lon_nhat)
```

**Giải thích code:**
* `filter` → [25, 40, 15].
* `max` → 40 (dùng `key=lambda x: x` để minh họa — với số thì key không bắt buộc).

**Độ phức tạp:** O(n).

---

### Bài 20: Xếp hạng giảm dần + tổng lương

**Phân tích:** Tổng hợp: sắp xếp + đánh thứ hạng; tính tổng bằng lambda qua `map`/`sum`.

**Ý tưởng:** Phần 1 dùng `sorted(reverse=True)` + `enumerate`; phần 2 dùng `sum(map(lambda nv: nv[1], ...))`.

**Thuật toán:**
1. Sắp học giảm dần theo điểm.
2. In vòng lặp với thứ hạng.
3. Tính tổng lương bằng `sum(map(...))`.

**Code:**

```python
hoc_sinh = [("An", 8.5), ("Binh", 6.0), ("Cuong", 9.0)]
nhan_vien = [("Minh", 5000), ("Lan", 8000), ("Thai", 6000)]

# Phần 1: xếp hạng học sinh giảm dần theo điểm
bang = sorted(hoc_sinh, key=lambda hs: hs[1], reverse=True)
for thu_hang, hs in enumerate(bang, start=1):
    print(f"{thu_hang}. {hs[0]} - {hs[1]}")

# Phần 2: tổng lương công ty
tong_luong = sum(map(lambda nv: nv[1], nhan_vien))
print("Tong luong:", tong_luong)
```

**Giải thích code:**
* `enumerate(bang, start=1)` — cặp (thứ hạng, học sinh).
* `map(lambda nv: nv[1], ...)` — lấy lương từng nhân viên; `sum` gộp: 5000+8000+6000 = 19000.

**Độ phức tạp:** O(n log n).

---

## 📌 Lời khuyên cuối

* Luôn nhớ lambda chỉ có **một biểu thức** — phức tạp hãy dùng `def`.
* `filter` **giữ/lọc**, `map` **biến đổi** — đều trả iterable, đừng quên `list()`.
* `sorted(key=...)` sẽ xuất hiện ở nhiều bài sau (danh sách dataclass, JSON).
* Khi cùng một lambda dùng nhiều nơi, hãy đặt tên + `def` cho dễ bảo trì.

👉 Tiếp theo: **[Bài 26: List Comprehension](../26_List_Comprehension/bai_giang.md)**