# Catalan's constant preprint: source lock, refutation of the posted proof, and Riemann map

> [!CAUTION]
> **Critical review update — 4 September 2026.** The proof in
> `arXiv:2609.04176v1` is invalid as written. Before reading the original
> digest, read [`DEEP_HOSTILE_REVIEW.md`](DEEP_HOSTILE_REVIEW.md) and
> [`HEIGHT_BOUND_COUNTERCHECK.md`](HEIGHT_BOUND_COUNTERCHECK.md). The latter
> identifies an uncancelled positive `B^2 log B/800` term in the exact
> max-summand majorant used by Proposition 9.5. This does **not** prove that
> Catalan's constant is rational; it means the preprint does not establish
> irrationality.

```text
Status: IMPORTED / POSTED_PROOF_INVALID / HEADLINE_THEOREM_UNRESOLVED
Scope: exact 20-page source receipt; hostile theorem-level review; deterministic diagnostics
Source: Zhi-Wei Sun, arXiv:2609.04176v1, 3 September 2026
Riemann base: main@6dda8b5125457ed936330229f8c9eb6491728e76
Companion code or formalization found: none in the searches recorded here
Riemann Hypothesis: unproved; this preprint does not imply RH
```

The preprint claims that Catalan's constant

\[
G=\beta(2)=L(2,\chi_{-4})
 =\sum_{k\ge0}\frac{(-1)^k}{(2k+1)^2}
\]

is irrational. The claim would be a major Diophantine breakthrough, but the
v1 argument does not close.

The initial import classified Proposition 9.5 as the main unverified ledger.
A second hostile pass now gives a proof-level obstruction to that ledger. The
paper combines a **minimum** common local valuation over Cauchy--Binet subsets
with a **maximum** absolute archimedean summand. A compulsory subset
`I_0={0,...,S-1}` retains

\[
\frac{\rho^2}{2}B^2\log B
\]

in the resulting majorant. At `rho=1/20` this is `B^2 log B/800`. The paper
instead asserts that all `B^2 log B` terms cancel and only a finite `B^2`
coefficient remains. Therefore Proposition 9.5 is not proved, Theorem 9.1 does
not follow, and the final integer contradiction fails.

## Exact source receipt

```text
File: 2609.04176(1).pdf
SHA256:
1d05b36a5675cb8084935ec6945e004f1af9387c8fae6c48b242b4a94d73bd90

Size:       378564 bytes
Pages:      20
PDF:        1.7
Page size:  612 x 792 points
Title:      Catalan's constant is irrational
Author:     Zhi-Wei Sun
```

All twenty pages were rendered at 1870 by 2420 pixels and visually inspected.
See `PDF_AUDIT.md`.

No public companion repository, formal certificate, exact cell table, or
machine-readable interval certificate was located in the searches performed on
4 September 2026. The paper says that AI produced the numerical data, but the
posted PDF does not contain those artifacts.

## What the proof tries to do

The argument is a proposed adelic determinant contraction.

```text
Catalan tail recurrence
  -> weighted tails u_m
  -> finite-difference residual matrix R
  -> full column rank
  -> one nonzero selected residual minor
  -> Newton completion to a square scalar qhat_B
  -> Pascal-Cauchy Cauchy-Binet expansion
  -> two Vandermonde factors
  -> p-adic lower bounds for every summand
  -> same-scalar upper bound for the minimal denominator H_B^min
  -> archimedean upper bound for |qhat_B|
  -> claimed negative B^2 exponent
  -> claimed nonzero integer of absolute value < 1.
```

The source-design idea is the weighted tail

\[
u_m=\frac{T_m}{2m+1},
\qquad
T_m+T_{m+1}=\frac1{(2m+1)^2}.
\]

It makes the recurrence compatible with a Cauchy kernel
`1/(2(i+j)+1)` while preserving odd prime-power structure. Several finite
algebraic components remain interesting even though the global height estimate
fails.

## Decisive hostile-review finding

Let `M_B` denote the largest-summand majorant obtained exactly as stated in the
first paragraph of Proposition 9.5 from equations (3.5), (4.1), and (5.24).
The countercheck proves

\[
\mathcal M_B\ge
\frac{\rho^2}{2}B^2\log B-O_\rho(B^2).
\]

The ingredients are all internal to the paper:

1. the subset `I_0={0,...,S-1}` has a nonzero integral Pascal minor;
2. its selected clearing factors contribute
   `2 rho B^2 log B+O(B^2)`;
3. the paper's own small-prime local minimum has singular coefficient
   `A_rho=2rho-rho^2/2`;
