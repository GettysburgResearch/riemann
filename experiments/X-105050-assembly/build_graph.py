#!/usr/bin/env python3
"""Lane A1: build assembly_graph.json — canonical machine graph of the transport
program's route to RH (2026-08-21/22 review wave). Zero third-party deps.
All coordinates are (claim_id, path, branch, 40-hex sha), path-qualified per
Reviewer C. Statuses/edge types per the synthesized fail-closed spec
(t4_graph_spec.md section a + SYNTHESIZED COMPLETE SPEC)."""
import json, os

D = os.path.dirname(os.path.abspath(__file__))

SHA = {
    "REVA": "55fe0b6f23d9163e2b602608da84194ba243d7c4",   # Reviewer A packet / PR 709
    "PR652": "24ab64551225f2dba9aa53a533eb9b0285c6e363",
    "PR653": "e928fd615d753882706bb88c51b717bd8d4a86ba",
    "PR649": "433fd3662f7b2e4ba384ce64f196380e88624090",
    "PR650": "3f9e80f09fe1f595927ea7dce6fb49ac68c5c21b",
    "PR696": "f4016db548afceb31b150547cb6cd48b4cddb77d",
    "PR702": "89f995450977c3590aada0c1447a7e6af7fcd9ac",
    "PR703": "0a46dba5c74e573945e3612937606f6ca735a1d3",
    "PR707": "7bf3308d40ac8ed1ba50e404ff6e9c47526d89e4",
    "PR685": "4f69b7656f42dcb5ff250d13adc9f88e8d18f315",
    "S105":  "e81eaca5c93e833fd465dd3917f9dce03e57fc04",
}
BR = {
    "REVA": "origin/review/2026-08-21/arithmetic-native-implication",
    "PR652": "origin/review/gpt56-pro/99600-three-interface-hostile-audit",
    "PR653": "origin/review/gpt56-pro/99270-three-vulnerability-hardening",
    "PR649": "origin/research/gpt56-pro/99260-three-vulnerability-hardening",
    "PR650": "origin/review/gpt56-pro/99280-triad-hardening",
    "PR696": "origin/research/gpt56-sol/102000-parabolic-bessel-vaughan-correction",
    "PR702": "origin/research/gpt56-pro/103100-fractional-hankel-near-collision",
    "PR703": "origin/research/gpt56-pro/102100-carrier-free-staircase-matrix",
    "PR707": "origin/research/gpt56-pro/103300-balanced-phase-gram",
    "PR685": "origin/research/gpt56-pro/100300-two-route-endgame",
    "S105":  "claude/riemann-proof-review-8nz34i",
}

def C(key, claim_id, path):
    return {"claim_id": claim_id, "path": path, "branch": BR[key], "sha": SHA[key]}

nodes = []
def N(sid, kind, status, statement, coords, required_fixes=None, notes=None):
    n = {"semantic_id": sid, "kind": kind, "status": status,
         "statement": statement, "coordinates": coords}
    if required_fixes: n["required_fixes"] = required_fixes
    if notes: n["notes"] = notes
    nodes.append(n)

# ---------------- terminal ----------------
N("RH", "terminal", "OPEN_RH_EQUIVALENT",
  "The Riemann Hypothesis: every nontrivial zero of zeta(s) has Re s = 1/2; UNPROVED, declared terminal node (Reviewer B G-RH-TERMINAL-001 repair).",
  {"claim_id": "RH", "path": "review/2026-08-22/cross-b-of-a/CROSS_REVIEW_REPORT.md",
   "branch": "origin/review/2026-08-22/reviewer-b-cross-review-a",
   "sha": "945a6eec3406cce8f6cd63eba6c69fb60676c41d"},
  notes="Terminal only: may appear solely as an edge conclusion. RH status everywhere in the reviewed corpus: unproved.")

# ---------------- native spur claims ----------------
N("L-99601", "claim", "VERIFIED",
  "Sequential first-owner Euler identity: prod_{i=1..k}(I - r_i U_i) f = s_k f + sum_i lambda_i (I-U_i) prod_{h>i}(I - r_h U_h) f with r_i=p_i^{-1/2}, s_i=prod_{h<=i}(1-r_h), lambda_i=r_i s_{i-1}, s_k+sum lambda_i=1, preserving every native coefficient and parity (L-99601.7).",
  C("PR652", "L-99601", "claims/lemmas/L-99601-sequential-first-owner-euler-hazard.md"),
  notes="CLAIMS.tsv ARITH.SHARP.SEQUENTIAL_FIRST_OWNER VERIFIED (LIGHT_EXACT_REPLAY); supersedes refuted alpha-child promotion R-99600.")
N("R-99600", "claim", "REFUTED",
  "REFUTED MECHANISM (firewall): the alpha-child hazard is NOT the native Euler source — the contracted causal identity's net shifted coefficient is 0 (magnitude 2r^2) versus the native -r; missing native source r(1-2r)>0 for p>=67 (R-99600.5); alpha-child native promotion is FALSE.",
  C("PR652", "R-99600", "claims/refutations/R-99600-alpha-child-hazard-is-not-the-native-euler-source.md"),
  notes="CLAIMS.tsv ARITH.SHARP.ALPHA_NATIVE_PROMOTION = FALSE. The dead route edge EDGE.NATIVE.ALPHA_PROMOTION (ROUTE_EDGES.tsv line 5, verdict FALSE) is retained as history only and is NOT reproduced as a live edge here.")
N("L-99602", "claim", "VERIFIED_WITH_FIXES",
  "Exact two-row Mellin-Landau consumer: with c_X(j)=sum_{n<=X/j} mu(n) n^{-1/2} Q_{X/n}(j), C_j(s)=C_j/s^2 + P_j(s+1/2)/(s^2 zeta(s+1/2)); P_2(z)=2*2^{-z}-1-3^{-z} and 3P_3(z)=5*3^{-z}-2^{-z}-1-3*4^{-z} have no common zero in Re z>0 (L-99602.5); hence c_X(2)>=0 and c_X(3)>=0 for large X (or the L-99602.6 holomorphic-defect split) implies RH via Landau + functional equation.",
  C("PR652", "L-99602", "claims/lemmas/L-99602-exact-two-row-mellin-landau-consumer.md"),
  required_fixes=["Separate convergence from continuation (CONSUMER.MELLIN.FIXED_ROW, LINE_BY_LINE_RECONSTRUCTION fix)"],
  notes="Two ledger rows: CONSUMER.MELLIN.FIXED_ROW VERIFIED_WITH_FIXES; CONSUMER.MELLIN.TWO_ROW VERIFIED.")
