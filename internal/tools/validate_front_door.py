#!/usr/bin/env python3
"""Lightweight validation for the durable Riemann repository front door.

The validator checks information architecture, links, provenance headings,
stable machine-contract identities, and compatibility wrappers. It performs no
mathematical, zero, prime, interval, spectral, special-function, Robin, or
matrix-production computation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import sys
from urllib.parse import unquote

DEFAULT_ROOT = pathlib.Path(__file__).resolve().parents[2]

REQUIRED = [
    "README.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "research/README.md",
    "research/RESULTS_INDEX.md",
    "research/IMPORT_MANIFEST.md",
    "research/integrated/README.md",
    "research/integrated/corrections/proof-boundary-corrections.md",
    "research/integrated/robin/finite-robin-foundations.md",
    "research/integrated/xi/derivative-free-pick-loewner.md",
    "research/integrated/xi/finite-pick-controls.md",
    "research/exploratory/README.md",
    "canonical/README.md",
    "canonical/registry.yaml",
    "canonical/aliases.yaml",
    "canonical/provenance.schema.json",
    "internal/README.md",
    "internal/archive/README.md",
    "internal/registry/README.md",
    "internal/tools/README.md",
    "internal/tools/capture_snapshot.py",
    "internal/tools/validate_front_door.py",
    "internal/tools/archive/validate_integration_20260801.py",
    "integration/README.md",
    "scripts/integration/README.md",
    "scripts/integration/capture_snapshot.py",
    "scripts/integration/validate_integration.py",
]

FORBIDDEN = [
    "START_HERE.md",
    "RESEARCH_MAP.md",
    "FRONTIERS.md",
    ".github/workflows/integration-snapshot.yml",
    "internal/registry/registry.yaml",
    "internal/registry/aliases.yaml",
    "internal/registry/provenance.schema.json",
]

CURATED_MARKDOWN = [
    pathlib.Path(path)
    for path in REQUIRED
    if path.endswith(".md")
]

PACKETS = [
    pathlib.Path("research/integrated/corrections/proof-boundary-corrections.md"),
    pathlib.Path("research/integrated/robin/finite-robin-foundations.md"),
    pathlib.Path("research/integrated/xi/derivative-free-pick-loewner.md"),
    pathlib.Path("research/integrated/xi/finite-pick-controls.md"),
]

EXPECTED_CANONICAL_BLOBS = {
    "canonical/registry.yaml": "fcdd9200753c62413ae3519223bb3c72588405e1",
    "canonical/aliases.yaml": "bd71c06c3234660c448ba6beab6e8fb030242ed6",
    "canonical/provenance.schema.json": "ea21850a9c095348a39598b60aeb233df6349cef",
}

EXPECTED_REGISTRY_IDS = [
    "CANON-REVIEW-WAVE-20260801",
    "CANON-ROBIN-FINITE-BASE",
    "CANON-ROBIN-POWERED-ENVELOPE",
    "CANON-XI-SECANT-LOEWNER",
    "CANON-XI-BARYCENTRIC-MATCHED",
    "CANON-CARRIER-FIXED-VECTOR-POSITIVE",
    "CANON-PICK-BOX-POSITIVE",
    "CANON-PICK-WHOLE-MATRIX-RECHECK",
    "CANON-DIRECT-XI-PR71-PACKET",
    "CANON-POSITIVE-ANCHOR-ONE-SCALAR",
    "CANON-AUDIT-LOCAL-GLOBAL",
    "CANON-AUDIT-HERMITE-TARGETED-LI",
    "CANON-CARDINAL-FINITE-SECTION",
    "CANON-THREE-BLOCK-SCHUR",
    "CANON-DEFICIT-AUGMENTATION",
    "CANON-KERNEL-DEFECT-BOUNDARY",
    "CANON-LOCAL-MOBIUS-INVERSION",
    "CANON-TWO-FRAME-SCHUR",
]

LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
ID_RE = re.compile(r"^\s*-\s+id:\s+([A-Za-z0-9_.:-]+)\s*$", re.MULTILINE)
STALE_RE = re.compile(
    r"\bRound\s+[12]\b|draft\s+PR\s*#?214|PR\s*#214",
    re.IGNORECASE,
)


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def parse_external_shas(values: list[str]) -> dict[str, str]:
    result: dict[str, str] = {}
    for value in values:
        if "=" not in value:
            fail(f"bad --canonical-sha value: {value!r}")
        path, sha = value.split("=", 1)
        path = path.strip()
        sha = sha.strip().lower()
        if not re.fullmatch(r"[0-9a-f]{40}", sha):
            fail(f"bad Git blob SHA for {path}: {sha!r}")
        result[path] = sha
    return result


def check_paths(root: pathlib.Path) -> None:
    missing = [path for path in REQUIRED if not (root / path).is_file()]
    if missing:
        fail("missing required files: " + ", ".join(missing))
    present_forbidden = [path for path in FORBIDDEN if (root / path).exists()]
    if present_forbidden:
        fail("forbidden/stale paths remain: " + ", ".join(present_forbidden))


def check_readme(root: pathlib.Path) -> None:
    text = (root / "README.md").read_text(encoding="utf-8")
    if "RH remains unsolved" not in text:
        fail("README must state exactly that RH remains unsolved")
    if "integration/2026-08-01/PR_LEDGER.md" in text:
        fail("README must not route newcomers directly to the complete ledger")
    match = re.search(r"^## Begin here\s*$([\s\S]*?)(?=^##\s)", text, re.MULTILINE)
    if not match:
        fail("README lacks a durable 'Begin here' section")
    numbered = re.findall(r"^\d+\.\s", match.group(1), re.MULTILINE)
    if len(numbered) != 2:
        fail(f"README human entry must offer exactly two numbered choices, found {len(numbered)}")
    for required_link in (
        "research/RESULTS_INDEX.md",
        "research/integrated/README.md",
        "AGENTS.md",
    ):
        if required_link not in text:
            fail(f"README lacks required navigation target {required_link}")


def check_status_and_stale_language(root: pathlib.Path) -> None:
    for relative in CURATED_MARKDOWN:
        text = (root / relative).read_text(encoding="utf-8")
        if STALE_RE.search(text):
            fail(f"{relative}: contains temporary task/PR language")
        if relative in PACKETS:
            lowered = text.lower()
            for label in (
                "packet status",
                "scope:",
                "global status",
                "review evidence",
                "source",
            ):
                if label not in lowered:
                    fail(f"{relative}: missing packet provenance label {label!r}")
            if "rh remains unsolved" not in lowered:
                fail(f"{relative}: must state that RH remains unsolved")


def check_links(root: pathlib.Path) -> None:
    errors: list[str] = []
    resolved_root = root.resolve()
    for relative in CURATED_MARKDOWN:
        path = root / relative
        text = path.read_text(encoding="utf-8")
        for raw_target in LINK_RE.findall(text):
            target = raw_target.strip().split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            target = unquote(target)
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(resolved_root)
            except ValueError:
                errors.append(f"{relative}: link escapes repository: {raw_target}")
                continue
            if not resolved.exists():
                errors.append(f"{relative}: missing link target: {raw_target}")
    if errors:
        fail("\n  ".join(errors))


def check_results_index(root: pathlib.Path) -> None:
    text = (root / "research/RESULTS_INDEX.md").read_text(encoding="utf-8")
    for marker in ("LOCAL_PACKET", "SOURCE_PINNED", "BLOCKED_INTERFACE", "ARCHIVAL_METADATA"):
        if marker not in text:
            fail(f"results index lacks residency marker {marker}")
    missing_ids = [item for item in EXPECTED_REGISTRY_IDS if item not in text]
    if missing_ids:
        fail("results index omits registry families: " + ", ".join(missing_ids))
    if "Why there is no resident operator packet yet" not in text:
        fail("results index must state the operator import decision")
    if "Why there is no resident Weil/screw packet yet" not in text:
        fail("results index must state the Weil/screw import decision")
    if len(re.findall(r"\b[0-9a-f]{40}\b", text)) < 24:
        fail("results index lacks sufficient exact-SHA provenance")


def check_canonical_contract(
    root: pathlib.Path,
    external_shas: dict[str, str],
) -> None:
    for path, expected in EXPECTED_CANONICAL_BLOBS.items():
        if path in external_shas:
            actual = external_shas[path]
        else:
            actual = git_blob_sha1((root / path).read_bytes())
        if actual != expected:
            fail(f"{path}: stable Git blob changed: expected {expected}, got {actual}")

    registry_text = (root / "canonical/registry.yaml").read_text(encoding="utf-8")
    ids = ID_RE.findall(registry_text)
    if ids != EXPECTED_REGISTRY_IDS:
        fail(f"canonical registry ID/order mismatch: {ids!r}")

    aliases_text = (root / "canonical/aliases.yaml").read_text(encoding="utf-8")
    if not aliases_text.startswith("schema: riemann.canonical.aliases.v1\n"):
        fail("canonical aliases schema changed")

    schema = json.loads(
        (root / "canonical/provenance.schema.json").read_text(encoding="utf-8")
    )
    expected_id = "https://github.com/gfreund123/riemann/canonical/provenance.schema.json"
    if schema.get("$id") != expected_id:
        fail("canonical JSON Schema $id changed")
    if schema.get("properties", {}).get("source", {}).get("properties", {}).get("commit") is None:
        fail("canonical schema lost exact source-commit binding")


def check_wrappers(root: pathlib.Path) -> None:
    wrappers = {
        "scripts/integration/capture_snapshot.py": "internal/tools/capture_snapshot.py",
        "scripts/integration/validate_integration.py": "internal/tools/validate_front_door.py",
    }
    for path, target in wrappers.items():
        source = (root / path).read_text(encoding="utf-8")
        compile(source, str(root / path), "exec")
        if target not in source.replace('"', "").replace("'", ""):
            if pathlib.Path(target).name not in source:
                fail(f"{path}: does not target {target}")
    compile(
        (root / "internal/tools/capture_snapshot.py").read_text(encoding="utf-8"),
        "internal/tools/capture_snapshot.py",
        "exec",
    )
    compile(
        (root / "internal/tools/validate_front_door.py").read_text(encoding="utf-8"),
        "internal/tools/validate_front_door.py",
        "exec",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        type=pathlib.Path,
        default=DEFAULT_ROOT,
        help="repository root; defaults to the checkout containing this script",
    )
    parser.add_argument(
        "--canonical-sha",
        action="append",
        default=[],
        metavar="PATH=GIT_BLOB_SHA",
        help=(
            "supply an independently queried Git blob SHA for a canonical file; "
            "useful when validating a staged mirror without copying the full machine files"
        ),
    )
    args = parser.parse_args()
    root = args.root.resolve()
    external_shas = parse_external_shas(args.canonical_sha)

    check_paths(root)
    check_readme(root)
    check_status_and_stale_language(root)
    check_links(root)
    check_results_index(root)
    check_canonical_contract(root, external_shas)
    check_wrappers(root)

    print("PASS: durable front door is internally consistent")
    print(f"  curated Markdown files checked: {len(CURATED_MARKDOWN)}")
    print(f"  reviewed registry families indexed: {len(EXPECTED_REGISTRY_IDS)}")
    print("  canonical machine blobs: compatibility-stable")
    print("  local/source-pinned residency distinction: present")
    print("  temporary task language: absent")
    print("  retired integration snapshot workflow: absent")
    print("  compatibility wrappers: syntax and targets valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
