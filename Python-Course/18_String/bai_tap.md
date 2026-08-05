# 📝 Bài 18: Bài Tập – Chuỗi (String)

> 🎯 **Chủ đề:** Tạo, nối, lặp, truy cập, cắt chuỗi; phương thức biến đổi; tìm kiếm; kiểm tra; f-string.

---

## 📌 Hướng dẫn làm bài

* Mỗi bài tập cần **tự viết code** rồi chạy thử trước khi xem đáp án.
* Đáp án chi tiết 20 bài: 👉 [xem file dap_an.md](dap_an.md)

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Nối chuỗi chào hỏi

* **Đề bài:** Tạo biến `ten = "An"` và in ra câu `Xin chao An, chuc mot ngay tot lanh!` bằng cách nối chuỗi với `+`.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Xin chao An, chuc mot ngay tot lanh!
  ```
* **Gợi ý:** `"Xin chao " + ten + ", ..."` — nhớ thêm khoảng trắng khi nối.

### Bài 2: In hoa tên mình

* **Đề bài:** Tạo chuỗi `ten = "python"`, in ra chuỗi in hoa và chuỗi in thường của nó.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  PYTHON
  python
  ```
* **Gợi ý:** `ten.upper()` và `ten.lower()`.

### Bài 3: Độ dài chuỗi

* **Đề bài:** Cho chuỗi `thong_bao = "Hom nay troi dep"` — in ra độ dài của chuỗi.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Do dai: 16
  ```
* **Gợi ý:** Hàm `len()` đếm số ký tự (tính cả khoảng trắng).

### Bài 4: Lấy tên riêng từ họ tên

* **Đề bài:** Cho chuỗi `ho_ten = "Nguyen Van An"`. Dùng `split()` để lấy và in ra **tên riêng** (từ cuối cùng).
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Ten rieng: An
  ```
* **Gợi ý:** `ho_ten.split()` cho danh sách từ; tên riêng là phần tử cuối `[-1]`.

### Bài 5: Thay thế chữ

* **Đề bài:** Chuỗi `cau = "Toi thich an pho"` — dùng `replace()` thay `pho` thành `bun` và in kết quả.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Toi thich an bun
  ```
* **Gợi ý:** `cau.replace("pho", "bun")` — nhớ gán kết quả.

### Bài 6: Tìm vị trí chữ

* **Đề bài:** Chuỗi `cau = "Python la ngon ngu tuyen voi"` — in vị trí đầu tiên của từ `ngon` và vị trí của từ `khong` (không có).
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Vi tri 'ngon': 10
  Vi tri 'khong': -1
  ```
* **Gợi ý:** `cau.find("ngon")`; `find` trả về `-1` khi không tìm thấy.

### Bài 7: Xóa khoảng trắng thừa

* **Đề bài:** Chuỗi nhập lộn xộn `s = "   Xin chao Python   "` — dùng `strip()` in ra chuỗi sạch không còn khoảng trắng 2 đầu.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Xin chao Python
  ```
* **Gợi ý:** `s.strip()`.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Đếm số lần xuất hiện

* **Đề bài:** Chuỗi `cau = "Python la ngon ngu tuyen voi"` — đếm số lần ký tự `n` xuất hiện và in kết quả.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  So lan xuat hien cua 'n': 5
  ```
* **Gợi ý:** `cau.count("n")`.

### Bài 9: Kiểm tra đầu và cuối chuỗi

* **Đề bài:** Cho `ten_file = "baitho.docx"` — kiểm tra: file có bắt đầu bằng `bai` không? có kết thúc bằng `.txt` không? In `True`/`False`.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Bat dau bang 'bai': True
  Ket thuc bang '.txt': False
  ```
* **Gợi ý:** `startswith("bai")`, `endswith(".txt")`.

### Bài 10: Kiểm tra chuỗi toàn số

* **Đề bài:** Kiểm tra các chuỗi `"12345"`, `"12a45"`, `"1.5"` có phải toàn chữ số không, in kết quả từng dòng.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  12345: True
  12a45: False
  1.5: False
  ```
* **Gợi ý:** `isdigit()` — chỉ đúng khi **tất cả** ký tự là chữ số.

### Bài 11: Nối danh sách bằng join

* **Đề bài:** Danh sách `lop = ["10A1", "10A2", "10A3"]` — dùng `join` nối thành chuỗi cách nhau dấu `, ` và in ra.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  10A1, 10A2, 10A3
  ```
* **Gợi ý:** `", ".join(lop)`.

### Bài 12: Đếm số từ trong câu

* **Đề bài:** Câu `cau = "Hom nay toi di hoc tieng Anh"` — in ra số từ trong câu.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  So tu: 7
  ```
* **Gợi ý:** `split()` rồi `len()`.

### Bài 13: Kết hợp in hoa – in thường

