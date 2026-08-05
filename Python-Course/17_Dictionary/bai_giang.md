# 📖 Bài 17: Dictionary (Từ Điển) Trong Python

> 🎓 **Chương 5 – Cấu trúc dữ liệu: List, Tuple, Set và Dictionary**

Ở bài 14, 15, 16 bạn đã làm quen với **list**, **tuple**, **set**. Giờ đến "ông vua" tra cứu: **Dictionary** — nơi mỗi thông tin có **nhãn** (khóa) đi kèm giá trị, giống hệt quyển **từ điển** hay **sổ liên lạc**.

---

## 🎯 Mục tiêu

Sau bài học này, học viên sẽ:

* ✅ Hiểu **Dictionary là gì**, vì sao cần nó thay vì list.
* ✅ **Tạo** từ điển bằng `{}` và hàm `dict()`.
* ✅ **Truy cập** giá trị qua khóa với `x['key']` và `get()`.
* ✅ **Thêm, sửa, xóa** phần tử bằng `del`, `pop`, `clear`.
* ✅ **Duyệt** từ điển với `keys()`, `values()`, `items()`.
* ✅ **Kiểm tra** khóa bằng toán tử `in` và lấy số phần tử bằng `len()`.
* ✅ Làm quen **dict comprehension** cơ bản (sẽ học sâu ở bài 26).

---

## 📖 Kiến thức

### 1. Dictionary là gì?

> 💬 **Nói đơn giản:** Dictionary là **hộp lưu dữ liệu theo cặp "khóa – giá trị" (key – value)**. Muốn lấy dữ liệu, chỉ cần gọi đúng **tên khóa** — nhanh như tra từ điển.

**Ví dụ đời thực:** 📒 sổ liên lạc (tên → số điện thoại), 🏫 bảng điểm (môn → điểm), 🍜 menu quán ăn (món → giá tiền).

So sánh với **list**:

```python
mon_hoc = ["Toan", "Van", "Anh"]
diem     = [8.5, 7.0, 9.0]              # ❌ điểm và môn tách rời, dễ nhầm
diem     = {"Toan": 8.5, "Van": 7.0, "Anh": 9.0}   # ✅ gói gọn, tra cứu nhanh
```

```mermaid
mindmap
  root((Dictionary))
    Cặp khóa - giá trị
      Khóa: nhãn bất biến (str, int, tuple)
      Giá trị: mọi kiểu
    Thao tác
      Tạo: {} / dict()
      Truy cập: x["key"], get()
      Thêm - sửa: x["key"] = value
      Xóa: del, pop, clear
      Duyệt: keys(), values(), items()
      Kiểm tra: in, len()
```

### 2. Tạo dictionary

| Cách | Cú pháp | Ví dụ |
|---|---|---|
| Có sẵn dữ liệu | `{khóa: giá_trị, ...}` | `diem = {"Toan": 8.5}` |
| Từ khóa | `dict(...)` | `diem = dict(Toan=8.5)` |
| Rỗng | `{}` hoặc `dict()` | `diem = {}` |

```python
diem = {}                  # từ điển rỗng
diem["ten"] = "Nguyen An"  # thêm khóa "ten" với giá trị "Nguyen An"
```

> ⚠️ **Khóa (key) phải là kiểu bất biến** — thường là chuỗi, số hoặc tuple. Không được dùng **list** làm khóa.

### 3. Truy cập giá trị

```python
diem = {"Toan": 8.5, "Van": 7.0, "Anh": 9.0}

print(diem["Toan"])          # 8.5 — nếu khóa không có sẽ báo KeyError!
print(diem.get("Ly"))        # None — an toàn, không lỗi
print(diem.get("Ly", 0))     # 0 — khóa không có thì trả giá trị mặc định
print(diem.get("Anh", 0))    # 9.0 — khóa có thì lấy giá trị thật
```

> 💡 **`get()` an toàn hơn `diem["khóa"]`**: không báo lỗi khi khóa không tồn tại — dùng cho dữ liệu nhập từ bên ngoài.

