#!/usr/bin/env python3
"""Stage the scoped, director-adjudicated Round 14 research records."""
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDITS = "audits/adversarial_reviews/"
RMT = AUDITS + "director_quantitative_rmt_round14.md"
ARITH = AUDITS + "director_arithmetic_strata_round14.md"
CERT = "experiments/results/geometry111_rankone_hankel_certificate.json"
SOURCE_SHARD = "papers/round14_dependency_records.jsonl"
GROUP_LEDGER = "audits/reviewed_claim_groups.jsonl"
SCOPED = "adjudicated_scoped"

BAKER = "PAPER-R112-BAKER2012"
BHM = "PAPER-R112-BHM2007"
GHOSH = "PAPER-WEIGHTED107-GHOSH-THESIS1981"
REN = "PAPER-WEIGHTED107-REN2005"
KOROLEV = "PAPER-WEIGHTED107-KOROLEV2018"
FS = "PAPER-R114-FOUVRY-SHPARLINSKI2011"
PETROV = "PAPER-GEOMETRY102-PETROV2026"
BARRIER = "OBS-ROOTED-CUE-ALL-RANK-FINITE-SQUARE-BARRIER"
EXACT_BRIDGE = "LEM-PETROV-ROOTED-CUE-EXACT-FACTOR-BRIDGE"
QUADRATIC_GAP = "OBS-PETROV-ROOTED-CUE-GRAM-QUADRATIC-MISMATCH"
CSTAR = "LEM-HLZ-REFLECTED-EDGE-FIXED-SEQUENCE"
OPEN_CSTAR = "OPEN-HLZ-PURE-FOURTH-CSTAR-CANCELLATION"

HANKEL = "THM-ROOTED-CUE-HANKEL-WITNESS-DEGREE-BOUND"
HERMITE = "THM-ROOTED-CUE-RANK-ONE-HERMITE-WITNESS"
FIXTURES = "CERT-ROOTED-CUE-RANK-ONE-HANKEL-FIXTURES"
SCHUR = "LEM-PETROV-ROOTED-CUE-FINITE-SCHUR-TAIL"
GRAM = "THM-PETROV-ROOTED-CUE-TRUE-CUTOFF-CONTINUUM-GRAM"
TRUNCATE = "LEM-PETROV-ROOTED-CUE-FACTORIAL-HANKEL-TRUNCATION"
MODULUS = "LEM-CSTAR-EFFECTIVE-MODULUS-AND-SHORT-FACTOR"
POWERS = "LEM-CSTAR-SHARED-FACTORS-AND-HIGHER-POWERS"
SQUARES = "LEM-CSTAR-ALL-PRIME-SQUARES-BELOW-9-17"
PRIME_WINDOW = "LEM-CSTAR-GCD-RESOLVED-INVERSE-PRIME-WINDOWS"
ALT_WINDOW = "LEM-CSTAR-KOROLEV-POINTWISE-INVERSE-PRIME-BAND"
ZEROS = "OBS-CSTAR-CHARACTER-TWIST-ZERO-RESIDUES"


def read(path):
    return [json.loads(line) for line in (ROOT / path).read_text().splitlines() if line.strip()]


def write(path, rows):
    (ROOT / path).write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows))


def claim(ident, note, section, statement, hypotheses, kind, *, evidence=None, related_paper_ids=None):
    row = dict(id=ident, paper_id=None, locator=note + " · " + section,
               evidence=evidence or note, statement=statement, hypotheses=hypotheses,
               claim_kind=kind, status=SCOPED, novelty_claim=False)
    if related_paper_ids:
        row["related_paper_ids"] = related_paper_ids
    return row


