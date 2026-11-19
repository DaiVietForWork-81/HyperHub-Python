# -*- coding: utf-8 -*-
import re
from pathlib import Path

ROOT = Path(r"D:\HyperHub - HSG Tin")

for lesson_dir in sorted(ROOT.iterdir()):
    if not (lesson_dir.is_dir() and re.match(r'b\d{2}-', lesson_dir.name)):
        continue
    f = lesson_dir / "bai.md"
    if not f.exists():
        continue
    text = f.read_text(encoding="utf-8")
    
    ex_match = re.search(r'## 🧩 Bài tập', text)
    ans_match = re.search(r'## ✅ Đáp án', text)
    
    if ex_match and ans_match:
        section = text[ex_match.end():ans_match.start()]
        exercises = [l for l in section.split('\n') if l.strip().startswith('### Bài ')]
        print(f"{lesson_dir.name}: {len(exercises)} exercises")
    else:
        print(f"{lesson_dir.name}: NO MATCH - ex_match={bool(ex_match)}, ans_match={bool(ans_match)}")