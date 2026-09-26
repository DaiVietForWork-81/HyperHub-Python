<!-- TỰ ĐỘNG ĐỒNG BỘ từ 01-Co-Ban/27-Generator/bai.md — đừng sửa trực tiếp, sửa bản chính rồi chạy tools/sync_tracks.py -->

# Bài 27 — Generator – Sinh Dữ Liệu "Từng Phần Một"

> 🎓 **Chương 5 – Lập trình hướng đối tượng & các công cụ nâng cao**

## 🧠 Điều kiện tiên quyết

- [Bài 12 — Hàm (Function) Trong Python](../12-Ham/bai.md)
- [Bài 26 — List Comprehension – Vòng Lặp "Viết Trong Một Dòng"](../26-List-Comprehension/bai.md)

---

## 🎯 Mục tiêu

Sau bài học này, học viên sẽ:

* ✅ Hiểu **generator là gì** và vì sao nó **tiết kiệm bộ nhớ** đến vậy.
* ✅ Viết được **generator function** dùng từ khóa `yield`.
* ✅ Phân biệt được **`yield` và `return`** — sự khác biệt cốt lõi.
* ✅ Viết được **generator expression** — "list comprehension" không ngoặc list.
* ✅ Dựng được **dãy Fibonacci** bằng generator.
* ✅ Biết **đọc file lớn từng dòng** bằng generator — kỹ năng xử lý dữ liệu thực tế.

---

## 📖 Kiến thức

### 1. Vấn đề: list bình thường nuốt bộ não

Ở bài 26, ta viết `[x*x for x in range(10)]` — toàn bộ kết quả **chất đầy bộ nhớ** ngay lập tức. Nếu cần sinh `range(10_000_000)` (10 triệu số bình phương), máy phải lưu hết 10 triệu số cùng lúc — rất tốn RAM.

```python
# Ngốn bộ nhớ: phải chứa 10 triệu số trong list
lon = [x * x for x in range(10_000_000)]
```

Thực tế, ta thường **chỉ cần dùng từng giá trị một** (in, cộng dồn, ghi file...). Vậy tại sao phải chuẩn bị sẵn hết cả dãy?

> 💬 **Nói đơn giản:** List = "nấu sẵn cả mâm cơm rồi mới lên mâm". Generator = "ai gọi món nào, nấu món đó ngay lúc đó". Generator **không lưu nguyên dãy** — nó **nhớ cách sinh** (công thức) và **sinh ra từng giá trị khi được yêu cầu** (lazy).

### 2. Generator function và `yield`

Dùng hàm thường với từ khóa `yield` thay cho `return`:

```python
def dem(den):           # thường thôi
    i = 0
    while i < den:
        yield i         # "tra" i, rồi TẠM DỪNG
        i += 1

g = dem(3)
print(next(g))   # 0 — yêu cầu lần 1
print(next(g))   # 1 — tiếp tục từ chỗ dừng
print(next(g))   # 2
```

| Điểm | `return` | `yield` |
|---|---|---|
| Kết quả | Trả về MỘT giá trị, hàm **kết thúc** | Trả về MỘT giá trị, hàm **TẠM DỪNG (chờ gọi tiếp)** |
| Lệnh kế | Không bao giờ chạy tiếp | Chạy tiếp từ đúng dòng dang dở |
| Kiểu hàm | Hàm thường | **Generator function** — trả về `generator` |

### 3. Hai cách "nuốt" generator

Generator là "vòi nước" — cần phải **mở vòi** mới có nước:

```python
def binh_phuong(n):
    for x in range(n):
        yield x * x

# Cách 1: duyệt trực tiếp
for gia_tri in binh_phuong(5):
    print(gia_tri)   # 0 1 4 9 16

# Cách 2: next() từng cái
g = binh_phuong(5)
print(next(g))   # 0
print(next(g))   # 1
```

> ⚠️ `next(g)` gọi tới lần vượt quá sẽ báo `StopIteration` — báo "vòi đã cạn".

```mermaid
flowchart LR
    A[generator object] -->|next() hoặc vòng for| B[Sinh giá trị kế]
    B --> C{yield tiếp?}
    C -->|Còn| A
    C -->|Hết| D[StopIteration]
```

### 4. Generator expression (biểu thức generator)

Dùng **dấu ngoặc tròn** thay cho ngoặc vuông — chỉ khác ở chỗ:

```python
# List comprehension: sinh ngay cả list
bp_list = [x * x for x in range(1_000_000)]     # bộ nhớ lớn

# Generator expression: gọn hơn, tạm sinh sau
bp_gen = (x * x for x in range(1_000_000))      # bộ nhớ nhỏ
```

`bp_gen` là generator — chưa lấy được giá trị nào; cần giá trị thì `next()` hoặc vòng lặp. Cả hai đều "mách" công thức như nhau, chỉ khác ở thời điểm sinh.

> 💬 Ví dụ với `sum`: `sum(x*x for x in range(10_000_000))` — cộng dồn từng bình phương, **không mang cả triệu số vào RAM**. Cách viết này rất được ưa chuộng — bỏ cả ngoặc vuông luôn.

### 5. Dãy Fibonacci bằng generator

Fibonacci: số sau = tổng 2 số trước: 0, 1, 1, 2, 3, 5, 8, 13...

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for so in fibonacci(8):
    print(so, end=" ")   # 0 1 1 2 3 5 8 13
```

Nếu dùng list, muốn 1 triệu số Fibonacci là chết bộ nhớ. Generator chỉ nhớ **2 biến `a`, `b`** — bất kể đến số thứ bao nhiêu.

### 6. Đọc file lớn từng dòng

Bài 22 dạy `read()` và `readlines()` — nhưng file 10 GB thì **chết mất** vì phải nạp cả file. Generator là giải pháp:

```python
def doc_tung_dong(ten_file):
    with open(ten_file, encoding="utf-8") as f:
        for dong in f:          # duyệt từng dòng, không cần readlines
            yield dong.strip()  # tra về từng dòng một

for dong in doc_tung_dong("nhat_ky.txt"):
    print(dong)     # xử lý từng dòng — bộ nhớ luôn chỉ có 1 dòng
```

> Đọc `for dong in f` là trình duyệt "lười" của file — mỗi lần chỉ đưa ra 1 dòng. Chính là generator do Python xây sẵn. 🧠

### 7. Tiết kiệm bộ nhớ — so chi phí cụ thể

```python
import sys

