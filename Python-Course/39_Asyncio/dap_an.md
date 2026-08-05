# ✅ Bài 39: Đáp Án – Asyncio

> 🎯 **Hướng dẫn:** Mỗi bài giải gồm **Phân tích → Ý tưởng → Thuật toán → Code → Giải thích → Độ phức tạp**. Toàn bộ code chạy được với **Python 3.9+**, không cần thư viện ngoài chuẩn. Hãy tự làm trước khi xem!

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Coroutine đầu tiên

**Phân tích:** Bài đầu làm quen cấu trúc tối thiểu của chương trình asyncio: khai báo coroutine, `await asyncio.sleep`, và chạy bằng `asyncio.run`.

**Ý tưởng:** Các câu lệnh bên trong coroutine chạy tuần tự; `asyncio.sleep(1)` chỉ tạm dừng coroutine này mà không chặn cả chương trình.

**Thuật toán:**
1. `import asyncio`.
2. Khai báo coroutine `chao`.
3. In `Bat dau` → `await asyncio.sleep(1)` → in `Xong` → `return "OK"`.
4. `asyncio.run(chao())`.

**Code:**

```python
import asyncio

async def chao() -> str:
    """Coroutine đơn giản: in, chờ, in, trả về."""
    print("Bat dau")
    await asyncio.sleep(1)     # tạm dừng 1 giây — không chặn event loop
    print("Xong")
    return "OK"

asyncio.run(chao())
```

**Giải thích code:**
* `async def chao()` khai báo coroutine (hàm bất đồng bộ).
* `await asyncio.sleep(1)` là quãng chờ — nếu chạy song song với tác vụ khác, khoảng thời gian này sẽ được tận dụng.
* `asyncio.run(chao())` là điểm vào duy nhất để khởi động event loop.

**Độ phức tạp:** O(1) — chỉ in và chờ cố định.

---

### Bài 2: Hàm chào có tham số

**Phân tích:** Coroutine cũng nhận tham số và khai báo type hints như hàm thường (ôn bài 38).

**Ý tưởng:** `await asyncio.sleep(0.5)` mô phỏng "đang làm việc" rồi trả về f-string.

**Thuật toán:**
1. Khai báo `async def chao(ten: str) -> str`.
2. `await asyncio.sleep(0.5)`.
3. `return f"Xin chao, {ten}!"`.
4. Trong `main`: `print(await chao("Mai"))`.

**Code:**

```python
import asyncio

async def chao(ten: str) -> str:
    """Tạo lời chào cho một cái tên."""
    await asyncio.sleep(0.5)
    return f"Xin chao, {ten}!"

async def main() -> None:
    loi_chao = await chao("Mai")
    print(loi_chao)

asyncio.run(main())
```

**Giải thích code:**
* `await chao("Mai")` — chờ coroutine hoàn thành rồi lấy giá trị trả về (chuỗi).
* Nếu có coroutine khác đang chạy, event loop sẽ điều phối nó trong lúc 0.5s này.

**Độ phức tạp:** O(1).

---

### Bài 3: Đếm từ 1 đến 3

**Phân tích:** Kết hợp vòng lặp `for` bên trong coroutine; mỗi vòng lặp có một lần "chờ".

**Ý tưởng:** "Cứ mỗi giây in một số" — `await asyncio.sleep(1)` đặt ngay trong vòng lặp.

**Thuật toán:**
1. Khai báo `async def dem(n: int) -> None`.
2. Vòng lặp từ 1 đến n: in i rồi `await asyncio.sleep(1)`.
3. Gọi `dem(3)`.

**Code:**

```python
import asyncio

async def dem(n: int) -> None:
    """In các số từ 1 đến n, mỗi số cách nhau 1 giây."""
    for i in range(1, n + 1):
        print(i)
        await asyncio.sleep(1)   # giữa mỗi số chờ đúng 1 giây

asyncio.run(dem(3))
```

**Giải thích code:**
* `-> None` vì hàm chỉ in ra, không trả về.
* Mỗi vòng lặn `await asyncio.sleep(1)` chỉ dừng coroutine này — các coroutine khác vẫn chạy bình thường.

**Độ phức tạp:** O(n) vòng lặp cộng n lần chờ.

---

### Bài 4: Coroutine trả tổng

**Phân tích:** Coroutine có thể tính toán và trả về giá trị như hàm thường — điểm khác là cách chạy (qua event loop).

