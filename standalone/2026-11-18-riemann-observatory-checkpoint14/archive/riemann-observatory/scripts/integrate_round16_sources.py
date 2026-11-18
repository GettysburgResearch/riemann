#!/usr/bin/env python3
"""Admit the pinned Luecking journal article and record two complete readings."""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
ID = "PAPER-LUECKING1986-BERGMAN-MULTIPLIERS"
TITLE = "Multipliers of Bergman spaces into Lebesgue spaces"
DOI = "10.1017/S001309150001748X"
URL = f"https://doi.org/{DOI}"
VERSION = "1986 Cambridge journal version, Proceedings of the Edinburgh Mathematical Society 29(1), 125–131"
SOURCE = "sources/prime146_mellin_provenance/luecking1986.pdf"
PIN = "e5d194ad05a844e376a65b18bc7082864baa38b01ddb1d4f217f67c28cb0d301"
BYTES = 298914
REVIEWS = [
    "audits/adversarial_reviews/prime150_luecking_whole_advocate.md",
    "audits/adversarial_reviews/analytic150_luecking_whole_skeptic.md",
]
TRACK = "papers/round16_dependency_records.jsonl"
OVERLAY = "quality/zzzzzzzzzzzz_round16_source_scope_updates.jsonl"
NOTE = f"papers/{ID}.md"
RECEIPT = "quality/round16_dependency_admission_receipt.json"
RESULT = (
    "For 0<q<p<∞ and a positive finite Borel measure on the unit disk, the "
    "embedding A^p→L^q(μ) is bounded exactly when the fixed-radius pseudohyperbolic "
    "disk mass divided by its normalized area lies in L^{p/(p−q)}."
)
SCOPE = (
    "Two independent complete readings of the pinned seven-page journal article, "
    "pp. 125–131. Coverage includes the main criterion, radius independence, "
    "necessity via uniform interpolation, and the multiplier consequence."
)
REASON = (
    "Adjacent Bergman-space antecedent for the ambient weighted Mellin trace "
    "criterion. The strip transfer uses further inputs. The article supplies "
    "neither a physically constrained counterexample nor a signed endpoint result."
)


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def normalize(value):
    return re.sub(r"[^a-z0-9]", "", str(value).casefold())


def encode(record):
    return json.dumps(record, ensure_ascii=False, sort_keys=True)


def prepare(root):
    source = root / SOURCE
    if source.stat().st_size != BYTES or digest(source) != PIN:
        raise ValueError("Journal PDF fails the pinned size or SHA-256 check")
    reviews = {}
    for path in REVIEWS:
        review = root / path
        if PIN not in review.read_text(encoding="utf-8"):
            raise ValueError(f"Reading does not identify the exact journal copy: {path}")
        reviews[path] = digest(review)

    sources = [root / "corpus/bibliography.jsonl", *sorted((root / "papers").glob("*records.jsonl"))]
    for path in sources:
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            if not any((
                row.get("id") == ID,
                normalize(row.get("doi", "")).endswith(normalize(DOI)),
                normalize(row.get("title", "")) == normalize(TITLE),
            )):
                continue
            if row.get("id") == ID and row.get("source_sha256") == PIN and (
                path == root / TRACK or path == root / "corpus/bibliography.jsonl"
            ):
                continue
            raise ValueError(f"Existing work identity in {path}: {row.get('id')}")

    record = dict(
        id=ID, paper_id=ID, title=TITLE, authors=["Daniel H. Luecking"], year=1986,
        venue="Proceedings of the Edinburgh Mathematical Society", volume="29", issue="1",
        pages="125–131", doi=DOI, canonical_url=URL, source_url=URL,
        publication_status="Published journal article", version=VERSION,
        family=["H"], area="Bergman spaces", audit_level=0,
        full_text_accessed=True, access_status="full_text_accessed", pdf_pages=7,
        source_path=SOURCE, source_sha256=PIN, source_bytes=BYTES,
        bibliography_verified=True, selected=True, whole_work_read=False,
        substantive_reading=False, novelty_claim=False, main_result=RESULT,
        selection_reason=REASON, selection_status="selected_scoped_dependency",
        source_locator="p. 126 main criterion, p. 127 radius lemma, pp. 127–130 necessity, and pp. 130–131 multipliers",
        read_scope="Exact journal copy authenticated at admission. Complete readings are recorded in the separate scope overlay.",
        record_path=NOTE, selection_review=REVIEWS[0], admission_receipt=RECEIPT,
    )
    overlay = dict(id=ID, evidence=REVIEWS[0], fields=dict(
        audit_level=1, whole_work_read=True, substantive_reading=True,
        independent_whole_reading_reviews=REVIEWS, read_scope=SCOPE,
        claim_verification_status="Complete reading at Level 1.",
    ))
    receipt = dict(
        paper_id=ID, doi=DOI, exact_version=VERSION, pdf_pages=7,
        source=dict(path=SOURCE, bytes=BYTES, sha256=PIN),
        reading_review_sha256=reviews, admission_audit_level=0, resulting_audit_level=1,
        family=["H"], record=TRACK, scope_overlay=OVERLAY, identity_check="DOI and normalized title",
    )
    links = "\n".join(f"- [{Path(path).stem}](../{path})" for path in REVIEWS)
    note = f"""# {TITLE}

Daniel H. Luecking. {VERSION}. [Publisher]({URL})

{RESULT}

{REASON}

{SCOPE} Level 1.

{links}
"""
    return {TRACK: encode(record) + "\n", OVERLAY: encode(overlay) + "\n",
            NOTE: note, RECEIPT: json.dumps(receipt, ensure_ascii=False, indent=2) + "\n"}


