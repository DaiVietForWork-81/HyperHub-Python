# -*- coding: utf-8 -*-
"""Đồng bộ các track học tự chứa (generated copies) từ bản chính.

Nguồn chính (sửa ở đây):
  01-Co-Ban/          29 bài, số 1-29
  02-Thuat-Toan/      19 bài thuật toán, số 23-41 (KHÔNG có copy ở đây)
  03-Thuc-Chien/      12 bài, số 30-41

Bản copy tự động (KHÔNG sửa trực tiếp):
  02-Thuat-Toan/01-..-22-../   22 bài cơ bản, đánh số lại 1-22 (lược 7 bài)
      + 23-..-41-../           (bản chính) = track phẳng (1)-(41)
  04-Full/Phan-1-Co-Ban/       copy 29 bài, giữ số gốc
  04-Full/Phan-2-Thuat-Toan/   copy 19 bài, đánh số lại 1-19
  04-Full/Phan-3-Thuc-Chien/   copy 12 bài, giữ số gốc

Chạy lại bất cứ lúc nào (idempotent). Xong chạy tools/validate.py.
"""
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARK = ("<!-- TỰ ĐỘNG ĐỒNG BỘ từ {src} — đừng sửa trực tiếp, "
        "sửa bản chính rồi chạy tools/sync_tracks.py -->\n\n")

KEPT_ORDER = ["01-Gioi-Thieu", "02-Cai-Dat-Python", "04-Bien",
              "05-Kieu-Du-Lieu", "06-Toan-Tu", "07-Input-Output",
              "08-Cau-Lenh-If", "10-Vong-Lap-For", "11-Vong-Lap-While",
              "12-Ham", "13-Scope", "14-List", "15-Tuple", "16-Set",
              "17-Dictionary", "18-String", "20-Module", "22-File", "23-OOP",
              "25-Lambda", "26-List-Comprehension", "27-Generator"]
EXCLUDE_02_BASICS = {"03-VSCode", "09-Match-Case", "19-Exception",
                     "21-Package", "24-Dataclass", "28-Decorator",
                     "29-Iterator"}

BASIC_TRACK = {}  # thư mục gốc -> (số track, thư mục track)
for _i, _old in enumerate(KEPT_ORDER, 1):
    BASIC_TRACK[_old] = (_i, f"{_i:02d}-{_old[3:]}")
BMAP_NUM = {int(o[:2]): n for o, (n, _) in BASIC_TRACK.items()}
TRACK_BASIC_FOLDER = {o: new for o, (_, new) in BASIC_TRACK.items()}
ORIG_BASIC_FOLDER = {new: o for o, (_, new) in BASIC_TRACK.items()}

ALGO_OLD_TO_NEW = {
    "01-Tu-Duy-Thuat-Toan": "23-Tu-Duy-Thuat-Toan",
    "02-Do-Phuc-Tap": "24-Do-Phuc-Tap",
    "03-Tim-Kiem": "25-Tim-Kiem",
    "04-Sap-Xep": "26-Sap-Xep",
    "05-Stack-Queue-Hashing": "27-Stack-Queue-Hashing",
    "06-De-Quy": "28-De-Quy",
    "07-Quay-Lui": "29-Quay-Lui",
    "08-Hai-Con-Tro": "30-Hai-Con-Tro",
    "09-Tham-Lam": "31-Tham-Lam",
    "10-Quy-Hoach-Dong": "32-Quy-Hoach-Dong",
    "11-Toan-Hoc-So-Hoc": "33-Toan-Hoc-So-Hoc",
    "12-Do-Thi-BFS-DFS": "34-Do-Thi-BFS-DFS",
    "13-Duong-Di-Ngan-Nhat": "35-Duong-Di-Ngan-Nhat",
    "14-Cay-Va-DSU": "36-Cay-Va-DSU",
    "15-Segment-Tree": "37-Segment-Tree",
    "16-Xu-Ly-Chuoi": "38-Xu-Ly-Chuoi",
    "17-Bitmask": "39-Bitmask",
    "18-DP-Nang-Cao": "40-DP-Nang-Cao",
    "19-Chien-Luoc-Thi-HSG": "41-Chien-Luoc-Thi-HSG",
}
ALGO_NEW_TO_OLD = {v: k for k, v in ALGO_OLD_TO_NEW.items()}
AMAP_NUM = {i + 1: i + 23 for i in range(19)}      # algo cũ -> track (23-41)
RAMAP_NUM = {v: k for k, v in AMAP_NUM.items()}    # track -> cũ (1-19)

