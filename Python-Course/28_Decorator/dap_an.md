# ✅ Bài 28: Đáp Án – Decorator

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án để việc học hiệu quả nhất.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Hàm trong biến

**Phân tích:** Bài tập chứng minh trong Python, hàm là đối tượng có thể gán cho biến.

**Ý tưởng:** Định nghĩa hàm như bình thường, gán tên hàm (không có dấu ngoặc) cho biến khác rồi gọi qua biến đó.

**Thuật toán:**
1. Định nghĩa `chao(ten)` trả về chuỗi chào.
2. Gán `ham = chao`.
3. Gọi `ham("Mai")` và in.

**Code:**

```python
def chao(ten):
    """Trả về lời chào dành cho ten."""
    return "Xin chào " + ten

# Gán hàm cho biến (không có dấu ngoặc!)
ham = chao
# Gọi hàm qua biến
print(ham("Mai"))
```

**Giải thích code:**
* `def chao(ten):` — định nghĩa hàm thông thường.
* `ham = chao` — gán biến `ham` trỏ tới hàm `chao`; **không viết `chao()`** vì có ngoặc là gọi hàm.
* `ham("Mai")` — gọi hàm qua biến, kết quả là chuỗi `"Xin chào Mai"`.

**Độ phức tạp:** O(1).

---

### Bài 2: Truyền hàm vào hàm

**Phân tích:** Hàm nhận một hàm khác làm tham số — khái niệm hàm bậc cao.

**Ý tưởng:** `ban_sao(loai, du_lieu)` chỉ việc gọi `loai(du_lieu)`.

**Thuật toán:**
1. Định nghĩa `ban_sao` nhận hai đối số.
2. Trả về kết quả `loai(du_lieu)`.
3. Gọi với `len` và danh sách.

**Code:**

```python
def ban_sao(loai, du_lieu):
    """Gọi loai với du_lieu và trả về kết quả."""
    return loai(du_lieu)

print(ban_sao(len, [1, 2, 3, 4]))
```

**Giải thích code:**
* `loai` là **hàm** được truyền vào; `ban_sao(len, ...)` truyền hàm `len` (không có ngoặc).
* `len([1, 2, 3, 4])` trả về `4` — số phần tử của danh sách.

**Độ phức tạp:** O(1) (phụ thuộc hàm truyền vào).

---

### Bài 3: Hàm trả về hàm

**Phân tích:** Viết closure — hàm con "nhớ" biến của hàm cha.

**Ý tưởng:** Hàm `tao_nhac_nho(loi)` định nghĩa hàm con in `loi`, rồi trả về hàm con đó.

**Thuật toán:**
1. Định nghĩa hàm cha nhận `loi`.
2. Bên trong định nghĩa hàm con `in_loi()`.
3. Hàm cha `return in_loi`.
4. Gọi kết quả trả về.

**Code:**

```python
def tao_nhac_nho(loi):
    """Trả về hàm in loi hai lần."""
    def in_loi():
        print(loi)
        print(loi)
    return in_loi

nhac_nho = tao_nhac_nho("Hãy cố gắng!")
nhac_nho()
```

**Giải thích code:**
* `in_loi` là hàm con dùng biến `loi` của hàm cha — nhờ **closure**, hàm con "khóa" biến `loi` bên trong.
* `return in_loi` — trả về hàm con (không gọi).
* Gọi `nhac_nho()` in ra hai dòng.

**Độ phức tạp:** O(1).

---

### Bài 4: Decorator in dấu hoa thị

**Phân tích:** Decorator đơn giản nhất: thêm phần in trước và sau khi gọi hàm gốc.

**Ý tưởng:** Hàm bên trong decorator in 2 dấu `*`, gọi `ham()`, in tiếp 2 dấu `*`.

**Thuật toán:**
1. Định nghĩa decorator nhận `ham`.
2. Hàm bên trong: in `*`, in `*`, gọi `ham()`, in `*`, in `*`.
3. Trả về hàm bên trong; áp dụng `@dong_khung`.

