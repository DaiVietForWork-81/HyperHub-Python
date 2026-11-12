# -*- coding: utf-8 -*-
"""Validator cho cấu trúc phẳng b01..b44."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []
warnings = []

md_files = [p for p in ROOT.rglob("*.md")]

for p in md_files:
    try:
        text = p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        errors.append(f"[ENCODE] Không đọc được UTF-8: {p.relative_to(ROOT)}")
        continue
    rel = p.relative_to(ROOT)

    # 1. Link tương đối hỏng
    for m in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", text):
        target = m.group(1).strip()
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        target = target.split("#")[0]
        if not target:
            continue
        resolved = (p.parent / target).resolve()
        if not resolved.exists():
            errors.append(f"[LINK] {rel}: link hỏng -> {target}")

    # 2. Code fence cân bằng
    fences = len(re.findall(r"^\s*```", text, re.M))
    if fences % 2 != 0:
        errors.append(f"[FENCE] {rel}: code fence lẻ ({fences})")

    # 3. <details> đóng đủ
    opens = len(re.findall(r"^<details>", text, re.M))
    closes = len(re.findall(r"^</details>", text, re.M))
    if opens != closes:
        errors.append(f"[DETAILS] {rel}: <details>={opens} != </details>={closes}")

    # 4. Tiêu đề H1
    h1 = [ln for ln in text.splitlines() if ln.startswith("# ")]
    if not h1:
        warnings.append(f"[H1] {rel}: thiếu tiêu đề H1")
    elif not re.match(r"^# Bài \d+ — ", h1[0]):
        warnings.append(f"[H1] {rel}: H1 không theo định dạng -> {h1[0][:60]}")

# 5. Mỗi thư mục bài học có đúng 1 bai.md
lesson_dirs = [d for d in ROOT.iterdir() if d.is_dir() and d.name.startswith("b") and d.name[1:3].isdigit()]
for d in sorted(lesson_dirs):
    md_in_dir = list(d.glob("*.md"))
    if len(md_in_dir) == 0:
        errors.append(f"[FILE] {d.name}: thiếu bai.md")
    elif len(md_in_dir) > 1:
        warnings.append(f"[FILE] {d.name}: thừa file {md_in_dir}")

print("=== LỖI ===")
if errors:
    for e in errors:
        print(" ", e)
else:
    print("  Không có lỗi!")
print("=== CẢNH BÁO ===")
if warnings:
    for w in warnings:
        print(" ", w)
else:
    print("  Không có cảnh báo!")
print(f"\nTổng: {len(md_files)} file .md, {len(lesson_dirs)} thư mục bài, {len(errors)} lỗi, {len(warnings)} cảnh báo")