N("L-99261", "claim", "VERIFIED",
  "Five-three fixed detector: W_X=5c_X(2)+3c_X(3) has Mellin transform 6/s^2 - 3(2^{-z}-1)(2^{-z}-2)/(s^2 zeta(z)), z=s+1/2, with numerator zero-free in 0<Re z<1; eventual nonnegativity of the single scalar W_X implies RH (Landau one-sign).",
  C("PR649", "L-99261", "claims/lemmas/L-99261-five-three-row-zero-free-mellin-witness.md"),
  notes="CLAIMS.tsv CONSUMER.MELLIN.FIVE_THREE VERIFIED (LIGHT_EXACT_REPLAY). Depends on L-99240 (ARITH.SHARP.ROW_KERNEL, VERIFIED_WITH_FIXES, PR 642 @ 07aa0d4838458a1b2d3af9e5bc96616baa6b4767).")
N("L-99270", "claim", "VERIFIED_WITH_FIXES",
  "Zero-free smoothing and negative mass for the fixed zero-safe scalar h=H_67(x)=Psi(x)-67^{-1/2}Psi(x/67), Psi(x)=sum_{n<=x} mu(n) n^{-1/2}(4 sqrt(x/n)-3): either one-octave log-box nonnegativity (S_A h)(X)>=0 eventually (L-99270.7/.8) or subpower logarithmic negative mass M_-(X)=O_eps(X^eps) (L-99270.10) implies RH.",
  C("PR653", "L-99270", "claims/lemmas/L-99270-zero-free-smoothing-and-negative-mass.md"),
  required_fixes=["State local integrability and finite abscissa (CONSUMER.MELLIN.NEGATIVE_MASS fix)"],
  notes="Rows: CONSUMER.MELLIN.NEGATIVE_MASS VERIFIED_WITH_FIXES; CONSUMER.MELLIN.ZERO_SAFE_BOX VERIFIED. Known ledger defect PROV.A.MISSING_LEADING_E: ZERO_SAFE_BOX row carries 39-char SHA 928fd615... (expected e928fd615d753882706bb88c51b717bd8d4a86ba); recorded, not normalized silently.")
N("L-99272", "claim", "VERIFIED_WITH_FIXES",
  "Specialized Landau theorem + scalar firewall: a nonnegative locally integrable Mellin density (not a.e. 0) with finite abscissa sigma_c has a singularity at s=sigma_c; F(s) and K_A(s)F(s) for the H_67 scalar are analytic at every real s>0.",
  C("PR653", "L-99272", "claims/lemmas/L-99272-specialized-landau-and-scalar-firewall.md"),
  required_fixes=["Keep the finite-abscissa step explicit (CONSUMER.MELLIN.LANDAU_SPECIALIZED fix)"],
  notes="Analytic backbone consumed by L-99270; self-contained (no row/Hall/score imports).")
N("L-99282", "claim", "VERIFIED_WITH_FIXES",
  "Holomorphic perturbation Landau transfer: for some fixed large row j, c_X(j)=d_X(j)+e_X(j) with d_X(j)>=0 and e in H_0 (Mellin transform holomorphic on Re s>0), plus stated growth, implies RH via the large-row numerator asymptotic P_j(z) = -(z(z+1)/(1-z)) j^{-z-1} + O(...) (L-99282.5).",
  C("PR650", "L-99282", "claims/lemmas/L-99282-holomorphic-perturbation-landau-transfer.md"),
  required_fixes=["Defect must stay fixed and signed (CONSUMER.MELLIN.HOLOMORPHIC_DEFECT fix)"],
  notes="rh_relationship 'conditional transfer'. No Reviewer A route edge exists for its consumer interface ('positive surrogate absent'); therefore no edge is drawn — node retained as verified analytic API.")
N("L-99281", "claim", "DEPOSITED_UNREVIEWED",
  "Subpower defect resolvent: H_0 = {f: |f(X)| <= C_eps X^eps for all eps>0} has Mellin transform holomorphic on Re s>0 (L-99281.2), plus alpha-only factor-67 resolvent with mass contraction kappa<1/8 preserving H_0.",
  C("PR650", "L-99281", "claims/lemmas/L-99281-subpower-defect-resolvent.md"),
  notes="HONEST STATUS: no own CLAIMS.tsv row; verified only as an internal step of the PR 650 triad; enters the lattice solely through L-99282's H_0 hypothesis.")

# ---------------- Vaughan lattice (PR 696) ----------------
N("L-102001", "claim", "VERIFIED",
  "Balanced Vaughan large-divisor Hankel form: exact balanced Vaughan source identity a_U*a_U*mu = b_U*a_U with b_U(n)=mu(n)1_{n>U}, retaining mu^2(gab)=1 in gcd coordinates.",
  C("PR696", "L-102001", "claims/lemmas/L-102001-balanced-vaughan-large-divisor-hankel-form.md"),
  notes="CLAIMS.tsv ARITH.VAUGHAN.LARGE_DIVISOR VERIFIED (LIGHT_EXACT_REPLAY); open remainder: signed balanced estimate.")
N("L-102009", "claim", "VERIFIED",
  "Ratio-four two-field factorization: B_U(X) = int_U^{X/U} F_{U,-}(Y) F_{U,+}(X/Y) dY/Y exactly (L-102009.13), with A_-(y)=1 on (1,2), -sqrt(2) on (2,4), 0 else, and Cauchy-Schwarz product certificate (B_U(X))_-^2 <= E_{U,-}(X) E_{U,+}(X) (L-102009.14).",
  C("PR696", "L-102009", "claims/lemmas/L-102009-ratiofour-two-field-factorization-of-balanced-vaughan.md"),
  notes="CLAIMS.tsv ARITH.VAUGHAN.RATIO4_TWO_FIELD VERIFIED (LINE_BY_LINE_RECONSTRUCTION); 'Use product AB in Cauchy gate'.")
N("L-102010", "claim", "VERIFIED_WITH_FIXES",
  "Half-divisor symmetric one-field reduction: with eta multiplicative, sum_k eta(p^k) z^k = (1-z)^{-1/2}, eta*eta=1, h_U=b_U*eta gives a_U*a_U*mu = h_U*h_U (L-102010.4); Hardy relation reduces the two fields to one: |B_U(X)| <= const * H_U(X), H_U(X)=int_U^{4X/U} |H_{U,-}(Y)|^2 dY/Y.",
  C("PR696", "L-102010", "claims/lemmas/L-102010-half-divisor-symmetric-one-field-reduction.md"),
  required_fixes=["Keep support truncation before full-line Hardy (ARITH.VAUGHAN.HALF_DIVISOR fix)"],
  notes="At the pinned PR-696 head f4016db5 the file carries the SHARP Hardy constant 3 (T-102001.5, endorsed in row 43 conclusion and Reviewer B VERDICT_DELTA line 24 'Hardy norm 3 survive.'); the older copy at 89f99545 (103100 branch) carries 5 via Young. Transfer read with the truncated-field energy Ht per T-105051 Step 0 / T-105050 section 4.11. Defines gate HHFE102010.")
