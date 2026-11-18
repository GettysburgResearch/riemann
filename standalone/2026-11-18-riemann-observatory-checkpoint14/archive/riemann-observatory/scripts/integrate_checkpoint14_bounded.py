#!/usr/bin/env python3
"""Stage the director-adjudicated R17 bounded common-sequence supplement."""
import json
from pathlib import Path
from tempfile import NamedTemporaryFile

from integrate_research_round17 import COMMON, GROUP_LEDGER, CONNECTION_UPDATES
from integrate_research_round17 import SCOPED, SEQUENCE, claim, proof, read


ROOT = Path(__file__).resolve().parents[1]
REVIEWS = "audits/adversarial_reviews/"
DIRECTOR = REVIEWS + "director_bounded_common_checkpoint14.md"
PRIME = REVIEWS + "prime172_bounded_common_countermodel.md"
ANALYTIC = REVIEWS + "analytic172_bounded_common_skeptic.md"
FRESH = REVIEWS + "checkpoint14_bounded_math_final_review.md"
REAL = "OBS-CSTAR-BOUNDED-COMMON-REAL-SEQUENCE-NORM-COUNTERMODEL"
INTEGER = "OBS-CSTAR-BOUNDED-COMMON-INTEGER-SEQUENCE-NORM-COUNTERMODEL"
SECOND_DERIVATIVE = "EXT-VAN-DER-CORPUT-SECOND-DERIVATIVE"
GROUP = "REVIEW-GROUP-R17-BOUNDED-COMMON-SEQUENCE-PHASE"
CONNECTION = "CONN-CSTAR-COMMON-SEQUENCE-NORM-OBSTRUCTION"
CLAIM_SHARD = "theorems/checkpoint14_bounded_claims.jsonl"
PROOF_SHARD = "theorems/checkpoint14_bounded_proof_edges.jsonl"
ORIGINAL_CONNECTIONS = "connections/research_round17_connections.jsonl"

HYPOTHESES = (
    "Fix 1/2<θ<2/3, K≍T^θ, integer P≍KT and J=[P,2P)∩ℤ. "
    "Take the primes in [X,(1+η)X] with X=K^(1/4) and fixed 0<η<2^(1/4)−1. "
    "Its full fourth-power support S⊂[K,2K) includes repeated factors, with "
    "|S|≍K/log⁴K and multinomial coefficients 1≤c_k≤24. "
    "The residue rows arise from one sequence and agree on marginals modulo common divisors. On units, the induced mean at each modulus is "
    "the total sequence mass on that modulus’s units divided by φ(k). "
    "This ordinary integer-interval setting leaves the prime-model P/φ(k) baseline, "
    "prime or sieve support, and the smooth C_* sum open."
)
DISCREPANCY = (
    "The pooled squared discrepancy of the residue rows from P/k over k≤2K is O(PK), "
    "and the sum of the maximum absolute row discrepancies is O(K√P). "
    "On units the same orders hold about their induced means. The maximum-error budget is O_A(P/log^A T) for every fixed A."
)
PROJECTION = (
    "The unit-centered real projection against W(n)=Σ_(k∈S)(c_k/k)·1_((n,k)=1)·"
    "(cos(2πn/k)−μ(k)/φ(k)) is ≫|S|√T, exceeding T log⁴T by a divergent factor."
)
CLAIMS = [
    claim(REAL, DIRECTOR, "Bounded construction and progression budgets",
          "bounded_common_real_sequence_norm_countermodel",
          "One real sequence supported on J has exact mass P and takes values in [1/2,3/2] on J. "
          + DISCREPANCY + " " + PROJECTION, HYPOTHESES),
    claim(INTEGER, DIRECTOR, "Cap-preserving integerization",
          "bounded_common_integer_sequence_norm_countermodel",
          "One sequence supported on J takes values in {0,1,2} and has exact mass P. "
          + DISCREPANCY + " " + PROJECTION, HYPOTHESES),
]
PROOFS = [
    proof(REAL, SECOND_DERIVATIVE, DIRECTOR,
          "Graham and Kolesnik, Van der Corput’s Method of Exponential Sums, Theorem 2.2, p. 8. "
          "For real C² f on an interval of length N with λ≤|f″|≤Aλ and λ>0, the sum of "
          "e(f(l)) over the integers in the interval is O(AN√λ+λ^(−1/2)), up to O(1) "
          "for endpoint conventions. In the application f(l)=n/l and λ≍T/K². "
          "https://assets.cambridge.org/97805213/39278/excerpt/9780521339278_excerpt.pdf",
          "uses_second_derivative_bound_for_uniform_real_cap"),
    proof(REAL, SEQUENCE, DIRECTOR, PRIME + " · Bounded real sequence",
          "reuses_full_support_and_progression_parseval_estimates"),
    proof(INTEGER, REAL, DIRECTOR, PRIME + " · Integer sequence and exact mass",
          "uses_independent_rounding_and_single_unit_mass_correction"),
]


