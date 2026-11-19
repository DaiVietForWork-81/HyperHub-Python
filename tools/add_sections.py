# -*- coding: utf-8 -*-
"""Chèn 'thẻ nhóm', 'Bài tập về nhà', 'Tra cứu nhanh', 'Điều kiện tiên quyết' vào từng bài (data-driven).

Dữ liệu: tools/sections_data.py → DATA[folder] = {tag, homework, tracuu_title, tracuu}
- Idempotent: mục nào đã có thì bỏ qua.
- Lưu ý: tools/sections_data*.py chỉ là dữ liệu, không sửa khi không cần.

Dùng: python tools/add_sections.py [--apply]
"""
import re
import sys
import importlib
from pathlib import Path

print("SCRIPT STARTED", flush=True)

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

APPLY = "--apply" in sys.argv
FOLDERS = sorted([d.name for d in ROOT.iterdir() if d.is_dir() and re.match(r"^b\d{2}-", d.name)])

def load_sections_data():
    """Load and reload sections_data module to get fresh data."""
    import sections_data as sd
    importlib.reload(sd)
    return sd

def merge_data(sd):
    data = {}
    for name in dir(sd):
        if name.startswith("DATA_") and name not in ("DATA_PREREQS",):
            obj = getattr(sd, name)
            if isinstance(obj, dict):
                data.update(obj)
    # Add prerequisites to each lesson
    if hasattr(sd, 'DATA_PREREQS'):
        for folder, prereqs in sd.DATA_PREREQS.items():
            if folder in data:
                data[folder]["prerequisites"] = prereqs
            else:
                data[folder] = {"prerequisites": prereqs}
    return data

def inject_prerequisites(text, folder, prereq_items):
    """Cập nhật/Thêm mục 'Điều kiện tiên quyết' với danh sách prerequisites từ data."""
    if not prereq_items:
        return text
    
    # Build the prerequisite list markdown
    prereq_lines = []
    for item in prereq_items:
        # Try to convert to link if it references another lesson
        # Pattern: "Bài N — Title" or just text
        m = re.match(r"Bài (\d+) — (.+)", item)
        if m:
            num = int(m.group(1))
            title = m.group(2)
            # Find target folder
            target_folder = None
            for d in sorted(ROOT.iterdir()):
                if d.is_dir() and d.name.startswith(f"b{num:02d}-"):
                    target_folder = d.name
                    break
            if target_folder:
                prereq_lines.append(f"- [Bài {num} — {title}](../{target_folder}/bai.md)")
            else:
                prereq_lines.append(f"- Bài {num} — {title}")
        elif item.startswith("Không cần") or "không cần" in item.lower():
            prereq_lines.append(f"- {item}")
        elif item.startswith("Toàn bộ"):
            prereq_lines.append(f"- {item}")
        else:
            prereq_lines.append(f"- {item}")
    
    prereq_block = "\n".join(prereq_lines)
    
    # Check if section already exists
    if "## 🧠 Điều kiện tiên quyết" in text:
        # Replace the content between "## 🧠 Điều kiện tiên quyết" and next "---" or "## "
        pattern = r"(## 🧠 Điều kiện tiên quyết\n\n)(.*?)(\n---|\n## )"
        def repl(m):
            return m.group(1) + prereq_block + "\n\n" + m.group(3)
        text = re.sub(pattern, repl, text, flags=re.DOTALL)
    else:
        # Insert after banner (first line starting with > 📚)
        banner_pattern = r"(^> 📚 \*\*Dãy phẳng[^\n]*\*\*$)"
        m = re.search(banner_pattern, text, re.MULTILINE)
        if m:
            insert_pos = m.end()
            block = f"\n\n## 🧠 Điều kiện tiên quyết\n\n{prereq_block}\n\n---\n\n"
            text = text[:insert_pos] + block + text[insert_pos:]
    
    return text

def main():
    import sections_data as sd
    data = {}
    for name in dir(sd):
        if name.startswith("DATA"):
            data.update(getattr(sd, name))
    
    print("MODULE LEVEL: Starting", flush=True)
APPLY = "--apply" in sys.argv
FOLDERS = sorted([d.name for d in ROOT.iterdir() if d.is_dir() and re.match(r"^b\d{2}-", d.name)])
print(f"MODULE LEVEL: APPLY={APPLY}, FOLDERS={len(FOLDERS)}", flush=True)

def main():
        print("DEBUG: main() started", flush=True)
        sd = load_sections_data()
        print("DEBUG: sections_data loaded", flush=True)
        data = merge_data(sd)
        print(f"DEBUG: data keys = {list(data.keys())[:5]}", flush=True)
        n_tag = n_hw = n_tc = n_pre = 0
        skipped = []
        
        for folder in FOLDERS:
            item = data.get(folder)
            if not item:
                skipped.append(folder)
                continue
            f = ROOT / folder / "bai.md"
            text = f.read_text(encoding="utf-8")
            orig = text

            # 0) Prerequisites — inject/update before tag
            prereq_items = item.get("prerequisites", [])
            if prereq_items:
                text = inject_prerequisites(text, folder, prereq_items)
                n_pre += 1

        # 1) thẻ nhóm — chèn ngay sau dòng banner
        tag = item.get("tag")
        if tag and "🏷️ **Nhóm bài:**" not in text:
            m = re.search(r"^> 📚 \*\*Dãy phẳng[^\n]*\*\*$", text, re.M)
            if m:
                text = text[:m.end()] + f"\n\n> 🏷️ **Nhóm bài:** {tag}" + text[m.end():]
                n_tag += 1
            else:
                skipped.append(f"{folder} (no banner)")

        # 2) Bài tập về nhà — chèn trước Điều hướng
        hw = item.get("homework")
        if hw and "## 🏠 Bài tập về nhà" not in text:
            anchor = "## ➡️ Điều hướng"
            idx = text.find(anchor)
            if idx > 0:
                block = ("## 🏠 Bài tập về nhà\n\n"
                         "> 📝 Làm vào vở (hoặc nộp GV). Đáp án chi tiết sẽ bổ sung trong đợt hoàn thiện.\n\n"
                         f"{hw.strip()}\n\n---\n\n")
                text = text[:idx] + block + text[idx:]
                n_hw += 1
            else:
                skipped.append(f"{folder} (no nav)")

        # 3) Tra cứu nhanh — chèn trước Điều hướng (sau homework nếu có)
        tc_title = item.get("tracuu_title")
        tc = item.get("tracuu")
        if tc and "## 📎 Tra cứu nhanh" not in text:
            anchor = "## ➡️ Điều hướng"
            idx = text.find(anchor)
            if idx > 0:
                block = (f"## 📎 Tra cứu nhanh — {tc_title}\n\n"
                         f"{tc.strip()}\n\n---\n\n")
                text = text[:idx] + block + text[idx:]
                n_tc += 1

        if APPLY and text != orig:
            f.write_text(text, encoding="utf-8", newline="\n")

        print(("APPLY " if APPLY else "DRY ") + f"tag={n_tag} homework={n_hw} tracuu={n_tc} prereq={n_pre}")
        if skipped:
            print("Không có dữ liệu / bỏ qua:", ", ".join(skipped))

if __name__ == "__main__":
    main()
