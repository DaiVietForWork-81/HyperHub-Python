# ✅ Bài 22: Đáp Án – Đọc Và Ghi File

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án để việc học hiệu quả nhất.

> 📌 Mọi lời giải đều dùng `with open(...)` + `encoding="utf-8"` và **tự tạo file dữ liệu ngay trong code** (mode `"w"`) trước khi xử lý — chạy được ngay mà không sợ lỗi file không tồn tại.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Ghi rồi đọc lại

**Phân tích:** Hai thao tác ngược nhau: ghi bằng `write`, đọc bằng `read`.

**Ý tưởng:** Mở file mode `"w"` ghi chuỗi; mở lại mode `"r"` đọc toàn bộ và in.

**Thuật toán:**
1. `open("hello.txt", "w", encoding="utf-8")` → `write("Xin chao the gioi Python!")`.
2. `open("hello.txt", "r", encoding="utf-8")` → `read()`.
3. In nội dung đọc được.

**Code:**

```python
# Bước 1: ghi chuỗi vào file (mode "w" tự tạo file nếu chưa có)
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("Xin chao the gioi Python!")

# Bước 2: đọc lại toàn bộ nội dung
with open("hello.txt", "r", encoding="utf-8") as f:
    noi_dung = f.read()

print(noi_dung)
```

**Giải thích code:**
* Mode `"w"` — ghi đè từ đầu; file chưa tồn tại thì Python tự tạo.
* `read()` trả về toàn bộ nội dung dạng chuỗi.
* Hai `with` riêng biệt: mở để ghi xong đóng, rồi mở lại để đọc.

**Độ phức tạp:** O(n) với n là số ký tự file.

---

### Bài 2: Ghi nhiều dòng

**Phân tích:** Mỗi dòng là một lần `write`; phải tự thêm `\n`.

**Ý tưởng:** Ghi 3 lần với `\n`, đọc bằng vòng lặp `for dong in f`.

**Thuật toán:**
1. Mở `"w"`, `write` 3 dòng mỗi dòng kèm `"\n"`.
2. Mở `"r"`, vòng `for` in từng dòng đã `strip()`.

**Code:**

```python
# Ghi 3 dòng vào file
with open("mon_hoc.txt", "w", encoding="utf-8") as f:
    f.write("Toan\n")
    f.write("Van\n")
    f.write("Anh\n")

# Đọc lại từng dòng và in
with open("mon_hoc.txt", "r", encoding="utf-8") as f:
    for dong in f:
        print("Mon:", dong.strip())
```

**Giải thích code:**
* `write("Toan\n")` — `\n` là ký tự xuống dòng; thiếu nó mọi dòng sẽ dính làm một.
* `for dong in f` — Python duyệt file từng dòng một, tiết kiệm bộ nhớ.
* `dong.strip()` — bỏ `\n` và khoảng trắng thừa.

**Độ phức tạp:** O(n) với n tổng số ký tự.

---

### Bài 3: Đọc toàn bộ bằng `read()`

**Phân tích:** `read()` đọc cả file thành một chuỗi; `len()` đếm ký tự kèm cả `\n`.

**Ý tưởng:** Ghi 2 câu thơ, đọc lại, in nội dung và độ dài.

**Thuật toán:**
1. Ghi `"Rung xanh la biec\n"` và `"Chim hot trong cay\n"`.
2. `read()` → in nội dung.
3. `len(noi_dung)` → in số ký tự.

**Code:**

```python
# Tạo file thơ
with open("tho.txt", "w", encoding="utf-8") as f:
    f.write("Rung xanh la biec\n")
    f.write("Chim hot trong cay\n")

# Đọc toàn bộ
with open("tho.txt", "r", encoding="utf-8") as f:
    noi_dung = f.read()

print(noi_dung, end="")          # end="" để không in thêm xuống dòng
print("So ky tu:", len(noi_dung))
```

**Giải thích code:**
* Chuỗi đọc được là `"Rung xanh la biec\nChim hot trong cay\n"`.
* Đếm: `17 + 1 + 18 + 1 = 37` ký tự — hai dấu `\n` cũng được đếm.
* `print(noi_dung, end="")` — nội dung đã có sẵn `\n`, tránh in thêm dòng trống.