**Code:**

```python
def dong_khung(ham):
    """Trang trí: in dấu * xung quanh hàm gốc."""
    def ham_moi():
        print("*")
        print("*")
        ham()
        print("*")
        print("*")
    return ham_moi

@dong_khung
def in_ten():
    print("An")

in_ten()
```

**Giải thích code:**
* `ham_moi` bọc `ham()` ở giữa hai phần in `*`.
* `@dong_khung` tương đương `in_ten = dong_khung(in_ten)`.

**Độ phức tạp:** O(1).

---

### Bài 5: `__name__` sau khi trang trí

**Phân tích:** Không dùng `@wraps` thì hàm mới giữ tên của hàm bên trong.

**Ý tưởng:** Viết decorator bình thường rồi in `tong.__name__` để thấy kết quả là `ham_moi`.

**Thuật toán:**
1. Định nghĩa decorator `trang_tri`.
2. Áp dụng cho `tong`.
3. In `tong.__name__`.

**Code:**

```python
def trang_tri(ham):
    """Decorator không dùng @wraps."""
    def ham_moi(*args, **kwargs):
        return ham(*args, **kwargs)
    return ham_moi

@trang_tri
def tong(a, b):
    return a + b

print(tong.__name__)   # ham_moi
```

**Giải thích code:**
* `tong` đã bị thay bằng hàm `ham_moi` nên `__name__` là `ham_moi`.
* Đây chính là vấn đề mà `@wraps` giải quyết (bài 7).

**Độ phức tạp:** O(1).

---

### Bài 6: Decorator gọi hàm nhiều lần

**Phân tích:** Decorator **có đối số** — cần ba tầng hàm.

**Ý tưởng:** Tầng ngoài nhận `so_lan`, trả về decorator nhận `ham`, tầng trong gọi `ham` `so_lan` lần.

**Thuật toán:**
1. `chao_py(so_lan)` → trả về `decorator`.
2. `decorator(ham)` → trả về `ham_moi`.
3. `ham_moi` chạy vòng lặp gọi `ham()` `so_lan` lần.

**Code:**

```python
def chao_py(so_lan):
    """Trả về decorator gọi hàm gốc so_lan lần."""
    def decorator(ham):
        def ham_moi(*args, **kwargs):
            for _ in range(so_lan):
                ham(*args, **kwargs)
        return ham_moi
    return decorator

@chao_py(2)
def in_polo():
    print("Polo!")

in_polo()
```

**Giải thích code:**
* `@chao_py(2)` — Python gọi `chao_py(2)` trước để lấy decorator thật, rồi áp dụng lên hàm.
* Vòng `for _ in range(so_lan)` gọi hàm gốc đúng 2 lần.

**Độ phức tạp:** O(so_lan).

---

### Bài 7: Dùng `@wraps`

**Phân tích:** `@wraps` chép danh tính (tên, docstring) từ hàm gốc sang hàm mới.

**Ý tưởng:** Import `wraps` và đặt `@wraps(ham)` lên hàm bên trong.

**Thuật toán:**
1. Import `wraps`.
2. Đặt `@wraps(ham)` cho `ham_moi`.
3. In `__name__` và `__doc__`.

**Code:**

```python
from functools import wraps

def giu_ten(ham):
    """Decorator dùng @wraps để giữ danh tính hàm gốc."""
    @wraps(ham)
    def ham_moi(*args, **kwargs):
        return ham(*args, **kwargs)
    return ham_moi

@giu_ten
def in_ten():
    """Hàm in tên."""
    print("An")

print(in_ten.__name__)   # in_ten
print(in_ten.__doc__)    # Hàm in tên.
```

**Giải thích code:**
* `@wraps(ham)` chép `__name__`, `__doc__`, chữ ký từ `ham` sang `ham_moi`.
* Nhờ vậy, các công cụ gỡ lỗi và IntelliSense hiểu đúng hàm gốc.

