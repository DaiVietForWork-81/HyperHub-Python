# ✅ Bài 18: Đáp Án – Chuỗi (String)

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án để việc học hiệu quả nhất.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Nối chuỗi chào hỏi

**Phân tích:** Cần ghép biến `ten` vào giữa câu văn.

**Ý tưởng:** Dùng toán tử `+` nối các chuỗi; phải thêm khoảng trắng thủ công.

**Thuật toán:**
1. Tạo biến `ten`.
2. Nối `"Xin chao " + ten + ", chuc mot ngay tot lanh!"`.
3. In kết quả.

**Code:**

```python
ten = "An"

# Nối chuỗi bằng dấu + (nhớ thêm khoảng trắng)
cau = "Xin chao " + ten + ", chuc mot ngay tot lanh!"
print(cau)
```

**Giải thích code:**
* `"Xin chao "` — có khoảng trắng cuối để tách với tên.
* `+ ten +` — chèn biến vào giữa.
* Kết quả: `Xin chao An, chuc mot ngay tot lanh!`.

**Độ phức tạp:** O(n) với n là độ dài chuỗi tạo ra.

---

### Bài 2: In hoa tên mình

**Phân tích:** Cần bản in hoa và in thường của cùng một chuỗi.

**Ý tưởng:** `upper()` và `lower()` — đều trả về chuỗi mới.

**Thuật toán:**
1. Tạo chuỗi `ten`.
2. In `ten.upper()`.
3. In `ten.lower()`.

**Code:**

```python
ten = "python"

# In hoa toàn bộ
print(ten.upper())
# In thường toàn bộ
print(ten.lower())
```

**Giải thích code:**
* `ten.upper()` → `PYTHON`.
* `ten.lower()` → `python` (giống chuỗi gốc).
* Chuỗi gốc không đổi — hai phương thức này trả về chuỗi mới.

**Độ phức tạp:** O(n).

---

### Bài 3: Độ dài chuỗi

**Phân tích:** Đếm số ký tự của chuỗi, tính cả khoảng trắng.

**Ý tưởng:** Dùng hàm `len()`.

**Thuật toán:**
1. Tạo chuỗi.
2. In `len(thong_bao)`.

**Code:**

```python
thong_bao = "Hom nay troi dep"

# len() đếm mọi ký tự, kể cả khoảng trắng
print("Do dai:", len(thong_bao))
```

**Giải thích code:**
* `"Hom nay troi dep"` gồm 13 chữ cái + 3 khoảng trắng = 16 ký tự.

**Độ phức tạp:** O(1).

---

### Bài 4: Lấy tên riêng từ họ tên

**Phân tích:** Tên riêng là từ cuối cùng của họ tên.

**Ý tưởng:** `split()` tách thành danh sách từ, lấy phần tử cuối bằng `[-1]`.

**Thuật toán:**
1. Tạo chuỗi họ tên.
2. `split()` → danh sách từ.
3. In `cac_tu[-1]`.

**Code:**

```python
ho_ten = "Nguyen Van An"

# split() mặc định tách theo khoảng trắng
cac_tu = ho_ten.split()
print("Ten rieng:", cac_tu[-1])
```

**Giải thích code:**
* `ho_ten.split()` → `['Nguyen', 'Van', 'An']`.
* `cac_tu[-1]` — chỉ số âm đếm từ cuối → `'An'`.

**Độ phức tạp:** O(n).

---

### Bài 5: Thay thế chữ

**Phân tích:** Thay một từ bằng từ khác trong chuỗi.

**Ý tưởng:** `replace(a, b)` thay toàn bộ `a` bằng `b`; phải gán lại kết quả.

**Thuật toán:**
1. Tạo chuỗi.
2. `cau.replace("pho", "bun")`.
3. Gán lại và in.

**Code:**

```python
cau = "Toi thich an pho"

# replace trả về chuỗi mới — cần gán lại
cau_moi = cau.replace("pho", "bun")
print(cau_moi)
```

