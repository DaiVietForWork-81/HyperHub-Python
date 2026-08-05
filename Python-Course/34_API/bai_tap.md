# 📝 Bài 34: Bài Tập – API

> 🌐 **Chương 10 – Dữ liệu và mạng**
> Bạn đã học lý thuyết API: phương thức HTTP, endpoint, status code, JSON response. Giờ hãy luyện tập bằng các bài mô phỏng — máy chủ được mô phỏng bằng hàm, dữ liệu trả về là chuỗi JSON. (Việc gọi API thật sẽ học ở bài 35 với thư viện `requests`.)
>
> 💡 **Lưu ý:** Hãy tự làm trước, chỉ xem đáp án sau khi đã thử hết sức. Đáp án nằm ở file `dap_an.md` cùng thư mục.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: In bảng 4 phương thức HTTP

* **Đề bài:** Viết chương trình in ra bảng 4 phương thức HTTP: `GET`, `POST`, `PUT`, `DELETE` kèm hành động tương ứng (Lấy, Tạo, Sửa, Xóa).
* **Input:** Không có.
* **Output:**
  ```
  GET - Lấy dữ liệu
  POST - Tạo dữ liệu mới
  PUT - Cập nhật dữ liệu
  DELETE - Xóa dữ liệu
  ```
* **Gợi ý:** Danh sách các tuple `(ten, hanh_dong)` + vòng lặp `for`.

### Bài 2: Tách URL thành endpoint và tham số

* **Đề bài:** Cho URL `"https://api.open-meteo.com/v1/forecast?latitude=21.0285&longitude=105.8542&current_weather=true"`. Dùng `split("?")` tách thành endpoint và phần tham số, in cả hai.
* **Input:** URL cho sẵn.
* **Output:** Hai dòng: `Endpoint: ...` và `Tham so: ...`.
* **Gợi ý:** `url.split("?")` trả list 2 phần tử; gán lần lượt cho hai biến.

### Bài 3: In thực đơn của "API nhà hàng"

* **Đề bài:** Mô phỏng thực đơn nhà hàng bằng list dict (khóa `ten`, `gia`). In từng món dạng `1. Pho bo - 50000 dong`.
* **Input:** 3 món: `Pho bo` 50000, `Bun cha` 45000, `Com tam` 60000.
* **Output:** 3 dòng thực đơn như trên.
* **Gợi ý:** `enumerate(mon_an, start=1)` để có số thứ tự.

### Bài 4: Giải thích status code

* **Đề bài:** Viết hàm `y_nghia(ma)` nhận một status code (int) và trả về chuỗi giải thích: `200` → `"Thanh cong (OK)"`, `201` → `"Da tao moi"`, `400` → `"Loi yeu cau"`, `404` → `"Khong tim thay"`, `500` → `"Loi may chu"`, còn lại → `"Khong ro"`. In kết quả của 6 mã.
* **Input:** Lần lượt gọi với `200, 201, 400, 404, 500, 302`.
* **Output:** 6 dòng giải thích tương ứng.
* **Gợi ý:** Dùng `if/elif/else`; 302 không nằm trong danh sách nên trả `"Khong ro"`.

### Bài 5: Đọc JSON mô phỏng phản hồi thời tiết

* **Đề bài:** Chuỗi JSON mô phỏng phản hồi của Open-Meteo chứa `temperature` và `windspeed`. Dùng `json.loads` để đọc, in nhiệt độ và tốc độ gió.
* **Input:** `'{"temperature": 30.2, "windspeed": 11.5}'`.
* **Output:**
  ```
  Nhiet do: 30.2°C
  Gio: 11.5 km/h
  ```
* **Gợi ý:** `import json`; `json.loads(chuoi)` trả dict, lấy theo khóa.

### Bài 6: Bắt lỗi JSON hỏng

* **Đề bài:** Cho chuỗi JSON hỏng `'{"ten": "An", "diem": }'` (thiếu giá trị). Viết chương trình dùng `try/except` bắt lỗi `json.JSONDecodeError` và in `"JSON loi"` thay vì để chương trình sập.
* **Input:** Chuỗi JSON hỏng cho sẵn.
* **Output:** `JSON loi: ...` (không được sập chương trình).
* **Gợi ý:** Đặt `json.loads(chuoi)` trong khối `try`, in thông báo trong `except`.

