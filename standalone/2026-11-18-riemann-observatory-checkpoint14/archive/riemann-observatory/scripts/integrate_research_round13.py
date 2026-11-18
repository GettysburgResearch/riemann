#!/usr/bin/env python3
"""Stage the director-adjudicated Round 13 research records and one source promotion."""
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDITS = "audits/adversarial_reviews/"
CUE = AUDITS + "director_cue_windows_round13.md"
TIGHT = AUDITS + "director_two_scale_round13.md"
HR = AUDITS + "director_hughes_rudnick_whole_round13.md"
PURE = AUDITS + "director_pure_fourth_round13.md"
FIXED = AUDITS + "uniform99_fixed_sequence_adjudication.md"
PETROV = AUDITS + "director_petrov_round13.md"
PETROV_PAPER = "PAPER-GEOMETRY102-PETROV2026"
HR_PAPER = "PAPER-AN79-HR-ZETA"
HR_VERSION = "2002 journal typeset version, C. R. Math. 335(8), 667–670"
HR_SHA = "b4572e5bdbf3cf7e891a4128aeb3bb56d151f2b16d23f9e63a94b1a2d2c09139"
HR_REVIEWS = [AUDITS + name for name in (
    "analytic89_hr_whole_advocate.md", "weighted88_hr_whole_skeptic.md",
)]
SCOPED = "adjudicated_scoped"
OPEN = "open_sufficient_target"


def read(path):
    source = ROOT / path
    return [json.loads(line) for line in source.read_text().splitlines() if line.strip()]


def write(path, rows):
    (ROOT / path).write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows))


def upsert(path, rows):
    records = {row["id"]: row for row in read(path)}
    records.update({row["id"]: row for row in rows})
    write(path, records.values())


def claim(ident, note, section, statement, hypotheses, kind, *, paper=None, status=SCOPED, evidence=None):
    return dict(id=ident, paper_id=paper, locator=note + " · " + section,
                evidence=evidence or note, statement=statement, hypotheses=hypotheses,
                claim_kind=kind, status=status, novelty_claim=False)


