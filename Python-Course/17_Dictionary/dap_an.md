# ✅ Bài 17: Đáp Án – Dictionary (Từ Điển)

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án để việc học hiệu quả nhất.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Tạo từ điển điểm môn học

**Phân tích:** Tạo dictionary 3 cặp khóa – giá trị rồi in ra.

**Ý tưởng:** Dùng ngoặc nhọn `{}` với cú pháp `{khóa: giá_trị, ...}`.

**Thuật toán:**
1. Tạo từ điển `diem` với 3 môn.
2. In từ điển ra màn hình.

**Code:**

```python
# Tạo từ điển điểm 3 môn
diem = {"Toan": 8.5, "Van": 7.0, "Anh": 9.0}
# In toàn bộ từ điển
print(diem)
```

**Giải thích code:**
* `diem = {...}` — tạo dictionary; mỗi môn là một **khóa**, điểm là **giá trị**.
* `print(diem)` — in cả từ điển, Python hiển thị dạng `{'Toan': 8.5, ...}`.

**Độ phức tạp:** O(1).

---

### Bài 2: Tra cứu điểm

**Phân tích:** Cần lấy đúng giá trị của hai khóa cụ thể.

**Ý tưởng:** Dùng cú pháp ngoặc vuông `diem["Toan"]`.

**Thuật toán:**
1. Tạo từ điển `diem`.
2. In giá trị của khóa `"Toan"` và `"Anh"`.

**Code:**

```python
diem = {"Toan": 8.5, "Van": 7.0, "Anh": 9.0}

# Tra cứu điểm theo khóa
print("Diem Toan:", diem["Toan"])
print("Diem Anh:", diem["Anh"])
```

**Giải thích code:**
* `diem["Toan"]` — trả về `8.5`, giá trị ứng với khóa `"Toan"`.
* `diem["Anh"]` — trả về `9.0`.

**Độ phức tạp:** O(1) — truy cập theo khóa rất nhanh.

---

### Bài 3: Tra cứu an toàn với get()

**Phân tích:** Món `Ga ran` không có trong menu — nếu dùng `menu["Ga ran"]` sẽ báo `KeyError`.

**Ý tưởng:** Dùng `get(khóa, mặc_định)` để trả về `0` khi không tìm thấy.

**Thuật toán:**
1. Tạo menu.
2. In giá món `Pho` bằng `get` với mặc định 0.
3. In giá món `Ga ran` bằng `get` với mặc định 0.

**Code:**

```python
menu = {"Pho": 45, "Bun": 30}

# get(key, default): không có khóa thì trả về mặc định
print("Pho:", menu.get("Pho", 0))
print("Ga ran:", menu.get("Ga ran", 0))
```

**Giải thích code:**
* `menu.get("Pho", 0)` — khóa có tồn tại → trả về `45`.
* `menu.get("Ga ran", 0)` — khóa không tồn tại → trả về `0`, không báo lỗi.

**Độ phức tạp:** O(1).

---

### Bài 4: Thêm môn học mới

**Phân tích:** Khóa chưa tồn tại nên gán giá trị sẽ thêm cặp mới.

**Ý tưởng:** `diem["Van"] = 7.0` — Python tự thêm nếu khóa chưa có.

**Thuật toán:**
1. Tạo từ điển có 1 môn.
2. Gán lần lượt 2 môn còn lại.
3. In kết quả.

**Code:**

```python
# Từ điển ban đầu chỉ có môn Toán
diem = {"Toan": 8.5}

# Gán cho khóa chưa tồn tại => THÊM mới
diem["Van"] = 7.0
diem["Anh"] = 9.0

print(diem)
```

**Giải thích code:**
* `diem["Van"] = 7.0` — khóa `"Van"` chưa có trong từ điển → cặp mới được thêm vào.
* Thứ tự in ra giữ nguyên thứ tự thêm.

**Độ phức tạp:** O(1) mỗi lần thêm.

---

### Bài 5: Sửa điểm

**Phân tích:** Khóa `"Toan"` đã tồn tại nên gán giá trị sẽ **thay thế** giá trị cũ.

**Ý tưởng:** `diem["Toan"] = 9.0`.

**Thuật toán:**
1. Tạo từ điển 2 môn.
2. Gán giá trị mới cho khóa `"Toan"`.
3. In kết quả.