**Giải thích code:**
* `replace("pho", "bun")` — tìm `"pho"` và thay bằng `"bun"`.
* Kết quả: `Toi thich an bun`.

**Độ phức tạp:** O(n).

---

### Bài 6: Tìm vị trí chữ

**Phân tích:** Cần vị trí xuất hiện đầu tiên của một từ; `-1` nếu không có.

**Ý tưởng:** Dùng `find()`.

**Thuật toán:**
1. Tạo chuỗi.
2. In `find("ngon")` và `find("khong")`.

**Code:**

```python
cau = "Python la ngon ngu tuyen voi"

# find trả về vị trí đầu tiên, hoặc -1 nếu không tìm thấy
print("Vi tri 'ngon':", cau.find("ngon"))
print("Vi tri 'khong':", cau.find("khong"))
```

**Giải thích code:**
* `cau.find("ngon")` — từ "ngon" bắt đầu ở vị trí 10.
* `cau.find("khong")` — không tồn tại → `-1`.

**Độ phức tạp:** O(n).

---

### Bài 7: Xóa khoảng trắng thừa

**Phân tích:** Chuỗi có khoảng trắng thừa ở hai đầu.

**Ý tưởng:** `strip()` xóa khoảng trắng đầu và cuối chuỗi.

**Thuật toán:**
1. Tạo chuỗi lộn xộn.
2. `s.strip()` và in.

**Code:**

```python
s = "   Xin chao Python   "

# strip xóa khoảng trắng ở cả 2 đầu
sach = s.strip()
print(sach)
```

**Giải thích code:**
* `"   Xin chao Python   ".strip()` → `"Xin chao Python"`.

**Độ phức tạp:** O(n).

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Đếm số lần xuất hiện

**Phân tích:** Đếm số lần ký tự `n` xuất hiện trong chuỗi.

**Ý tưởng:** `count("n")` đếm toàn bộ.

**Thuật toán:**
1. Tạo chuỗi.
2. In `cau.count("n")`.

**Code:**

```python
cau = "Python la ngon ngu tuyen voi"

# count đếm số lần xuất hiện của ký tự/từ
print("So lan xuat hien cua 'n':", cau.count("n"))
```

**Giải thích code:**
* Đếm ký tự `n` trong câu: Python(1) + ngon(2) + ngu(1) + tuyen(1) = 5.

**Độ phức tạp:** O(n).

---

### Bài 9: Kiểm tra đầu và cuối chuỗi

**Phân tích:** Kiểm tra phần đầu và phần cuối của tên file.

**Ý tưởng:** `startswith()` và `endswith()` trả về `True`/`False`.

**Thuật toán:**
1. Tạo tên file.
2. In kết quả hai phép kiểm tra.

**Code:**

```python
ten_file = "baitho.docx"

# startswith: bắt đầu bằng?
print("Bat dau bang 'bai':", ten_file.startswith("bai"))
# endswith: kết thúc bằng?
print("Ket thuc bang '.txt':", ten_file.endswith(".txt"))
```

**Giải thích code:**
* `"baitho.docx".startswith("bai")` → True.
* `"baitho.docx".endswith(".txt")` → False (đuôi là `.docx`).

**Độ phức tạp:** O(k) với k là độ dài chuỗi kiểm tra.

---

### Bài 10: Kiểm tra chuỗi toàn số

**Phân tích:** Cần biết chuỗi có phải "toàn chữ số" hay không.

**Ý tưởng:** `isdigit()` chỉ trả `True` khi **mọi** ký tự đều là chữ số.

**Thuật toán:**
1. Lần lượt kiểm tra 3 chuỗi.
2. In kết quả.

**Code:**

```python
print("12345:", "12345".isdigit())   # toàn số -> True
print("12a45:", "12a45".isdigit())   # có chữ cái -> False
print("1.5:", "1.5".isdigit())       # có dấu chấm -> False
```

