#!/usr/bin/env python3
"""Verify packet transport and finite diagnostics, never analytic theorems.

The manifest is an inventory, not an independent trust anchor. Authenticate
its containing Git commit with PUBLICATION_RECEIPTS.md or the repository.
Ordinary mode is read-only. --replay runs the three reviewed local producers
in both interpreter modes, writing reports only in a temporary directory.
"""

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parent
EXCLUDED = {"MANIFEST.json", "PUBLICATION_RECEIPTS.md"}
DIAGNOSTICS = (
    ("conjugate_pair", "check_conjugate_pair.py",
     "CONJUGATE_PAIR_CONDUCTOR_SIEVE.md", "producer_sha256"),
    ("prime_degree", "check_prime_degree.py",
     "PRIME_DEGREE_COHERENCE.md", "checker_sha256"),
    ("necklace_horizons", "check_necklace_horizons.py",
     "HORIZON_NECKLACE_FACTORIZATION.md", "checker_sha256"),
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def packet_path(relative):
    require(isinstance(relative, str), "path must be a string")
    pure = PurePosixPath(relative)
    require(not pure.is_absolute() and bool(pure.parts)
            and ".." not in pure.parts and str(pure) == relative,
            "noncanonical packet path: " + relative)
    result = ROOT.joinpath(*pure.parts)
    require(result.resolve().is_relative_to(ROOT),
            "path escapes packet: " + relative)
    require(result.is_file() and not result.is_symlink(),
            "missing regular file: " + relative)
    return result


def identity(data):
    return {
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "git_blob": hashlib.sha1(
            b"blob " + str(len(data)).encode("ascii") + b"\0" + data
        ).hexdigest(),
    }


def verify_identity(entry, keys):
    actual = identity(packet_path(entry["path"]).read_bytes())
    for key in keys:
        require(entry[key] == actual[key],
                entry["path"] + ": mismatched " + key)
    return actual


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--replay", action="store_true",
                        help="rerun the finite diagnostics into temporary files")
    args = parser.parse_args()

    manifest = json.loads(packet_path("MANIFEST.json").read_text())
    require(manifest["schema"] == "riemann-packet-manifest-v1",
            "unsupported manifest schema")
    require(set(manifest["excluded_paths"]) == EXCLUDED,
            "unexpected manifest exclusions")
    entries = manifest["files"]
    paths = [entry["path"] for entry in entries]
    require(paths == sorted(set(paths)), "manifest is not sorted and unique")
    actual_paths = sorted(
        str(path.relative_to(ROOT).as_posix())
        for path in ROOT.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts
        and path.relative_to(ROOT).as_posix() not in EXCLUDED
    )
    require(paths == actual_paths, "manifest does not cover the exact packet")
    for entry in entries:
        verify_identity(entry, ("bytes", "sha256", "git_blob"))

    provenance = json.loads(packet_path("PROVENANCE.json").read_text())
    require(provenance["schema"] ==
            "riemann-standalone-research-provenance-v1",
            "unsupported provenance schema")
    require(provenance["repository"] == "GettysburgResearch/riemann",
            "unexpected source repository")
    source_paths = []
    for entry in provenance["source_transports"]:
        verify_identity(entry, ("bytes", "sha256", "git_blob"))
        commit = entry["commit"]
        require(len(commit) == 40
                and all(c in "0123456789abcdef" for c in commit),
                "source commit must be an immutable Git object ID")
        expected_url = (
            "https://github.com/" + provenance["repository"] + "/blob/"
            + commit + "/" + entry["source_path"]
        )
        require(entry["url"] == expected_url,
                "source URL does not match its commit and path")
        source_paths.append(entry["path"])
    require(len(source_paths) == 11 and len(set(source_paths)) == 11,
            "expected eleven distinct source transports")
    require(set(source_paths) == {p for p in paths if p.startswith("sources/")},
            "unbound or missing copied source")
    proof_paths = []
    for entry in provenance["proof_files"]:
        verify_identity(entry, ("bytes", "sha256"))
        proof_paths.append(entry["path"])
    require(len(proof_paths) == 7 and len(set(proof_paths)) == 7,
            "expected seven distinct mathematical files")

    for stem, producer, proof, producer_key in DIAGNOSTICS:
        ordinary = packet_path("checks/" + stem + ".json").read_bytes()
        optimized = packet_path(
            "checks/" + stem + ".optimized.json").read_bytes()
        require(ordinary == optimized, stem + ": interpreter reports differ")
        result = json.loads(ordinary)
        require(result["status"] == "PASS", stem + ": report did not pass")
        proof_identity = identity(packet_path(proof).read_bytes())
        require(proof in proof_paths, stem + ": unbound mathematical source")
        for key in ("bytes", "sha256"):
            require(result["proof_" + key] == proof_identity[key],
                    stem + ": report/proof " + key + " mismatch")
        require(result[producer_key] ==
                identity(packet_path(producer).read_bytes())["sha256"],
                stem + ": producer hash mismatch")

        if args.replay:
            with tempfile.TemporaryDirectory(prefix="riemann-strike-") as temp:
                for flags, suffix in (([], "ordinary"), (["-O"], "optimized")):
                    report = Path(temp) / (stem + "." + suffix + ".json")
                    command = (
                        [sys.executable] + flags
                        + [str(packet_path(producer)), "--proof",
                           str(packet_path(proof)), "--report", str(report)]
                    )
                    replay = subprocess.run(
                        command, cwd=ROOT, check=False, capture_output=True,
                        text=True, timeout=300,
                    )
                    require(replay.returncode == 0,
                            stem + ": replay failed: " + replay.stderr[-2000:])
                    require(report.read_bytes() == ordinary,
                            stem + ": replay bytes differ in " + suffix)

    print(json.dumps({
        "status": "PASS",
        "manifest_files": len(entries),
        "source_transports": len(source_paths),
        "mathematical_files": len(proof_paths),
        "identical_report_pairs": len(DIAGNOSTICS),
        "diagnostic_replays": 2 * len(DIAGNOSTICS) if args.replay else 0,
        "scope": "byte identity, source bindings and exact finite diagnostics",
        "not_certified": [
            "authenticity of an unpinned manifest",
            "external analytic theorems", "native moment hierarchy", "RH",
        ],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
