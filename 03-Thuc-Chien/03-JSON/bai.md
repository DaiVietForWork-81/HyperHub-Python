# Bài 32 — JSON – Ngôn Ngữ Lưu Trữ Dữ Liệu

> 🎓 **Chương 10 – Dữ liệu và mạng**
> Bài 22 bạn đã học ghi/đọc file văn bản; bài 30-31 là môi trường ảo và pip. Bây giờ đến lượt một định dạng đặc biệt quan trọng: **JSON** — ngôn ngữ mà mọi website, điện thoại và ứng dụng dùng để trao đổi dữ liệu. Học JSON là bước đệm hoàn hảo cho bài 34 (API) và bài 35 (Requests).

## 🧠 Điều kiện tiên quyết

- [Bài 22 — Đọc Và Ghi File Trong Python](../../01-Co-Ban/22-File/bai.md)

---

## 🎯 Mục tiêu

Sau bài học này, học viên sẽ:

* ✅ Hiểu **JSON là gì**, vì sao nó phổ biến nhất trong lập trình hiện đại.
* ✅ Nắm được **cấu trúc JSON**: object `{}` và array `[]`.
* ✅ Chuyển đổi Python ↔ JSON bằng **`json.dumps`** và **`json.loads`**.
* ✅ Ghi/đọc file JSON bằng **`json.dump`** và **`json.load`**.
* ✅ Xử lý **tiếng Việt trong JSON** (`ensure_ascii=False`, `encoding='utf-8'`).
* ✅ Nhận biết và sửa các **lỗi thường gặp** khi làm việc với JSON.
* ✅ Viết được ứng dụng thực tế: **danh bạ**, **danh sách sản phẩm**, **cấu hình ứng dụng**.

---

## 📖 Kiến thức

### 1. Nhắc nhẹ bài trước — nối tiếp hành trình dữ liệu

Ở bài 22, bạn ghi dữ liệu vào file dạng văn bản thuần. Nhưng có một vấn đề: dữ liệu đó chỉ là "chữ", không phân biệt được đâu là số, đâu là danh sách, đâu là từ điển. **JSON ra đời để giải quyết chuyện đó** — một định dạng văn bản có **cấu trúc rõ ràng** mà cả máy tính lẫn con người đều đọc được.

### 2. JSON là gì?

**JSON** (JavaScript Object Notation — Ký hiệu đối tượng JavaScript) là **định dạng văn bản để lưu trữ và trao đổi dữ liệu** có cấu trúc.

* 🌍 Phổ biến nhất thế giới: web, app, API đều dùng JSON.
* 📖 Dễ đọc: con người nhìn là hiểu.
* 🔗 Độc lập ngôn ngữ: Python, JavaScript, Java, C#... đều đọc được.

> 💬 **Ví dụ đời thực:** JSON giống **phiếu mua hàng có khuôn mẫu** — ghi tên hàng, số lượng, giá tiền theo đúng ô. Dù người bán nào nhận phiếu, họ đều hiểu được ô nào là gì, vì mọi người cùng dùng chung "khuôn".

**Ví dụ JSON thật:**

```json
{
  "ten": "Nguyễn Văn An",
  "tuoi": 15,
  "mon_hoc": ["Toán", "Tin học"],
  "diem_tb": 8.5,
  "dang_hoc": true
}
```

### 3. Cấu trúc JSON — hai "khối xây" chính

JSON chỉ có hai khối cơ bản, lồng nhau tùy ý:

| Khối | Ký hiệu | Ví dụ | Tương ứng Python |
|---|---|---|---|
| 📦 **Object** | `{}` | `{"ten": "An"}` | `dict` |
| 📚 **Array** | `[]` | `["Toán", "Lý"]` | `list` |

**Các kiểu dữ liệu trong JSON:**

| Kiểu JSON | Ví dụ | Python tương ứng |
|---|---|---|
| Chuỗi | `"Xin chào"` | `str` |
| Số | `15`, `8.5` | `int` / `float` |
| Boolean | `true` / `false` | `True` / `False` |
| Null | `null` | `None` |
| Object | `{...}` | `dict` |
| Array | `[...]` | `list` |

> ⚠️ **Chú ý:** JSON dùng `true`, `false`, `null` **viết thường** — khác Python (`True`, `False`, `None`).

```mermaid
mindmap
  root((JSON))
    📦 Object { }
      Cặp "khóa": giá trị
      Tương đương dict
    📚 Array [ ]
      Danh sách có thứ tự
      Tương đương list
    🔤 Kiểu dữ liệu
      Chuỗi, số, boolean, null
      Lồng nhau vô hạn
```

