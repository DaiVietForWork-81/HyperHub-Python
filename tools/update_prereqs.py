# -*- coding: utf-8 -*-
"""Tự động nạp prerequisites từ 46 bài vào sections_data.py, sau đó chạy add_sections.py"""
import re
import sys
from pathlib import Path

ROOT = Path(r"D:\HyperHub - HSG Tin")
sys.path.insert(0, str(ROOT / "tools"))
import sections_data as sd

# Trích prerequisites từ bài học
def extract_prereqs():
    from pathlib import Path
    ROOT = Path(r"D:\HyperHub - HSG Tin")
    prereqs = {}
    for d in sorted(ROOT.iterdir()):
        if d.is_dir() and re.match(r'b\d{2}-', d.name):
            f = d / 'bai.md'
            if f.exists():
                text = f.read_text(encoding='utf-8')
                if 'Điều kiện tiên quyết' in text:
                    lines = text.split('\n')
                    in_section = False
                    items = []
                    for line in lines:
                        if 'Điều kiện tiên quyết' in line:
                            in_section = True
                            continue
                        if in_section:
                            if line.strip().startswith('---'):
                                break
                            if line.strip().startswith('- [Bài'):
                                # Extract lesson reference
                                m = re.search(r'\[Bài (\d+) — ([^\]]+)\]', line)
                                if m:
                                    items.append(f"Bài {m.group(1)} — {m.group(2)}")
                            elif line.strip().startswith('Không cần'):
                                items.append(line.strip())
                    if items:
                        prereqs[d.name] = items
    return prereqs

