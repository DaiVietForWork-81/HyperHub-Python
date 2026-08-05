# ✅ Bài 34: Đáp Án – API

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án. Toàn bộ đáp án bài này **mô phỏng** máy chủ API bằng hàm — không cần internet, chạy được ngay trên máy bạn.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: In bảng 4 phương thức HTTP

**Phân tích:** Bốn phương thức HTTP và hành động tương ứng là dữ liệu dạng cặp giá trị — lưu vào list tuple.

**Ý tưởng:** Duyệt list tuple và in theo định dạng.

**Thuật toán:**
1. Tạo list `(ten, hanh_dong)` cho 4 phương thức.
2. Vòng `for` in từng cặp.

**Code:**

```python
# Danh sách 4 phương thức HTTP kèm hành động
phuong_thuc = [
    ("GET", "Lay du lieu"),
    ("POST", "Tao du lieu moi"),
    ("PUT", "Cap nhat du lieu"),
    ("DELETE", "Xoa du lieu"),
]

for ten, hanh_dong in phuong_thuc:
    print(f"{ten} - {hanh_dong}")
```

**Giải thích code:**
* Mỗi phần tử là tuple `(ten, hanh_dong)` — nhớ 4 phương thức HTTP là kiến thức cốt lõi của bài.
* `for ten, hanh_dong in phuong_thuc` — giải nén tuple trong vòng lặp.
* `f"{ten} - {hanh_dong}"` — f-string nối chuỗi (bài 18).

**Độ phức tạp:** O(1) — chỉ 4 phần tử cố định.

---

### Bài 2: Tách URL thành endpoint và tham số

**Phân tích:** URL có cấu trúc `endpoint?thamso` — dấu `?` là ranh giới.

**Ý tưởng:** `split("?")` cắt chuỗi tại dấu `?`.

**Thuật toán:**
1. Khai báo URL.
2. `split("?")` → list 2 phần tử.
3. In endpoint và tham số.

**Code:**

```python
# URL API thời tiết (bài 35 sẽ gọi thật bằng requests)
url = "https://api.open-meteo.com/v1/forecast?latitude=21.0285&longitude=105.8542&current_weather=true"

endpoint, tham_so = url.split("?")   # cắt tại dấu chấm hỏi

print("Endpoint:", endpoint)
print("Tham so :", tham_so)
```

**Giải thích code:**
* `url.split("?")` — trả list `["https://...forecast", "latitude=21.0285&..."]`.
* `endpoint, tham_so = ...` — giải nén đúng 2 phần tử.
* Tham số gồm các cặp `khóa=giá trị` ngăn cách bằng `&` — kỹ năng đọc URL cần thiết để tự tra tài liệu API.

**Độ phức tạp:** O(n) với n là độ dài URL.

---

### Bài 3: In thực đơn của "API nhà hàng"

**Phân tích:** Thực đơn là list dict; cần in kèm số thứ tự bắt đầu từ 1.

**Ý tưởng:** `enumerate(list, start=1)` tạo số thứ tự.

**Thuật toán:**
1. Tạo list 3 dict món ăn.
2. `enumerate` từ 1, in `stt. ten - gia dong`.

**Code:**

```python
# Thực đơn nhà hàng (mô phỏng dữ liệu từ server)
thuc_don = [
    {"ten": "Pho bo", "gia": 50000},
    {"ten": "Bun cha", "gia": 45000},
    {"ten": "Com tam", "gia": 60000},
]

for stt, mon in enumerate(thuc_don, start=1):
    print(f"{stt}. {mon['ten']} - {mon['gia']} dong")
```

**Giải thích code:**
* `enumerate(thuc_don, start=1)` — trả cặp `(số thứ tự, món)`; mặc định bắt đầu 0 nên phải `start=1`.
* `mon['ten']`, `mon['gia']` — truy cập khóa của dict (bài 17).

**Độ phức tạp:** O(n) với n là số món.

---

### Bài 4: Giải thích status code

**Phân tích:** Ánh xạ số → chuỗi; một số mã có thể không nằm trong danh sách — cần nhánh mặc định.

**Ý tưởng:** Hàm `y_nghia(ma)` với `if/elif/else`.

**Thuật toán:**
1. Định nghĩa hàm trả về chuỗi theo mã.
2. Gọi hàm với 6 mã và in.

**Code:**

```python
def y_nghia(ma):
    """Tra cứu ý nghĩa của một status code."""
    if ma == 200:
        return "Thanh cong (OK)"
    if ma == 201:
        return "Da tao moi"
    if ma == 400:
        return "Loi yeu cau"
    if ma == 404:
        return "Khong tim thay"
    if ma == 500:
        return "Loi may chu"
    return "Khong ro"          # mã chưa biết

# Kiểm tra các mã quan trọng
for ma in [200, 201, 400, 404, 500, 302]:
    print(f"{ma}: {y_nghia(ma)}")
```

