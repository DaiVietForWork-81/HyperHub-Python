# -*- coding: utf-8 -*-
"""Kiểm tra toàn vẹn khóa học:
- Link tương đối hỏng trong file .md
- Tham chiếu tới file đã xóa (bai_giang.md / bai_tap.md / dap_an.md)
- Mỗi thư mục bài học có đúng 1 file bai.md
- Khối code fence cân bằng
- Khối <details> đóng đủ
- Tiêu đề H1 đúng định dạng
"""
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

    # 2. Tham chiếu file đã xóa — chỉ tính link điều hướng thật ([...](...)),
    # việc nhắc tên file trong văn bản (mô tả validator...) là hợp lệ
    for m in re.finditer(r"\[[^\]]*\]\(([^)]*(?:bai_giang|bai_tap|dap_an)\.md[^)]*)\)", text):
        errors.append(f"[STALE] {rel}: link tới file cũ -> {m.group(1)}")

    # 3. Code fence cân bằng
    fences = len(re.findall(r"^\s*```", text, re.M))
    if fences % 2 != 0:
        errors.append(f"[FENCE] {rel}: code fence lẻ ({fences})")

    # 4. <details> đóng đủ (chỉ đếm tag ở đầu dòng)
    opens = len(re.findall(r"^<details>", text, re.M))
    closes = len(re.findall(r"^</details>", text, re.M))
    if opens != closes:
        errors.append(f"[DETAILS] {rel}: <details>={opens} != </details>={closes}")

    # 5. Tiêu đề H1: bài học phải đúng "Bài N — ...", tài liệu khác chỉ cần có H1
    h1 = [ln for ln in text.splitlines() if ln.startswith("# ")]
    if not h1:
        warnings.append(f"[H1] {rel}: thiếu tiêu đề H1")
        continue
    in_branch = str(rel).startswith(("01-Co-Ban", "02-Thuat-Toan", "03-Thuc-Chien"))
    if in_branch and not re.match(r"^# Bài \d+ — ", h1[0]):
        warnings.append(f"[H1] {rel}: H1 không theo định dạng -> {h1[0][:60]}")

# 6. Mỗi thư mục bài học có đúng 1 bai.md
for branch in ("01-Co-Ban", "02-Thuat-Toan", "03-Thuc-Chien"):
    b = ROOT / branch
    if not b.exists():
        errors.append(f"[DIR] Thiếu nhánh: {branch}")
        continue
    for lesson in sorted(b.iterdir()):
        if not lesson.is_dir():
            continue
        files = list(lesson.glob("*.md"))
        if "bai.md" not in [f.name for f in files]:
            errors.append(f"[FILE] {branch}/{lesson.name}: thiếu bai.md")
        extra = [f.name for f in files if f.name != "bai.md"]
        if extra:
            warnings.append(f"[FILE] {branch}/{lesson.name}: file thừa {extra}")

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
print(f"\nTổng: {len(md_files)} file .md, {len(errors)} lỗi, {len(warnings)} cảnh báo")
