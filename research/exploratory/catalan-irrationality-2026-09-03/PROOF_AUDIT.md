# Proof audit: revised hostile verdict

```text
Disposition: PROOF INVALID AS WRITTEN
Headline theorem: not established by arXiv:2609.04176v1
Fatal point: the largest-summand majorant in Proposition 9.5 retains
             (rho^2/2) B^2 log B
Catalan rationality: not established
Catalan irrationality: remains unresolved pending a different or repaired proof
```

The technical countercheck is in
[`HEIGHT_BOUND_COUNTERCHECK.md`](HEIGHT_BOUND_COUNTERCHECK.md). The executive
review is in [`DEEP_HOSTILE_REVIEW.md`](DEEP_HOSTILE_REVIEW.md).

## Audit labels

```text
CHECKED_ALGEBRAICALLY
  The displayed implication can be reconstructed directly.

PLAUSIBLE_AFTER_REPAIR
  A finite or structural argument appears salvageable after named corrections.

DIAGNOSTICALLY_CORROBORATED
  Independent finite or floating computation agrees, but is not a proof.

REPAIR_REQUIRED
  A definition, hypothesis, sign, or bound is missing or incorrect.

PROOF_REFUTED
  A stated proof step is incompatible with an exact consequence of the same
  formulas.

CLAIM_NOT_ESTABLISHED
  The source's theorem does not follow from the posted argument.
```

## 1. Tail identities

**Status:** `CHECKED_ALGEBRAICALLY / ONE MISSING DEFINITION`.

For positive `m`, the definitions imply

\[
T_m=(-1)^m(G-S_{m-1}),
\qquad
T_m+T_{m+1}=(2m+1)^{-2}.
\]

The alternating-series bounds are correctly oriented. Theorem 2.1 later uses
`T_0` although tails were defined only for positive indices. The natural
repair is

\[
T_0:=G,
\]

which makes `T_0+T_1=1`.

## 2. Theorem 2.1: full rank

**Status:** `PLAUSIBLE_AFTER_REPAIR`.

The finite-difference annihilation, injectivity of
`lambda -> P_lambda^*`, degree bounds, and zero-count contradiction form a
coherent mechanism.

The posted derivation contains a tail-index/sign inconsistency. Equation (2.3)
gives

\[
T_{i+j}=(-1)^jT_i+
\sum_{0\le k<j}\frac{(-1)^{j-1-k}}{(2(i+k)+1)^2}.
\]

Therefore the residual formula immediately following it should use `T_i`.
One may instead reindex through `T_{i+1}`, but then the correct leading factor
is `(-1)^{j-1}`, not `(-1)^j`. This is a global sign on each column and does
not affect rank or absolute determinant values.

Further small repairs:

- handle explicitly the polynomial/no-pole case before choosing a pole of the
  rational solution to (2.17);
- expand the divisibility of `K(X)` by `G_0(X)` with multiplicities;
- state the polynomial extension of the factorial quotient used later.

After these changes the rank argument appears salvageable.

## 3. Proposition 3.1: Newton completion

**Status:** `REPAIR_REQUIRED / PLAUSIBLE_AFTER_REPAIR`.

The source never defines `D`. The square dimension and the pivot product force

\[
D=2B.
\]

With that insertion, the finite-difference transform gives the advertised
triangular reference block and the three auxiliary unit vectors. The current
statement is literally incomplete, but this does not appear to be the fatal
issue.

## 4. Proposition 3.2: minimal integerizer

**Status:** `CHECKED_ALGEBRAICALLY`, conditional on the repaired scalar.

For a nonzero rational `x`, the denominator exponent is `[-v_p(x)]_+`.
Applying this to (3.5) gives (3.7), and the integerization statement follows.

## 5. Lemmas 4.1--4.2: Pascal--Cauchy factorization

**Status:** `CHECKED_AT_THE_IDENTITY_LEVEL / LOCAL REPAIRS`.

The Cauchy determinant contributes one Vandermonde and the Pascal alternant a
second. For the latter, the quotient

\[
P_a(i)=\prod_{r=a+1}^{S+2}(2B+r-i)
\]

should be used as the global polynomial definition; the displayed factorial
ratio is not literally defined when `i>2B+a`, although the polynomial has the
required zero there.

If `A^c={c_1,c_2,c_3}`, the Pascal alternant quotient has total selected-index
degree

\[
c_1+c_2+c_3-3\le3S.
\]

