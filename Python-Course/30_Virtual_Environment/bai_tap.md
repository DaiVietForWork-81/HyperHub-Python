# 📝 Bài 30: Bài Tập – Virtual Environment

> 🎯 **Chủ đề:** Tạo venv, kích hoạt (Windows/macOS/Linux), deactivate, venv trong VS Code, không commit venv.
> 🖥️ Đây là bài tập **lý thuyết + thao tác thực hành** — hãy mở terminal của bạn lên và làm theo từng bước!

---

## 📌 Hướng dẫn làm bài

* Mỗi bài **lý thuyết**: trả lời bằng chữ vào file `.txt` hoặc vở ghi.
* Mỗi bài **thao tác**: thực hiện trong terminal, chụp màn hình hoặc ghi lại kết quả.
* Có thể kiểm chứng bằng lệnh mình vừa học.
* Đáp án chi tiết 20 bài: 👉 [xem file dap_an.md](dap_an.md)

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Môi trường ảo là gì?

* **Đề bài:** Nêu khái niệm **môi trường ảo (virtual environment)** bằng 2-3 câu ngắn gọn theo cách hiểu của bạn.
* **Input:** Không có
* **Output:** Đoạn văn 2-3 câu.
* **Gợi ý:** Nhắc đến: thư mục tự chứa Python + thư viện riêng cho dự án.

### Bài 2: Vì sao cần môi trường ảo?

* **Đề bài:** Liệt kê ít nhất **3 lợi ích** của việc dùng môi trường ảo cho mỗi dự án.
* **Input:** Không có
* **Output:** Danh sách 3 lợi ích.
* **Gợi ý:** Nghĩ về: cách ly, phiên bản thư viện, sạch hệ thống, chia sẻ dễ.

### Bài 3: Nhận diện lệnh tạo venv

* **Đề bài:** Ghi lại **lệnh đầy đủ** tạo môi trường ảo tên `venv` trong thư mục dự án.
* **Input:** Không có
* **Output:** Một dòng lệnh.
* **Gợi ý:** Bắt đầu bằng `python -m`.

### Bài 4: Lệnh kích hoạt — Windows

* **Đề bài:** Ghi lệnh kích hoạt môi trường ảo `venv` trên **Windows** (dùng Command Prompt) và trên **Windows PowerShell**.
* **Input:** Không có
* **Output:** Hai dòng lệnh.
* **Gợi ý:** Thư mục `Scripts` — một bản `.bat`, một bản `.ps1`.

### Bài 5: Lệnh kích hoạt — macOS/Linux

* **Đề bài:** Ghi lệnh kích hoạt môi trường ảo `venv` trên **macOS/Linux**.
* **Input:** Không có
* **Output:** Một dòng lệnh.
* **Gợi ý:** Bắt đầu bằng `source` và thư mục `bin`.

### Bài 6: Dấu hiệu kích hoạt thành công

* **Đề bài:** Làm thao tác: tạo dự án `bai_tap_venv`, tạo venv, kích hoạt thành công. **Ghi lại dòng nhắc** bạn thấy sau khi kích hoạt (dòng đầu tiên của terminal).
* **Input:** Thao tác thật trên máy.
* **Output:** Dạng `(venv) C:\...>` hoặc `(venv) user@pc:...$`.
* **Gợi ý:** Sau khi kích hoạt, tên môi trường hiện trong ngoặc đơn đầu dòng.

### Bài 7: Lệnh tắt môi trường

* **Đề bài:** Sau khi kích hoạt thành công ở bài 6, ghi lệnh để **tắt** môi trường ảo.
* **Input:** Không có
* **Output:** Một dòng lệnh.
* **Gợi ý:** Chỉ một từ đơn giản, gõ xong thấy dấu `(venv)` biến mất.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Thực hành trọn quy trình — Windows

* **Đề bài:** Trên Windows (PowerShell): tạo thư mục `du_an_1` → tạo venv `venv` → kích hoạt → chạy `python --version` → `deactivate`. Ghi lại **toàn bộ lệnh** bạn đã gõ.
* **Input:** Thao tác thật.
* **Output:** 5 dòng lệnh theo đúng thứ tự.
* **Gợi ý:** Tuần tự: `mkdir`, `cd`, `python -m venv`, `.\venv\Scripts\Activate.ps1`, `deactivate`.

### Bài 9: Thực hành trọn quy trình — macOS/Linux

* **Đề bài:** Nếu bạn dùng macOS/Linux, ghi 5 lệnh tương ứng bài 8. Nếu dùng Windows, hãy **viết ra các lệnh** mà người dùng macOS/Linux cần gõ.
* **Input:** Không có
* **Output:** 5 dòng lệnh.
* **Gợi ý:** Kích hoạt bằng `source venv/bin/activate`; có thể dùng `python3`.

### Bài 10: Kiểm tra đường dẫn Python

* **Đề bài:** Trong venv đang kích hoạt, chạy `where python` (Windows) hoặc `which python` (Linux/macOS). Ghi lại kết quả và **kết luận**: đường dẫn có nằm trong thư mục venv không?
* **Input:** Thao tác thật.
* **Output:** Đường dẫn + câu kết luận.
* **Gợi ý:** `where`/`which` trả về đường dẫn thực thi; trong venv sẽ có chữ `venv` trong đường dẫn.

### Bài 11: Cài thử thư viện trong venv

* **Đề bài:** Trong venv, chạy `pip install requests` (bài 31 sẽ học sâu). Sau đó chạy `pip list` và ghi lại: `requests` có trong danh sách không? **Ghi lại 3 dòng đầu** của `pip list`.
* **Input:** Thao tác thật (cần internet).
* **Output:** Tên thư viện đã cài + 3 dòng đầu pip list.
* **Gợi ý:** `pip list` hiển thị bảng 2 cột: tên và phiên bản.

