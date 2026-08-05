# 📝 Bài 38: Bài Tập – Type Hints

> 🎯 **Chủ đề:** Chú thích kiểu dữ liệu cho biến, tham số, giá trị trả về; module `typing` (List, Dict, Optional, Union, Tuple, Any); type alias.
>
> 📌 **Lưu ý:** Type hints chỉ là ghi chú — chương trình chạy đúng với mọi đáp án dưới đây kể cả khi gỡ bỏ chú thích. Mục đích bài tập là **làm quen cú pháp và phong cách** đúng. Nếu chưa làm được, hãy xem lại bài giảng — **đáp án chi tiết ở [dap_an.md](dap_an.md)**.

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Khai báo biến có chú thích

* **Đề bài:** Khai báo 4 biến kèm chú thích kiểu: `ten` (str), `tuoi` (int), `diem_tb` (float), `da_tot_nghiep` (bool) với giá trị tùy ý, rồi in cả 4 ra màn hình.
* **Input:** Không có.
* **Output:**
  ```
  An 15 8.5 True
  ```
* **Gợi ý:** `ten: str = "An"` ... rồi `print(ten, tuoi, diem_tb, da_tot_nghiep)`.

### Bài 2: Hàm chào có chú thích

* **Đề bài:** Viết hàm `chao(ten: str) -> str` trả về `"Xin chao, <ten>!"`. Gọi với tên `Mai` và in kết quả.
* **Input:** Không có.
* **Output:**
  ```
  Xin chao, Mai!
  ```
* **Gợi ý:** `return "Xin chao, " + ten + "!"`.

### Bài 3: Hàm cộng hai số

* **Đề bài:** Viết hàm `cong(a: int, b: int) -> int` trả về tổng, gọi với `cong(3, 4)` và in kết quả.
* **Input:** Không có.
* **Output:**
  ```
  7
  ```
* **Gợi ý:** `return a + b`.

### Bài 4: Hàm gấp đôi chuỗi

* **Đề bài:** Viết hàm `gap_doi(chuoi: str) -> str` trả về chuỗi lặp lại 2 lần, gọi với `"abc"`.
* **Input:** Không có.
* **Output:**
  ```
  abcabc
  ```
* **Gợi ý:** `return chuoi * 2` (toán tử `*` với chuỗi — học ở bài 18).

### Bài 5: Danh sách điểm

* **Đề bài:** Khai báo `diem: List[float] = [8.5, 9.0, 7.5]` (nhớ import), in từng điểm và in tổng.
* **Input:** Không có.
* **Output:**
  ```
  8.5
  9.0
  7.5
  Tong: 25.0
  ```
* **Gợi ý:** `from typing import List`; `sum(diem)`.

### Bài 6: Từ điển tên – điểm

* **Đề bài:** Khai báo `bang_diem: Dict[str, float]` với 2 cặp (An: 8.5, Binh: 9.0), in điểm của An.
* **Input:** Không có.
* **Output:**
  ```
  Diem cua An: 8.5
  ```
* **Gợi ý:** `from typing import Dict`; `bang_diem["An"]`.

### Bài 7: Tuple thông tin

* **Đề bài:** Khai báo `thong_tin: Tuple[str, int] = ("Mai", 16)` và in `Ten: Mai - Tuoi: 16`.
* **Input:** Không có.
* **Output:**
  ```
  Ten: Mai - Tuoi: 16
  ```
* **Gợi ý:** `from typing import Tuple`; giải nén `ten, tuoi = thong_tin`.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Hàm tìm điểm — Optional

* **Đề bài:** Viết hàm `tim_diem(ten: str, bang_diem: Dict[str, float]) -> Optional[float]` trả điểm hoặc `None`. Gọi với tên có trong bảng và tên không có; in kết quả.
* **Input:** Không có.
* **Output:**
  ```
  Diem An: 8.5
  Diem X: None
  ```
* **Gợi ý:** `return bang_diem.get(ten)`.

### Bài 9: Union hai kiểu số

* **Đề bài:** Viết hàm `nhan_doi(so: Union[int, float]) -> Union[int, float]` trả `so * 2`, gọi với `5` và `2.5`.
* **Input:** Không có.
* **Output:**
  ```
  10
  5.0
  ```
* **Gợi ý:** `from typing import Union`; chỉ cần `return so * 2`.

### Bài 10: Any — nhận bất kỳ

* **Đề bài:** Viết hàm `in_du_lieu(du_lieu: Any) -> None` in ra loại và giá trị: `Loai: <type> - Gia tri: <value>`. Gọi với số, chuỗi và list.
* **Input:** Không có.
* **Output:**
  ```
  Loai: <class 'int'> - Gia tri: 10
  Loai: <class 'str'> - Gia tri: chao
  Loai: <class 'list'> - Gia tri: [1, 2]
  ```
* **Gợi ý:** `type(du_lieu)` trả loại; `-> None` cho hàm chỉ in.

### Bài 11: Type alias đầu tiên

* **Đề bài:** Tạo alias `Diem = List[float]`. Viết hàm `tong_diem(diem: Diem) -> float` trả tổng. Gọi với `[1.5, 2.5, 3.0]`.
* **Input:** Không có.
* **Output:**
  ```
  Tong: 7.0
  ```
* **Gợi ý:** `Diem = List[float]` đặt ở đầu file.

### Bài 12: Hàm trả về danh sách

* **Đề bài:** Viết hàm `tao_danh_sach_so(n: int) -> List[int]` trả danh sách các số từ `1` đến `n`. Gọi với `n = 5`.
* **Input:** Không có.
* **Output:**
  ```
  [1, 2, 3, 4, 5]
  ```