**Độ phức tạp:** O(n).

---

### Bài 4: Mode `"a"` — ghi thêm

**Phân tích:** Mode `"a"` (append) không xóa dữ liệu cũ — kiểm chứng bằng cách ghi 2 lần.

**Ý tưởng:** Lần 1 mode `"w"` ghi 2 dòng; lần 2 mode `"a"` ghi thêm 1 dòng; đọc lại toàn bộ.

**Thuật toán:**
1. Mở `"w"` ghi `Buoi sang`, `Buoi chieu`.
2. Mở `"a"` ghi `Buoi toi`.
3. Mở `"r"` in toàn bộ.

**Code:**

```python
# Lần 1: tạo file với 2 dòng
with open("nhat_ky.txt", "w", encoding="utf-8") as f:
    f.write("Buoi sang: hoc Python\n")
    f.write("Buoi chieu: lam bai tap\n")

# Lần 2: mode "a" chỉ thêm vào cuối, không xóa gì
with open("nhat_ky.txt", "a", encoding="utf-8") as f:
    f.write("Buoi toi: on lai bai\n")

# Đọc lại và in toàn bộ 3 dòng
with open("nhat_ky.txt", "r", encoding="utf-8") as f:
    print(f.read())
```

**Giải thích code:**
* Lần 1 dùng `"w"` vì cần tạo file mới; lần 2 phải dùng `"a"` để giữ 2 dòng cũ.
* Nếu lần 2 dùng `"w"` thì file chỉ còn 1 dòng — dữ liệu cũ biến mất.
* `read()` in cả 3 dòng, chứng minh mode `"a"` giữ nguyên dữ liệu.

**Độ phức tạp:** O(n).

---

### Bài 5: `readlines()` và đếm dòng

**Phân tích:** `readlines()` trả về list — đếm bằng `len()`, duyệt bằng vòng lặp.

**Ý tưởng:** Tạo file 4 tên, đọc thành list, in số dòng và từng tên sau `strip()`.

**Thuật toán:**
1. Ghi 4 tên học sinh (4 dòng).
2. `readlines()` → list.
3. In `len(list)` và từng phần tử đã `strip()`.

**Code:**

```python
# Tạo file 4 tên học sinh
with open("hs.txt", "w", encoding="utf-8") as f:
    f.writelines(["An\n", "Binh\n", "Cuong\n", "Dung\n"])

# Đọc thành list các dòng
with open("hs.txt", "r", encoding="utf-8") as f:
    danh_sach_dong = f.readlines()

print("So dong:", len(danh_sach_dong))
for dong in danh_sach_dong:
    print(dong.strip())
```

**Giải thích code:**
* `writelines(list)` — ghi cả list chuỗi liền mạch; vẫn phải có `\n` trong từng phần tử.
* `readlines()` trả về `["An\n", "Binh\n", "Cuong\n", "Dung\n"]` → 4 phần tử.
* `.strip()` xóa `\n` trước khi in.

**Độ phức tạp:** O(n) với n tổng ký tự.

---

### Bài 6: Ghi danh sách học sinh

**Phân tích:** Chuyển dữ liệu trong bộ nhớ (list tuple) thành dòng chữ trên file.

**Ý tưởng:** Duyệt list, ghi từng cặp `Ten,Lop` thành một dòng.

**Thuật toán:**
1. Khai báo list 3 tuple `("Ten", "Lop")`.
2. Mode `"w"`: mỗi cặp ghi `f"{ten},{lop}\n"`.
3. Đọc lại và in toàn bộ.

**Code:**

```python
# Danh sách học sinh trong chương trình
danh_sach = [
    ("Nguyen Van An", "10A1"),
    ("Tran Thi Mai", "10A1"),
    ("Le Quang Binh", "10A2"),
]

# Ghi toàn bộ vào file
with open("hoc_sinh.txt", "w", encoding="utf-8") as f:
    for ten, lop in danh_sach:
        f.write(f"{ten},{lop}\n")

# Đọc lại và in
with open("hoc_sinh.txt", "r", encoding="utf-8") as f:
    print(f.read(), end="")
```