### 4. Thêm và sửa phần tử

```python
diem = {"Toan": 8.5}
diem["Van"] = 7.0    # khóa "Van" chưa có → THÊM mới
diem["Toan"] = 9.0   # khóa "Toan" đã có  → SỬA thành 9.0
print(diem)          # {'Toan': 9.0, 'Van': 7.0}
```

> 💡 **Ghi nhớ:** Cùng cú pháp `diem[key] = value` — khóa chưa tồn tại là **thêm**, đã tồn tại là **sửa**.

### 5. Xóa phần tử

| Lệnh | Công dụng |
|---|---|
| `del dic["khóa"]` | Xóa cặp có khóa đó |
| `dic.pop("khóa")` | Xóa và **trả về giá trị** vừa xóa |
| `dic.pop("khóa", mặc_định)` | An toàn: không có khóa thì trả về mặc định |
| `dic.clear()` | Xóa **toàn bộ** từ điển |

### 6. Duyệt từ điển

```python
diem = {"Toan": 8.5, "Van": 7.0, "Anh": 9.0}

for mon in diem:                # duyệt qua các KHÓA
    print(mon)                  # Toan / Van / Anh

for d in diem.values():         # duyệt qua các GIÁ TRỊ
    print(d)                    # 8.5 / 7.0 / 9.0

for mon, d in diem.items():     # duyệt CẢ cặp khóa – giá trị (hay dùng nhất)
    print(mon, "->", d)         # Toan -> 8.5 ...
```

> 💡 `items()` trả về từng cặp; cú pháp `for mon, d in ...` gọi là **giải nén (unpacking)**.

### 7. Kiểm tra và số lượng

```python
diem = {"Toan": 8.5}

print("Toan" in diem)   # True  — khóa tồn tại
print("Ly" in diem)     # False — khóa không tồn tại
print(len(diem))        # 1 — số cặp khóa – giá trị
```

### 8. Dict comprehension (giới thiệu)

```python
diem = {"Toan": 4, "Van": 5, "Anh": 6}
binh_phuong = {mon: d * d for mon, d in diem.items()}
print(binh_phuong)   # {'Toan': 16, 'Van': 25, 'Anh': 36}
```

> 📌 Chỉ cần biết khái niệm ở bài này; bài **26_List_Comprehension** sẽ học chi tiết.

### 9. List hay Dictionary — khi nào dùng gì?

| Tiêu chí | List | Dictionary |
|---|---|---|
| Ý nghĩa | Danh sách có thứ tự | Bảng tra cứu theo nhãn |
| Truy cập | Theo **vị trí** `ds[0]` | Theo **khóa** `dic["ten"]` |
| Tốc độ tìm kiếm | Chậm khi list lớn | Rất nhanh (bảng băm) |
| Khi nào dùng | Danh sách hạng mục | Thông tin có nhãn: điểm môn, hồ sơ, menu |

---

## 💡 Ví dụ minh họa

### Ví dụ 1: Tạo từ điển điểm và tra cứu

```python
# Bước 1: tạo từ điển điểm 3 môn
diem = {"Toan": 8.5, "Van": 7.0, "Anh": 9.0}
# Bước 2: tra cứu điểm Toán
print("Diem Toan:", diem["Toan"])
# Bước 3: tra cứu an toàn môn chưa có
print("Diem Ly:", diem.get("Ly", "Chua co diem"))
```

Kết quả: `Diem Toan: 8.5` và `Diem Ly: Chua co diem`.

| Dòng code | Ý nghĩa |
|---|---|
| `diem = {...}` | Tạo từ điển với 3 cặp khóa – giá trị |
| `diem["Toan"]` | Lấy điểm môn Toán theo khóa |
| `diem.get("Ly", "Chua co diem")` | Không có môn Lý → trả về chuỗi mặc định |

### Ví dụ 2: Menu quán ăn — thêm, sửa, xóa

