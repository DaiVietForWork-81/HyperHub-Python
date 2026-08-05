# ✅ Bài 36: Đáp Án – SQLite

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án để việc học hiệu quả nhất.
>
> 📌 **Lưu ý chung:** Tất cả đáp án dùng module chuẩn `sqlite3`, lưu file `.db` trong thư mục chạy, chạy được với Python 3.9+. Muốn chạy lại từ đầu, hãy xóa file `.db` cũ.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Tạo cơ sở dữ liệu và bảng học sinh

**Phân tích:** Cần kết nối file `.db` (tự tạo nếu chưa có) và tạo bảng với khóa chính tự tăng.

**Ý tưởng:** Dùng `sqlite3.connect()` + `CREATE TABLE IF NOT EXISTS`.

**Thuật toán:**
1. Mở kết nối `bai_tap_36.db`.
2. Tạo con trỏ `cur`.
3. Chạy lệnh tạo bảng với đầy đủ kiểu dữ liệu cột.
4. Commit và đóng.

**Code:**

```python
import sqlite3

# Mở kết nối — file chưa có sẽ được tự tạo
conn = sqlite3.connect("bai_tap_36.db")
cur = conn.cursor()

# Tạo bảng hoc_sinh
cur.execute("""
    CREATE TABLE IF NOT EXISTS hoc_sinh (
        id  INTEGER PRIMARY KEY AUTOINCREMENT,
        ten TEXT NOT NULL,
        toan REAL,
        van  REAL
    )
""")

# Lưu thay đổi và đóng kết nối
conn.commit()
conn.close()

print("Đã tạo bảng hoc_sinh.")
```

**Giải thích code:**
* `INTEGER PRIMARY KEY AUTOINCREMENT` — cột id tự tăng 1, 2, 3...
* `TEXT NOT NULL` — cột tên bắt buộc có giá trị.
* `REAL` — kiểu số thực cho điểm.
* `IF NOT EXISTS` — nếu chạy lại lần hai, bảng không bị tạo trùng.

**Độ phức tạp:** O(1).

---

### Bài 2: Thêm ba học sinh đầu tiên

**Phân tích:** Bảng đã có; chỉ cần INSERT 3 dòng bằng tham số `?`.

**Ý tưởng:** Mỗi học sinh một câu INSERT, dùng `cur.lastrowid` để biết mã số.

**Thuật toán:**
1. Mở kết nối, con trỏ.
2. INSERT từng học sinh.
3. In mã số tự tăng của từng dòng.
4. Commit rồi đóng.

**Code:**

```python
import sqlite3

conn = sqlite3.connect("bai_tap_36.db")
cur = conn.cursor()

danh_sach = [
    ("Nguyễn Văn An", 8.5, 7.0),
    ("Trần Thị Bình", 9.0, 8.5),
    ("Lê Văn Cường", 6.5, 7.5),
]

for ten, toan, van in danh_sach:
    cur.execute(
        "INSERT INTO hoc_sinh (ten, toan, van) VALUES (?, ?, ?)",
        (ten, toan, van),
    )
    print(f"Đã thêm học sinh {ten} (mã số {cur.lastrowid}).")

conn.commit()
conn.close()
```

**Giải thích code:**
* `danh_sach` — list chứa 3 tuple `(ten, toan, van)`.
* Vòng `for` duyệt từng tuple, `?` nhận từng giá trị — an toàn, gọn gàng.
* `cur.lastrowid` trả về id vừa được cấp cho lần INSERT đó.
* Nếu chạy chương trình **lần 2**, sẽ thấy mã số 4, 5, 6 vì 3 học sinh cũ vẫn còn — đây chính là hành vi đúng của DB (dữ liệu đã được lưu lâu dài).

**Độ phức tạp:** O(n) với n là số học sinh thêm (ở đây n = 3).

---

### Bài 3: Xem toàn bộ danh sách học sinh

**Phân tích:** Đọc toàn bộ bảng và in đúng định dạng.

**Ý tưởng:** `SELECT *` + `fetchall()` + vòng lặp.

**Thuật toán:**
1. Đọc toàn bộ hàng dữ liệu.
2. Duyệt từng dòng và in định dạng.

**Code:**