**Giải thích code:**
* `for ten, lop in danh_sach` — giải nén tuple thành 2 biến.
* Định dạng `Ten,Lop` (dấu phẩy) là "quy ước" giúp bài sau tách cột bằng `split(",")`.
* Mỗi dòng kết thúc bằng `\n` để từng học sinh ở một dòng.

**Độ phức tạp:** O(n) với n học sinh.

---

### Bài 7: `readline()` lần lượt

**Phân tích:** Mỗi lần gọi `readline()` đọc đúng một dòng và con trỏ tự nhảy xuống dòng kế.

**Ý tưởng:** Tạo file 3 dòng, gọi `readline()` 2 lần, in với nhãn.

**Thuật toán:**
1. Ghi `"Python\n"`, `"la\n"`, `"ngon ngu\n"`.
2. `d1 = f.readline()`; `d2 = f.readline()`.
3. In `d1`, `d2` sau khi `strip()`.

**Code:**

```python
# Tạo file 3 dòng
with open("tinh.txt", "w", encoding="utf-8") as f:
    f.write("Python\n")
    f.write("la\n")
    f.write("ngon ngu\n")

# Đọc lần lượt 2 dòng đầu
with open("tinh.txt", "r", encoding="utf-8") as f:
    d1 = f.readline()
    d2 = f.readline()

print("Dong 1:", d1.strip())
print("Dong 2:", d2.strip())
```

**Giải thích code:**
* `readline()` thứ nhất trả `"Python\n"`, con trỏ xuống dòng 2.
* `readline()` thứ hai trả `"la\n"`.
* `.strip()` bỏ `\n` để in gọn đẹp.

**Độ phức tạp:** O(1) — chỉ đọc 2 dòng.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Đọc điểm từ file

**Phân tích:** Mỗi dòng là một bản ghi; cần tách cột, đổi kiểu dữ liệu, tính toán.

**Ý tưởng:** `strip()` → `split(",")` → `float()` từng điểm → trung bình.

**Thuật toán:**
1. Tạo `diem.txt` với 3 dòng `Ten,Toan,Van,Anh`.
2. Với mỗi dòng: bỏ `\n`, bỏ dòng trống, tách cột.
3. Tính TB = `sum(diem)/len(diem)`, in 2 chữ số thập phân.

**Code:**

```python
# Tạo file điểm mẫu (4 cột: tên + 3 điểm)
with open("diem.txt", "w", encoding="utf-8") as f:
    f.write("Nguyen Van An,8.5,7.0,9.0\n")
    f.write("Tran Thi Mai,6.0,6.5,7.0\n")
    f.write("Le Quang Binh,4.5,5.0,5.5\n")

# Đọc và tính trung bình từng bạn
with open("diem.txt", "r", encoding="utf-8") as f:
    for dong in f:
        dong = dong.strip()                # bỏ ký tự xuống dòng
        if not dong:                       # bỏ qua dòng trống
            continue
        phan = dong.split(",")             # tách cột
        ten = phan[0]                      # cột 1: tên
        diem = [float(x) for x in phan[1:]]  # các cột còn lại: điểm
        tb = sum(diem) / len(diem)
        print(f"{ten}: {tb:.2f}")
```

**Giải thích code:**
* `phan[1:]` — lấy từ cột 2 đến hết (3 điểm).
* `float(x)` — chuyển chuỗi `"8.5"` thành số 8.5; thiếu bước này sẽ lỗi phép tính.
* `{tb:.2f}` — in làm tròn 2 chữ số thập phân.

**Độ phức tạp:** O(n) với n học sinh.

---

### Bài 9: Bắt lỗi file không tồn tại

**Phân tích:** Đọc file chưa tồn tại sẽ ném `FileNotFoundError` — cần chặn để chương trình không sập.

**Ý tưởng:** Bọc thao tác mở file trong `try`, bắt lỗi trong `except FileNotFoundError`.

**Thuật toán:**
1. `try:` mở `"khong_co.txt"` mode `"r"`.
2. Nếu mở được: đọc và in.
3. `except FileNotFoundError:` in thông báo thân thiện.

**Code:**

```python
try:
    # File này KHÔNG tồn tại trong thư mục — thử đọc sẽ lỗi
    with open("khong_co.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("File khong ton tai! Hay kiem tra lai ten file.")

print("Chuong trinh van chay tiep binh thuong.")   # minh chứng không sập
```