### Bài 12: Deactivate rồi kiểm tra lại

* **Đề bài:** Sau bài 11, gõ `deactivate`, rồi `where python` lần nữa. So sánh đường dẫn trước và sau — **kết luận gì** về thư mục pip list.
* **Input:** Thao tác thật.
* **Output:** 2 đường dẫn + câu kết luận.
* **Gợi ý:** Sau deactivate, đường dẫn trỏ về Python hệ thống.

### Bài 13: Chọn interpreter trong VS Code

* **Đề bài:** Mở VS Code vào thư mục `du_an_1`, mở Command Palette (`Ctrl+Shift+P`), chọn `Python: Select Interpreter`. Ghi lại: tên interpreter chứa `venv` bạn chọn là gì?
* **Input:** Thao tác thật.
* **Output:** Tên interpreter (dạng `Python 3.x.x ('venv': venv)`).
* **Gợi ý:** Ở góc dưới trái VS Code cũng hiện interpreter đang dùng.

### Bài 14: `.gitignore` — không commit venv

* **Đề bài:** Trong thư mục `du_an_1`, tạo file `.gitignore` với nội dung bỏ qua thư mục `venv`. Ghi lại nội dung file.
* **Input:** Thao tác thật.
* **Output:** Nội dung file `.gitignore` (1-2 dòng).
* **Gợi ý:** Dòng `venv/` đã đủ; có thể thêm `__pycache__/`.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Xung đột phiên bản — viết kịch bản minh họa

* **Đề bài:** Viết một **kịch bản (câu chuyện) 5-7 câu** giải thích vì sao hai dự án A và B cần hai venv riêng, dù cả hai cùng dùng thư viện `numpy`.
* **Input:** Không có
* **Output:** Đoạn văn kịch bản.
* **Gợi ý:** Dùng ví dụ "hai sinh viên một phòng" hoặc "phiên bản numpy 1.24 vs 2.1".

### Bài 16: So sánh global và venv

* **Đề bài:** Lập **bảng so sánh** (4-6 dòng) giữa Python hệ thống và venv theo các tiêu chí: thư viện, xung đột phiên bản, cần kích hoạt, mức chuyên nghiệp.
* **Input:** Không có
* **Output:** Bảng (dùng dấu `|` trong file txt hoặc bảng markdown).
* **Gợi ý:** Tham khảo bảng trong phần "Bảng so sánh" của bài giảng.

### Bài 17: Tạo script tạo venv tự động

* **Đề bài:** Viết file `tao_moi_truong.bat` (Windows) chạy: tạo venv, kích hoạt, cài `requests`, chạy `python -c "print('OK')"`. Ghi nội dung file.
* **Input:** Không có
* **Output:** Nội dung file `.bat` (3-4 dòng).
* **Gợi ý:** Dòng 1: `python -m venv venv`; dòng 2: `venv\Scripts\activate`; dòng 3: `pip install requests`; dòng 4: `python -c "print('OK')"`.

### Bài 18: Khôi phục môi trường từ danh sách

* **Đề bài:** Trong venv của `du_an_1`, chạy `pip freeze > requirements.txt`. Mở file và ghi lại **5 dòng đầu**. Giải thích một dòng bất kỳ.
* **Input:** Thao tác thật (đã cài `requests` ở bài 11).
* **Output:** 5 dòng đầu của `requirements.txt` + lời giải thích.
* **Gợi ý:** Định dạng `ten_thu_vien==phien_ban`.

### Bài 19: Bảo trì venv — gỡ thư viện

* **Đề bài:** Trong venv đang kích hoạt, chạy `pip uninstall requests -y` rồi `pip show requests` để kiểm tra. Ghi lại kết quả của `pip show` (lỗi hay thành công) và giải thích vì sao.
* **Input:** Thao tác thật.
* **Output:** Kết quả pip show + giải thích.
* **Gợi ý:** Sau khi gỡ, `pip show` trả thông báo lỗi "not found" — giải thích rằng thư viện không còn trong venv.

### Bài 20: Tổng kết "phiếu kiểm tra môi trường"

* **Đề bài:** Tạo file `kiem_tra_moi_truong.md` (hoặc `.txt`) gồm checklist 5 mục để kiểm tra trước khi chạy một dự án Python:
  1. Đã ở đúng thư mục dự án chưa?
  2. Đã kích hoạt venv chưa (thấy `(venv)`)?
  3. `where python` có trỏ vào venv không?
  4. Đã cài đủ thư viện theo `requirements.txt` chưa?
  5. Không commit `venv` lên git.
* **Input:** Không có
* **Output:** File checklist 5 mục (ghi lại nội dung).
* **Gợi ý:** Mỗi mục kèm lệnh/kiểm tra tương ứng trong ngoặc.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Giải thích được môi trường ảo là gì và vì sao mỗi dự án cần một venv.
* ✅ Tạo, kích hoạt (Windows + macOS/Linux), tắt và xoá venv thành thạo.
* ✅ Biết chọn interpreter venv trong VS Code.
* ✅ Biết nguyên tắc: **không commit venv**, chỉ commit "hướng dẫn xây môi trường".

> 💪 Chưa tự làm được bài nào thì đừng lo — mở lại bài giảng, thực hành lại từng lệnh trong terminal. **Môi trường ảo là kỹ năng dùng hàng ngày — luyện nhiều sẽ quen!**

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 31: Pip](../31_Pip/bai_giang.md)**