**Ý tưởng:** Chờ 0.1 giây (giả lập trước khi tính) rồi `return a + b`.

**Thuật toán:**
1. Khai báo `async def tinh_tong(a: int, b: int) -> int`.
2. `await asyncio.sleep(0.1)`.
3. `return a + b`.
4. In `await tinh_tong(3, 4)`.

**Code:**

```python
import asyncio

async def tinh_tong(a: int, b: int) -> int:
    """Trả về tổng hai số sau một chờ nhỏ."""
    await asyncio.sleep(0.1)
    return a + b

async def main() -> None:
    print(await tinh_tong(3, 4))

asyncio.run(main())
```

**Giải thích code:**
* Kết quả là giá trị `7` mà coroutine trả về sau khi hoàn thành.
* Type hints giúp biết chắc `await tinh_tong(...)` luôn trả `int`.

**Độ phức tạp:** O(1).

---

### Bài 5: Hai câu tuần tự

**Phân tích:** Hai lần `await` liên tiếp — việc đầu xong mới đến việc sau (chạy tuần tự).

**Ý tưởng:** Gọi `await chao("An")`, in; rồi `await chao("Binh")`, in.

**Thuật toán:**
1. Viết `async def main() -> None`.
2. Dòng đầu: `print(await chao("An"))`.
3. Dòng thứ hai: `print(await chao("Binh"))`.

**Code:**

```python
import asyncio

async def chao(ten: str) -> str:
    await asyncio.sleep(0.5)
    return f"Xin chao, {ten}!"

async def main() -> None:
    # Chạy tuần tự: chờ hết câu đầu rồi mới bắt câu sau
    print(await chao("An"))     # 0.5 giây
    print(await chao("Binh"))   # cộng thêm 0.5 giây → tổng 1 giây

asyncio.run(main())
```

**Giải thích code:**
* Hai `await` nối tiếp nhau nghĩa là thời gian chờ **cộng dồn**: 0.5 + 0.5 = 1s.
* Muốn nhanh hơn phải dùng `gather` — chính là bài 6.

**Độ phức tạp:** O(1) nhưng tổng thời gian chờ bằng tổng các lần chờ.

---

### Bài 6: Gather hai việc

**Phân tích:** Khác biệt lớn nhất so với bài 5: hai coroutine chạy **song song** trong cùng khoảng thời gian.

**Ý tưởng:** `asyncio.gather(a, b)` đăng ký cả hai vào event loop; `await` chờ **tất cả**; kết quả là danh sách đúng thứ tự đầu vào.

**Thuật toán:**
1. Khai báo `async def lam_viec(ten: str, giay: float) -> str`.
2. `await asyncio.sleep(giay)`.
3. `return f"{ten} xong sau {giay}s"`.
4. `ket_qua = await asyncio.gather(lam_viec("A", 2), lam_viec("B", 1))`.
5. In `ket_qua`.

**Code:**

```python
import asyncio

async def lam_viec(ten: str, giay: float) -> str:
    """Mô phỏng một công việc tốn giây."""
    await asyncio.sleep(giay)
    return f"{ten} xong sau {giay}s"

async def main() -> None:
    # Hai coroutine đã được nạp đồng thời vào event loop
    ket_qua = await asyncio.gather(
        lam_viec("A", 2),
        lam_viec("B", 1),
    )
    print(ket_qua)

asyncio.run(main())
```

**Giải thích code:**
* `gather` chạy song song → tổng thời gian `max(2, 1) = 2s`, không phải `3s`.
* Thứ tự kết quả theo thứ tự đầu vào: `['A xong sau 2s', 'B xong sau 1s']`.

**Độ phức tạp:** O(max) của các lần chờ.

---

### Bài 7: Đo thời gian một tác vụ

**Phân tích:** Dùng `time.perf_counter()` — đồng hồ đo thời gian chính xác cao.

**Ý tưởng:** Ghi nhận thời điểm trước và sau khi chờ; hiệu hai thời điểm là thời gian trôi qua.

**Thuật toán:**
1. `import asyncio, time`.
2. Trong coroutine: `bat = time.perf_counter()`.
3. `await asyncio.sleep(2)`.
4. In `(time.perf_counter() - bat)` làm tròn 2 chữ số.

**Code:**

```python
import asyncio
import time

async def main() -> None:
    bat = time.perf_counter()
    await asyncio.sleep(2)          # tác vụ cần đo
    mat = time.perf_counter() - bat
    print(f"Mat: {mat:.2f}s")

asyncio.run(main())
```

