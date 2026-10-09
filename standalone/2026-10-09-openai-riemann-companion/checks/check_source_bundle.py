#!/usr/bin/env python3
"""Exercise companion source-bundle invariants in isolated temporary fixtures.

The old core verifier is stubbed only within each fixture to isolate the new
checker; run source_bundle.py verify separately against the real resident core.
These are integrity, selection, closure and assembly checks, not Lean tests.
The fake fixture sources intentionally do not claim mathematical content or
independent authentication against the public Git snapshot.
"""
from __future__ import annotations

from collections import Counter
from contextlib import contextmanager
import copy
import importlib.util
import json
from pathlib import Path
import stat
import tempfile


SCRIPT = Path(__file__).with_name("source_bundle.py")
spec = importlib.util.spec_from_file_location("companion_under_review", SCRIPT)
assert spec and spec.loader
bundle = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bundle)
POLICY = json.loads((bundle.PACKET / "SOURCE_SELECTION.json").read_text())
CONFIGS = json.loads((bundle.PACKET / "checks/artifacts/dependency-audit.json").read_text())["comparator_configurations"]
CORE_PATH = "lean/OAI/Review/Core.lean"
DEPENDENCY_PATH = "lean/OAI/Review/Dependency.lean"
UNREFERENCED_PATH = POLICY["families"][0]["manuscript_directories"][0] + "/REVIEW_FIXTURE.txt"
RESULTS = []


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n")


def metadata(path: str, storage: str, content: bytes) -> dict:
    return {"upstream_path": path, "storage": storage,
            "git_blob_sha1": bundle.core_import.git_blob_id(content), "git_mode": "100644",
            "sha256": bundle.digest(content), "bytes": len(content)}


def recalculate(manifest: dict) -> None:
    rows = manifest["files"]
    manifest.update(file_count=len(rows), total_bytes=sum(r["bytes"] for r in rows),
                    storage_counts=dict(Counter(r["storage"] for r in rows)),
                    storage_bytes={key: sum(r["bytes"] for r in rows if r["storage"] == key)
                                   for key in ("core", "supplement")})


@contextmanager
def fixture():
    with tempfile.TemporaryDirectory(prefix="rh-companion-review-") as directory:
        parent = Path(directory)
        saved = bundle.PACKET, bundle.CORE, bundle.verify_core
        bundle.PACKET, bundle.CORE = parent / "companion", parent / "core"
        bundle.verify_core = lambda *_: {"files": 1}
        write_json(bundle.PACKET / "SOURCE_SELECTION.json", copy.deepcopy(POLICY))
        sources = {path: b"Fixture only.\n" for path in bundle.core_import.SINGLE_FILES}
        for path in POLICY["additional_files"]:
            sources[path] = b"Fixture only.\n"
        for directory_name in bundle.core_import.DIRECTORIES:
            sources[directory_name + "/REVIEW_FIXTURE.txt"] = b"Fixture only.\n"
        for family in POLICY["families"]:
            for path in family["pdf_paths"] + family["scope_docs"]:
                sources[path] = b"Fixture only.\n"
        sources[UNREFERENCED_PATH] = b"Unreferenced manuscript companion fixture.\n"
        for stem, config in CONFIGS.items():
            sources[f"lean/ComparatorChallenges/{stem}.json"] = (json.dumps(config) + "\n").encode()
            sources[f"lean/ComparatorChallenges/{stem}.lean"] = ("import " + config["solution_module"] + "\n").encode()
            sources["lean/" + config["solution_module"].replace(".", "/") + ".lean"] = b"import OAI.Review.Dependency\n"
        sources[DEPENDENCY_PATH] = b"import OAI.Review.Core\n"
        sources[CORE_PATH] = b"namespace OAI\nend OAI\n"
        rows = []
        for path, data in sorted(sources.items()):
            storage = "core" if path == CORE_PATH else "supplement"
            root = bundle.CORE if storage == "core" else bundle.PACKET
            file = root / "upstream" / path
            file.parent.mkdir(parents=True, exist_ok=True)
            file.write_bytes(data)
            file.chmod(0o644)
            rows.append(metadata(path, storage, data))
        write_json(bundle.CORE / "UPSTREAM_FILES.json", {
            "upstream_commit": bundle.CORE_COMMIT,
            "files": [row for row in rows if row["storage"] == "core"],
        })
        manifest = {"schema": bundle.SCHEMA, "upstream_repository": bundle.REPOSITORY,
                    "upstream_commit": bundle.SNAPSHOT, "core_upstream_commit": bundle.CORE_COMMIT,
                    "base_head": bundle.BASE_HEAD, "base_pr": 908,
                    "selection_sha256": bundle.digest((bundle.PACKET / "SOURCE_SELECTION.json").read_bytes()),
                    "core_manifest_sha256": bundle.digest((bundle.CORE / "UPSTREAM_FILES.json").read_bytes()),
                    "files": rows}
        recalculate(manifest)
        write_json(bundle.PACKET / "SOURCE_MANIFEST.json", manifest)
        # All internal fixture files are reached by the ten distinct solution
        # roots and their two shared dependencies. No fixture imports externals.
        implementations = {p: data for p, data in sources.items() if p.startswith("lean/OAI/") and p.endswith(".lean")}
        audit = {"status": "LEXICAL_CLOSURE_ONLY",
                 "solution_roots": sorted({c["solution_module"] for c in CONFIGS.values()}),
                 "comparator_configurations": CONFIGS,
                 "internal_modules": len(implementations),
                 "internal_source_lines": sum(len(data.splitlines()) for data in implementations.values()),
                 "external_imports": [], "implementation_markers": [], "missing_internal_imports": [],
                 "lean_or_comparator_executed": False}
        write_json(bundle.PACKET / "checks/artifacts/dependency-audit.json", audit)
        try:
            yield manifest, parent
        finally:
            bundle.PACKET, bundle.CORE, bundle.verify_core = saved