RIEMANN_ID = "PAPER-S001"
HISTORY = "sources/history_round4/"
AUDITS = "audits/adversarial_reviews/"
RIEMANN_DIRECTOR = AUDITS + "director_riemann1859_whole_round16.md"
RIEMANN_REVIEWS = [AUDITS + name for name in (
    "analytic144_riemann1859_whole_advocate.md",
    "geometry144_riemann1859_whole_skeptic.md",
)]
RIEMANN_SOURCES = {
    "first_print": (HISTORY + "riemann1859_original.djvu",
                    "9e2b9cd404dd8d054689607ef4b7c49734fd0d6648a272244451f6ae9a5f9b4c"),
    "english_translation": ("sources/spectral/riemann.pdf",
                            "6b24341e3406d165baeb7ab1e00cfa0a544d0399e2b33175dfa71480bdddd24f"),
    "collected_edition": (HISTORY + "riemann1892_collected.pdf",
                          "55f149d350e4541d0c536222b4a26d74ce5f751a2f0ef97c3b8d3559894de358"),
    "genocchi_extract": ("sources/riemann_constant_skeptic_round4/genocchi1860_pp52-59.pdf",
                          "60c40a680b855cf36b17a588b94e70692d019416ce05654d895a82f149b5a35c"),
}
RIEMANN_REGISTRY = "quality/whole_work_audit_promotions.jsonl"
RIEMANN_OVERLAY = "quality/zzzzzzzzzzzzz_round16_riemann_source_scope_updates.jsonl"


