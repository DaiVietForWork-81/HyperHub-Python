# 🗂️ Bài 33: CSV – Dữ Liệu Dạng Bảng

> 🎓 **Chương 10 – Dữ liệu và mạng**
> Bài 32 bạn đã học JSON — định dạng lưu dữ liệu có cấu trúc lồng nhau. Bài này giới thiệu **CSV** — "người hàng xóm" đơn giản hơn nhiều: một file văn bản dạng bảng mà Excel, Google Sheets và các hệ thống khoa học dữ liệu đều mở được. Học CSV giúp bạn đọc/ghi dữ liệu bảng tính không cần phần mềm đặc biệt.

---

## 🎯 Mục tiêu

Sau bài học này, học viên sẽ:

* ✅ Hiểu **CSV là gì** và cấu trúc dạng bảng (cột, dòng, dấu phẩy).
* ✅ Đọc file CSV bằng **`csv.reader`** (từng dòng là list).
* ✅ Ghi file CSV bằng **`csv.writer`**.
* ✅ Đọc bằng **`csv.DictReader`** (mỗi dòng là từ điển) và ghi bằng **`csv.DictWriter`**.
* ✅ Xử lý được **dấu phân cách** khác (dấu chấm phẩy `;`) và **mã hóa** tiếng Việt.
* ✅ Ứng dụng thực tế: danh sách học sinh, xuất bảng điểm, lọc dữ liệu.

---

## 📖 Kiến thức

### 1. Nhắc nhẹ bài trước — từ JSON sang CSV

JSON lưu dữ liệu **lồng nhau** (dict trong list), CSV lưu dữ liệu **phẳng dạng bảng**. Khi nào dùng gì?

| Tiêu chí | JSON | CSV |
|---|---|---|
| Cấu trúc | Lồng nhau, linh hoạt | Bảng phẳng (dòng + cột) |
| Đọc bằng con người | Tương đối | Rất dễ (mở bằng Excel) |
| Kiểu dữ liệu | Có (số, boolean, null) | Tất cả là chuỗi văn bản |
| Dùng cho | Cấu hình, API, dữ liệu phức tạp | Bảng điểm, danh sách, xuất nhập dữ liệu |

### 2. CSV là gì?

**CSV** (Comma-Separated Values — Giá trị phân cách bằng dấu phẩy) là **định dạng văn bản lưu dữ liệu dạng bảng**:

* 🧾 Mỗi **dòng** là một **bản ghi** (học sinh, sản phẩm...).
* ➗ Mỗi dòng gồm các **cột** cách nhau bằng dấu phẩy `,`.
* 📑 Dòng đầu tiên thường là **tiêu đề cột** (tên các trường).

```csv
ten,lop,diem
An,10A1,8
Binh,10A2,7
Chi,10A1,9
```

> 💬 **Ví dụ đời thực:** CSV giống **bảng điểm giấy** — mỗi hàng là một bạn, mỗi ô là một thông tin, các ô cách nhau bằng dấu phẩy. Excel mở file CSV như mở bảng tính bình thường.

### 3. Đọc CSV bằng `csv.reader`

Module `csv` có sẵn trong Python — không cần cài:

```python
import csv

with open("hoc_sinh.csv", "r", encoding="utf-8") as f:
    doc = csv.reader(f)      # tạo đối tượng đọc
    for dong in doc:         # mỗi dòng là một LIST
        print(dong)
```

Kết quả (file ở mục 2):

```
['ten', 'lop', 'diem']
['An', '10A1', '8']
['Binh', '10A2', '7']
['Chi', '10A1', '9']
```

> 💡 `csv.reader(f)` trả về một **iterator** (bài 29!) — mỗi lần `next` trả một dòng dạng list. Chính xác là vòng lặp `for` tự duyệt.

**Đọc có tách tiêu đề:**

```python
with open("hoc_sinh.csv", "r", encoding="utf-8") as f:
    doc = csv.reader(f)
    tieu_de = next(doc)      # lấy dòng tiêu đề
    print("Các cột:", tieu_de)
    for dong in doc:         # các dòng còn lại
        print(dong[0], "—", dong[2])
```

