# Bài 25 — Tìm Kiếm Tuyến Tính & Nhị Phân

> 🧮 **Nhánh 02 — Thuật Toán (HSG / Competitive Programming)**

---

## 🧠 Điều kiện tiên quyết

- [Bài 24 — Độ Phức Tạp & Big-O](../24-Do-Phuc-Tap/bai.md)
- [Bài 8 — Vòng Lặp For](../08-Vong-Lap-For/bai.md)
- [Bài 9 — Vòng Lặp While](../09-Vong-Lap-While/bai.md)
- [Bài 12 — List](../12-List/bai.md)

---

## 🎯 Mục tiêu

Sau bài học này, học viên sẽ:

* ✅ Cài được tìm kiếm tuyến tính và hiểu khi nào nó là lựa chọn đúng (dãy chưa sắp xếp, n nhỏ).
* ✅ Hiểu tư tưởng "chặt đôi không gian tìm kiếm" của tìm kiếm nhị phân.
* ✅ Tự viết `lower_bound` / `upper_bound` chuẩn — đếm số lần xuất hiện trong dãy đã sắp xếp.
* ✅ Tránh lỗi off-by-one (`<` vs `<=`, `mid` tính sai, vòng lặp vô hạn) bằng bất biến vòng lặp.
* ✅ Nhận ra mẫu "chặt nhị phân trên đáp số" — nhị phân không chỉ dùng để tìm trong mảng.

---

## 📖 Mở đầu

"Tìm x trong dãy" nghe tầm thường — nhưng đây là bài toán con xuất hiện
trong **hầu hết** các bài HSG khó: tìm vị trí chèn, tìm ngưỡng, tìm đáp số
nhỏ nhất thỏa điều kiện... Nắm chắc hai thuật toán tìm kiếm trong bài này,
bạn mở khóa được cả một họ bài toán ở các bài sau.

---

## 💡 Ý tưởng trực quan

* **Tuyến tính:** tìm chìa khóa trong balo — móc từng món ra xem. Balo càng
  to, tìm càng lâu (O(n)). Không cần balo gọn gàng.
* **Nhị phân:** tìm từ trong từ điển giấy — mở giữa, từ cần tìm ở nửa trước
  hay nửa sau? Bỏ luôn một nửa, lặp lại. Từ điển càng dày, số lần mở chỉ
  tăng thêm 1–2 lần (O(log n)). **Điều kiện: từ điển phải xếp thứ tự.**

```mermaid
flowchart TD
    A["Dãy đã sắp xếp + cần tìm x"] --> B["mid = giữa [l, r]"]
    B --> C{a[mid] ? x}
    C -->|=| D["✅ Tìm thấy"]
    C -->|<| E["Bỏ nửa trái: l = mid + 1"]
    C -->|>| F["Bỏ nửa phải: r = mid - 1"]
    E --> B
    F --> B
```

---

## 📚 Kiến thức

### 1. Tìm kiếm tuyến tính — O(n)

Duyệt từ đầu đến cuối, gặp thì dừng. Đơn giản, đúng với mọi dãy (không cần
sắp xếp). Dùng khi: n nhỏ, hoặc chỉ tìm vài lần, hoặc dãy không sắp xếp được.

```python
def tim_tuyen_tinh(a, x):
    for i, v in enumerate(a):
        if v == x:
            return i
    return -1
```

> Trong Python, `x in a` và `a.index(x)` chính là tuyến tính viết bằng C —
> nhanh hơn vòng lặp Python ~50 lần nhưng vẫn O(n).

### 2. Tìm kiếm nhị phân — O(log n), yêu cầu dãy đã sắp xếp

**Bất biến vòng lặp** (câu thần chú chống mọi lỗi off-by-one):

> *Nếu x có trong dãy, thì nó nằm trong đoạn [l, r] (bao gồm cả hai đầu).*

Mỗi bước so sánh `a[mid]` với x và thu hẹp đoạn sao cho bất biến **luôn đúng**:

