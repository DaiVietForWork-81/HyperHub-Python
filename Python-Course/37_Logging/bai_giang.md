# 🐍 Bài 37: Logging – Ghi Nhật Ký Hoạt Động Chương Trình

> 🎓 **Chương 8 – Lập trình ứng dụng chuyên sâu**

---

## 🎯 Mục tiêu

Sau bài học này, học viên sẽ:

* ✅ Hiểu **log là gì** và vì sao chương trình thật cần log thay vì chỉ `print()`.
* ✅ Biết **5 mức độ log** (DEBUG, INFO, WARNING, ERROR, CRITICAL) và khi nào dùng mức nào.
* ✅ Cấu hình logging bằng **`logging.basicConfig()`**: mức, định dạng, ghi ra file.
* ✅ Viết log **trong nhiều module** bằng `logging.getLogger(__name__)`.
* ✅ Xây dựng chương trình **mô phỏng ATM** và **đọc file an toàn** có ghi log.

---

## 📖 Kiến thức

> 🔁 **Nhắc lại bài trước:** Bài 36 đã cho bạn cơ sở dữ liệu SQLite để lưu dữ liệu. Nhưng còn một thứ quan trọng nữa: làm sao biết **chương trình đang hoạt động ra sao, lỗi xảy ra lúc nào**? Đó là việc của **logging** — và hôm nay chúng ta học nó.

### 1. Log là gì?

> 💬 **Nói đơn giản:** Log (nhật ký) là **ghi lại lịch sử hoạt động của chương trình** — lúc chạy, làm gì, gặp gì, lỗi gì — kèm theo **thời gian**.

**Ví dụ đời thực:**

* ✈️ **Hộp đen máy bay** ghi lại mọi hoạt động của chuyến bay — khi sự cố, người ta xem hộp đen để biết chuyện gì đã xảy ra.
* 🏫 **Sổ trực của bảo vệ**: ghi ai vào, lúc nào, việc gì — đến cuối tháng dễ dàng rà soát.
* 🛒 **Nhật ký của app đặt đồ ăn**: "19:02 người dùng đặt món X", "19:05 thanh toán thành công", "19:06 lỗi gửi SMS — thử lại"...

Chương trình Python cũng cần cuốn "sổ trực" như vậy — module `logging` là công cụ để viết.

### 2. Vì sao không chỉ dùng `print()`?

| Tiêu chí | `print()` | `logging` |
|---|---|---|
| 👀 Mục đích | Hiển thị kết quả **cho người dùng** | Ghi lại sự kiện **cho lập trình viên** |
| 🕒 Thời gian | Không kèm thời gian | Có timestamp (giờ, ngày) chính xác |
| 🚦 Mức độ | Không phân biệt | 5 mức: DEBUG → CRITICAL |
| 📄 Lưu trữ | Chỉ ra màn hình | Ghi ra **file** để xem lại sau |
| 🔕 Tắt/bật | Phải sửa code, xóa từng dòng | Chỉ cần đổi 1 dòng cấu hình |
| 🧩 Người dùng | In lộn xộn chung với "chương trình chính" | Tách riêng, có tên module |

> 💡 **Quy tắc thực tế:** `print()` dành cho **kết quả** người dùng thấy (ví dụ "Tổng tiền: 50.000đ"). `logging` dành cho **câu chuyện nội bộ** của chương trình.

### 3. Năm mức độ log

```mermaid
flowchart LR
    A[DEBUG<br/>10 - chi tiết nhất] --> B[INFO<br/>20 - thông tin thường]
    B --> C[WARNING<br/>30 - cảnh báo]
    C --> D[ERROR<br/>40 - lỗi có thể xử lý]
    D --> E[CRITICAL<br/>50 - nguy kịch]
```

| Mức | Giá trị | Ý nghĩa | Ví dụ |
|---|---|---|---|
| `DEBUG` | 10 | Chi tiết kỹ thuật khi gỡ lỗi | "Đang đọc dòng 5 của file..." |
| `INFO` | 20 | Sự kiện bình thường | "Đăng nhập thành công" |
| `WARNING` | 30 | Có gì đó hơi sai, vẫn chạy được | "Mật khẩu yếu", "Sắp hết bộ nhớ" |
| `ERROR` | 40 | Lỗi, chức năng bị lỗi nhưng chương trình sống | "Không đọc được file" |
| `CRITICAL` | 50 | Sự cố nghiêm trọng, chương trình sắp sập | "Không kết nối được máy chủ, dừng hệ thống" |

