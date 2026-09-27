<div align="center">

# 🐍 HyperHub Python

**Khóa học Python hoàn chỉnh từ số 0 — Cơ bản bắt buộc, Thuật toán & Thực chiến tự chọn**

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Lessons](https://img.shields.io/badge/B%C3%A0i%20h%E1%BB%8Dc-60-orange)
![Lang](https://img.shields.io/badge/Ti%E1%BA%BFng%20Vi%E1%BB%87t-100%25-red)

*"Đừng chỉ đọc code — hãy viết code. Sai 100 lần vẫn tốt hơn nhìn đúng 100 lần."*

</div>

---

## 📖 HyperHub Python là gì?

**HyperHub Python** là bộ giáo trình lập trình Python **hoàn chỉnh, có cấu trúc
bài bản**, viết **100% tiếng Việt có dấu**, dành cho **học sinh, sinh viên và
người hoàn toàn mới bắt đầu**.

Khác với tài liệu liệt kê cú pháp khô khan, mỗi bài học ở đây được viết như một
người thầy giảng trực tiếp: ví dụ đời thực, sơ đồ minh họa, lỗi thường gặp,
trường hợp biên, bài tập phân cấp kèm đáp án giải thích chi tiết.

---

## 🗺️ Lộ trình học — 3 nhánh

```
                    PYTHON
                       |
                       v
              ┌── 01. CƠ BẢN ── ✅ BẮT BUỘC
              │      29 bài: từ số 0 đến OOP,
              │      Generator, Decorator, Iterator
              ▼
        Hoàn thành nền tảng
            /              \
           v                v
  02. THUẬT TOÁN      03. THỰC CHIẾN
  🧮 HSG / Thi đấu     🚀 API / Package / Project
  12 bài (tự chọn)     12 bài (tự chọn)
```

| Nhánh | Đối tượng | Xong thì làm được gì |
|---|---|---|
| **01. Cơ bản** ✅ bắt buộc | Mọi người — học đầu tiên | Viết chương trình Python hoàn chỉnh: biến, rẽ nhánh, vòng lặp, hàm, list/dict, file, OOP cơ bản |
| **02. Thuật toán** (tự chọn) | Học sinh giỏi, thi HSG, competitive programming | Phân tích độ phức tạp, tìm kiếm/sắp xếp, đệ quy, quay lui, tham lam, quy hoạch động, số học, chiến lược phòng thi |
| **03. Thực chiến** (tự chọn) | Ai muốn dùng Python làm dự án thật | pip/venv, JSON/CSV, gọi API, SQLite, logging, async, mini project + đồ án cuối khóa |

> ⚠️ **Quy tắc duy nhất:** học xong **01. Cơ bản** rồi mới chọn nhánh 02 hoặc 03.
> Hai nhánh sau **độc lập nhau** — không cần học 02 trước 03 hay ngược lại.

---

## 🗂️ Cấu trúc repository

```
HyperHub-Python/
│
├── README.md                  ← bạn đang đọc
├── REWORK_PLAN.md             ← tài liệu thiết kế & tái cấu trúc khóa học
│
├── 01-Co-Ban/                 ✅ MỤC 1: chỉ cơ bản (29 bài, bản chính)
│   ├── 01-Gioi-Thieu/bai.md
│   ├── ...
│   └── 29-Iterator/bai.md
│
├── 02-Thuat-Toan/             🧮 MỤC 2: dãy phẳng (1)–(41), tự chứa
│   ├── 01-Gioi-Thieu/bai.md   ← 22 bài cơ bản (copy, số 1–22, lược 7 bài)
│   ├── ...
│   ├── 22-Generator/bai.md
│   ├── 23-Tu-Duy-Thuat-Toan/bai.md   ← 19 bài thuật toán (bản chính, số 23–41)
│   ├── ...
│   └── 41-Chien-Luoc-Thi-HSG/bai.md
│
├── 03-Thuc-Chien/             🚀 bản chính thực chiến (14 bài)
│   ├── 01-Virtual-Environment/bai.md
│   ├── ...
│   ├── 12-Du-An-Cuoi-Khoa/bai.md
│   ├── 13-Pytest/bai.md
│   └── 14-Git/bai.md
│
├── 04-Full/                   🏆 MỤC 3: full — tất cả + tài liệu (tự chứa)
│   ├── Phan-1-Co-Ban/         ← copy 29 bài cơ bản
│   ├── Phan-2-Thuat-Toan/     ← copy 19 bài thuật toán
│   ├── Phan-3-Thuc-Chien/     ← copy 12 bài thực chiến
│   └── Tai-Lieu/              ← 3 file PDF giáo trình tham khảo
│
└── tools/                     🛠️ script bảo trì
    ├── migrate.py             ← gộp 3 file cũ thành bai.md (đã dùng xong)
    ├── complete_answers.py    ← bổ sung đáp án thiếu (đã dùng xong)
    ├── sync_tracks.py         ← đồng bộ các bản copy (chạy sau mỗi lần sửa)
    └── validate.py            ← kiểm tra link hỏng, file thiếu, format
```

> 🗂️ **Vì sao có bản copy?** Ba mục là 3 lộ trình **tự chứa** để người học chỉ
> cần mở một thư mục duy nhất:
>
> | Mục | Chứa gì | Dành cho ai |
> |---|---|---|
> | `01-Co-Ban` | Chỉ 29 bài cơ bản (bản chính) | Người mới bắt đầu |
> | `02-Thuat-Toan` | Cơ bản (lược còn 22 bài) + 19 bài thuật toán | Luyện HSG, không cần nhảy thư mục |
> | `04-Full` | Cơ bản + thuật toán + thực chiến + PDF | Học từ đầu đến cuối một mạch |
>
> ✂️ **Track Thuật toán lược 7 bài cơ bản không cần cho HSG:**
> VSCode, Match-Case, Exception, Package, Dataclass, Decorator, Iterator —
> còn lại đánh số lại liên tục (1)–(22), nối tiếp thuật toán (23)–(41).
> "Bài tiếp theo", điều kiện tiên quyết và văn xuôi đã chỉnh khớp.
> Cần đủ 29 bài gốc? Học ở `01-Co-Ban` hoặc `04-Full`.
>
> Các thư mục `Phan-*` trong `04-Full` và 22 bài cơ bản trong `02-Thuat-Toan`
> là **bản copy tự động** — đừng sửa trực tiếp! Sửa bản chính
> (`01-Co-Ban`, `02-Thuat-Toan/23-..-41-..`, `03-Thuc-Chien`) rồi chạy:
>
> ```bash
> python tools/sync_tracks.py
> python tools/validate.py
> ```

**Mỗi bài học = 1 file duy nhất `bai.md`**, gồm: mục tiêu, điều kiện tiên quyết,
kiến thức, ví dụ, lỗi thường gặp, tóm tắt, kiểm tra nhanh, **20 bài tập phân cấp**
(🟢 Dễ – 🟡 Trung bình – 🔴 Khó) và **đáp án chi tiết** (nhấn để mở từng câu).

---

## 📚 Mục lục

### ✅ 01. Cơ bản — bắt buộc (29 bài)

| # | Bài học | # | Bài học |
|---|---|---|---|
| 1 | [Giới Thiệu Python](01-Co-Ban/01-Gioi-Thieu/bai.md) | 16 | [Set](01-Co-Ban/16-Set/bai.md) |
| 2 | [Cài Đặt Python](01-Co-Ban/02-Cai-Dat-Python/bai.md) | 17 | [Dictionary](01-Co-Ban/17-Dictionary/bai.md) |
| 3 | [VSCode](01-Co-Ban/03-VSCode/bai.md) | 18 | [String](01-Co-Ban/18-String/bai.md) |
| 4 | [Biến](01-Co-Ban/04-Bien/bai.md) | 19 | [Exception](01-Co-Ban/19-Exception/bai.md) |
| 5 | [Kiểu Dữ Liệu](01-Co-Ban/05-Kieu-Du-Lieu/bai.md) | 20 | [Module](01-Co-Ban/20-Module/bai.md) |
| 6 | [Toán Tử](01-Co-Ban/06-Toan-Tu/bai.md) | 21 | [Package](01-Co-Ban/21-Package/bai.md) |
| 7 | [Input / Output](01-Co-Ban/07-Input-Output/bai.md) | 22 | [File](01-Co-Ban/22-File/bai.md) |
| 8 | [Câu Lệnh If](01-Co-Ban/08-Cau-Lenh-If/bai.md) | 23 | [OOP](01-Co-Ban/23-OOP/bai.md) |
| 9 | [Match – Case](01-Co-Ban/09-Match-Case/bai.md) | 24 | [Dataclass](01-Co-Ban/24-Dataclass/bai.md) |
| 10 | [Vòng Lặp For](01-Co-Ban/10-Vong-Lap-For/bai.md) | 25 | [Lambda](01-Co-Ban/25-Lambda/bai.md) |
| 11 | [Vòng Lặp While](01-Co-Ban/11-Vong-Lap-While/bai.md) | 26 | [List Comprehension](01-Co-Ban/26-List-Comprehension/bai.md) |
| 12 | [Hàm](01-Co-Ban/12-Ham/bai.md) | 27 | [Generator](01-Co-Ban/27-Generator/bai.md) |
| 13 | [Scope](01-Co-Ban/13-Scope/bai.md) | 28 | [Decorator](01-Co-Ban/28-Decorator/bai.md) |
| 14 | [List](01-Co-Ban/14-List/bai.md) | 29 | [Iterator](01-Co-Ban/29-Iterator/bai.md) |
| 15 | [Tuple](01-Co-Ban/15-Tuple/bai.md) | | |

### 🧮 02. Thuật toán — dãy phẳng (1)–(41), tự chứa

Học một mạch không nhảy thư mục: 22 bài cơ bản (lược gọn cho HSG) nối tiếp 19 bài thuật toán.

| # | Bài học | # | Bài học |
|---|---|---|---|
| 1 | [Giới Thiệu Python](02-Thuat-Toan/01-Gioi-Thieu/bai.md) | 22 | [Generator – Sinh Dữ Liệu "Từng Phần Một"](02-Thuat-Toan/22-Generator/bai.md) |
| 2 | [Cài Đặt Python](02-Thuat-Toan/02-Cai-Dat-Python/bai.md) | 23 | [Tư Duy Thuật Toán](02-Thuat-Toan/23-Tu-Duy-Thuat-Toan/bai.md) |
| 3 | [Biến Trong Python](02-Thuat-Toan/03-Bien/bai.md) | 24 | [Độ Phức Tạp & Big-O](02-Thuat-Toan/24-Do-Phuc-Tap/bai.md) |
| 4 | [Kiểu Dữ Liệu Cơ Bản](02-Thuat-Toan/04-Kieu-Du-Lieu/bai.md) | 25 | [Tìm Kiếm Tuyến Tính & Nhị Phân](02-Thuat-Toan/25-Tim-Kiem/bai.md) |
| 5 | [Toán Tử Trong Python](02-Thuat-Toan/05-Toan-Tu/bai.md) | 26 | [Sắp Xếp](02-Thuat-Toan/26-Sap-Xep/bai.md) |
| 6 | [Nhập và Xuất Dữ Liệu](02-Thuat-Toan/06-Input-Output/bai.md) | 27 | [Stack, Queue & Hashing](02-Thuat-Toan/27-Stack-Queue-Hashing/bai.md) |
| 7 | [Câu Lệnh If – Cấu Trúc Rẽ Nhánh](02-Thuat-Toan/07-Cau-Lenh-If/bai.md) | 28 | [Đệ Quy](02-Thuat-Toan/28-De-Quy/bai.md) |
| 8 | [Vòng Lặp For – Lặp Lại Một Số Lần Biết Trước](02-Thuat-Toan/08-Vong-Lap-For/bai.md) | 29 | [Quay Lui (Backtracking)](02-Thuat-Toan/29-Quay-Lui/bai.md) |
| 9 | [Vòng Lặp While – Lặp Cho Đến Khi Điều Kiện Sai](02-Thuat-Toan/09-Vong-Lap-While/bai.md) | 30 | [Hai Con Trỏ, Cửa Sổ Trượt & Tổng Tiền Tố](02-Thuat-Toan/30-Hai-Con-Tro/bai.md) |
| 10 | [Hàm (Function) Trong Python](02-Thuat-Toan/10-Ham/bai.md) | 31 | [Tham Lam (Greedy)](02-Thuat-Toan/31-Tham-Lam/bai.md) |
| 11 | [Phạm Vi Biến (Scope) Trong Python](02-Thuat-Toan/11-Scope/bai.md) | 32 | [Quy Hoạch Động (Dynamic Programming)](02-Thuat-Toan/32-Quy-Hoach-Dong/bai.md) |
| 12 | [Danh Sách (List) Trong Python](02-Thuat-Toan/12-List/bai.md) | 33 | [Toán Học & Số Học Thuật Toán](02-Thuat-Toan/33-Toan-Hoc-So-Hoc/bai.md) |
| 13 | [Tuple (Bộ Dữ Liệu) Trong Python](02-Thuat-Toan/13-Tuple/bai.md) | 34 | [Đồ Thị: BFS & DFS](02-Thuat-Toan/34-Do-Thi-BFS-DFS/bai.md) |
| 14 | [Set (Tập Hợp) Trong Python](02-Thuat-Toan/14-Set/bai.md) | 35 | [Đường Đi Ngắn Nhất](02-Thuat-Toan/35-Duong-Di-Ngan-Nhat/bai.md) |
| 15 | [Dictionary (Từ Điển) Trong Python](02-Thuat-Toan/15-Dictionary/bai.md) | 36 | [Cây & DSU (Hợp Nhất Tập Rời)](02-Thuat-Toan/36-Cay-Va-DSU/bai.md) |
| 16 | [Chuỗi (String) Trong Python](02-Thuat-Toan/16-String/bai.md) | 37 | [Segment Tree & Fenwick (Cây Đoạn & Cây BIT)](02-Thuat-Toan/37-Segment-Tree/bai.md) |
| 17 | [Module Trong Python](02-Thuat-Toan/17-Module/bai.md) | 38 | [Xử Lý Chuỗi Nâng Cao: KMP, Z, Hash & Trie](02-Thuat-Toan/38-Xu-Ly-Chuoi/bai.md) |
| 18 | [Đọc Và Ghi File Trong Python](02-Thuat-Toan/18-File/bai.md) | 39 | [Bitmask & Tối Ưu Trên Tập Hợp](02-Thuat-Toan/39-Bitmask/bai.md) |
| 19 | [Lập Trình Hướng Đối Tượng (OOP)](02-Thuat-Toan/19-OOP/bai.md) | 40 | [Quy Hoạch Động Nâng Cao: DAG, Digit, Tree & Interval](02-Thuat-Toan/40-DP-Nang-Cao/bai.md) |
| 20 | [Lambda – Hàm Vô Danh Siêu Ngắn Gọn](02-Thuat-Toan/20-Lambda/bai.md) | 41 | [Chiến Lược Thi HSG & Tổng Kết Nhánh Thuật Toán](02-Thuat-Toan/41-Chien-Luoc-Thi-HSG/bai.md) |
| 21 | [List Comprehension – Vòng Lặp "Viết Trong Một Dòng"](02-Thuat-Toan/21-List-Comprehension/bai.md) | | |

### 🚀 03. Thực chiến — API / Package / Project (14 bài)

| # | Bài học | # | Bài học |
|---|---|---|---|
| 1 | [Virtual Environment](03-Thuc-Chien/01-Virtual-Environment/bai.md) | 7 | [SQLite](03-Thuc-Chien/07-SQLite/bai.md) |
| 2 | [Pip](03-Thuc-Chien/02-Pip/bai.md) | 8 | [Logging](03-Thuc-Chien/08-Logging/bai.md) |
| 3 | [JSON](03-Thuc-Chien/03-JSON/bai.md) | 9 | [Typing](03-Thuc-Chien/09-Typing/bai.md) |
| 4 | [CSV](03-Thuc-Chien/04-CSV/bai.md) | 10 | [Asyncio](03-Thuc-Chien/10-Asyncio/bai.md) |
| 5 | [API](03-Thuc-Chien/05-API/bai.md) | 11 | [Mini Project](03-Thuc-Chien/11-Mini-Project/bai.md) |
| 6 | [Requests](03-Thuc-Chien/06-Requests/bai.md) | 13 | [Kiểm Thử Với pytest](03-Thuc-Chien/13-Pytest/bai.md) |
| 7 | [SQLite](03-Thuc-Chien/07-SQLite/bai.md) | 14 | [Git & GitHub](03-Thuc-Chien/14-Git/bai.md) |

---

## 🚦 Cách học

### Tự học

1. **Chọn mục của bạn** (xem bảng 3 mục ở trên):
   - Chỉ học nền tảng → mở `01-Co-Ban`, bắt đầu từ
     [Bài 1 — Giới Thiệu Python](01-Co-Ban/01-Gioi-Thieu/bai.md).
   - Luyện HSG → mở `02-Thuat-Toan`, học một mạch từ Bài 1 (Giới Thiệu)
     đến Bài 41 (Chiến Lược Thi) — 22 bài cơ bản gọn nhẹ nối tiếp
     19 bài thuật toán, không nhảy thư mục.
   - Học một mạch từ đầu đến cuối → mở `04-Full` (đi theo thứ tự
     Phan-1 → Phan-2 → Phan-3).
2. Mỗi bài: đọc kiến thức → chạy thử ví dụ → **tự làm bài tập ít nhất 15 phút**
   trước khi mở đáp án.
3. Mỗi tuần làm lại 1 bài khó nhất đã học để ghi nhớ lâu.

### Giảng dạy

- Dùng `bai.md` làm **giáo án** trên lớp (mục tiêu → kiến thức → ví dụ → lỗi
  thường gặp → tóm tắt có sẵn).
- Phần 🧩 Bài tập làm **bài tập về nhà**, phần ✅ Đáp án để kiểm tra.
- Mục 🧪 Kiểm tra nhanh cuối mỗi bài dùng để hỏi đáp tại lớp.

---

## 💻 Yêu cầu cài đặt

- **Python 3.9+**: tải tại [python.org/downloads](https://www.python.org/downloads/)
  (Windows nhớ tích `Add Python to PATH`). Chi tiết:
  [Bài 2 — Cài Đặt Python](01-Co-Ban/02-Cai-Dat-Python/bai.md).
- **VS Code** + extension Python (Microsoft). Chi tiết:
  [Bài 3 — VSCode](01-Co-Ban/03-VSCode/bai.md).
- Chưa cài đặt vẫn học được ngay trên [Replit](https://replit.com/),
  [Google Colab](https://colab.research.google.com/),
  [Python Tutor](https://pythontutor.com/).

Kiểm tra sau khi cài:

```bash
python --version
```

---

## 🛠️ Kiểm tra chất lượng (dành cho người bảo trì)

```bash
python tools/validate.py
```

Script kiểm tra: link tương đối hỏng, tham chiếu file cũ đã xóa
(`bai_giang.md` / `bai_tap.md` / `dap_an.md`), mỗi thư mục bài học có đúng
1 file `bai.md`, khối code fence và `<details>` cân bằng, tiêu đề H1 đúng
định dạng.

---

## 🤝 Đóng góp

Rất hoan nghênh mọi đóng góp:

- 🐛 Báo lỗi / sửa code mẫu sai
- 💡 Đề xuất bài học, ví dụ mới
- 📝 Sửa chính tả / thuật ngữ
- ✨ Cải thiện đáp án, gợi ý bài tập

Cách thực hiện:

1. **Fork** repository này.
2. Tạo nhánh mới: `git checkout -b content/ten-bai-hoc`
3. Commit rõ ràng: `git commit -m "content: ..."`
4. Push và mở **Pull Request**.

> Nội dung đóng góp đúng chuẩn: Markdown, tiếng Việt có dấu, code chạy được,
> đáp án giải thích lý do (không chỉ đưa code).

---

## 📝 Giấy phép (MIT License)

Bộ giáo trình được phát hành theo giấy phép **MIT** — tự do sử dụng, chỉnh sửa,
phân phối cho mục đích học tập và giảng dạy, với điều kiện **giữ nguyên thông
tin tác giả/nguồn**.

```text
MIT License

Copyright (c) 2026 HyperHub Python

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## ⭐ Ủng hộ

Nếu thấy khóa học hữu ích, hãy:

- Cho repository một ⭐ **ngôi sao** trên GitHub.
- Chia sẻ cho bạn bè cùng học.
- Tham gia **server Discord của HyperHub**: https://discord.gg/nEaFUUBMAM

**Chúc bạn học vui và trở thành một lập trình viên Python giỏi! 🎉**