bp_list = [x * x for x in range(100_000)]
bp_gen = (x * x for x in range(100_000))

print(sys.getsizeof(bp_list))   # vài trăm nghìn byte (lớn hơn nhiều)
print(sys.getsizeof(bp_gen))    # chỉ vài chục byte!
```

| Nội | `list` | `generator` |
|---|---|---|
| Khi tạo | Nạp toàn bộ vào RAM | Ghi nhớ "công thức" — bộ nhớ hầu như 0 |
| Truy cập ngẫu nhiên `lst[5]` | ✅ | ❌ (sinh tuần tự) |
| Lặp lại nhiều lần | ✅ Vẫn còn nguyên | ❌ một lần — dùng hết là cạn |
| `len()`, `index()` | ✅ | ❌ Không có |
| Ứng dụng | Cần giữ lại xử lý ngẫu nhiên | Dãy lớn/tính dần, đọc file, stream |

### 8. Khi nào dùng generator?

* Dãy cực lớn (hàng triệu/mươi triệu phần tử) → dùng để **đừng cháy RAM**.
* Đọc file xử lý từng dòng → luôn generator (thực tế trong nghề).
* Dãy vô hạn (đếm số thứ tự, số nguyên tố, stream JSON...).
* Không cần giữ toàn bộ, chỉ cần đếm/tìm min/max/tổng: `sum(x*x for x in so)`.

> ⚠️ Ngược lại: cần truy cập ngẫu nhiên `lst[5]`, duyệt nhiều lần, hoặc đếm độ dài → dùng list/tuple thường.

---

## 💡 Ví dụ minh họa

### Ví dụ 1: Generator đếm ngược

```python
def dem_nguoc(n):
    """Sinh các số từ n xuống 0."""
    while n > 0:
        yield n            # trả n, TẠM DỪNG
        n -= 1             # lần gọi sau bắt đầu từ đây

for so in dem_nguoc(5):
    print(so, end=" ")     # 5 4 3 2 1
```

**Giải thích từng dòng:**

| Dòng code | Ý nghĩa |
|---|---|
| `def dem_nguoc(n):` | Hàm CÓ `yield` → gọi hàm ra **generator object**, vòng lặp thân chưa chạy gì |
| `yield n` | Trả về `n`, tạm dừng chờ lần `next` sau |
| `n -= 1` | Chạy khi được gọi tiếp — biến vẫn "còn nhớ giá trị" |
| `for so in dem_nguoc(5)` | Lặp tự động `next()` tới khi hết |

### Ví dụ 2: next() từng phần tử

```python
def binh_phuong(n):
    for x in range(n):
        yield x * x

g = binh_phuong(4)
print(next(g))   # 0 — x=0
print(next(g))   # 1 — x=1
print(next(g))   # 4 — x=2
print(next(g))   # 9 — x=3
# print(next(g))  # Sẽ báo StopIteration tại đây
```

**Giải thích từng dòng:**

| Dòng code | Ý nghĩa |
|---|---|
| `g = binh_phuong(4)` | Tạo generator — **chưa tính gì cả** |
| `next(g)` | Chạy tới `yield`, trả về giá trị, dừng |
| `next(g)` lặp lại | Tiếp tục chạy từ chỗ dừng, lấy giá trị kế |
| Đến cuối vòng | `StopIteration` nhắc hết dữ liệu |

### Ví dụ 3: Generator expression tính tổng nhanh

```python
# Tính tổng bình phương các số chẵn từ 1..1_000_000
tong = sum(x * x for x in range(1_000_001) if x % 2 == 0)
# Sinh và cộng dồn lần lượt — không chứa cả dãy!
print(tong)
```

**Giải thích từng dòng:**

| Phần code | Ý nghĩa |
|---|---|
| `(x * x for x in ... if ...)` | Ngoặc tròn = generator expression |
| `sum(...)` | Nuốt từng giá trị sinh ra, không giữ dãy |
| `range(1_000_001)` | Dãy lên tới 1 triệu — an toàn nhờ gen |

---

## 🔬 Ví dụ nâng cao

### Ví dụ 1: Fibonacci generator — sinh bao nhiêu số muốn nên tránh cháy nhớ

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

so = [x for x in fibonacci(20)]      # 20 số Fibonacci đầu
print(so)
```

Kết quả:

```
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
```

> 💡 Thử `sum(fibonacci(1000))` — vẫn chỉ dùng 2 biến `a`, `b` trong RAM.

### Ví dụ 2: Đọc file lớn từng dòng và lọc

```python
def cac_dong(ten_file):
    with open(ten_file, encoding="utf-8") as f:
        for dong in f:
            yield dong.strip()

# Ghi thử một file nhỏ rồi đọc lại bằng generator
with open("log.txt", "w", encoding="utf-8") as f:
    f.write("OK bat dau\n")
    f.write("LOI tai buoc 2\n")
    f.write("OK ket thuc\n")

for dong in cac_dong("log.txt"):
    if dong.startswith("LOI") or dong.startswith("ERROR"):
        print("[Phat hien]", dong)
```

Kết quả:

```
[Phat hien] LOI tai buoc 2
```

> 🧠 Điều kiện `for dong in f` tự đọc từng dòng — bộ nhớ chỉ có 1 dòng tại một thời điểm.

### Ví dụ 3: Generator vô hạn — đếm mãi mãi

```python
def dem_mai():
    i = 0
    while True:          # vòng vô hạn — nhưng OK vì generator chỉ sinh khi hỏi
        yield i
        i += 1

from itertools import islice

# Lấy 5 số đầu tiên của dãy vô hạn
nam_so = list(islice(dem_mai(), 5))
print(nam_so)   # [0, 1, 2, 3, 4]
```

> ⚠️ List không làm được dãy vô hạn (cháy RAM ngay). Generator thì dễ như trở bàn tay — vì nó không chứa gì ngoài "công thức".

### Ví dụ 4: So sánh bộ nhớ list vs generator

```python
import sys

lst = [x * x for x in range(200_000)]
gen = (x * x for x in range(200_000))

print("List:", sys.getsizeof(lst), "byte")    # lớn
print("Gen :", sys.getsizeof(gen), "byte")    # bé xinh
```

> 🔬 Kết quả mẫu: List ~ vài MB, Gen ~ vài chục byte — hơn **nghìn lần.**

---

## ⚠️ Lỗi thường gặp

### Lỗi 1: Gọi hàm generator mà không dùng — "cạn bình"

