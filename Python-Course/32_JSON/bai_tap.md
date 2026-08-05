# 📝 Bài 32: Bài Tập – JSON

> 🎯 **Chủ đề:** `json.dumps`, `json.loads`, `json.dump`, `json.load`, cấu trúc JSON, tiếng Việt trong JSON, lỗi thường gặp, ứng dụng danh bạ / sản phẩm / cấu hình.
> 📘 Hãy **tự viết code và chạy thử** trước khi xem đáp án.

---

## 📌 Hướng dẫn làm bài

* Tạo file `.py` riêng cho từng bài (hoặc gom nhiều bài một file).
* Với bài ghi file, kiểm tra file JSON sinh ra bằng trình soạn thảo hoặc `python -m json.tool file.json`.
* Đáp án chi tiết 20 bài: 👉 [xem file dap_an.md](dap_an.md)

---

## 🟢 Dễ (Bài 1 – 7)

### Bài 1: Chuyển từ điển sang JSON

* **Đề bài:** Dùng `json.dumps` chuyển từ điển `{"ten": "An", "tuoi": 15}` thành chuỗi JSON rồi in ra. In cả `type()` của kết quả.
* **Input:** Không có
* **Output:**
  ```
  {"ten": "An", "tuoi": 15}
  <class 'str'>
  ```
* **Gợi ý:** `import json; chuoi = json.dumps(du_lieu)`.

### Bài 2: Chuyển JSON sang Python

* **Đề bài:** Dùng `json.loads` chuyển chuỗi `'{"lop": "10A1", "si_so": 40}'` thành từ điển. In `type()` và giá trị `"si_so"`.
* **Input:** Không có
* **Output:**
  ```
  <class 'dict'>
  40
  ```
* **Gợi ý:** `du_lieu["si_so"]`.

### Bài 3: JSON đẹp với indent

* **Đề bài:** Dùng `json.dumps` với `indent=2` in ra đẹp từ điển `{"a": 1, "b": [1, 2]}`.
* **Input:** Không có
* **Output:**
  ```
  {
    "a": 1,
    "b": [
      1,
      2
    ]
  }
  ```
* **Gợi ý:** `json.dumps(x, indent=2)`.

### Bài 4: List sang JSON

* **Đề bài:** Chuyển danh sách `[10, 20, "ba"]` sang chuỗi JSON và in ra.
* **Input:** Không có
* **Output:**
  ```
  [10, 20, "ba"]
  ```
* **Gợi ý:** `json.dumps` làm việc với cả list.

### Bài 5: Boolean và None

* **Đề bài:** Chuyển từ điển `{"ok": True, "x": None, "diem": 8.5}` sang JSON và in ra.
* **Input:** Không có
* **Output:**
  ```
  {"ok": true, "x": null, "diem": 8.5}
  ```
* **Gợi ý:** Chú ý `true`, `null` viết thường trong JSON.

### Bài 6: Ghi file JSON đầu tiên

* **Đề bài:** Ghi từ điển `{"mon": "Toan", "diem": 9}` vào file `mon.json` (mã hóa utf-8, giữ tiếng Việt). Kiểm tra file tồn tại.
* **Input:** Không có
* **Output:** File `mon.json` xuất hiện (nội dung dạng JSON).
* **Gợi ý:** `with open("mon.json", "w", encoding="utf-8") as f: json.dump(...)`.

### Bài 7: Đọc file JSON

* **Đề bài:** Đọc lại file `mon.json` từ bài 6 bằng `json.load`, in ra `type()` của dữ liệu và giá trị `"diem"`.
* **Input:** File `mon.json` đã tạo ở bài 6.
* **Output:**
  ```
  <class 'dict'>
  9
  ```
* **Gợi ý:** `with open("mon.json", "r", encoding="utf-8") as f: du_lieu = json.load(f)`.

---

## 🟡 Trung bình (Bài 8 – 14)

### Bài 8: Danh bạ điện thoại

