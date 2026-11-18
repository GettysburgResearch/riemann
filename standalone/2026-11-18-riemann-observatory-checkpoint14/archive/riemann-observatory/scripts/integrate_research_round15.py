#!/usr/bin/env python3
"""Write the adjudicated Round 15 research shards and reviewed-group entries."""
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDITS = "audits/adversarial_reviews/"
ENDPOINT = AUDITS + "director_critical_endpoint_round15.md"
MELLIN = AUDITS + "director_mellin_explicit_formula_round15.md"
LONG = AUDITS + "director_long_prime_round15.md"
ABEL = AUDITS + "director_explicit_abel_round15.md"
MORSE = AUDITS + "director_morse_scoped_round15.md"
MORSE_PAPER = "PAPER-LAG2009-MORSE"
MORSE_SOURCES = [
    dict(version="arXiv:0712.3238v6, 2009-08-18",
         source_path="sources/prefix_skeptic62_spectral/lagarias_morse.pdf",
         source_sha256="307d253d70abc7d8ef3d24355e9ab7708010bda18c7b9060a4913033c6e224be"),
    dict(version="2009 journal, CNTP 3(2), 323–361, DOI 10.4310/CNTP.2009.v3.n2.a3",
         source_path="sources/geometry120_morse_references/lagarias_morse_journal.pdf",
         source_sha256="268dff410dae549b457c45375007922e91cc8b9b7e23530814044d42bb54b280"),
]
GROUP_LEDGER = "audits/reviewed_claim_groups.jsonl"
BL = "PAPER-L002"
BL_PDF = "sources/uniform121_bombieri_lagarias/bombieri_lagarias_author.pdf"
BL_HASH = "cd13c8560f961c68e21256e5ba107bdd08fa7f34ce1e2cffbd4b63a16e8d48e0"
BL_VERSION = "Michigan author-hosted 12-page manuscript, version date unverified"
FIORI = "PAPER-P122-FIORI-JASKARI-PNT"
GONEK = "PAPER-LF63-GONEK1984"
RVM = "PAPER-GEO82-MANGOLDT1905"
PASCADI = "sources/prime117_references/pascadi.pdf"
PASCADI_REF = "EXT-PASCADI-DEF-1.1-THM-1.3-I"
SOURCE_SHARD = "papers/round15_dependency_records.jsonl"
SOURCE_RECEIPT = "quality/round15_dependency_admission_receipt.json"
CSTAR = "OPEN-HLZ-PURE-FOURTH-CSTAR-CANCELLATION"
PRIME_WINDOWS = "LEM-CSTAR-GCD-RESOLVED-INVERSE-PRIME-WINDOWS"
SCOPED = "adjudicated_scoped"

RAW = "OBS-BL-RAW-HEIGHT-SMOOTH-COUNTEREXAMPLE"
SOBOLEV = "THM-MELLIN-STRIP-SOBOLEV-ZERO-TRACE"
CRITICAL = "THM-MELLIN-CRITICAL-LOG-ZERO-TRACE"
STRICT = "OBS-MELLIN-CRITICAL-LOG-SMOOTH-STRICT-INCLUSION"
CUTOFF = "LEM-BL-FINITE-CUTOFF-COMPENSATOR"
ARRAY = "OBS-CSTAR-LONG-PRIME-PROGRESSION-NORM-COUNTERMODEL"
SQUARE = "OPEN-CSTAR-LONG-PRIME-MOVING-PHASE-SQUARE"
PADDED = "THM-PRIME-PRODUCT-EXACT-PADDED-FACTORABILITY"
ABOUND = "LEM-GONEK-EXPLICIT-ABEL-PRIME-SUBSTITUTION"

LOG_END = "OBS-MELLIN-CRITICAL-LOG-ENDPOINT-ABSOLUTE-DIVERGENCE"
MORSE_SHIFT = "OBS-MORSE-PRINTED-SHIFTED-FAMILY-SELF-REFLECTION"
MORSE_QUOTIENT = "OBS-MORSE-PRINTED-HERGLOTZ-QUOTIENT-SIGN"

RAW_SECTION = "A fixed smooth witness for which the stated height limit fails"
SOBOLEV_SECTION = "A sufficient strip-Sobolev condition"
LOG_SECTION = "A weaker critical logarithmic class"
CUTOFF_SECTION = "A separate finite-cutoff identity and why the main theorem survives"
ARRAY_SECTION = "An exact limitation of two progression norms"
SQUARE_SECTION = "The exact prime form"
PADDED_SECTION = "Exact padded factorability"
ABEL_SECTION = "Uniform Abel estimate"