N("T-102001", "claim", "CONDITIONAL_EXACT",
  "Ratio-four two-field AND gate + sharp single-field constant: T-102001.5 gives |B_U(X)| <= 3 Ht_U(X) (truncated-field energy, per the T-105051 Step 0 repair of the annulus step); the two-energy AND gates LMTE102001 and DCTE102001 jointly imply BVD100310 and hence RH; superseded as interface by the single-field HHFE102010.",
  C("PR696", "T-102001", "claims/theorems/T-102001-ratiofour-two-field-and-gate.md"),
  notes="HONEST STATUS: no separate CLAIMS.tsv row; the sharp constant 3 is audited inside ARITH.VAUGHAN.HALF_DIVISOR (row 43 conclusion 'reduce to one with Hardy norm 3') and Reviewer B VERDICT_DELTA line 24.")

# ---------------- near-collision lane (PR 702) ----------------
N("L-103100", "claim", "VERIFIED",
  "Exact half-completed Haar Gram: the one-field energy admits the exact Gram expansion over pairs (m,n) with the explicit even piecewise-linear ratio-four autocorrelation R(log(m/n)) of A_- supported on 1/4<m/n<4 (L-103100.2).",
  C("PR702", "L-103100", "claims/lemmas/L-103100-exact-half-completed-haar-gram.md"),
  notes="CLAIMS.tsv ARITH.VAUGHAN.HAAR_GRAM VERIFIED.")
N("L-103101", "claim", "VERIFIED",
  "The Gram diagonal is unconditionally subpower: D = N^{o(1)}; the signed off-diagonal remains.",
  C("PR702", "L-103101", "claims/lemmas/L-103101-diagonal-is-unconditionally-subpower.md"),
  notes="CLAIMS.tsv ARITH.VAUGHAN.DIAGONAL VERIFIED.")
N("L-103102", "claim", "CONDITIONAL_EXACT",
  "Fractional Nyman representation + exact near-collision equivalence: Mellin-Plancherel gives int_U^{4N}|H_{U,N}|^2 dY/Y = (1/2pi) int_R |hat A_-(i gamma)|^2 |P_{U,N}(1/2+i gamma)|^2 d gamma with P_{U,N}(z)=sum_{U<n<=N} h_U(n) n^{-z} (a compactly weighted finite fractional Nyman-Beurling error, zeta^{-1/2} vs M_U zeta^{1/2}); since H>=0 and D=N^{o(1)}: O_+<=H and H<=D+O_+, so HCNC103100 <=> HHFE102010.",
  C("PR702", "L-103102", "claims/lemmas/L-103102-fractional-nyman-and-near-collision-equivalence.md"),
  notes="CLAIMS.tsv row 46 (ARITH.VAUGHAN.NEAR_COLLISION) rows the OPEN gate HCNC103100, not this proved reduction; the reduction/equivalence content is endorsed via ROUTE_EDGES line 15 (EQUIVALENCE_AFTER_DIAGONAL, CONDITIONAL_EXACT) and Reviewer B VERDICT_DELTA line 25 ('Haar Gram and subpower diagonal leave signed one-sided off-diagonal O_+'; 'First open half-divisor arrow').")

# ---------------- staircase lane (PR 703) ----------------
N("L-102100", "claim", "VERIFIED",
  "Survival-weighted mixed coboundary and staircase telescope (exact identity).",
  C("PR703", "L-102100", "claims/lemmas/L-102100-survival-weighted-mixed-coboundary-and-staircase-telescope.md"),
  notes="CLAIMS.tsv ARITH.STAIRCASE.SURVIVAL_COBOUNDARY VERIFIED. ROUTE_EDGES line 22 premise carries the typo 'SURVIVAL_COBBOUNDARY' (G-DANGLE class); repaired here to this node, defect recorded.")
N("L-102103", "claim", "VERIFIED",
  "Carrier-free filter N=J(I-S_2)(I-sqrt2 S_2) for the quadratic wavelet bridge: both channels are compact ratio-32 kernels with true half-order zero and no cancellation of the open-strip 1/zeta pole.",
  C("PR703", "L-102103", "claims/lemmas/L-102103-carrier-free-filter-for-the-quadratic-wavelet-bridge.md"),
  notes="CLAIMS.tsv ARITH.STAIRCASE.COMMON_FILTER VERIFIED.")
N("L-102105", "claim", "VERIFIED_WITH_FIXES",
  "Vector Vaughan reduction at U=X^{1/3}: all complete-lattice + Type-I terms are O(X^{-1/6}).",
  C("PR703", "L-102105", "claims/lemmas/L-102105-vector-vaughan-reduction.md"),
  required_fixes=["Use identical cutoff/source in both coordinates (ARITH.STAIRCASE.VECTOR_VAUGHAN fix)"])
N("T-102100", "claim", "CONDITIONAL_EXACT",
  "Carrier-free staircase/Perron frontier: T-102100.2 proves CFBB102100 => RH; the balanced two-channel subcritical matrix gate CFBB102100 itself is open; R-102100 refutes one-prime cone invariance.",
  C("PR703", "T-102100", "claims/theorems/T-102100-carrier-free-staircase-perron-frontier.md"),
  notes="CLAIMS.tsv ARITH.STAIRCASE.CFBB rows the open gate (OPEN_SUFFICIENT_FOR_RH, 'No local cone substitute'); the conditional implication content is the proved part.")
N("T-102110", "claim", "DEPOSITED_UNREVIEWED",
  "Near-collision incoming edge to the joint matrix: via L-102106, |B_A^dag(X)|+|B_Q^dag(X)| <= C H_U(X); hence HCNC103100 => N_A+N_Q = Y^{o(1)} => CFBB102100 holds with the zero matrix => RH (converse not asserted).",
  C("PR703", "T-102110", "claims/theorems/T-102110-near-collision-incoming-edge-to-the-joint-matrix.md"),
  notes="HONEST STATUS: PROVED CONDITIONAL COMPOSITION per deposit, but NO Reviewer A CLAIMS.tsv row and no ROUTE_EDGES row; the gate-order edge HCNC -> CFBB drawn from it is deposit-backed only (excluded in strict mode).")