### 4. `json.dumps` — Python → chuỗi JSON

Hàm `dumps` (**d**ump **s**tring) chuyển **đối tượng Python** thành **chuỗi JSON**:

```python
import json

du_lieu = {"ten": "An", "diem": [8, 9, 7]}
chuoi_json = json.dumps(du_lieu)
print(chuoi_json)   # {"ten": "An", "diem": [8, 9, 7]}
print(type(chuoi_json))   # <class 'str'>
```

**Bảng chuyển đổi Python → JSON:**

| Python | JSON |
|---|---|
| `dict` | `{}` |
| `list`, `tuple` | `[]` |
| `str` | `"..."` |
| `int`, `float` | số |
| `True` / `False` | `true` / `false` |
| `None` | `null` |

> 💡 `json.dumps(du_lieu, indent=2)` — tham số `indent` giúp JSON in ra **đẹp, có thụt lề** dễ đọc.

### 5. `json.loads` — chuỗi JSON → Python

Hàm `loads` (**lo**ad **s**tring) làm điều ngược lại:

```python
import json

chuoi_json = '{"ten": "An", "diem": [8, 9, 7]}'
du_lieu = json.loads(chuoi_json)
print(du_lieu["ten"])          # An
print(du_lieu["diem"][1])      # 9
print(type(du_lieu))           # <class 'dict'>
```

> 💬 **Ví dụ đời thực:** `dumps` giống **đóng gói hàng vào thùng có nhãn**; `loads` giống **mở thùng và lấy hàng ra**. Hàng đi xa thì phải đóng gói (dumps), nhận được thì mở ra (loads).

### 6. `json.dump` và `json.load` — làm việc với FILE

Không có chữ `s` = làm việc trực tiếp với **file**:

| Hàm | Việc làm |
|---|---|
| `json.dump(du_lieu, f)` | Ghi đối tượng Python vào file `f` |
| `json.load(f)` | Đọc dữ liệu từ file `f` trả về đối tượng Python |

**Ghi file JSON:**

```python
import json

danh_bạ = {"An": "0901 234 567", "Binh": "0902 345 678"}

with open("danh_ba.json", "w", encoding="utf-8") as f:
    json.dump(danh_bạ, f, ensure_ascii=False, indent=2)
```

**Đọc file JSON:**

```python
import json

with open("danh_ba.json", "r", encoding="utf-8") as f:
    danh_bạ = json.load(f)

print(danh_bạ["An"])   # 0901 234 567
```

> 💡 Cách nhớ dễ: `dumps`/`loads` — chữ **s** = **string** (chuỗi). `dump`/`load` — không có s = **file**.

### 7. JSON tiếng Việt — `ensure_ascii=False` và `encoding='utf-8'`

**Vấn đề:** mặc định Python ghi ký tự tiếng Việt dưới dạng `\u...` khó đọc:

```python
import json

print(json.dumps({"ten": "An"}))
# {"ten": "An"} — tiếng Việt bị biến thành mã \u
```

**Giải pháp: hai "bùa chú" đi kèm nhau:**

```python
with open("du_lieu.json", "w", encoding="utf-8") as f:
    json.dump(du_lieu, f, ensure_ascii=False, indent=2)
```

| Tham số | Tác dụng |
|---|---|
| `ensure_ascii=False` | Giữ nguyên ký tự tiếng Việt (không chuyển thành `\u...`) |
| `encoding="utf-8"` | Ghi file theo chuẩn Unicode — đọc được đúng dấu |

> ⚠️ **Quy tắc vàng:** **ghi** tiếng Việt thì dùng cả hai. **Đọc** file chỉ cần `encoding="utf-8"` — nếu quên, tiếng Việt đọc ra sẽ bị lỗi (mojibake): `dấu` thành ký tự loạn.

### 8. Lỗi thường gặp khi làm việc với JSON

Phần lớn lỗi JSON đến từ **sai định dạng** — JSON rất khắt khe:

| Lỗi | Ví dụ sai | Đúng |
|---|---|---|
| Dùng `'` thay `"` | `{'ten': 'An'}` | `{"ten": "An"}` |
| `True`/`None` Python | `{"ok": True}` | `{"ok": true}` |
| Dấu phẩy thừa cuối | `[1, 2,]` | `[1, 2]` |
| Thiếu dấu ngoặc | `{"ten": "An"` | `{"ten": "An"}` |

Sai định dạng → `json.loads` báo lỗi **`JSONDecodeError`** với dòng cột cụ thể — chịu khó đọc thông báo sẽ tìm ra chỗ sai.