def run(name, change, *, rejection: str | None = None):
    with fixture() as (manifest, parent):
        change(manifest, parent)
        recalculate(manifest)
        write_json(bundle.PACKET / "SOURCE_MANIFEST.json", manifest)
        try:
            result = bundle.verify_bundle()
        except (OSError, ValueError, KeyError, TypeError) as error:
            if rejection is None or rejection not in str(error):
                raise AssertionError(f"{name}: unexpected rejection: {error}") from error
            RESULTS.append({"case": name, "status": "PASS", "rejected": str(error)})
        else:
            if rejection is not None:
                raise AssertionError(f"{name}: required rejection did not occur")
            assert result["status"] == "PASS"
            assert result["required_selection_and_internal_closure_checked"] is True
            assert result["recorded_dependency_audit_compared"] is True
            assert result["complete_frozen_selection_compared"] is False
            assert result["kernel_build_run"] is False
            RESULTS.append({"case": name, "status": "PASS"})


def corrupt_core(_, __):
    (bundle.CORE / "upstream" / CORE_PATH).write_bytes(b"corrupt\n")


def extra_file(_, __):
    (bundle.PACKET / "upstream/undeclared.txt").write_text("extra")


def symlink(_, __):
    file = bundle.PACKET / "upstream" / DEPENDENCY_PATH
    file.unlink()
    file.symlink_to(bundle.CORE / "upstream" / CORE_PATH)


def redundant_supplement(manifest, _):
    row = next(row for row in manifest["files"] if row["upstream_path"] == CORE_PATH)
    data = (bundle.CORE / "upstream" / CORE_PATH).read_bytes()
    file = bundle.PACKET / "upstream" / CORE_PATH
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_bytes(data)
    row["storage"] = "supplement"


def remove_file(manifest, path):
    manifest["files"] = [row for row in manifest["files"] if row["upstream_path"] != path]
    (bundle.PACKET / "upstream" / path).unlink()


def change_policy(manifest, update):
    file = bundle.PACKET / "SOURCE_SELECTION.json"
    policy = json.loads(file.read_text())
    update(policy)
    write_json(file, policy)
    manifest["selection_sha256"] = bundle.digest(file.read_bytes())


def stale_audit(_, __):
    path = bundle.PACKET / "checks/artifacts/dependency-audit.json"
    audit = json.loads(path.read_text())
    audit["internal_modules"] += 1
    write_json(path, audit)