Kết quả:

```
Các cột: ['ten', 'lop', 'diem']
An — 8
Binh — 7
Chi — 9
```

### 4. Ghi CSV bằng `csv.writer`

```python
import csv

du_lieu = [
    ["ten", "lop", "diem"],
    ["An", "10A1", 8],
    ["Binh", "10A2", 7],
]

with open("hoc_sinh.csv", "w", encoding="utf-8", newline="") as f:
    ghi = csv.writer(f)
    for dong in du_lieu:
        ghi.writerow(dong)   # ghi từng dòng
```

> ⚠️ **Quan trọng:** khi ghi CSV trên Windows phải thêm **`newline=""`** khi mở file — nếu không, file sẽ có dòng trống giữa mỗi dòng dữ liệu!

**Ghi nhiều dòng cùng lúc bằng `writerows`:**

```python
ghi.writerows(du_lieu)   # ghi cả danh sách dòng một lần
```

### 5. `csv.DictReader` — mỗi dòng là từ điển

Tiện hơn: dòng tiêu đề trở thành **khóa**, mỗi dòng trở thành **dict**:

```python
import csv

with open("hoc_sinh.csv", "r", encoding="utf-8") as f:
    doc = csv.DictReader(f)
    for dong in doc:
        print(dong["ten"], "học lớp", dong["lop"])
```

Kết quả:

```
An học lớp 10A1
Binh học lớp 10A2
Chi học lớp 10A1
```

> 💡 Truy cập cột bằng tên (`dong["diem"]`) thay vì vị trí (`dong[2]`) — dễ đọc và bền vững khi thứ tự cột thay đổi.

### 6. `csv.DictWriter` — ghi từ điển

```python
import csv

du_lieu = [
    {"ten": "An", "lop": "10A1", "diem": 8},
    {"ten": "Binh", "lop": "10A2", "diem": 7},
]

with open("hoc_sinh.csv", "w", encoding="utf-8", newline="") as f:
    cot = ["ten", "lop", "diem"]
    ghi = csv.DictWriter(f, fieldnames=cot)
    ghi.writeheader()       # tự ghi dòng tiêu đề từ fieldnames
    for dong in du_lieu:
        ghi.writerow(dong)
```

| Phương thức | Việc làm |
|---|---|
| `csv.DictWriter(f, fieldnames=cot)` | Tạo đối tượng ghi, khai báo thứ tự cột |
| `writeheader()` | Ghi dòng tiêu đề (tên các cột) |
| `writerow(dict)` | Ghi một dòng từ từ điển |

### 7. Dấu phân cách khác — chấm phẩy `;`

Một số vùng (và Excel khi đặt ngôn ngữ khác) dùng `;` thay vì `,`:

```python
with open("du_lieu.csv", "r", encoding="utf-8") as f:
    doc = csv.reader(f, delimiter=";")   # chỉ định dấu phân cách
    for dong in doc:
        print(dong)
```

```python
ghi = csv.writer(f, delimiter=";")
```

> 💡 Nếu file dùng `\t` (tab), dùng `delimiter="\t"`. Kỹ thuật giống hệt, chỉ đổi tham số.

### 8. Mã hóa tiếng Việt trong CSV

Giống bài 32 — chú ý `encoding`:

* ✅ **Chuẩn nhất:** `encoding="utf-8"` — hiện đại, đúng chuẩn.
* ⚠️ **Excel cũ đôi khi:** `encoding="utf-8-sig"` (có BOM để Excel mở không lỗi dấu).
* ⚠️ **File Việt cũ:** `encoding="cp1258"` hoặc `"latin-1"` — khi mở file lạ không rõ mã hóa, thử các giá trị này.

```python
with open("bang_diem.csv", "r", encoding="utf-8-sig") as f:
    doc = csv.DictReader(f)
    for dong in doc:
        print(dong["ten"], dong["diem"])
```

> 🧪 **Mẹo xử lý nhanh:** gặp file đọc ra "loạn dấu", thử lần lượt `utf-8-sig` → `cp1258` → `latin-1`.

