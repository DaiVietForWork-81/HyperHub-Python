# -*- coding: utf-8 -*-
"""ONE-SHOT: đánh số lại sources thuật toán 1-19 thành 23-41 (track phẳng).

Chạy 1 lần duy nhất rồi bỏ. Bản copy/full do tools/sync_tracks.py lo.
Xem REWORK_PLAN.md để hiểu toàn cảnh.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ALGO = ROOT / "02-Thuat-Toan"

OLD_SLUGS = ["01-Tu-Duy-Thuat-Toan", "02-Do-Phuc-Tap", "03-Tim-Kiem",
             "04-Sap-Xep", "05-Stack-Queue-Hashing", "06-De-Quy",
             "07-Quay-Lui", "08-Hai-Con-Tro", "09-Tham-Lam",
             "10-Quy-Hoach-Dong", "11-Toan-Hoc-So-Hoc", "12-Do-Thi-BFS-DFS",
             "13-Duong-Di-Ngan-Nhat", "14-Cay-Va-DSU", "15-Segment-Tree",
             "16-Xu-Ly-Chuoi", "17-Bitmask", "18-DP-Nang-Cao",
             "19-Chien-Luoc-Thi-HSG"]
NEW_SLUGS = ["23-Tu-Duy-Thuat-Toan", "24-Do-Phuc-Tap", "25-Tim-Kiem",
             "26-Sap-Xep", "27-Stack-Queue-Hashing", "28-De-Quy",
             "29-Quay-Lui", "30-Hai-Con-Tro", "31-Tham-Lam",
             "32-Quy-Hoach-Dong", "33-Toan-Hoc-So-Hoc", "34-Do-Thi-BFS-DFS",
             "35-Duong-Di-Ngan-Nhat", "36-Cay-Va-DSU", "37-Segment-Tree",
             "38-Xu-Ly-Chuoi", "39-Bitmask", "40-DP-Nang-Cao",
             "41-Chien-Luoc-Thi-HSG"]
AMAP = {i + 1: i + 23 for i in range(19)}          # số bài cũ -> mới
FOLDER = dict(zip(OLD_SLUGS, NEW_SLUGS))            # thư mục cũ -> mới
NUM_OF_NEWFOLDER = {v: int(v[:2]) for v in NEW_SLUGS}

# Bài cơ bản cũ -> thư mục track (giữ lại để trỏ prereq trong track).
KEPT = ["01-Gioi-Thieu", "02-Cai-Dat-Python", "04-Bien", "05-Kieu-Du-Lieu",
        "06-Toan-Tu", "07-Input-Output", "08-Cau-Lenh-If", "10-Vong-Lap-For",
        "11-Vong-Lap-While", "12-Ham", "13-Scope", "14-List", "15-Tuple",
        "16-Set", "17-Dictionary", "18-String", "20-Module", "22-File",
        "23-OOP", "25-Lambda", "26-List-Comprehension", "27-Generator"]
TRACK_BASIC = {}
for i, old in enumerate(KEPT, 1):
    TRACK_BASIC[old] = f"{i:02d}-{old[3:]}"
TRACK_BASIC_NUM = {old: int(new[:2]) for old, new in TRACK_BASIC.items()}

SKIP_CONTEST = ("nghĩ 40%", "tương tự", "(dễ):", "(TB):", "(khó):")


NEW_BASIC_NUM = {v: int(v[:2]) for v in TRACK_BASIC.values()}


def disp_for_folder(folder):
    """Số hiển thị = số đầu thư mục (track hoặc algo mới)."""
    if folder in NUM_OF_NEWFOLDER:
        return NUM_OF_NEWFOLDER[folder]
    if folder in TRACK_BASIC:
        return int(TRACK_BASIC[folder][:2])
    if folder in NEW_BASIC_NUM:
        return NEW_BASIC_NUM[folder]
    return None


def fix_structural_line(line):
    """Nav/prereq: đồng bộ số hiển thị theo thư mục trong cùng dòng."""
    def repl(m):
        pre, mid, folder, post = m.groups()
        n = disp_for_folder(folder)
        if n is None:
            return m.group(0)
        return f"{pre}{n}{mid}{folder}{post}"
    line = re.sub(
        r"(\*\*Bài tiếp theo:\*\* \[Bài )\d+( — [^\]]*\]\(\.\./)([^/)]+)(/bai\.md\))",
        repl, line)
    line = re.sub(
        r"(👉 Tiếp theo: \*\*\[Bài )\d+(: [^\]]*\]\(\.\./)([^/)]+)(/bai\.md\)\*\*)",
        repl, line)
    line = re.sub(
        r"^(- \[Bài )\d+( — [^\]]*\]\(\.\./)([^/)]+)(/bai\.md\))",
        repl, line)
    return line


DROPPED_BASICS = {"03-VSCode", "09-Match-Case", "19-Exception",
                    "21-Package", "24-Dataclass", "28-Decorator", "29-Iterator"}


def process(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    out = []
    for ln in lines:
        # 0. Bullet prereq trỏ bài cơ bản bị lược khỏi track -> xóa dòng
        m0 = re.match(r"^- \[Bài \d+ — [^\]]*\]\(\.\./\.\./01-Co-Ban/([^/)]+)/bai\.md\)", ln)
        if m0 and m0.group(1) in DROPPED_BASICS:
            continue
        # 0b. Dòng Vị trí: cập nhật thư mục
        for old_f, new_f in FOLDER.items():
            if f"`02-Thuat-Toan/{old_f}/bai.md`" in ln:
                ln = ln.replace(f"`02-Thuat-Toan/{old_f}/bai.md`",
                                f"`02-Thuat-Toan/{new_f}/bai.md`")
        # 1. Link anh em algo: ../OLD/ -> ../NEW/
        ln = re.sub(r"\(\.\./(0[1-9]-[A-Za-z-]+|1[0-9]-[A-Za-z-]+)/bai\.md\)",
                    lambda m: "(../" + FOLDER.get(m.group(1), m.group(1))
                    + "/bai.md)", ln)
        # 2. Prereq sang cơ bản gốc -> anh em trong track phẳng
        ln = re.sub(r"\(\.\./\.\./01-Co-Ban/([0-9]{2}-[A-Za-z-]+)/bai\.md\)",
                    lambda m: "(../" + TRACK_BASIC.get(m.group(1), m.group(1))
                    + "/bai.md)", ln)
        # 3. H1
        m = re.match(r"^# Bài (\d+) — ", ln)
        if m and int(m.group(1)) in AMAP:
            ln = f"# Bài {AMAP[int(m.group(1))]} — " + ln[m.end():]
        # 4. Số hiển thị theo thư mục (nav/prereq)
        ln = fix_structural_line(ln)
        # 5. Range Bài 1–19 -> Bài 23–41
        ln = re.sub(r"Bài 1\s*[–—-]\s*19\b", "Bài 23–41", ln)
        # 6. Hàng bảng tóm tắt "| 12. Đồ thị |" (file chiến lược)
        if path.parent.name == "41-Chien-Luoc-Thi-HSG":
            ln = re.sub(r"^(\| )(1[0-9]|[1-9])(\. )",
                        lambda m: m.group(1) + str(AMAP[int(m.group(2))])
                        + m.group(3), ln)
        # 7. Nhắc số trần: remap, trừ các trường hợp giữ nguyên
        s = ln.strip()
        if (s.startswith("### Bài ") or s.startswith("<summary>")
                or s.startswith("- [Bài") or s.startswith("# ")
                or s.startswith("**Bài ")
                or "Bài tiếp theo" in s or "Tiếp theo:" in s
                or any(k in s for k in SKIP_CONTEST)):
            out.append(ln)
            continue
        def repl_bare(m):
            # "Bài X — Bài Y" (bài tập X của bài học Y): giữ X, remap Y ở lượt nó
            after = ln[m.end():m.end() + 12]
            if re.match(r"\s+—\s+Bài\b", after):
                return m.group(0)
            # range "Bài X – M": giữ (bài tập), trừ Bài 1–19 đã xử lý ở bước 5
            if re.match(r"\s*[–—-]\s*\d", after):
                return m.group(0)
            n = int(m.group(1))
            if n in AMAP:
                print(f"  remap {path.parent.name}: Bài {n} -> Bài {AMAP[n]} :: {s[:70]}")
                return f"Bài {AMAP[n]}"
            return m.group(0)
        ln = re.sub(r"Bài (1[0-9]|[1-9])\b", repl_bare, ln)
        out.append(ln)
    path.write_text("\n".join(out) + "\n", encoding="utf-8")


def main():
    for new in NEW_SLUGS:
        process(ALGO / new / "bai.md")
    print("Xong renumber sources algo.")


if __name__ == "__main__":
    main()
