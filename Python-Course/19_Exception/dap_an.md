# ✅ Bài 19: Đáp Án – Ngoại Lệ (Exception)

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án để việc học hiệu quả nhất.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Bắt lỗi chia cho 0

**Phân tích:** Phép chia cho 0 luôn ném `ZeroDivisionError`; cần giữ chương trình chạy tiếp.

**Ý tưởng:** Đặt phép chia trong `try`, bắt lỗi bằng `except`.

**Thuật toán:**
1. Đặt `10 / 0` trong `try`.
2. `except ZeroDivisionError` in thông báo.
3. In dòng kết thúc (ngoài try — chứng tỏ chương trình không chết).

**Code:**

```python
try:
    ket_qua = 10 / 0          # ném ZeroDivisionError
except ZeroDivisionError:
    print("Khong the chia cho 0!")

# Ngoài try/except: vẫn chạy bình thường
print("Chuong trinh van chay tiep")
```

**Giải thích code:**
* `10 / 0` bên trong `try` — lỗi bị "bắt" thay vì làm sập chương trình.
* `except ZeroDivisionError` — bắt đúng loại lỗi chia cho 0.
* Dòng `print` cuối ngoài khối try — chạy bình thường.

**Độ phức tạp:** O(1).

---

### Bài 2: Bắt lỗi nhập sai kiểu

**Phân tích:** `int("abc")` không chuyển được → `ValueError`.

**Ý tưởng:** Bắt `ValueError` trong khối `except`.

**Thuật toán:**
1. Gọi `int("abc")` trong `try`.
2. Bắt `ValueError`, in thông báo.

**Code:**

```python
try:
    so = int("abc")           # không chuyển được -> ValueError
except ValueError:
    print("Khong phai so nguyen!")
```

**Giải thích code:**
* `int("abc")` ném `ValueError` vì "abc" không phải số.
* `except ValueError` bắt và in thông báo thân thiện.

**Độ phức tạp:** O(1).

---

### Bài 3: Bắt lỗi chỉ số ngoài phạm vi

**Phân tích:** List có 3 phần tử nhưng truy cập vị trí 5.

**Ý tưởng:** Bắt `IndexError`.

**Thuật toán:**
1. Tạo list 3 phần tử.
2. Truy cập `ds[5]` trong `try`.
3. Bắt `IndexError` và in thông báo.

**Code:**

```python
ds = [10, 20, 30]

try:
    phan_tu = ds[5]           # vượt quá chỉ số 0..2 -> IndexError
except IndexError:
    print("Chi so nam ngoai danh sach!")
```

**Giải thích code:**
* Chỉ số hợp lệ của `ds` là 0, 1, 2 — truy cập 5 ném `IndexError`.
* `except IndexError` — bắt lỗi này và in thông báo.

**Độ phức tạp:** O(1).

---

### Bài 4: Bắt lỗi khóa không tồn tại

**Phân tích:** Truy cập khóa không có trong dictionary (ôn lại bài 17).

**Ý tưởng:** Bắt `KeyError`.

**Thuật toán:**
1. Tạo từ điển 1 môn.
2. Truy cập `diem["Ly"]` trong `try`.
3. Bắt `KeyError` và in thông báo.

**Code:**

```python
diem = {"Toan": 8}

try:
    d = diem["Ly"]            # khóa "Ly" không tồn tại -> KeyError
except KeyError:
    print("Mon nay chua co diem!")
```

**Giải thích code:**
* `diem["Ly"]` ném `KeyError` vì từ điển không có khóa "Ly".
* `except KeyError` — bắt lỗi khóa và báo cho người dùng.

**Độ phức tạp:** O(1).

---

### Bài 5: finally luôn chạy

**Phân tích:** Cần minh họa `finally` chạy dù lỗi xảy ra.

**Ý tưởng:** Khối `try` có lỗi; `except` xử lý; `finally` vẫn chạy.

**Thuật toán:**
1. `try`: `10 / 0`.
2. `except`: in "Đã bắt được lỗi!".
3. `finally`: in "Đang dọn dẹp tài nguyên...".
4. In dòng kết thúc.