**Độ phức tạp:** O(1).

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Decorator đo thời gian

**Phân tích:** Đo khoảng thời gian giữa trước và sau khi gọi hàm gốc.

**Ý tưởng:** `time.time()` cho số giây; hiệu hai lần đo là thời gian chạy.

**Thuật toán:**
1. Lưu thời điểm bắt đầu.
2. Gọi hàm gốc.
3. In thời gian chênh lệch định dạng 4 chữ số thập phân.

**Code:**

```python
import time
from functools import wraps

def do_gio(ham):
    """In thời gian chạy của hàm gốc."""
    @wraps(ham)
    def ham_moi(*args, **kwargs):
        bat_dau = time.time()          # thời điểm bắt đầu
        ket_qua = ham(*args, **kwargs) # chạy hàm gốc
        thoi_gian = time.time() - bat_dau
        print(f"{ham.__name__} mất {thoi_gian:.4f} giây")
        return ket_qua
    return ham_moi

@do_gio
def tinh_tong(n):
    return sum(range(n + 1))

print("Tổng:", tinh_tong(10_000_000))
```

**Giải thích code:**
* `time.time()` trả về số giây kể từ một mốc cố định — hiệu hai lần gọi là thời gian trôi qua.
* `{thoi_gian:.4f}` — định dạng 4 chữ số sau dấu phẩy.
* Hàm gốc vẫn trả kết quả bình thường nhờ `return ket_qua`.

**Độ phức tạp:** O(1) cho phần decorator; hàm gốc chi phí riêng.

---

### Bài 9: Yêu cầu đăng nhập

**Phân tích:** Chặn truy cập khi chưa đăng nhập — mẫu decorator bảo mật điển hình.

**Ý tưởng:** Kiểm tra cờ toàn cục trước khi cho phép gọi hàm gốc.

**Thuật toán:**
1. Nếu `not co_phien_moi`: in cảnh báo, trả `None`.
2. Ngược lại gọi hàm gốc.

**Code:**

```python
from functools import wraps

co_phien_moi = True   # mô phỏng trạng thái đăng nhập

def can_dang_nhap(ham):
    """Chỉ chạy khi người dùng đã đăng nhập."""
    @wraps(ham)
    def ham_moi(*args, **kwargs):
        if not co_phien_moi:
            print("Cần đăng nhập")
            return None
        return ham(*args, **kwargs)
    return ham_moi

@can_dang_nhap
def xem_ho_so():
    print("Ho so: An - lop 10A1")

xem_ho_so()
```

**Giải thích code:**
* `co_phien_moi = True` nên điều kiện `not co_phien_moi` sai → chạy hàm gốc.
* Nếu đổi thành `False`, chương trình chỉ in `Cần đăng nhập`.

**Độ phức tạp:** O(1).

---

### Bài 10: Đếm số lần gọi hàm

**Phân tích:** Cần một biến đếm tồn tại lâu dài — gắn thẳng lên hàm thay thế.

**Ý tưởng:** Khởi tạo `ham_moi.so_lan = 0`; mỗi lần gọi tăng lên 1 rồi in.

**Thuật toán:**
1. Trong decorator, định nghĩa `ham_moi`.
2. Sau khi định nghĩa, gán `ham_moi.so_lan = 0`.
3. Trong `ham_moi`: tăng biến, in, gọi hàm gốc.

**Code:**

```python
from functools import wraps

def dem_lan(ham):
    """Đếm và in số lần hàm được gọi."""
    @wraps(ham)
    def ham_moi(*args, **kwargs):
        ham_moi.so_lan += 1
        print(f"Số lần: {ham_moi.so_lan}")
        return ham(*args, **kwargs)
    ham_moi.so_lan = 0   # khởi tạo bộ đếm trên chính hàm
    return ham_moi

@dem_lan
def gioi_thieu():
    print("Tôi là An")

gioi_thieu()
gioi_thieu()
gioi_thieu()
```