NEXT_REDIRECT = {
    "03-VSCode": (3, "Biến Trong Python", "03-Bien"),
    "09-Match-Case": (7, "Vòng Lặp For – Lặp Lại Một Số Lần Biết Trước",
                       "08-Vong-Lap-For"),
    "19-Exception": (17, "Module Trong Python", "17-Module"),
    "21-Package": (18, "Đọc Và Ghi File Trong Python", "18-File"),
    "24-Dataclass": (20, "Lambda – Hàm Vô Danh Siêu Ngắn Gọn", "20-Lambda"),
}
FINALE_02 = (
    "🎉 **Bạn đã hoàn thành phần Cơ bản của track Thuật toán "
    "(Bài 1–22)!** Nền tảng đã đủ để luyện giải thuật — tiếp tục với:\n"
    "- 🧮 [Bài 23 — Tư Duy Thuật Toán](../23-Tu-Duy-Thuat-Toan/bai.md)"
)

PROSE_FIXES = [
    ("20-Module",
     "Bài 21 (Package) và Bài 30 (Virtual Environment) sẽ dạy cách tổ chức chuyên nghiệp hơn.",
     "Với người mới, chỉ cần nhớ: file module và file dùng nó nằm cùng thư mục."),
    ("20-Module",
     "Lưu ý: cần xử lý trường hợp người dùng nhập chữ *(dùng ứng dụng Bài 19)*.",
     "Lưu ý: cần xử lý trường hợp người dùng nhập chữ *(bọc try/except — xem mẫu ở Bài 22-File)*."),
    ("20-Module",
     "* Lời khuyên: bọc `int(input(...))` trong `try/except` (Bài 19) để an toàn.",
     "* Lời khuyên: bọc `int(input(...))` trong `try/except` (mẫu ở Bài 22-File) để an toàn."),
    ("22-File",
     "Giải pháp: bọc trong `try/except` (kiến thức **Bài 19**):",
     "Giải pháp: bọc trong `try/except`:"),
    ("22-File",
     "> 💡 `float(x)` có thể gây `ValueError` nếu dữ liệu lỗi — kết hợp `try/except` (Bài 19) khi dữ liệu không tin cậy.",
     "> 💡 `float(x)` có thể gây `ValueError` nếu dữ liệu lỗi — kết hợp `try/except` khi dữ liệu không tin cậy."),
    ("23-OOP",
     "* **Gợi ý:** Dùng `try/except` để bắt lỗi truy cập trực tiếp (kiến thức Bài 19).",
     "* **Gợi ý:** Dùng `try/except` để bắt lỗi truy cập trực tiếp."),
]

SKIP_CONTEST = ("nghĩ 40%", "tương tự", "(dễ):", "(TB):", "(khó):")


def new_display_for_target(target):
    """Số hiển thị suy từ thư mục trong link target."""
    m = re.search(r"Phan-[123]-[A-Za-z-]+/([0-9]{2})-[A-Za-z-]+/bai\.md$",
                  target)
    if m:
        return int(m.group(1))
    m = re.search(r"\.\./([0-9]{2})-[A-Za-z-]+/bai\.md$", target)
    if m:
        return int(m.group(1))
    return None


def sync_link_displays(text):
    """Đồng bộ số 'Bài N' trong link [...](...) theo thư mục đích.
    Bỏ qua code fence (trừ mermaid), vì label mermaid cũng cần đúng số."""

    def fix_line(ln):
        def repl(m):
            n = new_display_for_target(m.group(2))
            if n is None:
                return m.group(0)
            return f"[Bài {n} — {m.group(1)}]({m.group(2)})"

        def repl2(m):
            n = new_display_for_target(m.group(2))
            if n is None:
                return m.group(0)
            return f"[Bài {n}: {m.group(1)}]({m.group(2)})"

        ln = re.sub(r"\[Bài \d+ — ([^\]]*)\]\(([^)]+)\)", repl, ln)
        ln = re.sub(r"\[Bài \d+: ([^\]]*)\]\(([^)]+)\)", repl2, ln)
        return ln

    out, in_fence, lang = [], False, ""
    for ln in text.splitlines():
        if ln.strip().startswith("```"):
            if not in_fence:
                in_fence, lang = True, ln.strip()[3:].strip()
            else:
                in_fence, lang = False, ""
            out.append(ln)
            continue
        if in_fence and lang != "mermaid":
            out.append(ln)
            continue
        out.append(fix_line(ln))
    return "\n".join(out)


