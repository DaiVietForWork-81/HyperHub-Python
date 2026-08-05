# 📝 Bài 9: Bài Tập – Câu Lệnh Match – Case

> 🎯 **Chủ đề:** So khớp nhiều giá trị bằng `match-case`, dấu `|`, `case _`, guard, khớp bộ giá trị.
>
> ⚠️ Tất cả bài tập cần **Python 3.10 trở lên** — kiểm tra bằng `python --version`.

---

## 📌 Hướng dẫn làm bài

* Mỗi bài tập cần **tự viết code** rồi chạy thử trước khi xem đáp án.
* Nhớ dùng `input()` để nhập dữ liệu như bài 7 đã học.
* Đáp án chi tiết 20 bài: 👉 [xem file dap_an.md](dap_an.md)

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Thứ trong tuần

* **Đề bài:** Nhập một số nguyên từ 1 đến 7, in ra thứ tương ứng (1 = Chủ nhật, 2 = Thứ Hai, ..., 7 = Thứ Bảy). Số khác thì in `So khong hop le!`.
* **Input:** Một số nguyên.
* **Output:** Tên thứ trong tuần.
* **Ví dụ:**
  ```
  Nhập số (1-7): 3
  Thứ Ba
  ```
* **Gợi ý:** Dùng `match so:` với 7 case, case cuối là `case _:`.

### Bài 2: Số ngày trong tháng

* **Đề bài:** Nhập một tháng (1–12), in ra số ngày của tháng đó (tháng 2 tính 28 ngày, không xét năm nhuận).
* **Input:** Một số nguyên từ 1 đến 12.
* **Output:** Số ngày của tháng.
* **Ví dụ:**
  ```
  Nhập tháng: 4
  Tháng 4 có 30 ngày
  ```
* **Gợi ý:** Gộp các tháng 30 ngày bằng `case 4 | 6 | 9 | 11:`.

### Bài 3: Điểm chữ

* **Đề bài:** Nhập một chữ cái A, B, C, D hoặc F, in ra nhận xét tương ứng (ví dụ A → `Xuat sac`, B → `Gioi`, C → `Kha`, D → `Trung binh`, F → `Khong dat`).
* **Input:** Một chữ cái (có thể viết thường).
* **Output:** Nhận xét xếp loại.
* **Ví dụ:**
  ```
  Nhập điểm chữ: b
  Gioi
  ```
* **Gợi ý:** Dùng `.upper()` để nhận cả chữ thường lẫn chữ hoa.

### Bài 4: Menu món ăn trưa

* **Đề bài:** Căn tin có menu: `1. Pho`, `2. Bun`, `3. Com`, `4. My xao`. Nhập số 1–4, in tên món đã chọn; nhập khác thì in `Mon khong co trong menu!`.
* **Input:** Số nguyên 1–4.
* **Output:** Tên món ăn.
* **Ví dụ:**
  ```
  Nhập lựa chọn (1-4): 2
  Ban chon: Bun
  ```
* **Gợi ý:** Mỗi case in ra một món.

### Bài 5: Kích cỡ áo

* **Đề bài:** Nhập kích cỡ `S`, `M`, `L`, `XL`, in ra số đo tương ứng: S = 36, M = 38, L = 40, XL = 42. Kích cỡ khác in `Khong co kich co nay`.
* **Input:** Chuỗi kích cỡ (có thể viết thường).
* **Output:** Số đo hoặc thông báo lỗi.
* **Ví dụ:**
  ```
  Nhập kích cỡ: l
  Kich co L - so do 40
  ```
* **Gợi ý:** `case "XL" | "xl":` hoặc chuẩn hóa bằng `.upper()` trước khi match.

### Bài 6: Chào hỏi bằng nhiều ngôn ngữ

* **Đề bài:** Nhập tên ngôn ngữ `viet`, `anh`, `phap`, `nhat`, in ra lời chào tương ứng (Xin chào / Hello / Bonjour / Konnichiwa). Khác → `Chua ho tro ngon ngu nay!`.
* **Input:** Tên ngôn ngữ.
* **Output:** Lời chào.
* **Ví dụ:**
  ```
  Nhập ngôn ngữ (viet/anh/phap/nhat): anh
  Hello!
  ```