**Giải thích code:**
* `ham_moi.so_lan` — Python cho phép gắn thuộc tính lên hàm (vì hàm là đối tượng).
* Vì `so_lan` nằm trên chính `ham_moi`, mỗi lần gọi qua `@dem_lan` đều thấy được bộ đếm.

**Độ phức tạp:** O(1) mỗi lần gọi.

---

### Bài 11: Bọc kết quả thành chữ in hoa

**Phân tích:** Decorator thay đổi **giá trị trả về** của hàm gốc.

**Ý tưởng:** Gọi hàm gốc, lấy chuỗi, trả về phiên bản `.upper()`.

**Thuật toán:**
1. Gọi hàm gốc, giữ kết quả.
2. Trả về `ket_qua.upper()`.

**Code:**

```python
from functools import wraps

def in_hoa(ham):
    """Trả về kết quả của hàm gốc dưới dạng chữ in hoa."""
    @wraps(ham)
    def ham_moi(*args, **kwargs):
        ket_qua = ham(*args, **kwargs)
        return ket_qua.upper()
    return ham_moi

@in_hoa
def cau_hoi():
    return "Do you want to quit?"

print(cau_hoi())
```

**Giải thích code:**
* Hàm gốc **trả về** chuỗi thường; decorator biến thành chữ hoa trước khi trả ra.
* Nếu hàm gốc dùng `print` thay vì `return` thì decorator không thể đổi được — nên luôn `return` dữ liệu.

**Độ phức tạp:** O(len(ket_qua)).

---

### Bài 12: Kiểm tra số âm

**Phân tích:** Decorator xác thực dữ liệu đầu vào trước khi gọi hàm.

**Ý tưởng:** Kiểm tra tham số vị trí đầu tiên trong `args`.

**Thuật toán:**
1. Nếu `args[0] < 0`: in cảnh báo, trả `None`.
2. Ngược lại chạy hàm gốc.

**Code:**

```python
from functools import wraps

def kiem_tra_am(ham):
    """Chặn tham số âm trước khi chạy hàm gốc."""
    @wraps(ham)
    def ham_moi(*args, **kwargs):
        if args[0] < 0:
            print("Số âm không hợp lệ")
            return None
        return ham(*args, **kwargs)
    return ham_moi

@kiem_tra_am
def tinh_binh_phuong(x):
    return x * x

print(tinh_binh_phuong(-3))
print(tinh_binh_phuong(4))
```

**Giải thích code:**
* `args[0]` là tham số vị trí đầu tiên — ở đây là `x`.
* Với `-3`: in cảnh báo, trả `None` (in ra `None`).
* Với `4`: chạy hàm gốc, trả `16`.

**Độ phức tạp:** O(1).

---

### Bài 13: Log tên hàm đang chạy

**Phân tích:** Dùng `__name__` để log — giúp theo dõi chương trình chạy hàm nào.

**Ý tưởng:** Một decorator dùng chung cho nhiều hàm; `ham.__name__` tự lấy tên từng hàm.

**Thuật toán:**
1. Trong `ham_moi`, in `"Đang chạy: " + ham.__name__`.
2. Gọi hàm gốc.

**Code:**

```python
from functools import wraps

def ghi_ten(ham):
    """In tên hàm trước khi gọi."""
    @wraps(ham)
    def ham_moi(*args, **kwargs):
        print(f"Đang chạy: {ham.__name__}")
        return ham(*args, **kwargs)
    return ham_moi

@ghi_ten
def foo():
    print("foo đang chạy")

@ghi_ten
def bar():
    print("bar đang chạy")

foo()
bar()
```

**Giải thích code:**
* Cùng một decorator nhưng khi áp lên `foo` và `bar`, `ham.__name__` lần lượt là `foo`, `bar`.

**Độ phức tạp:** O(1).

---

### Bài 14: Decorator xử lý chia cho 0

