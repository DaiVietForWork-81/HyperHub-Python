# ✅ Bài 37: Đáp Án – Logging

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án để việc học hiệu quả nhất.
>
> 📌 **Lưu ý chung:** Các đáp án chạy được với Python 3.9+, không cần thư viện ngoài. Ở máy thật, màn hình có thể hiển thị định dạng thời gian theo hệ thống của bạn.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Dòng log đầu tiên

**Phân tích:** Ghi một log INFO với cấu hình mặc định.

**Ý tưởng:** Chỉ cần `import logging` và gọi `logging.info()`.

**Thuật toán:**
1. Import module logging.
2. Gọi `logging.info("...")`.

**Code:**

```python
import logging

logging.info("Chao mung ban den voi Python logging.")
```

**Giải thích code:**
- `logging.info(...)` ghi log mức INFO.
- Vì mặc định ngưỡng là WARNING, dòng này **không được in ra** — đây chính là bài học đầu tiên về ngưỡng log.

**Độ phức tạp:** O(1).

---

### Bài 2: Ghi cả năm mức

**Phân tích:** So sánh hành vi hiển thị giữa "không cấu hình" và "level=DEBUG".

**Ý tưởng:** Viết 5 dòng ghi log; lần 1 không cấu hình, lần 2 cấu hình DEBUG.

**Thuật toán:**
1. Ghi 5 mức không cấu hình → chỉ thấy WARNING, ERROR, CRITICAL.
2. Thêm `basicConfig(level=logging.DEBUG)` → thấy đủ 5 dòng.

**Code:**

```python
import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("Day la dong DEBUG")
logging.info("Day la dong INFO")
logging.warning("Day la dong WARNING")
logging.error("Day la dong ERROR")
logging.critical("Day la dong CRITICAL")
```

**Giải thích code:**
- `level=logging.DEBUG` hạ ngưỡng xuống thấp nhất → mọi dòng đều hiển thị.
- Nếu bỏ dòng `basicConfig`, chỉ 3 dòng cuối (WARNING trở lên) hiện ra.

**Độ phức tạp:** O(1).

---

### Bài 3: Cấu hình hiển thị từ INFO

**Phân tích:** Ngưỡng INFO chặn DEBUG, cho phép INFO.

**Ý tưởng:** `basicConfig(level=logging.INFO)` trước khi ghi.

**Code:**

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.debug("Dong nay bi an")            # không hiện vì thấp hơn INFO
logging.info("Chuong trinh bat dau")       # hiện vì đúng mức INFO
print("Xong!")
```

**Giải thích code:**
- DEBUG (10) < INFO (20) → bị chặn.
- `print("Xong!")` hiển thị trên màn hình — minh họa sự khác biệt giữa print (kết quả) và log (nội bộ).

**Độ phức tạp:** O(1).

---

### Bài 4: Thêm thời gian vào log

**Phân tích:** Cần thẻ thời gian và định dạng ngày tháng Việt Nam.

**Ý tưởng:** Dùng `%(asctime)s` + `datefmt`.

**Code:**

```python
import logging

logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
)

logging.warning("Truy cap thanh cong.")
```

**Giải thích code:**
- `%(asctime)s` — thời điểm ghi log.
- `datefmt="%d/%m/%Y %H:%M:%S"` — hiển thị kiểu `05/08/2026 20:05:00` (ngày/tháng/năm giờ:phút:giây).

**Độ phức tạp:** O(1).

---

### Bài 5: Ghi log ra file

**Phân tích:** Chuyển hướng log vào file bằng `filename=`.

**Ý tưởng:** Thêm `filename` và `filemode="a"` vào `basicConfig`.

**Code:**

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="bai_tap.log",
    filemode="a",          # "a" = thêm tiếp vào cuối file
)

logging.info("Lan chay thu nhat")
logging.info("Lan chay thu hai")
```

**Giải thích code:**
- Có `filename=` thì log không in ra màn hình nữa — tất cả đổ vào `bai_tap.log`.
- `filemode="a"` giữ lại nội dung cũ; dùng `"w"` nếu muốn ghi đè.