### 9. CSV vs file thường — vì sao không tự ghi bằng `split(",")`?

Bạn có thể "tự làm" nhưng dễ sai: dữ liệu chứa dấu phẩy trong nội dung (ví dụ tên `"Nguyen, Van"`) sẽ làm vỡ cột. Module `csv` xử lý hết: **bọc nội dung có dấu phẩy bằng nháy kép**, xử lý `\n` bên trong... Nói chung — **đừng tự làm, cứ dùng `csv`!**

> 💬 **Ví dụ đời thực:** `csv` giống **máy in tiêu chuẩn** — bạn đưa dữ liệu, máy lo phần "đóng gói" đúng quy cách. Tự `split(",")` giống đóng gói bằng tay: nhanh lúc đầu, vỡ lúc sau.

---

## 💡 Ví dụ minh họa

### Ví dụ 1: Danh sách học sinh — ghi và đọc

```python
import csv

# 1. Dữ liệu học sinh
hoc_sinh = [
    {"ten": "Nguyễn Văn An", "lop": "10A1", "diem": 8},
    {"ten": "Trần Thị Bình", "lop": "10A2", "diem": 7},
    {"ten": "Lê Văn Cường", "lop": "10A1", "diem": 9},
]

# 2. Ghi file CSV
cot = ["ten", "lop", "diem"]
with open("hoc_sinh.csv", "w", encoding="utf-8", newline="") as f:
    ghi = csv.DictWriter(f, fieldnames=cot)
    ghi.writeheader()
    ghi.writerows(hoc_sinh)

# 3. Đọc lại và hiển thị
with open("hoc_sinh.csv", "r", encoding="utf-8") as f:
    doc = csv.DictReader(f)
    for hs in doc:
        print(f"{hs['ten']} - {hs['lop']} - {hs['diem']}")
```

**Giải thích từng dòng:**

| Dòng | Ý nghĩa |
|---|---|
| `cot = ["ten", "lop", "diem"]` | Khai báo thứ tự cột |
| `csv.DictWriter(f, fieldnames=cot)` | Ghi theo tên cột |
| `ghi.writeheader()` | Tự tạo dòng tiêu đề |
| `ghi.writerows(hoc_sinh)` | Ghi cả danh sách một lúc |
| `csv.DictReader(f)` | Đọc, dòng đầu làm khóa |
| `hs['ten']` | Lấy giá trị cột theo tên |

### Ví dụ 2: Xuất bảng điểm ra file CSV

```python
import csv

diem_van = {"An": 8, "Binh": 7, "Chi": 9}
diem_toan = {"An": 9, "Binh": 6, "Chi": 10}

with open("bang_diem.csv", "w", encoding="utf-8", newline="") as f:
    ghi = csv.writer(f)
    ghi.writerow(["ten", "van", "toan", "tb"])   # dòng tiêu đề
    for ten in diem_van:
        van = diem_van[ten]
        toan = diem_toan[ten]
        tb = (van + toan) / 2
        ghi.writerow([ten, van, toan, tb])

print("Đã xuất bang_diem.csv")
```

Kết quả trong file:

```csv
ten,van,toan,tb
An,8,9,8.5
Binh,7,6,6.5
Chi,9,10,9.5
```

### Ví dụ 3: Lọc dữ liệu từ CSV

```python
import csv

# Giả sử đã có file hoc_sinh.csv từ ví dụ 1
with open("hoc_sinh.csv", "r", encoding="utf-8") as f:
    doc = csv.DictReader(f)
    for hs in doc:
        if float(hs["diem"]) >= 8:      # lọc học sinh điểm cao
            print(hs["ten"], "được", hs["diem"], "điểm")
```

Kết quả:

```
Nguyễn Văn An được 8 điểm
Lê Văn Cường được 9 điểm
```

> ⚠️ Chú ý: dữ liệu đọc từ CSV luôn là **chuỗi** — cần `float(...)`/`int(...)` trước khi so sánh số!

---

## 🔬 Ví dụ nâng cao

### Ví dụ 1: Tính điểm trung bình cả lớp từ CSV