```python
import sqlite3

conn = sqlite3.connect("bai_tap_36.db")
cur = conn.cursor()

cur.execute("SELECT * FROM hoc_sinh")
rows = cur.fetchall()

for row in rows:
    print(f"Mã {row[0]}: {row[1]} - Toán {row[2]} - Văn {row[3]}")

conn.close()
```

**Giải thích code:**
- `fetchall()` trả về `[(1, 'Nguyễn Văn An', 8.5, 7.0), ...]`.
- Mỗi `row` là một tuple; `row[0]`=id, `row[1]`=tên, `row[2]`=toán, `row[3]`=văn.
- f-string giúp ghép chữ và số dễ đọc.

**Độ phức tạp:** O(n) với n là số dòng.

---

### Bài 4: Lọc học sinh có điểm Văn trên 7.0

**Phân tích:** Câu hỏi cần điều kiện lọc (`WHERE`) trên cột văn.

**Ý tưởng:** `SELECT ten, van ... WHERE van > 7.0`.

**Thuật toán:**
1. Chạy truy vấn có điều kiện.
2. Duyệt và in kết quả.

**Code:**

```python
import sqlite3

conn = sqlite3.connect("bai_tap_36.db")
cur = conn.cursor()

cur.execute("SELECT ten, van FROM hoc_sinh WHERE van > 7.0")
for ten, van in cur.fetchall():
    print(f"{ten} - Van {van}")

conn.close()
```

**Giải thích code:**
- `SELECT ten, van` — chỉ lấy 2 cột cần thiết (không lấy *).
- `WHERE van > 7.0` — bộ lọc tại cơ sở dữ liệu, nhanh hơn lọc trong Python.
- Vòng lặp tuần tự giải nén tuple trực tiếp vào `ten, van`.

**Độ phức tạp:** O(n).

---

### Bài 5: Cập nhật điểm Toán

**Phân tích:** Sửa 1 dòng theo điều kiện id, kiểm tra bằng `rowcount`.

**Ý tưởng:** `UPDATE ... SET ... WHERE id = ?`.

**Thuật toán:**
1. Chạy lệnh UPDATE.
2. In số dòng bị ảnh hưởng.
3. Commit.

**Code:**

```python
import sqlite3

conn = sqlite3.connect("bai_tap_36.db")
cur = conn.cursor()

cur.execute("UPDATE hoc_sinh SET toan = ? WHERE id = ?", (10.0, 1))
print("So dong da sua:", cur.rowcount)

conn.commit()
conn.close()
```

**Giải thích code:**
- `SET toan = ?` — giá trị mới đi qua tham số an toàn.
- `WHERE id = ?` — chỉ nhắm đúng mã số 1.
- `rowcount` = 1 chứng tỏ đã nhắm đúng 1 dòng. Nếu id không tồn tại, `rowcount` = 0.

**Độ phức tạp:** O(log n) nếu SQLite dùng index khóa chính, thực tế O(1).

---

### Bài 6: Xóa một học sinh

**Phân tích:** Xóa theo id rồi xem lại danh sách để kiểm chứng.

**Ý tưởng:** `DELETE ... WHERE id = ?` + in lại bằng bài đã làm.

**Code:**

```python
import sqlite3

conn = sqlite3.connect("bai_tap_36.db")
cur = conn.cursor()

cur.execute("DELETE FROM hoc_sinh WHERE id = ?", (3,))
print("So dong da xoa:", cur.rowcount)
conn.commit()

# In lại danh sách để kiểm tra
cur.execute("SELECT * FROM hoc_sinh")
for row in cur.fetchall():
    print(f"Mã {row[0]}: {row[1]} - Toán {row[2]} - Văn {row[3]}")

conn.close()
```

**Giải thích code:**
- `DELETE` chỉ tác động đúng dòng id = 3 nhờ `WHERE`.
- `rowcount` xác nhận 1 dòng đã bị xóa.
- Bước in lại danh sách chính là cách kiểm tra thủ công ("manual test").

**Độ phức tạp:** O(n) với n là số dòng.

---

### Bài 7: Đếm số lượng học sinh

**Phân tích:** Cần hàm SUM của SQL: `COUNT`.

**Ý tưởng:** `SELECT COUNT(*) FROM hoc_sinh`; kết quả nằm ở `rows[0]`.

**Code:**