**Code:**

```python
diem = {"Toan": 8.5, "Van": 7.0}

# Khóa "Toan" đã tồn tại => SỬA giá trị cũ thành 9.0
diem["Toan"] = 9.0

print(diem)
```

**Giải thích code:**
* Cùng cú pháp gán như bài 4, nhưng khóa đã có nên đây là **sửa** chứ không phải thêm.

**Độ phức tạp:** O(1).

---

### Bài 6: Xóa món khỏi menu bằng pop()

**Phân tích:** Cần vừa xóa vừa lấy giá trị của món đã xóa.

**Ý tưởng:** `pop("Com")` trả về giá trị `25` đồng thời xóa cặp đó.

**Thuật toán:**
1. Tạo menu.
2. `pop` món "Com" và lưu giá trị.
3. In giá trị vừa xóa và menu còn lại.

**Code:**

```python
menu = {"Pho": 45, "Bun": 30, "Com": 25}

# pop vừa xóa vừa trả về giá trị của khóa bị xóa
gia = menu.pop("Com")

print("Da xoa:", gia)
print(menu)
```

**Giải thích code:**
* `menu.pop("Com")` — xóa cặp `"Com": 25` và trả về `25`.
* Sau `pop`, menu chỉ còn `{'Pho': 45, 'Bun': 30}`.

**Độ phức tạp:** O(1).

---

### Bài 7: Kiểm tra khóa tồn tại

**Phân tích:** Cần biết khóa có tồn tại hay không trước khi truy cập.

**Ý tưởng:** Toán tử `in` trả về `True`/`False`.

**Thuật toán:**
1. Tạo từ điển.
2. Kiểm tra `"Toan" in diem`.
3. Kiểm tra `"Ly" in diem`.

**Code:**

```python
diem = {"Toan": 8.5, "Anh": 9.0}

# in: kiểm tra khóa có tồn tại không
print("Toan:", "Toan" in diem)   # True
print("Ly:", "Ly" in diem)       # False
```

**Giải thích code:**
* `"Toan" in diem` — khóa tồn tại → `True`.
* `"Ly" in diem` — khóa không tồn tại → `False`.

**Độ phức tạp:** O(1).

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Duyệt khóa và in từng môn

**Phân tích:** Vòng lặp `for` trên dictionary mặc định duyệt qua các **khóa**.

**Ý tưởng:** `for mon in diem:` — `mon` lần lượt nhận từng khóa.

**Thuật toán:**
1. Tạo từ điển.
2. Vòng lặp in từng khóa.

**Code:**

```python
diem = {"Toan": 8.5, "Van": 7.0, "Anh": 9.0}

# Duyệt từ điển: biến mon nhận từng KHÓA
for mon in diem:
    print(mon)
```

**Giải thích code:**
* `for mon in diem:` — viết tắt của `for mon in diem.keys()`.
* Ba lần lặp ứng với ba khóa: `Toan`, `Van`, `Anh`.

**Độ phức tạp:** O(n) với n là số cặp khóa–giá trị.

---

### Bài 9: Tính tổng và trung bình điểm

**Phân tích:** Cần cộng toàn bộ giá trị và chia cho số môn.

**Ý tưởng:** `sum(diem.values())` và `len(diem)`.

**Thuật toán:**
1. Tính tổng giá trị.
2. Trung bình = tổng / số môn.
3. Làm tròn 2 chữ số và in.

**Code:**

```python
diem = {"Toan": 8.5, "Van": 7.0, "Anh": 9.0}

tong = sum(diem.values())          # tổng các giá trị: 8.5 + 7.0 + 9.0
trung_binh = tong / len(diem)      # chia cho số môn

print("Tong:", tong)
print("Trung binh:", round(trung_binh, 2))
```

**Giải thích code:**
* `diem.values()` — tập hợp toàn bộ giá trị (điểm).
* `sum(...)` — hàm cộng tất cả phần tử.
* `round(trung_binh, 2)` — giữ 2 chữ số sau dấu phẩy: `8.17`.

**Độ phức tạp:** O(n).

---

### Bài 10: Duyệt cặp khóa – giá trị

**Phân tích:** Cần cả khóa lẫn giá trị trong mỗi vòng lặp.

**Ý tưởng:** `items()` trả về từng cặp; viết `for mon, d in diem.items()` để giải nén.

