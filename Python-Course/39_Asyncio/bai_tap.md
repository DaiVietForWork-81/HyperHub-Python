# 📝 Bài 39: Bài Tập – Asyncio

> 🎯 **Chủ đề:** Coroutine (`async def`), `await`, `asyncio.run()`, `asyncio.sleep()`, `asyncio.gather()`, đo thời gian, mô phỏng tải trang và gọi API Open-Meteo.
>
> 📌 **Lưu ý:** Tất cả bài tập đều viết file `.py` và chạy trực tiếp (không cần cài thư viện). Bài dùng Open-Meteo cần có mạng — nếu mất mạng hãy đọc phần chú thích để biết cách chạy mô phỏng. Nếu chưa làm được, hãy xem lại bài giảng — **đáp án chi tiết ở [dap_an.md](dap_an.md)**.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Coroutine đầu tiên

* **Đề bài:** Viết coroutine `chao() -> str` in ra `"Bat dau"`, sau đó `await asyncio.sleep(1)` rồi in `"Xong"` và trả về `"OK"`. Chạy bằng `asyncio.run()`.
* **Input:** Không có.
* **Output:**
  ```
  Bat dau
  Xong
  ```
* **Gợi ý:** Nhớ `import asyncio`; cuối file gọi `asyncio.run(chao())`.

### Bài 2: Hàm chào có tham số

* **Đề bài:** Viết coroutine `chao(ten: str) -> str` trả về `"Xin chao, <ten>!"` sau khi chờ `asyncio.sleep(0.5)`. Gọi với tên `Mai` và in kết quả.
* **Input:** Không có.
* **Output:**
  ```
  Xin chao, Mai!
  ```
* **Gợi ý:** `return f"Xin chao, {ten}!"`; dùng `await chao("Mai")` trong `main`.

### Bài 3: Đếm từ 1 đến 3

* **Đề bài:** Viết coroutine `dem(n: int) -> None` in các số từ 1 đến n, giữa mỗi số `await asyncio.sleep(1)`. Gọi `dem(3)`.
* **Input:** Không có.
* **Output:**
  ```
  1
  2
  3
  ```
* **Gợi ý:** Vòng lặp `for i in range(1, n + 1): print(i); await asyncio.sleep(1)`.

### Bài 4: Coroutine trả tổng

* **Đề bài:** Viết coroutine `tinh_tong(a: int, b: int) -> int` trả `a + b` (kèm `await asyncio.sleep(0.1)` mô phỏng công việc). In kết quả `tinh_tong(3, 4)`.
* **Input:** Không có.
* **Output:**
  ```
  7
  ```
* **Gợi ý:** `async def tinh_tong(a: int, b: int) -> int:`.

### Bài 5: Hai câu tuần tự

* **Đề bài:** Viết `main()`: gọi `await chao("An")` rồi `await chao("Binh")` (mỗi lần in câu chào). Đây là chạy **tuần tự**.
* **Input:** Không có.
* **Output:**
  ```
  Xin chao, An!
  Xin chao, Binh!
  ```
* **Gợi ý:** Hai dòng `print(await chao(...))` liên tiếp nhau.

### Bài 6: Gather hai việc

* **Đề bài:** Viết coroutine `lam_viec(ten: str, giay: float) -> str` trả `f"{ten} xong sau {giay}s"`. Dùng `asyncio.gather` chạy 2 việc song song và in danh sách kết quả.
* **Input:** Không có.
* **Output:**
  ```
  ['A xong sau 2s', 'B xong sau 1s']
  ```
* **Gợi ý:** `ket_qua = await asyncio.gather(lam_viec("A", 2), lam_viec("B", 1))`.

### Bài 7: Đo thời gian một tác vụ

* **Đề bài:** Dùng `time.perf_counter()` đo thời gian chạy `await asyncio.sleep(2)` trong coroutine, in ra `"Mat: X.XXs"`.
* **Input:** Không có.
* **Output:**
  ```
  Mat: 2.00s
  ```
* **Gợi ý:** `bat = time.perf_counter()` trước, `time.perf_counter() - bat` sau.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Mô phỏng tải 3 trang song song