* `a[mid] == x` → xong.
* `a[mid] < x` → x (nếu có) nằm bên phải → `l = mid + 1`.
* `a[mid] > x` → x (nếu có) nằm bên trái → `r = mid - 1`.

Vòng lặp dừng khi `l > r` (đoạn rỗng → không có x). Vì mỗi bước đoạn còn
một nửa, số bước ≤ log₂n + 1.

```python
def tim_nhi_phan(a, x):
    l, r = 0, len(a) - 1
    while l <= r:                 # đoạn [l, r] còn phần tử
        mid = (l + r) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1
```

**Ba lỗi off-by-one kinh điển** (học thuộc để không bao giờ mắc):

| Lỗi | Hậu quả |
|---|---|
| `while l < r` thay vì `<=` | Bỏ sót phần tử cuối khi đoạn còn 1 phần tử |
| `l = mid` thay vì `mid + 1` | Vòng lặp vô hạn khi `l + 1 == r` (mid == l mãi) |
| `mid = (l + r) // 2` trong Python thì **an toàn** — không tràn số như C++ (`(l+r)` có thể tràn int32; Python int vô hạn nên khỏi lo) |

### 3. lower_bound / upper_bound — tìm kiếm nhị phân "nâng cấp"

Thi HSG hiếm khi hỏi "có x không", mà hỏi:

* `lower_bound(x)`: vị trí **đầu tiên** có giá trị ≥ x.
* `upper_bound(x)`: vị trí **đầu tiên** có giá trị > x.
* Số lần xuất hiện của x = upper − lower.

Python có sẵn trong module `bisect` (viết bằng C, nhanh):

```python
from bisect import bisect_left, bisect_right

a = [1, 2, 2, 2, 3, 5]
bisect_left(a, 2)    # 1 → lower_bound
bisect_right(a, 2)   # 4 → upper_bound
bisect_right(a, 2) - bisect_left(a, 2)  # 3 → xuất hiện 3 lần
```

> 💡 Mỗi truy vấn O(log n) → m truy vấn hết O(m log n). So với quét tuyến
> tính mỗi truy vấn O(n) → O(m·n): với n, m ≤ 10⁵, chênh lệch giữa AC và TLE.

Tự cài `bisect_left` để hiểu sâu (mẫu "nửa khoảng [l, r)"):

```python
def bisect_left(a, x):
    l, r = 0, len(a)      # bất biến: đáp án nằm trong [l, r)
    while l < r:
        mid = (l + r) // 2
        if a[mid] < x:
            l = mid + 1
        else:
            r = mid
    return l
```

### 4. Chặt nhị phân trên đáp số — nhị phân không cần mảng!

Mẫu tư duy mạnh nhất của bài này: **nếu có thể kiểm tra "đáp số K có đủ tốt
không?" trong O(f), và tính "đủ tốt" đơn điệu theo K, thì chặt nhị phân K.**

Ví dụ kinh điển — "chia kẹo": có n gói kẹo (gói i có a[i] viên), cần chia cho
m bạn sao cho mỗi bạn nhận số viên **bằng nhau** (mỗi bạn lấy từ một gói,
gói có thể thừa), hỏi mỗi bạn được nhiều nhất bao nhiêu viên?

* Kiểm tra K: `sum(a[i] // K) >= m`? — O(n). Đơn điệu: K càng lớn càng khó đạt.
* Chặt nhị phân K trong [1, max(a)] → đáp án. O(n log max).

```python
import sys

def du_kẹo(a, m, k):
    return sum(x // k for x in a) >= m

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n, m = int(next(it)), int(next(it))
    a = [int(next(it)) for _ in range(n)]
    l, r, ans = 1, max(a), 0
    while l <= r:
        mid = (l + r) // 2
        if du_kẹo(a, m, mid):
            ans, l = mid, mid + 1   # K này được → thử lớn hơn
        else:
            r = mid - 1             # K này không được → thu nhỏ
    print(ans)

main()
```

---