CLAIMS = [
    claim("LEM-ROOTED-CUE-TAGGED-COMPRESSION", CUE, "Measure and exact complementary determinant; separate signed totals",
          "The rank-two rooted CUE MGF equals e^(−H_N z_c) det A det(U* A^−1 U). For each tagged word with positive and negative totals P,Q≤n=N+1, the compressed inverse coefficient uses the oriented sum from Q to n−P; its constant/linear matrix is the polynomial in ell=n−P−Q and D=P−Q in the director note.",
          "Global joint Haar-matrix/root-label derivative-square tilt with the deterministic root reinserted; formal coefficients at zero. The reversed interval contributes an oriented sum, including P=n or Q=n. No fixed-symbol asymptotic is invoked.",
          "intrinsic_exact_finite_identity"),
    claim("THM-ROOTED-CUE-JOINT-CLOSED-MOMENT-WINDOW", CUE, "Joint quartic and exact finite-size surrogate",
          "At each fixed total degree r with rb≤1, the limiting mixed moments are the factorial-weighted coefficients of exp[H z_c+H(z_c²+z_s²)/4] [(1−d z_c)^4+2J3 z_c(1−d z_c)−3J2² z_s²], where H=log(b/a), d=b−a and J_j=(b^j−a^j)/j. The exact finite surrogate uses H_N, d_N, J_j,N and the n^−2 correction in the note.",
          "Fixed 0<a<b<1; negative cosine/sine bands, one deterministic root, global rank-two tilt. Finite agreement through degree r holds for r K_N≤n=N+1. The arithmetic window remains rb<1/2 under RH; this result is intrinsic.",
          "intrinsic_finite_mixed_moment_window"),
    claim("THM-ROOTED-CUE-FIRST-FREQUENCY-CORRECTION", CUE, "First new frequency chamber",
          "For (r−1)b≤1<rb, the first cosine raw-moment discrepancy from its formal continuation is −2^(1−r) I_r, where I_r=∫_{[a,b]^r, sum x_i>1}(2−4 sum x_i+2(sum x_i)^3) prod dx_i/x_i>0. The joint degree-r MGF difference is −[(z_c−i z_s)^r+(z_c+i z_s)^r] I_r/(2^r r!).",
          "Same fixed rank-two model; only the first crossing is evaluated. The pure cosine sign is strict; mixed rays can vanish or change sign.",
          "intrinsic_first_chamber_correction"),
    claim("CERT-ROOTED-CUE-FIRST-CHAMBER-FOURTH", CUE, "Independent exact finite and continuum checks",
          "For N=40, n=41 and modes 9,10,11 the exact fourth moment minus the formal surrogate is −3384187/302541624000. For band (0.22,0.28) an exact rational enclosure of the limiting fourth correction near −1.116093794622113479066e−5 has width <2.63e−27.",
          "Exact rational projection/cumulant and simplex checks. The director's finite calculation is experiments/results/director_round13_cue_fourth.json. These certificates do not give an arithmetic chamber or convergence rate.",
          "exact_finite_and_interval_certificate", evidence=AUDITS + "uniform92_first_chamber_certificate_review.md"),
    claim("THM-ROOTED-CUE-INTEGER-RANK-WINDOW", CUE, "Every fixed integer tilt rank has an extrapolation barrier",
          "At fixed integer rank J≥1 the cosine-window coefficients for rb≤1 are those of exp[(J−1)H z+H z²/4] det B_J(z), with B_J the formal oriented Legendre matrix in the note, B_J(0)=I, and deg det B_J≤J².",
          "Global root tilt |Z′|^(2(J−1)), ambient dimension N+J−1, one deterministic root, fixed positive band and fixed degree. Formal compound-Poisson notation computes polynomial coefficients.",
          "intrinsic_fixed_rank_moment_window"),
    claim("OBS-ROOTED-CUE-ALL-RANK-FINITE-SQUARE-BARRIER", CUE, "Every fixed integer tilt rank has an extrapolation barrier",
          "For each integer J≥1 and fixed 0<a<b<1 the formal all-order cosine continuation has a positive real MGF zero and a finite negative square witness. For J≥3 the {0,2} principal minor at z=1/d has determinant −20(m3/d)², forcing a zero before 1/d. Centered finite Taylor approximants to exp(z* X/2) eventually have negative formal square expectation.",
          "The polynomial-exponential signed inverse has Gaussian moment domination. The witness is at finite but potentially large degree in the formal sequence; no contradiction to the true finite window or novelty is claimed.",
          "formal_extrapolation_positivity_obstruction"),
    claim("THM-ROOTED-CUE-RANK-CORRECTION-PARITY", CUE, "Every fixed integer tilt rank has an extrapolation barrier",
          "For (r−1)b≤1<rb the first cosine raw-moment discrepancy at fixed rank J has sign (−1)^(J+1). The pure-sign continuation A_J(t) has sign (−1)^J for t>1; rank three gives A_3(t)=−6t^5+12t³−9t+3 and a finite example with correction +9/160.",
          "Intrinsic globally weighted rooted model. Christoffel–Darboux and Legendre parity apply to the reversed integration interval. This is a first crossing sign only.",
          "intrinsic_first_chamber_rank_sign"),
    claim("THM-GRID-TWO-SCALE-UNIVERSAL-TIGHTNESS", TIGHT, "Statement with the quantifiers fixed",
          "For node increments bounded in pth moment by C min(h^a+epsilon_n,A_n h^b), the polygonal modulus satisfies ||omega(delta)||_p≤C1 [delta^((a′−1)/p)+lambda_n^(1/p) min(1,(delta/w_n)^((b′−1)/p))], where a′=min(a,p), b′=min(b,p), w_n=(epsilon_n/A_n)^(1/b), lambda_n=epsilon_n/w_n. The universal tightness criterion A_n epsilon_n^(b−1)→0 is sharp, with a single random spike giving failure otherwise.",
          "Fixed p,a,b>1 and C>0, A_n≥1, 0<epsilon_n≤1 tending to zero, arbitrary deterministic finite grids, tight initial values for each family. A guarantee uniform across families needs uniformly tight initial values. Step transfer uses mesh→0, jumps→0, or exact composition and continuous clock comparison as specified. Necessity quantifies over grids and laws rather than one process.",
          "unconditional_sharp_universal_tightness"),
    claim("LEM-GRID-TWO-SCALE-DIRECT-EXPONENT", TIGHT, "Direct exponents, arithmetic use and Lean boundary",
          "For 1<q≤min(a,b), the optimal scalar envelope constant is comparable to 1+A_n^(q/b) epsilon_n^(1−q/b). For a=b=2, A=L² and epsilon=L^−M, the sharp universal saving threshold is M>2 and the maximal common direct exponent is 2M/(M+2) as L→infinity.",
          "All scalar distances 0<h≤1; realized distances in a particular grid can give stronger estimates. For M≤2 no uniform q>1 follows from the envelope. Polygonal interpolation caps the power at p.",
          "unconditional_scalar_envelope_bound"),
    claim("CERT-LEAN-TWO-SCALE-SCALAR", TIGHT, "Direct exponents, arithmetic use and Lean boundary",
          "Lean declaration Observatory.twoScaleScalarBound proves X≤2 C u³ from X≤C(u⁴+v⁶), X v²≤C u⁴, 0≤u≤1, 0<v≤1 and C≥0. With h=u² and L=1/v this is the M=6 scalar step.",
          "Lean 4.33.0-rc2, standard axiom closure propext, Classical.choice and Quot.sound, no sorryAx. Both scalar inequalities are premises; the probability and number-theoretic inputs and Brownian limit are outside this declaration.",
          "locally_compiled_formal_scalar_check", evidence="experiments/results/two_scale_scalar_lean_check.txt"),
    claim("THM-HR-REPAIRED-FINITE-GAUSSIAN-MOMENTS", HR, "Statistic, literal hypotheses and repaired theorem",
          "The first m raw zero-statistic moments converge to the Gaussian moments of mean I=∫f and variance ∫min(|v|,1) fhat(v)² dv, provided I=0 or ∫w(u) log^m(2+|u|)du<infinity. For I≠0 that logarithmic moment is necessary for finiteness of the mth absolute moment at any fixed T>1,H>0.",
          "No RH. Real even f with smooth compact Fourier transform in [−sigma,sigma], m sigma/2<a, H=T^a, 0<a≤1; evaluate the entire extension at complex ordinates. Nonnegative mass-one w with compact Fourier support. Finite moment window; the repair controls mixed gamma and polar terms additively.",
          "versioned_repaired_source_theorem", paper=HR_PAPER),
    claim("THM-HR-OSCILLATORY-PRINTED-WEIGHT-WINDOW", HR, "Reconstruction of the valid argument",
          "The oscillatory prime statistic alone has the stated finite Gaussian moment window with the original nonnegative unit-mass bandlimited weights. Compact Fourier support eliminates unequal product frequencies and the leading equal-product terms give Wick pairings.",
          "No RH and no logarithmic moment required for this oscillatory theorem. Same strict m sigma/2<a; the variance identification is needed only when m≥2. This theorem excludes the centering and polar contributions to the full statistic.",
          "versioned_source_theorem_reconstruction", paper=HR_PAPER),
    claim("OBS-HLZ-FOURTH-PURE-ARM-REDUCTION", PURE, "Exact target and what is already covered",
          "For the cosine band W=Re D and 1/8<b<1/6, the difference between E_Y W⁴ and its formal fourth coefficient is (Re E_Y D⁴−m4_pure)/8+o(1), with m4_pure=4![z⁴] exp(H0 z)[(1−d z)^4+2m3 z(1−d z)+3m2² z²]. The mixed arms and a uniform sixth absolute moment are already covered.",
          "RH, fixed 0<a<b, and the symmetric strict derivative-square tail. The 3+1 and 2+2 arms have longest length ≤Y^(3b)<sqrt(Y); the long pure arm is unresolved. Intrinsic CUE gives no arithmetic main term.",
          "conditional_exact_single_arm_reduction"),
    claim("LEM-HLZ-ONE-SIDED-LONG-CONTINUOUS", PURE, "One-sided continuous moments do not impose the half-power barrier",
          "The continuous shifted zeta product against one bounded-coefficient Dirichlet polynomial of length y≤T^theta, theta<1, has the explicit two-diagonal formula in the note with error O_epsilon(T^epsilon[(yT)^(1/2)+y^(1/4)T^(3/4)]), also with the logarithmic weight. The diagonal poles cancel.",
          "Unconditional continuous-height integral, constant second arm and fixed microscopic shift radius. The direct asymmetric AFE proof does not estimate the discrete nonprincipal edge.",
          "unconditional_asymmetric_continuous_estimate"),
    claim("LEM-HLZ-SMOOTH-REFLECTED-SADDLE", PURE, "A smooth contour formulation closes the saddle error",
          "A two-transition compact comparable-height cutoff of width H=T^kappa with kappa>(1+theta)/2, theta=4b, gives a reflected saddle error O(T/H²) per comparable term. The aggregated error is bounded by T^epsilon[T²y/H²+y+Ty/H]. Sharp zero-sum endpoints are recovered after differentiation with transition mass O(T^epsilon(H+Y^(2b))).",
          "RH for the zero-sampling endpoint comparison, fixed microscopic shifts, theta<1 and kappa<1. The cutoff is shift-independent before differentiation. The result applies to the smooth saddle and does not recover the original hard arithmetic cutoff.",
          "conditional_smooth_saddle_and_endpoint_replacement"),
    claim("LEM-HLZ-REFLECTED-EDGE-FIXED-SEQUENCE", FIXED, "Differentiation and the original-modulus average; Reduction to the single Mangoldt convolution",
          "The three differentiated reflected shifts give A(m)+log(k/m)(log*log)(m), with A=d_2*Lambda*Lambda*Lambda. The original-modulus unit average of e(−m/k) is mu(q)/phi(q), q=k/(k,m). The divisor products decay faster than any fixed power for the smooth cutoff; the remaining edge is (1/2) E_Cstar+O_N(T^−N), where Cstar=d_2*(Lambda log²).",
          "Compact-local smooth contour formulation, k≤y≤T^theta, H=T^kappa with kappa>(1+theta)/2, bounded outer coefficients. Divisor removal is unconditional via Poisson or Hurwitz–Mellin cancellation. Arbitrary decay applies to discarded divisor pieces; inherited contour errors keep their separate bounds.",
          "proved_fixed_arithmetic_sequence_reduction"),
    claim("OPEN-HLZ-PURE-FOURTH-CSTAR-CANCELLATION", FIXED, "Reduction to the single Mangoldt convolution",
          "The remaining sufficient target is Re E_Cstar=o(T log⁴T), with E_Cstar=∑_{k≤Y^(4b)} (c_k/k)∑_m Cstar(m) w_T(2πm/k)[e(−m/k)−mu(q)/phi(q)], q=k/(k,m), and c_k the coefficients of D⁴.",
          "Compact comparable heights T approximately Y, fixed 1/8<b<1/6 and the same two-transition taper and principal subtraction. The target is unproved. RH and the established compact-to-strict-tail comparison would transfer a proof to the pure and real fourth moments.",
          "open_arithmetic_sufficient_condition", status=OPEN),
]

