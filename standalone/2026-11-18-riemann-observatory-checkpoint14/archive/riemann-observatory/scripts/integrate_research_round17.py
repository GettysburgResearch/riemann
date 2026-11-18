#!/usr/bin/env python3
"""Stage scoped Round 17 research records from director adjudications."""
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REVIEWS = "audits/adversarial_reviews/"
MELLIN = REVIEWS + "director_negative_mellin_round17.md"
COMMON = REVIEWS + "director_common_sequence_round17.md"
GROUP_LEDGER = "audits/reviewed_claim_groups.jsonl"
CONNECTION_UPDATES = "quality/connection_status_updates.jsonl"
SCOPED = "adjudicated_scoped"

CRITICAL = "THM-MELLIN-CRITICAL-STRIP-SYMMETRIC-EXPLICIT-FORMULA"
LITERAL = "LEM-BL-LITERAL-TEST-CLASS-LOCAL-MELLIN-H1"
TITCH = "EXT-TITCH-1986-9.6A"
ARRAY = "OBS-CSTAR-LONG-PRIME-PROGRESSION-NORM-COUNTERMODEL"
SQUARE = "OPEN-CSTAR-LONG-PRIME-MOVING-PHASE-SQUARE"
CSTAR = "OPEN-HLZ-PURE-FOURTH-CSTAR-CANCELLATION"
PNT = "EXT-CLASSICAL-PNT"

PACKET = "LEM-MELLIN-NEGATIVE-LOG-SHARP-INVERSION-PACKET"
WITNESS = "OBS-MELLIN-ALL-NEGATIVE-LOG-SIGNED-DIVERGENCE"
SHARP = "THM-MELLIN-EXACT-SIGNED-LOG-BOUNDARY"
SEQUENCE = "OBS-CSTAR-COMMON-NONNEGATIVE-SEQUENCE-NORM-COUNTERMODEL"
INTEGER = "OBS-CSTAR-COMMON-INTEGER-SEQUENCE-NORM-COUNTERMODEL"


def read(path):
    return [json.loads(line) for line in (ROOT / path).read_text().splitlines() if line.strip()]


def write(path, rows):
    (ROOT / path).write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows))


def claim(ident, note, section, kind, statement, hypotheses):
    return dict(id=ident, paper_id=None, locator=note + " · " + section, evidence=note,
                claim_kind=kind, statement=statement, hypotheses=hypotheses,
                status=SCOPED, novelty_claim=False)


