# ✅ Bài 32: Đáp Án – JSON

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án để việc học hiệu quả nhất.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Chuyển từ điển sang JSON

**Phân tích:** Dùng `json.dumps` — từ đối tượng Python thành chuỗi JSON.

**Ý tưởng:** `json.dumps(du_lieu)` rồi in chuỗi và `type()`.

**Thuật toán:**
1. Import `json`.
2. Tạo từ điển.
3. `dumps` và in.

**Code:**

```python
import json

# Từ điển cần chuyển
du_lieu = {"ten": "An", "tuoi": 15}

# Chuyển thành chuỗi JSON
chuoi_json = json.dumps(du_lieu)

print(chuoi_json)
print(type(chuoi_json))
```

**Giải thích code:**
* `json.dumps` (dump string) trả về chuỗi JSON.
* Kết quả in: `{"ten": "An", "tuoi": 15}` và `<class 'str'>` — giờ là chuỗi văn bản thuần.

**Độ phức tạp:** O(n) với n là kích thước dữ liệu.

---

### Bài 2: Chuyển JSON sang Python

**Phân tích:** `json.loads` làm ngược lại — chuỗi JSON thành đối tượng Python.

**Ý tưởng:** `loads` chuỗi rồi truy cập khóa `"si_so"`.

**Thuật toán:**
1. Import `json`.
2. `loads` chuỗi.
3. In `type` và giá trị.

**Code:**

```python
import json

# Chuỗi JSON thô
chuoi = '{"lop": "10A1", "si_so": 40}'

# Chuyển thành từ điển Python
du_lieu = json.loads(chuoi)

print(type(du_lieu))
print(du_lieu["si_so"])
```

**Giải thích code:**
* `json.loads` (load string) phân tích chuỗi JSON thành `dict`.
* `du_lieu["si_so"]` truy cập như từ điển thường → `40`.

**Độ phức tạp:** O(n).

---

### Bài 3: JSON đẹp với indent

**Phân tích:** `indent` thêm thụt lề giúp JSON dễ đọc cho con người.

**Ý tưởng:** `json.dumps(du_lieu, indent=2)`.

**Thuật toán:**
1. Import `json`.
2. Tạo từ điển.
3. `dumps` với `indent=2`, in.

**Code:**

```python
import json

du_lieu = {"a": 1, "b": [1, 2]}

# indent=2: thụt lề 2 khoảng trắng
print(json.dumps(du_lieu, indent=2))
```

**Giải thích code:**
* Mỗi cấp lồng nhau được thụt lề thêm 2 khoảng trắng.
* Output đúng như mẫu — từng phần tử của mảng cũng xuống dòng riêng.

**Độ phức tạp:** O(n).

---

### Bài 4: List sang JSON

**Phân tích:** JSON hỗ trợ mảng `[]` — list Python chuyển thẳng.

**Ý tưởng:** `json.dumps([10, 20, "ba"])`.

**Thuật toán:**
1. Import `json`.
2. `dumps` danh sách và in.

**Code:**

```python
import json

danh_sach = [10, 20, "ba"]

print(json.dumps(danh_sach))
```

**Giải thích code:**
* List Python → mảng JSON `[10, 20, "ba"]`.
* Số giữ nguyên, chuỗi bọc `"` kép.

**Độ phức tạp:** O(n).

---

### Bài 5: Boolean và None

**Phân tích:** JSON không dùng `True`/`None` — phải chuyển thành `true`/`null`.

**Ý tưởng:** `json.dumps` tự lo chuyển đổi chuẩn.

**Thuật toán:**
1. Tạo từ điển.
2. `dumps` và in.

**Code:**

```python
import json

du_lieu = {"ok": True, "x": None, "diem": 8.5}

print(json.dumps(du_lieu))
```

**Giải thích code:**
* `True` → `true`, `None` → `null` — đúng chuẩn JSON viết thường.
* `8.5` giữ nguyên là số.

**Độ phức tạp:** O(n).

---

### Bài 6: Ghi file JSON đầu tiên

**Phân tích:** `json.dump` ghi thẳng vào file — cần mở file với `encoding="utf-8"`.

**Ý tưởng:** `with open(...)` + `json.dump`.

