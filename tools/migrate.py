# -*- coding: utf-8 -*-
"""Gộp 3 file (bai_giang/bai_tap/dap_an) của mỗi bài cũ thành 1 file bai.md
theo cấu trúc 3 lộ trình mới. Đảm bảo không mất nội dung hữu ích.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OLD = ROOT / "Python-Course"

BASIC = [
    "01-Gioi-Thieu", "02-Cai-Dat-Python", "03-VSCode", "04-Bien",
    "05-Kieu-Du-Lieu", "06-Toan-Tu", "07-Input-Output", "08-Cau-Lenh-If",
    "09-Match-Case", "10-Vong-Lap-For", "11-Vong-Lap-While", "12-Ham",
    "13-Scope", "14-List", "15-Tuple", "16-Set", "17-Dictionary",
    "18-String", "19-Exception", "20-Module", "21-Package", "22-File",
    "23-OOP", "24-Dataclass", "25-Lambda", "26-List-Comprehension",
    "27-Generator", "28-Decorator", "29-Iterator",
]
PRACTICAL = [
    "01-Virtual-Environment", "02-Pip", "03-JSON", "04-CSV", "05-API",
    "06-Requests", "07-SQLite", "08-Logging", "09-Typing", "10-Asyncio",
    "11-Mini-Project", "12-Du-An-Cuoi-Khoa",
]
OLD_DIRS = [
    "01_Gioi_thieu", "02_Cai_dat_Python", "03_VSCode", "04_Bien",
    "05_Kieu_du_lieu", "06_Toan_tu", "07_Input_Output", "08_Cau_lenh_if",
    "09_Match_case", "10_Vong_lap_for", "11_Vong_lap_while", "12_Ham",
    "13_Scope", "14_List", "15_Tuple", "16_Set", "17_Dictionary",
    "18_String", "19_Exception", "20_Module", "21_Package", "22_File",
    "23_OOP", "24_Dataclass", "25_Lambda", "26_List_Comprehension",
    "27_Generator", "28_Decorator", "29_Iterator",
    "30_Virtual_Environment", "31_Pip", "32_JSON", "33_CSV", "34_API",
    "35_Requests", "36_SQLite", "37_Logging", "38_Typing", "39_Asyncio",
    "40_Mini_Project", "41_Du_an_Cuoi_Khoa",
]

# Phụ thuộc: số bài cũ -> danh sách số bài cũ cần học trước
PREREQ = {
    1: [], 2: [1], 3: [1, 2], 4: [1, 2, 3], 5: [4], 6: [4, 5],
    7: [1, 4], 8: [6, 7], 9: [8], 10: [6], 11: [10], 12: [8, 10, 11],
    13: [12], 14: [10, 12], 15: [14], 16: [14], 17: [14], 18: [5, 14],
    19: [12], 20: [12], 21: [20], 22: [20, 21], 23: [12, 14, 17],
    24: [23], 25: [12], 26: [10, 14], 27: [12, 26], 28: [12, 27],
    29: [27], 30: [1, 3], 31: [30], 32: [22], 33: [22], 34: [20, 32],
    35: [34], 36: [22, 32], 37: [12, 19], 38: [23, 25], 39: [12, 35],
}

PATH_MAP = {}   # số bài cũ -> (nhánh, thư mục mới)
for i, d in enumerate(OLD_DIRS[:29]):
    PATH_MAP[i + 1] = ("01-Co-Ban", BASIC[i])
for i, d in enumerate(OLD_DIRS[29:]):
    PATH_MAP[i + 30] = ("03-Thuc-Chien", PRACTICAL[i])

TITLES = {}     # số bài cũ -> tiêu đề


def read(p):
    return p.read_text(encoding="utf-8-sig")


def extract_title(path):
    """Trích tiêu đề từ dòng H1 đầu tiên của bai_giang.md
    (bỏ qua mọi emoji prefix, nhận cả ':' '–' '—' '-' sau số bài)."""
    first = read(path).splitlines()[0]
    m = re.match(r"^#.*?Bài\s*(\d+)\s*[:–—-]\s*(.+)$", first.strip())
    if m:
        return m.group(2).strip()
    return first.lstrip("# ").strip()


def strip_giang(text):
    """Bỏ H1, bỏ blockquote chương, bỏ phần 'Kết thúc bài' (link cũ).
    Trả về phần thân bắt đầu từ mục '##' đầu tiên."""
    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    start = None
    for i, ln in enumerate(lines):
        if ln.startswith("## "):
            start = i
            break
    if start is None:
        start = 0
    out = []
    for ln in lines[start:]:
        if ln.startswith("## 🏁"):
            break
        out.append(ln)
    body = "\n".join(out).strip()
    body = re.sub(r"(\n---\s*){2,}\n", "\n\n---\n\n", body)
    return body


def chapter_quote(text):
    """Trích blockquote 'Chương ...' ngay sau H1 của bai_giang."""
    lines = text.splitlines()[1:]
    quote = []
    for ln in lines:
        if ln.startswith("> "):
            quote.append(ln)
        elif quote:
            break
    return "\n".join(quote).strip()


def strip_tap(text):
    """Bỏ H1 + điều hướng trỏ tới dap_an.md; giữ chủ đề (blockquote) và bài tập."""
    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    quote = [ln for ln in lines if ln.startswith("> ")]
    start = None
    for i, ln in enumerate(lines):
        if ln.startswith("## ") and "Hướng dẫn" not in ln:
            start = i
            break
    if start is None:
        start = len(lines)
    body = "\n".join(lines[start:]).strip()
    body = "\n".join(
        ln for ln in body.splitlines()
        if "bai_giang.md" not in ln and "dap_an.md" not in ln
    ).strip()
    head = ""
    if quote:
        head = "> 📝 " + quote[0][2:].strip() + "\n\n"
    return head + body


def strip_an(text):
    """Bỏ H1 + blockquote đầu; trả về phần đáp án."""
    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    start = None
    for i, ln in enumerate(lines):
        if ln.startswith("## "):
            start = i
            break
    if start is None:
        for i, ln in enumerate(lines):
            if ln.strip() == "---":
                start = i + 1
                break
        if start is None:
            start = 0
    body = "\n".join(lines[start:]).strip()
    body = "\n".join(
        ln for ln in body.splitlines() if "dap_an.md" not in ln
    ).strip()
    return body


def fold_answers(text):
    """Bọc mỗi mục '### Bài N: ...' trong <details> riêng.
    Mục '##' (nhóm mức độ) giữ ngoài. Nếu không có '###' -> bọc toàn bộ."""
    lines = text.splitlines()
    has_ex = any(ln.startswith("### ") for ln in lines)
    if not has_ex:
        return ("<details>\n<summary>✅ Xem đáp án</summary>\n\n"
                + text + "\n\n</details>")

    out = ["## ✅ Đáp án", "", "> 💡 **Hãy tự làm bài tập trước** rồi mới mở đáp án.", ""]
    in_details = False
    for ln in lines:
        if ln.startswith("### "):
            if in_details:
                out.append("</details>")
                out.append("")
            title = ln[4:].strip()
            out.append("<details>")
            out.append(f"<summary>✅ {title}</summary>")
            out.append("")
            in_details = True
        elif ln.startswith("## "):
            if in_details:
                out.append("</details>")
                out.append("")
                in_details = False
            out.append(ln)
            out.append("")
        else:
            out.append(ln)
    if in_details:
        out.append("</details>")
    return "\n".join(out).strip()


def fix_old_links(text, current_branch):
    """Chép link cũ (../NN_dir/bai_giang.md ...) thành link mới theo cấu trúc 3 nhánh."""
    def repl(m):
        old_dir = m.group(2)
        if old_dir not in OLD_DIRS:
            return m.group(0)
        n = OLD_DIRS.index(old_dir) + 1
        tbranch, tfolder = PATH_MAP[n]
        if tbranch == current_branch:
            rel = f"../{tfolder}/bai.md"
        else:
            rel = f"../../{tbranch}/{tfolder}/bai.md"
        return f"({rel})"
    return re.sub(
        r"\(((?:\.\./)*)(\d{2}_[^/)]+)/bai_(?:giang|tap|an)\.md\)", repl, text
    )


def prereq_section(old_num):
    branch, folder = PATH_MAP[old_num]
    nums = PREREQ.get(old_num, [])
    if not nums:
        return ("## 🧠 Điều kiện tiên quyết\n\n"
                "Không cần kiến thức lập trình trước đó — bài này là điểm khởi đầu.")
    items = []
    for n in nums:
        tbranch, tfolder = PATH_MAP[n]
        if tbranch == branch:
            rel = f"../{tfolder}/bai.md"
        else:
            rel = f"../../{tbranch}/{tfolder}/bai.md"
        items.append(f"- [Bài {n} — {TITLES[n]}]({rel})")
    return "## 🧠 Điều kiện tiên quyết\n\n" + "\n".join(items)


def nav_section(old_num):
    branch, folder = PATH_MAP[old_num]
    parts = [f"**Vị trí:** `{branch}/{folder}/bai.md`", ""]
    if branch == "01-Co-Ban":
        if old_num == 29:
            parts.append(
                "🎉 **Bạn đã hoàn thành lộ trình Cơ bản!** Giờ bạn có thể chọn nhánh:\n"
                "- 🧮 [Nhánh 02 — Thuật Toán (HSG/CP)](../../02-Thuat-Toan/01-Tu-Duy-Thuat-Toan/bai.md)\n"
                "- 🚀 [Nhánh 03 — Thực Chiến (API/Package/Project)](../../03-Thuc-Chien/01-Virtual-Environment/bai.md)"
            )
        else:
            nxt = old_num + 1
            parts.append(f"**Bài tiếp theo:** [Bài {nxt} — {TITLES[nxt]}]"
                         f"(../{PATH_MAP[nxt][1]}/bai.md)")
    else:
        if old_num == 41:
            parts.append(
                "🏆 **Bạn đã hoàn thành lộ trình Thực chiến!** Hãy quay lại nhánh "
                "[02 — Thuật Toán](../../02-Thuat-Toan/01-Tu-Duy-Thuat-Toan/bai.md) "
                "nếu bạn muốn luyện tư duy giải thuật cho HSG."
            )
        else:
            nxt = old_num + 1
            parts.append(f"**Bài tiếp theo:** [Bài {nxt} — {TITLES[nxt]}]"
                         f"(../{PATH_MAP[nxt][1]}/bai.md)")
    return "## ➡️ Điều hướng\n\n" + "\n".join(parts)


def build_bai(old_num):
    d = OLD / OLD_DIRS[old_num - 1]
    raw = read(d / "bai_giang.md")
    tap = strip_tap(read(d / "bai_tap.md"))
    an = strip_an(read(d / "dap_an.md"))

    title = TITLES[old_num]
    quote = chapter_quote(raw)
    giang = strip_giang(raw)
    branch, folder = PATH_MAP[old_num]

    # chép link cũ trong nội dung giữ lại
    giang = fix_old_links(giang, branch)
    tap = fix_old_links(tap, branch)
    an = fix_old_links(an, branch)
    # xoá mọi dòng còn lại tham chiếu file cũ
    def drop_stale(text):
        return "\n".join(
            ln for ln in text.splitlines()
            if "bai_giang.md" not in ln and "bai_tap.md" not in ln
            and "dap_an.md" not in ln
        ).strip()
    giang = drop_stale(giang)
    tap = drop_stale(tap)
    an = drop_stale(an)

    parts = [f"# Bài {old_num} — {title}", ""]
    if quote:
        parts += [quote, ""]
    parts += [
        prereq_section(old_num),
        "",
        "---",
        "",
        giang,
        "",
        "---",
        "",
        "## 🧩 Bài tập",
        "",
        tap,
        "",
        "---",
        "",
        fold_answers(an),
        "",
        "---",
        "",
        nav_section(old_num),
        "",
    ]
    return branch, folder, "\n".join(parts)


def main():
    for n in range(1, 42):
        TITLES[n] = extract_title(OLD / OLD_DIRS[n - 1] / "bai_giang.md")

    created = []
    for n in range(1, 42):
        branch, folder, content = build_bai(n)
        target = ROOT / branch / folder
        target.mkdir(parents=True, exist_ok=True)
        (target / "bai.md").write_text(content, encoding="utf-8")
        created.append(f"{branch}/{folder}/bai.md")
    print(f"Đã tạo {len(created)} file bai.md")
    for c in created:
        print(" -", c)


if __name__ == "__main__":
    main()