def remap_bare_numbers(text, num_map):
    """Remap 'Bài N' văn xuôi; giữ tiêu đề/exercise/range/nav/contest/code."""

    def skip_line(s):
        return (s.startswith("### Bài ") or s.startswith("<summary>")
                or s.startswith("- [Bài") or s.startswith("# ")
                or s.startswith("**Bài ")
                or "Bài tiếp theo" in s or "Tiếp theo:" in s
                or any(k in s for k in SKIP_CONTEST))

    out, in_fence, lang = [], False, ""
    for ln in text.splitlines():
        if ln.strip().startswith("```"):
            if not in_fence:
                in_fence, lang = True, ln.strip()[3:].strip()
            else:
                in_fence, lang = False, ""
            out.append(ln)
            continue
        if (in_fence and lang != "mermaid") or skip_line(ln.strip()):
            out.append(ln)
            continue

        def repl_bare(m):
            after = ln[m.end():m.end() + 12]
            if re.match(r"\s+—\s+Bài\b", after):
                return m.group(0)
            if re.match(r"\s*[–—-]\s*\d", after):
                return m.group(0)
            n = int(m.group(1))
            if n in num_map:
                return f"Bài {num_map[n]}"
            return m.group(0)

        out.append(re.sub(r"Bài (\d+)\b", repl_bare, ln))
    return "\n".join(out)


