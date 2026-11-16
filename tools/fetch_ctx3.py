# -*- coding: utf-8 -*-
"""Grep các chuỗi cần fix toàn cục: Thực Chiến, Nhánh, Dãy phẳng, 44 bài..."""
import re
from pathlib import Path

ROOT = Path(r"D:\HyperHub - HSG Tin")
OUT = Path(r"C:\Users\Mk2012\AppData\Local\Temp\opencode\fetch_ctx3.txt")
rep = []

pats = ["Thực Chiến", "thực chiến", "Nhánh ", "nhánh 0", "Dãy phẳng", "b1–b44", "44 bài", "b44)", "(Bài 44", "b43", "b44"]
for d in sorted([x for x in ROOT.iterdir() if x.is_dir() and re.match(r"^b\d{2}-", x.name)]):
    t = (d / "bai.md").read_text(encoding="utf-8").splitlines()
    for i, ln in enumerate(t, 1):
        for p in pats:
            if p in ln:
                rep.append(f"  {d.name}:{i}: {ln.strip()[:170]}")
                break

OUT.write_text("\n".join(rep), encoding="utf-8")
print("done", len(rep))
