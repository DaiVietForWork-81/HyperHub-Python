# 📝 Bài 35: Bài Tập – Thư Viện Requests

> 📡 **Chương 10 – Dữ liệu và mạng**
> Bạn đã học `requests.get`, `params`, `headers`, `.status_code`, `.text`, `.json()`, `timeout` và `try/except`. Giờ hãy thực hành: **một số bài gọi API thật** (httpbin.org, Open-Meteo — miễn phí, không cần key, cần có internet), **các bài còn lại là mô phỏng** bằng chuỗi JSON để bạn luyện được cả khi không có mạng.
>
> 💡 **Lưu ý:**
> * Trước khi làm các bài gọi API thật, hãy cài thư viện: `pip install requests`.
> * Đáp án nằm ở file `dap_an.md` cùng thư mục.
> * Các bài mô phỏng ghi rõ *(Mô phỏng)* trong tên.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Kiểm tra thư viện requests

* **Đề bài:** Viết chương trình `import requests` và in ra số phiên bản của thư viện để kiểm tra đã cài đặt thành công.
* **Input:** Không có.
* **Output:** Một dòng số phiên bản, ví dụ `2.32.3`.
* **Gợi ý:** Sau khi `import requests`, in thuộc tính `requests.__version__`. (Nếu báo `ModuleNotFoundError` thì chạy `pip install requests`.)

### Bài 2: GET đơn giản — chào httpbin (chạy được)

* **Đề bài:** Gọi `requests.get("https://httpbin.org/get")` với `timeout=10`, in ra `status_code` và `text`.
* **Input:** Không có (cần internet).
* **Output:** Dòng `Status: 200` và nội dung text (JSON).
* **Gợi ý:** `phong_hoi.status_code`; `phong_hoi.text`.

### Bài 3: GET với params — httpbin (chạy được)

* **Đề bài:** Gọi `https://httpbin.org/get` với `params={"name": "An", "lop": "10A1"}`, in ra `status_code` và URL thực tế đã gửi (`phong_hoi.url`).
* **Input:** Không có (cần internet).
* **Output:** `Status: 200` và URL dạng `...get?name=An&lop=10A1`.
* **Gợi ý:** `requests` tự nối tham số — không tự dùng dấu `?`.

### Bài 4: Xử lý "phản hồi mô phỏng" (Mô phỏng)

* **Đề bài:** Bạn có dict mô phỏng phản hồi: `{"status_code": 200, "text": '{"ok": true}'}` và bản `{"status_code": 404, "text": "Not Found"}`. Viết hàm `xu_ly(phong_hoi)` nhận dict này: nếu `status_code == 200` in `"Thanh cong"` + text, ngược lại in `"Loi {status_code}"`.
* **Input:** Hai dict mô phỏng trên.
* **Output:** `Thanh cong {"ok": true}` và `Loi 404`.
* **Gợi ý:** Truy cập `phong_hoi["status_code"]`; nhớ tên khóa của dict giống hệt thuộc tính của Response thật.

### Bài 5: Đọc chuỗi JSON mô phỏng thời tiết (Mô phỏng)

* **Đề bài:** Chuỗi JSON mô phỏng phản hồi Open-Meteo: `'{"current_weather": {"temperature": 30.2, "windspeed": 11.5}}'`. Dùng `json.loads` (giống `.json()` của requests) để đọc và in nhiệt độ, tốc độ gió.
* **Input:** Chuỗi JSON cho sẵn.
* **Output:**
  ```
  Nhiet do: 30.2°C
  Gio: 11.5 km/h
  ```
* **Gợi ý:** `json.loads` trả dict; truy cập hai tầng `["current_weather"]["temperature"]`.

### Bài 6: Bắt lỗi JSON hỏng (Mô phỏng)

* **Đề bài:** Viết chương trình parse chuỗi JSON `'{"ten": "An", "diem": }'` (hỏng) bằng `json.loads`, dùng `try/except` bắt `json.JSONDecodeError` và in `"JSON loi"`. Chương trình phải chạy tiếp bình thường.
* **Input:** Chuỗi JSON hỏng cho sẵn.
* **Output:** `JSON loi: ...` (không sập chương trình).
* **Gợi ý:** `except json.JSONDecodeError:` — đây chính là loại lỗi `.json()` của requests cũng ném ra.