**Giải thích code:**
* `time.perf_counter()` trả số giây kiểu float (độ phân giải rất cao).
* `f"{mat:.2f}s"` in ra `2.00s`.

**Độ phức tạp:** O(1).

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Mô phỏng tải 3 trang song song

**Phân tích:** 3 trang web tải cùng lúc — mỗi trang mất thời gian ngẫu nhiên; dùng `gather` chạy song song. `random` mô phỏng sự khác nhau của mạng.

**Ý tưởng:** `random.uniform(0.5, 1.5)` tạo thời gian chờ; tổng thời gian cả chương trình ≈ thời gian trang chậm nhất.

**Thuật toán:**
1. Import `asyncio, random`.
2. Coroutine `tai_trang(so_thu_tu)` — chờ ngẫu nhiên rồi in.
3. Tạo list các coroutine bằng list comprehension.
4. `await asyncio.gather(*list_coro)`.

**Code:**

```python
import asyncio
import random

async def tai_trang(so_thu_tu: int) -> None:
    """Mô phỏng tải một trang web tốn thời gian ngẫu nhiên."""
    giay = random.uniform(0.5, 1.5)
    await asyncio.sleep(giay)
    print(f"Trang {so_thu_tu}: tai xong ({giay:.1f}s)")

async def main() -> None:
    # 3 coroutine được tạo sẵn rồi cùng chạy
    cac_trang = [tai_trang(i) for i in range(1, 4)]
    await asyncio.gather(*cac_trang)

asyncio.run(main())
```

**Giải thích code:**
* `[tai_trang(i) for i in range(1, 4)]` tạo 3 coroutine nhưng **chưa chạy**.
* `asyncio.gather(*cac_trang)` — dấu `*` giải nén list thành nhiều đối số → chạy song song.
* Thứ tự `in` có thể khác nhau giữa các lần chạy vì thời gian chờ ngẫu nhiên.

**Độ phức tạp:** O(n) tạo list; thời gian chờ ≈ `max(giây)`.

---

### Bài 9: So sánh tuần tự vs song song

**Phân tích:** Đây là bài đo lường minh chứng sức mạnh của asyncio: cùng 3 tác vụ 1 giây, cách chạy khác nhau cho thời gian khác nhau.

**Ý tưởng:** Viết hai coroutine đóng vai việc đo: một `chay_tuan_tu` (3 lần `await` liên tiếp), một `chay_song_song` (gather 3 cái). Đo bằng `perf_counter`.

**Thuật toán:**
1. Coroutine `tai(n)` trả về sau `sleep(n)`.
2. `chay_tuan_tu`: vòng lặp `for` với 3 lần `await tai(1)`; đo thời gian.
3. `chay_song_song`: `await asyncio.gather(tai(1), tai(1), tai(1))`; đo thời gian.
4. In kết quả.

**Code:**

```python
import asyncio
import time

async def tai(n: int) -> int:
    await asyncio.sleep(n)
    return n

async def chay_tuan_tu() -> float:
    bat = time.perf_counter()
    for _ in range(3):
        await tai(1)
    return time.perf_counter() - bat

async def chay_song_song() -> float:
    bat = time.perf_counter()
    await asyncio.gather(tai(1), tai(1), tai(1))
    return time.perf_counter() - bat

async def main() -> None:
    tuan_tu = await chay_tuan_tu()
    song_song = await chay_song_song()
    print(f"Tuan tu: {tuan_tu:.2f}s")
    print(f"Song song: {song_song:.2f}s")

asyncio.run(main())
```

**Giải thích code:**
* Tuần tự: 1 + 1 + 1 = 3 giây.
* Song song: tối đa một lần chờ dài nhất = 1 giây.
* Kết quả điển hình: `Tuan tu: 3.00s / Song song: 1.00s`.

**Độ phức tạp:** tuần tự O(n·t), song song O(t) với 1 lần chờ t.

---

### Bài 10: Danh sách tác vụ động

**Phân tích:** Chương trình tải số trang **do người dùng quyết định** — số lượng coroutine thay đổi theo tham số `n`, dùng list comprehension tạo động.

**Ý tưởng:** `tai_nhieu(n)` sinh n coroutine rồi `gather`; in từng dòng kết quả.

