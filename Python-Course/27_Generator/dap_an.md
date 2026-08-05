# ✅ Bài 27: Đáp Án – Generator

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án để việc học hiệu quả nhất.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Generator in 5 số đầu

**Phân tích:** Bài làm quen: viết hàm có `yield`, gọi ra `generator`, duyệt bằng `for`.

**Ý tưởng:** `for x in range(n): yield x` — vòng lặp tự gọi `next()` từng cái.

**Thuật toán:**
1. Định nghĩa generator.
2. Gọi tạo generator.
3. Duyệt và in.

**Code:**

```python
def dem_den(n):
    """Sinh các số từ 0 đến n-1."""
    for x in range(n):
        yield x

for so in dem_den(5):
    print(so, end=" ")
```

**Giải thích code:**
* `yield x` — mỗi lần duyệt, generator "tra" 1 số rồi tạm dừng.
* `for so in dem_den(5)` — tự động `next()` hết dữ liệu; `end=" "` giữ cùng dòng.

**Độ phức tạp:** O(n).

---

### Bài 2: Generator bình phương

**Phân tích:** Y hệt bài 1, chỉ đổi biểu thức `yield`.

**Ý tưởng:** `yield x * x`.

**Code:**

```python
def binh_phuong(n):
    for x in range(n):
        yield x * x

for gtri in binh_phuong(6):
    print(gtri, end=" ")
```

**Giải thích code:** x = 0..5 → 0, 1, 4, 9, 16, 25.

**Độ phức tạp:** O(n).

---

### Bài 3: Chuyển generator thành list

**Phân tích:** `list(generator)` "uống cạn" generator và lưu thành list.

**Ý tưởng:** `list(chan(10))`.

**Code:**

```python
def chan(n):
    # Sinh số chẵn 0, 2, 4, ...
    for x in range(n):
        if x % 2 == 0:
            yield x

ket_qua = list(chan(10))
print(ket_qua)
```

**Giải thích code:** filter `x % 2 == 0` bên trong — chỉ yield số chẵn; list đóng gói.

**Độ phức tạp:** O(n).

---

### Bài 4: Dùng next() lấy từng phần tử

**Phân tích:** `next()` yêu cầu generator sinh giá trị kế tại đúng lúc.

**Ý tưởng:** gọi `next(g)` đúng 3 lần.

**Code:**

```python
def doi(x):
    for i in range(x):
        yield i * 2

g = doi(3)
print(next(g))   # 0
print(next(g))   # 2
print(next(g))   # 4
```

**Giải thích code:** mỗi `next(g)` chạy tới `yield`, lấy `i*2` rồi dừng; biến `i` không mất.

**Độ phức tạp:** O(1) mỗi lần next.

---

### Bài 5: Generator đếm ngược

**Phân tích:** Dùng `while` giảm dần, yield từng giá trị.

**Ý tưởng:** `while n > 0: yield n; n -= 1`.

**Code:**

```python
def dem_nguoc(n):
    while n > 0:
        yield n
        n -= 1

for so in dem_nguoc(5):
    print(so, end=" ")
```

**Giải thích code:** n giảm từ 5→1; mỗi vòng yield xong tạm dừng, lệnh `n -= 1` chạy khi gọi tiếp.

**Độ phức tạp:** O(n).

---

### Bài 6: Generator bảng cửu chương

**Phân tích:** Generator sinh chuỗi có định dạng f-string.

**Ý tưởng:** `yield f"{k} x {i} = {k * i}"`.

**Code:**

```python
def bang_nhan(k):
    for i in range(1, 11):
        yield f"{k} x {i} = {k * i}"

for dong in bang_nhan(3):
    print(dong)
```

**Giải thích code:** f-string chèn `k`, `i`, `k*i`; mỗi phép tính sinh ra khi duyệt.

**Độ phức tạp:** O(10) = O(1).

---

### Bài 7: Generator expression nhỏ

**Phân tích:** Generator expression giống list comprehension nhưng ngoặc tròn — không nạp sẵn.

**Ý tưởng:** `sum(x * 3 for x in range(1, 6))`.

**Code:**

```python
tong = sum(x * 3 for x in range(1, 6))
print(tong)
```

**Giải thích code:** 3+6+9+12+15 = 45; `sum` nuốt từng giá trị generator.

**Độ phức tạp:** O(n).