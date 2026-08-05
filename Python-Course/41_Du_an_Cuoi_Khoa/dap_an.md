# ✅ Bài 41: Đáp Án – Dự Án Cuối Khóa: Ứng Dụng Quản Lý Thư Viện

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án để việc học hiệu quả nhất. Đáp án các bài từ Bài 5 trở đi thao tác với file **`thu_vien.db` — được tạo tự động tại thư mục đang chạy chương trình**.
>
> 📄 Cuối file là **[CODE HOÀN CHỈNH](#-code-hoàn-chỉnh--ứng-dụng-quản-lý-thư-viện)** của toàn bộ dự án — một file `.py` duy nhất chạy được ngay.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Tạo lớp `Sach` cơ bản

**Phân tích:** Lớp đơn giản nhất của dự án — chỉ chứa dữ liệu và cách mô tả chính mình qua `__str__`.

**Ý tưởng:** `__init__` lưu 4 thuộc tính; `__str__` trả chuỗi dùng f-string để ghép thông tin.

**Thuật toán:**
1. Khai báo class `Sach` với `__init__` gán 4 thuộc tính.
2. Viết `__str__` trả về chuỗi theo mẫu yêu cầu.
3. Tạo 2 đối tượng và in ra.

**Code:**

```python
class Sach:
    """Một đầu sách trong thư viện."""

    def __init__(self, ten: str, tac_gia: str, nam: int, so_luong: int = 1) -> None:
        self.ten = ten
        self.tac_gia = tac_gia
        self.nam = nam
        self.so_luong = so_luong

    def __str__(self) -> str:
        """Chuỗi mô tả ngắn gọn đầu sách."""
        return f"{self.ten} - {self.tac_gia} ({self.nam}), {self.so_luong} cuon"


sach1 = Sach("De Men Phieu Luu Ky", "To Hoai", 1941, 10)
sach2 = Sach("Tuoi tho du doi", "Nguyen Nhat Anh", 2008, 5)
print(sach1)
print(sach2)
```

**Giải thích code:**
* `__init__(self, ten, tac_gia, nam, so_luong=1)` — hàm khởi tạo, `so_luong` có giá trị mặc định 1 (bài 12, 23).
* `__str__` — dùng `return` chứ không `print`: hàm này chỉ *trả về chuỗi*, còn `print(sach)` gọi ngầm nó.
* f-string `f"{self.ten} - ..."` — ghép chuỗi hiện đại (bài 18).

**Độ phức tạp:** O(1) — chỉ gán thuộc tính và tạo chuỗi.

---

### Bài 2: Nâng cấp lớp `Sach` — mã sách, số đang mượn, số còn lại

**Phân tích:** Sách thật có thêm mã số và trạng thái mượn/trả. `con_lai` không phải dữ liệu lưu trữ mà là **giá trị tính được** — dùng `@property`.

**Ý tưởng:** Thêm tham số `dang_muon=0`, `ma=None`; viết `@property con_lai`; cập nhật `__str__` kèm trạng thái `con`/`het`.

**Thuật toán:**
1. Thêm hai tham số mặc định vào `__init__`.
2. Viết property `con_lai = so_luong - dang_muon`.
3. Trong `__str__`, so sánh `con_lai > 0` để chọn trạng thái.

**Code:**

```python
from typing import Optional


class Sach:
    """Một đầu sách trong thư viện (nâng cấp: ma, dang_muon, con_lai)."""

    def __init__(self, ten: str, tac_gia: str, nam: int, so_luong: int = 1,
                 dang_muon: int = 0, ma: Optional[int] = None) -> None:
        self.ma = ma
        self.ten = ten
        self.tac_gia = tac_gia
        self.nam = nam
        self.so_luong = so_luong
        self.dang_muon = dang_muon

    @property
    def con_lai(self) -> int:
        """Số cuốn còn lại chưa được mượn."""
        return self.so_luong - self.dang_muon

    def __str__(self) -> str:
        trang_thai = "con" if self.con_lai > 0 else "het"
        return (f"[{self.ma}] {self.ten} - {self.tac_gia} ({self.nam}) | "
                f"con {self.con_lai}/{self.so_luong} cuon [{trang_thai}]")


sach = Sach("De Men Phieu Luu Ky", "To Hoai", 1941, 10, dang_muon=3, ma=1)
print(sach)
print("Con lai:", sach.con_lai)
```

**Giải thích code:**
* `ma: Optional[int] = None` — lúc nhập mới chưa có mã, database cấp mã sau (bài 38 `Optional`).
* `@property` — `sach.con_lai` đọc như biến nhưng chạy phương thức bên trong; **không ai gán được** `sach.con_lai = 5` vì không có setter — bảo vệ tính nhất quán (bài 23, 24).
* `trang_thai = "con" if ... else "het"` — biểu thức điều kiện gọn gàng (bài 8).

**Độ phức tạp:** O(1).

---

### Bài 3: Kết nối cơ sở dữ liệu SQLite

**Phân tích:** Bước đầu chạm vào SQLite: mở kết nối, chạy truy vấn, đóng kết nối — đúng chu trình sống của một kết nối.

**Ý tưởng:** `sqlite3.connect` tạo hoặc mở file; `SELECT sqlite_version()` trả phiên bản; luôn `close()`.

**Thuật toán:**
1. `import sqlite3`.
2. `ket_noi = sqlite3.connect("thu_vien.db")` — nếu file chưa có, SQLite tự tạo file rỗng.
3. Chạy `SELECT sqlite_version()`, lấy giá trị bằng `fetchone()[0]`.
4. In và đóng kết nối.

**Code:**

```python
import sqlite3

# Mở kết nối: file thu_vien.db được tạo ngay tại thư mục đang chạy
ket_noi = sqlite3.connect("thu_vien.db")

# Truy vấn phiên bản SQLite
con_tro = ket_noi.execute("SELECT sqlite_version()")
print("Phien ban SQLite:", con_tro.fetchone()[0])

ket_noi.close()  # luôn đóng kết nối sau khi dùng xong
```

**Giải thích code:**
* `sqlite3.connect("thu_vien.db")` — đường dẫn tương đối, nên file được tạo **trong thư mục đang chạy chương trình**, không phải thư mục chứa code.
* `execute()` trả về một **con trỏ (cursor)** — kết quả truy vấn nằm trong đó.
* `fetchone()` trả dòng đầu tiên dưới dạng tuple; `[0]` lấy ô đầu tiên.
* `close()` — đóng file DB, tránh khóa file (quan trọng trên Windows).

**Độ phức tạp:** O(1).

---

### Bài 4: Tạo bảng `Sach` trong database

**Phân tích:** Bảng là "khung sườn" chứa dữ liệu. Cần định nghĩa đủ 6 cột với ràng buộc đúng để nghiệp vụ mượn/trả sau này không bị sai.

**Ý tưởng:** `CREATE TABLE IF NOT EXISTS` — chạy bao nhiêu lần cũng an toàn; `with ket_noi:` để câu lệnh tự COMMIT.

**Thuật toán:**
1. Kết nối `thu_vien.db`.
2. Bọc `CREATE TABLE` trong `with ket_noi:`.
3. In cấu trúc bằng `PRAGMA table_info(Sach)` để tự kiểm tra.
4. Đóng kết nối.

**Code:**

```python
import sqlite3

ket_noi = sqlite3.connect("thu_vien.db")

with ket_noi:  # context manager: tự COMMIT khi thành công
    ket_noi.execute(
        """CREATE TABLE IF NOT EXISTS Sach (
               id         INTEGER PRIMARY KEY AUTOINCREMENT,
               ten        TEXT    NOT NULL,
               tac_gia    TEXT    NOT NULL,
               nam        INTEGER,
               so_luong   INTEGER NOT NULL,
               dang_muon  INTEGER NOT NULL DEFAULT 0
           )"""
    )

# Kiểm tra cấu trúc bảng: PRAGMA table_info trả 1 dòng cho mỗi cột
for dong in ket_noi.execute("PRAGMA table_info(Sach)"):
    print(dong)

ket_noi.close()
```

**Giải thích code:**
* `PRIMARY KEY AUTOINCREMENT` — `id` tự tăng và duy nhất, database quản lý, không phải tự đếm tay (bài 36).
* `NOT NULL` — không cho phép tên/tác giả/số lượng rỗng: dữ liệu dơ không thể vào bảng.
* `DEFAULT 0` — mỗi đầu sách mới bắt đầu với 0 cuốn đang mượn.
* `PRAGMA table_info` — lệnh tự kiểm tra cấu trúc, mỗi dòng trả về: `(vị trí, tên cột, kiểu, not_null, giá trị mặc định, khóa chính)`.

**Độ phức tạp:** O(1) — tạo bảng một lần.

---

### Bài 5: Phương thức `them_sach` cho lớp `ThuVien`

**Phân tích:** Đây là khởi đầu của lớp trung tâm `ThuVien` — nơi chứa mọi câu SQL. `__init__` mở kết nối và tự tạo bảng, `them_sach` ghi một dòng mới.

**Ý tưởng:** Giữ kết nối trong `self.ket_noi` (dùng chung cho mọi phương thức); `INSERT` với `?` placeholder; mã mới ở `cursor.lastrowid`.

**Thuật toán:**
1. `__init__`: kết nối, đặt `row_factory = sqlite3.Row`, gọi `tao_bang()`.
2. `tao_bang()`: `CREATE TABLE IF NOT EXISTS` trong `with self.ket_noi:`.
3. `them_sach`: `INSERT` 5 cột, bọc `with`, trả `con_tro.lastrowid`.

**Code:**

```python
import sqlite3
from typing import Optional


class Sach:
    """Một đầu sách trong thư viện."""

    def __init__(self, ten: str, tac_gia: str, nam: int, so_luong: int = 1,
                 dang_muon: int = 0, ma: Optional[int] = None) -> None:
        self.ma = ma
        self.ten = ten
        self.tac_gia = tac_gia
        self.nam = nam
        self.so_luong = so_luong
        self.dang_muon = dang_muon


class ThuVien:
    """Quản lý mọi thao tác với cơ sở dữ liệu SQLite."""

    def __init__(self, duong_dan_db: str = "thu_vien.db") -> None:
        self.duong_dan_db = duong_dan_db
        # row_factory: mỗi dòng trả về truy cập được theo tên cột (dong["ten"])
        self.ket_noi = sqlite3.connect(duong_dan_db)
        self.ket_noi.row_factory = sqlite3.Row
        self.tao_bang()

    def tao_bang(self) -> None:
        """Tạo bảng Sach nếu chưa tồn tại."""
        with self.ket_noi:
            self.ket_noi.execute(
                """CREATE TABLE IF NOT EXISTS Sach (
                       id         INTEGER PRIMARY KEY AUTOINCREMENT,
                       ten        TEXT    NOT NULL,
                       tac_gia    TEXT    NOT NULL,
                       nam        INTEGER,
                       so_luong   INTEGER NOT NULL,
                       dang_muon  INTEGER NOT NULL DEFAULT 0
                   )"""
            )

    def them_sach(self, sach: Sach) -> int:
        """Thêm đầu sách mới; trả về mã sách vừa tạo."""
        with self.ket_noi:
            con_tro = self.ket_noi.execute(
                "INSERT INTO Sach (ten, tac_gia, nam, so_luong, dang_muon) "
                "VALUES (?, ?, ?, ?, ?)",
                (sach.ten, sach.tac_gia, sach.nam, sach.so_luong, sach.dang_muon),
            )
        return con_tro.lastrowid


tv = ThuVien()
ma1 = tv.them_sach(Sach("De Men Phieu Luu Ky", "To Hoai", 1941, 10))
ma2 = tv.them_sach(Sach("Tuoi tho du doi", "Nguyen Nhat Anh", 2008, 5))
print("Da them sach co ma", ma1)
print("Da them sach co ma", ma2)
tv.ket_noi.close()
```

**Giải thích code:**
* `row_factory = sqlite3.Row` — một dòng kết quả đọc được theo tên cột; bắt buộc đặt **ngay sau** `connect`.
* `INSERT ... VALUES (?, ?, ?, ?, ?)` — 5 dấu `?` tương ứng 5 giá trị trong tuple. Lưu ý **không** ghi `id` — database tự cấp.
* `con_tro.lastrowid` — mã tự tăng vừa được SQLite cấp cho dòng mới (bài 36).
* `with self.ket_noi:` — lệnh ghi tự COMMIT; nếu lệnh lỗi sẽ tự ROLLBACK.

**Độ phức tạp:** O(1) — ghi một dòng, có index khóa chính.

---

### Bài 6: Phương thức `xem_danh_sach`

**Phân tích:** Hàm đọc (Read) quan trọng nhất: trả về **toàn bộ** dữ liệu sách dưới dạng list dict — định dạng mà tầng `App` sẽ in bảng.

**Ý tưởng:** `SELECT * ... ORDER BY id` để thứ tự ổn định; `[dict(dong) for dong in ...]` biến từng `Row` thành dict.

**Thuật toán:**
1. Chạy `SELECT * FROM Sach ORDER BY id`.
2. `fetchall()` lấy mọi dòng.
3. Duyệt và biến mỗi `Row` thành `dict` bằng `dict(dong)`.
4. Trả list kết quả.

**Code:**

```python
import sqlite3
from typing import Dict, List, Optional


class Sach:
    """Một đầu sách trong thư viện."""

    def __init__(self, ten: str, tac_gia: str, nam: int, so_luong: int = 1,
                 dang_muon: int = 0, ma: Optional[int] = None) -> None:
        self.ma = ma
        self.ten = ten
        self.tac_gia = tac_gia
        self.nam = nam
        self.so_luong = so_luong
        self.dang_muon = dang_muon


class ThuVien:
    """Quản lý mọi thao tác với cơ sở dữ liệu SQLite."""

    def __init__(self, duong_dan_db: str = "thu_vien.db") -> None:
        self.duong_dan_db = duong_dan_db
        self.ket_noi = sqlite3.connect(duong_dan_db)
        self.ket_noi.row_factory = sqlite3.Row
        self.tao_bang()

    def tao_bang(self) -> None:
        """Tạo bảng Sach nếu chưa tồn tại."""
        with self.ket_noi:
            self.ket_noi.execute(
                """CREATE TABLE IF NOT EXISTS Sach (
                       id         INTEGER PRIMARY KEY AUTOINCREMENT,
                       ten        TEXT    NOT NULL,
                       tac_gia    TEXT    NOT NULL,
                       nam        INTEGER,
                       so_luong   INTEGER NOT NULL,
                       dang_muon  INTEGER NOT NULL DEFAULT 0
                   )"""
            )

    def them_sach(self, sach: Sach) -> int:
        """Thêm đầu sách mới; trả về mã sách vừa tạo."""
        with self.ket_noi:
            con_tro = self.ket_noi.execute(
                "INSERT INTO Sach (ten, tac_gia, nam, so_luong, dang_muon) "
                "VALUES (?, ?, ?, ?, ?)",
                (sach.ten, sach.tac_gia, sach.nam, sach.so_luong, sach.dang_muon),
            )
        return con_tro.lastrowid

    def xem_danh_sach(self) -> List[Dict[str, object]]:
        """Trả về danh sách toàn bộ đầu sách, sắp theo mã."""
        con_tro = self.ket_noi.execute("SELECT * FROM Sach ORDER BY id")
        return [dict(dong) for dong in con_tro.fetchall()]


tv = ThuVien()
tv.them_sach(Sach("De Men Phieu Luu Ky", "To Hoai", 1941, 10))
tv.them_sach(Sach("Tuoi tho du doi", "Nguyen Nhat Anh", 2008, 5))

for sach in tv.xem_danh_sach():
    print(sach)

tv.ket_noi.close()
```

**Giải thích code:**
* `ORDER BY id` — kết quả luôn theo thứ tự mã; không có nó, thứ tự là tuỳ ý của database (bài 36).
* `dict(dong)` — nhờ `row_factory`, `Row.keys()` trả tên cột nên `dict()` chuyển thẳng thành từ điển `{"id": ..., "ten": ...}`.
* `-> List[Dict[str, object]]` — type hint mô tả chính xác kiểu trả về (bài 38).

**Độ phức tạp:** O(n) — phải duyệt toàn bộ `n` dòng.

---

### Bài 7: Phương thức `_lay_sach` — lấy sách theo mã

**Phân tích:** Hàm dùng chung cho sửa, xóa, mượn, trả: kiểm tra "sách này có tồn tại không và đang ở trạng thái nào?". Kết quả `None` là ngôn ngữ chuẩn cho "không tìm thấy".

**Ý tưởng:** `SELECT ... WHERE id = ?`; `fetchone()` trả `None` khi hết dòng; đặt tên `_lay_sach` với gạch dưới — quy ước "phương thức nội bộ".

**Thuật toán:**
1. Chạy `SELECT * FROM Sach WHERE id = ?` với `(ma,)`.
2. `fetchone()` lấy một dòng hoặc `None`.
3. Trả `dict(dong)` nếu có, ngược lại `None`.

**Code:**

```python
import sqlite3
from typing import Dict, List, Optional


class Sach:
    """Một đầu sách trong thư viện."""

    def __init__(self, ten: str, tac_gia: str, nam: int, so_luong: int = 1,
                 dang_muon: int = 0, ma: Optional[int] = None) -> None:
        self.ma = ma
        self.ten = ten
        self.tac_gia = tac_gia
        self.nam = nam
        self.so_luong = so_luong
        self.dang_muon = dang_muon


class ThuVien:
    """Quản lý mọi thao tác với cơ sở dữ liệu SQLite."""

    def __init__(self, duong_dan_db: str = "thu_vien.db") -> None:
        self.duong_dan_db = duong_dan_db
        self.ket_noi = sqlite3.connect(duong_dan_db)
        self.ket_noi.row_factory = sqlite3.Row
        self.tao_bang()

    def tao_bang(self) -> None:
        """Tạo bảng Sach nếu chưa tồn tại."""
        with self.ket_noi:
            self.ket_noi.execute(
                """CREATE TABLE IF NOT EXISTS Sach (
                       id         INTEGER PRIMARY KEY AUTOINCREMENT,
                       ten        TEXT    NOT NULL,
                       tac_gia    TEXT    NOT NULL,
                       nam        INTEGER,
                       so_luong   INTEGER NOT NULL,
                       dang_muon  INTEGER NOT NULL DEFAULT 0
                   )"""
            )

    def them_sach(self, sach: Sach) -> int:
        """Thêm đầu sách mới; trả về mã sách vừa tạo."""
        with self.ket_noi:
            con_tro = self.ket_noi.execute(
                "INSERT INTO Sach (ten, tac_gia, nam, so_luong, dang_muon) "
                "VALUES (?, ?, ?, ?, ?)",
                (sach.ten, sach.tac_gia, sach.nam, sach.so_luong, sach.dang_muon),
            )
        return con_tro.lastrowid

    def _lay_sach(self, ma: int) -> Optional[Dict[str, object]]:
        """Lấy một dòng sách theo mã; trả về None nếu không có."""
        con_tro = self.ket_noi.execute("SELECT * FROM Sach WHERE id = ?", (ma,))
        dong = con_tro.fetchone()
        return dict(dong) if dong else None


tv = ThuVien()
tv.them_sach(Sach("De Men Phieu Luu Ky", "To Hoai", 1941, 10))

print("Sach ma 1:", tv._lay_sach(1))
print("Sach ma 999:", tv._lay_sach(999))
tv.ket_noi.close()
```

**Giải thích code:**
* `(ma,)` — cặp ngoặc + dấu phẩy để tạo **tuple 1 phần tử**; nếu thiếu dấu phẩy, `(ma)` chỉ là số nguyên và `execute` sẽ báo lỗi.
* `fetchone()` — hiệu quả hơn `fetchall()` khi chỉ cần một dòng.
* `return dict(dong) if dong else None` — viết gọn cho "có thì trả dict, không thì None" — chỗ dùng `Optional` của bài 38.
* Gạch dưới đầu tên (`_lay_sach`) — quy ước: chỉ gọi nội bộ trong class, không gọi từ `App`.

**Độ phức tạp:** O(1) — tìm theo khóa chính `id`, SQLite dùng index.

---

### Bài 8: Tìm sách theo tên

**Phân tích:** Người dùng không nhớ tên chính xác, chỉ nhớ một phần. `LIKE '%...%'` giải quyết: tìm mọi tên **chứa** chuỗi nhập vào.

**Ý tưởng:** `WHERE ten LIKE ?` với giá trị `f"%{ten.strip()}%"`; trả list dict như `xem_danh_sach`.

**Thuật toán:**
1. Làm sạch chuỗi tìm bằng `strip()`.
2. Ghép mẫu `%` hai đầu.
3. `SELECT * FROM Sach WHERE ten LIKE ? ORDER BY id`.
4. Trả list dict.

**Code:**

```python
import sqlite3
from typing import Dict, List, Optional


class Sach:
    """Một đầu sách trong thư viện."""

    def __init__(self, ten: str, tac_gia: str, nam: int, so_luong: int = 1,
                 dang_muon: int = 0, ma: Optional[int] = None) -> None:
        self.ma = ma
        self.ten = ten
        self.tac_gia = tac_gia
        self.nam = nam
        self.so_luong = so_luong
        self.dang_muon = dang_muon


class ThuVien:
    """Quản lý mọi thao tác với cơ sở dữ liệu SQLite."""

    def __init__(self, duong_dan_db: str = "thu_vien.db") -> None:
        self.duong_dan_db = duong_dan_db
        self.ket_noi = sqlite3.connect(duong_dan_db)
        self.ket_noi.row_factory = sqlite3.Row
        self.tao_bang()

    def tao_bang(self) -> None:
        """Tạo bảng Sach nếu chưa tồn tại."""
        with self.ket_noi:
            self.ket_noi.execute(
                """CREATE TABLE IF NOT EXISTS Sach (
                       id         INTEGER PRIMARY KEY AUTOINCREMENT,
                       ten        TEXT    NOT NULL,
                       tac_gia    TEXT    NOT NULL,
                       nam        INTEGER,
                       so_luong   INTEGER NOT NULL,
                       dang_muon  INTEGER NOT NULL DEFAULT 0
                   )"""
            )

    def them_sach(self, sach: Sach) -> int:
        """Thêm đầu sách mới; trả về mã sách vừa tạo."""
        with self.ket_noi:
            con_tro = self.ket_noi.execute(
                "INSERT INTO Sach (ten, tac_gia, nam, so_luong, dang_muon) "
                "VALUES (?, ?, ?, ?, ?)",
                (sach.ten, sach.tac_gia, sach.nam, sach.so_luong, sach.dang_muon),
            )
        return con_tro.lastrowid

    def tim_theo_ten(self, ten_can_tim: str) -> List[Dict[str, object]]:
        """Tìm đầu sách có tên chứa chuỗi cho trước."""
        con_tro = self.ket_noi.execute(
            "SELECT * FROM Sach WHERE ten LIKE ? ORDER BY id",
            (f"%{ten_can_tim.strip()}%",),
        )
        return [dict(dong) for dong in con_tro.fetchall()]


tv = ThuVien()
tv.them_sach(Sach("De Men Phieu Luu Ky", "To Hoai", 1941, 10))

print("Tim 'de men':", tv.tim_theo_ten("de men"))
print("Tim 'mat khong co':", tv.tim_theo_ten("mat khong co"))
tv.ket_noi.close()
```

**Giải thích code:**
* `LIKE ?` với `"%de men%"` — dấu `%` là **ký tự đại diện**: đứng trước và sau chuỗi nghĩa là "bất kỳ chuỗi nào chứa 'de men'".
* `LIKE` chuẩn của SQLite **không phân biệt hoa thường** với chữ cái thường (A-Z/a-z), nên `"DE MEN"` cũng khớp (bài 18 chuỗi, bài 36 SQL).
* `string.strip()` — bỏ khoảng trắng thừa người dùng hay gõ đầu cuối; nếu nhập toàn khoảng trắng thì trả mọi sách — hãy nhớ kiểm tra lại trong `App`.
* Chuỗi nhập nằm trong **tham số `?`**, không nằm trong SQL — an toàn, không thể SQL Injection.

**Độ phức tạp:** O(n) — phải quét từng dòng để so khớp `LIKE`.

---

### Bài 9: Tìm sách theo tác giả

**Phân tích:** Giống hệt bài 8, chỉ khác cột. Đây là lúc thấy lợi ích của việc tách hàm: copy-paste từng dòng nhưng đổi `ten` → `tac_gia`.

**Ý tưởng:** Viết phương thức tương tự `tim_theo_ten`, đổi tên cột trong `WHERE`.

**Thuật toán:**
1. Làm sạch chuỗi tìm.
2. `SELECT * FROM Sach WHERE tac_gia LIKE ? ORDER BY id`.
3. Trả list dict.

**Code:**

```python
import sqlite3
from typing import Dict, List, Optional


class Sach:
    """Một đầu sách trong thư viện."""

    def __init__(self, ten: str, tac_gia: str, nam: int, so_luong: int = 1,
                 dang_muon: int = 0, ma: Optional[int] = None) -> None:
        self.ma = ma
        self.ten = ten
        self.tac_gia = tac_gia
        self.nam = nam
        self.so_luong = so_luong
        self.dang_muon = dang_muon


class ThuVien:
    """Quản lý mọi thao tác với cơ sở dữ liệu SQLite."""

    def __init__(self, duong_dan_db: str = "thu_vien.db") -> None:
        self.duong_dan_db = duong_dan_db
        self.ket_noi = sqlite3.connect(duong_dan_db)
        self.ket_noi.row_factory = sqlite3.Row
        self.tao_bang()

    def tao_bang(self) -> None:
        """Tạo bảng Sach nếu chưa tồn tại."""
        with self.ket_noi:
            self.ket_noi.execute(
                """CREATE TABLE IF NOT EXISTS Sach (
                       id         INTEGER PRIMARY KEY AUTOINCREMENT,
                       ten        TEXT    NOT NULL,
                       tac_gia    TEXT    NOT NULL,
                       nam        INTEGER,
                       so_luong   INTEGER NOT NULL,
                       dang_muon  INTEGER NOT NULL DEFAULT 0
                   )"""
            )

    def them_sach(self, sach: Sach) -> int:
        """Thêm đầu sách mới; trả về mã sách vừa tạo."""
        with self.ket_noi:
            con_tro = self.ket_noi.execute(
                "INSERT INTO Sach (ten, tac_gia, nam, so_luong, dang_muon) "
                "VALUES (?, ?, ?, ?, ?)",
                (sach.ten, sach.tac_gia, sach.nam, sach.so_luong, sach.dang_muon),
            )
        return con_tro.lastrowid

    def tim_theo_tac_gia(self, tac_gia_can_tim: str) -> List[Dict[str, object]]:
        """Tìm đầu sách theo tác giả (chứa chuỗi cho trước)."""
        con_tro = self.ket_noi.execute(
            "SELECT * FROM Sach WHERE tac_gia LIKE ? ORDER BY id",
            (f"%{tac_gia_can_tim.strip()}%",),
        )
        return [dict(dong) for dong in con_tro.fetchall()]


tv = ThuVien()
tv.them_sach(Sach("De Men Phieu Luu Ky", "To Hoai", 1941, 10))

print("Tim 'hoai':", tv.tim_theo_tac_gia("hoai"))
tv.ket_noi.close()
```

**Giải thích code:**
* Chỉ khác bài 8 ở tên cột trong câu SQL: `tac_gia LIKE ?`.
* `ORDER BY id` — kết quả ổn định giữa các lần chạy, dễ đối chiếu khi kiểm thử.

**Độ phức tạp:** O(n).

---

### Bài 10: Sửa thông tin sách

**Phân tích:** Câu `UPDATE` cần biết **cột nào** và **giá trị mới nào**. Vì tên cột không thể đưa qua `?` (SQL chỉ cho placeholder *giá trị*), ta phải tự kiểm tra tên cột bằng danh sách trắng `COT_HOP_LE` — đây là "tường lửa" chống SQL Injection vào tên cột.

**Ý tưởng:** Nếu `cot` không hợp lệ → `raise ValueError`; sách không tồn tại → `False`; ngược lại `UPDATE ... SET {cot} = ? WHERE id = ?` → `True`.

**Thuật toán:**
1. Kiểm tra `cot in COT_HOP_LE`, sai thì `raise ValueError`.
2. Kiểm tra `_lay_sach(ma) is None`, đúng thì `return False`.
3. Chạy UPDATE với `(gia_tri, ma)`, bọc `with`.
4. `return True`.

**Code:**

```python
import sqlite3
from typing import Dict, List, Optional


class Sach:
    """Một đầu sách trong thư viện."""

    def __init__(self, ten: str, tac_gia: str, nam: int, so_luong: int = 1,
                 dang_muon: int = 0, ma: Optional[int] = None) -> None:
        self.ma = ma
        self.ten = ten
        self.tac_gia = tac_gia
        self.nam = nam
        self.so_luong = so_luong
        self.dang_muon = dang_muon


class ThuVien:
    """Quản lý mọi thao tác với cơ sở dữ liệu SQLite."""

    COT_HOP_LE = ("ten", "tac_gia", "nam", "so_luong")

    def __init__(self, duong_dan_db: str = "thu_vien.db") -> None:
        self.duong_dan_db = duong_dan_db
        self.ket_noi = sqlite3.connect(duong_dan_db)
        self.ket_noi.row_factory = sqlite3.Row
        self.tao_bang()

    def tao_bang(self) -> None:
        """Tạo bảng Sach nếu chưa tồn tại."""
        with self.ket_noi:
            self.ket_noi.execute(
                """CREATE TABLE IF NOT EXISTS Sach (
                       id         INTEGER PRIMARY KEY AUTOINCREMENT,
                       ten        TEXT    NOT NULL,
                       tac_gia    TEXT    NOT NULL,
                       nam        INTEGER,
                       so_luong   INTEGER NOT NULL,
                       dang_muon  INTEGER NOT NULL DEFAULT 0
                   )"""
            )

    def them_sach(self, sach: Sach) -> int:
        """Thêm đầu sách mới; trả về mã sách vừa tạo."""
        with self.ket_noi:
            con_tro = self.ket_noi.execute(
                "INSERT INTO Sach (ten, tac_gia, nam, so_luong, dang_muon) "
                "VALUES (?, ?, ?, ?, ?)",
                (sach.ten, sach.tac_gia, sach.nam, sach.so_luong, sach.dang_muon),
            )
        return con_tro.lastrowid

    def _lay_sach(self, ma: int) -> Optional[Dict[str, object]]:
        """Lấy một dòng sách theo mã; trả về None nếu không có."""
        con_tro = self.ket_noi.execute("SELECT * FROM Sach WHERE id = ?", (ma,))
        dong = con_tro.fetchone()
        return dict(dong) if dong else None

    def sua_sach(self, ma: int, cot: str, gia_tri: object) -> bool:
        """Sửa một cột hợp lệ của đầu sách; trả về True nếu sửa được."""
        if cot not in ThuVien.COT_HOP_LE:
            raise ValueError(f"Khong ho tro sua cot: {cot}")
        if self._lay_sach(ma) is None:
            return False
        with self.ket_noi:
            self.ket_noi.execute(
                f"UPDATE Sach SET {cot} = ? WHERE id = ?", (gia_tri, ma)
            )
        return True


tv = ThuVien()
ma = tv.them_sach(Sach("De Men Phieu Luu Ky", "To Hoai", 1941, 10))

print("Sua ten:", tv.sua_sach(ma, "ten", "De Men Phieu Luu Ky (bia cung)"))
print("Sua nam:", tv.sua_sach(ma, "nam", 2010))
print("Sach khong ton tai:", tv.sua_sach(999, "ten", "abc"))
try:
    tv.sua_sach(ma, "gia", 50000)   # 'gia' không có trong bảng
except ValueError as loi:
    print("Loi:", loi)
tv.ket_noi.close()
```

**Giải thích code:**
* `COT_HOP_LE` — hằng số lớp: tên cột được phép sửa. Người dùng chỉ gõ từ danh sách này, mọi chuỗi khác bị chặn → tên cột an toàn.
* `f"UPDATE ... SET {cot} = ?"` — `{cot}` chỉ nhận giá trị từ `COT_HOP_LE` (đã kiểm tra), còn giá trị mới `gia_tri` vẫn qua `?` — kết hợp an toàn cả hai phía.
* `return False` khi sách không tồn tại; `raise ValueError` khi cột sai — đúng hai "ngôn ngữ" đã bàn ở bài giảng.

**Độ phức tạp:** O(1).

---

### Bài 11: Xóa sách

**Phân tích:** Lệnh `DELETE` nguy hiểm — xóa là mất vĩnh viễn. Phải kiểm tra sách tồn tại trước và trả kết quả rõ ràng để tầng `App` xác nhận với người dùng.

**Ý tưởng:** Kiểm tra `_lay_sach(ma)`, nếu có thì `DELETE ... WHERE id = ?` trong `with`.

**Thuật toán:**
1. `_lay_sach(ma)` trả `None` → `return False`.
2. Ngược lại chạy `DELETE`, bọc `with`, trả `True`.

**Code:**

```python
import sqlite3
from typing import Dict, List, Optional


class Sach:
    """Một đầu sách trong thư viện."""

    def __init__(self, ten: str, tac_gia: str, nam: int, so_luong: int = 1,
                 dang_muon: int = 0, ma: Optional[int] = None) -> None:
        self.ma = ma
        self.ten = ten
        self.tac_gia = tac_gia
        self.nam = nam
        self.so_luong = so_luong
        self.dang_muon = dang_muon


class ThuVien:
    """Quản lý mọi thao tác với cơ sở dữ liệu SQLite."""

    def __init__(self, duong_dan_db: str = "thu_vien.db") -> None:
        self.duong_dan_db = duong_dan_db
        self.ket_noi = sqlite3.connect(duong_dan_db)
        self.ket_noi.row_factory = sqlite3.Row
        self.tao_bang()

    def tao_bang(self) -> None:
        """Tạo bảng Sach nếu chưa tồn tại."""
        with self.ket_noi:
            self.ket_noi.execute(
                """CREATE TABLE IF NOT EXISTS Sach (
                       id         INTEGER PRIMARY KEY AUTOINCREMENT,
                       ten        TEXT    NOT NULL,
                       tac_gia    TEXT    NOT NULL,
                       nam        INTEGER,
                       so_luong   INTEGER NOT NULL,
                       dang_muon  INTEGER NOT NULL DEFAULT 0
                   )"""
            )

    def them_sach(self, sach: Sach) -> int:
        """Thêm đầu sách mới; trả về mã sách vừa tạo."""
        with self.ket_noi:
            con_tro = self.ket_noi.execute(
                "INSERT INTO Sach (ten, tac_gia, nam, so_luong, dang_muon) "
                "VALUES (?, ?, ?, ?, ?)",
                (sach.ten, sach.tac_gia, sach.nam, sach.so_luong, sach.dang_muon),
            )
        return con_tro.lastrowid

    def _lay_sach(self, ma: int) -> Optional[Dict[str, object]]:
        """Lấy một dòng sách theo mã; trả về None nếu không có."""
        con_tro = self.ket_noi.execute("SELECT * FROM Sach WHERE id = ?", (ma,))
        dong = con_tro.fetchone()
        return dict(dong) if dong else None

    def xoa_sach(self, ma: int) -> bool:
        """Xóa đầu sách theo mã; trả về True nếu xóa được."""
        if self._lay_sach(ma) is None:
            return False
        with self.ket_noi:
            self.ket_noi.execute("DELETE FROM Sach WHERE id = ?", (ma,))
        return True


tv = ThuVien()
ma1 = tv.them_sach(Sach("De Men Phieu Luu Ky", "To Hoai", 1941, 10))
tv.them_sach(Sach("Tuoi tho du doi", "Nguyen Nhat Anh", 2008, 5))

print("Xoa sach", ma1, ":", tv.xoa_sach(ma1))
print("Xoa sach 999:", tv.xoa_sach(999))
print("Danh sach con lai:", [s["ten"] for s in tv.xem_danh_sach()])
tv.ket_noi.close()
```

**Giải thích code:**
* Xóa trước, kiểm tra sau sẽ gây hiểu nhầm: `DELETE` với mã không tồn tại vẫn "thành công" (0 dòng bị xóa). Kiểm tra trước để phân biệt "không có" với "đã xóa".
* Trong dự án hoàn chỉnh, tầng `App` sẽ hỏi "Chac chan xoa? (y/n)" trước khi gọi — an toàn tuyệt đối (bài 40 cũng làm thế).

**Độ phức tạp:** O(1).

---

### Bài 12: Mượn sách

**Phân tích:** Nghiệp vụ lõi của thư viện. Mượn phải tuân thủ quy tắc: **không mượn quá số cuốn hiện có**. Cần đọc kiểm tra trước, ghi sau.

**Ý tưởng:** `_lay_sach(ma)` kiểm tra tồn tại; so sánh `dang_muon >= so_luong` → hết sách, `raise ValueError`; còn thì `UPDATE ... dang_muon = dang_muon + 1`.

**Thuật toán:**
1. `dong = _lay_sach(ma)`; `dong is None` → `False`.
2. `dong["dang_muon"] >= dong["so_luong"]` → `raise ValueError`.
3. `UPDATE Sach SET dang_muon = dang_muon + 1 WHERE id = ?`.
4. `return True`.

**Code:**

```python
import sqlite3
from typing import Dict, List, Optional


class Sach:
    """Một đầu sách trong thư viện."""

    def __init__(self, ten: str, tac_gia: str, nam: int, so_luong: int = 1,
                 dang_muon: int = 0, ma: Optional[int] = None) -> None:
        self.ma = ma
        self.ten = ten
        self.tac_gia = tac_gia
        self.nam = nam
        self.so_luong = so_luong
        self.dang_muon = dang_muon


class ThuVien:
    """Quản lý mọi thao tác với cơ sở dữ liệu SQLite."""

    def __init__(self, duong_dan_db: str = "thu_vien.db") -> None:
        self.duong_dan_db = duong_dan_db
        self.ket_noi = sqlite3.connect(duong_dan_db)
        self.ket_noi.row_factory = sqlite3.Row
        self.tao_bang()

    def tao_bang(self) -> None:
        """Tạo bảng Sach nếu chưa tồn tại."""
        with self.ket_noi:
            self.ket_noi.execute(
                """CREATE TABLE IF NOT EXISTS Sach (
                       id         INTEGER PRIMARY KEY AUTOINCREMENT,
                       ten        TEXT    NOT NULL,
                       tac_gia    TEXT    NOT NULL,
                       nam        INTEGER,
                       so_luong   INTEGER NOT NULL,
                       dang_muon  INTEGER NOT NULL DEFAULT 0
                   )"""
            )

    def them_sach(self, sach: Sach) -> int:
        """Thêm đầu sách mới; trả về mã sách vừa tạo."""
        with self.ket_noi:
            con_tro = self.ket_noi.execute(
                "INSERT INTO Sach (ten, tac_gia, nam, so_luong, dang_muon) "
                "VALUES (?, ?, ?, ?, ?)",
                (sach.ten, sach.tac_gia, sach.nam, sach.so_luong, sach.dang_muon),
            )
        return con_tro.lastrowid

    def _lay_sach(self, ma: int) -> Optional[Dict[str, object]]:
        """Lấy một dòng sách theo mã; trả về None nếu không có."""
        con_tro = self.ket_noi.execute("SELECT * FROM Sach WHERE id = ?", (ma,))
        dong = con_tro.fetchone()
        return dict(dong) if dong else None

    def muon_sach(self, ma: int) -> bool:
        """Mượn một cuốn; từ chối nếu sách không còn."""
        dong = self._lay_sach(ma)
        if dong is None:
            return False
        if dong["dang_muon"] >= dong["so_luong"]:
            raise ValueError("Sach nay da duoc muon het")
        with self.ket_noi:
            self.ket_noi.execute(
                "UPDATE Sach SET dang_muon = dang_muon + 1 WHERE id = ?", (ma,)
            )
        return True


tv = ThuVien()
ma = tv.them_sach(Sach("Nha Gia Kim", "Paulo Coelho", 1988, 2))

print("Muon lan 1:", tv.muon_sach(ma))      # True
print("Muon lan 2:", tv.muon_sach(ma))      # True
try:
    tv.muon_sach(ma)                         # hết sách -> ValueError
except ValueError as loi:
    print("Loi:", loi)
print("Muon sach khong ton tai:", tv.muon_sach(999))   # False
tv.ket_noi.close()
```

**Giải thích code:**
* `dang_muon = dang_muon + 1` — SQL tự tăng **trên database**, không cần đọc rồi gán lại qua Python — tránh "race condition" khi hai máy cùng truy cập.
* So sánh `>=` không phải `==`: chỉ cần mượn đủ hết là chặn, kể cả dữ liệu từng bị lỗi.
* `raise ValueError` — để tầng `App` in lời nhắn; còn `return False` — để `App` in "không tìm thấy" (bài 19).

**Độ phức tạp:** O(1).

---

### Bài 13: Trả sách

**Phân tích:** Phép toán ngược của bài 12 nhưng có một ràng buộc riêng: **không thể trả khi chưa mượn** — tránh `dang_muon` thành số âm.

**Ý tưởng:** Kiểm tra tồn tại → `False`; `dang_muon <= 0` → `raise ValueError`; còn thì `dang_muon = dang_muon - 1`.

**Thuật toán:**
1. `dong = _lay_sach(ma)`; `None` → `False`.
2. `dong["dang_muon"] <= 0` → `raise ValueError`.
3. `UPDATE ... dang_muon = dang_muon - 1`.
4. `return True`.

**Code:**

```python
import sqlite3
from typing import Dict, List, Optional


class Sach:
    """Một đầu sách trong thư viện."""

    def __init__(self, ten: str, tac_gia: str, nam: int, so_luong: int = 1,
                 dang_muon: int = 0, ma: Optional[int] = None) -> None:
        self.ma = ma
        self.ten = ten
        self.tac_gia = tac_gia
        self.nam = nam
        self.so_luong = so_luong
        self.dang_muon = dang_muon


class ThuVien:
    """Quản lý mọi thao tác với cơ sở dữ liệu SQLite."""

    def __init__(self, duong_dan_db: str = "thu_vien.db") -> None:
        self.duong_dan_db = duong_dan_db
        self.ket_noi = sqlite3.connect(duong_dan_db)
        self.ket_noi.row_factory = sqlite3.Row
        self.tao_bang()

    def tao_bang(self) -> None:
        """Tạo bảng Sach nếu chưa tồn tại."""
        with self.ket_noi:
            self.ket_noi.execute(
                """CREATE TABLE IF NOT EXISTS Sach (
                       id         INTEGER PRIMARY KEY AUTOINCREMENT,
                       ten        TEXT    NOT NULL,
                       tac_gia    TEXT    NOT NULL,
                       nam        INTEGER,
                       so_luong   INTEGER NOT NULL,
                       dang_muon  INTEGER NOT NULL DEFAULT 0
                   )"""
            )

    def them_sach(self, sach: Sach) -> int:
        """Thêm đầu sách mới; trả về mã sách vừa tạo."""
        with self.ket_noi:
            con_tro = self.ket_noi.execute(
                "INSERT INTO Sach (ten, tac_gia, nam, so_luong, dang_muon) "
                "VALUES (?, ?, ?, ?, ?)",
                (sach.ten, sach.tac_gia, sach.nam, sach.so_luong, sach.dang_muon),
            )
        return con_tro.lastrowid

    def _lay_sach(self, ma: int) -> Optional[Dict[str, object]]:
        """Lấy một dòng sách theo mã; trả về None nếu không có."""
        con_tro = self.ket_noi.execute("SELECT * FROM Sach WHERE id = ?", (ma,))
        dong = con_tro.fetchone()
        return dict(dong) if dong else None

    def tra_sach(self, ma: int) -> bool:
        """Trả một cuốn; từ chối nếu không có cuốn nào đang mượn."""
        dong = self._lay_sach(ma)
        if dong is None:
            return False
        if dong["dang_muon"] <= 0:
            raise ValueError("Khong co cuon nao dang muon de tra")
        with self.ket_noi:
            self.ket_noi.execute(
                "UPDATE Sach SET dang_muon = dang_muon - 1 WHERE id = ?", (ma,)
            )
        return True


tv = ThuVien()
ma = tv.them_sach(Sach("Nha Gia Kim", "Paulo Coelho", 1988, 2))
tv.muon_sach(ma)      # mượn 1 cuốn để có thứ trả

print("Tra lan 1:", tv.tra_sach(ma))     # True
try:
    tv.tra_sach(ma)                       # không còn cuốn đang mượn
except ValueError as loi:
    print("Loi:", loi)
print("Tra sach khong ton tai:", tv.tra_sach(999))   # False
tv.ket_noi.close()
```

**Giải thích code:**
* Điều kiện `<= 0` — chặn mọi khả năng `dang_muon` xuống âm; một số âm sẽ làm `con_lai = so_luong - dang_muon` vượt cả tổng kho — lỗi logic khó phát hiện.
* Cặp bài 12 + 13 hoàn chỉnh "vòng đời" một cuốn sách: mượn → đang mượn → trả → lên kệ.

**Độ phức tạp:** O(1).

---

### Bài 14: Thống kê thư viện

**Phân tích:** Database tính hộ mọi con số — không cần kéo toàn bộ dữ liệu về Python. Bẫy duy nhất: `SUM` trên bảng trống trả `NULL`.

**Ý tưởng:** Một câu `SELECT` với `COUNT(*)`, `SUM`, `COALESCE`; `AS` đặt tên cột; tính `con_lai` bằng Python.

**Thuật toán:**
1. `SELECT COUNT(*) AS so_dau, COALESCE(SUM(so_luong), 0) AS tong_cuon, COALESCE(SUM(dang_muon), 0) AS dang_muon FROM Sach`.
2. `dict(fetchone())` thành từ điển.
3. Thêm khóa `con_lai = tong_cuon - dang_muon`.
4. Trả về.

**Code:**

```python
import sqlite3
from typing import Dict, List, Optional


class Sach:
    """Một đầu sách trong thư viện."""

    def __init__(self, ten: str, tac_gia: str, nam: int, so_luong: int = 1,
                 dang_muon: int = 0, ma: Optional[int] = None) -> None:
        self.ma = ma
        self.ten = ten
        self.tac_gia = tac_gia
        self.nam = nam
        self.so_luong = so_luong
        self.dang_muon = dang_muon


class ThuVien:
    """Quản lý mọi thao tác với cơ sở dữ liệu SQLite."""

    def __init__(self, duong_dan_db: str = "thu_vien.db") -> None:
        self.duong_dan_db = duong_dan_db
        self.ket_noi = sqlite3.connect(duong_dan_db)
        self.ket_noi.row_factory = sqlite3.Row
        self.tao_bang()

    def tao_bang(self) -> None:
        """Tạo bảng Sach nếu chưa tồn tại."""
        with self.ket_noi:
            self.ket_noi.execute(
                """CREATE TABLE IF NOT EXISTS Sach (
                       id         INTEGER PRIMARY KEY AUTOINCREMENT,
                       ten        TEXT    NOT NULL,
                       tac_gia    TEXT    NOT NULL,
                       nam        INTEGER,
                       so_luong   INTEGER NOT NULL,
                       dang_muon  INTEGER NOT NULL DEFAULT 0
                   )"""
            )

    def them_sach(self, sach: Sach) -> int:
        """Thêm đầu sách mới; trả về mã sách vừa tạo."""
        with self.ket_noi:
            con_tro = self.ket_noi.execute(
                "INSERT INTO Sach (ten, tac_gia, nam, so_luong, dang_muon) "
                "VALUES (?, ?, ?, ?, ?)",
                (sach.ten, sach.tac_gia, sach.nam, sach.so_luong, sach.dang_muon),
            )
        return con_tro.lastrowid

    def muon_sach(self, ma: int) -> bool:
        """Mượn một cuốn; từ chối nếu sách không còn."""
        dong = self._lay_sach(ma)
        if dong is None:
            return False
        if dong["dang_muon"] >= dong["so_luong"]:
            raise ValueError("Sach nay da duoc muon het")
        with self.ket_noi:
            self.ket_noi.execute(
                "UPDATE Sach SET dang_muon = dang_muon + 1 WHERE id = ?", (ma,)
            )
        return True

    def _lay_sach(self, ma: int) -> Optional[Dict[str, object]]:
        """Lấy một dòng sách theo mã; trả về None nếu không có."""
        con_tro = self.ket_noi.execute("SELECT * FROM Sach WHERE id = ?", (ma,))
        dong = con_tro.fetchone()
        return dict(dong) if dong else None

    def thong_ke(self) -> Dict[str, object]:
        """Tổng hợp: đầu sách, tổng cuốn, đang mượn, còn lại."""
        con_tro = self.ket_noi.execute(
            """SELECT COUNT(*) AS so_dau,
                      COALESCE(SUM(so_luong), 0)  AS tong_cuon,
                      COALESCE(SUM(dang_muon), 0) AS dang_muon
               FROM Sach"""
        )
        dong = dict(con_tro.fetchone())
        dong["con_lai"] = dong["tong_cuon"] - dong["dang_muon"]
        return dong


tv = ThuVien()
ma1 = tv.them_sach(Sach("De Men Phieu Luu Ky", "To Hoai", 1941, 3))
ma2 = tv.them_sach(Sach("Tuoi tho du doi", "Nguyen Nhat Anh", 2008, 2))
tv.muon_sach(ma1)     # đang mượn 1 cuốn

print(tv.thong_ke())
tv.ket_noi.close()
```

**Giải thích code:**
* `COUNT(*)` — đếm số dòng = số đầu sách. Không bao giờ trả `NULL`.
* `COALESCE(x, 0)` — nếu `x` là `NULL` thì thay bằng `0`. `SUM` trên bảng trống trả `NULL`; bỏ `COALESCE`, bảng trống sẽ báo cáo `tong_cuon: None` và `con_lai` phép trừ sẽ gãy.
* `AS so_dau` — đặt tên cho cột tính toán; nhờ `row_factory`, `dict()` giữ đúng các tên này.
* `con_lai` tính bằng Python vì nó là phép trừ hai cột đã có sẵn — thêm vào cùng một truy vấn cũng được, nhưng tách ra dễ đọc hơn.

**Độ phức tạp:** O(n) — `SUM`/`COUNT` phải quét các dòng.

---

### Bài 15: In danh sách sách dạng bảng

**Phân tích:** Dữ liệu lấy từ database đã là list dict; công việc còn lại là trình bày. Hàm **không dùng chung database** — nhận list đầu vào, dễ kiểm thử.

**Ý tưởng:** f-string với `:<N` căn trái trên độ rộng cố định; tiêu đề và gạch ngang tạo khung bảng.

**Thuật toán:**
1. Danh sách rỗng → in "Khong co sach nao." và `return`.
2. Xây chuỗi tiêu đề 6 cột với độ rộng cố định.
3. In tiêu đề + đường gạch `"-" * len(tieu_de)`.
4. Duyệt từng sách, in một dòng với cùng độ rộng.

**Code:**

```python
from typing import Dict, List


def in_bang_sach(danh_sach: List[Dict[str, object]]) -> None:
    """In danh sách sách dạng bảng với các cột thẳng hàng."""
    if not danh_sach:
        print("Khong co sach nao.")
        return
    tieu_de = f"{'Ma':<4}{'Ten':<28}{'Tac gia':<18}{'Nam':<6}{'SL':<4}{'Dang muon':<10}"
    print(tieu_de)
    print("-" * len(tieu_de))
    for s in danh_sach:
        print(f"{s['id']:<4}{s['ten']:<28}{s['tac_gia']:<18}"
              f"{s['nam']:<6}{s['so_luong']:<4}{s['dang_muon']:<10}")


mau = [
    {"id": 1, "ten": "De Men Phieu Luu Ky", "tac_gia": "To Hoai",
     "nam": 1941, "so_luong": 3, "dang_muon": 1},
    {"id": 2, "ten": "Tuoi tho du doi", "tac_gia": "Nguyen Nhat Anh",
     "nam": 2008, "so_luong": 2, "dang_muon": 0},
]
in_bang_sach(mau)
in_bang_sach([])   # Khong co sach nao.
```

**Giải thích code:**
* `f"{'Ma':<4}"` — chuỗi hằng `'Ma'` bên trong cặp ngoặc nhọn của f-string → in ra `"Ma  "` (đủ 4 ký tự, căn trái). `<` = căn trái, con số = độ rộng (bài 18).
* `{"Ten":<28}` — cột tên rộng 28 cho tên sách dài; cột khác ngắn hơn để bảng không quá to.
* `"-" * len(tieu_de)` — nhân chuỗi (bài 10) tạo đường gạch vừa khít bề rộng tiêu đề.
* `-> None` — hàm chỉ in, không trả dữ liệu.

**Độ phức tạp:** O(n) — in n dòng.

---

### Bài 16: Nhập liệu an toàn — không bao giờ cho phép gõ sai

**Phân tích:** Người dùng là "kẻ thù" lớn nhất của chương trình: gõ chữ vào chỗ số, bỏ trống tên, số lượng âm... Mục tiêu: **không bao giờ để chương trình gãy vì nhập liệu**.

**Ý tưởng:** `while True` + `try/except ValueError` cho số; `while not ten` cho chuỗi rỗng; vòng lặp phụ kiểm tra `so_luong >= 0`.

**Thuật toán:**
1. `nhap_so_nguyen`: lặp `int(input())`; `except ValueError` → in cảnh báo → hỏi lại.
2. `nhap_sach_moi`: nhập `ten`, lặp khi rỗng; nhập `tac_gia`, lặp khi rỗng; `nam` = `nhap_so_nguyen`; `so_luong` = `nhap_so_nguyen` rồi lặp khi `so_luong < 0`.
3. Trả `Sach(...)`.

**Code:**

```python
from typing import Optional


class Sach:
    """Một đầu sách trong thư viện."""

    def __init__(self, ten: str, tac_gia: str, nam: int, so_luong: int = 1,
                 dang_muon: int = 0, ma: Optional[int] = None) -> None:
        self.ma = ma
        self.ten = ten
        self.tac_gia = tac_gia
        self.nam = nam
        self.so_luong = so_luong
        self.dang_muon = dang_muon


def nhap_so_nguyen(loi_nhan: str) -> int:
    """Nhập số nguyên; lặp lại đến khi người dùng gõ đúng."""
    while True:
        try:
            return int(input(loi_nhan))      # Nhập: abc
        except ValueError:
            print("Vui long nhap mot so nguyen hop le.")


def nhap_sach_moi() -> Sach:
    """Hỏi thông tin rồi tạo đối tượng Sach mới (dữ liệu hợp lệ bắt buộc)."""
    ten = input("Ten sach: ").strip()
    while not ten:                            # Nhập: (Enter) -> hỏi lại
        ten = input("Ten sach khong duoc rong, nhap lai: ").strip()

    tac_gia = input("Tac gia: ").strip()
    while not tac_gia:
        tac_gia = input("Tac gia khong duoc rong, nhap lai: ").strip()

    nam = nhap_so_nguyen("Nam xuat ban: ")    # Nhập: 1941
    so_luong = nhap_so_nguyen("So luong: ")   # Nhập: -1 -> hỏi lại
    while so_luong < 0:
        so_luong = nhap_so_nguyen("So luong phai >= 0, nhap lai: ")

    return Sach(ten, tac_gia, nam, so_luong)


sach = nhap_sach_moi()
print("Da tao:", sach)
```

**Giải thích code:**
* `return int(input(loi_nhan))` trong `try` — thành công thì trả về và **thoát vòng lặp ngay**; thất bại thì cảnh báo và hỏi lại.
* `while not ten` — chuỗi rỗng (kể cả toàn khoảng trắng sau `strip`) là "sai" trong Python → vòng lặp giữ người dùng cho tới khi nhập đủ.
* Block `while so_luong < 0` — kiểm tra **miền giá trị**, không phải kiểu; биên giới hợp lệ của nghiệp vụ được kiểm soát ngay tầng nhập.
* Kết quả là một hàm dùng được ngay trong `App` của bài 18 — tiết kiệm viết lại.

**Độ phức tạp:** O(1) — mỗi lần nhập kiểm tra hằng số lần trung bình.

---

### Bài 17: Xử lý lỗi toàn diện cho mượn/trả

**Phân tích:** Bài này thống nhất mọi "kênh lỗi" của mượn/trả thành một chỗ: `return False` (không tồn tại) và `raise ValueError` (vi phạm nghiệp vụ) — cả hai đều phải xử lý để chương trình không gãy.

**Ý tưởng:** Hàm `xu_ly_muon_tra` nhận `thu_vien`, `ma`, `loai`; gọi phương thức tương ứng trong `try/except`; phân biệt thông báo theo `False` hay `ValueError`.

**Thuật toán:**
1. Chọn `muon_sach` hay `tra_sach` theo `loai`.
2. `try`: kết quả `True` → "Thanh cong.", `False` → "Khong tim thay sach".
3. `except ValueError as loi:` → in `"Loi:", loi`.
4. Kiểm thử đủ 5 tình huống — không có traceback.

**Code:**

```python
import sqlite3
from typing import Dict, Optional


class Sach:
    """Một đầu sách trong thư viện."""

    def __init__(self, ten: str, tac_gia: str, nam: int, so_luong: int = 1,
                 dang_muon: int = 0, ma: Optional[int] = None) -> None:
        self.ma = ma
        self.ten = ten
        self.tac_gia = tac_gia
        self.nam = nam
        self.so_luong = so_luong
        self.dang_muon = dang_muon


class ThuVien:
    """Quản lý mọi thao tác với cơ sở dữ liệu SQLite."""

    def __init__(self, duong_dan_db: str = "thu_vien.db") -> None:
        self.duong_dan_db = duong_dan_db
        self.ket_noi = sqlite3.connect(duong_dan_db)
        self.ket_noi.row_factory = sqlite3.Row
        self.tao_bang()

    def tao_bang(self) -> None:
        """Tạo bảng Sach nếu chưa tồn tại."""
        with self.ket_noi:
            self.ket_noi.execute(
                """CREATE TABLE IF NOT EXISTS Sach (
                       id         INTEGER PRIMARY KEY AUTOINCREMENT,
                       ten        TEXT    NOT NULL,
                       tac_gia    TEXT    NOT NULL,
                       nam        INTEGER,
                       so_luong   INTEGER NOT NULL,
                       dang_muon  INTEGER NOT NULL DEFAULT 0
                   )"""
            )

    def them_sach(self, sach: Sach) -> int:
        """Thêm đầu sách mới; trả về mã sách vừa tạo."""
        with self.ket_noi:
            con_tro = self.ket_noi.execute(
                "INSERT INTO Sach (ten, tac_gia, nam, so_luong, dang_muon) "
                "VALUES (?, ?, ?, ?, ?)",
                (sach.ten, sach.tac_gia, sach.nam, sach.so_luong, sach.dang_muon),
            )
        return con_tro.lastrowid

    def _lay_sach(self, ma: int) -> Optional[Dict[str, object]]:
        """Lấy một dòng sách theo mã; trả về None nếu không có."""
        con_tro = self.ket_noi.execute("SELECT * FROM Sach WHERE id = ?", (ma,))
        dong = con_tro.fetchone()
        return dict(dong) if dong else None

    def muon_sach(self, ma: int) -> bool:
        """Mượn một cuốn; từ chối nếu sách không còn."""
        dong = self._lay_sach(ma)
        if dong is None:
            return False
        if dong["dang_muon"] >= dong["so_luong"]:
            raise ValueError("Sach nay da duoc muon het")
        with self.ket_noi:
            self.ket_noi.execute(
                "UPDATE Sach SET dang_muon = dang_muon + 1 WHERE id = ?", (ma,)
            )
        return True

    def tra_sach(self, ma: int) -> bool:
        """Trả một cuốn; từ chối nếu không có cuốn nào đang mượn."""
        dong = self._lay_sach(ma)
        if dong is None:
            return False
        if dong["dang_muon"] <= 0:
            raise ValueError("Khong co cuon nao dang muon de tra")
        with self.ket_noi:
            self.ket_noi.execute(
                "UPDATE Sach SET dang_muon = dang_muon - 1 WHERE id = ?", (ma,)
            )
        return True


def xu_ly_muon_tra(thu_vien: ThuVien, ma: int, loai: str) -> None:
    """Mượn hoặc trả sách; bắt mọi lỗi để chương trình không gãy."""
    try:
        if loai == "muon":
            ok = thu_vien.muon_sach(ma)
        else:
            ok = thu_vien.tra_sach(ma)
        if ok:
            print("Thanh cong.")
        else:
            print("Khong tim thay sach co ma", ma)
    except ValueError as loi:
        print("Loi:", loi)


tv = ThuVien()
ma = tv.them_sach(Sach("Nha Gia Kim", "Paulo Coelho", 1988, 1))

xu_ly_muon_tra(tv, ma, "muon")               # Thanh cong.
xu_ly_muon_tra(tv, ma, "muon")               # Loi: Sach nay da duoc muon het
xu_ly_muon_tra(tv, ma, "tra")                # Thanh cong.
xu_ly_muon_tra(tv, ma, "tra")                # Loi: Khong co cuon nao dang muon de tra
xu_ly_muon_tra(tv, 999, "muon")              # Khong tim thay sach co ma 999
tv.ket_noi.close()
```

**Giải thích code:**
* `try/except ValueError` chỉ bao lấy **phần nguy hiểm** — không bao toàn bộ chương trình: lỗi nghiệp vụ được bắt, còn bug lập trình thì vẫn nên lộ ra để biết mà sửa.
* `except ValueError as loi` — `loi` chứa chuỗi thông điệp đã viết trong `raise` — in thẳng ra cho người dùng đọc.
* Hàm trả `None` (chỉ in thông báo) — vai trò đúng đắn của tầng giao diện.

**Độ phức tạp:** O(1).

---

### Bài 18: Menu hoàn chỉnh

**Phân tích:** Bài tổng hợp: mọi thứ từ bài 1–17 ráp vào class `App`. `App` chỉ làm đúng 3 việc: in menu, nhập liệu an toàn, gọi `ThuVien`.

**Ý tưởng:** `__init__` tạo `self.thu_vien`; `in_menu` in 10 lựa chọn; `chay` là `while True` + `if/elif` gọi từng hàm — mỗi nhánh ngắn gọn, việc dài tách sang hàm riêng.

**Thuật toán:**
1. `__init__`: `self.thu_vien = ThuVien()`.
2. `in_menu`: in 9 chức năng + thoát.
3. `chay`: lặp — in menu, đọc lựa chọn, rẽ `if/elif` theo 10 nhánh; chọn "0" → đóng kết nối, `break`.
4. `if __name__ == "__main__":` khởi động.

**Code:**

```python
# quan_ly_thu_vien.py (bản đang xây dần — nối tiếp các bài trước)

import sqlite3
from typing import Dict, List, Optional


class Sach:
    """Một đầu sách trong thư viện."""

    def __init__(self, ten: str, tac_gia: str, nam: int, so_luong: int = 1,
                 dang_muon: int = 0, ma: Optional[int] = None) -> None:
        self.ma = ma
        self.ten = ten
        self.tac_gia = tac_gia
        self.nam = nam
        self.so_luong = so_luong
        self.dang_muon = dang_muon

    @property
    def con_lai(self) -> int:
        """Số cuốn còn lại chưa được mượn."""
        return self.so_luong - self.dang_muon

    def __str__(self) -> str:
        trang_thai = "con" if self.con_lai > 0 else "het"
        return (f"[{self.ma}] {self.ten} - {self.tac_gia} ({self.nam}) | "
                f"con {self.con_lai}/{self.so_luong} cuon [{trang_thai}]")


class ThuVien:
    """Quản lý mọi thao tác với cơ sở dữ liệu SQLite."""

    COT_HOP_LE = ("ten", "tac_gia", "nam", "so_luong")

    def __init__(self, duong_dan_db: str = "thu_vien.db") -> None:
        self.duong_dan_db = duong_dan_db
        self.ket_noi = sqlite3.connect(duong_dan_db)
        self.ket_noi.row_factory = sqlite3.Row
        self.tao_bang()

    def tao_bang(self) -> None:
        """Tạo bảng Sach nếu chưa tồn tại."""
        with self.ket_noi:
            self.ket_noi.execute(
                """CREATE TABLE IF NOT EXISTS Sach (
                       id         INTEGER PRIMARY KEY AUTOINCREMENT,
                       ten        TEXT    NOT NULL,
                       tac_gia    TEXT    NOT NULL,
                       nam        INTEGER,
                       so_luong   INTEGER NOT NULL,
                       dang_muon  INTEGER NOT NULL DEFAULT 0
                   )"""
            )

    def them_sach(self, sach: Sach) -> int:
        """Thêm đầu sách mới; trả về mã sách vừa tạo."""
        with self.ket_noi:
            con_tro = self.ket_noi.execute(
                "INSERT INTO Sach (ten, tac_gia, nam, so_luong, dang_muon) "
                "VALUES (?, ?, ?, ?, ?)",
                (sach.ten, sach.tac_gia, sach.nam, sach.so_luong, sach.dang_muon),
            )
        return con_tro.lastrowid

    def xem_danh_sach(self) -> List[Dict[str, object]]:
        """Trả về danh sách toàn bộ đầu sách, sắp theo mã."""
        con_tro = self.ket_noi.execute("SELECT * FROM Sach ORDER BY id")
        return [dict(dong) for dong in con_tro.fetchall()]

    def tim_theo_ten(self, ten_can_tim: str) -> List[Dict[str, object]]:
        """Tìm đầu sách có tên chứa chuỗi cho trước."""
        con_tro = self.ket_noi.execute(
            "SELECT * FROM Sach WHERE ten LIKE ? ORDER BY id",
            (f"%{ten_can_tim.strip()}%",),
        )
        return [dict(dong) for dong in con_tro.fetchall()]

    def tim_theo_tac_gia(self, tac_gia_can_tim: str) -> List[Dict[str, object]]:
        """Tìm đầu sách theo tác giả."""
        con_tro = self.ket_noi.execute(
            "SELECT * FROM Sach WHERE tac_gia LIKE ? ORDER BY id",
            (f"%{tac_gia_can_tim.strip()}%",),
        )
        return [dict(dong) for dong in con_tro.fetchall()]

    def _lay_sach(self, ma: int) -> Optional[Dict[str, object]]:
        """Lấy một dòng sách theo mã; trả về None nếu không có."""
        con_tro = self.ket_noi.execute("SELECT * FROM Sach WHERE id = ?", (ma,))
        dong = con_tro.fetchone()
        return dict(dong) if dong else None

    def sua_sach(self, ma: int, cot: str, gia_tri: object) -> bool:
        """Sửa một cột hợp lệ của đầu sách; trả về True nếu sửa được."""
        if cot not in ThuVien.COT_HOP_LE:
            raise ValueError(f"Khong ho tro sua cot: {cot}")
        if self._lay_sach(ma) is None:
            return False
        with self.ket_noi:
            self.ket_noi.execute(
                f"UPDATE Sach SET {cot} = ? WHERE id = ?", (gia_tri, ma)
            )
        return True

    def xoa_sach(self, ma: int) -> bool:
        """Xóa đầu sách theo mã; trả về True nếu xóa được."""
        if self._lay_sach(ma) is None:
            return False
        with self.ket_noi:
            self.ket_noi.execute("DELETE FROM Sach WHERE id = ?", (ma,))
        return True

    def muon_sach(self, ma: int) -> bool:
        """Mượn một cuốn; từ chối nếu sách không còn."""
        dong = self._lay_sach(ma)
        if dong is None:
            return False
        if dong["dang_muon"] >= dong["so_luong"]:
            raise ValueError("Sach nay da duoc muon het")
        with self.ket_noi:
            self.ket_noi.execute(
                "UPDATE Sach SET dang_muon = dang_muon + 1 WHERE id = ?", (ma,)
            )
        return True

    def tra_sach(self, ma: int) -> bool:
        """Trả một cuốn; từ chối nếu không có cuốn nào đang mượn."""
        dong = self._lay_sach(ma)
        if dong is None:
            return False
        if dong["dang_muon"] <= 0:
            raise ValueError("Khong co cuon nao dang muon de tra")
        with self.ket_noi:
            self.ket_noi.execute(
                "UPDATE Sach SET dang_muon = dang_muon - 1 WHERE id = ?", (ma,)
            )
        return True

    def thong_ke(self) -> Dict[str, object]:
        """Tổng hợp: đầu sách, tổng cuốn, đang mượn, còn lại."""
        con_tro = self.ket_noi.execute(
            """SELECT COUNT(*) AS so_dau,
                      COALESCE(SUM(so_luong), 0)  AS tong_cuon,
                      COALESCE(SUM(dang_muon), 0) AS dang_muon
               FROM Sach"""
        )
        dong = dict(con_tro.fetchone())
        dong["con_lai"] = dong["tong_cuon"] - dong["dang_muon"]
        return dong

    def dong_ket_noi(self) -> None:
        """Đóng kết nối trước khi thoát chương trình."""
        self.ket_noi.close()


class App:
    """Giao diện menu điều khiển toàn bộ chương trình."""

    def __init__(self) -> None:
        self.thu_vien = ThuVien()

    def in_menu(self) -> None:
        """In bảng menu cho người dùng."""
        print("\n===== QUAN LY THU VIEN =====")
        print("1. Them sach")
        print("2. Xem danh sach")
        print("3. Tim theo ten")
        print("4. Tim theo tac gia")
        print("5. Muon sach")
        print("6. Tra sach")
        print("7. Sua sach")
        print("8. Xoa sach")
        print("9. Thong ke")
        print("0. Thoat")

    def in_bang_sach(self, danh_sach: List[Dict[str, object]]) -> None:
        """In danh sách sách dạng bảng thẳng hàng."""
        if not danh_sach:
            print("Khong co sach nao.")
            return
        tieu_de = f"{'Ma':<4}{'Ten':<28}{'Tac gia':<18}{'Nam':<6}{'SL':<4}{'Dang muon':<10}"
        print(tieu_de)
        print("-" * len(tieu_de))
        for s in danh_sach:
            print(f"{s['id']:<4}{s['ten']:<28}{s['tac_gia']:<18}"
                  f"{s['nam']:<6}{s['so_luong']:<4}{s['dang_muon']:<10}")

    def nhap_so_nguyen(self, loi_nhan: str) -> int:
        """Nhập số nguyên; lặp lại đến khi người dùng gõ đúng."""
        while True:
            try:
                return int(input(loi_nhan))
            except ValueError:
                print("Vui long nhap mot so nguyen hop le.")

    def nhap_sach_moi(self) -> Sach:
        """Hỏi thông tin rồi tạo đối tượng Sach mới."""
        ten = input("Ten sach: ").strip()
        while not ten:                                 # Nhập: (Enter)
            ten = input("Ten sach khong duoc rong, nhap lai: ").strip()
        tac_gia = input("Tac gia: ").strip()
        while not tac_gia:
            tac_gia = input("Tac gia khong duoc rong, nhap lai: ").strip()
        nam = self.nhap_so_nguyen("Nam xuat ban: ")    # Nhập: 1941
        so_luong = self.nhap_so_nguyen("So luong: ")   # Nhập: 3
        while so_luong < 0:
            so_luong = self.nhap_so_nguyen("So luong phai >= 0, nhap lai: ")
        return Sach(ten, tac_gia, nam, so_luong)

    def xu_ly_muon_tra(self, ma: int, loai: str) -> None:
        """Mượn hoặc trả sách, bắt mọi lỗi để chương trình không gãy."""
        try:
            if loai == "muon":
                ok = self.thu_vien.muon_sach(ma)
            else:
                ok = self.thu_vien.tra_sach(ma)
            if ok:
                print("Thanh cong.")
            else:
                print("Khong tim thay sach co ma", ma)
        except ValueError as loi:
            print("Loi:", loi)

    def xu_ly_sua_sach(self) -> None:
        """Hỏi cột cần sửa rồi cập nhật một giá trị."""
        ma = self.nhap_so_nguyen("Ma sach can sua: ")   # Nhập: 1
        if self.thu_vien._lay_sach(ma) is None:
            print("Khong tim thay sach co ma", ma)
            return
        print("Cot hop le: ten, tac_gia, nam, so_luong")
        cot = input("Ten cot can sua: ").strip()         # Nhập: so_luong
        if cot not in ThuVien.COT_HOP_LE:
            print("Cot khong hop le.")
            return
        if cot in ("nam", "so_luong"):
            gia_tri = self.nhap_so_nguyen("Gia tri moi: ")   # Nhập: 5
        else:
            gia_tri = input("Gia tri moi: ").strip()         # Nhập: De Men Moi
        print("Da sua sach ma", ma if self.thu_vien.sua_sach(ma, cot, gia_tri)
              else "that bai.")

    def xu_ly_thong_ke(self) -> None:
        """In báo cáo thống kê thư viện."""
        tk = self.thu_vien.thong_ke()
        print("\n----- THONG KE THU VIEN -----")
        print(f"So dau sach      : {tk['so_dau']}")
        print(f"Tong so cuon     : {tk['tong_cuon']}")
        print(f"Dang duoc muon   : {tk['dang_muon']}")
        print(f"Con lai tren ke  : {tk['con_lai']}")

    def chay(self) -> None:
        """Vòng lặp menu chính của chương trình."""
        while True:
            self.in_menu()
            chon = input("Chon chuc nang: ").strip()     # Nhập: 1
            if chon == "1":
                sach = self.nhap_sach_moi()
                print("Da them sach ma", self.thu_vien.them_sach(sach))
            elif chon == "2":
                self.in_bang_sach(self.thu_vien.xem_danh_sach())
            elif chon == "3":
                ten = input("Nhap ten can tim: ").strip()   # Nhập: De Men
                self.in_bang_sach(self.thu_vien.tim_theo_ten(ten))
            elif chon == "4":
                tac_gia = input("Nhap tac gia can tim: ").strip()  # Nhập: Hoai
                self.in_bang_sach(self.thu_vien.tim_theo_tac_gia(tac_gia))
            elif chon == "5":
                self.xu_ly_muon_tra(self.nhap_so_nguyen("Ma sach can muon: "), "muon")
            elif chon == "6":
                self.xu_ly_muon_tra(self.nhap_so_nguyen("Ma sach can tra: "), "tra")
            elif chon == "7":
                self.xu_ly_sua_sach()
            elif chon == "8":
                ma = self.nhap_so_nguyen("Ma sach can xoa: ")   # Nhập: 2
                print("Da xoa sach." if self.thu_vien.xoa_sach(ma)
                      else "Khong tim thay sach.")
            elif chon == "9":
                self.xu_ly_thong_ke()
            elif chon == "0":
                print("Tam biet!")
                break
            else:
                print("Lua chon khong hop le.")
        self.thu_vien.dong_ket_noi()


if __name__ == "__main__":
    app = App()
    app.chay()
```

**Giải thích code:**
* Mỗi nhánh `elif` chỉ 1–4 dòng — nếu dài hơn thì nhường cho hàm riêng (`xu_ly_sua_sach`, `xu_ly_thong_ke`, `xu_ly_muon_tra`) → vòng `chay` đọc như bản đồ menu.
* `App` **không viết câu SQL nào**; `ThuVien` **không gọi `input()`** — ranh giới hai lớp được giữ, đúng "một trách nhiệm".
* `xoa_sach` trả `True/False` → lồng vào `print("Da xoa sach." if ... else ...)` — code gọn (bài 8).
* `if __name__ == "__main__":` — chỉ chạy khi gõ trực tiếp file (bài 20).

**Độ phức tạp:** O(1) cho mỗi lần lựa chọn menu (không tính độ phức tạp của hàm con được gọi).

---

### Bài 19: Tối ưu hóa + tìm kiếm tổng hợp

**Phân tích:** Chương trình đã chạy; giờ là giai đoạn "làm sạch": hằng số, docstring, gộp hai hàm tìm kiếm thành một tổng hợp — giảm thao tác cho người dùng.

**Ý tưởng:** Hằng số `TEN_FILE_DB` đặt đầu file; `tim_tong_hop` dùng `WHERE ten LIKE ? OR tac_gia LIKE ?`; đảm bảo mọi SQL dùng `?`.

**Thuật toán:**
1. Đặt `TEN_FILE_DB = "thu_vien.db"` ở đầu file, `__init__` mặc định dùng nó.
2. Thêm `tim_tong_hop(chuoi)` với một câu `WHERE ... OR ...`.
3. Rà soát: mọi giá trị nhập đi qua `?`; docstring đủ cho class và phương thức.
4. Kiểm thử cả hai hướng tìm.

**Code:**

```python
# Chỉ trình bày phần mới/tối ưu — các lớp khác giữ nguyên như bài 18

import sqlite3
from typing import Dict, List, Optional

# File thu_vien.db sẽ được tạo tự động tại thư mục đang chạy chương trình
TEN_FILE_DB = "thu_vien.db"


class Sach:
    """Một đầu sách trong thư viện."""

    def __init__(self, ten: str, tac_gia: str, nam: int, so_luong: int = 1,
                 dang_muon: int = 0, ma: Optional[int] = None) -> None:
        self.ma = ma
        self.ten = ten
        self.tac_gia = tac_gia
        self.nam = nam
        self.so_luong = so_luong
        self.dang_muon = dang_muon


class ThuVien:
    """Quản lý mọi thao tác với cơ sở dữ liệu SQLite."""

    COT_HOP_LE = ("ten", "tac_gia", "nam", "so_luong")

    def __init__(self, duong_dan_db: str = TEN_FILE_DB) -> None:
        """Mở kết nối, bật đọc theo tên cột và tạo bảng nếu chưa có."""
        self.duong_dan_db = duong_dan_db
        self.ket_noi = sqlite3.connect(duong_dan_db)
        self.ket_noi.row_factory = sqlite3.Row
        self.tao_bang()

    def tao_bang(self) -> None:
        """Tạo bảng Sach nếu chưa tồn tại."""
        with self.ket_noi:
            self.ket_noi.execute(
                """CREATE TABLE IF NOT EXISTS Sach (
                       id         INTEGER PRIMARY KEY AUTOINCREMENT,
                       ten        TEXT    NOT NULL,
                       tac_gia    TEXT    NOT NULL,
                       nam        INTEGER,
                       so_luong   INTEGER NOT NULL,
                       dang_muon  INTEGER NOT NULL DEFAULT 0
                   )"""
            )

    def them_sach(self, sach: Sach) -> int:
        """Thêm đầu sách mới; trả về mã sách vừa tạo."""
        with self.ket_noi:
            con_tro = self.ket_noi.execute(
                "INSERT INTO Sach (ten, tac_gia, nam, so_luong, dang_muon) "
                "VALUES (?, ?, ?, ?, ?)",
                (sach.ten, sach.tac_gia, sach.nam, sach.so_luong, sach.dang_muon),
            )
        return con_tro.lastrowid

    def tim_tong_hop(self, chuoi_can_tim: str) -> List[Dict[str, object]]:
        """Tìm theo cả tên lẫn tác giả — người dùng nhớ gì tìm nấy."""
        mau = f"%{chuoi_can_tim.strip()}%"
        con_tro = self.ket_noi.execute(
            "SELECT * FROM Sach WHERE ten LIKE ? OR tac_gia LIKE ? ORDER BY id",
            (mau, mau),
        )
        return [dict(dong) for dong in con_tro.fetchall()]


tv = ThuVien()
tv.them_sach(Sach("De Men Phieu Luu Ky", "To Hoai", 1941, 10))
tv.them_sach(Sach("Tuoi tho du doi", "Nguyen Nhat Anh", 2008, 5))

print("Tim 'hoai' (tac gia):", [s["ten"] for s in tv.tim_tong_hop("hoai")])
print("Tim 'de men' (ten):  ", [s["ten"] for s in tv.tim_tong_hop("de men")])
print("Tim 'tho' (trong ten 'Tuoi tho...'):", [s["ten"] for s in tv.tim_tong_hop("tho")])
tv.ket_noi.close()
```

**Giải thích code:**
* `TEN_FILE_DB` — hằng số: tên file DB chỉ xuất hiện **một lần** trong toàn chương trình; đổi tên DB chỉ sửa một dòng (quy tắc DRY – Don't Repeat Yourself).
* `WHERE ten LIKE ? OR tac_gia LIKE ?` — một lần tìm phủ cả hai cột; cùng một mẫu `mau` truyền hai lần — giữ nguyên placeholder, không ghép chuỗi.
* Docstring viết theo PEP 257: mô tả việc làm, không mô tả chi tiết cài đặt.
* Tối ưu thật sự nằm ở chỗ **giảm API**: thay vì 2 hàm `tim_theo_ten`/`tim_theo_tac_gia`, một hàm tổng hợp phục vụ tốt hơn cho menu thật (bài 20 dùng nó).

**Độ phức tạp:** O(n) — quét toàn bộ để so `LIKE` trên hai cột.

---

### Bài 20: Dự án hoàn chỉnh + kịch bản kiểm thử tổng thể

**Phân tích:** Bước cuối: ghép hoàn chỉnh (đã có ở Bài 18/19) và **chứng minh chương trình đúng** bằng kịch bản kiểm thử tự động — kiểm tra nghiệp vụ lẫn tính bền vững của dữ liệu.

**Ý tưởng:** Viết hàm `kiem_thu()` chạy đúng kịch bản 8 bước, dùng `assert` để máy tự báo sai nếu kết quả không khớp; mở lại database ở cuối để chứng minh dữ liệu còn nguyên.

**Thuật toán:**
1. Xóa file DB cũ (kịch bản bắt đầu sạch) — chú thích rõ để không lạm dụng ngoài kiểm thử.
2. Thêm 3 sách, kiểm tra mã trả về.
3. Mượn sách 1 ba lần; lần 4 bắt `ValueError`.
4. Mượn sách 3; kiểm tra `dang_muon`.
5. Trả sách 1 một lần.
6. `thong_ke()` khớp số liệu.
7. Xóa sách 2; còn 2 sách.
8. Đóng kết nối → mở lại → dữ liệu vẫn còn.

**Code:**

```python
import os
import sqlite3
from typing import Dict, List, Optional

TEN_FILE_DB = "thu_vien.db"


class Sach:
    """Một đầu sách trong thư viện."""

    def __init__(self, ten: str, tac_gia: str, nam: int, so_luong: int = 1,
                 dang_muon: int = 0, ma: Optional[int] = None) -> None:
        self.ma = ma
        self.ten = ten
        self.tac_gia = tac_gia
        self.nam = nam
        self.so_luong = so_luong
        self.dang_muon = dang_muon


class ThuVien:
    """Quản lý mọi thao tác với cơ sở dữ liệu SQLite."""

    COT_HOP_LE = ("ten", "tac_gia", "nam", "so_luong")

    def __init__(self, duong_dan_db: str = TEN_FILE_DB) -> None:
        self.duong_dan_db = duong_dan_db
        self.ket_noi = sqlite3.connect(duong_dan_db)
        self.ket_noi.row_factory = sqlite3.Row
        self.tao_bang()

    def tao_bang(self) -> None:
        """Tạo bảng Sach nếu chưa tồn tại."""
        with self.ket_noi:
            self.ket_noi.execute(
                """CREATE TABLE IF NOT EXISTS Sach (
                       id         INTEGER PRIMARY KEY AUTOINCREMENT,
                       ten        TEXT    NOT NULL,
                       tac_gia    TEXT    NOT NULL,
                       nam        INTEGER,
                       so_luong   INTEGER NOT NULL,
                       dang_muon  INTEGER NOT NULL DEFAULT 0
                   )"""
            )

    def them_sach(self, sach: Sach) -> int:
        """Thêm đầu sách mới; trả về mã sách vừa tạo."""
        with self.ket_noi:
            con_tro = self.ket_noi.execute(
                "INSERT INTO Sach (ten, tac_gia, nam, so_luong, dang_muon) "
                "VALUES (?, ?, ?, ?, ?)",
                (sach.ten, sach.tac_gia, sach.nam, sach.so_luong, sach.dang_muon),
            )
        return con_tro.lastrowid

    def xem_danh_sach(self) -> List[Dict[str, object]]:
        """Trả về danh sách toàn bộ đầu sách, sắp theo mã."""
        con_tro = self.ket_noi.execute("SELECT * FROM Sach ORDER BY id")
        return [dict(dong) for dong in con_tro.fetchall()]

    def _lay_sach(self, ma: int) -> Optional[Dict[str, object]]:
        """Lấy một dòng sách theo mã; trả về None nếu không có."""
        con_tro = self.ket_noi.execute("SELECT * FROM Sach WHERE id = ?", (ma,))
        dong = con_tro.fetchone()
        return dict(dong) if dong else None

    def xoa_sach(self, ma: int) -> bool:
        """Xóa đầu sách theo mã; trả về True nếu xóa được."""
        if self._lay_sach(ma) is None:
            return False
        with self.ket_noi:
            self.ket_noi.execute("DELETE FROM Sach WHERE id = ?", (ma,))
        return True

    def muon_sach(self, ma: int) -> bool:
        """Mượn một cuốn; từ chối nếu sách không còn."""
        dong = self._lay_sach(ma)
        if dong is None:
            return False
        if dong["dang_muon"] >= dong["so_luong"]:
            raise ValueError("Sach nay da duoc muon het")
        with self.ket_noi:
            self.ket_noi.execute(
                "UPDATE Sach SET dang_muon = dang_muon + 1 WHERE id = ?", (ma,)
            )
        return True

    def tra_sach(self, ma: int) -> bool:
        """Trả một cuốn; từ chối nếu không có cuốn nào đang mượn."""
        dong = self._lay_sach(ma)
        if dong is None:
            return False
        if dong["dang_muon"] <= 0:
            raise ValueError("Khong co cuon nao dang muon de tra")
        with self.ket_noi:
            self.ket_noi.execute(
                "UPDATE Sach SET dang_muon = dang_muon - 1 WHERE id = ?", (ma,)
            )
        return True

    def thong_ke(self) -> Dict[str, object]:
        """Tổng hợp: đầu sách, tổng cuốn, đang mượn, còn lại."""
        con_tro = self.ket_noi.execute(
            """SELECT COUNT(*) AS so_dau,
                      COALESCE(SUM(so_luong), 0)  AS tong_cuon,
                      COALESCE(SUM(dang_muon), 0) AS dang_muon
               FROM Sach"""
        )
        dong = dict(con_tro.fetchone())
        dong["con_lai"] = dong["tong_cuon"] - dong["dang_muon"]
        return dong

    def dong_ket_noi(self) -> None:
        """Đóng kết nối trước khi thoát chương trình."""
        self.ket_noi.close()


def kiem_thu() -> None:
    """Chạy kịch bản kiểm thử 8 bước; assert báo lỗi nếu sai."""
    # CHỈ DÙNG TRONG KIỂM THỬ: bắt đầu với database sạch
    if os.path.exists(TEN_FILE_DB):
        os.remove(TEN_FILE_DB)

    tv = ThuVien(TEN_FILE_DB)

    # Bước 1: thêm 3 sách
    ma1 = tv.them_sach(Sach("De Men Phieu Luu Ky", "To Hoai", 1941, 3))
    ma2 = tv.them_sach(Sach("Tuoi tho du doi", "Nguyen Nhat Anh", 2008, 2))
    ma3 = tv.them_sach(Sach("Nha Gia Kim", "Paulo Coelho", 1988, 1))
    assert (ma1, ma2, ma3) == (1, 2, 3)
    print("Buoc 1 - Them 3 sach: OK (ma 1, 2, 3)")

    # Bước 2: xem danh sách — đúng 3 đầu sách
    assert len(tv.xem_danh_sach()) == 3
    print("Buoc 2 - Xem danh sach: OK (3 dau sach)")

    # Bước 3: mượn sách 1 ba lần (3 cuốn), lần 4 phải báo lỗi
    assert tv.muon_sach(ma1) and tv.muon_sach(ma1) and tv.muon_sach(ma1)
    try:
        tv.muon_sach(ma1)
        raise SystemExit("Sai: dang le phai bao het sach")
    except ValueError:
        pass
    print("Buoc 3 - Muon het 3/3 cuon: OK (lan 4 bao loi)")

    # Bước 4: mượn sách 3 (chỉ có 1 cuốn) — đang mượn tăng đúng
    assert tv.muon_sach(ma3)
    dong1 = tv._lay_sach(ma1)
    dong3 = tv._lay_sach(ma3)
    assert dong1["dang_muon"] == 3 and dong3["dang_muon"] == 1
    print("Buoc 4 - Muon sach 3: OK (dang_muon: sach1=3, sach3=1)")

    # Bước 5: trả sách 1 một lần
    assert tv.tra_sach(ma1)
    assert tv._lay_sach(ma1)["dang_muon"] == 2
    print("Buoc 5 - Tra sach 1: OK (dang_muon=2)")

    # Bước 6: thống kê — 3 đầu, 6 cuốn, mượn 3, còn 3
    tk = tv.thong_ke()
    assert (tk["so_dau"], tk["tong_cuon"], tk["dang_muon"], tk["con_lai"]) == (3, 6, 3, 3)
    print("Buoc 6 - Thong ke: OK", tk)

    # Bước 7: xóa sách 2
    assert tv.xoa_sach(ma2)
    assert len(tv.xem_danh_sach()) == 2
    print("Buoc 7 - Xoa sach 2: OK (con 2 dau sach)")

    # Bước 8: đóng, mở lại — dữ liệu vẫn còn (bền vững)
    tv.dong_ket_noi()
    tv_moi = ThuVien(TEN_FILE_DB)
    assert len(tv_moi.xem_danh_sach()) == 2
    print("Buoc 8 - Mo lai chuong trinh: OK (du lieu con nguyen)")
    tv_moi.dong_ket_noi()

    print("\n✅ TAT CA 8 BUOC DEU QUA — DU AN SAN SAN NOP BAI!")


if __name__ == "__main__":
    kiem_thu()
```

**Giải thích code:**
* `assert dieu_kien` — nếu điều kiện sai, chương trình dừng và báo lỗi: máy tự kiểm tra thay con người đếm tay (bài 19, 23).
* Bước 3 dùng `try/except ValueError` **ngược**: mong đợi lỗi xuất hiện — nếu không xuất hiện nghĩa là hàm mượn sai.
* Bước 8 là **điểm mấu chốt của SQLite**: đóng kết nối, mở lại, dữ liệu vẫn nguyên — điều mà List+JSON của bài 40 phải lưu tay mới có được.
* Kịch bản này có thể dán vào cuối bài nộp như "bằng chứng kiểm thử" — điểm sáng tạo trong rubric.

**Độ phức tạp:** Tổng thể kịch bản O(n) — mỗi thao tác database là O(1) với khóa chính, O(n) với `LIKE`/`SUM`.

---

## 🚀 CODE HOÀN CHỈNH – Ứng Dụng Quản Lý Thư Viện

> 📄 Lưu thành file **`quan_ly_thu_vien.py`** rồi chạy `python quan_ly_thu_vien.py`. Chương trình chỉ dùng thư viện chuẩn `sqlite3` — **không cần cài đặt gì thêm**.
>
> 💾 Khi chạy lần đầu, file **`thu_vien.db` được tạo tự động tại thư mục đang chạy** chương trình.

```python
# quan_ly_thu_vien.py
"""
Dự án cuối khóa: Ứng dụng Quản lý Thư viện (Library Manager).

Tổng hợp toàn bộ khóa học: OOP + SQLite + xử lý lỗi + typing.
Chương trình dùng thư viện chuẩn sqlite3 — không cần cài thêm gì.

Lưu ý: file dữ liệu 'thu_vien.db' sẽ được tạo tự động ngay tại
thư mục đang chạy chương trình khi mở kết nối lần đầu.
"""

import sqlite3
from typing import Dict, List, Optional

# Hằng số: đổi tên file DB ở đúng một chỗ này
TEN_FILE_DB = "thu_vien.db"


class Sach:
    """Một đầu sách trong thư viện."""

    def __init__(self, ten: str, tac_gia: str, nam: int, so_luong: int = 1,
                 dang_muon: int = 0, ma: Optional[int] = None) -> None:
        self.ma = ma
        self.ten = ten
        self.tac_gia = tac_gia
        self.nam = nam
        self.so_luong = so_luong
        self.dang_muon = dang_muon

    @property
    def con_lai(self) -> int:
        """Số cuốn còn lại chưa được mượn."""
        return self.so_luong - self.dang_muon

    def __str__(self) -> str:
        """Chuỗi mô tả ngắn gọn, tiện in để kiểm tra."""
        trang_thai = "con" if self.con_lai > 0 else "het"
        return (f"[{self.ma}] {self.ten} - {self.tac_gia} ({self.nam}) | "
                f"con {self.con_lai}/{self.so_luong} cuon [{trang_thai}]")


class ThuVien:
    """Quản lý mọi thao tác với cơ sở dữ liệu SQLite."""

    # Danh sách cột được phép sửa — chống SQL Injection vào tên cột
    COT_HOP_LE = ("ten", "tac_gia", "nam", "so_luong")

    def __init__(self, duong_dan_db: str = TEN_FILE_DB) -> None:
        """Mở kết nối, bật đọc theo tên cột và tạo bảng nếu chưa có."""
        self.duong_dan_db = duong_dan_db
        # row_factory: mỗi dòng trả về truy cập được theo tên cột (dong["ten"])
        self.ket_noi = sqlite3.connect(duong_dan_db)
        self.ket_noi.row_factory = sqlite3.Row
        self.tao_bang()

    def tao_bang(self) -> None:
        """Tạo bảng Sach nếu chưa tồn tại (chạy mỗi lần mở ứng dụng)."""
        with self.ket_noi:  # context manager: tự COMMIT khi thành công
            self.ket_noi.execute(
                """CREATE TABLE IF NOT EXISTS Sach (
                       id         INTEGER PRIMARY KEY AUTOINCREMENT,
                       ten        TEXT    NOT NULL,
                       tac_gia    TEXT    NOT NULL,
                       nam        INTEGER,
                       so_luong   INTEGER NOT NULL,
                       dang_muon  INTEGER NOT NULL DEFAULT 0
                   )"""
            )

    def them_sach(self, sach: Sach) -> int:
        """Thêm đầu sách mới; trả về mã sách vừa tạo."""
        with self.ket_noi:
            con_tro = self.ket_noi.execute(
                "INSERT INTO Sach (ten, tac_gia, nam, so_luong, dang_muon) "
                "VALUES (?, ?, ?, ?, ?)",
                (sach.ten, sach.tac_gia, sach.nam, sach.so_luong, sach.dang_muon),
            )
        return con_tro.lastrowid

    def xem_danh_sach(self) -> List[Dict[str, object]]:
        """Trả về danh sách toàn bộ đầu sách, sắp theo mã."""
        con_tro = self.ket_noi.execute("SELECT * FROM Sach ORDER BY id")
        return [dict(dong) for dong in con_tro.fetchall()]

    def tim_theo_ten(self, ten_can_tim: str) -> List[Dict[str, object]]:
        """Tìm đầu sách có tên chứa chuỗi cho trước."""
        con_tro = self.ket_noi.execute(
            "SELECT * FROM Sach WHERE ten LIKE ? ORDER BY id",
            (f"%{ten_can_tim.strip()}%",),
        )
        return [dict(dong) for dong in con_tro.fetchall()]

    def tim_theo_tac_gia(self, tac_gia_can_tim: str) -> List[Dict[str, object]]:
        """Tìm đầu sách theo tác giả."""
        con_tro = self.ket_noi.execute(
            "SELECT * FROM Sach WHERE tac_gia LIKE ? ORDER BY id",
            (f"%{tac_gia_can_tim.strip()}%",),
        )
        return [dict(dong) for dong in con_tro.fetchall()]

    def _lay_sach(self, ma: int) -> Optional[Dict[str, object]]:
        """Lấy một dòng sách theo mã; trả về None nếu không có."""
        con_tro = self.ket_noi.execute("SELECT * FROM Sach WHERE id = ?", (ma,))
        dong = con_tro.fetchone()
        return dict(dong) if dong else None

    def sua_sach(self, ma: int, cot: str, gia_tri: object) -> bool:
        """Sửa một cột hợp lệ của đầu sách; trả về True nếu sửa được."""
        if cot not in ThuVien.COT_HOP_LE:
            raise ValueError(f"Khong ho tro sua cot: {cot}")
        if self._lay_sach(ma) is None:
            return False
        with self.ket_noi:
            self.ket_noi.execute(
                f"UPDATE Sach SET {cot} = ? WHERE id = ?", (gia_tri, ma)
            )
        return True

    def xoa_sach(self, ma: int) -> bool:
        """Xóa đầu sách theo mã; trả về True nếu xóa được."""
        if self._lay_sach(ma) is None:
            return False
        with self.ket_noi:
            self.ket_noi.execute("DELETE FROM Sach WHERE id = ?", (ma,))
        return True

    def muon_sach(self, ma: int) -> bool:
        """Mượn một cuốn; từ chối nếu sách không còn."""
        dong = self._lay_sach(ma)
        if dong is None:
            return False                                    # không có sách
        if dong["dang_muon"] >= dong["so_luong"]:
            raise ValueError("Sach nay da duoc muon het")   # hết sách
        with self.ket_noi:
            self.ket_noi.execute(
                "UPDATE Sach SET dang_muon = dang_muon + 1 WHERE id = ?", (ma,)
            )
        return True

    def tra_sach(self, ma: int) -> bool:
        """Trả một cuốn; từ chối nếu không có cuốn nào đang mượn."""
        dong = self._lay_sach(ma)
        if dong is None:
            return False
        if dong["dang_muon"] <= 0:
            raise ValueError("Khong co cuon nao dang muon de tra")
        with self.ket_noi:
            self.ket_noi.execute(
                "UPDATE Sach SET dang_muon = dang_muon - 1 WHERE id = ?", (ma,)
            )
        return True

    def thong_ke(self) -> Dict[str, object]:
        """Tổng hợp: đầu sách, tổng cuốn, đang mượn, còn lại."""
        con_tro = self.ket_noi.execute(
            """SELECT COUNT(*) AS so_dau,
                      COALESCE(SUM(so_luong), 0)  AS tong_cuon,
                      COALESCE(SUM(dang_muon), 0) AS dang_muon
               FROM Sach"""
        )
        dong = dict(con_tro.fetchone())
        dong["con_lai"] = dong["tong_cuon"] - dong["dang_muon"]
        return dong

    def dong_ket_noi(self) -> None:
        """Đóng kết nối trước khi thoát chương trình."""
        self.ket_noi.close()


class App:
    """Giao diện menu điều khiển toàn bộ chương trình."""

    def __init__(self) -> None:
        self.thu_vien = ThuVien(TEN_FILE_DB)

    def in_menu(self) -> None:
        """In bảng menu cho người dùng."""
        print("\n===== QUAN LY THU VIEN =====")
        print("1. Them sach")
        print("2. Xem danh sach")
        print("3. Tim theo ten")
        print("4. Tim theo tac gia")
        print("5. Muon sach")
        print("6. Tra sach")
        print("7. Sua sach")
        print("8. Xoa sach")
        print("9. Thong ke")
        print("0. Thoat")

    def in_bang_sach(self, danh_sach: List[Dict[str, object]]) -> None:
        """In danh sách sách dạng bảng thẳng hàng."""
        if not danh_sach:
            print("Khong co sach nao.")
            return
        tieu_de = f"{'Ma':<4}{'Ten':<28}{'Tac gia':<18}{'Nam':<6}{'SL':<4}{'Dang muon':<10}"
        print(tieu_de)
        print("-" * len(tieu_de))
        for s in danh_sach:
            print(f"{s['id']:<4}{s['ten']:<28}{s['tac_gia']:<18}"
                  f"{s['nam']:<6}{s['so_luong']:<4}{s['dang_muon']:<10}")

    def nhap_so_nguyen(self, loi_nhan: str) -> int:
        """Nhập số nguyên; lặp lại đến khi người dùng gõ đúng."""
        while True:
            try:
                return int(input(loi_nhan))      # Nhập: 1941
            except ValueError:
                print("Vui long nhap mot so nguyen hop le.")

    def nhap_sach_moi(self) -> Sach:
        """Hỏi thông tin rồi tạo đối tượng Sach mới (dữ liệu hợp lệ bắt buộc)."""
        ten = input("Ten sach: ").strip()
        while not ten:                            # Nhập: (Enter) -> hỏi lại
            ten = input("Ten sach khong duoc rong, nhap lai: ").strip()
        tac_gia = input("Tac gia: ").strip()
        while not tac_gia:
            tac_gia = input("Tac gia khong duoc rong, nhap lai: ").strip()
        nam = self.nhap_so_nguyen("Nam xuat ban: ")     # Nhập: 1941
        so_luong = self.nhap_so_nguyen("So luong: ")    # Nhập: 3
        while so_luong < 0:
            so_luong = self.nhap_so_nguyen("So luong phai >= 0, nhap lai: ")
        return Sach(ten, tac_gia, nam, so_luong)

    def xu_ly_muon_tra(self, ma: int, loai: str) -> None:
        """Mượn hoặc trả sách; bắt mọi lỗi để chương trình không gãy."""
        try:
            if loai == "muon":
                ok = self.thu_vien.muon_sach(ma)
            else:
                ok = self.thu_vien.tra_sach(ma)
            if ok:
                print("Thanh cong.")
            else:
                print("Khong tim thay sach co ma", ma)
        except ValueError as loi:
            print("Loi:", loi)

    def xu_ly_sua_sach(self) -> None:
        """Hỏi cột cần sửa rồi cập nhật một giá trị."""
        ma = self.nhap_so_nguyen("Ma sach can sua: ")    # Nhập: 1
        if self.thu_vien._lay_sach(ma) is None:
            print("Khong tim thay sach co ma", ma)
            return
        print("Cot hop le: ten, tac_gia, nam, so_luong")
        cot = input("Ten cot can sua: ").strip()          # Nhập: so_luong
        if cot not in ThuVien.COT_HOP_LE:
            print("Cot khong hop le.")
            return
        if cot in ("nam", "so_luong"):
            gia_tri = self.nhap_so_nguyen("Gia tri moi: ")   # Nhập: 5
        else:
            gia_tri = input("Gia tri moi: ").strip()         # Nhập: De Men Moi
        if self.thu_vien.sua_sach(ma, cot, gia_tri):
            print("Da sua sach ma", ma)
        else:
            print("Sua that bai.")

    def xu_ly_thong_ke(self) -> None:
        """In báo cáo thống kê thư viện."""
        tk = self.thu_vien.thong_ke()
        print("\n----- THONG KE THU VIEN -----")
        print(f"So dau sach      : {tk['so_dau']}")
        print(f"Tong so cuon     : {tk['tong_cuon']}")
        print(f"Dang duoc muon   : {tk['dang_muon']}")
        print(f"Con lai tren ke  : {tk['con_lai']}")

    def chay(self) -> None:
        """Vòng lặp menu chính của chương trình."""
        while True:
            self.in_menu()
            chon = input("Chon chuc nang: ").strip()       # Nhập: 1
            if chon == "1":
                sach = self.nhap_sach_moi()
                print("Da them sach ma", self.thu_vien.them_sach(sach))
            elif chon == "2":
                self.in_bang_sach(self.thu_vien.xem_danh_sach())
            elif chon == "3":
                ten = input("Nhap ten can tim: ").strip()  # Nhập: De Men
                self.in_bang_sach(self.thu_vien.tim_theo_ten(ten))
            elif chon == "4":
                tac_gia = input("Nhap tac gia can tim: ").strip()  # Nhập: Hoai
                self.in_bang_sach(self.thu_vien.tim_theo_tac_gia(tac_gia))
            elif chon == "5":
                self.xu_ly_muon_tra(
                    self.nhap_so_nguyen("Ma sach can muon: "), "muon")
            elif chon == "6":
                self.xu_ly_muon_tra(
                    self.nhap_so_nguyen("Ma sach can tra: "), "tra")
            elif chon == "7":
                self.xu_ly_sua_sach()
            elif chon == "8":
                ma = self.nhap_so_nguyen("Ma sach can xoa: ")  # Nhập: 2
                print("Da xoa sach." if self.thu_vien.xoa_sach(ma)
                      else "Khong tim thay sach.")
            elif chon == "9":
                self.xu_ly_thong_ke()
            elif chon == "0":
                print("Tam biet!")
                break
            else:
                print("Lua chon khong hop le.")
        self.thu_vien.dong_ket_noi()


if __name__ == "__main__":
    App().chay()
```

**Hướng dẫn sử dụng nhanh:**

1. Lưu code trên thành `quan_ly_thu_vien.py`.
2. Chạy: `python quan_ly_thu_vien.py`.
3. Thử kịch bản: `1` (thêm "De Men Phieu Luu Ky", "To Hoai", 1941, 3) → `1` (thêm "Nha Gia Kim", "Paulo Coelho", 1988, 1) → `2` (xem) → `5` (mượn sách mã 1) → `9` (thống kê) → `0` (thoát) → chạy lại → `2` (dữ liệu vẫn còn!).

---

## 🏁 Lời kết

Bạn đã đi hết **20 bài tập + 1 dự án hoàn chỉnh** — từ class `Sach` 10 dòng đến chương trình 250 dòng với OOP + SQLite + xử lý lỗi toàn diện. Đây chính là bài tổng hợp cuối cùng của khóa học:

* ✅ Bạn biết **phân tích yêu cầu, thiết kế dữ liệu, thiết kế lớp** trước khi viết code.
* ✅ Bạn viết được **SQL an toàn** (`?` placeholder), tự kiểm thử bằng kịch bản.
* ✅ Bạn đã có **sản phẩm đầu tiên** — hãy thêm một tính năng của riêng mình và khoe với bạn bè!

👉 Ôn lại bài trước: **[Bài 40: Mini Project](../40_Mini_Project/bai_giang.md)** — so sánh để thấy bạn đã tiến bộ xa đến đâu!
