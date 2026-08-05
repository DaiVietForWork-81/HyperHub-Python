# ✅ Bài 13: Đáp Án – Phạm Vi Biến (Scope)

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án để việc học hiệu quả nhất.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Biến trong hàm là local

**Phân tích:** Minh chứng trực quan rằng biến tạo trong hàm không tồn tại ngoài hàm.

**Ý tưởng:** In biến trong hàm thành công; in ngoài hàm sẽ lỗi `NameError` — dùng comment để ghi chú thay vì để chương trình chết.

**Thuật toán:**
1. Định nghĩa hàm tạo biến local và in.
2. Gọi hàm.
3. Thử in biến ở ngoài (kèm comment giải thích lỗi).

**Code:**

```python
def in_so():
    so = 42               # so là biến LOCAL của in_so
    print("So trong ham:", so)

in_so()
# print(so)  # ❌ Bỏ comment dòng này sẽ lỗi NameError:
#            #    name 'so' is not defined (biến đã "chết" khi hết hàm)
```

**Giải thích code:**
* `so = 42` nằm trong hàm → local, tồn tại khi hàm chạy.
* Khi hàm kết thúc, `so` biến mất — in ngoài hàm là lỗi.

**Độ phức tạp:** O(1).

---

### Bài 2: Đọc biến global trong hàm

**Phân tích:** Hàm chỉ đọc biến global — hành vi mặc định, không cần khai báo.

**Ý tưởng:** Dùng `phi_phuc_vu` trực tiếp trong biểu thức trả về.

**Thuật toán:**
1. Khai báo biến global.
2. Viết hàm dùng biến đó.
3. Gọi và in.

**Code:**

```python
phi_phuc_vu = 5000     # biến global

def tong_tien(mon):
    """Tính tiền món ăn cộng phí phục vụ."""
    return mon * 30000 + phi_phuc_vu

print(tong_tien(2))    # 2 * 30000 + 5000 = 65000
```

**Giải thích code:**
* Không có lệnh gán `phi_phuc_vu` trong hàm → Python tìm ở global và đọc được.
* Kết quả `65000`.

**Độ phức tạp:** O(1).

---

### Bài 3: Hàm gán biến — có sửa global không?

**Phân tích:** Gán biến trong hàm tạo local mới — global giữ nguyên.

**Ý tưởng:** `x = 99` trong hàm là biến local; in `x` ngoài hàm vẫn ra `10`.

**Thuật toán:**
1. Khai báo `x = 10`.
2. Hàm gán `x = 99` (không `global`).
3. Gọi hàm, in `x`.

**Code:**

```python
x = 10

def doi_x():
    x = 99    # local — chỉ tồn tại trong hàm
    print("x trong ham:", x)

doi_x()
print(x)      # vẫn 10
```

**Giải thích code:**
* Hai biến `x` khác nhau: local trong hàm và global ngoài.
* Lệnh gán trong hàm không bao giờ chạm tới biến global.

**Độ phức tạp:** O(1).

---

### Bài 4: Dùng từ khóa `global`

**Phân tích:** Cần sửa biến global từ trong hàm → khai báo `global`.

**Ý tưởng:** `global so_lan` cho phép `so_lan += 1` chạm đúng biến toàn cục.

**Thuật toán:**
1. Khai báo `so_lan = 0`.
2. Hàm khai báo `global` rồi tăng biến.
3. Gọi 3 lần.

**Code:**

```python
so_lan = 0

def lap_mot_lan():
    global so_lan
    so_lan += 1
    print(f"Lan lap: {so_lan}")

lap_mot_lan()
lap_mot_lan()
lap_mot_lan()
```

**Giải thích code:**
* Dòng `global so_lan` phải đặt **trước** khi dùng.
* Mỗi lần gọi, biến global tăng thêm 1 và giữ giá trị giữa các lần gọi.

**Độ phức tạp:** O(1).

---

### Bài 5: Trả về thay vì global

**Phân tích:** Cách "sạch" không cần `global`: dữ liệu vào qua tham số, ra qua `return`.

**Ý tưởng:** Gán kết quả trả về cho biến ngoài: `n = cong_mot(n)`.

**Thuật toán:**
1. Viết hàm `cong_mot(so)` trả về `so + 1`.
2. Khởi tạo `n = 0`.
3. Gán `n = cong_mot(n)` ba lần, in `n`.