4. the Cauchy determinant is only `exp(O(B^2))` and the tail product only
   `exp(O(B log B))`;
5. Lemma 5.5, even if granted, changes only `o(B^2)`.

Thus `2rho-A_rho=rho^2/2` survives. Missing finite cell certificates cannot
repair this, because they change the finite quadratic coefficient rather than
the leading logarithmic order.

The finding refutes the **published proof route**, not the mathematical
possibility that another proof or a substantially revised determinant could
establish irrationality.

## Other source defects

The v1 text also contains the following independent issues:

1. Section 3 uses an undefined parameter `D`; dimensions force `D=2B`.
2. `T_0` is implicitly used but never defined; the natural repair is `T_0=G`.
3. The residual formula following (2.3) switches from `T_i` to `T_{i+1}` with
   the wrong global column sign. Absolute determinants survive the repair.
4. Theorem 5.1 omits the hypothesis `S<=B/20` used in its proof.
5. Lemma 5.5's literal `5B` support cutoff is false; a safe linear cutoff such
   as `7B` preserves only the order estimate.
6. The 178 small-prime cells and 235 middle-prime cells are not published.

These are documented separately in `PROOF_AUDIT.md`. Items 1–5 are not the
reason the final proof fails; the uncancelled leading term is.

## Independent diagnostics

Two diagnostic lanes are retained, both explicitly non-proof.

### Original numerical reconstruction

The original replay corroborates:

```text
published final decimal subtraction;
small-prime constant to about 3.5e-18;
middle-prime integral within quadrature error;
437661 finite cases of the reduced local inequality (5.21).
```

### Hostile height replay

The new deterministic script

```text
diagnostics/catalan_height_hostile_replay.py
```

evaluates the exact ideal local minima and a rigorous two-term-tail lower bound
for the compulsory `I_0` contribution. For `B=100,200,300,500,1000,1500`, the
one-term lower bound divided by `B^2` is respectively approximately

```text
1.82178, 1.84998, 1.86552, 1.87489, 1.88418, 1.88604.
```

These finite values corroborate the structural mismatch. The analytic proof in
`HEIGHT_BOUND_COUNTERCHECK.md`, not the floating logarithms, is the decisive
result.

## What remains valuable

Subject to the local repairs, the following components deserve independent
extraction:

- the weighted-tail recurrence and source design;
- the rational difference-equation obstruction behind full rank;
- Newton completion with `D=2B`;
- the Pascal--Cauchy double Vandermonde;
- the local occupancy formulation and corrected Theorem 5.1;
- a general warning about mixing local minima with archimedean maxima.

A repaired irrationality proof would need new signed Cauchy--Binet cancellation,
a stronger common divisor, redesigned weights/completion, or a different
adelic scalar. Adding the missing interval tables alone is insufficient.

## Relevance to Riemann

The direct L-function connection is a special value, not a zero theorem. The
method does not use the functional equation, the explicit formula, a zero-free
region, or RH.

The failed proof nevertheless supplies a valuable firewall for Riemann's
determinant, Gram, Schur, and divisor-wavelet programs:

```text
minimum common local valuation
  is not automatically compatible with
maximum absolute archimedean summand.
```

Nonvanishing, local divisibility, archimedean contraction, and the direction of
all auxiliary optimizations must remain attached to the same finite object.

## Reading order

1. `DEEP_HOSTILE_REVIEW.md` — executive adversarial verdict and salvage map.
2. `HEIGHT_BOUND_COUNTERCHECK.md` — proof of the uncancelled leading term.
3. `ONLINE_CLAIMS_REVIEW.md` — public-search boundary and terminology.
4. `PROOF_AUDIT.md` — theorem-by-theorem revised status.
5. `PDF_AUDIT.md` — exact source and page map.
6. `MATHEMATICAL_DIGEST.md` — reconstruction of the intended architecture.
7. `NUMERICAL_REPLAY.md` — original independent diagnostics.
8. `CLAIM_MAP.tsv` — compact status table.
9. `RIEMANN_CONNECTION_MAP.md` and `RH_LFUNCTION_BRIDGE.md` — repository map.
10. `REPRODUCE.md` and `REVIEW_CHECKLIST.md` — replay and review requirements.

## Current nonclaims

This packet does not claim:

- that Catalan's constant is rational;
- that no repair of the architecture is possible;
- a formal Lean refutation;
- a peer-reviewed community consensus;
- that the finite diagnostics prove the asymptotic countercheck;
- that irrationality of one L-value would constrain zeta zeros;
- any progress proving RH.
