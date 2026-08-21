# L-21702 — Uniform parabolic Hausdorff saddle positivity

Claim ID: `L-21702`  
Title: The fixed-row Hausdorff positivity sector extends uniformly to a complete cone `k >= C_R m^2`  
Status: `PROPOSED — UNIFORM SADDLE PROOF CANDIDATE; CENTRAL ESTIMATE COMPLETE, TAIL UNIFORMITY PENDING INDEPENDENT REVIEW`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-07  
Dependencies: the central zero/Hausdorff normalization of PR #158; `L-21701`; the unconditional Riemann–von Mangoldt formula with `O(log T)` remainder; elementary beta concentration and complex Taylor bounds  
Scope: an unconditional infinite two-parameter positivity sector in the full Hausdorff hierarchy  
Related counterexample candidates: none

## 1. Hausdorff rows

Write every positive-ordinate nontrivial zero as

\[
 \rho=\frac12+a+i\gamma,
 \qquad
 \gamma>0,
 \qquad
 |a|\le\frac12,
 \tag{L-21702.1}
\]

with multiplicity `m_rho`. Put

\[
 x_\rho
 =-\frac1{(\rho-1/2)^2}
 =\frac1{(\gamma-ia)^2}.
 \tag{L-21702.2}
\]

Fix

\[
 R>\gamma_1^{-2},
 \tag{L-21702.3}
\]

where `gamma_1` is the least positive zero ordinate. For integers `m>=1` and `k>=0`, define

\[
 \boxed{
 \mathcal H_{m,k}(R)
 =\sum_{\Im\rho>0}m_\rho
  x_\rho^m(R-x_\rho)^k.}
 \tag{L-21702.4}
\]

The symmetry `a -> -a` makes this sum real. Complete nonnegativity of all these rows is the inherited central Hausdorff criterion for RH. The purpose of the present lemma is not to assume that criterion, but to prove one genuinely unbounded sector of it without RH.

Define the positive real-line surrogate

\[
 \boxed{
 M_{m,k}(R)
 =\sum_{\Im\rho>0}m_\rho
  \gamma^{-2m}(R-\gamma^{-2})^k.}
 \tag{L-21702.5}
\]

Condition (L-21702.3) makes every summand nonnegative.

## 2. Statement

Let `m=m_j>=1` and `k=k_j` be any sequence such that

\[
 k\longrightarrow\infty,
 \qquad
 \frac{m}{\sqrt k}\longrightarrow0.
 \tag{L-21702.6}
\]

Then

\[
 \boxed{
 \mathcal H_{m,k}(R)
 =I_{m,k}(R)(1+o_R(1))}
 \tag{L-21702.7}
\]

uniformly over all such sequences, where

\[
 \boxed{
\begin{aligned}
 I_{m,k}(R)
 ={}&\frac{R^{k+m-1/2}}{8\pi}
 B\!\left(m-\frac12,k+1\right)\\
 &\times
 \left[
  \psi\!\left(k+m+\frac12\right)
  -\psi\!\left(m-\frac12\right)
  -\log(4\pi^2R)
 \right].
\end{aligned}}
 \tag{L-21702.8}
\]

In particular, `I_(m,k)(R)>0` throughout the sector for all sufficiently large indices, and therefore

\[
 \boxed{
 \mathcal H_{m,k}(R)>0
 \quad\text{whenever}\quad
 m/\sqrt k\to0.}
 \tag{L-21702.9}
\]

The uniformity gives a fixed-cone consequence.

### Parabolic cone

There exist constants

\[
 C_R<\infty,
 \qquad
 K_R<\infty
 \tag{L-21702.10}
\]

such that

\[
 \boxed{
 k\ge C_Rm^2,
 \qquad
 k+m\ge K_R
 \quad\Longrightarrow\quad
 \mathcal H_{m,k}(R)>0.}
 \tag{L-21702.11}
\]

Thus the proposed parabolic wedge of `L-21701` has a concrete uniform proof architecture. Promotion of the fixed cone remains contingent on an independent audit of Section 8.

## 3. Exact beta main term

Put

\[
 f_{m,k}(t)=t^{-2m}(R-t^{-2})^k,
 \qquad t\ge\gamma_1.
 \tag{L-21702.12}
\]

It is positive and has one maximum. Indeed,

\[
 \frac{d}{dt}\log f_{m,k}(t)
 =-\frac{2m}{t}
  +\frac{2k}{t(Rt^2-1)},
 \tag{L-21702.13}
\]

so the saddle is

