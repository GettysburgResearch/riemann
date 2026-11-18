#!/usr/bin/env python3
"""Record two complete readings of the existing 1895 von Mangoldt edition."""
import argparse
from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ID = "PAPER-H406"
HISTORY = "sources/history_round4/"
PDF = HISTORY + "mangoldt1895_pp255-305.pdf"
EXTRACTION = HISTORY + "mangoldt1895_article_extract_corpus.json"
PIN = "4a75707d429a2ba3c310e0150bfd00d0c79a2c0d8b94df6eb2fd0a8cc071c3e6"
DOI = "10.1515/crll.1895.114.255"
VERSION = "1895 J. reine angew. Math. 114, original German journal print, pp. 255–305"
REVIEWS = [
    f"audits/adversarial_reviews/{name}.md" for name in (
        "analytic167_mangoldt1895_whole_advocate",
        "geometry167_mangoldt1895_whole_skeptic",
    )
]
OUT = "quality/zzzzzzzzzzzzzz_round17_source_scope_updates.jsonl"


def read_rows(path):
    with path.open(encoding="utf-8") as stream:
        return [json.loads(line) for line in stream if line.strip()]


def prepare(root):
    catalog = read_rows(root / "corpus/bibliography.jsonl")
    records = [row for row in catalog if row["id"] == ID]
    if len(records) != 1:
        raise ValueError("Expected one existing PAPER-H406 work")
    record = records[0]
    if (record.get("doi"), record.get("year"), record.get("source_sha256")) != (DOI, 1895, PIN):
        raise ValueError("The existing work points to a different identity or edition")
    if record.get("source_path", record.get("source_file")) != PDF or record["audit_level"] not in (0, 1):
        raise ValueError("The existing source or audit level differs from the expected reading scope")
    registry = read_rows(root / "quality/whole_work_audit_promotions.jsonl")
    if any(row["id"] == ID for row in registry):
        raise ValueError("This reading event must preserve any existing higher audit")

    extract = json.loads((root / EXTRACTION).read_text(encoding="utf-8"))
    data = (root / PDF).read_bytes()
    if (extract.get("article_file"), extract.get("article_sha256"), extract.get("article_bytes"),
        extract.get("printed_pages"), extract.get("source_pdf_pages")) != (
        PDF, PIN, len(data), "255–305", "262–312"
    ) or sha256(data).hexdigest() != PIN:
        raise ValueError("The original article extract does not match the exact source receipt")

    review_hashes = {}
    for review in REVIEWS:
        content = (root / review).read_bytes()
        if PIN not in content.decode("utf-8"):
            raise ValueError(f"Reading lacks the exact source pin: {review}")
        review_hashes[review] = sha256(content).hexdigest()

    return dict(id=ID, evidence=REVIEWS[0], fields=dict(
        version=VERSION, source_path=PDF, source_sha256=PIN, source_bytes=len(data),
        pdf_pages=51, source_locator="Print pp. 255–305; bound-volume PDF pp. 262–312",
        source_extraction_receipt=EXTRACTION, audit_level=1,
        whole_work_read=True, substantive_reading=True,
        independent_whole_reading_reviews=REVIEWS,
        whole_reading_review_sha256=review_hashes,
        read_scope=(
            "Two independent complete readings of the 51 original German printed pages, "
            "covering the inclusive zero count, ordered explicit formula, grouped remainder "
            "and cutoff conventions. The existing scope of the distinct 1894 announcement is unchanged."
        ),
        claim_verification_status=(
            "Complete reading at Level 1. The p. 293 uniformity wording is tracked as an "
            "interpretive scope question; the reviewers document the compact-domain version."
        ),
    ))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write the complete-reading overlay")
    args = parser.parse_args()
    event = json.dumps(prepare(ROOT), ensure_ascii=False, sort_keys=True) + "\n"
    path = ROOT / OUT
    if path.exists() and path.read_text(encoding="utf-8") != event:
        raise ValueError(f"Conflicting overlay already exists: {OUT}")
    if args.apply and not path.exists():
        path.write_text(event, encoding="utf-8")
    print(event, end="")


if __name__ == "__main__":
    main()
