# -*- coding: utf-8 -*-
"""In ngữ cảnh (±5 dòng) cho các ref cần quyết định khi fix."""
from pathlib import Path

ROOT = Path(r"D:\HyperHub - HSG Tin")
OUT = Path(r"C:\Users\Mk2012\AppData\Local\Temp\opencode\fetch_ctx.txt")

PLACES = [
    ("b01-Gioi-Thieu", [1214]),
    ("b05-Toan-Tu", [900, 1211]),
    ("b07-Cau-Lenh-If", [1477]),
    ("b08-Vong-Lap-For", [1188, 1201, 1288]),
    ("b09-Vong-Lap-While", [1263, 1303, 1403, 1658]),
    ("b15-Dictionary", [780]),
    ("b18-File", [29]),
    ("b19-OOP", [31]),
    ("b20-Lambda", [249]),
    ("b22-Generator", [989, 1365]),
    ("b24-Tu-Duy-Thuat-Toan", [137]),
    ("b25-Do-Phuc-Tap", [647]),
    ("b30-Quay-Lui", [271]),
    ("b42-Chien-Luoc-Thi-HSG", [337]),
]

rep = []
for name, lns in PLACES:
    f = ROOT / name / "bai.md"
    lines = f.read_text(encoding="utf-8").splitlines()
    for ln in lns:
        rep.append(f"##### {name} L{ln}")
        for j in range(max(0, ln - 6), min(len(lines), ln + 5)):
            mark = ">>" if j + 1 == ln else "  "
            rep.append(f"{mark} {j+1}: {lines[j][:170]}")
        rep.append("")

OUT.write_text("\n".join(rep), encoding="utf-8")
print("done", len(rep))