**Code:**

```python
def cong_mot(so):
    """Trả về số đã cộng thêm 1."""
    return so + 1

n = 0
n = cong_mot(n)   # 1
n = cong_mot(n)   # 2
n = cong_mot(n)   # 3
print(n)
```

**Giải thích code:**
* Hàm không sửa biến ngoài — nó **tính và trả về**.
* Việc cập nhật biến do nơi gọi tự quyết định → dễ hiểu, dễ kiểm thử.

**Độ phức tạp:** O(1).

---

### Bài 6: Tìm mức LEGB

**Phân tích:** Áp dụng LEGB: biến local có sẵn thì dùng ngay.

**Ý tưởng:** Trong `ham_trong`, biến `ten` local được gán `"L"` → in `"L"`.

**Thuật toán:**
1. Sao chép code vào file.
2. Chạy và quan sát.

**Code:**

```python
ten = "G"

def ham_ngoai():
    ten = "E"

    def ham_trong():
        ten = "L"
        print(ten)   # L — mức Local thắng

    ham_trong()

ham_ngoai()
```

**Giải thích code:**
* Python tìm `ten` theo LEGB: tìm thấy ở mức **Local** trước tiên nên không cần nhìn ra Enclosing hay Global.
* Ba biến tên `ten` ở 3 mức khác nhau — hoàn toàn độc lập.

**Độ phức tạp:** O(1).

---

### Bài 7: Hàm đọc biến global làm việc bình thường

**Phân tích:** Đọc global là hành vi mặc định.

**Ý tưởng:** `gia * (1 - giam_gia)` với `giam_gia` là biến global.

**Thuật toán:**
1. Khai báo `giam_gia = 0.2`.
2. Viết hàm tính giá sau giảm.
3. Gọi và in.

**Code:**

```python
giam_gia = 0.2     # biến global

def gia_sau_giam(gia):
    """Tính giá sau khi giảm theo hệ số global."""
    return gia * (1 - giam_gia)

print(gia_sau_giam(100000))   # 100000 * 0.8 = 80000.0
```

**Giải thích code:**
* Hàm chỉ đọc `giam_gia`, không gán → không cần `global`.
* Kết quả float `80000.0`.

**Độ phức tạp:** O(1).

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Trước hay sau? Không thay đổi được

**Phân tích:** Tham số của hàm cũng là biến local — gán lại bên trong không ảnh hưởng biến ngoài.

**Ý tưởng:** `x = 999` trong hàm ghi đè tham số local; `x` ngoài không đổi.

**Thuật toán:**
1. Khai báo `x = 5` ngoài.
2. Hàm nhận tham số `x`, gán `x = 999`, trả về.
3. In kết quả và biến ngoài.

**Code:**

```python
x = 5

def kho_dam(x):
    """Gán lại tham số rồi trả về."""
    x = 999
    return x

print(kho_dam(5))   # 999 — bên trong hàm
print(x)            # 5 — biến ngoài không đổi
```

**Giải thích code:**
* Tham số `x` là bản sao tên riêng trong hàm.
* Gán `x = 999` chỉ ảnh hưởng bản local.

**Độ phức tạp:** O(1).

---

### Bài 9: Đếm lượt mở ứng dụng

**Phân tích:** Kết hợp `global` với f-string để thông báo.

**Ý tưởng:** Tăng biến global rồi đọc giá trị mới để in.

**Thuật toán:**
1. Khai báo `so_luot_mo = 0`.
2. Hàm khai báo `global`, tăng, trả về chuỗi.
3. Gọi 2 lần, in tổng.

**Code:**

```python
so_luot_mo = 0

def mo_ung_dung():
    """Tăng số lượt mở và trả về thông báo."""
    global so_luot_mo
    so_luot_mo += 1
    return f"Da mo ung dung lan thu {so_luot_mo}"

print(mo_ung_dung())
print(mo_ung_dung())
print("Tong so luot mo:", so_luot_mo)
```

**Giải thích code:**
* Sau hai lần gọi, `so_luot_mo = 2` — giá trị tồn tại giữa các lần gọi nhờ `global`.

**Độ phức tạp:** O(1).

---

### Bài 10: Sửa lỗi UnboundLocalError

**Phân tích:** `diem += 1` là phép gán → Python coi `diem` là local → lỗi khi đọc trước khi gán.