CLAIMS = [
    claim(HANKEL, RMT, "A quantitative finite witness for every fixed rank",
          "For the formal fixed-rank cosine series M and a real zero 0<t_*≤1/d, let R=2/d and B≥1 majorize |M| on |z|=R. With L=ceil(log_2(8B(B+1))), the two degree-L Taylor polynomials of exp(±t_*x/2) give a strictly negative two-by-two moment determinant. The order-L Hankel form is therefore not positive semidefinite, using moments through degree 2L. A sufficient explicit majorant is B=J! D^J exp((J−1)HR+HR²/4), D=(2J−1)16^(2J−2)(2J−1)! exp(1+R d exp(b)).",
          "Fixed positive integer rank J and 0<a<b<1, H=log(b/a), d=b−a. The form is for the extrapolated cosine series. The bound is sufficient, not generally the least witness order.",
          "intrinsic_quantitative_formal_positivity_obstruction"),
    claim(HERMITE, RMT, "At rank one the least order is known exactly",
          "At rank one set σ²=H/2. The order-L formal Hankel form is congruent to I−(d/σ²)T_L, with Hermite Jacobi edges σ sqrt(k), 1≤k≤L. A negative witness exists exactly when the largest zero of He_(L+1) strictly exceeds σ/d. Equality gives singular positive semidefiniteness. The least order lies above σ²/(4d²) and at most floor(σ²/d²)+1; it is σ²/(4d²)+O(σ/d) as σ/d→infinity.",
          "Fixed positive band at rank one, with the formal Gaussian density modifier 1−d x/σ². He denotes the probabilists' Hermite polynomial. The asymptotic concerns small d/σ, and the criterion does not test the true law outside the supported moment window.",
          "intrinsic_exact_rank_one_formal_witness_degree"),
    claim(FIXTURES, RMT, "At rank one the least order is known exactly",
          "For the standardized series exp(z²/2)(1−z/2), all principal minors through Hankel order two are nonnegative and q(x)=2x³+9x²+6x−3 has formal square expectation −30. At standardized tilt 1/sqrt(3), after rescaling y=sqrt(3)x, the order-two form is singular positive semidefinite, y²+3y is null, and y³+4y²+12y has square expectation −27.",
          "Exact rational formal-moment fixtures with director replay. They check the strict Hermite threshold and are separate from the general degree proof.",
          "exact_rank_one_hankel_certificate", evidence=CERT),
    claim(SCHUR, RMT, "The exact Petrov tail quotient has a positive finite representation",
          "With L=P_nT(φ_+)|P_n, M=U*L^(−*)L^(−1)U and A_n=P_nT(φ)|P_n, the tilted-to-ambient Fredholm ratio is det S, S=M^(−1/2)(U*A_n^(−1)U)M^(−1/2), and det Γ(z)/det Γ(0)=det M. For real z the ratio is in [exp(−H_N z²/4),1]; det M and det(U*A_n^(−1)U) lie in [exp(−J|z|H_N),exp(J|z|H_N)]. The mass-removed complementary determinant has liminf at least exp(−2JH z_*) at any positive formal zero z_*.",
          "Fixed N≥2 and deleted rank J≥1, n=N+J−1, global rooted cosine CUE model, real z, fixed positive band for uniformity in N. No invertibility of Petrov's optional fixed-tail chart is needed.",
          "intrinsic_exact_real_tail_quotient_and_nonvanishing", related_paper_ids=[PETROV]),
    claim(GRAM, RMT, "A true-cutoff continuum Gram and a factorial approximation",
          "For real z≥0, e^(−H_N z)M_ij converges to E[1_(max(p,q)≤1) ∫_(max(p,q))^1 u_i(t−p)u_j(t−q)dt], with independent compound-Poisson shift totals p,q of intensity z dx/(2x) on [a,b] and shifted orthonormal Legendre profiles u_j. For p,q≤1 its kernel differs from the transposed oriented formal kernel by an ordinary lower interval of length min(p,q).",
          "Fixed rank and 0<a<b<1. Exact Gram limit with the finite convolution cutoff. Pure-sign agreement is within the coefficient window; the formal extrapolation can use unsupported shifts.",
          "intrinsic_true_cutoff_continuum_limit", related_paper_ids=[PETROV]),
    claim(TRUNCATE, RMT, "A true-cutoff continuum Gram and a factorial approximation",
          "For h=H(φ_−/φ_+), the Hilbert–Schmidt error after cutting both indices at M_cut≥n is at most |z|sqrt(H_N/2) times ∑_(s≥floor(M_cut/k_*)) (|z|H_N)^s/s!, where k_* is the maximum band index. Schatten Hölder bounds the induced trace-norm K error, and the log-determinant quotient error is at most twice that error divided by exp(−2|z|H_N).",
          "Fixed positive band, fixed deleted rank, real z in a compact interval. A nonempty finite band is required for k_*; an empty band has K=0 and both tails equal one.",
          "intrinsic_uniform_finite_tail_approximation", related_paper_ids=[PETROV]),
    claim(MODULUS, ARITH, "Exact effective modulus and removal of several strata",
          "For fixed Mangoldt factor ν, put g=(k,ν), q=k/g, M=kT/ν and δ=H/T. The centered divisor twist reduces exactly to a unit numerator at q and vanishes when q=1. It is bounded by O_B(M log(2+M)(1+Hg/√(kTν))^(−B)) and O_B(q δ^(−2)(q²/(Mδ²))^B). Thus ν/g²≤(H²/(kT))T^(−δ_0) can be discarded with arbitrary fixed-power savings for a fixed positive margin δ_0.",
          "Compact comparable-height cutoff with derivative bounds, T≈Y, k≤Y^θ, H=T^κ and fixed κ>(1+θ)/2 for the short-factor claim. The weak pointwise loss O_ε(qT^ε) requires choosing κ close to one and then a small positive B. The divisor argument n need not be coprime to q.",
          "unconditional_centered_divisor_transform_and_short_factor"),
    claim(POWERS, ARITH, "Exact effective modulus and removal of several strata",
          "All supported prime powers sharing a prime with the modulus contribute o(T). All powers p^j with j≥3 contribute O(Y^θ T^(1/3+ε) log^C T), hence o(T) for θ<2/3 with fixed power margin and sufficiently small ε.",
          "The fixed d₂*(Λ log²) smooth signed sum, four-prime-supported bounded outer coefficients c_k, T≈Y, fixed 0<a<b, θ=4b∈(1/2,2/3). The taper exponent is chosen sufficiently near one. This is an unconditional estimate for these arithmetic strata.",
          "unconditional_partial_prime_power_elimination"),
    claim(SQUARES, ARITH, "Ghosh's primary quadratic estimate removes every square in a strict range",
          "At k≈K and square base p≈X the reduced quadratic numerator estimate, weighted over gcd classes, costs O(T^ε(KT/X)[K^(−1/4)+X^(−1/8)+K^(1/4)X^(−1/2)]). Combined with small-X pointwise control it gives a power saving for all square factors when 1/2<θ<9/17, equivalently 1/8<b<9/68.",
          "Same compact signed sum and bounded four-prime coefficients. Ghosh's thesis Theorem 2 on exact reduced rational phases, two monotone taper transitions and fixed strict power margins. The endpoint and the genuine-prime stratum are outside this estimate.",
          "unconditional_all_square_stratum_power_saving", related_paper_ids=[GHOSH, REN]),
    claim(PRIME_WINDOW, ARITH, "Divisor Voronoi and averaged inverse-prime bounds",
          "For K≈T^θ and P≈T^ξ, the coprime genuine-prime block saves a power in either open region: Baker θ/2<ξ<θ, (11/10)θ+(4/5)ξ<1 and θ+(11/12)ξ<1; Fouvry–Shparlinski 0<ξ<(3/2)θ, (13/10)θ+(3/5)ξ<1 and (13/12)θ+(5/6)ξ<1. Centered divisor Voronoi and a uniform O(T^ε δ^(−5/2)) cumulative kernel-and-first-derivative envelope permit full dual gcd resolution.",
          "1/2<θ<2/3 on the stated dyadic scales. Use averages at common prime endpoints and reduce each nonunit dual index to modulus k/gcd(k,l). No least-prime-factor restriction on these gcd estimates. Choose the taper exponent sufficiently near one on compact subsets of the strict regions. The longer-prime scales remain outside them.",
          "unconditional_gcd_resolved_inverse_prime_savings", related_paper_ids=[BAKER, FS, BHM]),
    claim(ALT_WINDOW, ARITH, "An alternate inverse-prime input and an excluded shortcut",
          "The 2018 homogeneous Korolev unit-numerator prefix estimate and common short dual truncation give a power saving near P=T^(1−θ) on K≈T^θ for 1/2<θ<10/17; the principal inverse-prime exponent at the center is (64+17θ)/74 before the small taper and interval losses.",
          "Original homogeneous theorem range q^(7/10+ε)≤X≤q, fixed strict margins, supported modulus primes above Y^a and common dual truncation below Y^a. Prime partial summation adds one vertical factor and changes the cutoff cost to δ^(−3−2B). The later inhomogeneous theorem with two unit coefficients is a different result.",
          "unconditional_alternate_local_inverse_prime_saving", related_paper_ids=[KOROLEV]),
    claim(ZEROS, ARITH, "An alternate inverse-prime input and an excluded shortcut",
          "The character twist of d₂*(Λ log²) is L(s,χ)²(−L'/L)'' in absolute convergence. At a simple zero ρ it has residue −2L'(ρ,χ)²; at a zero of order at least two there is no pole. Hence a contour move treating the full twist as an ordinary divisor/Eisenstein twist would omit these zero residues.",
          "Ordinary Dirichlet characters with their Euler factors. The statement concerns the indicated meromorphic continuation and poles at zeros, not a bound on their residue sum. Freezing the prime factor gives a different, valid divisor transform. No Dirichlet GRH is assumed.",
          "meromorphic_obstruction_to_full_sequence_divisor_transform"),
]

