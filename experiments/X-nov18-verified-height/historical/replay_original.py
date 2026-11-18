"""Re-execute exact archived Platt jobs and compare their original mathematical reports."""
import argparse
import hashlib
import json
import os
import subprocess
from pathlib import Path

from check_runs import DONE, LOOK, MISS, parse_log, read_all

BINARY_HASH = "9aa12c66e9d3c4078c408d1aa7f330fe843d0653e6558845afbac6af2ee6b691"


def signature(output):
    parse_log(output)
    return [line for line in output.splitlines()
            if LOOK.fullmatch(line) or DONE.fullmatch(line) or MISS.fullmatch(line)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--binary", required=True, type=Path)
    parser.add_argument("--library-dir", required=True, type=Path)
    parser.add_argument("--runs", type=Path, default=Path(__file__).parent / "runs")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--snapshot", type=Path, help="rerun every job in a pinned inventory")
    group.add_argument("--transcript", help="rerun one local raw transcript filename")
    args = parser.parse_args()
    binary = args.binary.resolve()
    if hashlib.sha256(binary.read_bytes()).hexdigest() != BINARY_HASH:
        raise ValueError("Historical executable SHA-256 differs")
    if args.snapshot:
        expected = json.loads(args.snapshot.read_text())["transcripts"]
        read_all(args.runs, expected)
        names = sorted(expected)
    else:
        if Path(args.transcript).name != args.transcript or not args.transcript.endswith(".log"):
            raise ValueError("Expected a raw transcript filename")
        names = [args.transcript]
    env = dict(os.environ, LD_LIBRARY_PATH=str(args.library_dir.resolve()))
    digest = hashlib.sha256()
    for name in names:
        raw = (args.runs / name).read_text()
        old = signature(raw)
        # parse_log already checked parameter domains and all iteration outcomes.
        _, precision, start, count, step = raw.splitlines()[0].removeprefix("Command line:- ").split()
        proc = subprocess.run([str(binary), precision, start, count, step], env=env,
                              capture_output=True, text=True, check=True)
        new = signature(proc.stdout)
        if new != old:
            raise ValueError(f"Re-execution disagreed with the original bounds or signs in {name}")
        digest.update((name+"\n"+"\n".join(new)+"\n").encode("ascii"))
        print(f"{name}: matched {count} original regional outcomes", flush=True)
    print(f"regional signature SHA-256: {digest.hexdigest()}")


if __name__ == "__main__":
    main()