# ---------------- phase/occupancy lane (PR 707) ----------------
N("L-103300", "claim", "VERIFIED",
  "Critical-carrier-normalized balanced homotopy: after exact critical carrier removal, the balanced completed-to-native homotopy has positive nonzero-phase Dirichlet form with only polylog finite-Euler gain.",
  C("PR707", "L-103300", "claims/lemmas/L-103300-critical-carrier-normalized-balanced-homotopy.md"),
  notes="CLAIMS.tsv ARITH.PHASE.CARRIER_NORMALIZED_HOMOTOPY VERIFIED.")
N("L-103303", "claim", "VERIFIED",
  "Centered cubic B-spline autocorrelation Gram factorization of the positive cubic compactifier.",
  C("PR707", "L-103303", "claims/lemmas/L-103303-centered-cubic-bspline-autocorrelation.md"),
  notes="CLAIMS.tsv ARITH.CUBIC.GRAM VERIFIED.")
N("L-103304", "claim", "VERIFIED",
  "The half-divisor field is the literal convolution square root of the Moebius source.",
  C("PR707", "L-103304", "claims/lemmas/L-103304-half-divisor-field-is-source-square-root.md"),
  notes="CLAIMS.tsv ARITH.HALF_DIVISOR.SOURCE_SQRT VERIFIED.")
N("T-103300", "claim", "CONDITIONAL_EXACT",
  "Balanced phase amplitude is closed; physical occupancy is the common surviving frontier: T-103300.4 proves {balanced homotopy phase Dirichlet form, half-divisor source sqrt/cubic Gram, BPOE103300} => HHFE102010 => RH; firewall R-103300 blocks invariant-cone / regional-absolute substitutes for BPOE.",
  C("PR707", "T-103300", "claims/theorems/T-103300-balanced-phase-amplitude-and-physical-occupancy-frontier.md"),
  notes="CLAIMS.tsv ARITH.OCCUPANCY.BPOE rows the open gate; Reviewer B: 'BPOE is first unsupported arrow', ACCEPT_HIGHEST_PRIORITY_OPEN_INTERFACE.")

# ---------------- BVD100310 mechanism lemmas (PR 685) — deposit-only ----------------
N("L-100310", "claim", "DEPOSITED_UNREVIEWED",
  "One extra safe half-order notch closes the complete Type-I channel (exact analytic theorem on the minimal ratio-eight Moebius wavelet K_0 of PR 674/675).",
  C("PR685", "L-100310", "claims/lemmas/L-100310-extra-half-order-notch-and-type-I-decay.md"),
  notes="HONEST STATUS: git grep '100310' over Reviewer A review/2026-08-21/arithmetic/CLAIMS.tsv @ 55fe0b6f = 0 matches — no ledger row. Mechanism carrier of EDGE.HHFE.RH; the edge itself IS registered (ROUTE_EDGES line 16).")
N("L-100311", "claim", "DEPOSITED_UNREVIEWED",
  "Exact Vaughan decomposition leaves one compact balanced trilinear form (one arithmetic form open).",
  C("PR685", "L-100311", "claims/lemmas/L-100311-vaughan-decomposition-to-one-balanced-trilinear.md"),
  notes="No Reviewer A CLAIMS.tsv row; mechanism carrier of EDGE.HHFE.RH.")
N("L-100312", "claim", "DEPOSITED_UNREVIEWED",
  "The balanced Vaughan deficit is an exact RH-equivalent terminal gate (proved conditional conclusion + converse), at U_X=floor(X^{1/3}).",
  C("PR685", "L-100312", "claims/lemmas/L-100312-balanced-vaughan-deficit-is-rh-equivalent.md"),
  notes="No Reviewer A CLAIMS.tsv row; Mellin-Landau consumer half of BVD100310, used by T-102001.7/L-102010.14 to give HHFE102010 => RH.")

# ---------------- gate hypothesis nodes ----------------
N("HYP.HHFE102010", "hypothesis", "OPEN_SUFFICIENT_FOR_RH",
  "GATE HHFE102010: with h_U=(mu 1_{n>U})*eta (eta multiplicative, sum_k eta(p^k)z^k=(1-z)^{-1/2}), A_-(y)=1 on (1,2), -sqrt(2) on (2,4), 0 else, and the TRUNCATED-field energy Ht_U(X)=int_U^{4X/U}|sum_{U<n<=X/U} h_U(n) n^{-1/2} A_-(Y/n)|^2 dY/Y, U_X=floor(X^{1/3}): int_{2^L}^{2^{L+1}} Ht_{U_X}(X) dX/X = 2^{o(L)} as L -> infinity. [Read with Ht per T-105051 Step 0 / T-105050 section 4.11: the deposited untruncated form's transfer inequality has an unjustified annulus step; the proved transfer is |B_U| <= 3 Ht_U, and the L-103102 equivalence with HCNC103100 holds for the truncated object.]",
  C("PR696", "HHFE102010", "claims/lemmas/L-102010-half-divisor-symmetric-one-field-reduction.md"),
  notes="Interface node ARITH.VAUGHAN.HHFE of Reviewer A's graph (hypothesis string only — no CLAIMS.tsv row of its own; G-DANGLE repair: declared here as a typed node). Listed among 'valid sufficient open conditions' (REPORT.md @ 55fe0b6f). Equivalent to HCNC103100 after the proved diagonal (L-103101 + L-103102).")
N("HYP.HCNC103100", "hypothesis", "OPEN_SUFFICIENT_FOR_RH",
  "GATE HCNC103100: int_{2^L}^{2^{L+1}} [O_{U_X,N_X}]_+ dX/X = 2^{o(L)}, where O_{U,N} = sum_{U<m,n<=N, m!=n, 1/4<m/n<4} h_U(m) h_U(n) (mn)^{-1/2} R(log(m/n)), R the explicit even piecewise-linear ratio-four autocorrelation of A_- (L-103100.2), U_X=floor(X^{1/3}), N_X=floor(X/U_X).",
  C("PR702", "HCNC103100", "claims/lemmas/L-103102-fractional-nyman-and-near-collision-equivalence.md"),
  notes="CLAIMS.tsv row 46 ARITH.VAUGHAN.NEAR_COLLISION OPEN_SUFFICIENT_FOR_RH; 'Do not replace by absolute correlation.'")
