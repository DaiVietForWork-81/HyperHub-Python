# ✅ Bài 35: Đáp Án – Thư Viện Requests

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án.
>
> ⚠️ **Quan trọng:** Trước khi chạy, hãy cài thư viện bằng lệnh:
> ```powershell
> pip install requests
> ```
> Các bài ghi *(chạy được)* cần có **internet**; các bài *(Mô phỏng)* chỉ xử lý chuỗi JSON — chạy được cả khi không có mạng.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Kiểm tra thư viện requests

**Phân tích:** Kiểm tra cài đặt bằng cách import rồi in phiên bản.

**Ý tưởng:** `import requests` không báo lỗi là đã cài xong; `requests.__version__` chứa số phiên bản.

**Thuật toán:**
1. Import requests.
2. In `requests.__version__`.

**Code:**

```python
# Cài đặt trước: pip install requests
import requests

# Kiểm tra phiên bản đã cài đặt
print(requests.__version__)
```

**Giải thích code:**
* `import requests` — nếu chưa cài sẽ báo `ModuleNotFoundError`; lúc đó chạy `pip install requests`.
* `requests.__version__` — thuộc tính lưu số phiên bản (ví dụ `2.32.3`).

**Độ phức tạp:** O(1).

---

### Bài 2: GET đơn giản — chào httpbin (chạy được)

**Phân tích:** Lời gọi GET đầu tiên tới httpbin — dịch vụ miễn phí trả về chính yêu cầu của bạn.

**Ý tưởng:** `requests.get(url, timeout=10)`; in `.status_code` và `.text`.

**Thuật toán:**
1. Import requests.
2. Gọi GET httpbin với timeout 10.
3. In status_code và text.

**Code:**

```python
# Cài đặt trước: pip install requests
import requests

# Gửi yêu cầu GET — cần internet
phong_hoi = requests.get("https://httpbin.org/get", timeout=10)

print("Status:", phong_hoi.status_code)   # 200 = thành công
print("Text:", phong_hoi.text)            # nội dung thô dạng chuỗi JSON
```

**Giải thích code:**
* `timeout=10` — chờ tối đa 10 giây, tránh treo chương trình.
* `.status_code` — mã trạng thái của phản hồi.
* `.text` — toàn bộ nội dung phản hồi ở dạng chuỗi.

**Độ phức tạp:** Phụ thuộc tốc độ mạng.

---

### Bài 3: GET với params — httpbin (chạy được)

**Phân tích:** Tham số URL phải được nối đúng chuẩn — requests làm hộ qua `params`.

**Ý tưởng:** Truyền dict `{"name": "An", "lop": "10A1"}` cho `params`; kiểm tra `.url` để thấy kết quả.

**Thuật toán:**
1. Import requests.
2. Gọi GET với `params` và `timeout`.
3. In status và URL đã tạo.

**Code:**

```python
# Cài đặt trước: pip install requests
import requests

# params: requests tự nối thành ?name=An&lop=10A1
phong_hoi = requests.get(
    "https://httpbin.org/get",
    params={"name": "An", "lop": "10A1"},
    timeout=10,
)

print("Status:", phong_hoi.status_code)
print("URL da gui:", phong_hoi.url)
```

**Giải thích code:**
* `params={...}` — dict tham số; requests xử lý dấu `?`, `&` và mã hóa URL.
* `.url` — URL thật đã gửi, cho phép kiểm tra `params` hoạt động đúng.
* So sánh với hàm `tao_url` tự viết ở bài 34 — đây chính là lý do dùng thư viện.

**Độ phức tạp:** Phụ thuộc mạng.

---

### Bài 4: Xử lý "phản hồi mô phỏng" (Mô phỏng)

**Phân tích:** Trước khi gọi API thật, luyện tư duy xử lý phản hồi — dict mô phỏng giống hệt `Response`.

**Ý tưởng:** Hàm nhận dict, kiểm tra `status_code` rồi hành xử tương ứng.

**Thuật toán:**
1. Định nghĩa hàm `xu_ly(phong_hoi)` nhận dict.
2. Nếu `status_code == 200`: in "Thanh cong" + text; ngược lại in lỗi.
3. Gọi với 2 dict mô phỏng.

**Code:**