```python
import csv

with open("bang_diem.csv", "r", encoding="utf-8") as f:
    doc = csv.DictReader(f)
    danh_sach = list(doc)   # chuyển iterator thành list để dùng lại

tong = 0
for hs in danh_sach:
    tong += float(hs["tb"])

print(f"Điểm TB cả lớp: {tong / len(danh_sach):.2f}")
```

### Ví dụ 2: Thêm cột tính toán khi xuất

```python
import csv

with open("bang_diem.csv", "r", encoding="utf-8") as f:
    doc = csv.DictReader(f)
    danh_sach = list(doc)

# Thêm cột xếp loại
for hs in danh_sach:
    tb = float(hs["tb"])
    hs["loai"] = "Gioi" if tb >= 8 else "Dat"

with open("bang_diem_xep_loai.csv", "w", encoding="utf-8", newline="") as f:
    cot = ["ten", "van", "toan", "tb", "loai"]
    ghi = csv.DictWriter(f, fieldnames=cot)
    ghi.writeheader()
    ghi.writerows(danh_sach)

print("Đã xuất file có cột xếp loại")
```

### Ví dụ 3: Đọc CSV dấu `;` — dữ liệu xuất từ Excel Việt

```python
import csv

# File tạo sẵn với dấu ; (Excel VN hay xuất kiểu này)
with open("du_lieu_vn.csv", "r", encoding="utf-8-sig") as f:
    doc = csv.reader(f, delimiter=";")
    for dong in doc:
        print(dong)
```

> 🏪 **Tình huống thực tế:** Cô giáo xuất danh sách từ Excel, gửi qua Zalo; bạn nhận file CSV, mở bằng Python, lọc học sinh đậu, xuất bảng xếp loại — toàn bộ chỉ cần module `csv` có sẵn.

---

## ⚠️ Lỗi thường gặp

### Lỗi 1: Quên `newline=""` khi ghi → file toàn dòng trống

```python
with open("x.csv", "w", encoding="utf-8") as f:   # ❌ thiếu newline=""
    ...
```

* **Nguyên nhân:** Windows chèn thêm ký tự xuống dòng cho mỗi `\n`.
* **Cách sửa:** `open("x.csv", "w", encoding="utf-8", newline="")`.

### Lỗi 2: So sánh số mà quên chuyển đổi kiểu

```python
if hs["diem"] >= 8:   # ❌ "diem" là chuỗi "8", so sánh sai
```

* **Nguyên nhân:** CSV lưu toàn bộ là văn bản.
* **Cách sửa:** `if float(hs["diem"]) >= 8:`.

### Lỗi 3: Tiếng Việt đọc ra loạn dấu

* **Nguyên nhân:** mã hóa file không phải `utf-8` (Excel VN hay dùng `cp1258`/`utf-8-sig`).
* **Cách sửa:** thử lần lượt `encoding="utf-8-sig"` → `"cp1258"` → `"latin-1"`.

### Lỗi 4: `KeyError` khi dùng DictReader

* **Nguyên nhân:** tên cột không khớp (thường do tiêu đề bị dấu cách thừa, hoặc thiếu `writeheader()`).
* **Cách sửa:** in thử dòng đầu bằng `next(doc)` để xem tên cột thực tế; kiểm tra file.

### Lỗi 5: Quên rằng DictReader là iterator — dùng lại lần hai thấy rỗng

```python
doc = csv.DictReader(f)
print(list(doc))   # đầy đủ
print(list(doc))   # [] — đã duyệt hết!
```

* **Nguyên nhân:** iterator dùng một lần (bài 29!).
* **Cách sửa:** `danh_sach = list(doc)` ngay sau khi đọc.

---

## 💎 Mẹo

* 🧾 **`DictReader`/`DictWriter` là lựa chọn số 1** — code theo tên cột, dễ đọc, ít lỗi.
* 📄 Ghi CSV luôn nhớ ba thứ: `encoding="utf-8"`, `newline=""`, `delimiter` đúng.
* 🔢 **Ép kiểu ngay khi đọc:** `int(dong["so_luong"])` — đừng để số như chuỗi lan sang tính toán.
* 🐍 `csv.reader` trả iterator — nếu cần dùng lại, chuyển `list()`.
* 🧪 Mở file CSV bằng Excel để "nhìn thấy" kết quả — trực quan, dễ tự kiểm tra.
* 🔀 Giữa JSON và CSV: dữ liệu lồng nhau dùng JSON; bảng phẳng dùng CSV; API trả JSON nhưng Excel cần CSV.