> 🧠 **Mẹo ghi nhớ:** DEBUG dành cho lúc **mò kim đáy bể**, CRITICAL dành cho lúc **cháy nhà**. Mức càng cao, độ nghiêm trọng càng lớn, số càng to.

### 4. Mức mặc định và mức tối thiểu

Mặc định, logging chỉ hiển thị từ **WARNING trở lên** — các dòng DEBUG, INFO bị "im lặng". Ta đổi ngưỡng bằng `basicConfig(level=...)`:

```python
import logging

# Chỉ chấp nhận từ INFO trở lên
logging.basicConfig(level=logging.INFO)

logging.debug("Chi tiết khi gỡ lỗi")     # bị bỏ qua
logging.info("Chương trình khởi động")   # hiện ra
```

### 5. `basicConfig` – cấu hình một lần

```python
logging.basicConfig(
    level=logging.INFO,                    # ngưỡng tối thiểu
    format="%(asctime)s | %(levelname)s | %(message)s",   # định dạng
    datefmt="%d/%m/%Y %H:%M:%S",           # định dạng thời gian
    filename="app.log",                    # ghi ra file
    filemode="a",                          # "a" = thêm vào file ("w" = ghi đè)
)
```

**Các thẻ định dạng `%(...)s` thông dụng:**

| Thẻ | Ý nghĩa | Ví dụ hiển thị |
|---|---|---|
| `%(asctime)s` | Thời gian ghi | `2026-08-05 19:30:15,123` |
| `%(levelname)s` | Tên mức độ | `INFO`, `ERROR` |
| `%(message)s` | Nội dung log | `Đăng nhập thành công` |
| `%(name)s` | Tên logger (thường là tên module) | `main`, `atm` |
| `%(lineno)d` | Số dòng code ghi log | `42` |
| `%(funcName)s` | Tên hàm đang chạy | `rut_tien` |

### 6. Ghi log ra file

Thêm `filename="app.log"` vào `basicConfig` — mọi log tự động đổ vào file, màn hình **không còn** hiển thị:

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log",
    filemode="a",
)

logging.info("Ghi vào file app.log")
```

> 🗂️ Muốn **vừa ra file vừa ra màn hình**, phải dùng kỹ thuật nâng cao `FileHandler` + `StreamHandler` (xem Mẹo cuối bài).

### 7. Logging trong nhiều module

Chương trình thật chia thành nhiều file. Mỗi file nên tạo logger riêng mang tên mình:

```python
import logging

# Logger riêng của module này
logger = logging.getLogger(__name__)

logger.info("Đây là log từ module này")
```

* `getLogger(__name__)` — `__name__` tự động mang tên module (vd `atm`, `main`), giúp biết log đến từ đâu.
* Quy ước: dùng `logger = logging.getLogger(__name__)` và gọi `logger.info(...)` chứ không dùng `logging.info(...)` trực tiếp — dễ phân biệt nguồn gốc log.

### 8. Khi nào dùng mức nào?

* **DEBUG** — khi đang viết code, muốn nhìn chi tiết từng bước; sau khi xong thì tắt (nâng ngưỡng lên INFO).
* **INFO** — các sự kiện quan trọng vừa đủ: "khởi động", "đăng nhập", "lưu file thành công".
* **WARNING** — tình huống bất thường chưa gây lỗi: "tuổi < 18", "số lượng tồn kho thấp".
* **ERROR** — một chức năng thất bại: "không mở được file", "sai mật khẩu lần 3".
* **CRITICAL** — chương trình không thể tiếp tục: "mất kết nối cơ sở dữ liệu".

---

## 💡 Ví dụ minh họa

### Ví dụ 1: Log đầu tiên với 5 mức

```python
import logging

# Cấu hình hiển thị từ DEBUG trở lên, kèm thời gian
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%H:%M:%S",
)