CLAIMS = [
    claim(PACKET, MELLIN, "One packet: a large sharp inverse with small weakened norm",
          "negative_logarithmic_sharp_inversion_packet_estimate",
          "Fix a prime p, u_*=log p, b=1/p and 0<A<q. The one-sided packet F_T(u_*+v)=b χ(v/W)η(Tv)sin(Tv), W=log^A(T)/T, has squared N_(−q) norm O(b²[W√T+TW/log^q T]) and tends to zero in this norm. On a=1+ε/2 its sharp inverse at u_* equals b exp((a−1/2)u_*) log(TW)/(2π)+O(b), with O(bW) change for U∈[T,T+1]. The target prime contributes −b log p log(TW)/(2π√p) in the folded contour, while all other prime terms tend to zero and the gamma piece is O(N_(−q)).",
          "Fixed prime, strip margin 0<ε<1/4 and fixed 0<A<q. Constants may depend on the stage, including p,q,A,ε. The packet shrinks strictly between the target prime center and the next prime-power center. The contour statement uses a good height in [T,T+1]."),
    claim(WITNESS, MELLIN, "A single globally smooth test",
          "simultaneous_negative_logarithmic_strip_signed_counterexample",
          "For each fixed strip with 0<ε<1/4 one real smooth f, zero near zero and one and O(x^(−3/2)) at infinity, has finite N_(−q) for every fixed q>0. Its samples f(n) at prime powers and f(1/n) for n≥1 vanish. The ordinary symmetric raw zero sum with multiplicity has a subsequence tending to −∞ and a bounded subsequence. The pole and archimedean terms are absolutely finite.",
          "Use one locally finite escaped-prime packet sequence with q_j=1/j and A_j=q_j/2 before choosing each carrier. Stagewise protection controls both finite-height subsequences. The witness satisfies literal (A) and (B). Its critical norm is infinite, and the weakened norms need not be bounded uniformly as q decreases to zero."),
    claim(SHARP, MELLIN, "What this obstruction says",
          "sharp_signed_symmetric_logarithmic_strip_boundary",
          "The exponent p=0 is the exact boundary for a universal ordinary symmetric height formula in this logarithmic strip scale. Every p≥0 suffices under the original value bounds and local H¹ around x=1 or the literal (A) class with midpoint values. One smooth witness in that class defeats all weights √(1+t²)/log^q(e+|t|), q>0.",
          "Fix 0<ε<1/4 so both sufficiency and the counterexample apply on the stated strip. This is a universal symmetric result for the stated test class. No individual necessity claim, uniform q-bound, or separate half-axis threshold is asserted."),
    claim(SEQUENCE, COMMON, "Exact statement",
          "common_sequence_all_residue_and_induced_unit_norm_countermodel",
          "For K≈T^θ, 1/2<θ<2/3 and integer P≈KT, one nonnegative real sequence b(n) on J=[P,2P)∩ℤ has exact mass P. Writing B_(k,u)=Σ_(n≡u mod k)b(n), the all-residue squared error about P/k totals O(PK) over k≤2K and the sum of row maxima is O(K√P). Both bounds hold on the unit rows centered by their induced means. For the full support S of the narrow-band fourth prime polynomial, including repeated factors, |S|=binom(M+3,4)≍K/log⁴K where M is the number of band primes. The coefficients c_k=4!/∏_(p|k)m_p! satisfy 1≤c_k≤24. The h=1 unit-centered real phase projection with weights c_k/k is ≫√(P|S|), exceeding T log⁴T by a divergent factor.",
          "Fix a narrow relative prime band [X,(1+η)X] with K=X⁴ and (1+η)⁴<2 so S lies in [K,2K). All congruence rows arise from the same sequence and whole-row common-divisor marginals agree. The all-residue centering and induced unit means concern an integer interval, with no prime support, simultaneous unit support, P/φ(k) baseline, or Mangoldt pointwise cap."),
    claim(INTEGER, COMMON, "Integer-valued realization with exact mass",
          "integer_valued_common_sequence_countermodel",
          "In the common-sequence countermodel the weights can be nonnegative integers while preserving mass P, the same order of discrepancy bounds and the phase lower bound. Draw P integers from probabilities b(n)/P. The multinomial summed expected variance is O(PK), and the projection variance O(P(|S|/K)²) is negligible against P|S|. Markov and Chebyshev give a realization satisfying both bounds.",
          "Same single interval, full fourth-power support and centering as the real-weight model. Integer values can include repeated draws. This remains an abstract obstruction and does not estimate the genuine prime term or the full smooth C_* sum."),
]


def proof(start, end, note, locator, relation):
    return dict(evidence=note, locator=locator, relation=relation, status=SCOPED,
                **{"from": start, "to": end})


PROOFS = [
    proof(PACKET, TITCH, MELLIN, "Titchmarsh–Heath-Brown (1986), Theorem 9.6(A), printed p. 217", "uses_good_height_logarithmic_derivative"),
    proof(WITNESS, PACKET, MELLIN, MELLIN + " · A single globally smooth test", "diagonalizes_fixed_prime_packet_estimates"),
    proof(SHARP, CRITICAL, MELLIN, REVIEWS + "director_signed_mellin_round16.md · Statement and distinction from absolute sampling", "uses_critical_symmetric_sufficiency"),
    proof(SHARP, LITERAL, MELLIN, REVIEWS + "director_signed_mellin_round16.md · Literal local hypotheses", "uses_literally_admissible_local_class"),
    proof(SHARP, WITNESS, MELLIN, MELLIN + " · Exact statement", "uses_one_witness_for_all_strict_weakenings"),
    proof(SEQUENCE, PNT, COMMON, COMMON + " · Exact statement, classical PNT for a fixed relative interval", "uses_pnt_to_count_supported_moduli"),
    proof(INTEGER, SEQUENCE, COMMON, COMMON + " · Integer-valued realization with exact mass", "uses_weighted_sampling_distribution"),
]

BOUNDARIES = [
    (PACKET, CRITICAL, "reuses_finite_contour_method_without_invoking_critical_theorem", MELLIN),
    (WITNESS, CRITICAL, "exhibits_divergence_outside_critical_norm", MELLIN),
    (SHARP, LITERAL, "identifies_universal_boundary_in_literally_admissible_class", MELLIN),
    (SEQUENCE, ARRAY, "restores_common_sequence_under_all_residue_or_induced_unit_centering", COMMON),
    (SEQUENCE, SQUARE, "limits_norm_only_implication_while_leaving_prime_estimate_open", COMMON),
    (INTEGER, CSTAR, "changes_weights_to_integers_without_imposing_prime_support", COMMON),
]