```python
# Cài đặt trước: pip install requests
import requests

def xu_ly(phong_hoi):
    """Xử lý dict mô phỏng phản hồi (giống Response của requests)."""
    if phong_hoi["status_code"] == 200:
        print("Thanh cong", phong_hoi["text"])
    else:
        print("Loi", phong_hoi["status_code"])

# Hai "phản hồi" mô phỏng
phong_hoi_ok = {"status_code": 200, "text": '{"ok": true}'}
phong_hoi_loi = {"status_code": 404, "text": "Not Found"}

xu_ly(phong_hoi_ok)
xu_ly(phong_hoi_loi)
```

**Giải thích code:**
* Khóa của dict (`status_code`, `text`) trùng tên thuộc tính của Response thật — dễ chuyển sang dùng thật.
* `if phong_hoi["status_code"] == 200` — quy tắc "status trước, dữ liệu sau".

**Độ phức tạp:** O(1).

---

### Bài 5: Đọc chuỗi JSON mô phỏng thời tiết (Mô phỏng)

**Phân tích:** `.json()` của requests bên trong cũng là `json.loads` — luyện trực tiếp bằng chuỗi JSON không mạng.

**Ý tưởng:** `json.loads(chuoi)` → dict; truy cập hai tầng khóa.

**Thuật toán:**
1. Import json.
2. Parse chuỗi JSON.
3. Lấy `current_weather` rồi các giá trị, in ra.

**Code:**

```python
import json

# Chuỗi JSON mô phỏng đúng định dạng Open-Meteo trả về
chuoi_json = '{"current_weather": {"temperature": 30.2, "windspeed": 11.5}}'

# json.loads tương đương với .json() của requests
du_lieu = json.loads(chuoi_json)
cw = du_lieu["current_weather"]           # rút dict con

print(f"Nhiet do: {cw['temperature']}°C")
print(f"Gio: {cw['windspeed']} km/h")
```

**Giải thích code:**
* `json.loads` — chuỗi → dict; dữ liệu giống hệt khi gọi API thật.
* `cw = du_lieu["current_weather"]` — biến ngắn gọn, dễ đọc.

**Độ phức tạp:** O(n) với n là độ dài chuỗi.

---

### Bài 6: Bắt lỗi JSON hỏng (Mô phỏng)

**Phân tích:** Khi gọi API thật, server có thể trả nội dung không phải JSON → `.json()` ném `JSONDecodeError`. Tập bắt lỗi này bằng `json.loads`.

**Ý tưởng:** Đặt `json.loads` trong `try`, bắt `json.JSONDecodeError`.

**Thuật toán:**
1. Khai báo chuỗi JSON hỏng.
2. `try`: parse; `except json.JSONDecodeError`: in thông báo.
3. In dòng tiếp theo để chứng minh chương trình vẫn chạy.

**Code:**

```python
import json

# Chuỗi JSON hỏng: thiếu giá trị của khóa "diem"
chuoi_hong = '{"ten": "An", "diem": }'

try:
    du_lieu = json.loads(chuoi_hong)     # ném JSONDecodeError
    print("Doc thanh cong:", du_lieu)
except json.JSONDecodeError:
    print("JSON loi: chuoi khong hop le")

print("Chuong trinh van chay tiep binh thuong")
```

**Giải thích code:**
* `json.JSONDecodeError` — đúng loại lỗi `.json()` của requests ném.
* Bắt lỗi giúp chương trình không sập khi dữ liệu xấu — nền tảng cho mọi code gọi API.

**Độ phức tạp:** O(n).

---

### Bài 7: POST với JSON — httpbin (chạy được)

**Phân tích:** POST gửi dữ liệu lên server; `json=` tự chuyển dict thành JSON.

**Ý tưởng:** `requests.post(url, json=du_lieu, timeout=10)`; đọc lại từ `phong_hoi.json()["json"]`.

**Thuật toán:**
1. Khai báo dữ liệu cần gửi.
2. `requests.post` với `json`.
3. Kiểm tra status, in dữ liệu server trả lại.

**Code:**

```python
# Cài đặt trước: pip install requests
import requests

# Dữ liệu gửi lên server
du_lieu = {"ten": "An", "diem": 8}

phong_hoi = requests.post(
    "https://httpbin.org/post",
    json=du_lieu,          # tự chuyển dict -> JSON
    timeout=10,
)

if phong_hoi.status_code == 200:
    # httpbin trả về đúng dữ liệu nó nhận được ở khóa "json"
    print("Status:", phong_hoi.status_code)
    print("Server nhan:", phong_hoi.json()["json"])
else:
    print("Loi:", phong_hoi.status_code)
```