**Thuật toán:**
1. Tạo từ điển.
2. Vòng lặp in `khóa: giá_trị`.

**Code:**

```python
diem = {"Toan": 8.5, "Van": 7.0, "Anh": 9.0}

# items() cho từng cặp (khóa, giá trị); giải nén vào 2 biến
for mon, d in diem.items():
    print(mon, ": ", d, sep="")
```

**Giải thích code:**
* `diem.items()` — danh sách các cặp như `("Toan", 8.5)`.
* `for mon, d in ...` — `mon` nhận khóa, `d` nhận giá trị.
* `sep=""` — không thêm khoảng trắng giữa các đối số.

**Độ phức tạp:** O(n).

---

### Bài 11: Đếm số phần tử

**Phân tích:** Số phần tử của dictionary là số cặp khóa – giá trị.

**Ý tưởng:** Dùng `len()`.

**Thuật toán:**
1. Tạo từ điển từ vựng.
2. In `len(tu_vung)`.

**Code:**

```python
tu_vung = {"apple": "qua tao", "book": "quyen sach", "pen": "cay but"}

# len() đếm số cặp khóa - giá trị
print("So tu dang hoc:", len(tu_vung))
```

**Giải thích code:**
* `len(tu_vung)` — trả về `3` vì có 3 cặp khóa – giá trị.

**Độ phức tạp:** O(1).

---

### Bài 12: Bảng tuổi của bạn bè

**Phân tích:** In đẹp mắt từng cặp tên – tuổi.

**Ý tưởng:** Kết hợp `items()` với f-string.

**Thuật toán:**
1. Tạo từ điển `ban_be`.
2. Duyệt `items()`, in dạng f-string.

**Code:**

```python
ban_be = {"An": 15, "Binh": 16, "Chi": 15}

# f-string: nhúng biến trực tiếp vào chuỗi
for ten, tuoi in ban_be.items():
    print(f"{ten} {tuoi} tuoi")
```

**Giải thích code:**
* `f"{ten} {tuoi} tuoi"` — Python thay `{ten}` bằng tên, `{tuoi}` bằng số tuổi.

**Độ phức tạp:** O(n).

---

### Bài 13: get() với giá trị mặc định khi điểm danh

**Phân tích:** `Chi` chưa có điểm — cần giá trị mặc định thay vì lỗi.

**Ý tưởng:** `get("Chi", 0)` trả về 0.

**Thuật toán:**
1. Tạo từ điển điểm danh.
2. In điểm `An` (có sẵn).
3. In điểm `Chi` với mặc định 0.

**Code:**

```python
diem = {"An": 8, "Binh": 7}

# Khóa "An" tồn tại => lấy giá trị thật
print("An:", diem.get("An", 0))
# Khóa "Chi" không tồn tại => trả về 0
print("Chi:", diem.get("Chi", 0))
```

**Giải thích code:**
* `diem.get("An", 0)` — có khóa → trả về `8`.
* `diem.get("Chi", 0)` — không có khóa → trả về `0`.

**Độ phức tạp:** O(1).

---

### Bài 14: Xóa bằng del và clear()

**Phân tích:** Hai cách xóa: xóa 1 phần tử (`del`) và xóa tất cả (`clear`).

**Ý tưởng:** Dùng `del` trước, in kết quả; rồi `clear()` và in tiếp.

**Thuật toán:**
1. Tạo menu 4 món.
2. `del menu["Bun"]` — xóa 1 món, in kết quả.
3. `menu.clear()` — xóa hết, in kết quả.

**Code:**

```python
menu = {"Pho": 45, "Bun": 30, "Com": 25, "My xao": 35}

# del xóa cặp có khóa "Bun"
del menu["Bun"]
print("Sau khi del:", menu)

# clear xóa toàn bộ từ điển
menu.clear()
print("Sau khi clear:", menu)
```

**Giải thích code:**
* `del menu["Bun"]` — xóa đúng cặp `"Bun": 30`, các món khác còn nguyên.
* `menu.clear()` — từ điển trở thành rỗng `{}`.

**Độ phức tạp:** `del` là O(1); `clear` là O(1).

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Đếm tần suất chữ cái

**Phân tích:** Mỗi chữ cái là một khóa, số lần xuất hiện là giá trị.

