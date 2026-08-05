# 📝 Bài 7: Bài Tập – Nhập và Xuất Dữ Liệu

> 🎯 **Chủ đề:** `print()` với `sep`/`end`, `input()` trả về chuỗi, ép kiểu `int`/`float`/`str`, f-string cơ bản. Tất cả bài đều có nhập liệu từ bàn phím.

---

## 📌 Hướng dẫn làm bài

* Mỗi bài tập cần **tự viết code** rồi chạy thử trước khi xem đáp án.
* Mọi chương trình đều chạy theo luồng: **nhập → xử lý → in kết quả**.
* Đáp án chi tiết 20 bài: 👉 [xem file dap_an.md](dap_an.md)

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Máy chào hỏi

* **Đề bài:** Nhập tên của bạn rồi in ra lời chào `Xin chào <tên>!`
* **Input:** Một dòng là tên.
* **Output:** Dòng chào có chứa tên.
* **Ví dụ:**
  ```
  Bạn tên gì? Mai
  Xin chào Mai!
  ```
* **Gợi ý:** `ten = input("Bạn tên gì? ")` rồi in với f-string.

### Bài 2: Hỏi và in lại câu trả lời

* **Đề bài:** Hỏi người dùng "Bạn thích ăn gì?" rồi in lại câu `Hôm nay bạn sẽ ăn <món> nhé!`
* **Input:** Một dòng là tên món ăn.
* **Output:** Dòng nhắc lại món ăn.
* **Ví dụ:**
  ```
  Bạn thích ăn gì? Phở
  Hôm nay bạn sẽ ăn Phở nhé!
  ```
* **Gợi ý:** Kết quả `input()` lưu vào biến rồi mới dùng.

### Bài 3: Cộng hai số

* **Đề bài:** Nhập hai số nguyên từ bàn phím, in ra tổng của chúng.
* **Input:** Hai dòng, mỗi dòng một số nguyên.
* **Output:** `Tổng của <a> và <b> là <tổng>`
* **Ví dụ:**
  ```
  Nhập số thứ nhất: 7
  Nhập số thứ hai: 5
  Tổng của 7 và 5 là 12
  ```
* **Gợi ý:** Quên ép kiểu `int()` thì `"7" + "5"` sẽ thành `"75"` — nhớ ép kiểu ngay khi nhập.

### Bài 4: In liền một dòng với `end`

* **Đề bài:** Nhập một chuỗi bất kỳ rồi in nó 3 lần **trên cùng một dòng**, cách nhau một dấu cách, dùng tham số `end`.
* **Input:** Một dòng là chuỗi (ví dụ `hoc`).
* **Output:** Chuỗi đó lặp lại 3 lần trên một dòng.
* **Ví dụ:**
  ```
  Nhập từ cần lặp: hoc
  hoc hoc hoc
  ```
* **Gợi ý:** `print(tu, end=" ")` hai lần rồi lần cuối in bình thường để xuống dòng.

### Bài 5: Ngăn cách bằng `sep`

* **Đề bài:** Nhập tên, lớp và trường rồi in cả ba trên một dòng, ngăn cách bởi dấu ` - `.
* **Input:** Ba dòng dữ liệu.
* **Output:** Một dòng có dạng `Tên - Lớp - Trường`.
* **Ví dụ:**
  ```
  Nhập tên: Mai
  Nhập lớp: 10A1
  Nhập trường: THPT Python
  Mai - 10A1 - THPT Python
  ```
* **Gợi ý:** `print(ten, lop, truong, sep=" - ")`.

### Bài 6: Diện tích hình chữ nhật

* **Đề bài:** Nhập chiều dài và chiều rộng (số thực), in ra diện tích hình chữ nhật.
* **Input:** Hai dòng số thực.
* **Output:** `Diện tích hình chữ nhật là: <kết quả>`
* **Ví dụ:**
  ```
  Nhập chiều dài: 5
  Nhập chiều rộng: 10
  Diện tích hình chữ nhật là: 50.0
  ```
* **Gợi ý:** Diện tích = dài × rộng; chiều dài có thể là số thập phân nên dùng `float`.

### Bài 7: Trung bình cộng ba số

* **Đề bài:** Nhập ba số thực, in ra trung bình cộng của chúng.
* **Input:** Ba dòng số thực.
* **Output:** `Trung bình cộng của a, b, c: <kết quả>`
* **Ví dụ:**
  ```
  Nhập số a: 4
  Nhập số b: 5
  Nhập số c: 7
  Trung bình cộng của a, b, c: 5.333333333333333
  ```
* **Gợi ý:** Trung bình = (a + b + c) / 3 — nhớ ngoặc bao tử số.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Tính tuổi

* **Đề bài:** Nhập năm sinh (số nguyên), tính và in tuổi tính đến năm 2026.
* **Input:** Một dòng là năm sinh.
* **Output:** `Bạn <tuổi> tuổi.`
* **Ví dụ:**
  ```
  Bạn sinh năm bao nhiêu? 2010
  Bạn 16 tuổi.
  ```