**Thuật toán:**
1. Coroutine `tai_trang(i)` chờ ngẫu nhiên rồi trả chuỗi.
2. `tai_nhieu(n)` tạo list, gather, in từng dòng.
3. Chạy với `n = 5`.

**Code:**

```python
import asyncio
import random

async def tai_trang(i: int) -> str:
    giay = random.uniform(0.3, 1.0)
    await asyncio.sleep(giay)
    return f"Tai xong trang {i}"

async def tai_nhieu(n: int) -> None:
    cac_tac_vu = [tai_trang(i) for i in range(1, n + 1)]   # tạo động n coroutine
    ket_qua = await asyncio.gather(*cac_tac_vu)
    for dong in ket_qua:
        print(dong)

asyncio.run(tai_nhieu(5))
```

**Giải thích code:**
* List comprehension tạo **đúng n** coroutine, chỉ cần đổi `n` là số lượng thay đổi.
* `gather` chạy ĐỦ 5 trang cùng lúc; tổng thời gian ≈ trang chậm nhất (~1s) thay vì 5 × ~.5s.

**Độ phức tạp:** O(n) tạo task; thời gian chờ ≈ max.

---

### Bài 11: Lấy kết quả từ gather

**Phân tích:** `gather` không chỉ "chạy" mà còn **trả về danh sách kết quả** theo đúng thứ tự đầu vào — ta dùng để tính và in.

**Ý tưởng:** Mỗi coroutine `tinh(x)` trả `x * x`; gather 3 cái thành `[4, 9, 16]`.

**Thuật toán:**
1. Coroutine `tinh(n: int) -> int` — chờ 0.5s rồi `return n * n`.
2. Tạo list `[tinh(x) for x in [2, 3, 4]]`.
3. `ket_qua = await asyncio.gather(*list)`.
4. In `ket_qua`.

**Code:**

```python
import asyncio

async def tinh(n: int) -> int:
    await asyncio.sleep(0.5)
    return n * n

async def main() -> None:
    ket_qua = await asyncio.gather(*[tinh(x) for x in [2, 3, 4]])
    print(ket_qua)

asyncio.run(main())
```

**Giải thích code:**
* Nhờ `gather`, ba phép tính chạy song song; tổng thời gian 0.5s.
* `ket_qua` giữ đúng thứ tự đầu vào: `2*2=4`, `3*3=9`, `4*4=16`.
* In ra `[4, 9, 16]`.

**Độ phức tạp:** O(n) tính, O(1) thời gian chờ (một lần 0.5s).

---

### Bài 12: Coroutine gọi coroutine khác

**Phân tích:** Coroutine thứ hai gọi `await` coroutine thứ nhất — kỹ thuật **lồng coroutine**, rất thường gặp trong ứng dụng thật.

**Ý tưởng:** `chay()` chờ `chuan_bi()` rồi ghép vào câu trả lời.

**Thuật toán:**
1. `chuan_bi()` chờ 0.5s, trả `"da chuan bi"`.
2. `chay()` gọi `kq = await chuan_bi()`, trả `f"Xong - {kq}"`.
3. Chạy và in.

**Code:**

```python
import asyncio

async def chuan_bi() -> str:
    """Bước chuẩn bị."""
    await asyncio.sleep(0.5)
    return "da chuan bi"

async def chay() -> str:
    """Coroutine điều phối: gọi coroutine khác."""
    kq = await chuan_bi()
    return f"Xong - {kq}"

async def main() -> None:
    print(await chay())

asyncio.run(main())
```

**Giải thích code:**
* `await chuan_bi()` bên trong `chay()` — kết quả từng bước được ghép vào bước sau, kiến trúc tầng lớp dễ đọc.

**Độ phức tạp:** O(1).

---

### Bài 13: Thời gian mô phỏng 10 trang

**Phân tích:** 10 tác vụ đồng thời, mỗi tác vụ chờ ngẫu nhiên. Mục tiêu cho thấy: 10 trang mà tổng thời gian vẫn nhỏ vì chờ song song.

**Ý tưởng:** Chờ mỗi trang `random.uniform(0.2, 1.0)`; `gather` toàn; đo tổng; in số trang.

**Thuật toán:**
1. Tạo 10 coroutine chờ ngẫu nhiên.
2. Gather + đo thời gian.
3. In số trang và tổng thời gian.

**Code:**