**Ý tưởng:** Công thức kinh điển `dem[chu] = dem.get(chu, 0) + 1` — lấy số lần cũ (mặc định 0) rồi cộng 1.

**Thuật toán:**
1. Khởi tạo từ điển rỗng `dem`.
2. Duyệt từng ký tự: bỏ qua dấu cách, tăng bộ đếm.
3. In từng cặp chữ – số lần.

**Code:**

```python
cau = "python la ngon ngu tuyen voi"
dem = {}                            # từ điển rỗng: chữ -> số lần

for chu in cau:
    if chu != " ":                  # bỏ qua dấu cách
        dem[chu] = dem.get(chu, 0) + 1

# In kết quả theo thứ tự xuất hiện
for chu, so_lan in dem.items():
    print(f"{chu}: {so_lan}")
```

**Giải thích code:**
* `dem.get(chu, 0)` — số lần xuất hiện cũ của chữ đó (0 nếu mới gặp lần đầu).
* `+ 1` — tăng thêm một lần.
* Kết quả ví dụ: `t` xuất hiện 2 lần ("python", "tuyen"), `o` xuất hiện 3 lần ("python", "ngon", "voi").

**Độ phức tạp:** O(m) với m là số ký tự của câu.

---

### Bài 16: Máy tính tiền quán ăn

**Phân tích:** Nhập nhiều món cho tới khi gõ `xong`; tra giá từng món và cộng dồn.

**Ý tưởng:** Vòng lặp `while True`; kiểm tra khóa bằng `in`; `break` khi gõ `xong`.

**Thuật toán:**
1. Tạo menu.
2. Lặp: nhập tên món; nếu `xong` thì thoát; nếu món có trong menu thì cộng giá, ngược lại báo không có.
3. In tổng tiền.

**Code:**

```python
menu = {"Pho": 45, "Bun": 30, "Com": 25, "My xao": 35}
tong = 0

while True:
    mon = input("Nhap mon (xong de dung): ")   # Nhập: Pho
    if mon == "xong":                          # gõ xong => dừng
        break
    if mon in menu:                            # món có trong menu
        tien = menu[mon]
        tong += tien
        print(f"{mon}: {tien}k")
    else:
        print("Khong co mon nay!")

print("Tong tien:", tong, "k")
```

**Giải thích code:**
* `while True:` — vòng lặp vô hạn có điều kiện thoát.
* `mon in menu` — kiểm tra món tồn tại trước khi truy cập, tránh `KeyError`.
* `break` — thoát vòng lặp khi khách gõ `xong`.

**Độ phức tạp:** O(k × n) với k là số món khách gọi, mỗi lần kiểm tra `in` là O(1) trung bình → thực tế gần O(k).

---

### Bài 17: Quản lý điểm — thêm, sửa, xóa

**Phân tích:** Kết hợp các thao tác: thêm, sửa, xóa trên cùng một từ điển.

**Ý tưởng:** Gán để thêm/sửa, `pop` để xóa, `items()` để in.

**Thuật toán:**
1. Tạo từ điển 2 môn.
2. Thêm `Anh: 9.0`.
3. Sửa `Toan` thành `9.5`.
4. Xóa `Van` bằng `pop`.
5. In bảng điểm cuối cùng.

**Code:**

```python
diem = {"Toan": 8.5, "Van": 7.0}

diem["Anh"] = 9.0      # THÊM môn mới
diem["Toan"] = 9.5     # SỬA điểm Toán
diem.pop("Van")        # XÓA môn Văn

# In bảng điểm cuối cùng
for mon, d in diem.items():
    print(f"{mon}: {d}")
```

**Giải thích code:**
* `diem["Anh"] = 9.0` — khóa mới → thêm.
* `diem["Toan"] = 9.5` — khóa cũ → sửa.
* `diem.pop("Van")` — xóa môn Văn.
* Kết quả chỉ còn `Toan: 9.5` và `Anh: 9.0`.

**Độ phức tạp:** O(n) với n là số môn còn lại (do bước in).

---

### Bài 18: Tìm môn điểm cao nhất

**Phân tích:** Duyệt toàn bộ cặp, lưu môn có điểm cao nhất; nếu bằng điểm thì giữ môn gặp trước (chỉ dùng `>`).

