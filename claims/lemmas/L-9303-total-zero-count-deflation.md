# L-9303 — Total-zero-count deflation for direct-xi modulus witnesses

Claim ID: L-9303  
Title: Unconditional total-zero lower counts become optimal critical-line order-statistic deflation under the RH hypothesis  
Status: PROPOSED  
Authoring agent: `gpt56-02-j`  
Created: 2026-07-26  
Dependencies: L-7501; L-7504; L-9301; L-9302; an unconditional argument-principle or Turing total-zero count  
Scope: division-free completed-xi modulus witnesses from nested ordinate windows  
Related counterexample candidates: none

## Statement

Fix a real ordinate `T>0`. For `u>0`, write

\[
 H_T(u)=\left|\xi\!\left(\frac12+\sqrt u+iT\right)\right|^2,
 \qquad G_T(u)=\log H_T(u).
\]

Let

\[
 0<R_1<R_2<\cdots<R_K<T
\]

be exact rational radii. Suppose an **unconditional** proof-grade computation
certifies that the full critical-strip slab

\[
 T-R_k<\operatorname{Im}\rho<T+R_k
\]

contains at least `M_k` nontrivial zeros of `zeta`, counted with multiplicity,
where

\[
 0=M_0\le M_1\le\cdots\le M_K.
\]

No zero is assumed to lie on the critical line in the certificate. Put

\[
 d_k=M_k-M_{k-1}
\]

and define

\[
 \boxed{
 G_{T,\mathrm{tot}}(u)=G_T(u)-\sum_{k=1}^{K}d_k\log(u+R_k^2).
 }
\]

Then, **under RH**:

1. `G_{T,tot}'` is completely monotone on `(0,\infty)`.
2. The secant kernel
   \[
   L_{T,\mathrm{tot}}(u,v)
   =\frac{G_{T,\mathrm{tot}}(u)-G_{T,\mathrm{tot}}(v)}{u-v}
   \]
   is a positive Gram kernel.
3. Every increasing cross-Loewner minor of `G_{T,tot}` is nonnegative.
4. For every `0<u<v`, the division-free inequality
   \[
   \boxed{
   H_T(v)\prod_{k=1}^{K}(u+R_k^2)^{d_k}
   \ge
   H_T(u)\prod_{k=1}^{K}(v+R_k^2)^{d_k}
   }
   \]
   holds.

Consequently, one strict directed reversal of any displayed inequality is a
finite RH-disproof witness, subject to the named completed-xi normalization,
primitive-enclosure, and total-count gates. Individual Hardy-`Z` zero isolation,
simplicity, and a critical-line count are not required.

## Proof

Assume RH. Every nontrivial zero counted by the unconditional slab certificate
then has real part `1/2`. List all critical-line zero ordinates with multiplicity
and order their squared distances from `T`:

\[
 0\le y_1\le y_2\le\cdots,
 \qquad y_j=(T-\gamma_j)^2.
\]

The total-zero lower count in the `k`th symmetric window becomes, under the RH
assumption, a critical-line lower count in the same window. Hence at least
`M_k` of the numbers `y_j` satisfy `y_j\le R_k^2`. Equivalently,

\[
 y_j\le B_j,
 \qquad B_j=\min\{R_k^2:M_k\ge j\},
 \qquad 1\le j\le M_K.
\]

This is exactly the order-statistic hypothesis of L-9302. Pair the `j`th
selected actual zero with `B_j`. Its residual secant kernel is

\[
 \begin{aligned}
 &\frac{\log(u+y_j)-\log(v+y_j)}{u-v}
 -\frac{\log(u+B_j)-\log(v+B_j)}{u-v}\\
 &\qquad=\int_{y_j}^{B_j}\frac{ds}{(u+s)(v+s)}\succeq0.
 \end{aligned}
\]

Every unselected zero retains its full positive Stieltjes kernel. Summing gives
the positive Gram representation and complete monotonicity. The shell identity

\[
 \sum_{j=1}^{M_K}\log(u+B_j)
 =\sum_{k=1}^{K}d_k\log(u+R_k^2)
\]

then gives the stated `G_{T,tot}`. Cross-Loewner total positivity follows from
the same Cauchy--Binet argument as L-7504 and L-9302. Exponentiating the
one-by-one monotonicity inequality gives the division-free product inequality.

If a directed computation violates one of these RH consequences, the assumption
RH is false. The original total-zero certificate remains unconditional
throughout; only its conversion into critical-line mass occurs inside the proof
by contradiction. ∎

## Why this is stronger than isolated Hardy-zero deflation

A sign-changing Hardy-`Z` interval proves at least one critical-line zero, but it
can miss an even-multiplicity zero and requires one isolating object per root.
An argument-principle or Turing count:

- counts every zero with multiplicity;
- is unconditional;
- can cover a whole nested window with two endpoint evaluations;
- remains useful when individual roots are too close to isolate cheaply.

