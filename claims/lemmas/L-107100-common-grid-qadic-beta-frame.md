# L-107100 — Common-grid q-adic second-difference frame for native beta

**Claim ID:** `L-107100`  
**Status:** proved exact finite-vector theorem; analytic inputs source-locked  
**Date:** 2026-08-31  
**RH:** not assumed

Let `q=67`,

\[
\mu^{\langle q\rangle}(n)=\mu(n)\mathbf 1_{q\nmid n},
\qquad
\beta=(\delta_1-\delta_q)^{*2}*\mu^{\langle q\rangle}.
\]

Fix an outer horizon `X`. Use one outer Poisson period, frequency grid and
hyperbolic detector weight

\[
t_{k,X}=2\pi k/P_A(X),\qquad
w_{k,X}=P_A(X)^{-1/2}e^{1-\cosh t_{k,X}}\widehat B(it_{k,X}),
\quad |k|\le K_A(X),
\]

where `B` is one fixed compact beta detector. The proofs of L-107020 and
L-107021 use only compact support, fixedness and noncancellation, so they apply
to this source-locked detector without changing it with `X`.

For `Y<=X`, define parent-grid vectors

\[
U_X(Y)=\left(w_{k,X}\sum_{n\le Y,\ q\nmid n}
\mu(n)n^{-1/2-it_{k,X}}\right)_k,
\]

\[
G_X(Y)=\left(w_{k,X}\sum_{n\le Y}
\beta(n)n^{-1/2-it_{k,X}}\right)_k.
\]

Put `J=floor(log_q X)`, `u_j=U_X(X/q^j)`, `g_j=G_X(X/q^j)`, extend by zero,
and set

\[
A_X=\operatorname{diag}(q^{-1/2-it_{k,X}}),\qquad \|A_X\|=q^{-1/2}=:a.
\]

Then every sharp cutoff is retained and

\[
\boxed{g_j=u_j-2A_Xu_{j+1}+A_X^2u_{j+2}.}\tag{1}
\]

With `S` the q-adic unilateral shift,

\[
\boxed{g=(I-A_XS)^2u.}\tag{2}
\]

Since `||A_XS||<=a<1`,

\[
\boxed{(1-a)^4\sum_j\|u_j\|^2
\le\sum_j\|g_j\|^2
\le(1+a)^4\sum_j\|u_j\|^2.}\tag{3}
\]

The inverse is finite at every `X`:

\[
\boxed{u_j=\sum_{m=0}^{J-j}(m+1)A_X^m g_{j+m}.}\tag{4}
\]

Thus the complete beta stack and one q-free central stack have the same power
exponent with constants independent of feature dimension. This is a
simultaneous vector statement, not the invalid same-prefix scalar multiplier
shortcut.
