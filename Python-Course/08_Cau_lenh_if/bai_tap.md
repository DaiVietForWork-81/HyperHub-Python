# 📝 Bài 8: Bài Tập – Câu Lệnh If (Cấu Trúc Rẽ Nhánh)

> 🎯 **Chủ đề:** `if`, `if - else`, `if - elif - else`, if lồng nhau; kiểm tra chẵn lẻ, xếp loại điểm, tiền điện bậc thang, ATM, game đoán số...

---

## 📌 Hướng dẫn làm bài

* Mỗi bài tập cần **tự viết code** rồi chạy thử trước khi xem đáp án.
* Kết hợp kiến thức bài 6 (toán tử, so sánh) và bài 7 (nhập - ép kiểu) với `if` của bài này.
* Đáp án chi tiết 20 bài: 👉 [xem file dap_an.md](dap_an.md)

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Chẵn hay lẻ?

* **Đề bài:** Nhập một số nguyên, in `Chan` nếu số chẵn, ngược lại in `Le`.
* **Input:** Một dòng là số nguyên.
* **Output:** `Chan` hoặc `Le`.
* **Ví dụ:**
  ```
  Nhập một số nguyên: 42
  Chan
  ```
* **Gợi ý:** Số chẵn khi `so % 2 == 0` (chia hết cho 2).

### Bài 2: Số dương hay số âm?

* **Đề bài:** Nhập một số thực, in `So duong` nếu lớn hơn 0, `So am` nếu nhỏ hơn 0, còn lại in `So khong`.
* **Input:** Một dòng số thực.
* **Output:** Một trong ba kết quả trên.
* **Ví dụ:**
  ```
  Nhập một số: -3.5
  So am
  ```
* **Gợi ý:** Số bằng 0 là trường hợp "còn lại" — dùng `else`.

### Bài 3: Kiểm tra tuổi xem phim

* **Đề bài:** Nhập tuổi, in `Duoc xem phim nguoi lon` nếu đủ 18, ngược lại in `Can nguoi lon di kem`.
* **Input:** Một dòng số nguyên.
* **Output:** Một trong hai câu trên.
* **Ví dụ:**
  ```
  Nhập tuổi: 16
  Can nguoi lon di kem
  ```
* **Gợi ý:** Điều kiện `tuoi >= 18`.

### Bài 4: Đậu hay rớt?

* **Đề bài:** Nhập điểm trung bình (thang 10), in `Dau` nếu điểm từ 5 trở lên, ngược lại in `Rot`.
* **Input:** Một dòng điểm (số thực).
* **Output:** `Dau` hoặc `Rot`.
* **Ví dụ:**
  ```
  Nhập điểm: 4.5
  Rot
  ```
* **Gợi ý:** `diem >= 5` — điểm có thể là số thập phân nên dùng `float`.

### Bài 5: Số nào lớn hơn?

* **Đề bài:** Nhập hai số nguyên `a`, `b`. Nếu `a > b` in `a lon hon b`, nếu ngược lại in `b lon hon hoac bang a`.
* **Input:** Hai dòng số nguyên.
* **Output:** Một trong hai kết quả trên.
* **Ví dụ:**
  ```
  Nhập a: 10
  Nhập b: 3
  a lon hon b
  ```
* **Gợi ý:** Chỉ cần một câu `if - else` với `a > b`.

### Bài 6: Số chia hết cho 3?

* **Đề bài:** Nhập một số nguyên, in `Chia het cho 3` nếu số đó chia hết cho 3, ngược lại in `Khong chia het cho 3`.
* **Input:** Một dòng số nguyên.
* **Output:** Một trong hai dòng trên.
* **Ví dụ:**
  ```
  Nhập một số: 15
  Chia het cho 3
  ```
* **Gợi ý:** Chia hết khi `so % 3 == 0`.

### Bài 7: Chào theo buổi

* **Đề bài:** Nhập giờ (số nguyên 0–23). Nếu giờ < 12 in `Chao buoi sang`, ngược lại in `Chao buoi chieu`.
* **Input:** Một dòng số nguyên.
* **Output:** Một trong hai câu chào trên.
* **Ví dụ:**
  ```
  Nhập giờ: 9
  Chao buoi sang
  ```
* **Gợi ý:** Điều kiện `gio < 12`.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Số lớn nhất trong ba số

* **Đề bài:** Nhập ba số thực `a`, `b`, `c`. In ra số lớn nhất (không dùng hàm `max()`).
* **Input:** Ba dòng số thực.
* **Output:** Một dòng là số lớn nhất.
* **Ví dụ:**
  ```
  Nhập a: 5
  Nhập b: 9.5
  Nhập c: 3
  9.5
  ```
* **Gợi ý:** `if a >= b and a >= c` thì `a` lớn nhất; dùng `elif` cho `b`, `c`; hãy suy nghĩ điều kiện nào đến trước.

### Bài 9: Xếp loại điểm 4 mức