**Độ phức tạp:** O(1).

---

### Bài 6: Log chào mừng người dùng ATM

**Phân tích:** Kết hợp `print()` cho người dùng và logging cho lập trình viên.

**Ý tưởng:** Cấu hình DEBUG để thấy cả INFO và DEBUG.

**Code:**

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

print("Chao mung ban den voi ATM!")
logging.info("Nguoi dung bat dau su dung ATM.")
logging.debug("Hien menu chinh.")
```

**Giải thích code:**
- `print(...)` — dòng chào cho người dùng nhìn thấy.
- `logging.info/debug(...)` — ghi "sổ trực" nội bộ.

**Độ phức tạp:** O(1).

---

### Bài 7: Tên module trong log

**Phân tích:** Đặt tên cho logger để biết log đến từ đâu.

**Ý tưởng:** `logging.getLogger("may_giat")` + `%(name)s` trong format.

**Code:**

```python
import logging

logger = logging.getLogger("may_giat")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)

logger.info("Bat dau giat.")
```

**Giải thích code:**
- `getLogger("may_giat")` tạo logger riêng.
- `%(name)s` hiển thị `may_giat` — khi chương trình có nhiều module, biết ngay log từ bộ phận nào.

**Độ phức tạp:** O(1).

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Format đầy đủ và ghi đè file

**Phân tích:** Thêm `%(lineno)d` (số dòng code) và dùng `filemode="w"`.

**Ý tưởng:** Cấu hình một lần với cả hai tùy chọn.

**Code:**

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(lineno)d | %(message)s",
    filename="dai_han.log",
    filemode="w",          # "w" = xóa nội dung cũ trước khi ghi
)

logging.info("Bien so = 5")
logging.info("Bien ten = An")
```

**Giải thích code:**
- `%(lineno)d` — số dòng code đang thực hiện lệnh ghi log (dòng 15, 16 trong file .py).
- `filemode="w"` — mỗi lần chạy file log được tạo mới nên chạy 2 lần file vẫn chỉ có 2 dòng.

**Độ phức tạp:** O(1).

---

### Bài 9: Log tên hàm đang chạy

**Phân tích:** Cần biết log xuất phát từ hàm nào — dùng `%(funcName)s`.

**Ý tưởng:** Đặt format và ghi log trong từng hàm.

**Code:**

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(funcName)s - %(message)s",
)


def tinh_tien(so_luong, don_gia):
    """Tính tiền và ghi log."""
    tong = so_luong * don_gia
    logging.info("Tinh tien %d x %d = %d", so_luong, don_gia, tong)
    return tong


def in_hoa_don():
    """In hóa đơn và ghi log."""
    logging.info("Bat dau in hoa don")


tinh_tien(3, 20000)
in_hoa_don()
```

**Giải thích code:**
- `%(funcName)s` tự động lấy tên hàm hiện tại (`tinh_tien`, `in_hoa_don`) — không cần ghi tay.
- Cách `logging.info("... %d", so)` truyền số liệu vào chuỗi format.

**Độ phức tạp:** O(1).

---

### Bài 10: Chia số bắt lỗi ghi ERROR

**Phân tích:** Chia cho 0 là lỗi toán học — ghi ERROR và trả `None`.

**Ý tưởng:** Kiểm tra `b == 0` trước khi chia.

**Code:**

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def chia(a, b):
    """Chia a cho b; ghi log ERROR nếu b = 0."""
    if b == 0:
        logging.error("Khong the chia cho 0")
        return None
    return a / b


for a, b in [(10, 2), (10, 0)]:
    ket_qua = chia(a, b)
    print(f"Ket qua {a} / {b} = {ket_qua}")
```

**Giải thích code:**
- `logging.error(...)` ghi đúng mức ERROR — chương trình vẫn tiếp tục chạy.
- Trả về `None` để hàm gọi biết kết quả "không hợp lệ".

**Độ phức tạp:** O(1).

---

### Bài 11: Đọc file không tồn tại

**Phân tích:** Lỗi file không có phải được bắt và ghi log.

**Ý tưởng:** `try/except FileNotFoundError` + `logging.error`.

