# Proof audit: status, checks, and load-bearing gaps

```text
Disposition: PROMISING BUT NOT YET VERIFIED
Headline theorem: source claim, not accepted theorem in Riemann
```

## Audit scale

The labels used here are:

```text
CHECKED_ALGEBRAICALLY
  The displayed implication can be reconstructed directly from the source.

DIAGNOSTICALLY_CORROBORATED
  Independent finite or floating computation agrees, but is not a proof.

REPAIR_REQUIRED
  A concrete missing definition, hypothesis, or incorrect bound was found.

EXPANSION_REQUIRED
  The strategy may work, but the posted exposition omits a load-bearing
  derivation or machine artifact.

NOT_REVIEWED_TO_CLOSURE
  No independent complete verification was performed.
```

## 1. Tail identities

**Status:** `CHECKED_ALGEBRAICALLY`.

The definitions imply

\[
T_m=(-1)^m(G-S_{m-1}),
\qquad
T_m+T_{m+1}=(2m+1)^{-2}.
\]

The alternating-series bound is standard and correctly oriented.

## 2. Theorem 2.1: full rank

**Status:** `PLAUSIBLE / HIGH-PRIORITY FORMALIZATION`.

The finite-difference annihilation, injectivity of
\(\lambda\mapsto P_\lambda^*\), degree bounds, and zero-count contradiction
form a coherent proof.

Two small exposition repairs are advisable:

- explicitly handle the possibility that the rational function in (2.17) is
  polynomial before choosing a pole;
- expand the divisibility of `K(X)` by `G_0(X)` so every multiplicity is
  transparent.

Neither appears structurally difficult.

## 3. Proposition 3.1: Newton completion

**Status:** `REPAIR_REQUIRED`.

The source never defines `D`. The square dimension and the factorial product
force

\[
D=2B.
\]

With that insertion, the finite-difference transform gives the advertised
triangular reference block and the three auxiliary unit vectors. This is a
typographical/definition gap, but the current statement is literally
incomplete.

## 4. Proposition 3.2: minimal integerizer

**Status:** `CHECKED_ALGEBRAICALLY`, conditional on the repaired scalar.

For a nonzero rational \(x\), the denominator exponent is
\([ -v_p(x)]_+\). Applying this to (3.5) gives the formula.

## 5. Lemmas 4.1–4.2: double Vandermonde

**Status:** `CHECKED_AT_THE_IDENTITY_LEVEL`.

The Cauchy determinant gives one \(V(I)\). The Pascal alternant gives another
because an alternating polynomial is divisible by the Vandermonde.

A missing asymptotic lemma should be added for the quotient
\(\Psi_A(I)\). If \(A^c=\{c_1,c_2,c_3\}\), then its total degree in the
selected indices is

\[
\sum c_t-3\le3S.
\]

This is precisely why three completion columns are sufficient to keep the
Pascal defect subquadratic. A coefficient-height bound should then establish

\[
\log|\Psi_A(I)|=O(B\log B)
\]

uniformly in `A` and `I`.

## 6. Lemma 5.3: valuation lower bound

**Status:** `PLAUSIBLE / NEEDS LINE AUDIT`.

The two Vandermonde factors correctly produce twice the residue-collision
valuation. The integer \(\Psi_A(I)\) may be discarded in a lower p-adic
bound. The nonarchimedean triangle inequality justifies taking the minimum
over Cauchy-Binet terms.

A formal proof should audit every factorial sign and every boundary indicator
in (5.7), especially the tail denominator contribution (5.11).

## 7. Theorem 5.1: local saturation

**Status:** `REPAIR_REQUIRED`, then `STRONGLY CORROBORATED`.

The proof invokes \(S\le B/20\), but the statement omits it. A repaired
statement should read at least:

```text
For B >= 20, 1 <= S <= B/20, and every odd prime power Q,
a_{Q,B} >= m^A_{Q,B}.
```

The final use with \(S=\lfloor B/20\rfloor\) satisfies this.

The diagnostic script checked the reduced inequality (5.21) for:

```text
20 <= B <= 300
1 <= S <= floor(B/20)
every odd Q <= 2B+S+3
437661 cases
```

No failure was found. Checking every odd `Q` is stronger than checking only
odd prime powers at those finite sizes.

## 8. Lemma 5.4: prime 2

**Status:** `PLAUSIBLE`.

The products \(\Pi_i\) and all Cauchy denominators are odd. Under the rational
hypothesis, `q T_m` has odd denominator, so the residual determinant is
2-integral. Since the factorial contribution makes the denominator layer
negative, its positive part is zero.

This special treatment is important: adding a naive `p=2` local density to
the odd-prime constant would estimate a different object.

## 9. Lemma 5.5: full-row stability

**Status:** `REPAIR_REQUIRED + EXPANSION_REQUIRED`.

