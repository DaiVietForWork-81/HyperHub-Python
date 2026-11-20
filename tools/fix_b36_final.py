# -*- coding: utf-8 -*-
from pathlib import Path

f = Path(r"D:\HyperHub - HSG Tin\b36-Toan-Hoc-So-Hoc\bai.md")
text = f.read_text(encoding="utf-8")

lines = text.split("\n")

# Fix H1
if lines[0].startswith("# "):
    lines[0] = "# Bài 36 — Toán Học & Số Học Thuật Toán"

# Fix banner and tag
for i, line in enumerate(lines):
    if "📚 **Dãy phẳng" in line and "�" in line:
        lines[i] = "> 📚 **Dãy phẳng b1–b46 — Nền tảng + Thuật toán**"
    if "🏷️ **Nhóm bài:**" in line and "�" in line:
        lines[i] = "> 🏷️ **Nhóm bài:** Chuyên đề · Toán học & số học thuật toán"

new_text = "\n".join(lines)
f.write_text("\n".join(lines), encoding="utf-8", newline="\n")
print("Fixed b36 completely")