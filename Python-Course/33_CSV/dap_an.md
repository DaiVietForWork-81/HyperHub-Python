# ✅ Bài 33: Đáp Án – CSV

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án để việc học hiệu quả nhất. Mỗi đáp án dưới đây tự tạo file dữ liệu mẫu trước khi xử lý nên chạy được ngay trên máy của bạn.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Ghi danh sách môn học

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

### Bài 2: Đọc file và in từng dòng

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

### Bài 3: Ghi danh sách học viên

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

### Bài 4: In tên và điểm bằng DictReader

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

### Bài 5: Xuất bảng điểm bằng DictWriter

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

### Bài 6: Đọc file dấu chấm phẩy

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

### Bài 7: Đếm số học viên

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

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Tính điểm trung bình từng học viên

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

### Bài 9: Lọc học viên điểm cao

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

### Bài 10: Tìm học viên điểm cao nhất

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

### Bài 11: Xuất CSV thêm cột tổng và trung bình

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

### Bài 12: Xếp loại học lực

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

### Bài 13: Chuyển JSON sang CSV

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

### Bài 14: Cộng điểm hai file CSV

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

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Thống kê theo lớp

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

### Bài 16: Gộp nhiều file CSV

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

### Bài 17: Cập nhật điểm trong CSV

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

### Bài 18: Kiểm tra file CSV hợp lệ

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

### Bài 19: Chuyển đổi mã hóa và dấu phân cách

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

### Bài 20: Hệ thống quản lý điểm (Mini Project)

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

## 📌 Lời khuyên cuối

* 🧾 **Ghi CSV nhớ 3 thứ:** `encoding="utf-8"`, `newline=""`, và `delimiter` đúng (mặc định `,`).
* 🔢 **Ép kiểu ngay khi đọc:** `float(dong["diem"])` trước mọi tính toán — CSV toàn chuỗi.
* 🔁 **DictReader là iterator:** muốn dùng lại nhiều lần, hãy `list(doc)` ngay sau khi đọc.
* 🗂️ **Kiểm tra bằng mắt:** mở file CSV bằng Excel để xem kết quả ghi có đúng không.

👉 Tiếp theo: **[Bài 34: API – Giao Tiếp Giữa Các Chương Trình](../34_API/bai_giang.md)**
