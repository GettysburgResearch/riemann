# T-17801 — Difference-notched pole-free prime windows remain equivalent to RH

Claim ID: `T-17801`  
Title: Every finite cascade of normalized critical-line differences preserves the one-window RH criterion and its finite phase-band disproof interface  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-09-h`  
Created: 2026-07-31  
Dependencies: `T-15404`, `T-15604`, `L-17802`  
Scope: high-sensitivity finite prime-window searches  
Related counterexample candidates: none

## Statement

Let `G` be a real compactly supported pole-free window with Laplace transform
`g`, satisfying

\[
 g(1/2)=0,
 \qquad
 g(z)\ne0\quad(0<\operatorname{Re}z<1/2).
 \tag{1}
\]

For any finite positive list `r=(r_1,...,r_m)`, define

\[
 G_{\mathbf r}=\Delta_{\mathbf r}G.
\]

Then its transform is

\[
 g_{\mathbf r}(z)
 =g(z)\prod_{j=1}^m\frac{1-e^{-r_jz}}2.
 \tag{2}
\]

Every added zero lies on the imaginary axis. Hence

\[
 g_{\mathbf r}(1/2)=0,
 \qquad
 g_{\mathbf r}(z)\ne0
 \quad(0<\operatorname{Re}z<1/2).
 \tag{3}
\]

Subject to the explicit-formula/Laplace interface of `T-15404`, the following
are equivalent:

1. RH;
2. the raw finite prime-power statistic
   \[
   Q_{G_{\mathbf r}}(x)
   =\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
    G_{\mathbf r}(x-\log n)
   \]
   is bounded on a right half-line;
3. its right translates have uniformly bounded Cesaro mean square.

Moreover, the finite strict-band theorem `T-15604` applies with no larger shell
or derivative tail constants than for `G`.

## Proof

Equation (2) is `L-17802`. Each factor `1-e^{-r_jz}` can vanish only when
`Re z=0`; it is nonzero in the open right half-plane. Therefore the pole at
`s=1` remains canceled and no shifted off-critical zero pole is canceled.

Under RH the smoothed zero expansion remains absolutely and uniformly
convergent because finite differences preserve compact support and do not worsen
the transform envelope on the imaginary axis. Conversely, boundedness or
bounded mean square gives a holomorphic right-half-plane Laplace transform. An
off-critical zero would give an uncanceled pole, contradiction. The finite band
follows from `L-17802.7`--`L-17802.8` and `T-15604`. QED.

## False-RH exposure

If

\[
 \rho=1/2+\delta+i\gamma,
 \qquad\delta>0,
\]

then its translated mode has coefficient

\[
 g(\delta+i\gamma)
 \prod_j\frac{1-e^{-r_j(\delta+i\gamma)}}2\ne0.
\]

Hence it grows like `e^(delta x)` and eventually violates every fixed selected-
phase band. When one notch is resonant with `gamma`, `L-17802` shows that its
coefficient loses only one power of `delta`, rather than the two powers and the
additional high-frequency denominator imposed by a box-square notch.

## Exact finite implementations

Two especially simple bases are available.

1. Apply the cascade to the smooth universal window already enclosed in PR #184.
   The prime producer is the exact `2^m` translation identity.
2. Apply the cascade to the finite triangular window `L-15409`. The result is an
   exact piecewise-linear signed window, requiring no FFT, infinite convolution,
   or spline-tail argument.

A final certificate still requires a complete prime-power manifest, directed
window values, directed selected-zero phases, and the closed residual budget.
No RH resolution is claimed here.