**Thuật toán:**
1. Import `json`.
2. Mở file ở chế độ ghi.
3. `json.dump` dữ liệu.

**Code:**

```python
import json

mon_hoc = {"mon": "Toan", "diem": 9}

with open("mon.json", "w", encoding="utf-8") as f:
    json.dump(mon_hoc, f)
```

**Giải thích code:**
* `open("mon.json", "w")` — mở file để ghi (chế độ `w`).
* `json.dump(mon_hoc, f)` — ghi từ điển vào file dưới dạng JSON.
* `with` tự đóng file khi xong.

**Độ phức tạp:** O(n).

---

### Bài 7: Đọc file JSON

**Phân tích:** `json.load` đọc cả file và trả đối tượng Python.

**Ý tưởng:** Mở file ở chế độ đọc + `json.load`.

**Thuật toán:**
1. Mở file `mon.json` (`"r"`).
2. `json.load(f)`.
3. In type và giá trị.

**Code:**

```python
import json

with open("mon.json", "r", encoding="utf-8") as f:
    du_lieu = json.load(f)

print(type(du_lieu))
print(du_lieu["diem"])
```

**Giải thích code:**
* `json.load(f)` đọc nội dung file và chuyển về `dict`.
* `du_lieu["diem"]` → `9`.

**Độ phức tạp:** O(n).

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Danh bạ điện thoại

**Phân tích:** Ứng dụng danh bạ: ghi cả từ điển, đọc lại, tra cứu.

**Ý tưởng:** `json.dump` với `ensure_ascii=False, indent=2`; `json.load` để đọc.

**Thuật toán:**
1. Tạo danh bạ 3 người.
2. Ghi file.
3. Đọc lại.
4. In số người thứ 2.

**Code:**

```python
import json

# Danh bạ: tên → số điện thoại
danh_ba = {
    "Nguyễn Văn An": "0901 234 567",
    "Trần Thị Bình": "0902 345 678",
    "Lê Văn Cường": "0903 456 789",
}

# Ghi file (giữ tiếng Việt + format đẹp)
with open("danh_ba.json", "w", encoding="utf-8") as f:
    json.dump(danh_ba, f, ensure_ascii=False, indent=2)

# Đọc lại
with open("danh_ba.json", "r", encoding="utf-8") as f:
    danh_ba_doc = json.load(f)

# Lấy người thứ 2 (chuyển khóa thành danh sách)
ten_2 = list(danh_ba_doc.keys())[1]
print(danh_ba_doc[ten_2])
```

**Giải thích code:**
* `ensure_ascii=False` — tên tiếng Việt hiển thị nguyên dấu trong file.
* `indent=2` — file dễ đọc.
* `list(...keys())[1]` — lấy khóa thứ hai `"Trần Thị Bình"`.

**Độ phức tạp:** O(n).

---

### Bài 9: Lưu danh sách sản phẩm

**Phân tích:** Ghi list dict phức tạp, đọc lại, đếm.

**Ý tưởng:** `json.dump(san_pham, f, ...)`; `len()` sau khi load.

**Thuật toán:**
1. Tạo danh sách 3 sản phẩm.
2. Ghi file.
3. Đọc lại và in số lượng.

**Code:**

```python
import json

san_pham = [
    {"ma": 1, "ten": "Bút bi", "gia": 5000, "ton_kho": 100},
    {"ma": 2, "ten": "Vở ô ly", "gia": 8000, "ton_kho": 50},
    {"ma": 3, "ten": "Thước kẻ", "gia": 3000, "ton_kho": 200},
]

with open("san_pham.json", "w", encoding="utf-8") as f:
    json.dump(san_pham, f, ensure_ascii=False, indent=2)

with open("san_pham.json", "r", encoding="utf-8") as f:
    danh_sach = json.load(f)

print("Tổng mặt hàng:", len(danh_sach))
```

**Giải thích code:**
* JSON lưu được list lồng dict — cấu trúc rất thực tế.
* `len(danh_sach)` → `3`.

**Độ phức tạp:** O(n).

---

### Bài 10: Cấu hình ứng dụng

**Phân tích:** Vòng đời "đọc → sửa → ghi" của file cấu hình.

**Ý tưởng:** `load` → tăng `am_luong` → `dump` đè lại.