**Code:**

```python
try:
    x = 10 / 0               # lỗi xảy ra
except ZeroDivisionError:
    print("Da bat duoc loi!")
finally:
    print("Dang don dep tai nguyen...")   # luôn chạy

print("Ket thuc chuong trinh")
```

**Giải thích code:**
* Lỗi xảy ra → `except` chạy.
* `finally` chạy **sau cùng bất kể** có lỗi hay không.
* Dòng cuối ngoài khối — chứng minh chương trình còn sống.

**Độ phức tạp:** O(1).

---

### Bài 6: else chạy khi không lỗi

**Phân tích:** `10 / 2` không lỗi nên `except` không chạy, `else` phải chạy.

**Ý tưởng:** Viết đủ `try/except/else` và quan sát.

**Thuật toán:**
1. `try`: `x = 10 / 2`.
2. `except`: in "Có lỗi!" (không chạy).
3. `else`: in "Không có lỗi gì!".

**Code:**

```python
try:
    x = 10 / 2               # không lỗi
except ZeroDivisionError:
    print("Co loi!")
else:
    print("Khong co loi gi!")   # chỉ chạy khi try không lỗi
```

**Giải thích code:**
* `10 / 2 = 5.0` — không ném lỗi.
* Vì không có lỗi → `except` bỏ qua, `else` chạy.

**Độ phức tạp:** O(1).

---

### Bài 7: Sử dụng biến lỗi

**Phân tích:** Cần in nội dung chi tiết của ngoại lệ.

**Ý tưởng:** `except ValueError as e` — `e` chứa thông điệp lỗi.

**Thuật toán:**
1. Gọi `int("abc")` trong `try`.
2. `except ValueError as e`: in `e`.

**Code:**

```python
try:
    so = int("abc")
except ValueError as e:
    print("Loi:", e)
```

**Giải thích code:**
* `as e` gán đối tượng ngoại lệ vào biến `e`.
* `print("Loi:", e)` — in thông điệp gốc của Python: `invalid literal for int() with base 10: 'abc'`.

**Độ phức tạp:** O(1).

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Nhập số nguyên cho tới khi đúng

**Phân tích:** Người dùng có thể nhập sai nhiều lần — cần vòng lặp nhập lại.

**Ý tưởng:** `while True` + `try/except` + `break` khi thành công (vòng lặp bảo vệ).

**Thuật toán:**
1. Vòng lặp vô hạn.
2. Nhập và chuyển `int`.
3. Lỗi → báo, quay lại nhập.
4. Thành công → `break`.

**Code:**

```python
while True:
    try:
        so = int(input("Nhap so nguyen: "))   # Nhập: abc
    except ValueError:
        print("Sai roi, nhap lai!")
    else:
        break          # nhập đúng thì thoát vòng lặp

print("So da nhap:", so)
```

**Giải thích code:**
* `except ValueError` — nhập "abc" không chuyển được → báo và lặp lại.
* `else` + `break` — chỉ thoát khi `int()` thành công.
* Đây là khuôn mẫu **vòng lặp bảo vệ nhập liệu** dùng khắp nơi.

**Độ phức tạp:** O(k) với k là số lần nhập sai.

---

### Bài 9: Bắt nhiều loại lỗi cùng lúc

**Phân tích:** Hai loại lỗi khác nhau cần hai thông báo khác nhau.

**Ý tưởng:** Hai khối `except` viết liên tiếp — Python thử từng cái.

**Thuật toán:**
1. Nhập số, tính `100 / so`.
2. `except ValueError` — báo nhập sai.
3. `except ZeroDivisionError` — báo chia 0.
4. `else` — in kết quả.

**Code:**

```python
try:
    so = int(input("Nhap so: "))   # Nhập: 0
    ket_qua = 100 / so
except ValueError:
    print("Ban phai nhap so nguyen!")
except ZeroDivisionError:
    print("Khong duoc chia cho 0!")
else:
    print("Ket qua:", ket_qua)
```

**Giải thích code:**
* Nhập `0` → phép chia ném `ZeroDivisionError` → đúng khối thứ hai.
* Nhập `"abc"` → `ValueError` → khối thứ nhất.
* `else` chỉ in kết quả khi không lỗi.