Under RH, the total count is exactly the line count needed by L-9302. Thus the
new input is logically weaker and computationally cheaper, while the resulting
deflation is multiplicity-complete.

This does **not** assert that the counted zeros are actually on the line. It says
that if RH were true, they would be; a negative residual therefore contradicts
RH.

## Optimality from the supplied information

Under RH the only location data forced by the nested total counts are the order
bounds `y_j\le B_j`. L-9302 proves that

\[
 \sum_{j=1}^{M_K}1_{[B_j,\infty)}(s)\,ds
\]

is the largest pointwise common Stieltjes submeasure present in every line-zero
configuration satisfying those bounds. Therefore the subtraction in this lemma
is the maximal universal subtraction justified by the total-count table alone,
among RH worlds consistent with that table.

A stronger safe subtraction requires genuinely stronger count or localization
information, such as a smaller radius at which the same lower count is proved.
For a tightened order bound `B_j'\le B_j`, the exact added scalar derivative
subtraction at node `u` is

\[
 \frac{1}{u+B_j'}-\frac{1}{u+B_j}
 =\frac{B_j-B_j'}{(u+B_j')(u+B_j)}.
\]

This is a proof-producing priority score for adaptive Turing refinements.

## Counterexample-first count/deflation dichotomy

The same unconditional count infrastructure has two logically distinct uses.

1. If an exact critical-line-empty slab has positive total-zero count, L-5605
   already gives an unconditional RH counterexample.
2. Otherwise, or in larger windows containing line zeros, the nested total counts
   feed the present deflation. A strict negative direct-xi row gives a different
   finite RH counterexample.

Thus no successful total-count computation is wasted: a positive gap
discrepancy is decisive immediately, while ordinary positive counts become
certified removable background in the direct-xi offense.

## Existential completeness is preserved

Suppose RH fails at

\[
 \rho=\frac12+\delta+i\gamma,
 \qquad d=\delta^2>0.
\]

At `T=\gamma`, the corresponding factor contributes

\[
 2m\log|u-d|
\]

to `G_T(u)`. Every finite total-count subtraction in this lemma is a finite sum
of functions `\log(u+R_k^2)`, analytic in a neighbourhood of the positive point
`u=d`. Hence it cannot cancel the off-line logarithmic singularity.

For the interlaced four-point pattern

\[
 (u_1,u_2)=(d-2h,d+h),
 \qquad (v_1,v_2)=(d-h,d+2h),
\]

the deflated cross-Loewner determinant still has leading term

\[
 -\frac{(2m\log2)^2}{h^2}+O(h^{-1})<0
\]

for sufficiently small `h`. Strictness permits exact dyadic points. The
four-point total-count-deflated family is therefore existentially complete for
RH failure, just as the undeflated and line-zero-deflated families are.

## Finite certificate contract

A proof object must bind:

1. the exact rational ordinate `T`;
2. exact rational radii `R_k` and endpoint conventions;
3. unconditional outward count balls for `N(T-R_k)` and `N(T+R_k)`;
4. a unique integer lower count `M_k` obtained from each pair;
5. nondecreasing counts and strictly increasing radii;
6. the direct completed-xi rectangles and normalization fingerprint;
7. the exact shell increments `d_k`;
8. the exact final row interval and strict sign.

A smooth Riemann--von Mangoldt estimate, sampled sign changes, or an empirical
`S(t)` census is not a count certificate. The endpoint count balls must isolate
integers and be independently auditable.

## Adversarial tests

1. Twenty total zeros within radius one in the synthetic model
   `H(u)=(u-5)^2(u+1)^20`: the raw monotonicity and Loewner rows are positive,
   while total-count deflation makes both strictly negative.
2. Split the same count into nested shells and verify exact order-statistic
   increments.
3. Decrease one cumulative count and require rejection.
4. Repeat or reverse one radius and require rejection.
5. Replace the unconditional total-count gate by a smooth-count estimate and
   require rejection.
6. Insert an even-multiplicity line zero: the total-count table retains its full
   multiplicity although a sign-change ledger would miss it.
7. Mutate a count ball so it contains two integers and require fail-closed output.
8. Move an off-line zero outside every counted window; the singular local
   four-point witness must remain available.

## Remaining uncertainty

No Riemann-xi row has been certified negative by this lemma. The active PR #71
workflow still needs a successful FLINT/Arb run or another directed backend.
Any negative must be reproduced independently and the parent direct-xi product
normalization must be reviewed before project-level promotion.

## Suggested next attack

At the exact PR #71 ordinate, replace the 128 individually isolated Hardy-zero
balls by nested exact total counts at dyadic radii. Feed their shell increments
into the existing nine-point direct-xi table. Check the division-free two-point
rows first, then the interlaced order-two through order-four determinants. If all
remain positive, move the same count-plus-xi primitive stack to newly nominated
ordinate windows rather than refining the already-explained PR #71 near-null.