# Mapping folder name -> prerequisites text
PREREQS = {
    "b01-Gioi-Thieu": ["Không cần kiến thức lập trình trước đó — bài này là điểm khởi đầu."],
    "b02-Cai-Dat-Python": ["Bài 1 — Giới Thiệu Python"],
    "b03-Bien": ["Bài 1 — Giới Thiệu Python", "Bài 2 — Cài Đặt Python"],
    "b04-Kieu-Du-Lieu": ["Bài 3 — Biến Trong Python"],
    "b05-Toan-Tu": ["Bài 3 — Biến Trong Python", "Bài 4 — Kiểu Dữ Liệu Cơ Bản"],
    "b06-Input-Output": ["Bài 1 — Giới Thiệu Python", "Bài 3 — Biến Trong Python"],
    "b07-Cau-Lenh-If": ["Bài 5 — Toán Tử Trong Python", "Bài 6 — Nhập và Xuất Dữ Liệu"],
    "b08-Vong-Lap-For": ["Bài 5 — Toán Tử Trong Python"],
    "b09-Vong-Lap-While": ["Bài 8 — Vòng Lặp For – Lặp Lại Một Số Lần Biết Trước"],
    "b10-Ham": ["Bài 7 — Câu Lệnh If – Cấu Trúc Rẽ Nhánh", "Bài 8 — Vòng Lặp For – Lặp Lại Một Số Lần Biết Trước", "Bài 9 — Vòng Lặp While – Lặp Cho Đến Khi Điều Kiện Sai"],
    "b11-Scope": ["Bài 10 — Hàm (Function) Trong Python"],
    "b12-List": ["Bài 8 — Vòng Lặp For – Lặp Lại Một Số Lần Biết Trước", "Bài 10 — Hàm (Function) Trong Python"],
    "b13-Tuple": ["Bài 12 — Danh Sách (List) Trong Python"],
    "b14-Set": ["Bài 12 — Danh Sách (List) Trong Python"],
    "b15-Dictionary": ["Bài 12 — Danh Sách (List) Trong Python"],
    "b16-String": ["Bài 4 — Kiểu Dữ Liệu Cơ Bản", "Bài 12 — Danh Sách (List) Trong Python"],
    "b17-Module": ["Bài 10 — Hàm (Function) Trong Python"],
    "b18-File": ["Bài 17 — Module Trong Python"],
    "b19-OOP": ["Bài 10 — Hàm (Function) Trong Python", "Bài 12 — Danh Sách (List) Trong Python", "Bài 15 — Dictionary (Từ Điển) Trong Python"],
    "b20-Lambda": ["Bài 10 — Hàm (Function) Trong Python"],
    "b21-List-Comprehension": ["Bài 8 — Vòng Lặp For – Lặp Lại Một Số Lần Biết Trước", "Bài 12 — Danh Sách (List) Trong Python"],
    "b22-Generator": ["Bài 10 — Hàm (Function) Trong Python", "Bài 21 — List Comprehension – Vòng Lặp \"Viết Trong Một Dòng\""],
    "b23-Regex": ["Bài 16 — Chuỗi (String)", "Bài 8 — Vòng Lặp For"],
    "b24-Tu-Duy-Thuat-Toan": ["Bài 10 — Hàm (Function)", "Bài 8 — Vòng Lặp For", "Bài 9 — Vòng Lặp While", "Bài 12 — List"],
    "b25-Do-Phuc-Tap": ["Bài 24 — Tư Duy Thuật Toán", "Bài 10 — Hàm (Function)", "Bài 8 — Vòng Lặp For"],
    "b26-Vet-Can": ["Bài 24 — Tư Duy Thuật Toán", "Bài 25 — Độ Phức Tạp & Big-O", "Bài 8 — Vòng Lặp For", "Bài 12 — Danh Sách (List)"],
    "b27-Tim-Kiem": ["Bài 25 — Độ Phức Tạp & Big-O", "Bài 8 — Vòng Lặp For", "Bài 9 — Vòng Lặp While", "Bài 12 — List"],
    "b28-Sap-Xep": ["Bài 27 — Tìm Kiếm", "Bài 25 — Độ Phức Tạp", "Bài 8 — Vòng Lặp For", "Bài 12 — List"],
    "b29-Stack-Queue-Hashing": ["Bài 25 — Độ Phức Tạp", "Bài 12 — List", "Bài 15 — Dictionary"],
    "b30-Tan-Suat": ["Bài 29 — Stack, Queue & Hashing", "Bài 15 — Dictionary (Từ Điển)", "Bài 14 — Set (Tập Hợp)", "Bài 8 — Vòng Lặp For"],
    "b31-De-Quy": ["Bài 10 — Hàm", "Bài 29 — Stack, Queue & Hashing", "Bài 28 — Sắp Xếp"],
    "b32-Quay-Lui": ["Bài 31 — Đệ Quy", "Bài 10 — Hàm", "Bài 12 — List"],
    "b33-Hai-Con-Tro": ["Bài 27 — Tìm Kiếm", "Bài 28 — Sắp Xếp", "Bài 29 — Stack, Queue & Hashing"],
    "b34-Tham-Lam": ["Bài 28 — Sắp Xếp", "Bài 25 — Độ Phức Tạp", "Bài 24 — Tư Duy Thuật Toán"],
    "b35-Quy-Hoach-Dong": ["Bài 31 — Đệ Quy (đặc biệt memoization + lru_cache)", "Bài 32 — Quay Lui", "Bài 34 — Tham Lam (biết khi tham lam sai → DP)", "Bài 12 — List"],
    "b36-Toan-Hoc-So-Hoc": ["Bài 31 — Đệ Quy (lũy thừa nhanh, Euclid đệ quy)", "Bài 25 — Độ Phức Tạp", "Bài 8 — Vòng Lặp For"],
    "b37-Do-Thi-BFS-DFS": ["Bài 29 — Stack, Queue & Hashing (deque, visited-set)", "Bài 31 — Đệ Quy", "Bài 25 — Độ Phức Tạp"],
    "b38-Duong-Di-Ngan-Nhat": ["Bài 37 — Đồ Thị: BFS & DFS", "Bài 29 — Stack, Queue & Hashing (heapq, deque)", "Bài 25 — Độ Phức Tạp"],
    "b39-Cay-Va-DSU": ["Bài 37 — Đồ Thị: BFS & DFS", "Bài 38 — Đường Đi Ngắn Nhất (Dijkstra, heap)", "Bài 28 — Sắp Xếp"],
    "b40-Segment-Tree": ["Bài 31 — Đệ Quy", "Bài 25 — Độ Phức Tạp", "Bài 28 — Sắp Xếp (đếm nghịch thế — sẽ làm lại bằng BIT)"],
    "b41-Xu-Ly-Chuoi": ["Bài 16 — String (cơ bản chuỗi Python)", "Bài 25 — Độ Phức Tạp", "Bài 29 — Stack, Queue & Hashing (dict, hashing)"],
    "b42-Bitmask": ["Bài 32 — Quay Lui (bitmask duyệt tập con)", "Bài 35 — Quy Hoạch Động", "Bài 25 — Độ Phức Tạp"],
    "b43-DP-Nang-Cao": ["Bài 35 — Quy Hoạch Động (5 bước, lăn mảng)", "Bài 37 — Đồ Thị (topo DAG)", "Bài 39 — Cây & DSU (DFS cây, tập độc lập)", "Bài 31 — Đệ Quy (memo, lru_cache)"],
    "b44-Chien-Luoc-Thi-HSG": ["Toàn bộ Bài 24–46 phần Thuật Toán (đặc biệt Bài 24 — tư duy, Bài 25 — Big-O)"],
    "b45-Itertools": ["Bài 33 — Hai Con Trỏ (duyệt thông minh)", "Bài 32 — Quay Lui (liệt kê thủ công — giờ học cách liệt kê có sẵn!)", "Bài 10 — Hàm"],
    "b46-Ly-Thuyet-Tro-Choi": ["Bài 35 — Quy Hoạch Động (truy hồi + memo — Grundy chính là DP!)", "Bài 42 — Bitmask (XOR ^ dùng hằng ngày ở đây)", "Bài 31 — Đệ Quy"],
}

import re

def build_prereq_text(folder):
    items = PREREQS.get(folder, [])
    if not items:
        return ""
    lines = []
    for item in items:
        # Try to find the folder for referenced lessons
        # For now, just output as plain list with relative links where possible
        lines.append(f"- {item}")
    return "\n".join(lines)

# Update sections_data.py
def update_sections_data():
    sections_file = ROOT / "tools" / "sections_data.py"
    content = sections_file.read_text(encoding="utf-8")
    
    # We'll append a new DATA_PREREQS dict at the end before the closing }
    # First, let's create the prerequisites data as a dict to be merged
    
    prereq_dict = {}
    for folder, items in PREREQS.items():
        if folder in [d.name for d in ROOT.iterdir() if d.is_dir() and re.match(r'b\d{2}-', d.name)]:
            prereq_dict[folder] = items
    
    # Generate Python dict string
    lines = ["\n# ================= PREREQUISITES FOR ALL 46 LESSONS =================\n", "DATA_PREREQS = {"]
    for folder, items in sorted(prereq_dict.items()):
        lines.append(f'    "{folder}": {repr(items)},')
    lines.append("}\n")
    
    new_content = content.rstrip() + "\n" + "\n".join(lines) + "\n"
    sections_file.write_text(new_content, encoding="utf-8")
    print(f"Added prerequisites for {len(prereq_dict)} lessons")

if __name__ == "__main__":
    update_sections_data()