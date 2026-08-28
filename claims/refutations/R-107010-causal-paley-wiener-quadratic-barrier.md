# R-107010 — Exact quadratic Nyquist rank is impossible by source-blind causal tail deletion

Claim ID: `R-107010`  
Status: **PROVED ANALYTIC NO-GO THEOREM**  
Created: 2026-08-27  
Depends on: classical Paley--Wiener uniqueness  
RH status: **not involved**

Let \(B\in L^2(\mathbf R)\) be nonzero and supported in a finite interval.
Write

\[
 F_B(T)
 =
 \int_{|t|\ge T}|\widehat B(t)|^2\,dt.
\]

## 1. No exponential Fourier-energy tail

Suppose that for some \(c>0\),

\[
 F_B(T)\ll e^{-cT}.
 \tag{R-107010.1}
\]

For every \(0<a<c/2\), layer-cake integration gives

\[
 \int_{\mathbf R}
 e^{2a|t|}|\widehat B(t)|^2dt<\infty.
\]

Fourier inversion then extends \(B\) holomorphically to the strip
\(|\Im z|<a\). On the real axis, \(B\) vanishes on a nonempty open interval
outside its compact support. The identity theorem forces \(B=0\), a
contradiction.

Thus

\[
 \boxed{
 F_B(T)\ne O(e^{-cT})
 \quad\text{for every }c>0.
 }
 \tag{R-107010.2}
\]

## 2. Consequence for source-blind beta truncation

Suppose an exterior estimate is obtained solely from

\[
 |D_X(t)|\le C\sqrt X
\]

and a fixed compact detector, so that it requires

\[
 F_B(T_A(X))\ll X^{-A-1}.
 \tag{R-107010.3}
\]

If \(T_A(X)\le C_A\log X\) for all sufficiently large \(X\), take
\(X=e^{T/C_A}\). Monotonicity of \(F_B\) gives

\[
 F_B(T)
 \le
 F_B(T_A(X))
 \ll
 e^{-(A+1)T/C_A},
\]

contradicting (R-107010.2). Therefore

\[
 \boxed{
 \frac{T_A(X)}{\log X}
 \text{ cannot remain bounded.}
 }
 \tag{R-107010.4}
\]

Since exact Nyquist sampling has spacing
\(2\pi/(\log X+O(1))\), any such source-blind causal truncation must retain

\[
 \boxed{
 \omega((\log X)^2)
 }
\]

samples. Exact \(O((\log X)^2)\) rank is impossible in this architecture.

## 3. Cartwright/Bartrand refinement

For a nonzero compactly supported \(B\), the classical logarithmic-integral
theorem gives

\[
 \int_{\mathbf R}
 \frac{\log|\widehat B(t)|}{1+t^2}\,dt>-\infty.
\]

Therefore an envelope

\[
 |\widehat B(t)|
 \le
 C\exp\{-c|t|/V(|t|)\}
\]

requires

\[
 \int^\infty\frac{dt}{tV(t)}<\infty.
 \tag{R-107010.5}
\]

The weights \(W_m\) in `L-107010` satisfy this condition exactly because the
last iterated logarithm is squared. Replacing that final square by first
power makes the integral diverge. The Bertrand ladder therefore sits at the
causal Paley--Wiener boundary at every finite depth.

This no-go concerns analytic exterior deletion. It does not preclude an
arithmetic theorem which controls high frequencies more efficiently than the
trivial beta bound.
