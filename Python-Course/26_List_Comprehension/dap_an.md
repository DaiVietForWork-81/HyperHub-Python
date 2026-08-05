# ✅ Bài 26: Đáp Án – List Comprehension

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án để việc học hiệu quả nhất.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Bình phương các số 0–9

**Phân tích:** Tạo list mới bằng biểu thức đơn giản không cần append.

**Ý tưởng:** `[x * x for x in range(10)]` — biểu thức bên trái, vòng lặp bên phải.

**Thuật toán:**
1. Duyệt x từ 0 đến 9.
2. Tính x*x và nạp vào list.

**Code:**

```python
bp = [x * x for x in range(10)]
print(bp)
```

**Giải thích code:**
* `x * x` — thành phần giá trị.
* `for x in range(10)` — bộ duyệt.
* Kết quả: [0, 1, 4, 9, ... 81].

**Độ phức tạp:** O(n).

---

### Bài 2: Danh sách số chẵn 1–20

**Phân tích:** Duyệt + lọc điều kiện chẵn.

**Ý tưởng:** `[x for x in range(1, 21) if x % 2 == 0]`.

**Code:**

```python
so_chan = [x for x in range(1, 21) if x % 2 == 0]
print(so_chan)
```

**Giải thích code:**
* `if x % 2 == 0` — bộ lọc phía sau for: phần tử lẻ bị bỏ.
* `range(1, 21)` → 1..20.

**Độ phức tạp:** O(n).

---

### Bài 3: Viết hoa tên học sinh

**Phân tích:** Biến đổi từng chuỗi bằng `.upper()`.

**Ý tưởng:** `[t.upper() for t in ten]`.

**Code:**

```python
ten = ["an", "binh", "cuong"]
hoa = [t.upper() for t in ten]
print(hoa)
```

**Giải thích code:** mỗi `t` được gọi `.upper()` → `['AN', 'BINH', 'CUONG']`.

**Độ phức tạp:** O(n).

---

### Bài 4: Nhân đôi và cộng thêm 1

**Phân tích:** Biểu thức biến đổi phức hợp một bước.

**Ý tưởng:** `[x * 2 + 1 for x in so]`.

**Code:**

```python
so = [1, 2, 3, 4]
moi = [x * 2 + 1 for x in so]
print(moi)
```

**Giải thích code:** `1→3, 2→5, 3→7, 4→9`.

**Độ phức tạp:** O(n).

---

### Bài 5: Chữ cái của một chuỗi

**Phân tích:** Chuỗi là iterable nên duyệt trực tiếp từng ký tự.

**Ý tưởng:** `[c for c in "python"]`.

**Code:**

```python
ket = [c for c in "python"]
print(ket)
```

**Giải thích code:** `for c in "python"` — mỗi chữ cái thành một phần tử.

**Độ phức tạp:** O(n).

---

### Bài 6: Số lớn hơn 10

**Phân tích:** Lọc theo điều kiện > 10.

**Ý tưởng:** `[x for x in data if x > 10]`.

**Code:**

```python
data = [3, 12, 7, 20, 1, 15]
lon = [x for x in data if x > 10]
print(lon)
```

**Giải thích code:** 12, 20, 15 > 10 `d`ược giữ; 3, 7, 1 bị bỏ.

**Độ phức tạp:** O(n).

---

### Bài 7: Độ dài từng tên

**Phân tích:** Biến đổi tên → độ dài.

**Ý tưởng:** `[len(t) for t in ten]`.

**Code:**

```python
ten = ["An", "Binh", "Cuong"]
do_dai = [len(t) for t in ten]
print(do_dai)
```

**Giải thích code:** `len("An")=2`, `len("Binh")=4`, `len("Cuong")=5`.

**Độ phức tạp:** O(n).

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Lọc chẵn rồi bình phương

**Phân tích:** Hai công việc trong một dòng: lọc + biến đổi.

**Ý tưởng:** đưa `if` (lọc) vào trước biến đổi: `[x * x for x in so if x % 2 == 0]`.

**Code:**

```python
so = list(range(1, 11))
bp_chan = [x * x for x in so if x % 2 == 0]
print(bp_chan)
```