```python
menu = {"Pho": 45, "Bun": 30, "Com": 25}   # món -> giá (nghìn đồng)
menu["My xao"] = 35     # THÊM món mới
menu["Pho"] = 50        # SỬA giá phở
menu.pop("Com")         # XÓA món cơm (bán hết)

for mon, gia in menu.items():          # duyệt toàn bộ menu
    print(f"{mon}: {gia}k")
```

Kết quả:

```
Pho: 50k
Bun: 30k
My xao: 35k
```

---

## 🔬 Ví dụ nâng cao

### Ví dụ 1: Quản lý điểm học sinh 🏫

```python
diem = {"Toan": 8.5, "Van": 7.0, "Anh": 9.0}

for mon, d in diem.items():            # in bảng điểm
    print(f"{mon}: {d}")

tong = sum(diem.values())              # cộng toàn bộ giá trị
print("Diem trung binh:", round(tong / len(diem), 2))

mon_max = max(diem, key=diem.get)      # so sánh bằng giá trị để lấy khóa
print("Mon cao nhat:", mon_max, "-", diem[mon_max])
```

Kết quả: bảng 3 môn, `Diem trung binh: 8.17`, `Mon cao nhat: Anh - 9.0`.

### Ví dụ 2: Đếm tần suất xuất hiện của chữ cái 🔡

```python
cau = "hello python"
dem = {}                              # từ điển rỗng: chữ -> số lần

for chu in cau:
    if chu != " ":                    # bỏ qua dấu cách
        dem[chu] = dem.get(chu, 0) + 1   # lấy số cũ (mặc định 0) rồi cộng 1

for chu, so_lan in dem.items():
    print(f"{chu}: {so_lan}")
```

> 💡 Kỹ thuật kinh điển `dem.get(chu, 0) + 1` dùng nhiều trong phân tích văn bản.

### Ví dụ 3: Máy tính tiền quán ăn 🍜

```python
menu = {"Pho": 45, "Bun": 30, "Com": 25, "My xao": 35}
goi = ["Pho", "Com"]                   # khách gọi 2 món

tong = 0
for mon in goi:
    tien = menu.get(mon, 0)            # món không có trong menu thì tính 0
    tong += tien
    print(f"{mon}: {tien}k")
print("Tong tien:", tong, "k")
```

Kết quả: `Pho: 45k`, `Com: 25k`, `Tong tien: 70k`.

---

## ⚠️ Lỗi thường gặp

### Lỗi 1: Truy cập khóa không tồn tại — KeyError

```python
diem = {"Toan": 8.5}
print(diem["Ly"])   # ❌ SAI — KeyError: 'Ly', chương trình dừng đột ngột
```

* **Cách sửa:** `diem.get("Ly", 0)` hoặc kiểm tra `if "Ly" in diem:` trước.

### Lỗi 2: Quên dấu phẩy giữa các cặp

```python
diem = {"Toan": 8.5 "Van": 7.0}   # ❌ SAI — SyntaxError
diem = {"Toan": 8.5, "Van": 7.0}  # ✅ ĐÚNG
```

### Lỗi 3: Khóa bị trùng — cặp sau "nuốt" cặp trước

```python
diem = {"Toan": 8.5, "Toan": 9.0}  # chỉ còn {'Toan': 9.0}
```

* **Nguyên nhân:** khóa phải **duy nhất** — mỗi khóa chỉ xuất hiện một lần.

### Lỗi 4: Dùng list làm khóa

```python
diem = {["Toan"]: 8.5}   # ❌ SAI — TypeError: unhashable type: 'list'
```

* **Cách sửa:** dùng khóa bất biến: chuỗi, số, tuple.

### Lỗi 5: Sửa từ điển khi đang duyệt

```python
diem = {"Toan": 8.5, "Van": 7.0, "Anh": 9.0}
for mon in diem:
    del diem[mon]   # ❌ SAI — RuntimeError: dictionary changed size
```

* **Cách sửa:** duyệt bản sao danh sách khóa: `for mon in list(diem):`.

---

## 💎 Mẹo