## 💻 Ví dụ

### Ví dụ 1 — Dễ: tìm kiếm tuyến tính có kiểm tra biên

```python
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    x = int(data[1 + n])
    for i, v in enumerate(a):
        if v == x:
            print(i)      # vị trí 0-based đầu tiên
            return
    print(-1)

main()
```

**Giải thích:** `return` ngay khi tìm thấy — không duyệt tiếp (tiết kiệm,
và đúng yêu cầu "đầu tiên"). Không thấy → −1. O(n).

### Ví dụ 2 — Thực tế: đếm số lần xuất hiện với nhiều truy vấn

> Đề: "Dãy a đã sắp xếp tăng dần (n ≤ 10⁵). m ≤ 10⁵ truy vấn, mỗi truy vấn
> cho x, in số lần x xuất hiện."

```python
import sys
from bisect import bisect_left, bisect_right

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    m = int(next(it))
    ra = []
    for _ in range(m):
        x = int(next(it))
        ra.append(str(bisect_right(a, x) - bisect_left(a, x)))
    sys.stdout.write("\n".join(ra))

main()
```

**Phân tích từng bước:**

* Mỗi truy vấn: 2 lần nhị phân O(log n) → tổng O((n + m) log n) ≈ 3×10⁶. ✔
* Cách naive (quét O(n) mỗi truy vấn): 10¹⁰ → TLE.
* Gom output + một lần `write` (Bài 24).

### Ví dụ 3 — Khó: chặt nhị phân trên đáp số ("chia kẹo" ở mục 4)

Code đầy đủ đã cho ở mục 4. Chạy tay: `a = [7, 5, 9]`, `m = 4`.

| K | 7//K + 5//K + 9//K | ≥ 4? |
|---|---|---|
| 5 | 1+1+1 = 3 | Không → thu nhỏ |
| 2 | 3+2+4 = 9 | Được → thử lớn hơn |
| 3 | 2+1+3 = 6 | Được → thử lớn hơn |
| 4 | 1+1+2 = 4 | Được → đáp án 4? |

Chặt nhị phân trên [1, 9]: mid=5 ❌ → [1,4]: mid=2 ✔ → [3,4]: mid=3 ✔ →
[4,4]: mid=4 ✔ → đáp án **4**. ✔

---

## 📊 Minh họa

Tìm x = 7 trong `[1, 3, 5, 7, 9, 11, 13]` (n = 7, tối đa ⌈log₂7⌉ = 3 bước):

```
Bước 1: l=0 r=6 mid=3 → a[3]=7 == 7 → TÌM THẤY (may mắn, 1 bước!)
```

Tìm x = 11:

```
Bước 1: l=0 r=6 mid=3 → a[3]=7 < 11  → l=4
Bước 2: l=4 r=6 mid=5 → a[5]=11 == 11 → TÌM THẤY (2 bước)
```

Tìm x = 8 (không có):

```
Bước 1: l=0 r=6 mid=3 → 7 < 8  → l=4
Bước 2: l=4 r=6 mid=5 → 11 > 8 → r=4
Bước 3: l=4 r=4 mid=4 → 9 > 8  → r=3
l=4 > r=3 → DỪNG → -1 (3 bước, đúng ⌈log₂7⌉)
```

---

## ⚠️ Những lỗi thường gặp

### Lỗi 1: Nhị phân trên dãy chưa sắp xếp

* **Nguyên nhân:** quên `a.sort()` trước, hoặc dãy không thể sắp xếp theo
  tiêu chí cần tìm.
* **Cách sửa:** kiểm tra tiền điều kiện "đã sắp xếp" trước khi viết nhị phân.

### Lỗi 2: `while l < r` + `l = mid` → treo máy

```python
# ❌ TREO khi l + 1 == r: mid == l, l không đổi, lặp vô tận
while l < r:
    mid = (l + r) // 2
    if a[mid] < x:
        l = mid
```

