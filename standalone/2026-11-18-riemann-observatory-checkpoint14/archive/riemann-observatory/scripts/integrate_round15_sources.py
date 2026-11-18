#!/usr/bin/env python3
"""Stage the pinned Gonek adjudication and two complete-reading events."""
from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDITS = "audits/adversarial_reviews/"
GONEK = AUDITS + "director_gonek_whole_round15.md"
GONEK_ID = "PAPER-LF63-GONEK1984"
GONEK_VERSION = "1984 journal typeset scan, Inventiones Mathematicae 75(1), 123–141"
GONEK_PDF = "sources/classical63_lfunctions/gonek1984.pdf"
GONEK_SHA = "dfdd2444a2f62f1947c897e87101080225714dbf1f21db8ca19096d2a6e80fc3"
GONEK_REVIEWS = [AUDITS + name for name in (
    "geometry88_gonek_whole_advocate.md", "prime88_gonek_whole_skeptic.md",
)]
LOCAL_REVIEWS = [*GONEK_REVIEWS, AUDITS + "weighted89_gonek_local_adjudication_input.md"]
MORSE_ID = "PAPER-LAG2009-MORSE"
MORSE_PDF = "sources/prefix_skeptic62_spectral/lagarias_morse.pdf"
MORSE_SHA = "307d253d70abc7d8ef3d24355e9ab7708010bda18c7b9060a4913033c6e224be"
MORSE_REVIEWS = [AUDITS + name for name in (
    "geometry120_lagarias_morse_whole_advocate.md", "analytic120_lagarias_morse_whole_skeptic.md",
)]
COMPLEMENTS_ID = "PAPER-L002"
COMPLEMENTS_PDF = "sources/uniform121_bombieri_lagarias/bombieri_lagarias_author.pdf"
COMPLEMENTS_SHA = "cd13c8560f961c68e21256e5ba107bdd08fa7f34ce1e2cffbd4b63a16e8d48e0"
COMPLEMENTS_ADJUDICATION = AUDITS + "director_mellin_explicit_formula_round15.md"
COMPLEMENTS_REVIEWS = [AUDITS + name for name in (
    "uniform121_bombieri_lagarias_whole_advocate.md", "weighted121_bombieri_lagarias_whole_skeptic.md",
)]
INUMARU_ID = "PAPER-P122-INUMARU-SUGIYAMA-TWISTED-DENSITY"
INUMARU_EVENT = "quality/pending_round15/geometry132_inumaru_reading_event.jsonl"
INUMARU_EVENT_SHA = "4a81f5252cc675d5305698cb2e16db38c1e7c597938c2593234a0a5ed9f122aa"
ADMISSION = "quality/round15_dependency_admission_receipt.json"


def rows(path):
    return [json.loads(line) for line in (ROOT / path).read_text().splitlines() if line.strip()]


def write(path, values):
    (ROOT / path).write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in values))


def finding(ident, title, locator, witness, scope):
    return dict(id=ident, title=title, classification="Verified mathematical error",
                status="adjudicated_exact_journal_counterexample_and_repair", sources=[GONEK_ID],
                evidence=GONEK, director_adjudication=GONEK, independent_reviews=LOCAL_REVIEWS,
                verified_author_error=True, version=GONEK_VERSION, source_sha256=GONEK_SHA,
                source_locator=locator, explicit_witness=witness, scope=scope)


PROMOTION = dict(id=GONEK_ID, level=3, version=GONEK_VERSION, source_sha256=GONEK_SHA,
                 evidence=GONEK, independent_reviews=GONEK_REVIEWS,
                 whole_work_coverage_checklist=[
                     "All nineteen published pages 123–141, exact scan and author-copy comparison, title, reception history and references.",
                     "Unconditional shifted (4), fixed derivative orders and full real shift window, kernel beta integral, conjugate reflected edge and RH Corollaries 1–2.",
                     "Contour, pole exclusion, good heights, multiplicity and arbitrary cutoff transfer; Lemmas 1–5 and endpoint saddle checks.",
                     "Lemmas 6–10, differentiated gamma factors, log weights, ordinary PNT convolution, main coefficients and error budgets.",
                     "Three independently witnessed display repairs, bulk interval coverage for Corollary 3 and exact gap integral enclosure.",
                     "Derivative-prefix and strict weighted tail consequences, with scope and effective-constant limitations.",
                 ],
                 external_inputs="Functional equation, Stirling and fixed derivatives, classical convexity, local zero count and logarithmic derivative, effective ordinary PNT and cited oscillatory estimates. The audit does not extend to every cited edition or all upstream proofs.")