# Each edge records the exact use stated in the director note.
DEPENDENCIES = [
    (HANKEL, BARRIER, RMT),
    (HERMITE, BARRIER, RMT),
    (FIXTURES, HERMITE, RMT),
    (SCHUR, EXACT_BRIDGE, RMT),
    (SCHUR, PETROV, RMT),
    (GRAM, SCHUR, RMT),
    (TRUNCATE, SCHUR, RMT),
    (MODULUS, CSTAR, ARITH),
    (POWERS, MODULUS, ARITH),
    (SQUARES, MODULUS, ARITH),
    (SQUARES, GHOSH, ARITH),
    (PRIME_WINDOW, BAKER, ARITH),
    (PRIME_WINDOW, FS, ARITH),
    (PRIME_WINDOW, BHM, ARITH),
    (PRIME_WINDOW, MODULUS, ARITH),
    (ALT_WINDOW, KOROLEV, ARITH),
    (ALT_WINDOW, MODULUS, ARITH),
    (ZEROS, CSTAR, ARITH),
]

BOUNDARIES = [
    (FIXTURES, HERMITE, "checks_strict_threshold_and_equality", RMT),
    (GRAM, QUADRATIC_GAP, "separates_true_cutoff_from_oriented_formal_kernel", RMT),
    (SCHUR, BARRIER, "bounds_exact_factors_away_from_formal_zero", RMT),
    (SQUARES, REN, "primary_corroboration_of_quadratic_exponents", ARITH),
    (SQUARES, OPEN_CSTAR, "removes_square_stratum_without_resolving_target", ARITH),
    (PRIME_WINDOW, OPEN_CSTAR, "removes_certified_prime_scales_without_resolving_target", ARITH),
    (ZEROS, PRIME_WINDOW, "motivates_freezing_prime_before_divisor_transform", ARITH),
]