N("HYP.CFBB102100", "hypothesis", "OPEN_SUFFICIENT_FOR_RH",
  "GATE CFBB102100: there exists a fixed nonnegative 2x2 matrix M with rho(M)<1 and source-faithful positive completions such that (N_Q,N_A)^T <= M (N_Q,N_A)^T + Y^{o(1)}(1,1)^T (equivalently a<1, d<1, bc<(1-a)(1-d)).",
  C("PR703", "CFBB102100", "claims/theorems/T-102100-carrier-free-staircase-perron-frontier.md"),
  notes="CLAIMS.tsv row 62 ARITH.STAIRCASE.CFBB OPEN_SUFFICIENT_FOR_RH; 'No local cone substitute.'")
N("HYP.BPOE103300", "hypothesis", "OPEN_SUFFICIENT_FOR_RH",
  "GATE BPOE103300: the observation map O_L (prime exponent vector -> integer product, compact kernel -> product, restricted to the actual dyadic shell, retaining same-occurrence cutoff data) satisfies ||O_L||^2_{H_L -> L^2(dX/X)} = 2^{o(L)}.",
  C("PR707", "BPOE103300", "claims/theorems/T-103300-balanced-phase-amplitude-and-physical-occupancy-frontier.md"),
  notes="CLAIMS.tsv row 66 ARITH.OCCUPANCY.BPOE OPEN_SUFFICIENT_FOR_RH — 'highest-priority open interface'; firewall R-103300: no invariant-cone or regional-absolute substitute.")
N("HYP.FCHD67", "hypothesis", "OPEN_SUFFICIENT_FOR_RH",
  "GATE FCHD67: a source-faithful realization, or a sufficient global one-sided estimate, for the complete paired first-owner current family Delta_i^fut f = (I-U_i) prod_{h>i}(I - r_h U_h) f (L-99601.8) in the actual SHARP target/common-row source.",
  C("PR652", "FCHD67", "claims/lemmas/L-99601-sequential-first-owner-euler-hazard.md"),
  notes="CLAIMS.tsv row 17 ARITH.FCHD67 OPEN_SUFFICIENT_FOR_RH ('open arithmetic producer', first_broken_arrow 'future-current estimate'). Nonlocal; honest replacement for the refuted alpha promotion (R-99600). Reviewer B: only sufficient, and the two-row consumer needs SIMULTANEOUS native fixed-row production.")
N("HYP.WX53POS", "hypothesis", "OPEN_SUFFICIENT_FOR_RH",
  "GATE (five-three scalar): W_X = 5 c_X(2) + 3 c_X(3) >= 0 for all sufficiently large X (equivalently subpower negative mass of the fixed 5:3 detector), where c_X(j) = sum_{n<=X/j} mu(n) n^{-1/2} Q_{X/n}(j).",
  C("PR649", "ARITH.FIVE_THREE.NEGATIVE_MASS", "claims/lemmas/L-99261-five-three-row-zero-free-mellin-witness.md"),
  notes="Hypothesis string ARITH.FIVE_THREE.NEGATIVE_MASS of ROUTE_EDGES line 3 ('fixed scalar sign/negative mass absent'), declared as a typed node (G-DANGLE repair).")
N("HYP.HNM67", "hypothesis", "OPEN_SUFFICIENT_FOR_RH",
  "GATE HNM67 (subpower negative mass): N(T) = int_1^T max(-H_67(x),0) dx/x = T^{o(1)} for the fixed zero-safe scalar H_67(x) = Psi(x) - 67^{-1/2} Psi(x/67), Psi(x)=sum_{n<=x} mu(n) n^{-1/2}(4 sqrt(x/n)-3); the one-octave log-box form int_{X/67}^X H_67(t) dt/t >= 0 eventually also suffices.",
  C("PR653", "ARITH.FIXED_DETECTOR.SUBPOWER_NEGATIVE_MASS", "claims/lemmas/L-99270-zero-free-smoothing-and-negative-mass.md"),
  notes="Hypothesis string of ROUTE_EDGES line 4, declared as typed node. Same gate as L-99603 (HNM67) @ PR 652. 10^8 finite certificate L-99252 (PR 647) is RETAINED_HEAVY_CERTIFICATE — a finite certificate, never merged into this global edge (Reviewer C lifecycle rule).")
N("HYP.ROWS23", "hypothesis", "OPEN_SUFFICIENT_FOR_RH",
  "Rows 2 and 3 eventually nonnegative: c_X(2) >= 0 and c_X(3) >= 0 for all sufficiently large X, each with finite Mellin abscissa (or the L-99602.6 holomorphic-defect split with defect Mellin-holomorphic on Re s>0).",
  C("PR652", "ARITH.ROWS23.NONNEGATIVE", "claims/lemmas/L-99602-exact-two-row-mellin-landau-consumer.md"),
  notes="Intermediate open interface (hypothesis string ARITH.ROWS23.NONNEGATIVE of ROUTE_EDGES lines 2 and 6, declared as typed node). Implied by FCHD67 through L-99601.")

# ---------------- 105xxx deposited context nodes (this session's lane) ----------------
ctx105 = "CONTEXT NODE, DEPOSITED-UNREVIEWED (branch claude/riemann-proof-review-8nz34i tip; no review-wave ledger row; NOT a premise of any RH edge)."
N("T-105000", "claim", "DEPOSITED_UNREVIEWED",
  "Hazard-budget theorem and conservation trichotomy: every admissible hierarchical factor-67 scheme pays (1+o(1))/p per rough prime for native first-order delivery, and the total price over a fixed rough alphabet diverges — a method-space classification unifying seven prior refutations; not progress on RH itself.",
  C("S105", "T-105000", "claims/theorems/T-105000-hazard-budget-and-conservation-trichotomy.md"), notes=ctx105)
N("O-105010", "claim", "DEPOSITED_UNREVIEWED",
  "Budget feasibility selects the moving-cut (Vaughan-type) architecture: a fixed factor-67 cut pays sum_{67<=p<=Y} 1/p = loglog Y - O(1) -> infinity, while rough primes p > Y^theta pay log(1/theta)+o(1) — architecture selection consistent with, and context for, the U_X = X^{1/3} Vaughan gate; no positivity theorem claimed.",
  C("S105", "O-105010", "claims/observations/O-105010-moving-cut-budget-feasibility-selects-the-vaughan-architecture.md"),
  notes=ctx105 + " Architecture selection is CONTEXT for the HHFE gate, not a premise of any RH edge.")