* **Gợi ý:** `tuoi = 2026 - nam_sinh`; năm sinh phải ép `int`.

### Bài 9: Chu vi và diện tích hình tròn

* **Đề bài:** Nhập bán kính (số thực), in chu vi và diện tích hình tròn với `pi = 3.14`, làm tròn 2 chữ số thập phân.
* **Input:** Một dòng là bán kính.
* **Output:** Hai dòng `Chu vi: <kết quả>` và `Diện tích: <kết quả>` (2 chữ số thập phân).
* **Ví dụ:**
  ```
  Nhập bán kính: 5
  Chu vi: 31.40
  Diện tích: 78.50
  ```
* **Gợi ý:** `chu_vi = 2 * 3.14 * r`, `dien_tich = 3.14 * r * r`; dùng `{:.2f}` trong f-string.

### Bài 10: Đổi tiền VND sang USD

* **Đề bài:** Nhập số tiền VND, đổi sang USD theo tỉ giá `1 USD = 25000 VND`, in kết quả 2 chữ số thập phân.
* **Input:** Một dòng số tiền VND.
* **Output:** `<số VND> VND được đổi thành <số USD> USD`
* **Ví dụ:**
  ```
  Hãy nhập số tiền VND muốn quy đổi thành USD: 2350000
  2350000 VND được đổi thành 94.00 USD
  ```
* **Gợi ý:** `so_usd = so_vnd / 25000`; tiền là số thực, dùng `{:.2f}`.

### Bài 11: Vận tốc trung bình

* **Đề bài:** Nhập quãng đường (km) và thời gian (giờ), tính vận tốc theo công thức `v = s / t` và in kết quả.
* **Input:** Hai dòng số thực (quãng đường, thời gian).
* **Output:** `Vận tốc = <vận tốc> km/h` (1 chữ số thập phân).
* **Ví dụ:**
  ```
  Nhập số km: 120
  Nhập thời gian (h): 2.5
  Vận tốc = 48.0 km/h
  ```
* **Gợi ý:** `v = s / t`; nhớ ép `float` cho cả hai.

### Bài 12: Chương trình tính BMI

* **Đề bài:** Nhập cân nặng (kg) và chiều cao (m), tính BMI theo công thức `BMI = kg / (cao * cao)`, in 2 chữ số thập phân.
* **Input:** Hai dòng số thực (kg, chiều cao).
* **Output:** `BMI của bạn là: <kết quả>`
* **Ví dụ:**
  ```
  Hãy nhập số kg: 80
  Hãy nhập chiều cao (m): 1.6
  BMI của bạn là: 31.25
  ```
* **Gợi ý:** Chiều cao là số thực → `float`; đừng quên ngoặc quanh `cao * cao`.

### Bài 13: Đổi độ C sang độ F

* **Đề bài:** Nhập nhiệt độ theo độ C, đổi sang độ F theo công thức `F = C * 9 / 5 + 32`, in kết quả 1 chữ số thập phân.
* **Input:** Một dòng nhiệt độ C (số thực).
* **Output:** `C độ C = <kết quả> độ F`
* **Ví dụ:**
  ```
  Nhập nhiệt độ (°C): 20.5
  20.5 độ C = 68.9 độ F
  ```
* **Gợi ý:** Lưu cả giá trị gốc vào biến để in lại trong f-string; dùng `{:.1f}`.

### Bài 14: Giới thiệu bản thân bằng f-string

* **Đề bài:** Nhập tên, tuổi, lớp học. In một câu giới thiệu duy nhất: `Tôi tên là <tên>, <tuổi> tuổi, học lớp <lớp>.`
* **Input:** Ba dòng: tên, tuổi, lớp.
* **Output:** Một dòng giới thiệu như trên.
* **Ví dụ:**
  ```
  Nhập tên: An
  Nhập tuổi: 15
  Nhập lớp: 10A1
  Tôi tên là An, 15 tuổi, học lớp 10A1.
  ```
* **Gợi ý:** Tuổi nên ép `int` (và in lại số 15, không có dấu nháy); dùng một câu f-string.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Đổi giây ra giờ:phút:giây

* **Đề bài:** Nhập một số giây (số nguyên), đổi ra giờ, phút, giây. Biết `1 giờ = 3600 giây`, `1 phút = 60 giây`.
* **Input:** Một dòng số nguyên.
* **Output:** `<giờ> giờ <phút> phút <giây> giây`
* **Ví dụ:**
  ```
  Nhập số giây: 3725
  1 giờ 2 phút 5 giây
  ```
* **Gợi ý:** `gio = s // 3600`; `phut = (s % 3600) // 60`; `giay = s % 60` — kết hợp `//` và `%` từ bài 6.

### Bài 16: Hóa đơn quán cà phê