```python
import asyncio
import random
import time

async def tai(k: int) -> int:
    await asyncio.sleep(random.uniform(0.2, 1.0))
    return k

async def main() -> None:
    bat = time.perf_counter()
    ket_qua = await asyncio.gather(*(tai(i) for i in range(1, 11)))
    mat = time.perf_counter() - bat
    print(f"Tai xong {len(ket_qua)} trang trong {mat:.2f}s")

asyncio.run(main())
```

**Giải thích code:**
* `*(tai(i) for i in ...)` — giải nén generator thành đối số cho `gather`.
* Vì tải song song, total ≈ thời gian trang chậm nhất (< 2 giây dù có 10 trang).
* `len(ket_qua)` = số trang đã hoàn tất (mọi).

**Độ phức tạp:** O(n) tạo, thời gian chờ O(max ngẫu nhiên).

---

### Bài 14: Kiểm tra một task lỗi — return_exceptions

**Phân tích:** Khi một coroutine ném ngoại lệ, mặc định `gather` báo lỗi và **hủy các task khác**. `return_exceptions=True` biến mỗi ngoại lệ thành **một phần tử kết quả** — chương trình vẫn sống.

**Ý tưởng:** `go_api("fail")` ném `ValueError`; gather không crash vì `return_exceptions`; vòng lặp phân biệt kết quả/lỗi bằng `isinstance(kq, BaseException)`.

**Thuật toán:**
1. Coroutine `go_api(ten)`: nếu `ten == "fail"` thì `raise ValueError("Loi API")`, ngược lại trả chuỗi.
2. `gather(..., return_exceptions=True)` với `"user"` và `"fail"`.
3. Duyệt: lỗi in `LOI:`, không lỗi in chuỗi.

**Code:**

```python
import asyncio

async def go_api(ten: str) -> str:
    await asyncio.sleep(1)
    if ten == "fail":
        raise ValueError("Loi API!")
    return f"Du lieu {ten}"

async def main() -> None:
    ket_qua = await asyncio.gather(
        go_api("user"),
        go_api("fail"),
        return_exceptions=True,   # lỗi trở thành phần tử, không hủy task
    )
    for kq in ket_qua:
        if isinstance(kq, BaseException):
            print("LOI:", kq)
        else:
            print(kq)

asyncio.run(main())
```

**Giải thích code:**
* Phần tử 0 là chuỗi `"Du lieu user"`; phần tử 1 là đối tượng `ValueError`.
* `isinstance(kq, BaseException)` nhận diện ngoại lệ.
* Output chuẩn: `Du lieu user` / `LOI: Loi API!`.

**Độ phức tạp:** O(1) thời gian chờ (1 giây song song).

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: wait_for — chống treo

**Phân tích:** API ngoài có thể chậm vô hạn. `asyncio.wait_for(coro, timeout)` giới hạn thời gian chờ; quá hạn ném `asyncio.TimeoutError`.

**Ý tưởng:** Coroutine `tai_rat_lau` chờ 10s; bọc bằng `wait_for(..., timeout=2)`; bắt `TimeoutError` và in thông báo.

**Thuật toán:**
1. Coroutine `tai_rat_lau()` chờ 10 giây.
2. Trong `main`: `try: await asyncio.wait_for(tai_rat_lau(), timeout=2)`.
3. `except asyncio.TimeoutError:` in thông báo bỏ tác vụ.

**Code:**

```python
import asyncio

async def tai_rat_lau() -> str:
    await asyncio.sleep(10)              # thật sự rất chậm
    return "Du lieu"

async def main() -> None:
    try:
        du_lieu = await asyncio.wait_for(tai_rat_lau(), timeout=2)
        print(du_lieu)
    except asyncio.TimeoutError:
        print("Qua han 2 giay, bo tac vu.")

asyncio.run(main())
```

**Giải thích code:**
* `wait_for` hủy coroutine khi quá thời gian cho phép — chương trình không treo.
* Output: `Qua han 2 giay, bo tac vu.`

**Độ phức tạp:** O(timeout) — chờ tối đa 2 giây.

---

### Bài 16: Tải trang nhanh nhất

**Phân tích:** Cần so sánh thời gian từng tác vụ → mỗi coroutine trả về **tuple** `(giay, ten)` để `min()` so sánh được.

**Ý tưởng:** `tai_trang(i)` trả `(giay, f"trang{i}")`; `min(ket_qua)` lấy phần tử nhỏ nhất theo giây.

