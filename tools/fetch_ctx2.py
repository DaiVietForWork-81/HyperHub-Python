# -*- coding: utf-8 -*-
"""Lấy chính xác các dòng cần replace + tìm nguồn 'mỗi học sinh là một dict'."""
import re
from pathlib import Path

ROOT = Path(r"D:\HyperHub - HSG Tin")
OUT = Path(r"C:\Users\Mk2012\AppData\Local\Temp\opencode\fetch_ctx2.txt")
rep = []

def show(name, a, b):
    f = ROOT / name / "bai.md"
    lines = f.read_text(encoding="utf-8").splitlines()
    rep.append(f"##### {name} [{a}..{b}] (total {len(lines)})")
    for j in range(a - 1, min(len(lines), b)):
        rep.append(f"{j+1}: {lines[j]}")
    rep.append("")

show("b24-Tu-Duy-Thuat-Toan", 104, 112)
show("b42-Chien-Luoc-Thi-HSG", 74, 90)
show("b44-Ly-Thuyet-Tro-Choi", 590, 596)
show("b01-Gioi-Thieu", 1213, 1216)
show("b25-Do-Phuc-Tap", 677, 682)
show("b28-Stack-Queue-Hashing", 691, 696)

rep.append("===== grep 'học sinh là một dict' =====")
for d in sorted([x for x in ROOT.iterdir() if x.is_dir() and re.match(r"^b\d{2}-", x.name)]):
    t = (d / "bai.md").read_text(encoding="utf-8")
    for i, ln in enumerate(t.splitlines(), 1):
        if "một dict" in ln or ("Nhắc lại" in ln and "Bài" in ln):
            rep.append(f"  {d.name}:{i}: {ln.strip()[:160]}")

OUT.write_text("\n".join(rep), encoding="utf-8")
print("done")