def read(path):
    return [json.loads(line) for line in (ROOT / path).read_text().splitlines() if line.strip()]


def write(path, rows):
    (ROOT / path).write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows))


def digest(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def claim(ident, note, section, statement, hypotheses, kind, *, sources=(), status=SCOPED):
    row = dict(id=ident, paper_id=None, locator=note + " · " + section, evidence=note,
               statement=statement, hypotheses=hypotheses, claim_kind=kind,
               status=status, novelty_claim=False)
    if sources:
        row["related_paper_ids"] = list(sources)
    return row


CLAIMS = [
    claim(RAW, MELLIN, RAW_SECTION,
          "There exists a fixed smooth real f satisfying the pinned manuscript's literal endpoint and local hypotheses whose zero sum fails under symmetric raw-height cutoffs. Disjoint log-coordinate bumps with amplitudes a_j=exp(−(1/2+δ)j), b_j=exp(−(1+δ)j), and separated high-frequency carriers produce symmetric height increments exceeding 2j/5. The arithmetic side has ordinary absolute convergence.",
          "Nontrivial zeta zeros with multiplicity, actual unaveraged cutoffs |Im ρ|≤T, and the auxiliary formula on pinned manuscript pp. 5–6. Uses the unconditional zero count in populated high cells. The compact jump tests in the main theorem have a separate justification.",
          "intrinsic_smooth_raw_height_counterexample", sources=(BL,)),
    claim(SOBOLEV, MELLIN, SOBOLEV_SECTION,
          "For h(s)=∫₀∞ f(x)x^(s−1)dx and N_s² the strip area integral of |h(β+it)|²(1+t²)^s, the zero trace is absolutely summable. With r=min(ε/2,1/4), its ℓ¹ bound is C_N/(√π r) times [2·5^s Σ_n log²(2+|n|)/(1+n²)^s]^(1/2) N_s. Restricting the series to |n|>T−1 gives tail O(N_s T^(1/2−s) log(2+T)). The compensated explicit formula follows by compact smooth approximation, with automatic central trace control.",
          "Continuous f with the original endpoint value bounds at margin δ>0, 0<ε<δ, finite norm on β∈[−ε,1+ε], s>1/2. C_N bounds the number of zeta zeros with n≤Im ρ<n+1 by C_N log(2+|n|), including multiplicities.",
          "sufficient_absolute_zero_trace_and_explicit_formula", sources=(BL,)),
    claim(CRITICAL, MELLIN, LOG_SECTION,
          "Replacing the strip weight by w_p(t)=√(1+t²) log^p(e+|t|) gives an absolute zero trace, with tail O(N_log,p [log(2+T)]^((3−p)/2)). Fourier inversion on the central line gives the Dini modulus O(N_log,p [log(e/|u|)]^((1−p)/2)) near u=0. Approximation establishes the same compensated explicit formula.",
          "Continuous f with the original endpoint value bounds, strip margin 0<ε<δ, and finite area norm with p>3. The endpoint claim separately addresses failure of universal absolute sampling at p=3.",
          "sufficient_critical_logarithmic_zero_trace_and_explicit_formula", sources=(BL,)),
    claim(STRICT, MELLIN, LOG_SECTION,
          "For each p>3 a smooth real example lies in the critical-log strip class and in none of the polynomial strip classes with s>1/2. Use disjoint log bumps at j, carrier Γ_j=2^(j²), and amplitudes Γ_j^(−1/2) log^(−p/2)(e+Γ_j) j^(−2)e^(−2j) in x^(−1/2) times the log-coordinate series. Uniform carrier lower bounds give divergence of every heavier polynomial norm.",
          "Fixed ε=1/4 and fixed nonnegative smooth compact bump. The value is O(x^(−2)) as x→∞ and vanishes for x near zero. This example concerns strict class inclusion and has absolute zero trace.",
          "smooth_strict_inclusion_of_mellin_trace_classes"),
    claim(CUTOFF, MELLIN, CUTOFF_SECTION,
          "In pinned manuscript p. 8 equation (3.5), the finite-cutoff equality requires the additive gamma-compensator term n∫_(1/ε)^∞ dx/[x(x²−1)] = −(n/2)log(1−ε²). For n=1 and ε=2/3 the missing positive term is (1/2)log(9/5). The term tends to zero at O_n(ε²), and the compact jump formula with midpoint values gives the main limiting identity.",
          "Exact finite equality in the pinned author manuscript, with the manuscript's jump convention. The witness cutoff 3/2 avoids prime powers. This calculation concerns the finite formula and its true limit.",
          "exact_finite_cutoff_correction", sources=(BL,)),
    claim(ARRAY, LONG, ARRAY_SECTION,
          "On true supported squarefree four-prime moduli k≈K at P=KT, a nonnegative centered row model satisfies Σ_k max_u|E_(k,u)|≪√(PS) and Σ_(k,u)* |E_(k,u)|²≈PK, where S≈K/log⁴T. Its h=1 real projection with coefficients a_k/k is (12+o(1))√(PS), exceeding T log⁴T by a divergent factor. The common-divisor CRT marginals differ at 1 for two moduli gv₁ and gv₂, excluding a single common unit-supported sequence.",
          "Fixed 1/8<b<1/6, K≈Y^(4b), T≈Y, and all four distinct factors in one fixed near-top multiplicative prime band. This is an abstract implication countermodel; it gives no lower bound for genuine primes.",
          "abstract_phase_blind_norm_countermodel"),
    claim(SQUARE, LONG, SQUARE_SECTION,
          "A sufficient open target on each residual block is Σ_(k≈K,h≈D)|Σ_(p≈P,(p,k)=1)(log p)³p^(−it)[e(−hp/k)−μ(q)/φ(q)]|²≪T^(2−η)K/D with q=k/(h,k), uniformly for |t|≤T^ε and some fixed η>0. Cauchy–Schwarz costs O(T^ε√(D/K)) and the Mellin integral costs O(T^(1−κ)).",
          "T≈Y, DP≈KT, a_k≤24, cutoff H=T^κ with κ sufficiently near one, and 1−κ+ε<η/2 with strict margin. The k-sum may be restricted to actual modulus support. All divisor gcds are retained. No square estimate on genuine primes is claimed.",
          "open_sufficient_moving_phase_target", status="open_sufficient_target"),
    claim(PADDED, LONG, PADDED_SECTION,
          "For the full ordered m-prime coefficient c_m/m! from a finite nonempty set with largest prime p_*, the exact r-way 1-bounded well-factorable level is p_*^(m+r−1). Completely multiplicative |g|≤1 preserves sufficiency and preserves necessity if g(p_*)≠0. For m=4,r=3 the padded Y^(6b) level fits Pascadi's longest-block fixed-residue exponent 5/8 with a strict margin when b<5/28.",
          "Integers m,r≥1, and every prescribed real split Q=∏Q_i with Q_i≥1. The sequence is untruncated. The comparison to Pascadi uses x≈Y^(1+4b) and fixed nonzero residue; no sharp-shell factorability or varying-residue conclusion follows.",
          "intrinsic_exact_padded_factorability"),
    claim(ABOUND, ABEL, ABEL_SECTION,
          "Let A_m be the difference between Σ_(n≤x) Λ(n)n^(iδ−1)log^m(x/n) and ∫₁ˣu^(iδ−1)log^m(x/u)du. With L=log x and K=|Im δ|L it is bounded by L^m+4e^K 1_(m=0)+20e^K|iδ−1|L^m+20m e^K L^(m−1). For real |δ|≤1/2 a common bound is 31L^m+20mL^(m−1).",
          "Real x>1, integer m≥0, complex δ; omit the final term for m=0 and take the zeroth log power to be one. The right endpoint includes prime-power jumps. Uses Fiori–Jaskari v2 unconditionally for the absolute PNT error bounds r≤4 and ∫r(u)du/u<20. This is one substitution in Gonek Lemma 8.",
          "unconditional_explicit_abel_substitution", sources=(FIORI, GONEK)),
    claim(LOG_END, ENDPOINT, "Exact assertion",
          "A real smooth f vanishing near zero and one and satisfying f(x)=O(x^(−4)) has finite Mellin area norm on β∈[−1/4,5/4] with weight √(1+t²) log³(e+|t|), yet Σ_ρ|h(ρ)| diverges. Every realization of the disjoint finite-carrier packet signs has finite norm, and divergence holds for almost every independent symmetric sign realization.",
          "Actual nontrivial zeta zeros counted with multiplicity, using unconditional Riemann–von Mangoldt counting. The same example excludes universal absolute sampling for p≤3. Signed symmetric height convergence at p=3 remains open.",
          "critical_log_endpoint_counterexample_to_absolute_zero_sampling"),
    claim(MORSE_SHIFT, MORSE, "The nonzero-shift function is self-reflected",
          "The printed E_h=(P+Q)/2−i(P−Q)/(2h), where P(z)=ξ(1/2−iz+h) and Q(z)=ξ(1/2−iz−h), equals its Schwarz reflection for every real h≠0 because P#=Q and Q#=P. Thus h=1/2,z=i already gives equality in the absolute values required to be strictly ordered by (5.1). The local limit of the printed family is ξ−iξ′.",
          "The display immediately preceding (5.5) in the pinned arXiv v6 and journal versions. The separately defined h=0 function and the fixed-boundary spectral results are outside this claim.",
          "exact_source_local_hermite_biehler_counterexample", sources=(MORSE_PAPER,)),
    claim(MORSE_QUOTIENT, MORSE, "The explicit quotient has the opposite Herglotz sign",
          "At z=i and x=e^u, the printed quotient (6.2) is −i exp(−x)/(1+x), so u=0 gives −i/(2e). Its imaginary part is strictly negative. With the printed decomposition E=A−iB, the compatible Herglotz quotient is +B/A.",
          "Equation (6.2) and the positive-imaginary convention in the pinned arXiv v6 and journal versions. This is an auxiliary quotient in the z variable. The Appendix B Weyl–Titchmarsh quotient uses energy E=z² and has its own sign.",
          "exact_source_local_herglotz_sign_counterexample", sources=(MORSE_PAPER,)),
]

DEPENDENCIES = [
    (RAW, BL, MELLIN), (SOBOLEV, BL, MELLIN), (CRITICAL, SOBOLEV, MELLIN),
    (STRICT, CRITICAL, MELLIN), (CUTOFF, BL, MELLIN),
    (ARRAY, CSTAR, LONG), (SQUARE, CSTAR, LONG), (SQUARE, PRIME_WINDOWS, LONG),
    (ABOUND, FIORI, ABEL), (ABOUND, GONEK, ABEL),
    (MORSE_SHIFT, MORSE_PAPER, MORSE), (MORSE_QUOTIENT, MORSE_PAPER, MORSE),
]

SOURCE_PROOF_EDGES = [
    dict(locator="von Mangoldt (1905), Riemann–von Mangoldt counting asymptotic",
         evidence=ENDPOINT, relation="uses_unconditional_dyadic_zero_count",
         status=SCOPED, **{"from": LOG_END, "to": RVM}),
    dict(locator=PASCADI + " · p. 2, Definition 1.1 and Theorem 1.3(i)",
         evidence=LONG, relation="uses_factorability_definition_and_fixed_residue_range",
         status=SCOPED, **{"from": PADDED, "to": PASCADI_REF}),
]

BOUNDARIES = [
    (SOBOLEV, RAW, "gives_sufficient_hypothesis_excluding_raw_height_failure", MELLIN),
    (STRICT, SOBOLEV, "exhibits_strict_inclusion_at_fixed_strip", MELLIN),
    (LOG_END, CRITICAL, "shows_sharp_range_for_universal_absolute_sampling_only", ENDPOINT),
    (CUTOFF, BL, "corrects_finite_manuscript_equality_with_vanishing_term", MELLIN),
    (ARRAY, SQUARE, "separates_abstract_norms_from_common_sequence_phase_target", LONG),
    (PADDED, SQUARE, "weight_condition_alone_leaves_varying_phase_open", LONG),
    (SQUARE, CSTAR, "sufficient_input_leaves_cancellation_open", LONG),
    (ABOUND, GONEK, "quantifies_one_abel_step_only", ABEL),
    (MORSE_SHIFT, MORSE_PAPER, "limits_finding_to_printed_nonzero_shift_family", MORSE),
    (MORSE_QUOTIENT, MORSE_PAPER, "limits_finding_to_auxiliary_z_quotient", MORSE),
]

MELLIN_FINAL = "analytic138_director_mellin_final_qa.md"
RAW_REVIEWS = [
    "geometry130_explicit_formula_countermodel.md",
    "weighted130_explicit_formula_countermodel_review.md",
    "analytic131_explicit_formula_countermodel_adjudication.md",
    MELLIN_FINAL,
]
CUTOFF_REVIEWS = [
    "uniform121_bombieri_lagarias_whole_advocate.md",
    "weighted121_bombieri_lagarias_whole_skeptic.md",
    "geometry127_bombieri_lagarias_adjudication_input.md",
    MELLIN_FINAL,
]
MORSE_REVIEWS = [
    "geometry120_lagarias_morse_whole_advocate.md",
    "analytic120_lagarias_morse_whole_skeptic.md",
    "weighted128_morse_conventions_adjudication.md",
    "geometry138_morse_local_findings.md",
]
GROUPS = [
    ("BL-RAW-HEIGHT", "Fixed smooth witness against the manuscript's literal raw-height formula", MELLIN, RAW_REVIEWS),
    ("MELLIN-SOBOLEV", "Strip Sobolev zero trace and compensated formula", MELLIN,
     ["analytic132_mellin_trace_repair.md", "weighted132_mellin_trace_repair_review.md",
      "uniform133_mellin_repair_adjudication.md", MELLIN_FINAL]),
    ("MELLIN-CRITICAL-LOG", "Critical-log sufficient trace and smooth strict class inclusion", MELLIN,
     ["analytic135_critical_log_mellin_repair.md", "weighted135_critical_log_repair_review.md",
      "uniform136_critical_log_adjudication.md", MELLIN_FINAL]),
    ("BL-FINITE-CUTOFF", "Finite gamma-compensator correction for the pinned author manuscript", MELLIN, CUTOFF_REVIEWS),
    ("CSTAR-LONG-PRIME", "Moving-phase target and progression-norm countermodel", LONG,
     ["prime117_long_prime_obstacle.md", "weighted119_blackbox_phase_review.md",
      "analytic129_long_prime_adjudication.md", "release140_long_prime_final_qa.md"]),
    ("PRIME-PRODUCT-FACTORABILITY", "Exact padded level of full prime-product coefficient", LONG,
     ["prime137_padded_factorability.md", "geometry137_padded_factorability_review.md",
      "release140_long_prime_final_qa.md"]),
    ("GONEK-ABEL", "Explicit uniform prime-to-integral substitution", ABEL,
     ["prime126_explicit_abel_constant.md", "weighted134_explicit_abel_review.md",
      "prime140_director_abel_qa.md"]),
    ("MELLIN-CRITICAL-ENDPOINT", "Critical-log p=3 fails for absolute zero sampling", ENDPOINT,
     ["weighted138_critical_endpoint_campaign.md", "analytic139_critical_endpoint_adversarial.md",
      "geometry141_critical_endpoint_adjudication.md"]),
    ("MORSE-LOCAL", "Two exact auxiliary contradictions in both pinned Morse manifestations", MORSE, MORSE_REVIEWS),
]


CLAIM_LOCATORS = {row["id"]: row["locator"] for row in CLAIMS}
CLAIM_LOCATORS.update({
    BL: BL_PDF + " · pp. 5–6 and p. 8, (3.5)",
    CSTAR: "audits/adversarial_reviews/prime98_fixed_arithmetic_sequence.md",
    PRIME_WINDOWS: AUDITS + "director_arithmetic_strata_round14.md · Divisor Voronoi and averaged inverse-prime bounds",
    FIORI: "arXiv:2609.23222v2 · Theorem 1.1/table p. 4, Theorem 5.2 p. 44, §5.1 p. 45",
    GONEK: AUDITS + "director_gonek_whole_round15.md · 1984 journal Lemma 8",
    RVM: "von Mangoldt (1905), zero-counting asymptotic as used in " + ENDPOINT,
})


def connection(ident, note, sources, statement, hypotheses, proved, conjectural, next_step, tests,
               failures, significance, difficulty, *, extra_locators=()):
    source_claims = [dict(id=source, locator=CLAIM_LOCATORS[source]) for source in sources]
    source_claims.extend(dict(locator=locator) for locator in extra_locators)
    return dict(id=ident, sources=sources, statement=statement, hypotheses=hypotheses,
                already_proved=proved, conjectural=conjectural, next_step=next_step,
                source_theorems=sources, source_claims=source_claims,
                compatible_assumptions=hypotheses, new_claim_suggested=conjectural,
                conjectural_or_unresolved=conjectural, next_precise_step=next_step,
                potential_counterexamples=failures, significance=significance, difficulty=difficulty,
                tests=tests, status=SCOPED, evidence=note, novelty_claim=False)


CONNECTIONS = [
    connection("CONN-MELLIN-RAW-HEIGHT-AND-STRIP-TRACE", MELLIN,
               [BL, RAW, SOBOLEV, CRITICAL, STRICT, CUTOFF],
               "The auxiliary raw-height assertion can fail for a smooth function. Two sufficient area-norm hypotheses give absolute traces and ordinary compensated formulas, and the finite cutoff has a separate correction.",
               "Pinned author manuscript for both source findings; continuous functions with the stated value and strip hypotheses for the repairs.",
               "Counterexample, two sufficient trace classes, smooth strict inclusion, and exact finite compensator.",
               "Signed symmetric convergence at the logarithmic endpoint.",
               "Study weaker trace hypotheses and the structure of the central compensation.",
               "Populated zero cells, disk mean values, Dini control, Fourier carrier estimates, and exact finite integration.",
               "The literal value and local bounds already allow the smooth raw-height failure. The compact jump tests lie outside the strip repairs.",
               "Validates a precise test class and an explicit truncation error for zero-trace calculations.",
               "Moderate for sufficiency using standard analytic estimates. The signed endpoint requires further control."),
    connection("CONN-MELLIN-CRITICAL-LOG-ABSOLUTE-ENDPOINT", ENDPOINT,
               [CRITICAL, LOG_END, RVM],
               "Universal absolute zero sampling holds for p>3 and fails at p=3 and below in the stated logarithmic scale.",
               "Original endpoint value bounds, logarithmically weighted strip area norm and actual nontrivial zeros with multiplicity.",
               "Sufficient p>3 repair and a smooth p=3 absolute-trace counterexample.",
               "Signed symmetric raw-height convergence at p=3.",
               "Test signed height convergence, which absolute divergence alone does not decide.",
               "Weighted synthesis, dyadic zero counts, two probability bounds and a tail zero–one law.",
               "The finite-norm p=3 example rules out a universal absolute trace, including all weaker p≤3 weights in this scale.",
               "Identifies the exact threshold for universal absolute sampling in this logarithmic family.",
               "The absolute endpoint uses a probabilistic construction. A signed example or convergence proof remains substantial."),
    connection("CONN-CSTAR-LONG-PRIME-PHASE-AND-COMPATIBILITY", LONG,
               [CSTAR, PRIME_WINDOWS, ARRAY, SQUARE],
               "A Mellin representation isolates a genuine moving additive phase. Abstract row-wise progression norms do not control it without further structure.",
               "Remaining genuine-prime blocks, coprime prime factor, exact divisor gcd, and compact taper.",
               "Sufficiency of the square target and a norm-only countermodel with inconsistent CRT marginals.",
               "A bound for genuine primes in the required moving Fourier mode.",
               "Estimate the square or the prescribed signed projection using common-sequence structure.",
               "Mellin inversion, Cauchy–Schwarz, row variance and common-divisor CRT marginals.",
               "Positive centered rows with small maximum errors and ideal variance can carry a large phase projection. The row model fails the compatibility test for a common sequence.",
               "Separates established prime windows from the remaining long-prime step in the fourth-moment reduction.",
               "High. The target requires cancellation in a phase coupled to both modulus and divisor index."),
    connection("CONN-CSTAR-PADDED-WEIGHT-AND-FIXED-RESIDUE", LONG,
               [PADDED, SQUARE],
               "The complete prime-product coefficient meets a padded factorability condition in the longest-block range. The phase target needs simultaneous varying residues.",
               "Full normalized prime-product coefficient and Pascadi's fixed-residue setting at the padded level.",
               "Exact minimal level and the longest-block exponent comparison.",
               "Control of the signed moving phase with the genuinely supported moduli.",
               "Look for arithmetic inputs that retain the residue Fourier mode.",
               "Integer allocation over every split and a prescribed split excluding the top prime power.",
               "An insufficient prescribed split excludes the top prime power. Neither hard dyadic restriction nor the moving residue phase is covered by the factorization proof.",
               "Settles the precise coefficient-level obstruction and locates the remaining phase restriction.",
               "Elementary for the exact factorability. High for an applicable signed phase estimate.",
               extra_locators=(PASCADI + " · p. 2, Definition 1.1 and Theorem 1.3(i)",)),
    connection("CONN-GONEK-FIORI-EXPLICIT-ABEL-INPUT", ABEL,
               [FIORI, GONEK, ABOUND],
               "The unconditional absolute PNT error gives a uniform explicit bound for the prime-to-integral step in Gonek Lemma 8.",
               "Pinned versions with Stieltjes upper endpoint included and finite-interval complex-shift control.",
               "Explicit real and complex Abel bounds.",
               "Numerical constants for the rest of the weighted derivative-tail argument.",
               "Allocate constants to the remaining divisor, contour and tail estimates.",
               "Absolute error integration and two independent Stieltjes calculations.",
               "For negative imaginary shifts the factor u^(−Im δ) must be bounded on the finite interval before integrating the remaining error to infinity.",
               "Supplies an explicit constant for one reusable step in the derivative-moment proof.",
               "Direct for the Abel step. A full numerical onset requires separate divisor, contour and tail constants."),
]


def finding(ident, title, locator, related_claim, reviews, witness, scope):
    return dict(id=ident, title=title, classification="Verified mathematical error",
                status="adjudicated_exact_manuscript_counterexample_and_repair",
                sources=[BL], related_claim_ids=[related_claim], evidence=MELLIN,
                director_adjudication=MELLIN, independent_reviews=[AUDITS + review for review in reviews],
                verified_author_error=True, version=BL_VERSION, source_path=BL_PDF,
                source_sha256=BL_HASH, source_locator=locator, explicit_witness=witness, scope=scope)


FINDINGS = [
    finding("FIND-R15-BL-RAW-HEIGHT-TEST-CLASS",
            "The manuscript's literal auxiliary test class allows a divergent raw-height sum",
            "Pinned 12-page author manuscript, pp. 5–6, auxiliary explicit formula and test-function conditions.",
            RAW, RAW_REVIEWS,
            "A fixed smooth disjoint log-bump function obeys the literal value and local hypotheses. Populated symmetric high zero cells and separated carriers force increments greater than 2j/5 under raw-height summation while the arithmetic side converges absolutely.",
            "Pinned author-hosted manuscript only. The auxiliary formula needs stronger hypotheses for the stated summation mode. The generalized multiset criterion and the compact main application retain separate proofs. No journal-version finding."),
    finding("FIND-R15-BL-FINITE-CUTOFF-COMPENSATOR",
            "The printed finite-cutoff equality loses its upper-tail compensator",
            "Pinned 12-page author manuscript, p. 8, equation (3.5).",
            CUTOFF, CUTOFF_REVIEWS,
            "At n=1 and ε=2/3 the gamma compensator contributes an omitted positive (1/2)log(9/5). The cutoff 3/2 is distinct from every prime power.",
            "Pinned author-hosted manuscript only. The omitted term is O_n(ε²) and vanishes in the limiting theorem. No journal-version finding."),
]


def morse_finding(ident, title, v6_locator, journal_locator, related_claim, witness, scope):
    return dict(id=ident, title=title, classification="Verified mathematical error",
                status="adjudicated_exact_versioned_local_counterexample_and_repair",
                sources=[MORSE_PAPER], related_claim_ids=[related_claim], evidence=MORSE,
                director_adjudication=MORSE,
                independent_reviews=[AUDITS + review for review in MORSE_REVIEWS],
                verified_author_error=True,
                version=MORSE_SOURCES[0]["version"], source_sha256=MORSE_SOURCES[0]["source_sha256"],
                source_manifestations=[
                    dict(MORSE_SOURCES[0], source_locator=v6_locator),
                    dict(MORSE_SOURCES[1], source_locator=journal_locator),
                ],
                source_locator=v6_locator + " " + journal_locator,
                explicit_witness=witness, scope=scope)


MORSE_FINDINGS = [
    morse_finding("FIND-R15-MORSE-SHIFTED-FAMILY-SELF-REFLECTION",
                  "The displayed shifted family is self-reflected",
                  "ArXiv v6 p. 20, display before (5.5) and its attached assertion, with (5.1) on p. 19.",
                  "Journal printed pp. 344 and 346, PDF pp. 22 and 24.",
                  MORSE_SHIFT,
                  "Reflection exchanges P and Q and conjugates −i, so the displayed E_h#=E_h and the strict Hermite–Biehler inequality fails at h=1/2,z=i.",
                  "The nonzero-shift display and its attached claim. The separately defined zero-shift criterion and cited single-shift result retain their own arguments."),
    morse_finding("FIND-R15-MORSE-EXPLICIT-HERGLOTZ-QUOTIENT-SIGN",
                  "The explicit Herglotz quotient has negative imaginary part",
                  "ArXiv v6 p. 23, (6.1)–(6.2), with decomposition on p. 19.",
                  "Journal printed pp. 344 and 349, PDF pp. 22 and 27.",
                  MORSE_QUOTIENT,
                  "Whittaker evenness and the integral for U give U(1,3,x)=x⁻¹+x⁻² and U(2,3,x)=x⁻². At u=0,z=i the printed equation evaluates to −i/(2e).",
                  "The auxiliary z-plane quotient and its stated Herglotz convention. The fixed-boundary spectral theorems and Appendix B energy-plane Weyl quotient retain their separate arguments."),
]


def main():
    required = {MELLIN, LONG, ABEL, MORSE, ENDPOINT, BL_PDF, SOURCE_SHARD, SOURCE_RECEIPT, GROUP_LEDGER,
                "theorems/theorems.jsonl", "corpus/bibliography.jsonl",
                PASCADI}
    required.update(source["source_path"] for source in MORSE_SOURCES)
    required.update(AUDITS + name for _, _, _, reviews in GROUPS for name in reviews)
    for path in sorted(required):
        if not (ROOT / path).is_file():
            raise FileNotFoundError(path)

    bibliography = {row["id"]: row for row in read("corpus/bibliography.jsonl")}
    receipt = json.loads((ROOT / SOURCE_RECEIPT).read_text())
    admitted = {row.get("id") or row.get("paper_id") for row in read(SOURCE_SHARD)}
    if FIORI not in admitted or FIORI not in receipt["ids"] or receipt["admitted_shard"] != SOURCE_SHARD:
        raise ValueError("Missing Fiori–Jaskari source admission")
    if digest(SOURCE_SHARD) != receipt["admitted_shard_sha256"]:
        raise ValueError("Round 15 source shard differs from its admission receipt")
    if digest(BL_PDF) != BL_HASH or BL not in bibliography:
        raise ValueError("Missing or changed pinned Bombieri–Lagarias manuscript")
    for source in MORSE_SOURCES:
        if digest(source["source_path"]) != source["source_sha256"]:
            raise ValueError(f"Changed pinned Morse manifestation: {source['source_path']}")
    claim_ids = {row["id"] for row in CLAIMS}
    if len(claim_ids) != len(CLAIMS):
        raise ValueError("Duplicate Round 15 claim ID")
    paper_ids = set(bibliography) | admitted
    known = paper_ids | claim_ids | {row["id"] for row in read("theorems/theorems.jsonl")}
    endpoints = {ident for start, end, *_ in DEPENDENCIES + BOUNDARIES for ident in (start, end)}
    endpoints.update(ident for row in CONNECTIONS for ident in row["sources"])
    endpoints.update(row[key] for row in SOURCE_PROOF_EDGES for key in ("from", "to"))
    known.add(PASCADI_REF)
    if not endpoints <= known:
        raise ValueError(f"Unknown Round 15 endpoints: {sorted(endpoints - known)}")

    shards = {
        "theorems/research_round15_claims.jsonl": CLAIMS,
        "theorems/research_round15_proof_edges.jsonl": [
            dict(locator=note, evidence=note, relation="uses_exact_scoped_input",
                 status=SCOPED, **{"from": start, "to": end})
            for start, end, note in DEPENDENCIES
        ] + SOURCE_PROOF_EDGES,
        "graphs/research_round15_boundaries.jsonl": [
            dict(record_type="edge", relation=relation, provenance=note,
                 status=SCOPED, **{"from": start, "to": end})
            for start, end, relation, note in BOUNDARIES
        ],
        "connections/research_round15_connections.jsonl": CONNECTIONS,
        "audits/research_round15_bombieri_lagarias_findings.jsonl": FINDINGS,
        "audits/research_round15_morse_findings.jsonl": MORSE_FINDINGS,
    }
    groups = {row["id"]: row for row in read(GROUP_LEDGER)}
    for ident, title, note, reviews in GROUPS:
        group_id = "REVIEW-GROUP-R15-" + ident
        groups[group_id] = dict(id=group_id, title=title, status=SCOPED,
                                director_adjudication=note,
                                independent_reviews=[AUDITS + name for name in reviews])
    for path, rows in shards.items():
        write(path, rows)
    write(GROUP_LEDGER, groups.values())
    print(json.dumps(dict(staged_shards={name: len(rows) for name, rows in shards.items()},
                          scoped_groups=len(GROUPS), claim_ids=sorted(claim_ids)), indent=2))


if __name__ == "__main__":
    main()
