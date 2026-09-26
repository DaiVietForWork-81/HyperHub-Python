<!-- TỰ ĐỘNG ĐỒNG BỘ từ 03-Thuc-Chien/04-CSV/bai.md — đừng sửa trực tiếp, sửa bản chính rồi chạy tools/sync_tracks.py -->

# Bài 33 — CSV – Dữ Liệu Dạng Bảng

> 🎓 **Chương 10 – Dữ liệu và mạng**
> Bài 32 bạn đã học JSON — định dạng lưu dữ liệu có cấu trúc lồng nhau. Bài này giới thiệu **CSV** — "người hàng xóm" đơn giản hơn nhiều: một file văn bản dạng bảng mà Excel, Google Sheets và các hệ thống khoa học dữ liệu đều mở được. Học CSV giúp bạn đọc/ghi dữ liệu bảng tính không cần phần mềm đặc biệt.

## 🧠 Điều kiện tiên quyết

- [Bài 22 — Đọc Và Ghi File Trong Python](../Phan-1-Co-Ban/22-File/bai.md)

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

---

## 🧩 Bài tập

> 📝 📋 **Chương 10 – Dữ liệu và mạng**

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Ghi danh sách môn học

* **Đề bài:** Dùng `csv.writer` ghi danh sách các môn học của trường ra file `mon_hoc.csv`. Mỗi môn một dòng, cột đầu là mã môn, cột sau là tên môn.
* **Input:** Danh sách mã môn: `"TOAN", "VAN", "TIN"` kèm tên: `"Toán", "Ngữ văn", "Tin học"`.
* **Output:** File `mon_hoc.csv` với 3 dòng dữ liệu (không cần tiêu đề).
* **Ví dụ:**
  ```
  TOAN,Toán
  VAN,Ngữ văn
  TIN,Tin học
  ```
* **Gợi ý:** Tạo danh sách các dòng, mỗi dòng là một list hai phần tử; dùng `with open(...)` với `newline=""`.

### Bài 2: Đọc file và in từng dòng

* **Đề bài:** Đọc file `mon_hoc.csv` (tạo ở bài 1) bằng `csv.reader` và in từng dòng ra màn hình dưới dạng list.
* **Input:** File `mon_hoc.csv` có sẵn.
* **Output:**
  ```
  ['TOAN', 'Toán']
  ['VAN', 'Ngữ văn']
  ['TIN', 'Tin học']
  ```
* **Gợi ý:** Mở file với `encoding="utf-8"`, tạo `csv.reader(f)` rồi `for dong in doc: print(dong)`.

### Bài 3: Ghi danh sách học viên

* **Đề bài:** Dùng `csv.writer` ghi danh sách 3 học viên (tên, lớp) ra file `hoc_vien.csv`.
* **Input:** `"An"` – `"10A1"`, `"Binh"` – `"10A2"`, `"Chi"` – `"10A1"`.
* **Output:** File `hoc_vien.csv` có dòng tiêu đề `ten,lop` và 3 dòng dữ liệu.
* **Gợi ý:** Dòng đầu tiên là tiêu đề cột, sau đó mới đến dữ liệu; mỗi lần ghi một dòng bằng `writerow(...)`.

### Bài 4: In tên và điểm bằng DictReader

* **Đề bài:** Đọc file `bang_diem.csv` (có tiêu đề `ten,diem`) bằng `csv.DictReader`, in ra mỗi dòng dạng `ten - diem`.
* **Input:**
  ```csv
  ten,diem
  An,8
  Binh,7
  Chi,9
  ```
* **Output:**
  ```
  An - 8
  Binh - 7
  Chi - 9
  ```
* **Gợi ý:** Truy cập cột bằng tên khóa: `dong["ten"]`, `dong["diem"]`.

### Bài 5: Xuất bảng điểm bằng DictWriter

* **Đề bài:** Dùng `csv.DictWriter` ghi danh sách học viên dạng dict (tên, lớp, điểm) ra file `bang_diem_moi.csv`, có dòng tiêu đề.
* **Input:** Danh sách dict: `{"ten": "An", "lop": "10A1", "diem": 8}`, `{"ten": "Binh", "lop": "10A2", "diem": 7}`.
* **Output:** File `bang_diem_moi.csv` với tiêu đề `ten,lop,diem` và 2 dòng dữ liệu.
* **Gợi ý:** `fieldnames=["ten", "lop", "diem"]`, gọi `writeheader()` trước khi `writerow()`.

### Bài 6: Đọc file dấu chấm phẩy

* **Đề bài:** Đọc file `du_lieu_vn.csv` dùng dấu `;` làm phân cách, in từng dòng ra màn hình.
* **Input:**
  ```csv
  ten;lop
  An;10A1
  Binh;10A2
  ```
* **Output:** Các list tương ứng với từng dòng.
* **Gợi ý:** Truyền tham số `delimiter=";"` cho `csv.reader`.

### Bài 7: Đếm số học viên

* **Đề bài:** Đọc file `hoc_vien.csv` (bài 3) bằng `csv.reader`, đếm xem có bao nhiêu học viên (không tính dòng tiêu đề).
* **Input:** File `hoc_vien.csv` có tiêu đề `ten,lop` + 3 dòng dữ liệu.
* **Output:** `So hoc vien: 3`
* **Gợi ý:** Dùng `next(doc)` để bỏ qua dòng tiêu đề, đếm các dòng còn lại trong vòng `for`.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Tính điểm trung bình từng học viên

* **Đề bài:** Đọc file `bang_diem.csv` (tiêu đề `ten,van,toan`), tính trung bình 2 môn của từng học viên và in ra.
* **Input:**
  ```csv
  ten,van,toan
  An,8,9
  Binh,7,6
  Chi,9,10
  ```
* **Output:**
  ```
  An: 8.5
  Binh: 6.5
  Chi: 9.5
  ```
* **Gợi ý:** Giá trị đọc từ CSV là chuỗi — nhớ ép kiểu `float()` trước khi cộng.

### Bài 9: Lọc học viên điểm cao

* **Đề bài:** Đọc file `bang_diem.csv` (tiêu đề `ten,diem`), in ra tên các học viên có điểm từ 8 trở lên.
* **Input:**
  ```csv
  ten,diem
  An,8
  Binh,7
  Chi,9
  Duong,6
  ```
* **Output:**
  ```
  An
  Chi
  ```
* **Gợi ý:** Dùng `csv.DictReader` + điều kiện `float(dong["diem"]) >= 8`.

### Bài 10: Tìm học viên điểm cao nhất

* **Đề bài:** Đọc file `bang_diem.csv` (tiêu đề `ten,diem`), tìm và in tên học viên có điểm cao nhất kèm số điểm.
* **Input:**
  ```csv
  ten,diem
  An,8
  Binh,7
  Chi,9
  ```
* **Output:** `Chi dat diem cao nhat: 9`
* **Gợi ý:** Lưu biến `ten_max` và `diem_max`, cập nhật khi gặp điểm lớn hơn.