**Ý tưởng:** Sửa bằng `global` — cách trực tiếp nhất với bài này.

**Thuật toán:**
1. Thêm `global diem` vào đầu hàm.
2. Chạy và in.

**Code:**

```python
diem = 10

def tang_diem():
    global diem
    diem += 1

tang_diem()
print(diem)   # 11
```

**Giải thích code:**
* `global diem` báo Python: dùng biến toàn cục, đừng tạo local.
* Cách khác: `return diem + 1` rồi `diem = tang_diem()` — cũng đúng và "sạch" hơn.

**Độ phức tạp:** O(1).

---

### Bài 11: Vì sao lỗi? Giải thích bằng comment

**Phân tích:** Biến chỉ được gán trong một nhánh `if` — khi nhánh không chạy, biến chưa tồn tại.

**Ý tưởng:** Chạy với `flag = False` để thấy lỗi, ghi chú nguyên nhân.

**Thuật toán:**
1. Định nghĩa hàm như đề.
2. Gọi với `flag = False`.
3. Nhận xét lỗi qua comment.

**Code:**

```python
def ham_lu(flag):
    if flag:
        gia_tri = 1          # gia_tri chỉ được tạo khi flag = True
    return gia_tri           # ❌ khi flag = False, biến chưa tồn tại
    # → UnboundLocalError: local variable 'gia_tri' referenced before assignment

# ham_lu(False)  # Bỏ comment để thấy lỗi
```

**Giải thích code:**
* Không phải lỗi scope mặc định — là biến **chưa được gán lần nào** khi `flag = False`.
* Cách khắc phục: gán `gia_tri = 0` trước `if`.

**Độ phức tạp:** O(1).

---

### Bài 12: Hàm lồng nhau không dùng nonlocal

**Phân tích:** Hàm trong gán biến của hàm ngoài → bắt buộc `nonlocal`.

**Ý tưởng:** Đầu tiên chạy bản lỗi để thấy `UnboundLocalError`, sau đó thêm `nonlocal`.

**Thuật toán:**
1. Viết bản chưa có `nonlocal`, chạy thử.
2. Thêm `nonlocal n`.
3. Gọi hàm trong 2 lần, in `n`.

**Code:**

```python
def dem_ngoai():
    n = 0

    def dem_trong():
        nonlocal n     # cho phép sửa biến n của hàm ngoài
        n = n + 1

    dem_trong()
    dem_trong()
    print(n)           # 2

dem_ngoai()
```

**Giải thích code:**
* Không có `nonlocal`: `n = n + 1` tạo biến local mới trong `dem_trong` → `UnboundLocalError`.
* Có `nonlocal`: Python hiểu `n` là biến của `dem_ngoai` và sửa đúng nó.

**Độ phức tạp:** O(1).

---

### Bài 13: Tách biến global — đặt tên khác

**Phân tích:** Tránh nhầm lẫn bằng cách đặt tên local khác — không cần `global`.

**Ý tưởng:** Dùng `tong_local` cho biến cục bộ, giữ `tong` cho biến toàn cục.

**Thuật toán:**
1. Khai báo `tong = 100`.
2. Hàm dùng `tong_local`.
3. In cả hai.

**Code:**

```python
tong = 100

def tinh_tong_cuc_bo(a, b):
    tong_local = a + b    # tên khác → không đụng biến global
    return tong_local

print(tinh_tong_cuc_bo(7, 8))   # 15
print(tong)                     # 100
```

**Giải thích code:**
* Đặt tên khác biệt giúp code rõ ràng, tránh tưởng lầm hai biến liên quan nhau.

**Độ phức tạp:** O(1).

---

### Bài 14: Hóa đơn cửa hàng — tổng hợp scope

**Phân tích:** Kết hợp đọc global (`thue`) và gán local (`giam_them`).

**Ý tưởng:** Tính giá sau giảm rồi cộng thuế.

**Thuật toán:**
1. Khai báo `thue = 0.1` global.
2. Hàm tính `giam_them` theo điều kiện.
3. Trả về giá sau giảm × (1 + thuế).

**Code:**

```python
thue = 0.1     # biến global — hàm chỉ đọc

def thanh_toan(gia_goc):
    """Tính tiền phải trả sau giảm giá và cộng thuế."""
    if gia_goc >= 100000:
        giam_them = 0.05          # local
    else:
        giam_them = 0             # local
    gia_sau_giam = gia_goc * (1 - giam_them)
    return round(gia_sau_giam * (1 + thue))

print(thanh_toan(120000))   # 120000 * 0.95 * 1.1 = 125400
print(thanh_toan(50000))    # 50000 * 1.1 = 55000
```

