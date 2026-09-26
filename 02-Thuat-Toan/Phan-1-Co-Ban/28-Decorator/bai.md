<!-- TỰ ĐỘNG ĐỒNG BỘ từ 01-Co-Ban/28-Decorator/bai.md — đừng sửa trực tiếp, sửa bản chính rồi chạy tools/sync_tracks.py -->

# Bài 28 — Decorator – Trang Trí Cho Hàm

> 🎓 **Chương 9 – Lập trình nâng cao**
> Từ bài 25 đến bài 29, chúng ta học những kỹ thuật lập trình "cao cấp" để viết code gọn gàng và chuyên nghiệp: lambda, list comprehension, generator, decorator, iterator. Bài 27 đã dạy bạn **generator** — cách tạo ra chuỗi giá trị chậm rãi, tiết kiệm bộ nhớ. Bài này, chúng ta học **decorator** — "phụ kiện" gắn thêm cho hàm mà không phải sửa chính hàm đó.

## 🧠 Điều kiện tiên quyết

- [Bài 12 — Hàm (Function) Trong Python](../12-Ham/bai.md)
- [Bài 27 — Generator – Sinh Dữ Liệu "Từng Phần Một"](../27-Generator/bai.md)

---

## 🎯 Mục tiêu

Sau bài học này, học viên sẽ:

* ✅ Hiểu **hàm bậc cao (higher-order function)** — hàm nhận hàm khác làm tham số hoặc trả về hàm.
* ✅ Hiểu **closure** — hàm lồng bên trong hàm khác, "nhớ" được biến của hàm bao quanh.
* ✅ Viết được **decorator bằng cú pháp `@`** — cách trang trí hàm ngắn gọn nhất.
* ✅ Viết được **decorator có đối số** và **decorator không đối số**.
* ✅ Biết dùng **`functools.wraps`** để giữ thông tin gốc của hàm khi trang trí.
* ✅ Xử lý được tham số **`*args` / `**kwargs`** bên trong decorator.
* ✅ Áp dụng decorator vào các tình huống thực tế: đo thời gian, kiểm tra đăng nhập, ghi log, đếm lần gọi, kết hợp nhiều decorator.

---

## 📖 Kiến thức

### 1. Nhắc nhẹ bài trước và bài này nối tiếp thế nào

Ở bài 27, bạn đã thấy một ví dụ về **hàm trả về hàm**:

```python
def tao_bien_dem():
    dem = 0
    def tang():
        nonlocal dem
        dem += 1
        return dem
    return tang
```

Đây chính là nền tảng của **decorator**: mọi thứ xoay quanh khả năng của Python cho phép **truyền hàm vào hàm** và **trả hàm từ hàm**.

> 🐍 **Sự thật thú vị:** Trong Python, hàm cũng là một **đối tượng** như số, chuỗi, danh sách. Bạn có thể gán hàm cho biến, đưa vào danh sách, truyền làm đối số — và tất nhiên, trả về từ hàm khác!

### 2. Hàm bậc cao (Higher-order function)

**Hàm bậc cao** là hàm thỏa mãn ít nhất một trong hai điều kiện:

| Điều kiện | Ví dụ đơn giản |
|---|---|
| 📥 Nhận hàm khác làm **tham số** | `sorted([3, 1, 2], key=len)` — truyền hàm `len` vào |
| 📤 Trả về một hàm mới | `tao_bien_dem()` ở trên trả về hàm `tang` |

> 💬 **Ví dụ đời thực:** Giống như **nhà máy đóng gói** — bạn đưa một món hàng (hàm) vào, nhà máy bọc thêm giấy, thêm nơ, thêm thẻ giá rồi trả ra món hàng mới đẹp hơn (hàm mới). Bản chất món hàng vẫn vậy, nhưng giờ nó có thêm "phụ kiện".

**Kiểm chứng nhanh** — chạy thử trong Python:

```python
# Hàm thông thường
def chao(ten):
    return f"Xin chào {ten}!"

# Gán hàm cho biến (hàm cũng là đối tượng)
ham_giu = chao
print(ham_giu("Mai"))       # Xin chào Mai!
print(chao.__name__)        # chao — hàm giữ nguyên tên gốc
print(ham_giu.__name__)     # chao — vẫn là chao
```

### 3. Closure — hộp ký ức của hàm

Khi viết một hàm **bên trong** một hàm khác, hàm trong được gọi là **closure** nếu nó dùng biến của hàm ngoài:

```python
def tao_ham_nhan(so):
    # Hàm bên trong "nhớ" giá trị của so
    def nhan(x):
        return x * so
    return nhan

nhan_2 = tao_ham_nhan(2)
nhan_5 = tao_ham_nhan(5)

print(nhan_2(10))   # 20
print(nhan_5(10))   # 50
```

> 💡 Hàm `nhan` "đóng gói" biến `so` vào trong — dù hàm `tao_ham_nhan` đã chạy xong, `nhan_2` vẫn nhớ `so = 2`. Đó là lý do gọi là **closure** (đóng kín biến bên trong).

### 4. Decorator là gì?

