# Compact source changes can preserve entry and create a nonreal zero

Status: proposed analytic counterexample with explicit Rouché margins.
Scope: smooth positive densities with the same eventual theta tail.
This is not a perturbation claim about the arithmetic source being arbitrary.

Use the true even theta density in the convention

\[
\Phi_\theta(u)=\sum_{n\ge1}
 \bigl(4\pi^2n^4e^{9u/2}-6\pi n^2e^{5u/2}\bigr)
 e^{-\pi n^2e^{2u}},\quad u\ge0,
\qquad \Xi(z)=2\int_0^\infty\Phi_\theta(u)\cos(zu)\,du.
\]

Its positivity, even smooth extension and normalization are the inherited
classical theta/Mellin inputs reconstructed in
`reviews/D-pass3/PROOFS_AND_REPAIRS.md#R16`. We do not assert RH to use them.

## 1. Smooth positive density with a certified nonreal zero

Fix `0<delta<=log 2`, `c=cosh delta`, `epsilon=c/cosh(2 delta)` and
`z_0=pi+i delta`. Write `s=sinh delta`, and choose

\[
0<a\le\min\{\delta/4,1/4,s/(4\cosh(\delta+1))\}.
\]

Let `h` be any even, nonnegative, normalized `C^infinity` bump with support
`[-eta,eta]`, where

\[
0<\eta<\min\{1/4,\log(3/2)/(|z_0|+a)\}.
\]

Define its entire transform `B(z)=integral h(v)exp(izv)dv`. On the closed
disk `|z-z_0|<=a`,

\[
|B(z)-1|\le e^{\eta |z|}-1<1/2,\quad |B(z)|>1/2.   \tag{T1}
\]

For `C(z)=cos z+epsilon cos(2z)`, the factorization (D1) gives a direct
boundary bound. Taylor's formula on `|z-z_0|=a` yields

\[
|\cos z+c|\ge sa-\tfrac12a^2\cosh(\delta+a)
             \ge7sa/8.
\]

Also

\[
|\cos z-1/(2c)|
 \ge c+1/(2c)-a\cosh(\delta+a)\ge3c/4.
\]

Hence

\[
|B(z)C(z)|>\epsilon c s a/2.                       \tag{T2}
\]

Put

\[
K=2\int_0^\infty\Phi_\theta(u)\cosh((\delta+a)u)\,du>0,
\qquad 0<\tau\le\epsilon csa/(4K).
\]

The explicit positive smooth source

\[
\Phi_*(u)=\tfrac12h(u-1)+\tfrac\epsilon2h(u-2)
                         +\tau\Phi_\theta(u),\qquad u\ge0
\]

has even smooth extension and is strictly positive. Its transform is

\[
F_*(z)=B(z)C(z)+\tau\Xi(z).                         \tag{T3}
\]

On the boundary disk, `|tau Xi(z)|<=tau K<=epsilon csa/4`, strictly below
(T2). Rouché therefore gives exactly one zero in this disk: B is zero-free
there, and C has exactly the simple zero z_0 there. Since `a<=delta/4`,
the disk is disjoint from the real axis. Reality and evenness yield the
conjugate and reflected nonreal zeros as well.

For every `u>2+eta`, `Phi_*(u)=tau Phi_theta(u)` **exactly**. Therefore
the eventual log-tail derivative identities

\[
(\log\Phi_*)'=9/2-2\pi e^{2u}+O(e^{-2u}),\qquad
(\log\Phi_*)''=-4\pi e^{2u}+O(e^{-2u})
\]

are identical to those used by the repaired high-order entry proof. On every
bounded interval the source is strictly positive and smooth, so its second
log derivative is bounded above. The log-concavity and local-quadratic/
exterior-exponential argument of `reviews/A/supplement/REPORT.md#S06`
therefore applies to this density as well, with constants and the starting
order allowed to depend on the chosen perturbation. It gives high-order
complete lower-ray entry in the same regime `T^2 log r/r ->0`, even though
the original transform has a nonreal zero.

This is a source-class obstruction: the tail and the generic high-order entry
mechanism cannot themselves establish low-order descent. It does not claim
the smooth perturbation's positive derivatives are globally real-rooted;
that stronger property belongs to the separate discrete model.

## 2. A uniform quantitative compact-source invisibility bound

The obstruction can also be seen directly at the source level. Let
`Phi_*=tau Phi_theta+b`, with `b>=0` supported in `[0,U]`, total mass B_0.
Choose any fixed `V>U` and

\[
C_V=\int_V^{V+1}\Phi_\theta(u)\,du>0.
\]

For `r>=0` and `y>=0`, the ratio of compact to theta positive tilted masses
satisfies

\[
q_{r,y}=\frac{\int u^re^{yu}b(u)\,du}
                 {\tau\int u^re^{yu}\Phi_\theta(u)\,du}
 \le\frac{B_0}{\tau C_V}(U/V)^r e^{-y(V-U)}.         \tag{T4}
\]

For r=0, use the usual convention `u^0=1`. This is just an upper bound by
`B_0 U^r e^{yU}` and a lower bound by `tau C_V V^r e^{yV}`; no saddle
approximation is hidden in it.

Let `nu_*` and `nu_theta` be the corresponding normalized positive tilted
probability measures. The mixture formula gives

\[
\|\nu_*-\nu_\theta\|_{\rm TV}
 \le q_{r,y}/(1+q_{r,y}),                            \tag{T5}
\]

where TV means `sup_A |nu_*(A)-nu_theta(A)|` (the L1 density bound has an
extra factor two). Since V can be fixed arbitrarily large before r grows,
compact-source effects on these normalized measures decay faster than any
prescribed fixed exponential in r, uniformly for y>=0. Weighted moment
versions follow by applying the same bound with r replaced by r+k and using
the explicit normalization; total variation alone is not asserted to control
unbounded observables.

Thus even an exponentially accurate high-order positive-source description
can miss a genuine low-order nonreal zero. A descent theorem must price the
complete source at low orders rather than infer it from tail universality.
