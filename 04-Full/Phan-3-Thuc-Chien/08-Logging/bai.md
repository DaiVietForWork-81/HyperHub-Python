<!-- TỰ ĐỘNG ĐỒNG BỘ từ 03-Thuc-Chien/08-Logging/bai.md — đừng sửa trực tiếp, sửa bản chính rồi chạy tools/sync_tracks.py -->

# Bài 37 — Logging – Ghi Nhật Ký Hoạt Động Chương Trình

> 🎓 **Chương 8 – Lập trình ứng dụng chuyên sâu**

## 🧠 Điều kiện tiên quyết

- [Bài 12 — Hàm (Function) Trong Python](../../Phan-1-Co-Ban/12-Ham/bai.md)
- [Bài 19 — Ngoại Lệ (Exception) Trong Python](../../Phan-1-Co-Ban/19-Exception/bai.md)

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

---

## 🧩 Bài tập

> 📝 🎯 **Chủ đề:** Ghi nhật ký hoạt động chương trình bằng module `logging` — 5 mức độ, `basicConfig`, format, ghi file, log trong module.

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Dòng log đầu tiên

* **Đề bài:** Viết chương trình ghi một log mức INFO: `Chao mung ban den voi Python logging.` (không cần cấu hình gì thêm).
* **Input:** Không có.
* **Output:** Mặc định chỉ hiện từ WARNING — quan sát xem có gì được in ra không.
* **Gợi ý:** `import logging` rồi `logging.info("...")`.

### Bài 2: Ghi cả năm mức

* **Đề bài:** Ghi lần lượt cả 5 mức: DEBUG, INFO, WARNING, ERROR, CRITICAL với nội dung tự đặt (ví dụ `Day la dong DEBUG`...). Chạy **không cấu hình** rồi chạy **có** `level=logging.DEBUG` và so sánh.
* **Input:** Không có.
* **Output:** Khi đã cấu hình DEBUG, hiện đủ 5 dòng; chưa cấu hình chỉ hiện 3 dòng cuối.
* **Gợi ý:** `logging.basicConfig(level=logging.DEBUG)` đặt trước khi ghi.

### Bài 3: Cấu hình hiển thị từ INFO

* **Đề bài:** Cấu hình `basicConfig` với `level=logging.INFO`, ghi một dòng DEBUG và một dòng INFO. In ra màn hình `Xong!`.
* **Input:** Không có.
* **Output:**
  ```
  2026-08-05 20:00:00,000 - INFO - Chuong trinh bat dau
  Xong!
  ```
* **Gợi ý:** Đặt `level=logging.INFO` — DEBUG sẽ bị chặn.

### Bài 4: Thêm thời gian vào log

* **Đề bài:** Cấu hình format gồm `%(asctime)s - %(levelname)s - %(message)s` và `datefmt="%d/%m/%Y %H:%M:%S"`. Ghi log WARNING `Truy cap thanh cong.`.
* **Input:** Không có.
* **Output:**
  ```
  05/08/2026 20:05:00 - WARNING - Truy cap thanh cong.
  ```
* **Gợi ý:** `format=` và `datefmt=` nằm trong `basicConfig`.

### Bài 5: Ghi log ra file

* **Đề bài:** Cấu hình ghi log vào file `bai_tap.log` (định dạng `%(asctime)s - %(levelname)s - %(message)s`), ghi 2 log INFO. Sau khi chạy, mở file `bai_tap.log` kiểm tra.
* **Input:** Không có.
* **Output:** Màn hình **không** in gì; nội dung trong file `bai_tap.log` có 2 dòng.
* **Gợi ý:** Thêm `filename="bai_tap.log"` và `filemode="a"`.

### Bài 6: Log chào mừng người dùng ATM

* **Đề bài:** Viết chương trình giả lập bước đầu của máy ATM: in ra màn hình `Chao mung ban den voi ATM!`, ghi log INFO `Nguoi dung bat dau su dung ATM.`, ghi log DEBUG `Hien menu chinh.`.
* **Input:** Không có.
* **Output:**
  ```
  Chao mung ban den voi ATM!
  ```
  (kèm 2 dòng log trên màn hình nếu level đủ thấp)
* **Gợi ý:** Cấu hình `level=logging.DEBUG` để thấy cả DEBUG; `print()` cho dòng chào người dùng.

### Bài 7: Tên module trong log

