# L-14307 — Fixed-support residual-limit and no-free-cutoff theorem

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

The cofinal criterion in L-14305 contains the constrained reciprocal-Hardy
numerator

\[
 \mathcal R_W(z_N;p_N),
 \qquad
 p_N=P_Nk,
 \qquad
 z_N=(A_N-\mu_NI)p_N.
\]

It is tempting to hope that this numerator becomes small merely by increasing
the Fourier cutoff `N`.  This lemma shows that, under the natural graph-limit
hypothesis, it instead converges to the residual of the ambient target `k`.
Thus cutoff refinement removes discretization error but cannot remove a genuine
failure of `k` to be an eigenvector of the fixed-support Weil operator.

## Statement

Let `K` be a real or complex Hilbert space and let `A` be self-adjoint on
`D(A)`.  Let

\[
 H_1\subset H_2\subset\cdots\subset D(A)
\]

be finite-dimensional subspaces with ordinary orthogonal projections `P_N`.
Let `k in D(A)` be nonzero and put

\[
 p_N=P_Nk.
 \tag{L-14307.1}
\]

Assume the **graph approximation**

\[
 \boxed{
 \|p_N-k\|+\|Ap_N-Ak\|\longrightarrow0.}
 \tag{L-14307.2}
\]

For every sufficiently large `N`, define the finite compression

\[
 A_N=P_NA|_{H_N},
 \qquad
 \mu_N=\frac{\langle A_Np_N,p_N\rangle}{\|p_N\|^2},
 \qquad
 z_N=(A_N-\mu_NI)p_N.
 \tag{L-14307.3}
\]

Define also the ambient Rayleigh quotient and residual

\[
 \mu=\frac{\langle Ak,k\rangle}{\|k\|^2},
 \qquad
 z=(A-\mu I)k.
 \tag{L-14307.4}
\]

Then

\[
 \boxed{\mu_N\longrightarrow\mu,\qquad z_N\longrightarrow z.}
 \tag{L-14307.5}
\]

Let `W` be bounded, positive and boundedly invertible.  For nonzero `p`, set

\[
 \mathcal R_W(y;p)^2
 :=\langle W^{-1}y,y\rangle
 -\frac{|\langle W^{-1}y,p\rangle|^2}
        {\langle W^{-1}p,p\rangle}.
 \tag{L-14307.6}
\]

Then

\[
 \boxed{
 \mathcal R_W(z_N;p_N)\longrightarrow
 \mathcal R_W(z;k).}
 \tag{L-14307.7}
\]

Moreover,

\[
 \boxed{
 \mathcal R_W(y;p)
 =\inf_{c\in\mathbb C}\|y-cp\|_{W^{-1}},}
 \tag{L-14307.8}
\]

with real scalars in the real case.  Consequently,

\[
 \boxed{
 \mathcal R_W(z;k)=0
 \iff z\in\mathbb Ck
 \iff Ak\in\mathbb Ck
 \iff k\text{ is an eigenvector of }A.}
 \tag{L-14307.9}
\]

(The middle equivalence uses the definition of `z=(A-mu I)k`.)

## Quantitative finite-cutoff form

Put

\[
 e_N=\|p_N-k\|,
 \qquad
 d_N=\|Ap_N-Ak\|.
 \tag{L-14307.10}
\]

Suppose `e_N<=||k||/2`.  Then `||p_N||>=||k||/2`, and a direct quotient
estimate gives

\[
 |\mu_N-\mu|
 \leq
 \frac{2}{\|k\|}\,d_N
 +\frac{2(|\mu|+d_N/\|k\|)}{\|k\|}\,e_N.
 \tag{L-14307.11}
\]

Also

\[
 \boxed{
 \|z_N-z\|
 \leq d_N+|\mu_N-\mu|\,\|p_N\|+|\mu|e_N.}
 \tag{L-14307.12}
\]

Since `W^{-1}` is bounded and the denominator in (L-14307.6) stays away
from zero, these estimates turn any proof-grade graph-tail bounds `e_N,d_N`
into a directed enclosure comparing the finite and ambient constrained
residuals.

## Proof

Because `p_N -> k` and `Ap_N -> Ak`, one has

\[
 \langle Ap_N,p_N\rangle\to\langle Ak,k\rangle,
 \qquad
 \|p_N\|^2\to\|k\|^2>0.
\]

Also `A_Np_N=P_NAp_N`.  Since `P_N -> I` strongly on every vector that is
approximated by the nested union, and in particular

