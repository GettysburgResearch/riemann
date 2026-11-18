#!/usr/bin/env python3
"""Stage scoped Round 16 mathematical records from director adjudications."""
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REVIEWS = "audits/adversarial_reviews/"
MELLIN = REVIEWS + "director_signed_mellin_round16.md"
GONEK_NOTE = REVIEWS + "director_gonek_constants_round16.md"
RIEMANN_NOTE = REVIEWS + "director_riemann1859_whole_round16.md"
GROUPS_FILE = "audits/reviewed_claim_groups.jsonl"
CONNECTION_UPDATES = "quality/connection_status_updates.jsonl"

TITCH = "PAPER-M001"
LOCAL_LOG_DERIV = "EXT-TITCH-1986-9.6A"
LUECKING = "PAPER-LUECKING1986-BERGMAN-MULTIPLIERS"
LUECKING_SHARD = "papers/round16_dependency_records.jsonl"
RIEMANN = "PAPER-S001"
GENOCCHI = "PAPER-H402"
MANGOLDT = "PAPER-H406"
HADAMARD = "EXT-HADAMARD-FACTORIZATION-ORDER-BELOW-ONE"
MANGOLDT_PSI = "EXT-VON-MANGOLDT-ORDERED-PSI-MIDPOINT-FORMULA"
PRODUCT = "THM-RIEMANN1859-MODERN-GENUS-ZERO-PAIRED-PRODUCT"
ORDERED_J = "THM-RIEMANN1859-MODERN-ORDERED-J0-FORMULA"
LUECKING_CONTEXT = "sources/prime146_mellin_provenance/luecking1986.pdf"
PREDECESSOR_REVIEW = REVIEWS + "prime146_mellin_trace_prior_art.md"
BL = "PAPER-L002"
GONEK = "PAPER-LF63-GONEK1984"
LOG_REPAIR = "THM-MELLIN-CRITICAL-LOG-ZERO-TRACE"
ABS_ENDPOINT = "OBS-MELLIN-CRITICAL-LOG-ENDPOINT-ABSOLUTE-DIVERGENCE"
ABEL = "LEM-GONEK-EXPLICIT-ABEL-PRIME-SUBSTITUTION"
RAW_CONNECTION = "CONN-MELLIN-RAW-HEIGHT-AND-STRIP-TRACE"
ENDPOINT_CONNECTION = "CONN-MELLIN-CRITICAL-LOG-ABSOLUTE-ENDPOINT"
SIGNED = "THM-MELLIN-CRITICAL-STRIP-SYMMETRIC-EXPLICIT-FORMULA"
SELBERG_REMAINDER = "LEM-MELLIN-SELBERG-PROJECTION-AND-COUNT-REMAINDER"
ROUND_QA = REVIEWS + "geometry155_director_round16_qa.md"
RIEMANN_QA = REVIEWS + "geometry157_director_riemann_whole_qa.md"
HALF_AXES = "THM-MELLIN-LOG-SIGNED-HALF-AXIS-CONVERGENCE"
LITERAL = "LEM-BL-LITERAL-TEST-CLASS-LOCAL-MELLIN-H1"
CUSP = "OBS-MELLIN-LOG-SIGNED-BOUNDARY-CUSP"
CONVOLUTION = "LEM-GONEK-EXPLICIT-POSITIVE-DERIVATIVE-CONVOLUTION"
M11 = "LEM-GONEK-EXPLICIT-LEMMA8-ORDER-ONE-PAIR"
SCOPED = "adjudicated_scoped"
DENSITY_LOC = "Titchmarsh–Heath-Brown, second ed. (1986), Chapter IX, Theorem 9.19(C), printed p. 237"
LOCAL_LOG_DERIV_LOC = "Titchmarsh–Heath-Brown, second ed. (1986), Chapter IX, Theorem 9.6(A), printed p. 217"
MEAN_LOC = "Titchmarsh–Heath-Brown, second ed. (1986), Chapter IX, Notes §9.25 (9.25.1), with Theorem 9.3"


