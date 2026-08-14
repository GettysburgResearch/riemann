#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

SCHEMA = "riemann.t91656.final-single-sharp-lock.v1"
REQUIRED_LOAD = {"R91659", "L91666", "L91670", "L91671", "T91656"}
REQUIRED_FIREWALLS = {"R91658", "L91668_REJECTED", "L91669_SUPERSEDED", "T91655_REJECTED"}
FORBIDDEN_LOAD = {"L91668", "L91669", "T91655", "L91330_TWO_CHANNEL_ROW"}
EXPECTED_X91670 = "a5b07f68367447da089ef8d8fa84adf2ea2615b4fcbb8f038d7f23cf5dc49dda"


def git_blob_sha(data: bytes) -> str:
    header = b"blob " + str(len(data)).encode() + b"\0"
    return hashlib.sha1(header + data).hexdigest()


def canonical_json(data: Any) -> bytes:
    return json.dumps(data, sort_keys=True, separators=(",", ":")).encode()


def is_hex(value: str, size: int) -> bool:
    return len(value) == size and all(c in "0123456789abcdef" for c in value)


def verify(repo: Path, manifest_path: Path) -> dict[str, Any]:
    manifest = json.loads(manifest_path.read_text())
    assert manifest["schema"] == "riemann.t91656.single-sharp-dependency-manifest.v1"
    assert manifest["root_normalization"] == "single-SHARP: w_Psi=3*w_(4/3)"
    assert manifest["recursive_quantity"] == "equality deficit, then native loss"

    load = manifest["load_bearing"]
    ids = [item["id"] for item in load]
    paths = [item["path"] for item in load]
    assert len(ids) == len(set(ids))
    assert len(paths) == len(set(paths))
    assert REQUIRED_LOAD <= set(ids)
    assert not (FORBIDDEN_LOAD & set(ids))

    firewalls = {item["id"] for item in manifest["firewalls"]}
    assert REQUIRED_FIREWALLS <= firewalls

    checked: list[dict[str, str]] = []
    for item in load + manifest["firewalls"] + manifest["artifacts"]:
        blob = item["blob_sha"]
        assert is_hex(blob, 40), item
        path = repo / item["path"]
        assert path.is_file(), item["path"]
        actual = git_blob_sha(path.read_bytes())
        assert actual == blob, (item["id"], actual, blob)
        checked.append({"id": item["id"], "path": item["path"], "blob": actual})

    for group in ("external_transform_chain", "external_endpoint_chain"):
        for item in manifest[group]:
            assert is_hex(item["source_commit"], 40)
            assert is_hex(item["blob_sha"], 40)

    result_path = repo / "experiments/X-91670-single-sharp-normalization-hardening/results/verification.json"
    result = json.loads(result_path.read_text())
    assert result["classification"] == "PASS_SINGLE_SHARP_NORMALIZATION_HARDENING"
    assert result["proof_object_sha256"] == EXPECTED_X91670
    assert result["core"]["normalization"]["old_balanced_reserve_row_multiplier"] == 3
    assert result["core"]["normalization"]["single_sharp_row_multiplier"] == 1
    assert result["core"]["scope"]["rh_established_by_replay"] is False

    core = {
        "content_commit": manifest["content_commit"],
        "manifest_sha256": hashlib.sha256(canonical_json(manifest)).hexdigest(),
        "checked_local_objects": checked,
        "external_objects": sum(len(manifest[g]) for g in ("external_transform_chain", "external_endpoint_chain")),
        "x91670_proof_object": EXPECTED_X91670,
        "scope": {
            "repository_freeze_validated": True,
            "mathematics_validated": False,
            "rh_established": False,
        },
    }
    return {
        "schema": SCHEMA,
        "classification": "PASS_T91656_FINAL_SINGLE_SHARP_LOCK",
        "proof_object_sha256": hashlib.sha256(canonical_json(core)).hexdigest(),
        "core": core,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--json", type=Path, required=True)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    result = verify(args.repo_root, args.manifest)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
