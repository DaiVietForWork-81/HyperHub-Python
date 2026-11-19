# -*- coding: utf-8 -*-
"""Thêm cheatsheet vào các bài học chính."""
import re
from pathlib import Path

ROOT = Path(r"D:\HyperHub - HSG Tin")

# Nội dung cheatsheet cho từng bài
CHEATSHEETS = {
    "b16-String": """
---

## 📌 Cheatsheet — Xử lý chuỗi (Buổi 1)

| Thao tác | Cú pháp | Ví dụ | Kết quả |
|---|---|---|---|
| Tạo chuỗi | `\"...\"`, `'...'`, `\"\"\"...\"\"\"` | `\"Xin chao\"` | Chuỗi |
| Nối chuỗi | `+` | `\"A\" + \"B\"` | `\"AB\"` |
| Lặp chuỗi | `*` | `\"A\" * 3` | `\"AAA\"` |
| Xóa trắng 2 đầu | `.strip()` | `\"  a  \".strip()` | `\"a\"` |
| Xóa trắng trái/phải | `.lstrip()` / `.rstrip()` | | |
| Cắt theo dấu phân cách | `.split(sep)` | `\"a,b\".split(\",\")` | `[\"a\",\"b\"]` |
| Nối list thành chuỗi | `\"sep\".join(list)` | `\"-\".join(['a','b'])` | `\"a-b\"` |
| Thay thế | `.replace(cũ, mới)` | `\"ana\".replace(\"a\",\"o\")` | `\"ono\"` |
| Tìm vị trí đầu/cuối | `.find(x)` / `.rfind(x)` | | `-1` nếu thiếu |
| Kiểm tra chứa | `x in s` | `\"an\" in \"banana\"` | `True` |
| Đếm | `.count(x)` | `\"banana\".count(\"an\")` | `2` |
| Bắt đầu / kết thúc | `.startswith(x)` / `.endswith(x)` | Lọc file `.py` | |
| Toàn số / chữ / trắng | `.isdigit()` / `.isalpha()` / `.isspace()` | Kiểm tra nhập liệu | |
| Viết hoa đầu từ / câu | `.title()` / `.capitalize()` | | |
| Đệm 0 bên trái | `.zfill(n)` | `\"7\".zfill(3)` | `\"007\"` |
| Căn trái/phải/giữa | `.ljust(n)` / `.rjust(n)` / `.center(n)` | | |
| Truy cập / cắt | `s[i]` / `s[a:b:c]` | `s[::-1]` đảo | Chuỗi mới |
| Độ dài | `len(s)` | | |
| Ký tự ↔ mã | `ord(c)` / `chr(n)` | `ord(\"a\")` → `97` | |

**Ghi nhớ:** chuỗi BẤT BIẾN — mọi `replace/upper...` trả chuỗi MỚI (không sửa gốc); muốn sửa thì gán lại.

---

## 📌 Cheatsheet — Lưu ý cú pháp hay nhầm (Python)

| Sai | Đúng | Giải thích |
|---|---|---|
| `a^2 + b^2 == c^2` | `a**2 + b**2 == c**2` | `^` là XOR bitwise, `**` là lũy thừa |
| `10^8` | `10**8` | `10^8` = 2 (XOR) |
| `if -10^8 <= a <= 10^18` | `if -10**8 <= a <= 10**18` | `^` là XOR |
| `a^2` | `a**2` hoặc `a*a` | `^` là XOR bitwise |
| `a % 2 == 0` (check chẵn) | ✅ Đúng | Cách chuẩn kiểm tra chẵn/lẻ |

**Quy tắc:** Luôn dùng `**` cho lũy thừa, `*` cho nhân, `a*a` cho bình phương.

---

""",
    "b12-List": """
---

## 📌 Cheatsheet — Mảng / List (Buổi 1, 3)

| Thao tác | Cú pháp | Ví dụ | Kết quả |
|---|---|---|---|
| Tạo list | `[1, 2, 3]` / `list()` | `[1,2,3]` | List |
| Truy xuất đầu/cuối | `a[0]`, `a[-1]` | `a[0]`, `a[-1]` | Phần tử đầu/cuối |
| Slice | `a[start:stop:step]` | `a[1:4]`, `a[::-1]` | List mới |
| Thêm cuối | `append(x)` | `[1,2].append(3)` | `[1,2,3]` |
| Nối list | `extend(other)` | `[1,2].extend([3,4])` | `[1,2,3,4]` |
| Chèn | `insert(i, x)` | `[1,3].insert(1,2)` | `[1,2,3]` |
| Xóa theo giá trị | `remove(x)` | `[1,2].remove(2)` | `[1]` |
| Xóa theo vị trí | `pop(i)` | `[1,2].pop()` → `2` | Trả về giá trị |
| Xóa sạch | `clear()` | | |
| Tìm vị trí | `index(x)` | `[5,6,7].index(6)` → `1` | Lỗi nếu không có |
| Đếm | `count(x)` | `[1,1,2].count(1)` → `2` | |
| Sắp xếp tại chỗ | `sort(key=, reverse=)` | `[3,1,2].sort()` | Trả `None`, đổi gốc |
| Sắp xếp bản mới | `sorted(ds, key=, reverse=)` | `sorted(ds)` | List mới |
| Đảo tại chỗ | `reverse()` | `[1,2].reverse()` | `[2,1]` |
| Đảo bản mới | `ds[::-1]` | | List mới |
| Copy an toàn | `ds.copy()` / `list(ds)` / `ds[:]` | `b = a.copy()` | Tránh bẫy `b = a` |
| Kiểm tra thuộc | `x in ds` | `3 in [1,2,3]` | `True` (O(n)) |
| Nối list | `a + b` | `[1]+[2]` → `[1,2]` | |
| Lặp list | `a * n` | `[1]*3` → `[1,1,1]` | |
| Thống kê | `len/min/max/sum` | `sum([1,2,3])` → `6` | Chỉ list số |
| Duyệt kèm chỉ số | `enumerate(ds)` | `enumerate(ds, start=1)` | Bắt đầu từ 1 |
| Duyệt song song | `zip(d1, d2)` | `zip(a, b)` | Cặp phần tử |

**Ghi nhớ quan trọng:**
- `sort()` trả `None` (đổi gốc!), `sorted()` trả list mới
- Copy an toàn: `ds.copy()` / `list(ds)` / `ds[:]` — **ĐỪNG** dùng `b = a`
- `x in list` là O(n); `x in set/dict` là O(1)
- `pop(0)` trên list là O(n) — dùng `deque.popleft()` cho queue

---

## ⚡ Kỹ thuật 2 con trỏ (Two Pointers) — Buổi 3

```python
# Dùng khi mảng ĐÃ SẮP XẾP hoặc cần tìm cặp thỏa điều kiện
left, right = 0, n - 1
while left < right:
    s = a[left] + a[right]
    if s == target: ...
    elif s < target: left += 1
    else: right -= 1
```

| Khuôn mẫu | Khi dùng |
|---|---|
| Hai con trỏ ngược (`l, r = 0, n-1`) | Dãy sort, tìm cặp/tổng |
| Cửa sổ trượt (`l = 0; for r in range(n): while đk xấu: l += 1`) | Đoạn liên tiếp thỏa điều kiện |
| Tiền tố + dict (`thay[P[i]]` tra "tổng gặp trước") | Đoạn tổng K (kể cả số âm) |

**Nhận diện:** đề có "liên tiếp/đoạn con" + "dài nhất/nhỏ nhất/đếm" → nghĩ ngay kỹ thuật dãy. Cửa sổ trượt chỉ chuẩn khi điều kiện **đơn điệu** (thêm phần tử không làm điều kiện tốt lên) — số âm phá điều kiện này.

---

## 📌 Cheatsheet — Mảng lớn (n ≤ 10⁶)

| Vấn đề | Giải pháp |
|---|---|
| Mảng index out of range | Khai báo size = n + 6 hoặc 1_000_006 |
| Đệ quy Fibonacci → Stack overflow | Dùng vòng lặp hoặc mảng DP |
| Kiểm tra SNT lặp nhiều lần | Dùng Sieve một lần, truy vấn O(1) |
| `a^2` trong Python là XOR, không phải bình phương | Dùng `a**2` hoặc `a*a` |

---

""",
    "b33-Hai-Con-Tro": """
---

## 📌 Cheatsheet — Template hai con trỏ & tổng tiền tố

| Khuôn mẫu | Template ngắn | Dùng khi |
|---|---|---|
| Hai con trỏ ngược | `l, r = 0, n-1` tiến vào nhau | dãy sort, cặp/tổng |
| Cửa sổ trượt | `l = 0; for r in range(n): while đk xấu: l += 1` | đoạn liên tiếp thỏa điều kiện |
| Tiền tố | `P[0]=0; P[i+1]=P[i]+a[i]` → `tong(l,r)=P[r+1]-P[l]` | hỏi tổng đoạn nhiều lần |
| Tiền tố + dict | `thay[P[i]]` tra "tổng gặp trước" | đoạn tổng K (kể cả số âm) |

**Nhận diện:** đề có chữ "liên tiếp/đoạn con" + "dài nhất/nhỏ nhất/đếm" → nghĩ ngay kỹ thuật dãy. Cửa sổ trượt chỉ chuẩn khi điều kiện **đơn điệu** (thêm phần tử không làm điều kiện tốt lên) — số âm phá điều kiện này.

---

## 📌 Cheatsheet — Kỹ thuật mảng hiệu (Difference Array) / Mảng hiệu phân

```python
# Cập nhật đoạn [l, r] += v trong O(1)
d[l] += v
d[r + 1] -= v

# Cộng dồn để lấy mảng kết quả
ra, s = [], 0
for i in range(n):
    s += d[i]
    ra.append(s)
```

Mỗi truy vấn O(1) + cộng dồn cuối O(n) → O(n+q) thay vì O(n·q).

---

""",
    "b36-Toan-Hoc-So-Hoc": """
---

## 📌 Cheatsheet — Sàng, Euclid, lũy thừa, Fermat, tổ hợp

| Kỹ thuật | Template | Ví dụ |
|---|---|---|
| Sàng Eratosthenes | `s = [True]*(n+1); for i in range(2, isqrt(n)+1):` | Liệt kê nguyên tố ≤ 10⁶ |
| Kiểm tra nguyên tố | Miller-Rabin (n ≤ 10¹⁸) | `pow(a, n-1, n) == 1` |
| GCD | `def gcd(a,b): return gcd(b, a%b) if b else a` | `gcd(48, 18)` → 6 |
| Lũy thừa nhanh | `pow_mod(x, n, m)` chia đôi mũ | `pow(x, n, m)` có sẵn |
| Fermat nhỏ | `a^(p-1) ≡ 1 (mod p)` | Nghịch đảo modulo |
| Tổ hợp C(n,k) mod p | `fact[n] * invfact[k] * invfact[n-k] % p` | `n, k ≤ 10⁶` |

**Ghi nhớ:** Python có sẵn `math.gcd`, `math.comb`, `pow(x, n, m)` — thi dùng luôn, tự cài chỉ để hiểu bản chất.

---

## 📌 Cheatsheet — Số chính phương

```python
import math
def is_square(n):
    r = int(math.isqrt(n))  # Python 3.8+
    return r * r == n
# hoặc không dùng math:
x = 0
while x * x <= n:
    if x * x == n: return True
    x += 1
```

---

## 📌 Cheatsheet — Fibonacci lặp (O(n), không đệ quy)

```python
# Cách 1: 2 biến (tối ưu bộ nhớ)
a, b = 0, 1
for _ in range(n):
    a, b = b, a + b
print(a)  # F(n)

# Cách 2: Mảng (khi cần truy xuất nhiều lần, n ≤ 10^6)
f = [0] * 1_000_006
f[1] = f[2] = 1
for i in range(3, n+1):
    f[i] = f[i-1] + f[i-2]
```

---

## 📌 Cheatsheet — Kiểm tra SNT (3 mức độ)

```python
# Cách 1: O(n) - cơ bản
def is_prime_basic(n):
    if n < 2: return False
    for i in range(2, n):
        if n % i == 0: return False
    return True

# Cách 2: O(√n) - TỐI ƯU (cần nhớ!)
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

# Cách 3: Sieve (Eratosthenes) - cho nhiều truy vấn, n ≤ 10^6
N = 1_000_006
is_prime = [True] * N
is_prime[0] = is_prime[1] = False
for i in range(2, int(N**0.5)+1):
    if is_prime[i]:
        for j in range(i*i, N, i):
            is_prime[j] = False
```

---

## 📌 Cheatsheet — Phân tích thừa số nguyên tố

```python
x = int(input())
y = 1
d = 2
while d * d <= x:
    cnt = 0
    while x % d == 0:
        x //= d
        cnt += 1
    if cnt % 2 == 1:      # số mũ lẻ → nhân vào kết quả
        y *= d
    d += 1
if x > 1:                 # thừa số nguyên tố lớn cuối cùng
    y *= x
print(y)
```

---

""",
    "b25-Do-Phuc-Tap": """
---

## 📌 Cheatsheet — Bảng chọn thuật toán theo ràng buộc & độ phức tạp thao tác

| n tối đa | Độ phức tạp khả thi | Gợi ý kỹ thuật |
|---|---|---|
| ≤ 10 | O(n!), O(2ⁿ·n) | hoán vị, vét cạn hết |
| ≤ 20–25 | O(2ⁿ), O(n·2ⁿ) | bitmask, quay lui + tỉa |
| ≤ 500 | O(n³) | DP 3 chiều, Floyd |
| ≤ 5.000 | O(n²) | vét cạn cặp, DP 2 chiều |
| ≤ 10⁵–10⁶ | O(n log n) | sort, nhị phân, heap |
| ≤ 10⁷–10⁸ | O(n) | một lượt, đếm, hai con trỏ |
| ≤ 10¹² | O(√n) | số học, kiểm tra ước |
| ≤ 10¹⁸ | O(log n) | lũy thừa nhanh, nhị phân đáp số |

**Độ phức tạp thao tác Python hay quên:**
- `x in list` O(n) — `x in set/dict` O(1)
- `pop(0)` trên list O(n) — dùng `deque`
- Nối chuỗi trong vòng lặp O(n²) — dùng list + `join`
- `in` chuỗi con O(n·m) — regex/KMP khi lớn

---

""",
    "b31-De-Quy": """
---

## 📌 Cheatsheet — Template đệ quy & memoization

| Khuôn mẫu | Cú pháp |
|---|---|
| Khung chuẩn | `def f(n): if base: return ...; return combine(f(n-1))` |
| Memo thủ công | `if n in nho: return nho[n]` trước khi tính |
| Memo 1 dòng | `from functools import lru_cache` + `@lru_cache(maxsize=None)` |
| Nới giới hạn | `import sys; sys.setrecursionlimit(300000)` |

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def f(n):
    ...
```

**Quy tắc sống còn:** (1) base đúng và "bao" biên, (2) mỗi gọi phải tiến gần base; bài con lặp lại → memo; sâu tuyến tính lớn → vòng lặp.

---

## 📌 Cheatsheet — Fibonacci lặp (O(n), không đệ quy)

```python
# Cách 1: 2 biến (tối ưu bộ nhớ)
a, b = 0, 1
for _ in range(n):
    a, b = b, a + b
print(a)  # F(n)

# Cách 2: Mảng (khi cần truy xuất nhiều lần, n ≤ 10^6)
f = [0] * 1_000_006
f[1] = f[2] = 1
for i in range(3, n+1):
    f[i] = f[i-1] + f[i-2]
```

---

""",
    "b05-Toan-Tu": """
---

## 📌 Cheatsheet — Toán tử & thứ tự ưu tiên

| Nhóm | Toán tử | Ví dụ | Ghi chú |
|---|---|---|---|
| Số học | `+ - * /` | `7 / 2` → `3.5` | `/` luôn ra `float` |
| Số học | `// % **` | `7 // 2`→`3`; `7 % 2`→`1`; `2 ** 10`→`1024` | chia nguyên, dư, lũy thừa |
| So sánh | `== != < <= > >=` | `3 != 4` → `True` | Trả về `bool` |
| Logic | `and or not` | `a > 0 and a < 10` | Học đủ bảng chân trị |
| Gán kết hợp | `+= -= *= //= %=` | `x += 1` | Ngắn cho `x = x + 1` |
| `in` | Kiểm tra thuộc | `\"a\" in \"cat\"` → `True` | Chuỗi, list, dict... |
| `is` | Cùng đối tượng? | `a is b` | Khác `==` (so giá trị) |

**Thứ tự ưu tiên (cao → thấp):** `**` → `* / // %` → `+ -` → so sánh → `not` → `and` → `or`. Không chắc thì cứ thêm ngoặc tròn.

---

## 📌 Cheatsheet — Cú pháp hay nhầm (Python)

| Sai | Đúng | Giải thích |
|---|---|---|
| `a^2 + b^2 == c^2` | `a**2 + b**2 == c**2` | `^` là XOR bitwise, `**` là lũy thừa |
| `10^8` | `10**8` | `10^8` = 2 (XOR) |
| `if -10^8 <= a <= 10^18` | `if -10**8 <= a <= 10**18` | `^` là XOR |
| `a^2` | `a**2` hoặc `a*a` | `^` là XOR bitwise |
| `a % 2 == 0` (check chẵn) | ✅ Đúng | Cách chuẩn kiểm tra chẵn/lẻ |

**Quy tắc:** Luôn dùng `**` cho lũy thừa, `*` cho nhân, `a*a` cho bình phương.

---

""",
    "b07-Cau-Lenh-If": """
---

## 📌 Cheatsheet — Rẽ nhánh & Logic điều kiện

| Cú pháp | Ý nghĩa | Ví dụ |
|---|---|---|
| `if đk:` | Chạy khi đúng | `if x > 0:` |
| `elif đk:` | Kiểm tra tiếp | Nhiều mức xếp loại |
| `else:` | Còn lại | Không cần điều kiện |
| Giá trị đúng/sai | Bảng truthiness | `if ds:` — list rỗng là sai |
| Ngoặc đơn dư | OK nhưng không cần | `if (x > 0):` |
| Chuỗi so sánh | Theo từ điển | `\"a\" < \"b\"` → `True` |
| So sánh chuỗi (chained) | `a < b < c` | `0 < x < 10` |
| Ba ngôi một dòng | `X if đk else Y` | `\"dương\" if x > 0 else \"âm\"` |

---

## 📌 Cheatsheet — Cú pháp hay nhầm (Logic điều kiện)

| Sai | Đúng | Giải thích |
|---|---|---|
| `if -10^8 <= a <= 10^18` | `if -10**8 <= a <= 10**18` | `^` là XOR |
| `a^2 + b^2 == c^2` | `a**2 + b**2 == c**2` | `^` là XOR |
| `a > 0 & b > 0` | `a > 0 and b > 0` | `&` là bitwise AND |
| `a == b or c` | `(a == b) or c` | `==` ưu tiên hơn `or` |

---

""",
}

def add_cheatsheet_to_file(folder_name, cheatsheet_content):
    """Thêm cheatsheet vào file bài học (chèn trước Điều hướng)."""
    f = ROOT / folder_name / "bai.md"
    if not f.exists():
        print(f"  SKIP: {folder_name} not found")
        return False
    
    text = f.read_text(encoding="utf-8")
    
    # Check if cheatsheet already exists
    if "## 📌 Cheatsheet" in text:
        print(f"  SKIP: {folder_name} already has cheatsheet")
        return False
    
    # Find the navigation section
    nav_pattern = r"## ➡️ Điều hướng"
    match = re.search(nav_pattern, text)
    if not match:
        print(f"  ERROR: {folder_name} - no navigation section found")
        return False
    
    insert_pos = match.start()
    new_text = text[:insert_pos] + cheatsheet_content + "\n\n" + text[insert_pos:]
    
    f.write_text(new_text, encoding="utf-8", newline="\n")
    print(f"  OK: {folder_name}")
    return True

def main():
    print("Adding cheatsheets to lesson files...")
    for folder, content in CHEATSHEETS.items():
        add_cheatsheet_to_file(folder, content)
    print("Done!")

if __name__ == "__main__":
    main()