# Ghi cả 5 mức
logging.debug("Giá trị biến x = 5")
logging.info("Chương trình bắt đầu chạy")
logging.warning("Sắp hết bộ nhớ")
logging.error("Không mở được file du_lieu.txt")
logging.critical("Mất kết nối máy chủ, dừng hệ thống!")
```

Kết quả (thời gian sẽ khác):

```
19:30:15 | DEBUG | Giá trị biến x = 5
19:30:15 | INFO | Chương trình bắt đầu chạy
19:30:15 | WARNING | Sắp hết bộ nhớ
19:30:15 | ERROR | Không mở được file du_lieu.txt
19:30:15 | CRITICAL | Mất kết nối máy chủ, dừng hệ thống!
```

**Giải thích từng dòng:**

| Dòng code | Ý nghĩa |
|---|---|
| `basicConfig(level=logging.DEBUG, ...)` | Cho hiện cả 5 mức (mặc định từ WARNING) |
| `format="%(asctime)s | %(levelname)s | %(message)s"` | Mỗi log có 3 phần: thời gian, mức, nội dung |
| `logging.debug/info/warning/error/critical(...)` | 5 hàm tương ứng 5 mức |

### Ví dụ 2: So sánh `print()` và log ra file

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="chao_hoi.log",   # ghi vào file
    filemode="a",              # thêm tiếp vào file cũ
)

print("Xin chào! Bạn đã bước vào chương trình.")   # người dùng thấy trên màn hình
logging.info("Người dùng khởi động chương trình")  # lập trình viên thấy trong file
```

**Giải thích từng dòng:**

| Dòng code | Ý nghĩa |
|---|---|
| `print("Xin chào...")` | Hiển thị cho người dùng — đây là "kết quả" |
| `logging.info(...)` | Ghi "sổ trực": ai, lúc nào khởi động — không in ra màn hình |
| Mở file `chao_hoi.log` | Sẽ thấy dòng: `2026-08-05 19:31:00 - INFO - Người dùng khởi động chương trình` |

### Ví dụ 3: Log lỗi đọc file an toàn

```python
import logging

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

ten_file = "du_lieu.txt"
try:
    with open(ten_file, "r", encoding="utf-8") as f:
        noi_dung = f.read()
    print("Đọc file thành công,", len(noi_dung), "ký tự.")
except FileNotFoundError:
    logging.error("Khong tim thay file %s", ten_file)
```

Kết quả (khi file không tồn tại):

```
2026-08-05 19:32:10 - ERROR - Khong tim thay file du_lieu.txt
```

**Giải thích từng dòng:**

| Dòng code | Ý nghĩa |
|---|---|
| `level=logging.ERROR` | Chỉ ghi từ ERROR — INFO/DEBUG không cần thiết |
| `try/except FileNotFoundError` | Bắt đúng lỗi file không tồn tại (học ở bài 19) |
| `logging.error("... %s", ten_file)` | Cách truyền biến: để `%s` trong chuỗi, biến để sau — đừng nối bằng `+` |

> 💡 Lưu ý kỹ thuật nhỏ: `logging.error("... %s", ten_file)` an toàn hơn `logging.error("... " + ten_file)` — đúng với mọi kiểu dữ liệu và chậm hơn không đáng kể.

---

## 🔬 Ví dụ nâng cao

### Ví dụ 1: Chương trình ATM có ghi log đầy đủ

```python
import logging

# Cấu hình log ghi ra file
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(funcName)s | %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
    filename="atm.log",
    filemode="a",
)

so_du = 500000


def rut_tien(so_tien):
    """Rút tiền: thành công ghi INFO, thất bại ghi ERROR."""
    global so_du
    if so_tien > so_du:
        logging.error("Rut %d that bai: so du khong du (con %d)", so_tien, so_du)
        return False
    so_du -= so_tien
    logging.info("Rut %d thanh cong. So du con: %d", so_tien, so_du)
    return True


def nap_tien(so_tien):
    """Nạp tiền ghi INFO."""
    global so_du
    so_du += so_tien
    logging.info("Nap %d thanh cong. So du: %d", so_tien, so_du)


# Chạy thử
nap_tien(200000)          # INFO: nạp tiền
rut_tien(100000)          # INFO: rút thành công
rut_tien(900000)          # ERROR: không đủ tiền
```

Nội dung file `atm.log` sau khi chạy:

```
05/08/2026 19:35:00 | INFO | nap_tien | Nap 200000 thanh cong. So du: 700000
05/08/2026 19:35:00 | INFO | rut_tien | Rut 100000 thanh cong. So du con: 600000
05/08/2026 19:35:01 | ERROR | rut_tien | Rut 900000 that bai: so du khong du (con 600000)
```

**Phân tích:**

* Log có **giờ, mức, tên hàm, nội dung** — đủ dữ kiện để dựng lại "câu chuyện" của chương trình.
* Ngân hàng thật dùng log kiểu này để điều tra khiếu nại: "19:35:01 khách rút 900.000 nhưng tài khoản chỉ còn 600.000 — đúng luật".

### Ví dụ 2: Log lỗi đọc nhiều file (đọc file cấu hình)

