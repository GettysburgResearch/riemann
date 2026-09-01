# Validation and replay boundary

Status: **BOUNDED EXACT ALGEBRA ONLY; ANALYTIC PROOFS REQUIRE INDEPENDENT REVIEW; RH REMAINS UNPROVED.**

## 1. Repository and branch freeze

```text
repository: gfreund123/riemann
base:       main@6dda8b5125457ed936330229f8c9eb6491728e76
branch:     research/gpt56-pro/20260901-architecture-e-widder-dossier
packet:     standalone/2026-09-01-architecture-e-widder-dossier/
```

The branch is standalone.  It does not modify the reviewed source PRs,
source experiments, canonical registries or production paths.

## 2. Bounded exact checkers

Run from the repository root:

```bash
python -B standalone/2026-09-01-architecture-e-widder-dossier/verify_widder_atom.py
python -B standalone/2026-09-01-architecture-e-widder-dossier/verify_height_order_geometry.py
python -B standalone/2026-09-01-architecture-e-widder-dossier/verify_order_product_and_reciprocal.py
python -B standalone/2026-09-01-architecture-e-widder-dossier/verify_invariant_resolvent.py
python -B standalone/2026-09-01-architecture-e-widder-dossier/verify_theta_darboux_andreief.py
```

The authoring runs produced the following exact-rational counts.

### Original Widder, recurrence and Loewner checker

```text
PASS_ARCHITECTURE_E_WIDDER_EXACT_CHECKS
widder_atom=42
widder_recurrence=30
Q_recurrence=33
normalized_microscope=96
loewner_difference=16
total=217
RH_UNPROVED
```

### Finite-height angular checker

```text
PASS_FINITE_HEIGHT_WIDDER_CONE_EXACT_CHECKS
complex_widder_atoms=36
diagonal_phase_formulas=27
published_budget=3
total=66
IMPORTED_ZERO_HEIGHT_NOT_REPLAYED
ALL_ORDER_EW_OPEN
RH_UNPROVED
```

### Order-product, reciprocal and Bernoulli-string checker

```text
PASS_ORDER_PRODUCT_AND_RECIPROCAL_EXACT_CHECKS
total=173
RH_UNPROVED
```

The detailed component count is printed by the committed script.

### Invariant resolvent and heat-moment checker

```text
PASS_INVARIANT_WIDDER_RESOLVENT_EXACT_CHECKS
matching_scale=18
resolvent=18
pair_numerator=27
pair_threshold=12
normalized_recurrence=72
heat_moment=72
total=219
ALL_ORDER_SOURCE_SIGN_OPEN
RH_UNPROVED
```

### Theta--Darboux/Andreief checker

```text
PASS_THETA_DARBOUX_ANDREIEF_EXACT_CHECKS
lowering_coefficients=1036
pascal_minors=6
composition_minors=6
self_adjointness=51
andreief=3
total=1102
WEIGHTED_THETA_DARBOUX_SIGN_OPEN
RH_UNPROVED
```

Combined bounded authoring controls:

\[
 \boxed{217+66+173+219+1102=1777.}
\]

Every checker uses only Python's standard library and exact `Fraction`
arithmetic.

## 3. What the checks authenticate

The 1777 controls cover finite instances of:

1. positive and complex Widder atom identities;
2. the `W_k`, `Q_k` and normalized `C_k` differential recurrences;
3. the invariant Hausdorff microscope;
4. the Loewner-difference identity, including diagonal cells;
5. the finite-height angular bound and the exact published height/order ratio;
6. the radial order product and reciprocal rectangle identities;
7. finite Bernoulli-string/quasi-free algebra;
8. the matching-scale transformed atom and its interior pole;
9. the closed invariant resolvent formula;
10. the exact conjugate-pair numerator and positivity threshold;
11. the Widder-to-heat Laplace moment identity;
12. the coefficient-lowering law `L b_n=b_(n-1)` on truncated exact series;
13. Pascal and coefficient-kernel total-positivity controls;
14. formal self-adjointness against a Gaussian test source;
15. finite weighted Cauchy--Binet/Andreief identities.

These are regression checks for algebra, indexing and normalization.  They are
not substitutes for the written continuum proofs.

## 4. Imported external inputs

The finite-height conclusions import the published Platt--Trudgian result that
all nontrivial zeta zeros through height

\[
 3\cdot10^{12}
\]

lie on the critical line.  The repository source lock is

```text
EXT.XI.PLATT_TRUDGIAN.2021
```

The external interval computation and Turing count were not rerun.

The dossier also cites recent primary-source results on a centered Toeplitz
cubic wedge and strict total positivity of the modified-Bessel spectral
kernel.  Their statements are imported only at the scopes recorded in the
literature and claim-ledger files.  No external computation or proof was
replayed by these rational checkers.

## 5. Analytic content not machine-certified

The checkers do **not** establish:

- existence, positivity or exact normalization of the full Riemann theta
  kernel;
- the infinite canonical products for `X` or `mathfrak X`;
- orbit multiplicity and normal convergence in every infinite zero sum;
- the negative-square theorem for the infinite zero set;
- the source-polarization Fourier bridge;
- the Stieltjes/Widder converse to RH;
- the published finite-height verification;
- the continuum angular and terminal-annulus theorems;
- the infinite radial determinant and count-law product interchanges;
- the one-scale `PF_infinity`/Poisson-binomial converse;
- the theta mixture or Fredholm determinant closure;
- strict total positivity of the complete infinite coefficient kernel beyond
  the written proof;
- the infinite theta--Darboux/Andreief integral and its weighted sign;
- complete monotonicity of the fixed-centre heat trace;
- the all-order E--Widder source inequality;
- RH or GRH.

These remain mathematical proof obligations and require independent review.

## 6. Review order for the latest pass

A reviewer should reconstruct, in this order:

1. the invariant entire descent and genus-zero orbit product;
2. the radial product/resolvent factorization and matching-pole residue;
3. the exact conjugate-pair positivity threshold;
4. the sharp direct-Euler half-ray and verified-height terminal annulus;
5. the identity between `K(t)` and the fixed-centre zero heat trace;
6. the Widder-to-heat moment bridge and Guinand--Weil normalization;
7. positivity and the lowering law for the coefficient basis `b_n`;
8. strict total positivity of the Pascal/Bessel coefficient kernel;
9. repeated self-adjoint transport of `L` onto the actual theta source;
10. the factor and determinant orientation in the Andreief formula;
11. the distinction between pointwise theta--Darboux positivity, which is not
    asserted, and the weighted gate actually required;
12. replay all five committed checkers from their remote bytes.

## 7. Current exact boundary

```text
remote packet residency                             CONFIRM AT FINAL HEAD
bounded exact authoring algebra                      1777 CONTROLS PASSED
repository-wide CI                                  NOT RUN
analytic proof review                               REQUIRED
E-Widder inequality through 4.71*10^12              PROPOSED COMPLETE / REVIEW
resummed radial positivity through terminal cutoff  PROPOSED COMPLETE / REVIEW
fixed-centre heat and theta-Darboux identities       PROPOSED COMPLETE / REVIEW
weighted theta-Darboux / quasi-free completion       OPEN / RH-EQUIVALENT
all-order E-Widder source inequality                 OPEN / RH-EQUIVALENT
Riemann Hypothesis                                   UNPROVED
```