```python
import sqlite3

conn = sqlite3.connect("bai_tap_36.db")
cur = conn.cursor()

cur.execute("SELECT COUNT(*) FROM hoc_sinh")
ket_qua = cur.fetchone()
print("Tong so hoc sinh:", ket_qua[0])

conn.close()
```

**Giải thích code:**
- `fetchone()` trả về tuple `(count,)` — truy cập `ket_qua[0]`.
- `COUNT(*)` đếm toàn bộ dòng, xử lý tại DB nên rất nhanh.
- Kết quả sẽ là `2` (sau khi xóa học sinh mã 3 ở bài 6).

**Độ phức tạp:** O(n) nhưng chạy cực nhanh ngay trong SQL.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Tìm học sinh theo đúng tên

**Phân tích:** Tìm đúng chuỗi tên, chỉ cần 1 bản ghi → `fetchone()`.

**Ý tưởng:** `WHERE ten = ?` kết hợp `fetchone()` và xử lý trường hợp `None`.

**Code:**

```python
import sqlite3

conn = sqlite3.connect("bai_tap_36.db")
cur = conn.cursor()

ten_can_tim = "Trần Thị Bình"
cur.execute("SELECT * FROM hoc_sinh WHERE ten = ?", (ten_can_tim,))
row = cur.fetchone()

if row is None:
    print("Khong tim thay.")
else:
    print(f"Tim thay: Mã {row[0]} - {row[1]} - Toán {row[2]} - Văn {row[3]}")

conn.close()
```

**Giải thích code:**
- `ten_can_tim` được đẩy qua tham số `?` — chuẩn chống SQL injection.
- `fetchone()` trả `None` nếu không khớp → kiểm tra trước khi dùng.
- Đây là khuôn mẫu quan trọng: **luôn xử lý trường hợp không tìm thấy**.

**Độ phức tạp:** O(n) , `WHERE` trên cột không index sẽ duyệt toàn bảng.

---

### Bài 9: Tìm học sinh theo từ khóa trong tên

**Phân tích:** Tìm một phần chữ xuất hiện trong tên → dùng `LIKE` với dấu `%`.

**Ý tưởng:** `WHERE ten LIKE ?` với `"%An%"`.

**Code:**

```python
import sqlite3

conn = sqlite3.connect("bai_tap_36.db")
cur = conn.cursor()

tu_khoa = "%An%"
cur.execute("SELECT id, ten FROM hoc_sinh WHERE ten LIKE ?", (tu_khoa,))

for ma, ten in cur.fetchall():
    print(f"Mã {ma}: {ten}")

conn.close()
```

**Giải thích code:**
- `%` trong LIKE là "bao nhiêu ký tự tùy ý": `%An%` = có chữ "An" ở giữa chuỗi.
- Tham số `?` vẫn được dùng — `%` nằm trong **giá trị**, không phải câu SQL.

**Độ phức tạp:** O(n).

---

### Bài 10: Sắp xếp theo điểm Môn giảm dần

**Phân tích:** Cần thứ tự kết quả → `ORDER BY`.

**Ý tưởng:** `ORDER BY toan DESC` để giảm dần.

**Code:**

```python
import sqlite3

conn = sqlite3.connect("bai_tap_36.db")
cur = conn.cursor()

cur.execute("SELECT id, ten, toan FROM hoc_sinh ORDER BY toan DESC")
for id, ten, toan in cur.fetchall():
    print(f"{id}: {ten} - {toan}")

conn.close()
```

**Giải thích code:**
- `DESC` = giảm dần; bỏ qua `DESC` sẽ là `ASC` tăng dần.
- Việc sắp xếp thực hiện tại SQL — nhanh hơn sort trong Python khi dữ liệu lớn.

**Độ phức tạp:** O(n log n).

---

### Bài 11: Trung bình cộng hai môn của từng học sinh

**Phân tích:** Mỗi học sinh tính trung bình hai cột ngay trong Python.

**Ý tưởng:** Lấy toàn bộ, tính `(toan + van) / 2`, làm tròn.

**Code:**

```python
import sqlite3

conn = sqlite3.connect("bai_tap_36.db")
cur = conn.cursor()

cur.execute("SELECT ten, toan, van FROM hoc_sinh")
for ten, toan, van in cur.fetchall():
    diem_tb = (toan + van) / 2
    print(f"{ten} - {round(diem_tb, 2)}")

conn.close()
```