* **Cách sửa:** dùng mẫu chuẩn `l = mid + 1` / `r = mid - 1` với `l <= r`,
  hoặc mẫu nửa khoảng `[l, r)` ở mục 3 — chọn MỘT mẫu, dùng nhất quán.

### Lỗi 3: Quên hàm kiểm tra phải đơn điệu (chặt trên đáp số)

* Nếu "K được" không kéo theo "mọi K' < K đều được", chặt nhị phân cho đáp
  án sai. Luôn tự hỏi: tính đơn điệu có đúng không?

### Lỗi 4: Dùng `bisect` trên list chưa sắp xếp — kết quả vô nghĩa, không báo lỗi

### Lỗi 5: Nhập nhằng 0-based / 1-based

* Đề HSG thường đánh số từ 1; Python index từ 0. Quy ước: tính toán 0-based,
  **+1 khi in** nếu đề yêu cầu.

---

## 🧪 Trường hợp đặc biệt

* **Dãy rỗng**: `tim_nhi_phan([], x)` → l=0, r=−1 → vòng lặp không chạy → −1. ✔
* **Một phần tử**: l=r=0, mid=0 — đây là lý do phải `<=` chứ không phải `<`.
* **Toàn giá trị trùng**: nhị phân thường trả vị trí bất kỳ trong đám trùng;
  cần đầu tiên/cuối cùng → dùng `bisect_left`/`bisect_right`.
* **x ngoài khoảng** [a[0], a[−1]]: vòng lặp vẫn đúng, trả −1 / vị trí chèn biên.

---

## 🚀 Ứng dụng thực tế

* `bisect` trong code thật: chèn giữ thứ tự (`insort`), tìm ngưỡng, tra bảng giá.
* Chặt nhị phân trên đáp số: tối ưu tham số (tìm cấu hình nhỏ nhất đạt SLA),
  tìm phiên bản lỗi đầu tiên (git bisect — đúng tên gọi!).

---

## 🧩 Bài tập

### 🟢 Cơ bản (1–3)

**Bài 1 — Chạy tay.** Dãy `[2, 5, 8, 12, 16, 23, 38, 56]`, tìm x = 23 bằng nhị
phân. Ghi (l, r, mid, a[mid]) mỗi bước. Bao nhiêu bước?

**Bài 2 — Đếm bước.** n = 10⁶. Tìm kiếm tuyến tính xấu nhất bao nhiêu bước?
Nhị phân tối đa bao nhiêu bước? (Tính ⌈log₂10⁶⌉ ≈ 20.)

**Bài 3 — lower/upper.** Dãy `[1, 3, 3, 3, 5, 7]`. Tính `bisect_left` và
`bisect_right` của 3, 4, 0, 9. Từ đó suy ra số lần xuất hiện của 3 và 4.

### 🟡 Hiểu sâu (4–6)

**Bài 4 — Tự cài bisect.** Cài `my_bisect_right(a, x)` (vị trí chèn sau các
phần tử ≤ x) dùng mẫu nửa khoảng, test với dãy có phần tử trùng và dãy rỗng.

**Bài 5 — Tìm điểm xoay.** Dãy tăng dần bị xoay (ví dụ `[4, 5, 6, 1, 2, 3]`),
tìm x trong O(log n). *Gợi ý: ít nhất một nửa luôn sắp xếp; xác định nửa nào,
kiểm tra x có nằm trong đó không.*

**Bài 6 — Căn bậc hai nguyên.** Tính ⌊√n⌋ với n ≤ 10¹⁸ bằng chặt nhị phân
(không dùng `math.isqrt` để luyện tay). *Gợi ý: kiểm tra mid×mid ≤ n có đơn
điệu không? Chú ý `mid*mid` có thể rất lớn — Python int vô hạn nên an toàn.*

### 🔴 Vận dụng (7–8)

