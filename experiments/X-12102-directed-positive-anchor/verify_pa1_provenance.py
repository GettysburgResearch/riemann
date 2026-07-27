#!/usr/bin/env python3
"""Provenance-hardened wrapper for the legacy PA-1 verifier.

The preserved basis table predates the legacy verifier's two SHA-256 conventions:
it binds the old certificate by its Git blob SHA-1.  This wrapper accepts exactly
three *typed* source bindings:

1. the SHA-256 of the complete certificate file;
2. the certificate's internal canonical SHA-256;
3. the Git blob SHA-1 recorded in ``source_certificate_git_blob_sha1``.

The third case is converted only in a temporary copy of the basis.  The legacy
verifier still checks the primitive digest, ordinate, normalization, common
scale, node table, count profile, and every mathematical contraction.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import tempfile
from fractions import Fraction
from pathlib import Path
from typing import Any

import verify_pa1 as legacy

SCHEMA = "riemann.x12102-directed-positive-anchor-pa1.provenance-v2"


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def _hex_digest(value: Any, length: int, name: str) -> str:
    if not isinstance(value, str) or len(value) != length:
        raise legacy.CertificateError(f"{name} is not a {length}-hex digest")
    try:
        int(value, 16)
    except ValueError as exc:
        raise legacy.CertificateError(f"{name} is not hexadecimal") from exc
    return value.lower()


def prepare_basis(
    certificate_path: Path,
    basis_path: Path,
) -> tuple[dict[str, Any], dict[str, str]]:
    certificate = legacy.parent.load_json(certificate_path)
    basis = legacy.parent.load_json(basis_path)

    file_sha256 = legacy.parent.file_sha256(certificate_path)
    internal_sha256 = _hex_digest(
        certificate.get("certificate_sha256"), 64, "certificate_sha256"
    )
    declared_sha256 = _hex_digest(
        basis.get("source_certificate_sha256"),
        64,
        "basis.source_certificate_sha256",
    )
    actual_blob_sha1 = git_blob_sha1(certificate_path)
    declared_blob_raw = basis.get("source_certificate_git_blob_sha1")
    declared_blob_sha1 = (
        _hex_digest(
            declared_blob_raw,
            40,
            "basis.source_certificate_git_blob_sha1",
        )
        if declared_blob_raw is not None
        else None
    )

    if declared_sha256 == file_sha256:
        mode = "FILE_SHA256"
        replacement = declared_sha256
    elif declared_sha256 == internal_sha256:
        mode = "INTERNAL_CERTIFICATE_SHA256"
        replacement = declared_sha256
    elif declared_blob_sha1 == actual_blob_sha1:
        mode = "GIT_BLOB_SHA1"
        # The legacy verifier accepts the internal digest.  Only the temporary
        # compatibility copy is rewritten; the immutable source basis is not.
        replacement = internal_sha256
    else:
        raise legacy.CertificateError(
            "old basis does not match the certificate under any typed binding"
        )

    patched = dict(basis)
    patched["source_certificate_sha256"] = replacement
    audit = {
        "binding_mode": mode,
        "certificate_file_sha256": file_sha256,
        "certificate_internal_sha256": internal_sha256,
        "certificate_git_blob_sha1": actual_blob_sha1,
        "basis_file_sha256": legacy.parent.file_sha256(basis_path),
        "basis_declared_sha256": declared_sha256,
        "basis_declared_git_blob_sha1": declared_blob_sha1 or "",
    }
    return patched, audit


def verify(
    old_certificate: Path,
    old_basis: Path,
    anchor_low: Path,
    anchor_high: Path,
    log_terms: int,
    delta: Fraction,
) -> dict[str, Any]:
    patched_basis, provenance = prepare_basis(old_certificate, old_basis)
    with tempfile.TemporaryDirectory(prefix="pa1-provenance-") as directory:
        path = Path(directory) / "basis.compat.json"
        path.write_text(
            json.dumps(patched_basis, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        compatibility_basis_sha256 = legacy.parent.file_sha256(path)
        result = legacy.verify(
            old_certificate,
            path,
            anchor_low,
            anchor_high,
            log_terms,
            delta,
        )
    source = result.get("source")
    if not isinstance(source, dict):
        raise legacy.CertificateError("legacy PA1 result lacks source manifest")
    source["compatibility_basis_sha256"] = compatibility_basis_sha256
    source["old_basis_sha256"] = provenance["basis_file_sha256"]
    result["legacy_schema"] = result.get("schema")
    result["schema"] = SCHEMA
    result["provenance_binding"] = provenance
    result["proof_boundary"] = (
        result.get("proof_boundary", "")
        + " Source identity was checked through an explicitly typed digest "
        "binding; a Git blob binding is not treated as a SHA-256 value. The "
        "reported old-basis hash is the immutable input, not the temporary "
        "compatibility copy."
    ).strip()
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--old-certificate", type=Path, required=True)
    parser.add_argument("--old-basis", type=Path, required=True)
    parser.add_argument("--anchor-low", type=Path, required=True)
    parser.add_argument("--anchor-high", type=Path, required=True)
    parser.add_argument("--log-terms", type=int, default=240)
    parser.add_argument(
        "--delta", type=Fraction, default=Fraction(1, 1_000_000)
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        result = verify(
            args.old_certificate,
            args.old_basis,
            args.anchor_low,
            args.anchor_high,
            args.log_terms,
            args.delta,
        )
        code = 1 if result["verdict"].startswith("CERTIFIED_NEGATIVE") else 0
    except (OSError, json.JSONDecodeError, legacy.CertificateError) as exc:
        result = {
            "schema": SCHEMA,
            "classification": "REJECTED",
            "reason": str(exc),
        }
        code = 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
