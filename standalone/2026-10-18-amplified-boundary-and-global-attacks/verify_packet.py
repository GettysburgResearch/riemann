"""Verify the frozen payload and optionally replay its exact algebra.

This authenticates the committed file inventory and the new rational
parameter calculation. It does not verify any imported analytic theorem.
Only the Python standard library is used; checks remain active under -O.
"""
from pathlib import Path, PurePosixPath
from fractions import Fraction
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--replay", action="store_true")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    manifest = json.loads((root / "MANIFEST.json").read_text())
    entries = manifest["files"]
    actual = {
        p.relative_to(root).as_posix()
        for p in root.rglob("*")
        if p.is_file() and p != root / "MANIFEST.json"
        and "__pycache__" not in p.parts and p.suffix != ".pyc"
    }
    require(actual == set(entries), "payload inventory differs from manifest")
    for name, metadata in entries.items():
        relative = PurePosixPath(name)
        require(not relative.is_absolute() and ".." not in relative.parts,
                "unsafe manifest path")
        data = (root / name).read_bytes()
        require(len(data) == metadata["bytes"], "byte length: " + name)
        require(sha256(data) == metadata["sha256"], "SHA-256: " + name)
        git_blob = hashlib.sha1(
            b"blob " + str(len(data)).encode() + b"\0" + data
        ).hexdigest()
        require(git_blob == metadata["git_blob_sha1"], "Git blob: " + name)

    report = {
        "status": "PASS",
        "scope": "payload integrity and exact parameter algebra only",
        "files": len(entries),
        "manifest_sha256": sha256((root / "MANIFEST.json").read_bytes()),
        "replayed": False,
    }
    if args.replay:
        # Replay from a clean copy of the verified source files, so local
        # bytecode caches or extra files cannot supply a different module.
        with tempfile.TemporaryDirectory(prefix="riemann-boundary-") as tmp:
            work = Path(tmp)
            for name in entries:
                target = work / name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(root / name, target)
            output = work / "replay"
            output.mkdir()
            normal = {}
            for optimized in (False, True):
                flag = "optimized" if optimized else "normal"
                prefix = [sys.executable, "-S", "-B"]
                if optimized:
                    prefix.append("-O")
                for lane, source, receipt, extra in (
                    ("parent", "correlated/certify_boundary.py",
                     "correlated/certificate.json",
                     ["--check", str(work / "correlated/certificate.json")]),
                    ("independent", "review/check_xu_candidate_independent.py",
                     "review/xu_candidate_independent_root_params.json",
                     ["--b", "173/2000"]),
                ):
                    target = output / (lane + "-" + flag + ".json")
                    command = prefix + [str(work / source)] + extra + [
                        "--output", str(target)
                    ]
                    result = subprocess.run(
                        command, cwd=work, capture_output=True, text=True,
                        timeout=30
                    )
                    require(result.returncode == 0,
                            lane + " " + flag + " failed: " + result.stderr)
                    require(not result.stderr, lane + " emitted stderr")
                    data = target.read_bytes()
                    require(data == (work / receipt).read_bytes(),
                            lane + " receipt differs from frozen reconstruction")
                    if not optimized:
                        normal[lane] = json.loads(data)
            common = [
                "parameters", "margins", "A_y_ascending", "B_y_ascending",
                "C_y_ascending", "four_AC_minus_B2_y_ascending"
            ]
            for key in common:
                require(normal["parent"][key] == normal["independent"][key],
                        "independent reconstruction differs: " + key)
            require(Fraction(normal["parent"]["parameters"]["boundary"])
                    == Fraction(43744333, 50000000), "candidate boundary")

            # A concrete below-ceiling candidate must fail at the
            # mathematical discriminant condition, not at a generic crash.
            negative = subprocess.run(
                [sys.executable, "-S", "-B", "-O",
                 str(work / "review/check_xu_candidate_independent.py"),
                 "--b", "173/2000", "--boundary", "87488664/100000000",
                 "--g", "1/100000000"],
                cwd=work, capture_output=True, text=True, timeout=30
            )
            require(negative.returncode != 0
                    and "ArithmeticError: 4AC-B^2 has a negative coefficient"
                    in negative.stderr, "negative mathematical control")
            report.update({
                "replayed": True,
                "accepting_replays": 4,
                "normal_and_optimized_receipts_identical": True,
                "independent_common_data_identical": True,
                "below_ceiling_control": "rejected at discriminant predicate",
                "boundary": "43744333/50000000",
                "parent_certificate_sha256": entries[
                    "correlated/certificate.json"]["sha256"],
                "independent_certificate_sha256": entries[
                    "review/xu_candidate_independent_root_params.json"]["sha256"],
            })
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
