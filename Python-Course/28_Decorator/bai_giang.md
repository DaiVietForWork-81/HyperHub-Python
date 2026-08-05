# 🎀 Bài 28: Decorator – Trang Trí Cho Hàm

> 🎓 **Chương 9 – Lập trình nâng cao**
> Từ bài 25 đến bài 29, chúng ta học những kỹ thuật lập trình "cao cấp" để viết code gọn gàng và chuyên nghiệp: lambda, list comprehension, generator, decorator, iterator. Bài 27 đã dạy bạn **generator** — cách tạo ra chuỗi giá trị chậm rãi, tiết kiệm bộ nhớ. Bài này, chúng ta học **decorator** — "phụ kiện" gắn thêm cho hàm mà không phải sửa chính hàm đó.

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

## 🏁 Kết thúc bài

🎉 Bạn đã biết cách "trang trí" hàm bằng decorator — một công cụ mạnh mẽ của Python. Nhưng có một khái niệm rất gần gũi mà chúng ta vẫn "lờ mờ": **vòng lặp `for` thực sự chạy thế nào bên trong?** Câu trả lời nằm ở **iterator** — người anh em sinh đôi với generator đã học. Hãy sang:

👉 **[Bài 29: Iterator – Vòng lặp hoạt động thế nào](../29_Iterator/bai_giang.md)**