**Giải thích code:**
* Mỗi `if` trả về ngay — không cần `elif` cũng đúng vì mỗi mã khác nhau.
* `return "Khong ro"` cuối cùng — bẫy mọi mã không nằm trong danh sách (302, 503...).
* Vòng lặp in 6 dòng: 302 không có trong bảng nên ra `"Khong ro"`.

**Độ phức tạp:** O(1) mỗi lần tra cứu.

---

### Bài 5: Đọc JSON mô phỏng phản hồi thời tiết

**Phân tích:** Server trả dữ liệu dạng chuỗi JSON; Python cần `json.loads` để biến thành dict (bài 32).

**Ý tưởng:** Parse chuỗi, lấy khóa `temperature`, `windspeed`, in ra.

**Thuật toán:**
1. `import json`.
2. Khai báo chuỗi JSON.
3. `json.loads` → dict, in giá trị.

**Code:**

```python
import json

# Chuỗi JSON mô phỏng phản hồi API thời tiết
chuoi_json = '{"temperature": 30.2, "windspeed": 11.5}'

du_lieu = json.loads(chuoi_json)     # chuỗi JSON -> dict Python

print(f"Nhiet do: {du_lieu['temperature']}°C")
print(f"Gio: {du_lieu['windspeed']} km/h")
```

**Giải thích code:**
* `json.loads(chuoi_json)` — chuỗi → dict `{"temperature": 30.2, "windspeed": 11.5}`.
* `du_lieu['temperature']` — lấy giá trị theo khóa; `°C` là ký tự Unicode in trực tiếp.

**Độ phức tạp:** O(n) với n là độ dài chuỗi.

---

### Bài 6: Bắt lỗi JSON hỏng

**Phân tích:** Dữ liệu từ bên ngoài (mạng) có thể hỏng — chương trình phải tự bảo vệ bằng `try/except`.

**Ý tưởng:** Đặt `json.loads` trong `try`, bắt `json.JSONDecodeError` trong `except`.

**Thuật toán:**
1. Khai báo chuỗi JSON hỏng.
2. `try`: parse và in.
3. `except`: in thông báo lỗi.

**Code:**

```python
import json

# Chuỗi JSON hỏng: thiếu giá trị của khóa "diem"
chuoi_json = '{"ten": "An", "diem": }'

try:
    du_lieu = json.loads(chuoi_json)   # dòng này sẽ ném lỗi
    print("Dọc thanh cong:", du_lieu)
except json.JSONDecodeError:
    print("JSON loi: chuoi khong hop le")
```

**Giải thích code:**
* `json.loads` gặp chuỗi hỏng sẽ ném ngoại lệ `JSONDecodeError`.
* `except json.JSONDecodeError:` — bắt đúng loại lỗi, in thông báo thân thiện thay vì để chương trình sập.
* Kỹ thuật này là nền tảng cho bài 35 khi nhận dữ liệu từ API thật.

**Độ phức tạp:** O(n).

---

### Bài 7: Mô phỏng "máy chủ" trả dữ liệu có status code

**Phân tích:** Server trả về **2 thứ**: status code và dữ liệu — mô phỏng bằng tuple.

**Ý tưởng:** Hàm kiểm tra món có trong thực đơn hay không rồi trả tuple khác nhau.

**Thuật toán:**
1. Khai báo thực đơn.
2. Hàm `phuc_vu(mon)`: có → `(200, ...)`, không → `(404, ...)`.
3. Gọi với 2 món và in.

**Code:**

```python
# Thực đơn của "API nhà hàng"
thuc_don = ["Pho bo", "Bun cha"]

def phuc_vu(mon):
    """Mô phỏng server: trả (status code, thông báo)."""
    if mon in thuc_don:
        return 200, f"Co mon: {mon}"     # thành công
    return 404, f"Khong co mon: {mon}"   # không tìm thấy

for mon in ["Pho bo", "Banh my"]:
    status, thong_bao = phuc_vu(mon)     # giải nén tuple
    print(f"{status} - {thong_bao}")
```

**Giải thích code:**
* `mon in thuc_don` — kiểm tra tồn tại trong list (bài 14).
* `return 200, f"..."` — trả tuple 2 phần tử; `status, thong_bao = ...` giải nén.
* Đây là mô hình đúng của mọi API thật: luôn có status + dữ liệu.

**Độ phức tạp:** O(n) do `in` duyệt list.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Mô phỏng GET — tìm học sinh theo mã số