* **Đề bài:** Tạo từ điển danh bạ 3 người (tên → số điện thoại), ghi vào `danh_ba.json` (có `ensure_ascii=False`, `indent=2`), đọc lại và in số điện thoại của người thứ 2.
* **Input:** Không có
* **Output:** Số điện thoại của người thứ 2 (một dòng).
* **Gợi ý:** Làm theo Ví dụ 1 trong bài giảng.

### Bài 9: Lưu danh sách sản phẩm

* **Đề bài:** Danh sách 3 sản phẩm `{"ma", "ten", "gia", "ton_kho"}`. Ghi vào `san_pham.json`, đọc lại và in ra tổng số mặt hàng.
* **Input:** Không có
* **Output:**
  ```
  Tổng mặt hàng: 3
  ```
* **Gợi ý:** `len(danh_sach)` sau khi `json.load`.

### Bài 10: Cấu hình ứng dụng

* **Đề bài:** Tạo cấu hình `{"ten_ung_dung": "LopHocApp", "so_dong": 10, "am_luong": 0.5}`. Lưu vào `cau_hinh.json`, đọc lại, tăng `am_luong` thêm 0.2 rồi lưu lại. In ra cấu hình cuối cùng.
* **Input:** Không có
* **Output:**
  ```
  LopHocApp — âm lượng: 0.7
  ```
* **Gợi ý:** Đọc → sửa `cau_hinh["am_luong"] += 0.2` → ghi lại.

### Bài 11: Thêm ghi chú

* **Đề bài:** Đọc file `ghi_chu.json` (nếu chưa có thì dùng `[]`), thêm một ghi chú `{"tieu_de": "Bai 32", "noi_dung": "Da xong"}` vào cuối, lưu lại. Chạy 2 lần và in số ghi chú sau mỗi lần.
* **Input:** Không có
* **Output:**
  ```
  1
  2
  ```
* **Gợi ý:** Kiểm tra file tồn tại bằng `os.path.exists`; `append` rồi `json.dump`.

### Bài 12: Tính tổng từ JSON phức tạp

* **Đề bài:** Dữ liệu `hoc_sinh = [{"ten": "An", "mon": [8, 7]}, {"ten": "Binh", "mon": [9, 10]}]`. Ghi vào file, đọc lại, in ra tổng điểm của từng học sinh.
* **Input:** Không có
* **Output:**
  ```
  An: 15
  Binh: 19
  ```
* **Gợi ý:** `sum(hs["mon"])` cho mỗi học sinh.

### Bài 13: Sửa lỗi JSON thủ công

* **Đề bài:** File `loi.json` có nội dung sai:
  ```json
  {"ten": 'An', "diem": [8, 9,],}
  ```
  Chạy `json.loads` và ghi lại lỗi xuất hiện. Sau đó sửa lại chuỗi đúng và in kết quả.
* **Input:** Chuỗi JSON sai ở trên.
* **Output:**
  ```
  Lỗi: JSONDecodeError ...
  {'ten': 'An', 'diem': [8, 9]}
  ```
* **Gợi ý:** Lỗi do `'An'` (nháy đơn) và dấu phẩy thừa; sửa bằng `"An"` và bỏ `,`.

### Bài 14: Lọc sản phẩm rẻ

* **Đề bài:** Tạo danh sách sản phẩm 4 món (tên, giá), ghi file, đọc lại và in ra các sản phẩm có giá **dưới 10000 đồng**.
* **Input:** Không có
* **Output:** Tên các sản phẩm rẻ (mỗi tên một dòng).
* **Gợi ý:** Vòng lặp kiểm tra `sp["gia"] < 10000`.

---

## 🔴 Khó (Bài 15 – 20)

### Bài 15: Điểm trung bình và xếp loại

* **Đề bài:** Dữ liệu 4 học sinh `{"ten", "mon": [3 điểm]}`. Ghi file, đọc lại, tính điểm TB mỗi người và xếp loại: TB ≥ 8 là "Giỏi", ≥ 5 là "Đạt", còn lại "Cần cố gắng". In kết quả.
* **Input:** Không có
* **Output:**
  ```
  An: 8.0 - Giỏi
  Binh: 6.0 - Đạt
  ...
  ```
