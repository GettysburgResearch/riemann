# L-14309 — Exact radical-truncation residual identity

Claim ID: `L-14309`  
Title: Truncating a global radical vector transfers every localized residual exactly to its discarded tail  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-09-b`  
Created: 2026-07-30  
Dependencies: elementary Hermitian-form algebra; the global `E`-range radical statement in the Connes–Consani framework for the intended application  
Scope: abstract forms and the CCM prolate near-radical construction  
Related counterexample candidates: none

## Algebraic statement

Let `Q` be a Hermitian sesquilinear form on a complex vector space `D`.  Let
`r∈D` belong to the radical:

\[
 Q(r,g)=0\qquad(g\in D).
 \tag{L-14309.1}
\]

Suppose

\[
 r=k+t,
 \qquad k,t\in D.
 \tag{L-14309.2}
\]

Then for every `g∈D`,

\[
 \boxed{Q(k,g)=-Q(t,g).}
 \tag{L-14309.3}
\]

Moreover,

\[
 \boxed{Q(k,k)=Q(t,t).}
 \tag{L-14309.4}
\]

Thus the quadratic value and the complete residual functional of the retained
piece `k` are determined by the discarded tail `t`; no ground-state comparison
is involved.

## Proof

Equation (L-14309.3) is immediate from

\[
 0=Q(r,g)=Q(k,g)+Q(t,g).
\]

Taking `g=k` gives

\[
 Q(k,k)=-Q(t,k).
 \tag{L-14309.5}
\]

Taking `g=t` gives

\[
 Q(k,t)=-Q(t,t).
 \tag{L-14309.6}
\]

Since `Q` is Hermitian, `Q(t,k)=overline{Q(k,t)}`, while the diagonal values
are real.  Conjugating (L-14309.6) and comparing with (L-14309.5) proves
(L-14309.4).  QED.

## Continuous-form corollary

Assume the form is continuous with respect to a tail norm `X` and a test norm
`Y`:

\[
 |Q(f,g)|\le C\|f\|_X\|g\|_Y.
 \tag{L-14309.7}
\]

Then

\[
 \boxed{
 \|Q(k,\cdot)\|_{Y^*}
 \le C\|t\|_X.}
 \tag{L-14309.8}
\]

If the same norm controls both arguments, then

\[
 \boxed{|Q(k,k)|=|Q(t,t)|\le C\|t\|_X^2.}
 \tag{L-14309.9}
\]

Combined with the scalar corollary of `L-14308`, this produces an energy loss
of order

\[
 \frac{C^2\|t\|_X^2}{h\|k\|^2},
 \tag{L-14309.10}
\]

rather than the linear tail-to-gap ratio required for eigenvector convergence.

## Projection version

Let `P` be any linear projection preserving the form domain and put

\[
 k=Pr,
 \qquad
 t=(I-P)r.
\]

Then

\[
 Q(Pr,g)=-Q((I-P)r,g),
 \qquad
 Q(Pr,Pr)=Q((I-P)r,(I-P)r).
 \tag{L-14309.11}
\]

The projection need not be orthogonal for the algebraic identities, although
orthogonality is useful when inserting the result into `L-14308`.

## CCM specialization to be audited

The Connes–Consani construction states that the range of the arithmetic map

\[
 E(f)(u)=u^{1/2}\sum_{n\ge1}f(nu)
\]

lies in the radical of the global Weil form for the declared Schwartz
codimension-two source space.  The explicit CCM target `k_lambda` is obtained by
restricting such an `E(h_lambda)` to the multiplicative interval
`[lambda^{-1},lambda]`.

Provided the exact source normalization and form domains agree, set

\[
 r_\lambda=E(h_\lambda),
 \qquad
 k_\lambda=P_\lambda r_\lambda,
 \qquad
 t_\lambda=(I-P_\lambda)r_\lambda.
\]

Then the localized Weil residual obeys the exact transport identity

\[
 \boxed{
 QW(k_\lambda,g)=-QW(t_\lambda,g)
 \quad
 (\operatorname{supp}g\subset[\lambda^{-1},\lambda]).}
 \tag{L-14309.12}
\]

This isolates a concrete analytic target: bound the **external prolate tail in a
norm on which the Weil form is continuous**.  The ordinary `L2` prolate leakage
alone is not automatically such a norm.

## Relation to the newest CCM evidence

The source compares the very small localized Weil eigenvalues with the prolate
concentration defect `1-chi(lambda)`.  L-14309 explains what a proof must make
quantitative: the same discarded tail that measures failure of exact simultaneous
localization is exactly responsible for the localized Weil residual.

If one proves a graph/form-norm estimate

\[
 \|t_\lambda\|_X\le D_\lambda
 (1-\chi(\lambda))^{1/2}
 \tag{L-14309.13}
\]

with `D_lambda` growing slower than the superexponential prolate decay, then both
the target Rayleigh value and the squared Schur penalty become explicit vanishing
quantities.  No inference of this kind is made from `L2` leakage without the
missing continuity theorem.

## Proof-producing interface

A production packet should bind:

1. the exact global source `h_lambda` and its `E`-image convention;
2. the proof that `E(h_lambda)` lies in the declared radical;
3. the exact support projector and tail definition;
4. a directed graph/form-norm enclosure of the tail;
5. a proved continuity constant for the Weil form;
6. the complement coercivity packet required by `L-14308`.

## Gap audit

- The elementary identity is exact, but the CCM specialization depends on
  normalization and domain compatibility that must be independently checked.
- A global radical vector need not itself be compactly supported.
- `L2` smallness does not control an unbounded or distributional quadratic form.
- Tail decay of Mellin transforms on compact substrips is not by itself a
  residual bound for the Weil operator.
- This lemma does not establish complement positivity.
- The result is a bridge from prolate leakage to a lower-floor program, not a
  completed RH proof.