**Độ phức tạp:** O(1).

---

### Bài 10: Chương trình chia an toàn

**Phân tích:** Lỗi phải dẫn tới **nhập lại cả hai số** cho tới khi thành công.

**Ý tưởng:** Vòng lặp bảo vệ với `break` đặt trong `else`.

**Thuật toán:**
1. Vòng lặp: nhập `a`, `b`.
2. Bắt `ValueError` và `ZeroDivisionError`.
3. Không lỗi → in thương và `Tinh xong!`, `break`.

**Code:**

```python
while True:
    try:
        a = float(input("Nhap a: "))   # Nhập: 10
        b = float(input("Nhap b: "))   # Nhập: 0
        thuong = a / b
    except ValueError:
        print("Phai nhap SO!")
    except ZeroDivisionError:
        print("Khong chia duoc cho 0!")
    else:
        print("Thuong:", thuong)
        print("Tinh xong!")
        break          # thành công thì thoát
```

**Giải thích code:**
* Bước nhập và chia đều nằm trong `try` nên được bảo vệ trọn vẹn.
* Lỗi → in thông báo, vòng lặp lặp lại.
* `else` + `break` — chỉ thoát khi không lỗi.

**Độ phức tạp:** O(k) với k là số lần nhập lại.

---

### Bài 11: Nhập tuổi hợp lệ bằng raise

**Phân tích:** Dùng `raise` chủ động ném lỗi khi dữ liệu không hợp lệ.

**Ý tưởng:** Hàm kiểm tra ném `ValueError`; nơi gọi bắt bằng `try/except`.

**Thuật toán:**
1. Định nghĩa hàm kiểm tra tuổi, `raise` khi ngoài 0–150.
2. Gọi hàm với `-5` trong `try`.
3. `except ValueError as e` in lỗi.

**Code:**

```python
def kiem_tra_tuoi(tuoi):
    # Tuổi không hợp lệ thì chủ động ném lỗi
    if tuoi < 0 or tuoi > 150:
        raise ValueError("Tuoi phai tu 0 den 150!")
    return tuoi

try:
    tuoi = kiem_tra_tuoi(-5)     # sẽ ném ValueError
except ValueError as e:
    print("Loi:", e)
```

**Giải thích code:**
* `raise ValueError("...")` — tạo và ném ngoại lệ kèm thông điệp.
* Hàm chỉ "hô hoán" — nơi gọi quyết định bắt hay để lọt.

**Độ phức tạp:** O(1).

---

### Bài 12: Đọc file không tồn tại

**Phân tích:** `open()` file không tồn tại ném `FileNotFoundError`.

**Ý tưởng:** Bắt `FileNotFoundError`; `finally` minh họa dọn dẹp luôn chạy.

**Thuật toán:**
1. `try`: mở file `"khong_co.txt"`.
2. `except FileNotFoundError`: in thông báo.
3. `finally`: in dòng dọn dẹp.

**Code:**

```python
try:
    f = open("khong_co.txt", "r")   # file không tồn tại
except FileNotFoundError:
    print("Khong tim thay file!")
finally:
    print("Da ket thuc xu ly file")   # luôn chạy
```

**Giải thích code:**
* `open("khong_co.txt", "r")` ném `FileNotFoundError` — bài 22 sẽ học kỹ về file.
* `finally` luôn chạy để báo quá trình xử lý kết thúc.

**Độ phức tạp:** O(1).

---

### Bài 13: Tránh lỗi ngoài try

**Phân tích:** `int(input(...))` nằm ngoài `try` nên lỗi nhập không được bảo vệ.

**Ý tưởng:** Đưa lệnh nhập vào trong `try`, thêm `except ValueError`.

**Thuật toán:**
1. Chuyển `int(input(...))` vào trong `try`.
2. Giữ `except ZeroDivisionError`.
3. Thêm `except ValueError`.

**Code:**

```python
try:
    a = int(input("Nhap so: "))   # Nhập: abc
    print(10 / a)
except ValueError:
    print("Phai nhap so nguyen!")
except ZeroDivisionError:
    print("Khong chia 0!")
```