* **Gợi ý:** `sum(hs["mon"]) / len(hs["mon"])` + cấu trúc `if/elif/else`.

### Bài 16: Cập nhật tồn kho khi bán hàng

* **Đề bài:** Đọc `san_pham.json` (3 sản phẩm có `ton_kho`), bán 2 món mã 1, ghi lại file, in ra sản phẩm có `ton_kho` còn lại của mã 1.
* **Input:** File từ bài 9 (hoặc tự tạo).
* **Output:**
  ```
  Ton kho con lai: X
  ```
  (X = ton_kho ban đầu - 2)
* **Gợi ý:** Duyệt danh sách tìm `ma == 1`, giảm `ton_kho`, `json.dump`.

### Bài 17: Gộp hai file JSON

* **Đề bài:** Tạo `lopA.json` (2 học sinh) và `lopB.json` (2 học sinh). Viết chương trình đọc cả hai, gộp vào một danh sách, lưu `tat_ca.json`, in tổng số học sinh.
* **Input:** Hai file JSON tự tạo.
* **Output:**
  ```
  Tổng số học sinh: 4
  ```
* **Gợi ý:** `danh_sach = lop_a + lop_b`.

### Bài 18: Tìm kiếm trong JSON

* **Đề bài:** Danh bạ 5 người lưu trong file. Viết chương trình đọc file và in ra tên của tất cả người có **số điện thoại bắt đầu bằng "0903"**.
* **Input:** Không có
* **Output:** Tên người tìm được (mỗi tên một dòng).
* **Gợi ý:** Duyệt `danh_ba.items()`; kiểm tra `so.startswith("0903")`.

### Bài 19: Đếm số sản phẩm theo loại

* **Đề bài:** Danh sách sản phẩm có trường `"loai"` (VD: "van_phong", "hoc_tap", "sach"). Ghi file, đọc lại, đếm số sản phẩm mỗi loại và in ra.
* **Input:** Không có
* **Output:**
  ```
  van_phong: 2
  hoc_tap: 3
  ...
  ```
* **Gợi ý:** Dùng dict đếm: `dem[sp["loai"]] = dem.get(sp["loai"], 0) + 1`.

### Bài 20: Ứng dụng quản lý điểm chuẩn hoàn chỉnh

* **Đề bài:** Xây ứng dụng nhỏ: menu lựa chọn (1. Thêm học sinh, 2. Xem danh sách, 3. Thoát). Dữ liệu lưu trong `hoc_sinh.json` (danh sách `{"ten", "diem"}`). Thao tác mỗi lần lưu đều ghi lại file.
* **Input:** Nhập từ bàn phím: `1`, `An 8` (tên kèm điểm), `2`, `3`.
* **Output:** Xem danh sách hiển thị từng học sinh kèm điểm; thoát khi chọn 3.
* **Gợi ý:** Dùng `while True`, `if chon == "1"` đọc file → append → ghi; `if chon == "2"` đọc và in; `if chon == "3"` `break`.

---

## 🎯 Tổng kết sau khi làm bài

Sau 20 bài tập, bạn đã:

* ✅ Chuyển đổi thành thạo giữa Python và JSON (dumps/loads/dump/load).
* ✅ Ghi/đọc file JSON tiếng Việt đúng chuẩn (`utf-8`, `ensure_ascii=False`).
* ✅ Xây được các ứng dụng thực tế: danh bạ, sản phẩm, cấu hình, ghi chú, quản lý điểm.
* ✅ Nhận biết và sửa các lỗi JSON phổ biến.

> 💪 Chưa tự làm được bài nào thì đừng lo — đọc lại bài giảng, làm từng bước: ghi thử, mở file xem nội dung, đọc lại. **Lập trình là luyện tập!**

👉 Xem **[Đáp án chi tiết 20 bài](dap_an.md)** | Tiếp theo: **[Bài 33: CSV](../33_CSV/bai_giang.md)**