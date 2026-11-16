# -*- coding: utf-8 -*-
"""Audit 3: ref 'bài N' sót từ flatten (lowercase / bài đã lược) — N trong 3..29, mọi vùng."""
import re
from pathlib import Path

ROOT = Path(r"D:\HyperHub - HSG Tin")
OUT = Path(r"C:\Users\Mk2012\AppData\Local\Temp\opencode\audit_refs3.txt")
rep = []

dirs = sorted([d for d in ROOT.iterdir() if d.is_dir() and re.match(r"^b\d{2}-", d.name)])
ref_re = re.compile(r"[Bb]ài (\d+)")
KEY = re.compile(r"(dataclass|ngoại lệ|exception|package|match|vscode|visual|decorator|iterator|từ điển|dictionary|chuỗi|string|tập hợp|set\b|dict\b|lớp dữ liệu)", re.I)

for d in dirs:
    f = d / "bai.md"
    lines = f.read_text(encoding="utf-8").splitlines()
    zone = "PRE"
    out_lines = []
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
        if re.match(r"^#{2,4} ", s) and re.search(r"\(Bài \d+", s):
            continue
        if s.startswith("<summary>"):
            continue
        if re.match(r"^### Bài \d+", s) or re.match(r"^\*\*Bài \d+", s) or re.match(r"^[-\s]*\*\*Bài \d+", s):
            continue
        for m in ref_re.finditer(s):
            n = int(m.group(1))
            if n > 29:
                continue
            lowcase = s[m.start():m.start()+4].startswith("bài")
            if lowcase or KEY.search(s):
                out_lines.append(f"  [{zone}] L{i} B{n}: {s[:180]}")
    if out_lines:
        rep.append(f"===== {d.name} =====")
        rep.extend(out_lines)

OUT.write_text("\n".join(rep), encoding="utf-8")
print("done", len(rep))