**Giải thích code:**
- `cur.fetchall()` trả các tuple; vòng lặp giải nén ra `ten, toan, van`.
- `(toan + van)` có thể là số thực → trung bình ra `.0` hoặc `.5`, `round(x, 2)` giữ 2 chữ số.
- (Nếu về sau dùng tới, phép tổng hợp `AVG` của SQL cũng làm được tương tự.)

**Độ phức tạp:** O(n).

---

### Bài 12: Điểm trung bình toàn lớp

**Phân tích:** Dùng đúng hàm tổng hợp của SQL `AVG`.

**Ý tưởng:** `SELECT AVG(toan)` → `fetchone()[0]`.

**Code:**

```python
import sqlite3

conn = sqlite3.connect("bai_tap_36.db")
cur = conn.cursor()

cur.execute("SELECT AVG(toan) FROM hoc_sinh")
trung_binh = cur.fetchone()[0]
print("Diem toan trung binh:", round(trung_binh, 2))

conn.close()
```

**Giải thích code:**
- `AVG(toan)` trả điểm trung bình của toàn cột Toán về một giá trị duy nhất.
- `round(..., 2)` làm gọn kết quả kiểu `9.5`.
- Đây là cách truy vấn tổng hợp — không cần kéo toàn bộ dữ liệu về Python.

**Độ phức tạp:** O(n).

---

### Bài 13: Lọc theo khoảng điểm

**Phân tích:** Lấy các dòng thuộc khoảng điểm nhất định.

**Ý tưởng:** Dùng `BETWEEN ? AND ?`.

**Code:**

```python
import sqlite3

conn = sqlite3.connect("bai_tap_36.db")
cur = conn.cursor()

diem_min, diem_max = 7.0, 8.5
cur.execute(
    "SELECT ten, van FROM hoc_sinh WHERE van BETWEEN ? AND ?",
    (diem_min, diem_max),
)
for ten, van in cur.fetchall():
    print(f"{ten} - Van {van}")

conn.close()
```

**Giải thích code:**
- `BETWEEN 7.0 AND 8.5` là bao gồm cả hai đầu mút (≥ và ≤).
- Có thể thay bằng `van >= ? AND van <= ?` — cùng kết quả, dịch ra tương tự.

**Độ phức tạp:** O(n).

---

### Bài 14: Cập nhật nhiều bản ghi cùng lúc

**Phân tích:** Một câu UPDATE tác động nhiều dòng, dùng phép cộng ngay trong SQL.

**Ý tưởng:** Dùng `SET van = van + 1` trong phạm vi `WHERE van < 8`.

**Code:**

```python
import sqlite3

conn = sqlite3.connect("bai_tap_36.db")
cur = conn.cursor()

cur.execute("UPDATE hoc_sinh SET van = van + ? WHERE van < ?", (1.0, 8.0))
print("So dong da sua:", cur.rowcount)
conn.commit()

# In lại để kiểm chứng
cur.execute("SELECT id, ten, van FROM hoc_sinh ORDER BY id")
for id, ten, van in cur.fetchall():
    print(f"Mã {id}: {ten} - Văn {van}")

conn.close()
```

**Giải thích code:**
- `van = van + 1` — tăng mỗi dòng đang trong điều kiện lên 1.0.
- Trong ví dụ này chỉ bạn An có văn 7.0 nên nâng lên 8.0 → `rowcount` = 1.
- Đây là cách cập nhật **hàng loạt** một cách an toàn và nhanh.

**Độ phức tạp:** O(n).

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Bảng sản phẩm với CRUD đầy đủ

**Phân tích:** Ứng dụng CRUD trên thực thể khác — sách sản phẩm, hàm hóa mọi bước.

**Ý tưởng:** tạo DB riêng `cua_hang.db`, viết các hàm thêm/xem/sửa/xóa.

**Thuật toán:**
1. Tạo bảng `san_pham` có cột `gia REAL`.
2. Thêm 4 sản phẩm.
3. In danh sách.
4. Sửa giá sản phẩm mã 2.
5. Xóa sản phẩm có `gia < 10000`.
6. In lại danh sách.

**Code:**