> 💬 **Ví dụ đời thực:** JSON giống **biên bản họp lớp** — mục nào cũng phải viết đúng quy ước, thiếu một dấu ngoặc là "biên bản hỏng" (không đọc được).

### 9. Khi nào dùng JSON?

* 💾 Lưu cấu hình ứng dụng (`config.json`).
* 📱 Trao đổi dữ liệu giữa app và máy chủ (bài 34-35).
* 🗄️ Lưu dữ liệu nhỏ thay cho cơ sở dữ liệu (danh bạ, ghi chú, sản phẩm).
* 🌐 Mọi API hiện đại đều trả JSON.

---

## 💡 Ví dụ minh họa

### Ví dụ 1: Danh bạ điện thoại lưu vào JSON

```python
import json

# 1. Dữ liệu: danh bạ dạng từ điển
danh_ba = {
    "Nguyễn Văn An": "0901 234 567",
    "Trần Thị Bình": "0902 345 678",
    "Lê Văn Cường": "0903 456 789",
}

# 2. Ghi vào file JSON (giữ tiếng Việt, format đẹp)
with open("danh_ba.json", "w", encoding="utf-8") as f:
    json.dump(danh_ba, f, ensure_ascii=False, indent=2)

# 3. Đọc lại từ file
with open("danh_ba.json", "r", encoding="utf-8") as f:
    danh_ba_doc_lai = json.load(f)

# 4. Tìm số điện thoại
ten = "Trần Thị Bình"
print(f"Số của {ten}: {danh_ba_doc_lai[ten]}")
```

**Giải thích từng dòng:**

| Dòng | Ý nghĩa |
|---|---|
| `danh_ba = {...}` | Từ điển lưu tên → số điện thoại |
| `json.dump(danh_ba, f, ...)` | Ghi cả từ điển vào file dạng JSON |
| `ensure_ascii=False` | Giữ dấu tiếng Việt khi ghi |
| `indent=2` | Thụt lề 2 khoảng trắng — file nhìn đẹp |
| `json.load(f)` | Đọc lại toàn bộ file thành từ điển |
| `danh_ba_doc_lai[ten]` | Tra số điện thoại như tra từ điển thường |

### Ví dụ 2: Cấu hình ứng dụng

```python
import json

# Cấu hình mặc định
cau_hinh = {
    "ten_ung_dung": "Quản lý lớp học",
    "so_dong_moi_trang": 10,
    "am_luong": 0.8,
    "che_do_toi": False,
}

# Lưu cấu hình
with open("cau_hinh.json", "w", encoding="utf-8") as f:
    json.dump(cau_hinh, f, ensure_ascii=False, indent=2)

# Đọc cấu hình khi khởi động
with open("cau_hinh.json", "r", encoding="utf-8") as f:
    cau_hinh = json.load(f)

print("Ứng dụng:", cau_hinh["ten_ung_dung"])
print("Âm lượng:", cau_hinh["am_luong"])
```

> 🎮 **Ví dụ đời thực:** Khi bạn chỉnh âm lượng hay chế độ tối trong game/ứng dụng, phần mềm lưu các lựa chọn đó vào một file JSON. Lần sau mở lên, nó đọc lại file và áp dụng đúng thiết lập của bạn.

### Ví dụ 3: Danh sách sản phẩm phức tạp (lồng nhau)

```python
import json

san_pham = [
    {"ma": 1, "ten": "Bút bi", "gia": 5000, "ton_kho": 100},
    {"ma": 2, "ten": "Vở ô ly", "gia": 8000, "ton_kho": 50},
    {"ma": 3, "ten": "Thước kẻ", "gia": 3000, "ton_kho": 200},
]

# Ghi danh sách vào file
with open("san_pham.json", "w", encoding="utf-8") as f:
    json.dump(san_pham, f, ensure_ascii=False, indent=2)

# Đọc lại và tính tổng giá trị tồn kho
with open("san_pham.json", "r", encoding="utf-8") as f:
    sp = json.load(f)

tong = sum(item["gia"] * item["ton_kho"] for item in sp)
print(f"Tổng giá trị tồn kho: {tong:,} đồng")
```

---

## 🔬 Ví dụ nâng cao

### Ví dụ 1: Ứng dụng ghi chú hoàn chỉnh (thêm + lưu + đọc)