### Bài 11: Xuất CSV thêm cột tổng và trung bình

* **Đề bài:** Đọc file `bang_diem.csv` (tiêu đề `ten,van,toan`), thêm cột `tong` (tổng 2 môn) và `tb` (trung bình) rồi ghi ra file `bang_diem_tong.csv`.
* **Input:**
  ```csv
  ten,van,toan
  An,8,9
  Binh,7,6
  ```
* **Output:** File `bang_diem_tong.csv` với tiêu đề `ten,van,toan,tong,tb`.
* **Gợi ý:** Đọc hết vào list dict, tính toán thêm khóa mới, rồi `csv.DictWriter` với `fieldnames` đầy đủ.

### Bài 12: Xếp loại học lực

* **Đề bài:** Đọc file `bang_diem_tong.csv` (bài 11), xếp loại theo điểm TB: `>= 8` là "Gioi", `>= 6.5` là "Kha", còn lại là "TB". Xuất ra file `xep_loai.csv` thêm cột `loai`.
* **Input:** File `bang_diem_tong.csv` từ bài 11.
* **Output:** File `xep_loai.csv` có cột `loai` tương ứng.
* **Gợi ý:** Dùng câu lệnh `if/elif/else` trên `float(hs["tb"])`.

### Bài 13: Chuyển JSON sang CSV

* **Đề bài:** Bạn có danh sách sản phẩm dạng JSON (list dict với các trường `ten`, `gia`, `so_luong`). Dùng `json.loads` (bài 32) để đọc, rồi ghi ra file `san_pham.csv` bằng `csv.DictWriter`.
* **Input:** Chuỗi JSON: `[{"ten": "Vo", "gia": 5000, "so_luong": 10}, {"ten": "But", "gia": 3000, "so_luong": 15}]`.
* **Output:** File `san_pham.csv` với tiêu đề `ten,gia,so_luong`.
* **Gợi ý:** `json.loads(chuoi)` trả list dict; ghi bằng `csv.DictWriter(f, fieldnames=["ten", "gia", "so_luong"])`.

### Bài 14: Cộng điểm hai file CSV

* **Đề bài:** File `diem_van.csv` (tiêu đề `ten,diem`) và file `diem_toan.csv` (tiêu đề `ten,diem`) của cùng danh sách học viên. Đọc cả hai, ghép theo tên và ghi file `diem_tong.csv` với tiêu đề `ten,van,toan,tb`.
* **Input:** Hai file có cùng các tên học viên (có thể khác thứ tự).
* **Output:** File `diem_tong.csv` gồm đủ 3 học viên.
* **Gợi ý:** Đọc từng file thành dict `{ten: diem}`, lặp qua danh sách tên của file thứ nhất.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Thống kê theo lớp

* **Đề bài:** Đọc file `hoc_sinh.csv` (tiêu đề `ten,lop,diem`), tính số lượng học viên và điểm trung bình của từng lớp. In kết quả.
* **Input:**
  ```csv
  ten,lop,diem
  An,10A1,8
  Binh,10A2,7
  Chi,10A1,9
  Dung,10A2,5
  Em,10A1,6
  ```
* **Output:**
  ```
  10A1: 3 hoc vien, diem TB 7.67
  10A2: 2 hoc vien, diem TB 6.00
  ```
* **Gợi ý:** Dùng dict với khóa là tên lớp, giá trị là [tổng điểm, số lượng]; làm tròn 2 chữ số bằng `round(x, 2)`.

### Bài 16: Gộp nhiều file CSV

* **Đề bài:** Có 3 file `lop_a.csv`, `lop_b.csv`, `lop_c.csv` (cùng tiêu đề `ten,diem`). Gộp toàn bộ dữ liệu vào một file `tat_ca.csv` (chỉ một dòng tiêu đề duy nhất).
* **Input:** 3 file với mỗi file 2–3 học viên.
* **Output:** File `tat_ca.csv` có đầy đủ học viên của 3 lớp.
* **Gợi ý:** Mở file đích ở chế độ `"w"` một lần, ghi tiêu đề rồi mở từng file nguồn bằng `csv.reader`; dùng `next(doc)` để bỏ tiêu đề của file nguồn.

### Bài 17: Cập nhật điểm trong CSV

* **Đề bài:** Đọc file `bang_diem.csv` (tiêu đề `ten,diem`), học viên nào điểm dưới 7 được cộng thêm 1 điểm (không vượt quá 10). Ghi kết quả đè lại chính file đó.
* **Input:**
  ```csv
  ten,diem
  An,8
  Binh,6
  Chi,9
  Duong,5
  ```
* **Output:** Trong file: Binh thành 7, Duong thành 6; An, Chi giữ nguyên.
* **Gợi ý:** Đọc hết vào list, sửa giá trị rồi ghi lại với `newline=""`; dùng `min(diem + 1, 10)`.

### Bài 18: Kiểm tra file CSV hợp lệ

* **Đề bài:** File `du_lieu.txt` có các dòng, dòng nào có đúng 3 cột là hợp lệ, dòng nào khác số cột là lỗi. Viết chương trình đọc (dùng `csv.reader`) và in kết quả kiểm tra từng dòng.
* **Input:**
  ```
  ten,lop,diem
  An,10A1,8
  Binh,10A2
  Chi,10A1,9
  Dung,10A2,7
  ```
* **Output:**
  ```
  Dong 1 (tieu de): 3 cot - OK
  Dong 2: 3 cot - OK
  Dong 3: 2 cot - LOI
  Dong 4: 3 cot - OK
  Dong 5: 3 cot - OK
  ```
* **Gợi ý:** `len(dong)` chính là số cột của dòng đó; đếm số thứ tự dòng bằng biến đếm trong vòng lặp.

### Bài 19: Chuyển đổi mã hóa và dấu phân cách

* **Đề bài:** File `excel_vn.csv` do Excel tiếng Việt xuất ra: mã hóa `utf-8-sig`, dấu phân cách `;`, tiêu đề `ho_ten;lop;diem`. Đọc đúng file này và ghi ra file `chuan.csv` chuẩn hóa: mã hóa `utf-8`, dấu phân cách `,`.
* **Input:**
  ```csv
  ho_ten;lop;diem
  Nguyễn Văn An;10A1;8
  Trần Thị Bình;10A2;7
  ```
* **Output:** File `chuan.csv` với dấu `,`, mở bằng Excel không loạn dấu.
* **Gợi ý:** Đọc với `encoding="utf-8-sig"` + `delimiter=";"`, ghi với `encoding="utf-8"` + `newline=""` (dấu `,` là mặc định).

### Bài 20: Hệ thống quản lý điểm (Mini Project)