def write_file(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def sync_track02_flat():
    """Track 2 phẳng tại 02-Thuat-Toan/: 22 copy (1-22) + 19 sources (23-41)."""
    root = ROOT / "02-Thuat-Toan"
    old_phan = root / "Phan-1-Co-Ban"
    if old_phan.exists():
        shutil.rmtree(old_phan)
        print("  xóa Phan-1-Co-Ban cũ")
    count = 0
    for old_folder in KEPT_ORDER:
        num, new_folder = BASIC_TRACK[old_folder]
        text = (ROOT / "01-Co-Ban" / old_folder / "bai.md").read_text(
            encoding="utf-8")
        # 1. Link anh em cũ -> thư mục track
        for o, (_, new_f) in BASIC_TRACK.items():
            text = text.replace(f"](../{o}/bai.md)", f"](../{new_f}/bai.md)")
        # 2. Link sang algo gốc -> anh em track (23-41)
        for o, new_f in ALGO_OLD_TO_NEW.items():
            text = text.replace(f"](../../02-Thuat-Toan/{o}/bai.md)",
                                f"](../{new_f}/bai.md)")
        # 3. Xóa prereq tới bài bị lược
        drop = "|".join(sorted(EXCLUDE_02_BASICS))
        text = re.sub(r"^- \[Bài \d+ — .*?\]\(\.\./(?:" + drop
                      + r")/bai\.md\)\s*\n", "", text, flags=re.M)
        # 4. H1 + Vị trí
        text = re.sub(r"^# Bài \d+ — ", f"# Bài {num} — ", text,
                      count=1, flags=re.M)
        text = text.replace(f"`01-Co-Ban/{old_folder}/bai.md`",
                            f"`02-Thuat-Toan/{new_folder}/bai.md`")
        # 5. Display link + bare numbers + prose
        text = sync_link_displays(text)
        text = remap_bare_numbers(text, BMAP_NUM)
        for fname, old, new in PROSE_FIXES:
            if old_folder == fname and old in text:
                text = text.replace(old, new)
        # 6. Next redirect / finale
        nav = "|".join(sorted(NEXT_REDIRECT))

        def repl_next(m):
            n2, t2, f2 = NEXT_REDIRECT[m.group(1)]
            return (f"**Bài tiếp theo:** [Bài {n2} — {t2}]"
                    f"(../{f2}/bai.md)")

        def repl_next2(m):
            n2, t2, f2 = NEXT_REDIRECT[m.group(1)]
            return (f"👉 Tiếp theo: **[Bài {n2}: {t2}]"
                    f"(../{f2}/bai.md)**")

        text = re.sub(
            r"\*\*Bài tiếp theo:\*\* \[Bài \d+ — [^\]]*\]"
            r"\(\.\./(" + nav + r")/bai\.md\)", repl_next, text)
        text = re.sub(
            r"👉 Tiếp theo: \*\*\[Bài \d+: [^\]]*\]"
            r"\(\.\./(" + nav + r")/bai\.md\)\*\*", repl_next2, text)
        if old_folder == "27-Generator":
            text = re.sub(
                r"\*\*Bài tiếp theo:\*\* \[Bài \d+ — [^\]]*\]"
                r"\(\.\./28-Decorator/bai\.md\)", FINALE_02, text)
        text = MARK.format(
            src=f"01-Co-Ban/{old_folder}/bai.md") + text
        target = root / new_folder
        if target.exists():
            shutil.rmtree(target)
        write_file(target / "bai.md", text)
        count += 1
    print(f"  02-Thuat-Toan phẳng: {count} copy cơ bản (1-22)")


def sync_full():
    """04-Full: Phan-1 (giữ số) + Phan-2 (reverse 23-41 -> 1-19) + Phan-3."""
    # --- Phan-1: copy nguyên, chỉ đổi link nhánh + Vị trí
    d1 = ROOT / "04-Full" / "Phan-1-Co-Ban"
    if d1.exists():
        shutil.rmtree(d1)
    for src in sorted((ROOT / "01-Co-Ban").glob("*/bai.md")):
        text = src.read_text(encoding="utf-8")
        # sources 01 trỏ algo bằng thư mục MỚI (23-..41) -> Phan-2 tên cũ
        for new_f, old_f in ALGO_NEW_TO_OLD.items():
            text = text.replace(
                f"](../../02-Thuat-Toan/{new_f}/bai.md)",
                f"](../../Phan-2-Thuat-Toan/{old_f}/bai.md)")
        text = text.replace("](../../03-Thuc-Chien/",
                            "](../../Phan-3-Thuc-Chien/")
        text = text.replace("`01-Co-Ban/", "`04-Full/Phan-1-Co-Ban/")
        text = MARK.format(src=src.relative_to(ROOT).as_posix()) + text
        write_file(d1 / src.parent.name / "bai.md", text)
    print("  04-Full/Phan-1-Co-Ban: 29 file")
    # --- Phan-2: từ sources algo (23-41), thư mục đích tên cũ (01-19)
    d2 = ROOT / "04-Full" / "Phan-2-Thuat-Toan"
    if d2.exists():
        shutil.rmtree(d2)
    for new_folder, old_folder in sorted(ALGO_NEW_TO_OLD.items()):
        src = ROOT / "02-Thuat-Toan" / new_folder / "bai.md"
        text = src.read_text(encoding="utf-8")
        # anh em algo mới -> tên cũ
        for nf, of in ALGO_NEW_TO_OLD.items():
            text = text.replace(f"](../{nf}/bai.md)", f"](../{of}/bai.md)")
        # anh em cơ bản track -> Phan-1 gốc (sang Phan khác: 2 tầng ..)
        for track_f, orig_f in ORIG_BASIC_FOLDER.items():
            text = text.replace(f"](../{track_f}/bai.md)",
                                f"](../../Phan-1-Co-Ban/{orig_f}/bai.md)")
        text = text.replace("](../../03-Thuc-Chien/",
                            "](../../Phan-3-Thuc-Chien/")
        # H1 23-41 -> 1-19
        text = re.sub(r"^# Bài (2[3-9]|3[0-9]|4[01]) — ",
                      lambda m: f"# Bài {int(m.group(1)) - 22} — ",
                      text, count=1, flags=re.M)
        # range + bảng tóm tắt
        text = text.replace("Bài 23–41", "Bài 1–19")
        if "41-Chien-Luoc-Thi-HSG" in new_folder:
            text = re.sub(r"^(\| )(2[3-9]|3[0-9]|4[01])(\. )",
                          lambda m: m.group(1) + str(int(m.group(2)) - 22)
                          + m.group(3), text, flags=re.M)
        text = sync_link_displays(text)
        text = remap_bare_numbers(text, RAMAP_NUM)
        text = text.replace(f"`02-Thuat-Toan/{new_folder}/bai.md`",
                            f"`04-Full/Phan-2-Thuat-Toan/{old_folder}/bai.md`")
        text = MARK.format(src=src.relative_to(ROOT).as_posix()) + text
        write_file(d2 / old_folder / "bai.md", text)
    print("  04-Full/Phan-2-Thuat-Toan: 19 file (đánh số lại 1-19)")
    # --- Phan-3: copy nguyên, đổi link nhánh + Vị trí
    d3 = ROOT / "04-Full" / "Phan-3-Thuc-Chien"
    if d3.exists():
        shutil.rmtree(d3)
    for src in sorted((ROOT / "03-Thuc-Chien").glob("*/bai.md")):
        text = src.read_text(encoding="utf-8")
        text = text.replace("](../../01-Co-Ban/",
                            "](../../Phan-1-Co-Ban/")
        # sources 03 trỏ algo bằng thư mục MỚI (23-..41) -> Phan-2 tên cũ
        for new_f, old_f in ALGO_NEW_TO_OLD.items():
            text = text.replace(
                f"](../../02-Thuat-Toan/{new_f}/bai.md)",
                f"](../../Phan-2-Thuat-Toan/{old_f}/bai.md)")
        text = text.replace("](../../03-Thuc-Chien/", "](../")
        text = text.replace("`03-Thuc-Chien/", "`04-Full/Phan-3-Thuc-Chien/")
        text = MARK.format(src=src.relative_to(ROOT).as_posix()) + text
        write_file(d3 / src.parent.name / "bai.md", text)
    print("  04-Full/Phan-3-Thuc-Chien: 12 file")


def main():
    print("Đồng bộ các track...")
    sync_track02_flat()
    sync_full()
    print("Xong. Chạy tools/validate.py để kiểm tra.")


if __name__ == "__main__":
    main()
