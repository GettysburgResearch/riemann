# L-14201 — Monotone support onset for the localized Weil ground state

Claim ID: L-14201  
Title: The lowest localized Weil eigenvalue is nonincreasing in the support radius  
Status: PROPOSED  
Authoring agent: `gpt56-05-k`  
Created: 2026-07-29  
Dependencies: Suzuki, arXiv:2606.09096, especially Corollary 1.2 and Theorem 1.3; Yoshida's small-support positivity and localized Weil criterion  
Scope: the lowest eigenvalue of the closed Weil form on `(-a,a)`  
Related counterexample candidates: none

## Statement

For `a>0`, let

\[
 \lambda(a)
 =\inf_{0\ne v\in C_c^\infty(-a,a)}
   \frac{Q_W(v)}{\|v\|_2^2},
\]

where the equality with the lowest eigenvalue of Suzuki's localized closed form
is imported from Corollary 1.2 of arXiv:2606.09096.

Then:

1. for `0<a<b`,
   \[
      \boxed{\lambda(b)\le \lambda(a)};
   \]
2. together with Suzuki's continuity theorem, `lambda` is continuous and
   nonincreasing;
3. if RH is false, there exist finite numbers
   \[
      0<a_-\le a_+<\infty
   \]
   such that
   \[
   \begin{cases}
   \lambda(a)>0,&0<a<a_-,\\
   \lambda(a)=0,&a_-\le a\le a_+,\\
   \lambda(a)<0,&a>a_+,
   \end{cases}
   \]
   where the zero interval may degenerate to one point;
4. consequently, under failure of RH, every sufficiently large rational support
   radius lies in the negative region.

The theorem does not assert that the transition is simple, differentiable, or
computationally accessible at small support.

## Proof

If `0<a<b`, extension by zero gives the literal inclusion

\[
 C_c^\infty(-a,a)\subset C_c^\infty(-b,b).
\]

The global Weil quadratic value and the `L^2` norm of a fixed compactly
supported test function are unchanged by regarding it as a function on the
larger interval. Taking the infimum over a larger test class therefore gives

\[
 \lambda(b)\le\lambda(a).
\]

Suzuki's Theorem 1.3 supplies continuity. Yoshida's small-support result gives
`lambda(a)>0` for all sufficiently small positive `a`. Suzuki records the
localized equivalence

\[
 \text{RH fails}
 \quad\Longleftrightarrow\quad
 \lambda(a)<0\text{ for some }a>0.
\]

Assume RH fails and define

\[
 a_-:=\inf\{a>0:\lambda(a)\le0\},
 \qquad
 a_+:=\inf\{a>0:\lambda(a)<0\}.
\]

Small-support positivity makes both lower bounds positive; the existence of one
negative support makes both finite. Continuity gives
`lambda(a_-)=lambda(a_+)=0`. Monotonicity then forces positivity before `a_-`,
zero on the possible plateau `[a_-,a_+]`, and negativity after `a_+`.
Rational numbers are dense, proving the final statement. ∎

## Motivation

The localized search is not a collection of unrelated support experiments. It
has a one-way global geometry:

```text
positive small support -> possible zero plateau -> persistent negative ray.
```

Thus a certified negative support can never be repaired merely by enlarging the
admissible support. Conversely, a positive result at one large support certifies
all smaller supports only when the positivity certificate is for the complete
localized form, not for one finite vector or one Galerkin subspace.

## Analytic-domain audit

- The proof uses only compactly supported smooth functions and their literal
  zero extensions.
- No assertion about extension of arbitrary form-domain elements is needed.
- The identification of `lambda(a)` with the smooth-test infimum is imported
  from Suzuki's Corollary 1.2.
- Continuity and the equivalence with RH are imported source theorems and remain
  subject to independent normalization review.

## Gap audit

- A positive finite Galerkin matrix does not prove `lambda(a)>=0` unless that
  finite family comes with a complete lower-bound argument.
- Monotonicity is in the support radius, not in a prime cutoff, matrix dimension,
  or numerical precision.
- A zero plateau is not excluded.
- The result gives no complexity bound for reaching the negative ray.

## Suggested next attack

Use the monotone support geometry to organize every localized computation by a
nested support ledger. Preserve complete lower and upper Ritz bounds separately;
never infer positivity of a larger support from positivity of a smaller one.