**Giải thích code:**
* Giờ cả hai lệnh nguy hiểm (nhập + chia) đều trong `try`.
* Nhập `"abc"` → `except ValueError` chạy: `Phai nhap so nguyen!`.

**Độ phức tạp:** O(1).

---

### Bài 14: Bộ đủ try – except – else – finally

**Phân tích:** Minh họa đầy đủ 4 khối theo đúng thứ tự quy định.

**Ý tưởng:** `try` → `except` → `else` → `finally`.

**Thuật toán:**
1. `try`: nhập `n`, tính bình phương.
2. `except ValueError`: báo nhập sai.
3. `else`: in bình phương.
4. `finally`: in kết thúc.

**Code:**

```python
try:
    n = int(input("Nhap n: "))   # Nhập: 6
    binh_phuong = n * n
except ValueError:
    print("Nhap sai!")
else:
    print("Binh phuong:", binh_phuong)
finally:
    print("Ket thuc chuong trinh")
```

**Giải thích code:**
* Nhập `6` → không lỗi → `else` in `36`.
* `finally` luôn in `Ket thuc chuong trinh`.
* Nếu nhập sai → `except` chạy, `else` bỏ qua, `finally` vẫn chạy.

**Độ phức tạp:** O(1).

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Nhập điểm hợp lệ (0–10)

**Phân tích:** Hai tầng kiểm tra: số hợp lệ (`ValueError`) và khoảng giá trị (`raise`).

**Ý tưởng:** Vòng lặp bảo vệ kết hợp `float()` + kiểm tra khoảng.

**Thuật toán:**
1. `while True`: nhập `float(diem)`.
2. `except ValueError` → báo sai và lặp lại.
3. Kiểm tra 0–10; ngoài khoảng → `raise ValueError` (bị `except` cùng khối bắt).
4. Hợp lệ → `break`.

**Code:**

```python
while True:
    try:
        diem = float(input("Nhap diem (0-10): "))   # Nhập: abc
        if diem < 0 or diem > 10:
            raise ValueError("Diem ngoai khoang 0-10!")
        break
    except ValueError:
        print("Sai roi, nhap lai!")

print("Diem hop le:", diem)
```

**Giải thích code:**
* `raise ValueError` ném lỗi **từ bên trong try** — bị chính `except ValueError` của khối bắt, không cần khối mới.
* Nhập `"abc"` → `float` lỗi → thông báo; nhập `12` → ngoài khoảng → cũng thông báo.
* Nhập `8.5` → hợp lệ → `break`.

**Độ phức tạp:** O(k) với k là số lần nhập sai.

---

### Bài 16: Máy tính 4 phép tính không bao giờ "sập"

**Phân tích:** Cần xử lý chuỗi nhập `a op b`, bắt lỗi định dạng, chia 0, toán tử lạ.

**Ý tưởng:** `split()` lấy 3 phần; `try/except` bao quanh toàn bộ; `if` chọn phép toán.

**Thuật toán:**
1. Vòng lặp nhập phép tính; `thoat` → kết thúc.
2. `split()` → nếu không đủ 3 phần thì ném `ValueError`.
3. Chọn phép toán theo toán tử; `else` ném `ValueError`.
4. Bắt lỗi, in thông báo, lặp lại.

**Code:**

```python
while True:
    phep_tinh = input("Nhap phep tinh: ")   # Nhập: 10 / 0

    if phep_tinh == "thoat":
        print("Tam biet!")
        break

    try:
        # Tách thành [a, toán tử, b]
        phan = phep_tinh.split()
        if len(phan) != 3:
            raise ValueError("thieu thanh phan")

        a = float(phan[0])
        b = float(phan[2])
        toan_tu = phan[1]

        # Chọn phép toán theo toán tử
        if toan_tu == "+":
            ket_qua = a + b
        elif toan_tu == "-":
            ket_qua = a - b
        elif toan_tu == "*":
            ket_qua = a * b
        elif toan_tu == "/":
            ket_qua = a / b          # chia 0 sẽ ném ZeroDivisionError
        else:
            raise ValueError("toan tu khong hop le")

        print("Ket qua:", ket_qua)

    except ValueError:
        print("Loi: phep tinh khong hop le!")
    except ZeroDivisionError:
        print("Loi: khong chia duoc cho 0!")
```

