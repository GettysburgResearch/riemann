#!/usr/bin/env python3
"""Verify, deterministically compress, and manifest a production certificate."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path

from verify import Verifier, load_certificate


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate")
    parser.add_argument("--compressed", required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--verification", required=True)
    parser.add_argument("--verification-input")
    args = parser.parse_args()

    source = Path(args.certificate)
    raw = source.read_bytes()
    certificate = load_certificate(str(source))
    if args.verification_input:
        verification = json.loads(
            Path(args.verification_input).read_text(encoding="utf-8")
        )
        if not verification.get("verified"):
            raise ValueError("supplied verification is not accepted")
        if verification.get("certificate_sha256") != certificate.get(
            "certificate_sha256"
        ):
            raise ValueError("supplied verification targets another certificate")
    else:
        verification = Verifier(certificate).verify()

    compressed = gzip.compress(raw, compresslevel=9, mtime=0)
    compressed_path = Path(args.compressed)
    compressed_path.write_bytes(compressed)

    verification_path = Path(args.verification)
    verification_path.write_text(
        json.dumps(verification, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    terminal_streams = certificate["terminal_streams"]
    terminal_bytes = json.dumps(
        terminal_streams, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")

    source_files = [
        "certmath.py",
        "search.py",
        "verify.py",
        "pack_release.py",
        "parameter_probe.py",
        "parameter_ladder.py",
        "tests/test_engine.py",
    ]
    source_hashes = {
        name: sha256_file(Path(name))
        for name in source_files
        if Path(name).exists()
    }

    manifest = {
        "schema": "riemann.robin.powered-canonical.release-manifest.v1",
        "certificate_schema": certificate["schema"],
        "finite_region": certificate["finite_region"],
        "parameters": certificate["parameters"],
        "dual_ladder": certificate["dual_ladder"],
        "root_upper_bits": certificate["root_upper_bits"],
        "status": certificate["status"],
        "counts": certificate["counts"],
        "powered_dual_use": certificate["powered_dual_use"],
        "global_canonical_normalized_ratio_upper": certificate[
            "global_canonical_normalized_ratio_upper"
        ],
        "all_integer_consequence": certificate["all_integer_consequence"],
        "certificate_internal_sha256": certificate["certificate_sha256"],
        "certificate_uncompressed": {
            "filename": source.name,
            "bytes": len(raw),
            "sha256": sha256_bytes(raw),
            "committed": False,
        },
        "certificate_gzip": {
            "filename": compressed_path.name,
            "bytes": len(compressed),
            "sha256": sha256_bytes(compressed),
            "compression": "gzip level 9, mtime=0",
            "committed": True,
        },
        "terminal_stream_sha256": sha256_bytes(terminal_bytes),
        "verification": {
            "filename": verification_path.name,
            "sha256": sha256_file(verification_path),
            "verified": verification["verified"],
        },
        "source_sha256": source_hashes,
        "proof_boundary": (
            "The compressed file contains the complete terminal stream. The manifest "
            "binds both byte representations and the reconstructed verification output. "
            "Structural parent claims retain their repository statuses."
        ),
    }
    Path(args.manifest).write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