* **Đề bài:** Tạo logger bằng `logging.getLogger("may_giat")` và ghi log INFO `Bat dau giat.` với format có `%(name)s`.
* **Input:** Không có.
* **Output:**
  ```
  2026-08-05 20:10:00,000 - INFO - may_giat - Bat dau giat.
  ```
* **Gợi ý:** Format: `"%(asctime)s - %(levelname)s - %(name)s - %(message)s"`.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Format đầy đủ và ghi đè file

* **Đề bài:** Cấu hình format `%(asctime)s | %(levelname)s | %(lineno)d | %(message)s` ghi ra file `dai_han.log` với `filemode="w"`. Ghi 2 log rồi chạy lại 2 lần và kiểm tra file chỉ có 2 dòng.
* **Input:** Không có.
* **Output:** Sau 2 lần chạy, file `dai_han.log` chỉ chứa 2 dòng (lần chạy sau xóa nội dung cũ).
* **Gợi ý:** `%(lineno)d` in số dòng code; `"w"` = write (ghi đè).

### Bài 9: Log tên hàm đang chạy

* **Đề bài:** Viết 2 hàm `tinh_tien(so_luong, don_gia)` và `in_hoa_don()`; mỗi hàm ghi log INFO với format có `%(funcName)s`. Gọi cả 2 hàm và quan sát.
* **Input:** Không có.
* **Output:** Mỗi dòng log có tên hàm tương ứng: `tinh_tien`, `in_hoa_don`.
* **Gợi ý:** `format="%(asctime)s - %(funcName)s - %(message)s"`.

### Bài 10: Chia số bắt lỗi ghi ERROR

* **Đề bài:** Viết hàm `chia(a, b)` trả về thương; nếu `b == 0`, ghi log ERROR `Khong the chia cho 0` và trả về `None`. Gọi với `(10, 2)` và `(10, 0)`.
* **Input:** Không có.
* **Output:**
  ```
  Ket qua 10 / 2 = 5.0
  2026-08-05 20:15:00,000 - ERROR - Khong the chia cho 0
  Ket qua 10 / 0 = None
  ```
* **Gợi ý:** Dùng `if b == 0` để ghi log; `print(f"Ket qua {a} / {b} = {ket_qua}")`.

### Bài 11: Đọc file không tồn tại

* **Đề bài:** Viết chương trình mở file `khong_co_file.txt` bằng `try/except`; nếu `FileNotFoundError` thì ghi log ERROR kèm tên file. Ghi ra file `loi_file.log`.
* **Input:** Không có.
* **Output:** Màn hình in `Khong mo duoc file.`; trong `loi_file.log` có 1 dòng ERROR.
* **Gợi ý:** `logging.error("Khong mo duoc file: %s", ten_file)`.

### Bài 12: Logger riêng trong module

* **Đề bài:** Tạo file `dich_vu.py` chứa hàm `kiem_tra_ngay(ngay)` ghi INFO/WARNING, sử dụng `logger = logging.getLogger(__name__)`. Tạo file `main.py` cấu hình `basicConfig` rồi gọi hàm. (Có thể làm gọn: dùng `getLogger("dich_vu")`.)
* **Input:** Không có.
* **Output:** Log từ hàm có tên `dich_vu` trong cột `%(name)s`.
* **Gợi ý:** Trong module con chỉ dùng `logger.xxx(...)`, không gọi `basicConfig`.

### Bài 13: Đếm số lần nhập mật khẩu sai

* **Đề bài:** Giả lập đăng nhập: mật khẩu đúng là `python123`. Cho người dùng nhập mật khẩu (lặp tối đa 3 lần). Mỗi lần sai ghi WARNING `Sai mat khau lan thu N`; đúng ghi INFO `Dang nhap thanh cong`.
* **Input:** Nhập 2 lần sai rồi 1 lần đúng: `abc`, `xyz`, `python123`.
* **Output:**
  ```
  WARNING - Sai mat khau lan thu 1
  WARNING - Sai mat khau lan thu 2
  INFO - Dang nhap thanh cong
  ```
* **Gợi ý:** Vòng lặp `for lan in range(1, 4)`; `if` so sánh với mật khẩu đúng.

### Bài 14: Kiểm tra tuổi truy cập

* **Đề bài:** Viết hàm `kiem_tra_do_tuoi(tuoi)`: tuổi từ 18 trở lên ghi INFO `Cho phep truy cap`; dưới 18 ghi WARNING `Do tuoi chua du (N tuoi)`. Gọi với tuổi 15 và 20.
* **Input:** Không có.
* **Output:**
  ```
  INFO - Do tuoi 20: cho phep truy cap
  WARNING - Do tuoi 15: chua du dieu kien
  ```