* **Đề bài:** Xây dựng chương trình quản lý điểm một lớp học:
  1. Tạo danh sách 5 học viên (tên, lớp, điểm 3 môn Toán – Văn – Anh).
  2. Ghi file `bang_diem_day_du.csv` gồm cột `ten,lop,toan,van,anh,tong,tb,xep_loai`.
  3. Đọc lại file, xếp hạng học viên theo điểm TB từ cao xuống thấp, in bảng xếp hạng kèm hạng `1, 2, 3...`.
* **Input:** Danh sách học viên tự chọn (5 bạn).
* **Output:** File CSV đầy đủ + bảng xếp hạng in ra màn hình.
* **Gợi ý:** Sắp xếp bằng `sorted(danh_sach, key=lambda hs: float(hs["tb"]), reverse=True)`; dùng `enumerate` để gán thứ hạng.

---

## 🎯 Tổng kết

Chúc mừng bạn đã hoàn thành 20 bài tập về CSV! Bạn đã luyện:

* ✅ Đọc/ghi CSV cơ bản (`reader`, `writer`) và theo tên cột (`DictReader`, `DictWriter`).
* ✅ Xử lý dấu phân cách `;`, mã hóa tiếng Việt `utf-8-sig`, `cp1258`.
* ✅ Các tình huống thực tế: bảng điểm, danh sách học viên, xếp loại, xếp hạng, gộp và chuyển đổi file.


Tiếp theo, bạn sẽ ra ngoài "thế giới mạng" — học về **API** để lấy dữ liệu từ các dịch vụ trực tuyến:

---

## ✅ Đáp án

> 💡 **Hãy tự làm bài tập trước** rồi mới mở đáp án.

## 🟢 Dễ (Bài 1 – 7)


<details>
<summary>✅ Bài 1: Ghi danh sách môn học</summary>


**Phân tích:** Cần ghi các dòng dữ liệu vào file; không cần dòng tiêu đề. Mỗi dòng là một list hai phần tử (mã môn, tên môn).

**Ý tưởng:** Dùng `csv.writer` + vòng lặp ghi từng dòng bằng `writerow()`.

**Thuật toán:**
1. Tạo danh sách các môn học (mỗi môn là một list).
2. Mở file ở chế độ ghi `"w"` với `encoding="utf-8"` và `newline=""`.
3. Ghi từng dòng bằng `writerow()`.

**Code:**

```python
import csv

# Danh sách môn học: mỗi dòng là [mã môn, tên môn]
mon_hoc = [
    ["TOAN", "Toán"],
    ["VAN", "Ngữ văn"],
    ["TIN", "Tin học"],
]

# Mở file để ghi: newline="" tránh dòng trống trên Windows
with open("mon_hoc.csv", "w", encoding="utf-8", newline="") as f:
    ghi = csv.writer(f)          # tạo đối tượng ghi CSV
    for dong in mon_hoc:         # duyệt từng môn học
        ghi.writerow(dong)       # ghi một dòng ra file
```

**Giải thích code:**
* `csv.writer(f)` — tạo "cây bút" ghi CSV vào file `f`.
* `ghi.writerow(dong)` — ghi một list thành một dòng, các phần tử tự động ngăn cách bởi dấu phẩy.
* `newline=""` — bắt buộc khi ghi CSV trên Windows, tránh dòng trống thừa.

**Độ phức tạp:** O(n) với n là số môn học.

---

</details>

<details>
<summary>✅ Bài 2: Đọc file và in từng dòng</summary>


**Phân tích:** Đọc file vừa tạo và in từng dòng dưới dạng list — đây chính là hành vi mặc định của `csv.reader`.

**Ý tưởng:** Mở file ở chế độ đọc, duyệt `csv.reader` bằng vòng `for`.

**Thuật toán:**
1. Tạo file mẫu `mon_hoc.csv` (gọi lại cách bài 1).
2. Mở file đọc với `encoding="utf-8"`.
3. In từng dòng.

**Code:**

```python
import csv

# Tạo file mẫu (như bài 1)
mon_hoc = [
    ["TOAN", "Toán"],
    ["VAN", "Ngữ văn"],
    ["TIN", "Tin học"],
]
with open("mon_hoc.csv", "w", encoding="utf-8", newline="") as f:
    csv.writer(f).writerows(mon_hoc)   # writerows: ghi cả list list một lúc

# Đọc lại và in từng dòng
with open("mon_hoc.csv", "r", encoding="utf-8") as f:
    doc = csv.reader(f)        # tạo đối tượng đọc
    for dong in doc:           # mỗi dòng là một list
        print(dong)
```

**Giải thích code:**
* `csv.writer(f).writerows(mon_hoc)` — rút gọn: ghi tất cả dòng trong một lệnh.
* `for dong in doc` — `csv.reader` trả về iterator, `for` duyệt lần lượt từng dòng.
* Kết quả in ra: `['TOAN', 'Toán']`, `['VAN', 'Ngữ văn']`, `['TIN', 'Tin học']`.

**Độ phức tạp:** O(n) với n là số dòng.

---

</details>

<details>
<summary>✅ Bài 3: Ghi danh sách học viên</summary>


**Phân tích:** Khác bài 1 — phải có **dòng tiêu đề** `ten,lop` trước dữ liệu.

**Ý tưởng:** Ghi dòng tiêu đề trước, sau đó ghi từng dòng học viên.

**Thuật toán:**
1. Ghi dòng tiêu đề `["ten", "lop"]`.
2. Ghi lần lượt 3 học viên.
3. Đọc lại để kiểm tra.

**Code:**

```python
import csv

# Dữ liệu học viên: dòng đầu là tiêu đề
hoc_vien = [
    ["ten", "lop"],
    ["An", "10A1"],
    ["Binh", "10A2"],
    ["Chi", "10A1"],
]

with open("hoc_vien.csv", "w", encoding="utf-8", newline="") as f:
    ghi = csv.writer(f)
    ghi.writerows(hoc_vien)    # ghi tiêu đề + dữ liệu trong một lệnh

# Kiểm tra bằng cách đọc lại
with open("hoc_vien.csv", "r", encoding="utf-8") as f:
    for dong in csv.reader(f):
        print(dong)
```

**Giải thích code:**
* Dòng `["ten", "lop"]` nằm đầu danh sách nên được ghi trước — thành dòng tiêu đề.
* `writerows(hoc_vien)` — ghi toàn bộ danh sách dòng cùng lúc (nhanh hơn vòng lặp).
* Đọc lại để xác nhận file đúng như mong muốn — thói quen nên có khi làm việc với file.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 4: In tên và điểm bằng DictReader</summary>


**Phân tích:** `csv.DictReader` lấy dòng đầu làm khóa, mỗi dòng sau trở thành dict — truy cập bằng tên cột rất trực quan.

**Ý tưởng:** Tạo file mẫu, đọc bằng `DictReader`, in `dong["ten"]` và `dong["diem"]`.

**Thuật toán:**
1. Tạo file `bang_diem.csv` mẫu.
2. Đọc bằng `csv.DictReader`.
3. In từng dòng dạng `ten - diem`.

**Code:**