**Phân tích:** Ngăn chặn lỗi chia cho 0 trước khi nó xảy ra — kiểu "phòng bệnh hơn chữa bệnh".

**Ý tưởng:** Kiểm tra `args[1] == 0` (số chia) trước khi gọi hàm gốc.

**Thuật toán:**
1. Nếu `args[1] == 0`: in lỗi, trả `None`.
2. Ngược lại chạy `ham(*args, **kwargs)`.

**Code:**

```python
from functools import wraps

def an_toan_chia(ham):
    """Chặn phép chia cho 0."""
    @wraps(ham)
    def ham_moi(*args, **kwargs):
        if args[1] == 0:
            print("Lỗi chia cho 0!")
            return None
        return ham(*args, **kwargs)
    return ham_moi

@an_toan_chia
def chia(a, b):
    return a / b

print(chia(10, 2))
print(chia(10, 0))
```

**Giải thích code:**
* `args[1]` là tham số `b`. Với `b = 0` chương trình không gọi hàm gốc nên không có ngoại lệ `ZeroDivisionError`.
* `chia(10, 2)` → `5.0` (phép `/` luôn trả số thực).

**Độ phức tạp:** O(1).

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Decorator báo cáo có tên sự kiện

**Phân tích:** Decorator có đối số — cần ba tầng hàm để nhận cả `ten_su_kien` lẫn `ham`.

**Ý tưởng:** Tầng ngoài giữ `ten_su_kien`; tầng trong in "Bắt đầu", gọi hàm, in "Kết thúc".

**Thuật toán:**
1. `bao_cao(ten_su_kien)` trả về decorator.
2. Decorator nhận `ham`, trả về `ham_moi`.
3. `ham_moi` in `Bắt đầu ...`, gọi hàm gốc, in `Kết thúc ...`.

**Code:**

```python
from functools import wraps

def bao_cao(ten_su_kien):
    """In báo cáo trước và sau khi chạy hàm gốc."""
    def decorator(ham):
        @wraps(ham)
        def ham_moi(*args, **kwargs):
            print(f"Bắt đầu {ten_su_kien}")
            ket_qua = ham(*args, **kwargs)
            print(f"Kết thúc {ten_su_kien}")
            return ket_qua
        return ham_moi
    return decorator

@bao_cao("xử lý")
def xu_ly():
    print("Đang xử lý...")

xu_ly()
```

**Giải thích code:**
* `@bao_cao("xử lý")` — trước hết chạy `bao_cao("xử lý")` để lấy decorator, rồi áp dụng lên `xu_ly`.
* Tên sự kiện "xử lý" được closure "khóa" trong ba tầng hàm.

**Độ phức tạp:** O(1) cho phần decorator.

---

### Bài 16: Xếp chồng hai decorator

**Phân tích:** Thứ tự xếp chồng quyết định thứ tự chạy — decorator gần hàm nhất áp dụng trước.

**Ý tưởng:** `@f2 @f1` tương đương `hang = f2(f1(hang))` — f1 chạy trong cùng, f2 bọc ngoài.

**Thuật toán:**
1. Viết `f1` in trước/sau quanh hàm gốc.
2. Viết `f2` tương tự.
3. Xếp `@f2` trên `@f1` và chạy.

**Code:**

```python
from functools import wraps

def f1(ham):
    @wraps(ham)
    def ham_moi(*args, **kwargs):
        print("F1 trước")
        ket_qua = ham(*args, **kwargs)
        print("F1 sau")
        return ket_qua
    return ham_moi

def f2(ham):
    @wraps(ham)
    def ham_moi(*args, **kwargs):
        print("F2 trước")
        ket_qua = ham(*args, **kwargs)
        print("F2 sau")
        return ket_qua
    return ham_moi

@f2
@f1
def hang():
    print("Thân hàm")

hang()
```