* **Gợi ý:** `logging.warning("Do tuoi chua du (%d tuoi)", tuoi)`.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Chương trình ATM hoàn chỉnh có log

* **Đề bài:** Viết chương trình ATM với menu (Rút tiền, Nạp tiền, Xem số dư, Thoát). Số dư ban đầu 500.000. Ghi log: INFO khi nạp/rút thành công, WARNING khi rút quá số dư, CRITICAL khi người dùng nhập sai chức năng quá 3 lần. Ghi ra file `atm.log`.
* **Input:** Chọn `1` (rút) nhập `700000`, chọn `1` rút `100000`, chọn `4` (thoát).
* **Output:** Trên màn hình thông báo kết quả; file `atm.log` chứa các dòng WARNING/INFO tương ứng.
* **Gợi ý:** Mỗi chức năng một hàm; đếm lựa chọn sai bằng biến đếm.

### Bài 16: Hàm xử lý nhiều ngoại lệ

* **Đề bài:** Viết hàm `xu_ly_du_lieu(du_lieu)`: nếu không phải số → ERROR; nếu là số âm → WARNING; nếu là số dương → INFO. Gọi với chuỗi `"abc"`, số `-5`, số `10`. Ghi ra file `xu_ly.log`.
* **Input:** Không có.
* **Output:** 3 dòng log với 3 mức khác nhau trong file `xu_ly.log`.
* **Gợi ý:** Kiểm tra bằng `isinstance(du_lieu, (int, float))` (học ở bài 38) hoặc `str(du_lieu).replace(".", "").replace("-", "").isdigit()`.

### Bài 17: Máy tính cầm tay có nhật ký

* **Đề bài:** Viết hàm `tinh(a, b, phep_toan)` nhận `+`, `-`, `*`, `/`. Mỗi lần tính ghi DEBUG kèm phép tính; phép chia cho 0 ghi ERROR. Gọi thử 3 phép tính, ghi ra file `may_tinh.log`.
* **Input:** Không có.
* **Output:** File `may_tinh.log` có 3-4 dòng, trong đó phép chia 0 là ERROR.
* **Gợi ý:** `logging.debug("%d %s %d = %s", a, phep_toan, b, ket_qua)`.

### Bài 18: Xử lý danh sách số từ file

* **Đề bài:** Tạo file `so.txt` chứa 3 dòng: `10`, `abc`, `20`. Viết chương trình đọc từng dòng, chuyển thành số: thành công ghi DEBUG `Dong N = gia tri`; thất bại ghi ERROR `Dong N khong phai so: abc`. Cuối cùng in tổng các số hợp lệ.
* **Input:** Không có (file `so.txt` đã có).
* **Output:**
  ```
  Tong cac so hop le: 30
  ```
  (kèm 3 dòng log trên màn hình nếu level DEBUG)
* **Gợi ý:** `try: int(dong.strip()) except ValueError:` (bài 19 về exception).

### Bài 19: Chặn log dữ liệu nhạy cảm

* **Đề bài:** Viết hàm `dang_nhap(ten_dang_nhap, mat_khau)` ghi INFO `Nguoi dung abc dang nhap.` **không được chứa mật khẩu**. Sau đó gọi với `("admin", "bi_mat_123")` và kiểm tra file `bao_mat.log` không chứa chuỗi `bi_mat_123`.
* **Input:** Không có.
* **Output:** File `bao_mat.log` chứa 1 dòng INFO có tên đăng nhập nhưng không có mật khẩu.
* **Gợi ý:** Chỉ đưa `ten_dang_nhap` vào message; thử đọc lại file và `assert "bi_mat_123" not in noi_dung`.

### Bài 20: Hệ thống quản lý lớp học có log