**Phân tích:** GET theo id: duyệt tìm khớp id; có → trả dữ liệu, không → 404.

**Ý tưởng:** Vòng `for` tìm `hs["id"] == id`, trả `(200, hs)` ngay khi thấy; hết vòng mà chưa thấy trả `(404, None)`.

**Thuật toán:**
1. Khai báo danh sách 3 học sinh.
2. Hàm `get_hoc_sinh(id)` duyệt tìm.
3. Gọi với id 2 và 99, in kết quả.

**Code:**

```python
# "Cơ sở dữ liệu" mô phỏng
hoc_sinh = [
    {"id": 1, "ten": "An", "lop": "10A1"},
    {"id": 2, "ten": "Binh", "lop": "10A2"},
    {"id": 3, "ten": "Chi", "lop": "10A1"},
]

def get_hoc_sinh(id):
    """Mô phỏng GET: trả (status, dữ liệu) theo id."""
    for hs in hoc_sinh:
        if hs["id"] == id:
            return 200, hs          # tìm thấy
    return 404, None                # không tìm thấy

for id_kiem_tra in [2, 99]:
    status, du_lieu = get_hoc_sinh(id_kiem_tra)
    print(f"GET id {id_kiem_tra}: status {status}, du lieu {du_lieu}")
```

**Giải thích code:**
* `return 200, hs` trong vòng lặp — dừng ngay khi tìm thấy, không duyệt tiếp.
* `return 404, None` sau vòng lặp — chỉ chạy khi không tìm thấy (không có return nào trước đó).
* `None` đại diện "không có dữ liệu" — giống phản hồi JSON rỗng của API thật.

**Độ phức tạp:** O(n) với n là số học sinh.

---

### Bài 9: Mô phỏng POST — thêm học sinh mới

**Phân tích:** POST tạo dữ liệu mới; server tự sinh id (id lớn nhất + 1) và trả status **201** — khác GET ở chỗ tài nguyên vừa được tạo.

**Ý tưởng:** `max(...)` tìm id lớn nhất, thêm dict mới bằng `append`, trả `(201, dict)`.

**Thuật toán:**
1. Khai báo danh sách 2 học sinh (id 1, 2).
2. Hàm `post_hoc_sinh(ten, lop)`: sinh id, thêm, trả 201.
3. Gọi thử, in danh sách sau khi thêm.

**Code:**

```python
hoc_sinh = [
    {"id": 1, "ten": "An", "lop": "10A1"},
    {"id": 2, "ten": "Binh", "lop": "10A2"},
]

def post_hoc_sinh(ten, lop):
    """Mô phỏng POST: tạo học sinh mới, trả (201, dữ liệu mới)."""
    id_moi = max(hs["id"] for hs in hoc_sinh) + 1   # id lớn nhất + 1
    hs_moi = {"id": id_moi, "ten": ten, "lop": lop}
    hoc_sinh.append(hs_moi)                          # thêm vào "cơ sở dữ liệu"
    return 201, hs_moi

status, hs_moi = post_hoc_sinh("Dung", "10A2")
print(f"Status: {status}, da them: {hs_moi}")

print("Danh sach sau khi them:")
for hs in hoc_sinh:
    print(hs)
```

**Giải thích code:**
* `max(hs["id"] for hs in hoc_sinh)` — generator duyệt lấy id lớn nhất; `+ 1` sinh id mới.
* `append(hs_moi)` — thêm dict vào list; danh sách gốc thay đổi vì list là tham chiếu.
* Status `201` — "Created": khác 200, báo hiệu đã tạo tài nguyên mới.

**Độ phức tạp:** O(n) (max duyệt toàn danh sách).

---

### Bài 10: Mô phỏng PUT — cập nhật điểm

**Phân tích:** PUT sửa dữ liệu theo id — tìm rồi gán giá trị mới cho cột.

**Ý tưởng:** Tìm thấy → sửa `hs["diem"]`, trả `(200, hs)`; không → `(404, None)`.

**Thuật toán:**
1. Khai báo danh sách có cột `diem`.
2. Hàm `put_diem(id, diem_moi)` tìm và sửa.
3. Gọi với id có và không có.

**Code:**

```python
hoc_sinh = [
    {"id": 1, "ten": "An", "diem": 8},
    {"id": 2, "ten": "Binh", "diem": 7},
]

def put_diem(id, diem_moi):
    """Mô phỏng PUT: cập nhật điểm theo id."""
    for hs in hoc_sinh:
        if hs["id"] == id:
            hs["diem"] = diem_moi      # sửa trực tiếp trên dict
            return 200, hs             # sửa thành công
    return 404, None                   # không tìm thấy id

for id_kiem_tra in [1, 99]:
    status, du_lieu = put_diem(id_kiem_tra, 10)
    print(f"PUT id {id_kiem_tra}: status {status}, du lieu {du_lieu}")

print("Sau khi sua:", hoc_sinh)
```