This supports a prospective uniform bound

\[
\log|\Psi_A(I)|=O(B\log B),
\]

but such a bound is not written in v1.

For the consecutive subset `I_0={0,...,S-1}`, the Pascal evaluation minor is a
nonzero integer for every selected row set `A`; this fact becomes decisive in
the Proposition 9.5 countercheck.

## 6. Lemma 5.3: valuation lower bound

**Status:** `PLAUSIBLE_AFTER_REPAIR`.

The two Vandermonde factors correctly produce twice the residue-collision
valuation. The row factorials, clearing factors, Cauchy denominators, and tail
denominator bound match the listed local layer at the structural level.

A formal proof must:

- treat a zero Cauchy--Binet summand as valuation `+infinity`, rather than
  applying `v_p` to zero without comment;
- audit every boundary indicator in (5.7);
- fix the `T_i`/`T_{i+1}` indexing consistently;
- justify the finite support of the prime-power layers with a correct cutoff.

The nonarchimedean inequality

\[
\min_I\sum_\nu\lambda_{p^\nu}(I)
\ge\sum_\nu\min_I\lambda_{p^\nu}(I)
\]

is legal. The later failure is not this inequality by itself, but its
combination with an archimedean **maximum**.

## 7. Theorem 5.1: local saturation

**Status:** `REPAIR_REQUIRED / STRONGLY CORROBORATED`.

The proof invokes

\[
S\le B/20,
\]

but the theorem statement omits it. A corrected statement should read at
least:

```text
For B >= 20, 1 <= S <= B/20, and every odd prime power Q,
a_{Q,B} >= m^A_{Q,B}.
```

The final use with `S=floor(B/20)` satisfies the missing condition.

The original diagnostic checked the reduced inequality (5.21) for

```text
20 <= B <= 300
1 <= S <= floor(B/20)
every odd Q <= 2B+S+3
437661 cases
```

with no failure. This supports the repaired local theorem but does not address
the global height mismatch.

## 8. Lemma 5.4: prime 2

**Status:** `PLAUSIBLE / IMPORTANT BOOKKEEPING WARNING`.

The clearing products and Cauchy denominators are odd. Under the rationality
hypothesis, `qT_m` has odd denominator, so `qR` is 2-integral and the 2-adic
**denominator** positive part is zero.

At the same time, the real scalar contains the numerator factor

\[
F_B=\prod_{r=0}^{2B-1}r!,
\]

with

\[
v_2(F_B)=2B^2+O(B\log B).
\]

Thus `v_2(F_B)log 2` is a large positive real-place contribution. Lemma 5.4
only says that no power of two is needed in the denominator integerizer; it
does not delete the real numerator factor.

## 9. Lemma 5.5: full-row stability

**Status:** `REPAIR_REQUIRED + EXPANSION_REQUIRED`.

The exchange idea may still prove an `o(B^2)` transfer, but the posted proof is
too compressed. It needs an explicit minimizer exchange, uniform base-cost and
collision estimates, and a corresponding real-place/Pascal estimate.

The literal statement that all relevant nonzero layers satisfy `p^nu<5B` is
false for the full-row/ideal-row denominator-layer difference. The diagnostic
example

\[
B=100,\quad S=5,\quad Q=503
\]

has ideal layer `108`, actual layer `114`, and difference `6`, although
`503>5B`. A safe cutoff below `6B+2S+5<7B` in the final regime preserves a
subquadratic total error.

Granting a corrected Lemma 5.5 does not repair Proposition 9.5: the new
countercheck allows the full/ideal difference to be `o(B^2)` and still finds a
positive `B^2 log B` term.

## 10. Proposition 6.3: odd small-prime constant

**Status:** `DIAGNOSTICALLY_CORROBORATED / CERTIFICATE MISSING`.

The independent reconstruction gives

\[
c_{\rm odd}=0.006276744728100986,
\]

within approximately `3.5e-18` of the displayed decimal.

The claimed directed proof uses 178 merged cells, shifted Hurwitz-zeta and
Gamma evaluations, and outward rounding. Those cells and interval records are
not supplied.

More importantly for the hostile review, equations (6.17)--(6.19) state the
singular coefficient

\[
A_\rho=2\rho-\frac{\rho^2}{2}.
\]

That coefficient is one half of the internal inconsistency in Proposition
9.5: the compulsory Cauchy--Binet term carries coefficient `2rho` from its
selected clearing factors.