**Thuật toán:**
1. Tạo và lưu cấu hình ban đầu.
2. Đọc lại.
3. Sửa `am_luong`.
4. Ghi đè và in.

**Code:**

```python
import json

# Cấu hình ban đầu
cau_hinh = {
    "ten_ung_dung": "LopHocApp",
    "so_dong": 10,
    "am_luong": 0.5,
}

with open("cau_hinh.json", "w", encoding="utf-8") as f:
    json.dump(cau_hinh, f, ensure_ascii=False, indent=2)

# Đọc lại và sửa
with open("cau_hinh.json", "r", encoding="utf-8") as f:
    cau_hinh = json.load(f)

cau_hinh["am_luong"] += 0.2

with open("cau_hinh.json", "w", encoding="utf-8") as f:
    json.dump(cau_hinh, f, ensure_ascii=False, indent=2)

print(cau_hinh["ten_ung_dung"], "— âm lượng:", cau_hinh["am_luong"])
```

**Giải thích code:**
* `+= 0.2` biến `0.5` thành `0.7`.
* Ghi đè file ghi giữ mọi thay đổi — lần mở ứng dụng sau sẽ đọc được.

**Độ phức tạp:** O(n).

---

### Bài 11: Thêm ghi chú

**Phân tích:** Ứng dụng ghi chú: đọc file cũ (hoặc tạo mới), thêm, lưu.

**Ý tưởng:** `os.path.exists` kiểm tra file; `append` rồi `dump`.

**Thuật toán:**
1. Nếu file tồn tại → load; ngược lại `[]`.
2. Append ghi chú.
3. Lưu lại và in số lượng.

**Code:**

```python
import json
import os

ten_file = "ghi_chu.json"

# Đọc dữ liệu cũ nếu có
if os.path.exists(ten_file):
    with open(ten_file, "r", encoding="utf-8") as f:
        ghi_chu = json.load(f)
else:
    ghi_chu = []

# Thêm ghi chú mới
ghi_chu.append({"tieu_de": "Bai 32", "noi_dung": "Da xong"})

# Lưu lại
with open(ten_file, "w", encoding="utf-8") as f:
    json.dump(ghi_chu, f, ensure_ascii=False, indent=2)

print(len(ghi_chu))
```

**Giải thích code:**
* Lần chạy 1: file chưa có → `[]` → sau khi append có 1 ghi chú → in `1`.
* Lần chạy 2: file có sẵn → load ra 1 → append → in `2`.

**Độ phức tạp:** O(n).

---

### Bài 12: Tính tổng từ JSON phức tạp

**Phân tích:** Dữ liệu lồng nhau: list dict, trong dict có list điểm.

**Ý tưởng:** Load file rồi `sum(hs["mon"])` từng học sinh.

**Thuật toán:**
1. Tạo dữ liệu, ghi file.
2. Đọc lại.
3. In tổng điểm từng người.

**Code:**

```python
import json

hoc_sinh = [
    {"ten": "An", "mon": [8, 7]},
    {"ten": "Binh", "mon": [9, 10]},
]

with open("diem.json", "w", encoding="utf-8") as f:
    json.dump(hoc_sinh, f, ensure_ascii=False, indent=2)

with open("diem.json", "r", encoding="utf-8") as f:
    danh_sach = json.load(f)

for hs in danh_sach:
    print(f"{hs['ten']}: {sum(hs['mon'])}")
```

**Giải thích code:**
* `hs["mon"]` là list điểm → `sum()` tính tổng.
* Kết quả: `An: 15`, `Binh: 19`.

**Độ phức tạp:** O(n × m) với m là số điểm mỗi người.

---

### Bài 13: Sửa lỗi JSON thủ công

**Phân tích:** Rèn kỹ năng đọc lỗi `JSONDecodeError` và sửa cú pháp.

**Ý tưởng:** Thử `loads` chuỗi sai → ghi nhận lỗi; sửa chuỗi → load lại.

**Thuật toán:**
1. Chuỗi sai: `{"ten": 'An', "diem": [8, 9,],}`.
2. Bắt lỗi bằng `try/except`.
3. Sửa: dùng `"An"`, bỏ dấu phẩy thừa.

**Code:**