```python
import csv

# Tạo file mẫu
with open("bang_diem.csv", "w", encoding="utf-8", newline="") as f:
    ghi = csv.writer(f)
    ghi.writerows([
        ["ten", "diem"],
        ["An", 8],
        ["Binh", 7],
        ["Chi", 9],
    ])

# Đọc bằng DictReader: dòng tiêu đề trở thành khóa
with open("bang_diem.csv", "r", encoding="utf-8") as f:
    doc = csv.DictReader(f)
    for dong in doc:
        print(f"{dong['ten']} - {dong['diem']}")
```

**Giải thích code:**
* `csv.DictReader(f)` — tự nhận dòng đầu là tiêu đề, mỗi dòng sau là dict `{"ten": "An", "diem": "8"}`.
* `dong["ten"]` — lấy giá trị theo tên cột, không cần nhớ vị trí.
* Lưu ý: `dong["diem"]` là chuỗi `"8"` — mọi giá trị CSV đều là văn bản.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 5: Xuất bảng điểm bằng DictWriter</summary>


**Phân tích:** Ghi dữ liệu dạng dict, cần khai báo thứ tự cột qua `fieldnames` để file đúng thứ tự.

**Ý tưởng:** `csv.DictWriter` + `writeheader()` tự sinh dòng tiêu đề.

**Thuật toán:**
1. Khai báo `cot = ["ten", "lop", "diem"]`.
2. Tạo `csv.DictWriter(f, fieldnames=cot)`.
3. Ghi tiêu đề rồi từng dòng dữ liệu.

**Code:**

```python
import csv

# Dữ liệu dạng từ điển
hoc_vien = [
    {"ten": "An", "lop": "10A1", "diem": 8},
    {"ten": "Binh", "lop": "10A2", "diem": 7},
]

cot = ["ten", "lop", "diem"]

with open("bang_diem_moi.csv", "w", encoding="utf-8", newline="") as f:
    ghi = csv.DictWriter(f, fieldnames=cot)
    ghi.writeheader()          # tự ghi dòng tiêu đề: ten,lop,diem
    for hs in hoc_vien:
        ghi.writerow(hs)       # ghi từng dict thành một dòng

# Đọc lại kiểm tra
with open("bang_diem_moi.csv", "r", encoding="utf-8") as f:
    for dong in csv.reader(f):
        print(dong)
```

**Giải thích code:**
* `fieldnames=cot` — quy định thứ tự cột; DictWriter dùng nó để biết lấy gì từ dict.
* `writeheader()` — ghi dòng tiêu đề tự động từ `fieldnames`.
* `writerow(hs)` — giá trị lấy theo khóa; nếu dict thiếu khóa, file có ô trống.
* DictWriter giúp code dễ đọc hơn Writer và ít sai khi số cột nhiều.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 6: Đọc file dấu chấm phẩy</summary>


**Phân tích:** File dùng `;` thay vì `,` — chỉ cần báo cho `csv` biết qua tham số `delimiter`.

**Ý tưởng:** Mở file, `csv.reader(f, delimiter=";")`, duyệt và in.

**Thuật toán:**
1. Tạo file `du_lieu_vn.csv` dấu `;`.
2. Đọc với `delimiter=";"`.
3. In từng dòng.

**Code:**

```python
import csv

# Tạo file mẫu dùng dấu chấm phẩy (Excel tiếng Việt hay xuất kiểu này)
with open("du_lieu_vn.csv", "w", encoding="utf-8", newline="") as f:
    f.write("ten;lop\nAn;10A1\nBinh;10A2\n")

# Đọc với đúng dấu phân cách
with open("du_lieu_vn.csv", "r", encoding="utf-8") as f:
    doc = csv.reader(f, delimiter=";")   # khai báo dấu phân cách
    for dong in doc:
        print(dong)
```

**Giải thích code:**
* `f.write(...)` — ghi chuỗi thô trực tiếp vào file (đơn giản khi tạo file mẫu).
* `delimiter=";"` — báo cho `csv.reader` rằng các cột ngăn cách bằng dấu `;`.
* Cùng kỹ thuật với `delimiter="\t"` cho file tab.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 7: Đếm số học viên</summary>


**Phân tích:** `csv.reader` đọc cả dòng tiêu đề — phải "nhảy qua" nó bằng `next()` rồi mới đếm.

**Ý tưởng:** `next(doc)` lấy dòng tiêu đề, vòng `for` đếm số dòng còn lại.

**Thuật toán:**
1. Tạo file `hoc_vien.csv` mẫu.
2. Gọi `next(doc)` bỏ qua dòng tiêu đề.
3. Đếm các dòng còn lại.

**Code:**

```python
import csv

# Tạo file mẫu
with open("hoc_vien.csv", "w", encoding="utf-8", newline="") as f:
    ghi = csv.writer(f)
    ghi.writerows([
        ["ten", "lop"],
        ["An", "10A1"],
        ["Binh", "10A2"],
        ["Chi", "10A1"],
    ])

dem = 0
with open("hoc_vien.csv", "r", encoding="utf-8") as f:
    doc = csv.reader(f)
    next(doc)              # bỏ qua dòng tiêu đề (dòng đầu tiên)
    for dong in doc:
        dem += 1           # mỗi dòng còn lại là một học viên

print("So hoc vien:", dem)
```

**Giải thích code:**
* `next(doc)` — lấy (và bỏ qua) dòng tiếp theo của iterator, ở đây là tiêu đề.
* `dem += 1` — tăng biến đếm mỗi khi có một dòng dữ liệu.
* Vòng `for` sau `next()` chỉ còn duyệt các dòng dữ liệu thật sự.

**Độ phức tạp:** O(n).

---

</details>

## 🟡 Trung bình (Bài 8 – 14)


<details>
<summary>✅ Bài 8: Tính điểm trung bình từng học viên</summary>


**Phân tích:** Mỗi dòng có điểm 2 môn dạng chuỗi — cần `float()` rồi mới tính `(van + toan) / 2`.

**Ý tưởng:** Duyệt `DictReader`, ép kiểu, tính trung bình, in kết quả.

**Thuật toán:**
1. Tạo file `bang_diem.csv` (ten, van, toan).
2. Với mỗi dòng: ép `van`, `toan` sang float, tính trung bình.
3. In kết quả.

**Code:**

```python
import csv

# Tạo file mẫu
with open("bang_diem.csv", "w", encoding="utf-8", newline="") as f:
    ghi = csv.writer(f)
    ghi.writerows([
        ["ten", "van", "toan"],
        ["An", 8, 9],
        ["Binh", 7, 6],
        ["Chi", 9, 10],
    ])

with open("bang_diem.csv", "r", encoding="utf-8") as f:
    doc = csv.DictReader(f)
    for dong in doc:
        van = float(dong["van"])    # ép kiểu: CSV trả về chuỗi
        toan = float(dong["toan"])
        tb = (van + toan) / 2       # trung bình 2 môn
        print(f"{dong['ten']}: {tb}")
```