**Giải thích code:**
* `hs["diem"] = diem_moi` — gán giá trị mới ngay trên dict đang có trong list — thay đổi có hiệu lực ngay.
* Trả `hs` sau khi sửa để client thấy dữ liệu mới — giống API thật.
* id 99 không tồn tại → 404.

**Độ phức tạp:** O(n).

---

### Bài 11: Mô phỏng DELETE — xóa học sinh

**Phân tích:** DELETE xóa phần tử khỏi danh sách theo id; không có → 404.

**Ý tưởng:** Tìm đối tượng, `list.remove()`; hoặc tạo list mới bằng comprehension rồi so sánh độ dài.

**Thuật toán:**
1. Khai báo danh sách 3 học sinh.
2. Hàm `delete_hoc_sinh(id)`: tìm và `remove`, trả 200; không → 404.
3. In danh sách còn lại.

**Code:**

```python
hoc_sinh = [
    {"id": 1, "ten": "An", "lop": "10A1"},
    {"id": 2, "ten": "Binh", "lop": "10A2"},
    {"id": 3, "ten": "Chi", "lop": "10A1"},
]

def delete_hoc_sinh(id):
    """Mô phỏng DELETE: xóa học sinh theo id."""
    for hs in hoc_sinh:
        if hs["id"] == id:
            hoc_sinh.remove(hs)        # xóa đối tượng khỏi danh sách
            return 200, f"Da xoa hoc sinh id {id}"
    return 404, None

status, thong_bao = delete_hoc_sinh(2)
print(f"Status: {status}, {thong_bao}")

print("Danh sach con lai:")
for hs in hoc_sinh:
    print(hs)
```

**Giải thích code:**
* `hoc_sinh.remove(hs)` — xóa theo **giá trị** (đối tượng), không phải vị trí.
* `return 200, ...` ngay trong vòng lặp — đảm bảo chỉ xóa đúng một phần tử rồi dừng.
* Danh sách cuối còn đúng 2 học sinh: An và Chi.

**Độ phức tạp:** O(n).

---

### Bài 12: Mô phỏng API thời tiết với tọa độ không hợp lệ

**Phân tích:** Giống Open-Meteo thật: kiểm tra dữ liệu đầu vào, sai → **400** (lỗi do client gửi yêu cầu hỏng).

**Ý tưởng:** Kiểm tra phạm vi tọa độ trước; đúng → 200, sai → 400.

**Thuật toán:**
1. Hàm `thoi_tiet(kinh_do, vi_do)` kiểm tra phạm vi.
2. Trả `(400, error)` hoặc `(200, data)`.
3. Gọi thử 2 cặp tọa độ.

**Code:**

```python
def thoi_tiet(kinh_do, vi_do):
    """Mô phỏng Open-Meteo: kiểm tra tọa độ, trả (status, dữ liệu)."""
    if not (-90 <= vi_do <= 90) or not (-180 <= kinh_do <= 180):
        return 400, {"error": "Toa do khong hop le"}
    return 200, {"temperature": 30.2}    # dữ liệu mô phỏng

# Tọa độ Hà Nội: hợp lệ
status, du_lieu = thoi_tiet(105.85, 21.03)
print(f"Status {status}: {du_lieu}")

# Vĩ độ 91: ngoài phạm vi -90..90
status, du_lieu = thoi_tiet(105.85, 91)
print(f"Status {status}: {du_lieu}")
```

**Giải thích code:**
* `not (-90 <= vi_do <= 90)` — phép so sánh chuỗi kép trong Python; `not` đảo ngược.
* `or` — chỉ cần một tọa độ sai là trả 400.
* Status 400 báo client "bạn gửi sai" — server không lỗi gì cả.

**Độ phức tạp:** O(1).

---

### Bài 13: Đọc JSON phản hồi lồng nhau

**Phân tích:** Dữ liệu `current_weather` nằm **trong** đối tượng gốc — truy cập hai tầng khóa.

**Ý tưởng:** `du_lieu["current_weather"]["temperature"]` — lấy dict con trước, khóa trong sau.

**Thuật toán:**
1. Khai báo chuỗi JSON lồng nhau.
2. `json.loads`, truy cập hai tầng cho từng thông tin.
3. In 4 dòng.

**Code:**