GROUPS = [
    ("HANKEL-QUANTITATIVE", "Finite fixed-rank positivity witness and exact rank-one threshold", RMT,
     ["geometry102_finite_hankel_bound.md", "weighted106_hankel_rankone_review.md",
      "uniform110_rmt_quantitative_adjudication.md"]),
    ("PETROV-POSITIVE-TAIL", "Exact finite tail quotient, true cutoff and uniform approximation", RMT,
     ["analytic102_petrov_positive_tail_reduction.md", "geometry102_petrov_tail_qa.md",
      "uniform110_rmt_quantitative_adjudication.md"]),
    ("CSTAR-STRATA", "Exact gcd reduction and elimination of short, shared and higher-power factors", ARITH,
     ["prime101_coprime_prime_strata.md", "weighted101_single_mangoldt_strata.md",
      "uniform105_strata_adjudication.md"]),
    ("CSTAR-SQUARES", "Entire prime-square stratum below θ=9/17", ARITH,
     ["weighted107_quadratic_and_inverse_prime_savings.md", "geometry108_ghosh_source_qa.md",
      "analytic109_arithmetic_partial_adjudication.md"]),
    ("CSTAR-INVERSE-PRIMES", "Gcd-resolved averaged prime windows and alternate local bound", ARITH,
     ["prime107_inverse_prime_voronoi.md", "prime113_uniform_voronoi_envelope.md",
      "uniform108_baker_bridge_qa.md", "uniform113_bessel_kernel_mass_review.md",
      "uniform115_general_prime_window_qa.md", "geometry114_korolev_primary_qa.md"]),
]


def connection(ident, note, sources, statement, hypotheses, proved, conjectural, next_step, tests):
    return dict(id=ident, sources=sources, statement=statement, hypotheses=hypotheses,
                already_proved=proved, conjectural=conjectural, next_step=next_step,
                tests=tests, status=SCOPED, evidence=note)