```python
import json
import os

ten_file = "ghi_chu.json"

# 1. Đọc ghi chú cũ (nếu có)
if os.path.exists(ten_file):
    with open(ten_file, "r", encoding="utf-8") as f:
        ghi_chu = json.load(f)
else:
    ghi_chu = []

# 2. Thêm ghi chú mới
ghi_chu.append({"tieu_de": "Học bài 32", "noi_dung": "JSON rất quan trọng!"})
ghi_chu.append({"tieu_de": "Mua sách", "noi_dung": "Sách Python cơ bản"})

# 3. Lưu lại
with open(ten_file, "w", encoding="utf-8") as f:
    json.dump(ghi_chu, f, ensure_ascii=False, indent=2)

# 4. Hiển thị
with open(ten_file, "r", encoding="utf-8") as f:
    danh_sach = json.load(f)

for i, gc in enumerate(danh_sach, 1):
    print(f"{i}. {gc['tieu_de']}: {gc['noi_dung']}")
```

### Ví dụ 2: Máy tính điểm trung bình — đọc từ JSON

```python
import json

# Dữ liệu điểm học sinh (giả sử đã có sẵn file)
diem_hs = [
    {"ten": "An", "mon": [8, 7, 9]},
    {"ten": "Binh", "mon": [5, 6, 7]},
    {"ten": "Chi", "mon": [9, 10, 8]},
]

with open("diem.json", "w", encoding="utf-8") as f:
    json.dump(diem_hs, f, ensure_ascii=False, indent=2)

with open("diem.json", "r", encoding="utf-8") as f:
    danh_sach = json.load(f)

for hs in danh_sach:
    diem_tb = sum(hs["mon"]) / len(hs["mon"])
    trang_thai = "Đậu" if diem_tb >= 5 else "Trượt"
    print(f"{hs['ten']}: TB {diem_tb:.1f} — {trang_thai}")
```

### Ví dụ 3: Cập nhật cấu hình (đọc → sửa → ghi lại)

```python
import json

# Đọc cấu hình hiện tại
with open("cau_hinh.json", "r", encoding="utf-8") as f:
    cau_hinh = json.load(f)

# Sửa một vài mục
cau_hinh["so_dong_moi_trang"] = 20
cau_hinh["che_do_toi"] = True

# Ghi đè lại file
with open("cau_hinh.json", "w", encoding="utf-8") as f:
    json.dump(cau_hinh, f, ensure_ascii=False, indent=2)

print("Cấu hình đã cập nhật:", cau_hinh)
```

> 🏪 **Tình huống thực tế:** Phần mềm quản lý cửa hàng lưu danh sách sản phẩm vào JSON; khi bán một món, chương trình đọc file, giảm `ton_kho`, rồi ghi lại — vòng đời "đọc → sửa → ghi" là mẫu phổ biến nhất khi làm việc với JSON.

---

## ⚠️ Lỗi thường gặp

### Lỗi 1: `JSONDecodeError` — file JSON hỏng

* **Nguyên nhân:** file có cú pháp sai: thiếu ngoặc, dấu phẩy thừa, dùng `'` thay `"`...
* **Kết quả báo:** `json.decoder.JSONDecodeError: Expecting ',' delimiter...`
* **Cách sửa:** mở file đọc dòng báo lỗi, sửa cú pháp đúng chuẩn JSON; kiểm tra dấu `"` và `{}` `[]` khớp nhau.

### Lỗi 2: Ghi tiếng Việt bị loạn khi đọc lại

* **Nguyên nhân:** quên `encoding="utf-8"` khi ghi/đọc file.
* **Cách sửa:** luôn ghi `with open("x.json", "w", encoding="utf-8")`; đọc cũng dùng `encoding="utf-8"`.

### Lỗi 3: Tiếng Việt biến thành `\u1e69...` trong file

* **Nguyên nhân:** mặc định `ensure_ascii=True` — Python chuyển mọi ký tự không phải ASCII thành mã.
* **Cách sửa:** thêm `ensure_ascii=False` khi gọi `json.dump`/`json.dumps`.

### Lỗi 4: `json.JSONDecodeError: Extra data`

* **Nguyên nhân:** file chứa **nhiều JSON nối tiếp** mà bạn đọc một lần bằng `json.load`.
* **Cách sửa:** mỗi file chỉ chứa **một** đối tượng JSON duy nhất; hoặc đọc từng dòng bằng `json.loads`.

### Lỗi 5: Lưu đối tượng không hợp lệ (set, datetime...)

* **Nguyên nhân:** `set`, `datetime`, hàm... không có kiểu tương ứng trong JSON.
* **Kết quả báo:** `TypeError: Object of type set is not JSON serializable`.
* **Cách sửa:** chuyển về kiểu hợp lệ trước khi lưu (ví dụ `list(du_lieu_set)`, hoặc dùng `str(datetime)`).

---