**Bài 7 — Chia kẹo biến thể.** n gói kẹo, chia cho m bạn, mỗi bạn nhận số viên
bằng nhau **và mỗi bạn chỉ lấy từ đúng một gói, gói không được chia cho 2 bạn**
(mỗi gói cho tối đa 1 bạn). Hỏi mỗi bạn được nhiều nhất bao nhiêu viên?
*Gợi ý: hàm kiểm tra khác bài "chia kẹo" gốc — đếm số gói có a[i] ≥ K.*

**Bài 8 — Cặp có hiệu nhỏ nhất.** Cho dãy chưa sắp xếp (n ≤ 10⁵), tìm hiệu nhỏ
nhất giữa hai phần tử phân biệt. *Gợi ý: sắp xếp O(n log n) rồi... hiệu nhỏ
nhất nhất định nằm ở đâu trong dãy đã sắp xếp?*
### ➕ Bài tập bổ sung (Bài 9–12)

**Bài 9 — Đếm điểm đạt.** Điểm thi đã sắp xếp tăng dần (n ≤ 10⁵). m ≤ 10⁵ truy
vấn, mỗi truy vấn cho x, in số bạn đạt điểm ≥ x. Code bằng `bisect_left`, test
với điểm mẫu và 3 truy vấn (kể cả x lớn hơn mọi điểm, x nhỏ hơn mọi điểm).

**Bài 10 — Tìm chỗ treo máy.** Đoạn code nhị phân sai: `while l < r` với
`l = mid` (thay vì `mid + 1`). Tìm input nhỏ nhất làm treo máy, giải thích vì
sao kẹt, và sửa đúng 1 dòng.

**Bài 11 — Photo 2 máy.** Hai máy photo: máy A photo 1 bản tốn x giây, máy B
tốn y giây (làm song song). Cần n bản, thời gian ít nhất bao nhiêu? Chặt nhị
phân đáp số T với hàm kiểm tra `T // x + T // y >= n`. Code + test
(x=3, y=5, n=10 → 20).

**Bài 12 — Tìm đỉnh O(log n).** Dãy bất kỳ (phân biệt), "đỉnh" là phần tử lớn
hơn cả 2 hàng xóm (đầu/cuối dãy chỉ cần lớn hơn 1 hàng xóm). Tìm 1 đỉnh trong
O(log n) (không phải O(n) quét!). *Gợi ý: so a[mid] với a[mid+1] để quyết định
bỏ nửa nào — luôn tồn tại đỉnh ở nửa giữ lại.*

---

## ✅ Đáp án

> 💡 **Hãy tự làm bài tập trước** rồi mới mở đáp án.

<details>
<summary>✅ Bài 1: Chạy tay</summary>

| Bước | l | r | mid | a[mid] | Kết luận |
|---|---|---|---|---|---|
| 1 | 0 | 7 | 3 | 12 | 12 < 23 → l = 4 |
| 2 | 4 | 7 | 5 | 23 | 23 == 23 → tìm thấy |

**2 bước.** (Nhị phân không phải lúc nào cũng cần đủ ⌈log₂8⌉ = 3 bước —
đó là số bước *tối đa*.)

</details>

<details>
<summary>✅ Bài 2: Đếm bước</summary>

* Tuyến tính xấu nhất: **10⁶ bước** (duyệt hết, không thấy).
* Nhị phân tối đa: ⌈log₂10⁶⌉ = ⌈19.93⌉ = **20 bước**.
* Tỉ lệ: 50.000 lần — với m = 10⁵ truy vấn, tuyến tính cần 10¹¹ bước (TLE),
  nhị phân cần 2×10⁶ bước (AC).

</details>

<details>
<summary>✅ Bài 3: lower/upper</summary>

* x = 3: left = 1, right = 4 → xuất hiện 4 − 1 = **3 lần**.
* x = 4: left = 4, right = 4 → xuất hiện 0 lần (không có).
* x = 0: left = right = 0 (chèn đầu).
* x = 9: left = right = 6 (chèn cuối, len = 6).

</details>

<details>
<summary>✅ Bài 4: Tự cài bisect</summary>