```python
import json

# Phản hồi mô phỏng đúng cấu trúc Open-Meteo
chuoi_json = '''{
    "current_weather": {
        "temperature": 30.2,
        "windspeed": 11.5,
        "time": "2026-08-05T09:00"
    },
    "timezone": "Asia/Bangkok"
}'''

du_lieu = json.loads(chuoi_json)
cw = du_lieu["current_weather"]      # rút gọn: dict con

print(f"Thoi diem: {cw['time']}")
print(f"Nhiet do : {cw['temperature']}°C")
print(f"Gio      : {cw['windspeed']} km/h")
print(f"Musi gio : {du_lieu['timezone']}")
```

**Giải thích code:**
* `du_lieu["current_weather"]` — lấy dict con, gán biến `cw` cho gọn.
* `cw['time']` — lấy giá trị tầng thứ hai.
* `du_lieu['timezone']` — khóa nằm tầng ngoài, truy cập trực tiếp.

**Độ phức tạp:** O(n) với n là độ dài chuỗi.

---

### Bài 14: Kiểm tra status trước khi đọc dữ liệu

**Phân tích:** Đọc dữ liệu chỉ hợp lệ khi status 200 — xử lý từng trạng thái riêng, giống cách bài 35 sẽ làm với `response.status_code`.

**Ý tưởng:** `if/elif/else` theo status; chỉ `json.loads` ở nhánh 200.

**Thuật toán:**
1. Hàm `xu_ly(status, chuoi_json)`.
2. 200 → parse và in dữ liệu; các mã khác → in thông báo tương ứng.
3. Gọi với 4 trường hợp.

**Code:**

```python
import json

def xu_ly(status, chuoi_json):
    """Xử lý phản hồi: chỉ đọc dữ liệu khi status là 200."""
    if status == 200:
        du_lieu = json.loads(chuoi_json)   # thành công mới parse JSON
        print("Thanh cong:", du_lieu)
    elif status == 400:
        print("Loi: yeu cau sai")
    elif status == 404:
        print("Loi: khong tim thay")
    elif status == 500:
        print("Loi: may chu")

# Kiểm tra 4 tình huống
xu_ly(200, '{"ok": true}')
xu_ly(400, "{}")
xu_ly(404, "{}")
xu_ly(500, "{}")
```

**Giải thích code:**
* `json.loads` chỉ nằm trong nhánh 200 — tránh parse dữ liệu lỗi.
* Các nhánh khác in thông báo phù hợp từng mã.
* Nguyên tắc "kiểm tra status trước, đọc dữ liệu sau" sẽ dùng nguyên vẹn ở bài 35.

**Độ phức tạp:** O(1).

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Xây dựng "mini API" quản lý thư viện

**Phân tích:** Bài tổng hợp 4 phương thức; tránh code trùng lặp bằng hàm nhỏ `tim_sach`.

**Ý tưởng:** Hàm `phuc_vu(phuong_thuc, du_lieu)` rẽ nhánh theo phương thức; mỗi nhánh trả `(status, dữ liệu)`.

**Thuật toán:**
1. Khai báo danh sách 2 sách.
2. Hàm `tim_sach(ds, id)` tái sử dụng cho PUT/DELETE.
3. `phuc_vu` xử lý GET (toàn bộ), POST, PUT, DELETE.
4. Chạy kịch bản kiểm tra.

**Code:**

```python
# "Cơ sở dữ liệu" thư viện
sach = [
    {"id": 1, "ten": "Dac Nhan Tam", "gia": 80000},
    {"id": 2, "ten": "Nha Gia Kim", "gia": 65000},
]

def tim_sach(ds, id):
    """Tìm sách theo id, trả dict hoặc None."""
    for cuon in ds:
        if cuon["id"] == id:
            return cuon
    return None

def phuc_vu(phuong_thuc, du_lieu=None):
    """Mô phỏng API thư viện: xử lý 4 phương thức HTTP."""
    if phuong_thuc == "GET":
        return 200, sach                          # trả toàn bộ danh sách

    if phuong_thuc == "POST":
        id_moi = max(c["id"] for c in sach) + 1   # sinh id tự tăng
        cuon_moi = {"id": id_moi, **du_lieu}
        sach.append(cuon_moi)
        return 201, cuon_moi                      # Created

    if phuong_thuc == "PUT":
        cuon = tim_sach(sach, du_lieu["id"])
        if cuon is None:
            return 404, None
        cuon["gia"] = du_lieu["gia"]              # cập nhật giá
        return 200, cuon

    if phuong_thuc == "DELETE":
        cuon = tim_sach(sach, du_lieu["id"])
        if cuon is None:
            return 404, None
        sach.remove(cuon)
        return 200, {"da_xoa": cuon["ten"]}

    return 405, {"error": "Phuong thuc khong ho tro"}

# Kịch bản kiểm tra
print("GET:", phuc_vu("GET"))
print("POST:", phuc_vu("POST", {"ten": "Truyen Kieu", "gia": 90000}))
print("PUT:", phuc_vu("PUT", {"id": 2, "gia": 70000}))
print("DELETE:", phuc_vu("DELETE", {"id": 1}))
print("GET cuoi:", phuc_vu("GET"))
```

