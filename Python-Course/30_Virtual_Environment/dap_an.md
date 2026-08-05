# ✅ Bài 30: Đáp Án – Virtual Environment

> 💡 **Hãy tự làm bài tập trước** rồi mới xem đáp án để việc học hiệu quả nhất. Bài này gồm cả lý thuyết lẫn thao tác — đáp án mô tả từng lệnh.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Môi trường ảo là gì?

**Phân tích:** Kiểm tra khái niệm nền tảng.

**Ý tưởng:** Trả lời ngắn với 2-3 ý: thư mục tự chứa, Python riêng, thư viện riêng.

**Đáp án mẫu:**

> Môi trường ảo (virtual environment) là một **thư mục tự chứa** trong dự án, bao gồm một **bản Python riêng** và một **bộ thư viện riêng** (nằm trong `site-packages`). Khi môi trường được kích hoạt, mọi lệnh `python`, `pip` chỉ làm việc với bộ thư viện đó, hoàn toàn tách biệt với Python hệ thống.

---

### Bài 2: Vì sao cần môi trường ảo?

**Phân tích:** Kiểm tra lợi ích bằng liệt kê.

**Đáp án mẫu:**

1. 🔒 **Cách ly:** mỗi dự án có bộ thư viện riêng, dự án này không phá hỏng dự án kia.
2. 🕒 **Phiên bản đúng:** mỗi dự án dùng đúng phiên bản thư viện mình cần (ví dụ `numpy==1.24` vs `numpy==2.1`).
3. 🧹 **Sạch sẽ:** không làm ô nhiễm Python hệ thống bằng hàng tá thư viện lộn xộn.
4. 🤝 **Chia sẻ dễ:** xuất `requirements.txt` để nhóm phát triển dựng lại môi trường y hệt.

---

### Bài 3: Nhận diện lệnh tạo venv

**Đáp án:**

```bash
python -m venv venv
```

Giải thích: `python -m venv` chạy **module `venv`** của Python, đối số `venv` là tên thư mục môi trường.

---

### Bài 4: Lệnh kích hoạt — Windows

**Đáp án:**

* **Command Prompt (cmd):**
  ```
  venv\Scripts\activate.bat
  ```
* **PowerShell:**
  ```
  venv\Scripts\Activate.ps1
  ```

> 💡 Nếu PowerShell báo lỗi execution policy, chạy một lần:
> ```powershell
> Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
> ```

---

### Bài 5: Lệnh kích hoạt — macOS/Linux

**Đáp án:**

```bash
source venv/bin/activate
```

Giải thích: trên macOS/Linux, tập lệnh kích hoạt nằm trong thư mục `bin`. `source` chạy tập lệnh trong đúng shell hiện tại.

---

### Bài 6: Dấu hiệu kích hoạt thành công

**Đáp án mẫu (tuỳ hệ điều hành):**

```
(venv) C:\Users\An\bai_tap_venv>
(venv) an@pc:~/bai_tap_venv$
```

**Cách kiểm chứng:** thấy `(venv)` ở **đầu dòng nhắc** là môi trường ảo đang hoạt động. Muốn chắc chắn, gõ `where python` (Windows) hoặc `which python` (Linux) — đường dẫn có chứa `venv`.

---

### Bài 7: Lệnh tắt môi trường

**Đáp án:**

```bash
deactivate
```

Sau khi gõ, dấu `(venv)` biến mất → đã trở về Python hệ thống. Đóng cửa sổ terminal cũng tự "tắt" venv.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Thực hành trọn quy trình — Windows

**Đáp án (5 lệnh theo đúng thứ tự, chạy trong PowerShell):**

```powershell
mkdir du_an_1
cd du_an_1
python -m venv venv
.\venv\Scripts\Activate.ps1
deactivate
```

**Giải thích:**
* `mkdir du_an_1` — tạo thư mục dự án.
* `cd du_an_1` — đi vào dự án.
* `python -m venv venv` — tạo môi trường ảo tên `venv`.
* `.\venv\Scripts\Activate.ps1` — vào môi trường.
* `deactivate` — thoát môi trường.