* **Đề bài:** Nhập điểm trung bình (thang 10), xếp loại: từ 8 trở lên `Gioi`, từ 6.5 `Kha`, từ 5 `Trung binh`, còn lại `Yeu`.
* **Input:** Một dòng điểm (số thực).
* **Output:** Một trong bốn mức trên.
* **Ví dụ:**
  ```
  Nhập điểm: 7.2
  Kha
  ```
* **Gợi ý:** Xét từ cao xuống thấp: 8 → 6.5 → 5 → else.

### Bài 10: Tiền điện bậc thang

* **Đề bài:** Nhập số kWh tiêu thụ. Giá: 0–50 kWh là 2000đ/kWh; 51–100 kWh là 2500đ/kWh; trên 100 kWh là 3000đ/kWh. In số tiền phải trả.
* **Input:** Một dòng số kWh (số thực).
* **Output:** `So tien phai tra la: <kết quả> VND`
* **Ví dụ:**
  ```
  Nhập số điện tiêu thụ (kWh): 65
  So tien phai tra la: 162500.0 VND
  ```
* **Gợi ý:** Xác định `don_gia` theo bậc rồi mới nhân với kWh.

### Bài 11: Năm nhuận

* **Đề bài:** Nhập một năm (số nguyên). In `Nam nhuan` nếu năm đó nhuận, ngược lại in `Khong phai nam nhuan`. Quy tắc: chia hết cho 4, không chia hết cho 100, **trừ khi** chia hết cho 400.
* **Input:** Một dòng năm.
* **Output:** Một trong hai dòng trên.
* **Ví dụ:**
  ```
  Nhập năm: 2024
  Nam nhuan
  ```
* **Gợi ý:** Điều kiện `nam % 4 == 0 and (nam % 100 != 0 or nam % 400 == 0)` (công thức từ bài 6).

### Bài 12: Máy ATM rút tiền

* **Đề bài:** Số dư khởi tạo `1000000`. Nhập số tiền cần rút. Nếu số tiền ≤ số dư, in `Rut thanh cong. So du con lai: <kết quả> VND`; ngược lại in `So du khong du!`.
* **Input:** Một dòng số tiền rút (số thực).
* **Output:** Một trong hai dòng trên.
* **Ví dụ:**
  ```
  Nhập số tiền muốn rút: 500000
  Rut thanh cong. So du con lai: 500000.0 VND
  ```
* **Gợi ý:** Kiểm tra `so_rut <= so_du` trước; trong nhánh đúng mới trừ `so_du -= so_rut`.

### Bài 13: Phân loại tam giác

* **Đề bài:** Nhập ba cạnh `a`, `b`, `c` (số thực). Nếu cả ba bằng nhau in `Tam giac deu`; nếu có đúng hai cạnh bằng nhau in `Tam giac can`; ngược lại in `Tam giac thuong`.
* **Input:** Ba dòng số thực.
* **Output:** Một trong ba kết quả trên.
* **Ví dụ:**
  ```
  Nhập cạnh a: 5
  Nhập cạnh b: 5
  Nhập cạnh c: 3
  Tam giac can
  ```
* **Gợi ý:** `a == b and b == c` cho tam giác đều; `a == b or b == c or a == c` cho tam giác cân. Xét đều **trước** rồi mới cân.

### Bài 14: Tiền vé tham quan

* **Đề bài:** Nhập tuổi. Vé: dưới 6 tuổi miễn phí (0đ); 6–12 tuổi 20.000đ; 13–17 tuổi 40.000đ; từ 18 tuổi trở lên 60.000đ. In số tiền vé phải trả.
* **Input:** Một dòng tuổi (số nguyên).
* **Output:** `Tien ve: <kết quả> VND`
* **Ví dụ:**
  ```
  Nhập tuổi: 14
  Tien ve: 40000 VND
  ```
* **Gợi ý:** Xét từ trường hợp miễn phí đến đắt dần: `< 6`, `<= 12`, `<= 17`, còn lại 60000.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Xếp loại học lực 5 mức + kiểm tra điểm hợp lệ

* **Đề bài:** Nhập điểm trung bình (thang 10). Xếp loại: 9–10 `Xuat sac`; 8–8.9 `Gioi`; 6.5–7.9 `Kha`; 5–6.4 `Trung binh`; dưới 5 `Yeu`. Nếu điểm nhỏ hơn 0 hoặc lớn hơn 10, in `Diem khong hop le`.
* **Input:** Một dòng điểm (số thực).
* **Output:** Một trong các kết quả trên.
* **Ví dụ:**
  ```
  Nhập điểm trung bình (0 - 10): 8.4
  Gioi
  ```
  ```
  Nhập điểm trung bình (0 - 10): 15
  Diem khong hop le
  ```
* **Gợi ý:** Dùng `if diem < 0 or diem > 10` để chặn điểm rác trước, rồi mới xếp loại trong `else`; nhớ 8.4 phải rơi vào nhánh `>= 8`.

### Bài 16: Máy tính bốn phép tính