```python
import sqlite3

DB = "cua_hang.db"


def tao_bang():
    """Tạo bảng san_pham nếu chưa có."""
    with sqlite3.connect(DB) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS san_pham (
                id  INTEGER PRIMARY KEY AUTOINCREMENT,
                ten TEXT NOT NULL,
                gia REAL
            )
        """)
        conn.commit()


def them_san_pham(ten, gia):
    """Thêm một sản phẩm."""
    with sqlite3.connect(DB) as conn:
        conn.execute(
            "INSERT INTO san_pham (ten, gia) VALUES (?, ?)", (ten, gia)
        )
        conn.commit()


def hien_thi(tieu_de):
    """In danh sách sản phẩm kèm tiêu đề."""
    print(f"--- {tieu_de} ---")
    with sqlite3.connect(DB) as conn:
        rows = conn.execute("SELECT * FROM san_pham").fetchall()
    for id, ten, gia in rows:
        print(f"{id}: {ten} - {gia}")


def sua_gia(ma, gia_moi):
    """Sửa giá sản phẩm theo mã."""
    with sqlite3.connect(DB) as conn:
        r = conn.execute(
            "UPDATE san_pham SET gia = ? WHERE id = ?", (gia_moi, ma)
        )
        conn.commit()
        print(f"Đã sửa {r.rowcount} sản phẩm.")


def xoa_duoi_gia(nguong):
    """Xóa sản phẩm có giá dưới ngưỡng."""
    with sqlite3.connect(DB) as conn:
        r = conn.execute("DELETE FROM san_pham WHERE gia < ?", (nguong,))
        conn.commit()
        print(f"Đã xóa {r.rowcount} sản phẩm.")


if __name__ == "__main__":
    tao_bang()
    them_san_pham("Sách Python", 120000)
    them_san_pham("Bút bi", 5000)
    them_san_pham("Vở ô ly", 8000)
    them_san_pham("Balo", 250000)
    hien_thi("Sau khi thêm")
    sua_gia(2, 15000)
    xoa_duoi_gia(20000)
    hien_thi("Sau khi sửa và xóa")
```

**Giải thích code:**
- Dùng `conn.execute()` trực tiếp từ connection (vẫn cho phép SQL như cursor, chỉ ngắn gọn hơn — kết quả trả về có `.fetchall()`, `.rowcount`).
- Hàm `hien_thi(tieu)` nhận tên tiêu đề — tái sử dụng cho nhiều lần in.
- `rowcount` giúp màn báo đúng số dòng bị tác động.
- File `cua_hang.db` được tạo trong thư mục chạy.

**Độ phức tạp:** O(n) mỗi thao tác duyệt bảng.

---

### Bài 16: Chương trình menu quản lý học sinh

**Phân tích:** Tách 4 chức năng CRUD thành hàm, menu lặp bằng `while True`.

**Ý tưởng:** Mỗi lựa chọn gọi đúng hàm tương ứng; trường hợp `5` thoát vòng lặp.

**Thuật toán:**
1. Tạo bảng.
2. Vòng lặp in menu và đọc lựa chọn.
3. Rẽ nhánh theo lựa chọn: `1` nhập tên, điểm rồi thêm; `2` in danh sách; `3` chọn mã, môn, điểm mới rồi sửa; `4` nhập mã rồi xóa; `5` thoát vòng lặp.
4. Đóng chương trình.

**Code:**