**Giải thích code:** số chẵn trong 1..10 là 2,4,6,8,10 → bình phương → [4, 16, 36, 64, 100].

**Độ phức tạp:** O(n).

---

### Bài 9: Nhãn chẵn/lẻ (if/else)

**Phân tích:** Mỗi phần tử vẫn giữ, chỉ đổi giá trị → dùng if/else **ở vị trí biểu thức**.

**Ý tưởng:** `["E" if x % 2 == 0 else "O" for x in so]`.

**Code:**

```python
so = [1, 2, 3, 4, 5]
nhan = ["E" if x % 2 == 0 else "O" for x in so]
print(nhan)
```

**Giải thích code:** lẻ→"O", chẵn→"E" → `['O', 'E', 'O', 'E', 'O']`.

**Độ phức tạp:** O(n).

---

### Bài 10: Set comprehension – bình phương tập số

**Phân tích:** Set tự loại trùng và không theo thứ tự.

**Ý tưởng:** `{x * x for x in so}`.

**Code:**

```python
so = [1, 2, 2, 3, 3, 4]
bp = {x * x for x in so}
print(bp)
```

**Giải thích code:** các giá trị bình phương {16, 1, 9, 4} — ngoặc `{}` tự loại phần tử trùng.

**Độ phức tạp:** O(n).

---

### Bài 11: Dict comprehension – khóa và bình phương

**Phân tích:** Chỉ cần cặp khóa: giá trị.

**Ý tưởng:** `{x: x * x for x in range(1, 6)}`.

**Code:**

```python
bp = {x: x * x for x in range(1, 6)}
print(bp)
```

**Giải thích code:** mỗi x → cặp `x: x*x` — đầu ra {1:1, 2:4, 3:9, 4:16, 5:25}.

**Độ phức tạp:** O(n).

---

### Bài 12: Bảng cửu chương nhân 5

**Phân tích:** Tạo chuỗi có định dạng, sau đó in từng dòng.

**Ý tưởng:** comprehension sinh chuỗi, vòng `for` in.

**Code:**

```python
bang = [f"5 x {k} = {5 * k}" for k in range(1, 11)]
for dong in bang:
    print(dong)
```

**Giải thích code:** `f"..."` chèn k và kết quả `5*k` vào chuỗi; vòng lặp in 10 dòng.

**Độ phức tạp:** O(n).

---

### Bài 13: Đếm số chẵn bằng comprehension

**Phân tích:** đếm lượng phần tử thỏa điều kiện.

**Ý tưởng:** comprehension tạo list chứa số chẵn rồi đo `len`.

**Code:**

```python
so = [3, 8, 12, 7, 20, 1, 24]
dem = len([x for x in so if x % 2 == 0])
print(dem)
```

**Giải thích code:** list lọc là [8, 12, 20, 24] → len = 4.

**Độ phức tạp:** O(n).

---

### Bài 14: Làm phẳng ma trận (nested)

**Phân tích:** Vòng ngoài duyệt từng hàng, vòng trong duyệt từng phần tử trong hàng.

**Ý tưởng:** `[x for hang in ma_tran for x in hang]`.

**Code:**

```python
ma_tran = [[1, 2], [3, 4], [5, 6]]
phang = [x for hang in ma_tran for x in hang]
print(phang)
```

**Giải thích code:** thứ tự vòng: hang -> x; kết quả [1, 2, 3, 4, 5, 6].

**Độ phức tạp:** O(tổng số phần tử).

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Điểm trung bình lớp bằng comprehension

**Phân tích:** Điểm trung bình = tổng / số lượng.

**Ý tưởng:** comprehension tạo list điểm, dùng `sum` + `len`, làm tròn 2 chữ số.

**Thuật toán:**
1. Tính tổng danh sách điểm bằng `sum`.
2. Chia cho số lượng `len`.
3. Làm tròn và in.

**Code:**

```python
diem = [8.5, 6.0, 9.0, 7.5]

tong = sum([d for d in diem])
trung_binh = round(tong / len(diem), 2)
print(trung_binh)
```

**Giải thích code:**
* `sum([d for d in diem])` — comprehension rõ ý: "d cho từng d trong diem".
* `31.0 / 4 = 7.75` → 2 chữ số thập phân.