def read(path):
    return [json.loads(line) for line in (ROOT / path).read_text().splitlines() if line.strip()]


def write(path, rows):
    (ROOT / path).write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows))


def claim(ident, note, section, sources, kind, statement, hypotheses):
    return dict(id=ident, paper_id=None, related_paper_ids=sources, locator=note + " · " + section,
                evidence=note, claim_kind=kind, status=SCOPED, novelty_claim=False,
                statement=statement, hypotheses=hypotheses)


CLAIMS = [
    claim(SIGNED, MELLIN, "Statement and distinction from absolute sampling",
          [BL, TITCH], "sufficient_critical_strip_symmetric_explicit_formula",
          "The ordinary inclusive symmetric height sum over nontrivial zeta zeros counted with multiplicity converges to the ordinary compensated Guinand–Weil formula with critical Mellin strip area weight √(1+t²). Consequently the logarithmic weights √(1+t²) log^p(e+|t|) suffice for every p≥0 under the same local hypotheses.",
          "Continuous f with f(x)=O(x^δ) at zero and O(x^(−1−δ)) at infinity, F(u)=e^(u/2)f(e^u) in H¹ on a neighborhood of 0, and a finite stated strip norm on β∈[−ε,1+ε], 0<ε<δ. Unconditional. The contour proof establishes symmetric convergence, with separate half-axis convergence established by the Selberg route for p>1."),
    claim(SELBERG_REMAINDER, MELLIN, "Literal local hypotheses and the independent Selberg route",
          [TITCH], "absolute_projection_and_count_remainder_bounds",
          "For p>1, writing H(t)=h(1/2+it), Σ_ρ|h(ρ)−H(Im ρ)|<∞. If S₀(t)=N(t)−M(t) is the right-continuous positive-height counting remainder, then ∫₂∞|H′(t)S₀(t)|dt<∞ and H(T)S₀(T)→0 at every height. The same control holds with H(−t) on the negative half-axis.",
          "Original endpoint value bounds and finite logarithmic Mellin strip area norm with p>1 and positive strip margin. Neither local H¹ nor a smooth-density convergence assumption is needed. The lemma does not address the projected term ∫ H M′."),
    claim(HALF_AXES, MELLIN, "Literal local hypotheses and the independent Selberg route",
          [TITCH], "sufficient_separate_signed_height_convergence",
          "For p>1 the same signed zero sum converges separately on each half-height axis. The uniform density bound makes the projection onto Re s=1/2 an absolutely summable correction. The second moment of the counting remainder handles the signed Stieltjes integral, including the exact ordinate endpoint.",
          "Same value, local H¹ and strip hypotheses as the symmetric theorem but with weight √(1+t²) log^p(e+|t|), p>1. No separate half-axis conclusion at p≤1 is asserted."),
    claim(LITERAL, MELLIN, "Literal local hypotheses and the independent Selberg route",
          [BL], "source_scope_local_regularization_implication",
          "Under the pinned manuscript's literal conditions (A) and (B), finite critical strip norm gives central F∈H¹⁄². Its Gagliardo seminorm excludes any genuine jump. The source midpoint values then select the continuous representative, and finite one-sided limits of f′ give local H¹ near x=1, so the critical symmetric formula applies.",
          "Pinned 12-page Michigan author manuscript only. Condition (A) places the first-kind restriction on both f and f′ at its exceptional points. The general continuous class with the same value bounds needs a separate local assumption."),
    claim(CUSP, MELLIN, "A counterexample when the local-origin condition is omitted",
          [TITCH], "counterexample_to_universal_signed_sampling_without_local_regularity",
          "A real continuous compactly supported f, smooth off x=1, has finite p=3 logarithmic strip norm and symmetric raw-height sum tending to positive infinity. Its local archimedean compensation diverges. In log coordinates take a compact positive-definite multiplier times the inverse Fourier transform of a positive even spectrum comparable to 1/(|t| log²|t| loglog|t|). The smooth counting density diverges positively while the signed projection and count-remainder corrections converge.",
          "Any fixed finite strip of the indicated form. The cusp lies outside literal (A) and the neighborhood H¹ theorem. It is separate from the smooth p=3 example of absolute divergence and supplies no additional author finding."),
    claim(CONVOLUTION, GONEK_NOTE, "All positive integer orders",
          [GONEK], "unconditional_explicit_positive_derivative_convolution",
          "For integer μ,ν≥1, z>1, M=μ+ν and L=log z, the unsigned log-power divisor sum differs from μ!ν!/(M+1)! times zL^(M+1) by at most [min(μ,ν)+1/e+μ^μν^ν/M^M] zL^M.",
          "Gonek Lemma 7 (40), both derivative orders positive. The sign (−1)^(μ+ν) multiplies both parts in the Dirichlet series convention. The counting sum includes the integer endpoint. No claim of optimality or full numerical derivative-tail bound."),
    claim(M11, GONEK_NOTE, "A convenient rational (1,1) allocation and its finite use",
          [GONEK], "unconditional_explicit_finite_prime_divisor_step",
          "For the (1,1) coefficient B_n in Gonek Lemma 8, letting L=log x and I₃=∫₁ˣ u^(iδ−1) log³(x/u)du, the finite error |Σ_(n≤x) B_n(1,1,δ)+(x/6)I₃| is at most x[(19/4)L³+(229/4)L²+90L].",
          "Real x>1 and real |δ|≤1/2. Uses the convenient rational (1,1) convolution bound 9/4 and the positive-power Abel specialization with vanishing upper boundary. This concerns only the divisor and prime-to-integral steps."),
    claim(PRODUCT, RIEMANN_NOTE, "Continuation and the product: the exact missing steps",
          [RIEMANN], "known_modern_reconstruction_of_historical_product",
          "Let Xi(t)=ξ_*(1/2+it), with ξ_*(s)=s(s−1)π^(−s/2)Γ(s/2)ζ(s)/2. Its even Taylor series defines G(w)=Xi(√w), entire of order at most 1/2 by log M_Xi(R)=O(R log(R+2)), with order exactly 1/2 by Stirling along positive real s. Hadamard gives the genus-zero product Xi(t)=Xi(0) ∏_(Re α>0)(1−t²/α²), including multiplicities. In s coordinates the paired normalization is Xi(0)∏_α(1+1/(4α²))=ξ_*(0)=1/2.",
          "Riemann's theta and cosine representations, evenness, positivity on the imaginary t axis, and external modern finite-order Hadamard factorization. No RH, square-root branch choice, or zero-count asymptotic is used for the product. This is a known modern reconstruction of the 1859 product."),
    claim(ORDERED_J, RIEMANN_NOTE, "Exact arithmetic identity, branches and the known constant",
          [RIEMANN, GENOCCHI, MANGOLDT], "known_modern_reconstruction_of_historical_ordered_explicit_formula",
          "For x>1, midpoint J₀(x) equals li(x)−lim_(T→∞)Σ_(|Im ρ|≤T) E_ρ(x)+∫ₓ∞du/[u(u²−1)log u]−log 2. Use E_ρ(x)=Ei(ρ log x)−iπ sgn(Im ρ) with the continued log x^ρ=ρ log x. The offsets cancel under conjugate ordering. The summable O_I((1+|Im ρ|)^(−2)) kernel remainder reduces raw pointwise convergence to the later von Mangoldt midpoint ψ₀ formula. Unit-height counts and O_x(1/T) terms give equivalence with the source's |α| order.",
          "Midpoint values at prime powers, zeros with multiplicity, the stated height order, paired normalization, and external later ordered von Mangoldt formula. The real constant −log 2 is Genocchi's known correction. No proof of the ordered limit is attributed to the 1859 text and no novelty is claimed."),
]