### Bài 7: POST với JSON — httpbin (chạy được)

* **Đề bài:** Gửi `requests.post("https://httpbin.org/post", json={"ten": "An", "diem": 8}, timeout=10)`, in `status_code` và phần dữ liệu server trả lại (trong JSON trả về, khóa `"json"`).
* **Input:** Không có (cần internet).
* **Output:** `Status: 200` và dòng chứa `{'ten': 'An', 'diem': 8}`.
* **Gợi ý:** `phong_hoi.json()["json"]` — httpbin "phản hồi lại" đúng dữ liệu đã nhận.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Tìm học viên trong JSON mô phỏng (Mô phỏng)

* **Đề bài:** Chuỗi JSON mô phỏng danh sách học viên (list dict `id`, `ten`, `diem`). Dùng `json.loads` đọc, tìm học viên có `id = 2` và in tên + điểm; nếu không có in `"Khong tim thay"`.
* **Input:**
  ```json
  [{"id": 1, "ten": "An", "diem": 8},
   {"id": 2, "ten": "Binh", "diem": 7},
   {"id": 3, "ten": "Chi", "diem": 9}]
  ```
* **Output:** `Binh - 7 diem` (tìm id 2), `Khong tim thay` (tìm id 99).
* **Gợi ý:** Duyệt list dict; giống bài 34 nhưng dữ liệu đến từ chuỗi JSON.

### Bài 9: Thời tiết Hà Nội — Open-Meteo (chạy được)

* **Đề bài:** Gọi Open-Meteo với `latitude=21.0285, longitude=105.8542, current_weather=True` (dùng `params` + `timeout=10`), in thời điểm, nhiệt độ và tốc độ gió từ `phong_hoi.json()["current_weather"]`.
* **Input:** Không có (cần internet).
* **Output:** 3 dòng: `Thoi diem`, `Nhiet do`, `Gio` (giá trị lấy từ API).
* **Gợi ý:** URL: `https://api.open-meteo.com/v1/forecast`; `True` trong params tự thành `true`.

### Bài 10: Tính tổng tiền đơn hàng từ JSON (Mô phỏng)

* **Đề bài:** Chuỗi JSON mô phỏng phản hồi API đơn hàng: list dict `ten`, `gia`, `so_luong`. Đọc và tính tổng tiền (`gia * so_luong`), in từng món và tổng cộng.
* **Input:**
  ```json
  [{"ten": "Vo", "gia": 5000, "so_luong": 3},
   {"ten": "But", "gia": 3000, "so_luong": 5},
   {"ten": "Sach", "gia": 25000, "so_luong": 1}]
  ```
* **Output:**
  ```
  Vo: 15000
  But: 15000
  Sach: 25000
  Tong: 55000
  ```
* **Gợi ý:** `float()` cho `gia`; cộng dồn biến `tong`.

### Bài 11: Xử lý lỗi mạng mô phỏng — timeout và mất kết nối (Mô phỏng)

* **Đề bài:** Viết hàm `goi_api_an_toan(url)` mô phỏng lời gọi requests: nếu URL chứa `"cham"`, nâng ngoại lệ `requests.exceptions.Timeout`; nếu chứa `"loi"`, nâng `requests.exceptions.ConnectionError`; ngược lại trả về `(200, {"ok": True})`. Bên ngoài dùng `try/except` in thông báo tương ứng. Gọi thử cả 3 URL.
* **Input:** `"https://api.example.com/nhanh"`, `".../cham"`, `".../loi"`.
* **Output:** Thông báo thành công, `Het thoi gian cho`, `Mat ket noi` — không sập.
* **Gợi ý:** Dùng `raise requests.exceptions.Timeout("...")` để giả lập; cấu trúc `try/except` giống hệt khi gọi mạng thật.

### Bài 12: Kiểm tra status trước khi đọc dữ liệu (Mô phỏng)

