# L-97905 — A constant-killing scale filter has a positive subpower rough cube

Claim ID: `L-97905`  
Status: **PROVED UNCONDITIONAL ASYMPTOTIC THEOREM**  
Created: 2026-08-18  
Depends on: the sharp `P_61` annular asymptotic; classical PNT and Mertens theorems  
RH status: **not assumed**

Let `b(Y)=F_61(Y)` and define the additional factor-four difference

\[
 b^{\Delta}(Y)=b(Y)-b(Y/4).
 \tag{L-97905.1}
\]

The constant term cancels exactly. From

\[
 b(Y)=a_*\sqrt Y+c_*+O(Y^{-3/2})
\]

one obtains

\[
 \boxed{
 b^{\Delta}(Y)=\frac{a_*}{2}\sqrt Y+O(Y^{-3/2}).
 }
 \tag{L-97905.2}
\]

There is also a global bound `|b^Delta(Y)|<=C sqrt(Y)`.

Put

\[
 \ell=\log\log X,
 \qquad
 K_X=\ell^2,
 \qquad
 Z_X=X^{1/K_X},
 \qquad
 L_X=\exp(K_X).
 \tag{L-97905.3}
\]

Define

\[
 \mathcal B_Z^{\Delta}(X)=
 \sum_{d\mid\prod_{67\le p\le Z_X}p}
 \frac{\mu(d)}{\sqrt d}b^{\Delta}(X/d),
 \qquad
 U_Z^{\Delta}(X)=\frac{\mathcal B_Z^{\Delta}(X)}{\sqrt X}.
 \tag{L-97905.4}
\]

Then

\[
 \boxed{
 U_Z^{\Delta}(X)
 =\frac{a_*}{2}
 \prod_{67\le p\le Z_X}\left(1-\frac1p\right)
 +o\!\left(\frac1{\log Z_X}\right)>0.
 }
 \tag{L-97905.5}
\]

In particular

\[
 U_Z^{\Delta}(X)\asymp\frac1{\log Z_X}
 =\frac{K_X}{\log X}.
 \tag{L-97905.6}
\]

## Proof

Let `D_X=X/L_X`. For `d<=D_X`, substitute (L-97905.2). The normalized
remainder is

\[
 O\!\left(X^{-2}\sum_{d\le D_X}d\right)=O(L_X^{-2}).
 \tag{L-97905.7}
\]

There is no constant-term divisor sum.

It remains to control divisors `d>D_X`. Put

\[
 \eta_X=\frac{\log K_X}{\log Z_X};
 \qquad Z_X^{\eta_X}=K_X.
 \tag{L-97905.8}
\]

For large `X`, `0<eta_X<1/2`. Rankin's inequality gives

\[
 \sum_{d\mid P_Z\atop d>D_X}\frac1d
 \le D_X^{-\eta_X}
 \prod_{67\le p\le Z_X}(1+p^{\eta_X-1}).
 \tag{L-97905.9}
\]

Uniform partial summation over primes yields

\[
 \sum_{p\le Z_X}p^{\eta_X-1}
 \ll\frac{Z_X^{\eta_X}}{\eta_X\log Z_X}
 =\frac{K_X}{\log K_X}.
 \tag{L-97905.10}
\]

On the other hand,

\[
 \eta_X\log D_X
 =K_X\log K_X+o(K_X\log K_X).
 \tag{L-97905.11}
\]

Thus (L-97905.9) is

\[
 \exp\{-K_X\log K_X+O(K_X/\log K_X)\}.
 \tag{L-97905.12}
\]

The global square-root bound for `b^Delta` makes the actual activated tail no
larger. Both (L-97905.7) and (L-97905.12) are
`o(K_X/log X)`, while Mertens' theorem gives the main product in
(L-97905.5). This proves the theorem.

## Why the filter is analytically safe

If `mathcal A_X` is the native annular scalar, then its filtered version is

\[
 \mathcal A_X^{\Delta}=\mathcal A_X-\mathcal A_{X/4}.
 \tag{L-97905.13}
\]

Its Mellin transform is the already reconstructed annular transform multiplied
by one additional factor

\[
 1-4^{-s}.
 \tag{L-97905.14}
\]

This factor has no zero in `Re(s)>0`. Therefore eventual nonnegativity of the
filtered native scalar is itself sufficient for RH through the same Landau
argument. The filtering does not weaken the zero-detection consumer.