#!/usr/bin/env python3
"""Fail-closed validator for the T-91652 provenance ledger lock."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any

LOCK_REL = Path("integration/2026-08-13/t91652-full-ledger-lock.json")
RESULT_REL = Path("experiments/X-91651-t91652-ledger-lock/results/verification.json")
EXPECTED_SCHEMA = "t91652-full-ledger-lock-v1"
L91112_SCOPE = "retained displays L-91112.25--26 only"


def run_git(root: Path, *args: str) -> bytes:
    proc = subprocess.run(
        ["git", "-C", str(root), *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(
            f"git {' '.join(args)} failed: {proc.stderr.decode(errors='replace').strip()}"
        )
    return proc.stdout


def git_blob_sha(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode()
    return hashlib.sha1(header + data).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def validate_entry(
    root: Path,
    entry: dict[str, Any],
    default_commit: str | None,
    kind: str,
) -> dict[str, str]:
    path = entry["path"]
    expected = entry["blob_sha"]
    commit = entry.get("source_commit") or default_commit
    require(bool(commit), f"{kind}:{path}: missing source_commit")

    run_git(root, "cat-file", "-e", f"{commit}^{{commit}}")
    committed = run_git(root, "show", f"{commit}:{path}")
    committed_sha = git_blob_sha(committed)
    require(
        committed_sha == expected,
        f"{kind}:{path}: locked {expected}, source commit has {committed_sha}",
    )

    if kind == "local":
        working_path = root / path
        require(working_path.is_file(), f"local:{path}: missing working-tree file")
        working_sha = git_blob_sha(working_path.read_bytes())
        require(
            working_sha == expected,
            f"local:{path}: working tree has {working_sha}, expected {expected}",
        )

    return {
        "id": entry["id"],
        "path": path,
        "source_commit": commit,
        "blob_sha": expected,
        "scope": entry.get("scope", "full file"),
    }


def main() -> None:
    root = Path(run_git(Path.cwd(), "rev-parse", "--show-toplevel").decode().strip())
    lock_path = root / LOCK_REL
    require(lock_path.is_file(), f"missing lock: {LOCK_REL}")
    lock = json.loads(lock_path.read_text())

    require(lock.get("schema") == EXPECTED_SCHEMA, "unexpected lock schema")
    source_commit = lock.get("local_source_commit")
    require(bool(source_commit), "missing local_source_commit")
    run_git(root, "cat-file", "-e", f"{source_commit}^{{commit}}")

    local_entries = lock.get("local_entries", [])
    external_entries = lock.get("external_entries", [])
    require(local_entries, "no local entries")
    require(external_entries, "no external entries")

    ids: set[str] = set()
    keys: set[tuple[str, str]] = set()
    checked: list[dict[str, str]] = []

    for kind, entries, default in (
        ("local", local_entries, source_commit),
        ("external", external_entries, None),
    ):
        for entry in entries:
            require(entry["id"] not in ids, f"duplicate id: {entry['id']}")
            ids.add(entry["id"])
            commit = entry.get("source_commit") or default
            key = (str(commit), entry["path"])
            require(key not in keys, f"duplicate source/path: {key}")
            keys.add(key)
            checked.append(validate_entry(root, entry, default, kind))

    l91112 = [x for x in checked if x["id"] == "L91112_RETAINED"]
    require(len(l91112) == 1, "expected exactly one L91112_RETAINED entry")
    require(l91112[0]["scope"] == L91112_SCOPE, "invalid L-91112 scope lock")

    required_interfaces = {
        "compact_causal_debt",
        "same_index_child_embedding",
        "complete_root_datum",
        "endpoint_deficit_bridge",
        "packet_envelope",
    }
    require(
        set(lock.get("interfaces", {})) == required_interfaces,
        "interface set is incomplete or contains unreviewed aliases",
    )

    result = {
        "classification": "PASS_T91652_FULL_LEDGER_LOCK",
        "schema": EXPECTED_SCHEMA,
        "local_source_commit": source_commit,
        "local_entries_checked": len(local_entries),
        "external_entries_checked": len(external_entries),
        "entries": checked,
        "scope_firewall": L91112_SCOPE,
        "mathematical_scope": (
            "Repository provenance only. This result does not certify theorem correctness "
            "or establish the Riemann Hypothesis."
        ),
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()

    output = root / RESULT_REL
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)


if __name__ == "__main__":
    main()
