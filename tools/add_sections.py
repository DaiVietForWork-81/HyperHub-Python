# -*- coding: utf-8 -*-
"""Chèn 'thẻ nhóm', 'Bài tập về nhà', 'Tra cứu nhanh' vào từng bài (data-driven).

Dữ liệu: tools/sections_data.py → DATA[folder] = {tag, homework, tracuu_title, tracuu}
- Idempotent: mục nào đã có thì bỏ qua.
- Lưu ý: tools/sections_data*.py chỉ là dữ liệu, không sửa khi không cần.

Dùng: python tools/add_sections.py [--apply]
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import sections_data as sd  # noqa: E402  (nạp DATA gộp)

APPLY = "--apply" in sys.argv
FOLDERS = sorted([d.name for d in ROOT.iterdir() if d.is_dir() and re.match(r"^b\d{2}-", d.name)])

def merge_data():
    data = {}
    for name in dir(sd):
        if name.startswith("DATA"):
            data.update(getattr(sd, name))
    return data

def main():
    data = merge_data()
    n_tag = n_hw = n_tc = 0
    skipped = []
    for folder in FOLDERS:
        item = data.get(folder)
        if not item:
            skipped.append(folder)
            continue
        f = ROOT / folder / "bai.md"
        text = f.read_text(encoding="utf-8")
        orig = text

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

    print(("APPLY " if APPLY else "DRY ") + f"tag={n_tag} homework={n_hw} tracuu={n_tc}")
    if skipped:
        print("Không có dữ liệu / bỏ qua:", ", ".join(skipped))

if __name__ == "__main__":
    main()
