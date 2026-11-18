"""Run the unmodified second and third K839 C++ searches with exact preflight checks."""
import argparse
import datetime
import fcntl
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
import re
import struct
import subprocess
import sys
import time


ROOT = Path(__file__).resolve().parents[2]
VENDOR = ROOT / "experiments/code/vendor/839_reference"
COMMIT = "0e961ea199b425010843bc8044676d4ad29fe031"
WINDOWS = {
    "second": (8, 535332163, 267666082, 202511130, 65154952, 63),
    "third": (7, 572959453, 286479727, 256891820, 29587907, 68),
}
FLAGS = ("-std=c++23", "-O3", "-DNDEBUG", "-D_GLIBCXX_ASSERTIONS")


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def save(path, value):
    temp = path.with_suffix(".tmp")
    value["date_utc"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    temp.write_text(json.dumps(value, indent=2) + "\n")
    temp.replace(path)


def preflight(label):
    folder = ROOT / f"experiments/inputs/839_{label}_window"
    provenance = json.loads((folder / "PROVENANCE.json").read_text())
    data = json.loads((folder / "inputs.json").read_text())
    hashes = {name: digest(folder / name) for name in ("inputs.json", "kernel_lower.bin")}
    independently_checked = json.loads(
        (ROOT / "experiments/results/independent_kernel_cells_second_third.json").read_text()
    )
    table_check = next(row for row in independently_checked["results"] if row["label"] == label)
    assert provenance["commit"] == table_check["source_commit"] == COMMIT
    assert all(provenance["files"][name]["sha256"] == value for name, value in hashes.items())
    assert hashes["inputs.json"] == table_check["input_sha256"]
    assert hashes["kernel_lower.bin"] == table_check["table_sha256"] == data["table_sha256"]
    assert table_check["all_table_lower_bounds_certified"] and not table_check["mismatches"]

    n = data.get("points", 7)
    assert n == WINDOWS[label][0]
    pairs = list(combinations(range(n), 2))
    gaps = n - 1
    weights, rewards, potentials = data["weights"], data["h"], data["cob_knots"]
    assert list(map(len, weights)) == [len(pairs)] * 3
    assert list(map(len, rewards)) == [n] * 2
    assert len(potentials) == gaps and all(list(map(len, gap)) == [14] * 3 for gap in potentials)
    assert all(0 <= small <= large for small, large in zip(*rewards))
    assert all(0 <= w0 <= min(w1, w2) for w0, w1, w2 in zip(*weights))
    for row, cap in zip(weights, (2_000_000, 4_000_000, 8_000_000)):
        assert all(sum(w for w, (i, j) in zip(row, pairs) if j - i == d) <= cap for d in range(1, n))
    assert all(row[0] == row[-1] == 0 for gap in potentials for row in gap)
    assert all(sum(gap[t][k] for gap in potentials) == 0 for t in range(3) for k in range(14))
    budget = -sum(min(0, *(b for row in gap for b in row)) for gap in potentials)
    assert budget == data["budget"]
    r, g, s, a = (data[key] for key in ("R", "grid", "scale", "alpha"))
    separation = Fraction(data["separation"])
    assert data["denominator"] == 1_000_000 and separation == Fraction(17, 20)
    minimum = int(separation * g)
    assert minimum > 0 and gaps * minimum < r and Fraction(minimum, g) <= separation
    assert 0 < r <= 2**21 and 0 < g <= 2**20 and 0 < s <= 2**30 and 0 < a <= 10**9
    assert g % 8 == s % g == s % (g // 8) == 0
    knot_step = g // 8
    last_knot = 3 * g // 4 + 13 * knot_step
    budget_margin = a * r - g * (sum(rewards[1]) + budget)
    assert budget_margin > 0
    assert max(gaps * r, 2 * r + 2, last_knot) < 2**31
    table = (folder / "kernel_lower.bin").read_bytes()
    assert len(table) == 4 * (r + 1) and table_check["cells"] == r + 1
    assert max(value for (value,) in struct.iter_unpack("<I", table)) <= s

    w = max(w for row in weights for w in row)
    b = max(abs(b) for gap in potentials for row in gap for b in row)
    h = max(rewards[1])
    assert max(w, b, h) <= 10**9
    pressure = a * (s // g)
    basic = 2 * pressure * r + s * (3 * n * gaps * w + (4 * n + 2) * gaps * b + 4 * n * h)
    search_bound = 512 * s * (w + b + h) + 64 * pressure * (r + 2)
    support_bound = 4 * s * (r + 2) + 4 * b * s * (1 + r // knot_step)
    kernel_offset = s * (r + 3)
    potential_slope = 2 * b * (s // knot_step)
    potential_offset = b * s + potential_slope * r
    assert max(basic, search_bound, support_bound, kernel_offset, potential_offset) < 2**63 - 1
    affine = (2 * gaps * (potential_offset + (pressure + potential_slope) * r)
              + len(pairs) * w * (kernel_offset + s * gaps * r)
              + 2 * n * h * s + basic)
    assert affine < 2**127 - 1
    return folder, {
        "file_sha256": hashes, "points": n, "minimum_gap_grid_steps": minimum,
        "grid_stop": r, "closed_cell_count": r + 1, "potential_budget": budget,
        "positive_span_margin": budget_margin, "basic_64_bit_bound": basic,
        "source_64_bit_search_bound": search_bound, "source_64_bit_support_bound": support_bound,
        "kernel_offset_64_bit_bound": kernel_offset, "potential_offset_64_bit_bound": potential_offset,
        "affine_128_bit_bound": affine,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--work-dir", type=Path, required=True)
    parser.add_argument("--result-dir", type=Path, default=ROOT / "experiments/results")
    parser.add_argument("--windows", choices=WINDOWS, nargs="+", default=tuple(WINDOWS))
    parser.add_argument("--preflight-only", action="store_true")
    args = parser.parse_args()
    args.work_dir.mkdir(parents=True, exist_ok=True)
    args.result_dir.mkdir(parents=True, exist_ok=True)
    lock = (args.result_dir / ".839_later_windows.lock").open("a")
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    preflights = {label: preflight(label) for label in args.windows}
    compiler = subprocess.check_output(["g++", "--version"], text=True).splitlines()[0]
    source_hashes = {name: digest(VENDOR / name) for name in ("verify.cpp", "make_parameters.py", "LICENSE")}
    for name, expected in {
        "verify.cpp": "c30310214c121d0acf4b4ae562f396c1e13be13992b1f01e02df584dbd602142",
        "make_parameters.py": "7cc149b14d0060448712b59c3317b8dab7760865080c11e6e78487d7ff55e18e",
        "LICENSE": "29ebb443d81df1ef96b296e604e233228979edeebf043ccaf8699fd6d6bd49a8",
    }.items():
        assert source_hashes[name] == expected
    if args.preflight_only:
        print(json.dumps({key: value[1] for key, value in preflights.items()}, indent=2))
        return 0
    prepared = {}
    for label, (folder, evidence) in preflights.items():
        result_path = args.result_dir / f"839_reference_{label}_replay.json"
        if result_path.exists():
            previous = json.loads(result_path.read_text())
            if previous["status"] == "completed_counts_match":
                continue
            raise SystemExit(f"Previous {label} result exists at {result_path}. Preserve it before restarting.")
        n, *counts = WINDOWS[label]
        expected = dict(zip(("nodes", "leaves", "basic", "affine", "max_stack"), counts))
        expected["status"] = "PASS_COB_CONTINUUM"
        run_dir = args.work_dir / label
        run_dir.mkdir(exist_ok=True)
        exe, parameters = run_dir / f"verify{n}", run_dir / "parameters.txt"
        command = ["g++", *FLAGS, f"-DVERIFY_POINT_COUNT={n}", str(VENDOR / "verify.cpp"), "-o", str(exe)]
        subprocess.run(command, check=True)
        subprocess.run([sys.executable, str(VENDOR / "make_parameters.py"), str(folder / "inputs.json"),
                        str(parameters)], check=True)
        argv = [str(exe), str(parameters), str(folder / "kernel_lower.bin")]
        out_path, err_path = run_dir / "stdout.log", run_dir / "stderr.log"
        report = {
            "status": "running", "window": label, "source_commit": COMMIT,
            "scope": "Unmodified author C++ continuum search; separate rational table validation. No Lean build.",
            "compiler": compiler, "compiler_flags": [*FLAGS, f"-DVERIFY_POINT_COUNT={n}"],
            "source_sha256": source_hashes, "preflight": evidence,
            "parameters_sha256": digest(parameters), "binary_sha256": digest(exe),
            "expected": expected,
        }
        prepared[label] = (argv, result_path, report, out_path, err_path)
    active = {}
    all_matched = True
    for label, (argv, result_path, report, out_path, err_path) in prepared.items():
        with out_path.open("w") as out, err_path.open("w") as err:
            process = subprocess.Popen(argv, stdout=out, stderr=err)
        report["pid"] = process.pid
        active[label] = (process, result_path, report, out_path, err_path, time.monotonic())
        save(result_path, report)
    while active:
        for label, (process, result_path, report, out_path, err_path, start) in list(active.items()):
            report["elapsed_seconds"] = round(time.monotonic() - start, 3)
            stderr = err_path.read_text()
            milestones = re.findall(r"verify: (\d+) boxes examined, (\d+) waiting", stderr)
            report["last_confirmed_progress"] = (
                {"nodes": int(milestones[-1][0]), "waiting": int(milestones[-1][1])} if milestones else None
            )
            code = process.poll()
            if code is not None:
                report.update(exit_code=code, stdout=out_path.read_text(), stderr=stderr)
                try:
                    report["observed"] = json.loads(report["stdout"])
                except json.JSONDecodeError:
                    report["observed"] = None
                matched = code == 0 and report["observed"] == report["expected"]
                report["status"] = "completed_counts_match" if matched else "completed_without_matching_pass"
                all_matched &= matched
                del active[label]
                print(json.dumps(report), flush=True)
            save(result_path, report)
        if active:
            time.sleep(30)
    return 0 if all_matched else 1


if __name__ == "__main__":
    raise SystemExit(main())
