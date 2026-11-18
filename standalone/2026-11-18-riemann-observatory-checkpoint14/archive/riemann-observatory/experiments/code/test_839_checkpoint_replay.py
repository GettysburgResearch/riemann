"""Exercise pause/resume and input binding against the unmodified reference verifier."""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import time

from replay_839_later_windows import FLAGS, ROOT, VENDOR, digest, save
from stage_839_checkpoint_verifier import stage


def execute(binary, *arguments):
    outcome = subprocess.run([str(binary), *map(str, arguments)], capture_output=True, text=True, timeout=50)
    return outcome.returncode, outcome.stdout, outcome.stderr


def kill_and_restore(adapted, params, table, work, identity, expected_stdout):
    state = work / "killed.state"
    process = subprocess.Popen([str(adapted), str(params), str(table), str(state), identity],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    try:
        limit = time.monotonic() + 20
        while not state.is_file() and process.poll() is None and time.monotonic() < limit:
            time.sleep(0.01)
        assert state.is_file() and process.poll() is None
        process.kill()
        stdout, stderr = process.communicate(timeout=10)
        assert process.returncode == -9 and stdout == "", stderr
    finally:
        if process.poll() is None:
            process.kill()
            process.communicate(timeout=10)
    nodes = int(state.read_text().splitlines()[0].split()[3])
    assert 0 < nodes < json.loads(expected_stdout)["nodes"]
    code, stdout, stderr = execute(adapted, params, table, state, identity)
    assert code == 0 and stdout == expected_stdout and f"restored {nodes} completed boxes" in stderr
    return nodes


def run_fixture(label, points, work, compiler, ratio):
    vendor = VENDOR / "verify.cpp"
    staged = work / "checkpointed.cpp"
    staged.write_text(stage())
    flags = [*FLAGS, f"-DVERIFY_POINT_COUNT={points}"]
    unmodified, adapted = work / "original", work / "adapted"
    for source, binary in ((vendor, unmodified), (staged, adapted)):
        subprocess.run(["g++", *flags, str(source), "-o", str(binary)], check=True, timeout=30)
    inputs = ROOT / f"experiments/inputs/839_{label}_window"
    original = json.loads((inputs / "inputs.json").read_text())
    numerator, denominator = ratio
    original["alpha"] = original["alpha"] * numerator // denominator
    fixture = work / "easier_alpha.json"
    fixture.write_text(json.dumps(original))
    params = work / "parameters.txt"
    table = inputs / "kernel_lower.bin"
    subprocess.run([sys.executable, str(VENDOR / "make_parameters.py"), str(fixture), str(params)], check=True)
    identity = sha256((digest(params) + digest(table) + digest(staged)).encode()).hexdigest()
    code, expected_stdout, stderr = execute(unmodified, params, table)
    assert code == 0, stderr
    expected = json.loads(expected_stdout)
    assert expected["status"] == "PASS_COB_CONTINUUM"
    if ratio != (2, 1):
        assert expected["affine"] > 0
    uninterrupted = work / "uninterrupted.state"
    resumed = work / "resumed.state"
    code, stdout, stderr = execute(adapted, params, table, uninterrupted, identity)
    assert code == 0 and stdout == expected_stdout, stderr
    pauses = sorted({expected["nodes"] // d for d in (5, 3, 2)})
    assert not resumed.exists()
    assert all(node > 0 for node in pauses)
    for node in pauses:
        code, stdout, stderr = execute(adapted, params, table, resumed, identity, node)
        assert code == 75 and stdout == "", stderr
        assert "intentional pause after durable checkpoint" in stderr
        header = resumed.read_text().splitlines()[0].split()
        assert int(header[3]) == node and int(header[-1]) > 0
        if node != pauses[0]:
            assert "verify: restored " in stderr
    code, stdout, stderr = execute(adapted, params, table, resumed, "0" * 64)
    assert code == 5 and stdout == "" and "checkpoint data or I/O error" in stderr
    valid = resumed.read_text()
    resumed.write_text(valid.removesuffix("end\n"))
    code, stdout, stderr = execute(adapted, params, table, resumed, identity)
    assert code == 5 and stdout == "" and "checkpoint data or I/O error" in stderr
    resumed.write_text(valid)
    code, stdout, stderr = execute(adapted, params, table, resumed, identity)
    assert code == 0 and stdout == expected_stdout, stderr
    assert resumed.read_bytes() == uninterrupted.read_bytes()
    code, stdout, stderr = execute(adapted, params, table, resumed, identity)
    assert code == 0 and stdout == expected_stdout, stderr
    recovered_nodes = (kill_and_restore(adapted, params, table, work, identity, expected_stdout)
                       if expected["nodes"] > 3_000_000 else None)
    return {
        "fixture": label, "alpha_multiplier_rounded_down": f"{numerator}/{denominator}",
        "points": points, "compiler": compiler, "restored_nodes_after_sigkill": recovered_nodes,
        "staged_sha256": digest(staged), "parameter_sha256": digest(params),
        "unmodified_counts": expected, "separate_pause_nodes": pauses,
        "uninterrupted_and_resumed_final_state_bytes_match": True,
        "wrong_identity_and_truncated_state_rejected": True,
        "completed_state_reopens_to_same_result": True,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--work-dir", required=True, type=Path)
    parser.add_argument("--result", required=True, type=Path)
    parser.add_argument("--affine-fixtures", action="store_true")
    args = parser.parse_args()
    args.work_dir.mkdir(parents=True, exist_ok=True)
    compiler = subprocess.check_output(["g++", "--version"], text=True).splitlines()[0]
    ratios = {"first": (5, 4), "second": (5, 4), "third": (7, 6)} if args.affine_fixtures else {}
    results = []
    for label, points in (("first", 7), ("second", 8), ("third", 7)):
        fixture = args.work_dir / label
        fixture.mkdir()
        results.append(run_fixture(label, points, fixture, compiler, ratios.get(label, (2, 1))))
    result = {"status": "functional_checkpoint_replay_equivalence_tests_passed",
              "scope": "In-process reference tests with easier fixtures. Exact full searches separate.",
              "fixtures": results}
    save(args.result, result)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
