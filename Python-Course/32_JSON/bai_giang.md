# 📊 Bài 32: JSON – Ngôn Ngữ Lưu Trữ Dữ Liệu

> 🎓 **Chương 10 – Dữ liệu và mạng**
> Bài 22 bạn đã học ghi/đọc file văn bản; bài 30-31 là môi trường ảo và pip. Bây giờ đến lượt một định dạng đặc biệt quan trọng: **JSON** — ngôn ngữ mà mọi website, điện thoại và ứng dụng dùng để trao đổi dữ liệu. Học JSON là bước đệm hoàn hảo cho bài 34 (API) và bài 35 (Requests).

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

## 🏁 Kết thúc bài

📊 Tuyệt vời! Bạn đã biết lưu dữ liệu có cấu trúc bằng JSON. Một "họ hàng" cũng phổ biến không kém trong bảng tính và khoa học dữ liệu là **CSV** — định dạng bảng đơn giản nhất. Hãy sang:

👉 **[Bài 33: CSV – Dữ Liệu Dạng Bảng](../33_CSV/bai_giang.md)**