**Thuật toán:**
1. Coroutine trả `(thoi_gian, ten_trang)`.
2. Gather 5 tác vụ.
3. `nhanh_nhat = min(ket_qua)` — tuple so sánh từ phần tử đầu.
4. In tên và thời gian.

**Code:**

```python
import asyncio
import random
from typing import List, Tuple

async def tai_trang(i: int) -> Tuple[float, str]:
    """Trả về (thời gian tải, tên trang)."""
    giay = random.uniform(0.5, 2.0)
    await asyncio.sleep(giay)
    return giay, f"trang{i}"

async def main() -> None:
    cac_trang: List[Tuple[float, str]] = await asyncio.gather(
        *(tai_trang(i) for i in range(1, 6))
    )
    nhanh_nhat = min(cac_trang)   # so theo giây trước, rồi tên
    print(f"Trang nhanh nhat: {nhanh_nhat[1]} ({nhanh_nhat[0]:.2f}s)")

asyncio.run(main())
```

**Giải thích code:**
* `min` trên tuple so sánh lần lượt từng phần tử → đúng thứ tự cần.
* Kết quả ví dụ: `Trang nhanh nhat: trang4 (0.52s)`.

**Độ phức tạp:** O(n) để gather; O(n) để tìm min.

---

### Bài 17: Open-Meteo — nhiệt độ 3 thành phố

**Phân tích:** Gọi HTTP là thao tác **blocking** (chặn) — nếu gọi trực tiếp trong coroutine sẽ làm đơ event loop. Giải pháp: hàm đồng bộ + `asyncio.to_thread`.

**Ý tưởng:** Hàm `lay_nhiet_do` dùng `urllib` đọc JSON (đồng bộ). Coroutine `tai_nhiet_do` bọc nó bằng `asyncio.to_thread`. `gather` 3 thành phố cùng lúc.

**Thuật toán:**
1. Hàm `lay_nhiet_do(thanh_pho, vi_do, kinh_do)`: tạo URL, `urlopen`, đọc JSON, trả dict.
2. Coroutine `tai_nhiet_do(*args)` → `await asyncio.to_thread(lay_nhiet_do, *args)`.
3. `gather` 3 thành phố; in từng nhiệt độ.

**Code:**

```python
import asyncio
import json
import urllib.request
from typing import Dict

def lay_nhiet_do(thanh_pho: str, vi_do: float, kinh_do: float) -> Dict[str, object]:
    """Đồng bộ: gọi Open-Meteo và đọc nhiệt độ hiện tại."""
    url = (f"https://api.open-meteo.com/v1/forecast?latitude={vi_do}"
           f"&longitude={kinh_do}&current_weather=true")
    with urllib.request.urlopen(url, timeout=10) as phan_hoi:
        du_lieu = json.loads(phan_hoi.read().decode("utf-8"))
    nhiet_do = du_lieu["current_weather"]["temperature"]
    return {"thanh_pho": thanh_pho, "nhiet_do": nhiet_do}

async def tai_nhiet_do(*args) -> Dict[str, object]:
    """Bọc hàm đồng bộ vào luồng riêng — event loop không bị chặn."""
    return await asyncio.to_thread(lay_nhiet_do, *args)

async def main() -> None:
    cac_thanh_pho = [
        ("Ha Noi", 21.03, 105.85),
        ("Da Nang", 16.07, 108.22),
        ("TP.HCM", 10.82, 106.63),
    ]
    ket_qua = await asyncio.gather(*(tai_nhiet_do(*tp) for tp in cac_thanh_pho))
    for kq in ket_qua:
        print(f"{kq['thanh_pho']}: {kq['nhiet_do']}°C")

asyncio.run(main())
```

**Giải thích code:**
* `urllib.request.urlopen` chặn luồng — nhưng vì nằm trong `to_thread`, mỗi thành phố chạy **một luồng riêng**, chờ mạng không đóng băng ai cả.
* `gather` làm 3 luồng chạy đồng thời → tổng thời gian ≈ thành phố chậm nhất.
* Nếu mất mạng, chương trình báo lỗi `URLError` — chạy lại khi có mạng.

**Độ phức tạp:** O(max) thời gian HTTP của 3 thành phố (song song).

---

### Bài 18: API với giới hạn thời gian

**Phân tích:** Mở rộng bài 17 với "cửa an toàn": nếu một API quá chậm, đừng chờ vô hạn.

**Ý tưởng:** Bọc từng tác vụ trong `asyncio.wait_for(..., timeout=5)`; bắt `TimeoutError` và thay bằng thông báo.