* **Đề bài:** Nhập giá một ly cà phê và số ly. Nếu tổng từ 100.000đ trở lên thì giảm 10%. In tiền phải trả 2 chữ số thập phân. *(Chưa học `if` — hãy tận dụng kỹ thuật `int(điều kiện)` ở bài 6.)*
* **Input:** Hai dòng: giá ly (số thực), số ly (số nguyên).
* **Output:** `Tổng tiền: <tổng>` và `Tiền phải trả: <kết quả>` (2 chữ số thập phân).
* **Ví dụ:**
  ```
  Nhập giá một ly: 35000
  Nhập số ly: 3
  Tổng tiền: 105000.00
  Tiền phải trả: 94500.00
  ```
* **Gợi ý:** `tong = gia * so_ly`; `khuyen_mai = tong >= 100000`; `tien = tong - tong * 0.1 * int(khuyen_mai)`.

### Bài 17: Tiền lãi tiết kiệm một năm

* **Đề bài:** Nhập số tiền gửi (số thực). Với lãi suất `6.5%/năm`, tính số tiền lãi sau 1 năm và tổng tiền (gốc + lãi). In cả hai, 2 chữ số thập phân.
* **Input:** Một dòng số tiền gửi.
* **Output:** Hai dòng `Tiền lãi: <kết quả>` và `Tổng tiền nhận được: <kết quả>`
* **Ví dụ:**
  ```
  Nhập số tiền gửi: 10000000
  Tiền lãi: 650000.00
  Tổng tiền nhận được: 10650000.00
  ```
* **Gợi ý:** `lai = tien * 0.065`; tổng = gốc + lãi; nhớ `{:.2f}`.

### Bài 18: Điểm trung bình có trọng số

* **Đề bài:** Nhập điểm Toán, Văn, Anh (thang 10, số thực). Điểm trung bình = `(Toán * 2 + Văn * 1 + Anh * 1) / 4`. In kết quả 2 chữ số thập phân.
* **Input:** Ba dòng điểm từng môn.
* **Output:** `Điểm trung bình: <kết quả>`
* **Ví dụ:**
  ```
  Nhập điểm Toán: 8
  Nhập điểm Văn: 7
  Nhập điểm Anh: 9
  Điểm trung bình: 8.00
  ```
* **Gợi ý:** Điểm có thể là 8.5 nên dùng `float`; ngoặc quanh tổng trước khi chia.

### Bài 19: Chia tiền sau bữa ăn

* **Đề bài:** Nhập tổng hóa đơn (số thực) và số người cùng chia. Mỗi người trả phần bằng nhau (làm tròn 2 chữ số thập phân), in kết quả.
* **Input:** Hai dòng: tổng hóa đơn, số người (số nguyên).
* **Output:** `Mỗi người phải trả: <kết quả> VND`
* **Ví dụ:**
  ```
  Nhập tổng hóa đơn: 850000
  Nhập số người: 4
  Mỗi người phải trả: 212500.00 VND
  ```
* **Gợi ý:** `moi_nguoi = tong / so_nguoi`; số người dùng `int`, hóa đơn dùng `float`.

### Bài 20: Hồ sơ học sinh hoàn chỉnh

* **Đề bài:** Nhập: họ tên, tuổi, trường, môn học yêu thích. In ra một **hồ sơ 3 dòng** dùng f-string, ngăn cách các thông tin trong mỗi dòng bằng dấu ` | ` (dùng `sep`).
  * Dòng 1: Hồ sơ cá nhân
  * Dòng 2: Tên, tuổi, trường
  * Dòng 3: Môn yêu thích
* **Input:** Bốn dòng dữ liệu (họ tên, tuổi, trường, môn học).
* **Output:** Ba dòng như mô tả.
* **Ví dụ:**
  ```
  Nhập họ tên: Nguyễn Văn An
  Nhập tuổi: 16
  Nhập trường: THPT Python
  Nhập môn yêu thích: Tin học
  ===== HỒ SƠ CÁ NHÂN =====
  Nguyễn Văn An | 16 tuổi | THPT Python
  Môn yêu thích: Tin học
  ```
* **Gợi ý:** Kết hợp f-string (dòng 2) và `print(..., sep=" | ")`; nhớ tuổi ép `int` rồi chèn vào f-string.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Dùng `input()` nhận dữ liệu và luôn nhớ nó trả về chuỗi.
* ✅ Ép kiểu `int`/`float` đúng lúc, đúng chỗ để tính toán chuẩn xác.
* ✅ Làm chủ `print()` với `sep` và `end` để trang trí dòng in.
* ✅ Viết f-string với `{:.2f}` để in tiền, điểm, kết quả đẹp như phần mềm thật.

> 💪 Từ giờ chương trình của bạn đã biết "nghe" người dùng! Hãy chắc chắn mọi bài đều chạy thử với **nhiều giá trị nhập khác nhau**.

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 8: Câu Lệnh If](../08_Cau_lenh_if/bai_giang.md)**