* **Gợi ý:** Match trên chuỗi trực tiếp.

### Bài 7: Mùa trong năm

* **Đề bài:** Nhập tháng (1–12), in ra mùa: tháng 12, 1, 2 → Mùa đông; 3, 4, 5 → Mùa xuân; 6, 7, 8 → Mùa hè; 9, 10, 11 → Mùa thu. Khác → `Thang khong hop le!`.
* **Input:** Số nguyên.
* **Output:** Tên mùa.
* **Ví dụ:**
  ```
  Nhập tháng: 6
  Mùa hè
  ```
* **Gợi ý:** Mỗi mùa gộp 3 tháng bằng dấu `|`.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Máy tính hai số

* **Đề bài:** Nhập hai số và một phép toán (`+`, `-`, `*`, `/`), in ra kết quả. Nếu phép toán không hợp lệ → `Phep toan khong hop le!`. Nếu chia cho 0 → `Khong the chia cho 0!`.
* **Input:** Hai số thực và một ký tự phép toán.
* **Output:** Kết quả phép tính.
* **Ví dụ:**
  ```
  Nhập số thứ nhất: 10
  Nhập số thứ hai: 4
  Nhập phép toán (+, -, *, /): /
  10.0 / 4.0 = 2.5
  ```
* **Gợi ý:** Trong `case "/":` dùng `if b == 0` để kiểm tra.

### Bài 9: Xếp loại điểm trung bình

* **Đề bài:** Nhập điểm trung bình (0–10), xếp loại: >= 9 → `Xuat sac`, >= 8 → `Gioi`, >= 6.5 → `Kha`, >= 5 → `Trung binh`, >= 0 → `Yeu`, ngoài khoảng → `Diem khong hop le!`.
* **Input:** Số thực.
* **Output:** Xếp loại.
* **Ví dụ:**
  ```
  Nhập điểm trung bình: 8.2
  Gioi
  ```
* **Gợi ý:** Dùng guard: `case _ if diem >= 9:`.

### Bài 10: Số ngày trong tháng (có năm nhuận)

* **Đề bài:** Nhập tháng và năm, in số ngày. Tháng 2: 29 ngày nếu năm nhuận (chia hết cho 400, hoặc chia hết cho 4 mà không chia hết cho 100), ngược lại 28 ngày.
* **Input:** Tháng (1–12) và năm nguyên dương.
* **Output:** Số ngày của tháng đó.
* **Ví dụ:**
  ```
  Nhập tháng: 2
  Nhập năm: 2024
  Tháng 2 năm 2024 có 29 ngày
  ```
* **Gợi ý:** Trong `case 2:` dùng `if` kiểm tra năm nhuận; các tháng khác như bài 2.

### Bài 11: Đổi ngoại tệ

* **Đề bài:** Nhập mã tiền tệ `USD` (1 USD = 25 000 VND), `EUR` (1 EUR = 27 000 VND), `JPY` (1 JPY = 170 VND) và số tiền ngoại tệ; in ra số VND tương ứng. Mã khác → `Ma tien te khong hop le!`.
* **Input:** Mã tiền tệ và số tiền cần đổi.
* **Output:** Số tiền quy đổi ra VND.
* **Ví dụ:**
  ```
  Nhập mã tiền tệ: usd
  Nhập số tiền: 2
  2 USD = 50000 VND
  ```
* **Gợi ý:** Chuẩn hóa mã bằng `.upper()`; giá trị mỗi case là tỉ giá khác nhau.

### Bài 12: Xếp loại học lực (điểm + hạnh kiểm)

* **Đề bài:** Nhập điểm trung bình (0–10) và hạnh kiểm (`Tot`, `Kha`, `Yeu`). Xếp loại: hạnh kiểm Yếu → `Khen thuong: Khong`; hạnh kiểm Tốt và điểm >= 8 → `Khen thuong: Gioi`; hạnh kiểm Khá và điểm >= 8 → `Khen thuong: Kha`; còn lại → `Khen thuong: Trung binh`.
* **Input:** Điểm (float) và hạnh kiểm (chuỗi).
* **Output:** Mức khen thưởng.
* **Ví dụ:**
  ```
  Nhập điểm: 8.5
  Nhập hạnh kiểm: Tot
  Khen thuong: Gioi
  ```