**Code:**

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="loi_file.log",
    filemode="a",
)

ten_file = "khong_co_file.txt"
try:
    with open(ten_file, "r", encoding="utf-8") as f:
        noi_dung = f.read()
    print("Doc file thanh cong.")
except FileNotFoundError:
    logging.error("Khong mo duoc file: %s", ten_file)
    print("Khong mo duoc file.")
```

**Giải thích code:**
- Khối `with` tự đóng file nếu mở thành công.
- `logging.error("... %s", ten_file)` — truyền biến kiểu `%s`, đúng phong cách logging.

**Độ phức tạp:** O(1).

---

### Bài 12: Logger riêng trong module

**Phân tích:** Module con chỉ khai báo logger, không cấu hình; cấu hình tập trung ở main.

**Ý tưởng:** `logger = logging.getLogger("dich_vu")` trong module, `basicConfig` ngoài main.

**Code:**

```python
# file dich_vu.py
import logging

logger = logging.getLogger("dich_vu")


def kiem_tra_ngay(ngay):
    """Kiểm tra ngày trong tháng (1-31)."""
    if 1 <= ngay <= 31:
        logger.info("Ngay %d hop le", ngay)
        return True
    logger.warning("Ngay %d khong hop le", ngay)
    return False
```

```python
# file main.py
import logging

from dich_vu import kiem_tra_ngay

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)

kiem_tra_ngay(15)
kiem_tra_ngay(40)
```

**Giải thích code:**
- Module `dich_vu` dùng `getLogger("dich_vu")` — cấu hình (level, format) kế thừa từ cấu hình chung ở main.
- `%(name)s` hiển thị `dich_vu` giúp truy vết log đến đúng module.
- Nếu chạy `dich_vu.py` riêng lẻ, log không hiện (chưa có cấu hình) — hành vi đúng của logging.

**Độ phức tạp:** O(1).

---

### Bài 13: Đếm số lần nhập mật khẩu sai

**Phân tích:** Vòng lặp tối đa 3 lần; mỗi lần sai ghi WARNING.

**Ý tưởng:** Đếm bằng chỉ số vòng lặp, so sánh với mật khẩu đúng.

**Code:**

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

mat_khau_dung = "python123"

for lan in range(1, 4):
    # Nhập: abc (lần 1), xyz (lần 2), python123 (lần 3)
    mat_khau = input("Nhap mat khau: ")
    if mat_khau == mat_khau_dung:
        logging.info("Dang nhap thanh cong")
        print("Chao mung ban!")
        break
    logging.warning("Sai mat khau lan thu %d", lan)
else:
    logging.error("Da nhap sai 3 lan, khoa tai khoan")
    print("Tai khoan da bi khoa.")
```

**Giải thích code:**
- `range(1, 4)` chạy tối đa 3 lần; biến `lan` chính là số lần thử.
- `break` khi đúng — thoát vòng lặp sớm.
- Nhánh `else` của `for` chỉ chạy khi **không** có `break` — nghĩa là 3 lần đều sai.

**Độ phức tạp:** O(1) (tối đa 3 lần lặp).

---

### Bài 14: Kiểm tra tuổi truy cập

**Phân tích:** Phân loại theo tuổi: đủ 18 → INFO, dưới 18 → WARNING.

**Ý tưởng:** Hàm nhận tuổi, `if` rẽ hai nhánh log.

**Code:**

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def kiem_tra_do_tuoi(tuoi):
    """Kiểm tra tuổi truy cập nội dung."""
    if tuoi >= 18:
        logging.info("Do tuoi %d: cho phep truy cap", tuoi)
        return True
    logging.warning("Do tuoi chua du (%d tuoi)", tuoi)
    return False