```python
import sqlite3

DB = "ql_hs.db"


def tao_bang():
    with sqlite3.connect(DB) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS hoc_sinh (
                id  INTEGER PRIMARY KEY AUTOINCREMENT,
                ten TEXT NOT NULL,
                toan REAL,
                van  REAL
            )
        """)
        conn.commit()


def them():
    ten = input("Ten: ")
    toan = float(input("Diem toan: "))
    van = float(input("Diem van: "))
    with sqlite3.connect(DB) as conn:
        cur = conn.execute(
            "INSERT INTO hoc_sinh (ten, toan, van) VALUES (?, ?, ?)",
            (ten, toan, van),
        )
        conn.commit()
        print(f"Da them hoc sinh {ten} (ma {cur.lastrowid}).")


def xem():
    with sqlite3.connect(DB) as conn:
        rows = conn.execute("SELECT * FROM hoc_sinh").fetchall()
    if not rows:
        print("Chưa có học sinh nào.")
        return
    for id, ten, toan, van in rows:
        print(f"Ma {id}: {ten} - Toan {toan} - Van {van}")


def sua():
    ma = int(input("Ma hoc sinh: "))
    mon = input("Mon (toan/van): ")
    diem = float(input("Diem moi: "))
    cot = "toan" if mon == "toan" else "van"
    with sqlite3.connect(DB) as conn:
        r = conn.execute(
            f"UPDATE hoc_sinh SET {cot} = ? WHERE id = ?", (diem, ma)
        )
        conn.commit()
    print("So dong da sua:", r.rowcount)


def xoa():
    ma = int(input("Ma hoc sinh: "))
    with sqlite3.connect(DB) as conn:
        r = conn.execute("DELETE FROM hoc_sinh WHERE id = ?", (ma,))
        conn.commit()
    print("So dong da xoa:", r.rowcount)


def menu():
    """Giao diện menu chạy liên tục."""
    tao_bang()
    while True:
        print("\n===== QUAN LY HOC SINH =====")
        print("1. Them hoc sinh")
        print("2. Xem danh sach")
        print("3. Sua diem")
        print("4. Xoa hoc sinh")
        print("5. Thoat")
        chon = input("Chon: ")
        if chon == "1":
            them()
        elif chon == "2":
            xem()
        elif chon == "3":
            sua()
        elif chon == "4":
            xoa()
        elif chon == "5":
            print("Tam biet!")
            break
        else:
            print("Lua chon khong hop le.")


if __name__ == "__main__":
    menu()
```

**Giải thích code:**
- Mọi truy vấn cố gắng dùng `?`; duy nhất tên cột `cot` được ghép vào câu SQL — an toàn vì `cot` chỉ nhận hai giá trị "toan"/"van" do chính mình đặt, không bao giờ là input trực tiếp.
- `float(input(...))` chuyển dữ liệu nhập sang số.
- Nhánh `else` thông báo chọn sai để người dùng không bối rối khi gõ nhầm.
- Khi chọn `5`, `break` thoát khỏi vòng **while** — chỉ thoát một vòng nên phải dùng tại mức menu.

**Độ phức tạp:** O(1) cho một số thao tác, toàn bộ phụ thuộc vào thao tác đang dùng.

---

### Bài 17: Chứng minh tham số an toàn

**Phân tích:** Thử gõ chuỗi nguy hiểm `x'); DROP TABLE hoc_sinh; --` để chứng minh tham số `?` vô hiệu hóa SQL injection.

**Ý tưởng:** Chèn chuỗi tấn công bằng tham số `?`, sau đó đếm lại số dòng để chứng tỏ bảng còn nguyên vẹn.

**Thuật toán:**
1. Kết nối `bai_tap_36.db` — bảng `hoc_sinh` đã có dữ liệu từ các bài trước.
2. Chèn chuỗi tấn công qua tham số `?`.
3. Đếm số dòng: kết quả = số dòng cũ + 1 chứng tỏ chuỗi chỉ là giá trị, không phá bảng.

**Code:**

```python
import sqlite3

conn = sqlite3.connect("bai_tap_36.db")
cur = conn.cursor()

# Ví dụ nhập: x'); DROP TABLE hoc_sinh; --
chuoi_tan_cong = "x'); DROP TABLE hoc_sinh; --"

# Dùng tham số ? — an toàn tuyệt đối
cur.execute(
    "INSERT INTO hoc_sinh (ten, toan, van) VALUES (?, ?, ?)",
    (chuoi_tan_cong, 0.0, 0.0),
)
conn.commit()

print("Da them hoc sinh co ten la:", chuoi_tan_cong)

# Kiểm tra bảng còn tồn tại và đếm dòng
cur.execute("SELECT COUNT(*) FROM hoc_sinh")  # không lỗi -> bảng còn
print("So dong hien co:", cur.fetchone()[0])

# Dọn dẹp: xóa dòng thử nghiệm để không ảnh hưởng các bài sau
cur.execute("DELETE FROM hoc_sinh WHERE ten = ?", (chuoi_tan_cong,))
conn.commit()
conn.close()
```

**Giải thích code:**
- Nếu nối chuỗi `"... VALUES ('" + ten + "')"`, chuỗi `x'); DROP TABLE hoc_sinh; --` sẽ làm câu lệnh trở thành `INSERT ... VALUES ('x'); DROP TABLE hoc_sinh; --')` — câu lệnh DROP chạy và xóa sạch bảng!
- Với `?`, SQLite coi toàn bộ chuỗi là **giá trị của cột tên** → không bị phân tích thành lệnh.
- `COUNT(*)` vẫn chạy được và bằng số dòng cũ cộng 1 (tức 3) → bằng chứng bảng còn nguyên.
- Cuối chương trình **dọn dẹp dòng thử nghiệm** bằng DELETE — thói quen tốt để dữ liệu thử không "bẩn" bảng cho các bài sau.

