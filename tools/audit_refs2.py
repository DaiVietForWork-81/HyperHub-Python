# -*- coding: utf-8 -*-
"""Audit toàn bộ tham chiếu 'Bài N' trong 44 bài — phân theo vùng (lý thuyết/bài tập/đáp án/nav).
Phục vụ renumber lần 2 (chèn b26 Vét Cạn + b30 Tần Suất)."""
import re
from pathlib import Path

ROOT = Path(r"D:\HyperHub - HSG Tin")
OUT = Path(r"C:\Users\Mk2012\AppData\Local\Temp\opencode\audit_refs2.txt")
rep = []

dirs = sorted([d for d in ROOT.iterdir() if d.is_dir() and re.match(r"^b\d{2}-", d.name)])
ref_re = re.compile(r"[Bb]ài (\d+)(?:\s*[–—-]\s*(\d+))?")

for d in dirs:
    f = d / "bai.md"
    lines = f.read_text(encoding="utf-8").splitlines()
    zone = "PRE"
    hits = []
    for i, ln in enumerate(lines, 1):
        s = ln.strip()
        if re.match(r"^## 🧩", s):
            zone = "EX"
            continue
        if re.match(r"^## ✅", s):
            zone = "ANS"
            continue
        if zone in ("ANS", "TAIL") and re.match(r"^## ", s) and not re.match(r"^##\s*(🟢|🟡|🔴|🟨|🟥|➕)", s):
            zone = "TAIL"
        if not s:
            continue
        if re.match(r"^#{2,4} ", s) and re.search(r"\(Bài \d+", s):
            continue  # tier header
        if s.startswith("<summary>"):
            continue
        if re.match(r"^### Bài \d+", s) or re.match(r"^\*\*Bài \d+", s) or re.match(r"^[-\s]*\*\*Bài \d+", s):
            continue
        for m in ref_re.finditer(s):
            n1 = int(m.group(1))
            n2 = int(m.group(2)) if m.group(2) else None
            hits.append((zone, n1, n2, i, s[:170]))
    rep.append(f"===== {d.name} =====")
    for zn, n1, n2, i, s in hits:
        if zn in ("PRE", "TAIL") and (n1 >= 20 or (n2 and n2 >= 20)):
            rep.append(f"  [{zn}] L{i} B{n1}{'-'+str(n2) if n2 else ''}: {s}")
        elif zn in ("EX", "ANS") and (n1 >= 13 or (n2 and n2 >= 13)):
            rep.append(f"  [{zn}] L{i} B{n1}{'-'+str(n2) if n2 else ''}: {s}")

OUT.write_text("\n".join(rep), encoding="utf-8")
print("done")
