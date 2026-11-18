#!/usr/bin/env python3
"""Verify a sealed Observatory ZIP without reading or changing the live workspace."""

import argparse
from collections import Counter
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import stat
import zipfile
from distribution_policy import is_distributable


PREFIX = "riemann-observatory/"
MANIFEST = "quality/distribution_manifest.json"
REPORTS = (
    "README.md",
    "executive_report.md",
    "quality/coverage_report.md",
    "final_synthesis/comprehensive_report.md",
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def members(archive):
    names = set()
    for member in archive.infolist():
        name = member.filename
        relative = name.removeprefix(PREFIX)
        parts = relative.split("/")
        require(name.startswith(PREFIX) and "\\" not in relative and
                all(part not in {"", ".", ".."} for part in parts), f"Unsafe ZIP path {name}")
        require(not member.is_dir() and not stat.S_ISLNK(member.external_attr >> 16),
                f"Unexpected ZIP member type {name}")
        require(relative not in names, f"Duplicate ZIP member {name}")
        require(is_distributable(relative),
                f"Private input or cache in ZIP {name}")
        names.add(relative)
    return names


def read(archive, path):
    return archive.read(PREFIX + path)


def load(archive, path):
    return json.loads(read(archive, path))


def read_rows(archive, path):
    return [json.loads(line) for line in read(archive, path).decode("utf-8").splitlines() if line.strip()]


def verify_manifest(archive, names):
    manifest = load(archive, MANIFEST)
    records = {row["path"]: row for row in manifest["files"]}
    require(len(records) == len(manifest["files"]), "Duplicate distribution manifest paths")
    require(set(records) == names - {MANIFEST}, "ZIP entry set differs from the manifest")
    require(manifest["included_files"] == len(names), "Incorrect manifest file count")
    for path, row in records.items():
        data = read(archive, path)
        require(len(data) == row["bytes"] and sha256(data) == row["sha256"],
                f"Manifest size or hash mismatch for {path}")
    for path in sorted(names):
        if path.endswith(".jsonl"):
            read_rows(archive, path)


def index(rows, label):
    lookup = {row["id"]: row for row in rows}
    require(len(lookup) == len(rows), f"Duplicate {label} ID")
    return lookup


def verify_provider_counts(archive, names):
    candidates = [row["candidate_id"] for row in read_rows(archive, "corpus/candidates.jsonl")]
    rejected = [row["candidate_id"] for row in read_rows(archive, "corpus/candidates_rejected.jsonl")]
    require(len(candidates) == len(set(candidates)), "Duplicate provider candidate ID")
    require(len(rejected) == len(set(rejected)) and set(rejected).issubset(candidates),
            "Duplicate or unknown lexical rejection")
    curated = [row for path in sorted(names) if re.fullmatch(r"corpus/curated_candidate_decisions[^/]*\.jsonl", path)
               for row in read_rows(archive, path)]
    require(len(curated) == len({row["candidate_id"] for row in curated}), "Duplicate curated candidate ID")
    candidate_ids = set(candidates)
    curated_matches = sum(row["candidate_id"] in candidate_ids for row in curated)
    return {
        "metadata_candidates": len(candidates),
        "metadata_candidates_rejected": len(rejected),
        "metadata_candidates_pending": len(candidates) - len(rejected),
        "curated_candidate_decisions": len(curated),
        "curated_priority_candidates": sum(row["decision"] in {"priority_candidate_verified_metadata", "priority_candidate_reviewed_provider_metadata"} for row in curated),
        "curated_provider_matches": curated_matches,
        "additional_curated_records_unreconciled": len(curated) - curated_matches,
    }


def verify_records(archive, names):
    bibliography = index(read_rows(archive, "corpus/bibliography.jsonl"), "paper")
    claims = index(read_rows(archive, "theorems/theorems.jsonl"), "claim")
    connections = index(read_rows(archive, "connections/connections.jsonl"), "connection")
    groups = index(read_rows(archive, "audits/reviewed_claim_groups.jsonl"), "review group")
    findings = index(read_rows(archive, "audits/findings.jsonl"), "finding")
    graph = read_rows(archive, "graphs/knowledge_graph.jsonl")
    nodes = index([row for row in graph if row["record_type"] == "node"], "graph node")
    edges = [row for row in graph if row["record_type"] == "edge"]
    require(len(graph) == len(nodes) + len(edges), "Unknown graph record type")

    registry = "quality/whole_work_audit_promotions.jsonl"
    promotions = index(read_rows(archive, registry), "audit promotion") if registry in names else {}
    for ident, paper in bibliography.items():
        require(paper["record_path"] in names and paper.get("source_url"), f"Incomplete paper link {ident}")
        level = paper["audit_level"]
        require(level in (0, 1, 2, 3) and paper["whole_work_read"] == (level >= 1),
                f"Reading-level mismatch for {ident}")
        if paper["whole_work_read"]:
            require(paper["access_status"] == "full_text_accessed", f"No full-text access for {ident}")
        if level >= 2:
            entry = promotions.get(ident, {})
            require(entry.get("level") == level and entry.get("evidence") and
                    entry.get("whole_work_coverage_checklist"), f"Missing promotion evidence for {ident}")
            for key in ("version", "source_sha256"):
                if key in entry:
                    require(entry[key] == paper.get(key), f"Promotion {key} mismatch for {ident}")
    for ident, entry in promotions.items():
        require(ident in bibliography and bibliography[ident]["audit_level"] == entry["level"],
                f"Unmatched promotion entry {ident}")
        require(entry.get("evidence") in names and
                len(set(entry.get("independent_reviews", []))) >= 2 and
                all(path in names for path in entry.get("independent_reviews", [])),
                f"Missing archived whole-work review for {ident}")
        require(re.fullmatch(r"[0-9a-f]{64}", entry.get("source_sha256", "")),
                f"Missing exact source hash for {ident}")

    for ident, claim in claims.items():
        paper = claim.get("paper_id")
        require((paper is None or paper in bibliography) and claim.get("locator"), f"Incomplete claim {ident}")
    for edge in edges:
        require(edge["from"] in nodes and edge["to"] in nodes and edge.get("provenance"),
                f"Incomplete graph edge {edge['from']} → {edge['to']}")
    for ident, finding in findings.items():
        if finding.get("verified_author_error"):
            reviews = {json.dumps(row, sort_keys=True) for row in finding.get("independent_reviews", [])}
            require(finding.get("director_adjudication") and finding.get("explicit_witness") and len(reviews) >= 2,
                    f"Incomplete finding evidence for {ident}")

    selected = [p for p in bibliography.values() if p["selection_status"] == "selected_checkpoint_priority_work"]
    levels = dict(Counter(str(p["audit_level"]) for p in selected))
    return {
        "catalogued_works": len(bibliography),
        "deferred_supporting_works": len(bibliography) - len(selected),
        "selected_checkpoint_works": len(selected),
        "fulltexts_accessed_selected": sum(p["access_status"] == "full_text_accessed" for p in selected),
        "selected_primary_excerpt_accessed": sum(p["access_status"] == "primary_source_excerpt_accessed" for p in selected),
        "whole_work_or_translation_read": sum(p["whole_work_read"] for p in selected),
        "whole_work_audit_levels": levels,
        "scoped_level3_claim_groups": sum(g.get("status") == "adjudicated_scoped" for g in groups.values()),
        "theorem_or_exercise_records": len(claims),
        "connection_records": len(connections),
        "graph_nodes": len(nodes),
        "graph_edges": len(edges),
    }


def verify_reports(archive, metrics):
    levels = metrics["whole_work_audit_levels"]
    tables = {
        "Selected source records": str(metrics["selected_checkpoint_works"]),
        "Selected full texts accessed": str(metrics["fulltexts_accessed_selected"]),
        "Selected primary-source excerpts only": str(metrics["selected_primary_excerpt_accessed"]),
        "Complete substantive readings": str(metrics["whole_work_or_translation_read"]),
        "Complete paper-wide Level2/3 audits": f"{levels.get('2', 0)} / {levels.get('3', 0)}",
        "Scoped independently adjudicated claim groups": str(metrics["scoped_level3_claim_groups"]),
        "Theorem/conjecture/exercise records": str(metrics["theorem_or_exercise_records"]),
        "Connection records": str(metrics["connection_records"]),
        "Graph nodes / edges": f"{metrics['graph_nodes']} / {metrics['graph_edges']}",
    }
    for path in REPORTS:
        lines = read(archive, path).decode("utf-8").splitlines()
        for label, expected in tables.items():
            values = [cells[2].strip().replace(",", "") for line in lines if line.startswith("|")
                      if len(cells := line.split("|")) == 4 and cells[1].strip() == label]
            require(values and values[0] == expected, f"Stale {label} in {path}")
    if levels.get("2", 0) or levels.get("3", 0):
        for path in ("quality/limitations.md", "quality/evidence_audit.md"):
            prose = read(archive, path).decode("utf-8")
            require(not re.search(r"whole.paper\s+level\s*2\s*/\s*3 counts remain zero", prose, re.I),
                    f"Stale zero audit count in {path}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("zip_path", type=Path)
    parser.add_argument("--sha256", required=True, help="Expected sealed ZIP hash from the release receipt")
    parser.add_argument("--checkpoint", required=True, help="Checkpoint suffix, for example 7 or 5a")
    parser.add_argument("--bytes", type=int, help="Expected byte count from the release receipt")
    parser.add_argument("--pdf", type=Path, help="Standalone synthesis PDF to compare byte for byte")
    parser.add_argument("--html", type=Path, help="Standalone synthesis HTML to compare byte for byte")
    parser.add_argument("--code-pin", action="append", default=[], metavar="RESULT=SOURCE",
                        help="Verify a result JSON's code_sha256 against the exact archived source")
    args = parser.parse_args()
    try:
        require(re.fullmatch(r"[1-9][0-9]*[a-z]?", args.checkpoint), "Invalid checkpoint suffix")
        blob = args.zip_path.read_bytes()
        digest = sha256(blob)
        require(digest == args.sha256.lower(), f"ZIP SHA-256 mismatch, actual {digest}")
        require(args.bytes is None or args.bytes == len(blob), "ZIP size differs from the release receipt")
        with zipfile.ZipFile(io.BytesIO(blob)) as archive:
            names = members(archive)
            verify_manifest(archive, names)
            actual = verify_provider_counts(archive, names) | verify_records(archive, names)
            current = load(archive, "quality/metrics.json")
            frozen = load(archive, f"quality/checkpoints/checkpoint{args.checkpoint}_metrics.json")
            require(all(frozen.get(key) == value for key, value in current.items()), "Live and frozen metrics differ")
            for key, value in actual.items():
                require(current.get(key) == value, f"Stale {key}, derived {value}")
            verify_reports(archive, actual)
            require(load(archive, "quality/validation.json")["validation"] == "PASS", "No passing structural receipt")
            for option in args.code_pin:
                result, separator, code = option.partition("=")
                require(separator and result in names and code in names, f"Invalid archived code pin {option}")
                pin = load(archive, result)
                source_digest = pin.get("code_sha256", pin.get("source_code_sha256"))
                require(source_digest == sha256(read(archive, code)),
                        f"Result code hash mismatch for {result}")
            pdf = read(archive, "final_synthesis/synthesis.pdf")
            html = read(archive, "final_synthesis/synthesis.html")
            require(pdf.startswith(b"%PDF-") and html.lstrip().startswith(b"<!doctype html>"),
                    "Missing or malformed rendered synthesis")
            require(args.pdf is None or args.pdf.read_bytes() == pdf, "Standalone PDF differs from ZIP")
            require(args.html is None or args.html.read_bytes() == html, "Standalone HTML differs from ZIP")
        print(json.dumps({"validation": "PASS", "checkpoint": args.checkpoint, "zip_bytes": len(blob),
                          "zip_sha256": digest, "manifest_payloads": len(names) - 1, "metrics": actual}, indent=2))
    except (OSError, ValueError, TypeError, KeyError, zipfile.BadZipFile) as exc:
        parser.exit(1, f"Sealed checkpoint validation failed: {exc}\n")


if __name__ == "__main__":
    main()