CLAIMS += [
    claim("THM-GR1974-GRR-MODULUS", AUDITS + "release92_tightness_source_selection.md",
          "Garsia and Rodemich; 1974 journal pp. 69–70, Theorem 1.2 and (1.2), (1.3), (1.7), (1.8)",
          "The reproduced GRR inequality bounds continuous-path increments in its power case by a constant times B^(1/p) ∫_0^h u^(−2/p)dg(u), with B the double energy in the director note.",
          "Continuous interpolation, increasing continuous gauge, finite energy, convergent scale integral. The source almost-everywhere estimate extends to a continuous path. Targeted primary passage; the 1974 article credits the three-author original.",
          "targeted_primary_source_dependency", paper="PAPER-U89-GARSIA-RODEMICH-REARRANGEMENT"),
    claim("THM-BILLINGSLEY1968-C-TIGHTNESS-AND-TRIANGLE", AUDITS + "release92_tightness_source_selection.md",
          "Billingsley; first edition Theorem 8.2 p. 55, Theorem 12.3 pp. 95–96 and §12 Problem 9 p. 103",
          "Tight initial values and asymptotically small modulus probabilities characterize tightness in C. The common-clock sufficient criterion requires a time exponent greater than one; a randomly located shrinking triangle demonstrates failure at the critical exponent.",
          "First-edition scanned passages only. Both the arbitrary-grid minimum envelope and its sharpness at a variable crossover are local adaptations.",
          "targeted_primary_source_dependency", paper="PAPER-U89-BILLINGSLEY-CONVERGENCE-1968"),
    claim("LEM-PETROV-ROOTED-CUE-EXACT-FACTOR-BRIDGE", PETROV, "Applicable source theorem and exact matching",
          "Petrov v1 Theorem 4.4, ordinary BOGC and finite Jacobi give det(U* A_n^−1 U)=(det Gamma/det Gamma(0)) L_obl/L_n for the rooted CUE cosine symbol. On the real Laplace axis both exact Gram and oblique tail determinants are strictly positive at every fixed N,z.",
          "Fixed integers N≥2 and J≥1, analytic polynomial tilts X=T((1−w)^J) on N−1 free modes and exponential finite Laurent symbol. The source theorem requires its Gram to be invertible; real z gives the adjoint structure. The optional fixed-tail chart requires separate invertibility.",
          "intrinsic_exact_source_theorem_transfer"),
    claim("OBS-PETROV-ROOTED-CUE-GRAM-QUADRATIC-MISMATCH", PETROV, "The tail contributes already at order two; Exact finite witness and optional chart",
          "The tilted tail contributes −kappa_(J,N) z² with kappa_(J,N)=Σ_(j<J)||H(F_+)*U_j||²>0. If 2 max(band)≤n and the band is nonempty, the normalized Gram already differs from the complementary determinant at order two. For N=4,J=2,k=2 the gap is 9/160; the optional chart determinant changes sign between z=0 and 8 while the exact factors remain positive.",
          "Same fixed-rank cosine model. The ordinary ambient tail is stable in the stated coefficient window. For fixed 0<a<b≤1/2 the quadratic gap has the positive Riemann-sum limit in the note. The chart obstruction is separate from the zero of the extrapolated formal moment polynomial.",
          "intrinsic_quadratic_nonidentification_and_chart_witness",
          evidence="experiments/results/director_petrov_quadratic_round13.json"),
]

