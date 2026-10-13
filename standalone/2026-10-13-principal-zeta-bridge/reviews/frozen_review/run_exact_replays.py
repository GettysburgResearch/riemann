#!/usr/bin/env python3
"""Independent execution receipt for three already extracted frozen checkers.

This driver does not decide the analytic review. It reruns the declared finite
diagnostics in ordinary and optimized Python and records their exact output.
"""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "source"
REPLAY = HERE / "replay"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_case(kind, optimized):
    script = SOURCE / "checks" / f"check_{kind}.py"
    mode = "optimized" if optimized else "normal"
    output = REPLAY / f"{kind}_{mode}.json"
    cmd = [sys.executable]
    if optimized:
        cmd.append("-O")
    cmd.append(str(script))
    if kind == "native_heat_defect":
        cmd += ["--proof", str(SOURCE / "NATIVE_HEAT_DEFECT_AND_PRIME_REMOVAL.md"),
                "--output", str(output)]
    run = subprocess.run(cmd, capture_output=True, check=False)
    require(run.returncode == 0, f"{kind}/{mode} failed: {run.stderr.decode()}")
    result = json.loads(run.stdout)
    require(result.get("status") == "PASS", f"{kind}/{mode} did not declare PASS")
    if kind != "native_heat_defect":
        output.write_bytes(run.stdout)
    report = json.loads(output.read_bytes())
    require(report.get("status") == "PASS", f"{kind}/{mode} report failed")
    if kind == "native_heat_defect":
        require(report["proof_sha256"] == sha(SOURCE / "NATIVE_HEAT_DEFECT_AND_PRIME_REMOVAL.md"),
                "heat proof binding failed")
        require(report["checker_sha256"] == sha(script), "heat checker binding failed")
    return {"kind": kind, "mode": mode, "checker_sha256": sha(script),
            "report": output.name, "report_sha256": sha(output), "result": report}


def main():
    extraction = json.loads((HERE / "extraction.json").read_text())
    for entry in extraction["files"]:
        relative = entry["path"].split("standalone/2026-10-13-principal-zeta-bridge/", 1)[1]
        require(sha(SOURCE / relative) == entry["sha256"], "frozen extraction changed")
    jobs = [(kind, optimized)
            for kind in ("periodic_transfer", "abelian_companions", "native_heat_defect")
            for optimized in (False, True)]
    with ThreadPoolExecutor(max_workers=6) as executor:
        futures = [executor.submit(run_case, *job) for job in jobs]
        results = [future.result() for future in futures]
    for kind, _ in jobs[::2]:
        normal = REPLAY / f"{kind}_normal.json"
        optimized = REPLAY / f"{kind}_optimized.json"
        require(normal.read_bytes() == optimized.read_bytes(),
                f"{kind} changed under optimized Python")
    receipt = {"status": "PASS", "source_commit": extraction["commit"],
               "source_tree": extraction["tree"], "driver_sha256": sha(Path(__file__)),
               "normal_optimized_byte_identical": True, "runs": results,
               "scope": "Independent execution of author finite checkers; not an analytic proof or external peer review."}
    output = REPLAY / "exact_replay_receipt.json"
    output.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "runs": len(results),
                      "receipt_sha256": sha(output),
                      "normal_optimized_byte_identical": True}, sort_keys=True))


if __name__ == "__main__":
    main()
