# L-98016 — The target root is constant two minus a bounded Euler-summation discrepancy

Claim ID: `L-98016`  
Status: **PROVED EXACT SOURCE IDENTITY**  
Created: 2026-08-18  
Depends on: `T-98012`; elementary Dirichlet convolution  
RH status: **not assumed**

Put

\[
S(Y)=\sum_{m\le Y}{1\over\sqrt m},
\qquad
T(Y)=(4\sqrt Y-3)\mathbf 1_{Y\ge1},
\]

and define the Euler-summation discrepancy

\[
\boxed{
E(Y)=2S(Y)-T(Y).
}
\tag{L-98016.1}
\]

For every real `X>=1`, finite divisor switching gives

\[
\begin{aligned}
\sum_{n\le X}{\mu(n)\over\sqrt n}S(X/n)
&=\sum_{nm\le X}{\mu(n)\over\sqrt{nm}}\\
&=\sum_{r\le X}{1\over\sqrt r}\sum_{n\mid r}\mu(n)\\
&=1.
\end{aligned}
\tag{L-98016.2}
\]

Therefore the complete target root satisfies the exact identity

\[
\boxed{
\mathcal T_X
=2-
\sum_{n\le X}{\mu(n)\over\sqrt n}E(X/n).
}
\tag{L-98016.3}
\]

Equivalently, Target Root Positivity is the sharp discrepancy barrier

\[
\boxed{
\sum_{n\le X}{\mu(n)\over\sqrt n}E(X/n)\le2
}
\tag{L-98016.4}
\]

for every sufficiently large real endpoint.

## 1. Exact local geometry of `E`

On an open cell `N<Y<N+1`,

\[
E(Y)=2\sum_{m\le N}{1\over\sqrt m}-4\sqrt Y+3,
\tag{L-98016.5}
\]

so `E` is strictly decreasing there, with derivative

\[
E'(Y)=-{2\over\sqrt Y}.
\]

At an integer `N>=2`, it jumps upward by exactly

\[
E(N)-E(N^-)= {2\over\sqrt N}.
\tag{L-98016.6}
\]

Thus `E` is a bounded centered lattice-versus-continuum sawtooth. Its jumps and continuous drift have the same square-root scale. The growing main term of `T` has disappeared before any Möbius estimate.

## 2. Mellin transform

For `Re s>1/2`,

\[
\int_1^\infty S(Y)Y^{-s-1}\,dY
={\zeta(s+1/2)\over s}.
\]

Consequently

\[
\boxed{
\widehat E(s)
={2\zeta(s+1/2)+3\over s}-{4\over s-1/2}.
}
\tag{L-98016.7}
\]

Writing `z=s+1/2`, this is

\[
\boxed{
\widehat E(s)
={2(z-1)\zeta(z)-z-1\over(z-1/2)(z-1)}.
}
\tag{L-98016.8}
\]

The apparent singularity at `z=1` is removable: the residue of zeta cancels the continuum main term exactly. This is the analytic expression of the boundedness of `E`.

Multiplication by `1/zeta(z)` and subtraction from `2/s` recovers the target transform of `T-98012` exactly.

## 3. Source-faithful interpretation

Equation (L-98016.3) is not an absolute-value estimate and not a substitution of an all-integer source for a rough store. It is an exact convolution identity on the fully completed squarefree owner ledger. Every source index keeps its native activation `X/n`, coefficient `mu(n)/sqrt(n)`, and first ownership.

The new barrier has a fixed constant budget `2` and a bounded local kernel. This does not prove (L-98016.4): the Möbius projection of a bounded sawtooth still carries the reciprocal-zeta pole. It does, however, remove the spurious square-root growth from the local Bellman state and provides a more rigid object for Type-I/Type-II or renewal analysis.
