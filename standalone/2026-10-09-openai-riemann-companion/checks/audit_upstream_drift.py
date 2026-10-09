#!/usr/bin/env python3
"""Compare both frozen Git trees; report source drift, not proof validity."""
from __future__ import annotations

import argparse
import collections
import json
from pathlib import Path
import subprocess

PACKET = Path(__file__).resolve().parents[1]
OLD = "adc7f1241b42e322a6451854ab7e4b4c146bf78a"
NEW = "fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb"


def tree(source: Path, commit: str) -> dict[str, dict[str, str]]:
    raw = subprocess.run(
        ["git", "-C", str(source), "ls-tree", "-r", "-z", commit],
        check=True, capture_output=True,
    ).stdout
    result = {}
    for record in raw.split(b"\0"):
        if not record:
            continue
        meta, path = record.split(b"\t", 1)
        mode, kind, blob = meta.decode("ascii").split()
        result[path.decode("utf-8")] = {"mode": mode, "type": kind, "blob": blob}
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    old, new = tree(args.source, OLD), tree(args.source, NEW)
    manifest = json.loads((PACKET / "SOURCE_MANIFEST.json").read_text())
    if manifest["upstream_commit"] != NEW or manifest["core_upstream_commit"] != OLD:
        raise ValueError("Manifest pins disagree with the fixed comparison")
    selected = manifest["files"]
    changes = []
    implementation = []
    seen = set()
    for row in selected:
        path = row["upstream_path"]
        if path in seen:
            raise ValueError(f"Duplicate selected path: {path}")
        seen.add(path)
        expected = {"mode": row["git_mode"], "type": "blob", "blob": row["git_blob_sha1"]}
        if new.get(path) != expected:
            raise ValueError(f"Manifest disagrees with new Git tree: {path}")
        if path.startswith("lean/OAI/") and path.endswith(".lean"):
            implementation.append(path)
        if old.get(path) != expected:
            changes.append({"path": path, "change": "added" if path not in old else "modified",
                            "old": old.get(path), "new": expected})
    statuses = collections.Counter()
    for path in old.keys() | new.keys():
        if old.get(path) != new.get(path):
            statuses["added" if path not in old else "deleted" if path not in new else "modified"] += 1
    report = {
        "status": "GIT_TREE_COMPARISON_ONLY",
        "repository": "https://github.com/openai/math",
        "old_commit": OLD, "new_commit": NEW,
        "global_changed_paths": sum(statuses.values()),
        "global_status_counts": dict(sorted(statuses.items())),
        "selected_files": len(selected),
        "implementation_modules": len(implementation),
        "selected_changes": changes,
        "changed_implementation_modules": [p for p in implementation if old.get(p) != new.get(p)],
        "proof_validity_checked": False,
    }
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    print(json.dumps({k: v for k, v in report.items() if k != "selected_changes"}, indent=2))
    print(f"Selected changes: {len(changes)}; details in output when --output is supplied.")


if __name__ == "__main__":
    main()