\[
 \boxed{
 t_*^2=\frac{k+m}{Rm}.}
 \tag{L-21702.14}
\]

Let `N_+(T)` count positive-ordinate zeros with multiplicity. The main density in the Riemann–von Mangoldt formula is

\[
 \frac1{2\pi}\log\frac{t}{2\pi}\,dt.
 \tag{L-21702.15}
\]

Its contraction over the full positive-support interval `t>R^(-1/2)` is exactly (L-21702.8). The omitted fixed interval up to the first zero contributes `O_R(f_(m,k)(gamma_1))`, exponentially smaller than the moving saddle. To evaluate the full-density integral, put

\[
 y=(Rt^2)^{-1}.
 \tag{L-21702.16}
\]

Then

\[
 f_{m,k}(t)
 =R^{m+k}y^m(1-y)^k,
 \qquad
 dt=\frac1{2\sqrt R}y^{-3/2}dy,
 \tag{L-21702.17}
\]

and differentiating the beta integral with respect to its first parameter produces the logarithmic factor. This recovers (L-21702.8) without an asymptotic approximation; only the fixed lower-cutoff correction is deferred to (L-21702.24).

## 4. Uniform size of the main saddle

Let

\[
 f_*=f_{m,k}(t_*).
 \tag{L-21702.18}
\]

The beta parameters are

\[
 \alpha=m-\frac12,
 \qquad
 \beta=k+1.
\]

Under (L-21702.6), `m^2/k -> 0`, and the uniform gamma-ratio estimate gives

\[
 B\!\left(m-\frac12,k+1\right)
 =\Gamma\!\left(m-\frac12\right)
  k^{-m+1/2}
  \exp\!\left(O(m^2/k)\right).
 \tag{L-21702.19}
\]

Also

\[
\begin{aligned}
 &\psi\!\left(k+m+\frac12\right)
 -\psi\!\left(m-\frac12\right)
 -\log(4\pi^2R)\\
 &\hspace{2cm}
 =\log(k/m)+O_R(1)
 \tag{L-21702.20}
\end{aligned}
\]

uniformly, with the bounded values `m=1` absorbed into the constant. Since `k/m -> infinity`, the bracket is positive and tends to infinity.

Stirling's formula, or the local beta normalization, now gives

\[
 \boxed{
 I_{m,k}(R)
 \asymp_R
 f_*\frac{\sqrt k}{m}
 \log(k/m).}
 \tag{L-21702.21}
\]

The factor `sqrt(k)/m` is the effective saddle width in the zero-ordinate variable:

\[
 \Delta t_*\asymp\frac{t_*}{\sqrt m}
 \asymp_R\frac{\sqrt k}{m}.
 \tag{L-21702.22}
\]

This width is the source of the parabolic scale.

## 5. Uniform Riemann–von Mangoldt remainder

Write

\[
 N_+(T)
 =N_0(T)+E(T),
 \qquad
 |E(T)|\le C\log(T+2),
 \tag{L-21702.23}
\]

where `N_0'` is the density (L-21702.15), with the standard lower-order smooth terms included in `N_0` if desired.

Stieltjes integration by parts gives

\[
 M_{m,k}(R)-I_{m,k}(R)
 =-\int_{\gamma_1}^{\infty}E(t)f_{m,k}'(t)\,dt
 +O_R(f_{m,k}(\gamma_1)).
 \tag{L-21702.24}
\]

The endpoint term is exponentially smaller than the moving saddle. Since `f_(m,k)` increases to `f_*` and then decreases,

\[
 \int|f_{m,k}'(t)|\log(t+2)dt
 \ll_R f_*\log(t_*+2).
 \tag{L-21702.25}
\]

On the decreasing tail, this follows by one more integration by parts; the remaining integral of `f(t)/(t+2)` is `O_R(f_*)`.

Combining (L-21702.21), (L-21702.24), and (L-21702.25) yields

\[
 \boxed{
 M_{m,k}(R)
 =I_{m,k}(R)
 \left(1+O_R(m/\sqrt k)+o_R(1)\right).}
 \tag{L-21702.26}
\]

Therefore

\[
 M_{m,k}(R)=I_{m,k}(R)(1+o_R(1))
 \tag{L-21702.27}
\]

uniformly in the parabolic regime.

This is stronger than a fixed-row application of Riemann–von Mangoldt: the moving saddle contains asymptotically many zeros exactly when `sqrt(k)/m -> infinity`.

## 6. Exact displacement ratio

For a zero (L-21702.1), put

