# -*- coding: utf-8 -*-
"""Debug merge_data function."""
import sys
from pathlib import Path

ROOT = Path(r"D:\HyperHub - HSG Tin")
sys.path.insert(0, str(ROOT / "tools"))
import sections_data as sd

# Check all DATA_* attributes
for name in dir(sd):
    if name.startswith("DATA_"):
        obj = getattr(sd, name)
        print(f"{name}: type={type(obj)}, len={len(obj) if hasattr(obj, '__len__') else 'N/A'}")

# Check merge_data
data = {}
for name in dir(sd):
    if name.startswith("DATA_") and name not in ("DATA_PREREQS",):
        obj = getattr(sd, name)
        print(f"Merging {name}: type={type(obj)}")
        if isinstance(obj, dict):
            data.update(obj)

print(f"\nTotal merged entries: {len(data)}")
for k, v in list(data.items())[:5]:
    print(f"  {k}: type={type(v)}, keys={list(v.keys()) if isinstance(v, dict) else 'not dict'}")

# Check if any values are lists
list_entries = [(k, v) for k, v in data.items() if isinstance(v, list)]
if list_entries:
    print("\nLIST ENTRIES FOUND:")
    for k, v in list_entries:
        print(f"  {k}: {v[:3]}...")
else:
    print("\nNo list entries in merged data")