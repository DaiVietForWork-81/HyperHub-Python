# -*- coding: utf-8 -*-
"""Quét các dòng bảng '| NN. ' và các ref cũ còn sót (Thực Chiến, JSON, CSV, pip...) trong toàn bộ bài."""
import re
from pathlib import Path

ROOT = Path(r"D:\HyperHub - HSG Tin")
OUT = Path(r"C:\Users\Mk2012\AppData\Local\Temp\opencode\scan_tablerows.txt")
rep = []

dirs = sorted([d for d in ROOT.iterdir() if d.is_dir() and re.match(r"^b\d{2}-", d.name)])
for d in dirs:
    f = d / "bai.md"
    t = f.read_text(encoding="utf-8").splitlines()
    for i, ln in enumerate(t, 1):
        s = ln.strip()
        if re.match(r"^\| \d{1,2}\. ", s):
            rep.append(f"TAB {d.name}:{i}: {s[:150]}")
        if re.search(r"Thực Chiến|Virtual Environment|pytest|SQLite|\bGit\b|requests|API key", s) and "Thực Chiến" not in "":
            if "thực chiến" in s.lower() or "Thực Chiến" in s:
                pass
        if re.search(r"JSON|CSV|pip\b|try/except", s) and re.search(r"bài \d+|Bài \d+", s):
            rep.append(f"OLD {d.name}:{i}: {s[:150]}")

# riêng: quét 'Thực Chiến'
for d in dirs:
    f = d / "bai.md"
    t = f.read_text(encoding="utf-8").splitlines()
    for i, ln in enumerate(t, 1):
        if "Thực Chiến" in ln or "thực chiến" in ln:
            rep.append(f"TC  {d.name}:{i}: {ln.strip()[:150]}")

OUT.write_text("\n".join(rep), encoding="utf-8")
print("done", len(rep))