**Độ phức tạp:** O(1).

---

### Bài 18: Báo cáo thống kê toàn diện

**Phân tích:** Tổng hợp số liệu lớp qua 4 câu `SELECT`.

**Ý tưởng:** Dùng `COUNT`, `MAX`, `MIN`, `AVG` — mỗi câu trả 1 giá trị.

**Code:**

```python
import sqlite3

conn = sqlite3.connect("bai_tap_36.db")
cur = conn.cursor()

cur.execute("SELECT COUNT(*) FROM hoc_sinh")
so_hs = cur.fetchone()[0]

cur.execute("SELECT MAX(toan) FROM hoc_sinh")
cao_nhat = cur.fetchone()[0]

cur.execute("SELECT MIN(toan) FROM hoc_sinh")
thap_nhat = cur.fetchone()[0]

cur.execute("SELECT AVG(toan) FROM hoc_sinh")
trung_binh = cur.fetchone()[0]

print("So hoc sinh:", so_hs)
print("Toan cao nhat:", cao_nhat)
print("Toan thap nhat:", thap_nhat)
print("Toan trung binh:", round(trung_binh, 2))

conn.close()
```

**Giải thích code:**

- COUNT/MAX/MIN/AVG đều xử lý trong SQL — đỡ tải cho Python khi dữ liệu lớn.
- `fetchone()[0]` mỗi lần chìa về một số duy nhất.

**Độ phức tạp:** O(n) cho mỗi câu truy vấn.

---

### Bài 19: Thêm cột và nhập dữ liệu cũ

**Phân tích:** Bảng cần thêm cột sau khi tạo — dùng `ALTER TABLE`, chú ý chỉ chạy một lần.

**Ý tưởng:** `ALTER TABLE ... ADD COLUMN`, rồi cập nhật email từng mã, cuối cùng in bảng mới.

**Code:**

```python
import sqlite3

conn = sqlite3.connect("bai_tap_36.db")
cur = conn.cursor()

# Bước 1: thêm cột (chạy lần đầu duy nhất; chạy lại sẽ lỗi nên bọc try/except)
try:
    cur.execute("ALTER TABLE hoc_sinh ADD COLUMN email TEXT")
    conn.commit()
    print("Đã thêm cột email.")
except Exception:
    print("Cột email đã tồn tại, tiếp tục.")

# Bước 2: cập nhật email từng học sinh theo mã
for ma, email in [(1, "an.nguyen@gmail.com"), (2, "binh.tran@gmail.com")]:
    cur.execute("UPDATE hoc_sinh SET email = ? WHERE id = ?", (email, ma))
conn.commit()

# Bước 3: in bảng mới
cur.execute("SELECT id, ten, email FROM hoc_sinh ORDER BY id")
for id, ten, email in cur.fetchall():
    print(f"{id} | {ten} | {email}")

conn.close()
```

**Giải thích code:**
- Một số thao tác DDL (`ALTER TABLE`) bên SQLite — chạy lại sẽ báo lỗi "duplicate column", vậy `try/except` là chuẩn mực.
- Cập nhật email từng dòng theo id — mỗi UPDATE nhắm đúng vào id.
- Câu in cuối cùng đóng vai trò kiểm tra dữ liệu vừa chuyển thành.

**Độ phức tạp:** O(n) khi in lại bảng.

---

### Bài 20 — Chương trình quản lý thư viện mini

**Phân tích:** Kết hợp toàn bộ kiến thức: CRUD + điều kiện `so_luong > 0` + logic mượn-trả giảm số.

**Ý tưởng:** Bảng sách; mượn một quyển là giảm count 1 nếu còn; dùng `rowcount` báo trạng thái.

**Thuật toán:**
1. Tạo bảng `sach` (id, ten_sach, tac_gia, nam, so_luong).
2. Menu 5 lựa chọn.
3. Mượn sách: `UPDATE ... SET so_luong = so_luong - 1 WHERE ten_sach = ? AND so_luong > 0`.

**Code:**