* **Đề bài:** Viết coroutine `tai_trang(so_thu_tu: int) -> str` in `f"Trang {so_thu_tu}: tai xong"` sau khi chờ `asyncio.sleep` ngẫu nhiên `random.uniform(0.5, 1.5)`. Tải 3 trang bằng `gather`.
* **Input:** Không có.
* **Output:** (thứ tự có thể khác nhau)
  ```
  Trang 1: tai xong
  Trang 2: tai xong
  Trang 3: tai xong
  ```
* **Gợi ý:** Tạo list `[tai_trang(i) for i in range(1, 4)]` rồi `await asyncio.gather(*list)`.

### Bài 9: So sánh tuần tự vs song song

* **Đề bài:** Chạy 3 tác vụ `tai(1 giây)` theo 2 cách: tuần tự (3 lần `await` lần lượt) và song song (`gather`). In thời gian cả hai.
* **Input:** Không có.
* **Output:**
  ```
  Tuan tu: 3.00s
  Song song: 1.00s
  ```
* **Gợi ý:** Đo bằng `time.perf_counter()` quanh từng đoạn.

### Bài 10: Danh sách tác vụ động

* **Đề bài:** Viết `tai_nhieu(n: int)` dùng list comprehension tạo **n** coroutine `tai_trang(i)` rồi `gather`. Gọi `tai_nhieu(5)` và in từng dòng `"Tai xong trang i"`.
* **Input:** Không có.
* **Output:**
  ```
  Tai xong trang 1
  Tai xong trang 2
  Tai xong trang 3
  Tai xong trang 4
  Tai xong trang 5
  ```
* **Gợi ý:** `cac_tac_vu = [tai_trang(i) for i in range(1, n + 1)]`.

### Bài 11: Lấy kết quả từ gather

* **Đề bài:** Coroutine `tinh(n: int) -> int` trả `n * n` sau khi chờ `asyncio.sleep(0.5)`. Dùng `gather` tính bình phương của `[2, 3, 4]` và in danh sách kết quả.
* **Input:** Không có.
* **Output:**
  ```
  [4, 9, 16]
  ```
* **Gợi ý:** `[tinh(x) for x in [2, 3, 4]]` rồi `gather(*...)`.

### Bài 12: Coroutine gọi coroutine

* **Đề bài:** Viết coroutine `chuan_bi() -> str` (chờ 0.5s, trả `"da chuan bi"`), và coroutine `chay() -> str` gọi `await chuan_bi()` rồi trả `f"Xong - {kq}"`. In kết quả của `chay()`.
* **Input:** Không có.
* **Output:**
  ```
  Xong - da chuan bi
  ```
* **Gợi ý:** Trong coroutine con có thể `await` coroutine khác.

### Bài 13: Thời gian mô phỏng 10 trang

* **Đề bài:** Tải 10 trang, mỗi trang chờ `random.uniform(0.2, 1.0)`. In tổng thời gian (dùng `perf_counter`) và số trang đã tải. Mục tiêu: tổng thời gian nhỏ hơn 2 giây.
* **Input:** Không có.
* **Output:**
  ```
  Tai xong 10 trang trong X.XXs
  ```
* **Gợi ý:** `gather` toàn bộ; in `len(ket_qua)`.

### Bài 14: Kiểm tra một task lỗi — return_exceptions

* **Đề bài:** Coroutine `go_api(ten: str) -> str` ném `ValueError("Loi API")` nếu `ten == "fail"`, ngược lại trả `f"Du lieu {ten}"`. Dùng `gather(..., return_exceptions=True)` với `"user"` và `"fail"`; in từng kết quả (lỗi thì in `LOI:` trước).
* **Input:** Không có.
* **Output:**
  ```
  Du lieu user
  LOI: Loi API
  ```
* **Gợi ý:** `isinstance(kq, BaseException)` để nhận diện lỗi.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: wait_for — chống treo

* **Đề bài:** Coroutine `tai_rat_lau() -> str` chờ `asyncio.sleep(10)`. Dùng `asyncio.wait_for(tai_rat_lau(), timeout=2)` và bắt `asyncio.TimeoutError`; in `"Qua han 2 giay, bo tac vu."`.
* **Input:** Không có.
* **Output:**
  ```
  Qua han 2 giay, bo tac vu.
  ```