\[
 q=\frac a\gamma,
 \qquad
 y=\frac1{R\gamma^2},
 \qquad
 A(q)=(1-iq)^{-2}.
 \tag{L-21702.28}
\]

The ratio of the actual summand to its positive surrogate is

\[
 \boxed{
 \mathfrak R_{m,k}(y,q)
 =A(q)^m
 \left(\frac{1-yA(q)}{1-y}\right)^k.}
 \tag{L-21702.29}
\]

The zero symmetry `a -> -a` replaces the pair by

\[
 2f_{m,k}(\gamma)\Re\mathfrak R_{m,k}(y,q).
 \tag{L-21702.30}
\]

The elementary relation

\[
 \boxed{q^2=a^2Ry\le\frac R4y}
 \tag{L-21702.31}
\]

couples the horizontal displacement to the saddle variable. It is the key uniform gain: as the saddle moves upward, every possible off-line displacement becomes proportionally smaller.

## 7. Central-window complex estimate

The beta saddle in `y` is

\[
 y_*={m\over m+k},
 \qquad
 \operatorname{sd}(y)\asymp{\sqrt m\over k}.
 \tag{L-21702.32}
\]

Choose `L=L_(m,k) -> infinity` sufficiently slowly that

\[
 Lm/\sqrt k\to0,
 \qquad
 L^2m/k\to0,
 \tag{L-21702.33}
\]

and, when `m` is bounded, also

\[
 L^{3/2}/\sqrt k\to0.
\]

Consider the central window

\[
 |y-y_*|\le L{\sqrt m\over k}.
 \tag{L-21702.34}
\]

For `y` in this window, (L-21702.31) makes `q=o(1)`. Taylor's theorem, uniformly on the window, gives

\[
\begin{aligned}
 \log\mathfrak R_{m,k}(y,q)
 ={}&2iq\left(m-\frac{ky}{1-y}\right)\\
 &+O_R\!\left(
  \frac{(m+ky)q^2}{(1-y)^2}
  +\frac{(m+ky)|q|^3}{(1-y)^3}
 \right).
\end{aligned}
 \tag{L-21702.35}
\]

The linear coefficient vanishes exactly at `y=y_*`. Since

\[
 \left|m-\frac{ky}{1-y}\right|
 \ll k|y-y_*|
 \ll L\sqrt m,
 \tag{L-21702.36}
\]

one obtains

\[
 q\left|m-\frac{ky}{1-y}\right|
 =o(1).
 \tag{L-21702.37}
\]

The real and higher-order terms satisfy

\[
 (m+ky)q^2=o(1),
 \qquad
 (m+ky)|q|^3=o(1)
 \tag{L-21702.38}
\]

by (L-21702.6), (L-21702.31), and the slow choice of `L`. Hence

\[
 \boxed{
 \mathfrak R_{m,k}(y,q)=1+o_R(1)}
 \tag{L-21702.39}
\]

uniformly for every zero whose surrogate saddle coordinate lies in the central window. In particular,

\[
 \Re\mathfrak R_{m,k}(y,q)=1+o_R(1)>0.
 \tag{L-21702.40}
\]

The cancellation in (L-21702.36) is essential. A termwise phase estimate away from the beta saddle would incorrectly demand a stronger cubic or higher schedule.

### Second-order saddle cancellation

There is a further exact structural reason the quadratic scale is natural. Expanding at the algebraic saddle `y_*=m/(m+k)` gives

\[
\begin{aligned}
 \log\mathfrak R_{m,k}(y_*,q)
 ={}&
 \frac{2m(k+m)}kq^2\\
 &+\frac{2im(5k^2+9km+4m^2)}{3k^2}q^3
 +O_R((m+k)q^4).
\end{aligned}
 \tag{L-21702.41}
\]

The positive quadratic modulus term is

\[
 \frac{2m(k+m)}kq^2.
 \tag{L-21702.42}
\]

On the other hand, the linear phase away from the saddle has derivative

\[
 -2q\frac{(m+k)^2}{k}
 \tag{L-21702.43}
\]

with respect to `y`. Contracting its square against the leading beta variance

\[
 \operatorname{Var}(y)
 \sim\frac{mk}{(m+k)^3}
 \tag{L-21702.44}
\]

produces the Gaussian characteristic-function loss

\[
 \frac12
 \left(2q\frac{(m+k)^2}{k}\right)^2
 \operatorname{Var}(y)
 \sim
 \frac{2m(k+m)}kq^2,
 \tag{L-21702.45}
\]