### Bài 7: Mô phỏng "máy chủ" trả dữ liệu có status code

* **Đề bài:** Viết hàm `phuc_vu(mon)` mô phỏng máy chủ nhà hàng: nếu món nằm trong thực đơn trả về `(200, "Co mon: <ten>")`, ngược lại trả về `(404, "Khong co mon: <ten>")`. In kết quả khi gọi với món có và món không có.
* **Input:** Thực đơn gồm `"Pho bo", "Bun cha"`; gọi với `"Pho bo"` và `"Banh my"`.
* **Output:** 2 dòng kèm status code 200 và 404.
* **Gợi ý:** Kiểm tra `mon in thuc_don`; trả tuple hai giá trị rồi giải nén khi in.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Mô phỏng GET — tìm học sinh theo mã số

* **Đề bài:** "Máy chủ" quản lý danh sách học sinh (list dict `id`, `ten`, `lop`). Viết hàm `get_hoc_sinh(id)` mô phỏng `GET`: tìm theo id, trả `(200, dict)` nếu có, `(404, None)` nếu không. In kết quả cho id có và id không có.
* **Input:** Danh sách 3 học sinh; gọi với `id=2` và `id=99`.
* **Output:** Kết quả 200 kèm thông tin, và 404.
* **Gợi ý:** Vòng `for` duyệt danh sách; `if hs["id"] == id: return 200, hs`.

### Bài 9: Mô phỏng POST — thêm học sinh mới

* **Đề bài:** Viết hàm `post_hoc_sinh(ds, ten, lop)` mô phỏng `POST`: tự sinh id mới (id lớn nhất + 1), thêm vào danh sách, trả về `(201, dict_moi)`. Gọi thử và in danh sách sau khi thêm.
* **Input:** Danh sách ban đầu 2 học sinh (id 1, 2); thêm `"Dung", "10A2"`.
* **Output:** Status `201` + thông tin học sinh mới (id 3), sau đó in lại toàn bộ danh sách.
* **Gợi ý:** `max(hs["id"] for hs in ds) + 1` để sinh id; dùng `append`.

### Bài 10: Mô phỏng PUT — cập nhật điểm

* **Đề bài:** Viết hàm `put_diem(ds, id, diem_moi)` mô phỏng `PUT`: tìm học sinh theo id, sửa điểm, trả `(200, hs)`; không tìm thấy trả `(404, None)`. Gọi thử với id có và không có.
* **Input:** Danh sách học sinh có cột `diem`; sửa id 1 thành 10.
* **Output:** In kết quả 200 kèm thông tin sau sửa, và 404 cho id lạ.
* **Gợi ý:** Sau khi tìm thấy, gán `hs["diem"] = diem_moi` rồi trả về — danh sách gốc tự thay đổi.

### Bài 11: Mô phỏng DELETE — xóa học sinh

* **Đề bài:** Viết hàm `delete_hoc_sinh(ds, id)` mô phỏng `DELETE`: tìm và xóa khỏi danh sách, trả `(200, "Da xoa")`; không tìm thấy trả `(404, None)`. Gọi thử và in danh sách còn lại.
* **Input:** Danh sách 3 học sinh; xóa id 2.
* **Output:** `200` kèm thông báo, sau đó in danh sách chỉ còn 2 học sinh.
* **Gợi ý:** Dùng `list.remove(hs)` sau khi tìm thấy; có thể tạo danh sách mới bằng comprehension.

### Bài 12: Mô phỏng API thời tiết với tọa độ không hợp lệ

* **Đề bài:** Viết hàm `thoi_tiet(kinh_do, vi_do)` mô phỏng Open-Meteo: nếu vĩ độ ngoài khoảng `-90..90` hoặc kinh độ ngoài `-180..180`, trả `(400, {"error": "Toa do khong hop le"})`; ngược lại trả `(200, {"temperature": 30.2})`. Gọi thử cả hai trường hợp.
* **Input:** `(105.85, 21.03)` và `(105.85, 91)`.
* **Output:** Status 200 và 400 kèm dữ liệu tương ứng.
* **Gợi ý:** Điều kiện: `not (-90 <= vi_do <= 90) or not (-180 <= kinh_do <= 180)`.

