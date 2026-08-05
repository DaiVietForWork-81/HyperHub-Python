# 📝 Bài 20: Bài Tập – Module Trong Python

> 🎯 **Chủ đề:** Import module theo 4 cách, tự tạo module `tien_ich`, dùng `math`, `random`, `datetime`, `os`, và `if __name__ == "__main__"`.

---

## 📌 Hướng dẫn làm bài

* Mỗi bài tập cần **tự viết code** rồi chạy thử trước khi xem đáp án.
* Với bài yêu cầu tạo module, hãy tạo **file `.py` riêng** (ví dụ `tien_ich.py`) đặt cùng thư mục với file chạy chính.
* Đáp án chi tiết 20 bài: 👉 [xem file dap_an.md](dap_an.md)

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Căn bậc hai với math

* **Đề bài:** Dùng module `math`, viết chương trình in ra căn bậc hai của 81.
* **Input:** Không có.
* **Output:**
  ```
  9.0
  ```
* **Gợi ý:** `import math` rồi gọi `math.sqrt(...)`.

### Bài 2: Tung xúc xắc

* **Đề bài:** Dùng module `random`, mô phỏng tung một con xúc xắc 6 mặt và in kết quả ra màn hình.
* **Input:** Không có.
* **Output:** Một số nguyên bất kỳ từ 1 đến 6 (thay đổi mỗi lần chạy), ví dụ:
  ```
  4
  ```
* **Gợi ý:** `random.randint(1, 6)`.

### Bài 3: Bí danh cho math

* **Đề bài:** Dùng `import math as m`, in ra giá trị của `pi` và kết quả `m.ceil(4.2)`.
* **Input:** Không có.
* **Output:**
  ```
  3.141592653589793
  5
  ```
* **Gợi ý:** Sau khi đặt bí danh `m`, gọi `m.pi` và `m.ceil(...)`.

### Bài 4: Chỉ lấy một hàm

* **Đề bài:** Dùng `from random import randint`, sinh và in một số nguyên ngẫu nhiên từ 1 đến 100.
* **Input:** Không có.
* **Output:** Một số nguyên bất kỳ trong khoảng 1 – 100.
* **Gợi ý:** Gọi thẳng `randint(...)` không cần tiền tố `random.`.

### Bài 5: Bốc thăm món ăn

* **Đề bài:** Có danh sách món ăn `["phở", "bún", "cơm", "bánh mì"]`. Dùng `random.choice` bốc thăm ngẫu nhiên một món và in ra.
* **Input:** Không có.
* **Output:** Một trong 4 món trên, ví dụ:
  ```
  phở
  ```
* **Gợi ý:** `random.choice(danh_sach)` chọn ngẫu nhiên một phần tử.

### Bài 6: Module chào hỏi của tôi

* **Đề bài:** Tạo file `chao_hon.py` chứa hàm `xin_chao(ten)` in ra `"Xin chao <ten>!"`. Viết thêm file `main.py` import và gọi hàm với tên `"Mai"`.
* **Input:** Không có.
* **Output:**
  ```
  Xin chao Mai!
  ```
* **Gợi ý:** Đặt hai file cùng thư mục, dùng `from chao_hon import xin_chao`.

### Bài 7: Số thực ngẫu nhiên

* **Đề bài:** Dùng `random.random()` in ra một số thực ngẫu nhiên trong khoảng 0 đến 1, rồi làm tròn 4 chữ số thập phân.
* **Input:** Không có.
* **Output:** Dạng số thực, ví dụ `0.8472`.
* **Gợi ý:** `random.random()` trả về giá trị trong `[0.0, 1.0)`; kết hợp `round(..., 4)`.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Module tiện ích hình tròn

* **Đề bài:** Tạo module `tien_ich.py` chứa hàm `dien_tich_hinh_tron(r)` và `chu_vi_hinh_tron(r)` (lấy `PI = 3.14159`). Tạo `main.py` nhập 2 hàm này, tính và in diện tích + chu vi hình tròn bán kính 5.
* **Input:** Không có.
* **Output:**
  ```
  Dien tich: 78.53975
  Chu vi: 31.4159
  ```
* **Gợi ý:** Module chỉ chứa hằng số và hàm; phần tính toán nằm trong `main.py`.