DEPENDENCIES = [
    ("THM-ROOTED-CUE-JOINT-CLOSED-MOMENT-WINDOW", "LEM-ROOTED-CUE-TAGGED-COMPRESSION", CUE),
    ("THM-ROOTED-CUE-FIRST-FREQUENCY-CORRECTION", "THM-ROOTED-CUE-JOINT-CLOSED-MOMENT-WINDOW", CUE),
    ("THM-ROOTED-CUE-INTEGER-RANK-WINDOW", "PAPER-LF63-HKO2000", CUE),
    ("THM-ROOTED-CUE-INTEGER-RANK-WINDOW", "LEM-ROOTED-CUE-TAGGED-COMPRESSION", CUE),
    ("OBS-ROOTED-CUE-ALL-RANK-FINITE-SQUARE-BARRIER", "THM-ROOTED-CUE-INTEGER-RANK-WINDOW", CUE),
    ("THM-ROOTED-CUE-RANK-CORRECTION-PARITY", "THM-ROOTED-CUE-INTEGER-RANK-WINDOW", CUE),
    ("THM-GRID-TWO-SCALE-UNIVERSAL-TIGHTNESS", "THM-GR1974-GRR-MODULUS", TIGHT),
    ("THM-GRID-TWO-SCALE-UNIVERSAL-TIGHTNESS", "THM-BILLINGSLEY1968-C-TIGHTNESS-AND-TRIANGLE", TIGHT),
    ("THM-SHRINKING-BAND-BROWNIAN-PROCESS", "THM-GRID-TWO-SCALE-UNIVERSAL-TIGHTNESS", TIGHT),
    ("THM-HR-REPAIRED-FINITE-GAUSSIAN-MOMENTS", "THM-HR-OSCILLATORY-PRINTED-WEIGHT-WINDOW", HR),
    ("OBS-HLZ-FOURTH-PURE-ARM-REDUCTION", "THM-HLZ-JOURNAL5-REAL-COEFFICIENTS", PURE),
    ("LEM-HLZ-REFLECTED-EDGE-FIXED-SEQUENCE", "LEM-HLZ-SMOOTH-REFLECTED-SADDLE", FIXED),
    ("LEM-PETROV-ROOTED-CUE-EXACT-FACTOR-BRIDGE", PETROV_PAPER, PETROV),
    ("LEM-PETROV-ROOTED-CUE-EXACT-FACTOR-BRIDGE", "LEM-ROOTED-CUE-TAGGED-COMPRESSION", PETROV),
    ("OBS-PETROV-ROOTED-CUE-GRAM-QUADRATIC-MISMATCH", "LEM-PETROV-ROOTED-CUE-EXACT-FACTOR-BRIDGE", PETROV),
]