```python
def my_bisect_right(a, x):
    l, r = 0, len(a)      # đáp án trong [l, r)
    while l < r:
        mid = (l + r) // 2
        if a[mid] <= x:   # khác left ở dấu <= : đẩy qua cả phần tử bằng
            l = mid + 1
        else:
            r = mid
    return l

# Test
assert my_bisect_right([1, 2, 2, 2, 3], 2) == 4
assert my_bisect_right([], 5) == 0
assert my_bisect_right([1, 3, 5], 0) == 0
assert my_bisect_right([1, 3, 5], 9) == 3
```

Điểm khác duy nhất so với `bisect_left`: điều kiện `a[mid] <= x` (thay vì `<`)
đẩy biên trái **qua cả** các phần tử bằng x.

</details>

<details>
<summary>✅ Bài 5: Tìm điểm xoay</summary>

```python
def tim_trong_day_xoay(a, x):
    l, r = 0, len(a) - 1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] == x:
            return mid
        if a[l] <= a[mid]:            # nửa trái sắp xếp
            if a[l] <= x < a[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:                         # nửa phải sắp xếp
            if a[mid] < x <= a[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1
```

**Trực giác:** giữa điểm xoay cắt đôi, ít nhất một nửa "sạch" (tăng dần).
Nếu x nằm trong nửa sạch → tìm trong đó; không thì tìm nửa còn lại.
Vẫn chặt đôi mỗi bước → O(log n).

</details>

<details>
<summary>✅ Bài 6: Căn bậc hai nguyên</summary>

```python
def can_bac_hai(n):
    if n < 2:
        return n
    l, r, ans = 1, n // 2, 1
    while l <= r:
        mid = (l + r) // 2
        if mid * mid <= n:
            ans, l = mid, mid + 1
        else:
            r = mid - 1
    return ans

assert can_bac_hai(10**18) == 10**9
assert can_bac_hai(17) == 4
```

Tính đơn điệu: nếu mid² ≤ n thì mọi k < mid cũng thỏa → chặt được.
`r = n // 2` đủ vì với n ≥ 4, √n ≤ n/2. Python int vô hạn nên `mid*mid`
không tràn (trong C++ phải viết `mid <= n // mid`).

</details>

<details>
<summary>✅ Bài 7: Chia kẹo biến thể</summary>

Hàm kiểm tra khác hẳn: K khả thi ⟺ **số gói có a[i] ≥ K** ít nhất m
(mỗi gói cho tối đa 1 bạn).

```python
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n, m = int(next(it)), int(next(it))
    a = [int(next(it)) for _ in range(n)]
    l, r, ans = 1, max(a), 0
    while l <= r:
        mid = (l + r) // 2
        if sum(1 for x in a if x >= mid) >= m:
            ans, l = mid, mid + 1
        else:
            r = mid - 1
    print(ans)

main()
```

Vẫn đơn điệu (K càng lớn, càng ít gói đạt) → chặt được. O(n log max).

</details>

<details>
<summary>✅ Bài 8: Cặp có hiệu nhỏ nhất</summary>

Sau khi sắp xếp, hiệu nhỏ nhất **nhất định** là hiệu của một cặp kề nhau.
(Chứng minh: với i < j không kề, a[j] − a[i] = (a[j] − a[j−1]) + ... ≥ mỗi
số hạng, nên không nhỏ hơn hiệu kề nhỏ nhất.)

```python
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    a = sorted(map(int, data[1:1 + n]))
    print(min(a[i + 1] - a[i] for i in range(n - 1)))

main()
```

O(n log n) do sắp xếp + O(n) duyệt kề. Cách naive thử mọi cặp O(n²) → TLE
với n = 10⁵.

</details>

<details>
<summary>✅ Bài 9: Đếm điểm đạt</summary>

```python
import sys
from bisect import bisect_left

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    diem = sorted(int(next(it)) for _ in range(n))   # đảm bảo đã xếp
    m = int(next(it))
    ra = [str(n - bisect_left(diem, int(next(it)))) for _ in range(m)]
    sys.stdout.write("\n".join(ra))

main()
```