**Thuật toán:**
1. Dùng lại `lay_nhiet_do` và `tai_nhiet_do` từ bài 17.
2. Coroutine `tai_co_thoi_gian(*args)`: `try: return await asyncio.wait_for(tai_nhiet_do(*args), timeout=5)`; `except TimeoutError: return {"thanh_pho": args[0], "loi": True}`.
3. `gather` và in kết quả.

**Code:**

```python
import asyncio
import json
import urllib.request
from typing import Dict

def lay_nhiet_do(thanh_pho: str, vi_do: float, kinh_do: float) -> Dict[str, object]:
    url = (f"https://api.open-meteo.com/v1/forecast?latitude={vi_do}"
           f"&longitude={kinh_do}&current_weather=true")
    with urllib.request.urlopen(url, timeout=10) as phan_hoi:
        du_lieu = json.loads(phan_hoi.read().decode("utf-8"))
    return {"thanh_pho": thanh_pho,
            "nhiet_do": du_lieu["current_weather"]["temperature"]}

async def tai_nhiet_do(*args) -> Dict[str, object]:
    return await asyncio.to_thread(lay_nhiet_do, *args)

async def tai_co_thoi_gian(*args) -> Dict[str, object]:
    """Tải nhiệt độ nhưng tối đa 5 giây, quá hạn thì báo lỗi."""
    try:
        return await asyncio.wait_for(tai_nhiet_do(*args), timeout=5)
    except asyncio.TimeoutError:
        return {"thanh_pho": args[0], "nhiet_do": None}

async def main() -> None:
    cac_thanh_pho = [
        ("Ha Noi", 21.03, 105.85),
        ("Da Nang", 16.07, 108.22),
        ("TP.HCM", 10.82, 106.63),
    ]
    ket_qua = await asyncio.gather(*(tai_co_thoi_gian(*tp) for tp in cac_thanh_pho))
    for kq in ket_qua:
        if kq["nhiet_do"] is None:
            print(f"{kq['thanh_pho']}: het thoi gian")
        else:
            print(f"{kq['thanh_pho']}: {kq['nhiet_do']}°C")

asyncio.run(main())
```

**Giải thích code:**
* `wait_for` hủy coroutine sau 5 giây; chương trình không bao giờ treo dù mạng chậm.
* `None` đóng vai trò "không có dữ liệu" — kiểu mẫu quen thuộc từ bài 38 (`Optional`).

**Độ phức tạp:** O(max(timeout, thời gian tải)).

---

### Bài 19: Trình tải tổng hợp có báo cáo

**Phân tích:** Ứng dụng thực tế pha trộn hai loại tác vụ: tải trang mô phỏng (sleep) và gọi API (to_thread). Chạy **hai nhóm gather riêng biệt** rồi tổng hợp báo cáo.

**Ý tưởng:** Nhóm 1: `gather` 8 trang mô phỏng. Nhóm 2: `gather` 3 API thời tiết. Đo tổng thời gian của cả quá trình.

**Thuật toán:**
1. Coroutine `tai_trang(i)` chờ ngẫu nhiên, trả `True`.
2. Coroutine `tai_nhiet_do(...)` dùng `to_thread` (như bài 17).
3. Trong `main`: đo thời gian, gather nhóm trang, gather nhóm API, in báo cáo.

**Code:**

```python
import asyncio
import json
import random
import time
import urllib.request
from typing import List

async def tai_trang(i: int) -> bool:
    await asyncio.sleep(random.uniform(0.3, 1.0))
    return True

def lay_nhiet_do(thanh_pho: str, vi_do: float, kinh_do: float) -> float:
    url = (f"https://api.open-meteo.com/v1/forecast?latitude={vi_do}"
           f"&longitude={kinh_do}&current_weather=true")
    with urllib.request.urlopen(url, timeout=10) as phan_hoi:
        du_lieu = json.loads(phan_hoi.read().decode("utf-8"))
    return du_lieu["current_weather"]["temperature"]

async def tai_nhiet_do(*args) -> float:
    return await asyncio.to_thread(lay_nhiet_do, *args)

async def main() -> None:
    bat = time.perf_counter()

    # Nhóm 1: tải 8 trang mô phỏng song song
    cac_trang = await asyncio.gather(*(tai_trang(i) for i in range(1, 9)))
    print(f"Tai duoc {len(cac_trang)}/8 trang")

    # Nhóm 2: gọi 3 API thời tiết song song
    cac_thanh_pho = [
        ("Ha Noi", 21.03, 105.85),
        ("Da Nang", 16.07, 108.22),
        ("TP.HCM", 10.82, 106.63),
    ]
    nhiet_do: List[float] = await asyncio.gather(*(tai_nhiet_do(*tp) for tp in cac_thanh_pho))
    chuoi_nhiet_do = ", ".join(f"{cac_thanh_pho[i][0]} {nhiet_do[i]}°C"
                               for i in range(len(cac_thanh_pho)))
    print(f"Nhiet do: {chuoi_nhiet_do}")

    print(f"Tong thoi gian: {time.perf_counter() - bat:.2f}s")

asyncio.run(main())
```

