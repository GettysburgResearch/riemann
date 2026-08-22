# L-105211 — The remaining low-order endpoint is one explicit Levinson zeta auxiliary

Claim ID: `L-105211`  
Status: **PROVED EXACT FACTORIZATION AND SAFE-LINE CARRIER AUDIT**  
Created: 2026-08-23  
Audited: 2026-08-23  
Depends on: `L-105206`, `L-105209`  
RH status: **not assumed**

## 1. Completed zeta factor

Write

\[
\xi(s)=H(s)\zeta(s),
\qquad
H(s)={1\over2}s(s-1)\pi^{-s/2}\Gamma(s/2),
\tag{L-105211.1}
\]

and put

\[
h(s)={H'(s)\over H(s)}
={1\over s}+{1\over s-1}
-{1\over2}\log\pi
+{1\over2}\psi(s/2).
\tag{L-105211.2}
\]

For a positive parameter `lambda`, the low endpoint companion is

\[
G_{0,\lambda}(s)
=\xi(s)+\lambda\xi'(s).
\]

A single differentiation gives the exact factorization

\[
\boxed{
G_{0,\lambda}(s)
=H(s)(1+\lambda h(s))
V_\lambda(s),
}
\tag{L-105211.3}
\]

where

\[
\boxed{
V_\lambda(s)
=\zeta(s)+\alpha_\lambda(s)\zeta'(s),
\qquad
\alpha_\lambda(s)
={\lambda\over1+\lambda h(s)}.
}
\tag{L-105211.4}
\]

This is the exact first-order Levinson differential polynomial selected by the
native high-derivative companion parameter.

## 2. The carrier is zero-free on the safe horizontal path

Fix a large regular ordinate `T` and let

\[
s=\sigma+iT,
\qquad \sigma\ge{1\over2}.
\]

Stirling's formula for the digamma function, uniformly in this half-ray, gives

\[
\Re h(\sigma+iT)
={1\over2}\log{|\sigma+iT|\over2\pi}
+O(1/T)
+O\!\left({1\over1+\sigma}\right).
\tag{L-105211.5}
\]

Consequently, for sufficiently large `T`,

\[
\boxed{
\Re h(\sigma+iT)\ge {1\over3}\log T-C
\qquad(\sigma\ge1/2).
}
\tag{L-105211.6}
\]

In particular, for every `lambda>0`, and especially for the native
`lambda=lambda_r`,

\[
\boxed{
1+\lambda h(\sigma+iT)\ne0
\qquad(\sigma\ge1/2)
}
\tag{L-105211.7}
\]

once `T` is sufficiently large.  The factors `H` and `1+lambda h` therefore
supply explicit continued arguments but no unknown safe-line zero.

## 3. Native coefficient size

For the natural terminal order

\[
r=T^2\log T\,L(T),
\qquad L(T)\to\infty,
\]

the positive Xi Fourier saddle gives

\[
\lambda_r={M_r\over M_{r+1}}
={1\over w_r}(1+o(1))
\asymp {1\over\log T}.
\tag{L-105211.8}
\]

On every fixed-width strip `1/2<=sigma<=A`, the correct complex Stirling
expansion is

\[
\boxed{
h(\sigma+iT)
={1\over2}\log{T\over2\pi}
+{i\pi\over4}
+O_A(1/T).
}
\tag{L-105211.9}
\]

The constant imaginary carrier was omitted in an earlier draft.  Since
`lambda_r=O(1/log T)`, it contributes only at the next order after inversion.
More precisely,

\[
\boxed{
\alpha_{\lambda_r}(\sigma+iT)
={c_T\over\log T}
+O_A\!\left({1\over\log^2T}\right),
}
\tag{L-105211.10}
\]

where `c_T` is real, positive, and stays in a fixed compact subinterval of
`(0,infinity)`; the imaginary part of `alpha_(lambda_r)` is
`O_A(1/log^2 T)`.  Thus the native coefficient has exactly the classical
Levinson scale.

No parameter is chosen after locating a hypothetical zero; `lambda_r` is the
moment-ratio parameter which cancels the reflected high-frequency carrier in
`L-105209`.

## 4. Exact argument decomposition

Let the argument on the safe horizontal path be continued from the far-right
Stirling/Euler region.  Equations (L-105211.3)--(L-105211.7) give

\[
\boxed{
\Delta_{\infty\to1/2}\arg G_{0,\lambda}
=
\Delta\arg H
+
\Delta\arg(1+\lambda h)
+
\Delta\arg V_\lambda.
}
\tag{L-105211.11}

The first two variations are explicit analytic carriers.  Combined with the
terminal quotient estimate of `L-105209` and the telescope of `L-105206`, the
only zero-bearing low-order term is

\[
\boxed{
V_{\lambda_r}(s)
=\zeta(s)
+{\lambda_r\over1+\lambda_rh(s)}\zeta'(s).
}
\tag{L-105211.12}

This is a one-function formulation of the actual Levinson difficulty.

## 5. Euler half-plane pinning

For every fixed `delta>0`, the absolutely convergent Dirichlet series gives,
uniformly on `sigma>=1+delta`,

\[
\zeta(s)=1+O_\delta(2^{-\sigma}),
\qquad
\zeta'(s)=O_\delta(2^{-\sigma}\log2).
\]

Since `alpha_lambda` is bounded on the safe ray,

\[
\boxed{
V_\lambda(s)=1+o(1)
\qquad(\sigma\to\infty),
}
\tag{L-105211.13}

which fixes the argument branch.  More quantitatively, for each fixed
`delta>0` and sufficiently large right cutoff `A_delta`, the tail
`sigma>=A_delta` has no zero and contributes arbitrarily small argument.

The unresolved interval is therefore a finite horizontal segment from the
Euler half-plane to the critical line.

## 6. Scope

The factorization does not bound

\[
\Delta\arg V_{\lambda_r}(\sigma+iT)
\qquad(1/2\le\sigma\le A).
\]

That finite-segment argument is precisely the classical Levinson difficulty.
The unconditional Fourier Gram and mean-orientation theorems `L-105207` and
`L-105208` provide new source-side constraints on this auxiliary, but a
fixed-height localization theorem is still required.