BOUNDARIES = [
    ("CERT-ROOTED-CUE-FIRST-CHAMBER-FOURTH", "THM-ROOTED-CUE-FIRST-FREQUENCY-CORRECTION",
     "checks_finite_and_continuum_correction", CUE, SCOPED),
    ("THM-ROOTED-CUE-JOINT-CLOSED-MOMENT-WINDOW", "THM-HLZ-FINITE-BAND-MOMENT-WINDOW",
     "compares_to_smaller_arithmetic_window", CUE, SCOPED),
    ("CERT-LEAN-TWO-SCALE-SCALAR", "LEM-SUBPOWER-SUBSET-TWO-SCALE-FOURTH",
     "formalizes_scalar_implication_only", TIGHT, SCOPED),
    ("OBS-HLZ-FOURTH-PURE-ARM-REDUCTION", "THM-ROOTED-CUE-JOINT-CLOSED-MOMENT-WINDOW",
     "intrinsic_comparator_without_arithmetic_transfer", PURE, SCOPED),
    ("OBS-HLZ-FOURTH-PURE-ARM-REDUCTION", "OPEN-HLZ-PURE-FOURTH-CSTAR-CANCELLATION",
     "identifies_open_sufficient_estimate_for_moment_extension", FIXED, OPEN),
    ("OPEN-HLZ-PURE-FOURTH-CSTAR-CANCELLATION", "LEM-HLZ-REFLECTED-EDGE-FIXED-SEQUENCE",
     "remaining_target_after_proved_reduction", FIXED, OPEN),
    ("OBS-PETROV-ROOTED-CUE-GRAM-QUADRATIC-MISMATCH", "OBS-ROOTED-CUE-ALL-RANK-FINITE-SQUARE-BARRIER",
     "distinguishes_exact_factors_from_formal_continuation", PETROV, SCOPED),
]

