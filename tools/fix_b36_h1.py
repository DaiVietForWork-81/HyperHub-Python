# -*- coding: utf-8 -*-
from pathlib import Path

f = Path(r"D:\HyperHub - HSG Tin\b36-Toan-Hoc-So-Hoc\bai.md")
text = f.read_text(encoding="utf-8")

# Fix H1
text = text.replace("# Bài 36 — Toán Học & Số Học Thuật Toán", "# Bài 36 — Toán Học & Số Học Thuật Toán")
# The issue is the H1 has mojibake in it
text = text.replace("# B�i 36 \u2014 To\u00e1n H\u1ecd\u00e3c & S\u1ed1 H\u1ecd\u00e3c Thu\u1eadt To\u00e1n", "# Bài 36 — Toán Học & Số Học Thuật Toán")

f.write_text(text, encoding="utf-8", newline="\n")
print("Fixed b36 H1")