## 💎 Mẹo

* 🎨 **Dùng `indent=2`** khi ghi — file JSON đẹp, dễ đọc, dễ sửa tay.
* 🇻🇳 **"Bùa chú đôi"** cho tiếng Việt: `encoding="utf-8"` + `ensure_ascii=False` — ghi nhớ là không bao giờ sai.
* 🧪 **Thử nhanh bằng terminal:** `python -m json.tool file.json` — công cụ kiểm tra và làm đẹp JSON ngay trong dòng lệnh.
* 📝 **JSON phải là "một khối duy nhất"** — ghi nhiều đối tượng vào một file dễ lỗi; hãy gom vào list hoặc dùng một file mỗi đối tượng.
* 🔍 **Khi lỗi `JSONDecodeError`**, hãy đọc kỹ vị trí dòng: cột — thường chỉ sai một dấu ngoặc hoặc dấu phẩy.
* 🛠️ Nếu dữ liệu phức tạp (ngày giờ, màu sắc), cân nhắc mở rộng bằng tham số `default` của json — bài nâng cao.

---

## 📝 Tóm tắt

| Hàm | Chức năng | Đối tượng |
|---|---|---|
| `json.dumps(x)` | Python → chuỗi JSON | str |
| `json.loads(s)` | Chuỗi JSON → Python | dict/list... |
| `json.dump(x, f)` | Python → file JSON | file |
| `json.load(f)` | File JSON → Python | file |
| `ensure_ascii=False` | Giữ tiếng Việt nguyên dấu | khi ghi |
| `encoding="utf-8"` | Đúng chuẩn Unicode | khi ghi/đọc file |
| `indent=2` | In JSON thụt lề đẹp | khi ghi |
| JSON ↔ Python | `{}`=dict, `[]`=list, `true/false`=True/False, `null`=None | — |

---

## 🧪 Kiểm tra nhanh

1. ❓ JSON là gì? Vì sao phổ biến?
2. ❓ Hai khối xây chính của JSON là gì? Tương ứng kiểu Python nào?
3. ❓ `json.dumps` và `json.dump` khác nhau thế nào?
4. ❓ Viết JSON tương đương của `{"ok": True, "x": None}` trong Python.
5. ❓ Hai tham số nào giúp ghi tiếng Việt đúng?
6. ❓ `JSONDecodeError` xảy ra khi nào?
7. ❓ Lệnh nào chuyển chuỗi `'{"a": 1}'` thành từ điển Python?
8. ❓ JSON có kiểu set không? Nếu không, phải làm gì?
9. ❓ `json.loads('{"a": 1,}')` chạy được không? Vì sao?
10. ❓ Kể 3 ứng dụng thực tế của JSON.

<details>
<summary>🔍 Xem đáp án</summary>

1. Định dạng văn bản lưu/trao đổi dữ liệu có cấu trúc; phổ biến vì dễ đọc, đa ngôn ngữ, mọi web/API dùng.
2. Object `{}` → dict; Array `[]` → list.
3. `dumps` trả chuỗi JSON; `dump` ghi thẳng vào file.
4. `{"ok": true, "x": null}` — viết thường `true`, `null`.
5. `encoding="utf-8"` và `ensure_ascii=False`.
6. Khi chuỗi/file JSON có cú pháp sai (thiếu ngoặc, dấu phẩy, nháy đơn...).
7. `json.loads('{"a": 1}')`.
8. Không có; chuyển về `list(...)` hoặc `str(...)` trước khi lưu.
9. Không — dấu phẩy thừa cuối cùng trước `}` không hợp lệ trong JSON.
10. Cấu hình ứng dụng, danh bạ, danh sách sản phẩm, dữ liệu API, ghi chú...

</details>

---

## 📚 Bài đọc thêm