kiem_tra_do_tuoi(20)
kiem_tra_do_tuoi(15)
```

**Giải thích code:**
- `tuoi >= 18` → INFO (sự kiện bình thường).
- ngược lại → WARNING (dưới ngưỡng nhưng chương trình vẫn chạy).
- Hàm trả `bool` để chương trình chính quyết định xử lý tiếp.

**Độ phức tạp:** O(1).

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Chương trình ATM hoàn chỉnh có log

**Phân tích:** Kết hợp menu, số dư và đủ loại log INFO/WARNING/CRITICAL.

**Ý tưởng:** Mỗi chức năng một hàm; đếm lựa chọn sai để phát CRITICAL.

**Thuật toán:**
1. Cấu hình log ra `atm.log`.
2. Vòng lặp menu.
3. Rút: đủ tiền → INFO; quá → WARNING.
4. Nạp: INFO.
5. Sai lựa chọn: đếm; lần thứ 3 → CRITICAL và dừng.

**Code:**

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(funcName)s - %(message)s",
    filename="atm.log",
    filemode="a",
)

so_du = 500000


def xem_so_du():
    """Hiển thị số dư."""
    print(f"So du hien tai: {so_du} dong")
    logging.info("Xem so du: %d dong", so_du)


def rut_tien():
    """Rút tiền với kiểm tra số dư."""
    global so_du
    so_tien = int(input("So tien can rut: "))
    if so_tien > so_du:
        logging.warning("Rut %d that bai: so du khong du (%d)", so_tien, so_du)
        print("Rut tien that bai: so du khong du!")
        return
    so_du -= so_tien
    logging.info("Rut %d thanh cong, con %d", so_tien, so_du)
    print(f"Rut tien thanh cong! Con {so_du} dong.")


def nap_tien():
    """Nạp tiền."""
    global so_du
    so_tien = int(input("So tien can nap: "))
    so_du += so_tien
    logging.info("Nap %d thanh cong, so du %d", so_tien, so_du)
    print(f"Nap thanh cong! So du: {so_du} dong.")


def chay_atm():
    """Vòng lặp chính của ATM."""
    dem_sai = 0
    while True:
        print("\n===== MENU ATM =====")
        print("1. Rut tien")
        print("2. Nap tien")
        print("3. Xem so du")
        print("4. Thoat")
        chon = input("Chon: ")
        if chon == "1":
            rut_tien()
        elif chon == "2":
            nap_tien()
        elif chon == "3":
            xem_so_du()
        elif chon == "4":
            print("Tam biet!")
            break
        else:
            dem_sai += 1
            logging.warning("Nhap sai lua chon lan %d", dem_sai)
            if dem_sai >= 3:
                logging.critical("Nhap sai qua 3 lan, khoa ATM")
                print("Ban da nhap sai qua 3 lan. ATM bi khoa.")
                break


if __name__ == "__main__":
    chay_atm()
```

**Giải thích code:**
- `global so_du` cho phép hàm đổi biến ngoài hàm (học ở bài 13).
- Rút quá số dư → WARNING: bất thường nhưng ATM vẫn chạy.
- Nhập sai 3 lần → CRITICAL: coi như nguy kịch, khóa ATM.
- Toàn bộ lịch sử ghi vào `atm.log` — ngân hàng có thể truy vết.

**Độ phức tạp:** O(1) cho mỗi thao tác.

---

### Bài 16: Hàm xử lý nhiều ngoại lệ

**Phân tích:** Phân loại dữ liệu thành 3 trường hợp với 3 mức log.

**Ý tưởng:** Kiểm tra kiểu và dấu của dữ liệu.

**Code:**

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="xu_ly.log",
    filemode="a",
)


def xu_ly_du_lieu(du_lieu):
    """Phân loại dữ liệu: dương, âm, không phải số."""
    if not isinstance(du_lieu, (int, float)):
        logging.error("Du lieu khong phai so: %s", du_lieu)
        return None
    if du_lieu < 0:
        logging.warning("So am %s: can kiem tra lai", du_lieu)
        return du_lieu
    logging.info("So duong hop le: %s", du_lieu)
    return du_lieu