SOURCE_UPDATES = [
    dict(id=GONEK_ID, evidence=GONEK,
         fields=dict(version=GONEK_VERSION, source_path=GONEK_PDF, source_sha256=GONEK_SHA,
                     audit_level=3, whole_work_read=True, substantive_reading=True,
                     independent_whole_reading_reviews=GONEK_REVIEWS,
                     claim_verification_status="Exact journal whole-work Level 3. Main theorem and all three corollaries survive; three local printed displays have narrow witnessed repairs.",
                     read_scope="Complete pinned journal, pp. 123–141, independently reconstructed by two reviewers and the director. The unconditional shifted theorem, RH corollaries and derivative prefix retain their hypotheses. The bulk-coverage repair is documented separately.",
                     correction_history="Current Rochester author-linked scan is byte-identical; Springer PDF route supplied subscription HTML. Bounded publisher, author and Crossref search found no separately indexed corrigendum.",
                     correction_history_evidence=AUDITS + "release123_gonek_version_history.md")),
    dict(id=MORSE_ID, evidence=MORSE_REVIEWS[0],
         fields=dict(version="arXiv:0712.3238v6, posted 18 August 2009, manuscript dated 10 August 2009",
                     source_url="https://arxiv.org/pdf/0712.3238v6", source_path=MORSE_PDF, source_sha256=MORSE_SHA, pdf_pages=33,
                     audit_level=1, whole_work_read=True, substantive_reading=True,
                     independent_whole_reading_reviews=MORSE_REVIEWS,
                     read_scope="Two independent complete readings of all 33 v6 pages, both appendices and references. Selected journal passages were separately compared; the complete reading is pinned to v6.",
                     claim_verification_status="Complete reading at Level 1. The scoped spectral constructions and their local printed qualifications await director adjudication.")),
    dict(id=COMPLEMENTS_ID, evidence=COMPLEMENTS_ADJUDICATION,
         fields=dict(version="Michigan author-hosted 12-page manuscript, version date unverified",
                     source_url="https://websites.umich.edu/~lagarias/doc/bombieri.pdf",
                     source_path=COMPLEMENTS_PDF, source_sha256=COMPLEMENTS_SHA, pdf_pages=12,
                     audit_level=1, whole_work_read=True, substantive_reading=True,
                     independent_whole_reading_reviews=COMPLEMENTS_REVIEWS,
                     read_scope="Two independent readings of all 12 rendered author-manuscript pages, sections, footnotes and references. The separately paginated 14-page publisher version was bibliographically matched; its PDF bytes were unavailable.",
                     audit_scope="Scoped director adjudication of the author-manuscript pp. 5–6 explicit-formula test class and p. 8 finite equation (3.5). The smooth countermodel defeats the asserted raw height limit on the broad printed class. A positive finite correction restores (3.5); it vanishes in the main theorem's limit.",
                     claim_verification_status="Complete author-manuscript reading at Level 1. Scoped countermodel and finite-cutoff repair adjudicated; compact tests and the multiset criterion survive. The source assessment is pinned to this manuscript.")),
]