**Giải thích code:**
* `{"id": id_moi, **du_lieu}` — nối dict: id mới + các khóa từ `du_lieu` (toán tử `**` — bài 17).
* `tim_sach` tái sử dụng 2 lần — tránh viết lại vòng tìm kiếm.
* Mỗi phương thức trả status đúng ngữ nghĩa: 200/201/404.
* `return 405` — "Method Not Allowed" cho phương thức lạ — chuẩn HTTP thật.

**Độ phức tạp:** O(n) cho các thao tác tìm kiếm.

---

### Bài 16: API thời tiết nâng cao — kiểm tra dữ liệu lỗi từ server

**Phân tích:** Dữ liệu từ server có thể hỏng theo nhiều cách: JSON vỡ, thiếu khóa — mỗi lỗi một status riêng.

**Ý tưởng:** `try/except` cho JSON hỏng (500), kiểm tra khóa bằng `in` cho thiếu dữ liệu (400).

**Thuật toán:**
1. Hàm `thoi_tiet_an_toan(chuoi_json)`.
2. `try` parse; `except JSONDecodeError` → 500.
3. Kiểm tra khóa `current_weather` → 400 nếu thiếu.
4. Hợp lệ → 200 kèm nhiệt độ.
5. Gọi thử 3 tình huống.

**Code:**

```python
import json

def thoi_tiet_an_toan(chuoi_json):
    """Phân tích phản hồi thời tiết, trả (status, kết quả) an toàn."""
    try:
        du_lieu = json.loads(chuoi_json)     # có thể ném JSONDecodeError
    except json.JSONDecodeError:
        return 500, "JSON loi"

    if "current_weather" not in du_lieu:
        return 400, "Thieu current_weather"  # dữ liệu không đủ cấu trúc

    nhiet_do = du_lieu["current_weather"]["temperature"]
    return 200, nhiet_do

# Tình huống 1: hợp lệ
print(thoi_tiet_an_toan('{"current_weather": {"temperature": 30.2}}'))
# Tình huống 2: thiếu khóa
print(thoi_tiet_an_toan('{"timezone": "Asia/Bangkok"}'))
# Tình huống 3: JSON hỏng
print(thoi_tiet_an_toan('{"current_weather": '))
```

**Giải thích code:**
* `try/except` bao quanh `json.loads` — lỗi văn bản → 500 (giống "server trả rác").
* `"current_weather" not in du_lieu` — kiểm tra cấu trúc → 400.
* Chỉ khi cả hai kiểm tra qua, mới đọc `temperature` và trả 200.
* Cách phân loại lỗi này giúp chương trình xử lý được dữ liệu xấu mà không sập.

**Độ phức tạp:** O(n).

---

### Bài 17: Tự tạo URL từ tham số

**Phân tích:** URL chuẩn: `endpoint?k1=v1&k2=v2`. Cần nối đúng dấu và chuyển `True` → `true` (JSON dùng chữ thường).

**Ý tưởng:** List comprehension tạo các đoạn `khóa=giá trị`, nối bằng `"&"`, ghép vào endpoint bằng `"?"`.

**Thuật toán:**
1. Hàm `tao_url(endpoint, tham_so)`.
2. Với mỗi cặp: `f"{k}={str(v).lower()}"`.
3. Nối list bằng `"&"`, ghép `endpoint + "?" + ...`.

**Code:**

```python
def tao_url(endpoint, tham_so):
    """Ghép endpoint với dict tham số thành URL chuẩn."""
    cac_doan = []
    for k, v in tham_so.items():
        gia_tri = str(v).lower()          # True -> "true" (đúng chuẩn JSON)
        cac_doan.append(f"{k}={gia_tri}")
    chuoi_tham_so = "&".join(cac_doan)    # nối các cặp bằng dấu &
    return f"{endpoint}?{chuoi_tham_so}"

endpoint = "https://api.open-meteo.com/v1/forecast"
tham_so = {"latitude": 21.03, "longitude": 105.85, "current_weather": True}

print(tao_url(endpoint, tham_so))
```

