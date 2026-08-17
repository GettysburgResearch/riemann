#!/usr/bin/env python3
from pathlib import Path
import hashlib
import sys

root = Path(__file__).resolve().parents[2]
manifest = root / "T97200_CONTENT_SHA256SUMS"
ok = True
for line in manifest.read_text(encoding="utf-8").splitlines():
    digest, rel = line.split("  ", 1)
    got = hashlib.sha256((root / rel).read_bytes()).hexdigest()
    if got != digest:
        print(f"FAIL {rel}: {got} != {digest}")
        ok = False
print("PASS_T97200_PACKET_CONTENT" if ok else "FAIL_T97200_PACKET_CONTENT")
sys.exit(0 if ok else 1)