GROUPS = [
    ("CUE-WINDOW", "Closed rooted CUE window and first correction", CUE,
     ["prime84_cue_moment_window.md", "weighted84_cue_moment_window_review.md",
      "uniform86_cue_window_adjudication_input.md"]),
    ("CUE-CHAMBER-CERT", "Exact finite and continuum rooted CUE checks", CUE,
     ["prime89_first_chamber_certificate.md", "uniform92_first_chamber_certificate_review.md"]),
    ("CUE-RANK-BARRIER", "All fixed ranks and finite square witnesses", CUE,
     ["geometry93_rank_three_barrier.md", "analytic93_rank_three_skeptic.md"]),
    ("GRID-TIGHTNESS", "Sharp universal two-scale grid tightness", TIGHT,
     ["uniform85_two_scale_tightness_lemma.md", "analytic86_two_scale_skeptic.md",
      "uniform89_tightness_priority.md"]),
    ("HR-WEIGHT", "Hughes–Rudnick exact repair and oscillatory theorem", HR,
     ["analytic89_hr_whole_advocate.md", "weighted88_hr_whole_skeptic.md",
      "analytic85_hughes_weight_repair_review.md"]),
    ("PURE-FOURTH", "Long pure fourth arm, smooth saddle and strict-tail reduction", PURE,
     ["prime90_pure_fourth_bottleneck.md", "weighted90_pure_fourth_review.md",
      "analytic95_pure_fourth_adjudication.md", "prime96_smooth_saddle_review.md",
      "weighted96_smooth_saddle_review.md"]),
    ("FIXED-CSTAR", "Three-shift fixed-sequence and divisor removal", PURE,
     ["prime98_fixed_arithmetic_sequence.md", "weighted98_fixed_sequence_review.md",
      "uniform99_fixed_sequence_adjudication.md"]),
    ("PETROV-BRIDGE", "Tilted Toeplitz factors, quadratic gap and optional chart", PETROV,
     ["geometry97_petrov_gram_match.md", "analytic100_petrov_match_skeptic.md"]),
]


def connection(ident, notes, sources, statement, hypotheses, proved, conjectural, next_step, tests):
    return dict(id=ident, sources=sources, statement=statement, hypotheses=hypotheses,
                already_proved=proved, conjectural=conjectural, next_step=next_step,
                tests=tests, status=SCOPED, evidence=notes)


