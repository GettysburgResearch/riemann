# L-19848 — Growing Meixner--Pollaczek analysis bound

Claim ID: `L-19848`  
Status: **PROPOSED SELF-CONTAINED SPECIAL-FUNCTION LEMMA**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-07  
Scope: supplies the growing analysis estimate used in `L-19847` without a numerical Christoffel constant

## 1. Statement

Let

\[
 \Phi_n(t)
 =c_n\Gamma\!\left(\frac14+\frac{it}{2}\right)
 P_n^{(1/4)}\!\left(\frac t2;\frac\pi2\right)
 \tag{L-19848.1}
\]

be the normalized Mellin transform of the even Hermite function `h_(2n)`.
Then, for every fixed `C_0`, there is `C` such that

\[
 \boxed{
 \sup_{|t|\le C_0L}
 \sum_{0\le n\le C_0L^2}|\Phi_n(t)|^2
 \le L^C.}
 \tag{L-19848.2}
\]

Consequently the naturally normalized sample-analysis map on the grid

\[
 t_k=2\pi k/\ell,
 \qquad
 |k|\le C_0L^2,
 \qquad
 \ell\asymp L,
 \tag{L-19848.3}
\]

has operator norm polynomial in `L`.

## 2. Generating function

For `lambda=1/4` and `phi=pi/2`, the Meixner--Pollaczek generating function is

\[
 \sum_{n=0}^\infty
 P_n^{(\lambda)}(x;\pi/2)z^n
 =(1-iz)^{-\lambda+ix}
  (1+iz)^{-\lambda-ix}.
 \tag{L-19848.4}
\]

Take `z=r` real with

\[
 r=1-\frac1{n+1}.
 \tag{L-19848.5}
\]

Cauchy's coefficient estimate gives

\[
 |P_n^{(\lambda)}(x;\pi/2)|
 \le r^{-n}(1+r^2)^{-\lambda}
 \exp\{2|x|\arctan r\}.
 \tag{L-19848.6}
\]

Here

\[
 r^{-n}\le e,
 \qquad
 2\arctan r\le\frac\pi2.
 \tag{L-19848.7}
\]

Therefore

\[
 |P_n^{(1/4)}(x;\pi/2)|
 \le C\exp\{\pi|x|/2\}.
 \tag{L-19848.8}
\]

The omitted normalization in (L-19848.1) is only polynomial in `n`: from the
exact orthogonality constant,

\[
 |c_n|\le C(n+1)^C.
 \tag{L-19848.9}
\]

## 3. Gamma cancellation

Stirling's bound in a fixed vertical strip gives

\[
 \left|\Gamma\!\left(\frac14+ix\right)\right|
 \le C(1+|x|)^C e^{-\pi|x|/2}.
 \tag{L-19848.10}
\]

Multiplying (L-19848.8) and (L-19848.10), the exponential factors cancel
exactly:

\[
 |\Phi_n(2x)|
 \le C(n+1)^C(1+|x|)^C.
 \tag{L-19848.11}
\]

For `n<=C_0L^2` and `|x|<=C_0L`, the right side is `L^C`. Summing
`O(L^2)` squares proves (L-19848.2).

The estimate is intentionally crude; only polynomial growth is required.

## 4. Sample analysis

For coefficients `a_n`, Cauchy--Schwarz and (L-19848.2) give

\[
 \left|
 \sum_{n\le C_0L^2}a_n\Phi_n(t_k)
 \right|^2
 \le L^C\sum|a_n|^2.
 \tag{L-19848.12}
\]

There are `O(L^2)` grid points. With the ordinary Fourier/Riemann-sum
normalization `1/ell` (or any equivalent finite CCM normalization), another
polynomial factor proves the asserted analysis bound.

## 5. Transfer to the prolate packet

The uniform low-mode prolate-to-Hermite expansion has coefficient norm
`L^C` and error `O(L^C/R)` after the mode-dependent phase/eigenvalue correction
is retained. Applying the same generating-function estimate to the finitely many
Hermite correction bands transfers (L-19848.2) to the exact low prolate packet:

\[
 \sup_{|t|\le C_0L}
 \sum_{n\le C_0L^2}|\mathcal Mp_{n,R}(t)|^2
 \le L^C.
 \tag{L-19848.13}
\]

Multiplication by zeta costs only another polynomial factor on `|t|<=C_0L` by
convexity. This proves the upper source-map estimate in `L-19847`.

## 6. Proof boundary

The generating-function and gamma cancellation are exact. The final transfer
(L-19848.13) uses the uniform low-mode prolate-to-Hermite coefficient expansion;
it does not require a determinant lower bound or a complete source inverse.
No RH statement is involved.