**Giải thích code:**
* Khi mở thất bại, `with` cũng chưa kịp chạy — lỗi bị `except` hứng ngay.
* Không có `try/except`, chương trình in lỗi đỏ và dừng đột ngột.

**Độ phức tạp:** O(1).

---

### Bài 10: Nhật ký đơn giản

**Phân tích:** Nhật ký phải giữ lịch sử → mode `"a"`; mỗi dòng kèm thời gian.

**Ý tưởng:** Hàm `ghi_log` dùng `datetime.now()` lấy giờ, ghi dòng `[giờ] sự kiện`.

**Thuật toán:**
1. `from datetime import datetime`.
2. Hàm `ghi_log`: lấy giờ hiện tại, `with` + `"a"` ghi một dòng.
3. Gọi 3 lần, đọc lại và in.

**Code:**

```python
from datetime import datetime

def ghi_log(thong_diep):
    """Ghi một dòng nhật ký kèm thời gian."""
    gio = datetime.now().strftime("%H:%M:%S")
    with open("nhat_ky.txt", "a", encoding="utf-8") as f:
        f.write(f"[{gio}] {thong_diep}\n")

# Gọi hàm 3 lần với các sự kiện mẫu
ghi_log("Chuong trinh khoi dong")
ghi_log("Xu ly du lieu")
ghi_log("Ket thuc")

# Đọc lại và in
with open("nhat_ky.txt", "r", encoding="utf-8") as f:
    print(f.read(), end="")
```

**Giải thích code:**
* `strftime("%H:%M:%S")` — định dạng giờ:phút:giây (kiến thức Bài 20).
* Mode `"a"` — mỗi lần chạy lại, log cũ vẫn còn, dòng mới thêm vào cuối.
* Tách hàm `ghi_log` giúp gọi lại nhiều nơi trong chương trình.

**Độ phức tạp:** O(1) mỗi lần ghi.

---

### Bài 11: Đếm dòng và chữ

**Phân tích:** Dòng đếm bằng vòng lặp; từ trong mỗi dòng đếm bằng `split()`.

**Ý tưởng:** Đếm biến chạy; `len(dong.split())` = số từ của một dòng.

**Thuật toán:**
1. Tạo file 3 câu ngắn (tổng 6 từ).
2. Với mỗi dòng: `so_dong += 1`; `so_tu += len(dong.split())`.
3. In kết quả.

**Code:**

```python
# Tạo file văn bản mẫu: 3 dòng, mỗi dòng 2 từ → tổng 6 từ
with open("van_ban.txt", "w", encoding="utf-8") as f:
    f.write("Python la\n")
    f.write("ngon ngu\n")
    f.write("de hoc\n")

so_dong = 0
so_tu = 0

with open("van_ban.txt", "r", encoding="utf-8") as f:
    for dong in f:
        dong = dong.strip()
        if not dong:            # dòng trống không tính
            continue
        so_dong += 1
        so_tu += len(dong.split())

print("So dong:", so_dong)
print("So tu:", so_tu)
```

**Giải thích code:**
* `dong.split()` — tách chuỗi theo khoảng trắng: `"Python la"` → `["Python", "la"]` = 2 từ.
* Ba dòng × 2 từ = 6 từ; ba dòng = 3 dòng.
* Biến đếm phải khai báo **trước** vòng lặp, nếu không sẽ báo `NameError`.

**Độ phức tạp:** O(n) với n ký tự file.

---

### Bài 12: Bảng cửu chương ra file

**Phân tích:** Sinh 10 dòng bằng vòng lặp rồi ghi file; đọc lại để kiểm chứng.

**Ý tưởng:** `for i in range(1, 11)` + `write(f"5 x {i} = {5*i}\n")`.

**Thuật toán:**
1. Mở `"w"`, vòng lặp ghi 10 dòng.
2. Mở `"r"`, in toàn bộ.

**Code:**

```python
# Ghi bảng cửu chương nhân 5 vào file
with open("bang_5.txt", "w", encoding="utf-8") as f:
    for i in range(1, 11):
        f.write(f"5 x {i} = {5 * i}\n")

# Đọc lại và in
with open("bang_5.txt", "r", encoding="utf-8") as f:
    print(f.read(), end="")
```