which cancels the modulus amplification to leading order. The present proof uses only the easier small-`m/sqrt(k)` consequence. The exact cancellation suggests a sharper transition-strip attack: evaluate the full complex saddle before taking absolute values, rather than charging phase and modulus separately.

## 8. Tail control, including the complex displacement

For `0<y<1`, direct algebra gives

\[
 |A(q)|=(1+q^2)^{-1}
 \tag{L-21702.46}
\]

and

\[
\begin{aligned}
 |1-yA(q)|^2-(1-y)^2
 ={}&\frac{q^2}{(1+q^2)^2}\\
 &\times\left[2y(3+q^2)-y^2(2+q^2)\right].
\end{aligned}
 \tag{L-21702.47}
\]

Thus, for `y` in a fixed sufficiently small interval,

\[
 \boxed{
 |\mathfrak R_{m,k}(y,q)|
 \le
 \exp\!\left(
 C_R{ky^2\over(1-y)^2}
 \right).}
 \tag{L-21702.48}
\]

The surrogate beta exponent outside (L-21702.34) dominates this perturbation. Standard beta Chernoff bounds, together with (L-21702.48), show that the actual and surrogate contributions from

\[
 y\le\eta_R,
 \qquad
 |y-y_*|>L\sqrt m/k
\]

are `o_R(I_(m,k))`.

For `y>=eta_R`, condition (L-21702.3), the universal bound on `|a|`, and compactness give

\[
 |1-yA(q)|\le r_R<1.
 \tag{L-21702.49}
\]

The resulting contribution is `O(r_R^k)` times a subexponential zero-count factor. Since `m=o(sqrt(k))`, this is exponentially smaller than the beta saddle. Therefore the complete displaced tail is also negligible.

Combining the central estimate and both tails yields

\[
 \boxed{
 \mathcal H_{m,k}(R)
 =M_{m,k}(R)(1+o_R(1)).}
 \tag{L-21702.50}
\]

Together with (L-21702.27), this proves (L-21702.7).

## 9. Fixed-cone extraction

The proof above is uniform in the single small parameter

\[
 \lambda={m\over\sqrt k}.
 \tag{L-21702.51}
\]

More precisely, the Riemann–von Mangoldt loss, central phase loss, and modulus loss are bounded by a function `eta_R(lambda)` with

\[
 \eta_R(\lambda)\to0
 \qquad(\lambda\downarrow0),
 \tag{L-21702.52}
\]

plus a term tending to zero as `k/m -> infinity`. Choose `lambda_R>0` so that the total relative error is below `1/2`, and put

\[
 C_R=\lambda_R^{-2}.
\]

After increasing the finite threshold `K_R`, every pair satisfying `k>=C_Rm^2` lies in the positive regime. This proves (L-21702.11).

No effective numerical value is claimed for `C_R` in this file. It can be made explicit by inserting a chosen explicit Riemann–von Mangoldt remainder and the constants in Sections 7–8.

## 10. Consequence for the full Hausdorff programme

The complete `(m,k)` quadrant has two candidate large sectors, one finite-directed and one supplied by the proposed uniform argument here:

1. **verified-height saddle sector:** rows whose saddle packet lies entirely inside the certified critical-line zero block;
2. **unconditional parabolic cone:**
   \[
   k\ge C_Rm^2.
   \]

The only genuinely global region left by these two mechanisms is a diagonal transition strip in which

```text
saddle ordinate exceeds the verified height,
while
sqrt(k)/m is not yet large enough for zero-density smoothing.
```

That strip is exactly where individual unverified zero geometry can influence a Hausdorff row. It is therefore a serious RH-bearing target, not a bookkeeping remainder.

A full resolution can now attack this strip with one of:

- a directed moving zero packet plus an off-line-safe residual;
- a local zero-spacing/phase estimate on the saddle window;
- the prime-energy/dispersion coordinate of PR #216;
- the screw–Stieltjes transform (L-21701.3), transferring a global prime-side positivity estimate into the remaining moment rows.

## 11. Proof boundary

Supplied here as a proposed proof, pending independent verification:

- the uniform beta main term;
- the uniform Riemann–von Mangoldt error in the regime `m/sqrt(k)->0`;
- the saddle cancellation of the first-order off-line phase;
- control of the displaced tails;
- eventual positivity throughout a fixed parabolic cone.

Not closed:

- the diagonal transition strip;
- a complete all-row Hausdorff proof;
- RH.

This result strengthens the fixed-row theorem of `L-21701` but does not retroactively verify that file or claim a full resolution.