```python
import logging
import json

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)

logger = logging.getLogger("cau_hinh")


def doc_cau_hinh(ten_file):
    """Đọc file JSON cấu hình; lỗi thì ghi log và trả về cấu hình mặc định."""
    mac_dinh = {"ten": "Khach hang", "gia": 1000}
    try:
        with open(ten_file, "r", encoding="utf-8") as f:
            du_lieu = json.load(f)
        logger.info("Doc cau hinh %s thanh cong", ten_file)
        return du_lieu
    except FileNotFoundError:
        logger.warning("Khong tim thay %s, dung cau hinh mac dinh", ten_file)
    except json.JSONDecodeError:
        logger.error("File %s bi loi dinh dang JSON", ten_file)
    return mac_dinh


# Chạy thử
cfg = doc_cau_hinh("khong_co_file.json")
print("Cấu hình đang dùng:", cfg)
```

Kết quả:

```
2026-08-05 19:36:22 - WARNING - cau_hinh - Khong tim thay khong_co_file.json, dung cau hinh mac dinh
Cấu hình đang dùng: {'ten': 'Khach hang', 'gia': 1000}
```

**Phân tích:**

* Chương trình **không sập** khi thiếu file — ghi WARNING rồi chạy tiếp với giá trị mặc định.
* `%(name)s` hiển thị tên logger `cau_hinh` — biết log thuộc module nào.
* File JSON lỗi định dạng (bài 32) thì ghi ERROR.

---

## ⚠️ Lỗi thường gặp

### Lỗi 1: Ghi DEBUG/INFO nhưng không thấy hiện ra

```python
import logging
logging.basicConfig(level=logging.WARNING)   # ngưỡng mặc định
logging.debug("chi tiet")      # ❌ không hiện
logging.info("thong tin")      # ❌ không hiện
logging.warning("canh bao")    # ✅ hiện
```

* **Nguyên nhân:** Ngưỡng mặc định là WARNING — các mức thấp hơn bị chặn.
* **Cách sửa:** `basicConfig(level=logging.DEBUG)` (hoặc INFO) để hạ ngưỡng.

### Lỗi 2: Ghi ra file nhưng không thấy file/màn hình trống

* **Nguyên nhân:** Khi đã khai `filename=` trong `basicConfig`, log chỉ vào file, không in ra màn hình.
* **Cách sửa:** Mở file log để xem, hoặc thêm cả `StreamHandler` (xem Mẹo) nếu muốn song song.

### Lỗi 3: `basicConfig` không có hiệu lực

```python
import logging
logging.basicConfig(level=logging.DEBUG)   # gọi lần 1
# ... code khác ...
logging.basicConfig(level=logging.ERROR)   # ❌ lần 2 KHÔNG tác dụng
```

* **Nguyên nhân:** `basicConfig` chỉ có tác dụng **một lần đầu tiên**; gọi lần sau bị bỏ qua im lặng.
* **Cách sửa:** Gọi cấu hình **duy nhất một lần** ở đầu chương trình (thường trong `main` hoặc module chính).

### Lỗi 4: Log nội dung nhạy cảm

```python
logging.info("Mat khau: %s", mat_khau)   # ❌ KHÔNG BAO GIỜ log mật khẩu
```

* **Nguyên nhân:** File log có thể bị đọc lại, bị gửi cho bộ phận hỗ trợ.
* **Cách sửa:** Chỉ log "Đã xác thực thành công cho user abc", không kèm mật khẩu, thẻ tín dụng, CCCD.

### Lỗi 5: Dùng `+` để nối dữ liệu log

```python
logging.error("Loi: " + ten_file + " gia tri: " + str(so))   # ❌ khó đọc, dễ lỗi kiểu
logging.error("Loi: %s gia tri: %d", ten_file, so)           # ✅ chuẩn của logging
```

* **Cách sửa:** Dùng chuỗi định dạng `%s`, `%d` và truyền giá trị sau dấu phẩy — đây là phong cách chính thức của logging.

---

## 💎 Mẹo

* 🏗️ **Gọi `basicConfig` một lần duy nhất** — thường đặt trong `if __name__ == "__main__":` trước khi gọi hàm chính.
* 🧩 **Mỗi module một logger riêng**: `logger = logging.getLogger(__name__)` rồi dùng `logger.xxx(...)`.
* 🚦 **Quy tắc ngón tay:** DEBUG = dành cho chính bạn khi gỡ lỗi; INFO = sự kiện bình thường; WARNING/ERROR/CRITICAL = vấn đề.
* 🗂️ Muốn **vừa file vừa màn hình** (không dùng thư viện ngoài):

  ```python
  import logging, sys

  logging.basicConfig(
      level=logging.INFO,
      format="%(asctime)s - %(levelname)s - %(message)s",
      handlers=[
          logging.FileHandler("app.log", encoding="utf-8"),
          logging.StreamHandler(sys.stdout),
      ],
  )
  ```

