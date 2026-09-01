# Validation and replay boundary

Status: **BOUNDED EXACT ALGEBRA ONLY; ANALYTIC PROOFS REQUIRE INDEPENDENT REVIEW; RH REMAINS UNPROVED.**

## 1. Repository and branch freeze

```text
repository: gfreund123/riemann
base:       main@6dda8b5125457ed936330229f8c9eb6491728e76
branch:     research/gpt56-pro/20260901-architecture-e-widder-dossier
packet:     standalone/2026-09-01-architecture-e-widder-dossier/
```

The branch was created directly from the stated `main` commit.  It does not modify the reviewed source PRs, source experiments, canonical registries or production paths.

## 2. Bounded checkers

Run from the repository root:

```bash
python -B standalone/2026-09-01-architecture-e-widder-dossier/verify_widder_atom.py
python -B standalone/2026-09-01-architecture-e-widder-dossier/verify_height_order_geometry.py
```

The first authoring execution produced

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

The second exact-rational authoring calculation produced the equivalent count profile

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

The second committed script was reconstructed in the authoring environment with the same rational panels and all 66 controls passed.  Both checkers use only Python's standard library and exact `Fraction` arithmetic.

Combined bounded controls:

\[
 217+66=283.
\]

## 3. What the first checker authenticates

The 217 controls cover:

1. the single-positive-Stieltjes-atom identity
   \[
   (-1)^{k-1}D^{2k-1}\left[\frac{u^k}{u+a}\right]
   =(2k-1)!\frac{a^k}{(u+a)^{2k}};
   \]
2. the differential recurrence
   \[
   W_{k+1}=-uW_k''-(2k+1)W_k';
   \]
3. the lower-order recurrence
   \[
   Q_{k+1}=uQ_k'+(k+1)Q_k;
   \]
4. the normalized microscope identity
   \[
   \frac{(4u)^k}{2(2k-1)!}W_k^{\rm atom}
   =\left[\frac{4ua}{(u+a)^2}\right]^k;
   \]
5. the Loewner-difference identity, including diagonal cells.

## 4. What the finite-height checker authenticates

The 66 new controls cover:

1. the full complex-atom Widder identity
   \[
   (-1)^nD^{n+k}\left[\frac{u^k}{u+a}\right]
   =(n+k)!\frac{a^k}{(u+a)^{n+k+1}}
   \]
   on exact rational complex atoms;
2. the exact diagonal phase formulas for
   \[
   z=\frac{a}{(u+a)^2};
   \]
3. positivity of `Re z` on the checked right-half-plane panels;
4. the algebraic angular domination
   \[
   |\arg z|\le|\arg a|
   \]
   in its tangent cross-multiplication form;
5. the exact published height/order ratio
   \[
   \frac{4{,}710{,}000{,}000{,}000}
        {3{,}000{,}000{,}000{,}000}
   =\frac{157}{100}.
   \]

The checkers are regression controls for algebra and indexing.  They are not substitutes for the written continuum proof.

## 5. Imported external theorem

The finite-height Widder theorem imports the published Platt–Trudgian result that all nontrivial zeta zeros through height

\[
 3\cdot10^{12}
\]

lie on the critical line.  The repository source lock is

```text
EXT.XI.PLATT_TRUDGIAN.2021
```

The external interval computation and Turing count were not rerun in this pass.  No stronger zero-height statement is inferred.

## 6. Remote readback

The original checker was read back from the remote branch with blob identity

```text
0b791b399214eb91b0a5e6a93610019238fab02a
```

The new theorem note and finite-height checker were also created through the GitHub contents API and their branch residency is checked again at the final remote-head audit.

## 7. Analytic content not machine-certified

The checkers do **not** establish:

- existence, positivity or exact normalization of the full Riemann theta kernel;
- the canonical-product expansions for `X` or `mathfrak X`;
- orbit multiplicity and local-uniform convergence in the infinite zero sum;
- the negative-square theorem for the infinite zero set;
- the Fourier transform from `A_Phi` to `B_X`;
- the Stieltjes continuation converse;
- the application of Widder's theorem to `q`;
- differentiated infinite Euler-series interchange in every declared regime;
- the published zero verification itself;
- the continuum angular theorem for all zero atoms;
- positivity at unbounded Widder order;
- the all-order E–Widder inequality;
- RH or GRH.

These are mathematical proof obligations and must be checked independently.

## 8. Review checklist

A reviewer should perform at least the following:

1. verify every frozen source head and imported statement;
2. reconstruct the companion/Hermite congruence;
3. check the feature-space negative-index proof and multiplicity caveat;
4. rederive the source transport equation and factor four;
5. check the Stieltjes converse on the cut plane;
6. pin Widder/Sokal's exact reduced condition;
7. verify the invariant entire descent and order conversion;
8. audit the Euler-safe source expansion and all fixed-order interchanges;
9. reconstruct the full complex-atom formula;
10. verify the phase interval and the bound `|arg a|<arctan(1/|gamma|)`;
11. check the use and scope of the Platt–Trudgian theorem;
12. verify the strict `4.71*10^12` corollary and one-way failure localization;
13. rerun both exact checkers from committed bytes.

## 9. Current exact boundary

```text
remote packet residency                         CONFIRM AT FINAL HEAD
bounded rational algebra                        283 AUTHORING CHECKS PASSED
repository-wide CI                              NOT RUN
analytic proof review                           REQUIRED
E-Widder inequality through 4.71*10^12          PROPOSED COMPLETE / REVIEW
all-order E-Widder inequality                   OPEN / RH-EQUIVALENT
Riemann Hypothesis                              UNPROVED
```