**Giải thích code:**
* `"12a45"` chứa chữ `a` → không phải toàn chữ số.
* `"1.5"` chứa dấu chấm → không phải chữ số.

**Độ phức tạp:** O(n).

---

### Bài 11: Nối danh sách bằng join

**Phân tích:** Cần nối các phần tử list thành chuỗi có dấu phân cách.

**Ý tưởng:** `", ".join(lop)` — nối bằng chuỗi `", "`.

**Thuật toán:**
1. Tạo danh sách.
2. `", ".join(lop)` và in.

**Code:**

```python
lop = ["10A1", "10A2", "10A3"]

# join nối danh sách thành chuỗi, xen dấu phẩy + khoảng trắng
chuoi = ", ".join(lop)
print(chuoi)
```

**Giải thích code:**
* `join` được gọi trên **chuỗi phân cách** `", "` và nhận danh sách làm đối số.
* Kết quả: `10A1, 10A2, 10A3`.

**Độ phức tạp:** O(n).

---

### Bài 12: Đếm số từ trong câu

**Phân tích:** Số từ = số phần tử sau khi tách theo khoảng trắng.

**Ý tưởng:** `cau.split()` → `len()`.

**Thuật toán:**
1. Tạo câu.
2. Tách thành danh sách từ.
3. In số phần tử.

**Code:**

```python
cau = "Hom nay toi di hoc tieng Anh"

# split tách theo khoảng trắng, len đếm số từ
so_tu = len(cau.split())
print("So tu:", so_tu)
```

**Giải thích code:**
* `"Hom nay toi di hoc tieng Anh".split()` → 6 từ.
* `len(...)` → 6.

**Độ phức tạp:** O(n).

---

### Bài 13: Kết hợp in hoa – in thường

**Phân tích:** Ba yêu cầu: in hoa, in thường, kiểm tra chuỗi gốc.

**Ý tưởng:** `upper()`, `lower()`, `isupper()`.

**Thuật toán:**
1. In bản in hoa.
2. In bản in thường.
3. In kết quả kiểm tra `isupper()`.

**Code:**

```python
s = "ToiDangHocPython"

# Ba thao tác trên cùng chuỗi gốc
print(s.upper())
print(s.lower())
print("Toan in hoa?", s.isupper())
```

**Giải thích code:**
* `s.upper()` → `TOIDANGHOCPYTHON`.
* `s.lower()` → `toidanghocpython`.
* `s.isupper()` → False vì chuỗi gốc có chữ thường.

**Độ phức tạp:** O(n).

---

### Bài 14: Vẽ viền bằng phép nhân chuỗi

**Phân tích:** Dòng viền lặp lại ký tự `*` 20 lần.

**Ý tưởng:** `"*" * 20` tạo chuỗi lặp.

**Thuật toán:**
1. In dòng viền trên.
2. In dòng chữ.
3. In dòng viền dưới.

**Code:**

```python
# Phép nhân chuỗi: lặp lại 20 lần
print("*" * 20)
print("CHAO MUNG")
print("*" * 20)
```

**Giải thích code:**
* `"*" * 20` — chuỗi gồm 20 dấu `*`.

**Độ phức tạp:** O(k) với k = 20.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Thu nhỏ họ tên

**Phân tích:** Hai việc: chuẩn hóa chữ hoa đầu từ, và lấy chữ cái đầu mỗi từ.

**Ý tưởng:** `title()` cho việc 1; `split()` + vòng lặp + `upper()` cho việc 2.

**Thuật toán:**
1. Tách tên thành danh sách từ.
2. Việc 1: nối các từ với `title()`.
3. Việc 2: gom chữ cái đầu mỗi từ, viết hoa.

**Code:**

```python
ho_ten = "nguyen van an"
cac_tu = ho_ten.split()          # ['nguyen', 'van', 'an']

# Việc 1: viết hoa đầu mỗi từ
chuan_hoa = " ".join(tu.title() for tu in cac_tu)
print("Chuan hoa:", chuan_hoa)   # Nguyen Van An

# Việc 2: lấy chữ cái đầu mỗi từ, viết hoa
viet_tat = ""
for tu in cac_tu:
    viet_tat += tu[0].upper()    # cộng dồn chữ cái đầu

print("Viet tat:", viet_tat)     # NVA
```