* **Đề bài:** Viết hàm `xu_ly_phong_hoi(status, chuoi_json)`: nếu status là 200 thì `json.loads(chuoi_json)` và in dữ liệu; nếu 400 in `"Loi: yeu cau sai"`; nếu 404 in `"Loi: khong tim thay"`; nếu 500 in `"Loi: may chu"`. Gọi thử 4 trường hợp.
* **Input:** `(200, '{"ok": true}')`, `(400, "{}")`, `(404, "{}")`, `(500, "{}")`.
* **Output:** 4 thông báo tương ứng.
* **Gợi ý:** Chỉ gọi `json.loads` trong nhánh 200 — đúng quy tắc "status trước, dữ liệu sau".

### Bài 13: Xử lý phản hồi lỗi của API (Mô phỏng)

* **Đề bài:** Một số API trả status 200 nhưng dữ liệu là lỗi: `'{"error": "Khong co du lieu"}'`. Viết chương trình đọc chuỗi JSON: nếu có khóa `"error"` in `"API bao loi: ..."`, ngược lại in nội dung. Gọi thử với chuỗi lỗi và chuỗi thường.
* **Input:** `'{"error": "Khong co du lieu"}'` và `'{"temperature": 30.2}'`.
* **Output:** `API bao loi: Khong co du lieu` và `Nhiet do: 30.2`.
* **Gợi ý:** Kiểm tra `if "error" in du_lieu:` — ứng dụng thực tế khi nhiều API trả lỗi qua JSON.

### Bài 14: Phân tích phản hồi Open-Meteo lồng nhau (Mô phỏng)

* **Đề bài:** Chuỗi JSON mô phỏng đầy đủ phản hồi Open-Meteo (có `current_weather` lồng bên trong). Đọc và in ra một "bảng" thời tiết gọn: thời điểm, nhiệt độ, gió, mã thời tiết.
* **Input:**
  ```json
  {"timezone": "Asia/Bangkok",
   "current_weather": {"time": "2026-08-05T09:00",
                       "temperature": 30.2, "windspeed": 11.5,
                       "weathercode": 1}}
  ```
* **Output:** 4 dòng thông tin (thời điểm, nhiệt độ, gió, mã thời tiết).
* **Gợi ý:** Rút biến con `cw = du_lieu["current_weather"]` cho gọn (giống bài giảng).

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Hàm lấy thời tiết theo thành phố — Open-Meteo (chạy được)

* **Đề bài:** Viết hàm `lay_thoi_tiet(ten_thanh_pho, vi_do, kinh_do)` gọi Open-Meteo với `params`, `timeout=10`, dùng `try/except` bắt `Timeout` và `ConnectionError`, kiểm tra `status_code` trước khi đọc `.json()`. Hàm trả chuỗi mô tả (nhiệt độ, gió) hoặc thông báo lỗi — không bao giờ ném ngoại lệ. Gọi thử với Hà Nội.
* **Input:** Hà Nội: `(21.0285, 105.8542)`.
* **Output:** Chuỗi dạng `Ha Noi: 30.2°C, gio 11.5 km/h` hoặc thông báo lỗi thân thiện.
* **Gợi ý:** Cấu trúc: `try → get → kiểm tra status → json()` với 3 nhánh `except`.

### Bài 16: Nhiệt độ trung bình một tuần từ JSON (Mô phỏng)

* **Đề bài:** Chuỗi JSON mô phỏng phản hồi dạng `{"daily": {"time": [...], "temperature_2m_max": [...]}}` của 7 ngày. Đọc, tính nhiệt độ TB tối đa của tuần, tìm ngày nóng nhất và in ra.
* **Input:** 7 ngày: `2026-08-01` → `2026-08-07` với nhiệt độ max ví dụ `[30, 31, 29, 33, 32, 34, 28]`.
* **Output:** `Nhiet do TB tuan: 31.0°C` và `Ngay nong nhat: 2026-08-06 (34°C)`.
* **Gợi ý:** `sum(...) / len(...)`; tìm max bằng `max(nhiet)` và `nhiet.index(...)`.

### Bài 17: Chương trình kiểm tra kết nối — httpbin (chạy được)