**Giải thích code:**
* `range(1, 11)` — 10 lần lặp từ 1 đến 10.
* `f"5 x {i} = {5 * i}"` — Python tính sẵn `5 * i` rồi chèn vào chuỗi.
* Kết quả dòng cuối: `5 x 10 = 50`.

**Độ phức tạp:** O(1) — số dòng cố định 10.

---

### Bài 13: Tìm kiếm trong file

**Phân tích:** Đọc từng dòng và lọc theo điều kiện chứa chuỗi con.

**Ý tưởng:** `if "An" in dong` — kiểm tra chuỗi con (kiến thức Bài 18).

**Thuật toán:**
1. Tạo file 4 tên, trong đó 2 tên chứa "An".
2. Duyệt từng dòng; nếu chứa `"An"` thì in ra.
3. Bỏ qua `\n` khi in.

**Code:**

```python
# Tạo danh sách lớp
with open("lop.txt", "w", encoding="utf-8") as f:
    f.write("Nguyen Van An\n")
    f.write("Tran Binh\n")
    f.write("Pham Thi Anh\n")
    f.write("Le Cuong\n")

# Tìm các bạn có tên chứa "An"
with open("lop.txt", "r", encoding="utf-8") as f:
    for dong in f:
        if "An" in dong:                 # kiểm tra chuỗi con
            print("Tim thay:", dong.strip())
```

**Giải thích code:**
* `"An" in "Pham Thi Anh"` → `True` vì chuỗi con "An" xuất hiện trong tên.
* `"An" in "Tran Binh"` → `False` (chữ "An" không khớp giữa chữ "Binh").
* `.strip()` xóa `\n` thừa khi in.

**Độ phức tạp:** O(n × m) với n dòng, m độ dài chuỗi trung bình.

---

### Bài 14: Xóa dòng trống

**Phân tích:** File có dòng trống; khi ghi file mới chỉ giữ dòng có nội dung.

**Ý tưởng:** Sau `strip()`, chuỗi rỗng nghĩa là dòng trống → `continue`.

**Thuật toán:**
1. Tạo file `lo_xinh.txt`: "Dong 1", "Dong 2", "" (trống), "Dong 4".
2. Đọc từng dòng; dòng sau `strip()` rỗng thì bỏ qua.
3. Ghi các dòng hợp lệ vào `sach.txt` (mode `"w"`).
4. Đọc lại và in.

**Code:**

```python
# Tạo file có chứa một dòng trống ở giữa
with open("lo_xinh.txt", "w", encoding="utf-8") as f:
    f.write("Dong 1\n")
    f.write("Dong 2\n")
    f.write("\n")                     # dòng trống
    f.write("Dong 4\n")

# Đọc và chỉ ghi những dòng có nội dung
with open("lo_xinh.txt", "r", encoding="utf-8") as f_doc, \
     open("sach.txt", "w", encoding="utf-8") as f_ghi:
    for dong in f_doc:
        dong = dong.strip()
        if not dong:                  # dòng trống -> bỏ qua
            continue
        f_ghi.write(dong + "\n")

# In nội dung file đã làm sạch
with open("sach.txt", "r", encoding="utf-8") as f:
    print(f.read(), end="")
```

**Giải thích code:**
* Mở **2 file cùng lúc** trong một `with` (ngăn cách bằng dấu phẩy) — đọc file nguồn, ghi file đích.
* `if not dong` — chuỗi rỗng mang giá trị `False`, dòng trống bị bỏ.
* Dấu `\` cuối dòng giúp tách câu lệnh dài sang dòng mới.

**Độ phức tạp:** O(n) với n ký tự file.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Nâng điểm cho học sinh

**Phân tích:** Quy trình "đọc → sửa → ghi lại" là cách phổ biến để cập nhật file.

**Ý tưởng:** Đọc vào list, điều chỉnh điểm, mở lại với `"w"` ghi toàn bộ.

**Thuật toán:**
1. Tạo `diem.txt` 4 dòng `Ten,Toan`.
2. Đọc vào list các chuỗi; tách điểm, nếu < 9.0 thì +2 (tối đa 10).
3. Ghi lại toàn bộ với `"w"`.
4. Đọc lại và in.

**Code:**

```python
# Tạo file điểm mẫu
with open("diem.txt", "w", encoding="utf-8") as f:
    f.write("An,5.5\n")
    f.write("Binh,3.0\n")
    f.write("Cuong,8.5\n")
    f.write("Dung,4.0\n")