```python
import json

chuoi_sai = "{'ten': 'An', \"diem\": [8, 9,],}"

try:
    json.loads(chuoi_sai)
except json.JSONDecodeError as e:
    print("Lỗi:", e)

# Chuỗi đã sửa: nháy kép + bỏ dấu phẩy thừa
chuoi_dung = '{"ten": "An", "diem": [8, 9]}'
print(json.loads(chuoi_dung))
```

**Giải thích code:**
* JSON yêu cầu nháy kép `"` và không chấp nhận dấu phẩy trước dấu đóng.
* Lỗi in ra là `JSONDecodeError` với vị trí cụ thể.
* Sau khi sửa, `loads` chạy ngon lành.

**Độ phức tạp:** O(n).

---

### Bài 14: Lọc sản phẩm rẻ

**Phân tích:** Kết hợp JSON + điều kiện lọc.

**Ý tưởng:** Load danh sách, vòng lặp kiểm tra `gia < 10000`.

**Thuật toán:**
1. Tạo dữ liệu, ghi file.
2. Đọc lại.
3. In tên sản phẩm rẻ.

**Code:**

```python
import json

san_pham = [
    {"ten": "Bút bi", "gia": 5000},
    {"ten": "Vở ô ly", "gia": 12000},
    {"ten": "Thước kẻ", "gia": 3000},
    {"ten": "Túi bút", "gia": 25000},
]

with open("san_pham_gia.json", "w", encoding="utf-8") as f:
    json.dump(san_pham, f, ensure_ascii=False, indent=2)

with open("san_pham_gia.json", "r", encoding="utf-8") as f:
    danh_sach = json.load(f)

for sp in danh_sach:
    if sp["gia"] < 10000:
        print(sp["ten"])
```

**Giải thích code:**
* Điều kiện `sp["gia"] < 10000` lọc ra Bút bi (5000) và Thước kẻ (3000).
* Vòng lặp duyệt danh sách đọc từ file — xử lý dữ liệu thật từ đĩa.

**Độ phức tạp:** O(n).

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Điểm trung bình và xếp loại

**Phân tích:** Tính toán + phân loại nhiều học sinh từ dữ liệu JSON.

**Ý tưởng:** Tính TB mỗi người, xếp loại bằng `if/elif/else`.

**Thuật toán:**
1. Ghi dữ liệu 4 học sinh.
2. Đọc lại.
3. Với mỗi học sinh: tính TB → xếp loại → in.

**Code:**

```python
import json

hoc_sinh = [
    {"ten": "An", "mon": [8, 8, 8]},
    {"ten": "Binh", "mon": [6, 6, 6]},
    {"ten": "Chi", "mon": [4, 5, 5]},
    {"ten": "Dung", "mon": [9, 10, 8]},
]

with open("hoc_sinh.json", "w", encoding="utf-8") as f:
    json.dump(hoc_sinh, f, ensure_ascii=False, indent=2)

with open("hoc_sinh.json", "r", encoding="utf-8") as f:
    danh_sach = json.load(f)

for hs in danh_sach:
    diem_tb = sum(hs["mon"]) / len(hs["mon"])
    if diem_tb >= 8:
        loai = "Giỏi"
    elif diem_tb >= 5:
        loai = "Đạt"
    else:
        loai = "Cần cố gắng"
    print(f"{hs['ten']}: {diem_tb:.1f} - {loai}")
```

**Giải thích code:**
* `sum / len` cho điểm TB chính xác.
* Xếp loại theo ngưỡng 8 và 5.
* `{diem_tb:.1f}` làm tròn 1 chữ số thập phân cho đẹp.

**Độ phức tạp:** O(n × m).

---

### Bài 16: Cập nhật tồn kho khi bán hàng

**Phân tích:** Mô phỏng giao dịch: tìm sản phẩm, giảm tồn kho, lưu lại.

**Ý tưởng:** Duyệt tìm `ma == 1`, `ton_kho -= 2`, `json.dump`.

**Thuật toán:**
1. Tạo (hoặc đọc) file sản phẩm.
2. Duyệt tìm mã 1, giảm tồn kho 2.
3. Ghi lại và in.

**Code:**