def unselected_declared_file(manifest, _):
    path, data = "lean/OAI/Unselected/Unreferenced.lean", b"namespace OAI\nend OAI\n"
    file = bundle.PACKET / "upstream" / path
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_bytes(data)
    manifest["files"].append(metadata(path, "supplement", data))


def main():
    run("valid_resident_selection_and_closure", lambda *_: None)
    run("corrupt_shared_core_byte", corrupt_core, rejection="Source integrity failure")
    run("wrong_snapshot", lambda m, _: m.update(upstream_commit="0" * 40), rejection="Manifest metadata mismatch")
    run("duplicate_entry", lambda m, _: m["files"].append(copy.deepcopy(m["files"][0])), rejection="Duplicate source entry")
    run("path_traversal", lambda m, _: m["files"][0].update(upstream_path="../escape"), rejection="Invalid relative path")
    run("symlink_source", symlink, rejection="Symlink in file path")
    run("undeclared_supplement_file", extra_file, rejection="Supplement has missing or unlisted files")
    run("identical_core_file_stored_again", redundant_supplement, rejection="Noncanonical source storage")
    run("omitted_dependency_after_manifest_rewrite", lambda m, _: remove_file(m, DEPENDENCY_PATH), rejection="Missing resident internal dependency")
    pdf = POLICY["families"][0]["pdf_paths"][0]
    run("omitted_required_pdf_after_manifest_rewrite", lambda m, _: remove_file(m, pdf), rejection="Missing required selection")
    run("wrong_prior_pin_in_policy", lambda m, _: change_policy(m, lambda p: p.update(prior_family003_commit="0" * 40)), rejection="Source-selection metadata mismatch")
    run("wrong_policy_schema", lambda m, _: change_policy(m, lambda p: p.update(schema="unrecognized")), rejection="Source-selection metadata mismatch")
    run("wrong_policy_repository", lambda m, _: change_policy(m, lambda p: p.update(upstream_repository="unrelated/repo")), rejection="Source-selection metadata mismatch")
    run("wrong_policy_base_pr", lambda m, _: change_policy(m, lambda p: p.update(base_pr=909)), rejection="Source-selection metadata mismatch")
    run("inconsistent_comparator_paths", lambda m, _: change_policy(m, lambda p: p["families"][0]["comparator_files"].append("lean/ComparatorChallenges/Unknown.lean")), rejection="Comparator paths disagree")
    run("policy_path_traversal", lambda m, _: change_policy(m, lambda p: p["families"][0].update(pdf_paths=["../escape.pdf"])), rejection="Invalid relative path")
    run("stale_dependency_audit", stale_audit, rejection="Recomputed dependency audit differs")
    run("unselected_declared_internal_file", unselected_declared_file, rejection="outside the required selection and import closure")
    # Without the pinned Git tree the checker cannot know about an omitted
    # unreferenced manuscript file. The result must keep full completeness false.
    run("offline_does_not_claim_full_git_directory_completeness", lambda m, _: remove_file(m, UNREFERENCED_PATH))
    with fixture() as (manifest, parent):
        view = parent / "assembled"
        bundle.assemble(view, None)
        files = {p.relative_to(view).as_posix() for p in view.rglob("*") if p.is_file()}
        assert files == {row["upstream_path"] for row in manifest["files"]}
        for row in manifest["files"]:
            file = view / row["upstream_path"]
            assert bundle.digest(file.read_bytes()) == row["sha256"]
            assert bool(file.stat().st_mode & stat.S_IXUSR) == (row["git_mode"] == "100755")
        RESULTS.append({"case": "fresh_assembly_exact_paths_hashes_and_modes", "status": "PASS"})
        try:
            bundle.assemble(view, None)
        except ValueError as error:
            assert "empty ordinary directory" in str(error)
            RESULTS.append({"case": "nonempty_assembly_destination", "status": "PASS"})
        else:
            raise AssertionError("Nonempty assembly destination accepted")
    print(json.dumps({"status": "PASS", "check": "isolated source-bundle fixtures",
                      "cases": len(RESULTS), "historical_core_verifier_mocked_in_fixtures": True,
                      "kernel_build_run": False, "results": RESULTS}, indent=2))


if __name__ == "__main__":
    main()