### Bài 9: Giải phương trình bậc hai

* **Đề bài:** Dùng `math.sqrt`, viết chương trình giải phương trình `x^2 - 5x + 6 = 0` (tính delta rồi in hai nghiệm).
* **Input:** Không có.
* **Output:**
  ```
  Nghiem x1 = 3.0
  Nghiem x2 = 2.0
  ```
* **Gợi ý:** `delta = b*b - 4*a*c`; nghiệm `(-b ± sqrt(delta)) / (2*a)`.

### Bài 10: Sinh 5 số và tìm số lớn nhất

* **Đề bài:** Sinh 5 số nguyên ngẫu nhiên từ 1 đến 99, in cả danh sách và số lớn nhất.
* **Input:** Không có.
* **Output:** (mỗi lần chạy khác nhau)
  ```
  Cac so: [12, 78, 45, 3, 90]
  So lon nhat: 90
  ```
* **Gợi ý:** Dùng vòng lặp `for` để gom vào list, sau đó dùng `max(danh_sach)`.

### Bài 11: Đồng hồ thông minh

* **Đề bài:** Dùng `datetime`, in ra thời điểm hiện tại dạng `HH:MM:SS DD/MM/YYYY`.
* **Input:** Không có.
* **Output:** Dạng ví dụ:
  ```
  14:30:05 05/08/2026
  ```
* **Gợi ý:** `datetime.now()` + `strftime("%H:%M:%S %d/%m/%Y")`.

### Bài 12: Khám phá thư mục

* **Đề bài:** Dùng module `os`, in thư mục hiện tại và đếm xem có bao nhiêu file Python (`.py`) trong đó.
* **Input:** Không có.
* **Output:**
  ```
  Thu muc hien tai: D:\random\Python-Course\20_Module
  So file .py: 2
  ```
* **Gợi ý:** `os.getcwd()` và `os.listdir()` + đếm bằng `if ten.endswith(".py")`.

### Bài 13: Đoán số một lượt

* **Đề bài:** Máy nghĩ số từ 1 đến 10. Người chơi nhập một số (dùng `input`). In `"Dung roi!"` nếu trùng, ngược lại in số bí mật để động viên.
* **Input:** Một số nguyên, ví dụ `7`.
* **Output:**
  ```
  Sai roi! So bi mat la 7
  ```
* **Gợi ý:** `so_bi_mat = random.randint(1, 10)` rồi so sánh với `int(input(...))`.

### Bài 14: Module có chạy thử

* **Đề bài:** Tạo module `tien_ich.py` chứa hàm `tong(*cac_so)` tính tổng nhiều số, kèm khối `if __name__ == "__main__":` để tự chạy thử in ra tổng của `1, 2, 3` khi chạy trực tiếp. Tạo `main.py` import hàm và in tổng của `10, 20, 30`.
* **Input:** Không có.
* **Output khi chạy `tien_ich.py`:** `Tong thu nghiem: 6`
* **Output khi chạy `main.py`:** `Tong: 60`
* **Gợi ý:** `*cac_so` cho phép hàm nhận nhiều đối số; khối `if __name__` chỉ chạy khi chạy trực tiếp.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Bộ tiện ích hình học hoàn chỉnh

* **Đề bài:** Tạo module `hinh_hoc.py` gồm 4 hàm: `dien_tich_hinh_tron(r)`, `chu_vi_hinh_tron(r)`, `dien_tich_tam_giac(a, h)`, `dien_tich_chu_nhat(a, b)`. Tạo `main.py` nhập 2 hàm hình tròn và 2 hàm hình chữ nhật, tính với dữ liệu mẫu và in kết quả đẹp mắt (có nhãn).
* **Input:** Không có.
* **Output:**
  ```
  Hinh tron r=5: Dien tich 78.54, Chu vi 31.42
  Hinh chu nhat 4x6: Dien tich 24
  ```
* **Gợi ý:** Tách rõ phần "định nghĩa" trong module và phần "dùng thử" trong `main.py`.

### Bài 16: Đoán số nhiều lượt