def connection(ident, note, sources, statement, assumptions, proved, proposed, failures,
               significance, difficulty, next_step, tests):
    return dict(id=ident, evidence=note,
                source_theorems=list(dict.fromkeys(source for source, _ in sources)),
                source_claims=[dict(id=source, locator=locator) for source, locator in sources],
                statement=statement, compatible_assumptions=assumptions, already_proved=proved,
                new_claim_suggested=proposed, conjectural_or_unresolved=proposed,
                potential_counterexamples=failures, significance=significance, difficulty=difficulty,
                next_precise_step=next_step, tests=tests, status=SCOPED, novelty_claim=False)


CONNECTIONS = [
    connection("CONN-MELLIN-CRITICAL-SIGNED-SHARP-LOG-BOUNDARY", MELLIN,
               [(CRITICAL, REVIEWS + "director_signed_mellin_round16.md · Endpoint sharp Fourier inversion"),
                (LITERAL, REVIEWS + "director_signed_mellin_round16.md · Literal local hypotheses"),
                (PACKET, MELLIN + " · One packet"), (WITNESS, MELLIN + " · A single globally smooth test"),
                (SHARP, MELLIN + " · What this obstruction says")],
               "The critical strip norm gives uniform sharp inversion needed for the full prime sum. Every strict logarithmic weakening admits one escaped-center smooth witness defeating the symmetric formula.",
               "Fixed positive strip margin, original value envelopes and local H¹ or literal manuscript (A) for the positive theorem. The smooth witness satisfies literal (A) and (B) on any fixed 0<ε<1/4.",
               "Critical sufficiency, per-stage packet gain, and one witness with all negative-log norms finite, zero prime samples, finite arithmetic terms and two incompatible subsequences.",
               "Determine whether a trace formula with a different infinite atomic input admits the same exact logarithmic boundary.",
               "Pointwise inversion at each fixed prime-power argument can hold while the infinite weighted prime sum fails to converge under the contour cutoff.",
               "Closes the universal signed symmetric boundary problem raised in Round 16 within the stated norm scale.",
               "The one-witness statement requires stage-specific norm and finite-height budgets in addition to the fixed-prime packet estimate.",
               "Specify one other arithmetic trace formula and check its contour bounds and atomic coefficients before transferring the construction.",
               "Tilted interpolation, the sharp Dirichlet kernel, good-height contour, and diagonal control of two subsequences."),
    connection("CONN-CSTAR-COMMON-SEQUENCE-NORM-OBSTRUCTION", COMMON,
               [(ARRAY, REVIEWS + "director_long_prime_round15.md · An exact limitation of two progression norms"),
                (SQUARE, REVIEWS + "director_long_prime_round15.md · The exact prime form"),
                (SEQUENCE, COMMON + " · Exact statement"),
                (INTEGER, COMMON + " · Integer-valued realization with exact mass")],
               "Common-sequence consistency, positivity and even integer multiplicities allow the large target projection under all-residue or induced-unit-mean discrepancy budgets.",
               "One ordinary integer interval, exact mass P, all-residue or induced-unit centering and the h=1 phase over the full narrow-band fourth-power support.",
               "Nonnegative real and integer versions with exact mass, stated two norm budgets, common-divisor compatibility and the phase lower bound.",
               "Determine what additional sieve or prime-support structure controls the genuine moving phase.",
               "The example allows mass on nonunits. Its stated bounds compare with P/k or an induced unit mean, and give no corresponding bound about the prime-model P/φ(k).",
               "Strengthens the earlier abstract row obstruction while preserving the open arithmetic estimate.",
               "Finite Fourier and sampling estimates suffice for the abstract examples. Sieve support or the genuine prime phase needs separate estimates.",
               "Test centered norm inequalities with the actual prime-model unit baseline or explicit sieve weights.",
               "Short positive convolution, rational-frequency Gram bounds, imprimitive denominator accounting and multinomial sampling."),
]

