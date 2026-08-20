# L-100001 — The critical quadratic and cubic Peano kernels

Claim ID: `L-100001`  
Status: **PROVED EXACT REDUCTION; CRITICAL SIGN OPEN**  
Created: 2026-08-20  
Depends on: `L-100000`; PR #668 quadratic variation descent  
RH status: **unproved**

The first open member of the hierarchy occurs already at `m=2`.

## 1. Quadratic critical remainder

Put

\[
H_2^U(x)=\sum_{n\le x}{\beta(n)\over\sqrt n}U(x/n)^2
\]

and

\[
\boxed{
C_2(x)=16\mathcal B(3/2)x-H_2^U(x).
}
\tag{L-100001.1}
\]

It has the absolutely convergent form

\[
C_2(x)
=16x\sum_{n\ge1}{\beta(n)\over n^{3/2}}
 \kappa_{2,1}(\sqrt{n/x}),
\]

where

\[
\kappa_{2,1}(t)=
\begin{cases}
2t-t^2,&0<t\le1,\\
1,&t\ge1.
\end{cases}
\tag{L-100001.2}
\]

The kernel is positive, but its sharp owner ratio is `1/q`; hence the labelled
level argument stops at the divergent prime harmonic series.

Writing

\[
G_2(u)=e^{-u}H_2^U(e^u),
\]

one has

\[
C_2(e^u)=e^u[16\mathcal B(3/2)-G_2(u)].
\tag{L-100001.3}
\]

Thus pointwise positivity of `C_2` is exactly the global upper-envelope theorem
for the normalized positive quadratic transform. PR #668 proves that the
corresponding critically weighted downward variation is RH-equivalent; ordinary
bounded variation is insufficient.

## 2. Cubic descent

Put

\[
H_3^U(x)=\sum_{n\le x}{\beta(n)\over\sqrt n}U(x/n)^3,
\]

\[
R_{3,1}(x)=64\mathcal B(2)x^{3/2}-H_3^U(x),
\]

and

\[
\boxed{
C_3(x)=192\mathcal B(3/2)x-R_{3,1}(x).
}
\tag{L-100001.4}
\]

`L-100000` proves `R_(3,1)>0` unconditionally. The differential identities

\[
(D-3/2)U^3=6U^2,
\qquad
(D-1)U^2=4U,
\qquad D=x{d\over dx},
\tag{L-100001.5}
\]

hold without activation atoms because `U^2` and `U^3` are clamped to the
required orders at `1`. Hence

\[
(D-3/2)R_{3,1}=-6H_2^U.
\]

Using the vanishing boundary at infinity gives the positive tail formula

\[
\boxed{
R_{3,1}(x)
=6x^{3/2}\int_x^\infty H_2^U(t)t^{-5/2}\,dt>0.
}
\tag{L-100001.6}
\]

Subtracting the exact leading term yields

\[
\boxed{
C_3(x)
=6x^{3/2}\int_x^\infty C_2(t)t^{-5/2}\,dt.
}
\tag{L-100001.7}
\]

Therefore

\[
C_2\ge0\Longrightarrow C_3\ge0,
\]

and the cubic criterion is a positive smoothing of the exact quadratic
critical envelope.

## 3. Self-reciprocal cubic kernel

The cubic remainder has the literal source form

\[
\boxed{
C_3(x)=\sum_{n\ge1}{\beta(n)\over\sqrt n}\Psi(x/n),
}
\tag{L-100001.8}
\]

where

\[
\Psi(y)=64
\begin{cases}
3y-y^{3/2},&0<y\le1,\\
3\sqrt y-1,&y\ge1.
\end{cases}
\tag{L-100001.9}
\]

It is strictly positive and obeys

\[
\Psi(y)=y^{3/2}\Psi(1/y).
\tag{L-100001.10}
\]

In logarithmic coordinate,

\[
k(u)=e^{-3u/4}{\Psi(e^u)\over64}
=3e^{-|u|/4}-e^{-3|u|/4}.
\]

Its Fourier transform is

\[
\boxed{
\widehat k(\gamma)
={3/4\over(\gamma^2+1/16)(\gamma^2+9/16)}>0.
}
\tag{L-100001.11}
\]

Thus the translate Gram of the critical cubic kernel is positive semidefinite.
This does **not** sign the linear Möbius convolution (L-100001.8). For example,
`delta_0-2 delta_(log 2)` has negative convolution value at zero despite
(L-100001.11). The PSD property is retained as a useful cross-core geometry,
not promoted to a pointwise theorem.
