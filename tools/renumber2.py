# -*- coding: utf-8 -*-
"""
Đánh số lại lần 2: chèn bài mới
  - b26 Vét Cạn  (sau b25)  -> b26
  - b30 Tần Suất (sau b28 cũ) -> b30
Mapping: 1-25 giữ; 26-28 -> +1; 29-44 -> +2. Tổng 46 bài.
- Fix ref sót từ flatten (specials, được bảo vệ khỏi shift)
- Shift inline "Bài N" >=26
- Đồng bộ: H1, banner, link targets, link labels, Vị trí
Dùng: python tools/renumber2.py [--apply]
"""
import re
import sys
import shutil
from pathlib import Path

ROOT = Path(r"D:\HyperHub - HSG Tin")
APPLY = "--apply" in sys.argv
REPORT = Path(r"C:\Users\Mk2012\AppData\Local\Temp\opencode\renumber2_report.txt")

SLUGS = {
    1: "Gioi-Thieu", 2: "Cai-Dat-Python", 3: "Bien", 4: "Kieu-Du-Lieu",
    5: "Toan-Tu", 6: "Input-Output", 7: "Cau-Lenh-If", 8: "Vong-Lap-For",
    9: "Vong-Lap-While", 10: "Ham", 11: "Scope", 12: "List", 13: "Tuple",
    14: "Set", 15: "Dictionary", 16: "String", 17: "Module", 18: "File",
    19: "OOP", 20: "Lambda", 21: "List-Comprehension", 22: "Generator",
    23: "Regex", 24: "Tu-Duy-Thuat-Toan", 25: "Do-Phuc-Tap",
    26: "Tim-Kiem", 27: "Sap-Xep", 28: "Stack-Queue-Hashing", 29: "De-Quy",
    30: "Quay-Lui", 31: "Hai-Con-Tro", 32: "Tham-Lam", 33: "Quy-Hoach-Dong",
    34: "Toan-Hoc-So-Hoc", 35: "Do-Thi-BFS-DFS", 36: "Duong-Di-Ngan-Nhat",
    37: "Cay-Va-DSU", 38: "Segment-Tree", 39: "Xu-Ly-Chuoi", 40: "Bitmask",
    41: "DP-Nang-Cao", 42: "Chien-Luoc-Thi-HSG", 43: "Itertools", 44: "Ly-Thuyet-Tro-Choi",
}
SHIFT_KEYS = range(26, 45)  # chỉ các bài 26-44 bị đổi số

def new_num(n: int) -> int:
    if n <= 25:
        return n
    if n <= 28:
        return n + 1
    return n + 2

SLUG_TO_NEW = {SLUGS[o]: new_num(o) for o in SLUGS}
SLUG_TO_OLD = {s: o for o, s in SLUGS.items()}

def old_folder(n): return f"b{n:02d}-{SLUGS[n]}"
def new_folder(n): return f"b{new_num(n):02d}-{SLUGS[n]}"