* 🛡️ **Ưu tiên `get()`** khi truy cập dữ liệu từ bên ngoài — tránh sập chương trình vì `KeyError`.
* ⚡ **`items()` là bạn thân** khi duyệt cả khóa lẫn giá trị.
* 🔑 **Khóa phải bất biến** (str, int, tuple) — đừng dùng list hay dict làm khóa.
* 🧮 **`sum(dic.values())`** tính tổng nhanh; kết hợp `len()` ra trung bình cộng.
* ✨ **f-string + items()** in bảng rất đẹp: `print(f"{mon}: {d}")`.
* 💾 `setdefault(k, v)` vừa đọc vừa tự thêm khóa nếu chưa có — tiện khởi tạo bộ đếm.

---

## 📝 Tóm tắt

| Thao tác | Cú pháp | Ghi chú |
|---|---|---|
| Tạo | `{...}` hoặc `dict()` | Khóa phải bất biến |
| Truy cập | `dic["khóa"]` | Lỗi `KeyError` nếu không có |
| Truy cập an toàn | `dic.get("khóa", mặc_định)` | Trả mặc định thay vì lỗi |
| Thêm / sửa | `dic["khóa"] = giá_trị` | Có thì sửa, không có thì thêm |
| Xóa | `del`, `pop`, `clear` | `pop` trả về giá trị đã xóa |
| Duyệt | `keys()`, `values()`, `items()` | `items()` cho cặp khóa – giá trị |
| Kiểm tra | `"khóa" in dic` | Tránh được `KeyError` |
| Số lượng | `len(dic)` | Số cặp khóa – giá trị |
| Comprehension | `{k: v for k, v in ...}` | Tạo từ điển từ vòng lặp |

---

## 🧪 Kiểm tra nhanh

1. ❓ Dictionary lưu dữ liệu theo cặp gì?
2. ❓ Viết cú pháp tạo từ điển điểm môn Toán bằng `{}`.
3. ❓ Truy cập `dic["khóa"]` mà khóa không tồn tại báo lỗi gì?
4. ❓ Làm sao truy cập an toàn không bị lỗi?
5. ❓ `dic["Toan"] = 9.0` khi khóa "Toan" đã có giá trị thì làm gì?
6. ❓ Lệnh nào xóa toàn bộ từ điển?
7. ❓ `for mon, d in dic.items():` — `mon` và `d` là gì?
8. ❓ Viết biểu thức kiểm tra khóa "Van" có trong `dic` không.
9. ❓ Khi nào gán giá trị cho khóa là **thêm mới**? Khi nào là **sửa**?
10. ❓ Vì sao không thể dùng list làm khóa?

<details>
<summary>🔍 Xem đáp án</summary>

1. Cặp **khóa – giá trị** (key – value).
2. `diem = {"Toan": 8.5}`.
3. `KeyError`.
4. Dùng `dic.get("khóa", giá_trị_mặc_định)` hoặc kiểm tra `in` trước.
5. **Sửa** giá trị cũ thành 9.0 (khóa đã tồn tại).
6. `dic.clear()`.
7. `mon` là khóa (môn học), `d` là giá trị (điểm).
8. `"Van" in dic`.
9. Thêm mới khi khóa **chưa tồn tại**; sửa khi khóa **đã tồn tại**.
10. Vì list là kiểu **có thể thay đổi** — Python yêu cầu khóa bất biến để tra cứu nhanh.

</details>

---

## 📚 Bài đọc thêm

* [Python.org – Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
* [W3Schools – Python Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)
* [Python.org – dict type](https://docs.python.org/3/library/stdtypes.html#dict)

---

## 🏁 Kết thúc bài

🎉 Bạn đã nắm được **Dictionary** — công cụ tra cứu "khóa – giá trị" cực mạnh của Python. Giờ bạn đã có đủ bộ tứ cấu trúc dữ liệu cơ bản, nhưng dữ liệu mới chỉ là số và nhãn — còn **văn bản** thì sao? Hãy sang:

👉 **[Bài 18: Chuỗi (String)](../18_String/bai_giang.md)** — xử lý mọi thứ liên quan đến chữ, từ, câu trong Python.