# Bước 1: đọc toàn bộ vào list
danh_sach = []
with open("diem.txt", "r", encoding="utf-8") as f:
    for dong in f:
        danh_sach.append(dong.strip())

# Bước 2: sửa điểm trong list
for i in range(len(danh_sach)):
    ten, diem = danh_sach[i].split(",")
    diem = float(diem)
    if diem < 9.0:                     # nâng điểm cho mọi bạn dưới 9
        diem = min(diem + 2, 10.0)     # cộng 2 nhưng không quá 10
    danh_sach[i] = f"{ten},{diem:.1f}"

# Bước 3: ghi lại toàn bộ (mode "w" — ghi đè file cũ)
with open("diem.txt", "w", encoding="utf-8") as f:
    for dong in danh_sach:
        f.write(dong + "\n")

# Bước 4: đọc lại kiểm chứng
print("Sau khi nang diem:")
with open("diem.txt", "r", encoding="utf-8") as f:
    print(f.read(), end="")
```

**Giải thích code:**
* `diem = min(diem + 2, 10.0)` — cộng 2 nhưng giới hạn ở 10 (hàm `min` lấy giá trị nhỏ hơn).
* `{diem:.1f}` — luôn in 1 chữ số thập phân (`5.0`, `10.0`) cho cột điểm đều đẹp.
* Ghi lại bằng `"w"` — nội dung mới thay thế hoàn toàn nội dung cũ.
* Kết quả: An 5.5→7.5, Binh 3.0→5.0, Cuong 8.5→10.0, Dung 4.0→6.0.

**Độ phức tạp:** O(n) với n học sinh.

---

### Bài 16: Ghép hai file

**Phân tích:** Ghép nội dung 2 file thành 1; đếm tổng số dòng.

**Ý tưởng:** Đọc từng file vào list, gộp list, ghi một lần.

**Thuật toán:**
1. Tạo 2 file, mỗi file 2 tên.
2. Đọc cả hai vào 1 list.
3. Ghi list gộp vào `hs_ca_khoi.txt`.
4. In số lượng và nội dung.

**Code:**

```python
# Tạo 2 file lớp
with open("hs_10a.txt", "w", encoding="utf-8") as f:
    f.write("An\n")
    f.write("Binh\n")

with open("hs_10b.txt", "w", encoding="utf-8") as f:
    f.write("Cuong\n")
    f.write("Dung\n")

# Đọc cả hai file vào một list
danh_sach = []
for ten_file in ["hs_10a.txt", "hs_10b.txt"]:
    with open(ten_file, "r", encoding="utf-8") as f:
        for dong in f:
            if dong.strip():
                danh_sach.append(dong.strip())

# Ghi gộp vào file mới
with open("hs_ca_khoi.txt", "w", encoding="utf-8") as f:
    for ten in danh_sach:
        f.write(ten + "\n")

# Báo cáo kết quả
print("Tong so hoc sinh:", len(danh_sach))
with open("hs_ca_khoi.txt", "r", encoding="utf-8") as f:
    print(f.read(), end="")
```

**Giải thích code:**
* Vòng lặp `for ten_file in [...]` — xử lý nhiều file với cùng đoạn code, không lặp lại 2 lần.
* `if dong.strip()` — lọc luôn dòng trống khi đọc.
* Số học sinh = `len(danh_sach)` = 4.

**Độ phức tạp:** O(n) với n tổng số dòng hai file.

---

### Bài 17: Phân loại và ghi kết quả

**Phân tích:** Chuỗi xử lý khép kín: tạo dữ liệu → đọc → tính → ghi kết quả → in.

**Ý tưởng:** Tách riêng 2 file: file nguồn (điểm) và file kết quả (xếp loại).

**Thuật toán:**
1. Tạo `diem.txt` 3 học sinh, 4 cột.
2. Với mỗi dòng: tính TB, xếp loại theo 4 mốc.
3. Ghi `Ten: Loai` vào `xep_loai.txt` (`"w"`).
4. Đọc file kết quả và in.

**Code:**

```python
# Tạo file điểm mẫu
with open("diem.txt", "w", encoding="utf-8") as f:
    f.write("Nguyen Van An,8.5,7.0,9.0\n")
    f.write("Tran Thi Mai,6.0,6.5,7.0\n")
    f.write("Le Quang Binh,4.0,4.5,5.0\n")

