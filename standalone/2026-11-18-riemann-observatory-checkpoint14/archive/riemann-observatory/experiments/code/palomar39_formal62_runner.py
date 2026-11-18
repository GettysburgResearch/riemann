"""Bounded stages for pinned local Palomar Solution and theorem type/axiom verification."""
import argparse
import datetime
import fcntl
from hashlib import file_digest
import json
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import sys
import time

from replay_839_later_windows import ROOT, save


PROJECT_PIN = "ee2a8a32be49a4f73c7386e9dffdea24d7e3d8c0"
MATHLIB_PIN = "065356127b1dc0016f66b7283ce0ce2c4055aa55"
LEAN_PIN = "11acb17ec6b07a8f9e9173e6845197929540936b"
QUERY = ROOT / "experiments/code/Palomar39Formal62Axioms.lean"
DECLARATIONS = {"GuthMaynardStatement.global_uniform", "GuthMaynardStatement.middle_large_values"}
STANDARD = {"propext", "Classical.choice", "Quot.sound"}


def digest(path):
    with path.open("rb") as stream:
        return file_digest(stream, "sha256").hexdigest()


def git(path, *args):
    return subprocess.check_output(["git", "-C", str(path), *args], text=True).strip()


def verify_pins(repo, project, mathlib, lean):
    assert git(repo, "rev-parse", "HEAD") == PROJECT_PIN
    assert git(mathlib, "rev-parse", "HEAD") == MATHLIB_PIN
    assert not git(repo, "status", "--porcelain", "--untracked-files=no")
    assert not git(mathlib, "status", "--porcelain", "--untracked-files=no")
    version = subprocess.check_output([str(lean), "--version"], text=True)
    assert "version 4.35.0-rc2" in version and LEAN_PIN in version
    for package in json.loads((project / "lake-manifest.json").read_text())["packages"]:
        package_repo = project / ".lake/packages" / package["name"]
        assert git(package_repo, "rev-parse", "HEAD") == package["rev"]
        assert not git(package_repo, "status", "--porcelain", "--untracked-files=no")


def cgroup():
    counters = Path("/sys/fs/cgroup/memory.events")
    return dict(line.split() for line in counters.read_text().splitlines()) if counters.exists() else {}