* **Gợi ý:** Bọc trong `try/except asyncio.TimeoutError`.

### Bài 16: Tải trang nhanh nhất

* **Đề bài:** Tạo 5 tác vụ tải trang (chờ ngẫu nhiên 0.5–2.0s). Dùng `asyncio.gather` lấy kết quả, tìm và in **trang xong nhanh nhất** (dùng `min` theo thời gian chờ ghi trong chuỗi kết quả hoặc min theo thứ tự).
* **Input:** Không có.
* **Output:**
  ```
  Trang nhanh nhat: trangX (0.50s)
  ```
* **Gợi ý:** Trả về tuple `(giay, ten)` từ coroutine để dễ so sánh.

### Bài 17: Open-Meteo — nhiệt độ 3 thành phố

* **Đề bài:** Dùng `asyncio.to_thread` + `urllib` gọi Open-Meteo (`https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true`) cho Hà Nội (21.03, 105.85), Đà Nẵng (16.07, 108.22), TP.HCM (10.82, 106.63). In `Ten: X.X°C` cho mỗi thành phố.
* **Input:** Không có (cần mạng).
* **Output:**
  ```
  Ha Noi: 28.4°C
  Da Nang: 30.1°C
  TP.HCM: 31.2°C
  ```
* **Gợi ý:** Hàm đồng bộ `lay_nhiet_do(...)` dùng `urllib.request.urlopen`, JSON lấy `du_lieu["current_weather"]["temperature"]`.

### Bài 18: API với giới hạn thời gian

* **Đề bài:** Mở rộng bài 17: bọc toàn bộ tác vụ tải trong `asyncio.wait_for(..., timeout=5)`. Nếu quá hạn, in `"Thanh pho X: het thoi gian"` thay vì nhiệt độ.
* **Input:** Không có (cần mạng).
* **Output:**
  ```
  Ha Noi: 28.4°C
  ...
  ```
* **Gợi ý:** Bắt `asyncio.TimeoutError` quanh `gather` hoặc quanh từng tác vụ.

### Bài 19: Trình tải tổng hợp có báo cáo

* **Đề bài:** Viết `main()`: tải **8 trang mô phỏng** (chờ ngẫu nhiên), đồng thời gọi **3 API thời tiết** (to_thread). In: tổng thời gian, số trang tải được, danh sách nhiệt độ. Dùng hai `gather` riêng biệt.
* **Input:** Không có (phần API cần mạng).
* **Output:**
  ```
  Tai duoc 8/8 trang
  Nhiet do: Ha Noi 28.4°C, Da Nang 30.1°C, TP.HCM 31.2°C
  Tong thoi gian: 1.35s
  ```
* **Gợi ý:** Chạy lần lượt hai `gather` trong `main`; cộng dồn thời gian.

### Bài 20: Speed test bất đồng bộ hoàn chỉnh

* **Đề bài:** Viết chương trình kiểm tra tốc độ: hàm `do_toc_do(ten: str, n: int)` chạy `n` tác vụ tải 0.5s và trả `(ten, thoi_gian)`. Chạy 3 lần đo song song với `gather`, in bảng kết quả và xếp hạng nhanh – chậm.
* **Input:** Không có.
* **Output:**
  ```
  Lan 1: 0.51s
  Lan 2: 0.50s
  Lan 3: 0.52s
  Nhanh nhat: Lan 2 (0.50s)
  ```
* **Gợi ý:** `gather` trả danh sách tuple `(ten, giay)`; sắp xếp bằng `sorted(..., key=lambda x: x[1])`.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Viết và chạy coroutine bằng `asyncio.run`, dùng `await` đúng cách.
* ✅ Chạy song song với `asyncio.gather` và so sánh thời gian với cách tuần tự.
* ✅ Mô phỏng tải nhiều trang web và gọi API Open-Meteo song song.
* ✅ Chống treo bằng `wait_for` và xử lý lỗi bằng `return_exceptions`.

> 💪 **Mẹo học:** Hãy viết 3 đoạn code "đồng bộ → gather → đo thời gian" từ đầu để thành phản xạ khi gặp bất kỳ tác vụ I/O nào.

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 40: Mini Project](../40_Mini_Project/bai_giang.md)**