N("L-105031", "claim", "DEPOSITED_UNREVIEWED",
  "Maximal transport license: exact reduction (Theorem R), removal of the 87.36 cap, equivalence with the signed rows, and log-cost of score debt; finite-range feasibility x <= 10^6; the arithmetic core is open and stated as such.",
  C("S105", "L-105031", "claims/lemmas/L-105031-maximal-license-reduction-and-the-removal-of-the-hall-cap.md"), notes=ctx105)
N("L-105032", "claim", "DEPOSITED_UNREVIEWED",
  "The moving boundary cancels the pole but not the log: at theta=1/2 the germ ledger is +/-4*log(s-1/2) and the pieces are not individually regular (corrected deposit; the first push's bounded-pieces assertion was wrong and is recorded).",
  C("S105", "L-105032", "claims/lemmas/L-105032-the-moving-boundary-cancels-the-pole-the-theta-half-ledger.md"), notes=ctx105)
N("T-105040", "claim", "DEPOSITED_UNREVIEWED",
  "The smooth half closes: the frozen 61-smooth aggregate-licensed transport block is feasible for every real x >= 2, unconditionally (elementary-finite + certified computation); model/deformation theorem — no deposited consumer consumes the frozen block at x >= 67; RH not addressed.",
  C("S105", "T-105040", "claims/theorems/T-105040-the-smooth-half-closes.md"),
  notes=ctx105 + " Smooth-half closure is CONTEXT for the gate lattice, not a premise of any RH edge.")

# ---------------- edges ----------------
edges = []
def E(eid, prem, concl, typ, src, notes=None, mode="strict"):
    e = {"edge_id": eid, "premises": prem, "arity": len(prem), "conclusion": concl,
         "type": typ, "source_coordinates": src, "trust_mode": mode}
    if notes: e["notes"] = notes
    edges.append(e)

RE = "review/2026-08-21/arithmetic/ROUTE_EDGES.tsv"
def src_reva(line, extra=None):
    s = [{"claim_id": "ROUTE_EDGES line %d" % line, "path": RE, "branch": BR["REVA"], "sha": SHA["REVA"]}]
    if extra: s += extra
    return s

E("E-NATIVE-FCHD", ["L-99601", "HYP.FCHD67"], "HYP.ROWS23", "CONDITIONAL_IMPLICATION",
  src_reva(6, [C("PR652", "L-99601 s.4", "claims/lemmas/L-99601-sequential-first-owner-euler-hazard.md")]),
  notes="Reviewer A EDGE.NATIVE.FCHD (PROVED_CONDITIONAL, verdict CONDITIONAL_EXACT, first_missing_input ARITH.FCHD67): FCHD67 + sequential first-owner identity => rows 2,3 nonnegative.")
E("E-MELLIN-ROWS23", ["L-99602", "HYP.ROWS23"], "RH", "CONDITIONAL_IMPLICATION",
  src_reva(2, [C("PR652", "L-99602.1-.6", "claims/lemmas/L-99602-exact-two-row-mellin-landau-consumer.md")]),
  notes="Reviewer A EDGE.MELLIN.ROWS23 (CONDITIONAL_EXACT). Landau backbone: L-99272 (VERIFIED_WITH_FIXES); defect variant uses L-99282 + L-99281 (L-99281 not separately rowed).")
E("E-MELLIN-FIVE-THREE", ["L-99261", "HYP.WX53POS"], "RH", "CONDITIONAL_IMPLICATION",
  src_reva(3, [C("PR649", "L-99261.4 s.4", "claims/lemmas/L-99261-five-three-row-zero-free-mellin-witness.md")]),
  notes="Reviewer A EDGE.MELLIN.FIVE_THREE (CONDITIONAL_EXACT): numerator -3(2^{-z}-1)(2^{-z}-2) zero-free in the strip; Landau one-sign.")
E("E-MELLIN-NEGMASS", ["L-99270", "HYP.HNM67"], "RH", "CONDITIONAL_IMPLICATION",
  src_reva(4, [C("PR653", "L-99270.10-.13", "claims/lemmas/L-99270-zero-free-smoothing-and-negative-mass.md")]),
  notes="Reviewer A EDGE.MELLIN.NEGATIVE_MASS (CONDITIONAL_EXACT), exact arity 2 preserved; specialized Landau theorem L-99272 is the analytic backbone (node present, recorded here rather than widening the reviewed arity).")
E("E-VAUGHAN-HALF-FIELD", ["L-102001", "L-102009", "L-102010"], "HYP.HHFE102010", "PROVED_REDUCTION",
  src_reva(14),
  notes="Reviewer A EDGE.VAUGHAN.HALF_FIELD (PROVED_REDUCTION, CONDITIONAL_EXACT, first_missing_input 'HHFE field energy'). REDUCTION INTO the open interface: never establishes HYP.HHFE102010 (typed semantics resolving G-CONDITIONAL-001).")
E("E-NC-TO-HHFE", ["L-103100", "L-103101", "HYP.HCNC103100"], "HYP.HHFE102010", "EQUIVALENCE_AFTER_DIAGONAL",
  src_reva(15, [C("PR702", "L-103102 (H<=D+O_+, D=N^{o(1)})", "claims/lemmas/L-103102-fractional-nyman-and-near-collision-equivalence.md")]),
  notes="Forward direction of Reviewer A EDGE.VAUGHAN.NEAR_COLLISION: HCNC + Haar Gram + subpower diagonal => HHFE.")
E("E-HHFE-TO-NC", ["L-103100", "L-103101", "L-103102", "HYP.HHFE102010"], "HYP.HCNC103100", "EQUIVALENCE_AFTER_DIAGONAL",
  src_reva(15, [C("PR702", "L-103102 (O_+<=H)", "claims/lemmas/L-103102-fractional-nyman-and-near-collision-equivalence.md")]),
  notes="Reverse direction of the same equivalence (edge type EQUIVALENCE_AFTER_DIAGONAL asserts both): O_+ <= H since H >= 0 and D >= 0.")
E("E-HHFE-RH", ["HYP.HHFE102010"], "RH", "CONDITIONAL_IMPLICATION",
  src_reva(16, [C("PR696", "T-102001.5 (|B_U(X)| <= 3 Ht_U(X), truncated-field energy per T-105051 Step 0) + L-102010.14", "claims/theorems/T-102001-ratiofour-two-field-and-gate.md"),
                C("PR685", "L-100310..L-100312 (BVD100310 Type-I + Mellin-Landau consumer)", "claims/lemmas/L-100312-balanced-vaughan-deficit-is-rh-equivalent.md")]),
  notes="Reviewer A EDGE.HHFE.RH (OPEN_SUFFICIENT_FOR_RH, first_missing_input HHFE102010), exact arity 1 preserved. CAVEAT carried honestly: the mechanism lemmas L-100310..L-100312 (PR 685 @ 4f69b765...) have no Reviewer A CLAIMS.tsv rows; the implication is registered as a route edge and endorsed in REPORT.md ('HHFE102010 ... valid sufficient open conditions').")