**Giải thích code:**
* `split()` với `"10 / 0"` → `['10', '/', '0']`; thiếu phần tử thì `raise ValueError`.
* Phép `/` với b = 0 ném `ZeroDivisionError` → bị bắt riêng.
* Toán tử lạ (như `%`) → `raise ValueError` → thông báo chung.
* Mọi lỗi đều kết thúc bằng vòng lặp quay lại — máy tính không bao giờ "sập".

**Độ phức tạp:** O(k) với k là số lần nhập.

---

### Bài 17: Ngoại lệ tùy chỉnh — tuổi

**Phân tích:** Lỗi có tên riêng của ứng dụng — dễ đọc, dễ xử lý đúng chỗ.

**Ý tưởng:** `class TuoiKhongHopLe(Exception)`; hàm ném lỗi này theo từng tình huống.

**Thuật toán:**
1. Định nghĩa lớp ngoại lệ.
2. Hàm kiểm tra: < 0 ném lỗi âm; > 150 ném lỗi quá lớn.
3. Gọi thử hai giá trị trong `try/except`.

**Code:**

```python
# Ngoại lệ riêng của ứng dụng
class TuoiKhongHopLe(Exception):
    pass

def kiem_tra_tuoi(tuoi):
    if tuoi < 0:
        raise TuoiKhongHopLe("Tuoi khong the la so am!")
    if tuoi > 150:
        raise TuoiKhongHopLe("Tuoi qua lon!")
    return tuoi

# Thử với -5
try:
    kiem_tra_tuoi(-5)
except TuoiKhongHopLe as e:
    print("Loi:", e)

# Thử với 200
try:
    kiem_tra_tuoi(200)
except TuoiKhongHopLe as e:
    print("Loi:", e)
```

**Giải thích code:**
* `class TuoiKhongHopLe(Exception)` — kế thừa `Exception` nên được xem là ngoại lệ.
* Mỗi trường hợp `raise` kèm thông điệp riêng.
* `except TuoiKhongHopLe as e` — bắt đúng loại lỗi của mình, in thông điệp.

**Độ phức tạp:** O(1).

---

### Bài 18: Ngoại lệ tùy chỉnh — tiền rút ATM

**Phân tích:** Rút tiền vượt số dư là lỗi nghiệp vụ — cần ngoại lệ riêng.

**Ý tưởng:** `class SoDuKhongDu(Exception)`; hàm ném khi `so_tien > so_du`.

**Thuật toán:**
1. Định nghĩa lớp ngoại lệ.
2. Hàm `rut_tien` ném lỗi khi vượt số dư, ngược lại trả số dư mới.
3. Gọi với số tiền lớn hơn số dư; bắt và in lỗi.

**Code:**

```python
class SoDuKhongDu(Exception):
    pass

def rut_tien(so_du, so_tien):
    if so_tien > so_du:
        raise SoDuKhongDu("So du khong du!")
    return so_du - so_tien

try:
    so_du_moi = rut_tien(50000, 100000)
except SoDuKhongDu as e:
    print("Loi:", e)
else:
    print("Rut thanh cong. So du:", so_du_moi)
```

**Giải thích code:**
* `so_tien (100000) > so_du (50000)` → ném `SoDuKhongDu`.
* `except SoDuKhongDu as e` — bắt lỗi nghiệp vụ của ATM và in thông điệp.
* `else` chỉ chạy khi rút thành công (không xảy ra ở ví dụ này).

**Độ phức tạp:** O(1).

---

### Bài 19: Điểm danh bằng get() và KeyError

**Phân tích:** Tra điểm theo tên; học sinh chưa có điểm thì không được "sập" chương trình.

**Ý tưởng:** Hàm `lay_diem` dùng `diem[ten]` (có thể ném `KeyError`); vòng lặp bắt lỗi.

