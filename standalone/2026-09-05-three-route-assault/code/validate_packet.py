#!/usr/bin/env python3
"""Check this research packet's bytes and local references, not its theorems.

--seal is an explicit authoring operation. The default mode never rewrites data.
All failures remain effective under python -O.
"""
from __future__ import annotations
import argparse
import ast
import csv
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "SHA256SUMS"
REQUIRED = {
    "README.md", "ROUTES_AND_NEXT_PASS.md", "CLAIMS.tsv", "SELF_AUDIT.md",
    "SOURCES.md", "SOURCE_LOCK.json", "VALIDATION.md", "PR_BODY.md",
    "proofs/R1_SOURCE_DETERMINANT_AND_MARKED_OBSTRUCTION.md",
    "proofs/R2_FIXED_FREQUENCY_AND_SHARP_TRANSPORT.md",
    "proofs/R3_HORIZONTAL_SURPLUS_IDENTITY.md",
    "proofs/R3_SCREENING_AND_CONDITIONING.md",
    "code/exact.py", "code/verify.py", "code/validate_packet.py",
    "tests/test_packet.py", "results/exact.json",
    "results/tests-normal.log", "results/tests-optimized.log",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def files() -> list[Path]:
    return sorted(p for p in ROOT.rglob("*") if p.is_file()
                  and p != MANIFEST and "__pycache__" not in p.parts
                  and p.suffix != ".pyc")


def manifest_bytes(paths: list[Path]) -> bytes:
    return "".join(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(ROOT).as_posix()}\n"
                   for p in paths).encode("utf-8")


def check_structure(paths: list[Path]) -> dict[str, int]:
    actual = {p.relative_to(ROOT).as_posix() for p in paths}
    require(REQUIRED <= actual, f"Missing required files: {sorted(REQUIRED-actual)}")
    links = 0
    python_files = 0
    for p in paths:
        require(not p.is_symlink(), f"Symlink disallowed: {p}")
        text = p.read_text(encoding="utf-8")
        require(not any(ord(ch) < 32 and ch not in "\n\t" for ch in text),
                f"Control byte or CR in {p}")
        require(text.endswith("\n"), f"No final newline: {p}")
        if p.suffix == ".py":
            ast.parse(text, filename=str(p))
            python_files += 1
        if p.suffix != ".md":
            continue
        require(text.count(r"\[") == text.count(r"\]"), f"Unbalanced display math: {p}")
        require(text.count(r"\(") == text.count(r"\)"), f"Unbalanced inline math: {p}")
        require(sum(line.startswith("```") for line in text.splitlines()) % 2 == 0,
                f"Unbalanced code fences: {p}")
        for target in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", text):
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            local = (p.parent / target.split("#", 1)[0]).resolve()
            require(local.is_relative_to(ROOT), f"Link escapes packet: {p}: {target}")
            require(local.exists(), f"Broken local link: {p}: {target}")
            links += 1
    with (ROOT / "CLAIMS.tsv").open(newline="", encoding="utf-8") as stream:
        claims = list(csv.DictReader(stream, delimiter="\t"))
    ids = [row["id"] for row in claims]
    require(len(ids) == len(set(ids)), "Duplicate local claim ID")
    for row in claims:
        require((ROOT / row["proof"]).is_file(), f"Missing claim proof: {row['id']}")
    lock = json.loads((ROOT / "SOURCE_LOCK.json").read_text())
    require(lock["base_commit"] == "6dda8b5125457ed936330229f8c9eb6491728e76", "Base changed")
    for item in lock["sources"]:
        for field in ("commit", "blob"):
            require(re.fullmatch(r"[0-9a-f]{40}", item[field]) is not None,
                    f"Malformed {field} in source lock")
    return {"files": len(paths), "local_links": links,
            "python_files_parsed": python_files, "claim_rows": len(claims)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seal", action="store_true", help="explicitly write new authoring checksums")
    args = parser.parse_args()
    try:
        paths = files()
        counts = check_structure(paths)
        expected = manifest_bytes(paths)
        if args.seal:
            MANIFEST.write_bytes(expected)
        require(MANIFEST.is_file(), "SHA256SUMS missing")
        require(MANIFEST.read_bytes() == expected, "Checksum or complete-file-list mismatch")
        print("PASS_THREE_ROUTE_PACKET_INTEGRITY")
        print(json.dumps(counts, sort_keys=True))
        print("INTEGRITY_ONLY; ANALYTIC_REVIEW_PENDING; RH_UNPROVED")
        return 0
    except (ValueError, OSError, SyntaxError, KeyError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
