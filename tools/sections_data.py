# -*- coding: utf-8 -*-
"""Dữ liệu cho tools/add_sections.py — thẻ nhóm + bài tập về nhà + tra cứu nhanh.

Quy ước: mỗi mục là folder bài (vd "b12-List"). Có thể thêm/sửa dần theo đợt —
script tự bỏ qua mục đã có sẵn (idempotent). Viết theo "bản thô": gọn, đúng, dễ hiểu.
"""

DATA_1 = {
    # ================= b01–b11 =================
    "b01-Gioi-Thieu": {
        "tag": "Nhập môn · Giới thiệu Python",
        "homework": (
            "1. **Tự giới thiệu bằng code:** viết 5 lệnh `print()` in thông tin của bạn (tên, tuổi, lớp, sở thích, mục tiêu) — mỗi thông tin một dòng.\n"
            "2. **Phá lỗi:** tự tạo 3 lỗi cú pháp khác nhau (thiếu ngoặc, thiếu nháy, sai hoa/thường), chạy thử để xem thông báo lỗi, rồi sửa từng lỗi.\n"
            "3. **Vẽ tay:** vẽ sơ đồ \"Python là gì / dùng ở đâu\" với 5 nhánh ứng dụng (AI, Web, dữ liệu, tự động hóa, game)."
        ),
    },
    "b02-Cai-Dat-Python": {
        "tag": "Nhập môn · Cài đặt môi trường",
        "homework": (
            "1. **Cài đặt & kiểm tra:** cài Python + VS Code theo bài; chạy `python --version` rồi ghi lại kết quả vào vở.\n"
            "2. **Chạy hai nơi:** chạy cùng một file `hello.py` bằng cửa sổ terminal và bằng nút Run của VS Code — ghi lại 2 cách.\n"
            "3. **Pip cơ bản:** chạy `pip list` và kể tên 5 thư viện bạn nhận ra (đọc hiểu tên là đủ)."
        ),
    },
    "b03-Bien": {
        "tag": "Cú pháp cơ bản · Biến & gán giá trị",
        "homework": (
            "1. **Hộ chiếu biến:** tạo 6 biến lưu thông tin cá nhân (đặt tên `snake_case` đúng chuẩn), in thành bảng thẳng cột.\n"
            "2. **Đổi nhãn:** viết chương trình hoán đổi 2 biến bằng `a, b = b, a` — giải thích 1 câu vì sao không cần biến tạm.\n"
            "3. **Săn lỗi:** đọc lại code đã viết, tìm 3 tên biến \"chưa đẹp\" và đổi tên lại cho rõ nghĩa."
        ),
        "tracuu_title": "Quy tắc đặt tên & gán biến",
        "tracuu": (
            "| Cú pháp | Ý nghĩa | Ví dụ |\n"
            "|---|---|---|\n"
            "| `ten_bien = giá_trị` | Gán (tạo nhãn) | `diem = 8.5` |\n"
            "| `a, b = 1, 2` | Gán nhiều biến một dòng | `x, y = 3, 4` |\n"
            "| `a, b = b, a` | Hoán đổi không cần biến tạm | `a, b = b, a` |\n"
            "| `del ten_bien` | Xóa biến | `del tam` |\n"
            "| `type(x)` | Xem kiểu dữ liệu | `type(8.5)` → `float` |\n"
            "| `id(x)` | Xem \"địa chỉ\" đối tượng | `id(a) == id(b)` |\n\n"
            "**Quy tắc đặt tên:** chữ cái/số/`_`; không bắt đầu bằng số; không trùng từ khóa (`if`, `for`...); phân biệt hoa–thường; "
            "quy ước viết thường + `_` (snake_case)."
        ),
    },
    "b04-Kieu-Du-Lieu": {
        "tag": "Cú pháp cơ bản · Kiểu dữ liệu & ép kiểu",
        "homework": (
            "1. **Thẻ căn cước kiểu:** cho 8 giá trị khác loại (số, chuỗi, bool...), đoán `type()` từng giá trị trước khi chạy và đối chiếu.\n"
            "2. **Trạm ép kiểu:** nhập điểm dạng chuỗi → ép `float` → in điểm +2; thử nhập chữ để xem lỗi `ValueError` thực tế.\n"
            "3. **Ngân hàng mini:** tính tổng tiền 3 món (float), làm tròn 2 chữ số thập phân, đối chiếu kết quả bằng tay."
        ),
        "tracuu_title": "Ép kiểu & hàm chuyển đổi kiểu",
        "tracuu": (
            "| Hàm | Việc | Ví dụ | Ghi chú |\n"
            "|---|---|---|---|\n"
            "| `int(x)` | Sang số nguyên | `int(\"7\")` → `7`; `int(3.9)` → `3` | Cắt phần thập phân |\n"
            "| `float(x)` | Sang số thực | `float(\"7.5\")` → `7.5` | |\n"
            "| `str(x)` | Sang chuỗi | `str(42)` → `\"42\"` | Dùng để nối chuỗi |\n"
            "| `bool(x)` | Sang đúng/sai | `bool(0)` → `False` | 0, \"\", [], None → False |\n"
            "| `type(x)` | Xem kiểu | `type(5)` → `int` | Chỉ đọc, không đổi |\n"
            "| `round(x, n)` | Làm tròn n chữ số | `round(3.14159, 2)` → `3.14` | |\n"
            "| `abs(x)` | Trị tuyệt đối | `abs(-5)` → `5` | |\n"
            "| `chr(n)` / `ord(c)` | Số ↔ ký tự | `ord(\"A\")` → `65` | Bảng mã Unicode |"
        ),
    },
    "b05-Toan-Tu": {
        "tag": "Cú pháp cơ bản · Toán tử",
        "homework": (
            "1. **Máy tính 6 phép:** nhập 2 số, in kết quả của `+ - * / // % **` — mỗi kết quả có nhãn.\n"
            "2. **Biểu thức đời thực:** viết 3 biểu thức tính tiền (điện, nước, gửi xe) — ghi rõ thứ tự ưu tiên từng biểu thức.\n"
            "3. **Săn bẫy:** chạy thử `0.1 + 0.2` và so với `0.3`; ghi lại nhận xét ngắn (số thực trong máy tính)."
        ),
        "tracuu_title": "Toàn bộ toán tử trong Python",
        "tracuu": (
            "| Nhóm | Toán tử | Ví dụ | Ghi chú |\n"
            "|---|---|---|---|\n"
            "| Số học | `+ - * /` | `7 / 2` → `3.5` | `/` luôn ra `float` |\n"
            "| Số học | `// % **` | `7 // 2`→`3`; `7 % 2`→`1`; `2 ** 10`→`1024` | chia nguyên, dư, lũy thừa |\n"
            "| So sánh | `== != < <= > >=` | `3 != 4` → `True` | Trả về `bool` |\n"
            "| Logic | `and or not` | `a > 0 and a < 10` | Học đủ bảng chân trị |\n"
            "| Gán kết hợp | `+= -= *= //= %=` | `x += 1` | Ngắn cho `x = x + 1` |\n"
            "| `in` | Kiểm tra thuộc | `\"a\" in \"cat\"` → `True` | Chuỗi, list, dict... |\n"
            "| `is` | Cùng đối tượng? | `a is b` | Khác `==` (so giá trị) |\n\n"
            "**Thứ tự ưu tiên (cao → thấp):** `**` → `* / // %` → `+ -` → so sánh → `not` → `and` → `or`. "
            "Không chắc thì cứ thêm ngoặc tròn."
        ),
    },
    "b06-Input-Output": {
        "tag": "Cú pháp cơ bản · Nhập & xuất dữ liệu",
        "homework": (
            "1. **Phiếu nhập xinh đẹp:** nhập tên + tuổi + lớp, in lại theo mẫu thẳng cột bằng f-string.\n"
            "2. **Máy tính lương:** nhập lương/giờ và số giờ làm, in lương gộp và lương sau thuế 10% (2 chữ số thập phân).\n"
            "3. **Sáng tạo:** tự thiết kế \"vé xem phim\" hoặc \"hóa đơn\" in ra màn hình — đủ các cột căn chỉnh bằng format."
        ),
        "tracuu_title": "print, input và định dạng f-string",
        "tracuu": (
            "| Cú pháp | Việc | Ví dụ |\n"
            "|---|---|---|\n"
            "| `print(a, b, sep=\"-\")` | In nhiều giá trị, ngăn cách tùy chọn | `print(1, 2, sep=\"-\")` → `1-2` |\n"
            "| `print(x, end=\" \")` | Không xuống dòng cuối | In dãy trên một hàng |\n"
            "| `input(\"nhãn\")` | Nhập từ bàn phím (luôn là chuỗi) | `tuoi = int(input(\"Tuổi: \"))` |\n"
            "| `f\"{x}\"` | Chèn giá trị vào chuỗi | `f\"Diem: {diem}\"` |\n"
            "| `f\"{x:.2f}\"` | 2 chữ số thập phân | `f\"{3.14159:.2f}\"` → `3.14` |\n"
            "| `f\"{x:>8}\"` / `f\"{x:<8}\"` | Căn phải / trái, rộng 8 | Bảng thẳng cột |\n"
            "| `f\"{x:^8}\"` | Căn giữa | |\n"
            "| `f\"{x:,}\"` | Dấu phẩy nghìn | `f\"{1000000:,}\"` → `1,000,000` |\n"
            "| `\\n \\t` | Xuống dòng / tab | `print(\"a\\nb\")` |"
        ),
    },
    "b07-Cau-Lenh-If": {
        "tag": "Cú pháp cơ bản · Rẽ nhánh if/elif/else",
        "homework": (
            "1. **Xếp loại cả lớp:** nhập điểm (0–10), xếp loại 5 mức bằng `elif` đúng thứ tự (kiểm tra cao → thấp).\n"
            "2. **Cây ATM 2 bước:** kiểm tra số dư đủ mới cho rút tiền; chặn số âm và dữ liệu không phải số.\n"
            "3. **Nhật ký if:** ghi lại 3 tình huống đời thực mà bạn từng ra quyết định kiểu if (rất ngắn gọn)."
        ),
        "tracuu_title": "Rẽ nhánh — cú pháp & mẹo",
        "tracuu": (
            "| Cú pháp | Ý nghĩa | Ví dụ |\n"
            "|---|---|---|\n"
            "| `if đk:` | Chạy khi đúng | `if x > 0:` |\n"
            "| `elif đk:` | Kiểm tra tiếp | Nhiều mức xếp loại |\n"
            "| `else:` | Còn lại | Không cần điều kiện |\n"
            "| Giá trị đúng/sai | Bảng truthiness | `if ds:` — list rỗng là sai |\n"
            "| Ngoặc đơn dư | OK nhưng không cần | `if (x > 0):` |\n"
            "| Chuỗi so sánh | Theo từ điển | `\"a\" < \"b\"` → `True` |\n"
            "| So sánh chuỗi (chained) | `a < b < c` | `0 < x < 10` |\n"
            "| Ba ngôi một dòng | `X if đk else Y` | `\"dương\" if x > 0 else \"âm\"` |"
        ),
    },
    "b08-Vong-Lap-For": {
        "tag": "Vòng lặp · for và range",
        "homework": (
            "1. **Bảng cửu chương cá nhân:** in bảng cửu chương của số bạn chọn — mỗi dòng một phép tính.\n"
            "2. **Thống kê điểm:** nhập n điểm vào list, in lớn nhất / nhỏ nhất / trung bình chỉ với các vòng lặp.\n"
            "3. **Kim tự tháp sao:** in tam giác sao `n` tầng (gợi ý: tầng thứ i có 2i−1 dấu sao)."
        ),
        "tracuu_title": "range, enumerate, zip & điều khiển vòng lặp",
        "tracuu": (
            "| Cú pháp | Việc | Ví dụ kết quả |\n"
            "|---|---|---|\n"
            "| `range(n)` | 0..n−1 | `range(3)` → 0,1,2 |\n"
            "| `range(a, b)` | a..b−1 | `range(2,5)` → 2,3,4 |\n"
            "| `range(a, b, s)` | Bước nhảy s | `range(0,10,2)` → 0,2,4,6,8 |\n"
            "| `range(n, 0, -1)` | Đếm ngược | n..1 |\n"
            "| `for x in ds:` | Duyệt giá trị | |\n"
            "| `for i, x in enumerate(ds):` | Kèm chỉ số | `enumerate(ds, start=1)` bắt đầu từ 1 |\n"
            "| `for a, b in zip(d1, d2):` | Duyệt song song | |\n"
            "| `break` | Thoát vòng lặp | Tìm thấy là dừng |\n"
            "| `continue` | Bỏ qua lượt này | |\n"
            "| `for ... else:` | else chạy khi KHÔNG break | Mẫu \"tìm kiếm thất bại\" |"
        ),
    },
    "b09-Vong-Lap-While": {
        "tag": "Vòng lặp · while",
        "homework": (
            "1. **Đoán số:** máy chọn số 1..100, bạn đoán — `while` + gợi ý lớn/nhỏ + đếm số lần đoán.\n"
            "2. **Nhập đến khi hợp lệ:** yêu cầu nhập số dương; nhập sai (chữ/số âm) thì bắt nhập lại.\n"
            "3. **Tự phân tích:** chọn 2 vòng `while` trong bài, ghi ra giấy 3 thành phần: khởi tạo — điều kiện — cập nhật."
        ),
        "tracuu_title": "Khuôn mẫu while & so sánh for/while",
        "tracuu": (
            "| Khuôn mẫu | Ví dụ | Dùng khi |\n"
            "|---|---|---|\n"
            "| Đếm ngược | `while n > 0: n -= 1` | Biết điều kiện dừng theo giá trị |\n"
            "| Nhập đến khi hợp lệ | `while True: x = input(...); if ok: break` | Kiểm tra dữ liệu người dùng |\n"
            "| Cờ (flag) | `while chua_xong:` | Điều kiện phức tạp |\n"
            "| Menu | `while True:` + `break` khi chọn 0 | Ứng dụng dạng menu |\n"
            "| `while ... else:` | else chạy khi không gặp `break` | Tìm kiếm thất bại |\n"
            "| Tránh vô hạn | Luôn đảm bảo \"3 bộ ba\": khởi tạo, điều kiện, cập nhật | Bắt buộc |\n\n"
            "**So sánh:** `for` khi biết trước số vòng/duyệt dãy — `while` khi lặp đến khi điều kiện sai. "
            "Trong `while`, đừng quên cập nhật biến điều khiển!"
        ),
    },
    "b10-Ham": {
        "tag": "Hàm · Xây dựng và gọi hàm",
        "homework": (
            "1. **Tủ hàm cá nhân:** viết 5 hàm tiện ích (`dien_tich_hcn`, `chu_vi_hcn`, `tb_3_so`, `dao_chuoi`, `la_chan`) — mỗi hàm 1–3 dòng.\n"
            "2. **Refactor:** lấy một đoạn code cũ 15–20 dòng, tách thành 2–3 hàm có tên rõ nghĩa, chạy lại cho đúng kết quả.\n"
            "3. **Docstring:** viết docstring (Input/Output) cho 3 hàm ở bài tập 1 theo mẫu trong bài."
        ),
        "tracuu_title": "Định nghĩa hàm — tham số & trả về",
        "tracuu": (
            "| Cú pháp | Ý nghĩa | Ví dụ |\n"
            "|---|---|---|\n"
            "| `def f(x):` | Hàm 1 tham số | `def binh(a): return a*a` |\n"
            "| `def f(x=5):` | Tham số mặc định | `def chao(ten=\"bạn\"):` |\n"
            "| `def f(*args):` | Nhận N tham số vị trí | `def tong(*so): sum(so)` |\n"
            "| `def f(**kwargs):` | Nhận N tham số tên | `def in_ra(**kv):` |\n"
            "| `return x` | Trả giá trị (kết thúc hàm) | `return a + b` |\n"
            "| `return a, b` | Trả nhiều giá trị (tuple) | `return min(a), max(a)` |\n"
            "| Không `return` | Trả `None` | Hàm chỉ in ra |\n"
            "| `\"\"\"Docstring\"\"\"` | Mô tả hàm | Đặt ngay sau `def` |\n"
            "| Gọi hàm | `f(1, 2)` hoặc `f(x=1)` | Kiểm tra trước khi tin |"
        ),
    },
    "b11-Scope": {
        "tag": "Hàm · Phạm vi biến (LEGB)",
        "homework": (
            "1. **Sơ đồ LEGB:** vẽ 4 tầng Local → Enclosing → Global → Built-in; đặt 1 biến ví dụ vào mỗi tầng.\n"
            "2. **Săn bug scope:** cố tình tạo lỗi `UnboundLocalError` rồi sửa — ghi chú vì sao lỗi đó xuất hiện.\n"
            "3. **Tranh luận ngắn:** viết 5–7 câu \"vì sao nên hạn chế `global`\" kèm ví dụ cụ thể của bạn."
        ),
        "tracuu_title": "Phạm vi biến — quy tắc hoạt động",
        "tracuu": (
            "| Tình huống | Quy tắc | Ví dụ |\n"
            "|---|---|---|\n"
            "| Đọc biến ngoài hàm | OK | `print(x)` trong hàm |\n"
            "| Gán trùng tên trong hàm | Tạo biến LOCAL mới | `x = 5` trong hàm không đổi x ngoài |\n"
            "| Đọc + gán cùng tên | Lỗi `UnboundLocalError` | Cần `global` hoặc đổi cách viết |\n"
            "| Sửa biến toàn cục | `global x` (hạn chế dùng) | Khai báo 1 lần trong hàm |\n"
            "| Hàm lồng nhau | `nonlocal x` | Sửa biến ở hàm cha |\n"
            "| Tham số hàm | Thực chất là biến local | Mọi gán trong hàm là cục bộ |\n\n"
            "**Cách viết an toàn:** coi hàm như \"cỗ máy\" — nhận tham số, `return` kết quả; hạn chế đụng biến ngoài."
        ),
    },

    # ================= b12–b16: CẤU TRÚC DỮ LIỆU =================
    "b12-List": {
        "tag": "Cấu trúc dữ liệu · List (danh sách)",
        "homework": (
            "1. **Quản lý điểm kiểm tra:** tạo list 8 điểm, thêm 1 đầu + 1 cuối, xóa 1 điểm thấp nhất, sắp giảm dần, in ra 3 cao nhất.\n"
            "2. **Săn lỗi tham chiếu:** tạo hai list `a`, `b = a`, sửa `b` rồi in `a` — giải thích 1 câu; sau đó sửa lại bằng `copy()`.\n"
            "3. **Sổ tay nhanh:** viết 5 dòng chú thích \"khi nào dùng gì\": `append` vs `extend`, `sort` vs `sorted`, `pop` vs `del`, `remove` vs `pop`."
        ),
        "tracuu_title": "Toàn bộ phương thức & thao tác của List",
        "tracuu": (
            "| # | Phương thức / thao tác | Việc nó làm | Ví dụ |\n"
            "|---|---|---|---|\n"
            "| 1 | `append(x)` | Thêm x vào cuối | `[1,2].append(3)` → `[1,2,3]` |\n"
            "| 2 | `extend(ds)` | Nối cả list khác vào cuối | `[1,2].extend([3,4])` |\n"
            "| 3 | `insert(i, x)` | Chèn x vào vị trí i | `[1,3].insert(1, 2)` → `[1,2,3]` |\n"
            "| 4 | `remove(x)` | Xóa phần tử đầu bằng x (lỗi nếu không có) | `[1,2].remove(2)` |\n"
            "| 5 | `pop(i=-1)` | Xóa & TRẢ VỀ phần tử vị trí i | `[1,2].pop()` → `2` |\n"
            "| 6 | `clear()` | Xóa sạch | `[1,2].clear()` → `[]` |\n"
            "| 7 | `index(x)` | Vị trí đầu tiên bằng x (lỗi nếu không có) | `[5,6,7].index(6)` → `1` |\n"
            "| 8 | `count(x)` | Đếm số lần xuất hiện | `[1,1,2].count(1)` → `2` |\n"
            "| 9 | `sort(key=, reverse=)` | Sắp tại chỗ (đổi gốc) | `[3,1,2].sort()` |\n"
            "| 10 | `reverse()` | Đảo tại chỗ | `[1,2].reverse()` → `[2,1]` |\n"
            "| 11 | `copy()` | Bản sao nông | `b = a.copy()` |\n"
            "| 12 | `ds[i]` / `ds[a:b:c]` | Truy cập / cắt (tạo list mới) | `ds[-1]`, `ds[::-1]` |\n"
            "| 13 | `x in ds` | Kiểm tra thuộc (O(n)) | `3 in [1,2,3]` → `True` |\n"
            "| 14 | `a + b` / `a * n` | Nối / lặp list | `[1]*3` → `[1,1,1]` |\n"
            "| 15 | `len/min/max/sum` | Thống kê nhanh | `sum([1,2,3])` → `6` |\n"
            "| 16 | `sorted(ds, key=, reverse=)` | Bản sắp mới (giữ gốc) | `sorted(ds)` |\n"
            "| 17 | `enumerate(ds)` / `zip(d1,d2)` | Duyệt kèm chỉ số / song song | |\n\n"
            "**Ghi nhớ:** list có thứ tự, cho sửa, cho trùng; `sort()` trả `None` (đổi gốc!), `sorted()` trả list mới; "
            "copy an toàn bằng `ds.copy()` / `list(ds)` / `ds[:]` — ĐỪNG dùng `b = a`."
        ),
    },
    "b13-Tuple": {
        "tag": "Cấu trúc dữ liệu · Tuple (bộ dữ liệu)",
        "homework": (
            "1. **Hộp quà tuple:** tạo tuple tọa độ 5 điểm; in điểm đầu, cuối, cắt 2 điểm giữa bằng slice.\n"
            "2. **Mở gói:** viết hàm trả `(min, max, tb)` của một list — gọi và nhận cả ba bằng một dòng.\n"
            "3. **Bảng so sánh:** kẻ bảng 2 cột list vs tuple: sửa được? tốc độ? dùng khi nào? — điền từ kiến thức bài."
        ),
        "tracuu_title": "Phương thức của Tuple & mở gói",
        "tracuu": (
            "| Cú pháp | Việc | Ví dụ |\n"
            "|---|---|---|\n"
            "| `(a, b, c)` | Tạo tuple | `diem = (8, 9, 7)` |\n"
            "| `t[i]` / `t[a:b]` | Truy cập / cắt | `diem[0]`, `diem[:2]` |\n"
            "| `x in t` | Kiểm tra thuộc | `9 in diem` |\n"
            "| `t.count(x)` | Đếm số lần | `(1,1,2).count(1)` → `2` |\n"
            "| `t.index(x)` | Vị trí đầu tiên | `(5,6).index(6)` → `1` |\n"
            "| `a, b = t` | Mở gói (unpack) | `x, y = (3, 4)` |\n"
            "| `a, *phan_con = t` | Mở gói một phần | `dau, *giua, cuoi = t` |\n"
            "| `return a, b` | Hàm trả nhiều giá trị (tuple) | `return min(ds), max(ds)` |\n"
            "| `tuple(ds)` | List → tuple | `tuple([1,2])` |\n\n"
            "**Vì sao dùng tuple:** bất biến (an toàn), nhanh hơn list chút, làm được **khóa dict** (list thì không), "
            "tự nhiên cho \"bộ cố định\" (tọa độ, RGB, ngày-tháng-năm, kết quả trả về nhiều giá trị)."
        ),
    },
    "b14-Set": {
        "tag": "Cấu trúc dữ liệu · Set (tập hợp)",
        "homework": (
            "1. **Lọc trùng lớp học:** cho list 20 tên (có lặp), in danh sách khách mời KHÔNG trùng theo 2 cách: `set()` và vòng lặp + `in`.\n"
            "2. **Điểm danh:** hai set A (sáng), B (chiều) — in: đi cả hai buổi, chỉ sáng, chỉ chiều, tổng số bạn (4 phép toán tập hợp).\n"
            "3. **Nhật ký giao thông:** đếm số biển số xe KHÁC NHAU trong ngày từ một list biển số (dùng set, 2 dòng)."
        ),
        "tracuu_title": "Toàn bộ phương thức & phép toán của Set",
        "tracuu": (
            "| # | Phương thức / phép toán | Việc | Ví dụ |\n"
            "|---|---|---|---|\n"
            "| 1 | `add(x)` | Thêm (bỏ trùng tự động) | `{1,2}.add(3)` |\n"
            "| 2 | `remove(x)` | Xóa x — LỖI nếu không có | `{1}.remove(1)` |\n"
            "| 3 | `discard(x)` | Xóa x — KHÔNG lỗi nếu thiếu | `{1}.discard(5)` |\n"
            "| 4 | `pop()` | Xóa & trả 1 phần tử bất kỳ | `{1,2}.pop()` |\n"
            "| 5 | `clear()` | Xóa hết | |\n"
            "| 6 | `A \\| B` / `A.union(B)` | Hợp | `{1,2} \\| {2,3}` → `{1,2,3}` |\n"
            "| 7 | `A & B` / `A.intersection(B)` | Giao | `{1,2} & {2,3}` → `{2}` |\n"
            "| 8 | `A - B` / `A.difference(B)` | Hiệu (có trong A, không trong B) | `{1,2} - {2,3}` → `{1}` |\n"
            "| 9 | `A ^ B` / `symmetric_difference` | Hiệu đối xứng | `{1,2} ^ {2,3}` → `{1,3}` |\n"
            "| 10 | `A.update(B)` | Thêm cả B vào A | |\n"
            "| 11 | `A.issubset(B)` / `A <= B` | A nằm trong B? | |\n"
            "| 12 | `A.issuperset(B)` / `A >= B` | A chứa B? | |\n"
            "| 13 | `A.isdisjoint(B)` | Rời nhau? | |\n"
            "| 14 | `x in A` | Kiểm tra thuộc — O(1) | `5 in {1,5}` |\n"
            "| 15 | `len(A)` | Số phần tử | |\n"
            "| 16 | `frozenset(A)` | Tập hợp bất biến (làm khóa được) | |\n\n"
            "**Ghi nhớ:** set KHÔNG có thứ tự, KHÔNG trùng, tra cứu O(1); `{}` trống là **dict** — set rỗng dùng `set()`."
        ),
    },
    "b15-Dictionary": {
        "tag": "Cấu trúc dữ liệu · Dictionary (từ điển)",
        "homework": (
            "1. **Sổ liên lạc:** tạo dict 5 bạn → số điện thoại; tra 1 tên, thêm 1 bạn, xóa 1 bạn, in tất cả theo `.items()`.\n"
            "2. **Điểm môn học:** dict môn → điểm; tính điểm trung bình, in môn cao nhất (dùng `max` với `key`).\n"
            "3. **Săn KeyError:** thử `d[\"khong_co\"]` thấy lỗi → sửa bằng `.get()` và bằng `in` — ghi chú 2 cách."
        ),
        "tracuu_title": "Toàn bộ phương thức & thao tác của Dictionary",
        "tracuu": (
            "| # | Phương thức / thao tác | Việc | Ví dụ |\n"
            "|---|---|---|---|\n"
            "| 1 | `d[k]` | Đọc — LỖI `KeyError` nếu thiếu k | |\n"
            "| 2 | `d.get(k, mac_dinh)` | Đọc an toàn (thiếu → None/mặc định) | `d.get(\"x\", 0)` |\n"
            "| 3 | `d[k] = v` | Thêm mới hoặc sửa | |\n"
            "| 4 | `keys()` / `values()` / `items()` | Duyệt khóa / giá trị / cả cặp | `for k, v in d.items():` |\n"
            "| 5 | `update(d2)` | Gộp d2 vào d (đè trùng khóa) | `d.update({\"a\": 1})` |\n"
            "| 6 | `pop(k)` | Xóa & trả giá trị | |\n"
            "| 7 | `popitem()` | Xóa & trả cặp cuối (3.7+) | |\n"
            "| 8 | `setdefault(k, v)` | Có thì trả; chưa có thì đặt v | Đếm nhóm gọn |\n"
            "| 9 | `fromkeys(ds, v)` | Tạo dict từ danh sách khóa | `dict.fromkeys(\"abc\", 0)` |\n"
            "| 10 | `k in d` | Kiểm tra khóa — O(1) | |\n"
            "| 11 | `del d[k]` | Xóa khóa | |\n"
            "| 12 | `len(d)` / `d.copy()` / `d.clear()` | Đếm / sao chép / xóa sạch | |\n"
            "| 13 | `{x: f(x) for x in ds}` | Dict comprehension | `{x: x*x for x in range(3)}` |\n\n"
            "**Mẫu vàng:** đếm `d[x] = d.get(x, 0) + 1`; gom nhóm `d.setdefault(khoa, []).append(x)`; "
            "tra cứu O(1); khóa phải **bất biến** (str, số, tuple)."
        ),
    },
    "b16-String": {
        "tag": "Cấu trúc dữ liệu · String (chuỗi)",
        "homework": (
            "1. **Hộ chiếu chuỗi:** nhập họ tên đầy đủ dạng \"nguyen  van AN\", in ra tên chuẩn hóa \"Nguyen Van An\" (dùng split + title/join).\n"
            "2. **Thống kê câu:** đếm số từ, số nguyên âm, in câu đảo ngược `[::-1]`.\n"
            "3. **Mật khẩu vui:** kiểm tra \"mật khẩu\" đủ 8 ký tự, có chữ và số — kết quả ĐẠT/CHƯA ĐẠT (dùng các hàm `is...`)."
        ),
        "tracuu_title": "Toàn bộ phương thức String thường dùng",
        "tracuu": (
            "| # | Phương thức | Việc | Ví dụ |\n"
            "|---|---|---|---|\n"
            "| 1 | `upper()` / `lower()` | HOA / thường | `\"An\".upper()` → `\"AN\"` |\n"
            "| 2 | `strip()` | Bỏ khoảng trắng 2 đầu | `\"  a  \".strip()` → `\"a\"` |\n"
            "| 3 | `lstrip()` / `rstrip()` | Bỏ trái / phải | |\n"
            "| 4 | `split(sep)` | Cắt thành list | `\"a,b\".split(\",\")` → `['a','b']` |\n"
            "| 5 | `\"sep\".join(ds)` | Nối list thành chuỗi | `\"-\".join(['a','b'])` → `\"a-b\"` |\n"
            "| 6 | `replace(a, b)` | Thay thế | `\"ana\".replace(\"a\",\"o\")` |\n"
            "| 7 | `find(x)` / `rfind(x)` | Vị trí đầu/cuối (−1 nếu thiếu) | |\n"
            "| 8 | `x in s` | Chứa? | `\"an\" in \"banana\"` |\n"
            "| 9 | `count(x)` | Đếm | `\"banana\".count(\"an\")` → `2` |\n"
            "| 10 | `startswith(x)` / `endswith(x)` | Bắt đầu / kết thúc | Lọc file `.py` |\n"
            "| 11 | `isdigit()` / `isalpha()` / `isspace()` | Toàn số / chữ / khoảng trắng? | Kiểm tra nhập liệu |\n"
            "| 12 | `title()` / `capitalize()` | Viết hoa đầu từ / đầu câu | |\n"
            "| 13 | `zfill(n)` | Đệm 0 bên trái | `\"7\".zfill(3)` → `\"007\"` |\n"
            "| 14 | `ljust(n)` / `rjust(n)` / `center(n)` | Căn trái/phải/giữa | |\n"
            "| 15 | `s[i]` / `s[a:b:c]` | Truy cập / cắt (chuỗi mới) | `s[::-1]` đảo |\n"
            "| 16 | `len(s)` | Độ dài | |\n"
            "| 17 | `splitlines()` | Cắt theo dòng | |\n"
            "| 18 | `ord(c)` / `chr(n)` | Ký tự ↔ mã | `ord(\"a\")` → `97` |\n\n"
            "**Ghi nhớ:** chuỗi BẤT BIẾN — mọi `replace/upper...` trả chuỗi MỚI (không sửa gốc); muốn sửa thì gán lại."
        ),
    },

    # ================= b17–b23: TỔ CHỨC MÃ & KỸ THUẬT =================
    "b17-Module": {
        "tag": "Tổ chức mã · Module & thư viện chuẩn",
        "homework": (
            "1. **Tủ đồ nghề riêng:** viết `tien_ich.py` chứa 4 hàm tiện ích; tạo file `main.py` import và dùng 3 trong 4 hàm.\n"
            "2. **Khám phá thư viện chuẩn:** dùng `math` tính diện tích hình tròn, `random` chọn 1 bạn trong lớp (giả lập), `datetime` in giờ hiện tại.\n"
            "3. **Ghi nhớ import:** viết 3 kiểu import khác nhau cho cùng thư viện `math` (import / from / alias) — ghi chú khác nhau chỗ nào."
        ),
        "tracuu_title": "Import & các module chuẩn thường dùng",
        "tracuu": (
            "| Cú pháp import | Ví dụ | Ghi chú |\n"
            "|---|---|---|\n"
            "| `import mod` | `import math` → `math.sqrt(9)` | Gọi qua tên module |\n"
            "| `from mod import ten` | `from math import sqrt` → `sqrt(9)` | Gọi trực tiếp |\n"
            "| `import mod as alias` | `import math as m` → `m.sqrt(9)` | Đặt bí danh |\n"
            "| `from mod import *` | — | ❌ hạn chế (rối tên) |\n\n"
            "**Module chuẩn hay dùng:**\n\n"
            "| Module | Hàm hay dùng | Ví dụ |\n"
            "|---|---|---|\n"
            "| `math` | `sqrt, ceil, floor, gcd, pi` | `math.gcd(12, 18)` → `6` |\n"
            "| `random` | `randint, choice, shuffle, random` | `random.randint(1, 6)` xúc xắc |\n"
            "| `datetime` | `datetime.now()` | `now.strftime(\"%d/%m %H:%M\")` |\n"
            "| `os` | `os.path.exists, os.listdir` | Kiểm tra file tồn tại |\n"
            "| `sys` | `sys.exit, sys.setrecursionlimit` | Dùng khi thi HSG |\n\n"
            "**Tự tạo module:** mỗi file `.py` là 1 module; muốn chạy 1 mình được thì bọc `if __name__ == \"__main__\":`."
        ),
    },
    "b18-File": {
        "tag": "Tổ chức mã · Làm việc với file",
        "homework": (
            "1. **Nhật ký học tập:** ghi thêm (mode `a`) một dòng `[ngày] nội dung` mỗi ngày — chạy thử 3 lần.\n"
            "2. **Điểm danh từ file:** tạo `diem.txt` 10 dòng \"tên điểm\", đọc và in tên + điểm TB.\n"
            "3. **Săn lỗi FileNotFoundError:** thử mở file không tồn tại → xem lỗi → sửa bằng `try/except` theo mẫu bài."
        ),
        "tracuu_title": "Mở file & các thao tác đọc/ghi",
        "tracuu": (
            "| Cú pháp | Việc | Ghi chú |\n"
            "|---|---|---|\n"
            "| `open(ten, \"r\")` | Mở đọc | Mode mặc định |\n"
            "| `open(ten, \"w\")` | Mở ghi (XOÁ hết file cũ) | Cẩn thận! |\n"
            "| `open(ten, \"a\")` | Mở ghi nối | Giữ nội dung cũ |\n"
            "| `open(ten, encoding=\"utf-8\")` | Mở với UTF-8 | Bắt buộc với tiếng Việt |\n"
            "| `with open(...) as f:` | Tự đóng file | Luôn dùng cách này |\n"
            "| `f.read()` | Đọc cả file (1 chuỗi) | File nhỏ |\n"
            "| `f.readline()` | Đọc 1 dòng | Vòng lặp đọc từng dòng |\n"
            "| `f.readlines()` | Đọc thành list dòng | File vừa |\n"
            "| `for dong in f:` | Duyệt từng dòng | Tiết kiệm bộ nhớ |\n"
            "| `f.write(s)` / `f.writelines(ds)` | Ghi chuỗi / list | Tự thêm `\\n` nếu cần |\n"
            "| `f.seek(0)` / `f.tell()` | Di chuyển / xem vị trí | |\n"
            "| `try/except FileNotFoundError` | Bắt lỗi file thiếu | Mẫu chuẩn |\n\n"
            "**Ghi nhớ:** luôn `with`; tiếng Việt thì `encoding=\"utf-8\"`; mode `w` xóa sạch file nếu đã tồn tại."
        ),
    },
    "b19-OOP": {
        "tag": "Tổ chức mã · Lập trình hướng đối tượng",
        "homework": (
            "1. **Class Sách:** thuộc tính ten/gia; method `mo_ta()`; tạo 3 sách và in thông tin (có `__str__`).\n"
            "2. **Kế thừa:** class `SachGiaoKhoa(Kế thừa Sach)` thêm `lop`; ghi đè `mo_ta()` — in cho cả 2 loại.\n"
            "3. **Bắt lỗi thiết kế:** thử tạo `Sach` rồi sửa `gia` thành số âm → thêm kiểm tra (raise lỗi hoặc phương thức `giam_gia` an toàn)."
        ),
        "tracuu_title": "OOP — cú pháp & phương thức đặc biệt",
        "tracuu": (
            "| Cú pháp | Việc | Ví dụ |\n"
            "|---|---|---|\n"
            "| `class Ten:` | Tạo lớp | `class Sach:` |\n"
            "| `__init__(self, ...)` | Hàm khởi tạo | Gán thuộc tính bằng `self.` |\n"
            "| `self` | Tham chiếu đối tượng hiện tại | Tham số đầu mọi method |\n"
            "| `def method(self):` | Phương thức | |\n"
            "| `class Con(Cha):` | Kế thừa | |\n"
            "| `super().__init__(...)` | Gọi constructor cha | |\n"
            "| `__str__` / `__repr__` | Chuỗi hiển thị khi in | `print(sach)` |\n"
            "| `__eq__(self, other)` | So sánh `==` | So theo mã |\n"
            "| `__lt__` | So sánh `<` (dùng được với `sorted`) | |\n"
            "| `__len__` | Hỗ trợ `len(obj)` | |\n"
            "| `_ten` / `__ten` | Quy ước nội bộ / che giấu | |\n"
            "| `@property` | Thuộc tính tính toán | `@property def con_lai(self):` |\n"
            "| `@staticmethod` / `@classmethod` | Hàm tĩnh / gắn lớp | |\n\n"
            "**Bốn chữ cái vàng:** đóng gói (gói dữ liệu + hành vi), kế thừa (cha → con), đa hình (cùng lệnh khác hành vi), "
            "trừu tượng (giấu chi tiết)."
        ),
    },
    "b20-Lambda": {
        "tag": "Kỹ thuật Python · Lambda (hàm vô danh)",
        "homework": (
            "1. **Sắp xếp 3 kiểu:** cho list 6 sản phẩm `(ten, gia, so_luong)` — sắp theo giá tăng, giá giảm, rồi theo tên.\n"
            "2. **Lambda cho khóa phụ:** sắp chuỗi theo \"số nguyên âm giảm dần rồi từ điển\" — một dòng `key=lambda`.\n"
            "3. **Chuyển hóa:** viết lại 2 vòng lặp cũ bằng `map`/`filter` + lambda; so sánh độ dài code."
        ),
        "tracuu_title": "Lambda & các hàm bậc cao",
        "tracuu": (
            "| Cú pháp | Việc | Ví dụ |\n"
            "|---|---|---|\n"
            "| `lambda x: biểu_thức` | Hàm vô danh 1 dòng | `lambda x: x * 2` |\n"
            "| `lambda x, y: ...` | Nhiều tham số | `lambda a, b: a + b` |\n"
            "| `sorted(ds, key=lambda x: ...)` | Sắp theo tiêu chí | `key=lambda sp: sp[1]` |\n"
            "| `key=lambda x: (-x[1], x[0])` | Tần suất giảm + tên tăng | Sắp hỗn hợp |\n"
            "| `min(ds, key=lambda ...)` / `max(...)` | Nhỏ/lớn theo tiêu chí | |\n"
            "| `map(f, ds)` | Áp dụng hàm (lazy) | `map(lambda x: x*x, ds)` |\n"
            "| `filter(f, ds)` | Lọc theo hàm | `filter(lambda x: x > 0, ds)` |\n"
            "| `functools.reduce(f, ds)` | Gộp dãy | `reduce(lambda a,b: a+b, ds)` |\n\n"
            "**Ghi nhớ:** lambda = \"công thức nhỏ dùng 1 lần\" — không có `return`, không nhiều lệnh; "
            "thấy lambda dài hơn ~2 phép tính → viết hàm thường cho dễ đọc."
        ),
    },
    "b21-List-Comprehension": {
        "tag": "Kỹ thuật Python · List comprehension",
        "homework": (
            "1. **Chuyển 5 vòng lặp:** lấy 5 vòng lặp for cũ (tạo list), viết lại thành comprehension.\n"
            "2. **Ma trận 3×3:** tạo ma trận bằng lồng comprehension, in đường chéo chính và đường chéo phụ.\n"
            "3. **Lọc nâng cao:** cho list điểm, in danh sách \"Học sinh giỏi\" kèm xếp loại từng bạn — 2 dòng comprehension."
        ),
        "tracuu_title": "Các khuôn mẫu comprehension",
        "tracuu": (
            "| Khuôn mẫu | Cú pháp | Ví dụ |\n"
            "|---|---|---|\n"
            "| Cơ bản | `[f(x) for x in ds]` | `[x*x for x in ds]` |\n"
            "| Lọc | `[x for x in ds if đk]` | `[x for x in ds if x % 2 == 0]` |\n"
            "| If-else | `[A if đk else B for x in ds]` | `[\"chẵn\" if x%2==0 else \"lẻ\" for x in ds]` |\n"
            "| Hai vòng | `[(i, j) for i in a for j in b]` | Bộ đôi từ 2 dãy |\n"
            "| Lồng (ma trận) | `[[0]*n for _ in range(m)]` | ⚠️ Không dùng `[[0]*n]*m` |\n"
            "| Làm phẳng | `[x for hang in mtr for x in hang]` | Ma trận → list |\n"
            "| Dict comp | `{k: v for ...}` | `{x: x*x for x in range(3)}` |\n"
            "| Set comp | `{x for x in ds}` | Lọc trùng |\n"
            "| Generator | `(x*x for x in ds)` | Không lưu list — lười (Bài 22) |\n\n"
            "**Khi nào nên/không nên:** 1 biểu thức đơn giản → dùng; logic 2+ lệnh hoặc khó đọc → quay lại vòng lặp thường."
        ),
    },
    "b22-Generator": {
        "tag": "Kỹ thuật Python · Generator",
        "homework": (
            "1. **Dãy Fibo lười:** viết generator fibonacci không giới hạn; lấy 15 số đầu bằng vòng for.\n"
            "2. **Đọc file khổng lồ:** sinh dữ liệu giả 100.000 dòng ra file rồi \"đọc lười\" từng dòng (không `read()` cả file).\n"
            "3. **Đo lợi ích:** so sánh `list(...)` 10 triệu bình phương vs generator — ghi lại khác biệt bộ nhớ/thời gian."
        ),
        "tracuu_title": "Generator — cú pháp & khuôn mẫu",
        "tracuu": (
            "| Cú pháp | Việc | Ví dụ |\n"
            "|---|---|---|\n"
            "| `yield x` | Sinh từng giá trị | Trong `def` |\n"
            "| `(f(x) for x in ds)` | Generator expression (lười) | `sum(x*x for x in ds)` |\n"
            "| `next(gen)` | Lấy 1 giá trị kế tiếp | Hết → `StopIteration` |\n"
            "| Duyệt `for x in gen:` | Duyệt lười | 1 lần rồi hết! |\n"
            "| `sum/any/all/max/min(gen)` | \"Kéo\" toàn bộ | `any(x < 0 for x in ds)` |\n"
            "| `itertools.islice(gen, n)` | Lấy n phần tử đầu | Vô hạn → cần chặn |\n"
            "| `itertools.count/cycle/chain` | Hộp đồ nghề | Bài 45 |\n\n"
            "**Ghi nhớ:** generator sinh từng giá trị khi cần — O(1) bộ nhớ; "
            "dùng 1 lần rồi cạn (muốn dùng lại phải tạo mới); thay thế tốt cho trung gian khi xử lý dữ liệu lớn."
        ),
    },
    "b23-Regex": {
        "tag": "Kỹ thuật Python · Regex (biểu thức chính quy)",
        "homework": (
            "1. **Sổ lọc dữ liệu:** cho câu lộn xộn \"AN: 038-1234, binh: 091-9999\", trích tất cả số điện thoại dạng `0xx-xxxx` bằng regex.\n"
            "2. **Dọn log:** cho 10 dòng log \"[SỐ] nội dung\", tách riêng số hiệu và nội dung (dùng nhóm đặt tên).\n"
            "3. **Kiểm tra mật khẩu:** viết pattern cho mật khẩu ≥ 8 ký tự, có chữ và số; giải thích từng mảnh pattern của bạn."
        ),
        "tracuu_title": "Regex — cú pháp & hàm thường dùng",
        "tracuu": (
            "| Nhóm | Mẫu | Ý nghĩa | Ví dụ |\n"
            "|---|---|---|---|\n"
            "| Lớp ký tự | `\\d` `\\w` `\\s` `.` | số / chữ+số / trắng / bất kỳ | `\\d+` chuỗi số |\n"
            "| Lớp tùy chọn | `[abc]` `[^abc]` `[a-z]` | thuộc / không thuộc / khoảng | |\n"
            "| Lượng từ | `*` `+` `?` `{m,n}` | 0+ / 1+ / 0-1 / m..n lần | |\n"
            "| Neo | `^` `$` | đầu / cuối | `^0\\d{9}$` số ĐT |\n"
            "| Nhóm | `(...)` `(?P<ten>...)` | nhóm lấy ra / nhóm đặt tên | |\n"
            "| Hoặc | `cat\\|dog` | một trong hai | |\n"
            "| Hàm | `re.search(p, s)` | Tìm khắp chuỗi, trả match đầu | Kiểm tra tồn tại |\n"
            "| Hàm | `re.match / re.fullmatch` | Khớp từ đầu / khớp trọn | |\n"
            "| Hàm | `re.findall(p, s)` | List mọi kết quả khớp nhóm | Trích số ĐT |\n"
            "| Hàm | `re.sub(p, thay, s)` | Thay thế | Dọn ký tự lạ |\n"
            "| Hàm | `re.split(p, s)` | Cắt theo mẫu | Cắt đa dấu |\n\n"
            "**Ghi nhớ:** luôn dùng **raw string** `r\"...\"`; lượng từ mặc định tham lam (greedy) — thêm `?` để lười; "
            "`flags=re.IGNORECASE` bỏ phân biệt hoa thường."
        ),
    },

    # ================= b24–b35: THUẬT TOÁN =================
    "b24-Tu-Duy-Thuat-Toan": {
        "tag": "Nhập môn thuật toán · Tư duy & quy trình",
        "homework": (
            "1. **Giải 3 đề bằng quy trình 5 bước:** chọn 3 bài dễ bất kỳ, viết đủ: Input/Output/Ràng buộc/Ví dụ/Biên — CHƯA cần code.\n"
            "2. **Sổ tay phản ví dụ:** nghĩ ra 5 dữ liệu \"quái\" để phá code ẩu (n = 1, trùng nhau, âm, rỗng, lớn bất thường).\n"
            "3. **Dịch đề:** lấy 1 đề có câu chuyện dài, tóm thành 3 dòng: cho gì — hỏi gì — ràng buộc gì."
        ),
        "tracuu_title": "Checklist đọc đề & chọn hướng giải",
        "tracuu": (
            "| Bước | Câu hỏi tự hỏi | Ví dụ |\n"
            "|---|---|---|\n"
            "| 1. Input | Dữ liệu gì, định dạng nào, đọc từ đâu? | Dòng đầu n, dòng sau n số |\n"
            "| 2. Output | In gì, đúng định dạng? | Một số nguyên trên dòng riêng |\n"
            "| 3. Ràng buộc | `n` tối đa? giới hạn thời gian? | n ≤ 10⁵ → nghĩ O(n log n) |\n"
            "| 4. Ví dụ | Chạy tay ví dụ xác nhận hiểu đề | Vẽ bảng nhỏ |\n"
            "| 5. Biên | n = 0/1? trùng? âm? rỗng? | 5 loại biên chuẩn |\n\n"
            "**Nhận diện mẫu nhanh:** \"cặp i<j\" → hai vòng/dict; \"đoạn liên tiếp\" → cửa sổ/tiền tố; "
            "\"tối ưu lựa chọn\" → tham lam/DP; \"nhỏ nhất dài nhất\" → nhị phân đáp số; \"quan hệ/lưới\" → đồ thị."
        ),
    },
    "b25-Do-Phuc-Tap": {
        "tag": "Nhập môn thuật toán · Độ phức tạp",
        "homework": (
            "1. **Đo thật:** chạy 4 đoạn code O(n), O(n²), O(n log n), O(log n) với n tăng dần — bảng thời gian thực tế của máy bạn.\n"
            "2. **Đọc ràng buộc:** sưu tầm 5 đề (sách mạng), ghi lại chỉ `n` tối đa — đoán độ phức tạp \"sống sót\" cho từng đề.\n"
            "3. **Săn bẫy Python:** tìm 3 dòng code của bạn từng viết có độ phức tạp ẩn (in trong vòng lặp, nối chuỗi, `in` trên list)."
        ),
        "tracuu_title": "Bảng chọn thuật toán theo ràng buộc & độ phức tạp thao tác",
        "tracuu": (
            "| n tối đa | Độ phức tạp khả thi | Gợi ý kỹ thuật |\n"
            "|---|---|---|\n"
            "| ≤ 10 | O(n!), O(2ⁿ·n) | hoán vị, vét cạn hết |\n"
            "| ≤ 20–25 | O(2ⁿ), O(n·2ⁿ) | bitmask, quay lui + tỉa |\n"
            "| ≤ 500 | O(n³) | DP 3 chiều, Floyd |\n"
            "| ≤ 5.000 | O(n²) | vét cạn cặp, DP 2 chiều |\n"
            "| ≤ 10⁵–10⁶ | O(n log n) | sort, nhị phân, heap |\n"
            "| ≤ 10⁷–10⁸ | O(n) | một lượt, đếm, hai con trỏ |\n"
            "| ≤ 10¹² | O(√n) | số học, kiểm tra ước |\n"
            "| ≤ 10¹⁸ | O(log n) | lũy thừa nhanh, nhị phân đáp số |\n\n"
            "**Độ phức tạp thao tác Python hay quên:** `x in list` O(n) — `x in set/dict` O(1); `pop(0)` trên list O(n) — dùng `deque`; "
            "nối chuỗi trong vòng lặp O(n²) — dùng list + `join`; `in` chuỗi con O(n·m) — regex/KMP khi lớn."
        ),
    },
    "b27-Tim-Kiem": {
        "tag": "Kỹ thuật cơ bản · Tìm kiếm & chặt nhị phân",
        "homework": (
            "1. **Cài từ đầu:** viết `binary_search(a, x)` tay (không dùng `bisect`) — test với 10 mảng ngẫu nhiên đã sort.\n"
            "2. **Đếm bằng bisect:** cho dãy đã sort, đếm số phần tử trong đoạn [L, R] chỉ bằng `bisect_left/right`, so tốc độ với cách lọc.\n"
            "3. **Chặt nhị phân đáp số:** giải bài \"cắt dây\" (tìm độ dài lớn nhất cắt được k đoạn) — viết hàm `duoc(x)` + chặt."
        ),
        "tracuu_title": "Tìm kiếm — template & bisect",
        "tracuu": (
            "| Kỹ thuật | Template | Dùng khi |\n"
            "|---|---|---|\n"
            "| Tuyến tính | `for x in a: if x == k:` | n nhỏ / không sort |\n"
            "| Nhị phân tay | `lo, hi = 0, n-1; while lo <= hi:` | hiểu bản chất |\n"
            "| `bisect_left(a, x)` | vị trí đầu tiên ≥ x | đếm số < x |\n"
            "| `bisect_right(a, x)` | vị trí đầu tiên > x | đếm số ≤ x |\n"
            "| Đếm trong [L, R] | `bisect_right(a,R) - bisect_left(a,L)` | đoạn giá trị |\n"
            "| Chặt đáp số | `while lo < hi: mid...; if duoc(mid): lo = mid+1` | \"lớn nhất/nhỏ nhất thỏa điều kiện đơn điệu\" |\n\n"
            "```python\nfrom bisect import bisect_left, bisect_right\n```\n"
            "**Bẫy:** chỉ chặt nhị phân khi dãy đã sort hoặc tính chất **đơn điệu**; cẩn thận biên lo/hi "
            "(`lo <= hi` vs `lo < hi`, trả về chỉ số hay giá trị)."
        ),
    },
    "b28-Sap-Xep": {
        "tag": "Kỹ thuật cơ bản · Sắp xếp",
        "homework": (
            "1. **Tam kiếm:** cho list 10 chuỗi tên, sắp theo: thứ tự từ điển; độ dài; độ dài giảm dần rồi từ điển.\n"
            "2. **Bảng xếp hạng:** cho (tên, điểm, số lỗi), xếp hạng theo điểm giảm, lỗi tăng, tên tăng — một `sorted`.\n"
            "3. **Cài merge sort:** viết bản merge sort đệ quy 15 dòng, test với mảng ngẫu nhiên so `sorted`."
        ),
        "tracuu_title": "Sắp xếp — sorted & khuôn mẫu khóa",
        "tracuu": (
            "| Cú pháp | Việc | Ví dụ |\n"
            "|---|---|---|\n"
            "| `sorted(ds)` | Bản mới, giữ gốc | |\n"
            "| `ds.sort()` | Sắp tại chỗ (trả None) | |\n"
            "| `key=len` | Theo độ dài | `sorted(ds, key=len)` |\n"
            "| `key=lambda x: x[1]` | Theo phần tử thứ 2 | |\n"
            "| `key=lambda x: (-x[1], x[0])` | Số giảm, tên tăng | Bảng xếp hạng |\n"
            "| `reverse=True` | Đảo chiều | |\n"
            "| `key=str.lower` | Không phân biệt hoa thường | |\n"
            "| `key=lambda x: (x % 2, x)` | Chẵn trước, rồi tăng | Khóa tổ hợp bất kỳ |\n\n"
            "**Ghi nhớ:** Python `sort` là Timsort — **ổn định** (ổn định: phần bằng nhau giữ thứ tự cũ), viết bằng C, rất nhanh; "
            "cần tự cài chỉ để học (merge/quick/counting). Đếm phân phối khi giá trị nhỏ: mảng đếm size giá trị."
        ),
    },
    "b29-Stack-Queue-Hashing": {
        "tag": "Bảng băm & ngăn xếp · Ứng dụng",
        "homework": (
            "1. **Ngoặc hợp lệ:** kiểm tra chuỗi ngoặc `()[]{}` hợp lệ bằng stack — test 6 chuỗi đúng/sai.\n"
            "2. **Hàng đợi cửa hàng:** mô phỏng hàng đợi bằng `deque` — thêm khách, phục vụ, in trạng thái mỗi bước.\n"
            "3. **Nhiệm vụ trùng:** cho list mã nhiệm vụ, in mã XUẤT HIỆN ĐẦU TIÊN hai lần (một lượt + set)."
        ),
        "tracuu_title": "collections & heapq — hộp đồ nghề ngăn xếp/hàng đợi/băm",
        "tracuu": (
            "| Công cụ | Import | Việc | Ví dụ |\n"
            "|---|---|---|---|\n"
            "| `deque` | `from collections import deque` | Hàng đợi 2 đầu O(1) | `d.appendleft/popleft/append/pop` |\n"
            "| `Counter` | `from collections import Counter` | Đếm tần suất | `Counter(ds).most_common(k)` |\n"
            "| `defaultdict` | `from collections import defaultdict` | Dict tự giá trị mặc định | `defaultdict(list)` gom nhóm |\n"
            "| `heapq.heappush(h, x)` | `import heapq` | Thêm vào heap | Hàng đợi ưu tiên |\n"
            "| `heapq.heappop(h)` | | Lấy phần tử NHỎ nhất | Dijkstra |\n"
            "| `heapq.heapify(ds)` | | Biến list thành heap tại chỗ | O(n) |\n"
            "| `heapq.nlargest(k, ds)` | | K phần tử lớn nhất | Top-K nhanh |\n"
            "| Stack | list | `append` / `pop` | LIFO |\n\n"
            "**Bẫy:** `list.pop(0)` là O(n) — hàng đợi thật phải dùng `deque.popleft()`; "
            "heapq chỉ là min-heap — muốn max-heap thì thêm dấu âm."
        ),
    },
    "b31-De-Quy": {
        "tag": "Đệ quy & quay lui · Đệ quy",
        "homework": (
            "1. **Ba công thức:** viết đệ quy tính giai thừa, tổng chữ số, in dãy Fibo thứ n — chỉ rõ base + bước.\n"
            "2. **Đo độ sâu:** chạy đệ quy sâu n = 10, 100, 1000, 10.000 — ghi lại kết quả và tìm giới hạn của máy.\n"
            "3. **Memo hóa:** tính C(n,k) bằng đệ quy + `lru_cache`, đối chiếu `math.comb` — so n từ 5 đến 30."
        ),
        "tracuu_title": "Template đệ quy & memoization",
        "tracuu": (
            "| Khuôn mẫu | Cú pháp |\n"
            "|---|---|\n"
            "| Khung chuẩn | `def f(n): if base: return ...; return combine(f(n-1))` |\n"
            "| Memo thủ công | `if n in nho: return nho[n]` trước khi tính |\n"
            "| Memo 1 dòng | `from functools import lru_cache` + `@lru_cache(maxsize=None)` |\n"
            "| Nới giới hạn | `import sys; sys.setrecursionlimit(300000)` |\n\n"
            "```python\nfrom functools import lru_cache\n\n@lru_cache(maxsize=None)\ndef f(n):\n    ...\n```\n"
            "**Quy tắc sống còn:** (1) base đúng và \"bao\" biên, (2) mỗi gọi phải tiến gần base; "
            "bài con lặp lại → memo; sâu tuyến tính lớn → vòng lặp."
        ),
    },
    "b32-Quay-Lui": {
        "tag": "Đệ quy & quay lui · Backtracking",
        "homework": (
            "1. **Nhị phân n=3:** viết quay lui in mọi xâu nhị phân độ dài 3, vẽ cây gọi ra giấy.\n"
            "2. **Tổ hợp chập k:** liệt kê mọi tổ hợp chập 3 của 1..6 — kiểm tra đủ 20 bộ, đúng thứ tự từ điển.\n"
            "3. **N-Queens n=5:** chạy bản bài học với n=5, đếm nghiệm; so với 2-BFS/backtracking tỉa thêm."
        ),
        "tracuu_title": "Template quay lui (chọn — thử — hoàn tác)",
        "tracuu": (
            "| Bước | Code mẫu |\n"
            "|---|---|\n"
            "| 1. Chọn | `duong.append(x)` |\n"
            "| 2. Đệ quy | `dq(i + 1)` |\n"
            "| 3. Hoàn tác | `duong.pop()` |\n"
            "| Base | `if i == n: ghi_nhan(duong); return` |\n"
            "| Tỉa | `if dieu_kien_sai: return` trước khi đệ quy |\n\n"
            "**Checklist tránh bug:** hoàn tác đủ (đối xứng với lúc chọn)? điều kiện tỉa đặt ĐÚNG chỗ (trước vòng for con)? "
            "kết quả ghi bằng bản sao `duong[:]` (không lưu tham chiếu)?"
        ),
    },
    "b33-Hai-Con-Tro": {
        "tag": "Kỹ thuật dãy số · Hai con trỏ & tiền tố",
        "homework": (
            "1. **Cặp tổng S:** giải \"2 số cộng bằng S\" trên dãy đã sort bằng hai con trỏ — so với vét cạn đếm số phép.\n"
            "2. **Đoạn dài nhất:** tìm đoạn dài nhất không có phần tử trùng (sliding window + dict vị trí cuối).\n"
            "3. **Tiền tố thần tốc:** cho dãy 10⁵ số, trả lời 10⁵ truy vấn tổng đoạn [l, r] — tiền tố O(1)/truy vấn."
        ),
        "tracuu_title": "Template hai con trỏ & tổng tiền tố",
        "tracuu": (
            "| Khuôn mẫu | Template ngắn | Dùng khi |\n"
            "|---|---|---|\n"
            "| Hai con trỏ ngược | `l, r = 0, n-1` tiến vào nhau | dãy sort, cặp/tổng |\n"
            "| Cửa sổ trượt | `l = 0; for r in range(n): while đk xấu: l += 1` | đoạn liên tiếp thỏa điều kiện |\n"
            "| Tiền tố | `P[0]=0; P[i+1]=P[i]+a[i]` → `tong(l,r)=P[r+1]-P[l]` | hỏi tổng đoạn nhiều lần |\n"
            "| Tiền tố + dict | `thay[P[i]]` tra \"tổng gặp trước\" | đoạn tổng K (kể cả số âm) |\n\n"
            "**Nhận diện:** đề có chữ \"liên tiếp/đoạn con\" + \"dài nhất/nhỏ nhất/đếm\" → nghĩ ngay kỹ thuật dãy. "
            "Cửa sổ trượt chỉ chuẩn khi điều kiện **đơn điệu** (thêm phần tử không làm điều kiện tốt lên) — số âm phá điều kiện này."
        ),
    },
    "b34-Tham-Lam": {
        "tag": "Kỹ thuật tối ưu · Tham lam",
        "homework": (
            "1. **Đổi tiền có điều kiện:** hệ tiền [1, 3, 4], tổng 6 — chỉ ra tham lam sai (4+1+1) và đúng (3+3).\n"
            "2. **Xếp lịch:** cho 6 việc (bắt đầu, kết thúc), chọn nhiều việc nhất không chồng — sort theo kết thúc.\n"
            "3. **5 phút phản ví dụ:** tự nghĩ 1 bài \"trông tham lam được\" nhưng có phản ví dụ — ghi lại."
        ),
        "tracuu_title": "Template tham lam & checklist chứng minh",
        "tracuu": (
            "| Bước | Nội dung |\n"
            "|---|---|\n"
            "| 1. Chọn tiêu chí | thường: sort theo đầu / cuối / tỉ lệ + 1 vòng chọn |\n"
            "| 2. Chọn dứt khoát | mỗi bước chọn \"tốt nhất hiện tại\", không quay lại |\n"
            "| 3. Chứng minh | đổi chỗ (exchange argument) hoặc \"tham lam không kém gì tối ưu\" |\n"
            "| 4. Phản ví dụ | 5 phút thử phá — không phá được thì mới dùng |\n\n"
            "**Khuôn mẫu hay gặp:** sort theo thời điểm kết thúc (xếp lịch); sort giảm theo giá trị/trọng (túi phân số); "
            "duyệt + chọn nếu không xung đột. **Thấy \"đổi tiền tổng quát\" → tham lam sai, phải DP.**"
        ),
    },
    "b35-Quy-Hoach-Dong": {
        "tag": "Kỹ thuật tối ưu · Quy hoạch động",
        "homework": (
            "1. **5 bước bằng tay:** lấy bài \"bậc thang n bậc\", viết đủ 5 bước (định nghĩa → truy hồi → base → thứ tự → đáp án) trước khi code.\n"
            "2. **Hai phiên bản:** giải bài đổi tiền ít tờ nhất bằng cả top-down (memo) và bottom-up — so sánh code và tốc độ.\n"
            "3. **Lăn mảng:** giải LIS/cái túi bản O(n) bộ nhớ (lăn 1 hàng) — kiểm tra kết quả khớp bản 2 hàng."
        ),
        "tracuu_title": "5 bước DP & khuôn mẫu thường gặp",
        "tracuu": (
            "| Bước | Câu hỏi | Ví dụ (bậc thang) |\n"
            "|---|---|---|\n"
            "| 1. Định nghĩa | `dp[...]` là gì? | `dp[i]` = số cách tới bậc i |\n"
            "| 2. Truy hồi | Từ bài nhỏ nào? | `dp[i] = dp[i-1] + dp[i-2]` |\n"
            "| 3. Base | Trường hợp nhỏ nhất | `dp[0] = 1` |\n"
            "| 4. Thứ tự | Duyệt sao cho bài nhỏ xong trước | i tăng dần |\n"
            "| 5. Đáp án | Ô nào? | `dp[n]` |\n\n"
            "**Mẫu hay gặp:** bậc thang/đổi tiền (1 chiều); túi 0/1 (2 chiều, duyệt ngược nếu lăn mảng); "
            "LIS O(n²); LCS (2 chiều). **Top-down** = đệ quy + memo (dễ nghĩ); **bottom-up** = vòng lặp + bảng (chuẩn thi)."
        ),
    },

    # ================= b36–b46: CHUYÊN ĐỀ THUẬT TOÁN NÂNG CAO =================
    "b36-Toan-Hoc-So-Hoc": {
        "tag": "Chuyên đề · Toán học & số học thuật toán",
        "homework": (
            "1. **Sàng lọc:** viết sàng Eratosthenes tìm số nguyên tố ≤ 10⁶ — so với `is_prime` lặp √n.\n"
            "2. **Euclid & lũy thừa nhanh:** cài `gcd` và `pow_mod(a, n, m)` tay (không dùng `math`/`pow`) — test 5 cặp số lớn.\n"
            "3. **Tổ hợp C(n,k) mod M:** giải bài chọn k món từ n món, kết quả modulo 10⁹+7 — dùng Fermat + fact/invfact."
        ),
        "tracuu_title": "Sàng, Euclid, lũy thừa, Fermat, tổ hợp",
        "tracuu": (
            "| Kỹ thuật | Template | Ví dụ |\n"
            "|---|---|---|\n"
            "| Sàng Eratosthenes | `s = [True]*(n+1); for i in range(2, isqrt(n)+1):` | Liệt kê nguyên tố ≤ 10⁶ |\n"
            "| Kiểm tra nguyên tố | Miller-Rabin (n ≤ 10¹⁸) | `pow(a, n-1, n) == 1` |\n"
            "| GCD | `def gcd(a,b): return gcd(b, a%b) if b else a` | `gcd(48, 18)` → 6 |\n"
            "| Lũy thừa nhanh | `pow_mod(x, n, m)` chia đôi mũ | `pow(x, n, m)` có sẵn |\n"
            "| Fermat nhỏ | `a^(p-1) ≡ 1 (mod p)` | Nghịch đảo modulo |\n"
            "| Tổ hợp C(n,k) mod p | `fact[n] * invfact[k] * invfact[n-k] % p` | `n, k ≤ 10⁶` |\n\n"
            "**Ghi nhớ:** Python có sẵn `math.gcd`, `math.comb`, `pow(x, n, m)` — thi dùng luôn, tự cài chỉ để hiểu bản chất."
        ),
    },
    "b37-Do-Thi-BFS-DFS": {
        "tag": "Chuyên đề · Đồ thị BFS & DFS",
        "homework": (
            "1. **BFS tìm đường:** giải bài \"đường đi ngắn nhất trong mê cung 0/1\" bằng BFS + queue — so với DFS không đảm bảo ngắn nhất.\n"
            "2. **DFS topo:** viết DFS tìm thứ tự topo của DAG 10 đỉnh — kiểm tra không có chu trình.\n"
            "3. **Hai phía:** cho đồ thị 2 màu có thể tô, kiểm tra bằng BFS tô 2 màu — test 3 đồ thị đúng/sai."
        ),
        "tracuu_title": "BFS, DFS, Topo, Hai phía, Flood fill",
        "tracuu": (
            "| Kỹ thuật | Template | Dùng khi |\n"
            "|---|---|---|\n"
            "| BFS (queue) | `deque([s]); while q: u = q.popleft()` | Đồ thị không trọng số, đường ngắn nhất |\n"
            "| DFS (stack/đệ quy) | `stack = [s]; while stack:` | Duyệt sâu, topo, flood fill |\n"
            "| Topo (Kahn) | `deque(u for u if deg[u]==0)` | DAG, sắp xếp phụ thuộc |\n"
            "| Hai phía | `color[u] = 1 - color[v]` | Đồ thị hai phía? |\n"
            "| Flood fill | BFS/DFS trên lưới | Mê cung, địa hình |\n\n"
            "**Ghi nhớ:** BFS = hàng đợi (deque), DFS = ngăn xếp/list; cả hai đều dùng `visited` set; "
            "đồ thị dùng list kề `adj[u] = [(v, w)]` cho trọng số hoặc `[v]` cho không trọng số."
        ),
    },
    "b38-Duong-Di-Ngan-Nhat": {
        "tag": "Chuyên đề · Đường đi ngắn nhất",
        "homework": (
            "1. **Dijkstra từ đầu:** cài Dijkstra với `heapq` cho đồ thị 10 đỉnh 20 cạnh — so với BFS (cạnh bằng nhau).\n"
            "2. **Bellman-Ford:** test đồ thị có cạnh âm (không chu trình âm) — phát hiện chu trình âm bằng vòng thứ n.\n"
            "3. **Floyd-Warshall:** ma trận 5×5, tìm mọi cặp đường ngắn nhất O(n³) — so với chạy n lần Dijkstra."
        ),
        "tracuu_title": "Dijkstra, Bellman-Ford, Floyd, 0-1 BFS",
        "tracuu": (
            "| Thuật toán | Độ phức tạp | Dùng khi |\n"
            "|---|---|---|\n"
            "| BFS | O(V+E) | Cạnh bằng nhau (mọi cạnh = 1) |\n"
            "| 0-1 BFS | O(V+E) | Cạnh chỉ 0 hoặc 1 | deque |\n"
            "| Dijkstra | O(E log V) | Trọng số ≥ 0, 1 nguồn | heapq |\n"
            "| Bellman-Ford | O(VE) | Có cạnh âm, 1 nguồn | Phát hiện chu trình âm |\n"
            "| Floyd-Warshall | O(V³) | Mọi cặp, V ≤ 400 | Ma trận kề |\n\n"
            "**Ghi nhớ:** Dijkstra chỉ đúng khi mọi cạnh ≥ 0; có cạnh âm → Bellman-Ford; mọi cặp → Floyd. "
            "Python `heapq` chỉ là min-heap — dùng `(-dist, u)` cho max-heap."
        ),
    },
    "b39-Cay-Va-DSU": {
        "tag": "Chuyên đề · Cây & DSU (Disjoint Set Union)",
        "homework": (
            "1. **DSU từ đầu:** cài `find(u)` nén đường + `union(u,v)` theo rank — test 10⁵ thao tác.\n"
            "2. **Đường kính cây:** 2-BFS/DFS tìm đường kính cây 10 đỉnh — so với cách tính qua LCA.\n"
            "3. **Kruskal MST:** cài Kruskal bằng DSU cho đồ thị 6 đỉnh 10 cạnh — so với Prim (heap)."
        ),
        "tracuu_title": "DSU, LCA, Đường kính, Kruskal, MST",
        "tracuu": (
            "| Kỹ thuật | Template | Ứng dụng |\n"
            "|---|---|---|\n"
            "| DSU (nén đường) | `def find(u): if p[u]!=u: p[u]=find(p[u]); return p[u]` | Hợp nhất tập rời, Kruskal |\n"
            "| DSU (rank) | `if rank[x]<rank[y]: x,y=y,x` | Giữ cây nông |\n"
            "| LCA binary lifting | `up[u][k]` tổ tiên 2ᵏ; `find_lca(u,v)` | Đường kính có trọng số, LCA |\n"
            "| 2-BFS đường kính | BFS từ node bất kỳ → xa nhất → BFS từ đó | Cây không trọng số |\n"
            "| Kruskal | Sort cạnh + DSU | MST, n,m ≤ 2×10⁵ |\n"
            "| Prim | heapq `(w, u)` + `used[]` | MST, đồ thị dày đặc |\n\n"
            "**Ghi nhớ:** DSU = hợp nhất tập rời — cốt lõi Kruskal & xử lý động; LCA binary lifting = nhảy theo lũy thừa 2^k, log n mỗi truy vấn."
        ),
    },
    "b40-Segment-Tree": {
        "tag": "Chuyên đề · Segment Tree & Fenwick (BIT)",
        "homework": (
            "1. **Fenwick từ đầu:** cài BIT 1-based (tổng tiền tố + cập nhật điểm) — test 10⁵ thao tác vs dict tiền tố.\n"
            "2. **Segment tree lười:** cài segment tree query tổng đoạn + cập nhật đoạn (lazy propagation) — test 10⁴ thao tác.\n"
            "3. **So sánh thực:** chọn 3 bài (tổng đoạn, max đoạn, đếm phần tử ≤ x trong đoạn) — đo thời gian BIT vs Segment Tree vs dict."
        ),
        "tracuu_title": "Segment Tree, Fenwick, Lazy, Cây đoạn lặp",
        "tracuu": (
            "| Cấu trúc | Template | Dùng khi |\n"
            "|---|---|---|\n"
            "| Fenwick (BIT) | `tree[i] += x; i += i & -i` (update) | Tổng tiền tố / điểm, query đơn điểm cập nhật điểm — O(log n) |\n"
            "| Segment tree (đệ quy) | `build(u,l,r)` + `query(u,l,r,L,R)` + `update(u,l,r,idx,val)` | Query đoạn + cập nhật điểm — O(log n) |\n"
            "| Segment tree (lười) | `push(u)` truyền tag con + `update_range` | Cập nhật đoạn + query đoạn — O(log n) |\n"
            "| Cây đoạn lặp | `for i in range(n, 2*n): tree[i] = a[i-n]` | Nén tọa độ + query đơn điểm — ngắn gọn, nhanh |\n\n"
            "**Ghi nhớ:** Fenwick = ngắn gọn nhất cho tổng tiền tố + cập nhật điểm; Segment tree = linh hoạt query đoạn + cập nhật đoạn; "
            "Cây đoạn lặp (iterative) = code ngắn, nhanh, phù hợp thi — nén tọa độ trước khi build."
        ),
    },
    "b41-Xu-Ly-Chuoi": {
        "tag": "Chuyên đề · Xử lý chuỗi nâng cao",
        "homework": (
            "1. **KMP từ đầu:** cài `compute_pi(p)` + `kmp_search(s, p)` — test tìm pattern trong text 10⁵ ký tự.\n"
            "2. **Z-function:** cài Z-function tìm pattern — so thời gian với KMP.\n"
            "3. **Rolling hash:** cài hash đa thức (base 31, mod 2⁶⁴ hoặc 10⁹+7) — tìm chuỗi con chung dài nhất 2 xâu."
        ),
        "tracuu_title": "KMP, Z-function, Rolling hash, Trie",
        "tracuu": (
            "| Kỹ thuật | Template | Ứng dụng |\n"
            "|---|---|---|\n"
            "| KMP (pi) | `pi[i] = độ dài tiền tố = hậu tố dài nhất của p[:i+1]` | Tìm pattern O(n+m) |\n"
            "| Z-function | `z[i] = độ dài tiền tố chung của s[i:] và s` | Tìm pattern O(n+m) |\n"
            "| Rolling hash | `h[i+1] = (h[i]*base + ord(s[i])) % mod` | So sánh xâu con O(1) |\n"
            "| Trie | Node: `con = {}`, `is_end` | Tìm prefix, đếm từ điển |\n"
            "| Aho-Corasick | Trie + fail link | Tìm nhiều pattern cùng lúc |\n\n"
            "**Ghi nhớ:** KMP/Z = tìm pattern chuẩn; Rolling hash = so sánh xâu con (khó so sánh trực tiếp O(L)); Trie = tiền tố / từ điển; "
            "Python có `hashlib` nhưng rolling hash tự cài nhanh hơn cho xâu con. Base thường dùng 31/131/911, mod 2⁶⁴ (unsigned) hoặc prime lớn."
        ),
    },
    "b42-Bitmask": {
        "tag": "Chuyên đề · Bitmask & Tối ưu trên tập hợp",
        "homework": (
            "1. **TSP bitmask:** giải Traveling Salesman n=12 bằng DP `dp[mask][i]` — so với vét cạn O(n!).\n"
            "2. **Meet-in-the-middle:** n=40, chia đôi 20+20, tìm cặp tổng bằng K — O(n·2ⁿ/²).\n"
            "3. **SOS DP:** cho 2ⁿ số, tính `sum[mask]` = tổng phần tử tập con `mask` — O(n·2ⁿ)."
        ),
        "tracuu_title": "Bitmask, TSP, Meet-in-the-middle, SOS DP",
        "tracuu": (
            "| Mẹo bit | Cú pháp | Ý nghĩa |\n"
            "|---|---|---|\n"
            "| Bật bit i | `mask \|= (1 << i)` | Thêm i vào tập |\n"
            "| Tắt bit i | `mask &= ~(1 << i)` | Bỏ i |\n"
            "| Kiểm tra bit i | `(mask >> i) & 1` | i có trong tập? |\n"
            "| lowbit | `x & -x` | Bit 1 thấp nhất |\n"
            "| Duyệt tập con | `for s in range(mask): s = (s-1) & mask` | Tất cả tập con |\n\n"
            "**Kỹ thuật hàng đầu:**\n"
            "| Kỹ thuật | Độ phức tạp | Dùng khi |\n"
            "|---|---|---|\n"
            "| DP bitmask | O(n²·2ⁿ) | n ≤ 20, trạng thái tập hợp |\n"
            "| Meet-in-the-middle | O(n·2ⁿ/²) | n ≤ 40, chia đôi tìm cặp |\n"
            "| SOS DP | O(n·2ⁿ) | Tổng tập con, đếm AND/OR |\n"
            "| XOR max | Trie 0/1 bit | Tối ưu XOR trên tập |\n\n"
            "**Ghi nhớ:** Python int vô hạn — bit thao tác nhanh; n ≤ 20 là ranh giới DP bitmask; "
            "n ≤ 40 dùng meet-in-the-middle; n ≤ 20 SOS DP ổn; Trie bit cho XOR max."
        ),
    },
    "b43-DP-Nang-Cao": {
        "tag": "Chuyên đề · Quy hoạch động nâng cao",
        "homework": (
            "1. **DP trên DAG:** viết DP topo + `dp[v] = max(dp[u] + w)` cho đồ thị 10 đỉnh có trọng số — so với Bellman-Ford.\n"
            "2. **Digit DP:** đếm số ≤ N có đúng K chữ số chẵn — 3 trạng thái (pos, tight, cnt).\n"
            "3. **Tree DP:** tìm đường kính cây có trọng số bằng `dfs(u, p)` trả `(đường kính, chiều cao tối đa)`."
        ),
        "tracuu_title": "DAG DP, Digit DP, Tree DP, Interval DP",
        "tracuu": (
            "| Loại DP nâng cao | Template | Ứng dụng |\n"
            "|---|---|---|\n"
            "| DAG DP | Topo sort + `dp[v] = max(dp[u] + w)` | Đường dài nhất, số cách |\n"
            "| Digit DP | `pos, tight, started, cnt` + memo | Đếm số thỏa điều kiện chữ số |\n"
            "| Tree DP | `dfs(u, p) → (ans, height)` + reroot | Đường kính, tập độc lập, MST trên cây |\n"
            "| Interval DP | Độ dài tăng dần, thử cắt cuối | Ma trận chuỗi, polygon triangulation |\n\n"
            "| Mẫu | Trạng thái | Chuyển trạng thái |\n"
            "|---|---|---|\n"
            "| DAG | `dp[v]` | `dp[v] = max(dp[u] + w(u,v))` |\n"
            "| Digit | `dp[pos][tight][cnt]` | Thử chữ số 0..9, cập nhật tight/started/cnt |\n"
            "| Tree | `dfs(u) → (ans, height)` | `ans = max(ans_con, h1 + h2)` |\n"
            "| Interval | `dp[l][r]` độ dài tăng dần | Thử cắt giữa: `dp[l][r] = max(dp[l][k] + dp[k+1][r] + cost)` |\n\n"
            "**Ghi nhớ:** DP nâng cao = \"DP 1 chiều không đủ\" → mở rộng trạng thái hoặc cấu trúc dữ liệu. "
            "DAG = topo sort; Digit = pos/tight/started; Tree = lá→gốc + reroot; Interval = độ dài tăng dần."
        ),
    },
    "b44-Chien-Luoc-Thi-HSG": {
        "tag": "Chiến lược · Chiến lược thi HSG & tổng kết",
        "homework": (
            "1. **Bàn tay mô phỏng:** làm 1 đề HSG tỉnh thật (4 bài, 180 phút) — ghi lại thời gian mỗi bài, điểm đạt được, phân tích SAI ở đâu.\n"
            "2. **Sổ mẫu 1 trang:** viết tay 1 trang tóm tắt toàn khóa (theo bảng Bài 44) — mang vào phòng thi (nếu được).\n"
            "3. **Tâm lý thi:** viết 5 câu tự nhắc khi bị bí / stress / hết giờ — đọc trước mỗi lần thi."
        ),
        "tracuu_title": "Quy trình thi, phân loại ràng buộc, sổ mẫu 1 trang",
        "tracuu": (
            "| Bước | Thời gian | Hành động |\n"
            "|---|---|---|\n"
            "| 1. Đọc 4 đề | 5–10 phút | Khoanh vùng dễ/khó, chọn 2 bài chắc ăn |\n"
            "| 2. Code bài dễ | 30–50 phút | Chắc ăn điểm, chạy test ngay |\n"
            "| 3. Bài giữa | 50–70 phút | Nghĩ kỹ, cài DP/đồ thị, stress test nhỏ |\n"
            "| 4. Bài khó | 60–90 phút | Viết brute force lấy điểm từng phần |\n"
            "| 5. Cuối giờ | 15 phút | Kiểm tra I/O, biên, test tự sinh |\n\n"
            "**Bảng chọn thuật toán từ ràng buộc (tóm tắt):**\n"
            "| n ≤ 10 | Hoán vị, vét cạn mọi thứ | Bài 26 (vét cạn), 32 (quay lui) |\n"
            "| ≤ 20–25 | Bitmask, quay lui + tỉa, DP mũ (TSP) | Bài 32, 42 (bitmask) |\n"
            "| ≤ 500 | DP O(n³), Floyd | Bài 35 (DP), 38 (Floyd) |\n"
            "| ≤ 5.000 | O(n²): DP, LIS O(n²), thử cặp | Bài 33, 35 |\n"
            "| ≤ 10⁵–10⁶ | O(n log n): sort, nhị phân, heap | Bài 27, 28, 34, 35 |\n"
            "| ≤ 10⁷–10⁸ | O(n): duyệt, hai con trỏ, Counter | Bài 30, 33, 35 |\n"
            "| ≤ 10¹² | O(√n): kiểm tra nguyên tố, thừa số | Bài 36 (số học) |\n"
            "| ≤ 10¹⁸ | O(log n): nhị phân đáp số, lũy thừa | Bài 27, 31, 36 |\n"
            "| Đồ thị 10⁵ | O(n+m): BFS/DFS; O(m log n): Dijkstra | Bài 37, 38 |\n"
            "| q truy vấn đoạn 10⁵ | O(log n)/truy vấn: BIT/segment tree | Bài 40 |\n\n"
            "**Tâm lý:** giữ bình tĩnh; bài khó → viết brute force lấy điểm từng phần; đừng bỏ trống."
        ),
    },
    "b45-Itertools": {
        "tag": "Công cụ · itertools cho thi đấu",
        "homework": (
            "1. **Liệt kê tổ hợp/hoán vị:** viết 3 bài (tổ hợp chập 3, hoán vị 4 phần tử, tích Descartes 2 dãy) bằng `itertools` 1 dòng.\n"
            "2. **Giảm vòng lặp:** viết lại 5 vòng lặp lồng nhau cũ bằng `product`, `permutations`, `combinations`.\n"
            "3. **Groupby + sort:** cho list 1000 từ, gom nhóm theo chữ cái đầu — `sorted + groupby` vs dict đếm."
        ),
        "tracuu_title": "product, permutations, combinations, accumulate, groupby",
        "tracuu": (
            "| Hàm | Việc | Ví dụ |\n"
            "|---|---|---|\n"
            "| `product(a, b)` | Tích Descartes | `product('ab', '12')` → `a1, a2, b1, b2` |\n"
            "| `permutations(a, k)` | Hoán vị k phần tử | `permutations('abc', 2)` |\n"
            "| `combinations(a, k)` | Tổ hợp chập k | `combinations('abc', 2)` |\n"
            "| `accumulate(a)` | Tổng tiền tố (lazy) | `list(accumulate([1,2,3]))` → `[1,3,6]` |\n"
            "| `groupby(a, key=)` | Gom nhóm kề (cần sort trước) | `groupby(sorted(a), key=lambda x: x[0])` |\n"
            "| `islice(gen, k)` | Lấy k phần tử đầu (chặn vô hạn) | `islice(count(), 5)` → `0..4` |\n"
            "| `count(start, step)` | Số vô hạn | `count(10, -1)` → `10,9,8...` |\n"
            "| `cycle(a)` | Lặp vô hạn | `cycle('ab')` → `a,b,a,b...` |\n"
            "| `chain(a, b)` | Nối iterator | `chain(a, b)` giống `a+b` cho iter |\n"
            "| `pairwise(a)` | Cặp kề (3.10+) | `pairwise([1,3,6])` → `(1,3), (3,6)` |\n\n"
            "**Ghi nhớ:** `itertools` là C tối ưu — nhanh hơn vòng lặp Python gấp chục lần; "
            "`groupby` **bắt buộc sort trước** nếu muốn gom toàn cục; iterator chỉ dùng **1 lần** — xong là hết!"
        ),
    },
    "b46-Ly-Thuyet-Tro-Choi": {
        "tag": "Chuyên đề · Lý thuyết trò chơi (Nim & Grundy)",
        "homework": (
            "1. **Nim cài từ đầu:** viết `grundy(n)` bằng `lru_cache` (mex) — test Nim 3 cọc [3,4,5].\n"
            "2. **Misère Nim:** sửa bản Nim cho luật \"người lấy cuối THUA\" — test [1,1] (người đầu thắng).\n"
            "3. **Sprague-Grundy:** 2 trò chơi con (cọc đá + ô cờ), tính Grundy mỗi trò rồi XOR — test 3 cặp trạng thái."
        ),
        "tracuu_title": "Nim, Grundy, Mex, Sprague-Grundy, Misère",
        "tracuu": (
            "| Khái niệm | Template | Ứng dụng |\n"
            "|---|---|---|\n"
            "| Nim position | `xor` tất cả cọc = 0 → P-position (thua) | Nim chuẩn |\n"
            "| Grundy | `mex({grundy(v) for v in next})` | Tách trò chơi thành trạng thái |\n"
            "| Mex | `min(i for i in range(...) if i not in S)` | Số nhỏ nhất không trong tập |\n"
            "| Sprague-Grundy | `grundy_total = grundy(game1) ^ grundy(game2)` | Gộp nhiều trò chơi con |\n"
            "| Misère | `if all(c == 1): return not xor; else return xor` | Nim misère |\n\n"
            "**Ghi nhớ:** impartial game = 2 người, biết hết thông tin, không may rủi; "
            "Grundy biến mọi trò chơi thành \"cọc Nim ảo\" — XOR là toán tử thống nhất. "
            "Misère chỉ khác khi TẤT CẢ cọc đều còn 1 đá."
        ),
    },
}
