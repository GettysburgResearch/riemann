#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, subprocess, sys

root = Path(__file__).resolve().parents[2]

def run(script):
    proc = subprocess.run([sys.executable, str(root / script)], cwd=root, capture_output=True, text=True)
    if proc.returncode != 0:
        print(proc.stdout)
        print(proc.stderr, file=sys.stderr)
        raise SystemExit(f"failed: {script}")
    return proc.stdout.strip().splitlines()[-1] if proc.stdout.strip() else ""

def verify_sha(directory, ledger_name="SHA256SUMS"):
    directory = root / directory
    ledger = directory / ledger_name
    checked = 0
    for line in ledger.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        digest, rel = line.split("  ", 1)
        p = directory / rel
        actual = hashlib.sha256(p.read_bytes()).hexdigest()
        if actual != digest:
            raise SystemExit(f"checksum mismatch: {p}")
        checked += 1
    return checked

mellin = run("canonical/consumers/mellin-landau/validate_consumer.py")
integration = run("integration/2026-08-22/validate_integration.py")
checks = {
    "mellin": verify_sha("canonical/consumers/mellin-landau"),
    "canonical": verify_sha("canonical/2026-08-22"),
    "integration": verify_sha("integration/2026-08-22"),
}
result = {
    "status": "PASS_2026_08_22_FINAL_INTEGRATION_PACKAGE",
    "rh_status": "UNPROVED",
    "proven_only_path_to_rh": False,
    "heavy_campaigns_rerun": False,
    "validator_outputs": {"mellin": mellin, "integration": integration},
    "checksum_entries": checks,
}
out = Path(__file__).resolve().parent / "results.json"
out.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
