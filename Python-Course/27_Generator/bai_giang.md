# 🔄 Bài 27: Generator – Sinh Dữ Liệu "Từng Phần Một"

> 🎓 **Chương 5 – Lập trình hướng đối tượng & các công cụ nâng cao**

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

## 🏁 Kết thúc bài

🎉 **Giỏi lắm!** Bạn đã hiểu cách sinh dữ liệu "từng phần một" — công cụ sống còn để xử lý dãy lớn và file khổng lồ, kèm dãy Fibonacci, generator expression và so sánh bộ nhớ thực tế.

Nhân tiện: từ khóa `@` và khái niệm "trang trí" đã ló mặt từ bài 24 (`@dataclass`) — bài sau sẽ dạy bạn **tự tay viết decorator** để bọc thêm hành vi cho hàm:

👉 **[Bài 28: Decorator](../28_Decorator/bai_giang.md)**