for row in CLAIMS:
    row["qa_evidence"] = [RIEMANN_QA if row["id"] in {PRODUCT, ORDERED_J} else ROUND_QA]


def proof(start, end, note, locator, relation):
    return dict(evidence=note, locator=locator, relation=relation, status=SCOPED,
                **{"from": start, "to": end})


PROOFS = [
    proof(SIGNED, LOCAL_LOG_DERIV, MELLIN, LOCAL_LOG_DERIV_LOC, "uses_local_logarithmic_derivative_on_good_heights"),
    proof(SIGNED, TITCH, MELLIN, "Titchmarsh–Heath-Brown (1986), Chapter IX, Theorems 9.2–9.3", "uses_unit_interval_zero_count_and_exact_height_convention"),
    proof(SELBERG_REMAINDER, TITCH, MELLIN, DENSITY_LOC, "uses_uniform_near_line_zero_density"),
    proof(SELBERG_REMAINDER, TITCH, MELLIN, MEAN_LOC, "uses_unconditional_count_remainder_mean_square"),
    proof(LITERAL, BL, MELLIN, "Pinned author manuscript pp. 5–6, literal conditions (A) and (B)", "uses_exact_printed_test_class"),
    proof(LITERAL, SIGNED, MELLIN, MELLIN, "verifies_sufficient_local_regularity"),
    proof(HALF_AXES, SELBERG_REMAINDER, MELLIN, MELLIN, "uses_absolute_projection_and_count_remainder"),
    proof(CUSP, SELBERG_REMAINDER, MELLIN, MELLIN, "uses_projection_and_stieltjes_steps_without_local_h1"),
    proof(CONVOLUTION, GONEK, GONEK_NOTE, "1984 journal pp. 133–134, Lemma 7 equation (40)", "quantifies_coefficient_estimate"),
    proof(M11, CONVOLUTION, GONEK_NOTE, GONEK_NOTE, "uses_order_one_pair_coefficient_bound"),
    proof(M11, ABEL, GONEK_NOTE, REVIEWS + "director_explicit_abel_round15.md", "uses_positive_log_power_specialization"),
    proof(M11, GONEK, GONEK_NOTE, "1984 journal pp. 134–135, Lemma 8", "quantifies_finite_lemma8_step"),
    proof(PRODUCT, "THM-HR401", RIEMANN_NOTE, "Original pp. 673–674, theta continuation and symmetric kernel", "uses_theta_continuation_and_growth"),
    proof(PRODUCT, "THM-HR402", RIEMANN_NOTE, "Original p. 674 and paired normalization in the director review", "uses_exact_xi_normalization"),
    proof(PRODUCT, HADAMARD, RIEMANN_NOTE, RIEMANN_NOTE + " · genus-zero factorization of an entire function of order below one", "uses_external_modern_factorization"),
    proof(ORDERED_J, PRODUCT, RIEMANN_NOTE, RIEMANN_NOTE + " · paired normalization", "uses_paired_product_normalization"),
    proof(ORDERED_J, "THM-HR404", RIEMANN_NOTE, "Original pp. 675–676, Euler logarithm and midpoint inverse Mellin transform", "uses_prime_power_midpoint_inverse"),
    proof(ORDERED_J, "THM-HR405", RIEMANN_NOTE, "Genocchi 1860 pp. 57–58, equation (11)", "uses_known_real_constant_correction"),
    proof(ORDERED_J, MANGOLDT_PSI, RIEMANN_NOTE, RIEMANN_NOTE + " · later ordered midpoint ψ₀ explicit formula, von Mangoldt 1895", "uses_external_ordered_midpoint_explicit_formula"),
    proof(ORDERED_J, TITCH, RIEMANN_NOTE, "Titchmarsh–Heath-Brown (1986), Chapter IX, unit-interval count", "uses_local_zero_count_for_equivalent_orderings"),
]