FINDINGS = [
    finding("FIND-R15-GONEK-P123-CONTINUOUS-DERIVATIVE-SIGN",
            "Continuous derivative-product comparison has the wrong sign at odd total order",
            "Pinned journal p. 123, introductory equation (2) and the derivative convention immediately below.",
            "With mu=1, nu=0, differentiating the functional equation on the line gives 2 Re[zeta′(s)zeta(1−s)]=(chi′/chi)(s)|zeta(s)|². The logarithmic derivative is −log(t/(2pi))+O(1/t); the ordinary second moment and partial summation give a negative leading term −T log²T/2, while (2) prints a positive term.",
            "Contextual display in this journal edition. Insert (−1)^(mu+nu). The discrete source theorem (4) already has the sign. No finding is attributed to Ingham’s primary work."),
    finding("FIND-R15-GONEK-P129-INNER-PHASE",
            "Printed auxiliary saddle phase fails its stated double-zero identity",
            "Pinned journal p. 129, proof of Lemma 1, immediately after extracting exp(−ir).",
            "Direct substitution into f(x)=(1+x)log(1+x)−(1+x) gives f(0)=−1. The expansion with the extracted constant requires F=f+1, for which F(0)=F′(0)=0 and F′′(0)=1.",
            "Auxiliary phase definition in the proof. The corrected signed square root gives the stated stationary-phase lemma and leaves (4) and its corollaries intact."),
    finding("FIND-R15-GONEK-P140-RECIPROCAL-GAP-SCALE",
            "Gap proof displays the reciprocal of the defined normalization",
            "Pinned journal p. 125, definition of lambda; p. 140 §6 opening display.",
            "The proof prints a factor 2pi/log gamma_n, whose gap limsup is zero by bounded gaps from the zero count. The defined factor log gamma_n/(2pi) has limsup at least one by mean density. The displayed quantities cannot agree.",
            "Restore the p. 125 factor for the gap proof. The separate bulk-interval covering repair justifies Corollary 3 and carries no verified-author-error flag. The p. 125 statement and the derivative prefix survive."),
]


def inumaru_update():
    if sha256((ROOT / INUMARU_EVENT).read_bytes()).hexdigest() != INUMARU_EVENT_SHA:
        raise ValueError("Inumaru complete-reading event differs from its pin")
    event, = rows(INUMARU_EVENT)
    fields = event["fields"]
    if event["id"] != INUMARU_ID or fields["audit_level"] != 1 or not fields["whole_work_read"]:
        raise ValueError("Unexpected Inumaru event identity or scope")
    return dict(id=INUMARU_ID, evidence=event["evidence"],
                fields={**fields, "independent_whole_reading_reviews": event["independent_full_readings"],
                        "claim_verification_status": "Complete pinned v1 reading at Level 1. The source's continuous fixed-character statistic is a comparator; no discrete long-prime estimate or whole-work Level 2/3 adjudication is claimed."})


def main():
    records = {row["id"]: row for row in rows("corpus/bibliography.jsonl")}
    admission = json.loads((ROOT / ADMISSION).read_text())
    shard = admission["admitted_shard"]
    if sha256((ROOT / shard).read_bytes()).hexdigest() != admission["admitted_shard_sha256"]:
        raise ValueError(f"Mismatched newly admitted source shard: {shard}")
    admitted = {row["id"]: row for row in rows(shard)}
    if set(admitted) != set(admission["ids"]) or INUMARU_ID not in admitted:
        raise ValueError("Unexpected new-source admission identities")
    for ident, record in admitted.items():
        if ident in records and records[ident].get("source_sha256") != record["source_sha256"]:
            raise ValueError(f"Conflicting admitted source edition: {ident}")
        records.setdefault(ident, record)
    updates = [*SOURCE_UPDATES, inumaru_update()]
    for event in updates:
        record = records[event["id"]]
        fields = event["fields"]
        source = ROOT / fields["source_path"]
        if record.get("source_sha256") != fields["source_sha256"]:
            raise ValueError(f"Conflicting registered edition: {event['id']}")
        if source.is_file() and sha256(source.read_bytes()).hexdigest() != fields["source_sha256"]:
            raise ValueError(f"Mismatched exact edition: {source}")
        for note in [event["evidence"], *fields["independent_whole_reading_reviews"]]:
            if not (ROOT / note).is_file():
                raise FileNotFoundError(note)
    audit_registry = "quality/whole_work_audit_promotions.jsonl"
    by_id = {row["id"]: row for row in rows(audit_registry)}
    for event in updates[1:]:
        if event["id"] in by_id:
            raise ValueError(f"Complete-reading event would supersede a whole-work audit: {event['id']}")
    by_id[GONEK_ID] = PROMOTION
    write("quality/zzzzzzzzzzz_round15_source_scope_updates.jsonl", updates)
    write("audits/research_round15_gonek_findings.jsonl", FINDINGS)
    write(audit_registry, by_id.values())
    print(json.dumps(dict(whole_work_promotion=GONEK_ID, complete_reading_events=[event["id"] for event in updates[1:]],
                          verified_local_displays=[row["id"] for row in FINDINGS])))


if __name__ == "__main__":
    main()