**Giải thích code:**
* `json=du_lieu` — requests tự `json.dumps`, đặt header `Content-Type: application/json`.
* `phong_hoi.json()["json"]` — httpbin lặp lại dữ liệu đã nhận — giúp ta "nhìn thấy" dữ liệu gửi đi.

**Độ phức tạp:** Phụ thuộc mạng.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Tìm học viên trong JSON mô phỏng (Mô phỏng)

**Phân tích:** Dữ liệu từ API là chuỗi JSON → chuyển list dict, tìm kiếm giống bài 34.

**Ý tưởng:** `json.loads` trả list; hàm tìm theo id; trả về hoặc in thông báo.

**Thuật toán:**
1. Parse chuỗi JSON → list dict.
2. Hàm tìm theo id.
3. Gọi với id 2 và 99.

**Code:**

```python
import json

# Chuỗi JSON mô phỏng danh sách học viên từ API
chuoi_json = '''[
    {"id": 1, "ten": "An", "diem": 8},
    {"id": 2, "ten": "Binh", "diem": 7},
    {"id": 3, "ten": "Chi", "diem": 9}
]'''

hoc_sinh = json.loads(chuoi_json)      # -> list dict

def tim_hoc_sinh(id):
    """Tìm học sinh theo id."""
    for hs in hoc_sinh:
        if hs["id"] == id:
            return hs                    # tìm thấy
    return None                          # không tìm thấy

hs = tim_hoc_sinh(2)
if hs:
    print(f"{hs['ten']} - {hs['diem']} diem")
else:
    print("Khong tim thay")

hs = tim_hoc_sinh(99)
if hs:
    print(f"{hs['ten']} - {hs['diem']} diem")
else:
    print("Khong tim thay")
```

**Giải thích code:**
* `json.loads` — dữ liệu API thành list dict sẵn sàng dùng.
* Hàm trả `None` khi không có — kiểm tra bằng `if hs:` (None là falsy, bài 6).
* Đây chính là bước "xử lý dữ liệu sau khi GET" trong thực tế.

**Độ phức tạp:** O(n) với n là số học viên.

---

### Bài 9: Thời tiết Hà Nội — Open-Meteo (chạy được)

**Phân tích:** Áp dụng đúng quy trình: GET + params + timeout + đọc JSON lồng nhau.

**Ý tưởng:** Gọi Open-Meteo với tọa độ Hà Nội, lấy `current_weather`.

**Thuật toán:**
1. Khai báo URL và params.
2. `requests.get` với params, timeout.
3. `.json()`, rút `current_weather`, in 3 thông tin.

**Code:**

```python
# Cài đặt trước: pip install requests
import requests

# Tọa độ Hà Nội
url = "https://api.open-meteo.com/v1/forecast"
tham_so = {
    "latitude": 21.0285,
    "longitude": 105.8542,
    "current_weather": True,     # True được chuyển thành true trong URL
}

phong_hoi = requests.get(url, params=tham_so, timeout=10)
du_lieu = phong_hoi.json()       # phân tích JSON

cw = du_lieu["current_weather"]  # dict con
print(f"Thoi diem: {cw['time']}")
print(f"Nhiet do : {cw['temperature']}°C")
print(f"Gio      : {cw['windspeed']} km/h")
```

**Giải thích code:**
* `params` — thay vì tự nối `?latitude=21.0285&...`, requests làm hộ.
* `phong_hoi.json()` — thay cho `json.loads` (khi server trả JSON hợp lệ).
* Truy cập 2 tầng: `du_lieu` → `current_weather` → giá trị.

**Độ phức tạp:** Phụ thuộc mạng.

---

### Bài 10: Tính tổng tiền đơn hàng từ JSON (Mô phỏng)

**Phân tích:** Đọc list dict từ chuỗi JSON, tính `gia * so_luong` và cộng dồn.

**Ý tưởng:** Vòng lặp từng món, ép `float` cho giá.

**Thuật toán:**
1. Parse chuỗi JSON → list.
2. Với mỗi món: tính thành tiền, in, cộng vào tổng.
3. In tổng cộng.

**Code:**

