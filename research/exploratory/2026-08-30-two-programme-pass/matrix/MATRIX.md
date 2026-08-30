# Cross-world survival/mechanism matrix (as built, 2026-08-30)

12 of 13 planned world records built (native_imports lost to session
limits; deferred). Cell = STATUS(rigor): H/F/O/C/- with p=proved-here,
i=imported, w=exact-witness, r=refuted-by-witness, n=numeric, s=synthetic,
o=open. Witness index below. rh_established=false throughout.

## Ladder view (#764)

| world | L0 | L1 | L2 | L3 | L4 | L5 | L6 | L7 | L8 | L9 | critical line |
|---|---|---|---|---|---|---|---|---|---|---|---|
| beurling | H(p) | H(p) | H(p) | H(w) | O(o) | O(o) | O(o) | O(o) | H(s) | F(i) | OPEN |
| counterfeit_deleted_euler | H(p) | H(p) | H(p) | H(p) | H(p) | F(p) | F(p) | H(p) | H(p) | F(p) | FALSE |
| counterfeit_random_phase | H(p) | H(p) | H(p) | H(p) | H(p) | O(o) | O(o) | H(p) | H(s) | O(o) | NOT_FORMULATED |
| counterfeit_wrong_gamma | H(p) | H(p) | H(p) | H(w) | H(p) | F(p) | F(p) | H(p) | F(p) | F(p) | NOT_FORMULATED |
| davenport_heilbronn | H(p) | F(r) | F(r) | F(r) | H(p) | H(p) | H(p) | O(o) | F(r) | F(i) | FALSE |
| dirichlet_mod5 | H(p) | H(p) | H(p) | H(w) | H(p) | H(i) | H(i) | H(p) | H(i) | H(i) | CONJECTURE |
| elliptic_11a | H(p) | H(p) | H(p) | H(p) | H(p) | H(i) | H(i) | H(i) | H(i) | C(o) | CONJECTURE |
| epstein_pair | H(p) | F(r) | F(r) | F(r) | F(r) | H(i) | H(i) | F(r) | H(p) | F(i) | FALSE |
| ff_elliptic_f5 | H(p) | H(p) | H(w) | H(w) | H(p) | H(p) | H(p) | H(w) | H(i) | H(p) | THEOREM |
| ihara_nonramanujan | H(p) | H(w) | H(w) | H(w) | H(p) | H(p) | H(p) | H(w) | H(w) | F(r) | FALSE |
| ihara_ramanujan | H(w) | H(w) | H(w) | H(w) | H(p) | H(i) | H(p) | H(w) | H(p) | H(p) | THEOREM |
| zeta | H(i) | H(p) | H(i) | H(w) | H(w) | H(i) | H(i) | H(w) | H(i) | C(o) | CONJECTURE |

## Mechanism view (#763)

| world | EULER | DUALITY | TRACE | POSITIVITY | TENSOR | FAMILY | critical line |
|---|---|---|---|---|---|---|---|
| beurling | H(p) | O(o) | O(o) | O(o) | O(o) | H(i) | OPEN |
| counterfeit_deleted_euler | H(p) | F(p) | H(p) | F(p) | H(p) | H(p) | FALSE |
| counterfeit_random_phase | H(p) | O(o) | O(o) | O(o) | H(p) | O(o) | NOT_FORMULATED |
| counterfeit_wrong_gamma | H(p) | F(p) | F(p) | -(p) | H(p) | H(s) | NOT_FORMULATED |
| davenport_heilbronn | F(r) | H(p) | O(o) | F(i) | O(o) | H(p) | FALSE |
| dirichlet_mod5 | H(p) | H(i) | H(i) | O(o) | H(p) | H(p) | CONJECTURE |
| elliptic_11a | H(p) | H(i) | H(i) | H(p) | H(w) | H(i) | CONJECTURE |
| epstein_pair | F(r) | H(i) | H(i) | F(i) | F(r) | H(p) | FALSE |
| ff_elliptic_f5 | H(w) | H(p) | H(w) | H(p) | H(w) | H(p) | THEOREM |
| ihara_nonramanujan | H(w) | H(p) | H(p) | F(r) | H(w) | H(w) | FALSE |
| ihara_ramanujan | H(w) | H(p) | H(p) | H(p) | H(w) | H(i) | THEOREM |
| zeta | H(i) | H(i) | H(i) | O(o) | H(w) | H(i) | CONJECTURE |

## Witness index (every FAILS / REFUTED_BY_WITNESS cell)