---

### Bài 9: Thực hành trọn quy trình — macOS/Linux

**Đáp án:**

```bash
mkdir du_an_1
cd du_an_1
python3 -m venv venv
source venv/bin/activate
deactivate
```

**Giải thích:** trên macOS/Linux thường dùng `python3`; lệnh kích hoạt là `source venv/bin/activate`.

---

### Bài 10: Kiểm tra đường dẫn Python

**Đáp án mẫu (Windows):**

```
where python
C:\Users\An\du_an_1\venv\Scripts\python.exe
```

**Kết luận:** đường dẫn `...\venv\Scripts\python.exe` nằm **trong thư mục venv** → môi trường ảo đang hoạt động đúng. Trên Linux dùng `which python` và trả về `.../venv/bin/python`.

---

### Bài 11: Cài thử thư viện trong venv

**Các lệnh:**

```bash
pip install requests
pip list
```

**Đáp án mẫu (3 dòng đầu `pip list`):**

```
Package            Version
------------------ ---------
certifi            2025.5.15
charset-normalizer 3.4.1
```

* `requests` có trong danh sách → đã cài vào **venv** thành công. Bạn cũng thấy các **package phụ thuộc** (certifi...) mà pip tự cài kèm.

---

### Bài 12: Deactivate rồi kiểm tra lại

**Đáp án mẫu (Windows):**

```bash
deactivate
where python
```

Kết quả lúc này trỏ về Python hệ thống, ví dụ `C:\Users\An\AppData\Local\Programs\Python\Python314\python.exe` — **không** còn `venv` trong đường dẫn.

**Kết luận:** khi tắt môi trường, các lệnh quay về dùng Python hệ thống. Muốn dùng thư viện đã cài trong venv phải kích hoạt lại.

---

### Bài 13: Chọn interpreter trong VS Code

**Các bước:**
1. VS Code → mở thư mục `du_an_1`.
2. `Ctrl + Shift + P` → gõ `Python: Select Interpreter`.
3. Chọn mục có `venv`, dạng:
   ```
   'venv': venv
   ```
   hoặc
   ```
   Python 3.14.2 ('venv': venv)
   ```

**Ghi nhận:** góc dưới trái VS Code hiển thị tên interpreter đang dùng — chọn đúng `venv` thì terminal mới tự kích hoạt môi trường.

---

### Bài 14: `.gitignore` — không commit venv

**Đáp án nội dung file `.gitignore`:**

```gitignore
venv/
__pycache__/
```

**Giải thích:** dòng `venv/` yêu cầu Git bỏ qua toàn bộ thư mục `venv`; `__pycache__/` bỏ qua thư mục bytecode tự sinh khi chạy Python.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Xung đột phiên bản — kịch bản mẫu

**Đáp án mẫu:**

> Một công ty nhỏ có hai dự án. Dự án **A** (ứng dụng toán học) đang chạy ổn định với `numpy==1.24.0`. Dự án **B** (phân tích dữ liệu mới) lại cần `numpy==2.1.0` vì tính năng mới. Nếu cả hai cùng cài "xịn chung" vào Python hệ thống, một trong hai dự án sẽ dùng sai phiên bản: `numpy` 2.1 sẽ báo lỗi hàm mà dự án A đang dùng ở phiên bản 1.24. Không ai thắng trong xung đột này. Giải pháp: tạo **hai môi trường ảo riêng** — dự án A kích hoạt venv A (numpy 1.24), dự án B kích hoạt venv B (numpy 2.1). Cả hai cùng tồn tại song song, không đụng nhau, công ty làm việc thuận lợi.

---

### Bài 16: So sánh global và venv

**Đáp án dạng bảng:**

