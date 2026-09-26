# -*- coding: utf-8 -*-
"""Đồng bộ các track học tự chứa (generated copies) từ bản chính.

Nguồn chính (sửa ở đây):
  01-Co-Ban/          29 bài cơ bản
  02-Thuat-Toan/      19 bài thuật toán (chỉ thư mục gốc, không gồm Phan-1)
  03-Thuc-Chien/      12 bài thực chiến

Bản copy tự động (KHÔNG sửa trực tiếp — sửa bản chính rồi chạy script này):
  02-Thuat-Toan/Phan-1-Co-Ban/   copy 29 bài cơ bản (mục thuật toán tự chứa)
  04-Full/Phan-1-Co-Ban/         copy 29 bài cơ bản
  04-Full/Phan-2-Thuat-Toan/     copy 19 bài thuật toán
  04-Full/Phan-3-Thuc-Chien/     copy 12 bài thực chiến

Script copy file, viết lại link tương đối cho đúng vị trí mới, và gắn
dòng đánh dấu generated ở đầu file. Chạy lại bất cứ lúc nào (idempotent).
"""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARK = ("<!-- TỰ ĐỘNG ĐỒNG BỘ từ {src} — đừng sửa trực tiếp, "
        "sửa bản chính rồi chạy tools/sync_tracks.py -->\n\n")


import re

# Bài cơ bản lược khỏi track Thuật toán (không cần cho HSG/CP).
# Giữ lại ở 01-Co-Ban (bản chính) và 04-Full — chỉ track 2 là gọn nhẹ.
EXCLUDE_02_BASICS = {"03-VSCode", "09-Match-Case", "19-Exception", "21-Package",
                     "24-Dataclass", "28-Decorator", "29-Iterator"}

# "Bài tiếp theo" trỏ tới bài bị lược → chuyển sang bài giữ lại kế tiếp.
# (số, tiêu đề, thư mục) — tiêu đề khớp H1 bản chính.
NEXT_REDIRECT = {
    "03-VSCode": ("4", "Biến Trong Python", "04-Bien"),
    "09-Match-Case": ("10", "Vòng Lặp For – Lặp Lại Một Số Lần Biết Trước",
                       "10-Vong-Lap-For"),
    "19-Exception": ("20", "Module Trong Python", "20-Module"),
    "21-Package": ("22", "Đọc Và Ghi File Trong Python", "22-File"),
    "24-Dataclass": ("25", "Lambda – Hàm Vô Danh Siêu Ngắn Gọn", "25-Lambda"),
}

FINALE_02 = (
    "🎉 **Bạn đã hoàn thành phần Cơ bản của track Thuật toán!** "
    "Nền tảng đã đủ để luyện giải thuật — tiếp tục với:\n"
    "- 🧮 [Bài 1 — Tư Duy Thuật Toán](../../01-Tu-Duy-Thuat-Toan/bai.md)"
)

# Sửa văn xuôi nhắc bài bị lược (chỉ trong bản copy track 2).
# (file, đoạn cũ, đoạn mới)
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


def prune_track02():
    """Hậu xử lý bản copy track 2: link/prereq/văn xuôi + finale cho bài cuối."""
    base = ROOT / "02-Thuat-Toan" / "Phan-1-Co-Ban"
    drop_pat = "|".join(sorted(EXCLUDE_02_BASICS))
    nav_pat = "|".join(sorted(NEXT_REDIRECT))  # trừ 28-Decorator (finale riêng)
    for bai_file in sorted(base.glob("*/bai.md")):
        text = bai_file.read_text(encoding="utf-8")
        # 1. Xóa bullet điều kiện tiên quyết trỏ tới bài bị lược
        text = re.sub(
            r"^- \[Bài \d+ — .*?\]\(\.\./(?:" + drop_pat + r")/bai\.md\)\s*\n",
            "", text, flags=re.M)
        # 2a. Dòng "**Bài tiếp theo:**" trỏ tới bài bị lược → chuyển tiếp
        def repl_next(m):
            num, title, folder = NEXT_REDIRECT[m.group(1)]
            return (f"**Bài tiếp theo:** [Bài {num} — {title}]"
                    f"(../{folder}/bai.md)")
        text = re.sub(
            r"\*\*Bài tiếp theo:\*\* \[Bài \d+ — [^\]]*\]"
            r"\(\.\./(" + nav_pat + r")/bai\.md\)",
            repl_next, text)
        # 2b. Dòng "👉 Tiếp theo:" trỏ tới bài bị lược → chuyển tiếp
        def repl_next2(m):
            num, title, folder = NEXT_REDIRECT[m.group(1)]
            return (f"👉 Tiếp theo: **[Bài {num}: {title}]"
                    f"(../{folder}/bai.md)**")
        text = re.sub(
            r"👉 Tiếp theo: \*\*\[Bài \d+: [^\]]*\]"
            r"\(\.\./(" + nav_pat + r")/bai\.md\)\*\*",
            repl_next2, text)
        bai_file.write_text(text, encoding="utf-8")
    # 3. Bài cuối track (27-Generator): finale sang phần thuật toán
    last = base / "27-Generator" / "bai.md"
    text = last.read_text(encoding="utf-8")
    text = re.sub(
        r"\*\*Bài tiếp theo:\*\* \[Bài \d+ — [^\]]*\]\(\.\./28-Decorator/bai\.md\)",
        FINALE_02, text)
    last.write_text(text, encoding="utf-8")
    # 4. Sửa văn xuôi nhắc bài bị lược
    for fname, old, new in PROSE_FIXES:
        f = base / fname / "bai.md"
        text = f.read_text(encoding="utf-8")
        if old in text:
            f.write_text(text.replace(old, new), encoding="utf-8")
        else:
            print(f"  CẢNH BÁO: không thấy đoạn cần sửa trong {fname}")