**Độ phức tạp:** O(n).

---

### Bài 16: Đếm tần suất chữ cái

**Phân tích:** Dict comprehension đếm tần suất; `set` để có danh sách chữ cái duy nhất.

**Ý tưởng:** `{c: cau.count(c) for c in set(cau) if c != " "}`.

**Code:**

```python
cau = "hoc hoc nua hoc mai"

dem = {c: cau.count(c) for c in set(cau) if c != " "}
print(dem)
```

**Giải thích code:**
* `set(cau)` — các chữ cái duy nhất.
* `cau.count(c)` — số lần chữ cái xuất hiện.
* `if c != " "` — bỏ khoảng trắng.

**Độ phức tạp:** O(n²) khi dùng `count(c)` nhiều lần (n nhỏ thì chấp nhận).

---

### Bài 17: Số chính phương nhỏ hơn 50

**Phân tích:** Lọc những bình phương thỏa điều kiện.

**Ý tưởng:** duyệt x từ 0 đến 7, giữ khi `x*x < 50`.

**Code:**

```python
cp = [x * x for x in range(8) if x * x < 50]
print(cp)
```

**Giải thích code:** 0,1,…,7 bình phương: 0,1,4,9,16,25,36,49 đều <50.

**Độ phức tạp:** O(k).

---

### Bài 18: Phân loại điểm học sinh

**Phân tích:** Cần 3 nhãn → dùng if/else lồng trong biểu thức.

**Ý tưởng:** `"Gioi" if d >= 8 else ("Kha" if d >= 6.5 else "TB")`.

**Code:**

```python
diem = [9.0, 5.5, 7.0, 3.5, 8.0]

nhan = [
    "Gioi" if d >= 8 else ("Kha" if d >= 6.5 else "TB")
    for d in diem
]
print(nhan)
```

**Giải thích code:**
* if/else đầu — chọn giá trị mọi phần tử.
* lồng `Kha`/`TB` cho trường hợp 6.5 > d.

**Độ phức tạp:** O(n).

---

### Bài 19: Lọc sản phẩm theo giá + tổng

**Phân tích:** Lọc giá > 60000 rồi sum.

**Ý tưởng:** `sum([g for g in gia if g > 60000])`.

**Code:**

```python
gia = [50000, 120000, 30000, 250000, 80000]

tong = sum([g for g in gia if g > 60000])
print(tong)
```

**Giải thích code:** 120000 + 250000 + 80000 = 450000 (bỏ 50000, 30000).

**Độ phức tạp:** O(n).

---

### Bài 20: Bảng điểm chi tiết (tổng hợp)

**Phân tích:** Kết hợp comprehension (danh sách tên) và `max` với key lambda.

**Ý tưởng:** lọc đậu trước, rồi `max` theo điểm.

**Code:**

```python
lop = [("An", 8.5), ("Binh", 4.0), ("Cuong", 9.0), ("Dung", 6.5)]

dau = [hs[0] for hs in lop if hs[1] >= 5]
cao_nhat = max(lop, key=lambda hs: hs[1])[1]

print("Hoc sinh dau:", dau)
print("Diem cao nhat:", cao_nhat)
```

**Giải thích code:**
* `[hs[0] for hs in lop if hs[1] >= 5]` — tên những người điểm ≥ 5.
* `max(lop, key=lambda hs: hs[1])` — tuple có điểm lớn nhất `("Cuong",9.0)`, `[1]` lấy điểm.

**Độ phức tạp:** O(n log n).

---

## 📌 Lời khuyên cuối

* Luôn nhớ: **if cuối = lọc**, **if/else đầu = chọn giá trị**.
* Comprehension ngắn mới đẹp — phức tạp quá hãy tách vòng lặp `for`.
* Kết hợp comprehension với `sum`, `len`, `max`, `min` xử lý thống kê rất nhanh gọn.
* Bài tiếp theo dùng **trình tự nạp từng phần tử một** (generator) — sẽ thấy comprehension có "anh em sinh đôi" đó.

👉 Tiếp theo: **[Bài 27: Generator](../27_Generator/bai_giang.md)**