E("E-STAIRCASE-CFBB", ["L-102100", "L-102103", "L-102105", "HYP.CFBB102100"], "RH", "HYPEREDGE",
  src_reva(22, [C("PR703", "T-102100.2", "claims/theorems/T-102100-carrier-free-staircase-perron-frontier.md")]),
  notes="Reviewer A EDGE.STAIRCASE.CFBB (OPEN_SUFFICIENT_FOR_RH, missing 'CFBB102100 arithmetic matrix'). Source premise name typo 'ARITH.STAIRCASE.SURVIVAL_COBBOUNDARY' repaired to L-102100 (defect recorded, not silently normalized: see provenance_defects).")
E("E-BPOE-HHFE", ["L-103300", "L-103303", "L-103304", "HYP.BPOE103300"], "HYP.HHFE102010", "HYPEREDGE",
  src_reva(23, [C("PR707", "T-103300.4", "claims/theorems/T-103300-balanced-phase-amplitude-and-physical-occupancy-frontier.md")]),
  notes="Reviewer A EDGE.BPOE.HHFE: balanced homotopy phase Dirichlet form AND half-divisor source sqrt/cubic Gram AND BPOE103300 => HHFE102010.")
E("E-BPOE-RH", ["HYP.BPOE103300"], "RH", "CONDITIONAL_IMPLICATION",
  src_reva(24),
  notes="Reviewer A EDGE.BPOE.RH ('highest-priority open route'); composition of E-BPOE-HHFE with E-HHFE-RH.")
E("E-HCNC-CFBB", ["T-102110", "HYP.HCNC103100"], "HYP.CFBB102100", "CONDITIONAL_IMPLICATION",
  [C("PR703", "T-102110 (via L-102106: |B_A^dag|+|B_Q^dag| <= C H_U)", "claims/theorems/T-102110-near-collision-incoming-edge-to-the-joint-matrix.md")],
  notes="DEPOSIT-BACKED ONLY (T-102110 has no CLAIMS.tsv/ROUTE_EDGES row): HCNC103100 => CFBB102100 with the zero matrix. Excluded from strict (reviewer-backed) computations; included in 'deposited' mode. Converse not asserted (CFBB potentially weaker).",
  mode="deposited")

aliases = [
    {"alias_id": "ARITH.SHARP.SEQUENTIAL_FIRST_OWNER", "canonical_semantic_id": "L-99601", "targets": ["L-99601"]},
    {"alias_id": "ARITH.SHARP.ALPHA_NATIVE_PROMOTION", "canonical_semantic_id": "R-99600", "targets": ["R-99600"]},
    {"alias_id": "CONSUMER.MELLIN.FIXED_ROW", "canonical_semantic_id": "L-99602", "targets": ["L-99602"]},
    {"alias_id": "CONSUMER.MELLIN.TWO_ROW", "canonical_semantic_id": "L-99602", "targets": ["L-99602"]},
    {"alias_id": "CONSUMER.MELLIN.FIVE_THREE", "canonical_semantic_id": "L-99261", "targets": ["L-99261"]},
    {"alias_id": "CONSUMER.MELLIN.NEGATIVE_MASS", "canonical_semantic_id": "L-99270", "targets": ["L-99270"]},
    {"alias_id": "CONSUMER.MELLIN.ZERO_SAFE_BOX", "canonical_semantic_id": "L-99270", "targets": ["L-99270"]},
    {"alias_id": "CONSUMER.MELLIN.LANDAU_SPECIALIZED", "canonical_semantic_id": "L-99272", "targets": ["L-99272"]},
    {"alias_id": "CONSUMER.MELLIN.HOLOMORPHIC_DEFECT", "canonical_semantic_id": "L-99282", "targets": ["L-99282"]},
    {"alias_id": "ARITH.FCHD67", "canonical_semantic_id": "HYP.FCHD67", "targets": ["HYP.FCHD67"]},
    {"alias_id": "ARITH.ROWS23.NONNEGATIVE", "canonical_semantic_id": "HYP.ROWS23", "targets": ["HYP.ROWS23"]},
    {"alias_id": "ARITH.FIVE_THREE.NEGATIVE_MASS", "canonical_semantic_id": "HYP.WX53POS", "targets": ["HYP.WX53POS"]},
    {"alias_id": "ARITH.FIXED_DETECTOR.SUBPOWER_NEGATIVE_MASS", "canonical_semantic_id": "HYP.HNM67", "targets": ["HYP.HNM67"]},
    {"alias_id": "HNM67", "canonical_semantic_id": "HYP.HNM67", "targets": ["HYP.HNM67"]},
    {"alias_id": "ARITH.VAUGHAN.LARGE_DIVISOR", "canonical_semantic_id": "L-102001", "targets": ["L-102001"]},
    {"alias_id": "ARITH.VAUGHAN.RATIO4_TWO_FIELD", "canonical_semantic_id": "L-102009", "targets": ["L-102009"]},
    {"alias_id": "ARITH.VAUGHAN.HALF_DIVISOR", "canonical_semantic_id": "L-102010", "targets": ["L-102010"]},
    {"alias_id": "ARITH.VAUGHAN.HHFE", "canonical_semantic_id": "HYP.HHFE102010", "targets": ["HYP.HHFE102010"]},
    {"alias_id": "HHFE102010", "canonical_semantic_id": "HYP.HHFE102010", "targets": ["HYP.HHFE102010"]},
    {"alias_id": "ARITH.VAUGHAN.HAAR_GRAM", "canonical_semantic_id": "L-103100", "targets": ["L-103100"]},
    {"alias_id": "ARITH.VAUGHAN.DIAGONAL", "canonical_semantic_id": "L-103101", "targets": ["L-103101"]},
    {"alias_id": "ARITH.VAUGHAN.NEAR_COLLISION", "canonical_semantic_id": "HYP.HCNC103100", "targets": ["HYP.HCNC103100"]},
    {"alias_id": "HCNC103100", "canonical_semantic_id": "HYP.HCNC103100", "targets": ["HYP.HCNC103100"]},
    {"alias_id": "ARITH.STAIRCASE.SURVIVAL_COBOUNDARY", "canonical_semantic_id": "L-102100", "targets": ["L-102100"]},
    {"alias_id": "ARITH.STAIRCASE.COMMON_FILTER", "canonical_semantic_id": "L-102103", "targets": ["L-102103"]},
    {"alias_id": "ARITH.STAIRCASE.VECTOR_VAUGHAN", "canonical_semantic_id": "L-102105", "targets": ["L-102105"]},
    {"alias_id": "ARITH.STAIRCASE.CFBB", "canonical_semantic_id": "HYP.CFBB102100", "targets": ["HYP.CFBB102100"]},
    {"alias_id": "CFBB102100", "canonical_semantic_id": "HYP.CFBB102100", "targets": ["HYP.CFBB102100"]},
    {"alias_id": "ARITH.PHASE.CARRIER_NORMALIZED_HOMOTOPY", "canonical_semantic_id": "L-103300", "targets": ["L-103300"]},
    {"alias_id": "ARITH.CUBIC.GRAM", "canonical_semantic_id": "L-103303", "targets": ["L-103303"]},
    {"alias_id": "ARITH.HALF_DIVISOR.SOURCE_SQRT", "canonical_semantic_id": "L-103304", "targets": ["L-103304"]},
    {"alias_id": "ARITH.OCCUPANCY.BPOE", "canonical_semantic_id": "HYP.BPOE103300", "targets": ["HYP.BPOE103300"]},
    {"alias_id": "BPOE103300", "canonical_semantic_id": "HYP.BPOE103300", "targets": ["HYP.BPOE103300"]},
    {"alias_id": "BVD100310", "canonical_semantic_id": "L-100312", "targets": ["L-100310", "L-100311", "L-100312"]},
]