# ================== SPECIALS: (folder_cũ, before, after) — chạy TRƯỚC shift, được bảo vệ ==================
SPECIALS = [
("b01-Gioi-Thieu",
 "* Luyện viết **biến** (đã thấy ở bài 15, 17, 19) — bài sau sẽ học kỹ hơn về biến!",
 "* Luyện viết **biến** — sẽ học kỹ ở **Bài 3 — Biến Trong Python**."),
("b02-Cai-Dat-Python",
 "### Ví dụ: Sử dụng pip cơ bản (học kỹ ở bài 31)",
 "### Ví dụ: Sử dụng pip cơ bản (dùng khi cần cài thư viện ngoài)"),
("b03-Bien",
 "số/chuỗi thì a không ảnh hưởng, list thì có (Bài 14)",
 "số/chuỗi thì a không ảnh hưởng, list thì có (Bài 12)"),
("b05-Toan-Tu",
 "kỹ năng sẽ học ở bài 7.",
 "kỹ năng sẽ học ở bài 6."),
("b05-Toan-Tu",
 "(sẽ đọc kỹ ở bài 7)",
 "(sẽ đọc kỹ ở bài 6)"),
("b06-Input-Output",
 "cách xử lý lỗi sẽ học ở bài 19.",
 "cách xử lý lỗi bằng `try/except` sẽ học khi làm việc với file (Bài 18)."),
("b06-Input-Output",
 "thay thế bằng `if` rõ ràng hơn ở bài 8.",
 "thay thế bằng `if` rõ ràng hơn ở bài 7."),
("b06-Input-Output",
 "Kết hợp tất cả kiến thức bài 7: nhập nhiều kiểu dữ liệu",
 "Kết hợp cả bài: nhập nhiều kiểu dữ liệu"),
("b07-Cau-Lenh-If",
 "thêm `elif gio >= 18` — bài 9 sẽ là nơi thử điều đó với `match`.",
 "thêm `elif gio >= 18` — mở rộng cho buổi tối."),
("b07-Cau-Lenh-If",
 "chờ vòng lặp ở bài 10–11.",
 "chờ vòng lặp ở bài 8–9."),
("b07-Cau-Lenh-If",
 "Khi học vòng lặp (bài 10, 11), thêm `while`",
 "Khi học vòng lặp (bài 8, 9), thêm `while`"),
("b15-Dictionary",
 "Cùng cú pháp gán như bài 4,",
 "Cùng cú pháp gán như bài 3,"),
("b15-Dictionary",
 "(sẽ học sâu ở bài 26).",
 "(sẽ học sâu ở bài 21)."),
("b16-String",
 "trong khối bắt lỗi (bài 19);",
 "trong khối bắt lỗi (try/except);"),
("b16-String",
 "— bài 19 sẽ học cách chuẩn hơn.",
 "— sẽ có cách xử lý lỗi chuẩn hơn ở phần sau."),
("b16-String",
 "(bài 19 sẽ học cách chuyên nghiệp hơn).",
 "(sẽ học cách xử lý lỗi chuyên nghiệp hơn ở phần sau)."),
("b17-Module",
 "**file module và file dùng nó nằm cùng thư mục**. Bài 21 (Package) và Bài 23 (Virtual Environment) sẽ dạy cách tổ chức chuyên nghiệp hơn.",
 "**file module và file dùng nó nằm cùng thư mục**. Cách tổ chức chuyên nghiệp hơn sẽ học khi làm dự án thật."),
("b17-Module",
 "| `json` | Dữ liệu JSON (bài 32) |",
 "| `json` | Dữ liệu JSON |"),
("b17-Module",
 "| `csv` | File CSV (bài 33) |",
 "| `csv` | File CSV |"),
("b17-Module",
 "Trước khi cài thư viện ngoài (Bài 32), hãy kiểm tra",
 "Trước khi cài thư viện ngoài, hãy kiểm tra"),
("b17-Module",
 "bọc `int(input(...))` trong `try/except` (Bài 19) để an toàn.",
 "bọc `int(input(...))` trong `try/except` để an toàn."),
("b18-File",
 "### 1. Nhắc lại Bài 21 — và vấn đề lớn nhất hiện tại",
 "### 1. Vấn đề lớn nhất hiện tại"),
("b18-File",
 "Ở **Bài 21**, dữ liệu (học sinh, điểm số) nằm trong biến",
 "Tới lúc này, dữ liệu (học sinh, điểm số) nằm trong biến"),
("b19-OOP",
 "### 1. Nhắc lại Bài 18 — điểm yếu của cách cũ",
 "### 1. Nhắc lại — điểm yếu của cách cũ"),
("b19-OOP",
 "Ở **Bài 22**, mỗi học sinh là một dict:",
 "Ở các bài trước, mỗi học sinh là một dict:"),
("b19-OOP",
 "(kiến thức Bài 19).",
 "(kiến thức try/except)."),
("b20-Lambda",
 "(kết hợp dataclass bài 24)",
 "(dùng `@dataclass` của thư viện chuẩn)"),
("b21-List-Comprehension",
 "Ở bài 10 (vòng lặp `for`) và bài 14 (list),",
 "Ở bài 8 (vòng lặp `for`) và bài 12 (list),"),
("b21-List-Comprehension",
 "giống hệt `filter` ở bài 25 nhưng gọn hơn:",
 "giống hệt `filter` ở bài 20 nhưng gọn hơn:"),
("b21-List-Comprehension",
 "| `filter` + lambda (bài 25) |",
 "| `filter` + lambda (bài 20) |"),
("b21-List-Comprehension",
 "(kết hợp dataclass bài 24)",
 "(dùng `@dataclass`)"),
("b21-List-Comprehension",
 "chi tiết bài 27!",
 "chi tiết bài 22!"),
("b22-Generator",
 "Ở bài 26, ta viết `[x*x for x in range(10)]`",
 "Ở bài 21, ta viết `[x*x for x in range(10)]`"),
("b24-Tu-Duy-Thuat-Toan",
 "(xem Bài 24).",
 "(xem Bài 25)."),
("b24-Tu-Duy-Thuat-Toan",
 "| Dãy đã sắp xếp + cần tìm nhanh | Tìm kiếm nhị phân (Bài 25) |",
 "| Dãy đã sắp xếp + cần tìm nhanh | Tìm kiếm nhị phân (Bài 27) |"),
("b24-Tu-Duy-Thuat-Toan",
 "\"Dãy con liên tiếp\" + tối ưu | Hai con trỏ / cửa sổ trượt (Bài 30) |",
 "\"Dãy con liên tiếp\" + tối ưu | Hai con trỏ / cửa sổ trượt (Bài 33) |"),
("b24-Tu-Duy-Thuat-Toan",
 "| Lựa chọn từng bước, không quay lui | Tham lam (Bài 31) |",
 "| Lựa chọn từng bước, không quay lui | Tham lam (Bài 34) |"),
("b24-Tu-Duy-Thuat-Toan",
 "| Bài toán con lặp lại, \"tối ưu\" | Quy hoạch động (Bài 32) |",
 "| Bài toán con lặp lại, \"tối ưu\" | Quy hoạch động (Bài 35) |"),
("b24-Tu-Duy-Thuat-Toan",
 "| Số nguyên tố, ước, chia hết | Số học (Bài 33) |",
 "| Số nguyên tố, ước, chia hết | Số học (Bài 36) |"),
("b25-Do-Phuc-Tap",
 "**Bài tiếp theo:** [Bài 26 — Tìm Kiếm Tuyến Tính & Nhị Phân](../b26-Tim-Kiem/bai.md)",
 "**Bài tiếp theo:** [Bài 26 — Vét Cạn (Brute Force)](../b26-Vet-Can/bai.md)"),
("b18-File",
 "Bài 33 (JSON) và Bài 34 (CSV) sẽ dạy định dạng lưu trữ chuẩn hơn.",
 "các định dạng chuẩn như JSON, CSV sẽ được dạy kỹ khi làm dự án thật."),
("b42-Chien-Luoc-Thi-HSG",
 "Tổng hợp từ Bài 23–41 thành",
 "Tổng hợp từ Bài 24–46 thành"),
("b28-Stack-Queue-Hashing",
 "**Bài tiếp theo:** [Bài 29 — Đệ Quy](../b29-De-Quy/bai.md)",
 "**Bài tiếp theo:** [Bài 30 — Tần Suất (Đếm & Thống Kê)](../b30-Tan-Suat/bai.md)"),
("b30-Quay-Lui",
 "(ôn Bài 34).",
 "(học sâu ở Bài 42)."),
("b42-Chien-Luoc-Thi-HSG",
 "- Toàn bộ Bài 23–41 nhánh Thuật Toán (đặc biệt Bài 23 — tư duy, Bài 24 — Big-O)",
 "- Toàn bộ Bài 24–46 phần Thuật Toán (đặc biệt Bài 24 — tư duy, Bài 25 — Big-O)"),
("b42-Chien-Luoc-Thi-HSG",
 "| 23. Đọc | Input? Output? Ràng buộc? Ví dụ? | 5–10 phút |\n| 24. Phân loại | Mẫu nào (Bài 23–41)? Big-O nào sống? (mục 2) | 5–15 phút |\n| 25. Nghĩ | Pseudocode + chạy tay + tìm phản ví dụ | 30–40% tổng |\n| 26. Code | Một mạch từ pseudocode, đặt tên rõ | 20–30% tổng |\n| 27. Test | Ví dụ + 4 loại biên + stress (mục 4) | 30% tổng |",
 "| 1. Đọc | Input? Output? Ràng buộc? Ví dụ? | 5–10 phút |\n| 2. Phân loại | Mẫu nào (Bài 24–46)? Big-O nào sống? (mục 2) | 5–15 phút |\n| 3. Nghĩ | Pseudocode + chạy tay + tìm phản ví dụ | 30–40% tổng |\n| 4. Code | Một mạch từ pseudocode, đặt tên rõ | 20–30% tổng |\n| 5. Test | Ví dụ + 4 loại biên + stress (mục 4) | 30% tổng |"),
("b42-Chien-Luoc-Thi-HSG",
 "| 23. Tư duy | Phân rã, mẫu, pseudocode, test 5 loại | \"Bắt đầu từ đâu?\" |\n| 24. Big-O | Đếm, bảng ràng buộc, bẫy Python | \"Có đủ nhanh không?\" |\n| 25. Tìm kiếm | Tuyến tính, nhị phân, bisect, chặt đáp số | \"Tìm trong dãy xếp?\" |\n| 26. Sắp xếp | `sorted` + key, merge, nghịch thế | \"Xếp rồi làm gì?\" |\n| 27. Stack/Queue/Hash | Ngoặc, deque đơn điệu, Counter, heap | \"Lồng/đếm/min liên tục?\" |\n| 28. Đệ quy | Base + niềm tin, memo, lũy thừa nhanh | \"Bài con giống bài cha?\" |\n| 29. Quay lui | Chọn–thử–hoàn tác, tỉa | \"n ≤ 25, liệt kê cách?\" |\n| 30. Hai con trỏ | Trỏ đôi, trượt, tiền tố (+dict) | \"Đoạn liên tiếp?\" |\n| 31. Tham lam | Sort + 1 vòng, exchange, phản VD | \"Chọn tốt nhất có an toàn?\" |\n| 32. DP | 5 bước, top-down/bottom-up, lăn mảng | \"Bài con gối nhau?\" |\n| 33. Số học | Sàng, Euclid, pow mod, Fermat, C(n,k) | \"Ước/nguyên tố/mod?\" |\n| 34. Đồ thị | BFS/DFS, thành phần, topo, hai phía | \"Quan hệ/lưới/mê cung?\" |\n| 35. Đường ngắn nhất | Dijkstra, Bellman-Ford, Floyd | \"Chi phí nhỏ nhất?\" |\n| 36. Cây & DSU | Đường kính, LCA, Kruskal, hợp nhất | \"Cây/MST/nhóm động?\" |\n| 37. Đoạn & BIT | Segment tree, Fenwick, range query | \"Truy vấn đoạn + cập nhật?\" |\n| 38. Chuỗi | KMP, Z, rolling hash, Trie | \"Tìm mẫu/đếm xâu con?\" |\n| 39. Bitmask | Bit tricks, meet-in-the-middle, TSP | \"n ≤ 20, trạng thái tập hợp?\" |\n| 40. DP nâng cao | DAG, digit DP, tree DP, interval DP | \"DP 1 chiều không đủ?\" |\n| 41. Thi cử | Quy trình, subtask, stress, checklist | \"Làm sao AC dưới áp lực?\" |",
 "| 24. Tư duy | Phân rã, mẫu, pseudocode, test 5 loại | \"Bắt đầu từ đâu?\" |\n| 25. Big-O | Đếm, bảng ràng buộc, bẫy Python | \"Có đủ nhanh không?\" |\n| 26. Vét cạn | Duyệt hết mọi khả năng khi n nhỏ | \"Thử hết được không?\" |\n| 27. Tìm kiếm | Tuyến tính, nhị phân, bisect, chặt đáp số | \"Tìm trong dãy xếp?\" |\n| 28. Sắp xếp | `sorted` + key, merge, nghịch thế | \"Xếp rồi làm gì?\" |\n| 29. Stack/Queue/Hash | Ngoặc, deque đơn điệu, Counter, heap | \"Lồng/đếm/min liên tục?\" |\n| 30. Tần suất | Đếm bằng dict/Counter, top-K, sắp theo số lần | \"Đếm xuất hiện bao nhiêu lần?\" |\n| 31. Đệ quy | Base + niềm tin, memo, lũy thừa nhanh | \"Bài con giống bài cha?\" |\n| 32. Quay lui | Chọn–thử–hoàn tác, tỉa | \"n ≤ 25, liệt kê cách?\" |\n| 33. Hai con trỏ | Trỏ đôi, trượt, tiền tố (+dict) | \"Đoạn liên tiếp?\" |\n| 34. Tham lam | Sort + 1 vòng, exchange, phản VD | \"Chọn tốt nhất có an toàn?\" |\n| 35. DP | 5 bước, top-down/bottom-up, lăn mảng | \"Bài con gối nhau?\" |\n| 36. Số học | Sàng, Euclid, pow mod, Fermat, C(n,k) | \"Ước/nguyên tố/mod?\" |\n| 37. Đồ thị | BFS/DFS, thành phần, topo, hai phía | \"Quan hệ/lưới/mê cung?\" |\n| 38. Đường ngắn nhất | Dijkstra, Bellman-Ford, Floyd | \"Chi phí nhỏ nhất?\" |\n| 39. Cây & DSU | Đường kính, LCA, Kruskal, hợp nhất | \"Cây/MST/nhóm động?\" |\n| 40. Đoạn & BIT | Segment tree, Fenwick, range query | \"Truy vấn đoạn + cập nhật?\" |\n| 41. Chuỗi | KMP, Z, rolling hash, Trie | \"Tìm mẫu/đếm xâu con?\" |\n| 42. Bitmask | Bit tricks, meet-in-the-middle, TSP | \"n ≤ 20, trạng thái tập hợp?\" |\n| 43. DP nâng cao | DAG, digit DP, tree DP, interval DP | \"DP 1 chiều không đủ?\" |\n| 44. Thi cử | Quy trình, subtask, stress, checklist | \"Làm sao AC dưới áp lực?\" |\n| 45. itertools | product/permutations/combinations, accumulate, groupby | \"Liệt kê/gom có sẵn?\" |\n| 46. Trò chơi | Nim, XOR, số Grundy | \"Thắng/thua khi chơi tối ưu?\" |"),
("b42-Chien-Luoc-Thi-HSG",
 "đủ mọi mẫu Bài 23–41 |",
 "đủ mọi mẫu Bài 24–46 |"),
("b42-Chien-Luoc-Thi-HSG",
 "(Bài 23 — ví dụ 3)",
 "(Bài 24 — ví dụ 3)"),
("b42-Chien-Luoc-Thi-HSG",
 "| ≤ 10 | Hoán vị, vét cạn mọi thứ | Bài 29 |\n| ≤ 20–25 | Bitmask, quay lui + tỉa, DP mũ (TSP) | Bài 29, 10 |\n| ≤ 500 | DP O(n³), Floyd | Bài 32 |\n| ≤ 5.000 | O(n²): DP, LIS O(n²), thử cặp | Bài 30, 10 |\n| ≤ 10⁵–10⁶ | O(n log n): sort, nhị phân, heap, DP O(n log n) | Bài 25, 4, 9, 10 |\n| ≤ 10⁷–10⁸ | O(n): duyệt, hai con trỏ, Counter | Bài 24, 5, 8 |\n| ≤ 10¹² | O(√n): kiểm tra nguyên tố, phân tích thừa số | Bài 33 |\n| ≤ 10¹⁸ | O(log n): nhị phân đáp số, lũy thừa nhanh/ma trận | Bài 25, 6, 11 |\n| Đồ thị n, m ≤ 10⁵–10⁶ | O(n+m): BFS/DFS; O(m log n): Dijkstra | Bài 34, 14 |\n| q truy vấn đoạn ≤ 10⁵ | O(log n)/truy vấn: segment tree / Fenwick | Bài 37 |",
 "| ≤ 10 | Hoán vị, vét cạn mọi thứ | Bài 26, 32 |\n| ≤ 20–25 | Bitmask, quay lui + tỉa, DP mũ (TSP) | Bài 32, 42 |\n| ≤ 500 | DP O(n³), Floyd | Bài 35, 38 |\n| ≤ 5.000 | O(n²): DP, LIS O(n²), thử cặp | Bài 26, 33, 35 |\n| ≤ 10⁵–10⁶ | O(n log n): sort, nhị phân, heap, DP O(n log n) | Bài 27, 28, 29, 35 |\n| ≤ 10⁷–10⁸ | O(n): duyệt, hai con trỏ, Counter | Bài 29, 33 |\n| ≤ 10¹² | O(√n): kiểm tra nguyên tố, phân tích thừa số | Bài 36 |\n| ≤ 10¹⁸ | O(log n): nhị phân đáp số, lũy thừa nhanh/ma trận | Bài 27, 36 |\n| Đồ thị n, m ≤ 10⁵–10⁶ | O(n+m): BFS/DFS; O(m log n): Dijkstra | Bài 37, 38 |\n| q truy vấn đoạn ≤ 10⁵ | O(log n)/truy vấn: segment tree / Fenwick | Bài 40 |"),
("b42-Chien-Luoc-Thi-HSG",
 "🎉 **Bạn đã hoàn thành nhánh Thuật Toán!** Hai hướng đi tiếp:\n- 🚀 Nhánh 03 — Thực Chiến (API/Package/Project)",
 "🎯 **Chiến lược đã nằm trong tay!** Hai hộp đồ nghề còn lại:\n- 🧰 [Bài 45 — itertools: Hộp Đồ Nghề Vòng Lặp Cho Thi Đấu](../b45-Itertools/bai.md)\n- 🎮 [Bài 46 — Lý Thuyết Trò Chơi: Nim & Số Grundy](../b46-Ly-Thuyet-Tro-Choi/bai.md)"),
("b23-Regex",
 "🏆 **Bạn đã hoàn thành lộ trình Cơ bản!** Giờ bạn có thể chọn nhánh:\n- 🧮 [Nhánh 02 — Thuật Toán (HSG/CP)](../b24-Tu-Duy-Thuat-Toan/bai.md)\n- 🚀 Nhánh 03 — Thực Chiến (API/Package/Project)",
 "🏆 **Bạn đã hoàn thành Phần 1 — Nền tảng (Bài 1–23)!** Tiếp tục ngay với:\n- 🧮 [Phần 2 — Thuật Toán (HSG/CP)](../b24-Tu-Duy-Thuat-Toan/bai.md) — từ **Bài 24 — Tư Duy Thuật Toán** tới **Bài 46 — Lý Thuyết Trò Chơi**."),
("b44-Ly-Thuyet-Tro-Choi",
 "🏆 **Bạn đã hoàn thành toàn bộ track Thuật toán (Bài 1–43)!** Ôn lại\n[Bài 24 — Tư Duy Thuật Toán](../b24-Tu-Duy-Thuat-Toan/bai.md) với con mắt mới,\nhoặc sang Nhánh 03 — Thực Chiến.",
 "🏆 **Bạn đã hoàn thành toàn bộ khóa học Nền tảng + Thuật toán (Bài 1–46)!** Ôn lại [Bài 24 — Tư Duy Thuật Toán](../b24-Tu-Duy-Thuat-Toan/bai.md) với con mắt mới, và bắt đầu luyện đề thi thật nhé!"),
("b01-Gioi-Thieu",
 "(cần kiến thức bài 7)",
 "(cần kiến thức bài 6)"),
("b07-Cau-Lenh-If",
 "vòng lặp sẽ học ở bài 10, 11.",
 "vòng lặp sẽ học ở bài 8, 9."),
("b07-Cau-Lenh-If",
 "**nhập - ép kiểu** (bài 7), **toán tử** (bài 6), và **rẽ nhánh** (bài này). Chỉ cần thêm vòng lặp (bài 10, 11)",
 "**nhập - ép kiểu** (bài 6), **toán tử** (bài 5), và **rẽ nhánh** (bài này). Chỉ cần thêm vòng lặp (bài 8, 9)"),
("b07-Cau-Lenh-If",
 "dài quá nghĩ cách tách hàm (bài 12).",
 "dài quá nghĩ cách tách hàm (bài 10)."),
("b07-Cau-Lenh-If",
 "(công thức từ bài 6).",
 "(công thức từ bài 5)."),
("b07-Cau-Lenh-If",
 "Tính trung bình trước (bài 7),",
 "Tính trung bình trước (bài 6),"),
("b07-Cau-Lenh-If",
 "Kết hợp bài 6 (toán tử) + bài 7 (nhập - ép kiểu) vào",
 "Kết hợp bài 5 (toán tử) + bài 6 (nhập - ép kiểu) vào"),
("b07-Cau-Lenh-If",
 "Dùng đúng biểu thức từ bài 6:",
 "Dùng đúng biểu thức từ bài 5:"),
("b07-Cau-Lenh-If",
 "toán tử gán kết hợp của bài 6 —",
 "toán tử gán kết hợp của bài 5 —"),
("b07-Cau-Lenh-If",
 "theo hệ số (bài 7), vừa xếp loại",
 "theo hệ số (bài 6), vừa xếp loại"),
("b08-Vong-Lap-For",
 "`while` (bài 11)",
 "`while` (bài 9)"),
("b08-Vong-Lap-For",
 "phép chia lấy dư (bài 6)",
 "phép chia lấy dư (bài 5)"),
("b09-Vong-Lap-While",
 "Kết hợp kiến thức bài 8 (if-elif) với while",
 "Kết hợp kiến thức bài 7 (if-elif) với while"),
("b09-Vong-Lap-While",
 "Biến tích lũy (bài 10) kết hợp while.",
 "Biến tích lũy (bài 8) kết hợp while."),
("b09-Vong-Lap-While",
 "Giống bài 5 (bài 10) nhưng bằng while.",
 "Giống bài 5 (bài 8) nhưng bằng while."),
("b09-Vong-Lap-While",
 "kết hợp while với if-elif (bài 8).",
 "kết hợp while với if-elif (bài 7)."),
("b09-Vong-Lap-While",
 "# Xếp loại (kiến thức bài 8)",
 "# Xếp loại (kiến thức bài 7)"),
("b09-Vong-Lap-While",
 "chi tiết bài 20).",
 "chi tiết bài 17)."),
("b10-Ham",
 "Nhìn lại bài 11 (vòng lặp while)",
 "Nhìn lại bài 9 (vòng lặp while)"),
("b10-Ham",
 "(mở rộng từ bài 11)",
 "(mở rộng từ bài 9)"),
("b11-Scope",
 "Nhớ lại bài 12:",
 "Nhớ lại bài 10:"),
("b13-Tuple",
 "(chi tiết bài 17).",
 "(chi tiết bài 15)."),
("b13-Tuple",
 "(bài 12, 23 sẽ gặp)",
 "(bài 10, 19 sẽ gặp)"),
("b13-Tuple",
 "(bài 17 sẽ thấy)",
 "(bài 15 sẽ thấy)"),
("b13-Tuple",
 "(bài 16, 17 sẽ gặp lại)",
 "(bài 14, 15 sẽ gặp lại)"),
("b14-Set",
 "dành riêng cho dictionary (bài 17).",
 "dành riêng cho dictionary (bài 15)."),
("b14-Set",
 "bằng dict đếm (bài 17).",
 "bằng dict đếm (bài 15)."),
("b17-Module",
 "Ở **Bài 19**, chúng ta học cách dùng `try/except` để **xử lý lỗi** mà không làm chương trình sập:",
 "Nhắc lại một kỹ năng quan trọng: dùng `try/except` để **xử lý lỗi** mà không làm chương trình sập:"),
("b18-File",
 "Giải pháp: bọc trong `try/except` (kiến thức **Bài 19**):",
 "Giải pháp: bọc trong `try/except`:"),
("b18-File",
 "kết hợp `try/except` (Bài 19) khi dữ liệu không tin cậy.",
 "kết hợp `try/except` khi dữ liệu không tin cậy."),
("b19-OOP",
 "— Bài tiếp theo **Dataclass** sẽ giúp viết class ngắn gọn hơn hẳn!",
 "— bạn sẽ dùng nó trong mọi bài phía sau!"),
("b19-OOP",
 "Bài sau sẽ gọn nhẹ hơn hẳn với **dataclass** — Python tự sinh `__init__`, `__str__`... cho bạn!",
 "Khi viết nhiều class, hãy tìm hiểu `@dataclass` — Python tự sinh `__init__`, `__str__`... giúp code gọn hơn!"),
]