xu_ly_du_lieu("abc")
xu_ly_du_lieu(-5)
xu_ly_du_lieu(10)
```

**Giải thích code:**
- `isinstance(du_lieu, (int, float))` — kiểm tra dữ liệu có phải số không.
- "abc" → ERROR (sai kiểu); -5 → WARNING (âm bất thường); 10 → INFO (bình thường).
- File `xu_ly.log` chứa 3 dòng với 3 mức khác nhau — ví dụ điển hình cho "khi nào dùng mức nào".

**Độ phức tạp:** O(1).

---

### Bài 17: Máy tính cầm tay có nhật ký

**Phân tích:** Ghi DEBUG cho mọi phép tính; ERROR riêng cho chia 0.

**Ý tưởng:** Hàm `tinh(a, b, phep_toan)` với rẽ nhánh 4 phép toán.

**Code:**

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="may_tinh.log",
    filemode="a",
)


def tinh(a, b, phep_toan):
    """Tính toán 4 phép cơ bản và ghi log."""
    if phep_toan == "/" and b == 0:
        logging.error("Phep chia cho 0: %d / %d", a, b)
        return None
    if phep_toan == "+":
        ket_qua = a + b
    elif phep_toan == "-":
        ket_qua = a - b
    elif phep_toan == "*":
        ket_qua = a * b
    else:
        ket_qua = a / b
    logging.debug("%d %s %d = %s", a, phep_toan, b, ket_qua)
    return ket_qua


tinh(10, 5, "+")
tinh(10, 5, "/")
tinh(10, 0, "/")
```

**Giải thích code:**
- Kiểm tra chia 0 **trước** khi tính.
- `logging.debug(...)` lưu mọi phép tính — ở mức DEBUG nên không làm rối file khi nâng ngưỡng lên INFO.

**Độ phức tạp:** O(1).

---

### Bài 18: Xử lý danh sách số từ file

**Phân tích:** Đọc file, xử lý từng dòng, ghi log kết quả, tính tổng số hợp lệ.

**Ý tưởng:** Duyệt từng dòng; `try/except ValueError` bắt dòng không phải số.

**Thuật toán:**
1. Mở file `so.txt`.
2. Với mỗi dòng: cố gắng `int()` — thành công ghi DEBUG và cộng dồn; thất bại ghi ERROR.
3. In tổng.

**Code:**

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

tong = 0
so_dong = 0

with open("so.txt", "r", encoding="utf-8-sig") as f:
    for dong in f:
        so_dong += 1
        gia_tri = dong.strip()
        try:
            so = int(gia_tri)
            tong += so
            logging.debug("Dong %d = %d", so_dong, so)
        except ValueError:
            logging.error("Dong %d khong phai so: %s", so_dong, gia_tri)

print("Tong cac so hop le:", tong)
```

**Giải thích code:**
- `encoding="utf-8-sig"` — an toàn với cả file có dấu BOM (Windows Notepad thường thêm BOM khi lưu UTF-8); không có BOM vẫn đọc tốt.
- `dong.strip()` bỏ ký tự xuống dòng cuối dòng.
- `int(gia_tri)` ném `ValueError` nếu không phải số → ghi ERROR và bỏ qua.
- Tổng chỉ cộng các số hợp lệ: 10 + 20 = 30.

**Độ phức tạp:** O(n) với n là số dòng trong file.

---

### Bài 19: Chặn log dữ liệu nhạy cảm

**Phân tích:** Log không bao giờ được chứa mật khẩu — kiểm tra bằng `assert`.

**Ý tưởng:** Chỉ đưa tên đăng nhập vào message; đọc lại file để xác minh.

**Code:**

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="bao_mat.log",
    filemode="a",
)


def dang_nhap(ten_dang_nhap, mat_khau):
    """Đăng nhập: log CHỈ tên đăng nhập, không bao giờ log mật khẩu."""
    logging.info("Nguoi dung %s dang nhap.", ten_dang_nhap)
    return ten_dang_nhap == "admin" and mat_khau == "bi_mat_123"


dang_nhap("admin", "bi_mat_123")

# Kiểm tra: mật khẩu không được xuất hiện trong file log
with open("bao_mat.log", "r", encoding="utf-8") as f:
    noi_dung = f.read()

assert "bi_mat_123" not in noi_dung, "LO: file log chua mat khau!"
print("Kiem tra thanh cong: mat khau khong bi ghi vao log.")
```

