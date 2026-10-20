"""Replay this packet's finite checks; never certify its analytic claims.

Python standard library only.  Run: python -I -S -B replay.py
The exact-check scripts run in ordinary and optimized mode, sequentially
for each script because some regenerate their own receipts.
"""
from pathlib import Path
from hashlib import sha256
import ast
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
CHECKERS = (
    "type_i/verify_type_i.py",
    "type_i/verify_profile_closure.py",
    "type_i/verify_numerator_barriers.py",
    "mixed/audit_cusp_minor.py",
    "mixed/check_marked_exponents.py",
    "mixed/check_quadratic_pair.py",
    "global/check_residue_algebra.py",
    "scalar/verify_tangent.py",
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def canonical(data):
    return json.dumps(data, sort_keys=True, separators=(",", ":")).encode("utf-8")


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    manifest_path = ROOT / "MANIFEST.json"
    require(manifest_path.is_file(), "Missing frozen source MANIFEST.json")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for relative, expected in manifest["source_sha256"].items():
        path = (ROOT / relative).resolve()
        require(path.is_relative_to(ROOT), "Manifest path escapes packet")
        require(path.is_file(), f"Missing source: {relative}")
        require(digest(path) == expected, f"Source hash changed: {relative}")

    results = []
    for relative in CHECKERS:
        path = ROOT / relative
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=relative)
        require(not any(isinstance(node, ast.Assert) for node in ast.walk(tree)),
                f"Acceptance checks disabled by -O in {relative}")
        variants = []
        for optimized in (False, True):
            args = [sys.executable, "-I", "-S", "-B"]
            if optimized:
                args.append("-O")
            args.append(str(path))
            run = subprocess.run(args, cwd=ROOT, capture_output=True,
                                 text=True, encoding="utf-8", timeout=180)
            require(run.returncode == 0,
                    f"{relative} failed (optimized={optimized}): {run.stderr}")
            require(not run.stderr.strip(), f"Unexpected diagnostic: {run.stderr}")
            receipt = json.loads(run.stdout)
            require(str(receipt.get("status", "")).lower() == "pass",
                    f"Non-passing receipt: {relative}")
            variants.append(receipt)
        require(canonical(variants[0]) == canonical(variants[1]),
                f"Ordinary/optimized receipts differ: {relative}")
        results.append({
            "checker": relative,
            "checker_sha256": digest(path),
            "normal_and_optimized_identical": True,
            "result_canonical_sha256": sha256(canonical(variants[0])).hexdigest(),
            "result": variants[0],
        })
        print(f"PASS {relative}")

    report = {
        "status": "pass",
        "scope": "Finite algebra and explicit coverage only; not analytic or zero-free certification.",
        "source_manifest_sha256": digest(manifest_path),
        "source_files_checked": len(manifest["source_sha256"]),
        "checkers": results,
        "excluded_exploration": "mixed/probe_centered_canonical.py is a numerical exploration, not an exact acceptance check.",
    }
    (ROOT / "REPLAY_RESULTS.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"PASS {len(results)} checkers in both modes; analytic inputs remain assumed.")


if __name__ == "__main__":
    main()