provenance_defects = [
    {"defect_id": "PROV.A.MISSING_LEADING_E", "artifact": "review/2026-08-21/arithmetic/CLAIMS.tsv row CONSUMER.MELLIN.ZERO_SAFE_BOX @ " + SHA["REVA"],
     "observed": "39-character SHA 928fd615d753882706bb88c51b717bd8d4a86ba", "expected": SHA["PR653"],
     "disposition": "Repaired in this canonical registry only; source review branch untouched (Reviewer C PROVENANCE_DEFECTS.tsv disposition)."},
    {"defect_id": "G-DANGLE.STAIRCASE_TYPO", "artifact": RE + " line 22 @ " + SHA["REVA"],
     "observed": "premise name ARITH.STAIRCASE.SURVIVAL_COBBOUNDARY (double B) does not match CLAIMS.tsv semantic id ARITH.STAIRCASE.SURVIVAL_COBOUNDARY",
     "expected": "ARITH.STAIRCASE.SURVIVAL_COBOUNDARY -> node L-102100",
     "disposition": "Repaired to L-102100 in edge E-STAIRCASE-CFBB; defect recorded (Reviewer B G-DANGLE-001 class)."},
    {"defect_id": "LEDGER.MISSING_ROWS.BVD100310", "artifact": "review/2026-08-21/arithmetic/CLAIMS.tsv @ " + SHA["REVA"],
     "observed": "L-100310, L-100311, L-100312 (PR 685 @ " + SHA["PR685"] + ") have no ledger rows although EDGE.HHFE.RH routes through them",
     "expected": "independent review rows for the BVD100310 consumer chain",
     "disposition": "Nodes carried as DEPOSITED_UNREVIEWED; flagged as an integration obligation."},
    {"defect_id": "LEDGER.MISSING_ROW.T-102110", "artifact": "review/2026-08-21/arithmetic/CLAIMS.tsv @ " + SHA["REVA"],
     "observed": "T-102110 (HCNC => CFBB composition) has no ledger row",
     "expected": "review row before the gate order HCNC -> CFBB is promoted",
     "disposition": "Edge E-HCNC-CFBB carried at trust_mode=deposited only."},
    {"defect_id": "LEDGER.MISSING_ROW.L-99281", "artifact": "review/2026-08-21/arithmetic/CLAIMS.tsv @ " + SHA["REVA"],
     "observed": "L-99281 (subpower defect resolvent) not separately rowed; verified only inside the PR 650 triad",
     "expected": "own row if the holomorphic-defect producer form is ever used",
     "disposition": "Node carried as DEPOSITED_UNREVIEWED."},
]

graph = {
    "meta": {
        "name": "assembly_graph — transport program route lattice to RH",
        "built": "2026-08-22", "builder": "swarm lane A1",
        "rh_status": "UNPROVED — no proved-only path to RH exists in this graph (asserted by validator.py; matches Reviewer B strict cross-review parser sanity result @ 945a6eec3406cce8f6cd63eba6c69fb60676c41d)",
        "spec": "Reviewer B fail-closed contract (CROSS_REVIEW_REPORT.md + GRAPH_DEFECTS.tsv @ 945a6eec...) + Reviewer C path-qualified semantic IDs (INTEGRATION_HANDOFF.md + PROVENANCE_DEFECTS.tsv @ a520556a...)",
        "status_vocabulary": ["VERIFIED", "VERIFIED_WITH_FIXES", "CONDITIONAL_EXACT", "OPEN_SUFFICIENT_FOR_RH", "OPEN_RH_EQUIVALENT", "REFUTED", "DEPOSITED_UNREVIEWED"],
        "edge_type_vocabulary": ["PROVED_REDUCTION", "CONDITIONAL_IMPLICATION", "EQUIVALENCE_AFTER_DIAGONAL", "HYPEREDGE"],
        "edge_semantics": {
            "PROVED_REDUCTION": "proved reduction INTO an open interface; never establishes a hypothesis conclusion",
            "CONDITIONAL_IMPLICATION": "establishes conclusion when all premises are established",
            "EQUIVALENCE_AFTER_DIAGONAL": "directional instance of a proved equivalence; establishes conclusion when all premises are established",
            "HYPEREDGE": "multi-premise AND gate; establishes conclusion when all premises are established",
            "trust_mode": "strict = reviewer-backed (all mechanism claims have review-wave ledger rows); deposited = mechanism includes DEPOSITED_UNREVIEWED claims"
        },
        "gates": ["HYP.HHFE102010", "HYP.HCNC103100", "HYP.CFBB102100", "HYP.BPOE103300", "HYP.FCHD67", "HYP.WX53POS", "HYP.HNM67", "HYP.ROWS23"],
    },
    "nodes": nodes, "edges": edges, "aliases": aliases,
    "provenance_defects": provenance_defects,
}

out = os.path.join(D, "assembly_graph.json")
with open(out, "w") as f:
    json.dump(graph, f, indent=1)
print("wrote", out, "| nodes:", len(nodes), "| edges:", len(edges), "| aliases:", len(aliases))