## 11. Proposition 7.4: middle-prime integral

**Status:** `DIAGNOSTICALLY_CORROBORATED / EXACT PARTITION MISSING`.

The displayed exact rational is internally consistent. Direct numerical
integration gives

\[
0.17635583794457388,
\]

versus

\[
0.17635583792864828\ldots
\]

from the exact fraction, within the non-directed quadrature error estimate.
The claimed 235-cell affine partition and exact sum are absent.

This term affects the finite `B^2` coefficient only. It cannot cancel the
newly identified `B^2 log B/800` obstruction.

## 12. Section 8: large-prime gain

**Status:** `DISPLAYED PIECES CHECKED / DERIVATION INCOMPLETE`.

Integrating the seven displayed affine pieces yields

\[
\Delta_{>B}=\frac23\rho+\frac12\rho^2,
\]

and at `rho=1/20` this is `83/2400`. A full audit must still derive those
pieces from the discrete local minimization.

Like the middle-prime term, this is only quadratic and cannot repair the
leading logarithmic mismatch.

## 13. Proposition 9.5: same-scalar quadratic estimate

**Status:** `PROOF_REFUTED — FATAL TO V1`.

The paper says that equations (3.5), (4.1), and (5.24), followed by replacement
of the Cauchy--Binet sum by its largest normalized summand, have all
`B^2 log B` terms cancel.

They do not.

Let `M_B` be that max-summand majorant. For the compulsory subset

\[
I_0=\{0,1,\ldots,S-1\},
\]

the Pascal minor is a nonzero integer. Exact cancellation of the `a_Q`
baseline leaves

\[
\begin{aligned}
\mathcal M_B\ge{}&v_2(F_B)\log2
-\sum_{p\ \mathrm{odd},\nu}m^A_{p^\nu,B}\log p\\
&+\log|C_{I_0,J}|+
\sum_{i<S}\log\Pi_i+
\sum_{i<S}\log T_{i+1}.
\end{aligned}
\]

The terms have leading orders

\[
\sum_{i<S}\log\Pi_i
=2\rho B^2\log B+O(B^2),
\]

\[
\sum_{p\ \mathrm{odd},\nu}m^A_{p^\nu,B}\log p
=\left(2\rho-\frac{\rho^2}{2}\right)B^2\log B+O(B^2),
\]

\[
\log|C_{I_0,J}|=O(B^2),
\qquad
\sum_{i<S}\log T_{i+1}=O(B\log B).
\]

Therefore

\[
\boxed{
\mathcal M_B\ge
\frac{\rho^2}{2}B^2\log B-O(B^2).
}
\]

At `rho=1/20`, the coefficient is `1/800`. Hence

\[
\mathcal M_B/B^2\to+\infty,
\]

not to the finite negative coefficient in (9.3).

This proves that the stated largest-summand argument cannot establish
Proposition 9.5. A possible true inequality for the signed determinant would
require a new cancellation theorem not present in the paper.

## 14. Theorem 9.1: numerical margin

**Status:** `ARITHMETIC SUBTRACTION CHECKED / THEOREM NOT ESTABLISHED`.

Given the three displayed finite constants and Proposition 9.5, the decimal
margin

\[
0.009662426525232350728735733\ldots
\]

is correctly positive. But Proposition 9.5 is not proved, and the missing
leading term dominates every finite quadratic constant. Thus Theorem 9.1 does
not follow.

## 15. Final contradiction

**Status:** `FORMALLY IMMEDIATE FROM A FAILED PREMISE`.

If the negative height estimate were valid, then

\[
N_B=q^SH_B^{\min}\widehat q_B
\]

would be a nonzero integer tending below one. That implication is elementary.
The failure lies entirely upstream: the required negative height estimate has
not been obtained.

## Bottom line

The paper contains salvageable finite algebra and an interesting weighted-tail
idea, but its central global estimate is invalid as derived. The missing cell
certificates and editorial repairs are now secondary.

A genuine repair would need at least one of:

1. a proof of signed cancellation across the full Cauchy--Binet sum;
2. a stronger common numerator divisor with singular coefficient at least
   `2rho`;
3. redesigned weights or completion eliminating the selected clearing-factor
   tax;
4. a different same-scalar adelic determinant.

Until then:

```text
arXiv:2609.04176v1 does not prove Catalan's constant irrational.
It also does not prove Catalan's constant rational.
The arithmetic nature of G remains unresolved.
```
