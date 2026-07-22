#!/usr/bin/env python3
"""Create the compact committed manifest for a regenerated X-2501 certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Sequence


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_sha256(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def build_manifest(certificate_path: Path) -> dict[str, object]:
    certificate = json.loads(certificate_path.read_text(encoding="utf-8"))
    if certificate.get("schema") != "riemann.robin.canonical-tree.v1":
        raise ValueError("unsupported certificate schema")
    body = dict(certificate)
    stored_digest = body.pop("certificate_sha256", None)
    recomputed_digest = canonical_sha256(body)
    if stored_digest != recomputed_digest:
        raise ValueError("certificate internal digest mismatch")
    streams = certificate.get("terminal_streams")
    if not isinstance(streams, list):
        raise ValueError("terminal streams missing")

    source_paths = [
        Path("certmath.py"),
        Path("search.py"),
        Path("verify.py"),
        Path("parameter_probe.py"),
        Path("parameter_ladder.py"),
        Path("make_manifest.py"),
        Path("tests/test_engine.py"),
    ]

    return {
        "schema": "riemann.robin.canonical-tree.production-manifest.v2",
        "experiment": "X-2501",
        "generation_command": (
            "python search.py --n-max "
            "1000000000000000000000000000000000000000000000000000000 "
            "--bits 256 --log-terms 88 --exp-terms 88 "
            "--harmonic-cutoff 250000 "
            "--output results/certificate.regenerated.json"
        ),
        "verification_command": (
            "python verify.py results/certificate.regenerated.json "
            "--output results/verification.regenerated.json"
        ),
        "certificate_internal_sha256": stored_digest,
        "certificate_pretty_file_sha256": sha256_file(certificate_path),
        "certificate_uncompressed_bytes": certificate_path.stat().st_size,
        "terminal_token_count": sum(len(stream) for stream in streams),
        "terminal_streams_sha256": canonical_sha256(streams),
        "expected_status": certificate["status"],
        "expected_finite_region": certificate["finite_region"],
        "expected_parameters": certificate["parameters"],
        "expected_prime_prefix": certificate["prime_prefix"],
        "expected_counts": certificate["counts"],
        "expected_global_canonical_normalized_ratio_upper": certificate[
            "global_canonical_normalized_ratio_upper"
        ],
        "expected_all_integer_consequence": certificate["all_integer_consequence"],
        "expected_closest_checked_leaf_discovery_only": certificate[
            "closest_checked_leaf_discovery_only"
        ],
        "source_sha256": {str(path): sha256_file(path) for path in source_paths},
        "proof_boundary": (
            "The full terminal stream is deterministically regenerated rather than "
            "committed. This manifest binds the exact certificate digests, stream "
            "digest, finite region, counts, quantitative bounds, and source snapshots."
        ),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate")
    parser.add_argument("--output", required=True)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    manifest = build_manifest(Path(args.certificate))
    Path(args.output).write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
