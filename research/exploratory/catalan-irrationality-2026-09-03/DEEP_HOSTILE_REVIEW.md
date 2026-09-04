# Deep hostile review of the Catalan irrationality preprint

```text
Source reviewed: Zhi-Wei Sun, arXiv:2609.04176v1, 3 September 2026
Review disposition: PROOF INVALID AS WRITTEN
Headline theorem: NOT ESTABLISHED BY THIS PREPRINT
Catalan's constant itself: not proved rational here; irrationality remains open
Riemann Hypothesis: unaffected and unproved
```

## Read this before the original import assessment

The initial import correctly classified the paper as unverified and isolated
Proposition 9.5 as its main missing ledger. A second, hostile pass has now gone
further: the leading-order cancellation asserted in the proof of Proposition
9.5 is incompatible with the paper's own Cauchy--Binet majorant and its own
small-prime singular coefficient.

The decisive calculation is in
[`HEIGHT_BOUND_COUNTERCHECK.md`](HEIGHT_BOUND_COUNTERCHECK.md). It shows that
the largest-absolute-summand bound used in the first paragraph of Proposition
9.5 retains

\[
\frac{\rho^2}{2}B^2\log B,
\]

not merely a finite multiple of `B^2`. At the paper's `rho=1/20` this is

\[
\frac1{800}B^2\log B.
\]

Accordingly, equation (9.3) is not proved by the stated argument, Theorem 9.1
does not follow, and the final integer contradiction does not close.

This is a failure of the posted proof, not a proof that Catalan's constant is
rational.

## 1. Treatment of the online claims

A current web search was carried out for the title, arXiv identifier, author,
Proposition 9.5, Theorem 5.1, the `B^2 log B` cancellation, and likely social
and specialist venues. The available index exposed general skepticism and
current status pages, but no stable, citable specialist post containing a
complete mathematical counterargument.

The review therefore does not appeal to social consensus. The online claims
were treated as a request for a fresh adversarial audit. The verdict below is
based on the attached v1 PDF and independently reconstructed formulas.

As of this review, public reference pages still describe the preprint as a
claim awaiting verification and Catalan irrationality as unresolved. Those
status pages are secondary evidence only; the mathematical reason for the
repository verdict is the countercheck in this packet.

## 2. The decisive flaw: local minima do not control the largest real term

The architecture uses two different optimizations over Cauchy--Binet subsets:

```text
p-adic side:
  m_Q^A = minimum local valuation layer over all subsets I

archimedean side:
  |sum_I Xi_I| <= number of terms times maximum_I |Xi_I|
```

Both operations are individually legal. The problem is that their leading
orders do not cancel.

For the compulsory subset

\[
I_0=\{0,1,\ldots,S-1\},
\]

the Pascal minor is a nonzero integer for every valid selected row set `A`, so
its absolute value is at least one. This one summand carries

\[
\prod_{i<S}\Pi_i,
\]

whose logarithm is

\[
2\rho B^2\log B+O(B^2).
\]

By contrast, the paper's own Section 6 says that the common local divisor
captured by the minima has singular coefficient

\[
A_\rho=2\rho-\frac{\rho^2}{2}.
\]

After the exact `a_Q` baseline cancels against the normalization
`F_B/prod Pi_i`, the difference is

\[
2\rho-A_\rho=\frac{\rho^2}{2}>0.
\]

The Cauchy determinant contributes only `O(B^2)`, because its numerator and
denominator `S^2 log S` terms cancel. The tail product contributes only
`O(B log B)`. The Pascal minor cannot help because it is an integer of
absolute value at least one. The surplus-row passage is only `o(B^2)` if Lemma
5.5 is granted.

Thus the max-summand majorant grows at least as

\[
\frac{\rho^2}{2}B^2\log B-O(B^2).
\]

It cannot be assigned the finite quadratic coefficient claimed in (9.3).

### Why signed determinant cancellation is not a hidden rescue

The determinant itself may exhibit severe cancellation among the terms
`Xi_I`. Such cancellation could in principle make the actual scalar far
smaller than its largest summand. But the published proof explicitly replaces
the sum by the largest absolute summand, paying only the logarithm of the
number of terms. Once that step is taken, cancellation is unavailable.

A repaired proof would have to establish a new signed cancellation theorem for
the complete Cauchy--Binet sum, or redesign the scalar. Neither appears in v1.

## 3. Independent finite diagnostic

The new script

```text
diagnostics/catalan_height_hostile_replay.py
```

computes the exact ideal local minima and evaluates a rigorous two-term-tail
lower bound for the `I_0` contribution to the max-summand majorant. It is
explicitly classified as `NON_PROOF_DIAGNOSTIC`; the analytic argument above,
not this table, establishes the structural obstruction.

For `S=floor(B/20)` the replay gives:

| B | S | one-term lower bound divided by B^2 |
|---:|---:|---:|
| 100 | 5 | 1.821777816169270 |
| 200 | 10 | 1.849984814303233 |
| 300 | 15 | 1.865521107324622 |
| 500 | 25 | 1.874889547532234 |
| 1000 | 50 | 1.884184990849831 |
| 1500 | 75 | 1.886035510685781 |

These finite values are nowhere near the claimed negative coefficient. They
also exhibit a large positive `2`-adic contribution from `F_B`, which is part
of the same real-place normalization and cannot simply be omitted. The
asymptotically decisive mismatch remains the positive `B^2 log B/800` term.