BOUNDARIES = [
    (SIGNED, ABS_ENDPOINT, "gives_signed_convergence_for_smooth_absolute_divergence_witness", MELLIN),
    (CUSP, SIGNED, "excludes_removing_local_h1_from_continuous_scale", MELLIN),
    (CUSP, LITERAL, "cusp_lies_outside_literal_test_class", MELLIN),
    (SIGNED, LOG_REPAIR, "establishes_symmetric_convergence_at_critical_weight_with_local_h1", MELLIN),
    (HALF_AXES, SIGNED, "establishes_stronger_one_sided_mode_for_stronger_weight", MELLIN),
    (PRODUCT, RIEMANN, "distinguishes_modern_product_proof_from_printed_quotient_argument", RIEMANN_NOTE),
    (ORDERED_J, RIEMANN, "distinguishes_known_ordered_reconstruction_from_printed_argument", RIEMANN_NOTE),
    (ORDERED_J, MANGOLDT, "points_to_later_ordered_midpoint_dependency", RIEMANN_NOTE),
    (LOG_REPAIR, LUECKING, "ambient_absolute_sampling_context_only", PREDECESSOR_REVIEW),
    (M11, GONEK, "quantifies_finite_coefficient_step_only", GONEK_NOTE),
]


def connection(ident, note, sources, statement, assumptions, proved, proposed, failures,
               significance, difficulty, next_step, tests):
    return dict(id=ident, evidence=note, source_theorems=list(dict.fromkeys(source for source, _ in sources)),
                source_claims=[dict(id=source, locator=locator) for source, locator in sources],
                statement=statement, compatible_assumptions=assumptions, already_proved=proved,
                new_claim_suggested=proposed, conjectural_or_unresolved=proposed,
                potential_counterexamples=failures, significance=significance, difficulty=difficulty,
                next_precise_step=next_step, tests=tests, status=SCOPED, novelty_claim=False)