**Giải thích code:**
* Thứ tự áp dụng: `f1` trước (gần hàm nhất), rồi `f2` bọc ngoài.
* Khi gọi: `F2 trước` → `F1 trước` → `Thân hàm` → `F1 sau` → `F2 sau` — đúng như output mong đợi (giống củ hành bóc từ ngoài vào trong).

**Độ phức tạp:** O(1).

---

### Bài 17: Bộ nhớ đệm (cache) kết quả

**Phân tích:** Lưu kết quả theo tham số để lần sau không tính lại — tăng tốc chương trình.

**Ý tưởng:** Dictionary nằm trong closure của decorator; trước khi gọi hàm gốc, kiểm tra dict.

**Thuật toán:**
1. Tạo `luu_tru = {}` ngoài `ham_moi`.
2. Nếu `args` có trong dict → in "Lấy từ cache", trả giá trị lưu.
3. Nếu chưa có → gọi hàm gốc, lưu vào dict, in "Tính toán", trả kết quả.

**Code:**

```python
from functools import wraps

def bo_nho_dem(ham):
    """Lưu kết quả theo tham số để tái sử dụng."""
    luu_tru = {}
    @wraps(ham)
    def ham_moi(*args, **kwargs):
        if args in luu_tru:
            print("Lấy từ cache")
            return luu_tru[args]
        print("Tính toán")
        ket_qua = ham(*args, **kwargs)
        luu_tru[args] = ket_qua
        return ket_qua
    return ham_moi

@bo_nho_dem
def binh_phuong(n):
    return n * n

print(binh_phuong(5))
print(binh_phuong(5))
```

**Giải thích code:**
* `args` là tuple `(5,)` — dùng được làm khóa của dict.
* Lần gọi thứ hai: `(5,)` đã có trong `luu_tru` nên không gọi hàm gốc.
* Đây chính là ý tưởng của `functools.lru_cache` có sẵn trong Python!

**Độ phức tạp:** O(1) cho lần gọi sau (cache hit); O(1) tính toán gốc.

---

### Bài 18: Kiểm tra kiểu dữ liệu tham số

**Phân tích:** Xác thực kiểu dữ liệu trước khi xử lý — tránh lỗi logic khó phát hiện.

**Ý tưởng:** Dùng `isinstance(args[0], int)` để kiểm tra tham số đầu tiên.

**Thuật toán:**
1. Nếu `not isinstance(args[0], int)`: in "Cần số nguyên", trả `None`.
2. Ngược lại chạy hàm gốc.

**Code:**

```python
from functools import wraps

def kiem_tra_kieu(ham):
    """Chỉ chấp nhận tham số là số nguyên."""
    @wraps(ham)
    def ham_moi(*args, **kwargs):
        if not isinstance(args[0], int):
            print("Cần số nguyên")
            return None
        return ham(*args, **kwargs)
    return ham_moi

@kiem_tra_kieu
def tong_tu_0(n):
    return sum(range(n + 1))

print(tong_tu_0(3))
print(tong_tu_0("abc"))
```

**Giải thích code:**
* `tong_tu_0(3)` → `0 + 1 + 2 + 3 = 6`.
* `"abc"` không phải `int` → bị chặn, tránh lỗi `TypeError` khi tính `range`.
* `isinstance` an toàn hơn so sánh `type(x) == int` vì nó xét cả kế thừa.

**Độ phức tạp:** O(n) với `n` là tham số truyền vào hàm gốc.

---

### Bài 19: Log đầy đủ tham số và kết quả

**Phân tích:** Ghi log chuyên nghiệp: tên hàm, tham số, kết quả — hữu ích khi gỡ lỗi ứng dụng.

**Ý tưởng:** Bóc gói `args`/`kwargs` để in dạng thân thiện, sau đó in kết quả trước khi trả về.

**Thuật toán:**
1. Gọi `ham(*args, **kwargs)`, giữ kết quả.
2. In dòng log gồm tên, args, kwargs, kết quả.
3. Trả về kết quả.