**Decorator** là một hàm bậc cao đặc biệt: **nhận vào một hàm, trả về một hàm mới đã được "trang trí" thêm chức năng**.

> 💬 **Ví dụ đời thực:** Bạn có một chiếc **áo trắng** (hàm gốc). Mang áo ra tiệm in hình lên ngực, bạn nhận lại chiếc áo **vẫn mặc được như cũ** nhưng giờ **đẹp hơn** (hàm mới). Bạn không cần may lại áo, chỉ thêm chút "trang trí" — đúng nghĩa chữ **decorator**.

```mermaid
flowchart LR
    A[Hàm gốc <br/>chao()] --> B[Decorator <br/>trang_tri]
    B --> C[Hàm mới <br/>chao + chức năng thêm]
    C --> D[Chạy: vẫn gọi là chao\&#40;&#41;]
```

**Cách viết không dùng cú pháp `@`:**

```python
def trang_tri(ham):
    def ham_moi(*args, **kwargs):
        print(">>> Trước khi gọi hàm")
        ket_qua = ham(*args, **kwargs)
        print(">>> Sau khi gọi hàm")
        return ket_qua
    return ham_moi

def chao():
    print("Xin chào!")

chao = trang_tri(chao)   # thay hàm cũ bằng phiên bản đã trang trí
chao()
```

Kết quả:

```
>>> Trước khi gọi hàm
Xin chào!
>>> Sau khi gọi hàm
```

### 5. Cú pháp `@` — cách viết ngắn gọn

Python cung cấp **đường cú pháp ngọt (syntactic sugar)** để việc trên gọn hơn:

```python
def trang_tri(ham):
    def ham_moi(*args, **kwargs):
        print(">>> Trước khi gọi hàm")
        ket_qua = ham(*args, **kwargs)
        print(">>> Sau khi gọi hàm")
        return ket_qua
    return ham_moi

@trang_tri          # tương đương: chao = trang_tri(chao)
def chao():
    print("Xin chào!")

chao()
```

> ✅ `@trang_tri` viết ngay phía trên `def` — Python sẽ tự động chạy `chao = trang_tri(chao)` và thay thế hàm. Kết quả giống hệt ví dụ trước, nhưng code đẹp và dễ đọc hơn nhiều.

### 6. Vì sao phải dùng `*args` / `**kwargs` trong decorator?

Hàm gốc có thể có **bất kỳ tham số nào** — 1 tham số, 5 tham số, tham số từ khóa... Decorator không thể biết trước, nên hàm trang trí phải nhận **tất cả**:

| Cú pháp | Ý nghĩa |
|---|---|
| `*args` | Gom **mọi tham số vị trí** vào một tuple |
| `**kwargs` | Gom **mọi tham số từ khóa** vào một dictionary |
| `ham(*args, **kwargs)` | Bóc gói và truyền **nguyên vẹn** vào hàm gốc |

```python
def trang_tri(ham):
    def ham_moi(*args, **kwargs):
        print(f"Nhận được: args={args}, kwargs={kwargs}")
        return ham(*args, **kwargs)   # truyền lại nguyên vẹn
    return ham_moi

@trang_tri
def cong(a, b=0):
    return a + b

print(cong(3, 5))        # args=(3, 5)
print(cong(3, b=7))      # args=(3,), kwargs={'b': 7}
```

### 7. Decorator không đối số vs có đối số

**a) Decorator không đối số** — cái ta đã thấy: `@trang_tri` nhận thẳng tên hàm.

**b) Decorator có đối số** — khi cần truyền tham số vào decorator như `@lap_lai(3)`:

```python
def lap_lai(so_lan):
    # Vòng ngoài nhận đối số của decorator
    def decorator(ham):
        # Vòng giữa nhận hàm gốc
        def ham_moi(*args, **kwargs):
            for _ in range(so_lan):
                ham(*args, **kwargs)
        return ham_moi
    return decorator

@lap_lai(3)
def thong_bao():
    print("Chào mừng bạn!")

thong_bao()
```

Kết quả in ra 3 lần `Chào mừng bạn!`.

> 💡 **Cách nhớ:** `@decorator` → decorator nhận **hàm**. `@decorator(3)` → decorator nhận **số 3**, rồi TRẢ VỀ một decorator khác nhận hàm. Ba tầng lồng nhau!

### 8. `functools.wraps` — giữ "danh tính" của hàm

Sau khi trang trí, hàm mới mất tên gốc và tài liệu gốc:

```python
def trang_tri(ham):
    def ham_moi(*args, **kwargs):
        return ham(*args, **kwargs)
    return ham_moi

@trang_tri
def chao():
    """In lời chào."""
    pass

print(chao.__name__)        # ham_moi — KHÔNG còn là chao!
print(chao.__doc__)         # None — mất tài liệu!
```

**Giải pháp:** dùng `functools.wraps` — nó chép tên, tài liệu, chữ ký từ hàm gốc sang hàm mới:

```python
from functools import wraps

def trang_tri(ham):
    @wraps(ham)   # chép danh tính của ham vào ham_moi
    def ham_moi(*args, **kwargs):
        return ham(*args, **kwargs)
    return ham_moi

@trang_tri
def chao():
    """In lời chào."""
    pass

print(chao.__name__)   # chao ✅
print(chao.__doc__)    # In lời chào. ✅
```

