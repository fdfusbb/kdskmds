#!/usr/bin/env python3
from pathlib import Path

desktop = Path.home() / "Desktop"
target = desktop / "ggg.txt"

target.write_text("ggg\n", encoding="utf-8")
print(f"Created: {target}")