### Bài 13: Đọc JSON phản hồi lồng nhau

* **Đề bài:** Chuỗi JSON mô phỏng phản hồi Open-Meteo: `{"current_weather": {"temperature": 30.2, "windspeed": 11.5, "time": "2026-08-05T09:00"}, "timezone": "Asia/Bangkok"}`. Dùng `json.loads`, in thời điểm, nhiệt độ, gió và múi giờ.
* **Input:** Chuỗi JSON cho sẵn.
* **Output:** 4 dòng thông tin.
* **Gợi ý:** Truy cập hai tầng: `du_lieu["current_weather"]["temperature"]`.

### Bài 14: Kiểm tra status trước khi đọc dữ liệu

* **Đề bài:** Viết hàm `xu_ly(status, chuoi_json)` nhận status code và chuỗi JSON: nếu status là 200, dùng `json.loads` và in dữ liệu; nếu 400 in `"Loi: yeu cau sai"`; nếu 404 in `"Loi: khong tim thay"`; nếu 500 in `"Loi: may chu"`. Gọi thử với cả 4 trường hợp.
* **Input:** Lần lượt gọi với `(200, '{"ok": true}')`, `(400, "{}")`, `(404, "{}")`, `(500, "{}")`.
* **Output:** 4 dòng thông báo tương ứng.
* **Gợi ý:** Dùng `if/elif/else`; chỉ `json.loads` trong nhánh 200.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Xây dựng "mini API" quản lý thư viện

* **Đề bài:** Xây dựng "máy chủ thư viện" mô phỏng đủ 4 phương thức: `GET` trả danh sách sách; `POST` thêm sách (id tự tăng); `PUT` sửa giá theo id; `DELETE` xóa theo id. Viết hàm `phuc_vu(phuong_thuc, du_lieu)` xử lý cả bốn, mỗi thành công trả status đúng (GET 200, POST 201, PUT 200, DELETE 200), thất bại trả 404.
* **Input:** Danh sách 2 sách (`id`, `ten`, `gia`); gọi thử GET, POST, PUT, DELETE.
* **Output:** Kết quả từng lệnh kèm status; sau mỗi lệnh ghi chú trạng thái danh sách.
* **Gợi ý:** Dùng `if phuong_thuc == "GET":` cho từng nhánh; tách phần tìm theo id thành hàm nhỏ `tim_sach(ds, id)` để tái sử dụng.

### Bài 16: API thời tiết nâng cao — kiểm tra dữ liệu lỗi từ server

* **Đề bài:** Viết hàm `thoi_tiet_an_toan(chuoi_json)` nhận chuỗi JSON mô phỏng phản hồi. Dùng `try/except`: nếu JSON hỏng, trả `(500, "JSON loi")`; nếu JSON không có khóa `current_weather`, trả `(400, "Thieu current_weather")`; nếu hợp lệ, trả `(200, nhiet_do)`. Gọi thử 3 tình huống.
* **Input:** Chuỗi hợp lệ, chuỗi thiếu khóa, chuỗi JSON hỏng.
* **Output:** 3 kết quả tương ứng.
* **Gợi ý:** `if "current_weather" not in du_lieu:`; bắt `json.JSONDecodeError` trong `except`.

### Bài 17: Tự tạo URL từ tham số

* **Đề bài:** Viết hàm `tao_url(endpoint, tham_so)` nhận endpoint (str) và dict tham số (ví dụ `{"latitude": 21.03, "longitude": 105.85, "current_weather": True}`), trả về URL đúng chuẩn: endpoint + `?` + các cặp `khóa=giá trị` ngăn cách `&` (giá trị True chuyển thành `true`).
* **Input:** Endpoint `"https://api.open-meteo.com/v1/forecast"` và dict trên.
* **Output:** URL hoàn chỉnh đúng thứ tự khai báo.
* **Gợi ý:** Tạo list chuỗi `f"{k}={str(v).lower()}"` cho từng cặp, nối bằng `"&"`; giá trị boolean cần `str(...).lower()` để thành `true`.

