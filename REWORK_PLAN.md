# 📋 Kế Hoạch Tái Cấu Trúc HyperHub Python

> Tài liệu này ghi lại toàn bộ quá trình phân tích, thiết kế và chuyển đổi khóa học.
> Mục đích: người bảo trì có thể hiểu được toàn bộ rework mà không phải đoán.

---

## 1. Kết quả kiểm kê (Audit)

### Hiện trạng repository trước khi rework

```
HyperHub - HSG Tin/
├── README.md                       ← gần như trống (chỉ có tiêu đề lỗi font)
├── Python-Course/                  ← 41 bài × 3 file (bai_giang, bai_tap, dap_an)
├── Python-Thuật Toán/              ← THƯ MỤC RỖNG (chưa có nội dung thuật toán)
├── Giao-Trinh-Lap-Trinh-Python-Co-Ban.pdf
├── Lap Trinh Python Cho Nguoi Moi Bat Dau-Moonbook-LNH.pdf
└── PythonCoban_UTEHY.pdf
```

### Phát hiện chính

| # | Vấn đề | Mức độ |
|---|---|---|
| 1 | README gốc gần như rỗng, font lỗi | 🔴 Cần viết lại toàn bộ |
| 2 | Tách 3 file `bai_giang.md` / `bai_tap.md` / `dap_an.md` — người học phải nhảy giữa 3 file | 🔴 Gộp thành 1 file `bai.md` |
| 3 | Không có lộ trình 3 nhánh (Cơ bản / Thuật toán / Thực chiến) | 🔴 Cần thiết kế lại |
| 4 | Thư mục `Python-Thuật Toán` rỗng — hoàn toàn thiếu nội dung thuật toán cho HSG | 🔴 Cải viết từ đầu |
| 5 | README `Python-Course` có lỗi chính tả / font: `thứ tự лі volume`, `검 tra nhanh`, `== loạim match – case`, `Danh ѕố List`, `Lộ rình`, `hướng đối hướng đối tượng` | 🟡 Sửa trong lần viết lại |
| 6 | Link tương đối trong bài có nguy cơ hỏng sau khi đổi cấu trúc | 🟡 Sinh lại link tự động |
| 7 | Chất lượng nội dung bài giảng tốt: tiếng Việt có dấu, mermaid, bảng, ví dụ, lỗi thường gặp, 20 bài tập/bài, đáp án chi tiết | ✅ Bảo toàn, không viết lại từ đầu |

### Nhận xét chất lượng nội dung cũ

* Bài giảng viết tự nhiên, có ví dụ đời thực, sơ đồ mermaid, bảng so sánh, mục "Lỗi thường gặp", "Mẹo", "Tóm tắt", "Kiểm tra nhanh" (10 câu có đáp án ẩn).
* Mỗi bài có 20 bài tập chia 3 mức (🟢 Dễ 1–7, 🟡 TB 8–14, 🔴 Khó 15–20) + đáp án chi tiết (Phân tích, Ý tưởng, Thuật toán, Code, Giải thích, Độ phức tạp).
* Tổng khối lượng: **~45.000 dòng** nội dung qua 123 file → phải chuyển đổi bằng script để **không mất nội dung**, sau đó nâng cấp tay từng bài quan trọng.

---

## 2. Cấu trúc mới — 3 lộ trình

```
PYTHON
  │
  ▼
01. CƠ BẢN  (bắt buộc — nền tảng cho mọi nhánh)
  │
  ▼
Hoàn thành nền tảng
      /              \
     ▼                ▼
02. THUẬT TOÁN    03. THỰC CHIẾN
  HSG / CP          API / Package / Project
```

* **01-Co-Ban**: bắt buộc. Từ số 0 đến OOP + Generator/Decorator/Iterator.
* **02-Thuat-Toan**: tùy chọn, dành cho HSG / competitive programming. Viết mới hoàn toàn.
* **03-Thuc-Chien**: tùy chọn, độc lập với 02. Dùng Python trong dự án thật.

### Bản đồ chuyển đổi bài học

**Nhánh 01-Co-Ban** (từ bài 1–29 cũ — đổi tên thư mục, gộp 3 file thành `bai.md`):

