#!/usr/bin/env python3
"""Import, authenticate, or assemble the pinned RH companion source bundle.

The original family-003 packet is immutable. Matching files are reused from it;
only additional or changed files reside in this packet's upstream directory.
The assembled view consists of the exact selected set, not a blind overlay.
This verifies source integrity and lexical import closure, NOT mathematical
correctness, Lean elaboration, Comparator equivalence, or external packages.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import shutil
import stat
import subprocess
import sys

PACKET = Path(__file__).resolve().parents[1]
CORE = PACKET.parent / "2026-10-07-openai-quasi-riemann-import"
SNAPSHOT = "fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb"
CORE_COMMIT = "adc7f1241b42e322a6451854ab7e4b4c146bf78a"
BASE_HEAD = "31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6"
REPOSITORY = "https://github.com/openai/math"
SCHEMA = "riemann-openai-companion-bundle-v1"
SELECTION_SCHEMA = "riemann-openai-companion-selection-v1"
FAMILY_COMPARATORS = {
    "007": ("OrdinaryElliott", "OrdinaryTwoPointCorrelations"),
    "011": (), "012": ("JointDickman",), "014": (),
    "021": ("Jacobsthal", "JacobsthalImproved"),
    "023": ("PattersonFirstMoment",), "026": ("PrimeGaps",),
    "029": (), "142": (), "182": ("SquareDifference",),
}
CORE_COMPARATORS = {"QuasiRiemannHypothesis", "DirichletSevenEighths",
                    "HeckeSevenEighths", "SiegelZeros"}
ADDITIONAL_FILES = {"history.md", "reasoning_traces/ordinary-two-point-correlations.pdf"}

# Reuse the historical, source-pinned path checks and Lean lexical filter.
sys.path.insert(0, str(CORE / "checks"))
import import_upstream as core_import
from audit_lean_sources import IMPORT_PATTERN, MARKER_PATTERN, mask_comments_and_literals
from verify_import import verify_packet as verify_core


def git(source: Path, *args: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(source), *args])


def safe_path(root: Path, relative: str, *, exists: bool = False) -> Path:
    return core_import.regular_file_path(root, relative, must_exist=exists)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def dump(path: Path, document: dict) -> None:
    path.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def selection() -> dict:
    value = json.loads(safe_path(PACKET, "SOURCE_SELECTION.json", exists=True).read_text())
    if not isinstance(value, dict):
        raise ValueError("Source selection must be a JSON object")
    for key, expected in {
        "schema": SELECTION_SCHEMA, "upstream_repository": "openai/math",
        "upstream_commit": SNAPSHOT, "prior_family003_commit": CORE_COMMIT,
        "base_pr": 908, "base_head": BASE_HEAD,
    }.items():
        if value.get(key) != expected or type(value.get(key)) is not type(expected):
            raise ValueError(f"Source-selection metadata mismatch: {key}")
    families = value.get("families")
    if (not isinstance(families, list) or not all(isinstance(f, dict) for f in families)
            or [f.get("family") for f in families] != list(FAMILY_COMPARATORS)):
        raise ValueError("Unexpected family selection")

    def paths(item: dict, key: str, *, nonempty: bool = False) -> list[str]:
        result = item.get(key)
        if not isinstance(result, list) or not all(isinstance(p, str) for p in result):
            raise ValueError(f"Selection {key} must be a list of paths")
        if len(set(result)) != len(result) or (nonempty and not result):
            raise ValueError(f"Empty or duplicate selection paths: {key}")
        for path in result:
            core_import.relative_posix_path(path)
        return result

    seen_directories = set()
    for family in families:
        number = family["family"]
        directories = paths(family, "manuscript_directories", nonempty=True)
        if any(len(d.split("/")) != 2 or not d.startswith("preprints/") for d in directories):
            raise ValueError(f"Invalid manuscript directory: {number}")
        if seen_directories.intersection(directories):
            raise ValueError(f"Repeated manuscript directory: {number}")
        seen_directories.update(directories)
        pdfs = paths(family, "pdf_paths", nonempty=True)
        if (any(not p.lower().endswith(".pdf") or not any(p.startswith(d + "/") for d in directories)
                for p in pdfs)
                or any(not any(p.startswith(d + "/") for p in pdfs) for d in directories)):
            raise ValueError(f"PDF paths do not cover the selected manuscript directories: {number}")
        roots = family.get("comparator_roots")
        if not isinstance(roots, list) or roots != list(FAMILY_COMPARATORS[number]):
            raise ValueError(f"Unexpected comparator roots: {number}")
        comparator_files = paths(family, "comparator_files")
        if set(comparator_files) != {f"lean/ComparatorChallenges/{stem}.lean" for stem in roots}:
            raise ValueError(f"Comparator paths disagree with roots: {number}")
        scopes = paths(family, "scope_docs")
        if scopes != ([f"lean/docs/{number}.md"] if roots else []):
            raise ValueError(f"Scope documents disagree with formalized families: {number}")
    if set(paths(value, "additional_files")) != ADDITIONAL_FILES:
        raise ValueError("Unexpected additional source selection")
    return value


def core_rows() -> dict:
    manifest = json.loads(safe_path(CORE, "UPSTREAM_FILES.json", exists=True).read_text())
    if manifest["upstream_commit"] != CORE_COMMIT:
        raise ValueError("Core snapshot mismatch")
    return {row["upstream_path"]: row for row in manifest["files"]}


def frozen_tree(source: Path) -> dict:
    entries = {}
    for raw in git(source, "ls-tree", "-r", "-z", SNAPSHOT).split(b"\0"):
        if not raw:
            continue
        metadata, path = raw.split(b"\t", 1)
        mode, kind, blob = metadata.decode().split()
        entries[path.decode()] = {"mode": mode, "type": kind, "blob": blob}
    return entries


def source_reader(source: Path, tree: dict, inherited: dict):
    cache = {}

    def read(path: str) -> bytes:
        if path in cache:
            return cache[path]
        core_import.relative_posix_path(path)
        item = tree.get(path)
        if item is None or item["type"] != "blob" or item["mode"] not in {"100644", "100755"}:
            raise ValueError(f"Missing or unsupported source object: {path}")
        old = inherited.get(path)
        if old and old["git_blob_sha1"] == item["blob"] and old["git_mode"] == item["mode"]:
            data = safe_path(CORE, "upstream/" + path, exists=True).read_bytes()
        elif (source / path).exists():
            data = safe_path(source, path, exists=True).read_bytes()
        else:
            # Works with a partial clone; Git may retrieve the pinned blob.
            data = git(source, "cat-file", "blob", item["blob"])
        if core_import.git_blob_id(data) != item["blob"]:
            raise ValueError(f"Bytes do not match frozen Git object: {path}")
        cache[path] = data
        return data

    return read


def lean_imports(path: str, data: bytes) -> tuple[list[str], list[dict]]:
    source = data.decode("utf-8")
    masked = mask_comments_and_literals(source)
    imports = []
    for match in IMPORT_PATTERN.finditer(masked):
        for module in match.group(1).split():
            if any(not part.replace("'", "_").isidentifier() for part in module.split(".")):
                raise ValueError(f"Unsupported import {module!r} in {path}")
            imports.append(module)
    markers = []
    if path.startswith("lean/OAI/"):
        for number, line in enumerate(masked.splitlines(), 1):
            markers.extend({"path": path, "line": number, "token": m.group()}
                           for m in MARKER_PATTERN.finditer(line))
    return imports, markers


def selected_paths_and_audit(policy: dict, inventory: set[str], inherited: dict, read) -> tuple[set[str], dict]:
    """Select resident paths and follow imports, or select from a full Git tree.

    A resident inventory can establish required entries and import closure, but
    cannot reveal an omitted, unreferenced file from an upstream directory.
    Only the full pinned Git inventory establishes that stronger completeness.
    """
    directories = list(core_import.DIRECTORIES)
    singles = set(core_import.SINGLE_FILES) | set(policy["additional_files"]) | set(inherited)
    comparator_stems = set(CORE_COMPARATORS)
    for family in policy["families"]:
        directories.extend(family["manuscript_directories"])
        singles.update(family["pdf_paths"])
        singles.update(family["scope_docs"])
        comparator_stems.update(family["comparator_roots"])
    for stem in comparator_stems:
        singles.update(f"lean/ComparatorChallenges/{stem}.{suffix}" for suffix in ("lean", "json"))
    paths = {p for p in inventory if p in singles or any(p.startswith(d + "/") for d in directories)}
    absent = singles - paths
    absent_directories = [d for d in directories if not any(p.startswith(d + "/") for p in paths)]
    if absent or absent_directories:
        raise ValueError(f"Missing required selection: {sorted(absent)}, {absent_directories}")
    pending = [p for p in paths if p.endswith(".lean") and p.startswith(("lean/OAI/", "lean/ComparatorChallenges/"))]
    roots, configs = [], {}
    for stem in sorted(comparator_stems):
        config = json.loads(read(f"lean/ComparatorChallenges/{stem}.json"))
        if not isinstance(config, dict) or config.get("challenge_module") != "ComparatorChallenges." + stem:
            raise ValueError(f"Comparator name mismatch: {stem}")
        root = config.get("solution_module")
        if (not isinstance(root, str) or not root.startswith("OAI.")
                or any(not part.replace("'", "_").isidentifier() for part in root.split("."))):
            raise ValueError(f"Non-internal solution root: {root}")
        roots.append(root)
        configs[stem] = config
        pending.append("lean/" + root.replace(".", "/") + ".lean")
    visited, external, markers = set(), set(), []
    total_lines = 0
    while pending:
        path = pending.pop()
        if path in visited:
            continue
        data = read(path)
        visited.add(path)
        paths.add(path)
        imports, found = lean_imports(path, data)
        markers.extend(found)
        if path.startswith("lean/OAI/"):
            total_lines += len(data.splitlines())
        for module in imports:
            if module.startswith(("OAI.", "ComparatorChallenges.")):
                pending.append("lean/" + module.replace(".", "/") + ".lean")
            else:
                external.add(module)
    audit = {
        "status": "LEXICAL_CLOSURE_ONLY", "solution_roots": sorted(set(roots)),
        "comparator_configurations": configs,
        "internal_modules": sum(p.startswith("lean/OAI/") for p in visited),
        "internal_source_lines": total_lines,
        "external_imports": sorted(external), "implementation_markers": sorted(markers, key=lambda x: (x["path"], x["line"])),
        "missing_internal_imports": [], "lean_or_comparator_executed": False,
    }
    return paths, audit


def selected_entries(source: Path) -> tuple[dict, dict, object]:
    """Recompute complete pinned directories and their internal import closure."""
    policy, tree, inherited = selection(), frozen_tree(source), core_rows()
    read = source_reader(source, tree, inherited)
    paths, audit = selected_paths_and_audit(policy, set(tree), inherited, read)
    return {p: tree[p] for p in sorted(paths)}, audit, read


def physical_path(row: dict) -> Path:
    if row.get("storage") not in {"core", "supplement"}:
        raise ValueError("Unknown source storage")
    root = CORE if row["storage"] == "core" else PACKET
    return safe_path(root, "upstream/" + row["upstream_path"], exists=True)


def physical_files() -> set[str]:
    root = PACKET / "upstream"
    if root.is_symlink() or not root.is_dir():
        raise ValueError("Supplement must be an ordinary directory")
    result = set()
    for path in root.rglob("*"):
        mode = path.lstat().st_mode
        if stat.S_ISLNK(mode) or not (stat.S_ISREG(mode) or stat.S_ISDIR(mode)):
            raise ValueError(f"Unsupported supplement object: {path}")
        if stat.S_ISREG(mode):
            result.add(path.relative_to(root).as_posix())
    return result


def import_bundle(source: Path) -> dict:
    verify_core(CORE, source)
    entries, audit, read = selected_entries(source)
    inherited = core_rows()
    rows, payloads = [], []
    for path, entry in entries.items():
        data = read(path)
        old = inherited.get(path)
        reuse = bool(old and old["git_blob_sha1"] == entry["blob"] and old["git_mode"] == entry["mode"])
        row = {"upstream_path": path, "storage": "core" if reuse else "supplement",
               "git_blob_sha1": entry["blob"], "git_mode": entry["mode"],
               "sha256": digest(data), "bytes": len(data)}
        rows.append(row)
        if not reuse:
            target = safe_path(PACKET, "upstream/" + path)
            if target.exists() and target.read_bytes() != data:
                raise ValueError(f"Refusing to overwrite changed supplement: {path}")
            payloads.append((target, data, entry["mode"]))
    # Preflight is complete before writing any source bytes.
    for target, data, mode in payloads:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        target.chmod(0o755 if mode == "100755" else 0o644)
    manifest = {
        "schema": SCHEMA, "upstream_repository": REPOSITORY, "upstream_commit": SNAPSHOT,
        "core_upstream_commit": CORE_COMMIT, "base_pr": 908, "base_head": BASE_HEAD,
        "selection_sha256": digest((PACKET / "SOURCE_SELECTION.json").read_bytes()),
        "core_manifest_sha256": digest((CORE / "UPSTREAM_FILES.json").read_bytes()),
        "file_count": len(rows), "total_bytes": sum(r["bytes"] for r in rows),
        "storage_counts": dict(Counter(r["storage"] for r in rows)),
        "storage_bytes": {k: sum(r["bytes"] for r in rows if r["storage"] == k) for k in ("core", "supplement")},
        "files": rows,
    }
    dump(safe_path(PACKET, "SOURCE_MANIFEST.json"), manifest)
    dump(safe_path(PACKET, "checks/artifacts/dependency-audit.json"), audit)
    return verify_bundle(source)


def verify_bundle(source: Path | None = None) -> dict:
    policy = selection()
    core_result = verify_core(CORE, source)
    manifest = json.loads(safe_path(PACKET, "SOURCE_MANIFEST.json", exists=True).read_text())
    for key, expected in {"schema": SCHEMA, "upstream_repository": REPOSITORY, "upstream_commit": SNAPSHOT,
                          "core_upstream_commit": CORE_COMMIT, "base_head": BASE_HEAD, "base_pr": 908,
                          "selection_sha256": digest((PACKET / "SOURCE_SELECTION.json").read_bytes()),
                          "core_manifest_sha256": digest((CORE / "UPSTREAM_FILES.json").read_bytes())}.items():
        if manifest.get(key) != expected:
            raise ValueError(f"Manifest metadata mismatch: {key}")
    rows, inherited = manifest["files"], core_rows()
    names, supplement, total = set(), set(), 0
    for row in rows:
        path = row["upstream_path"]
        core_import.relative_posix_path(path)
        if path in names:
            raise ValueError(f"Duplicate source entry: {path}")
        names.add(path)
        if row.get("git_mode") not in {"100644", "100755"} or type(row.get("bytes")) is not int:
            raise ValueError(f"Invalid source metadata: {path}")
        old = inherited.get(path)
        reuse = bool(old and old["git_blob_sha1"] == row["git_blob_sha1"] and old["git_mode"] == row["git_mode"])
        if row.get("storage") != ("core" if reuse else "supplement"):
            raise ValueError(f"Noncanonical source storage: {path}")
        if not reuse:
            supplement.add(path)
        file = physical_path(row)
        data = file.read_bytes()
        if len(data) != row["bytes"] or digest(data) != row["sha256"] or core_import.git_blob_id(data) != row["git_blob_sha1"]:
            raise ValueError(f"Source integrity failure: {path}")
        if bool(file.stat().st_mode & stat.S_IXUSR) != (row["git_mode"] == "100755"):
            raise ValueError(f"Executable-mode mismatch: {path}")
        total += len(data)
    if names != {r["upstream_path"] for r in rows} or physical_files() != supplement:
        raise ValueError("Supplement has missing or unlisted files")
    counts = dict(Counter(r["storage"] for r in rows))
    storage_bytes = {k: sum(r["bytes"] for r in rows if r["storage"] == k) for k in ("core", "supplement")}
    if len(rows) != manifest["file_count"] or total != manifest["total_bytes"] or counts != manifest["storage_counts"] or storage_bytes != manifest["storage_bytes"]:
        raise ValueError("Manifest totals mismatch")
    if source is not None:
        expected, audit, _ = selected_entries(source)
        if names != set(expected):
            raise ValueError("Complete frozen selection differs from manifest")
        for row in rows:
            item = expected[row["upstream_path"]]
            if item["blob"] != row["git_blob_sha1"] or item["mode"] != row["git_mode"]:
                raise ValueError(f"Frozen Git-tree mismatch: {row['upstream_path']}")
    else:
        by_path = {row["upstream_path"]: row for row in rows}

        def read_resident(path: str) -> bytes:
            if path not in by_path:
                raise ValueError(f"Missing resident internal dependency: {path}")
            return physical_path(by_path[path]).read_bytes()

        expected_paths, audit = selected_paths_and_audit(policy, names, inherited, read_resident)
        if names != expected_paths:
            raise ValueError("Manifest contains paths outside the required selection and import closure")
    recorded = json.loads(safe_path(PACKET, "checks/artifacts/dependency-audit.json", exists=True).read_text())
    if recorded != audit:
        raise ValueError("Recomputed dependency audit differs")
    return {"status": "PASS", "check": "source integrity and lexical closure, not theorem verification",
            "upstream_commit": SNAPSHOT, "files": len(rows), "bytes": total,
            "storage_counts": counts, "storage_bytes": storage_bytes,
            "required_selection_and_internal_closure_checked": True,
            "recorded_dependency_audit_compared": True,
            "complete_frozen_selection_compared": source is not None,
            "core_files_verified": core_result["files"], "kernel_build_run": False}


def assemble(output: Path, source: Path | None) -> dict:
    result = verify_bundle(source)
    output = output.absolute()
    if output.is_symlink() or (output.exists() and (not output.is_dir() or any(output.iterdir()))):
        raise ValueError("Assembly destination must be absent or an empty ordinary directory")
    manifest = json.loads((PACKET / "SOURCE_MANIFEST.json").read_text())
    for row in manifest["files"]:
        safe_path(output, row["upstream_path"])
    output.mkdir(parents=True, exist_ok=True)
    for row in manifest["files"]:
        target = safe_path(output, row["upstream_path"])
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(physical_path(row), target)
        target.chmod(0o755 if row["git_mode"] == "100755" else 0o644)
    result["assembled_view"] = str(output)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("import", "verify", "assemble"))
    parser.add_argument("--source", type=Path, help="Independently fetched openai/math Git checkout")
    parser.add_argument("--output", type=Path, help="Fresh directory for assemble mode")
    args = parser.parse_args()
    if args.mode == "import" and args.source is None:
        parser.error("import requires --source")
    if args.mode == "assemble" and args.output is None:
        parser.error("assemble requires --output")
    try:
        if args.mode == "import":
            result = import_bundle(args.source.resolve())
        elif args.mode == "verify":
            result = verify_bundle(args.source.resolve() if args.source else None)
        else:
            result = assemble(args.output, args.source.resolve() if args.source else None)
    except (OSError, ValueError, KeyError, TypeError, subprocess.CalledProcessError) as exc:
        raise SystemExit(str(exc)) from None
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