> 💎 **Quy tắc vàng:** Decorator nào cũng nên dùng `@wraps` — giúp trình gỡ lỗi và công cụ tự hoàn thành (IntelliSense) hoạt động chính xác.

### 9. Kết hợp nhiều decorator — xếp lớp trang trí

Có thể đặt nhiều `@` chồng lên nhau. Thứ tự áp dụng: **từ dưới lên trên** (gần hàm nhất chạy trước):

```python
def in_ten_decorator(ham):
    @wraps(ham)
    def ham_moi(*args, **kwargs):
        print(f"Đang chạy: {ham.__name__}")
        return ham(*args, **kwargs)
    return ham_moi

def do_thoi_gian(ham):
    @wraps(ham)
    def ham_moi(*args, **kwargs):
        import time
        bat_dau = time.time()
        ket_qua = ham(*args, **kwargs)
        print(f"Tốn {time.time() - bat_dau:.4f} giây")
        return ket_qua
    return ham_moi

@in_ten_decorator
@do_thoi_gian
def tinh_tong(n):
    return sum(range(n))

tinh_tong(1_000_000)
```

Thứ tự thực hiện: `in_ten_decorator(do_thoi_gian(tinh_tong))` — lớp trong cùng (`do_thoi_gian`) chạy trước khi đến thân hàm, lớp ngoài (`in_ten_decorator`) chạy bọc quanh.

---

## 💡 Ví dụ minh họa

### Ví dụ 1: Decorator đo thời gian chạy (phổ biến nhất)

```python
import time
from functools import wraps

def do_thoi_gian(ham):
    """Trang trí: in thời gian chạy của ham."""
    @wraps(ham)
    def ham_moi(*args, **kwargs):
        bat_dau = time.time()              # ghi lại giờ bắt đầu
        ket_qua = ham(*args, **kwargs)     # chạy hàm gốc
        cuoi = time.time()                 # giờ kết thúc
        print(f"{ham.__name__} chạy mất {cuoi - bat_dau:.4f} giây")
        return ket_qua                     # trả kết quả như cũ
    return ham_moi

@do_thoi_gian
def tinh_tong(n):
    return sum(i for i in range(n))

print("Tổng:", tinh_tong(10_000_000))
```

**Giải thích từng dòng:**

| Dòng | Ý nghĩa |
|---|---|
| `import time` | Nhập module thời gian (đo giây) |
| `from functools import wraps` | Nhập công cụ giữ danh tính hàm |
| `def do_thoi_gian(ham):` | Hàm bậc cao nhận hàm gốc |
| `def ham_moi(*args, **kwargs):` | Hàm thay thế — nhận mọi tham số |
| `bat_dau = time.time()` | Đếm thời điểm trước khi chạy |
| `ket_qua = ham(*args, **kwargs)` | Gọi hàm gốc, giữ kết quả |
| `print(...)` | In ra số giây đã trôi qua |
| `return ket_qua` | Trả kết quả nguyên vẹn cho người gọi |
| `@do_thoi_gian` | Áp dụng decorator cho hàm bên dưới |

### Ví dụ 2: Decorator kiểm tra đăng nhập

```python
from functools import wraps

dang_nhap = {"tai_khoan": "admin", "mat_khau": "123456"}

def yeu_cau_dang_nhap(ham):
    """Chỉ cho phép chạy khi người dùng đã đăng nhập."""
    @wraps(ham)
    def ham_moi(*args, **kwargs):
        if not current_user.get("dang_nhap"):   # chưa đăng nhập?
            print("⛔ Bạn cần đăng nhập trước!")
            return None
        return ham(*args, **kwargs)
    return ham_moi

current_user = {"dang_nhap": False}

@yeu_cau_dang_nhap
def xem_thong_tin():
    print("📄 Thông tin cá nhân: Nguyễn Văn An, lớp 10A1")

xem_thong_tin()          # ⛔ bị chặn
current_user["dang_nhap"] = True
xem_thong_tin()          # ✅ chạy được
```

### Ví dụ 3: Decorator đếm số lần gọi

```python
from functools import wraps

def dem_lan_goi(ham):
    """Đếm mỗi khi hàm được gọi."""
    @wraps(ham)
    def ham_moi(*args, **kwargs):
        ham_moi.so_lan += 1                    # tăng biến gắn trên chính hàm
        print(f"Lần gọi thứ: {ham_moi.so_lan}")
        return ham(*args, **kwargs)
    ham_moi.so_lan = 0                         # khởi tạo biến đếm
    return ham_moi

@dem_lan_goi
def goi_xin_chao():
    print("Xin chào!")

goi_xin_chao()   # Lần gọi thứ: 1
goi_xin_chao()   # Lần gọi thứ: 2
goi_xin_chao()   # Lần gọi thứ: 3
```

---

## 🔬 Ví dụ nâng cao

### Ví dụ 1: Hệ thống log cho ứng dụng (thực tế công việc)