* **Đề bài:** Nhập hai số thực `a`, `b` và lựa chọn phép tính (nhập `1` cộng, `2` trừ, `3` nhân, `4` chia). In kết quả. Nếu chọn phép chia mà `b = 0`, in `Khong the chia cho 0`.
* **Input:** Ba dòng: a, b, lựa chọn (số nguyên).
* **Output:** `Ket qua: <kết quả>` hoặc thông báo lỗi chia 0.
* **Ví dụ:**
  ```
  Nhập a: 10
  Nhập b: 3
  Chọn phép tính (1 cộng, 2 trừ, 3 nhân, 4 chia): 4
  Ket qua: 3.3333333333333335
  ```
* **Gợi ý:** Kiểm tra lựa chọn bằng `if - elif - else`; trong nhánh chia, kiểm tra tiếp `b != 0` bằng `if` lồng.

### Bài 17: Số ngày trong tháng

* **Đề bài:** Nhập tháng (1–12) và năm (số nguyên). In số ngày của tháng đó. Tháng 2: 29 ngày nếu năm nhuận, ngược lại 28 ngày. Tháng 4, 6, 9, 11 có 30 ngày. Các tháng còn lại có 31 ngày. Nếu tháng không hợp lệ, in `Thang khong hop le`.
* **Input:** Hai dòng: tháng, năm.
* **Output:** `Thang <tháng>/<năm> có <số ngày> ngày` hoặc báo lỗi.
* **Ví dụ:**
  ```
  Nhập tháng: 2
  Nhập năm: 2024
  Thang 2/2024 có 29 ngày
  ```
* **Gợi ý:** Dùng `if thang == 2` → xét nhuận bằng `if` lồng; tháng 4, 6, 9, 11 tạo một nhóm bằng `or`.

### Bài 18: Tiền nước sinh hoạt (bậc thang + thuế)

* **Đề bài:** Nhập số m³ nước tiêu thụ. Giá: 0–10 m³ là 6000đ/m³; 11–20 m³ là 8000đ/m³; 21–30 m³ là 10000đ/m³; trên 30 m³ là 12000đ/m³. Sau đó cộng thêm thuế VAT 10%. In tổng tiền.
* **Input:** Một dòng số m³ (số thực).
* **Output:** `Tong tien nuoc: <kết quả> VND` (2 chữ số thập phân).
* **Ví dụ:**
  ```
  Nhập số m3 nước tiêu thụ: 25
  Tong tien nuoc: 275000.00 VND
  ```
* **Gợi ý:** Bốn bậc giá; đơn giá = 6000/8000/10000/12000; tiền = m³ × đơn giá; tổng = tiền + tiền × 0.1; dùng `{:.2f}`.

### Bài 19: Điểm trung bình có trọng số + xếp loại

* **Đề bài:** Nhập điểm Toán, Văn, Anh (thang 10). Điểm trung bình = `(Toán*2 + Văn + Anh) / 4`. Xếp loại: `Xuat sac` nếu trung bình ≥ 8.5, `Gioi` nếu ≥ 7, `Kha` nếu ≥ 5.5, `Trung binh` nếu ≥ 4, còn lại `Yeu`. In cả điểm trung bình và xếp loại.
* **Input:** Ba dòng điểm từng môn.
* **Output:** `Diem trung binh: <kết quả>` (2 chữ số) và `Xep loai: <loại>`.
* **Ví dụ:**
  ```
  Nhập điểm Toán: 8
  Nhập điểm Văn: 6
  Nhập điểm Anh: 9
  Diem trung binh: 7.75
  Xep loai: Gioi
  ```
* **Gợi ý:** Tính trung bình trước (bài 7), rồi dùng `if - elif - else` xếp loại từ 8.5 → 7 → 5.5 → 4 → else.

### Bài 20: Trò chơi đoán số bí mật

* **Đề bài:** Chương trình giữ bí mật con số `7`. Nhập một số nguyên dự đoán. Nếu đúng, in `Chuc mung! Ban da doan dung.` Nếu nhập lớn hơn bí mật, in `So ban nhap lon hon dap an. Thu lai nhe!` Nếu nhỏ hơn, in `So ban nhap nho hon dap an. Thu lai nhe!`
* **Input:** Một dòng số nguyên.
* **Output:** Một trong ba câu trên.
* **Ví dụ:**
  ```
  Đoán con số bí mật (1 - 10): 9
  So ban nhap lon hon dap an. Thu lai nhe!
  ```
* **Gợi ý:** Kiểm tra `n == bi_mat` trước; hai trường hợp còn lại là `n > bi_mat` và `n < bi_mat` — suy nghĩ dùng `elif` hay `else`.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Viết thành thạo `if`, `if - else`, `if - elif - else` theo đúng thứ tự ưu tiên.
* ✅ Kiểm soát thụt lề và tránh các lỗi `SyntaxError`, `IndentationError` điển hình.
* ✅ Xây dựng chương trình ra quyết định thực tế: xếp loại, tính tiền, ATM, game đoán số.
* ✅ Kết hợp bài 6 (toán tử) + bài 7 (nhập - ép kiểu) vào các bài toán đời thực.

> 💪 `if` là "bộ não" của mọi chương trình. Càng luyện nhiều tình huống, bạn càng phản xạ nhanh khi đọc yêu cầu: *"Nếu... thì..., ngược lại..."*.

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 9: Match Case](../09_Match_case/bai_giang.md)**