GROUPS = [
    ("NEGATIVE-MELLIN", "One smooth witness for all strict signed logarithmic weakenings", MELLIN,
     ["weighted160_negative_log_counterexample_campaign.md", "geometry160_negative_log_skeptic.md",
      "analytic160_negative_log_packet_lemma.md", "analytic165_diagonal_log_weakening_review.md",
      "release168_negative_director_qa.md"]),
    ("COMMON-SEQUENCE-PHASE", "Common nonnegative and integer sequence phase countermodels", COMMON,
     ["prime161_common_sequence_phase_campaign.md", "geometry163_common_sequence_skeptic.md",
      "analytic163_common_sequence_review.md", "release169_common_director_qa.md"]),
]

SIGNED_STATE = (
    "Round 17 closes the weaker logarithmic-weight question for universal ordinary symmetric summation "
    "in the stated class. The critical weight suffices and one smooth witness defeats every strict weakening. "
    "Weaker local conditions and the separate half-axis threshold remain independent."
)
OPEN_LOCAL = "Investigate weaker local assumptions and separate half-axis convergence for 0≤p≤1."
STATE_UPDATES = {
    ident: dict(conjectural=OPEN_LOCAL, conjectural_or_unresolved=OPEN_LOCAL,
                new_claim_suggested=OPEN_LOCAL, next_step=OPEN_LOCAL, next_precise_step=OPEN_LOCAL,
                latest_signed_log_boundary=SIGNED_STATE, latest_signed_log_claim_ids=[PACKET, WITNESS, SHARP])
    for ident in ("CONN-MELLIN-SIGNED-LOCAL-REGULARITY", "CONN-MELLIN-RAW-HEIGHT-AND-STRIP-TRACE",
                  "CONN-MELLIN-CRITICAL-LOG-ABSOLUTE-ENDPOINT")
}


def main():
    required = {MELLIN, COMMON, GROUP_LEDGER, CONNECTION_UPDATES, "theorems/theorems.jsonl",
                "corpus/bibliography.jsonl", "connections/connections.jsonl"}
    required.update(REVIEWS + name for _, _, _, reviews in GROUPS for name in reviews)
    for item in sorted(required):
        if not (ROOT / item).is_file():
            raise FileNotFoundError(item)

    claims = {row["id"] for row in CLAIMS}
    known = claims | {row["id"] for row in read("theorems/theorems.jsonl")}
    known.update(row["id"] for row in read("corpus/bibliography.jsonl"))
    known.add(PNT)
    refs = {row[key] for row in PROOFS for key in ("from", "to")}
    refs.update(ident for start, end, *_ in BOUNDARIES for ident in (start, end))
    refs.update(ident for row in CONNECTIONS for ident in row["source_theorems"])
    if len(claims) != len(CLAIMS) or refs - known:
        raise ValueError(f"Duplicate claims or unresolved source references: {sorted(refs - known)}")
    current_connection_ids = {row["id"] for row in read("connections/connections.jsonl")}
    if missing := STATE_UPDATES.keys() - current_connection_ids:
        raise ValueError(f"Unknown connection status targets: {sorted(missing)}")

    groups = {row["id"]: row for row in read(GROUP_LEDGER)}
    for ident, title, note, reviews in GROUPS:
        group_id = "REVIEW-GROUP-R17-" + ident
        groups[group_id] = dict(id=group_id, title=title, status=SCOPED, director_adjudication=note,
                                independent_reviews=[REVIEWS + name for name in reviews])
    updates = {row["id"]: row for row in read(CONNECTION_UPDATES)}
    for ident, fields in STATE_UPDATES.items():
        updates[ident] = dict(id=ident, evidence=MELLIN,
                              fields=dict(updates.get(ident, {}).get("fields", {}), **fields))
    shards = {
        "theorems/research_round17_claims.jsonl": CLAIMS,
        "theorems/research_round17_proof_edges.jsonl": PROOFS,
        "graphs/research_round17_boundaries.jsonl": [
            dict(record_type="edge", relation=relation, provenance=note, status=SCOPED,
                 **{"from": start, "to": end})
            for start, end, relation, note in BOUNDARIES
        ],
        "connections/research_round17_connections.jsonl": CONNECTIONS,
    }
    for path, rows in shards.items():
        write(path, rows)
    write(GROUP_LEDGER, groups.values())
    write(CONNECTION_UPDATES, updates.values())
    print(json.dumps(dict(staged_shards={path: len(rows) for path, rows in shards.items()},
                          scoped_groups=len(GROUPS), later_connection_updates=len(STATE_UPDATES)), indent=2))


if __name__ == "__main__":
    main()