* **Đề bài:** Viết chương trình gọi `https://httpbin.org/status/404` và `https://httpbin.org/status/500` với `timeout=10`, dùng `try/except` + `raise_for_status()` để xử lý: in `"OK"` khi 2xx, in mã lỗi và nội dung khi có `HTTPError`. Chương trình không được sập.
* **Input:** Không có (cần internet).
* **Output:** Với 404: `Loi 404: ...`; với 500: `Loi 500: ...` (không sập).
* **Gợi ý:** `phong_hoi.raise_for_status()` ném `requests.exceptions.HTTPError` cho mã 4xx/5xx; bắt và in `loi.response.status_code`.

### Bài 18: So sánh thời tiết Hà Nội và TP.HCM — Open-Meteo (chạy được)

* **Đề bài:** Dùng hàm ở bài 15 (hoặc viết lại) để lấy nhiệt độ Hà Nội `(21.0285, 105.8542)` và TP.HCM `(10.8231, 106.6297)`, in thành phố nào đang nóng hơn kèm nhiệt độ cả hai.
* **Input:** Không có (cần internet).
* **Output:** `TP HCM nong hon Ha Noi (33.5 vs 30.2)` hoặc ngược lại (dữ liệu tùy thời điểm).
* **Gợi ý:** Tách nhiệt độ ra số bằng cách tìm trong chuỗi trả về, hoặc viết hàm phụ trả số `float` riêng.

### Bài 19: Sắp xếp và lọc dữ liệu từ JSON mô phỏng (Mô phỏng)

* **Đề bài:** Chuỗi JSON mô phỏng phản hồi danh sách sản phẩm (`ten`, `gia`). Đọc dữ liệu, in các sản phẩm giá từ 5000 đến 20000, rồi in danh sách đã sắp xếp giảm dần theo giá (tên + giá).
* **Input:**
  ```json
  [{"ten": "Vo", "gia": 5000}, {"ten": "But", "gia": 3000},
   {"ten": "Sach", "gia": 25000}, {"ten": "Thuoc ke", "gia": 15000}]
  ```
* **Output:** 2 sản phẩm lọc được (Vo, Thuoc ke) và danh sách sắp xếp: Sach, Thuoc ke, Vo, But.
* **Gợi ý:** List comprehension để lọc; `sorted(..., key=lambda sp: sp["gia"], reverse=True)` (bài 25).

### Bài 20: Mini Project — Tra cứu thời tiết nhiều thành phố (chạy được)

* **Đề bài:** Xây dựng chương trình hoàn chỉnh:
  1. Dict thành phố: `"Ha Noi": (21.0285, 105.8542)`, `"TP HCM": (10.8231, 106.6297)`, `"Da Nang": (16.0544, 108.2022)`.
  2. Hàm `lay_thoi_tiet(ten, vi_do, kinh_do)` an toàn như bài 15 (params, timeout, status check, try/except).
  3. Vòng lặp gọi từng thành phố và in bảng thời tiết đẹp dạng `Ten | Nhiet do | Gio`.
  4. In thêm thành phố nóng nhất và lạnh nhất.
* **Input:** 3 thành phố trên (cần internet).
* **Output:** Bảng 3 dòng thời tiết + dòng kết luận nóng nhất/lạnh nhất.
* **Gợi ý:** Lưu kết quả mỗi thành phố vào list để dễ tìm max/min; dùng f-string canh cột `f"{ten:<8}"`.

---

## 🎯 Tổng kết

Chúc mừng bạn đã hoàn thành 20 bài tập về `requests`! Bạn đã luyện:

* ✅ Cài đặt và kiểm tra thư viện.
* ✅ GET/POST với `params`, `headers`, `timeout` — gọi API thật (httpbin, Open-Meteo).
* ✅ Đọc dữ liệu với `.status_code`, `.text`, `.json()`.
* ✅ Xử lý lỗi: `Timeout`, `ConnectionError`, `HTTPError`, `JSONDecodeError`.
* ✅ Phân tích phản hồi JSON thật và mô phỏng (không cần internet).

👉 Kiểm tra đáp án tại **[dap_an.md](dap_an.md)**.

Dữ liệu từ API giờ đã nằm trong tay bạn — nhưng lưu trữ lâu dài thế nào? File CSV thô sơ, JSON rối — đã đến lúc học **cơ sở dữ liệu**:

👉 **[Bài 36: SQLite – Cơ Sở Dữ Liệu Trong Python](../36_SQLite/bai_giang.md)**
