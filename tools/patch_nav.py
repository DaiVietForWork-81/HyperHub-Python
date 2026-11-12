# -*- coding: utf-8 -*-
"""Patch các nav/prereq còn lỗi sau flatten."""
import re
from pathlib import Path

ROOT = Path(r"D:\HyperHub - HSG Tin")

# 1. b03-Bien: xoá prereq VSCode (line 9)
p = ROOT / "b03-Bien" / "bai.md"
text = p.read_text(encoding="utf-8")
text = re.sub(r"^- \[Bài 3 - Visual Studio Code.*?\n", "", text, flags=re.M)
p.write_text(text, encoding="utf-8", newline="\n")
print("Patched b03 prereq")

# 2. b18-File: xoá prereq Package (line 8)
p = ROOT / "b18-File" / "bai.md"
text = p.read_text(encoding="utf-8")
text = re.sub(r"^- \[Bài 21 - Package.*?\n", "", text, flags=re.M)
p.write_text(text, encoding="utf-8", newline="\n")
print("Patched b18 prereq")

# 3. b07-If: nav next should point to b08-For (not b09-Match-Case which was skipped)
# Check current nav
p = ROOT / "b07-Cau-Lenh-If" / "bai.md"
text = p.read_text(encoding="utf-8")
# The nav next currently might point to b09-Match-Case or b08-For
text = re.sub(r"\*\*Bài tiếp theo:\*\* \[Bài 8 — [^\]]*\]\([^)]+\)",
              "**Bài tiếp theo:** [Bài 8 — Vòng Lặp For – Lặp Lại Một Số Lần Biết Trước](../b08-Vong-Lap-For/bai.md)", text)
text = re.sub(r"👉 Tiếp theo: \*\*\[Bài 8: [^\]]*\]\([^)]+\)\*\*",
              "👉 Tiếp theo: **[Bài 8: Vòng Lặp For – Lặp Lại Một Số Lần Biết Trước](../b08-Vong-Lap-For/bai.md)**", text)
p.write_text(text, encoding="utf-8", newline="\n")
print("Patched b07 nav")

# 4. b23-Regex: add nav next to b24
p = ROOT / "b23-Regex" / "bai.md"
text = p.read_text(encoding="utf-8")
# Find the "## ➡️ Điều hướng" section and add nav next
nav_section = """## ➡️ Điều hướng

**Vị trí:** `b23-Regex/bai.md`

**Bài tiếp theo:** [Bài 24 — Tư Duy Thuật Toán](../b24-Tu-Duy-Thuat-Toan/bai.md)

👉 Tiếp theo: **[Bài 24: Tư Duy Thuật Toán](../b24-Tu-Duy-Thuat-Toan/bai.md)**"""
# Replace existing nav section
text = re.sub(r"## ➡️ Điều hướng\s*\n\s*\*\*Vị trí:\*\* `b23-Regex/bai\.md`\s*\n\s*",
              nav_section + "\n\n", text)
p.write_text(text, encoding="utf-8", newline="\n")
print("Patched b23 nav")

# 5. b22-Generator: verify nav is correct (already b23)
print("b22 nav already correct")

print("Done patching")