**Giải thích code:**
* Mỗi nhóm chạy song song nội bộ; hai nhóm chạy tuần tự nhau nhưng tổng vẫn nhanh hơn hẳn cách đồng bộ.
* `zip` qua tên thành phố và nhiệt độ để nối chuỗi báo cáo.
* Cần mạng cho phần API; phần trang luôn chạy được.

**Độ phức tạp:** O(t_max1 + t_max2) với hai nhóm song song.

---

### Bài 20: Speed test bất đồng bộ hoàn chỉnh

**Phân tích:** Chương trình "đo tốc độ" chạy nhiều lần thử song song, thu kết quả tuple, sắp xếp và chọn nhanh nhất.

**Ý tưởng:** `do_toc_do(ten, n)` chạy n tác vụ 0.5s bằng gather và trả `(ten, thoi_gian)`. Gather 3 lần thử; `sorted` theo thời gian.

**Thuật toán:**
1. Coroutine `tac_vu()` chờ 0.5s.
2. Coroutine `do_toc_do(ten, n)`: đo thời gian gather n tác vụ, trả tuple.
3. `ket_qua = await asyncio.gather(do_toc_do("Lan 1", 3), ..., 3 lần)`.
4. Sắp xếp theo giây, in bảng và xếp hạng.

**Code:**

```python
import asyncio
import time
from typing import List, Tuple

async def tac_vu() -> None:
    """Một công việc chờ 0.5 giây."""
    await asyncio.sleep(0.5)

async def do_toc_do(ten: str, n: int) -> Tuple[str, float]:
    """Chạy n tác vụ song song, trả về (tên lần đo, thời gian)."""
    bat = time.perf_counter()
    await asyncio.gather(*(tac_vu() for _ in range(n)))
    giay = time.perf_counter() - bat
    return ten, giay

async def main() -> None:
    # 3 lần đo chạy song song nhau
    ket_qua: List[Tuple[str, float]] = await asyncio.gather(
        do_toc_do("Lan 1", 3),
        do_toc_do("Lan 2", 3),
        do_toc_do("Lan 3", 3),
    )
    for ten, giay in ket_qua:
        print(f"{ten}: {giay:.2f}s")

    # Sắp xếp tăng dần theo thời gian
    xep_hang = sorted(ket_qua, key=lambda x: x[1])
    nhanh_nhat = xep_hang[0]
    print(f"Nhanh nhat: {nhanh_nhat[0]} ({nhanh_nhat[1]:.2f}s)")

asyncio.run(main())
```

**Giải thích code:**
* Cả 3 lần đo chạy **song song với nhau** → tổng thời gian ≈ 0.5s dù mỗi lần đo chạy 3 tác vụ.
* `sorted(..., key=lambda x: x[1])` sắp theo thời gian — lần nhanh nhất đứng đầu.
* Kết quả ví dụ: `Lan 1: 0.51s`, `Lan 2: 0.50s`, `Lan 3: 0.52s`, nhanh nhất `Lan 2`.

**Độ phức tạp:** O(1) thời gian chờ chính (0.5s), O(n log n) để sắp xếp.

---

## 🎯 Lời kết

Bạn đã hoàn thành **20 bài tập Asyncio** — từ coroutine đơn lẻ đến chương trình tải trang + gọi API song song có đo thời gian. Kỹ năng này giúp chương trình của bạn **không bao giờ đứng im chờ đợi** — vô cùng quan trọng khi làm ứng dụng thật.

👉 Tiếp theo: **[Bài 40: Mini Project – Quản Lý Cửa Hàng Sách](../40_Mini_Project/bai_giang.md)**