* **Gợi ý:** `match (diem, hanh_kiem):` với mẫu `(_, "Yeu")` — dấu `_` trong bộ giá trị khớp mọi điểm.

### Bài 13: Vé máy bay

* **Đề bài:** Nhập hạng vé `economy`, `business`, `first` và số lượng vé. Giá: economy 1000, business 3500, first 8000 (ngàn đồng). In tổng tiền; hạng không hợp lệ → `Hang ve khong hop le!`.
* **Input:** Hạng vé (chuỗi) và số lượng (số nguyên).
* **Output:** Tổng tiền.
* **Ví dụ:**
  ```
  Nhập hạng vé: business
  Nhập số lượng vé: 2
  Tổng tiền: 7000 ngàn đồng
  ```
* **Gợi ý:** Gán giá trong từng case rồi in phép nhân; dùng `.lower()`.

### Bài 14: Cung hoàng đạo (theo tháng)

* **Đề bài:** Nhập tháng sinh (1–12), in cung hoàng đạo theo quy tắc đơn giản sau (chỉ theo tháng): tháng 1 → `Bao Binh`, tháng 2 → `Song Ngu`, tháng 3 → `Bach Duong`, tháng 4 → `Kim Nguu`, tháng 5 → `Song Tu`, tháng 6 → `Cu Giai`, tháng 7 → `Su Tu`, tháng 8 → `Xu Nu`, tháng 9 → `Thien Binh`, tháng 10 → `Thien Yet`, tháng 11 → `Nhan Ma`, tháng 12 → `Ma Ket`.
* **Input:** Số nguyên 1–12.
* **Output:** Tên cung hoàng đạo.
* **Ví dụ:**
  ```
  Nhập tháng sinh: 9
  Cung của bạn: Thien Binh
  ```
* **Gợi ý:** 12 case đơn giản, case cuối là `case _:`.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Oẳn tù tì

* **Đề bài:** Người chơi nhập `kéo`, `búa` hoặc `bao`; máy luôn chọn `búa`. In kết quả thắng/thua/hòa theo luật: kéo thắng bao, bao thắng búa, búa thắng kéo; giống nhau thì hòa. Nhập khác → `Nhap khong dung!`.
* **Input:** Chuỗi lựa chọn của người chơi.
* **Output:** Kết quả ván chơi.
* **Ví dụ:**
  ```
  Bạn chọn (kéo/búa/bao): bao
  Máy chọn: búa
  Bạn thắng!
  ```
* **Gợi ý:** `match (nguoi, "búa"):` với 3 cặp thua, 3 cặp thắng, 3 cặp hòa gộp bằng `|`.

### Bài 16: Cung hoàng đạo (theo ngày + tháng)

* **Đề bài:** Nhập ngày và tháng sinh, in đúng cung hoàng đạo theo ranh giới ngày:
  * Bảo Bình (20/1 – 18/2), Song Ngư (19/2 – 20/3), Bạch Dương (21/3 – 19/4), Kim Ngưu (20/4 – 20/5), Song Tử (21/5 – 21/6), Cự Giải (22/6 – 22/7), Sư Tử (23/7 – 22/8), Xử Nữ (23/8 – 22/9), Thiên Bình (23/9 – 22/10), Thiên Yết (23/10 – 21/11), Nhân Mã (22/11 – 21/12), Ma Kết (22/12 – 19/1).
* **Input:** Ngày và tháng sinh (giả định hợp lệ).
* **Output:** Tên cung hoàng đạo.
* **Ví dụ:**
  ```
  Nhập ngày sinh: 15
  Nhập tháng sinh: 8
  Cung của bạn: Su Tu
  ```
* **Gợi ý:** `match (thang, ngay):` — mỗi tháng 1–2 case kèm guard so sánh ngày, ví dụ `case (1, _) if ngay >= 20:`.

