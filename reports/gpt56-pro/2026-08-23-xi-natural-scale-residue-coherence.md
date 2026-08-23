# Xi natural-scale residue coherence and cumulative reverse-Rolle budget

Date: 2026-08-23  
Dedicated branch: `research/gpt56-pro/105200-xi-natural-scale-residue-coherence`  
Stacked base: PR #723 at `51c5619ef3c4b793de756b1c359b39df2ac35466`  
Scientific status: **RH unproved**

## Repository synchronization

The 2026-08-22 scientific release on main canonicalizes the reviewed corpus
through PR #707 and leaves no reviewed-only path to RH. Two post-integration
programmes are live:

1. the common-mother scale/phase/completion programme, currently reduced to a
   carrier-recombined filtered Lorentz fluctuation;
2. the Xi reverse-Rolle/Riccati/Pick programme, currently equipped with an
   unconditional high-derivative entry and exact first/second critical-residue
   ledgers.

This branch joins the second programme. The reason is structural: the positive
Xi Fourier measure supplies an unconditional sign-bearing asymptotic that can
be pushed beyond a coordinate change, while the common-mother programme still
lacks a source-faithful sign producer.

## Main proposed theorem

For the tilted Xi measure

\[
d\nu_m(u)\propto u^m\Phi(u)\,du,
\]

let `w_m` be its saddle and

\[
s_m^2=(-S_m''(w_m))^{-1}\sim{w_m\over2m}.
\]

The packet proves by a direct uniform Laplace expansion that

\[
A_m(z)
=\exp(iw_mz-s_m^2z^2/2)(1+o(1))
\]

uniformly for every `m>=M` and

\[
|\Re z|\le C\sqrt{M/\log M},
\qquad |\Im z|\le H.
\]

This reaches a fixed multiple of the reciprocal standard deviation, not only
an `o(1)` multiple.

Consequences:

- all zeros of every `Xi^(m)`, `m>=M`, in the common natural box are real and
  simple;
- the entry derivative order for height `T` has the natural size
  `T^2 log T`;
- every adjacent critical residue is
  \[
  {\Xi^{(m)}(c)\over\Xi^{(m+2)}(c)}
  =-w_m^{-2}(1+o(1));
  \]
- the residue coherence tends to one uniformly in the high derivative tail;
- the open `RCMV104530` inequality holds there with every fixed margin below
  the optimum.

## New exact reverse-Rolle quantity

For a finite polynomial derivative ladder, exact conservation and the residue
coherence inequality give

\[
N_{nr}(p)
\le N_{nr}(p^{(r)})
 +2\sum_{j<r}R_j(1-\mathfrak C_j).
\]

For Xi in a regular rectangle, the complete ledger is

\[
O_0
\le O_r
 +2\sum_{j<r}R_j(1-\mathfrak C_j)
 +\sum_{j<r}(B_j+W_j-1).
\]

The unconditional natural-scale theorem makes `O_r=0` for
`r=O(T^2 log T)`. Therefore the remaining conclusion-facing object is the
finite low-order budget

\[
2\sum_{j<r}R_j(1-\mathfrak C_j)
+\sum_{j<r}(B_j+W_j-1)<2.
\]

This is `CRDB105200`. It remains open.

## Why this is progress rather than another RH-equivalent scalar

- The high-tail residue mean value is proved unconditionally from the actual
  Xi source.
- The height/order scale is sharpened to the natural `T^2 log T` threshold.
- The reverse-Rolle loss is additive and level-sensitive; no fixed percentage
  is multiplied through thousands of derivative levels.
- The exact first and second moment ledgers from PRs #720/#723 now feed one
  explicit cumulative budget.
- Boundary winding remains visible and is not hidden in an error term.

## Replay

```bash
python -B experiments/X-105200-natural-scale-residue-coherence/verify.py \
  --output experiments/X-105200-natural-scale-residue-coherence/results/verification.json
```

Retained verdict:

```text
PASS_X_105200_NATURAL_SCALE_RESIDUE_COHERENCE
```

The replay performs 6,645 exact Fraction/Sturm checks. It does not certify the
analytic saddle theorem, `CRDB105200`, or RH.

## Exact boundary

```text
natural-scale Gaussian Xi saddle         PROPOSED COMPLETE / REVIEW REQUIRED
natural-height high derivative entry     PROPOSED COMPLETE / REVIEW REQUIRED
high-tail critical residue asymptotic    PROPOSED COMPLETE / REVIEW REQUIRED
high-tail RCMV                           PROPOSED UNCONDITIONAL
finite coherence-defect budget           PROVED EXACT
CRDB105200                               OPEN / RH-BEARING
Riemann Hypothesis                       UNPROVED
```