**Giải thích code:**
* `thue` đọc tự do vì hàm không gán nó.
* `giam_them`, `gia_sau_giam` là local — không ảnh hưởng ngoài hàm.

**Độ phức tạp:** O(1).

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Máy rút tiền — lỗi kinh điển

**Phân tích:** `so_du -= tien` là phép gán → lỗi `UnboundLocalError`; phải `global`.

**Ý tưởng:** Thêm `global so_du` để hàm cập nhật đúng biến toàn cục.

**Thuật toán:**
1. Khai báo `so_du = 100000`.
2. Thêm `global so_du` trong hàm `rut`.
3. Gọi và in số dư.

**Code:**

```python
so_du = 100000

def rut(tien):
    """Rút tiền, cập nhật số dư toàn cục."""
    global so_du
    so_du -= tien
    return so_du

rut(20000)
print(so_du)   # 80000
```

**Giải thích code:**
* `so_du -= tien` ⟺ `so_du = so_du - tien` — có gán nên cần `global`.
* Sau khi sửa, biến global thực sự bị giảm.

**Độ phức tạp:** O(1).

---

### Bài 16: So sánh 2 cách cộng dồn

**Phân tích:** Hai phong cách: dùng `global` và dùng tham số + `return`.

**Ý tưởng:** Viết cả hai, cùng kết quả `6`, ghi chú đánh giá.

**Thuật toán:**
1. Cách (a): biến global, hàm dùng `global`.
2. Cách (b): hàm thuần, gán lại kết quả.
3. In kết quả hai cách.

**Code:**

```python
# Cách (a): dùng global — hàm gắn với trạng thái ngoài
n_a = 0

def cong_global(so):
    global n_a
    n_a += so

cong_global(2)
cong_global(2)
cong_global(2)
print("Cach global:", n_a)

# Cách (b): tham số vào - return ra — hàm độc lập, dễ kiểm thử
n_b = 0

def cong_thuan(so_hien_tai, them):
    return so_hien_tai + them

n_b = cong_thuan(n_b, 2)
n_b = cong_thuan(n_b, 2)
n_b = cong_thuan(n_b, 2)
print("Cach return:", n_b)
```

**Giải thích code:**
* Cách (b) đọc "sạch" hơn: dữ liệu đi vào – kết quả đi ra rõ ràng.
* Cách (a) ngắn hơn nhưng khó theo dõi khi nhiều hàm cùng dùng biến.

**Độ phức tạp:** O(1).

---

### Bài 17: Đếm số lần gọi hàm — dùng nonlocal

**Phân tích:** "Đóng gói" biến đếm bên trong hàm ngoài — kỹ thuật closure.

**Ý tưởng:** `tao_bo_dem()` trả về hàm `goi()`; `nonlocal lan` cho phép gọi nhiều lần liên tiếp.

**Thuật toán:**
1. Hàm ngoài khai báo `lan = 0`.
2. Hàm trong dùng `nonlocal lan`, tăng, in, trả về.
3. Gán hàm trong vào `bo_dem` và gọi 3 lần.

**Code:**

```python
def tao_bo_dem():
    """Trả về một hàm đếm có bộ nhớ riêng."""
    lan = 0

    def goi():
        nonlocal lan
        lan += 1
        print(f"Lan goi thu: {lan}")
        return lan

    return goi

bo_dem = tao_bo_dem()
bo_dem()
bo_dem()
bo_dem()
```

**Giải thích code:**
* `lan` chỉ tồn tại trong `tao_bo_dem` và được hàm `goi` "nhớ".
* Mỗi lần `bo_dem()` chạy, `lan` tăng 1 — như một bộ đếm riêng biệt.

**Độ phức tạp:** O(1).

---

### Bài 18: Game đoán số — tổng hợp global

**Phân tích:** Cộng trừ điểm vào biến global qua hàm.

**Ý tưởng:** `dung_sai=True` → +10, ngược lại -5, dùng `global`.

**Thuật toán:**
1. Khai báo `diem = 0`.
2. Hàm kiểm tra `dung_sai`, cập nhật `diem`.
3. Mô phỏng 3 ván, in điểm cuối.