def xep_loai(tb):
    """Xếp loại theo điểm trung bình."""
    if tb >= 8.0:
        return "Gioi"
    if tb >= 6.5:
        return "Kha"
    if tb >= 5.0:
        return "Trung binh"
    return "Yeu"

# Đọc, tính, ghi kết quả
with open("diem.txt", "r", encoding="utf-8") as f_doc, \
     open("xep_loai.txt", "w", encoding="utf-8") as f_ghi:
    for dong in f_doc:
        dong = dong.strip()
        if not dong:
            continue
        phan = dong.split(",")
        ten = phan[0]
        diem = [float(x) for x in phan[1:]]
        tb = sum(diem) / len(diem)
        f_ghi.write(f"{ten}: {xep_loai(tb)}\n")

# In kết quả
with open("xep_loai.txt", "r", encoding="utf-8") as f:
    print(f.read(), end="")
```

**Giải thích code:**
* Hàm `xep_loai` tách riêng giúp code dễ đọc, dễ kiểm tra.
* An TB 8.17 → Gioi; Mai TB 6.50 → Kha; Binh TB 4.50 → Yeu.
* Ghi và đọc dùng 2 `with` riêng: ghi xong đóng, rồi mới đọc lại.

**Độ phức tạp:** O(n) với n học sinh.

---

### Bài 18: Sổ tay ghi chú

**Phân tích:** List ghi chú được ghi nguyên khối bằng `writelines`, đọc lại để báo cáo.

**Ý tưởng:** Chuẩn bị sẵn list chuỗi có dấu `-` và `\n`, ghi 1 lần.

**Thuật toán:**
1. Tạo list 3 ghi chú dạng `"- ...\n"`.
2. `writelines` ghi vào `so_tay.txt`.
3. Đọc lại, in số ghi chú và từng ghi chú.

**Code:**

```python
# Danh sách ghi chú trong chương trình
ghi_chu = [
    "- Mua sach Python\n",
    "- Lam bai tap bai 22\n",
    "- On lai bai 21\n",
]

# Ghi toàn bộ vào file
with open("so_tay.txt", "w", encoding="utf-8") as f:
    f.writelines(ghi_chu)

# Đọc lại và báo cáo
with open("so_tay.txt", "r", encoding="utf-8") as f:
    danh_sach = f.readlines()

print("So ghi chu:", len(danh_sach))
for dong in danh_sach:
    print(dong.strip())
```

**Giải thích code:**
* `writelines` ghi cả list liền mạch — mỗi phần tử đã sẵn `\n` nên tự tách dòng.
* `readlines()` đọc lại đúng thành list 3 phần tử.
* `.strip()` bỏ `\n` khi in.

**Độ phức tạp:** O(n) với n ký tự.

---

### Bài 19: Nhật ký lỗi

**Phân tích:** Vừa ghi log, vừa lọc log — hai kỹ năng kết hợp trong một bài.

**Ý tưởng:** Hàm `ghi_log` ghi mọi sự kiện; khi đọc lại, lọc dòng chứa `"LOI"`.

**Thuật toán:**
1. Hàm `ghi_log` dùng `"a"` + encoding.
2. Ghi 3 sự kiện: 2 thường + 1 lỗi.
3. Đọc lại, chỉ in dòng chứa `"LOI"`.

**Code:**

```python
from datetime import datetime

def ghi_log(thong_diep):
    """Ghi một dòng nhật ký kèm thời gian."""
    gio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("nhat_ky.txt", "a", encoding="utf-8") as f:
        f.write(f"[{gio}] {thong_diep}\n")