**Giải thích code:**
* `float(dong["van"])` — bắt buộc vì `dong["van"]` là chuỗi `"8"`; cộng chuỗi sẽ ra `"89"` chứ không phải 17.
* `f"{dong['ten']}: {tb}"` — f-string chèn giá trị vào chuỗi.
* Kết quả: `An: 8.5`, `Binh: 6.5`, `Chi: 9.5`.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 9: Lọc học viên điểm cao</summary>


**Phân tích:** Lọc theo điều kiện — duyệt toàn bộ, giữ lại dòng thỏa mãn.

**Ý tưởng:** Điều kiện `float(dong["diem"]) >= 8`, in tên nếu đúng.

**Thuật toán:**
1. Tạo file mẫu có 4 học viên.
2. Với mỗi dòng, kiểm tra điểm >= 8.
3. In tên học viên đạt.

**Code:**

```python
import csv

# Tạo file mẫu
with open("bang_diem.csv", "w", encoding="utf-8", newline="") as f:
    ghi = csv.writer(f)
    ghi.writerows([
        ["ten", "diem"],
        ["An", 8],
        ["Binh", 7],
        ["Chi", 9],
        ["Duong", 6],
    ])

with open("bang_diem.csv", "r", encoding="utf-8") as f:
    doc = csv.DictReader(f)
    for dong in doc:
        if float(dong["diem"]) >= 8:     # lọc điểm từ 8 trở lên
            print(dong["ten"])
```

**Giải thích code:**
* `if float(dong["diem"]) >= 8` — so sánh số; nếu quên ép kiểu sẽ so chuỗi sai thứ tự.
* Chỉ in `dong["ten"]` khi điều kiện đúng — đây chính là kỹ thuật lọc dữ liệu.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 10: Tìm học viên điểm cao nhất</summary>


**Phân tích:** Bài toán tìm max — duyệt qua, nhớ lại dòng có điểm lớn nhất từng gặp.

**Ý tưởng:** Hai biến `ten_max`, `diem_max`; khởi tạo rỗng, cập nhật khi gặp điểm lớn hơn.

**Thuật toán:**
1. Khởi tạo `diem_max = -1`.
2. Duyệt từng dòng: nếu điểm > `diem_max`, cập nhật cả tên và điểm.
3. In kết quả sau vòng lặp.

**Code:**

```python
import csv

# Tạo file mẫu
with open("bang_diem.csv", "w", encoding="utf-8", newline="") as f:
    ghi = csv.writer(f)
    ghi.writerows([
        ["ten", "diem"],
        ["An", 8],
        ["Binh", 7],
        ["Chi", 9],
    ])

ten_max = ""
diem_max = -1       # điểm thấp nhất có thể là 0 nên khởi tạo -1

with open("bang_diem.csv", "r", encoding="utf-8") as f:
    doc = csv.DictReader(f)
    for dong in doc:
        diem = float(dong["diem"])
        if diem > diem_max:
            diem_max = diem       # lưu lại kỷ lục mới
            ten_max = dong["ten"]

print(f"{ten_max} dat diem cao nhat: {diem_max}")
```

**Giải thích code:**
* `diem_max = -1` — đảm bảo học viên đầu tiên luôn "phá kỷ lục".
* Trong vòng lặp, mỗi điểm cao hơn sẽ thay thế kỷ lục cũ.
* Sau vòng lặp, biến chứa kết quả cuối cùng — in một lần duy nhất.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 11: Xuất CSV thêm cột tổng và trung bình</summary>


**Phân tích:** Quy trình hai bước: đọc → biến đổi (thêm khóa) → ghi lại với `fieldnames` mở rộng.

**Ý tưởng:** Đọc hết vào list dict, tính `tong` và `tb`, ghi bằng `DictWriter`.

**Thuật toán:**
1. Đọc file vào `danh_sach` (list dict).
2. Với mỗi học viên: tính `tong`, `tb`, thêm vào dict.
3. Ghi file mới với 5 cột.

**Code:**

```python
import csv

# Tạo file mẫu
with open("bang_diem.csv", "w", encoding="utf-8", newline="") as f:
    ghi = csv.writer(f)
    ghi.writerows([
        ["ten", "van", "toan"],
        ["An", 8, 9],
        ["Binh", 7, 6],
    ])

# Bước 1: đọc vào list dict
with open("bang_diem.csv", "r", encoding="utf-8") as f:
    doc = csv.DictReader(f)
    danh_sach = list(doc)      # chuyển iterator thành list để dùng lại

# Bước 2: thêm cột tính toán
for hs in danh_sach:
    van = float(hs["van"])
    toan = float(hs["toan"])
    hs["tong"] = van + toan
    hs["tb"] = (van + toan) / 2

# Bước 3: ghi file mới
cot = ["ten", "van", "toan", "tong", "tb"]
with open("bang_diem_tong.csv", "w", encoding="utf-8", newline="") as f:
    ghi = csv.DictWriter(f, fieldnames=cot)
    ghi.writeheader()
    ghi.writerows(danh_sach)

# Kiểm tra
with open("bang_diem_tong.csv", "r", encoding="utf-8") as f:
    for dong in csv.reader(f):
        print(dong)
```

**Giải thích code:**
* `list(doc)` — DictReader là iterator dùng một lần; chuyển list để duyệt nhiều vòng.
* `hs["tong"] = ...` — thêm khóa mới vào dict, DictWriter ghi đúng tên cột.
* `fieldnames` mở rộng 5 cột — khớp với các khóa mới thêm.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 12: Xếp loại học lực</summary>


**Phân tích:** Phân nhóm theo khoảng điểm bằng `if/elif/else`, thêm cột `loai`, ghi ra file.

**Ý tưởng:** Đọc file bài 11 (hoặc tạo mới), thêm khóa `loai` theo điểm TB.

**Thuật toán:**
1. Tạo file `bang_diem_tong.csv` mẫu (ten, van, toan, tong, tb).
2. Với mỗi học viên, xét `tb` để gán loại.
3. Ghi `xep_loai.csv` với 6 cột.

**Code:**

```python
import csv

# Tạo file mẫu giống kết quả bài 11
with open("bang_diem_tong.csv", "w", encoding="utf-8", newline="") as f:
    ghi = csv.writer(f)
    ghi.writerows([
        ["ten", "van", "toan", "tong", "tb"],
        ["An", 8, 9, 17, 8.5],
        ["Binh", 7, 6, 13, 6.5],
        ["Chi", 5, 6, 11, 5.5],
    ])

with open("bang_diem_tong.csv", "r", encoding="utf-8") as f:
    doc = csv.DictReader(f)
    danh_sach = list(doc)

for hs in danh_sach:
    tb = float(hs["tb"])
    if tb >= 8:
        hs["loai"] = "Gioi"
    elif tb >= 6.5:
        hs["loai"] = "Kha"
    else:
        hs["loai"] = "TB"

cot = ["ten", "van", "toan", "tong", "tb", "loai"]
with open("xep_loai.csv", "w", encoding="utf-8", newline="") as f:
    ghi = csv.DictWriter(f, fieldnames=cot)
    ghi.writeheader()
    ghi.writerows(danh_sach)

# In ra màn hình để kiểm tra
with open("xep_loai.csv", "r", encoding="utf-8") as f:
    for dong in csv.DictReader(f):
        print(dong["ten"], "-", dong["loai"])
```