**Code:**

```python
diem = 0

def choi_mot_van(dung_sai):
    """Cộng 10 nếu đúng, trừ 5 nếu sai."""
    global diem
    if dung_sai:
        diem += 10
        return "Dung! +10 diem"
    diem -= 5
    return "Sai! -5 diem"

print(choi_mot_van(True))
print(choi_mot_van(False))
print(choi_mot_van(True))
print("Diem cuoi:", diem)   # 10 - 5 + 10 = 15
```

**Giải thích code:**
* Điểm tích lũy qua nhiều ván nhờ biến global.
* Điểm cuối: `10 - 5 + 10 = 15`.

**Độ phức tạp:** O(1).

---

### Bài 19: Nhiều hàm cùng chia sẻ biến — cảnh giác

**Phân tích:** Hai hàm cùng sửa một biến global; cần kiểm tra số dư trước khi trừ.

**Ý tưởng:** `nap` cộng, `tieu` kiểm tra rồi trừ.

**Thuật toán:**
1. Khai báo `quy = 1000`.
2. `nap(tien)`: cộng dồn.
3. `tieu(tien)`: nếu đủ thì trừ, ngược lại báo lỗi.
4. Gọi theo kịch bản, in quỹ.

**Code:**

```python
quy = 1000

def nap(tien):
    """Nạp tiền vào quỹ chung."""
    global quy
    quy += tien

def tieu(tien):
    """Tiêu tiền từ quỹ, chặn khi không đủ."""
    global quy
    if tien > quy:
        return "Khong du tien!"
    quy -= tien
    return "Da tieu " + str(tien)

nap(500)
print("Quy:", quy)             # 1500
print(tieu(200))               # Da tieu 200
print("Quy:", quy)             # 1300
print(tieu(2000))              # Khong du tien!
print("Quy:", quy)             # vẫn 1300
```

**Giải thích code:**

```python
# (Nhắc lại phần lõi để giải thích rõ hơn)
quy = 1000

def nap(tien):
    global quy
    quy += tien

def tieu(tien):
    global quy
    if tien > quy:
        return "Khong du tien!"
    quy -= tien
    return "Da tieu " + str(tien)

nap(500)
print("Quy:", quy)             # 1500
print(tieu(200))
print("Quy:", quy)             # 1300
print(tieu(2000))              # Khong du tien!
print("Quy:", quy)             # vẫn 1300
```

**Giải thích code:**
* `tieu` kiểm tra đủ tiền trước khi trừ → quỹ không bao giờ âm.
* Cả hai hàm phải khai báo `global quy` để cùng thao tác một biến.

**Độ phức tạp:** O(1).

---

### Bài 20: Dự đoán kết quả chương trình

**Phân tích:** Vận dụng đủ LEGB + nonlocal.

**Ý tưởng:** `g()` sửa `y` qua `nonlocal` trả về 3; `f()` cộng thêm `x` global = 4.

**Thuật toán:**
1. Phân tích từng hàm.
2. Chạy để đối chiếu.

**Code:**

```python
x = 1                    # G: global

def f():
    y = 2                # E: enclosing với g

    def g():
        nonlocal y       # sửa y của f
        y += 1           # y = 3
        return y         # 3

    return g() + x       # 3 + x(global = 1) = 4

print(f())               # 4
print(x)                 # 1 — x không bao giờ bị sửa
```

**Giải thích code:**
* `g()` → `y = 2 + 1 = 3`, trả về 3.
* `f()` → `3 + x`. `x` không có ở Local/Enclosing → tìm ở Global thấy `1`.
* Kết quả: `4`, và `x` vẫn nguyên `1` vì không hàm nào gán nó.

**Độ phức tạp:** O(1).

---

## 📌 Lời khuyên cuối

* **Gán trong hàm = tạo local** — ghi nhớ câu này để tránh 90% lỗi scope.
* **`global` chỉ dùng khi hàm phải CẬP NHẬT biến toàn cục** — đọc thì không cần.
* **`nonlocal` chỉ xuất hiện trong hàm lồng nhau** — dùng đúng ngữ cảnh.
* **Ưu tiên tham số + `return`** — hàm độc lập, dễ kiểm thử, dễ tái sử dụng.

👉 Tiếp theo: **[Bài 14: List](../14_List/bai_giang.md)**