def prepare_riemann(root, final_review=None):
    supplementary = {}
    for label, (path, pin) in RIEMANN_SOURCES.items():
        if digest(root / path) != pin:
            raise ValueError(f"Incorrect source hash: {path}")
        supplementary[label] = dict(path=path, sha256=pin, bytes=(root / path).stat().st_size)

    notes = [RIEMANN_DIRECTOR, *RIEMANN_REVIEWS, AUDITS + "geometry151_riemann_whole_third_adjudication.md"]
    for note in notes:
        (root / note).read_text(encoding="utf-8")
    if final_review:
        review_path = Path(final_review)
        if review_path.parent != Path(AUDITS) or not review_path.name.startswith("geometry157_"):
            raise ValueError("Expected the independent Geometry157 final QA note")
        if not (root / review_path).read_text(encoding="utf-8").strip():
            raise ValueError("The final QA note is empty")

    with (root / "corpus/bibliography.jsonl").open(encoding="utf-8") as stream:
        rows = [json.loads(line) for line in stream]
    work = [row for row in rows if row["id"] == RIEMANN_ID]
    if len(work) != 1 or not work[0]["whole_work_read"] or not work[0]["source_manifestation_overlays"]:
        raise ValueError("Expected the existing complete Riemann reading and manifestation history")

    path, pin = RIEMANN_SOURCES["first_print"]
    version = "November 1859 Academy first print, original German, pp. 671–680"
    promotion = dict(
        id=RIEMANN_ID, level=3, version=version, source_sha256=pin,
        evidence=RIEMANN_DIRECTOR, independent_reviews=RIEMANN_REVIEWS,
        third_adjudication=notes[-1], final_release_qa=final_review,
        whole_work_coverage_checklist=[
            "All ten first-print pages and the complete nine-page Wilkins translation, with original controlling discrepancies.",
            "Euler product and gamma-Hankel continuation, theta transformation, functional equation and completed even Xi.",
            "Zero-count forecast, later counting estimates and finite-order product repair.",
            "Mellin and midpoint inversion, inverse kernels, known correction of the additive constant and later ordered explicit formula.",
            "Finite Möbius inversion, historical numerical observations and explicitly conjectural RH.",
        ],
        external_inputs=(
            "Modern finite-order Hadamard factorization, argument control for zero counting, "
            "midpoint inversion for bounded variation, and von Mangoldt’s ordered explicit formula. "
            "The cited later results repair identified original proof gaps."
        ),
    )
    update = dict(id=RIEMANN_ID, evidence=RIEMANN_DIRECTOR, fields=dict(
        source_path=path, source_sha256=pin, source_bytes=supplementary["first_print"]["bytes"],
        source_url="https://upload.wikimedia.org/wikipedia/commons/d/d2/RiemannPrim1859.djvu",
        version=version, audit_level=3, substantive_reading=True, whole_work_read=True,
        independent_whole_reading_reviews=RIEMANN_REVIEWS,
        source_manifest=HISTORY + "source_manifest.json",
        historical_audit_source_pins=supplementary,
        read_scope=(
            "Whole first-print historical proof audit, pp. 671–680. The nine-page Wilkins translation "
            "was read in parallel. Selected 1892 collected-edition and Genocchi passages corroborate "
            "historical repairs. Original proof gaps and later proofs are separately identified."
        ),
        claim_verification_status=(
            "Historical proof audit at Level 3. Later results supply specified missing steps. "
            "The universal reality of the zeros remains conjectural. No new error finding was added."
        ),
    ))
    old_registry = (root / RIEMANN_REGISTRY).read_text(encoding="utf-8")
    registered = [json.loads(line) for line in old_registry.splitlines() if line.strip()]
    if len({row["id"] for row in registered if row["id"] != RIEMANN_ID}) != 8:
        raise ValueError("Expected eight distinct prior whole-work promotions")
    if any(row["id"] == RIEMANN_ID for row in registered):
        if registered[-1] != promotion or len(registered) != 9:
            raise ValueError("Conflicting Riemann promotion already present")
        new_registry = old_registry
    else:
        if len(registered) != 8:
            raise ValueError("Unexpected whole-work registry entries")
        separator = "" if old_registry.endswith("\n") else "\n"
        new_registry = old_registry + separator + encode(promotion) + "\n"
    return {RIEMANN_OVERLAY: encode(update) + "\n", RIEMANN_REGISTRY: new_registry}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write the four prepared source records")
    parser.add_argument("--riemann", action="store_true", help="include the first-print historical audit")
    parser.add_argument("--final-review", help="path to the passing Geometry157 final review")
    args = parser.parse_args()
    if args.riemann and args.apply and not args.final_review:
        parser.error("Applying the Riemann promotion requires passing Geometry157 final QA")
    if args.final_review and not args.riemann:
        parser.error("--final-review requires --riemann")
    outputs = prepare(ROOT)
    if args.riemann:
        outputs.update(prepare_riemann(ROOT, args.final_review))
    for name, content in outputs.items():
        path = ROOT / name
        if name != RIEMANN_REGISTRY and path.exists() and path.read_text(encoding="utf-8") != content:
            raise ValueError(f"Refusing to overwrite different evidence: {name}")
    if args.apply:
        for name, content in outputs.items():
            path = ROOT / name
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                path.write_text(content, encoding="utf-8")
    print(f"{'Wrote' if args.apply else 'Prepared'} {ID} at Level 1")
    print("\n".join(outputs))


if __name__ == "__main__":
    main()