def replace_rows(path, rows):
    target = ROOT / path
    with NamedTemporaryFile(mode="w", encoding="utf-8", dir=target.parent, delete=False) as stream:
        temp = Path(stream.name)
        try:
            for row in rows:
                stream.write(json.dumps(row, ensure_ascii=False) + "\n")
            stream.close()
            temp.chmod(target.stat().st_mode if target.exists() else 0o644)
            temp.replace(target)
        finally:
            temp.unlink(missing_ok=True)


def main():
    required = [DIRECTOR, PRIME, ANALYTIC, FRESH, COMMON, GROUP_LEDGER,
                CONNECTION_UPDATES, ORIGINAL_CONNECTIONS, "theorems/research_round17_claims.jsonl"]
    for path in required:
        if not (ROOT / path).is_file():
            raise FileNotFoundError(path)

    claim_ids = {row["id"] for row in CLAIMS}
    earlier_claims = {row["id"] for row in read("theorems/research_round17_claims.jsonl")}
    if len(claim_ids) != len(CLAIMS) or claim_ids & earlier_claims or SEQUENCE not in earlier_claims:
        raise ValueError("Duplicate bounded claims or missing Round 17 prerequisite")

    group = dict(id=GROUP, title="Uniformly bounded common real and integer sequence phase countermodels",
                 status=SCOPED, director_adjudication=DIRECTOR,
                 independent_reviews=[ANALYTIC, FRESH])
    groups = {row["id"]: row for row in read(GROUP_LEDGER)}
    groups[GROUP] = group

    connection = next(row for row in read(ORIGINAL_CONNECTIONS) if row["id"] == CONNECTION)
    updates = {row["id"]: row for row in read(CONNECTION_UPDATES)}
    fields = dict(updates.get(CONNECTION, {}).get("fields", {}))
    source_claims = [
        row for row in fields.get("source_claims", connection["source_claims"])
        if row["id"] not in claim_ids
    ]
    source_claims += [{"id": row["id"], "locator": row["locator"]} for row in CLAIMS]
    fields.update(
        source_claims=source_claims,
        source_theorems=list(dict.fromkeys(row["id"] for row in source_claims)),
        statement=("Common-sequence consistency, exact mass and uniform pointwise caps allow "
                   "the large h=1 phase projection under P/k and induced-unit-mean discrepancy budgets."),
        already_proved=(connection["already_proved"] + " The bounded versions have real weights in "
                        "[1/2,3/2] or integer weights in {0,1,2} on J. " + PROJECTION),
        tests=(connection["tests"] + " The bounded versions use the second-derivative estimate for "
               "the full modulus shell, the positive selected-frequency diagonal, and bounded rounding "
               "with a single-unit mass correction."),
    )
    updates[CONNECTION] = dict(id=CONNECTION, evidence=DIRECTOR, fields=fields)
    outputs = {
        CLAIM_SHARD: CLAIMS,
        PROOF_SHARD: PROOFS,
        GROUP_LEDGER: list(groups.values()),
        CONNECTION_UPDATES: list(updates.values()),
    }
    for path, rows in outputs.items():
        replace_rows(path, rows)
    print(json.dumps(dict(claims=len(CLAIMS), proof_edges=len(PROOFS),
                          scoped_group=GROUP, connection_overlay=CONNECTION), indent=2))


if __name__ == "__main__":
    main()