```python
import sqlite3

DB = "thu_vien.db"


def tao_bang():
    with sqlite3.connect(DB) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS sach (
                id       INTEGER PRIMARY KEY AUTOINCREMENT,
                ten_sach TEXT NOT NULL,
                tac_gia  TEXT,
                nam      INTEGER,
                so_luong INTEGER DEFAULT 0
            )
        """)
        conn.commit()


def them_sach():
    ten = input("Ten sach: ")
    tac_gia = input("Tac gia: ")
    nam = int(input("Nam: "))
    so_luong = int(input("So luong: "))
    with sqlite3.connect(DB) as conn:
        cur = conn.execute(
            "INSERT INTO sach (ten_sach, tac_gia, nam, so_luong) VALUES (?, ?, ?, ?)",
            (ten, tac_gia, nam, so_luong),
        )
        conn.commit()
        print(f"Da them sach {ten}.")


def xem_sach():
    with sqlite3.connect(DB) as conn:
        rows = conn.execute("SELECT * FROM sach").fetchall()
    if not rows:
        print("Thu vien trong.")
        return
    print("--- DANH SACH SACH ---")
    for id, ten, tac_gia, nam, so in rows:
        print(f"{id}: {ten} - {tac_gia} ({nam}) - con {so} quyen")


def tim_sach():
    tu_khoa = input("Tu khoa ten sach: ")
    with sqlite3.connect(DB) as conn:
        rows = conn.execute(
            "SELECT * FROM sach WHERE ten_sach LIKE ?", (f"%{tu_khoa}%",)
        ).fetchall()
    if not rows:
        print("Khong tim thay sach nao.")
        return
    for id, ten, tac_gia, nam, so in rows:
        print(f"{id}: {ten} - con {so} quyen")


def muon_sach():
    ten = input("Ten sach can muon: ")
    with sqlite3.connect(DB) as conn:
        r = conn.execute(
            "UPDATE sach SET so_luong = so_luong - 1 "
            "WHERE ten_sach = ? AND so_luong > 0",
            (ten,),
        )
        conn.commit()
    if r.rowcount == 1:
        with sqlite3.connect(DB) as conn:
            so = conn.execute(
                "SELECT so_luong FROM sach WHERE ten_sach = ?", (ten,)
            ).fetchone()[0]
        print(f"Da muon thanh cong. Con {so} quyen.")
    else:
        print("Muon that bai: khong co sach hoac het sach.")


def menu():
    tao_bang()
    while True:
        print("===== THU VIEN =====")
        print("1. Them sach")
        print("2. Xem sach")
        print("3. Tim sach")
        print("4. Muon sach")
        print("5. Thoat")
        chon = input("Chon: ")
        if chon == "1":
            them_sach()
        elif chon == "2":
            xem_sach()
        elif chon == "3":
            tim_sach()
        elif chon == "4":
            muon_sach()
        elif chon == "5":
            print("Tam biet!")
            break
        else:
            print("Chua hon le.")


if __name__ == "__main__":
    menu()
```

**Giải thích code:**
- `muon_sach()` dùng câu SQL có điều kiện kèm deadline: `AND so_luong > 0` — nếu hết sách, 0 dòng bị đổi → `rowcount` = 0 → thông báo đúng.
- Sau khi mượn thành công, mọi ô còn lại được đặt lại tạo 1 lần truy vấn mới — hiển thị cho người dùng.
- `DEFAULT 0` khi thiết lập cột cho `so_luong`.

**Độ phức tạp:** O(n) cho tìm kiếm `SQL` lượt.

---

## 📌 Lời khuyên cuối

* Khi thao tác ghi (INSERT/UPDATE/DELETE) **luôn commit()** — nếu quên, chương trình vẫn "thành công" nhưng dữ liệu không lưu.
* Dữ liệu đầu vào bắt buộc qua **`?`** — không ngoại trừ vào trường hợp nào.
* Sau UPDATE/DELETE, nhìn rowcount để xác nhận số hàng đã tác động.
* Muốn "reset" để chạy lại từ đầu, **thả file `.db` cũ** — một trong những lý do file DB nhỏ dễ thao tác này.

📌 Xem tiếp: **[Bài 37: Logging – Bài tập](../37_Logging/bai_tap.md)** | **[Bài 37: Logging – Bài giảng](../37_Logging/bai_giang.md)**