\[
 \|P_NAp_N-Ak\|
 \leq\|Ap_N-Ak\|+\|(I-P_N)Ak\|\to0,
\]

we obtain `mu_N -> mu` and

\[
 z_N=P_NAp_N-\mu_Np_N\to Ak-\mu k=z.
\]

This proves (L-14307.5).

Formula (L-14307.6) is continuous in `(y,p)` whenever `p` is nonzero, because
`W^{-1}` is bounded and

\[
 \langle W^{-1}p,p\rangle>0.
\]

Together with (L-14307.5) this proves (L-14307.7).

For (L-14307.8), expand

\[
 \|y-cp\|_{W^{-1}}^2
 =\langle W^{-1}y,y\rangle
 -2\operatorname{Re}\!\left(
 c\langle W^{-1}p,y\rangle\right)
 +|c|^2\langle W^{-1}p,p\rangle.
\]

Completing the square gives the minimizer

\[
 c_*=\frac{\langle W^{-1}y,p\rangle}
           {\langle W^{-1}p,p\rangle}
\]

under the convention that the inner product is linear in its first argument,
and the minimum is (L-14307.6).  The minimum vanishes exactly when `y` belongs
to the line spanned by `p`.  Applying this to `y=z` gives (L-14307.9).

For the quantitative statements, write

\[
 \mu_N-\mu
 =\frac{\langle Ap_N-Ak,p_N\rangle
       +\langle Ak,p_N-k\rangle}{\|p_N\|^2}
 +\mu\frac{\|k\|^2-\|p_N\|^2}{\|p_N\|^2}
\]

and use `||p_N||>=||k||/2`, Cauchy--Schwarz, and

\[
 |\|p_N\|^2-\|k\|^2|
 \leq e_N(\|p_N\|+\|k\|).
\]

A slightly looser collection of these terms yields (L-14307.11).
Finally add and subtract `mu_N p_N` and `mu p_N` to obtain
(L-14307.12).  QED.

## Hardy specialization

For the positive route at fixed `lambda`, take

\[
 W=W_\tau=2\cosh(2\tau t)
\]

on the compact interval `[-log lambda,log lambda]`.  Both `W` and `W^{-1}`
are bounded, with

\[
 2I\preceq W\preceq2\lambda^{2\tau}I,
 \qquad
 (2\lambda^{2\tau})^{-1}I\preceq W^{-1}\preceq\tfrac12I.
\]

Thus the theorem applies whenever the Fourier projections of `k_lambda`
converge in the graph norm of the ambient Weil operator `A_lambda`.

The fixed-support limiting numerator is then

\[
 \mathcal R_{W_\tau}
 \left((A_\lambda-\mu_\lambda I)k_\lambda;k_\lambda\right),
 \tag{L-14307.13}
\]

not zero by virtue of Fourier refinement alone.

## Consequence for the global program

The residual/coercivity target should be split into two independently visible
budgets:

1. **cutoff error:** certify graph-tail control comparing the finite residual
   with (L-14307.13);
2. **ambient prolate defect:** prove that, along `lambda -> infinity` and
   `tau -> 1/2`, the ambient constrained residual is small compared with the
   weighted complement coercivity.

The second budget is the genuinely analytic content.  It is where the trace
formula relating the Weil quadratic form, the time/frequency projections, and
the map `E` must enter.  Merely increasing `N` addresses only the first budget.

## Gap audit

- The theorem does **not** assert graph convergence for the CCM target.  This is
  a separate domain/regularity obligation for the unbounded ambient operator.
- It does not assert that the ambient residual in (L-14307.13) is nonzero; it
  identifies its exact meaning and proves that zero is equivalent to an exact
  eigenvector.
- It gives no lower bound for the coercivity `h`.
- It does not prove RH.
- For a changing support `lambda`, every object changes; the fixed-support limit
  must not be interchanged with the `lambda -> infinity` limit without a
  uniform theorem.

## Immediate proof-producing handoff

At each retained `lambda`, compute graph-tail bounds for

\[
 \|(I-P_N)k_\lambda\|,
 \qquad
 \|A_\lambda(P_Nk_\lambda)-A_\lambda k_\lambda\|,
\]

or an equivalent quadratic-form residual bound.  Then report separately:

```text
finite constrained residual
cutoff comparison radius
ambient constrained residual enclosure
weighted coercivity h
ambient-residual / h
```

A flat finite numerator as `N` grows is expected when the ambient prolate defect
dominates; it is not evidence that additional precision or a larger cutoff will
close the route.