```python
def dem(den):
    for x in range(den):
        yield x

g = dem(5)      # tạo generator
dem(5)          # ❌ SAI: gọi xong bỏ — generator mới không bao giờ được dùng
```

* **Kết quả:** không lỗi, nhưng code vô ích — generator chỉ sinh khi duyệt.
* **Cách sửa:** gán cho biến rồi duyệt: `for x in dem(5): ...`.

### Lỗi 2: Tưởng `yield` giống `return` — viết `return` ở giữa

```python
def dem(den):
    if den <= 0:
        return           # trả None — và KẾT THÚC generator
    for x in range(den):
        yield x
```

* **Nguyên nhân:** `return` làm hàm kết thúc luôn, các `yield` sau không chạy.
* **Cách sửa:** muốn dừng sớm vẫn dùng `return` — đó là cách chuẩn; chỉ cần hiểu khác bản chất: `return` dừng hẳn, `yield` tạm dừng.

### Lỗi 3: Duyệt generator **hai lần** — lần hai trống rỗng

```python
g = (x * x for x in range(5))

print(sum(g))    # 30 — đã "uống cạn"
print(sum(g))    # 0 — generator không còn gì!
```

* **Nguyên nhân:** generator một chiều — dùng xong là hết.
* **Cách sửa:** cần dùng lại nhiều lần → chuyển thành list: `lst = list(g)` rồi dùng `lst`.

### Lỗi 4: Gọi `len()` trên generator

```python
g = (x * x for x in range(5))
print(len(g))   # ❌ TypeError: object of type 'generator' has no len()
```

* **Cách sửa:** muốn biết số phần tử → `len(list(g))` (chấp nhận tốn bộ nhớ) hoặc đếm bằng vòng lặp.

### Lỗi 5: Quên bọc list() khi cần giữ kết quả

```python
print(g)   # <generator object <genexpr> at 0x...> — không thấy dữ liệu!
```

* **Cách sửa:** nếu muốn xem toàn bộ: `print(list(g))`.

---

## 💎 Mẹo

* 🎭 **Nhớ câu thần chú:** `yield` = tạm dừng, `return` = kết thúc.
* 🧘 **Viết hàm generator như "cuốn sách mở từng trang"** — code bên trong cứ viết tự nhiên, người đọc cứ lật từng trang bằng vòng lặp.
* 📦 **Comprehension ↔ generator chỉ khác ngoặc:** `[...]` (nạp ngay) vs `(...)` (nạp dần).
* 📖 **Luôn đọc file bằng `for dong in f`** — kết hợp generator rồi xử lý từng dòng, chuẩn nghề.
* 🚫 **Không dùng generator khi** cần chỉ mục, duyệt lại, hay `len()` thường xuyên.
* 🧪 **Bài sau (28) dùng `yield` rồi bọc hàm khác — mở ra decorator!**

---

## 📝 Tóm tắt

| Khái niệm | Nội dung chính |
|---|---|
| 🔑 `yield` | Trả giá trị và TẠM DỪNG — lần gọi sau tiếp tục từ dòng dừng |
| 🎩 Generator function | Hàm chứa `yield` — gọi ra generator object |
| 🍡 Generator expression | `(x * x for x in ...)` — sinh dần từng giá trị |
| 🧲 `next(g)` | Yêu cầu giá trị kế — hết sẽ `StopIteration` |
| 💾 Tiết kiệm nhớ | Không chứa dãy — chỉ nhớ "công thức" + vị trí |
| 📚 File lớn | `for dong in f` + yield → xử lý từng dòng an toàn |
| ⚠️ Hạn chế | Một chiều, không chỉ mục, không `len()`, duyệt 1 lần |

---

## 🧪 Kiểm tra nhanh

1. ❓ Viết generator function trả về bình phương các số 0..n.
2. ❓ `yield` khác `return` ở điểm cốt lõi nào?
3. ❓ Khi duyệt generator hết giá trị, `next(g)` báo lỗi gì?
4. ❓ Sự khác biệt chính giữa `[... for ...]` và `(... for ...)`?
5. ❓ Vì sao generator tiết kiệm bộ nhớ đến vậy?
6. ❓ Đúng hay sai: generator có thể duyệt lại nhiều lần như list?
7. ❓ Viết generator sinh n số Fibonacci.
8. ❓ Đọc file lớn nên dùng `readlines()` hay generator? Vì sao?

<details>
<summary>🔍 Xem đáp án</summary>

1. `def bp(n): for x in range(n): yield x * x`.
2. `return` kết thúc hàm, trả một giá trị; `yield` tạm dừng, lần gọi sau tiếp tục từ dòng dừng.
3. `StopIteration`.
4. List comprehension nạp toàn bộ ngay; generator expression sinh dần từng giá trị.
5. Vì generator không lưu dãy giá trị — chỉ giữ "công thức" và vị trí đang dừng.
6. Sai — generator một chiều, duyệt hết là hết.
7. Như ở phần Kiến thức mục 5 (0, 1, 1, 2, 3, 5, ...).
8. Generator — `readlines()` nạp cả file vào RAM, generator chỉ giữ 1 dòng.

</details>

---

## 📚 Bài đọc thêm