```python
import datetime
from functools import wraps

def ghi_log(ten_module):
    """Ghi lại mọi lần gọi hàm kèm thời gian và đối số."""
    def decorator(ham):
        @wraps(ham)
        def ham_moi(*args, **kwargs):
            gio = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"[{gio}] [{ten_module}] Gọi {ham.__name__}{args}{kwargs}")
            ket_qua = ham(*args, **kwargs)
            print(f"[{gio}] [{ten_module}] Kết quả: {ket_qua}")
            return ket_qua
        return ham_moi
    return decorator

@ghi_log("MAY-TINH")
def cong(a, b):
    return a + b

@ghi_log("MAY-TINH")
def nhan(a, b):
    return a * b

cong(3, 4)    # log đầy đủ cả tham số lẫn kết quả
nhan(2, 5)
```

> 🏪 **Tình huống thực tế:** Phần mềm quản lý cửa hàng cần biết AI NHIÊU lần chức năng "tính tiền" được bấm — gắn một decorator log lên hàm tính tiền là xong, không cần sửa code trong hàm.

### Ví dụ 2: Chạy thử nhiều lần để kiểm tra độ ổn định

```python
import random
from functools import wraps

def chay_nhieu_lan(so_lan):
    """Chạy hàm nhiều lần rồi trả về trung bình kết quả."""
    def decorator(ham):
        @wraps(ham)
        def ham_moi(*args, **kwargs):
            cac_ket_qua = [ham(*args, **kwargs) for _ in range(so_lan)]
            return sum(cac_ket_qua) / so_lan
        return ham_moi
    return decorator

@chay_nhieu_lan(5)
def tung_xuc_xac():
    return random.randint(1, 6)

print("Trung bình 5 lần tung:", tung_xuc_xac())
```

### Ví dụ 3: Ứng dụng "quản lý tiền ATM" với decorator bảo mật

```python
from functools import wraps

mat_khau_dung = "1234"
da_xac_thuc = False

def kiem_tra_pin(ham):
    """Bắt buộc xác thực PIN trước khi rút tiền."""
    @wraps(ham)
    def ham_moi(*args, **kwargs):
        global da_xac_thuc
        if not da_xac_thuc:
            pin = input("Nhập mã PIN: ")
            da_xac_thuc = (pin == mat_khau_dung)
            if not da_xac_thuc:
                print("⛔ Sai mã PIN!")
                return None
        return ham(*args, **kwargs)
    return ham_moi

@kiem_tra_pin
def rut_tien(so_tien):
    print(f"💰 Đã rút {so_tien:,} đồng")

rut_tien(500_000)   # lần đầu phải nhập PIN
rut_tien(200_000)   # lần sau không cần nhập lại
```

---

## ⚠️ Lỗi thường gặp

### Lỗi 1: Quên `return ham_moi` trong decorator

```python
def trang_tri(ham):
    def ham_moi():
        print("Đã trang trí")
        return ham()
    # ❌ SAI: quên return ham_moi

@trang_tri
def chao():
    return "Xin chào"

chao()   # TypeError: 'NoneType' object is not callable
```

* **Nguyên nhân:** Decorator trả về `None` thay vì hàm mới, nên `chao` biến thành `None`.
* **Cách sửa:** Thêm `return ham_moi` ở cuối hàm decorator.

### Lỗi 2: Quên `*args, **kwargs` khi hàm gốc có tham số

```python
def trang_tri(ham):
    def ham_moi():          # ❌ SAI: không nhận tham số
        return ham()
    return ham_moi

@trang_tri
def cong(a, b):
    return a + b

cong(3, 5)   # TypeError: ham_moi() takes 0 positional arguments
```

* **Nguyên nhân:** Hàm thay thế không nhận tham số mà hàm gốc đòi.
* **Cách sửa:** Khai báo `def ham_moi(*args, **kwargs):` và gọi `ham(*args, **kwargs)`.

### Lỗi 3: Quên `@wraps` làm mất tên hàm gốc

* **Nguyên nhân:** Hàm trang trí lấy tên của `ham_moi`, làm khó gỡ lỗi.
* **Cách sửa:** Luôn thêm `from functools import wraps` và `@wraps(ham)` cho hàm bên trong.

### Lỗi 4: Dùng decorator CÓ đối số nhưng chỉ viết `@ten(3)` thiếu tầng

* **Nguyên nhân:** Nhầm lẫn hai loại decorator; `@ten(3)` phải có ba tầng hàm lồng nhau.
* **Cách sửa:** Đọc lại mục 7 — decorator có đối số cần đủ `def ngoai(doi_so):` → `def giua(ham):` → `def trong(...):`.

### Lỗi 5: Viết dấu `@` nhưng quên khai báo hàm decorator

* **Nguyên nhân:** Dùng tên decorator chưa được định nghĩa.
* **Kết quả báo:** `NameError: name 'trang_tri' is not defined`.
* **Cách sửa:** Khai báo decorator TRƯỚC khi dùng `@` phía trên nó.

---

## 💎 Mẹo

