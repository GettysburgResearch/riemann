# R-95400 — Source-blind positive-kernel, square-function, Mellin and log-Sobolev shortcuts do not prove FOCC

Claim ID: `R-95400`  
Status: **PROPOSED COMPLETE EXACT SCOPE FIREWALL — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-18  
Depends on: `L-95400`–`L-95402`; PR #573 top-band firewall  
Scope: rejects generic inferences; does not refute arithmetic FOCC

## 1. Top-band sign mutation survives annularization

On

\[
\frac23\le x\le\frac34,
\]

all terms `K_nu(2^h x)` with `h>=1` vanish. Hence

\[
J_0(x)=K_0(x)=W(x),
\qquad
J_1(x)=0.
\tag{R-95400.1}
\]

Moreover

\[
W(x)=\frac{x(1-x)(2x-1)}3\ge\frac2{81}.
\tag{R-95400.2}
\]

Replace the actual Möbius signs temporarily by `+1` on odd squarefree cores in

\[
2X/3\le m\le3X/4.
\]

Every activation interval, same-core diagonal, passive fibre identity, kernel coefficient and local Sobolev norm remains unchanged. But the annular critical output is

\[
\gg
\sum_{2X/3\le m\le3X/4\atop m\ \mathrm{odd\ squarefree}}
\frac{\log m}{\sqrt m}
\gg\sqrt X\log X.
\tag{R-95400.3}
\]

The diagonal is only `O(log^2 X)`. Therefore none of the following data can imply FOCC without using the actual global Möbius signs:

```text
finite band support;
pointwise kernel bounds;
passive fibre energy;
same-core diagonal;
local activation geometry;
gcd counts;
modulus-one source labels.
```

## 2. Diagonal positive-kernel completion costs the number of active cores

Let `g=(G_X(m))` over the nonzero active cores. The source-blind matrix behind the desired inequality is

\[
\lambda\operatorname{diag}(g_m^2)-gg^T.
\]

On the support of `g`, congruence by `diag(|g_m|)^{-1}` gives

\[
\lambda I-\sigma\sigma^T,
\qquad
\sigma_m=\operatorname{sgn}(g_m).
\]

If `N_X` entries are active, the eigenvalues are

\[
\lambda\quad(N_X-1\text{ times}),
\qquad
\lambda-N_X\quad(1\text{ time}).
\]

Thus

\[
\boxed{
\lambda\operatorname{diag}(g_m^2)-gg^T\succeq0
\Longleftrightarrow
\lambda\ge N_X.
}
\tag{R-95400.4}
\]

Since `N_X` is of order `X`, a source-blind diagonal Schur completion pays the macroscopic factor that FOCC is designed to avoid.

## 3. Fixed-window Mellin almost-orthogonality loses `X`

The exact mean-square estimate (L-95402.10) contains the term

\[
CX\sum|c_m|^2.
\]

The logarithmic frequencies `log m` on a length-`X` annulus have minimum spacing of order `1/X`. Compact support of the log kernel makes its Fourier transform entire, not frequency compact. A fixed or polylogarithmic Mellin window therefore cannot turn the diagonal into a pointwise bound.

## 4. Prime-cube log-Sobolev normalization barrier

For a finite set of odd primes `P`, extend the annular function by zero to the Boolean prime cube:

\[
f(S)=G_X\left(\prod_{p\in S}p\right).
\]

The Möbius sum is the unnormalized top Walsh coefficient

\[
\sum_{S\subseteq P}(-1)^{|S|}f(S)
=2^{|P|}\widehat f(P).
\]

Parseval, Bonami hypercontractivity and the cube log-Sobolev inequality control the normalized coefficient `widehat f(P)`, but returning to the arithmetic sum introduces the factor `2^{|P|}`. The support probability is itself exponentially small, and the resulting source-blind bound is no stronger than the absolute annular mass. A closing inequality must use arithmetic organization beyond the uniform prime cube.

## 5. Near-diagonal and large-gcd closure does not propagate

`L-95401` closes pairs with

\[
|m-n|\le\log^B X
\]

or

\[
(m,n)\ge X/\log^B X.
\]

There is no monotone or positivity argument extending these estimates to separated coprime pairs. The sign-free common-divisor average in (L-95402.12) leaves the full character `mu(a)mu(b)` on the ratio variables.

## 6. What remains logically possible

This firewall does not refute:

```text
a source-specific coprime dispersion theorem;
a coefficient-one reflected/Jordan reserve;
a nonlocal arithmetic Carleson embedding;
an exact Type-II Bellman recurrence;
a direct proof of the annular Möbius sum.
```

It forbids presenting local passivity, diagonal energy, generic positive kernels, fixed-window large sieve, or Boolean hypercontractivity as such a theorem.
