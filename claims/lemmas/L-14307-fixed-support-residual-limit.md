# L-14307 — Fixed-support residual limit and no-free-cutoff theorem

Claim ID: L-14307  
Title: Fourier refinement cannot remove a nonzero ambient prolate eigen-residual  
Status: PROPOSED  
Authoring agent: `gpt56-pro-09-a`  
Created: 2026-07-30  
Last updated: 2026-07-30  
Dependencies: elementary graph convergence for a self-adjoint operator; L-14303  
Scope: structural interpretation of the remaining numerator in the positive Hardy--prolate route  
Related counterexample candidates: none

## Purpose

The cofinal criterion in L-14305 contains

\[
 \mathcal R_W(z_N;p_N),\qquad
 p_N=P_Nk,\qquad
 z_N=(A_N-\mu_NI)p_N.
\]

This lemma shows that, at fixed support, increasing the Fourier cutoff removes
only discretization error. Under graph convergence, the finite numerator tends
to the ambient failure of the prolate target to be an eigenvector of the Weil
operator. Thus a genuine ambient defect cannot be eliminated by cutoff polishing.

## Statement

Let `K` be a real or complex Hilbert space and let `A` be self-adjoint on
`D(A)`. Let

\[
 H_1\subset H_2\subset\cdots\subset D(A)
\]

be finite-dimensional subspaces with orthogonal projections `P_N`. Let
`k in D(A)` be nonzero and put `p_N=P_Nk`. Assume

\[
 \boxed{\|p_N-k\|+\|Ap_N-Ak\|\longrightarrow0.}
 \tag{L-14307.1}
\]

For sufficiently large `N`, define

\[
 A_N=P_NA|_{H_N},\qquad
 \mu_N=\frac{\langle A_Np_N,p_N\rangle}{\|p_N\|^2},\qquad
 z_N=(A_N-\mu_NI)p_N.
 \tag{L-14307.2}
\]

Define the ambient Rayleigh quotient and residual

\[
 \mu=\frac{\langle Ak,k\rangle}{\|k\|^2},\qquad
 z=(A-\mu I)k.
 \tag{L-14307.3}
\]

Then

\[
 \boxed{\mu_N\to\mu,\qquad z_N\to z.}
 \tag{L-14307.4}
\]

Let `W` be bounded, positive and boundedly invertible. For nonzero `p`, set

\[
 \mathcal R_W(y;p)^2
 :=\langle W^{-1}y,y\rangle
 -\frac{|\langle W^{-1}y,p\rangle|^2}
        {\langle W^{-1}p,p\rangle}.
 \tag{L-14307.5}
\]

Then

\[
 \boxed{\mathcal R_W(z_N;p_N)\to\mathcal R_W(z;k).}
 \tag{L-14307.6}
\]

Moreover,

\[
 \boxed{
 \mathcal R_W(y;p)=\inf_{c\in\mathbb C}\|y-cp\|_{W^{-1}},}
 \tag{L-14307.7}
\]

with real scalars in the real case. Consequently,

\[
 \boxed{
 \mathcal R_W(z;k)=0
 \iff z\in\mathbb Ck
 \iff Ak\in\mathbb Ck
 \iff k\text{ is an eigenvector of }A.}
 \tag{L-14307.8}
\]

## Safe quantitative comparison

Put

\[
 e_N=\|p_N-k\|,\qquad d_N=\|Ap_N-Ak\|.
\]

Whenever `p_N` is nonzero, the following direct estimate is valid:

\[
 \boxed{
 |\mu_N-\mu|
 \leq
 \frac{d_N\|p_N\|+\|Ak\|e_N
       +|\mu|e_N(\|p_N\|+\|k\|)}
      {\|p_N\|^2}.}
 \tag{L-14307.9}
\]

Also

\[
 \boxed{
 \|z_N-z\|
 \leq
 d_N+\|(I-P_N)Ak\|
 +|\mu_N-\mu|\|p_N\|+|\mu|e_N.}
 \tag{L-14307.10}
\]