```python
import json

san_pham = [
    {"ma": 1, "ten": "Bút bi", "gia": 5000, "ton_kho": 100},
    {"ma": 2, "ten": "Vở ô ly", "gia": 8000, "ton_kho": 50},
    {"ma": 3, "ten": "Thước kẻ", "gia": 3000, "ton_kho": 200},
]

with open("san_pham.json", "w", encoding="utf-8") as f:
    json.dump(san_pham, f, ensure_ascii=False, indent=2)

with open("san_pham.json", "r", encoding="utf-8") as f:
    danh_sach = json.load(f)

# Bán 2 món mã 1
for sp in danh_sach:
    if sp["ma"] == 1:
        sp["ton_kho"] -= 2

with open("san_pham.json", "w", encoding="utf-8") as f:
    json.dump(danh_sach, f, ensure_ascii=False, indent=2)

for sp in danh_sach:
    if sp["ma"] == 1:
        print("Ton kho con lai:", sp["ton_kho"])
```

**Giải thích code:**
* Vòng lặp tìm và sửa đúng đối tượng trong danh sách.
* `json.dump` đè lại file → dữ liệu tồn kho được cập nhật bền vững.

**Độ phức tạp:** O(n).

---

### Bài 17: Gộp hai file JSON

**Phân tích:** Kết hợp dữ liệu từ nhiều file — thao tác thường gặp khi phân tích.

**Ý tưởng:** Đọc hai file, cộng hai list, lưu file gộp.

**Thuật toán:**
1. Tạo `lopA.json`, `lopB.json`.
2. Load cả hai.
3. `danh_sach = lop_a + lop_b`.
4. Lưu và in tổng.

**Code:**

```python
import json

lop_a = [{"ten": "An"}, {"ten": "Binh"}]
lop_b = [{"ten": "Chi"}, {"ten": "Dung"}]

for ten_file, du_lieu in [("lopA.json", lop_a), ("lopB.json", lop_b)]:
    with open(ten_file, "w", encoding="utf-8") as f:
        json.dump(du_lieu, f, ensure_ascii=False, indent=2)

with open("lopA.json", "r", encoding="utf-8") as f:
    a = json.load(f)

with open("lopB.json", "r", encoding="utf-8") as f:
    b = json.load(f)

tat_ca = a + b

with open("tat_ca.json", "w", encoding="utf-8") as f:
    json.dump(tat_ca, f, ensure_ascii=False, indent=2)

print("Tổng số học sinh:", len(tat_ca))
```

**Giải thích code:**
* Vòng lặp nhỏ ghi lần lượt hai file.
* `a + b` nối hai list thành một.
* `len(tat_ca)` → `4`.

**Độ phức tạp:** O(n + m).

---

### Bài 18: Tìm kiếm trong JSON

**Phân tích:** Tìm kiếm theo điều kiện chuỗi (đầu số điện thoại).

**Ý tưởng:** Duyệt `danh_ba.items()`, kiểm tra `so.startswith("0903")`.

**Thuật toán:**
1. Tạo danh bạ 5 người, ghi file.
2. Đọc lại.
3. In tên người có số bắt đầu 0903.

**Code:**

```python
import json

danh_ba = {
    "An": "0901 234 567",
    "Binh": "0903 111 222",
    "Chi": "0912 345 678",
    "Dung": "0903 999 888",
    "Em": "0905 123 456",
}

with open("danh_ba.json", "w", encoding="utf-8") as f:
    json.dump(danh_ba, f, ensure_ascii=False, indent=2)

with open("danh_ba.json", "r", encoding="utf-8") as f:
    danh_ba_doc = json.load(f)

for ten, so in danh_ba_doc.items():
    if so.startswith("0903"):
        print(ten)
```

**Giải thích code:**
* `dict.items()` trả từng cặp (tên, số).
* `str.startswith("0903")` kiểm tra chuỗi bắt đầu.
* Kết quả: `Binh`, `Dung`.

**Độ phức tạp:** O(n × k) với k là độ dài số điện thoại.

---

### Bài 19: Đếm số sản phẩm theo loại

**Phân tích:** Thống kê nhóm — dùng dict làm "bộ đếm".

**Ý tưởng:** `dem[loai] = dem.get(loai, 0) + 1` cho từng sản phẩm.