* [Python.org – json module](https://docs.python.org/3/library/json.html)
* [W3Schools – JSON Tutorial](https://www.w3schools.com/js/js_json_intro.asp)
* [JSON.org – Giới thiệu chính thức](https://www.json.org/json-en.html)
* [Real Python – Working with JSON Data](https://realpython.com/python-json/)

---

---

## 🧩 Bài tập

> 📝 🎯 **Chủ đề:** `json.dumps`, `json.loads`, `json.dump`, `json.load`, cấu trúc JSON, tiếng Việt trong JSON, lỗi thường gặp, ứng dụng danh bạ / sản phẩm / cấu hình.

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Chuyển từ điển sang JSON

* **Đề bài:** Dùng `json.dumps` chuyển từ điển `{"ten": "An", "tuoi": 15}` thành chuỗi JSON rồi in ra. In cả `type()` của kết quả.
* **Input:** Không có
* **Output:**
  ```
  {"ten": "An", "tuoi": 15}
  <class 'str'>
  ```
* **Gợi ý:** `import json; chuoi = json.dumps(du_lieu)`.

### Bài 2: Chuyển JSON sang Python

* **Đề bài:** Dùng `json.loads` chuyển chuỗi `'{"lop": "10A1", "si_so": 40}'` thành từ điển. In `type()` và giá trị `"si_so"`.
* **Input:** Không có
* **Output:**
  ```
  <class 'dict'>
  40
  ```
* **Gợi ý:** `du_lieu["si_so"]`.

### Bài 3: JSON đẹp với indent

* **Đề bài:** Dùng `json.dumps` với `indent=2` in ra đẹp từ điển `{"a": 1, "b": [1, 2]}`.
* **Input:** Không có
* **Output:**
  ```
  {
    "a": 1,
    "b": [
      1,
      2
    ]
  }
  ```
* **Gợi ý:** `json.dumps(x, indent=2)`.

### Bài 4: List sang JSON

* **Đề bài:** Chuyển danh sách `[10, 20, "ba"]` sang chuỗi JSON và in ra.
* **Input:** Không có
* **Output:**
  ```
  [10, 20, "ba"]
  ```
* **Gợi ý:** `json.dumps` làm việc với cả list.

### Bài 5: Boolean và None

* **Đề bài:** Chuyển từ điển `{"ok": True, "x": None, "diem": 8.5}` sang JSON và in ra.
* **Input:** Không có
* **Output:**
  ```
  {"ok": true, "x": null, "diem": 8.5}
  ```
* **Gợi ý:** Chú ý `true`, `null` viết thường trong JSON.

### Bài 6: Ghi file JSON đầu tiên

* **Đề bài:** Ghi từ điển `{"mon": "Toan", "diem": 9}` vào file `mon.json` (mã hóa utf-8, giữ tiếng Việt). Kiểm tra file tồn tại.
* **Input:** Không có
* **Output:** File `mon.json` xuất hiện (nội dung dạng JSON).
* **Gợi ý:** `with open("mon.json", "w", encoding="utf-8") as f: json.dump(...)`.

### Bài 7: Đọc file JSON

* **Đề bài:** Đọc lại file `mon.json` từ bài 6 bằng `json.load`, in ra `type()` của dữ liệu và giá trị `"diem"`.
* **Input:** File `mon.json` đã tạo ở bài 6.
* **Output:**
  ```
  <class 'dict'>
  9
  ```
* **Gợi ý:** `with open("mon.json", "r", encoding="utf-8") as f: du_lieu = json.load(f)`.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Danh bạ điện thoại

* **Đề bài:** Tạo từ điển danh bạ 3 người (tên → số điện thoại), ghi vào `danh_ba.json` (có `ensure_ascii=False`, `indent=2`), đọc lại và in số điện thoại của người thứ 2.
* **Input:** Không có
* **Output:** Số điện thoại của người thứ 2 (một dòng).
* **Gợi ý:** Làm theo Ví dụ 1 trong bài giảng.

### Bài 9: Lưu danh sách sản phẩm

* **Đề bài:** Danh sách 3 sản phẩm `{"ma", "ten", "gia", "ton_kho"}`. Ghi vào `san_pham.json`, đọc lại và in ra tổng số mặt hàng.
* **Input:** Không có
* **Output:**
  ```
  Tổng mặt hàng: 3
  ```
* **Gợi ý:** `len(danh_sach)` sau khi `json.load`.

### Bài 10: Cấu hình ứng dụng

* **Đề bài:** Tạo cấu hình `{"ten_ung_dung": "LopHocApp", "so_dong": 10, "am_luong": 0.5}`. Lưu vào `cau_hinh.json`, đọc lại, tăng `am_luong` thêm 0.2 rồi lưu lại. In ra cấu hình cuối cùng.
* **Input:** Không có
* **Output:**
  ```
  LopHocApp — âm lượng: 0.7
  ```
* **Gợi ý:** Đọc → sửa `cau_hinh["am_luong"] += 0.2` → ghi lại.

### Bài 11: Thêm ghi chú

* **Đề bài:** Đọc file `ghi_chu.json` (nếu chưa có thì dùng `[]`), thêm một ghi chú `{"tieu_de": "Bai 32", "noi_dung": "Da xong"}` vào cuối, lưu lại. Chạy 2 lần và in số ghi chú sau mỗi lần.
* **Input:** Không có
* **Output:**
  ```
  1
  2
  ```
* **Gợi ý:** Kiểm tra file tồn tại bằng `os.path.exists`; `append` rồi `json.dump`.

### Bài 12: Tính tổng từ JSON phức tạp

* **Đề bài:** Dữ liệu `hoc_sinh = [{"ten": "An", "mon": [8, 7]}, {"ten": "Binh", "mon": [9, 10]}]`. Ghi vào file, đọc lại, in ra tổng điểm của từng học sinh.
* **Input:** Không có
* **Output:**
  ```
  An: 15
  Binh: 19
  ```
* **Gợi ý:** `sum(hs["mon"])` cho mỗi học sinh.

### Bài 13: Sửa lỗi JSON thủ công

* **Đề bài:** File `loi.json` có nội dung sai:
  ```json
  {"ten": 'An', "diem": [8, 9,],}
  ```
  Chạy `json.loads` và ghi lại lỗi xuất hiện. Sau đó sửa lại chuỗi đúng và in kết quả.
* **Input:** Chuỗi JSON sai ở trên.
* **Output:**
  ```
  Lỗi: JSONDecodeError ...
  {'ten': 'An', 'diem': [8, 9]}
  ```
* **Gợi ý:** Lỗi do `'An'` (nháy đơn) và dấu phẩy thừa; sửa bằng `"An"` và bỏ `,`.

### Bài 14: Lọc sản phẩm rẻ

* **Đề bài:** Tạo danh sách sản phẩm 4 món (tên, giá), ghi file, đọc lại và in ra các sản phẩm có giá **dưới 10000 đồng**.
* **Input:** Không có
* **Output:** Tên các sản phẩm rẻ (mỗi tên một dòng).
* **Gợi ý:** Vòng lặp kiểm tra `sp["gia"] < 10000`.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Điểm trung bình và xếp loại

* **Đề bài:** Dữ liệu 4 học sinh `{"ten", "mon": [3 điểm]}`. Ghi file, đọc lại, tính điểm TB mỗi người và xếp loại: TB ≥ 8 là "Giỏi", ≥ 5 là "Đạt", còn lại "Cần cố gắng". In kết quả.
* **Input:** Không có
* **Output:**
  ```
  An: 8.0 - Giỏi
  Binh: 6.0 - Đạt
  ...
  ```
* **Gợi ý:** `sum(hs["mon"]) / len(hs["mon"])` + cấu trúc `if/elif/else`.

### Bài 16: Cập nhật tồn kho khi bán hàng

* **Đề bài:** Đọc `san_pham.json` (3 sản phẩm có `ton_kho`), bán 2 món mã 1, ghi lại file, in ra sản phẩm có `ton_kho` còn lại của mã 1.
* **Input:** File từ bài 9 (hoặc tự tạo).
* **Output:**
  ```
  Ton kho con lai: X
  ```
  (X = ton_kho ban đầu - 2)
* **Gợi ý:** Duyệt danh sách tìm `ma == 1`, giảm `ton_kho`, `json.dump`.

### Bài 17: Gộp hai file JSON

* **Đề bài:** Tạo `lopA.json` (2 học sinh) và `lopB.json` (2 học sinh). Viết chương trình đọc cả hai, gộp vào một danh sách, lưu `tat_ca.json`, in tổng số học sinh.
* **Input:** Hai file JSON tự tạo.
* **Output:**
  ```
  Tổng số học sinh: 4
  ```
* **Gợi ý:** `danh_sach = lop_a + lop_b`.

### Bài 18: Tìm kiếm trong JSON

* **Đề bài:** Danh bạ 5 người lưu trong file. Viết chương trình đọc file và in ra tên của tất cả người có **số điện thoại bắt đầu bằng "0903"**.
* **Input:** Không có
* **Output:** Tên người tìm được (mỗi tên một dòng).
* **Gợi ý:** Duyệt `danh_ba.items()`; kiểm tra `so.startswith("0903")`.

### Bài 19: Đếm số sản phẩm theo loại

* **Đề bài:** Danh sách sản phẩm có trường `"loai"` (VD: "van_phong", "hoc_tap", "sach"). Ghi file, đọc lại, đếm số sản phẩm mỗi loại và in ra.
* **Input:** Không có
* **Output:**
  ```
  van_phong: 2
  hoc_tap: 3
  ...
  ```
* **Gợi ý:** Dùng dict đếm: `dem[sp["loai"]] = dem.get(sp["loai"], 0) + 1`.

### Bài 20: Ứng dụng quản lý điểm chuẩn hoàn chỉnh

* **Đề bài:** Xây ứng dụng nhỏ: menu lựa chọn (1. Thêm học sinh, 2. Xem danh sách, 3. Thoát). Dữ liệu lưu trong `hoc_sinh.json` (danh sách `{"ten", "diem"}`). Thao tác mỗi lần lưu đều ghi lại file.
* **Input:** Nhập từ bàn phím: `1`, `An 8` (tên kèm điểm), `2`, `3`.
* **Output:** Xem danh sách hiển thị từng học sinh kèm điểm; thoát khi chọn 3.
* **Gợi ý:** Dùng `while True`, `if chon == "1"` đọc file → append → ghi; `if chon == "2"` đọc và in; `if chon == "3"` `break`.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Chuyển đổi thành thạo giữa Python và JSON (dumps/loads/dump/load).
* ✅ Ghi/đọc file JSON tiếng Việt đúng chuẩn (`utf-8`, `ensure_ascii=False`).
* ✅ Xây được các ứng dụng thực tế: danh bạ, sản phẩm, cấu hình, ghi chú, quản lý điểm.
* ✅ Nhận biết và sửa các lỗi JSON phổ biến.

> 💪 Chưa tự làm được bài nào thì đừng lo — đọc lại bài giảng, làm từng bước: ghi thử, mở file xem nội dung, đọc lại. **Lập trình là luyện tập!**

---

## ✅ Đáp án

> 💡 **Hãy tự làm bài tập trước** rồi mới mở đáp án.

## 🟢 Dễ (Bài 1 – 7)


<details>
<summary>✅ Bài 1: Chuyển từ điển sang JSON</summary>


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

</details>

<details>
<summary>✅ Bài 2: Chuyển JSON sang Python</summary>


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

</details>

<details>
<summary>✅ Bài 3: JSON đẹp với indent</summary>


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

</details>

<details>
<summary>✅ Bài 4: List sang JSON</summary>


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

</details>

<details>
<summary>✅ Bài 5: Boolean và None</summary>


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

</details>

<details>
<summary>✅ Bài 6: Ghi file JSON đầu tiên</summary>


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

</details>

<details>
<summary>✅ Bài 7: Đọc file JSON</summary>


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

</details>

## 🟡 Trung bình (Bài 8 – 14)


<details>
<summary>✅ Bài 8: Danh bạ điện thoại</summary>


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

</details>

<details>
<summary>✅ Bài 9: Lưu danh sách sản phẩm</summary>


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

</details>

<details>
<summary>✅ Bài 10: Cấu hình ứng dụng</summary>


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

</details>

<details>
<summary>✅ Bài 11: Thêm ghi chú</summary>


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

</details>

<details>
<summary>✅ Bài 12: Tính tổng từ JSON phức tạp</summary>


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

</details>

<details>
<summary>✅ Bài 13: Sửa lỗi JSON thủ công</summary>


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

</details>

<details>
<summary>✅ Bài 14: Lọc sản phẩm rẻ</summary>


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

</details>

## 🔴 Khó (Bài 15 – 20)


<details>
<summary>✅ Bài 15: Điểm trung bình và xếp loại</summary>


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

</details>

<details>
<summary>✅ Bài 16: Cập nhật tồn kho khi bán hàng</summary>


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

</details>

<details>
<summary>✅ Bài 17: Gộp hai file JSON</summary>


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

</details>

<details>
<summary>✅ Bài 18: Tìm kiếm trong JSON</summary>


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

</details>

<details>
<summary>✅ Bài 19: Đếm số sản phẩm theo loại</summary>


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

</details>

<details>
<summary>✅ Bài 20: Ứng dụng quản lý điểm hoàn chỉnh</summary>


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

</details>

## 📌 Lời khuyên cuối


* Nhớ bộ tứ: `dumps`/`loads` cho chuỗi, `dump`/`load` cho file.
* Khi ghi: `encoding="utf-8"` + `ensure_ascii=False`; khi đọc: `encoding="utf-8"`.
* Gặp `JSONDecodeError` → mở file, kiểm tra ngoặc, nháy kép, dấu phẩy.
* Mỗi file JSON chỉ chứa một đối tượng duy nhất.
* JSON là nền tảng cho API (bài 34) và Requests (bài 35) — nắm chắc bài này bạn sẽ học sau rất nhẹ!

👉 Tiếp theo: **[Bài 33: CSV](../04-CSV/bai.md)**

---

## ➡️ Điều hướng

**Vị trí:** `03-Thuc-Chien/03-JSON/bai.md`

**Bài tiếp theo:** [Bài 33 — CSV – Dữ Liệu Dạng Bảng](../04-CSV/bai.md)