- **beurling.L9_EXPLICIT_FORMULA_POSITIVITY** [IMPORTED_THEOREM]: CLASS-LEVEL FAILS (imported row (a)): there exists a Beurling generalized prime system whose integer counting function is regular enough to yield PNT-type asymptotics (with de la Vallee Poussin-shape error), while its ze
- **counterfeit_deleted_euler.L5_CONDUCTOR_GAMMA_ROOT** [PROVED_HERE]: no canonical (conductor, gamma, root number) datum exists FOR zeta_odd ITSELF: any such datum would complete zeta_odd to a functional equation of standard reflection type, and every such FE is refuted exactly by the L6 z
- **counterfeit_deleted_euler.L6_CONTINUATION_FE** [PROVED_HERE]: continuation HOLDS (meromorphic on C, simple pole at s = 1, via the deleted-factor identity and import I1) — the FAILURE is the functional equation.  EXACT ZERO-SYMMETRY WITNESS.  For every nonzero integer k put s_k = 2 
- **counterfeit_deleted_euler.L9_EXPLICIT_FORMULA_POSITIVITY** [PROVED_HERE]: the explicit-formula PRIME SIDE survives (see TRACE_FORMULA: nonnegative von Mangoldt coefficients on odd prime powers, exact), but PRINCIPLED POSITIVITY FAILS: any Weil-type positivity criterion asserting that all non-r
- **counterfeit_deleted_euler.DUALITY_FE** [PROVED_HERE]: absent, and PROVABLY unrestorable: the zero set of zeta_odd is not s -> 1-s symmetric (exact witness family s_k = 2 pi i k / log 2, zeros with non-zero reflections — L6).  This is the isolated-mechanism row: EULER PRODUC
- **counterfeit_deleted_euler.POSITIVITY_PURITY** [PROVED_HERE]: local purity is PRESENT (every odd-prime factor is weight-0 pure with inverse root on |alpha| = 1, exact — L4), yet NO global positivity mechanism can exist: 'all non-real strip zeros on Re s = 1/2' is FALSE by the exact
- **counterfeit_wrong_gamma.L5_CONDUCTOR_GAMMA_ROOT** [PROVED_HERE]: THE ATTACHED GAMMA IS NOT CANONICAL, AND NO CHOICE OF ROOT NUMBER OR CONDUCTOR RESCUES IT.  Parity mismatch (exact): chi_5(-1) = chi_5(4) = +1, so the canonical archimedean datum is a = (1 - chi_5(-1))/2 = 0, i.e. Gamma_
- **counterfeit_wrong_gamma.L6_CONTINUATION_FE** [PROVED_HERE]: MEROMORPHIC CONTINUATION HOLDS, THE FUNCTIONAL EQUATION FAILS — and the failure is proved, not conjectured.  Lambda_wrong is meromorphic on all of C (entire L(s, chi_5) times a nowhere-zero meromorphic completion factor)
- **counterfeit_wrong_gamma.L8_REALIZATION** [PROVED_HERE]: Refutation of realization for the OBJECT Lambda_wrong (the underlying L(s, chi_5) of course retains its GL(1) realization — with the OTHER gamma).  (1) Lambda_wrong is not a Dirichlet series at all, hence lies in no Diri
- **counterfeit_wrong_gamma.L9_EXPLICIT_FORMULA_POSITIVITY** [PROVED_HERE]: no principled explicit formula attaches to the wrong completion: the Weil explicit formula is an identity DERIVED FROM the functional equation (contour shift plus the s <-> 1-s symmetry of the completed function), and La
- **counterfeit_wrong_gamma.DUALITY_FE** [PROVED_HERE]: THE EXACT OBSTRUCTION OF THIS WORLD.  THEOREM (proved here). Let chi_5 be the even quadratic Dirichlet character mod 5 (unit table (1,-1,-1,1), chi_5(-1) = +1, verified exactly) and Lambda_wrong(s) = pi^{-(s+1)/2} Gamma(
- **counterfeit_wrong_gamma.TRACE_FORMULA** [PROVED_HERE]: any theta/Poisson-summation (GL(1) trace-formula) mechanism attached to a completion produces exactly the s <-> 1-s functional equation for it; for Lambda_wrong that FE is refuted (see DUALITY_FE), so no trace-formula me
- **davenport_heilbronn.L1_MULTIPLICATIVITY** [REFUTED_BY_WITNESS]: a_6 != a_2 a_3.  EXACT WITNESS (coefficients of f in K = Q(zeta_20), coordinates on 1, z, ..., z^7): a_2 = kappa = (-1, 2, 0, -1, -1, 1, 1, -1), a_3 = -kappa, a_6 = 1 (6 = 1 mod 5).  a_2 a_3 = -kappa^2 and a_6 - a_2 a_3 
- **davenport_heilbronn.L2_EULER_PRODUCT** [REFUTED_BY_WITNESS]: no Euler product over the rational primes with unital local factors exists: any such formal factorization forces a_{mn} = a_m a_n for coprime m, n (proved lemma in the L1 witness), refuted exactly by a_6 - a_2 a_3 = 1 + 
- **davenport_heilbronn.L3_BOUNDED_DEGREE_RATIONAL** [REFUTED_BY_WITNESS]: there are no local factors to bound: a system of bounded-degree rational local factors multiplying out to f would BE a unital Euler product, refuted by the L1/L2 witness (a_6 != a_2 a_3, exact).  CURIOSITY (exact, record
- **davenport_heilbronn.L8_REALIZATION** [REFUTED_BY_WITNESS]: FAILS for every realization class that entails an Euler product over its own primes/closed orbits (automorphic L(s,pi), motivic/Hasse-Weil, Selberg/Ruelle dynamical, Ihara-type combinatorial): each such realization force
- **davenport_heilbronn.L9_EXPLICIT_FORMULA_POSITIVITY** [IMPORTED_THEOREM]: two independent failures.  (i) POSITIVITY: f has zeros off the critical line — infinitely many in Re s > 1 (Davenport-Heilbronn 1936, imported) and zeros in the open strip 1/2 < Re s < 1 (imported, citation-needed densit
- **davenport_heilbronn.EULER_PRODUCT** [REFUTED_BY_WITNESS]: absent, and exactly refuted: a_6 - a_2 a_3 = 1 + kappa^2 != 0 (Norm_{K/Q} = 6400); the proved formal lemma (L1 witness) upgrades the single triple to the nonexistence of ANY unital Euler product over the rational primes.
- **davenport_heilbronn.POSITIVITY_PURITY** [IMPORTED_THEOREM]: no positivity/purity mechanism exists for f, and none CAN: the RH analogue is FALSE for f (off-line zeros, imported), so any candidate positivity mechanism would prove a falsehood.  The exact weight-0 purity of the coeff
- **epstein_pair.L1_MULTIPLICATIVITY** [REFUTED_BY_WITNESS]: generic member Q2: EXACT witness: r_Q2(2) = 0, r_Q2(3) = 0, r_Q2(6) = 4 with gcd(2,3) = 1.  This refutes multiplicativity of c*r_Q2 for EVERY nonzero scalar normalization c (LHS c*4 != 0 = RHS); in the posed /4-normaliza
- **epstein_pair.L2_EULER_PRODUCT** [REFUTED_BY_WITNESS]: generic member Q2: the would-be Euler product assembled from the certified rational prime-power slices predicts a_6 = c(2) c(3) = 0 and a_14 = c(2) c(7) = 0 in the unit normalization c = r_Q2/2; the true exact values are
- **epstein_pair.L3_BOUNDED_DEGREE_RATIONAL** [REFUTED_BY_WITNESS]: no local factors exist for the generic member: any Euler factorization would force a_6 = a_2 a_3 in every normalization (refuted: the would-be Euler product assembled from the certified rational prime-power slices predic
- **epstein_pair.L4_WEIGHT_DUALITY** [REFUTED_BY_WITNESS]: generic member has NO local weight data to be coherent: EXACT witness: r_Q2(2) = 0, r_Q2(3) = 0, r_Q2(6) = 4 with gcd(2,3) = 1.  This refutes multiplicativity of c*r_Q2 for EVERY nonzero scalar normalization c (LHS c*4 !
- **epstein_pair.L7_TWIST_TENSOR_COMPAT** [REFUTED_BY_WITNESS]: generic member: no local Satake data exists to twist or tensor (see L1/L2 witness: r_Q2(2) = r_Q2(3) = 0, r_Q2(6) = 4).  Sub-row Q1: Q1 local object certified as a DIRECT SUM zeta_p (+) chi_-4,p by exact power-sum calcul
- **epstein_pair.L9_EXPLICIT_FORMULA_POSITIVITY** [IMPORTED_THEOREM]: generic member Q2: any Weil-positivity functional for Z_Q2 is impossible — Z_Q2 has zeros OFF the critical line, and (imported, Davenport-Heilbronn phenomenon for class number > 1) even infinitely many zeros in Re s > 1;
- **epstein_pair.EULER_PRODUCT** [REFUTED_BY_WITNESS]: generic member Q2: r_Q2(2) = 0, r_Q2(3) = 0, r_Q2(6) = 4 — no normalization is multiplicative; the would-be Euler product assembled from the certified rational prime-power slices predicts a_6 = c(2) c(3) = 0 and a_14 = c
- **epstein_pair.POSITIVITY_PURITY** [IMPORTED_THEOREM]: FAILS for the generic member Q2: off-critical-line zeros (imported, Davenport-Heilbronn) refute any positivity mechanism, and there is no purity structure on the raw coefficients (non-multiplicativity witness at (2,3,6))
- **epstein_pair.TENSOR_OPS** [REFUTED_BY_WITNESS]: generic member: no local objects exist to tensor (witness (2,3,6) as in L1).  Sub-row Q1: Q1 local object certified as a DIRECT SUM zeta_p (+) chi_-4,p by exact power-sum calculus at p in {3, 5, 7, 13}: op_direct_sum of 
- **ihara_nonramanujan.L9_EXPLICIT_FORMULA_POSITIVITY** [REFUTED_BY_WITNESS]: THE ABLATION CELL.  An exact, finite explicit formula EXISTS and is proved here: tr(B^k) = sum_{d|k} d pi_d pairs geodesic counts against the 96 inverse roots of zeta^-1 with no analytic remainder (Bass identity proved i
- **ihara_nonramanujan.POSITIVITY_PURITY** [REFUTED_BY_WITNESS]: REFUTED BY EXACT WITNESS -- the point of this world.  Self-adjointness of A supplies REALNESS of the spectrum (proved by Sturm) but NOT the Ramanujan/purity bound |lambda| <= 2 sqrt(2): the tree-spectrum positivity that 

## Mechanical ablation cross-tabulation

- **EULER_PRODUCT**: HOLDS in ['beurling', 'counterfeit_deleted_euler', 'counterfeit_random_phase', 'counterfeit_wrong_gamma', 'dirichlet_mod5', 'elliptic_11a', 'ff_elliptic_f5', 'ihara_nonramanujan', 'ihara_ramanujan', 'zeta']; FAILS in ['davenport_heilbronn', 'epstein_pair']; FAILS with line FALSE: ['davenport_heilbronn', 'epstein_pair']; HOLDS with line THEOREM: ['ff_elliptic_f5', 'ihara_ramanujan']
- **DUALITY_FE**: HOLDS in ['davenport_heilbronn', 'dirichlet_mod5', 'elliptic_11a', 'epstein_pair', 'ff_elliptic_f5', 'ihara_nonramanujan', 'ihara_ramanujan', 'zeta']; FAILS in ['counterfeit_deleted_euler', 'counterfeit_wrong_gamma']; FAILS with line FALSE: ['counterfeit_deleted_euler']; HOLDS with line THEOREM: ['ff_elliptic_f5', 'ihara_ramanujan']
- **TRACE_FORMULA**: HOLDS in ['counterfeit_deleted_euler', 'dirichlet_mod5', 'elliptic_11a', 'epstein_pair', 'ff_elliptic_f5', 'ihara_nonramanujan', 'ihara_ramanujan', 'zeta']; FAILS in ['counterfeit_wrong_gamma']; FAILS with line FALSE: []; HOLDS with line THEOREM: ['ff_elliptic_f5', 'ihara_ramanujan']
- **POSITIVITY_PURITY**: HOLDS in ['elliptic_11a', 'ff_elliptic_f5', 'ihara_ramanujan']; FAILS in ['counterfeit_deleted_euler', 'davenport_heilbronn', 'epstein_pair', 'ihara_nonramanujan']; FAILS with line FALSE: ['counterfeit_deleted_euler', 'davenport_heilbronn', 'epstein_pair', 'ihara_nonramanujan']; HOLDS with line THEOREM: ['ff_elliptic_f5', 'ihara_ramanujan']
- **TENSOR_OPS**: HOLDS in ['counterfeit_deleted_euler', 'counterfeit_random_phase', 'counterfeit_wrong_gamma', 'dirichlet_mod5', 'elliptic_11a', 'ff_elliptic_f5', 'ihara_nonramanujan', 'ihara_ramanujan', 'zeta']; FAILS in ['epstein_pair']; FAILS with line FALSE: ['epstein_pair']; HOLDS with line THEOREM: ['ff_elliptic_f5', 'ihara_ramanujan']
- **FAMILY**: HOLDS in ['beurling', 'counterfeit_deleted_euler', 'counterfeit_wrong_gamma', 'davenport_heilbronn', 'dirichlet_mod5', 'elliptic_11a', 'epstein_pair', 'ff_elliptic_f5', 'ihara_nonramanujan', 'ihara_ramanujan', 'zeta']; FAILS in []; FAILS with line FALSE: []; HOLDS with line THEOREM: ['ff_elliptic_f5', 'ihara_ramanujan']

- worlds with critical line THEOREM: ['ff_elliptic_f5', 'ihara_ramanujan']; of these, POSITIVITY_PURITY HOLDS in ['ff_elliptic_f5', 'ihara_ramanujan'] — co-occurrence EXACT (all) in this corpus

Validation problems: {}
