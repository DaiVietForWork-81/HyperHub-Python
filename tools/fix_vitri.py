# -*- coding: utf-8 -*-
"""Sửa dòng 'Vị trí' về đúng tên thư mục hiện tại (fix double-shift)."""
import re
from pathlib import Path

ROOT = Path(r"D:\HyperHub - HSG Tin")
VI_TRI_RE = re.compile(r"\*\*Vị trí:\*\* `b\d{2}-[^`]+`")
n_fixed = 0
for d in sorted(ROOT.iterdir()):
    if not d.is_dir() or not re.match(r"^b\d{2}-", d.name):
        continue
    f = d / "bai.md"
    t = f.read_text(encoding="utf-8")
    new = VI_TRI_RE.sub(f"**Vị trí:** `{d.name}/bai.md`", t)
    if new != t:
        f.write_text(new, encoding="utf-8", newline="\n")
        n_fixed += 1
print("fixed", n_fixed, "files")