---

## 📝 Tóm tắt

| Công cụ | Chức năng | Dữ liệu mỗi dòng |
|---|---|---|
| `csv.reader(f)` | Đọc CSV | List `[...]` |
| `csv.writer(f)` | Ghi CSV | `writerow(list)` / `writerows` |
| `csv.DictReader(f)` | Đọc CSV | Dict `{ten_cot: gia_tri}` |
| `csv.DictWriter(f, fieldnames=...)` | Ghi CSV | `writeheader()` + `writerow(dict)` |
| `delimiter=";"` | Đổi dấu phân cách | — |
| `encoding="utf-8"` | Mã hóa chuẩn | — |
| `newline=""` | Tránh dòng trống khi ghi | — |

---

## 🧪 Kiểm tra nhanh

1. ❓ CSV là gì? Mỗi dòng là gì, mỗi cột cách nhau bằng gì?
2. ❓ Sự khác nhau giữa `csv.reader` và `csv.DictReader`?
3. ❓ Ba tham số quan trọng khi mở file CSV để ghi?
4. ❓ Vì sao dữ liệu đọc từ CSV phải ép kiểu trước khi tính toán?
5. ❓ `writeheader()` dùng để làm gì?
6. ❓ File CSV dùng dấu `;` thì làm sao đọc đúng?
7. ❓ Quên `newline=""` gây lỗi gì?
8. ❓ Khi nào dùng JSON, khi nào dùng CSV?
9. ❓ Vì sao không nên tự `split(",")` để đọc CSV?
10. ❓ Làm gì khi đọc file CSV tiếng Việt ra loạn dấu?

<details>
<summary>🔍 Xem đáp án</summary>

1. Định dạng văn bản dạng bảng; mỗi dòng là một bản ghi, các cột cách nhau dấu phẩy.
2. `reader` trả mỗi dòng là list; `DictReader` trả mỗi dòng là dict theo tên cột.
3. `encoding="utf-8"`, `newline=""`, và `delimiter` (nếu cần).
4. Vì mọi giá trị CSV đều là chuỗi; so sánh/cộng số phải chuyển `int`/`float`.
5. Ghi dòng tiêu đề (tên các cột) từ `fieldnames`.
6. Dùng `csv.reader(f, delimiter=";")` (hoặc `;` cho writer).
7. File sinh ra có dòng trống giữa mỗi dòng dữ liệu (trên Windows).
8. JSON cho dữ liệu lồng nhau/phức tạp; CSV cho bảng phẳng, trao đổi với Excel.
9. Vì dữ liệu chứa dấu phẩy/nháy sẽ vỡ cột; module csv tự bọc nháy kép, xử lý chuẩn.
10. Thử lần lượt các mã hóa: `utf-8-sig` → `cp1258` → `latin-1`.

</details>

---

## 📚 Bài đọc thêm

* [Python.org – csv module](https://docs.python.org/3/library/csv.html)
* [Real Python – Reading and Writing CSV Files](https://realpython.com/python-csv/)
* [W3Schools – CSV Files](https://www.w3schools.com/python/python_file_handling.asp)
* [Wikipedia – CSV](https://vi.wikipedia.org/wiki/CSV)

---

## 🏁 Kết thúc bài

🗂️ Tuyệt vời! Bạn đã biết đọc/ghi dữ liệu bảng. Giờ là lúc bước ra **thế giới mạng**: làm sao lấy dữ liệu từ các trang web và dịch vụ trực tuyến? Câu trả lời nằm ở **API** — giao tiếp giữa các chương trình với nhau qua internet. Hãy sang:

👉 **[Bài 34: API – Giao Tiếp Giữa Các Chương Trình](../34_API/bai_giang.md)**