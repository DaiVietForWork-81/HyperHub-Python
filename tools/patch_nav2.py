# -*- coding: utf-8 -*-
"""Patch chính xác các link prereq còn lỗi."""
from pathlib import Path

ROOT = Path(r"D:\HyperHub - HSG Tin")

# 1. b03-Bien: xoá dòng prereq VSCode
p = ROOT / "b03-Bien" / "bai.md"
text = p.read_text(encoding="utf-8")
# Xoá dòng: - [Bài 3 — Visual Studio Code – Môi Trường Viết Code](../03-VSCode/bai.md)
text = text.replace("- [Bài 3 — Visual Studio Code – Môi Trường Viết Code](../03-VSCode/bai.md)\n", "")
p.write_text(text, encoding="utf-8", newline="\n")
print("Patched b03 prereq VSCode")

# 2. b18-File: xoá dòng prereq Package
p = ROOT / "b18-File" / "bai.md"
text = p.read_text(encoding="utf-8")
text = text.replace("- [Bài 21 — Package Trong Python](../21-Package/bai.md)\n", "")
p.write_text(text, encoding="utf-8", newline="\n")
print("Patched b18 prereq Package")

# 3. b23-Regex: ensure nav next exists
p = ROOT / "b23-Regex" / "bai.md"
text = p.read_text(encoding="utf-8")
if "**Bài tiếp theo:**" not in text:
    # Thêm nav vào cuối section "## ➡️ Điều hướng"
    nav_add = """

**Bài tiếp theo:** [Bài 24 — Tư Duy Thuật Toán](../b24-Tu-Duy-Thuat-Toan/bai.md)

👉 Tiếp theo: **[Bài 24: Tư Duy Thuật Toán](../b24-Tu-Duy-Thuat-Toan/bai.md)**"""
    text = text.replace("**Vị trí:** `b23-Regex/bai.md`", "**Vị trí:** `b23-Regex/bai.md`" + nav_add)
    p.write_text(text, encoding="utf-8", newline="\n")
    print("Patched b23 nav next")
else:
    print("b23 nav already exists")

print("Done")