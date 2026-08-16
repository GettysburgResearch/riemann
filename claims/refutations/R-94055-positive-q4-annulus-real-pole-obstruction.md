# R-94055 — The positive generalized-prime annulus cannot close the centered cubic criterion

Claim ID: `R-94055`  
Status: **PROPOSED COMPLETE EXACT SOURCE/POSITIVITY NO-GO — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: PR #474 `L-93019`; `L-94049`  
Scope: positivity and Mellin-pole shortcuts only; does not refute signed or bilinear arithmetic attacks

## 1. Positive generalized-prime source

Let

\[
G_4(s)={1\over A_4(s)}
 =\zeta(s){1-4^{-s}\over1-4^{1-s}},
\tag{R-94055.1}
\]

where \(A_4\) is the zero-safe Möbius source of `L-93019`. Define

\[
-{G_4'(s)\over G_4(s)}
 =\sum_{n\ge1}{\lambda_4(n)\over n^s}.
\tag{R-94055.2}
\]

The coefficients are nonnegative. For every odd prime \(p\),

\[
\lambda_4(p^k)=\log p.
\tag{R-94055.3}
\]

At powers of two,

\[
\boxed{
\lambda_4(2^e)
 =\begin{cases}
\log2,&e\text{ odd},\\
(2\cdot4^{e/2}-1)\log2,&e\text{ even}.
\end{cases}
}
\tag{R-94055.4}
\]

The compact-Q4 source is exactly

\[
\boxed{
c_\circ=(\varepsilon-4\delta_4)*\lambda_4.}
\tag{R-94055.5}
\]

This is the prime-source form of the logarithmic-derivative dictionary.

## 2. Exact positive annulus

Take the singular kernel \(H(x)=x^{-1}\) on \(0<x\le1\). Then

\[
H(x)-4H(4x)=0
\qquad(0<x\le1/4).
\tag{R-94055.6}
\]

Consequently

\[
\boxed{
\sum_{n\le N}c_\circ(n){N\over n}
 =N\sum_{N/4<n\le N}{\lambda_4(n)\over n}
 \ge0.
}
\tag{R-94055.7}
\]

This is a genuine unconditional positive Q4 observable.

Its Mellin transform, however, is

\[
{1\over s-1}
\sum_{n\ge1}{c_\circ(n)\over n^s}.
\tag{R-94055.8}
\]

At \(s=1\),

\[
\sum_{n\ge1}{c_\circ(n)\over n^s}
 \longrightarrow2\log4,
\tag{R-94055.9}
\]

so (R-94055.8) has an unavoidable positive real pole with residue \(2\log4\).
The positive annulus has linear main term \(2(\log4)N\). Landau's theorem sees
this real singularity before every open-strip zeta pole.

Subtracting the exact main term produces

\[
N\left[
\sum_{N/4<n\le N}{\lambda_4(n)\over n}-2\log4
\right],
\tag{R-94055.10}
\]

which takes both signs in the retained deterministic finite evaluation through `N=20000` and has no source-level positivity. The sign scan is diagnostic only; the exact real-pole and antisymmetry obstructions do not depend on it.
Thus the positive annulus does not prove RH.

## 3. Why the mean-zero cubic cannot inherit positivity

For any symmetric mean-zero endpoint weight, its antiderivative kernel satisfies

\[
K(1-x)=-K(x).
\tag{R-94055.11}
\]

The induced positive-source Q4 kernel is

\[
F_K(x)=K(x)-4\mathbf1_{x\le1/4}K(4x).
\tag{R-94055.12}
\]

On \(1/4<x<1\), one has simply \(F_K(x)=K(x)\). In particular, on
\(1/4<x<3/4\), both \(x\) and \(1-x\) lie in this range and

\[
F_K(1-x)=-F_K(x).
\tag{R-94055.13}
\]

Unless the observable is identically zero on that interval, \(F_K\) takes both
signs. Therefore the positive generalized-prime source cannot give the centered
cubic scalar a pointwise sign.

## 4. Exact boundary

Closed:

1. nonnegative generalized-prime coefficients;
2. exact scale-four source factorization;
3. exact positive reciprocal-kernel annulus;
4. unavoidable real-pole obstruction;
5. antisymmetry obstruction for every symmetric mean-zero cubic-type kernel.

Still live:

1. signed prime cancellation;
2. bilinear/additive covariance estimates;
3. the phase-locked heat hierarchy of this packet;
4. RH.