* 🔐 **Không bao giờ log** mật khẩu, số thẻ, mã PIN.
* 📏 Trong chương trình nhỏ vẫn nên dùng logging thay `print()` cho phần "nội bộ" — thói quen này chuẩn bị cho bạn làm việc nhóm, dự án thật.
* 🧹 Trước khi "giao" chương trình, nâng ngưỡng lên INFO hoặc WARNING để không đổ quá nhiều DEBUG vào file.

---

## 📝 Tóm tắt

| Khái niệm | Nội dung |
|---|---|
| 📒 Log | Nhật ký hoạt động của chương trình kèm thời gian |
| 🆚 So với `print()` | Log có mức độ, thời gian, ghi file, bật/tắt dễ |
| 🚦 5 mức | DEBUG(10), INFO(20), WARNING(30), ERROR(40), CRITICAL(50) |
| ⚙️ `basicConfig()` | Cấu hình ngưỡng, định dạng, file đích |
| 🎨 `%(asctime)s %(levelname)s %(message)s` | Các thẻ định dạng log |
| 📁 `filename=` | Ghi log ra file |
| 🧩 `getLogger(__name__)` | Logger riêng cho từng module |
| 🔐 An toàn | Không log mật khẩu, dữ liệu nhạy cảm |

---

## 🧪 Kiểm tra nhanh

1. ❓ Log là gì? Cho ví dụ đời thực về "log".
2. ❓ Kể tên 5 mức độ của logging từ thấp đến cao.
3. ❓ Mặc định logging chỉ hiển thị từ mức nào trở lên?
4. ❓ Tham số nào để ghi log ra file trong `basicConfig`?
5. ❓ `%(asctime)s` dùng để làm gì?
6. ❓ Vì sao nên dùng `logging` thay vì `print()` cho việc ghi nhật ký?
7. ❓ Điều gì xảy ra khi gọi `basicConfig` lần thứ hai?
8. ❓ Sự khác nhau giữa WARNING và ERROR?
9. ❓ Nên ghi log mức nào khi: (a) chương trình khởi động, (b) mật khẩu sai, (c) mất kết nối máy chủ?
10. ❓ Vì sao không được log mật khẩu?

<details>
<summary>🔍 Xem đáp án</summary>

1. Nhật ký ghi lại hoạt động của chương trình; ví dụ: hộp đen máy bay, sổ trực bảo vệ.
2. DEBUG, INFO, WARNING, ERROR, CRITICAL.
3. WARNING.
4. `filename="ten_file.log"`.
5. Chèn thời gian (giờ, ngày) vào dòng log.
6. Vì có mức độ, kèm thời gian, ghi được file, bật/tắt dễ dàng, không lẫn với kết quả in cho người dùng.
7. Bị bỏ qua — chỉ lần gọi đầu tiên có hiệu lực.
8. WARNING: bất thường nhưng chương trình vẫn chạy; ERROR: chức năng bị lỗi.
9. (a) INFO, (b) WARNING (hoặc ERROR nếu nhiều lần), (c) CRITICAL.
10. Vì file log có thể bị người khác đọc — lộ thông tin nhạy cảm.

</details>

---

## 📚 Bài đọc thêm

* [Python docs – logging](https://docs.python.org/3/library/logging.html)
* [Python docs – Logging HOWTO (tiếng Anh)](https://docs.python.org/3/howto/logging.html)
* [Real Python – Logging in Python](https://realpython.com/python-logging/)
* [Logging Cookbook – các mẫu cấu hình nâng cao](https://docs.python.org/3/howto/logging-cookbook.html)

---

## 🏁 Kết thúc bài

🎉 Bạn đã biết ghi "sổ trực" cho chương trình bằng logging. Trong các dự án thật, code thường có hàng nghìn dòng — làm sao để **người khác (và chính bạn sau 3 tháng) hiểu code ngay**? Bí quyết nằm ở **Type Hints** — chú thích kiểu dữ liệu:

👉 **[Bài 38: Type Hints – Chú Thích Kiểu Dữ Liệu](../38_Typing/bai_giang.md)**
