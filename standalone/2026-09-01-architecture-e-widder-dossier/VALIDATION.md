# Validation and replay boundary

Status: **BOUNDED EXACT ALGEBRA ONLY; ANALYTIC PROOFS REQUIRE INDEPENDENT REVIEW; RH REMAINS UNPROVED.**

## 1. Repository and branch freeze

```text
repository: gfreund123/riemann
base:       main@6dda8b5125457ed936330229f8c9eb6491728e76
branch:     research/gpt56-pro/20260901-architecture-e-widder-dossier
packet:     standalone/2026-09-01-architecture-e-widder-dossier/
```

The branch was created directly from the stated `main` commit.  It does not modify the five reviewed source PRs or the successor review/closure PRs.

## 2. Bounded checker

Run from the repository root:

```bash
python -B standalone/2026-09-01-architecture-e-widder-dossier/verify_widder_atom.py
```

Authoring execution produced:

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

The checker uses only Python's standard library and exact rational arithmetic.

## 3. What the checker authenticates

The 217 finite controls cover:

1. the single-Stieltjes-atom identity
   \[
   (-1)^{k-1}D^{2k-1}\left[\frac{u^k}{u+a}\right]
   =(2k-1)!\frac{a^k}{(u+a)^{2k}};
   \]
2. the exact differential recurrence
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

The controls use several exact rational panels and polynomial test functions.  They are regression checks for algebra and indexing, not evidence for the Riemann-data sign.

## 4. Remote readback

The committed checker was read back from the remote branch through the GitHub contents API.  Its remote blob identity at readback was

```text
0b791b399214eb91b0a5e6a93610019238fab02a
```

The packet directory was also read back remotely and contained the declared front door, seven proof/review notes and the checker before this validation file was added.

## 5. Analytic content not machine-certified

The checker does **not** establish:

- existence, positivity or exact normalization of the full Riemann theta kernel;
- the canonical-product expansions for `X` or `mathfrak X`;
- the negative-square theorem for an infinite zero set;
- the Fourier transform from `A_Phi` to `B_X`;
- the Stieltjes continuation converse;
- the application of Widder's theorem to `q`;
- differentiated infinite Euler-series interchange in every declared regime;
- positivity of any `W_k(u)` for actual Riemann data beyond imported results;
- the E–Widder inequality `(EW)`;
- RH or GRH.

These are mathematical proof obligations and must be checked independently.

## 6. Review checklist

A reviewer should perform at least the following:

1. verify every frozen source head and imported statement;
2. reconstruct the companion/Hermite congruence;
3. check the feature-space negative-index proof and multiplicity caveat;
4. rederive the source transport equation and factor four;
5. verify the safe-axis derivative signs;
6. check the Stieltjes converse on the cut plane;
7. pin Widder/Sokal's exact reduced condition;
8. verify the invariant entire descent and order conversion;
9. audit the Euler-safe source expansion and all fixed-order interchanges;
10. rerun the exact checker from committed bytes.

## 7. Current exact boundary

```text
remote packet residency                   CONFIRMED
bounded rational algebra                  217 CHECKS PASSED IN AUTHORING RUN
repository-wide CI                        NOT RUN
analytic proof review                     REQUIRED
E-Widder inequality (EW)                  OPEN / RH-EQUIVALENT
Riemann Hypothesis                        UNPROVED
```