### Bài 17: Tiền điện bậc thang

* **Đề bài:** Nhập số kWh tiêu thụ, tính tiền điện theo bậc: 0–50 kWh: 2000đ/kWh; 51–100 kWh: 2500đ/kWh; trên 100 kWh: 3000đ/kWh. In tổng tiền; số âm → `So lieu khong hop le!`.
* **Input:** Số thực (kWh).
* **Output:** Số tiền phải trả (đồng).
* **Ví dụ:**
  ```
  Nhập số điện tiêu thụ (kWh): 65
  Số tiền phải trả: 162500.0 đồng
  ```
* **Gợi ý:** Dùng guard: `case _ if so_kwh <= 50:` (công thức: 50×2000 + (số còn lại)×2500).

### Bài 18: Máy tính nâng cao

* **Đề bài:** Nhập hai số và phép toán `+`, `-`, `*`, `/`, `//` (chia nguyên), `%` (chia dư), `**` (lũy thừa). In kết quả; phép toán khác → `Phep toan khong hop le!`; chia cho 0 → `Khong the chia cho 0!`.
* **Input:** Hai số và một chuỗi phép toán.
* **Output:** Kết quả.
* **Ví dụ:**
  ```
  Nhập số thứ nhất: 7
  Nhập số thứ hai: 3
  Nhập phép toán: //
  7 // 3 = 2
  ```
* **Gợi ý:** Match chuỗi phép toán; kiểm tra `b == 0` trong các case có chia.

### Bài 19: Đặt món tại nhà hàng

* **Đề bài:** Nhà hàng có menu: món chính (1. Phở 35k, 2. Cơm gà 40k, 3. Bún 30k), size (S = 1 lần, L = 1.5 lần giá), đồ uống (1. Trà đá 5k, 2. Nước ngọt 10k, 3. Cà phê 15k). Nhập lần lượt món chính, size, đồ uống; in tổng tiền hóa đơn.
* **Input:** Số món chính, chuỗi size, số đồ uống.
* **Output:** Tổng tiền.
* **Ví dụ:**
  ```
  Món chính (1-3): 2
  Size (S/L): L
  Đồ uống (1-3): 3
  Tổng tiền: 75.0 ngàn đồng
  ```
* **Gợi ý:** Ba khối `match` liên tiếp, mỗi khối gán giá tiền vào một biến, cuối cùng tính tổng.

### Bài 20: Máy bán nước tự động

* **Đề bài:** Máy bán nước có 4 sản phẩm: 1. Trà đá 5k, 2. Coca 10k, 3. Nước cam 15k, 4. Cà phê 12k. Người mua nhập số sản phẩm, nhập số tiền bỏ vào (chẵn nghìn). Nếu tiền không đủ → `Thieu tien!`; đủ thì in tên món, giá và tiền thừa; số sản phẩm sai → `San pham khong ton tai!`.
* **Input:** Số sản phẩm (1–4) và số tiền (số nguyên).
* **Output:** Kết quả giao dịch.
* **Ví dụ:**
  ```
  Chọn sản phẩm (1-4): 3
  Nhập số tiền: 20000
  Ban mua: Nuoc cam - 15000 đồng
  Tiền thừa: 5000 đồng
  ```
* **Gợi ý:** Gán giá vào biến trong từng case, `case _` bắt sản phẩm sai; sau match dùng `if` so sánh tiền với giá.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Viết thành thạo `match-case` với `case`, `case _`, dấu `|`.
* ✅ Xử lý được chuỗi nhập vào bằng `.upper()` / `.lower()`.
* ✅ Dùng guard `case _ if ...` cho bài toán khoảng giá trị.
* ✅ Khớp **bộ giá trị** `match (a, b):` để giải quyết bài toán nhiều biến.
* ✅ Kết hợp match-case với `if` bên trong case để kiểm tra thêm.

> 💪 Chưa tự làm được bài nào thì đừng lo — hãy xem lại bài giảng rồi quay lại. **Lập trình là luyện tập!**

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 10: Vòng Lặp For](../10_Vong_lap_for/bai_giang.md)**