CONNECTIONS = [
    connection("CONN-MELLIN-SIGNED-LOCAL-REGULARITY", MELLIN,
               [(LOCAL_LOG_DERIV, LOCAL_LOG_DERIV_LOC), (TITCH, DENSITY_LOC), (TITCH, MEAN_LOC),
                (SIGNED, MELLIN), (SELBERG_REMAINDER, MELLIN), (HALF_AXES, MELLIN), (LITERAL, MELLIN),
                (CUSP, MELLIN), (ABS_ENDPOINT, REVIEWS + "director_critical_endpoint_round15.md")],
               "Sharp Fourier inversion on the two exterior lines gives the critical symmetric formula. The independent Selberg projection method gives separate half-axis convergence for p>1.",
               "Finite critical Mellin strip norm, original endpoint value bounds, and local H¹ in log coordinates for the contour theorem. Literal (A) and the norm imply the local condition. The Selberg route imposes the stronger p>1 weight.",
               "Ordinary inclusive symmetric convergence at p=0 including the smooth p=3 absolute-divergence witness, separate convergence on each half-axis for p>1, and signed failure for a continuous cusp outside the local and literal source classes.",
               "Determine whether the symmetric theorem survives logarithmically weaker strip weights, how far the local condition can be weakened, and whether the two half-height sums converge at smaller p.",
               "The compact p=3 cusp defeats the norm and value hypotheses alone, with divergent local archimedean integral.",
               "Separates critical signed symmetric convergence with local regularity from the p>3 universal absolute trace. Luecking's Bergman embedding is context for the ambient absolute threshold only.",
               "Uses endpoint Fourier inversion and a good-height contour, with additional work needed for weaker strip or local conditions.",
               "Check logarithmically weaker inversion bounds and possible cancellation without symmetric cutoff.",
               "Sharp versus Gaussian inversion, folded ξ′/ξ contour, restoration of exact heights, Selberg estimates, and compact smooth approximation."),
    connection("CONN-GONEK-EXPLICIT-CONVOLUTION-AND-ABEL", GONEK_NOTE,
               [(GONEK, "1984 journal pp. 133–135, Lemmas 7–8"), (CONVOLUTION, GONEK_NOTE),
                (M11, GONEK_NOTE), (ABEL, REVIEWS + "director_explicit_abel_round15.md")],
               "An explicit positive-order divisor estimate combines with the Abel prime substitution to bound the finite (1,1) step in Lemma 8.",
               "Positive integer derivative orders in the convolution and real shifts |δ|≤1/2 in the finite (1,1) application.",
               "An all-positive-order convolution constant and an explicit bound for the combined (1,1) finite remainder.",
               "Allocate constants in the remaining steps to obtain a certified onset for the derivative-tail estimate.",
               "The two-positive-order floor centering argument relies on vanishing weights at both endpoints. A zero order needs its own boundary analysis.",
               "Quantifies two reusable arithmetic steps in a numerical derivative-tail argument.",
               "Elementary for the finite estimates. A full onset requires additional contour and tail analysis.",
               "Bound the derivative gamma factors and associated contour errors with verified constants.",
               "Right-continuous floor summation, unimodality, a beta integral and the independently bounded Abel error."),
]