```python
import json

# Chuỗi JSON mô phỏng phản hồi API đơn hàng
chuoi_json = '''[
    {"ten": "Vo", "gia": 5000, "so_luong": 3},
    {"ten": "But", "gia": 3000, "so_luong": 5},
    {"ten": "Sach", "gia": 25000, "so_luong": 1}
]'''

don_hang = json.loads(chuoi_json)

tong = 0
for mon in don_hang:
    thanh_tien = float(mon["gia"]) * int(mon["so_luong"])   # ép kiểu
    print(f"{mon['ten']}: {thanh_tien}")
    tong += thanh_tien

print("Tong:", tong)
```

**Giải thích code:**
* `float(mon["gia"])` — JSON không phân biệt `5000` là số hay chữ; ép kiểu để chắc chắn (bài 33).
* `tong += thanh_tien` — cộng dồn.

**Độ phức tạp:** O(n) với n là số món.

---

### Bài 11: Xử lý lỗi mạng mô phỏng — timeout và mất kết nối (Mô phỏng)

**Phân tích:** Dạy đúng cấu trúc `try/except` của requests khi không có mạng — giả lập ngoại lệ bằng `raise`.

**Ý tưởng:** Hàm giả `requests.get`: tùy URL mà nâng `Timeout` hoặc `ConnectionError`; bên gọi bắt cả hai.

**Thuật toán:**
1. Định nghĩa `goi_api_an_toan(url)` mô phỏng.
2. Trong hàm: `raise` ngoại lệ tương ứng theo nội dung URL.
3. Bên ngoài `try/except` bắt lần lượt Timeout, ConnectionError.

**Code:**

```python
# Cài đặt trước: pip install requests
import requests

def goi_api_an_toan(url):
    """Mô phỏng lời gọi requests: URL chứa 'cham'/'loi' sẽ giả lập lỗi mạng."""
    if "cham" in url:
        raise requests.exceptions.Timeout("qua thoi gian cho 10 giay")
    if "loi" in url:
        raise requests.exceptions.ConnectionError("khong ket noi duoc")
    return 200, {"ok": True}

# Kiểm tra 3 tình huống
for url in ["https://api.example.com/nhanh",
            "https://api.example.com/cham",
            "https://api.example.com/loi"]:
    try:
        status, du_lieu = goi_api_an_toan(url)
        print(f"OK: {status} {du_lieu}")
    except requests.exceptions.Timeout:
        print("Het thoi gian cho (timeout)")
    except requests.exceptions.ConnectionError:
        print("Mat ket noi mang")
```

**Giải thích code:**
* `raise requests.exceptions.Timeout(...)` — tạo ngoại lệ đúng loại requests thật ném.
* Thứ tự `except` — bắt Timeout trước, ConnectionError sau; cả hai kế thừa `RequestException`.
* Cấu trúc này y hệt khi gọi mạng thật — chỉ khác nguồn ngoại lệ.

**Độ phức tạp:** O(1).

---

### Bài 12: Kiểm tra status trước khi đọc dữ liệu (Mô phỏng)

**Phân tích:** Nguyên tắc vàng bài 34–35: status trước, dữ liệu sau — không gọi `.json()` khi có lỗi.

**Ý tưởng:** Hàm `xu_ly_phong_hoi` rẽ nhánh theo status; chỉ parse JSON ở nhánh 200.

**Thuật toán:**
1. Định nghĩa hàm nhận `(status, chuoi_json)`.
2. `if/elif/else` theo 4 mã.
3. Gọi thử 4 trường hợp.

**Code:**

```python
import json

def xu_ly_phong_hoi(status, chuoi_json):
    """Xử lý phản hồi: chỉ parse chuỗi JSON khi status là 200."""
    if status == 200:
        du_lieu = json.loads(chuoi_json)
        print("Thanh cong:", du_lieu)
    elif status == 400:
        print("Loi: yeu cau sai")
    elif status == 404:
        print("Loi: khong tim thay")
    elif status == 500:
        print("Loi: may chu")

xu_ly_phong_hoi(200, '{"ok": true}')
xu_ly_phong_hoi(400, "{}")
xu_ly_phong_hoi(404, "{}")
xu_ly_phong_hoi(500, "{}")
```

**Giải thích code:**
* `json.loads` chỉ gọi khi 200 — tránh lỗi khi server trả HTML/lỗi.
* Đây chính là điều kiện `if response.status_code == 200` bạn sẽ viết trong ứng dụng thật.

**Độ phức tạp:** O(1).

---

### Bài 13: Xử lý phản hồi lỗi của API (Mô phỏng)