* 🧠 **Quy tắc ghi nhớ:** "Trang trí hàm = nhận hàm → trả hàm mới". Cứ nghĩ theo kiểu đó là viết đúng.
* ✍️ **Luôn `@wraps(ham)`** — không bao giờ sai, giúp tên và docstring của hàm gốc được giữ.
* ⏱️ **Đo thời gian là bài tập khởi động kinh điển** — viết `do_thoi_gian` một lần rồi dùng cho mọi hàm.
* 🔍 **`*args` / `**kwargs` là "chất bôi trơn"** — giúp decorator làm việc với hàm bất kỳ, dù tham số thế nào.
* 🧱 **Xếp chồng decorator theo thứ tự** — đọc từ dưới lên để biết thứ tự chạy thật sự.
* 🛡️ **Đừng lạm dụng** — decorator đẹp nhưng quá nhiều lớp sẽ khó đọc. 2–3 lớp là đủ.
* 🧪 Muốn chạy thử nhanh: dùng Python interactive (`python` rồi gõ trực tiếp).

---

## 📝 Tóm tắt

| Khái niệm | Ý nghĩa |
|---|---|
| 🎀 **Decorator** | Hàm bậc cao nhận hàm, trả về hàm mới có thêm chức năng |
| 📥 **Hàm bậc cao** | Hàm nhận/trả về hàm khác |
| 🧊 **Closure** | Hàm lồng trong hàm, nhớ biến của hàm bao quanh |
| `@ten` | Cú pháp ngắn gọn thay cho `ten(ham)` |
| `@ten(doi_so)` | Decorator có đối số — ba tầng hàm lồng nhau |
| `*args, **kwargs` | Nhận mọi tham số vị trí / từ khóa |
| `@wraps` | Giữ tên và tài liệu của hàm gốc |
| Thứ tự xếp chồng | Lớp gần hàm nhất chạy trước |

**Ứng dụng thực tế:** đo thời gian ⏱️, kiểm tra đăng nhập 🔐, ghi log 📋, đếm lần gọi 🔢, chạy thử nhiều lần 🎲, bảo mật PIN 💳.

---

## 🧪 Kiểm tra nhanh

1. ❓ Decorator là gì? Nó nhận vào gì và trả về gì?
2. ❓ Cú pháp `@ten` tương đương với lệnh gán nào?
3. ❓ `*args` và `**kwargs` dùng để làm gì trong decorator?
4. ❓ Hai loại decorator "không đối số" và "có đối số" khác nhau thế nào?
5. ❓ `functools.wraps` giải quyết vấn đề gì?
6. ❓ Khi xếp hai decorator `@A` và `@B` lên một hàm, cái nào chạy trước?
7. ❓ Viết decorator in "Bắt đầu..." trước khi gọi hàm bất kỳ.
8. ❓ Vì sao trong decorator phải `return ham(*args, **kwargs)`?
9. ❓ Hàm bậc cao là gì? Kể 2 ví dụ đã học.
10. ❓ Closure là gì và vì sao decorator cần nó?

<details>
<summary>🔍 Xem đáp án</summary>

1. Hàm bậc cao nhận một hàm và trả về hàm mới có thêm chức năng.
2. `ten(ham)` — ví dụ `chao = trang_tri(chao)`.
3. Nhận mọi tham số vị trí (args) và tham số từ khóa (kwargs) của hàm gốc rồi truyền nguyên vẹn vào.
4. Không đối số: `@ten` nhận thẳng hàm; có đối số: `@ten(3)` cần một tầng ngoài nhận đối số rồi mới trả về decorator nhận hàm.
5. Chép tên, docstring, chữ ký từ hàm gốc sang hàm mới.
6. Decorator gần hàm nhất (B) áp dụng trước, rồi đến A.
7. `def bat_dau(ham): def h_moi(*a, **kw): print("Bắt đầu..."); return ham(*a, **kw) return h_moi`.
8. Để giữ nguyên giá trị trả về của hàm gốc — decorator chỉ thêm phần trang trí, không được làm mất kết quả.
9. Hàm nhận hàm làm tham số hoặc trả về hàm — ví dụ: `sorted(key=...)`, `map()`, decorator.
10. Hàm lồng bên trong hàm khác và "nhớ" biến của hàm ngoài; decorator dùng closure để nắm giữ hàm gốc.

</details>

---

## 📚 Bài đọc thêm