* [Python.org – Generators (tài liệu chính thức)](https://docs.python.org/3/howto/functional.html#generators)
* [Real Python – Introduction to Python Generators](https://realpython.com/introduction-to-python-generators/)
* [W3Schools – Python Generators](https://www.w3schools.com/python/python_generators.asp)

---

---

## 🧩 Bài tập

> 📝 🎯 **Chủ đề:** Generator function với `yield`, `next()`, generator expression, Fibonacci, đọc file từng dòng, tiết kiệm bộ nhớ.

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Generator in 5 số đầu

* **Đề bài:** Viết generator `dem_den(n)` sinh các số từ 0 đến n-1. Gọi với n = 5 và in từng số bằng vòng lặp `for`.
* **Input:** Không có.
* **Output:**
  ```
  0 1 2 3 4
  ```
* **Gợi ý:** `for x in range(n): yield x`, sau đó `for so in dem_den(5): print(so, end=" ")`.

### Bài 2: Generator bình phương

* **Đề bài:** Viết generator `binh_phuong(n)` sinh bình phương các số 0..n-1. Gọi với n = 6, in từng giá trị.
* **Input:** Không có.
* **Output:**
  ```
  0 1 4 9 16 25
  ```
* **Gợi ý:** `yield x * x`.

### Bài 3: Chuyển generator thành list

* **Đề bài:** Viết generator `chan(n)` sinh các số chẵn 0, 2, 4... nhỏ hơn n. Gọi với n = 10, chuyển kết quả thành list bằng `list()` và in.
* **Input:** Không có.
* **Output:**
  ```
  [0, 2, 4, 6, 8]
  ```
* **Gợi ý:** `[0, 2, 4, 6, 8] = list(chan(10))`.

### Bài 4: Dùng next() lấy từng phần tử

* **Đề bài:** Viết generator `doi(x)` trả `x * 2`. Gọi và lấy 3 phần tử đầu bằng `next()` rồi in chúng.
* **Input:** Không có.
* **Output:**
  ```
  0
  2
  4
  ```
* **Gợi ý:** `g = doi(3)` rồi `print(next(g))` ba lần.

### Bài 5: Generator đếm ngược

* **Đề bài:** Viết generator `dem_nguoc(n)` sinh n, n-1, ..., 1. Gọi với n = 5 và in các giá trị trên một dòng.
* **Input:** Không có.
* **Output:**
  ```
  5 4 3 2 1
  ```
* **Gợi ý:** `while n > 0: yield n; n -= 1`.

### Bài 6: Generator bảng cửu chương

* **Đề bài:** Viết generator `bang_nhan(k)` sinh các chuỗi `"k x i = k*i"` cho i = 1..10. Gọi với k = 3 và in từng dòng.
* **Input:** Không có.
* **Output:**
  ```
  3 x 1 = 3
  3 x 2 = 6
  ...
  3 x 10 = 30
  ```
* **Gợi ý:** `yield f"{k} x {i} = {k * i}"`.

### Bài 7: Generator expression nhỏ

* **Đề bài:** Dùng generator expression `(x * 3 for x in range(1, 6))` rồi in tổng các giá trị.
* **Input:** Không có.
* **Output:**
  ```
  45
  ```
* **Gợi ý:** `sum(x * 3 for x in range(1, 6))` — 3+6+9+12+15.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Generator Fibonacci 10 số

* **Đề bài:** Viết generator `fibonacci(n)` sinh n số Fibonacci đầu tiên (0, 1, 1, 2, 3, 5...). Gọi với n = 10, in dãy.
* **Input:** Không có.
* **Output:**
  ```
  0 1 1 2 3 5 8 13 21 34
  ```
* **Gợi ý:** `a, b = 0, 1; yield a; a, b = b, a + b` trong vòng lặp.

### Bài 9: Generator số chẵn đến n

* **Đề bài:** Viết generator `so_chan(n)` sinh các số chẵn từ 0 đến n. Gọi với n = 20, tính tổng bằng `sum()`.
* **Input:** Không có.
* **Output:**
  ```
  110
  ```
* **Gợi ý:** `yield x` khi `x % 2 == 0`; 0+2+...+20 = 110.

### Bài 10: Đọc file từng dòng

* **Đề bài:** Tạo file `nhat_ky.txt` với 3 dòng nội dung bất kỳ (dùng `open(..., "w")`). Viết generator `doc_file(ten)` đọc và trả từng dòng đã bỏ ký tự xuống dòng. In 3 dòng ra màn hình.
* **Input:** Không có.
* **Output:** Ví dụ:
  ```
  Dong 1: Chao buoi sang
  Dong 2: Toi dang hoc Python
  Dong 3: Generator rat hay
  ```
* **Gợi ý:** `with open(ten, encoding="utf-8") as f: for dong in f: yield dong.strip()`.

### Bài 11: Lọc dòng chứa từ khóa

* **Đề bài:** File `log.txt` có 4 dòng (2 dòng bắt đầu bằng `LOI`, 2 dòng khác). Viết generator lọc và in ra những dòng bắt đầu bằng `LOI`.
* **Input:** Không có.
* **Output:** Ví dụ:
  ```
  LOI ket noi mang
  LOI tai lieu khong ton tai
  ```
* **Gợi ý:** `if dong.startswith("LOI"): yield dong`.

### Bài 12: Tổng bằng generator expression có điều kiện

* **Đề bài:** Dùng generator expression tính tổng **bình phương các số lẻ** từ 1 đến 10.
* **Input:** Không có.
* **Output:**
  ```
  165
  ```
* **Gợi ý:** `sum(x * x for x in range(1, 11) if x % 2 == 1)` — 1+9+25+49+81 = 165.

### Bài 13: Generator phân tách chữ số

* **Đề bài:** Viết generator `chu_so(so)` sinh từng chữ số của một số nguyên dương (từ trái sang phải). Gọi với 2026 và in các chữ số.
* **Input:** Không có.
* **Output:**
  ```
  2 0 2 6
  ```
* **Gợi ý:** đổi sang chuỗi `str(so)` rồi duyệt từng ký tự, `yield int(c)`.

### Bài 14: Generator xoay vòng ba môn học

* **Đề bài:** Viết generator `lich_hoc()` lặp vô hạn qua 3 môn `["Toan", "Ly", "Hoa"]` theo thứ tự. Dùng `islice` lấy 7 phần tử đầu và in.
* **Input:** Không có.
* **Output:**
  ```
  Toan Ly Hoa Toan Ly Hoa Toan
  ```
* **Gợi ý:** `while True:` duyệt danh sách rồi `yield mon`; `from itertools import islice`.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Generator số nguyên tố

* **Đề bài:** Viết generator `so_nguyen_to(n)` sinh các số nguyên tố nhỏ hơn n. Gọi với n = 30, in các số nguyên tố.
* **Input:** Không có.
* **Output:**
  ```
  2 3 5 7 11 13 17 19 23 29
  ```
* **Gợi ý:** hàm phụ `la_nguyen_to(x)` kiểm tra ước từ 2 đến `x - 1` (hoặc đến `int(x**0.5)`).

### Bài 16: So sánh bộ nhớ list vs generator

* **Đề bài:** Viết chương trình so sánh `sys.getsizeof` của list `[x for x in range(50000)]` và generator `(x for x in range(50000))`, in ra hai con số.
* **Input:** Không có.
* **Output:** Ví dụ:
  ```
  Kich thuoc list: 406632 byte
  Kich thuoc generator: 112 byte
  ```
* **Gợi ý:** `import sys; print(sys.getsizeof(lst)); print(sys.getsizeof(gen))`.

### Bài 17: Đếm dòng trong file lớn (giả lập)

* **Đề bài:** Tạo file `du_lieu.txt` có 5 dòng số. Dùng generator + `sum(1 for ...)` để đếm số dòng **không rỗng** và in ra.
* **Input:** Không có.
* **Output:**
  ```
  So dong khong rong: 5
  ```
* **Gợi ý:** `sum(1 for dong in f if dong.strip() != "")`.

### Bài 18: Generator ghép đôi hai danh sách

* **Đề bài:** Viết generator `ghep_doi(a, b)` sinh lần lượt phần tử a[0], b[0], a[1], b[1], ... Cho `a = ["A1","A2"]`, `b = ["B1","B2"]`, in kết quả.
* **Input:** Không có.
* **Output:**
  ```
  A1 B1 A2 B2
  ```
* **Gợi ý:** duyệt `range(len(a))` rồi `yield a[i]` và `yield b[i]`.

### Bài 19: Tổng Fibonacci 50 số (chứng minh tiết kiệm nhớ)

* **Đề bài:** Dùng generator `fibonacci(n)` (bài 8) tính tổng 50 số Fibonacci đầu tiên bằng `sum()` và in kết quả (số chẵn).
* **Input:** Không có.
* **Output:**
  ```
  Tong 50 so Fibonacci dau: 12586269024
  ```
* **Gợi ý:** `sum(fibonacci(50))` — chỉ cần generator, không cần list.

### Bài 20: Đọc log + thống kê lỗi (tổng hợp)

* **Đề bài:** Tạo file `he_thong.log` gồm các dòng dạng `OK ...` hoặc `LOI ...` (tự viết 6 dòng). Viết chương trình dùng generator đọc file, đếm số dòng `LOI` và in ra tổng.
* **Input:** Không có.
* **Output:** Ví dụ:
  ```
  So loi phan hien: 3
  ```
* **Gợi ý:** generator `doc_file` (bài 10) kết hợp `sum(1 for dong in doc_file(...) if dong.startswith("LOI"))`.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Viết generator function với `yield`, dùng `next()` và vòng lặp.
* ✅ Dùng generator expression tiết kiệm bộ nhớ.
* ✅ Dựng Fibonacci, số nguyên tố, dãy vô hạn.
* ✅ Xử lý file lớn từng dòng và đếm/thống kê bằng generator.

> 💪 Chưa tự làm được bài nào thì đừng lo — hãy xem lại bài giảng rồi quay lại. **Lập trình là luyện tập!**

---

## ✅ Đáp án

> 💡 **Hãy tự làm bài tập trước** rồi mới mở đáp án.

## 🟢 Dễ (Bài 1 – 7)


<details>
<summary>✅ Bài 1: Generator in 5 số đầu</summary>


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

</details>

<details>
<summary>✅ Bài 2: Generator bình phương</summary>


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

</details>

<details>
<summary>✅ Bài 3: Chuyển generator thành list</summary>


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

</details>

<details>
<summary>✅ Bài 4: Dùng next() lấy từng phần tử</summary>


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

</details>

<details>
<summary>✅ Bài 5: Generator đếm ngược</summary>


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

</details>

<details>
<summary>✅ Bài 6: Generator bảng cửu chương</summary>


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

</details>

<details>
<summary>✅ Bài 7: Generator expression nhỏ</summary>


**Phân tích:** Generator expression giống list comprehension nhưng ngoặc tròn — không nạp sẵn.

**Ý tưởng:** `sum(x * 3 for x in range(1, 6))`.

**Code:**

```python
tong = sum(x * 3 for x in range(1, 6))
print(tong)
```

**Giải thích code:** 3+6+9+12+15 = 45; `sum` nuốt từng giá trị generator.

**Độ phức tạp:** O(n).
</details>

<details>
<summary>✅ Bài 8: Generator Fibonacci 10 số</summary>

**Phân tích:** Dãy Fibonacci: số sau = tổng hai số trước (bắt đầu 0, 1).
Cần "sinh n số đầu" — không lưu list, chỉ `yield` từng số.

**Ý tưởng:** Giữ cặp `(a, b)`; mỗi vòng lặp `yield a` rồi trượt cặp
`a, b = b, a + b` — mẫu "trượt cửa sổ 2 số" rất hay gặp khi làm việc với dãy số.

**Thuật toán:**
1. `a, b = 0, 1`.
2. Lặp n lần: `yield a`; cập nhật `a, b = b, a + b`.
3. In bằng vòng lặp, cách nhau bằng dấu cách.

**Code:**

```python
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


for so in fibonacci(10):
    print(so, end=" ")
```

**Giải thích code:**
* `fibonacci(10)` sinh đúng 10 số: 0 1 1 2 3 5 8 13 21 34. ✔
* Nếu viết `return a` thay vì `yield a` thì hàm chỉ trả đúng 1 số đầu rồi dừng —
  đó là sự khác biệt cốt lõi giữa hàm thường và generator.

**Độ phức tạp:** O(n) thời gian, O(1) bộ nhớ (không lưu dãy).

</details>

<details>
<summary>✅ Bài 9: Generator số chẵn đến n</summary>

**Phân tích:** Sinh các số chẵn từ 0 đến n (bao gồm n nếu n chẵn), rồi tính
tổng bằng `sum()` — kết hợp generator với hàm tổng hợp sẵn có.

**Ý tưởng:** Duyệt `range(0, n + 1)`, `yield x` khi `x % 2 == 0`;
`sum()` tự "kéo" generator đến hết — không cần list trung gian.

**Thuật toán:**
1. `so_chan(n)`: lặp 0..n, yield số chẵn.
2. `print(sum(so_chan(20)))`.

**Code:**

```python
def so_chan(n):
    for x in range(0, n + 1):
        if x % 2 == 0:
            yield x


print(sum(so_chan(20)))
```

**Giải thích code:**
* 0 + 2 + 4 + ... + 20 = 110. ✔
* `range(0, n + 1)` chứ không phải `range(n)` — vì phải **bao gồm** n;
  lỗi "thiếu số cuối" khi quên `+ 1` là lỗi rất phổ biến.
* So sánh với list comprehension `[x for x in range(21) if x % 2 == 0]`:
  cho cùng kết quả nhưng tốn bộ nhớ lưu cả dãy.

**Độ phức tạp:** O(n) thời gian, O(1) bộ nhớ phụ.

</details>

<details>
<summary>✅ Bài 10: Đọc file từng dòng</summary>

**Phân tích:** Hai việc: (1) tạo file `nhat_ky.txt` 3 dòng bằng chế độ `"w"`,
(2) generator `doc_file(ten)` đọc file và trả từng dòng đã `.strip()`.

**Ý tưởng:** `with open(...)` tự đóng file; trong generator, `for dong in f`
duyệt file từng dòng **mà không cần đọc cả file vào RAM** — đây chính là lý do
generator ra đời (xử lý file lớn).

**Thuật toán:**
1. Ghi 3 dòng nội dung vào file (chế độ `"w"`, `encoding="utf-8"`).
2. `doc_file(ten)`: mở file, `yield dong.strip()` cho mỗi dòng.
3. Đánh số thứ tự khi in.

**Code:**

```python
# Bước 1 — tạo file mẫu
with open("nhat_ky.txt", "w", encoding="utf-8") as f:
    f.write("Chao buoi sang\n")
    f.write("Toi dang hoc Python\n")
    f.write("Generator rat hay\n")


# Bước 2 — generator đọc file
def doc_file(ten):
    with open(ten, encoding="utf-8") as f:
        for dong in f:
            yield dong.strip()


# Bước 3 — dùng
i = 1
for dong in doc_file("nhat_ky.txt"):
    print(f"Dong {i}: {dong}")
    i += 1
```

**Giải thích code:**
* `.strip()` bỏ ký tự xuống dòng `\n` ở cuối — không có nó, mỗi dòng in ra sẽ
  cách nhau một dòng trống (vì `print` tự thêm `\n`).
* Chế độ `"w"` ghi đè file nếu đã tồn tại — muốn giữ nội dung cũ thì dùng `"a"`.
* Mẫu này dùng lại nguyên vẹn ở bài 11, 17, 20 — học một lần, dùng nhiều lần.

**Độ phức tạp:** O(số dòng) thời gian, O(1) bộ nhớ (đọc lười từng dòng).

</details>

<details>
<summary>✅ Bài 11: Lọc dòng chứa từ khóa</summary>

**Phân tích:** Đọc file `log.txt` 4 dòng, chỉ giữ dòng bắt đầu bằng `LOI`.
Tái sử dụng đúng mẫu `doc_file` của bài 10 + thêm điều kiện lọc trong generator.

**Ý tưởng:** `str.startswith("LOI")` kiểm tra tiền tố; đặt điều kiện ngay trong
generator để phía dùng không phải lọc lại — generator "vừa đọc vừa lọc".

**Thuật toán:**
1. Tạo file `log.txt` với 2 dòng `LOI` và 2 dòng khác.
2. Generator duyệt từng dòng, `yield` dòng đã strip nếu bắt đầu bằng `LOI`.
3. In kết quả.

**Code:**

```python
# Tạo file mẫu
with open("log.txt", "w", encoding="utf-8") as f:
    f.write("LOI ket noi mang\n")
    f.write("OK chay thanh cong\n")
    f.write("LOI tai lieu khong ton tai\n")
    f.write("OK ket thuc\n")


def loc_loi(ten):
    with open(ten, encoding="utf-8") as f:
        for dong in f:
            if dong.startswith("LOI"):
                yield dong.strip()


for dong in loc_loi("log.txt"):
    print(dong)
```

**Giải thích code:**
* In ra đúng 2 dòng `LOI...`. ✔
* `startswith` phân biệt chữ hoa/thường: dòng `loi ...` (thường) sẽ bị bỏ qua —
  nếu muốn "không phân biệt", cần `dong.upper().startswith("LOI")`.
* Cùng một kỹ thuật áp dụng cho lọc email, lọc số điện thoại, lọc dòng CSV...

**Độ phức tạp:** O(số dòng) thời gian, O(1) bộ nhớ.

</details>

<details>
<summary>✅ Bài 12: Tổng bằng generator expression có điều kiện</summary>

**Phân tích:** Tính 1² + 3² + 5² + 7² + 9² = 165 bằng **một biểu thức duy nhất** —
không vòng lặp, không biến tạm. Dạng `( ... for ... if ... )` gọi là generator
expression có điều kiện.

**Ý tưởng:** `sum(X for x in range(1, 11) if LẺ)` — `sum` kéo từng giá trị,
cộng dồn, không tạo list trung gian.

**Thuật toán:** Một dòng: lọc số lẻ trong 1..10, bình phương, cộng dồn.

**Code:**

```python
tong = sum(x * x for x in range(1, 11) if x % 2 == 1)
print(tong)
```

**Giải thích code:**
* 1 + 9 + 25 + 49 + 81 = 165. ✔
* So sánh 3 cách viết cùng kết quả:
  * List comprehension: `sum([x*x for x in range(1,11) if x%2==1])` — tạo list
    trung gian trong RAM rồi mới cộng.
  * Generator expression (cách trên) — không tạo list, tiết kiệm nhớ.
  * Vòng lặp + biến cộng dồn — dài dòng nhưng dễ đọc nhất cho người mới.

**Độ phức tạp:** O(n) thời gian, O(1) bộ nhớ.

</details>

<details>
<summary>✅ Bài 13: Generator phân tách chữ số</summary>

**Phân tích:** Từ số nguyên 2026 sinh ra các chữ số 2, 0, 2, 6 theo thứ tự từ
trái sang phải. Phép chia lấy dư (`%`, `//`) cho ra chữ số từ **phải sang trái**
(khó hơn); cách đơn giản và trực quan là đổi số thành chuỗi rồi duyệt ký tự.

**Ý tưởng:** `str(so)` biến 2026 thành "2026"; mỗi ký tự là một chữ số —
`yield int(c)` để trả về số nguyên chứ không phải ký tự.

**Thuật toán:**
1. Đổi số thành chuỗi.
2. Duyệt từng ký tự, `yield int(ký tự)`.
3. In cách nhau bằng dấu cách.

**Code:**

```python
def chu_so(so):
    for c in str(so):
        yield int(c)


for c in chu_so(2026):
    print(c, end=" ")
```

**Giải thích code:**
* In ra: 2 0 2 6. ✔
* Số 0 ở giữa được giữ đúng vị trí — cách chia lấy dư cũng làm được nhưng phải
  xử lý khéo léo; cách chuỗi tự nhiên bảo toàn thứ tự và số 0 đứng giữa.
* `str(so)` với số âm (ví dụ -123) sẽ có ký tự `'-'` đầu — `int('-')` báo lỗi;
  muốn chắc chắn, dùng `abs(so)` trước.

**Độ phức tạp:** O(số chữ số) thời gian, O(1) bộ nhớ phụ.

</details>

<details>
<summary>✅ Bài 14: Generator xoay vòng ba môn học</summary>

**Phân tích:** Cần "lặp vô hạn" qua 3 môn theo thứ tự, rồi lấy 7 phần tử đầu.
Hai công cụ: `while True` (vòng lặp vô hạn) và `itertools.islice` (cắt lát một
dãy vô hạn mà không treo máy).

**Ý tưởng:** Generator `lich_hoc()` không bao giờ dừng (`while True` + lặp danh
sách); phía dùng quyết định lấy bao nhiêu bằng `islice` — tách bạch "sinh vô
hạn" và "lấy hữu hạn".

**Thuật toán:**
1. `lich_hoc()`: lặp vô tận, `yield` từng môn theo thứ tự.
2. `from itertools import islice`; `islice(lich_hoc(), 7)` lấy 7 phần tử.
3. In cách nhau bằng dấu cách.

**Code:**

```python
from itertools import islice


def lich_hoc():
    mon_hoc = ["Toan", "Ly", "Hoa"]
    while True:              # lặp vô hạn
        for mon in mon_hoc:
            yield mon


for mon in islice(lich_hoc(), 7):
    print(mon, end=" ")
```

**Giải thích code:**
* In ra: Toan Ly Hoa Toan Ly Hoa Toan. ✔
* `islice` kéo generator đúng 7 lần rồi dừng — generator vẫn "sống" nhưng không
  bị gọi tiếp; không dùng `islice` mà `list(lich_hoc())` sẽ **treo máy** vì cố
  biến dãy vô hạn thành list — lỗi nguy hiểm nhất khi làm việc với generator
  vô hạn.
* Ứng dụng thật: lịch xoay ca, vòng quay nhiệm vụ, sinh ID tuần hoàn...

**Độ phức tạp:** O(k) với k = số phần tử lấy ra; O(1) bộ nhớ.

</details>

<details>
<summary>✅ Bài 15: Generator số nguyên tố</summary>

**Phân tích:** Sinh các số nguyên tố nhỏ hơn n. Cần hàm phụ `la_nguyen_to(x)`
và generator lọc. Kiểm tra đến `√x` thay vì `x - 1` là tối ưu quan trọng
(n giảm từ O(x) xuống O(√x) mỗi số).

**Ý tưởng:** Duyệt 2..n-1, `yield x` khi `x` nguyên tố; `la_nguyen_to` loại
ngay số < 2 và thử ước từ 2 đến `int(x**0.5)`.

**Thuật toán:**
1. `la_nguyen_to(x)`: < 2 → False; ước nào chia hết → False; còn lại True.
2. `so_nguyen_to(n)`: duyệt 2..n-1, yield số thỏa mãn.
3. In cách nhau bằng dấu cách.

**Code:**

```python
def la_nguyen_to(x):
    if x < 2:
        return False
    for u in range(2, int(x ** 0.5) + 1):
        if x % u == 0:
            return False
    return True


def so_nguyen_to(n):
    for x in range(2, n):
        if la_nguyen_to(x):
            yield x


for so in so_nguyen_to(30):
    print(so, end=" ")
```

**Giải thích code:**
* In ra: 2 3 5 7 11 13 17 19 23 29. ✔
* `int(x ** 0.5) + 1` — cộng 1 để `range` bao gồm chính căn bậc hai
  (ví dụ x = 9, không có +1 sẽ bỏ sót ước 3 — lỗi tinh vi hay gặp!).
* Số 2 là số chẵn nguyên tố duy nhất; hàm xử lý đúng vì vòng `range(2, 2)`
  rỗng → trả True.

**Độ phức tạp:** O(n√n) thời gian, O(1) bộ nhớ phụ.

</details>

<details>
<summary>✅ Bài 16: So sánh bộ nhớ list vs generator</summary>

**Phân tích:** Chứng minh bằng số liệu: list 50.000 số tốn bao nhiêu byte,
generator tương ứng tốn bao nhiêu. `sys.getsizeof` đo kích thước đối tượng.

**Ý tưởng:** Tạo cả hai, in `getsizeof` từng cái; chênh lệch lớn là đáp án
cho câu hỏi "vì sao cần generator".

**Thuật toán:**
1. `import sys`.
2. List comprehension 50.000 số; generator expression tương ứng.
3. In hai con số.

**Code:**

```python
import sys

lst = [x for x in range(50000)]
gen = (x for x in range(50000))

print("Kich thuoc list:", sys.getsizeof(lst), "byte")
print("Kich thuoc generator:", sys.getsizeof(gen), "byte")
```

**Giải thích code:**
* Kết quả mẫu: list ~400.000+ byte, generator chỉ ~100 byte — chênh lệch
  hàng nghìn lần, và khoảng cách càng nới rộng khi dữ liệu càng lớn.
* `getsizeof(lst)` đo cả vùng chứa 50.000 số; `getsizeof(gen)` chỉ đo "bộ máy"
  sinh số (trạng thái + con trỏ), không chứa số nào.
* Lưu ý: `getsizeof` không đo sâu (đối tượng lồng trong list) — nhưng để so
  sánh tương đối hai cách lưu cùng dữ liệu thì hoàn toàn đủ.

**Độ phức tạp:** đo trong O(1) — hàm hệ thống trả kích thước đã biết sẵn.

</details>

<details>
<summary>✅ Bài 17: Đếm dòng trong file lớn (giả lập)</summary>

**Phân tích:** Đếm số dòng không rỗng trong file chỉ bằng generator +
`sum(1 for ...)`, không đọc cả file vào RAM. Với file thật hàng GB, đây là
cách duy nhất khả thi; ở đây giả lập bằng file 5 dòng.

**Ý tưởng:** Mỗi dòng không rỗng đóng góp `1` vào tổng; dòng rỗng (chỉ có
`\n` hoặc khoảng trắng) bị loại bởi `dong.strip() != ""`.

**Thuật toán:**
1. Tạo `du_lieu.txt` gồm 5 dòng số.
2. Reuse generator `doc_file` (bài 10).
3. `sum(1 for dong in doc_file(...) if dong.strip() != "")`.

**Code:**

```python
# Tạo file giả lập
with open("du_lieu.txt", "w", encoding="utf-8") as f:
    f.write("10\n20\n30\n40\n50\n")


def doc_file(ten):
    with open(ten, encoding="utf-8") as f:
        for dong in f:
            yield dong


so_dong = sum(1 for dong in doc_file("du_lieu.txt")
              if dong.strip() != "")
print("So dong khong rong:", so_dong)
```

**Giải thích code:**
* In ra: So dong khong rong: 5. ✔
* `sum(1 for ...)` là idiom đếm chuẩn Python: tổng của toàn số 1 = số dòng
  thỏa điều kiện; đọc cực nhanh sau khi đã quen mắt.
* Lỗi thường gặp: `sum(dong for ...)` — cộng chuỗi với số → `TypeError`.
  Phải là `sum(1 for ...)` (đếm) hoặc `sum(int(dong) ...)` (cộng giá trị).

**Độ phức tạp:** O(số dòng) thời gian, O(1) bộ nhớ — không phụ thuộc kích
thước file.

</details>

<details>
<summary>✅ Bài 18: Generator ghép đôi hai danh sách</summary>

**Phân tích:** Từ `a = ["A1","A2"]`, `b = ["B1","B2"]` sinh ra
A1, B1, A2, B2 — xen kẽ theo chỉ số. Giả định hai danh sách cùng độ dài
(đề bài ghi rõ), duyệt theo `range(len(a))`.

**Ý tưởng:** Mỗi vòng lặp `yield` hai lần: `a[i]` rồi `b[i]` — thứ tự yield
quyết định thứ tự xuất hiện trong kết quả.

**Thuật toán:**
1. Duyệt `i` từ 0 đến `len(a) - 1`.
2. `yield a[i]`, rồi `yield b[i]`.
3. In cách nhau bằng dấu cách.

**Code:**

```python
def ghep_doi(a, b):
    for i in range(len(a)):
        yield a[i]
        yield b[i]


a = ["A1", "A2"]
b = ["B1", "B2"]
for x in ghep_doi(a, b):
    print(x, end=" ")
```

**Giải thích code:**
* In ra: A1 B1 A2 B2. ✔
* Kỹ thuật "yield nhiều lần trong một vòng lặp" — một generator có thể sinh
  ra nhiều giá trị mỗi lần lặp, không giới hạn 1 yield / 1 vòng.
* Nếu hai danh sách khác độ dài: dùng `zip(a, b)` an toàn hơn
  (`for x, y in zip(a, b): yield x; yield y`) — dừng ở danh sách ngắn hơn,
  tránh `IndexError`.

**Độ phức tạp:** O(n) thời gian, O(1) bộ nhớ phụ.

</details>

<details>
<summary>✅ Bài 19: Tổng Fibonacci 50 số (chứng minh tiết kiệm nhớ)</summary>

**Phân tích:** Tính tổng 50 số Fibonacci đầu bằng `sum(fibonacci(50))` — không
list trung gian. Đáp án này còn **sửa một lỗi trong đề bài gốc**: đề ghi kết
quả `12586269024`, nhưng tổng 50 số đầu (F₀..F₄₉) đúng phải là `20365011073`
(đã kiểm chứng bằng cách chạy code).

**Ý tưởng:** Reuse generator `fibonacci(n)` (bài 8); `sum()` kéo toàn bộ;
chứng minh: với 50 số thì list vẫn ổn, nhưng với 5.000.000 số thì chỉ
generator mới sống sót.

**Thuật toán:**
1. Dùng nguyên generator `fibonacci(n)` đã viết.
2. `print("Tong 50 so Fibonacci dau:", sum(fibonacci(50)))`.

**Code:**

```python
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


print("Tong 50 so Fibonacci dau:", sum(fibonacci(50)))
```

**Giải thích code:**
* Chạy thật cho kết quả: `Tong 50 so Fibonacci dau: 20365011073`. ✔
* Vì sao đề gốc sai? `12586269024 = F₅₀ − 1` — đó là tổng 50 số **bắt đầu từ 1**
  (F₁..F₅₀), không phải dãy "0, 1, 1, 2..." như đề bài 8 định nghĩa. Bài học:
  **luôn chạy code để kiểm chứng**, đừng tin con số ghi sẵn — kể cả trong giáo
  trình này.
* Thử `sum(fibonacci(500000))` — vẫn chạy mượt vì generator; còn list 500.000
  số Fibonacci (số khổng lồ hàng trăm nghìn chữ số) sẽ nuốt RAM.

**Độ phức tạp:** O(n) thời gian, O(1) bộ nhớ (ngoài số nguyên lớn dần).

</details>

<details>
<summary>✅ Bài 20: Đọc log + thống kê lỗi (tổng hợp)</summary>

**Phân tích:** Bài tổng hợp: tạo file log 6 dòng (dạng `OK ...` / `LOI ...`),
reuse generator `doc_file` (bài 10), kết hợp idiom đếm `sum(1 for ...)`
(bài 17) và lọc tiền tố `startswith` (bài 11). Cả khóa Generator dồn vào một bài.

**Ý tưởng:** Generator đọc từng dòng; biểu thức đếm chỉ giữ dòng `LOI`;
kết quả duy nhất là một con số.

**Thuật toán:**
1. Tạo `he_thong.log` gồm 6 dòng, trong đó 3 dòng `LOI`.
2. `doc_file(ten_file)`: yield từng dòng đã strip.
3. `sum(1 for dong in doc_file(...) if dong.startswith("LOI"))`.

**Code:**

```python
# Tạo file log giả lập
with open("he_thong.log", "w", encoding="utf-8") as f:
    f.write("OK khoi dong\n")
    f.write("LOI ket noi database\n")
    f.write("OK tai du lieu\n")
    f.write("LOI ghi file that bai\n")
    f.write("OK gui bao cao\n")
    f.write("LOI email khong gui duoc\n")


def doc_file(ten):
    with open(ten, encoding="utf-8") as f:
        for dong in f:
            yield dong.strip()


so_loi = sum(1 for dong in doc_file("he_thong.log")
             if dong.startswith("LOI"))
print("So loi phat hien:", so_loi)
```

**Giải thích code:**
* In ra: So loi phat hien: 3. ✔
* Công thức "đọc lười + lọc + đếm trong một dòng" xử lý được log hàng GB —
  đúng cách các hệ thống thật thống kê lỗi mỗi ngày.

**Độ phức tạp:** O(số dòng) thời gian, O(1) bộ nhớ.

</details>



---

## ➡️ Điều hướng

**Vị trí:** `02-Thuat-Toan/Phan-1-Co-Ban/27-Generator/bai.md`

**Bài tiếp theo:** [Bài 28 — Decorator – Trang Trí Cho Hàm](../28-Decorator/bai.md)
