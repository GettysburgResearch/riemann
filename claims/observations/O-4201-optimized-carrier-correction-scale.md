# O-4201 — Rigorous nonprime correction scale at the optimized carrier

Claim ID: O-4201  
Title: The exact D-0801 archimedean and pole corrections are uniformly below `2.5e-10` at the PR #44 `c=10^11` cell  
Status: PARTIAL  
Authoring agent: `gpt56-05-e`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: L-4202; L-4203; X-4201; PR #44 parameter record  
Scope: correction-size gate at one reported optimized carrier parameter cell  
Related counterexample candidates: none

## Statement

Consider the exact D-0801 parameter values

\[
 c=10^{11},
 \qquad
 K=1024,
 \qquad
 T=4709203636353.65.
\]

Let

\[
 L=\log c,
 \qquad
 b=\frac{2L}{K}.
\]

Then

\[
 b<\frac1{20},
\]

so the L-4202 small-cell theorem applies. The standard-library exact checker
X-4201 proves

\[
 \boxed{
 \|A_K-\ell_TI\|_2<\frac1{5\cdot10^9}=2\cdot10^{-10},
 }
\]

and

\[
 \boxed{
 \|R_K\|_2<\frac1{5\cdot10^{15}}=2\cdot10^{-16}.
 }
\]

In particular,

\[
 \boxed{
 \|(A_K+R_K)-\ell_TI\|_2
 <\frac1{4\cdot10^9}=2.5\cdot10^{-10}.
 }
\]

The leading margin reported by PR #44 at this cell is

```text
+0.00026896626427230785
```

which, as an exact decimal string, is greater than

\[
 \frac1{4000}=2.5\cdot10^{-4}.
\]

Thus the **rigorous analytic correction envelope** is more than one million
times smaller than the **reported ordinary-floating leading margin**.

This comparison is a scale diagnosis, not a proof that the exact matrix is
positive. PR #44's prime phases, accumulation, and eigensolve are not directed
rounded, so its reported leading margin is not a rigorous lower bound.

## Exact inequalities used by X-4201

No floating special-function evaluation enters the bound.

Since `c=10^11`,

\[
 L=11\log10.
\]

The elementary inequalities

\[
 2<\log10<\frac{58}{25}
\]

give

\[
 22<L<\frac{638}{25}.
\]

For the upper bound, the exact exponential partial sum is

\[
 \sum_{n=0}^{6}\frac{(58/25)^n}{n!}
 =\frac{110699859859}{10986328125}>10,
\]

so `exp(58/25)>10`. For the lower bound, `e<3` implies
`e^2<9<10`. Therefore

\[
 b=\frac{2L}{1024}
 <\frac{2(638/25)}{1024}
 =\frac{319}{6400}
 <\frac1{20}.
\]

The archimedean checker substitutes only the safe lower bounds

\[
 L>22,
 \qquad
 \pi>3
\]

into L-4202 and reconstructs the exact harmonic number `H_1022` as a rational.

For the pole term, X-4201 additionally uses

\[
 \sinh(L/2)<\frac{\sqrt{10^{11}}}{2}<160000,
\]

\[
 \cosh^2(\pi h/2)<4,
\]

\[
 \sinh(\pi h)>\pi h,
\]

and the same lower bounds on `L` and `pi`. These deliberately loose estimates
are already far below the archimedean envelope.

## Consequence for the search strategy

At this parameter cell, exact archimedean quadrature is no longer the dominant
uncertainty. Even the uniform vector-independent correction envelope is over
six orders of magnitude below the reported leading margin.

The decisive next work is therefore:

1. directed range reduction for every huge phase in the complete prime stream;
2. directed accumulation of the Toeplitz coefficients;
3. rationalization of one fixed vector or a certified eigenvalue lower bound;
4. independent reconstruction of the D-0801/L-0801 normalization and
   admissibility.

If those steps produce a rigorous leading lower bound above `2.5e-10`, the
exact full matrix at this cell is positive without entrywise archimedean
quadrature. If they produce a rigorous leading upper bound below `-2.5e-10`,
the correction envelope preserves a negative exact value, subject to the shared
normalization audit.

## Proof classification

The following parts are rigorous, conditional only on their named proposed
normalization dependencies:

- the exact formulas in L-4201 and L-4203;
- the analytic operator bound in L-4202;
- the rational parameter inequalities and threshold comparisons in X-4201.

The following part is empirical:

- the PR #44 leading margin parsed from ordinary numerical output.

No rigorous statement compares the unknown exact leading eigenvalue with zero.

## Analytic domain audit

- `T`, `c`, and `K` are exact finite inputs; the decimal `T` is interpreted as
  the exact rational `94184072727073/20`.
- `L=log(c)` is real and positive.
- The elementary upper and lower bounds on `L` are sufficient for every
  threshold comparison.
- The reported margin is never promoted to an interval enclosure.

## Dependency audit

- L-4202 supplies the archimedean operator envelope.
- L-4203 supplies the pole envelope.
- X-4201 reconstructs the rational arithmetic independently of PR #44's
  numerical code.
- PR #44 supplies only the parameter tuple and the empirical margin string.

## Gap audit

1. A small correction does not certify a large leading value when the latter is
   ordinary floating output.
2. The correction bound is in the normalized cell basis; comparisons in any
   other basis require an exact isometry audit.
3. The parameter `T` is treated as its displayed exact decimal. If the actual
   search used a different binary value, the producer must record and certify
   that value separately.
4. The result does not certify D-0801 admissibility or the explicit-formula
   signs.
5. It excludes neither another carrier nor another cutoff with a genuinely
   negative exact form.

## Adversarial tests

1. Replace `K=1024` by a smaller value that violates `b<=1/20`; the checker must
   reject applicability.
2. Decrease `T` until the correction threshold fails; reject rather than reuse
   the committed status.
3. Mutate the harmonic index or any claimed numerator and require rejection.
4. Mark the empirical margin as certified and require schema rejection.
5. Compare the exact rational envelope with high-precision direct evaluation as
   a non-proof diagnostic.

## Remaining uncertainty

The exact prime-side value and the external explicit-formula normalization are
the remaining mathematical uncertainties at this cell. The nonprime correction
scale itself is controlled by the proposed lemmas and exact checker.

## Suggested next attack

Build a fixed-vector directed prime Rayleigh producer. It should consume the
complete shard manifest from PR #44, reduce every `T log(q)` phase with balls,
accumulate one exact-vector value, and compare its interval directly with the
`2.5e-10` correction gate.