CONNECTIONS = [
    connection("CONN-ROOTED-CUE-CLOSED-WINDOW-ARITHMETIC-GAP", CUE,
               ["THM-ROOTED-CUE-JOINT-CLOSED-MOMENT-WINDOW", "THM-HLZ-FINITE-BAND-MOMENT-WINDOW",
                "THM-ROOTED-CUE-FIRST-FREQUENCY-CORRECTION"],
               "The intrinsic closed CUE window gives a higher-support comparison formula, while the arithmetic length threshold differs.",
               "Fixed band and fixed moment degree; intrinsic rb≤1, source arithmetic rb<1/2 under RH.",
               "Exact complementary determinant and first intrinsic correction.",
               "Arithmetic moments exceeding the source length window.",
               "Estimate the long pure fourth arm before seeking a full fixed-band comparison.",
               "Tagged endpoint check, exact rational projection and continuum chamber certificates."),
    connection("CONN-GRID-TIGHTNESS-CLASSICAL-MODULUS", TIGHT,
               ["THM-GRID-TWO-SCALE-UNIVERSAL-TIGHTNESS", "THM-GR1974-GRR-MODULUS",
                "THM-BILLINGSLEY1968-C-TIGHTNESS-AND-TRIANGLE", "THM-SHRINKING-BAND-BROWNIAN-PROCESS"],
               "A classical modulus inequality and spike mechanism recover the exact universal parameter threshold once a local fine increment envelope is available.",
               "Deterministic grids, both increment bounds and tight initial values; arithmetic application assumes RH.",
               "Uniform interpolation and modulus, sharp worst-case obstruction, and the M>2 consequence for a=b=2.",
               "Arithmetic fine bound or effective path-law rates in other regimes.",
               "Establish the fine increment estimate appropriate to a new weighted process.",
               "Independent dyadic and GRR calculations and the local Lean scalar check."),
    connection("CONN-HR-BANDLIMITED-AVERAGE-LOG-TAIL", HR,
               ["THM-HR-REPAIRED-FINITE-GAUSSIAN-MOMENTS", "THM-HR-OSCILLATORY-PRINTED-WEIGHT-WINDOW"],
               "Bandlimiting removes unmatched prime products, while the full statistic's smooth gamma term needs separate log-tail integrability.",
               "Printed weight class and strict Fourier window in the pinned Hughes–Rudnick journal edition.",
               "The oscillatory result on the printed class, the fixed-weight counterexample and repaired finite moments.",
               "A full Gaussian law for a fixed test is outside this comparison.",
               "Track actual weight hypotheses in applications of the finite-moment theorem.",
               "Exact shifted log asymptotic and a positive fixed weighted translate series."),
    connection("CONN-PURE-FOURTH-SMOOTH-CSTAR-EDGE", FIXED,
               ["OBS-HLZ-FOURTH-PURE-ARM-REDUCTION", "LEM-HLZ-ONE-SIDED-LONG-CONTINUOUS",
                "LEM-HLZ-SMOOTH-REFLECTED-SADDLE", "LEM-HLZ-REFLECTED-EDGE-FIXED-SEQUENCE",
                "OPEN-HLZ-PURE-FOURTH-CSTAR-CANCELLATION"],
               "The arithmetic fourth-moment extension reduces to the signed nonprincipal sum for the fixed sequence d_2*(Lambda log²).",
               "RH for the target weighted-zero theorem, fixed 1/8<b<1/6, compact comparable-height tapers and strict-tail transfer.",
               "Mixed arms, asymmetric continuous estimate, smooth saddle and exact divisor removal.",
               "Re E_Cstar=o(T log⁴T) and hence the long pure and real fourth moments.",
               "Exploit the sign and four-prime outer structure in the surviving Mangoldt convolution.",
               "Independent contour/error reviews and Poisson and Hurwitz–Mellin identities."),
    connection("CONN-PETROV-EXACT-TAIL-AND-FORMAL-CUE-WINDOW", PETROV,
               [PETROV_PAPER, "LEM-PETROV-ROOTED-CUE-EXACT-FACTOR-BRIDGE",
                "OBS-PETROV-ROOTED-CUE-GRAM-QUADRATIC-MISMATCH", "THM-ROOTED-CUE-INTEGER-RANK-WINDOW"],
               "The exact tilted factorization gives an alternate intrinsic CUE interface and requires both the Gram and tail factors even inside the moment window.",
               "Fixed rank and finite exponential Laurent symbol. Real-axis positivity and the optional chart are distinct assertions.",
               "Exact factor bridge, strict quadratic gap, and a positive-axis failure of optional chart invertibility.",
               "Uniform finite-dimensional approximation of the tail quotient beyond low orders.",
               "Control the exact tail quotient uniformly in N and bounded real z while tracking the higher Fourier chambers.",
               "Independent operator matching and exact rational Gram, Jacobi and chart extraction."),
]

PROMOTION = dict(id=HR_PAPER, level=3, version=HR_VERSION, source_sha256=HR_SHA,
                 evidence=HR, independent_reviews=HR_REVIEWS,
                 whole_work_coverage_checklist=[
                     "All four controlling journal pages and all nine longer arXiv v1 pages, exact distinct edition pins, both abstracts and source statements.",
                     "Smooth count and gamma branch, entire test for complex ordinates, strip decay and explicit formula with all polar terms.",
                     "Literal weight class, exact fixed-T moment integrability, fixed translate-mixture counterexample and sufficient log-moment repair.",
                     "Mean, restricted support, unequal-product exclusion, prime-power pairings, diagonal variance and additive mixed-error proof including odd top moments.",
                     "Ordinary CUE comparison, variance and higher-moment remarks, acknowledgments, references and correction-history limits.",
                 ],
                 external_inputs="Matched functional equation, Stirling, local zero count and good heights, prime number theorem and Schur orthogonality. Selberg/Fujii background and all original ancestry are outside this exact whole-note promotion.")

