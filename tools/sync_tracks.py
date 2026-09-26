# -*- coding: utf-8 -*-
"""Đồng bộ các track học tự chứa (generated copies) từ bản chính.

Nguồn chính (sửa ở đây):
  01-Co-Ban/          29 bài cơ bản
  02-Thuat-Toan/      19 bài thuật toán (chỉ thư mục gốc, không gồm Phan-1)
  03-Thuc-Chien/      12 bài thực chiến

Bản copy tự động (KHÔNG sửa trực tiếp — sửa bản chính rồi chạy script này):
  02-Thuat-Toan/Phan-1-Co-Ban/   copy 29 bài cơ bản (mục thuật toán tự chứa)
  04-Full/Phan-1-Co-Ban/         copy 29 bài cơ bản
  04-Full/Phan-2-Thuat-Toan/     copy 19 bài thuật toán
  04-Full/Phan-3-Thuc-Chien/     copy 12 bài thực chiến

Script copy file, viết lại link tương đối cho đúng vị trí mới, và gắn
dòng đánh dấu generated ở đầu file. Chạy lại bất cứ lúc nào (idempotent).
"""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARK = ("<!-- TỰ ĐỘNG ĐỒNG BỘ từ {src} — đừng sửa trực tiếp, "
        "sửa bản chính rồi chạy tools/sync_tracks.py -->\n\n")


def copy_track(src_branch, dest_dir, link_rules, pos_old, pos_new):
    """Copy toàn bộ bai.md từ src_branch sang dest_dir, viết lại link."""
    dest = ROOT / dest_dir
    if dest.exists():
        shutil.rmtree(dest)
    count = 0
    for src_file in sorted((ROOT / src_branch).glob("*/bai.md")):
        lesson = src_file.parent.name
        target_dir = dest / lesson
        target_dir.mkdir(parents=True, exist_ok=True)
        text = src_file.read_text(encoding="utf-8")
        for old, new in link_rules:
            text = text.replace(old, new)
        text = text.replace("`" + pos_old, "`" + pos_new)
        rel_src = src_file.relative_to(ROOT).as_posix()
        text = MARK.format(src=rel_src) + text
        (target_dir / "bai.md").write_text(text, encoding="utf-8")
        count += 1
    print(f"  {dest_dir}: {count} file")


def main():
    print("Đồng bộ các track...")
    # Mục thuật toán: cơ bản + thuật toán (thuật toán giữ nguyên ở gốc 02)
    copy_track(
        "01-Co-Ban", "02-Thuat-Toan/Phan-1-Co-Ban",
        link_rules=[
            ("](../../02-Thuat-Toan/", "](../"),
        ],
        pos_old="01-Co-Ban/",
        pos_new="02-Thuat-Toan/Phan-1-Co-Ban/",
    )
    # Mục full: cả 3 phần
    copy_track(
        "01-Co-Ban", "04-Full/Phan-1-Co-Ban",
        link_rules=[
            ("](../../01-Co-Ban/", "](../"),
            ("](../../02-Thuat-Toan/", "](../Phan-2-Thuat-Toan/"),
            ("](../../03-Thuc-Chien/", "](../Phan-3-Thuc-Chien/"),
        ],
        pos_old="01-Co-Ban/",
        pos_new="04-Full/Phan-1-Co-Ban/",
    )
    copy_track(
        "02-Thuat-Toan", "04-Full/Phan-2-Thuat-Toan",
        link_rules=[
            ("](../../01-Co-Ban/", "](../Phan-1-Co-Ban/"),
            ("](../../02-Thuat-Toan/", "](../"),
            ("](../../03-Thuc-Chien/", "](../Phan-3-Thuc-Chien/"),
        ],
        pos_old="02-Thuat-Toan/",
        pos_new="04-Full/Phan-2-Thuat-Toan/",
    )
    copy_track(
        "03-Thuc-Chien", "04-Full/Phan-3-Thuc-Chien",
        link_rules=[
            ("](../../01-Co-Ban/", "](../Phan-1-Co-Ban/"),
            ("](../../02-Thuat-Toan/", "](../Phan-2-Thuat-Toan/"),
            ("](../../03-Thuc-Chien/", "](../"),
        ],
        pos_old="03-Thuc-Chien/",
        pos_new="04-Full/Phan-3-Thuc-Chien/",
    )
    print("Xong.")


if __name__ == "__main__":
    main()
