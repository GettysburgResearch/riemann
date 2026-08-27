#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FORMAL = ROOT / "formal"
REGISTRY = FORMAL / "registry"
MANIFEST = REGISTRY / "FORMAL_V0_1_MANIFEST.json"
MAP = REGISTRY / "FORMALIZATION_MAP.tsv"

EXPECTED_SOURCES = {
    "A": "ae0887b8125601c98dc809cffe01c7f1c78bb998",
    "B": "6d42bbc31c81e7d6a03909e205b56f30f6f7b49a",
    "C": "381a5a98ade7c6bad7122e5182c2fc07332dc747",
}
EXPECTED_TOPICS = {
    "RH",
    "MellinAPI",
    "ArithmeticRows23",
    "FixedDetectorFiveThree",
    "OperatorPositiveSchurRescue",
    "XiPickThreeNode",
    "XiPickOrderThreeConditional",
}
REQUIRED_LITERAL_STATUS = {
    "Riemann Hypothesis: UNPROVED",
    "Unconditional Lean theorem proving RH: NONE",
    "Conditional Lean theorem concluding RH: PRESENT, with every open premise explicit",
    "Trusted sorry/admit/custom axiom: NONE",
    "Challenge-only statement placeholders: EXACTLY SEVEN",
    "Post-PR-707 research: EXCLUDED",
    "Heavy numerical campaigns: NOT RUN",
}


def read_tsv(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        raise SystemExit(f"missing TSV: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def main() -> None:
    if not MANIFEST.is_file():
        raise SystemExit(f"missing release manifest: {MANIFEST}")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if manifest.get("schema") != "riemann-formal-v0.1-release-manifest-v1":
        raise SystemExit("wrong formal-v0.1 manifest schema")
    if manifest.get("scientific_status") != "RIEMANN_HYPOTHESIS_UNPROVED":
        raise SystemExit("manifest does not preserve RH-unproved status")
    if manifest.get("formal_bootstrap") != "573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f":
        raise SystemExit("wrong formal bootstrap lock")
    for owner, commit in EXPECTED_SOURCES.items():
        actual = manifest["formal_sources"][owner]["commit"]
        if actual != commit:
            raise SystemExit(f"wrong source lock for {owner}: {actual}")

    rows = read_tsv(MAP)
    if len(rows) != 139:
        raise SystemExit(f"expected 139 canonical map rows, found {len(rows)}")
    semantic_ids = [row["semantic_id"] for row in rows]
    if len(set(semantic_ids)) != 139:
        raise SystemExit("duplicate semantic ID in generated formalization map")
    statuses = Counter(row["formal_status"] for row in rows)
    expected_counts = manifest["registry_expectations"]
    for status in ("STATED", "PROVED", "PROVED_CONDITIONAL"):
        expected = int(expected_counts[status])
        if statuses[status] != expected:
            raise SystemExit(
                f"formal status count mismatch for {status}: {statuses[status]} != {expected}"
            )

    claimed: dict[str, str] = {}
    total = 0
    for owner in ("A", "B", "C"):
        path = REGISTRY / "deltas" / f"{owner}.tsv"
        for row in read_tsv(path):
            sid = row.get("semantic_id", "").strip()
            if not sid:
                continue
            total += 1
            if sid in claimed:
                raise SystemExit(f"duplicate canonical delta owner for {sid}: {claimed[sid]}, {owner}")
            claimed[sid] = owner
    if total != 31:
        raise SystemExit(f"expected 31 canonical delta rows, found {total}")
    if claimed.get("API.MELLIN.SUBPOWER_NEGATIVE_MASS") != "A":
        raise SystemExit("subpower negative-mass API is not owned uniquely by A")

    api_rows = read_tsv(REGISTRY / "deltas" / "C_API.tsv")
    if len(api_rows) != 6:
        raise SystemExit(f"expected six C API rows, found {len(api_rows)}")

    challenge_dir = FORMAL / "comparator" / "Challenge" / "RiemannComparatorChallenge"
    topics = {path.stem for path in challenge_dir.glob("*.lean")}
    if topics != EXPECTED_TOPICS:
        raise SystemExit(
            f"comparator topic inventory mismatch: expected={sorted(EXPECTED_TOPICS)} actual={sorted(topics)}"
        )

    analysis_aggregate = (FORMAL / "RiemannFormal" / "Analysis.lean").read_text(
        encoding="utf-8"
    )
    if "Analysis.ComparatorSmoke" in analysis_aggregate:
        raise SystemExit("ComparatorSmoke leaked into the trusted Analysis aggregate")

    front_door = (FORMAL / "FORMAL_V0_1.md").read_text(encoding="utf-8")
    for literal in REQUIRED_LITERAL_STATUS:
        if literal not in front_door:
            raise SystemExit(f"missing literal release status: {literal}")

    required_files = [
        FORMAL / "RESULTS.md",
        FORMAL / "OPEN_GATES.md",
        FORMAL / "TRUST.md",
        REGISTRY / "FORMAL_V0_1_THEOREMS.tsv",
        REGISTRY / "FORMAL_V0_1_EXCLUSIONS.tsv",
        FORMAL / "RiemannFormal" / "Release.lean",
    ]
    for path in required_files:
        if not path.is_file():
            raise SystemExit(f"missing formal-v0.1 release file: {path}")

    print(
        "PASS_FORMAL_V0_1_RELEASE_MANIFEST "
        f"claims={len(rows)} delta_rows={total} topics={len(topics)} "
        f"stated={statuses['STATED']} proved={statuses['PROVED']} "
        f"conditional={statuses['PROVED_CONDITIONAL']}"
    )


if __name__ == "__main__":
    main()