**Thuật toán:**
1. Tạo từ điển điểm.
2. Vòng lặp nhập tên; `thoat` → dừng.
3. Trong `try`: in điểm; `except KeyError`: báo không có điểm.

**Code:**

```python
diem = {"An": 8, "Binh": 7}

def lay_diem(ten):
    return diem[ten]          # có thể ném KeyError

while True:
    ten = input("Nhap ten hoc sinh: ")   # Nhập: An
    if ten == "thoat":
        break
    try:
        print("Diem cua", ten, ":", lay_diem(ten))
    except KeyError:
        print("Hoc sinh nay khong co diem!")
```

**Giải thích code:**
* `lay_diem(ten)` dùng `diem[ten]` — khóa không tồn tại ném `KeyError`.
* `except KeyError` bắt tại nơi gọi, chương trình tiếp tục nhận tên khác.
* Ví dụ: nhập `An` → in `8`; nhập `Chi` → báo không có điểm.

**Độ phức tạp:** O(k) với k là số tên nhập vào; mỗi lần tra là O(1).

---

### Bài 20: Quản lý điểm học sinh hoàn chỉnh

**Phân tích:** Tổng hợp toàn bộ bài: vòng lặp bảo vệ nhập từng môn, tính trung bình, xếp loại, bắt lỗi bất ngờ.

**Ý tưởng:** Hàm `nhap_diem(mon)` dùng vòng lặp bảo vệ; phần tính toán bọc `try/except Exception`.

**Thuật toán:**
1. Hàm `nhap_diem`: nhập `float`, kiểm tra 0–10, lặp tới khi hợp lệ.
2. Nhập điểm 3 môn.
3. Tính trung bình (làm tròn 2 chữ số), xếp loại.
4. `except Exception` bao quanh để chặn lỗi bất ngờ.

**Code:**

```python
def nhap_diem(mon):
    """Nhập điểm một môn cho tới khi hợp lệ (0-10)."""
    while True:
        try:
            d = float(input(f"Nhap diem {mon}: "))   # Nhập: abc
            if d < 0 or d > 10:
                raise ValueError("Diem ngoai khoang 0-10!")
            return d
        except ValueError:
            print("Diem khong hop le, nhap lai!")

try:
    # Nhập điểm 3 môn bằng hàm bảo vệ
    d_toan = nhap_diem("Toan")
    d_van = nhap_diem("Van")
    d_anh = nhap_diem("Anh")

    # Tính trung bình
    tb = round((d_toan + d_van + d_anh) / 3, 2)
    print("Trung binh:", tb)

    # Xếp loại
    if tb >= 8.0:
        loai = "Gioi"
    elif tb >= 6.5:
        loai = "Kha"
    elif tb >= 5.0:
        loai = "Trung binh"
    else:
        loai = "Yeu"
    print("Xep loai:", loai)

except Exception:
    print("Co loi khong mong doi!")
```

**Giải thích code:**
* Hàm `nhap_diem` trả về ngay khi hợp lệ (`return d`) — chạy với 8.5, 7, 9 → trung bình `8.17`.
* `raise ValueError` ngoài khoảng bị `except ValueError` trong chính hàm bắt.
* Lớp `except Exception` ngoài cùng là "lưới an toàn cuối cùng" cho lỗi bất ngờ.

**Độ phức tạp:** O(k) với k là tổng số lần nhập lại của cả 3 môn.

---

## 📌 Lời khuyên cuối

* Luôn bắt **loại ngoại lệ cụ thể** — `except ValueError` tốt hơn `except Exception` trong 90% tình huống.
* Vòng lặp bảo vệ nhập liệu (`while True` + `try/except` + `break`) là kỹ năng bắt buộc cho mọi chương trình thực tế.
* Dùng `raise` + ngoại lệ tự định nghĩa để code tự mô tả lỗi — ứng dụng ngân hàng, quản lý điểm đều áp dụng.
* `finally` là nơi duy nhất đảm bảo dọn dẹp tài nguyên — đừng bỏ qua.

👉 Tiếp theo: **[Bài 20: Module](../20_Module/bai_giang.md)**