# ================== HELPERS ==================
LINKS_RE = re.compile(r"\[[^\]]*\]\([^)]*\)")
LABEL_RE = re.compile(r"\[Bài (\d+)([^\]]*)\]\((\.\./)?b(\d{2})-([A-Za-z0-9-]+)/")
H1_RE = re.compile(r"^# Bài \d+ — ")
VI_TRI_RE = re.compile(r"\*\*Vị trí:\*\* `b\d{2}-[^`]+`")
BANNER_OLD = "b1–b44"
BANNER_NEW = "b1–b46"
PATH_RE = re.compile(r"b(\d{2})-([A-Za-z0-9-]+)")

SKIP_PREFIXES = ("### Bài ", "**Bài ", "- **Bài ", "## 🟢", "## 🟡", "## 🔴", "## 🟨", "## 🟥",
                 "## ➕", "### 🟢", "### 🟡", "### 🔴", "### ➕", "<summary>", "**Vị trí:**", "# ")

def in_slug_set(slug):
    return slug in SLUG_TO_NEW

def shift_links_and_paths(text):
    def repl(m):
        num, slug = int(m.group(1)), m.group(2)
        if in_slug_set(slug):
            return f"b{new_num(num):02d}-{slug}"
        return m.group(0)
    return PATH_RE.sub(repl, text)