**Phân tích:** Nhiều API (kể cả Open-Meteo) trả status 200 kèm dữ liệu lỗi — phải kiểm tra nội dung JSON, không chỉ status.

**Ý tưởng:** Kiểm tra khóa `"error"` sau khi parse.

**Thuật toán:**
1. Parse chuỗi JSON.
2. `if "error" in du_lieu`: in thông báo lỗi; ngược lại in dữ liệu.
3. Gọi với 2 chuỗi.

**Code:**

```python
import json

def xu_ly(chuoi_json):
    """Xử lý JSON phản hồi — phát hiện lỗi do API báo qua khóa error."""
    du_lieu = json.loads(chuoi_json)
    if "error" in du_lieu:
        print(f"API bao loi: {du_lieu['error']}")
    elif "temperature" in du_lieu:
        print(f"Nhiet do: {du_lieu['temperature']}")
    else:
        print("Khong ro du lieu")

xu_ly('{"error": "Khong co du lieu"}')
xu_ly('{"temperature": 30.2}')
```

**Giải thích code:**
* `"error" in du_lieu` — kiểm tra khóa tồn tại trước khi truy cập (bài 17).
* Kiểm tra cả status **và** nội dung — hai lớp phòng thủ khi gọi API thật.

**Độ phức tạp:** O(n).

---

### Bài 14: Phân tích phản hồi Open-Meteo lồng nhau (Mô phỏng)

**Phân tích:** Dữ liệu thật của Open-Meteo có nhiều tầng; rút biến con cho gọn.

**Ý tưởng:** `json.loads` → `cw = du_lieu["current_weather"]` → in 4 thông tin.

**Thuật toán:**
1. Parse chuỗi JSON lồng nhau.
2. Rút dict con `current_weather`.
3. In thời điểm, nhiệt độ, gió, mã thời tiết.

**Code:**

```python
import json

chuoi_json = '''{
    "timezone": "Asia/Bangkok",
    "current_weather": {
        "time": "2026-08-05T09:00",
        "temperature": 30.2,
        "windspeed": 11.5,
        "weathercode": 1
    }
}'''

du_lieu = json.loads(chuoi_json)
cw = du_lieu["current_weather"]

print(f"Thoi diem: {cw['time']}")
print(f"Nhiet do : {cw['temperature']}°C")
print(f"Gio      : {cw['windspeed']} km/h")
print(f"Ma thoi tiet: {cw['weathercode']}")
```

**Giải thích code:**
* `cw = du_lieu["current_weather"]` — biến ngắn, tránh viết lặp chuỗi khóa dài.
* Cấu trúc này giống hệt khi gọi API thật — bài 15 sẽ dùng lại.

**Độ phức tạp:** O(n).

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Hàm lấy thời tiết theo thành phố — Open-Meteo (chạy được)

**Phân tích:** Gói toàn bộ quy trình: params, timeout, kiểm tra status, try/except — vào một hàm tái sử dụng.

**Ý tưởng:** Hàm trả chuỗi mô tả hoặc thông báo lỗi; không bao giờ ném ngoại lệ ra ngoài.

**Thuật toán:**
1. Khai báo URL cố định.
2. `params` từ tọa độ.
3. `try`: GET với timeout; kiểm tra status; `.json()`; tạo chuỗi kết quả.
4. `except` 3 loại ngoại lệ → trả chuỗi lỗi.
5. Gọi với Hà Nội.

**Code:**

```python
# Cài đặt trước: pip install requests
import requests

def lay_thoi_tiet(ten_thanh_pho, vi_do, kinh_do):
    """Gọi Open-Meteo, trả chuỗi mô tả thời tiết hoặc thông báo lỗi."""
    url = "https://api.open-meteo.com/v1/forecast"
    tham_so = {
        "latitude": vi_do,
        "longitude": kinh_do,
        "current_weather": True,
    }
    try:
        phong_hoi = requests.get(url, params=tham_so, timeout=10)
        if phong_hoi.status_code != 200:                 # status trước
            return f"{ten_thanh_pho}: loi {phong_hoi.status_code}"

        cw = phong_hoi.json()["current_weather"]         # dữ liệu sau
        return (f"{ten_thanh_pho}: {cw['temperature']}°C, "
                f"gio {cw['windspeed']} km/h")
    except requests.exceptions.Timeout:
        return f"{ten_thanh_pho}: het thoi gian cho"
    except requests.exceptions.ConnectionError:
        return f"{ten_thanh_pho}: mat ket noi mang"
    except requests.exceptions.RequestException as loi:
        return f"{ten_thanh_pho}: loi khac {loi}"

# Gọi thử với Hà Nội
print(lay_thoi_tiet("Ha Noi", 21.0285, 105.8542))
```

