# -*- coding: utf-8 -*-
"""Debug merge_data function."""
import sys
from pathlib import Path

ROOT = Path(r"D:\HyperHub - HSG Tin")
sys.path.insert(0, str(ROOT / "tools"))
import sections_data as sd

data = {}
for name in dir(sd):
    if name.startswith("DATA_") and name not in ("DATA_PREREQS",):
        obj = getattr(sd, name)
        print(f"Found {name}: type={type(obj)}")
        if isinstance(obj, dict):
            print(f"  keys: {list(obj.keys())[:5]}")
            data.update(obj)

print(f"\nTotal merged entries: {len(data)}")
for k in sorted(data.keys()):
    v = data[k]
    print(f"  {k}: type={type(v)}, keys={list(v.keys()) if isinstance(v, dict) else 'not dict'}")

# Check prerequisites
if hasattr(sd, 'DATA_PREREQS'):
    print(f"\nDATA_PREREQS type: {type(sd.DATA_PREREQS)}")
    print(f"Keys: {list(sd.DATA_PREREQS.keys())[:5]}")

# Test merge
for folder, prereqs in sd.DATA_PREREQS.items():
    if folder in data:
        data[folder]["prerequisites"] = prereqs
        print(f"  Added prereqs to {folder}: {len(prereqs)} items")
    else:
        print(f"  Missing folder in data: {folder}")

print("\nFinal check:")
for k, v in list(data.items())[:5]:
    print(f"  {k}: type={type(v)}, has_prereq={'prerequisites' in v if isinstance(v, dict) else 'not dict'}")