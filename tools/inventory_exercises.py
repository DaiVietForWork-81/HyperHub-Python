# -*- coding: utf-8 -*-
"""Kiểm kê cấu trúc bài tập/đáp án của 44 bài — phục vụ rework nội dung."""
import re
from pathlib import Path

ROOT = Path(r"D:\HyperHub - HSG Tin")
OUT = Path(r"C:\Users\Mk2012\AppData\Local\Temp\opencode\inventory.txt")
rep = []

lesson_dirs = sorted([d for d in ROOT.iterdir() if d.is_dir() and re.match(r"^b\d{2}-", d.name)])

for d in lesson_dirs:
    f = d / "bai.md"
    text = f.read_text(encoding="utf-8")
    lines = text.splitlines()
    h1 = next((ln for ln in lines if ln.startswith("# ")), "?")
    ex_start = ans_start = None
    for i, ln in enumerate(lines):
        if ex_start is None and re.match(r"^## 🧩", ln):
            ex_start = i
        if ans_start is None and re.match(r"^## ✅", ln):
            ans_start = i
    rep.append(f"### {d.name}")
    rep.append(f"  H1: {h1}")
    if ex_start is None or ans_start is None:
        rep.append(f"  !! MISSING ex_start={ex_start} ans_start={ans_start}")
        rep.append("")
        continue
    ex_zone = lines[ex_start:ans_start]
    tail = lines[ans_start:]
    ans_zone = [tail[0]]
    end_ans = len(tail)
    for j, ln in enumerate(tail[1:], start=1):
        if re.match(r"^## ", ln) and not re.match(r"^##\s*(🟢|🟡|🔴|🟨|🟥|➕)", ln):
            end_ans = j
            break
        ans_zone.append(ln)

    def nums(zone, pats):
        found = []
        for ln in zone:
            for p in pats:
                m = re.match(p, ln)
                if m:
                    found.append(int(m.group(1)))
                    break
        return found

    ex_nums = nums(ex_zone, [r"^### Bài (\d+)", r"^\*\*Bài (\d+)", r"^[-\s]*\*\*Bài (\d+)"])
    ans_nums = nums(ans_zone, [r"^<summary>.*?B[àa]i (\d+)"])
    set_ex, set_ans = sorted(set(ex_nums)), sorted(set(ans_nums))
    rep.append(f"  EX items: {len(ex_nums)} (unique {len(set_ex)}) | range {set_ex[0] if set_ex else '-'}..{set_ex[-1] if set_ex else '-'}")
    rep.append(f"  ANS items: {len(ans_nums)} (unique {len(set_ans)}) | range {set_ans[0] if set_ans else '-'}..{set_ans[-1] if set_ans else '-'}")
    if set_ex != set_ans:
        rep.append(f"  !! EX vs ANS mismatch: ex-only={sorted(set(set_ex)-set(set_ans))} ans-only={sorted(set(set_ans)-set(set_ex))}")
    tiers_ex = [ln.strip() for ln in ex_zone if re.match(r"^#{2,3} .*(🟢|🟡|🔴|🟨|🟥|➕)", ln)]
    tiers_ans = [ln.strip() for ln in ans_zone if re.match(r"^#{2,3} .*(🟢|🟡|🔴|🟨|🟥|➕)", ln)]
    rep.append(f"  tiers EX: {tiers_ex}")
    rep.append(f"  tiers ANS: {tiers_ans}")
    tail_heads = [ln.strip() for ln in tail[end_ans:] if re.match(r"^## ", ln)]
    rep.append(f"  tail heads: {tail_heads}")
    m = re.search(r"Sau (\d+) bài tập", text)
    if m:
        rep.append(f"  'Sau {m.group(1)} bài tập'")
    if "Tra cứu" in text:
        rep.append("  !! Da co chu 'Tra cứu'")
    rep.append("")

OUT.write_text("\n".join(rep), encoding="utf-8")
print("done", len(lesson_dirs), "lessons")