| Tiêu chí | Python hệ thống | venv |
|---|---|---|
| Thư viện | Chung toàn máy | Riêng cho từng dự án |
| Xung đột phiên bản | Thường xảy ra | Không xảy ra |
| Cần kích hoạt | Không | Có |
| Ô nhiễm cài đặt | Có (tích nhiều thư viện không dùng) | Không |
| Chia sẻ đồng đội | Khó tái tạo | Dễ (qua requirements.txt) |
| Mức độ chuyên nghiệp | Dùng cho việc khởi sự/thử nghiệm | Chuẩn cho mọi dự án thật |

---

### Bài 17: Script tạo môi trường tự động (`tao_moi_truong.bat`)

**Đáp án nội dung file:**

```bat
@echo off
python -m venv venv
venv\Scripts\activate
pip install requests
python -c "print('OK')"
```

**Giải thích:**
* `@echo off` — tắt in lệnh thừa.
* `python -m venv venv` — tạo môi trường.
* `venv\Scripts\activate` — kích hoạt.
* `pip install requests` — cài thư viện.
* `python -c "print('OK')"` — kiểm tra, in `OK`.

> 💡 Phiên bản cho Linux/macOS: file `tao_moi_truong.sh` với `python3 -m venv venv` và `source venv/bin/activate`, kèm `chmod +x` để chạy.

---

### Bài 18: Khôi phục môi trường từ danh sách

**Các lệnh:**

```bash
pip freeze > requirements.txt
```

**Đáp án mẫu (5 dòng đầu file `requirements.txt`):**

```
certifi==2025.1.15
charset-normalizer==3.4.1
idna==3.10
requests==2.32.3
urllib3==2.3.0
```

**Giải một dòng:** `requests==2.32.3` — tên thư viện `requests`, phiên bản chính xác `2.32.3`. File này cho người khác biết **cài gì, phiên bản nào** để khôi phục môi trường bằng `pip install -r requirements.txt` (bài 31).

---

### Bài 19: Bảo trì venv — gỡ thư viện

**Các lệnh:**

```bash
pip uninstall requests -y
pip show requests
```

**Đáp án:** sau khi gỡ, `pip show requests` in thông báo lỗi dạng:

```
WARNING: No metadata found for requests. ...
```

hoặc:

```
pip show requests
```

→ **không tìm thấy package**. Giải thích: thư viện đã được gỡ khỏi venv nên `pip show` không còn thông tin; thư mục `requests` cũng không còn trong `site-packages`.

---

### Bài 20: Phiếu kiểm tra môi trường

**Đáp án file `kiem_tra_moi_truong.md`:**

```markdown
# ✅ Phiếu kiểm tra trước khi chạy dự án Python

1. Đã ở đúng thư mục dự án chưa? (`pwd` / `cd`)
2. Đã kích hoạt venv chưa? (thấy `(venv)` đầu dòng)
3. `where python`/`which python` có trỏ vào thư mục venv không?
4. Đã cài đủ thư viện theo `requirements.txt` chưa? (`pip install -r requirements.txt`)
5. Không commit thư mục `venv` lên Git (có `.gitignore`) chưa?
```

**Giải thích:** mỗi mục kèm lệnh/con trỏ kiểm tra; tick từng ô giúp tránh lỗi "chạy không được vì thiếu thư viện hoặc sai môi trường".

---

## 📌 Lời khuyên cuối

* Kỹ năng venv được dùng **mỗi ngày** trong công việc lập trình — hãy tập quen quy trình: `python -m venv venv` → kích hoạt → cài thư viện → làm việc → `deactivate`.
* Nếu bị lỗi PowerShell script suppressed, đừng sợ — đó là chính sách hệ thống, `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` giải quyết cho phiên làm việc.
* Mỗi dự án một venv, không nên đi chung — nhớ quy tắc vàng.
* Luôn xoá venv bằng cách xoá thư mục; không ảnh hưởng dự án hay Python.

👉 Tiếp theo: **[Bài 31: Pip](../31_Pip/bai_giang.md)**