**Giải thích code:**
* `if/elif/else` — kiểm tra theo thứ tự từ cao xuống thấp, kết quả đúng với mọi mức.
* Khóa `loai` thêm vào dict ghi ra file — DictWriter chỉ cần khóa nằm trong `fieldnames`.
* Kết quả: `An - Gioi`, `Binh - Kha`, `Chi - TB`.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 13: Chuyển JSON sang CSV</summary>


**Phân tích:** JSON (bài 32) và CSV "hợp tác" qua list dict — `json.loads` cho list dict, `csv.DictWriter` ghi list dict.

**Ý tưởng:** Parse chuỗi JSON → list dict → ghi CSV.

**Thuật toán:**
1. Khai báo chuỗi JSON dạng list dict.
2. `json.loads()` chuyển thành list dict.
3. Ghi bằng `DictWriter` với `fieldnames` theo thứ tự cột mong muốn.

**Code:**

```python
import csv
import json

# Dữ liệu JSON dạng chuỗi (thường nhận từ file hoặc API)
chuoi_json = '[{"ten": "Vo", "gia": 5000, "so_luong": 10}, {"ten": "But", "gia": 3000, "so_luong": 15}]'

san_pham = json.loads(chuoi_json)   # chuỗi JSON -> list dict

cot = ["ten", "gia", "so_luong"]
with open("san_pham.csv", "w", encoding="utf-8", newline="") as f:
    ghi = csv.DictWriter(f, fieldnames=cot)
    ghi.writeheader()
    ghi.writerows(san_pham)

# Kiểm tra
with open("san_pham.csv", "r", encoding="utf-8") as f:
    for dong in csv.reader(f):
        print(dong)
```

**Giải thích code:**
* `json.loads(chuoi_json)` — trả về list chứa 2 dict (kiến thức bài 32).
* `ghi.writerows(san_pham)` — ghi cả list dict một lúc.
* Kết quả file: tiêu đề `ten,gia,so_luong` + 2 dòng dữ liệu.
* Đây là kỹ năng quan trọng: nhận JSON từ API, lưu CSV cho Excel (sẽ dùng ở bài 34–35).

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 14: Cộng điểm hai file CSV</summary>


**Phân tích:** Ghép dữ liệu theo khóa (tên) — đọc mỗi file thành dict `{ten: diem}` rồi nối.

**Ý tưởng:** Dict thứ nhất chứa điểm văn, dict thứ hai chứa điểm toán; duyệt theo tên, tính TB, ghi file mới.

**Thuật toán:**
1. Đọc `diem_van.csv` → dict `{ten: diem}`.
2. Đọc `diem_toan.csv` → dict `{ten: diem}`.
3. Với mỗi tên: van + toan → tb, ghi `diem_tong.csv`.

**Code:**

```python
import csv

# Tạo 2 file mẫu (thứ tự tên khác nhau để thử ghép)
with open("diem_van.csv", "w", encoding="utf-8", newline="") as f:
    ghi = csv.writer(f)
    ghi.writerows([["ten", "diem"], ["An", 8], ["Binh", 7], ["Chi", 9]])

with open("diem_toan.csv", "w", encoding="utf-8", newline="") as f:
    ghi = csv.writer(f)
    ghi.writerows([["ten", "diem"], ["Chi", 10], ["An", 9], ["Binh", 6]])

# Hàm đọc file CSV thành dict {ten: diem}
def doc_diem(ten_file):
    ket_qua = {}
    with open(ten_file, "r", encoding="utf-8") as f:
        doc = csv.DictReader(f)
        for dong in doc:
            ket_qua[dong["ten"]] = float(dong["diem"])   # ten -> diem
    return ket_qua

van = doc_diem("diem_van.csv")
toan = doc_diem("diem_toan.csv")

with open("diem_tong.csv", "w", encoding="utf-8", newline="") as f:
    ghi = csv.writer(f)
    ghi.writerow(["ten", "van", "toan", "tb"])           # dòng tiêu đề
    for ten in van:                                      # duyệt theo tên file văn
        tb = (van[ten] + toan[ten]) / 2
        ghi.writerow([ten, van[ten], toan[ten], tb])

# Kiểm tra
with open("diem_tong.csv", "r", encoding="utf-8") as f:
    for dong in csv.reader(f):
        print(dong)
```

**Giải thích code:**
* Hàm `doc_diem` — tái sử dụng cho cả hai file, trả dict `{tên: điểm}`.
* `van[ten]` và `toan[ten]` — lấy điểm theo tên; thứ tự dòng khác nhau không còn quan trọng.
* Kết quả file: `ten,van,toan,tb` với đủ 3 học viên.

**Độ phức tạp:** O(n) với n là số học viên.

---

</details>

## 🔴 Khó (Bài 15 – 20)


<details>
<summary>✅ Bài 15: Thống kê theo lớp</summary>


**Phân tích:** Nhóm dữ liệu theo lớp — dùng dict với khóa là tên lớp, giá trị là [tổng điểm, số lượng].

**Ý tưởng:** Cập nhật dict theo từng dòng, sau vòng lặp chia tổng cho số lượng.

**Thuật toán:**
1. Khởi tạo `thong_ke = {}`.
2. Với mỗi dòng: cập nhật tổng điểm và số lượng cho lớp tương ứng.
3. In kết quả từng lớp, làm tròn 2 chữ số.

**Code:**

```python
import csv

# Tạo file mẫu
with open("hoc_sinh.csv", "w", encoding="utf-8", newline="") as f:
    ghi = csv.writer(f)
    ghi.writerows([
        ["ten", "lop", "diem"],
        ["An", "10A1", 8],
        ["Binh", "10A2", 7],
        ["Chi", "10A1", 9],
        ["Dung", "10A2", 5],
        ["Em", "10A1", 6],
    ])

# thong_ke[lop] = [tong_diem, so_luong]
thong_ke = {}

with open("hoc_sinh.csv", "r", encoding="utf-8") as f:
    doc = csv.DictReader(f)
    for dong in doc:
        lop = dong["lop"]
        diem = float(dong["diem"])
        if lop not in thong_ke:
            thong_ke[lop] = [0, 0]       # lớp mới: tổng = 0, số lượng = 0
        thong_ke[lop][0] += diem         # cộng dồn tổng điểm
        thong_ke[lop][1] += 1            # tăng số lượng

for lop, (tong, so_luong) in thong_ke.items():
    tb = round(tong / so_luong, 2)       # làm tròn 2 chữ số thập phân
    print(f"{lop}: {so_luong} hoc vien, diem TB {tb}")
```