### Bài 18: Phân tích phản hồi nhiều tầng và xử lý thiếu khóa

* **Đề bài:** Chuỗi JSON mô phỏng phản hồi Open-Meteo có thể **thiếu** khóa `daily` (ngày mưa). Viết chương trình đọc: nếu có `daily`, in tổng số ngày và nhiệt độ trung bình tối thiểu; nếu thiếu, in `"Khong co du lieu ngay"`. Dùng `.get()` để xử lý an toàn.
* **Input:**
  ```json
  {"daily": {"time": ["2026-08-01", "2026-08-02"], "temperature_2m_min": [25.1, 24.8]}}
  ```
  và bản thiếu `daily`.
* **Output:** Thông tin tính được hoặc thông báo thiếu.
* **Gợi ý:** `du_lieu.get("daily")` trả `None` khi thiếu; dùng `sum(...) / len(...)`.

### Bài 19: So sánh dữ liệu từ hai "API" thời tiết

* **Đề bài:** Viết hàm `lay_nhiet_do(chuoi_json)` nhận chuỗi JSON phản hồi mô phỏng của một thành phố, trả về `(ten_thanh_pho, nhiet_do)` hoặc `None` nếu lỗi. Dùng nó để so sánh nhiệt độ Hà Nội và TP.HCM (2 chuỗi JSON cho sẵn), in thành phố nào nóng hơn.
* **Input:** 2 chuỗi JSON: `{"city": "Ha Noi", "temperature": 30.2}` và `{"city": "TP HCM", "temperature": 33.5}`.
* **Output:** `TP HCM nong hon Ha Noi (33.5 vs 30.2)` hoặc tương tự.
* **Gợi ý:** Hàm trả tuple; so sánh `nhiet_do_1 > nhiet_do_2` và in câu phù hợp.

### Bài 20: Hệ thống "API quản lý điểm" hoàn chỉnh (Mini Project)

* **Đề bài:** Xây dựng hệ thống mô phỏng API quản lý điểm trường học:
  1. Danh sách ban đầu 4 học sinh (`id`, `ten`, `diem`).
  2. Hàm `phuc_vu(phuong_thuc, du_lieu)` hỗ trợ: `GET` danh sách, `GET id` một học sinh (404 nếu không có), `POST` thêm (201, id tự tăng), `PUT` sửa điểm (200/404), `DELETE` xóa (200/404).
  3. Sau đó chạy một "kịch bản" tuần tự: GET tất cả → GET id 2 → POST thêm → PUT sửa → DELETE → GET tất cả, in kết quả từng bước kèm status code.
* **Input:** Kịch bản như trên.
* **Output:** Báo cáo từng bước kèm status và dữ liệu; danh sách cuối cùng đúng 4 học sinh sau khi thêm/xóa.
* **Gợi ý:** Đưa "máy chủ" (danh sách + hàm xử lý) vào một khối; tách hàm nhỏ `tim_hoc_sinh`; mỗi nhánh phương thức trả `(status, du_lieu)`; dùng `enumerate`/`max` cho id.

---

## 🎯 Tổng kết

Chúc mừng bạn đã hoàn thành 20 bài tập về API! Bạn đã luyện:

* ✅ 4 phương thức HTTP: GET, POST, PUT, DELETE qua các hàm mô phỏng.
* ✅ Đọc và hiểu URL: endpoint, tham số, `?`, `&`.
* ✅ Xử lý status code: 200, 201, 400, 404, 500.
* ✅ Phân tích JSON response (phẳng và lồng nhau) bằng `json.loads`.
* ✅ Viết code an toàn với `try/except` khi dữ liệu lỗi.

👉 Kiểm tra đáp án tại **[dap_an.md](dap_an.md)**.

Giờ đã nắm vững lý thuyết, bạn sẽ học cách **gọi API thật** từ Python bằng thư viện `requests`:

👉 **[Bài 35: Thư Viện Requests – Gọi API Từ Python](../35_Requests/bai_giang.md)**