**Giải thích code:**
* Kiểm tra `status_code != 200` trước khi chạm `.json()` — tránh JSONDecodeError.
* `except requests.exceptions.RequestException` cuối cùng — lưới an toàn mọi lỗi còn lại.
* Hàm luôn trả chuỗi — chương trình chính không bao giờ sập vì mạng.

**Độ phức tạp:** Phụ thuộc mạng.

---

### Bài 16: Nhiệt độ trung bình một tuần từ JSON (Mô phỏng)

**Phân tích:** Dữ liệu `daily` chứa hai list song song (time và nhiệt độ) — cần duyệt theo chỉ số chung.

**Ý tưởng:** Parse, tính TB của `temperature_2m_max`, tìm vị trí max và ngày tương ứng.

**Thuật toán:**
1. Parse chuỗi JSON → dict `daily`.
2. Tính TB của `temperature_2m_max`.
3. Tìm chỉ số ngày nóng nhất (hàm `index` của max).
4. In kết quả.

**Code:**

```python
import json

chuoi_json = '''{
    "daily": {
        "time": ["2026-08-01", "2026-08-02", "2026-08-03",
                 "2026-08-04", "2026-08-05", "2026-08-06", "2026-08-07"],
        "temperature_2m_max": [30, 31, 29, 33, 32, 34, 28]
    }
}'''

du_lieu = json.loads(chuoi_json)
daily = du_lieu["daily"]
nhiet = daily["temperature_2m_max"]

# Nhiệt độ trung bình
tb = sum(nhiet) / len(nhiet)
print(f"Nhiet do TB tuan: {round(tb, 1)}°C")

# Ngày nóng nhất
nhiet_max = max(nhiet)                        # giá trị cao nhất
chi_so = nhiet.index(nhiet_max)               # vị trí của giá trị đó
ngay_nong = daily["time"][chi_so]             # ngày tương ứng cùng vị trí
print(f"Ngay nong nhat: {ngay_nong} ({nhiet_max}°C)")
```

**Giải thích code:**
* `sum(nhiet) / len(nhiet)` — trung bình cộng; `round(x, 1)` giữ 1 chữ số.
* `nhiet.index(max(nhiet))` — tìm **vị trí** của giá trị lớn nhất, rồi lấy ngày cùng vị trí từ list `time`.

**Độ phức tạp:** O(n) với n = 7 ngày.

---

### Bài 17: Chương trình kiểm tra kết nối — httpbin (chạy được)

**Phân tích:** `raise_for_status()` giúp biến mã lỗi thành ngoại lệ `HTTPError` — xử lý gọn hơn if thủ công.

**Ý tưởng:** Gọi `requests.get`, gọi `raise_for_status()` trong try; bắt `HTTPError` và in mã lỗi từ `loi.response.status_code`.

**Thuật toán:**
1. Import requests.
2. Với mỗi URL 404, 500: gọi GET timeout.
3. `try`: `raise_for_status()`, in OK.
4. `except requests.exceptions.HTTPError`: in mã lỗi.

**Code:**

```python
# Cài đặt trước: pip install requests
import requests

urls = [
    "https://httpbin.org/status/404",
    "https://httpbin.org/status/500",
]

for url in urls:
    try:
        phong_hoi = requests.get(url, timeout=10)
        # Nếu mã 4xx/5xx, lệnh này ném HTTPError (chương trình không sập)
        phong_hoi.raise_for_status()
        print("OK:", url)
    except requests.exceptions.HTTPError as loi:
        # loi.response chứa phản hồi gốc -> lấy mã lỗi
        ma_loi = loi.response.status_code
        print(f"Loi {ma_loi}: {url}")
```

**Giải thích code:**
* `raise_for_status()` — không làm gì khi 2xx, ném `HTTPError` khi 4xx/5xx.
* `loi.response.status_code` — ngoại lệ chứa phản hồi gốc, lấy được mã lỗi chính xác.
* Chương trình in `Loi 404: ...` và `Loi 500: ...` rồi tiếp tục chạy.