**Giải thích code:**
- Message log chỉ gồm `ten_dang_nhap` — `mat_khau` không bao giờ vào chuỗi log.
- `assert` là "kiểm tra tự động": nếu mật khẩu lọt vào file, chương trình báo lỗi ngay.
- Thói quen này cực kỳ quan trọng trong dự án thật (bảo mật thông tin).

**Độ phức tạp:** O(1).

---

### Bài 20: Hệ thống quản lý lớp học có log

**Phân tích:** Menu quản lý lớp; log INFO/WARNING/ERROR theo tình huống.

**Ý tưởng:** Danh sách học sinh trong list; kiểm tra tên trống (ERROR), không tìm thấy (WARNING).

**Thuật toán:**
1. Cấu hình log ra `lop_hoc.log`.
2. Thêm học sinh: tên trống → ERROR; khác → INFO.
3. Xóa học sinh: có trong lớp → INFO; không có → WARNING.
4. Xem danh sách và thoát.

**Code:**

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="lop_hoc.log",
    filemode="a",
)

lop = []


def them_hoc_sinh():
    """Thêm học sinh vào lớp."""
    ten = input("Ten hoc sinh: ")
    if ten.strip() == "":
        logging.error("Ten hoc sinh khong duoc bo trong")
        print("Ten khong hop le!")
        return
    lop.append(ten.strip())
    logging.info("Da them hoc sinh: %s", ten)
    print(f"Da them {ten}.")


def xoa_hoc_sinh():
    """Xóa học sinh khỏi lớp."""
    ten = input("Ten hoc sinh can xoa: ")
    if ten in lop:
        lop.remove(ten)
        logging.info("Da xoa hoc sinh: %s", ten)
        print(f"Da xoa {ten}.")
    else:
        logging.warning("Khong tim thay hoc sinh: %s", ten)
        print(f"Khong co hoc sinh {ten} trong lop.")


def xem_danh_sach():
    """In danh sách học sinh."""
    if not lop:
        print("Lop chua co hoc sinh.")
        return
    print("--- DANH SACH LOP ---")
    for i, ten in enumerate(lop, start=1):
        print(f"{i}. {ten}")


def menu():
    """Menu chính của chương trình."""
    while True:
        print("\n===== QUAN LY LOP HOC =====")
        print("1. Them hoc sinh")
        print("2. Xoa hoc sinh")
        print("3. Xem danh sach")
        print("4. Thoat")
        chon = input("Chon: ")
        if chon == "1":
            them_hoc_sinh()
        elif chon == "2":
            xoa_hoc_sinh()
        elif chon == "3":
            xem_danh_sach()
        elif chon == "4":
            print("Tam biet!")
            break
        else:
            print("Lua chon khong hop le.")


if __name__ == "__main__":
    menu()
```

**Giải thích code:**
- `ten.strip()` bỏ khoảng trắng hai đầu — tên chỉ toàn dấu cách bị coi là trống → ERROR.
- Xóa học sinh không tồn tại → WARNING (bất thường nhẹ, chương trình vẫn chạy).
- `enumerate(lop, start=1)` đánh số danh sách từ 1.

**Độ phức tạp:** O(n) khi tìm kiếm trong list.

---

## 📌 Lời khuyên cuối

* **Cấu hình một lần, dùng nhiều lần** — `basicConfig` chỉ gọi một lần duy nhất ở đầu chương trình.
* **Chọn mức theo ý nghĩa**, không theo cảm xúc: chương trình khởi động = INFO, dữ liệu lạ = WARNING, chức năng gãy = ERROR.
* **Kiểm tra file `.log`** sau mỗi lần chạy — đó là cách lập trình viên "đọc sổ trực" của chương trình.
* Trong bài 40 và 41 (dự án), bạn sẽ thấy logging xuất hiện ở các chương trình quản lý thực tế — hãy tái sử dụng các mẫu này!

👉 Tiếp theo: **[Bài 38: Type Hints – Bài giảng](../38_Typing/bai_giang.md)** | **[Bài 38: Type Hints – Bài tập](../38_Typing/bai_tap.md)**
