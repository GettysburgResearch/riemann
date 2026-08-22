#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, subprocess
from pathlib import Path
root = Path(__file__).resolve().parent
for line in (root / "SHA256SUMS").read_text().splitlines():
    if not line.strip():
        continue
    want, rel = line.split("  ", 1)
    got = hashlib.sha256((root / rel).read_bytes()).hexdigest()
    if got != want:
        raise SystemExit(f"hash mismatch: {rel}")
tmp = root / ".tmp.json"
try:
    subprocess.run([
        "python3",
        str(root / "experiments/X-102600-completion-defect/verify.py"),
        "--output", str(tmp)
    ], check=True)
    retained = root / "experiments/X-102600-completion-defect/results/verification.json"
    if tmp.read_bytes() != retained.read_bytes():
        raise SystemExit("replay mismatch")
finally:
    tmp.unlink(missing_ok=True)
lock = json.loads((root / "integration/2026-08-22/t102600-source-lock.json").read_text())
assert lock["rh_established"] is False
print("PASS_DETERMINISTIC_T102600_PACKET")