# Mô phỏng 3 sự kiện
ghi_log("Mo file thanh cong")
ghi_log("LOI: File diem.txt khong doc duoc")
ghi_log("Ket thuc chuong trinh")

# Đọc lại và chỉ in các dòng lỗi
with open("nhat_ky.txt", "r", encoding="utf-8") as f:
    for dong in f:
        if "LOI" in dong:
            print(dong.strip())
```

**Giải thích code:**
* Mọi sự kiện đều được ghi đầy đủ vào nhật ký — chỉ khi đọc mới lọc.
* `if "LOI" in dong` — lọc dòng có chuỗi con "LOI".
* Cách này giúp log đầy đủ mà báo cáo lỗi vẫn gọn gàng.

**Độ phức tạp:** O(1) mỗi lần ghi; O(n) khi quét toàn file.

---

### Bài 20: Quản lý điểm lưu file (tiểu dự án)

**Phân tích:** Bài tổng hợp toàn bộ: tạo file, đọc an toàn (bắt lỗi), tính toán, ghi kết quả, báo cáo.

**Ý tưởng:** Chia 4 bước rõ ràng, mỗi bước một khối `with` riêng.

**Thuật toán:**
1. Tạo `quan_ly_diem.txt` với 4 học sinh.
2. Đọc file trong `try/except` → tính TB và xếp loại.
3. Ghi bảng tổng kết vào `tong_ket.txt`.
4. In bảng tổng kết + dòng xác nhận.

**Code:**

```python
def xep_loai(tb):
    """Xếp loại theo điểm trung bình."""
    if tb >= 8.0:
        return "Gioi"
    if tb >= 6.5:
        return "Kha"
    if tb >= 5.0:
        return "Trung binh"
    return "Yeu"

# Bước 1: tạo dữ liệu mẫu
with open("quan_ly_diem.txt", "w", encoding="utf-8") as f:
    f.write("Nguyen Van An,8.5,7.0,9.0\n")
    f.write("Tran Thi Mai,6.0,6.5,7.0\n")
    f.write("Le Quang Binh,4.5,5.0,5.5\n")
    f.write("Pham Thu Ha,9.0,8.5,8.0\n")

# Bước 2: đọc file an toàn và tính điểm
ket_qua = []
try:
    with open("quan_ly_diem.txt", "r", encoding="utf-8") as f:
        for dong in f:
            dong = dong.strip()
            if not dong:
                continue
            phan = dong.split(",")
            ten = phan[0]
            diem = [float(x) for x in phan[1:]]
            tb = sum(diem) / len(diem)
            ket_qua.append(f"{ten} - {tb:.2f} - {xep_loai(tb)}")
except FileNotFoundError:
    print("File quan_ly_diem.txt khong ton tai!")

# Bước 3: ghi bảng tổng kết
with open("tong_ket.txt", "w", encoding="utf-8") as f:
    for dong in ket_qua:
        f.write(dong + "\n")

# Bước 4: in ra màn hình
for dong in ket_qua:
    print(dong)
print("Da ghi ket qua vao tong_ket.txt")
```

**Giải thích code:**
* Bước 2 nằm trong `try/except` — nếu file bị xóa mất, chương trình báo lỗi mà không sập.
* `ket_qua` là list chuỗi đã định dạng sẵn — vừa để ghi file, vừa để in ra.
* Mỗi bước một `with` riêng: tạo → đọc → ghi → in, trình tự rõ ràng.

**Độ phức tạp:** O(n) với n học sinh.

---

## 📌 Lời khuyên cuối

* Công thức bất biến: `with open(ten, mode, encoding="utf-8") as f:` — đủ 3 thành phần mới chuẩn.
* Muốn giữ dữ liệu cũ → `"a"`; muốn thay mới → `"w"`; chỉ đọc → `"r"`.
* File do người dùng đặt tên → luôn bọc trong `try/except FileNotFoundError`.
* Đọc từng dòng nhớ `.strip()` và bỏ qua dòng trống.
* Bài sau đã sẵn sàng: gói dữ liệu học sinh, điểm số thành **class** với lập trình hướng đối tượng!

👉 Tiếp theo: **[Bài 23: Lập Trình Hướng Đối Tượng](../23_OOP/bai_giang.md)**
