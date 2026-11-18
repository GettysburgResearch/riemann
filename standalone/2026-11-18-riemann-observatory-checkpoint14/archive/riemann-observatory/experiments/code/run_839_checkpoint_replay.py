"""Run or resume the separately staged, checkpointed K839 continuum search."""
import argparse
import datetime
import fcntl
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import time

from replay_839_later_windows import FLAGS, VENDOR, WINDOWS, digest, preflight, save
from stage_839_checkpoint_verifier import stage


def progress(path, identity, points):
    if not path.exists():
        return None
    with path.open() as stream:
        magic, binding, n, nodes, leaves, basic, affine, max_stack, waiting = stream.readline().split()
    if (magic, binding, int(n)) != ("observatory-839-checkpoint-v1", identity, points):
        raise ValueError(f"Checkpoint identity mismatch at {path}")
    return {key: int(value) for key, value in
            zip(("nodes", "leaves", "basic", "affine", "max_stack", "waiting"),
                (nodes, leaves, basic, affine, max_stack, waiting))}


def completed_checkpoint(observed):
    return {k: v for k, v in observed.items() if k != "status"} | {"waiting": 0}


def prepare(label, work, result_folder, staged, compiler):
    folder, checked = preflight(label)
    points, *counts = WINDOWS[label]
    expected = dict(zip(("nodes", "leaves", "basic", "affine", "max_stack"), counts))
    expected["status"] = "PASS_COB_CONTINUUM"
    subdir = work / label
    subdir.mkdir(exist_ok=True)
    source = subdir / "checkpointed_verify.cpp"
    source.write_text(staged)
    params = subdir / "parameters.txt"
    table = folder / "kernel_lower.bin"
    generator = VENDOR / "make_parameters.py"
    subprocess.run([sys.executable, str(generator), str(folder / "inputs.json"), str(params)], check=True)
    flags = [*FLAGS, f"-DVERIFY_POINT_COUNT={points}"]
    manifest = {
        "upstream_verifier_sha256": digest(VENDOR / "verify.cpp"),
        "parameter_generator_sha256": digest(generator),
        "staged_source_sha256": digest(source),
        "generated_parameters_sha256": digest(params),
        "input_hashes": checked["file_sha256"],
        "compiler": compiler,
        "compiler_flags": flags,
    }
    identity = sha256(json.dumps(manifest, sort_keys=True).encode()).hexdigest()
    state = subdir / "search.checkpoint"
    prior = progress(state, identity, points)
    result = result_folder / f"839_reference_{label}_checkpoint_replay.json"
    if result.exists():
        previous = json.loads(result.read_text())
        if previous["checkpoint_identity"] != identity:
            raise ValueError(f"Existing result used a different checkpoint identity: {result}")
        if previous["status"] == "checkpoint_replay_completed_counts_match":
            if previous.get("observed") != expected or prior != completed_checkpoint(expected):
                raise ValueError(f"Completed result and checkpoint disagree: {result}")
            return None
        preserve = subdir / f"prior_result_{time.time_ns()}.json"
        preserve.write_bytes(result.read_bytes())
    executable = subdir / f"verify{points}_checkpointed"
    temp = executable.with_suffix(".tmp")
    subprocess.run(["g++", *flags, str(source), "-o", str(temp)], check=True)
    temp.replace(executable)
    tag = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    out, err = subdir / f"{tag}.stdout.log", subdir / f"{tag}.stderr.log"
    report = {
        "status": "checkpoint_replay_running", "window": label, "attempt_utc": tag,
        "scope": "Staged author reference verifier with checkpoint hooks; separate from exact vendor replay and Lean.",
        "checkpoint_identity": identity, "identity_manifest": manifest,
        "binary_sha256": digest(executable), "preflight": checked, "expected": expected,
        "starting_checkpoint": prior, "last_durable_progress": prior,
    }
    return [str(executable), str(params), str(table), str(state), identity], out, err, state, result, report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--work-dir", type=Path, required=True)
    parser.add_argument("--result-dir", type=Path, required=True)
    parser.add_argument("--windows", nargs="+", choices=WINDOWS, default=tuple(WINDOWS))
    args = parser.parse_args()
    work = args.work_dir.resolve()
    work.mkdir(parents=True, exist_ok=True)
    args.result_dir.mkdir(parents=True, exist_ok=True)
    staged = stage()
    compiler = subprocess.check_output(["g++", "--version"], text=True).splitlines()[0]
    with ((work / "checkpoint-supervisor.lock").open("a") as lock,
          (args.result_dir / ".839_checkpoint_results.lock").open("a") as result_lock):
        for held in (lock, result_lock):
            fcntl.flock(held, fcntl.LOCK_EX | fcntl.LOCK_NB)
        prepared = [prepare(label, work, args.result_dir, staged, compiler)
                    for label in dict.fromkeys(args.windows)]
        active = []
        for item in prepared:
            if item is None:
                continue
            command, out, err, state, result, report = item
            with out.open("x") as stdout, err.open("x") as stderr:
                child = subprocess.Popen(command, stdout=stdout, stderr=stderr,
                                         pass_fds=(lock.fileno(), result_lock.fileno()))
            report["pid"] = child.pid
            save(result, report)
            active.append((child, time.monotonic(), out, err, state, result, report))
        failed = False
        while active:
            for item in active.copy():
                child, started, out, err, state, result, report = item
                report["elapsed_seconds_this_attempt"] = round(time.monotonic() - started, 3)
                latest = progress(state, report["checkpoint_identity"], report["preflight"]["points"])
                report["last_durable_progress"] = latest
                code = child.poll()
                if code is not None:
                    latest = progress(state, report["checkpoint_identity"], report["preflight"]["points"])
                    report["last_durable_progress"] = latest
                    report.update(exit_code=code, stdout=out.read_text(), stderr=err.read_text())
                    try:
                        observed = json.loads(report["stdout"])
                    except json.JSONDecodeError:
                        observed = None
                    report["observed"] = observed
                    matched = (code == 0 and observed == report["expected"]
                               and latest == completed_checkpoint(observed))
                    report["status"] = ("checkpoint_replay_completed_counts_match" if matched
                                        else "checkpoint_replay_stopped")
                    failed |= not matched
                    active.remove(item)
                    print(json.dumps(report), flush=True)
                save(result, report)
            if active:
                time.sleep(20)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