## 4. Additional source defects

The leading-order failure is independent of the following issues, all of which
were found in the earlier pass and remain valid.

### 4.1 Undefined completion dimension

Section 3 introduces power columns `i^r` for `0<=r<D` and Newton columns
`binom(i,D+c_t)` without defining `D`. The square dimension and the product
of pivots force

\[
D=2B.
\]

This is repairable, but the statement is incomplete as printed.

### 4.2 Missing definition of `T_0`

Theorem 2.1 extends a formula to `i=0` and then uses `T_i`, although tails were
defined only for positive indices. The natural repair is `T_0=G`.

### 4.3 Tail-index/sign inconsistency

Equation (2.3) yields

\[
T_{i+j}=(-1)^jT_i+\cdots,
\]

so the next displayed residual formula should contain `T_i`. An equivalent
reindexing through `T_{i+1}` gives the global factor `(-1)^{j-1}`, not
`(-1)^j`. The printed `T_{i+1}` formula therefore has a column sign error.
Absolute determinants survive this repair, so it is not the fatal issue.

### 4.4 Missing hypothesis in Theorem 5.1

The proof uses

\[
S\le B/20,
\]

but the theorem statement omits it. The final specialization satisfies the
missing condition.

### 4.5 Unsafe `5B` cutoff in Lemma 5.5

The full-row/ideal-row denominator-layer difference can remain nonzero above
`5B`. The explicit diagnostic

\[
B=100,\quad S=5,\quad Q=503
\]

has difference `6`, although `Q>5B`. A safe linear cutoff such as `7B` keeps
the desired subquadratic order, but the printed assertion is false.

### 4.6 Unpublished finite certificates

The paper's two central numerical claims refer to:

- 178 merged special-function cells for the small-prime constant;
- 235 exact affine cells for the middle-prime integral.

The cells, rational formulas, directed intervals, and exact summation records
are absent from v1. Independent floating reconstruction agrees closely with
the displayed constants, but that does not supply the claimed certificates.

## 5. What survives the hostile review

The paper is not devoid of useful mathematics. Subject to the local repairs
above, several layers appear coherent and deserve independent extraction.

### Weighted-tail source design

The transformation

\[
u_m=T_m/(2m+1)
\]

turns the tail recurrence into a Cauchy denominator while preserving odd
prime-power structure. This is an interesting source-design principle.

### Full-rank mechanism

The finite-difference annihilation and the rational difference-equation
obstruction in Theorem 2.1 appear salvageable after defining `T_0` and fixing
the tail index/sign.

### Newton completion

With `D=2B`, the completion to one square determinant and the extraction of a
nonzero residual minor are standard and plausible.

### Double Vandermonde structure

The Pascal alternant and Cauchy determinant genuinely provide two
Vandermonde factors. This is reusable finite algebra.

### Local saturation theorem

After adding `S<=B/20`, the coarse inequality underlying Theorem 5.1 has passed
a large independent finite search and appears plausible. It remains separate
from the failed global archimedean ledger.

### Standalone numerical constants

The published values of `c_odd`, `Lambda_mid`, and the final decimal
subtraction are strongly corroborated numerically. Correct constants cannot
repair an incorrect leading scale.

## 6. Possible repair programs

A v2 cannot be repaired by adding the missing cell tables alone. At least one
new global mechanism is required.

### Route A: signed Cauchy--Binet cancellation

Retain

\[
\sum_I\Xi_I
\]

as a signed determinant and prove cancellation of the large `I_0`-type terms
at the `B^2 log B` scale. This would require phase/sign information far beyond
the current local-minimum analysis.

### Route B: stronger common divisibility

Find a common numerator divisor of the complete determinant with singular
coefficient at least `2rho`, rather than
`2rho-rho^2/2`. It must divide the same scalar and survive summation, not just
selected terms.

### Route C: redesign the completion or weights

Construct a determinant in which the compulsory product of selected clearing
factors is absent or exactly matched by local saturation.

### Route D: a different adelic scalar

Preserve the attractive same-scalar philosophy but replace the present
Pascal--Cauchy determinant with an object having a complete product-formula
ledger.

Until one of these is supplied, the final irrationality claim is unsupported.

## 7. Relevance to the Riemann project after the refutation

The RH connection remains methodological, not implicational. The failure is
itself useful because it illustrates a recurrent danger in the repository:

```text
minimum common local valuation
is not automatically compatible with
maximum absolute archimedean summand.
```

Any determinant, Gram, Schur, or coefficient-extraction proof must keep four
quantities attached to the same object:

1. nonvanishing;
2. local divisibility or positivity;
3. archimedean contraction;
4. the optimization direction over auxiliary indices.

Switching from a local minimum to a real maximum can leave a leading entropy
or clearing-factor tax, exactly as it does here.

## 8. Final verdict

```text
Theorem 2.1 and finite algebra: potentially salvageable
Theorem 5.1: missing hypothesis, plausibly repairable
Lemma 5.5: printed cutoff false, proof incomplete
Propositions 6.3 and 7.4: numerical values corroborated, certificates absent
Proposition 9.5 proof: invalid due uncancelled B^2 log B term
Theorem 9.1 and final contradiction: do not follow
Catalan irrationality: not established by arXiv:2609.04176v1
Catalan rationality: not established either
```