**Thuật toán:**
1. Tạo dữ liệu có `loai`, ghi file.
2. Đọc lại.
3. Đếm và in từng loại.

**Code:**

```python
import json

san_pham = [
    {"ten": "Bút bi", "loai": "van_phong"},
    {"ten": "Vở ô ly", "loai": "hoc_tap"},
    {"ten": "Thước kẻ", "loai": "hoc_tap"},
    {"ten": "Sách Python", "loai": "sach"},
    {"ten": "Bút lông", "loai": "van_phong"},
]

with open("san_pham_loai.json", "w", encoding="utf-8") as f:
    json.dump(san_pham, f, ensure_ascii=False, indent=2)

with open("san_pham_loai.json", "r", encoding="utf-8") as f:
    danh_sach = json.load(f)

dem = {}
for sp in danh_sach:
    loai = sp["loai"]
    dem[loai] = dem.get(loai, 0) + 1

for loai, so_luong in dem.items():
    print(f"{loai}: {so_luong}")
```

**Giải thích code:**
* `dict.get(loai, 0)` trả 0 nếu chưa có khóa — không báo lỗi.
* Kết quả: `van_phong: 2`, `hoc_tap: 2`, `sach: 1`.

**Độ phức tạp:** O(n).

---

### Bài 20: Ứng dụng quản lý điểm hoàn chỉnh

**Phân tích:** Ứng dụng có menu, lưu trữ bền vững bằng JSON — tổng hợp toàn bài.

**Ý tưởng:** `while True` hiển thị menu; mỗi thao tác đọc file, sửa, ghi lại.

**Thuật toán:**
1. Vòng lặp vô hạn hiện menu.
2. Chọn 1: nhập tên + điểm, append, ghi file.
3. Chọn 2: đọc file, in danh sách.
4. Chọn 3: thoát.

**Code:**

```python
import json
import os

ten_file = "hoc_sinh.json"


def doc_du_lieu():
    """Đọc danh sách học sinh từ file (rỗng nếu chưa có)."""
    if os.path.exists(ten_file):
        with open(ten_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def ghi_du_lieu(danh_sach):
    """Ghi danh sách học sinh vào file."""
    with open(ten_file, "w", encoding="utf-8") as f:
        json.dump(danh_sach, f, ensure_ascii=False, indent=2)


while True:
    print("\n1. Thêm học sinh")
    print("2. Xem danh sách")
    print("3. Thoát")
    chon = input("Chọn: ")

    if chon == "1":
        # Nhập: An 8
        ten, diem = input("Tên và điểm (cách nhau dấu cách): ").split()
        danh_sach = doc_du_lieu()
        danh_sach.append({"ten": ten, "diem": float(diem)})
        ghi_du_lieu(danh_sach)
        print("Đã thêm!")
    elif chon == "2":
        danh_sach = doc_du_lieu()
        if not danh_sach:
            print("Chưa có học sinh nào.")
        for hs in danh_sach:
            print(f"- {hs['ten']}: {hs['diem']}")
    elif chon == "3":
        print("Tạm biệt!")
        break
    else:
        print("Chọn sai, thử lại!")
```

**Giải thích code:**
* Hai hàm phụ `doc_du_lieu` / `ghi_du_lieu` tách biệt logic — code dễ đọc.
* Mọi thao tác thêm đều ghi lại file → dữ liệu tồn tại sau khi thoát chương trình.
* `input().split()` tách `"An 8"` thành `["An", "8"]`.

**Độ phức tạp:** O(n) mỗi thao tác thêm/xem.

---

## 📌 Lời khuyên cuối

* Nhớ bộ tứ: `dumps`/`loads` cho chuỗi, `dump`/`load` cho file.
* Khi ghi: `encoding="utf-8"` + `ensure_ascii=False`; khi đọc: `encoding="utf-8"`.
* Gặp `JSONDecodeError` → mở file, kiểm tra ngoặc, nháy kép, dấu phẩy.
* Mỗi file JSON chỉ chứa một đối tượng duy nhất.
* JSON là nền tảng cho API (bài 34) và Requests (bài 35) — nắm chắc bài này bạn sẽ học sau rất nhẹ!

👉 Tiếp theo: **[Bài 33: CSV](../33_CSV/bai_giang.md)**