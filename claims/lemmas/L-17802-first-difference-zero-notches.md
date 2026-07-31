# L-17802 — Normalized first-difference zero notches preserve the proof moat and maximize open-strip sensitivity

Claim ID: `L-17802`  
Title: A two-tap first-difference filter is the unique maximal line-zero notch under the derivative-L1 contraction needed by the phase-aware prime bound  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-09-h`  
Created: 2026-07-31  
Dependencies: `L-15613`, `L-15406`, `L-15409`; elementary translation, Laplace-transform, and finite-difference algebra  
Scope: proof-grade critical-line background suppression for pole-free prime windows  
Related counterexample candidates: none

## 1. Normalized difference operator

For `r>0`, define

\[
 (\Delta_r G)(u)=\frac{G(u)-G(u-r)}2.
 \tag{1}
\]

For a finite list `r=(r_1,...,r_m)`, put

\[
 \Delta_{\mathbf r}=\Delta_{r_1}\cdots\Delta_{r_m}.
 \tag{2}
\]

Translations commute, so the order is irrelevant. If

\[
 g(z)=\int_{\mathbb R}e^{-zu}G(u)\,du,
\]

then

\[
 \boxed{
 g_{\mathbf r}(z)
 =g(z)\prod_{j=1}^m d_{r_j}(z),
 \qquad
 d_r(z)=\frac{1-e^{-rz}}2.}
 \tag{3}
\]

If `supp G subset [A,B]`, then

\[
 \operatorname{supp}(\Delta_{\mathbf r}G)
 \subset[A,B+r_1+\cdots+r_m].
 \tag{4}
\]

## 2. Exact prime-statistic finite difference

For

\[
 Q_G(x)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}G(x-\log n),
\]

one has exactly

\[
 \boxed{
 Q_{\Delta_{\mathbf r}G}(x)
 =2^{-m}\sum_{S\subseteq\{1,\ldots,m\}}
 (-1)^{|S|}
 Q_G\!\left(x-\sum_{j\in S}r_j\right).}
 \tag{5}
\]

Thus a difference-notched cell may be produced either directly from one signed
prime-power window or from `2^m` independently evaluated translations of the
base statistic.

The coefficient absolute sum is exactly one:

\[
 2^{-m}\sum_S1=1.
 \tag{6}
\]

Consequently the filter is stable in every supremum norm, and it annihilates
every polynomial in `x` of degree less than `m`.

## 3. Every phase-band envelope is preserved

Translations commute with differentiation. For every integer `p>=0`,

\[
 \boxed{
 \|(\Delta_{\mathbf r}G)^{(p)}\|_1
 \le\|G^{(p)}\|_1.}
 \tag{7}
\]

Indeed, each normalized difference has l1-coefficient norm one. Moreover, on
the critical line,

\[
 |d_r(it)|=|\sin(rt/2)|\le1.
 \tag{8}
\]

Therefore:

1. every finite-shell transform envelope in `L-15613` is no larger;
2. every integration-by-parts high-zero constant `A_p` is no larger;
3. every selected critical-zero phase can still be retained exactly;
4. the only scalar tail change is the explicit trivial-zero/support term caused
   by the larger right endpoint in (4).

This is the key proof-facing advantage over an unnormalized finite difference.

## 4. Certified line-zero attenuation

Suppose the design phase satisfies

\[
 |r\gamma-2\pi k|\le\eta.
\]

Then

\[
 \boxed{|d_r(i\gamma)|\le\eta/2.}
 \tag{9}
\]

For a zero ball

\[
 |\gamma-\widetilde\gamma|\le\varepsilon,
 \qquad r=2\pi/\widetilde\gamma,
\]

this gives

\[
 \boxed{
 |d_r(i\gamma)|
 \le\frac{\pi\varepsilon}{\widetilde\gamma}.}
 \tag{10}
\]

The attenuation is linear rather than quadratic in the zero-ball radius. That
is sufficient once selected phases are evaluated directly, as in `L-15613`.

## 5. Off-line displacement survives linearly

At exact resonance `r gamma=2 pi k`, put

\[
 z=\delta+i\gamma,
 \qquad\delta>0.
\]

Then

\[
 \boxed{
 |d_r(z)|=\frac{1-e^{-r\delta}}2.}
 \tag{11}
\]

In particular,

\[
 |d_r(\delta+i\gamma)|\sim\frac{r\delta}{2}
 \qquad(\delta\downarrow0),
 \tag{12}
\]

and for `0<=r delta<=1`,

\[
 \boxed{|d_r(\delta+i\gamma)|\ge r\delta/4.}
 \tag{13}
\]

Thus a notch removes the critical-line mode but retains a first-order response
to a horizontal displacement.

## 6. Optimality among two-tap proof-safe notches

Consider a two-tap filter

\[
 T=aI+b\tau_r,
 \qquad(\tau_rG)(u)=G(u-r),
\]

and suppose:

1. it vanishes at the resonant line phase, so `a+b=0`;
2. it preserves every derivative-L1 envelope, so `|a|+|b|<=1`.

Then `b=-a` and `|a|<=1/2`. At the displaced phase its response is

\[
 |a|\,|1-e^{-r\delta}|,
\]

which is maximized exactly when `|a|=1/2`. Up to an irrelevant global sign,

\[
 \boxed{T=\Delta_r}
 \tag{14}
\]

is the unique maximal two-tap notch compatible with the proof moat.

## 7. Strict comparison with the old box-square notch

The box-square factor used in `L-15406` is

\[
 b_r(z)^2
 =\left(\frac{1-e^{-rz}}{rz}\right)^2.
 \tag{15}
\]

For every `Re z>=0`,

\[
 \boxed{
 |d_r(z)|
 \ge\frac{|rz|^2}{4}|b_r(z)^2|.}
 \tag{16}
\]

The proof is immediate from `|1-e^{-rz}|<=2`. For a cascade,

\[
 \boxed{
 \prod_{j\in S}|d_{r_j}(z)|
 \ge
 \left(\prod_{j\in S}\frac{|r_jz|^2}{4}\right)
 \prod_{j\in S}|b_{r_j}(z)^2|.}
 \tag{17}
\]

The old convolution-square notch adds support `2r`; the normalized difference
adds only `r`. It therefore has half the support cost and avoids the artificial
`|z|^{-2}` high-frequency loss per replaced notch.

## 8. Verified-frontier gain for the first five notches

Let

\[
 T_0=3{,}000{,}175{,}332{,}800
\]

and design the first five notch lengths by `r_j=2 pi/gamma_j`. Using only

\[
 \pi>3,
 \qquad
 (\gamma_1,\ldots,\gamma_5)<(15,22,26,31,33),
\]

(17) gives, for every `Re z>=0` and `|z|>=T_0`,

\[
 \boxed{
 \prod_{j=1}^5\frac{|r_jz|^2}{4}
 >4.528486361179145\times10^{115}>10^{115}.}
 \tag{18}
\]

Replacing only the third box-square notch gives the rigorous factor

\[
 >1.198364914909383\times10^{23},
 \tag{19}
\]

and replacing only the fourth gives

\[
 >8.429705332765277\times10^{22}.
 \tag{20}
\]

These are lower bounds on retained open-strip sensitivity, not evidence that an
off-line zero exists.

## 9. Proof boundary

- The filter algebra and inequalities are elementary and exact.
- A production line-zero attenuation must use directed zero balls and directed
  `pi`/phase arithmetic.
- The verified-height value in Section 8 is an imported published computation;
  its use in a final certificate requires the exact cited frontier and
  normalization.
- Better response to a hypothetical off-line zero is not a counterexample.
- A finite prime-window violation still requires all gates in `T-15604`.