**Code:**

```python
from functools import wraps

def ghi_log(ham):
    """In tên, tham số và kết quả của mỗi lần gọi."""
    @wraps(ham)
    def ham_moi(*args, **kwargs):
        ket_qua = ham(*args, **kwargs)
        print(f"gọi {ham.__name__} args={args} kwargs={kwargs} -> {ket_qua}")
        return ket_qua
    return ham_moi

@ghi_log
def mua_hang(loai, so_tien=100000):
    return f"Đã mua {loai}"

print(mua_hang("trà", so_tien=500000))
```

**Giải thích code:**
* `args = ('trà',)`, `kwargs = {'so_tien': 500000}` — bóc gói đúng như truyền vào.
* Log được in trước `return`, nên thứ tự output đúng: dòng log rồi dòng kết quả.
* Kiểu log này rất giống log thật trong các ứng dụng web.

**Độ phức tạp:** O(1) ngoài chi phí hàm gốc.

---

### Bài 20: Kết hợp đếm lần gọi và đo thời gian

**Phân tích:** Xếp chồng hai decorator, chú ý thứ tự để bộ đếm tăng đúng mỗi lần gọi.

**Ý tưởng:** Đặt `@dem_lan` gần hàm nhất (bên dưới), `@do_gio` bọc ngoài — lúc đó mỗi lần gọi: `do_gio` bắt đầu đo → `dem_lan` tăng biến → chạy thân hàm.

**Thuật toán:**
1. Viết `dem_lan` (in "Lần gọi thứ n").
2. Viết `do_gio` (in tên hàm + thời gian).
3. Xếp `@do_gio` phía trên `@dem_lan`.
4. Gọi `hoc_tap()` hai lần.

**Code:**

```python
import time
from functools import wraps

def dem_lan(ham):
    """Đếm số lần gọi hàm."""
    @wraps(ham)
    def ham_moi(*args, **kwargs):
        ham_moi.so_lan += 1
        print(f"Lần gọi thứ {ham_moi.so_lan}")
        return ham(*args, **kwargs)
    ham_moi.so_lan = 0
    return ham_moi

def do_gio(ham):
    """Đo và in thời gian chạy."""
    @wraps(ham)
    def ham_moi(*args, **kwargs):
        bat_dau = time.time()
        ket_qua = ham(*args, **kwargs)
        print(f"Đang chạy {ham.__name__}, tốn {time.time() - bat_dau:.4f} giây")
        return ket_qua
    return ham_moi

@do_gio
@dem_lan
def hoc_tap():
    print("Học bài")

hoc_tap()
hoc_tap()
```

**Giải thích code:**
* `hoc_tap = do_gio(dem_lan(hoc_tap))` — `dem_lan` bọc trong, `do_gio` bọc ngoài.
* Mỗi lần gọi: `do_gio` đo → `dem_lan` in "Lần gọi thứ n" → thân hàm in "Học bài" → quay ra in thời gian.
* Nếu đảo thứ tự `@`, thời gian đo sẽ chỉ tính phần trang trí lẫn nhau — thử đổi để tự kiểm chứng!

**Độ phức tạp:** O(1) mỗi lần gọi ngoài chi phí thân hàm.

---

## 📌 Lời khuyên cuối

* Decorator = **nhận hàm → trả hàm mới**; cứ giữ khung này là viết đúng.
* Luôn `@wraps(ham)` và `*args/**kwargs` để decorator hoạt động với hàm bất kỳ.
* Decorator có đối số cần **ba tầng** hàm; đừng nhầm với loại không đối số.
* Khi xếp chồng, đọc từ **dưới lên** để biết thứ tự áp dụng.
* Trong dự án thật, các framework (Flask `@app.route`, Django `@login_required`) dùng decorator liên tục — giờ bạn đã hiểu chúng hoạt động ra sao!

👉 Tiếp theo: **[Bài 29: Iterator](../29_Iterator/bai_giang.md)**