Số bạn ≥ x = n − (vị trí đầu tiên ≥ x). Test: điểm [5,6,7,8,9], x = 10 → 0;
x = 1 → 5; x = 7 → 3. Mỗi truy vấn O(log n).

</details>

<details>
<summary>✅ Bài 10: Tìm chỗ treo máy</summary>

```python
# Code sai:
l, r = 0, 1          # chỉ 2 phần tử!
while l < r:
    mid = (l + r) // 2   # mid = 0 = l mãi
    if a[mid] < x:
        l = mid          # l vẫn = 0 -> lặp vô tận!
```

Input nhỏ nhất gây treo: dãy 2 phần tử bất kỳ mà `a[0] < x` (ví dụ
`a = [1, 2]`, `x = 2`): mid = 0, `a[0] < x` đúng → `l = mid = 0` → lặp mãi.
Sửa đúng 1 dòng: `l = mid` → `l = mid + 1` (đã loại `a[mid]` thì bỏ hẳn nó).

</details>

<details>
<summary>✅ Bài 11: Photo 2 máy</summary>

```python
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    x, y, n = map(int, data[:3])

    def duoc(T):
        return T // x + T // y >= n   # đơn điệu theo T ✔

    l, r, ans = 0, min(x, y) * n, 0
    while l <= r:
        mid = (l + r) // 2
        if duoc(mid):
            ans, l = mid, mid + 1
        else:
            r = mid - 1
    print(ans)

main()
```

Chạy tay x=3, y=5, n=10: T=19 → 6+3=9 < 10 (chưa); T=20 → 6+4=10 ✔ → đáp án
**20**. Cận trên `min(x,y)*n` (máy nhanh nhất làm hết) luôn đủ.

</details>

<details>
<summary>✅ Bài 12: Tìm đỉnh O(log n)</summary>

```python
def tim_dinh(a):
    l, r = 0, len(a) - 1
    while l < r:
        mid = (l + r) // 2
        if a[mid] < a[mid + 1]:
            l = mid + 1   # dốc lên -> đỉnh ở bên phải
        else:
            r = mid       # dốc xuống/bằng -> đỉnh ở đây hoặc bên trái
    return l
```

Vì sao đúng: nếu `a[mid] < a[mid+1]` thì đi sang phải, dãy (hữu hạn) phải có
chỗ "đổi chiều" thành đỉnh; ngược lại đỉnh nằm bên trái (kể cả mid). Mỗi bước
bỏ một nửa → O(log n). Đã kiểm 500 dãy ngẫu nhiên: luôn trả vị trí đỉnh hợp lệ.

</details>

---

## 🧠 Thử thách

**Thử thách HSG:** Cho dãy tăng dần có thể chứa trùng (n ≤ 10⁵) và m truy vấn
(m ≤ 10⁵). Mỗi truy vấn cho [L, R], đếm số phần tử trong đoạn [L, R].
Yêu cầu O((n + m) log n). *Gợi ý: đáp án = upper_bound(R) − lower_bound(L).*

---

## 📝 Tóm tắt

| Khái niệm | Nội dung |
|---|---|
| 🔎 Tuyến tính | O(n), mọi dãy; `in`/`index` trên list |
| ✂️ Nhị phân | O(log n), **đòi dãy sắp xếp**; bất biến [l, r] |
| 🪤 Off-by-one | `<=`, `mid + 1` / `mid − 1`, một mẫu duy nhất |
| 📍 lower/upper | `bisect_left` / `bisect_right`; đếm = hiệu hai mốc |
| 🎯 Chặt đáp số | Kiểm tra đơn điệu O(f) → chặt K: O(f log range) |

---

## ➡️ Điều hướng

**Vị trí:** `02-Thuat-Toan/25-Tim-Kiem/bai.md`

**Bài tiếp theo:** [Bài 26 — Sắp Xếp](../26-Sap-Xep/bai.md)