**Giải thích code:**
* `tham_so.items()` — duyệt cặp khóa-giá trị của dict (bài 17).
* `str(True).lower()` — `"True"` → `"true"`; URL/JSON dùng chữ thường.
* `"&".join(...)` — nối các đoạn đúng chuỗi ngăn cách.
* Kết quả đúng chuẩn: `...forecast?latitude=21.03&longitude=105.85&current_weather=true`.
* Bài 35 sẽ có thư viện `requests` làm việc này tự động qua `params`.

**Độ phức tạp:** O(m) với m là số tham số.

---

### Bài 18: Phân tích phản hồi nhiều tầng và xử lý thiếu khóa

**Phân tích:** Dữ liệu API không phải lúc nào cũng đầy đủ — `.get()` trả `None` khi thiếu khóa thay vì ném lỗi.

**Ý tưởng:** `du_lieu.get("daily")` kiểm tra sự tồn tại; nếu có, tính tổng/trung bình.

**Thuật toán:**
1. Hàm xử lý một dict (đã parse).
2. `daily = du_lieu.get("daily")`; `None` → in thông báo.
3. Có dữ liệu → in số ngày và nhiệt độ TB tối thiểu.

**Code:**

```python
import json

def phan_tich(chuoi_json):
    """Đọc phản hồi, xử lý an toàn khi thiếu khóa daily."""
    du_lieu = json.loads(chuoi_json)
    daily = du_lieu.get("daily")           # None nếu không có khóa daily
    if daily is None:
        print("Khong co du lieu ngay")
        return
    so_ngay = len(daily["time"])
    nhiet_min = daily["temperature_2m_min"]
    tb = sum(nhiet_min) / len(nhiet_min)
    print(f"So ngay: {so_ngay}")
    print(f"Nhiet do TB toi thieu: {round(tb, 2)}°C")

# Có dữ liệu daily
phan_tich('''{"daily": {
    "time": ["2026-08-01", "2026-08-02"],
    "temperature_2m_min": [25.1, 24.8]
}}''')

# Thiếu khóa daily
phan_tich('{"current_weather": {"temperature": 30.2}}')
```

**Giải thích code:**
* `du_lieu.get("daily")` — khóa thiếu trả `None`, không ném `KeyError` (bài 17).
* `if daily is None` — rẽ nhánh khi thiếu dữ liệu.
* `sum(nhiet_min) / len(nhiet_min)` — trung bình cộng; `round(..., 2)` làm tròn.

**Độ phức tạp:** O(m) với m là số ngày.

---

### Bài 19: So sánh dữ liệu từ hai "API" thời tiết

**Phân tích:** Gói gọn việc "gọi API và lấy nhiệt độ" vào một hàm trả tuple — gọi lại cho 2 thành phố rồi so sánh.

**Ý tưởng:** `lay_nhiet_do(chuoi_json)` trả `(ten, nhiet_do)`; so sánh và in câu kết luận.

**Thuật toán:**
1. Hàm `lay_nhiet_do` parse JSON, trả tuple.
2. Gọi cho Hà Nội và TP.HCM.
3. So sánh nhiệt độ, in kết luận.

**Code:**

```python
import json

def lay_nhiet_do(chuoi_json):
    """Mô phỏng gọi API: trả (tên thành phố, nhiệt độ) hoặc None nếu lỗi."""
    try:
        du_lieu = json.loads(chuoi_json)
        return du_lieu["city"], du_lieu["temperature"]
    except (json.JSONDecodeError, KeyError):
        return None

# "Phản hồi" của 2 thành phố
ha_noi = '{"city": "Ha Noi", "temperature": 30.2}'
tp_hcm = '{"city": "TP HCM", "temperature": 33.5}'

kq_1 = lay_nhiet_do(ha_noi)
kq_2 = lay_nhiet_do(tp_hcm)

if kq_1 is not None and kq_2 is not None:
    ten_1, nhiet_1 = kq_1
    ten_2, nhiet_2 = kq_2
    if nhiet_1 > nhiet_2:
        print(f"{ten_1} nong hon {ten_2} ({nhiet_1} vs {nhiet_2})")
    elif nhiet_1 < nhiet_2:
        print(f"{ten_2} nong hon {ten_1} ({nhiet_2} vs {nhiet_1})")
    else:
        print(f"{ten_1} va {ten_2} bang nhau ({nhiet_1})")
else:
    print("Khong lay duoc du lieu")
```

**Giải thích code:**
* `except (json.JSONDecodeError, KeyError)` — bắt nhiều loại lỗi trong một tuple — xử lý dữ liệu xấu gọn gàng.
* Hàm trả `None` khi lỗi — gọi 2 lần không sập chương trình.
* Ba nhánh so sánh: lớn hơn / nhỏ hơn / bằng nhau.

**Độ phức tạp:** O(n).

---