CONNECTIONS = [
    connection("CONN-ROOTED-CUE-FORMAL-ZERO-FINITE-HANKEL-ORDER", RMT,
               [BARRIER, HANKEL, HERMITE, FIXTURES],
               "A real zero of the extrapolating series yields an explicit finite negative Hankel witness, and at rank one the Jacobi matrix gives the least order.",
               "Fixed rank and fixed positive band. All positivity tests concern formal moments.",
               "Explicit upper degree, strict rank-one threshold and independently replayed exact fixtures.",
               "The least witness order for ranks exceeding one.",
               "Analyze higher-rank signed Gaussian-polynomial forms and compare their least order to the first raw moment crossing.",
               "Two Taylor polynomials, Cauchy bounds, Hermite recurrence and exact rational fixtures."),
    connection("CONN-PETROV-FINITE-SCHUR-TRUE-CUTOFF", RMT,
               [EXACT_BRIDGE, SCHUR, GRAM, TRUNCATE, QUADRATIC_GAP],
               "The exact tilted-to-ambient tail ratio has a positive finite Schur formula. The normalized Gram has a genuine cutoff rather than the oriented formal kernel.",
               "Real compact parameter intervals, fixed rank and positive band for uniform estimates.",
               "Exact finite quotient, positive uniform bounds, continuum Gram and factorial tail truncation.",
               "Descriptions of higher frequency chambers for the exact rooted law.",
               "Track the actual shifts and cutoff changes beyond the coefficient window.",
               "Triangular support, finite Jacobi, compact compression and weighted Fourier convolution."),
    connection("CONN-CSTAR-GCD-STRATA-AND-PRIME-WINDOW", ARITH,
               [MODULUS, POWERS, SQUARES, PRIME_WINDOW, ALT_WINDOW, ZEROS, OPEN_CSTAR],
               "Opening the single Mangoldt convolution retains exact gcds and isolates strata with unconditional savings. Freezing the prime factor avoids character-zero residues in a full-sequence divisor transform.",
               "Compact comparable heights, bounded four-prime-supported outer coefficients and a fixed taper chosen for the strict margins. RH is needed for transfer to the weighted fourth moment.",
               "Short, shared, and higher-power removals, complete square removal for θ<9/17 and the stated local genuine-prime regions.",
               "The residual signed estimate and the corresponding arithmetic fourth-moment limit.",
               "Estimate the prime scales outside the verified regions or bound their signed aggregate directly.",
               "Independent centered divisor transforms, rational quadratic prefixes, and common-endpoint averaged inverse-prime bounds."),
]


def main():
    required = {RMT, ARITH, CERT, SOURCE_SHARD, GROUP_LEDGER}
    required.update(AUDITS + name for _, _, _, reviews in GROUPS for name in reviews)
    for path in sorted(required):
        if not (ROOT / path).is_file():
            raise FileNotFoundError(path)

    expected_sources = {BAKER, BHM, GHOSH, REN, KOROLEV, FS}
    admitted = {row.get("id") or row.get("paper_id") for row in read(SOURCE_SHARD)}
    if not expected_sources <= admitted:
        raise ValueError(f"Missing admitted Round 14 source IDs: {sorted(expected_sources - admitted)}")

    shards = {
        "theorems/research_round14_claims.jsonl": CLAIMS,
        "theorems/research_round14_proof_edges.jsonl": [
            dict(locator=note, evidence=note, relation="uses_exact_scoped_input",
                 status=SCOPED, **{"from": start, "to": end})
            for start, end, note in DEPENDENCIES
        ],
        "graphs/research_round14_boundaries.jsonl": [
            dict(record_type="edge", relation=relation, provenance=note,
                 status=SCOPED, **{"from": start, "to": end})
            for start, end, relation, note in BOUNDARIES
        ],
        "connections/research_round14_connections.jsonl": CONNECTIONS,
    }
    groups = {row["id"]: row for row in read(GROUP_LEDGER)}
    for ident, title, note, reviews in GROUPS:
        group_id = "REVIEW-GROUP-R14-" + ident
        groups[group_id] = dict(id=group_id, title=title, status=SCOPED,
                                director_adjudication=note,
                                independent_reviews=[AUDITS + name for name in reviews])
    for path, rows in shards.items():
        write(path, rows)
    write(GROUP_LEDGER, groups.values())
    print(json.dumps(dict(staged_shards={name: len(rows) for name, rows in shards.items()},
                          scoped_groups=len(GROUPS), claim_ids=[row["id"] for row in CLAIMS]),
                     indent=2))


if __name__ == "__main__":
    main()