* **Đề bài:** Viết chương trình quản lý lớp học (menu: Thêm học sinh, Xóa học sinh, Xem danh sách, Thoát). Ghi log: INFO khi thêm/xóa thành công, WARNING khi xóa học sinh không có trong lớp, ERROR khi người dùng nhập tên trống. Ghi ra file `lop_hoc.log`.
* **Input:** Chọn `1` nhập `An`, chọn `2` nhập `An`, chọn `2` nhập `Binh` (không có), chọn `4`.
* **Output:** File `lop_hoc.log` có: 1 INFO thêm, 1 INFO xóa, 1 WARNING không tìm thấy.
* **Gợi ý:** Lưu danh sách học sinh trong list; kiểm tra `if ten.strip() == ""` để ghi ERROR; `if ten in lop` trước khi xóa.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Ghi log đủ 5 mức độ và hiểu ngưỡng hiển thị mặc định.
* ✅ Cấu hình `basicConfig`: level, format, ghi file, ghi đè.
* ✅ Dùng `%(asctime)s`, `%(name)s`, `%(funcName)s`, `%(lineno)d` trong format.
* ✅ Kết hợp log với `try/except` để ghi lỗi đọc file.
* ✅ Xây dựng chương trình thực tế (ATM, máy tính, quản lý lớp) có nhật ký đầy đủ.

> 💪 **Chạy lại nhiều lần và mở file `.log`** để xem "nhật ký" tích lũy như thế nào — đó chính là cách lập trình viên dò lỗi trong thực tế.

---

## ✅ Đáp án

> 💡 **Hãy tự làm bài tập trước** rồi mới mở đáp án.

## 🟢 Dễ (Bài 1 – 7)


<details>
<summary>✅ Bài 1: Dòng log đầu tiên</summary>


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

</details>

<details>
<summary>✅ Bài 2: Ghi cả năm mức</summary>


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

</details>

<details>
<summary>✅ Bài 3: Cấu hình hiển thị từ INFO</summary>


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

</details>

<details>
<summary>✅ Bài 4: Thêm thời gian vào log</summary>


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

</details>

<details>
<summary>✅ Bài 5: Ghi log ra file</summary>


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

</details>

<details>
<summary>✅ Bài 6: Log chào mừng người dùng ATM</summary>


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

</details>

<details>
<summary>✅ Bài 7: Tên module trong log</summary>


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

</details>

## 🟡 Trung bình (Bài 8 – 14)


<details>
<summary>✅ Bài 8: Format đầy đủ và ghi đè file</summary>


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

</details>

<details>
<summary>✅ Bài 9: Log tên hàm đang chạy</summary>


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

</details>

<details>
<summary>✅ Bài 10: Chia số bắt lỗi ghi ERROR</summary>


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

</details>

<details>
<summary>✅ Bài 11: Đọc file không tồn tại</summary>


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

</details>

<details>
<summary>✅ Bài 12: Logger riêng trong module</summary>


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

</details>

<details>
<summary>✅ Bài 13: Đếm số lần nhập mật khẩu sai</summary>


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

</details>

<details>
<summary>✅ Bài 14: Kiểm tra tuổi truy cập</summary>


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

</details>

## 🔴 Khó (Bài 15 – 20)


<details>
<summary>✅ Bài 15: Chương trình ATM hoàn chỉnh có log</summary>


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

</details>

<details>
<summary>✅ Bài 16: Hàm xử lý nhiều ngoại lệ</summary>


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

</details>

<details>
<summary>✅ Bài 17: Máy tính cầm tay có nhật ký</summary>


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

</details>

<details>
<summary>✅ Bài 18: Xử lý danh sách số từ file</summary>


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

</details>

<details>
<summary>✅ Bài 19: Chặn log dữ liệu nhạy cảm</summary>


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

</details>

<details>
<summary>✅ Bài 20: Hệ thống quản lý lớp học có log</summary>


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

</details>

## 📌 Lời khuyên cuối


* **Cấu hình một lần, dùng nhiều lần** — `basicConfig` chỉ gọi một lần duy nhất ở đầu chương trình.
* **Chọn mức theo ý nghĩa**, không theo cảm xúc: chương trình khởi động = INFO, dữ liệu lạ = WARNING, chức năng gãy = ERROR.
* **Kiểm tra file `.log`** sau mỗi lần chạy — đó là cách lập trình viên "đọc sổ trực" của chương trình.
* Trong bài 40 và 41 (dự án), bạn sẽ thấy logging xuất hiện ở các chương trình quản lý thực tế — hãy tái sử dụng các mẫu này!

👉 Tiếp theo: **[Bài 38: Type Hints – Bài giảng](../09-Typing/bai.md)** | **[Bài 38: Type Hints – Bài tập](../09-Typing/bai.md)**

---

## ➡️ Điều hướng

**Vị trí:** `04-Full/Phan-3-Thuc-Chien/08-Logging/bai.md`

**Bài tiếp theo:** [Bài 38 — Type Hints – Chú Thích Kiểu Dữ Liệu](../09-Typing/bai.md)