CONNECTIONS[0]["context_sources"] = [
    dict(id=LUECKING, locator=LUECKING_CONTEXT + " · p. 126, Bergman embedding theorem, and p. 127, radius lemma",
         evidence=PREDECESSOR_REVIEW,
         scope="Ambient absolute-sampling threshold only; no signed raw-height implication."),
]

GROUPS = [
    ("MELLIN-SIGNED-CRITICAL", "Critical symmetric convergence and the stronger-weight half-height result", MELLIN,
     ["weighted152_signed_p1_campaign.md", "uniform153_contour_signed_critical_review.md",
      "geometry154_critical_contour_and_cusp_adjudication.md", "weighted146_signed_endpoint_research.md",
      "uniform147_signed_endpoint_adversarial.md", "geometry149_signed_endpoint_third.md",
      "geometry155_director_round16_qa.md"]),
    ("MELLIN-LOCAL-CUSP", "Signed p=3 failure in the continuous class without local regularity", MELLIN,
     ["uniform147_signed_endpoint_adversarial.md", "geometry154_critical_contour_and_cusp_adjudication.md",
      "geometry155_director_round16_qa.md"]),
    ("GONEK-FINITE-CONSTANTS", "Explicit positive-order convolution and finite (1,1) Lemma 8 bound", GONEK_NOTE,
     ["prime142_gonek_convolution_constant.md", "weighted142_gonek_convolution_review.md",
      "prime145_explicit_all_derivative_convolution.md", "weighted145_explicit_all_derivative_review.md",
      "geometry155_director_round16_qa.md"]),
]

PENDING_SIGNED = "Weaker-than-critical strip weights, weaker local assumptions, and separate half-axis convergence at p≤1 remain open."
SIGNED_STATE = (
    "Round 16 proves inclusive symmetric raw-height convergence at p=0 with local H¹, including the smooth p=3 absolute-divergence witness, and separate half-axis convergence for p>1. "
    "A separate p=3 continuous compact cusp yields signed divergence outside this local class and the literal manuscript class."
)
OPEN_LOCAL_STEP = "Investigate signed sampling below the critical strip weight and characterize weaker local conditions on the logarithmic density term."
STATE_UPDATES = {
    RAW_CONNECTION: dict(conjectural=PENDING_SIGNED, conjectural_or_unresolved=PENDING_SIGNED,
                         new_claim_suggested=PENDING_SIGNED, next_step=OPEN_LOCAL_STEP,
                         next_precise_step=OPEN_LOCAL_STEP, later_signed_resolution=SIGNED_STATE,
                         later_signed_claim_ids=[SIGNED, HALF_AXES, LITERAL, CUSP]),
    ENDPOINT_CONNECTION: dict(conjectural=PENDING_SIGNED, conjectural_or_unresolved=PENDING_SIGNED,
                              new_claim_suggested=PENDING_SIGNED, next_step=OPEN_LOCAL_STEP,
                              next_precise_step=OPEN_LOCAL_STEP, later_signed_resolution=SIGNED_STATE,
                              later_signed_claim_ids=[SIGNED, HALF_AXES, LITERAL, CUSP]),
}