* **Đề bài:** Máy nghĩ số 1–100. Người chơi đoán nhiều lượt; mỗi lượt máy báo `Lon hon` / `Be hon`. Khi đoán đúng, in số lượt đã dùng. Xử lý ngoại lệ khi người chơi nhập không phải số.
* **Input:**
  ```
  50
  abc
  75
  62
  ```
* **Output:**
  ```
  Be hon
  Vui long nhap so nguyen!
  Lon hon
  Dung roi! So bi mat la 62. Ban doan 3 luot.
  ```
* **Gợi ý:** Kết hợp `while`, `try/except ValueError`, `random.randint`.

### Bài 17: Sinh mật khẩu ngẫu nhiên

* **Đề bài:** Dùng `random.choice`, sinh mật khẩu 6 ký tự gồm chữ thường, chữ hoa và chữ số. In ra mật khẩu vừa sinh.
* **Input:** Không có.
* **Output:** Một chuỗi 6 ký tự ngẫu nhiên, ví dụ `kQ7pZ2`.
* **Gợi ý:** Gộp `"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"` thành một chuỗi rồi bốc thăm từng ký tự trong vòng lặp.

### Bài 18: Module thống kê

* **Đề bài:** Tạo module `thong_ke.py` gồm các hàm `tong(ds)`, `trung_binh(ds)`, `lon_nhat(ds)`, `nho_nhat(ds)`. Tạo `main.py` nhập 4 hàm và dùng chúng cho danh sách điểm `[7, 8.5, 6, 9, 7.5]`, in tổng, trung bình (làm tròn 2 chữ số), lớn nhất, nhỏ nhất.
* **Input:** Không có.
* **Output:**
  ```
  Tong: 38.0
  Trung binh: 7.6
  Lon nhat: 9.0
  Nho nhat: 6.0
  ```
* **Gợi ý:** Viết thủ công bằng vòng lặp (không dùng `sum`/`max`/`min` sẵn có) để luyện tay; hoặc dùng hàm sẵn có nếu muốn.

### Bài 19: Module hai vai — chạy thử và bị import

* **Đề bài:** Tạo module `thoi_tiet.py` chứa hàm `mo_ta(t)`: trả về `"Nong"` nếu `t >= 30`, `"Mat"` nếu `t >= 20`, còn lại `"Lanh"`. Kèm khối `if __name__ == "__main__":` in kết quả kiểm thử 3 giá trị `35, 25, 10` khi chạy trực tiếp. Tạo `main.py` import hàm, hỏi người dùng nhiệt độ (dùng `input`) rồi in mô tả.
* **Input (chạy main.py):**
  ```
  32
  ```
* **Output (chạy thời_tiet.py):**
  ```
  Test 35 -> Nong
  Test 25 -> Mat
  Test 10 -> Lanh
  ```
* **Output (chạy main.py):**
  ```
  Thoi tiet hom nay: Nong
  ```
* **Gợi ý:** Kiểm thử nằm trong `if __name__ == "__main__"` để khi import không bị in ra.

### Bài 20: Trò chơi Oẳn tù tì

* **Đề bài:** Viết trò chơi "Búa – Kéo – Bao": máy chọn ngẫu nhiên (`"bua"`, `"keo"`, `"bao"`), người chơi nhập lựa chọn, in kết quả thắng/thua/hòa. Búa thắng Kéo, Kéo thắng Bao, Bao thắng Búa.
* **Input:**
  ```
  bua
  ```
* **Output:** (máy chọn ngẫu nhiên nên mỗi lần khác nhau)
  ```
  May chon: keo
  Ban thang!
  ```
* **Gợi ý:** `random.choice(["bua", "keo", "bao"])`; dùng từ điển để so sánh luật chơi thay vì cả đống `if`.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Thành thạo 4 cách import và biết khi nào nên dùng cách nào.
* ✅ Tự tạo module riêng và tái sử dụng trong nhiều file.
* ✅ Dùng được `math`, `random`, `datetime`, `os` cho việc thực tế.
* ✅ Hiểu `if __name__ == "__main__"` — viết được file vừa chạy vừa import.

> 💪 Chưa tự làm được bài nào thì đừng lo — hãy xem lại bài giảng rồi quay lại. **Lập trình là luyện tập!**

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 21: Package Trong Python](../21_Package/bai_giang.md)**