**Giải thích code:**
* `tu.title()` — viết hoa đầu mỗi từ; `" ".join(...)` nối lại.
* `tu[0]` — chữ cái đầu từ; `.upper()` — viết hoa; `+=` — cộng dồn.
* Kết quả: `Nguyen Van An` và `NVA`.

**Độ phức tạp:** O(n).

---

### Bài 16: Đếm nguyên âm và phụ âm

**Phân tích:** Duyệt từng ký tự, phân loại: nguyên âm, phụ âm, bỏ qua phần khác.

**Ý tưởng:** Vòng lặp kiểm tra `chu in "aeiou"` (đã hạ thường) và `chu.isalpha()`.

**Thuật toán:**
1. Hạ thường chuỗi để dễ so sánh.
2. Duyệt từng ký tự: nguyên âm nếu thuộc `"aeiou"`; phụ âm nếu là chữ cái còn lại.
3. In kết quả.

**Code:**

```python
cau = "Python la ngon ngu tuyen voi"
nguyen_am = 0
phu_am = 0

for chu in cau.lower():
    if chu in "aeiou":            # thuộc tập nguyên âm
        nguyen_am += 1
    elif chu.isalpha():           # còn là chữ cái -> phụ âm
        phu_am += 1

print("Nguyen am:", nguyen_am)
print("Phu am:", phu_am)
```

**Giải thích code:**
* `cau.lower()` — hạ thường để `"P"` và `"p"` đều so sánh được.
* `chu in "aeiou"` — kiểm tra ký tự có trong chuỗi nguyên âm không.
* `chu.isalpha()` — lọc chữ cái, loại khoảng trắng.
* Tổng: 8 nguyên âm, 15 phụ âm.

**Độ phức tạp:** O(n).

---

### Bài 17: Kiểm tra mật khẩu mạnh

**Phân tích:** Bốn điều kiện; cần kiểm tra "có ít nhất một" ký tự loại đó.

**Ý tưởng:** Dùng `any(... for chu in mat_khau)` — đúng nếu có ít nhất một ký tự thỏa mãn.

**Thuật toán:**
1. Nhập mật khẩu.
2. Kiểm tra 4 điều kiện bằng `len()` và `any()`.
3. In kết quả.

**Code:**

```python
mat_khau = input("Nhap mat khau: ")   # Nhập: An123@xyz

# 4 điều kiện
du_dai = len(mat_khau) >= 8
co_chu = any(c.isalpha() for c in mat_khau)   # có chữ cái
co_so = any(c.isdigit() for c in mat_khau)    # có chữ số
co_dac_biet = any(not c.isalnum() for c in mat_khau)  # có ký tự đặc biệt

if du_dai and co_chu and co_so and co_dac_biet:
    print("Manh")
else:
    print("Yeu")
```

**Giải thích code:**
* `any(...)` — trả về `True` nếu **ít nhất một** phần tử thỏa mãn.
* `not c.isalnum()` — ký tự không phải chữ và không phải số → ký tự đặc biệt (`@`).
* Mật khẩu `An123@xyz` đủ 4 điều kiện → `Manh`.

**Độ phức tạp:** O(n) với n là độ dài mật khẩu.

---

### Bài 18: Chuẩn hóa họ tên

**Phân tích:** Khoảng trắng thừa giữa các từ và hai đầu; chữ hoa lộn xộn.

**Ý tưởng:** `strip()` bỏ trắng hai đầu; `split()` mặc định tự gom nhiều khoảng trắng; `title()` viết hoa đầu từ.

**Thuật toán:**
1. Nhập họ tên.
2. `strip()` và `split()` để tách từ sạch.
3. Nối lại bằng `" "` với mỗi từ `title()`.

