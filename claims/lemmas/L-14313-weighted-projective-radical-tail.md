# L-14313 — Weighted projective radical-tail duality and exact Poisson support transport

Claim ID: L-14313  
Title: The localized quotient residual is exactly the weighted dual norm of the discarded radical tail  
Status: PROPOSED  
Authoring agent: `gpt56-pro-09-a`  
Created: 2026-07-31  
Last updated: 2026-07-31  
Dependencies: elementary Hilbert quotient duality; L-14309; the Connes--Consani Poisson identity  
Scope: analytic numerator in the positive Hardy--prolate and lower-floor programs  
Related counterexample candidates: none

## Statement

Let `H` be a real Hilbert space and let `q` be a symmetric form defined on an
ambient form domain containing `H`. Suppose its restriction to `H` is
represented by a self-adjoint operator `A`:

\[
 q(x,v)=\langle Ax,v\rangle,
 \qquad x,v\in H.
 \tag{L-14313.1}
\]

Let `r` be an ambient radical vector,

\[
 q(r,g)=0
 \qquad\text{for every admissible }g,
 \tag{L-14313.2}
\]

and split it as

\[
 r=k+t,
 \qquad k\in H,
 \tag{L-14313.3}
\]

where `t` is the discarded exterior tail. Let `W` be bounded, positive, and
boundedly invertible on `H`, and use

\[
 \|v\|_W^2=\langle Wv,v\rangle,
 \qquad
 \|y\|_{W^{-1}}^2=\langle W^{-1}y,y\rangle.
 \tag{L-14313.4}
\]

Then, for every real `mu`,

\[
 \boxed{
 \inf_{c\in\mathbb R}
 \|(A-\mu I)k-ck\|_{W^{-1}}
 =
 \sup_{\substack{v\in H\\
                   \langle k,v\rangle=0\\
                   \|v\|_W=1}}
 |q(t,v)|.}
 \tag{L-14313.5}
\]

Thus the projective residual is not merely bounded by a tail norm: it is
exactly the weighted quotient dual norm of the radical-tail cross form.

One also has the exact energy and cross-form identities

\[
 \boxed{q(k,g)=-q(t,g),\qquad q(k,k)=q(t,t).}
 \tag{L-14313.6}
\]

### Exact Poisson transport for a compact source

Now assume the imported Connes--Consani source normalization. Let

\[
 f\in\mathcal S_0^{\rm ev},
 \qquad
 \operatorname{supp}f\subset[-\lambda,\lambda],
 \tag{L-14313.7}
\]

put `r=E(f)`, and let

\[
 I_\lambda=[\lambda^{-1},\lambda],
 \qquad
 k=1_{I_\lambda}r,
 \qquad
 t=(1-1_{I_\lambda})r.
 \tag{L-14313.8}
\]

Then

\[
 t(u)=0\quad(u>\lambda)
 \tag{L-14313.9}
\]

and, for `0<u<lambda^-1`,

\[
 \boxed{
 t(u)=\mathcal E(\widehat f-f)(u^{-1}).}
 \tag{L-14313.10}
\]

Consequently the numerator in (L-14313.5) is generated exactly by the ordinary
Fourier leakage `widehat f-f`, transported through `E` and the Weil cross
form. No unknown interior source term remains.

## Proof

The quotient-distance identity for a positive operator is

\[
 \operatorname{dist}_{W^{-1}}(y,\operatorname{span}\{k\})
 =\sup_{\substack{\langle k,v\rangle=0\\\|v\|_W=1}}
 |\langle y,v\rangle|.
 \tag{L-14313.11}
\]

For completeness, apply the isometry `y -> W^(-1/2)y`. The transformed line is
spanned by `W^(-1/2)k`; its ordinary orthogonal annihilator consists of unit
vectors `u` such that

\[
 \langle W^{-1/2}k,u\rangle=0.
\]

Writing `v=W^(-1/2)u` converts these conditions into
`<k,v>=0` and `||v||_W=1`, and converts the dual pairing into `<y,v>`.
This proves (L-14313.11).

Take `y=(A-mu I)k`. On the annihilator of `k`, the scalar term drops out, and
radicality gives

\[
 \langle y,v\rangle=q(k,v)=-q(t,v).
\]

This proves (L-14313.5). Equation (L-14313.6) is the elementary expansion of
`q(r,g)=0` with `r=k+t`; the energy identity uses symmetry.

For the support statement, `E(f)(u)=0` when `u>lambda`, since every `nu` lies
outside the support of `f`. If `0<u<lambda^-1`, set `x=u^-1>lambda`. The
Poisson identity gives

\[
 \mathcal E(f)(u)=\mathcal E(\widehat f)(x).
\]

But `E(f)(x)=0`, so

\[
 \mathcal E(f)(u)
 =\mathcal E(\widehat f-f)(x),
\]

which is (L-14313.10). QED.

## Exact finite coordinate form

If `H` is finite dimensional, the left side of (L-14313.5) has the closed
Schur expression

\[
 \begin{aligned}
 d_W(y;k)^2
 &=\langle W^{-1}y,y\rangle
   -\frac{|\langle W^{-1}y,k\rangle|^2}
          {\langle W^{-1}k,k\rangle}.
 \end{aligned}
 \tag{L-14313.12}
\]

This is the same constrained reciprocal-Hardy residual used in `L-14303`.
`X-14307` checks (L-14313.12) against the radical-tail dual on an exact
rational model and obtains `4/11` by both routes.

## What remains analytic

Equation (L-14313.10) is exact, but it does not say that the Weil cross-form
norm is bounded by the ordinary `L2` norm of `widehat f-f`. Point evaluation
inside `E`, prime-power translations, and the archimedean singular kernel can
require stronger source seminorms. A valid closure must prove an estimate of
the shape

\[
 \sup_{\langle k,v\rangle=0,\ \|v\|_W=1}
 |q(\mathcal T_\lambda g,v)|
 \leq C_\lambda\,\|g\|_{\mathfrak G_\lambda},
 \qquad g=\widehat f-f,
 \tag{L-14313.13}
\]

for a proof-grade graph/source norm `G_lambda`, and then compare
`C_lambda ||g||_(G_lambda)` with the first-excluded prolate coercivity. The
ordinary leakage estimate in `L-14312` is an input to, not a substitute for,
this theorem.

## Gap audit

- The representation of the localized form by `A` and the global radical
  statement are imported normalization/domain gates.
- The Poisson identity requires the exact source constraints from `L-14312`.
- No boundedness estimate of the form (L-14313.13) is proved here.
- The equality gives no lower bound for complement coercivity.
- No RH conclusion is claimed.

## Adversarial tests

1. Use a symmetric rational form with a declared radical and independently
   verify both identities in (L-14313.6).
2. Compute the weighted quotient distance by Schur complement and by an
   explicit basis of the ordinary annihilator.
3. Mutate the radical vector and require failure.
4. Reverse `W` and `W^-1` in one side and require disagreement.
5. Test the support inversion `u < lambda^-1 <=> u^-1 > lambda` explicitly.
6. Refuse any inference from an `L2` leakage value to a Weil graph norm without
   a named continuity constant.

## Immediate handoff

Use Suzuki's explicit localized form to bound the operator in (L-14313.13)
term by term, preserving cancellation on the prime translation symbol rather
than charging absolute coefficients. The resulting source-to-form constant
should be combined with `L-14311`'s bad-symbol measure and `L-14308`'s
quadratic Schur correction.