SOURCE_UPDATE = dict(
    id=HR_PAPER, evidence=HR,
    fields=dict(version=HR_VERSION, source_sha256=HR_SHA, audit_level=3,
                whole_work_read=True, substantive_reading=True,
                read_scope="Complete four-page journal pinned and independently reconstructed; the separate nine-page arXiv v1 was also checked. The original oscillatory moment theorem survives the printed class. The full statistic needs the documented logarithmic-moment alternative and additive comparison.",
                claim_verification_status="Whole-work Level 3 for the exact journal version. One version-scoped missing-hypothesis finding and a valid repair. Finite moments without RH.",
                main_result="With real even f, smooth compact Fourier transform of strict radius sigma, m sigma/2<a and H=T^a, 0<a≤1, the oscillatory prime part has its finite Gaussian window for nonnegative unit-mass bandlimited w. The full statistic has the stated finite Gaussian moments if ∫f=0 or ∫w log^m(2+|u|)<infinity. The literal printed weight class alone is too broad.",
                independent_whole_reading_reviews=HR_REVIEWS,
                additional_source_manifestation=dict(
                    version="arXiv:math/0208220v1, nine pages",
                    source_sha256="2225d590d97abd13a4b973bd3d936a7b07fb45a3296739438f8ce57f657cdebd",
                    scope="Complete comparison by both independent reviewers; promotion pinned to journal.")))

FINDING = dict(
    id="FIND-R13-HR-AVERAGING-WEIGHT-LOG-MOMENT",
    title="The printed Hughes–Rudnick averaging class allows an infinite first moment",
    classification="Missing or insufficiently stated hypothesis",
    status="adjudicated_exact_journal_counterexample_and_repair",
    sources=[HR_PAPER], claim_id="THM-HR-REPAIRED-FINITE-GAUSSIAN-MOMENTS",
    evidence=HR, director_adjudication=HR, independent_reviews=HR_REVIEWS,
    verified_author_error=True, version=HR_VERSION, source_sha256=HR_SHA,
    source_locator="Journal Theorem 1.1 and printed weight definition; explicit formula (2)–(4), pp. 668–669.",
    explicit_witness="Let b=q²/∫q² for a nonzero real even Schwartz q with smooth compact Fourier support, and choose w(u)=∑_{j≥1}2^−j b(u−exp(4^j)). It is smooth, nonnegative, of mass one and bandlimited, but ∫w log(2+|u|)=∞. For a real even bandlimited Schwartz-square test with I=∫f>0 and sufficiently small support, N_f(tau)=(I/log T)log(1+|tau|)+O_{f,T}(1). Consequently its printed weighted first moment is +∞ for every fixed T>1,H>0.",
    scope="Literal full-statistic moment statement in the pinned journal only. The repaired finite window holds when I=0 or w has finite mth logarithmic moment. The oscillatory prime theorem remains valid on the full printed class. No variance error or broader claim is recorded.")


def main():
    for path in [CUE, TIGHT, HR, PURE, FIXED, PETROV, *HR_REVIEWS]:
        if not (ROOT / path).is_file():
            raise FileNotFoundError(path)
    hr_record = next(row for row in read("papers/prior_art82_records.jsonl") if row["id"] == HR_PAPER)
    if hr_record["source_sha256"] != HR_SHA:
        raise ValueError("Hughes–Rudnick contributor record has a different source pin")
    source = ROOT / hr_record["source_path"]
    if source.is_file() and hashlib.sha256(source.read_bytes()).hexdigest() != HR_SHA:
        raise ValueError("Hughes–Rudnick journal PDF differs from its pinned hash")

    shards = {
        "theorems/research_round13_claims.jsonl": CLAIMS,
        "theorems/research_round13_proof_edges.jsonl": [
            {"from": start, "to": end, "relation": "uses_exact_scoped_input",
             "locator": note, "evidence": note, "status": SCOPED}
            for start, end, note in DEPENDENCIES],
        "graphs/research_round13_boundaries.jsonl": [
            {"record_type": "edge", "from": start, "to": end, "relation": relation,
             "provenance": note, "status": status}
            for start, end, relation, note, status in BOUNDARIES],
        "connections/research_round13_connections.jsonl": CONNECTIONS,
        "audits/research_round13_findings.jsonl": [FINDING],
        "quality/zzzzzzzz_round13_research_source_scope_updates.jsonl": [SOURCE_UPDATE],
    }
    for path, records in shards.items():
        write(path, records)
    upsert("quality/whole_work_audit_promotions.jsonl", [PROMOTION])
    upsert("audits/reviewed_claim_groups.jsonl", [
        dict(id="REVIEW-GROUP-R13-" + ident, title=title, status=SCOPED,
             director_adjudication=note, independent_reviews=[AUDITS + file for file in references])
        for ident, title, note, references in GROUPS])
    print(json.dumps(dict(staged_shards={name: len(records) for name, records in shards.items()},
                          claim_ids=[row["id"] for row in CLAIMS],
                          scoped_groups=len(GROUPS), promoted_work=HR_PAPER), indent=2))


if __name__ == "__main__":
    main()
