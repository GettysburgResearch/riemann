# L-12204 — Reduced contraction for one moving anchor

Claim ID: L-12204  
Title: The sole moving-anchor moment is reconstructed from one new-old point difference and the old moment table  
Status: PROPOSED  
Authoring agent: `gpt56-05-j`  
Created: 2026-07-26  
Dependencies: L-12201; L-9309  
Scope: independent directed replay of the new scalar `c_0`  
Related counterexample candidates: moving-anchor direct-xi witnesses

## Statement

Use the old nodes `u_1,...,u_n`, old denominator

\[
 D(y)=\prod_{i=1}^{n}(y+u_i),
\]

and a distinct new node `t>0`. Let `F(u)` be the direct-xi logarithmic residual in one fixed normalization and count-deflation profile.

Let

\[
 \beta_t=-\frac1{D(-t)}
\]

be the new-node coefficient of the response-`1` portfolio, and let `gamma_i` be its old-node coefficients. Fix any old reference index `r` and define

\[
 \delta_i=\gamma_i+\beta_t1_{i=r}.
\]

Then `sum_i delta_i=0`, so there is a unique old response polynomial `P_(t,r)` of degree at most `n-2`. The new scalar satisfies

\[
 \boxed{
 c_0
 =\beta_t\bigl(F(t)-F(u_r)\bigr)
  +L_{\rm old}(P_{t,r}).
 }
\]

Moreover,

\[
 \boxed{
 P_{t,r}(y)
 =\frac{1+\beta_tD(y)}{y+t}
  -\beta_t\frac{D(y)}{y+u_r}.
 }
\]

The nominal degree-`n-1` terms cancel, so `deg P_(t,r)<=n-2`.

## Proof

The full response vector has zero sum:

\[
 \beta_t+\sum_i\gamma_i=0.
\]

Hence

\[
 \sum_i\delta_i=0.
\]

By the L-9309 response-map isomorphism, `delta` has a unique old response polynomial `P_(t,r)` of degree at most `n-2`. Therefore

\[
 \begin{aligned}
 c_0
 &=\beta_tF(t)+\sum_i\gamma_iF(u_i)\\
 &=\beta_t\bigl(F(t)-F(u_r)\bigr)
   +\sum_i\delta_iF(u_i)\\
 &=\beta_t\bigl(F(t)-F(u_r)\bigr)
   +L_{\rm old}(P_{t,r}).
 \end{aligned}
\]

The restricted old-node coefficients `gamma` have response polynomial

\[
 P_\gamma(y)=\frac{1+\beta_tD(y)}{y+t}
\]

by L-12201. Adding `beta_t` to the reference coefficient adds old response

\[
 -\beta_t\frac{D(y)}{y+u_r}.
\]

This gives the displayed closed form. Since `delta` is zero sum, its response degree is at most `n-2`; equivalently the leading terms cancel directly. ∎

## Directed overlap gate

Let `I_direct` be the interval obtained from the full `(n+1)`-point barycentric contraction and let `I_reduced` be the interval obtained from the boxed identity using:

- a directed interval for `F(t)-F(u_r)`;
- directed old moment intervals;
- exact rational coefficients of `P_(t,r)`.

Both enclose the same exact scalar. Therefore

\[
 \boxed{I_{\rm direct}\cap I_{\rm reduced}\ne\varnothing.}
\]

Failure of overlap is a deterministic proof-pipeline error. Their intersection is itself a valid, usually narrower enclosure.

## Reference-node choice

The point-difference interval is multiplied by `|beta_t|`. A useful deterministic selection rule is to minimize the exact bound

\[
 |\beta_t|\operatorname{width}(F(t)-F(u_r))
 +\sum_k|p_{t,r,k}|\operatorname{width}(a_k)
\]

over old references `r`. The searcher may estimate this cheaply, but the final producer records the exact chosen reference and full width ledger.

For anchors well to the right of the old microscopic PR #103 grid, the nearest old node is usually a reasonable but not theorem-optimal choice.

## Easy-half-plane specialization

When `sqrt(t)+1/2>1`, the new direct-xi point lies in the absolutely convergent half-plane. It may be evaluated through a directed Euler product or Dirichlet-series backend while the old reference remains on the Riemann-Siegel table. The common completed-xi scale cancels exactly in the point difference.

This provides a deliberately independent arithmetic fingerprint from the full barycentric replay.

## Analytic domain audit

Every logarithm is taken from a completed-xi modulus rectangle excluding zero. The old and new residuals must use the same additive scale, ordinate, and deflation terms before forming their difference.

## Gap audit

- The sign in `beta_t=-1/D(-t)` is essential.
- The reference correction subtracts `beta_t D/(y+u_r)`.
- Mixing scaled and unscaled logarithms without exact cancellation invalidates the identity.
- Old moments from another ordinate or count profile cannot be reused.
- Overlap is an algebraic consistency gate, not statistical independence.

## Adversarial tests

- Reconstruct `c_0` directly and through every possible old reference on a small rational table.
- Mutate the new-node sign and require all reduced intervals to disagree.
- Add an arbitrary common constant to every `F` value and verify exact invariance.
- Use mismatched old moments and require the overlap gate to fail.

## Suggested next attack

Implement both direct and reduced contractions for the `t=4` PR #103 control. The new point is in `Re(s)=5/2`, so a directed Euler-product evaluation supplies a strongly independent cross-check of the Riemann-Siegel primitive table.