| Bài cũ | Thư mục mới |
|---|---|
| 01_Gioi_thieu | 01-Co-Ban/01-Gioi-Thieu |
| 02_Cai_dat_Python | 01-Co-Ban/02-Cai-Dat-Python |
| 03_VSCode | 01-Co-Ban/03-VSCode |
| 04_Bien | 01-Co-Ban/04-Bien |
| 05_Kieu_du_lieu | 01-Co-Ban/05-Kieu-Du-Lieu |
| 06_Toan_tu | 01-Co-Ban/06-Toan-Tu |
| 07_Input_Output | 01-Co-Ban/07-Input-Output |
| 08_Cau_lenh_if | 01-Co-Ban/08-Cau-Lenh-If |
| 09_Match_case | 01-Co-Ban/09-Match-Case |
| 10_Vong_lap_for | 01-Co-Ban/10-Vong-Lap-For |
| 11_Vong_lap_while | 01-Co-Ban/11-Vong-Lap-While |
| 12_Ham | 01-Co-Ban/12-Ham |
| 13_Scope | 01-Co-Ban/13-Scope |
| 14_List | 01-Co-Ban/14-List |
| 15_Tuple | 01-Co-Ban/15-Tuple |
| 16_Set | 01-Co-Ban/16-Set |
| 17_Dictionary | 01-Co-Ban/17-Dictionary |
| 18_String | 01-Co-Ban/18-String |
| 19_Exception | 01-Co-Ban/19-Exception |
| 20_Module | 01-Co-Ban/20-Module |
| 21_Package | 01-Co-Ban/21-Package |
| 22_File | 01-Co-Ban/22-File |
| 23_OOP | 01-Co-Ban/23-OOP |
| 24_Dataclass | 01-Co-Ban/24-Dataclass |
| 25_Lambda | 01-Co-Ban/25-Lambda |
| 26_List_Comprehension | 01-Co-Ban/26-List-Comprehension |
| 27_Generator | 01-Co-Ban/27-Generator |
| 28_Decorator | 01-Co-Ban/28-Decorator |
| 29_Iterator | 01-Co-Ban/29-Iterator |

**Nhánh 02-Thuat-Toan** (nội dung MỚI — viết tay, chuẩn HSG/competitive programming):

| Bài | Thư mục mới | Nội dung |
|---|---|---|
| 1 | 01-Tu-Duy-Thuat-Toan | Tư duy thuật toán, phân tích đề, phân rã bài toán |
| 2 | 02-Do-Phuc-Tap | Độ phức tạp thời gian O(1)…O(n²), đếm phép toán |
| 3 | 03-Tim-Kiem | Tìm kiếm tuyến tính & nhị phân, chặt nhị phân trên đáp số |
| 4 | 04-Sap-Xep | Bubble, selection, insertion, merge sort, so sánh |
| 5 | 05-Stack-Queue-Hashing | Stack, queue, deque, bảng băm, map/set trong bài toán |
| 6 | 06-De-Quy | Đệ quy, ngăn xếp gọi, đệ quy có nhớ |
| 7 | 07-Quay-Lui | Backtracking: sinh xâu, tổ hợp, N-queens |
| 8 | 08-Hai-Con-Tro | Two pointers, sliding window, prefix sum |
| 9 | 09-Tham-Lam | Greedy: đổi tiền, xếp lịch, chọn đoạn |
| 10 | 10-Quy-Hoach-Dong | Quy hoạch động: LIS, LCS, cái túi |
| 11 | 11-Toan-Hoc-So-Hoc | Số nguyên tố, GCD/LCM, lũy thừa nhanh, đồng dư |
| 12 | 12-Do-Thi-BFS-DFS | Danh sách kề, BFS/DFS, thành phần, topo, hai phía, flood fill |
| 13 | 13-Duong-Di-Ngan-Nhat | Dijkstra, Bellman-Ford, Floyd, minimax, arbitrage |
| 14 | 14-Cay-Va-DSU | Đường kính, LCA binary lifting, DSU, Kruskal |
| 15 | 15-Segment-Tree | Segtree lặp, Fenwick, nén tọa độ, hiệu phân |
| 16 | 16-Xu-Ly-Chuoi | KMP/pi, Z, rolling hash, Trie, XOR max |
| 17 | 17-Bitmask | Bit tricks, TSP, phân công, meet-in-the-middle, SOS DP |
| 18 | 18-DP-Nang-Cao | DAG, digit DP, tree DP, interval DP |
| 19 | 19-Chien-Luoc-Thi-HSG | Đọc đề, chiến lược thi, quản lý thời gian, test case |

**Nhánh 03-Thuc-Chien** (từ bài 30–41 cũ — gộp 3 file thành `bai.md`):

| Bài cũ | Thư mục mới |
|---|---|
| 30_Virtual_Environment | 03-Thuc-Chien/01-Virtual-Environment |
| 31_Pip | 03-Thuc-Chien/02-Pip |
| 32_JSON | 03-Thuc-Chien/03-JSON |
| 33_CSV | 03-Thuc-Chien/04-CSV |
| 34_API | 03-Thuc-Chien/05-API |
| 35_Requests | 03-Thuc-Chien/06-Requests |
| 36_SQLite | 03-Thuc-Chien/07-SQLite |
| 37_Logging | 03-Thuc-Chien/08-Logging |
| 38_Typing | 03-Thuc-Chien/09-Typing |
| 39_Asyncio | 03-Thuc-Chien/10-Asyncio |
| 40_Mini_Project | 03-Thuc-Chien/11-Mini-Project |
| 41_Du_an_Cuoi_Khoa | 03-Thuc-Chien/12-Du-An-Cuoi-Khoa |

---

## 3. Định dạng `bai.md` hợp nhất

Mỗi bài học = **1 file duy nhất**, cấu trúc:

```markdown
# Bài N — Tên bài

## 🎯 Mục tiêu                  ← từ bai_giang
## 🧠 Điều kiện tiên quyết       ← MỚI (sinh theo bản đồ phụ thuộc)
## 📖 Kiến thức ...              ← từ bai_giang (giữ nguyên các mục con)
## ⚠️ Lỗi thường gặp             ← từ bai_giang
## 💎 Mẹo                        ← từ bai_giang
## 📝 Tóm tắt                    ← từ bai_giang
## 🧪 Kiểm tra nhanh             ← từ bai_giang (đã có đáp án ẩn sẵn)
## 🧩 Bài tập                    ← từ bai_tap (20 bài, 3 mức)
## ✅ Đáp án                     ← từ dap_an (mỗi bài bọc <details> riêng)
## ➡️ Bài tiếp theo              ← link tương đối mới, sinh tự động
```

### Quy tắc chuyển đổi

1. **Không xóa nội dung hữu ích** — script gộp toàn bộ 3 file.
2. Bỏ phần "Kết thúc bài" của `bai_giang` (link cũ) → sinh link mới đúng cấu trúc.
3. Bỏ phần điều hướng của `bai_tap` (trỏ tới `dap_an.md` — hết thời stale) .
4. Đáp án: mỗi câu bọc `<details><summary>✅ Bài N: …</summary>` — nhấn mới xem.
5. Link tương đối giữa các bài **sinh lại từ bản đồ cấu trúc mới** — không giữ link cũ.
6. Sau khi gộp và kiểm tra xong mới xóa cấu trúc cũ.

---

## 4. Chiến lược thực thi (phases)

| Phase | Công việc | Trạng thái |
|---|---|---|
| 1 | Audit toàn bộ repository | ✅ Xong |
| 2 | Thiết kế cấu trúc 3 lộ trình + bản đồ chuyển đổi | ✅ Xong (tài liệu này) |
| 3 | Script chuyển đổi 41 bài cũ → `bai.md` mới | ✅ Xong |
| 4 | Xóa cấu trúc cũ sau khi validate | ✅ Xong |
| 5 | Viết mới 12 bài nhánh Thuật toán | ✅ Xong |
| 5b | Mở rộng nhánh Thuật toán lên 19 bài (đồ thị, đường ngắn nhất, cây/DSU, segment tree, chuỗi, bitmask, DP nâng cao) | ✅ Xong |
| 5c | Gộp vật lý 3 mục tự chứa: 01-Co-Ban (gốc) + 02-Thuat-Toan/Phan-1 + 04-Full (3 phần + PDF) | ✅ Xong |
| 6 | Viết lại README gốc với roadmap 3 nhánh | ✅ Xong |
| 7 | Validate: link hỏng, file thiếu, tham chiếu cũ | ✅ Xong (script `tools/validate.py`) |

---

## 5. Chiến lược kiểm tra

* **Script kiểm tra** `tools/validate.py`:
  * Quét toàn bộ `.md` — tìm link tương đối hỏng.
  * Tìm tham chiếu tới file đã xóa (`bai_giang.md`, `bai_tap.md`, `dap_an.md`).
  * Kiểm tra mỗi thư mục bài học có đúng 1 file `bai.md`.
  * Kiểm tra khối code fence ` ``` ` cân bằng (mở/đóng đủ).
  * Kiểm tra khối `<details>` có `</details>` đóng đủ.
* **Kiểm tra Python thuần**: chạy trực tiếp các ví dụ khả thi bằng `python`.
* **Kiểm tra gói ngoài** (requests, FastAPI, SQLite…): đối chiếu tài liệu chính thức, tách rõ ví dụ cần internet/API key.

---

## 6. Quyết định thiết kế lớn (lưu lại lý do)

| Quyết định | Lý do |
|---|---|
| Giữ nội dung cũ, gộp bằng script thay vì viết lại từ đầu | Nội dung cũ chất lượng tốt (~45k dòng). Viết lại tay 41 bài trong một lần sẽ phát sinh lỗi và mất nội dung. Script gộp đảm bảo 0 mất mát, sau đó nâng cấp tay từng bài. |
| 3 mục tự chứa bằng copy + script đồng bộ (thay vì viết tay 3 lần) | Người học chỉ mở 1 thư mục duy nhất. Copy tay sẽ lệch nhau sau vài lần sửa → `tools/sync_tracks.py` tái tạo toàn bộ copy từ bản chính, `tools/validate.py` kiểm tra link. Quy tắc: chỉ sửa `01-Co-Ban`, `02-Thuat-Toan/*` (trừ `Phan-1`), `03-Thuc-Chien`. |
| Nhánh Thuật toán viết mới hoàn toàn | Thư mục cũ rỗng. Chuẩn HSG cần tư duy giải bài toán, không phải liệt kê định nghĩa. |
| Nhánh Thực chiến tách khỏi Thuật toán | Hai mục tiêu khác nhau: giải thuật vs dùng Python trong dự án thật. Không bắt buộc học 02 trước 03. |
| Đáp án bọc `<details>` theo từng câu | Người học chỉ mở đúng câu mình bí, không lộ đáp án các câu khác. |
| PDF giáo trình giữ nguyên ở gốc | Tài liệu tham khảo, không phải nội dung khóa học web. |