def copy_track(src_branch, dest_dir, link_rules, pos_old, pos_new,
               exclude=frozenset()):
    """Copy toàn bộ bai.md từ src_branch sang dest_dir, viết lại link."""
    dest = ROOT / dest_dir
    if dest.exists():
        shutil.rmtree(dest)
    count = 0
    for src_file in sorted((ROOT / src_branch).glob("*/bai.md")):
        lesson = src_file.parent.name
        if lesson in exclude:
            continue
        target_dir = dest / lesson
        target_dir.mkdir(parents=True, exist_ok=True)
        text = src_file.read_text(encoding="utf-8")
        for old, new in link_rules:
            text = text.replace(old, new)
        text = text.replace("`" + pos_old, "`" + pos_new)
        rel_src = src_file.relative_to(ROOT).as_posix()
        text = MARK.format(src=rel_src) + text
        (target_dir / "bai.md").write_text(text, encoding="utf-8")
        count += 1
    print(f"  {dest_dir}: {count} file")


def main():
    print("Đồng bộ các track...")
    # Mục thuật toán: cơ bản (lược 7 bài không cần cho HSG) + thuật toán
    # Quy tắc: link cùng Phan dùng ../ ; link sang Phan khác dùng ../../
    copy_track(
        "01-Co-Ban", "02-Thuat-Toan/Phan-1-Co-Ban",
        link_rules=[
            ("](../../02-Thuat-Toan/", "](../../"),
            ("](../../03-Thuc-Chien/", "](../../../03-Thuc-Chien/"),
        ],
        pos_old="01-Co-Ban/",
        pos_new="02-Thuat-Toan/Phan-1-Co-Ban/",
        exclude=EXCLUDE_02_BASICS,
    )
    prune_track02()
    # Mục full: cả 3 phần
    copy_track(
        "01-Co-Ban", "04-Full/Phan-1-Co-Ban",
        link_rules=[
            ("](../../02-Thuat-Toan/", "](../../Phan-2-Thuat-Toan/"),
            ("](../../03-Thuc-Chien/", "](../../Phan-3-Thuc-Chien/"),
        ],
        pos_old="01-Co-Ban/",
        pos_new="04-Full/Phan-1-Co-Ban/",
    )
    copy_track(
        "02-Thuat-Toan", "04-Full/Phan-2-Thuat-Toan",
        link_rules=[
            ("](../../01-Co-Ban/", "](../../Phan-1-Co-Ban/"),
            ("](../../02-Thuat-Toan/", "](../"),
            ("](../../03-Thuc-Chien/", "](../../Phan-3-Thuc-Chien/"),
        ],
        pos_old="02-Thuat-Toan/",
        pos_new="04-Full/Phan-2-Thuat-Toan/",
    )
    copy_track(
        "03-Thuc-Chien", "04-Full/Phan-3-Thuc-Chien",
        link_rules=[
            ("](../../01-Co-Ban/", "](../../Phan-1-Co-Ban/"),
            ("](../../02-Thuat-Toan/", "](../../Phan-2-Thuat-Toan/"),
            ("](../../03-Thuc-Chien/", "](../"),
        ],
        pos_old="03-Thuc-Chien/",
        pos_new="04-Full/Phan-3-Thuc-Chien/",
    )
    print("Xong.")


if __name__ == "__main__":
    main()