Thus proof-grade enclosures for `e_N`, `d_N`, and `||(I-P_N)Ak||` yield a
finite comparison between the computed residual and its ambient limit.

## Proof

Graph convergence gives

\[
 \langle Ap_N,p_N\rangle\to\langle Ak,k\rangle,
 \qquad
 \|p_N\|^2\to\|k\|^2>0,
\]

so `mu_N -> mu`. Also

\[
 A_Np_N=P_NAp_N
\]

and

\[
 \|P_NAp_N-Ak\|
 \leq\|Ap_N-Ak\|+\|(I-P_N)Ak\|\to0.
\]

Hence `z_N -> z`, proving (L-14307.4).

The expression in (L-14307.5) is continuous in `(y,p)` for nonzero `p`, since
`W^{-1}` is bounded and positive. This proves (L-14307.6).

Expanding `||y-cp||_{W^{-1}}^2` and completing the square gives the minimizer

\[
 c_*=rac{\langle W^{-1}y,p\rangle}
          {\langle W^{-1}p,p\rangle}
\]

under the convention that the inner product is linear in its first argument.
The minimum is exactly (L-14307.5), proving (L-14307.7). It vanishes precisely
when `y` belongs to the line spanned by `p`; applying this to
`y=(A-mu I)k` proves (L-14307.8).

For (L-14307.9), write

\[
 \mu_N-\mu
 =\frac{\langle Ap_N-Ak,p_N\rangle
       +\langle Ak,p_N-k\rangle}{\|p_N\|^2}
 +\mu\frac{\|k\|^2-\|p_N\|^2}{\|p_N\|^2}
\]

and use Cauchy--Schwarz together with

\[
 |\|p_N\|^2-\|k\|^2|
 \leq e_N(\|p_N\|+\|k\|).
\]

Finally,

\[
 z_N-z=P_N(Ap_N-Ak)-(I-P_N)Ak
       -(\mu_N-\mu)p_N-\mu(p_N-k),
\]

which gives (L-14307.10). QED.

## Hardy specialization

At fixed `lambda`, take

\[
 W=W_\tau=2\cosh(2\tau t)
\]

on `[-log lambda,log lambda]`. Then

\[
 2I\preceq W\preceq2\lambda^{2\tau}I,
 \qquad
 (2\lambda^{2\tau})^{-1}I\preceq W^{-1}\preceq\tfrac12I.
\]

Whenever the Fourier projections of `k_lambda` converge in the graph norm of
the ambient Weil operator `A_lambda`, the finite reciprocal-Hardy numerator
converges to

\[
 \boxed{
 \mathcal R_{W_\tau}
 \left((A_\lambda-\mu_\lambda I)k_\lambda;k_\lambda\right).}
 \tag{L-14307.11}
\]

It does not converge to zero merely because `N` grows.

## Strategic consequence

The remaining ratio must be separated into two budgets:

1. **cutoff budget:** compare the finite residual with (L-14307.11) using graph-tail bounds;
2. **ambient prolate budget:** prove, as `lambda -> infinity` and `tau -> 1/2`, that the ambient constrained residual is small compared with the weighted complement coercivity.

The second budget is the actual analytic obstacle. It is where the trace formula
relating the Weil form, the time/frequency projections, and the map `E` must
enter. Increasing `N` addresses only the first budget.

## Gap audit

- Graph convergence for the CCM target is not proved here.
- No sign or size is asserted for the ambient residual.
- No lower bound for the coercivity `h` is supplied.
- The fixed-support limit must not be interchanged with `lambda -> infinity`
  without a uniform theorem.
- This lemma does not prove RH.

## Immediate proof-producing handoff

At each retained support, report separately:

```text
finite constrained residual
cutoff comparison radius
ambient constrained residual enclosure
weighted coercivity h
ambient residual / h
```

A plateau in the finite numerator as `N` grows is expected when the ambient
prolate defect dominates. It is not evidence that more cutoff or precision will
close the route.