* **Gợi ý:** `return list(range(1, n + 1))`.

### Bài 13: Dict chứa List

* **Đề bài:** Khai báo `lop: Dict[str, List[float]]` với 2 học sinh mỗi em 3 điểm. Viết hàm `in_lop(lop: Dict[str, List[float]]) -> None` in từng học sinh kèm điểm.
* **Input:** Không có.
* **Output:**
  ```
  An: [8.5, 9.0, 7.0]
  Binh: [9.0, 8.0, 9.5]
  ```
* **Gợi ý:** Vòng lặp `for ten, diem in lop.items():`.

### Bài 14: Hàm kiểm tra chuỗi

* **Đề bài:** Viết hàm `kiem_tra_ten(ten: str) -> bool` trả `True` nếu tên dài ít nhất 3 ký tự và không chứa số. Gọi với `"An"`, `"Mai"`, `"A1"`.
* **Input:** Không có.
* **Output:**
  ```
  An: False
  Mai: True
  A1: False
  ```
* **Gợi ý:** `len(ten) >= 3 and not any(c.isdigit() for c in ten)` (kỹ thuật `any()` có thể học thêm).

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Optional với giá trị mặc định

* **Đề bài:** Viết hàm `tim_sinh_vien(ma: int, danh_sach: Dict[int, str]) -> Optional[str]` trả tên sinh viên theo mã; nếu không có trả `None`. Gọi với mã có và không có; với mã không có in thêm `Khong tim thay.`
* **Input:** Không có.
* **Output:**
  ```
  Ma 1: An
  Khong tim thay sinh vien ma 99.
  ```
* **Gợi ý:** Kiểm tra `if ma in danh_sach:`.

### Bài 16: Alias tuple hồ sơ

* **Đề bài:** Tạo alias `HoSo = Tuple[str, int, float]` (tên, năm sinh, điểm). Viết hàm `hien_ho_so(ho_so: HoSo) -> None` in `Ten - NamSinh - Diem`. Gọi với `("Mai", 2008, 8.75)`.
* **Input:** Không có.
* **Output:**
  ```
  Mai - 2008 - 8.75
  ```
* **Gợi ý:** Giải nén `ten, nam, diem = ho_so`.

### Bài 17: Thống kê lớp với Dict

* **Đề bài:** Viết hàm `thong_ke(bang_diem: Dict[str, List[float]]) -> Dict[str, float]` trả từ điển `ten -> điểm trung bình` (làm tròn 2 chữ số). Gọi với lớp 2 học sinh.
* **Input:** Không có.
* **Output:**
  ```
  {'An': 8.17, 'Binh': 8.83}
  ```
* **Gợi ý:** Duyệt `items()`, tính `round(sum(d) / len(d), 2)`.

### Bài 18: Danh sách Optional

* **Đề bài:** Khai báo `diem_thi: List[Optional[float]] = [8.5, None, 7.0, None]` (None = bỏ thi). Viết chương trình đếm số người thi, số người bỏ thi và in điểm trung bình của người thi.
* **Input:** Không có.
* **Output:**
  ```
  So nguoi thi: 2
  So nguoi bo thi: 2
  Diem trung binh: 7.75
  ```
* **Gợi ý:** `d is None` để nhận diện; lọc danh sách hợp lệ bằng list comprehension (bài 26) hoặc vòng lặp.

### Bài 19: Tìm sinh viên với Optional

* **Đề bài:** Viết hàm `tim_sv_theo_ten(ten: str, danh_sach: List[Tuple[int, str]]) -> Optional[int]` trả mã sinh viên đầu tiên khớp tên, `None` nếu không có. Gọi với tên có và tên không có.
* **Input:** Không có.
* **Output:**
  ```
  Ma cua Mai: 2
  Khong tim thay X.
  ```
* **Gợi ý:** Vòng lặp `for ma, ten_sv in danh_sach:` và `return` ngay khi khớp.

### Bài 20: Chương trình tiện ích đầy đủ type hints

* **Đề bài:** Viết chương trình quản lý sản phẩm nhỏ với đầy đủ type hints: alias `SanPham = Tuple[int, str, float]` (mã, tên, giá); hàm `them_san_pham(danh_sach: List[SanPham], ma: int, ten: str, gia: float) -> None`, `tim_san_pham(danh_sach: List[SanPham], ten: str) -> Optional[SanPham]`, `tong_gia_tri(danh_sach: List[SanPham]) -> float`. Khởi tạo 2 sản phẩm, thêm 1, tìm 1, in tổng giá trị.
* **Input:** Không có.
* **Output:**
  ```
  Tim thay: (2, 'Chuot', 150.0)
  Tong gia tri: 700.0
  ```
* **Gợi ý:** Mỗi hàm đều khai báo kiểu đầy đủ; `Optional[SanPham]` cho hàm tìm.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Khai báo chú thích kiểu cho biến, tham số và giá trị trả về.
* ✅ Dùng thành thạo `List`, `Dict`, `Tuple`, `Optional`, `Union`, `Any` từ module `typing`.
* ✅ Tạo type alias để code gọn gàng, dễ đọc.
* ✅ Viết hàm tìm kiếm đúng chuẩn trả về `Optional` khi có thể "không tìm thấy".

> 💪 **Mẹo học:** Hãy viết type hints cho **tất cả** các hàm bạn viết từ nay — kể cả ở các bài sau — để thành phản xạ.

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 39: Asyncio](../39_Asyncio/bai_giang.md)**