def sync_labels(text):
    def repl(m):
        slug = m.group(5)
        if slug not in SLUG_TO_NEW:
            return m.group(0)
        target_new = SLUG_TO_NEW[slug]
        return f"[Bài {target_new}{m.group(2)}]({m.group(3) or ''}b{target_new:02d}-{slug}/"
    return LABEL_RE.sub(repl, text)

def shift_refs(text, log):
    lines = text.splitlines()
    out = []
    for ln in lines:
        s = ln.strip()
        if ln.startswith(tuple(SKIP_PREFIXES)) or s.startswith(tuple(SKIP_PREFIXES)):
            out.append(ln)
            continue
        # bảo vệ link
        links = []
        def grab(m):
            links.append(m.group(0))
            return f"\ue100{len(links)-1}\ue101"
        masked = LINKS_RE.sub(grab, ln)

        def do_shift(m):
            n = int(m.group(2))
            nn = new_num(n) if n >= 26 else n
            if nn != n:
                log.append(f"    SHIFT: {m.group(1)}{n} -> {m.group(1)}{nn} :: {s[:90]}")
            return f"{m.group(1)}{nn}"

        masked = re.sub(r"([Bb]ài )(\d+)(\s*[–—-]\s*)(\d+)", lambda m: (
            (m.group(1) + str(new_num(int(m.group(2)))) + m.group(3) + str(new_num(int(m.group(4)))))
            if int(m.group(2)) >= 26 or int(m.group(4)) >= 26 else m.group(0)), masked)
        masked = re.sub(r"([Bb]ài )(\d+)", lambda m: do_shift2(m, log), masked)

        # restore links
        def ungrab(m):
            return links[int(m.group(1))]
        masked = re.sub(r"\ue100(\d+)\ue101", ungrab, masked)
        out.append(masked)
    return "\n".join(out)