**Độ phức tạp:** Phụ thuộc mạng.

---

### Bài 18: So sánh thời tiết Hà Nội và TP.HCM — Open-Meteo (chạy được)

**Phân tích:** Tái sử dụng hàm lấy thời tiết, nhưng cần nhiệt độ **dạng số** để so sánh.

**Ý tưởng:** Viết hàm phụ trả cặp `(ten, nhiet_do_float)`; so sánh và in kết luận.

**Thuật toán:**
1. Hàm `get_nhiet_do(ten, vi_do, kinh_do)` trả `(ten, float)` hoặc `None`.
2. Gọi cho Hà Nội và TP.HCM.
3. So sánh, in kết luận.

**Code:**

```python
# Cài đặt trước: pip install requests
import requests

def get_nhiet_do(ten, vi_do, kinh_do):
    """Gọi Open-Meteo, trả (tên thành phố, nhiệt độ float) hoặc None."""
    url = "https://api.open-meteo.com/v1/forecast"
    tham_so = {"latitude": vi_do, "longitude": kinh_do, "current_weather": True}
    try:
        phong_hoi = requests.get(url, params=tham_so, timeout=10)
        if phong_hoi.status_code != 200:
            return None
        nhiet_do = phong_hoi.json()["current_weather"]["temperature"]
        return ten, float(nhiet_do)
    except requests.exceptions.RequestException:
        return None

# Tọa độ hai thành phố
ha_noi = get_nhiet_do("Ha Noi", 21.0285, 105.8542)
tp_hcm = get_nhiet_do("TP HCM", 10.8231, 106.6297)

if ha_noi and tp_hcm:
    ten_1, nhiet_1 = ha_noi
    ten_2, nhiet_2 = tp_hcm
    if nhiet_1 > nhiet_2:
        print(f"{ten_1} nong hon {ten_2} ({nhiet_1} vs {nhiet_2})")
    elif nhiet_1 < nhiet_2:
        print(f"{ten_2} nong hon {ten_1} ({nhiet_2} vs {nhiet_1})")
    else:
        print(f"{ten_1} va {ten_2} bang nhau ({nhiet_1})")
else:
    print("Khong lay duoc du lieu thoi tiet")
```

**Giải thích code:**
* `float(nhiet_do)` — bảo đảm so sánh số, không so chuỗi.
* `if ha_noi and tp_hcm` — kết quả có thể là `None` khi mạng lỗi — kiểm tra trước khi giải nén.
* Kiểm tra `status_code`, bắt `RequestException` — hàm trả `None` thay vì sập.

**Độ phức tạp:** Phụ thuộc mạng (2 yêu cầu GET).

---

### Bài 19: Sắp xếp và lọc dữ liệu từ JSON mô phỏng (Mô phỏng)

**Phân tích:** Hai thao tác dữ liệu phổ biến sau khi GET: lọc theo điều kiện và sắp xếp theo khóa.

**Ý tưởng:** List comprehension lọc `5000 <= gia <= 20000`; `sorted` với `key=lambda`.

**Thuật toán:**
1. Parse chuỗi JSON → list dict.
2. Lọc và in các sản phẩm trong khoảng giá.
3. Sắp xếp giảm dần theo giá, in lại toàn bộ.

**Code:**

```python
import json

chuoi_json = '''[
    {"ten": "Vo", "gia": 5000}, {"ten": "But", "gia": 3000},
    {"ten": "Sach", "gia": 25000}, {"ten": "Thuoc ke", "gia": 15000}
]'''

san_pham = json.loads(chuoi_json)

# Lọc sản phẩm giá từ 5000 đến 20000
loc = [sp for sp in san_pham if 5000 <= int(sp["gia"]) <= 20000]
print("San pham trong khoang gia:")
for sp in loc:
    print(f"- {sp['ten']}: {sp['gia']}")

# Sắp xếp giảm dần theo giá
sap_xep = sorted(san_pham, key=lambda sp: int(sp["gia"]), reverse=True)
print("Sap xep giam dan theo gia:")
for sp in sap_xep:
    print(f"- {sp['ten']}: {sp['gia']}")
```

**Giải thích code:**
* List comprehension (bài 26) kết hợp điều kiện — lọc gọn một dòng.
* `sorted(..., key=lambda sp: int(sp["gia"]), reverse=True)` — sắp theo khóa, giảm dần (lambda — bài 25).
* Kết quả lọc: Vo, Thuoc ke; sắp xếp: Sach → Thuoc ke → Vo → But.