**Ý tưởng:** Khởi tạo `mon_max`, `diem_max`; cập nhật khi gặp điểm lớn hơn.

**Thuật toán:**
1. Khởi tạo với môn đầu tiên.
2. Duyệt `items()`, nếu điểm lớn hơn `diem_max` thì cập nhật.
3. In kết quả.

**Code:**

```python
diem = {"Toan": 7.5, "Van": 9.0, "Anh": 8.0, "Ly": 9.0}

# Khởi tạo với cặp đầu tiên
mon_max = ""
diem_max = -1

for mon, d in diem.items():
    if d > diem_max:          # dùng ">" nên gặp điểm bằng nhau giữ môn cũ
        mon_max = mon
        diem_max = d

print(f"Mon cao nhat: {mon_max}, diem: {diem_max}")
```

**Giải thích code:**
* `diem_max = -1` — điểm khởi tạo nhỏ hơn mọi điểm thật nên vòng lặp chắc chắn cập nhật ít nhất một lần.
* Điều kiện `>` giữ môn gặp trước khi hai môn bằng điểm (Van gặp trước Ly) → kết quả `Van`.

**Độ phức tạp:** O(n).

---

### Bài 19: Dict comprehension nhân đôi điểm

**Phân tích:** Tạo từ điển mới từ từ điển cũ với giá trị biến đổi.

**Ý tưởng:** `{mon: d * 2 for mon, d in diem.items()}`.

**Thuật toán:**
1. Tạo từ điển gốc.
2. Dùng dict comprehension tạo từ điển mới.
3. In kết quả.

**Code:**

```python
diem = {"Toan": 4, "Van": 5, "Anh": 6}

# Dict comprehension: với mỗi cặp (môn, điểm) => (môn, điểm*2)
diem_moi = {mon: d * 2 for mon, d in diem.items()}

print(diem_moi)
```

**Giải thích code:**
* `for mon, d in diem.items()` — duyệt từng cặp.
* `mon: d * 2` — khóa giữ nguyên, giá trị nhân đôi.
* Kết quả: `{'Toan': 8, 'Van': 10, 'Anh': 12}`.

**Độ phức tạp:** O(n).

---

### Bài 20: Tổng hợp — xếp loại học sinh

**Phân tích:** Gồm 3 phần: in bảng điểm, tính trung bình, xếp loại theo quy tắc.

**Ý tưởng:** Kết hợp `items()`, `sum()`/`len()` và chuỗi `if...elif...else`.

**Thuật toán:**
1. In bảng điểm từng môn.
2. Tính trung bình: tổng chia số môn, làm tròn 2 chữ số.
3. Xếp loại theo mốc: ≥ 8.0 → Giỏi; ≥ 6.5 → Khá; ≥ 5.0 → Trung bình; còn lại → Yếu.

**Code:**

```python
diem = {"Toan": 8.5, "Van": 7.0, "Anh": 9.0, "Ly": 6.5}

# Bước 1: in bảng điểm
for mon, d in diem.items():
    print(f"{mon}: {d}")

# Bước 2: tính điểm trung bình
tb = round(sum(diem.values()) / len(diem), 2)
print("Trung binh:", tb)

# Bước 3: xếp loại
if tb >= 8.0:
    loai = "Gioi"
elif tb >= 6.5:
    loai = "Kha"
elif tb >= 5.0:
    loai = "Trung binh"
else:
    loai = "Yeu"

print("Xep loai:", loai)
```

**Giải thích code:**
* `sum(diem.values())` — tổng điểm `8.5 + 7.0 + 9.0 + 6.5 = 31.0`.
* `31.0 / 4 = 7.75` → làm tròn giữ nguyên `7.75`.
* `7.75 >= 6.5` nhưng `< 8.0` → rơi vào nhánh `Kha`.

**Độ phức tạp:** O(n).

---

## 📌 Lời khuyên cuối

* Luôn dùng `get()` hoặc `in` trước khi truy cập dữ liệu nhập từ bên ngoài để tránh `KeyError`.
* Nhớ sự khác biệt: gán khóa **chưa có** = thêm, khóa **đã có** = sửa.
* `items()` là cách duyệt từ điển sạch đẹp nhất — hãy dùng thường xuyên.

👉 Tiếp theo: **[Bài 18: Chuỗi (String)](../18_String/bai_giang.md)**
