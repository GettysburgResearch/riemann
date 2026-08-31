"""Replay an explicit, hash-locked programme panel, one fresh process per job.

Workflow evidence only: a green replay is not an independent mathematical proof.
Reports go to stdout; this runner never edits scientific files or fixtures.
"""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path


def sha(data):
    return hashlib.sha256(data).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def lf(data):
    return data.replace(b"\r\n", b"\n")


def git(repo, *args):
    return (
        subprocess.check_output(
            ["git", "--no-replace-objects", "-C", str(repo), *args],
            stderr=subprocess.STDOUT,
        )
        .decode()
        .strip()
    )


def authenticate(repo, panel):
    if panel.get("schema") != "sixhour-pass3-explicit-replay-panel-v1":
        raise ValueError("wrong panel schema")
    rows = panel["modules"]
    if not rows or len({r["test"] for r in rows}) != len(rows):
        raise ValueError("empty or duplicate test panel")
    result = {}
    for row in rows:
        if row["runtime"] not in ("system", "flint"):
            raise ValueError("unknown runtime")
        for key in ("test", "producer"):
            name = row[key]
            path = (repo / name).resolve()
            if not path.is_relative_to(repo) or not path.is_file():
                raise ValueError("invalid or missing panel path: " + name)
            digest = sha(lf(path.read_bytes()))
            if digest != row[key + "_sha256_lf"]:
                raise ValueError("source changed: " + name)
            result[name] = digest
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", required=True)
    ap.add_argument("--panel", required=True)
    ap.add_argument("--system-python", required=True)
    ap.add_argument("--flint-python")
    ap.add_argument("--optimized", action="store_true")
    args = ap.parse_args()
    runner_bytes = Path(__file__).read_bytes()
    repo = Path(args.repo).resolve()
    panel_path = Path(args.panel).resolve()
    panel_bytes = panel_path.read_bytes()
    panel = json.loads(panel_bytes)
    initial = authenticate(repo, panel)
    head_before = git(repo, "rev-parse", "HEAD")
    interpreter = {"system": args.system_python, "flint": args.flint_python}
    versions = {}
    for name in sorted({r["runtime"] for r in panel["modules"]}):
        executable = interpreter[name]
        if not executable or not Path(executable).is_file():
            raise ValueError("missing interpreter: " + name)
        versions[name] = {
            "path": str(Path(executable).resolve()),
            "version": subprocess.check_output(
                [executable, "-B", "-c", "import sys; print(sys.version)"]
            )
            .decode()
            .strip(),
        }
    records = []
    total_tests = 0
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    for index, row in enumerate(panel["modules"], 1):
        prefix = [interpreter[row["runtime"]], "-B"]
        if args.optimized:
            prefix.append("-O")
        commands = [
            (
                "tests",
                prefix
                + [
                    "-m",
                    "unittest",
                    "discover",
                    "-s",
                    "tests",
                    "-p",
                    Path(row["test"]).name,
                ],
            ),
            ("producer_check", prefix + [row["producer"], "--check"]),
        ]
        for kind, command in commands:
            start = time.monotonic()
            proc = subprocess.run(
                command,
                cwd=repo,
                env=env,
                capture_output=True,
                timeout=3600,
                check=False,
            )
            output = proc.stdout + b"\n" + proc.stderr
            matches = re.findall(rb"Ran (\d+) tests? in ", output)
            count = int(matches[-1]) if matches else None
            passed = proc.returncode == 0
            if kind == "tests":
                passed = passed and count is not None and count > 0
                total_tests += count or 0
            record = {
                "test": row["test"],
                "kind": kind,
                "runtime": row["runtime"],
                "command": command,
                "exit_code": proc.returncode,
                "tests_run": count if kind == "tests" else None,
                "elapsed_seconds": round(time.monotonic() - start, 3),
                "stdout_sha256": sha(proc.stdout),
                "stderr_sha256": sha(proc.stderr),
                "status": "PASS" if passed else "FAIL",
            }
            if not passed:
                record["failure_tail"] = output[-6000:].decode(errors="replace")
            records.append(record)
            print(
                f"{index}/{len(panel['modules'])} {kind} "
                f"{Path(row['test']).name}: {record['status']} "
                f"({record['elapsed_seconds']}s; tests={record['tests_run']})",
                flush=True,
            )
    final = authenticate(repo, panel)
    if initial != final or panel_path.read_bytes() != panel_bytes:
        raise ValueError("panel inputs changed during replay")
    if Path(__file__).read_bytes() != runner_bytes:
        raise ValueError("runner changed during replay")
    report = {
        "schema": "sixhour-pass3-programme-replay-v1",
        "programme": panel["programme"],
        "panel_science_head": panel["science_head"],
        "panel_sha256_lf": sha(lf(panel_bytes)),
        "runner_sha256_lf": sha(lf(runner_bytes)),
        "observed_head_before": head_before,
        "observed_head_after": git(repo, "rev-parse", "HEAD"),
        "optimized": args.optimized,
        "interpreters": versions,
        "module_count": len(panel["modules"]),
        "total_tests": total_tests,
        "producer_checks": len(panel["modules"]),
        "all_science_input_hashes_unchanged": initial == final,
        "status": "PASS" if all(r["status"] == "PASS" for r in records) else "FAIL",
        "records": records,
        "boundary": "Exact declared test/producer input hashes only; fixtures and sources are checked by their producers. Analytic proof review remains separate.",
    }
    print("BEGIN_FINAL_REPLAY_JSON", flush=True)
    print(json.dumps(report, sort_keys=True, indent=2), flush=True)
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