### Bài 20: Hệ thống "API quản lý điểm" hoàn chỉnh (Mini Project)

**Phân tích:** Tổng hợp toàn bộ bài học: một "server" có dữ liệu + hàm xử lý 4 phương thức + kịch bản kiểm tra tuần tự.

**Ý tưởng:** Dữ liệu là list dict toàn cục; `phuc_vu` rẽ nhánh; hỗ trợ GET danh sách và GET theo id qua một tham số `id`.

**Thuật toán:**
1. Khởi tạo 4 học sinh.
2. Hàm `tim_hoc_sinh(id)`.
3. `phuc_vu(phuong_thuc, du_lieu)`: GET (cả list hoặc theo id), POST, PUT, DELETE.
4. Chạy kịch bản: GET tất cả → GET id 2 → POST → PUT → DELETE → GET cuối.

**Code:**

```python
# "Cơ sở dữ liệu" trường học
hoc_sinh = [
    {"id": 1, "ten": "An", "diem": 8},
    {"id": 2, "ten": "Binh", "diem": 7},
    {"id": 3, "ten": "Chi", "diem": 9},
    {"id": 4, "ten": "Dung", "diem": 6},
]

def tim_hoc_sinh(id):
    """Tìm học sinh theo id."""
    for hs in hoc_sinh:
        if hs["id"] == id:
            return hs
    return None

def phuc_vu(phuong_thuc, du_lieu=None):
    """Mô phỏng API quản lý điểm — trả (status code, dữ liệu)."""
    if phuong_thuc == "GET":
        if du_lieu is None:
            return 200, hoc_sinh                     # GET toàn bộ
        hs = tim_hoc_sinh(du_lieu)
        return (200, hs) if hs else (404, None)      # GET theo id

    if phuong_thuc == "POST":
        id_moi = max(hs["id"] for hs in hoc_sinh) + 1
        hs_moi = {"id": id_moi, **du_lieu}
        hoc_sinh.append(hs_moi)
        return 201, hs_moi

    if phuong_thuc == "PUT":
        hs = tim_hoc_sinh(du_lieu["id"])
        if hs is None:
            return 404, None
        hs["diem"] = du_lieu["diem"]
        return 200, hs

    if phuong_thuc == "DELETE":
        hs = tim_hoc_sinh(du_lieu["id"])
        if hs is None:
            return 404, None
        hoc_sinh.remove(hs)
        return 200, {"da_xoa": hs["ten"]}

    return 405, {"error": "Phuong thuc khong ho tro"}

# Kịch bản kiểm tra tuần tự
print("1. GET tat ca:", phuc_vu("GET")[0], len(phuc_vu("GET")[1]), "hoc sinh")

status, hs = phuc_vu("GET", 2)
print("2. GET id 2:", status, hs)

status, hs_moi = phuc_vu("POST", {"ten": "Em", "diem": 10})
print("3. POST them:", status, hs_moi)

status, hs = phuc_vu("PUT", {"id": 3, "diem": 10})
print("4. PUT sua:", status, hs)

status, tb = phuc_vu("DELETE", {"id": 4})
print("5. DELETE:", status, tb)

print("6. GET cuoi:", [hs["ten"] for hs in phuc_vu("GET")[1]])
```

**Giải thích code:**
* `phuc_vu("GET", 2)` — khi `du_lieu` là số id, hiểu là GET một bản ghi; `None` → GET toàn bộ: thiết kế đơn giản cho mô phỏng.
* `(200, hs) if hs else (404, None)` — biểu thức điều kiện rút gọn.
* `{"id": id_moi, **du_lieu}` — ghép dict (bài 17): id tự tăng + dữ liệu mới.
* Kịch bản in ra đúng 4 học sinh cuối cùng: An, Binh, Chi (10 điểm sau PUT), Em (mới thêm).

**Độ phức tạp:** O(n) mỗi thao tác tìm kiếm.

---

## 📌 Lời khuyên cuối

* 🚦 **Status code là "ngôn ngữ" của API:** luôn kiểm tra trước khi đọc dữ liệu (200 mới đọc).
* 🏪 **Tư duy mô phỏng:** mọi API thật đều có thể mô phỏng bằng hàm + dict — hãy dùng cách này để luyện tập khi chưa có internet.
* 🔄 **Tách hàm nhỏ** (`tim_hoc_sinh`, `tim_sach`) để tái sử dụng — đúng phong cách lập trình chuyên nghiệp.
* 📦 **JSON hỏng / thiếu khóa:** luôn bảo vệ bằng `try/except` và `.get()`.

👉 Tiếp theo: **[Bài 35: Thư Viện Requests – Gọi API Từ Python](../35_Requests/bai_giang.md)**