def monitor(command, project, env, log, status_file, report, lock, stage, min_free, max_time):
    start = time.monotonic()
    start_memory = cgroup()
    with log.open("x") as stream:
        proc = subprocess.Popen(command, cwd=project, env=env, stdout=stream, stderr=subprocess.STDOUT,
                                start_new_session=True, pass_fds=(lock.fileno(),))
    terminal_reason = None
    record = {"command": command, "pid": proc.pid, "started_with_memory_events": start_memory,
              "log_filename": log.name, "state": "running"}
    if stage in report:
        report.setdefault("previous_stage_attempts", []).append({"stage": stage, **report[stage]})
    report[stage] = record
    report["status"] = f"{stage}_running"
    save(status_file, report)
    while proc.poll() is None:
        record["elapsed_seconds"] = round(time.monotonic() - start, 3)
        record["disk_free_bytes"] = shutil.disk_usage(project).free
        if record["disk_free_bytes"] < min_free:
            terminal_reason = "disk_free_below_measured_guard"
        elif record["elapsed_seconds"] > max_time:
            terminal_reason = "time_budget_reached"
        elif stage == "solution_build":
            builds = re.findall(r"\] Built Mathlib(?:\.[^ ]+)? \(", log.read_text())
            record["local_mathlib_source_builds_observed"] = len(builds)
            if len(builds) > 10:
                terminal_reason = "unexpected_mathlib_source_fallback"
        if terminal_reason:
            try:
                os.killpg(proc.pid, signal.SIGTERM)
                proc.wait(timeout=5)
            except ProcessLookupError:
                pass
            except subprocess.TimeoutExpired:
                os.killpg(proc.pid, signal.SIGKILL)
            break
        save(status_file, report)
        time.sleep(15)
    code = proc.wait(timeout=5)
    record.update(state="completed" if code == 0 else "stopped", exit_code=code, stop_reason=terminal_reason,
                  elapsed_seconds=round(time.monotonic() - start, 3), log_sha256=digest(log),
                  final_memory_events=cgroup(), disk_free_bytes=shutil.disk_usage(project).free)
    report["status"] = f"{stage}_completed" if code == 0 else f"{stage}_stopped"
    save(status_file, report)
    return code


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=("cache", "build"))
    parser.add_argument("--base", type=Path, required=True)
    parser.add_argument("--status", type=Path, required=True)
    parser.add_argument("--build-seconds", type=int, default=3600)
    args = parser.parse_args()
    base = args.base.resolve()
    repo = base / "zeta-density-39-over-17-lean"
    project = repo / "lean"
    mathlib = project / ".lake/packages/mathlib"
    toolchain = base / "lean-4.35.0-rc2-linux/bin"
    lean, lake = toolchain / "lean", toolchain / "lake"
    env = os.environ.copy()
    env.update(PATH=str(toolchain) + os.pathsep + env["PATH"], LEAN_NUM_THREADS="2",
               MATHLIB_CACHE_DIR=str(base / "downloaded-mathlib-cache"))
    with (base / "palomar_formal62.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        verify_pins(repo, project, mathlib, lean)
        report = json.loads(args.status.read_text())
        tag = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
        if args.stage == "cache":
            probe = base / "mathlib_cache_probe.log"
            assert "Decompressed 65 file(s)" in probe.read_text()
            report["cache_probe"] = {"exit_code": 0, "files_downloaded": 65, "log_sha256": digest(probe),
                                     "endpoint": "https://cache.mathlib.org/mathlib4-master"}
            rc = monitor([str(lake), "exe", "cache", "get", "Mathlib"], project, env,
                         base / f"mathlib_full_cache_{tag}.log", args.status, report, lock, "hosted_cache",
                         min_free=4 * 2**30, max_time=1800)
            aggregate = mathlib / ".lake/build/lib/lean/Mathlib.olean"
            report["hosted_cache"]["mathlib_aggregate_olean_present"] = aggregate.is_file()
            save(args.status, report)
            return int(rc != 0 or not aggregate.is_file())

        assert report["hosted_cache"]["exit_code"] == 0
        assert report["hosted_cache"]["mathlib_aggregate_olean_present"]
        assert (mathlib / ".lake/build/lib/lean/Mathlib.olean").is_file()
        # A resumed build already has its retained project output on disk.
        min_start = (2 if "solution_build" in report else 4) * 2**30
        assert shutil.disk_usage(project).free >= min_start
        rc = monitor([str(lake), "--no-cache", "build", "Solution"], project, env,
                     base / f"solution_build_{tag}.log", args.status, report, lock, "solution_build",
                     min_free=2 * 2**30, max_time=args.build_seconds)
        if rc:
            return 1
        result = subprocess.run([str(lake), "env", "lean", str(QUERY)], cwd=project, env=env,
                                capture_output=True, text=True, timeout=120)
        axioms = {name: {value.strip() for value in values.split(",")}
                  for name, values in re.findall(r"'([^']+)' depends on axioms: \[([^\]]+)\]", result.stdout)}
        olean = project / ".lake/build/lib/lean/Solution.olean"
        verify_pins(repo, project, mathlib, lean)
        verified = (result.returncode == 0 and set(axioms) == DECLARATIONS
                    and all(value == STANDARD for value in axioms.values()) and olean.is_file())
        report["theorem_query"] = {"exit_code": result.returncode, "stdout": result.stdout, "stderr": result.stderr,
                                   "axioms": {name: sorted(values) for name, values in axioms.items()},
                                   "query_sha256": digest(QUERY),
                                   "target_olean_sha256": digest(olean) if olean.is_file() else None}
        report["status"] = ("solution_build_and_type_axiom_query_completed" if verified
                            else "solution_build_completed_without_expected_query")
        report["scope"] = ("Local pinned Solution source build with official cached Mathlib dependencies and "
                           "queries of two declarations. External Comparator and kernel replays are separate evidence.")
        save(args.status, report)
        return 0 if verified else 1


if __name__ == "__main__":
    sys.exit(main())