**Code:**

```python
ho_ten = input("Nhap ho ten: ")   # Nhập:    nguyen   van   an   

# split mặc định tự gom nhiều khoảng trắng; title viết hoa đầu từ
chuan = " ".join(tu.title() for tu in ho_ten.strip().split())
print(chuan)
```

**Giải thích code:**
* `ho_ten.strip()` — bỏ khoảng trắng hai đầu.
* `.split()` — tách theo bất kỳ khoảng trắng nào, nén nhiều trắng thành 1.
* `tu.title()` — mỗi từ viết hoa chữ đầu.
* `" ".join(...)` — nối lại với đúng 1 khoảng trắng.
* Kết quả: `Nguyen Van An`.

**Độ phức tạp:** O(n).

---

### Bài 19: Kiểm tra chuỗi đối xứng (Palindrome)

**Phân tích:** Cần so sánh chuỗi với bản đảo ngược, bỏ qua hoa/thường và khoảng trắng.

**Ý tưởng:** Lọc bỏ khoảng trắng, hạ thường, so sánh với `[::-1]`.

**Thuật toán:**
1. Nhập chuỗi.
2. Bỏ khoảng trắng bằng `replace(" ", "")`.
3. Hạ thường.
4. So sánh với chuỗi đảo ngược.

**Code:**

```python
chuoi = input("Nhap chuoi: ")   # Nhập: Race car

# Xóa khoảng trắng + hạ thường -> "racecar"
sach = chuoi.replace(" ", "").lower()

# So sánh với bản đảo ngược
if sach == sach[::-1]:
    print("Palindrome")
else:
    print("Khong phai palindrome")
```

**Giải thích code:**
* `chuoi.replace(" ", "")` — xóa mọi khoảng trắng.
* `.lower()` — đồng bộ chữ hoa/thường.
* `sach[::-1]` — đảo ngược chuỗi.
* `"racecar" == "racecar"` → `Palindrome`.

**Độ phức tạp:** O(n).

---

### Bài 20: Tạo tên đăng nhập từ họ tên

**Phân tích:** Quy tắc: chữ cái đầu họ + tên riêng + năm, toàn chữ thường.

**Ý tưởng:** `split()` lấy họ `[0]` và tên riêng `[-1]`; lấy `[0]` của họ; `lower()` toàn bộ.

**Thuật toán:**
1. Nhập họ tên.
2. Tách danh sách từ.
3. Họ = phần tử đầu, tên riêng = phần tử cuối.
4. Ghép: chữ đầu họ + tên riêng + "2026", hạ thường.

**Code:**

```python
ho_ten = input("Nhap ho ten: ")   # Nhập: Nguyen Van An
cac_tu = ho_ten.split()

# Họ là phần tử đầu, tên riêng là phần tử cuối
ho = cac_tu[0]
ten_rieng = cac_tu[-1]

# Chữ cái đầu họ + tên riêng + năm, tất cả viết thường
ten_dang_nhap = (ho[0] + ten_rieng + "2026").lower()
print(ten_dang_nhap)
```

**Giải thích code:**
* `ho[0]` — chữ `N` của "Nguyen".
* `"N" + "An" + "2026"` → `"NAn2026"`.
* `.lower()` → `nvan2026`.

**Độ phức tạp:** O(n).

---

## 📌 Lời khuyên cuối

* Khi nối nhiều chuỗi trong vòng lặp, hãy gom vào list rồi dùng `"".join()` — nhanh và sạch hơn.
* Chuỗi bất biến — mọi phương thức chỉ trả về chuỗi mới, đừng quên gán lại.
* Kiểm tra đầu vào bằng `isdigit()`, `isalpha()` trước khi xử lý để tránh lỗi bất ngờ (bài 19 sẽ học cách chuyên nghiệp hơn).

👉 Tiếp theo: **[Bài 19: Ngoại lệ (Exception)](../19_Exception/bai_giang.md)**