def do_shift2(m, log):
    n = int(m.group(2))
    nn = new_num(n) if n >= 26 else n
    if nn != n:
        log.append(f"    SHIFT: {m.group(1)}{n} -> {m.group(1)}{nn}")
    return f"{m.group(1)}{nn}"

# ================== MAIN ==================
def main():
    rep = []
    files = {}
    for n in range(1, 45):
        f = ROOT / old_folder(n) / "bai.md"
        if not f.exists():
            rep.append(f"MISSING: {f}")
            continue
        files[n] = f.read_text(encoding="utf-8")

    # 1) specials (bảo vệ)
    rep.append("== SPECIALS ==")
    holders = {}
    for idx, (folder, before, after) in enumerate(SPECIALS):
        src_n = int(folder[1:3])
        text = files[src_n]
        cnt = text.count(before)
        if cnt != 1:
            rep.append(f"  FAIL [{cnt}] {folder}: {before[:80]}...")
            continue
        token = f"\ue200{idx}\ue201"
        files[src_n] = text.replace(before, token)
        holders[token] = after
        rep.append(f"  ok  {folder}: {before[:60]}...")

    # 2) per-file transforms
    rep.append("== TRANSFORM ==")
    logs = {}
    for n in range(1, 45):
        text = files[n]
        log = []
        # H1
        if not H1_RE.search(text):
            rep.append(f"  [{n}] H1 pattern not found!")
        text = H1_RE.sub(f"# Bài {new_num(n)} — ", text, count=1)
        # banner
        text = text.replace(BANNER_OLD, BANNER_NEW)
        # global reword Nhánh Thuật Toán -> Phần Thuật Toán
        text = text.replace("Nhánh Thuật Toán", "Phần Thuật Toán").replace("nhánh Thuật Toán", "phần Thuật Toán")
        # Vị trí
        text = VI_TRI_RE.sub(f"**Vị trí:** `{new_folder(n)}/bai.md`", text)
        # paths + links
        text = shift_links_and_paths(text)
        # labels
        text = sync_labels(text)
        # inline shift
        text = shift_refs(text, log)
        logs[n] = log
        files[n] = text

    for n in range(1, 45):
        if logs[n]:
            rep.append(f"  [{n}] {len(logs[n])} shift")

    # 3) restore holders
    for n in range(1, 45):
        for token, after in holders.items():
            if token in files[n]:
                files[n] = files[n].replace(token, after)

    # leftover check
    rep.append("== LEFTOVER CHECK (ref >=26 outside links) ==")
    for n in range(1, 45):
        text = files[n]
        masked = LINKS_RE.sub("", text)
        for m in re.finditer(r"[Bb]ài (\d+)(?:\s*[–—-]\s*(\d+))?", masked):
            a = int(m.group(1)); b = int(m.group(2)) if m.group(2) else None
            if a >= 26 or (b and b >= 26):
                rep.append(f"  [{old_folder(n)}] B{a}{'-'+str(b) if b else ''}: ...{masked[max(0,m.start()-40):m.end()+40]}...".replace("\n", " "))

    # WRITE
    if APPLY:
        rep.append("== APPLY ==")
        # rename folders (descending)
        for n in sorted(SHIFT_KEYS, reverse=True):
            oldp = ROOT / old_folder(n)
            newp = ROOT / new_folder(n)
            if oldp.exists():
                shutil.move(str(oldp), str(newp))
                rep.append(f"  renamed {old_folder(n)} -> {new_folder(n)}")
        # write files
        for n in range(1, 45):
            dst = ROOT / new_folder(n) / "bai.md"
            dst.write_text(files[n], encoding="utf-8", newline="\n")
        rep.append("  wrote 44 files")

    REPORT.write_text("\n".join(rep), encoding="utf-8")
    print("APPLY" if APPLY else "DRY", "done;", "report:", REPORT)

if __name__ == "__main__":
    main()