The statement's local `O(1+B/Q)` exchange idea is reasonable, but the proof is
too compressed for a load-bearing uniform asymptotic. It should provide:

- an explicit exchange map for minimizers using the three surplus rows;
- a uniform bound for each changed base cost;
- an explicit bound for the change in the double collision term;
- a correct support cutoff;
- the corresponding real-place and Pascal-factor bounds.

The sentence “all nonzero layers satisfy `p^nu < 5B`” is not literally safe
for the full-row/ideal-row denominator-layer difference. The diagnostic
example

\[
B=100,\quad S=5,\quad Q=503
\]

gives ideal layer `108`, actual layer `114`, and difference `6`, although
\(503>5B\). From the definitions, a safe cutoff is below
\(6B+2S+5<7B\) in the final regime. This correction does not alter the
`O(B log B)=o(B^2)` conclusion.

## 10. Proposition 6.3: odd small-prime constant

**Status:** `DIAGNOSTICALLY_CORROBORATED / CERTIFICATE MISSING`.

The source gives enough formulas to reconstruct the function numerically. The
independent replay finds

\[
c_{\rm odd}=0.006276744728100986,
\]

within \(3.5\times10^{-18}\) of the displayed decimal.

The claimed proof, however, is a directed interval computation over 178
merged cells. The exact cells, rational coefficients, endpoint evaluations,
and outward-rounded intervals are not included. They should be released as a
producer artifact plus a small exact checker.

## 11. Proposition 7.4: middle-prime integral

**Status:** `DIAGNOSTICALLY_CORROBORATED / EXACT PARTITION MISSING`.

The exact displayed rational is internally consistent. A direct numerical
implementation of (7.7)–(7.13) gives

\[
0.17635583794457388,
\]

compared with

\[
0.17635583792864828\ldots
\]

from the exact fraction. The \(1.6\times10^{-11}\) discrepancy lies well
inside the non-directed quadrature's reported error accumulation.

The claimed 235-cell affine partition and exact summation are absent. Since
the final margin is only about `0.00966`, exact source artifacts are
indispensable.

## 12. Section 8: large-prime gain

**Status:** `CHECKED_ALGEBRAICALLY AT THE DISPLAYED PIECEWISE LEVEL`.

Integrating the seven displayed affine pieces yields

\[
\Delta_{>B}=\frac23\rho+\frac12\rho^2,
\]

and at \(\rho=1/20\) this is \(83/2400\).

A full audit still has to derive the seven pieces from the exact local
minimization, not merely integrate them.

## 13. Proposition 9.5: same-scalar quadratic estimate

**Status:** `EXPANSION_REQUIRED — MAIN GATE`.

This is the most consequential unresolved part of the posted proof. The
proposition asserts that all real and nonarchimedean contributions assemble to

\[
\frac{39}{200}+c_{\rm odd}-\Lambda_{\rm mid}-\frac{83}{2400},
\]

after cancellation of all \(B^2\log B\) terms.

The source provides a narrative, but not a complete ledger. A verification
must exhibit a uniform formula for

\[
\log|\Xi_I|
+
\sum_{p,\nu}(a_{p^\nu,B}-m^A_{p^\nu,B})\log p
\]

and then prove, uniformly over the selected row set `A` and every
Cauchy-Binet subset `I`:

1. the exact `B^2 log B` cancellation;
2. the raw real coefficient \(4\rho-2\rho^2\);
3. the odd-small-prime correction and the removed prime-2 term;
4. the middle-prime marginal minimum;
5. the large-prime improvement;
6. the `o(B^2)` contribution of higher powers;
7. the three surplus rows;
8. the Pascal quotient \(\Psi_A(I)\);
9. all Stirling and floor errors;
10. the fixed factor \(q^S\).

Until this is written or machine-checked, the final theorem should remain
`REVIEW_PENDING`.

## 14. Theorem 9.1: numerical margin

**Status:** `CHECKED EXACTLY FROM THE STATED BOUNDS`.

Using the upper endpoint for \(c_{\rm odd}\), the lower decimal bound for
\(\Lambda_{\rm mid}\), and \(83/2400\), the conservative margin is

\[
0.009662426525232350728735733\ldots
\]

which is strictly larger than the paper's
\(0.00966242652523235\).

This verifies only the arithmetic combination, not the preceding analytic
ledger.

## 15. Final contradiction

**Status:** `CHECKED CONDITIONALLY`.

If Proposition 9.5 and the integerizer construction are valid, then

\[
N_B=q^S H_B^{\min}\widehat q_B
\]

is a nonzero integer with \(\log|N_B|\to-\infty\), an immediate
contradiction.

## Bottom line

The preprint contains a serious and potentially correct new architecture.
The available evidence does not justify treating it as a settled theorem yet.
The most urgent next action is not more heuristic optimization: it is a
complete, independently replayable proof of Proposition 9.5 and publication
of the two finite cell certificates.