* **Đề bài:** Cho `s = "ToiDangHocPython"` — in ra: chuỗi in hoa, chuỗi in thường, và kiểm tra xem chuỗi gốc có phải toàn in hoa không.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  TOIDANGHOCPYTHON
  toidanghocpython
  Toan in hoa? False
  ```
* **Gợi ý:** `upper()`, `lower()`, `isupper()`.

### Bài 14: Vẽ viền bằng phép nhân chuỗi

* **Đề bài:** In ra một tấm biển chào mừng gồm dòng viền `*` dài 20, dòng chữ `CHAO MUNG`, và dòng viền thứ hai.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  ********************
  CHAO MUNG
  ********************
  ```
* **Gợi ý:** `"*" * 20`.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Thu nhỏ họ tên

* **Đề bài:** Cho `ho_ten = "nguyen van an"`. Viết chương trình:
  1. Chuẩn hóa thành `Nguyen Van An` (in hoa đầu mỗi từ).
  2. Tạo viết tắt `NVA` (lấy chữ cái đầu mỗi từ, in hoa).
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Chuan hoa: Nguyen Van An
  Viet tat: NVA
  ```
* **Gợi ý:** Dùng `title()` cho việc 1; `split()` + vòng lặp + `upper()` cho việc 2.

### Bài 16: Đếm nguyên âm và phụ âm

* **Đề bài:** Câu `cau = "Python la ngon ngu tuyen voi"`. Đếm số **nguyên âm** (a, e, i, o, u) và số **phụ âm** (kí tự chữ cái còn lại, không tính khoảng trắng) rồi in ra.
* **Input:** (không cần nhập gì)
* **Output:**
  ```
  Nguyen am: 8
  Phu am: 15
  ```
* **Gợi ý:** Vòng lặp qua từng ký tự; kiểm tra `chu in "aeiou"`; dùng `isalpha()` để loại khoảng trắng.

### Bài 17: Kiểm tra mật khẩu mạnh

* **Đề bài:** Nhập một mật khẩu. Kiểm tra và in `Manh` nếu có **đủ 4 điều kiện**: dài ≥ 8 ký tự, có chữ cái, có chữ số, có ký tự đặc biệt (không phải chữ và số). Ngược lại in `Yeu`.
* **Input:**
  ```
  Nhap mat khau: An123@xyz
  ```
* **Output:**
  ```
  Manh
  ```
* **Gợi ý:** Dùng `len()`, vòng lặp với `isalpha()`, `isdigit()`, `isalnum()`; `any()` có thể giúp kiểm tra nhanh.

### Bài 18: Chuẩn hóa họ tên

* **Đề bài:** Nhập họ tên có thể thừa nhiều khoảng trắng, ví dụ `"   nguyen   van   an   "`. In ra họ tên chuẩn: giữa các từ chỉ 1 khoảng trắng, đầu mỗi từ viết hoa.
* **Input:**
  ```
  Nhap ho ten:    nguyen   van   an   
  ```
* **Output:**
  ```
  Nguyen Van An
  ```
* **Gợi ý:** `strip()` + `split()` tự gom khoảng trắng thừa, sau đó `title()` hoặc tự viết hoa.

### Bài 19: Kiểm tra chuỗi đối xứng (Palindrome)

* **Đề bài:** Nhập một chuỗi, kiểm tra xem đọc xuôi và đọc ngược có giống nhau không (bỏ qua hoa/thường và khoảng trắng). In `Palindrome` hoặc `Khong phai palindrome`.
* **Input:**
  ```
  Nhap chuoi: Race car
  ```
* **Output:**
  ```
  Palindrome
  ```
* **Gợi ý:** Xóa khoảng trắng, hạ thường, rồi so sánh với bản đảo ngược `[::-1]`.

### Bài 20: Tạo tên đăng nhập từ họ tên

* **Đề bài:** Nhập họ tên, ví dụ `Nguyen Van An`. Tạo tên đăng nhập theo quy tắc: lấy **chữ cái đầu họ + tên riêng**, tất cả viết thường, thêm số `2026`. In ra tên đăng nhập.
* **Input:**
  ```
  Nhap ho ten: Nguyen Van An
  ```
* **Output:**
  ```
  nvan2026
  ```
* **Gợi ý:** `split()` → họ là phần tử `[0]`, tên riêng là `[-1]`; `lower()` toàn bộ; nối bằng `+`.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Thành thạo tạo, nối, lặp, truy cập và cắt chuỗi.
* ✅ Dùng được các phương thức biến đổi, tìm kiếm, kiểm tra và f-string.
* ✅ Xử lý văn bản thực tế: thu nhỏ tên, đếm từ, kiểm tra mật khẩu, palindrome.

> 💪 Chưa tự làm được bài nào thì đừng lo — xem lại bài giảng rồi quay lại. **Lập trình là luyện tập!**

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 19: Ngoại lệ](../19_Exception/bai_giang.md)**