* [Python.org – Decorators](https://docs.python.org/3/reference/compound_stmts.html#function-definitions)
* [Python.org – functools.wraps](https://docs.python.org/3/library/functools.html#functools.wraps)
* [Real Python – Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/)
* [GeeksforGeeks – Decorators in Python](https://www.geeksforgeeks.org/decorators-in-python/)
* [Python Tutor](https://pythontutor.com/) — xem từng bước decorator chạy

---

---

## 🧩 Bài tập

> 📝 🎯 **Chủ đề:** Hàm bậc cao, closure, cú pháp `@`, `functools.wraps`, decorator có đối số, `*args/**kwargs`, kết hợp nhiều decorator.

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Hàm trong biến

* **Đề bài:** Tạo hàm `chao(ten)` trả về chuỗi `"Xin chào " + ten`. Gán hàm này cho biến `ham` rồi gọi qua biến `ham` để in lời chào dành cho "Mai".
* **Input:** Không có.
* **Output:**
  ```
  Xin chào Mai
  ```
* **Gợi ý:** Trong Python hàm là đối tượng — `ham = chao` rồi gọi `ham("Mai")`.

### Bài 2: Truyền hàm vào hàm

* **Đề bài:** Viết hàm `ban_sao(loai, du_lieu)` nhận một hàm `loai` (ví dụ `len` hoặc `str`) và dữ liệu, rồi gọi `loai(du_lieu)` và trả về kết quả. In ra kết quả khi `loai` là `len`, `du_lieu` là `[1, 2, 3, 4]`.
* **Input:** Không có
* **Output:**
  ```
  4
  ```
* **Gợi ý:** Gọi `ban_sao(len, [1, 2, 3, 4])`.

### Bài 3: Hàm trả về hàm

* **Đề bài:** Viết hàm `tao_nhac_nho(loi)` trả về một **closure** mà khi gọi (không đối số) sẽ in ra `loi` hai lần, mỗi lần một dòng.
* **Input:** Không có
* **Output:**
  ```
  Hãy cố gắng!
  Hãy cố gắng!
  ```
* **Gợi ý:** Định nghĩa hàm con trong hàm cha, hàm cha `return` hàm con.

### Bài 4: Decorator in dấu hoa thị

* **Đề bài:** Dùng cú pháp `@` tạo decorator `dong_khung` — in 2 dấu `*`, gọi hàm gốc `in_ten()` in `"An"`, rồi in tiếp 2 dấu `*`.
* **Input:** Không có
* **Output:**
  ```
  *
  *
  An
  *
  *
  ```
* **Gợi ý:** Decorator chạy thân hàm gốc giữa các phần "trang trí".

### Bài 5: `__name__` sau khi trang trí

* **Đề bài:** Trang trí hàm `tong(a, b)` bằng decorator `trang_tri` KHÔNG dùng `@wraps`. In ra `tong.__name__` sau khi trang trí. **Viết chương trình để chứng minh** kết quả.
* **Input:** Không có
* **Output (dòng đầu có thể khác — chỉ cần đúng bản chất):**
  ```
  ham_moi
  ```
* **Gợi ý:** Hàm mới thay thế hàm cũ nên mang tên của hàm bên trong.

### Bài 6: Decorator gọi hàm nhiều lần

* **Đề bài:** Viết decorator `chao_py(so_lan)` — decorator **có đối số** — gọi hàm gốc đúng `so_lan` lần. Áp dụng `@chao_py(2)` cho hàm `in_polo()` in `"Polo!"`.
* **Input:** Không có
* **Output:**
  ```
  Polo!
  Polo!
  ```
* **Gợi ý:** Decorator có đối số gồm BA tầng hàm lồng nhau.

### Bài 7: Dùng `@wraps`

* **Đề bài:** Trang trí hàm `in_ten()` bằng decorator `giu_ten()` CÓ `@wraps`. In ra `in_ten.__name__` và `in_ten.__doc__` (tài liệu).
* **Input:** Không có
* **Output:**
  ```
  in_ten
  Hàm in tên.
  ```
* **Gợi ý:** `from functools import wraps`; ghi docstring `"""Hàm in tên."""` trong thân hàm.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Decorator đo thời gian

* **Đề bài:** Viết decorator `do_gio` in ra `"{tên hàm} mất {x:.4f} giây"` khi chạy `tinh_tong(10_000_000)` (tính tổng các số từ 0 đến n).
* **Input:** Không có
* **Output (số giây thay đổi tùy máy):**
  ```
  tinh_tong mất 0.6000 giây
  ```
* **Gợi ý:** `import time`, lấy `time.time()` trước và sau khi gọi hàm gốc.

### Bài 9: Yêu cầu đăng nhập

* **Đề bài:** Tạo biến toàn cục `co_phien_moi = True`. Decorator `can_dang_nhap()` nếu `not co_phien_moi` in `"Cần đăng nhập"` và trả về `None`; ngược lại chạy hàm gốc. Áp dụng cho hàm `xem_ho_so()` in thông tin hồ sơ.
* **Input:** Không có
* **Output:**
  ```
  Ho so: An - lop 10A1
  ```
* **Gợi ý:** `if not co_phien_moi: print("Cần đăng nhập"); return None`.

### Bài 10: Đếm số lần gọi hàm

* **Đề bài:** Decorator `dem_lan` đếm số lần gọi và in `"Số lần: {n}"`. Gọi hàm `@dem_lan gioi_thieu()` 3 lần.
* **Input:** Không có
* **Output:**
  ```
  Số lần: 1
  Số lần: 2
  Số lần: 3
  ```
* **Gợi ý:** Gắn biến đếm lên chính hàm: khởi tạo `ham_moi.so_lan = 0` rồi tăng mỗi lần gọi.

### Bài 11: Bọc kết quả thành chữ in hoa

* **Đề bài:** Viết decorator `in_hoa()` trang trí hàm `cau_hoi()` (trả về chuỗi `"Do you want to quit?"` viết thường) sao cho khi gọi, kết quả được in HOA toàn bộ.
* **Input:** Không có
* **Output:**
  ```
  DO YOU WANT TO QUIT?
  ```
* **Gợi ý:** `ket_qua = ham(); return ket_qua.upper()` — chú ý hàm gốc phải `return` chuỗi.

### Bài 12: Kiểm tra số âm

* **Đề bài:** Hàm `tinh_binh_phuong(x)` trả về `x * x`. Decorator `kiem_tra_am()` — nếu `x` âm in `"Số âm không hợp lệ"` và trả về `None`; ngược lại chạy hàm gốc. Gọi với `-3` và với `4`.
* **Input:** Không có
* **Output:**
  ```
  Số âm không hợp lệ
  16
  ```
* **Gợi ý:** Trong decorator kiểm tra `args[0] < 0`.

### Bài 13: Log tên hàm đang chạy

* **Đề bài:** Viết decorator `ghi_ten()` in `"Đang chạy: {tên hàm}"` trước khi gọi hàm gốc. Áp dụng cho hai hàm `foo()` (in `"foo đang chạy"`) và `bar()` (in `"bar đang chạy"`).
* **Input:** Không có
* **Output:**
  ```
  Đang chạy: foo
  foo đang chạy
  Đang chạy: bar
  bar đang chạy
  ```
* **Gợi ý:** Dùng `ham.__name__` lấy tên hàm; dùng `@ghi_ten` lên cả hai hàm.

### Bài 14: Decorator xử lý chia cho 0

* **Đề bài:** Hàm `chia(a, b)` trả về `a / b`. Viết decorator `an_toan_chia()` — nếu `b == 0` in `"Lỗi chia cho 0!"` và trả về `None`; ngược lại chạy hàm gốc. Gọi `chia(10, 2)` và `chia(10, 0)`.
* **Input:** Không có
* **Output:**
  ```
  5.0
  Lỗi chia cho 0!
  ```
* **Gợi ý:** Kiểm tra `args[1] == 0` trước khi `return ham(*args, **kwargs)`.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Decorator báo cáo có tên sự kiện

* **Đề bài:** Viết decorator `bao_cao(ten_su_kien)` — **có đối số** — in `"Bắt đầu {tên_sự_kiện}"`, chạy hàm gốc, rồi in `"Kết thúc {tên_sự_kiện}"`. Áp dụng `@bao_cao("xử lý")` cho hàm `xu_ly()` in `"Đang xử lý..."`.
* **Input:** Không có
* **Output:**
  ```
  Bắt đầu xử lý
  Đang xử lý...
  Kết thúc xử lý
  ```
* **Gợi ý:** Đây là decorator CÓ đối số — gồm ba tầng hàm lồng nhau.

### Bài 16: Xếp chồng hai decorator

* **Đề bài:** Tạo `f1` in `"F1 trước"` và `"F1 sau"` quanh hàm gốc; `f2` in `"F2 trước"` và `"F2 sau"`. Áp dụng:
  ```python
  @f2
  @f1
  def hang():
      print("Thân hàm")
  ```
* **Input:** Không có
* **Output:**
  ```
  F2 trước
  F1 trước
  Thân hàm
  F1 sau
  F2 sau
  ```
* **Gợi ý:** Decorator ở dưới (gần hàm nhất) áp dụng trước → `f1` bọc trong `f2`.

### Bài 17: Bộ nhớ đệm (cache) kết quả

* **Đề bài:** Viết decorator `bo_nho_dem()` lưu kết quả vào dictionary theo từng tham số. Hàm `binh_phuong(n)` trả về `n * n`. Gọi hai lần với `n = 5`: lần đầu phải tính toán (in `"Tính toán"`), lần thứ hai lấy từ cache (in `"Lấy từ cache"`).
* **Input:** Không có
* **Output:**
  ```
  Tính toán
  25
  Lấy từ cache
  25
  ```
* **Gợi ý:** Dùng dict nằm ngoài closure; nếu tham số đã có trong dict thì trả luôn, không gọi hàm gốc.

### Bài 18: Kiểm tra kiểu dữ liệu tham số

* **Đề bài:** Viết decorator `kiem_tra_kieu()` — trước khi chạy kiểm tra `isinstance(args[0], int)`, nếu không phải in `"Cần số nguyên"` và trả về `None`. Áp dụng cho hàm `tong_tu_0(n)` trả về tổng `0 + 1 + ... + n`. Gọi với `3` và với `"abc"`.
* **Input:** Không có
* **Output:**
  ```
  6
  Cần số nguyên
  ```
* **Gợi ý:** `sum(range(n + 1))` tính tổng từ 0 đến n.

### Bài 19: Log đầy đủ tham số và kết quả

* **Đề bài:** Viết decorator `ghi_log()` in một dòng: `"gọi {tên} args={args} kwargs={kwargs} -> {kết quả}"`. Áp dụng cho hàm `mua_hang(loai, so_tien=100000)` trả về chuỗi xác nhận. Gọi `mua_hang("trà", so_tien=500000)`.
* **Input:** Không có
* **Output (dạng log):**
  ```
  gọi mua_hang args=('trà',) kwargs={'so_tien': 500000} -> Đã mua trà
  Đã mua trà
  ```
* **Gợi ý:** Gọi `ket_qua = ham(*args, **kwargs)` rồi in trước khi `return ket_qua`.

### Bài 20: Kết hợp đếm lần gọi và đo thời gian

* **Đề bài:** Tạo hai decorator: `dem_lan()` (in `"Lần gọi thứ {n}"`) và `do_gio()` (in `"Đang chạy {tên}, tốn {x:.4f} giây"`). Xếp chồng để mỗi lần gọi hàm `hoc_tap()` (in `"Học bài"`) đều hiện đủ: dòng đo thời gian, dòng số lần gọi, rồi dòng nội dung. Gọi hàm 2 lần.
* **Input:** Không có
* **Output (dạng — giây thay đổi tùy máy):**
  ```
  Đang chạy hoc_tap, tốn 0.0000 giây
  Lần gọi thứ 1
  Học bài
  Đang chạy hoc_tap, tốn 0.0000 giây
  Lần gọi thứ 2
  Học bài
  ```
* **Gợi ý:** Thử thứ tự `@do_gio` và `@dem_lan` xem thứ tự nào cho kết quả trên — decorator gần hàm nhất áp dụng trước.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Thành thạo hàm bậc cao, closure và decorator cú pháp `@`.
* ✅ Phân biệt decorator không đối số và có đối số.
* ✅ Giữ danh tính hàm bằng `@wraps`, truyền tham số linh hoạt bằng `*args/**kwargs`.
* ✅ Áp dụng decorator cho log, đếm, cache, kiểm tra dữ liệu — đúng kiểu "trang trí" mà các framework web (Flask, Django) dùng!

> 💪 Chưa tự làm được bài nào thì đừng lo — đọc lại bài giảng, xem từng dòng code chậm lại, rồi thử lại. **Lập trình là luyện tập.**

---

## ✅ Đáp án

> 💡 **Hãy tự làm bài tập trước** rồi mới mở đáp án.

## 🟢 Dễ (Bài 1 – 7)


<details>
<summary>✅ Bài 1: Hàm trong biến</summary>


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

</details>

<details>
<summary>✅ Bài 2: Truyền hàm vào hàm</summary>


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

</details>

<details>
<summary>✅ Bài 3: Hàm trả về hàm</summary>


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

</details>

<details>
<summary>✅ Bài 4: Decorator in dấu hoa thị</summary>


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

</details>

<details>
<summary>✅ Bài 5: `__name__` sau khi trang trí</summary>


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

</details>

<details>
<summary>✅ Bài 6: Decorator gọi hàm nhiều lần</summary>


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

</details>

<details>
<summary>✅ Bài 7: Dùng `@wraps`</summary>


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

</details>

## 🟡 Trung bình (Bài 8 – 14)


<details>
<summary>✅ Bài 8: Decorator đo thời gian</summary>


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

</details>

<details>
<summary>✅ Bài 9: Yêu cầu đăng nhập</summary>


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

</details>

<details>
<summary>✅ Bài 10: Đếm số lần gọi hàm</summary>


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

</details>

<details>
<summary>✅ Bài 11: Bọc kết quả thành chữ in hoa</summary>


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

</details>

<details>
<summary>✅ Bài 12: Kiểm tra số âm</summary>


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

</details>

<details>
<summary>✅ Bài 13: Log tên hàm đang chạy</summary>


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

</details>

<details>
<summary>✅ Bài 14: Decorator xử lý chia cho 0</summary>


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

</details>

## 🔴 Khó (Bài 15 – 20)


<details>
<summary>✅ Bài 15: Decorator báo cáo có tên sự kiện</summary>


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

</details>

<details>
<summary>✅ Bài 16: Xếp chồng hai decorator</summary>


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

</details>

<details>
<summary>✅ Bài 17: Bộ nhớ đệm (cache) kết quả</summary>


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

</details>

<details>
<summary>✅ Bài 18: Kiểm tra kiểu dữ liệu tham số</summary>


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

</details>

<details>
<summary>✅ Bài 19: Log đầy đủ tham số và kết quả</summary>


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

</details>

<details>
<summary>✅ Bài 20: Kết hợp đếm lần gọi và đo thời gian</summary>


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

</details>

## 📌 Lời khuyên cuối


* Decorator = **nhận hàm → trả hàm mới**; cứ giữ khung này là viết đúng.
* Luôn `@wraps(ham)` và `*args/**kwargs` để decorator hoạt động với hàm bất kỳ.
* Decorator có đối số cần **ba tầng** hàm; đừng nhầm với loại không đối số.
* Khi xếp chồng, đọc từ **dưới lên** để biết thứ tự áp dụng.
* Trong dự án thật, các framework (Flask `@app.route`, Django `@login_required`) dùng decorator liên tục — giờ bạn đã hiểu chúng hoạt động ra sao!

👉 Tiếp theo: **[Bài 29: Iterator](../29-Iterator/bai.md)**

---

## ➡️ Điều hướng

**Vị trí:** `02-Thuat-Toan/Phan-1-Co-Ban/28-Decorator/bai.md`

**Bài tiếp theo:** [Bài 29 — Iterator – Vòng Lặp Hoạt Động Thế Nào?](../29-Iterator/bai.md)