**Độ phức tạp:** O(n log n) do `sorted`.

---

### Bài 20: Mini Project — Tra cứu thời tiết nhiều thành phố (chạy được)

**Phân tích:** Bài tổng hợp toàn chương: dict thành phố, hàm gọi API an toàn, vòng lặp, tìm max/min, in bảng đẹp.

**Ý tưởng:** Mỗi lần gọi API lưu một dict kết quả vào list; sau vòng lặp phân tích để kết luận.

**Thuật toán:**
1. Dict thành phố (tên → tọa độ).
2. Hàm `lay_thoi_tiet` an toàn trả dict hoặc None.
3. Vòng lặp gọi từng thành phố, in bảng.
4. Lọc kết quả hợp lệ, tìm nóng nhất/lạnh nhất.

**Code:**

```python
# Cài đặt trước: pip install requests
import requests

# Dict thành phố: tên -> (vĩ độ, kinh độ)
thanh_pho = {
    "Ha Noi": (21.0285, 105.8542),
    "TP HCM": (10.8231, 106.6297),
    "Da Nang": (16.0544, 108.2022),
}

def lay_thoi_tiet(ten, vi_do, kinh_do):
    """Gọi Open-Meteo, trả dict {'ten', 'nhiet', 'gio'} hoặc None."""
    url = "https://api.open-meteo.com/v1/forecast"
    tham_so = {"latitude": vi_do, "longitude": kinh_do, "current_weather": True}
    try:
        phong_hoi = requests.get(url, params=tham_so, timeout=10)
        if phong_hoi.status_code != 200:
            return None
        cw = phong_hoi.json()["current_weather"]
        return {"ten": ten,
                "nhiet": float(cw["temperature"]),
                "gio": float(cw["windspeed"])}
    except requests.exceptions.RequestException:
        return None

# Gọi và in bảng thời tiết
ket_qua = []
print(f"{'Thanh pho':<10}{'Nhiet do':<10}{'Gio'}")
for ten, (vi_do, kinh_do) in thanh_pho.items():
    du_lieu = lay_thoi_tiet(ten, vi_do, kinh_do)
    if du_lieu:
        ket_qua.append(du_lieu)
        print(f"{du_lieu['ten']:<10}{du_lieu['nhiet']:<10.1f}{du_lieu['gio']} km/h")
    else:
        print(f"{ten:<10}LOI ket noi")

# Kết luận nóng nhất / lạnh nhất
if ket_qua:
    nong_nhat = max(ket_qua, key=lambda k: k["nhiet"])
    lanh_nhat = min(ket_qua, key=lambda k: k["nhiet"])
    print(f"Nong nhat: {nong_nhat['ten']} ({nong_nhat['nhiet']}°C)")
    print(f"Lanh nhat: {lanh_nhat['ten']} ({lanh_nhat['nhiet']}°C)")
else:
    print("Khong lay duoc du lieu thanh pho nao")
```

**Giải thích code:**
* `thanh_pho.items()` — duyệt tên và tọa độ cùng lúc (bài 17).
* `key=lambda k: k["nhiet"]` — tìm max/min theo khóa nhiệt độ (bài 25).
* `f"{du_lieu['ten']:<10}"` — canh trái 10 ký tự cho bảng thẳng hàng.
* Hàm trả `None` khi lỗi — vòng lặp in "LOI ket noi" thay vì sập chương trình.

**Độ phức tạp:** Phụ thuộc mạng (3 yêu cầu GET) + O(m) phân tích.

---

## 📌 Lời khuyên cuối

* ⏱️ **Luôn đặt `timeout`** (5–10 giây) — chương trình không bao giờ "đứng hình".
* 🚦 **Kiểm tra status trước, `.json()` sau** — tránh JSONDecodeError.
* 🛡️ **try/except là bắt buộc** khi chạm mạng: Timeout, ConnectionError, RequestException.
* 🧪 **Luyện offline bằng chuỗi JSON mô phỏng** — tư duy xử lý giống hệt dữ liệu thật.
* 🌏 **Open-Meteo miễn phí, không key** — cứ luyện thời tiết Hà Nội thỏa thích.

👉 Tiếp theo: **[Bài 36: SQLite – Cơ Sở Dữ Liệu Trong Python](../36_SQLite/bai_giang.md)**