**Giải thích code:**
* `if lop not in thong_ke` — khởi tạo lớp lần đầu gặp; tránh lỗi khi truy cập khóa chưa tồn tại.
* `for lop, (tong, so_luong) in thong_ke.items()` — giải nén list hai phần tử.
* `round(x, 2)` — làm tròn để hiển thị gọn (7.666... → 7.67).

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 16: Gộp nhiều file CSV</summary>


**Phân tích:** Gộp dữ liệu nhiều file cùng cấu trúc — ghi tiêu đề một lần, mỗi file nguồn bỏ qua tiêu đề riêng của nó.

**Ý tưởng:** Dùng `next(doc)` để bỏ dòng tiêu đề từng file nguồn, ghi các dòng còn lại vào file đích.

**Thuật toán:**
1. Tạo 3 file nguồn mẫu.
2. Mở file đích `"w"`, ghi tiêu đề.
3. Với mỗi file nguồn: bỏ tiêu đề, ghi các dòng dữ liệu vào đích.

**Code:**

```python
import csv

# Tạo 3 file nguồn mẫu
with open("lop_a.csv", "w", encoding="utf-8", newline="") as f:
    f.write("ten,diem\nAn,8\nBinh,7\n")
with open("lop_b.csv", "w", encoding="utf-8", newline="") as f:
    f.write("ten,diem\nChi,9\nDung,6\n")
with open("lop_c.csv", "w", encoding="utf-8", newline="") as f:
    f.write("ten,diem\nEm,8\n")

danh_sach_file = ["lop_a.csv", "lop_b.csv", "lop_c.csv"]

with open("tat_ca.csv", "w", encoding="utf-8", newline="") as f_dich:
    ghi = csv.writer(f_dich)
    ghi.writerow(["ten", "diem"])            # ghi tiêu đề một lần duy nhất

    for ten_file in danh_sach_file:
        with open(ten_file, "r", encoding="utf-8") as f_nguon:
            doc = csv.reader(f_nguon)
            next(doc)                        # bỏ tiêu đề của file nguồn
            for dong in doc:
                ghi.writerow(dong)           # ghi dữ liệu vào file đích

# Kiểm tra
with open("tat_ca.csv", "r", encoding="utf-8") as f:
    for dong in csv.reader(f):
        print(dong)
```

**Giải thích code:**
* Vòng `for ten_file` mở lần lượt từng file nguồn — không cần viết code lặp lại.
* `next(doc)` — bỏ dòng tiêu đề từng file nguồn, tránh ghi "ten,diem" ba lần.
* File đích mở một lần ở ngoài — tất cả dữ liệu đổ vào một file duy nhất.

**Độ phức tạp:** O(n) với n là tổng số dòng.

---

</details>

<details>
<summary>✅ Bài 17: Cập nhật điểm trong CSV</summary>


**Phân tích:** Sửa dữ liệu rồi ghi đè — không thể sửa trực tiếp giữa file; đọc hết, sửa trong bộ nhớ, ghi lại toàn bộ.

**Ý tưởng:** Đọc vào list, dùng `min(diem + 1, 10)` để không vượt 10, ghi lại file cũ.

**Thuật toán:**
1. Đọc file vào list dict.
2. Học viên điểm < 7: tăng 1 điểm nhưng tối đa 10.
3. Ghi đè file với `newline=""`.

**Code:**

```python
import csv

# Tạo file mẫu
with open("bang_diem.csv", "w", encoding="utf-8", newline="") as f:
    ghi = csv.writer(f)
    ghi.writerows([
        ["ten", "diem"],
        ["An", 8],
        ["Binh", 6],
        ["Chi", 9],
        ["Duong", 5],
    ])

# Bước 1: đọc hết vào list
with open("bang_diem.csv", "r", encoding="utf-8") as f:
    doc = csv.DictReader(f)
    danh_sach = list(doc)

# Bước 2: cập nhật điểm
for hs in danh_sach:
    diem = float(hs["diem"])
    if diem < 7:
        hs["diem"] = min(diem + 1, 10)     # +1 điểm, không quá 10

# Bước 3: ghi đè lại chính file đó
cot = ["ten", "diem"]
with open("bang_diem.csv", "w", encoding="utf-8", newline="") as f:
    ghi = csv.DictWriter(f, fieldnames=cot)
    ghi.writeheader()
    ghi.writerows(danh_sach)

# Kiểm tra kết quả trong file
with open("bang_diem.csv", "r", encoding="utf-8") as f:
    for dong in csv.DictReader(f):
        print(dong)
```

**Giải thích code:**
* `min(diem + 1, 10)` — phép cộng nhưng bị "kẹp" ở mức tối đa 10 điểm.
* Ghi đè file: mở chế độ `"w"` sẽ xóa nội dung cũ và viết lại — kỹ thuật chuẩn để cập nhật CSV.
* Kiểm tra: Binh 6→7, Duong 5→6; An, Chi giữ nguyên.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 18: Kiểm tra file CSV hợp lệ</summary>


**Phân tích:** Mỗi dòng phải có đúng số cột; dùng `len(dong)` để đếm cột của từng dòng.

**Ý tưởng:** Duyệt các dòng, so `len(dong)` với số cột chuẩn (3), in thông báo kèm số thứ tự dòng.

**Thuật toán:**
1. Tạo file mẫu có một dòng lỗi (2 cột).
2. Đếm số thứ tự dòng bằng biến `so_dong`.
3. Với mỗi dòng: kiểm tra số cột và in kết quả.

**Code:**

```python
import csv

# Tạo file mẫu: dòng 3 (Binh) chỉ có 2 cột — dòng lỗi
with open("du_lieu.txt", "w", encoding="utf-8", newline="") as f:
    f.write("ten,lop,diem\nAn,10A1,8\nBinh,10A2\nChi,10A1,9\nDung,10A2,7\n")

so_cot_chuan = 3

with open("du_lieu.txt", "r", encoding="utf-8") as f:
    doc = csv.reader(f)
    so_dong = 0
    for dong in doc:
        so_dong += 1
        if so_dong == 1:
            trang_thai = "tieu de"
        else:
            trang_thai = "du lieu"
        if len(dong) == so_cot_chuan:
            print(f"Dong {so_dong} ({trang_thai}): {len(dong)} cot - OK")
        else:
            print(f"Dong {so_dong} ({trang_thai}): {len(dong)} cot - LOI")
```

**Giải thích code:**
* `so_dong += 1` — đếm số thứ tự dòng; dòng 1 là tiêu đề.
* `len(dong)` — số cột của dòng hiện tại, so với `so_cot_chuan` (3).
* Phát hiện dòng lỗi trước khi dữ liệu gây hỏng chương trình xử lý — kiểm tra dữ liệu là bước quan trọng khi nhận file từ người khác.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 19: Chuyển đổi mã hóa và dấu phân cách</summary>