def main():
    required = {MELLIN, GONEK_NOTE, RIEMANN_NOTE, ROUND_QA, RIEMANN_QA, LUECKING_CONTEXT, LUECKING_SHARD, PREDECESSOR_REVIEW, GROUPS_FILE, CONNECTION_UPDATES, "theorems/theorems.jsonl",
                "corpus/bibliography.jsonl", "connections/connections.jsonl"}
    required.update(REVIEWS + name for _, _, _, reviews in GROUPS for name in reviews)
    for item in sorted(required):
        if not (ROOT / item).is_file():
            raise FileNotFoundError(item)

    claims = {row["id"] for row in CLAIMS}
    known = claims | {row["id"] for row in read("theorems/theorems.jsonl")}
    known.update(row["id"] for row in read("corpus/bibliography.jsonl"))
    admitted = {row.get("id") or row.get("paper_id") for row in read(LUECKING_SHARD)}
    if LUECKING not in admitted:
        raise ValueError("Luecking context requires the separately admitted bibliography record")
    known.update(admitted | {HADAMARD, MANGOLDT_PSI})
    refs = {row[key] for row in PROOFS for key in ("from", "to")}
    refs.update(ident for start, end, *_ in BOUNDARIES for ident in (start, end))
    refs.update(ident for row in CONNECTIONS for ident in row["source_theorems"])
    if len(claims) != len(CLAIMS) or refs - known:
        raise ValueError(f"Duplicate claims or unresolved source references: {sorted(refs - known)}")
    prior_connections = {row["id"] for row in read("connections/connections.jsonl")}
    if missing := STATE_UPDATES.keys() - prior_connections:
        raise ValueError(f"Unknown connection status targets: {sorted(missing)}")

    groups = {row["id"]: row for row in read(GROUPS_FILE)}
    for ident, title, note, reviews in GROUPS:
        group_id = "REVIEW-GROUP-R16-" + ident
        groups[group_id] = dict(id=group_id, title=title, status=SCOPED, director_adjudication=note,
                                independent_reviews=[REVIEWS + name for name in reviews])
    updates = {row["id"]: row for row in read(CONNECTION_UPDATES)}
    for ident, fields in STATE_UPDATES.items():
        updates[ident] = dict(id=ident, evidence=MELLIN,
                              fields=dict(updates.get(ident, {}).get("fields", {}), **fields))
    shards = {
        "theorems/research_round16_claims.jsonl": CLAIMS,
        "theorems/research_round16_proof_edges.jsonl": PROOFS,
        "graphs/research_round16_boundaries.jsonl": [
            dict(record_type="edge", relation=relation, provenance=note,
                 status=SCOPED, **{"from": start, "to": end})
            for start, end, relation, note in BOUNDARIES
        ],
        "connections/research_round16_connections.jsonl": CONNECTIONS,
    }
    for path, rows in shards.items():
        write(path, rows)
    write(GROUPS_FILE, groups.values())
    write(CONNECTION_UPDATES, updates.values())
    print(json.dumps(dict(staged_shards={path: len(rows) for path, rows in shards.items()},
                          scoped_groups=len(GROUPS), later_connection_updates=len(STATE_UPDATES)), indent=2))


if __name__ == "__main__":
    main()