**Phân tích:** File từ Excel tiếng Việt: mã hóa `utf-8-sig`, dấu `;`. Cần đọc đúng rồi ghi chuẩn hóa `utf-8` + dấu `,`.

**Ý tưởng:** Đọc với `encoding="utf-8-sig"` + `delimiter=";"`, ghi với `encoding="utf-8"` (dấu phẩy là mặc định).

**Thuật toán:**
1. Tạo file `excel_vn.csv` mẫu (tiêu đề tiếng Việt, dấu `;`).
2. Đọc với `encoding="utf-8-sig"` và `delimiter=";"`.
3. Ghi file `chuan.csv` với `encoding="utf-8"`, `newline=""`.

**Code:**

```python
import csv

# Tạo file mẫu giống file Excel tiếng Việt xuất ra
with open("excel_vn.csv", "w", encoding="utf-8-sig", newline="") as f:
    f.write("ho_ten;lop;diem\nNguyễn Văn An;10A1;8\nTrần Thị Bình;10A2;7\n")

# Bước 1: đọc đúng kiểu file Excel VN
with open("excel_vn.csv", "r", encoding="utf-8-sig") as f:
    doc = csv.reader(f, delimiter=";")     # dấu phân cách là ;
    danh_sach = [dong for dong in doc]     # đọc hết vào list

# Bước 2: ghi chuẩn hóa (dấu , mặc định, mã hóa utf-8)
with open("chuan.csv", "w", encoding="utf-8", newline="") as f:
    ghi = csv.writer(f)
    ghi.writerows(danh_sach)

# Kiểm tra
with open("chuan.csv", "r", encoding="utf-8") as f:
    for dong in csv.reader(f):
        print(dong)
```

**Giải thích code:**
* `encoding="utf-8-sig"` — có BOM, Excel VN mở file đúng dấu tiếng Việt; `utf-8` thường đọc cũng được nhưng có thể dính ký tự lạ đầu file.
* `delimiter=";"` — đọc đúng các cột đang ngăn cách bằng `;`.
* Ghi ra file mới với `utf-8` chuẩn — mở bằng Excel không loạn dấu.

**Độ phức tạp:** O(n).

---

</details>

<details>
<summary>✅ Bài 20: Hệ thống quản lý điểm (Mini Project)</summary>


**Phân tích:** Bài tổng hợp đầy đủ quy trình: ghi CSV nhiều cột → đọc lại → tính toán → sắp xếp → in báo cáo.

**Ý tưởng:** Tạo dữ liệu 5 học viên, ghi file qua DictWriter, đọc lại, tính `tong`/`tb`/`xep_loai`, sắp xếp giảm dần theo `tb` và in thứ hạng.

**Thuật toán:**
1. Tạo danh sách 5 học viên (dict: ten, lop, toan, van, anh).
2. Ghi `bang_diem_day_du.csv` (8 cột).
3. Đọc lại, tính tong, tb, xếp loại.
4. Sắp xếp theo tb giảm dần, in bảng xếp hạng.

**Code:**

```python
import csv

# Bước 1: dữ liệu 5 học viên
hoc_vien = [
    {"ten": "An", "lop": "10A1", "toan": 8, "van": 7, "anh": 6},
    {"ten": "Binh", "lop": "10A2", "toan": 9, "van": 8, "anh": 10},
    {"ten": "Chi", "lop": "10A1", "toan": 7, "van": 9, "anh": 8},
    {"ten": "Dung", "lop": "10A2", "toan": 5, "van": 6, "anh": 5},
    {"ten": "Em", "lop": "10A1", "toan": 10, "van": 9, "anh": 9},
]

# Bước 2: tính toán + ghi file
cot = ["ten", "lop", "toan", "van", "anh", "tong", "tb", "xep_loai"]
with open("bang_diem_day_du.csv", "w", encoding="utf-8", newline="") as f:
    ghi = csv.DictWriter(f, fieldnames=cot)
    ghi.writeheader()
    for hs in hoc_vien:
        tong = hs["toan"] + hs["van"] + hs["anh"]
        tb = tong / 3
        if tb >= 8:
            loai = "Gioi"
        elif tb >= 6.5:
            loai = "Kha"
        else:
            loai = "TB"
        # Ghi dict đầy đủ các cột
        ghi.writerow({
            "ten": hs["ten"], "lop": hs["lop"],
            "toan": hs["toan"], "van": hs["van"], "anh": hs["anh"],
            "tong": tong, "tb": tb, "xep_loai": loai,
        })

# Bước 3: đọc lại và sắp xếp
with open("bang_diem_day_du.csv", "r", encoding="utf-8") as f:
    doc = csv.DictReader(f)
    danh_sach = list(doc)

danh_sach.sort(key=lambda hs: float(hs["tb"]), reverse=True)  # tb cao lên đầu

# Bước 4: in bảng xếp hạng
print(f"{'Hang':<6}{'Ten':<8}{'Lop':<8}{'Tong':<8}{'TB':<8}{'Loai'}")
for thu_hang, hs in enumerate(danh_sach, start=1):
    print(f"{thu_hang:<6}{hs['ten']:<8}{hs['lop']:<8}"
          f"{hs['tong']:<8}{float(hs['tb']):<8.2f}{hs['xep_loai']}")
```

**Giải thích code:**
* `ghi.writerow({...})` — tạo dict mới đủ 8 khóa khớp `fieldnames`; không thể thêm khóa vào dict cũ khi đã duyệt theo khóa gốc 5 mục.
* `sort(key=lambda hs: float(hs["tb"]), reverse=True)` — sắp giảm dần theo TB (lambda đã học bài 25).
* `enumerate(danh_sach, start=1)` — gán thứ hạng 1, 2, 3...
* `f"{thu_hang:<6}"` — canh trái 6 ký tự cho cột thẳng hàng đẹp.

**Độ phức tạp:** O(n log n) do bước sắp xếp.

---

</details>

## 📌 Lời khuyên cuối


* 🧾 **Ghi CSV nhớ 3 thứ:** `encoding="utf-8"`, `newline=""`, và `delimiter` đúng (mặc định `,`).
* 🔢 **Ép kiểu ngay khi đọc:** `float(dong["diem"])` trước mọi tính toán — CSV toàn chuỗi.
* 🔁 **DictReader là iterator:** muốn dùng lại nhiều lần, hãy `list(doc)` ngay sau khi đọc.
* 🗂️ **Kiểm tra bằng mắt:** mở file CSV bằng Excel để xem kết quả ghi có đúng không.

👉 Tiếp theo: **[Bài 34: API – Giao Tiếp Giữa Các Chương Trình](../05-API/bai.md)**

---

## ➡️ Điều hướng

**Vị trí:** `04-Full/Phan-3-Thuc-Chien/04-CSV/bai.md`

**Bài tiếp theo:** [Bài 34 — API – Giao Tiếp Giữa Các Chương Trình](../05-API/bai.md)
