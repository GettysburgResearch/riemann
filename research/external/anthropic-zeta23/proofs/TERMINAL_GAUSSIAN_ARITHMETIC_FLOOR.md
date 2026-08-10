# Terminal Gaussian arithmetic floor: an exact completed-Chebyshev normal form

**Status:** `PROPOSED COMPLETE NORMAL-FORM THEOREM / THE FINAL ONE-SIDED ARITHMETIC INEQUALITY REMAINS OPEN`  
**RH status:** **unproved**  
**Dependencies:** the Guinand--Weil normalization used in the imported Zeta23 paper; PR #364's proposed terminal-pair theorem; PR #365's complete form/metric capture; PR #199's corrected-kernel equivalence.

This note attacks the remaining corrected-kernel floor directly on the explicit Gaussian family that detects a hypothetical terminal off-line pair. It removes the matrix, Schur-complement, Gram-conditioning, pole-main-term, and archimedean bookkeeping from the final arithmetic question.

The surviving statement is one explicit oscillatory transform of the completed Chebyshev discrepancy

\[
 \Theta(t)=\psi(e^t)-e^t+1,
 \qquad
 \psi(X)=\sum_{n\le X}\Lambda(n).
\]

Proving its asymptotic nonnegativity would prove the corrected-kernel floor and RH. This note does **not** prove that last sign.

## 1. A general exact normal form

Use the Fourier convention

\[
 \widehat f(\tau)=\int_{\mathbb R}f(u)e^{i\tau u}\,du.
\]

For a Schwartz function `f`, put

\[
 k_f(v)=(f*\widetilde f)(v)
       =\int_{\mathbb R}f(u)\overline{f(u-v)}\,du,
 \qquad
 \widetilde f(u)=\overline{f(-u)}.
\]

Then

\[
 \widehat{k_f}(\tau)=|\widehat f(\tau)|^2
 \quad(\tau\in\mathbb R),
 \qquad
 k_f(-v)=\overline{k_f(v)}.
\]

Write

\[
 S_f(v)=k_f(v)+k_f(-v)=2\operatorname{Re}k_f(v),
 \qquad
 w_f(v)=e^{-v/2}S_f(v)
 \quad(v\ge0).
\]

Let

\[
 \Gamma(f)=\int_{\mathbb R}|\widehat f(\tau)|^2\mu(\tau)\,d\tau,
\]

where `mu` is the archimedean density in the imported explicit formula.

### Theorem 1.1 (completed-Chebyshev representation)

For every Schwartz `f` for which the displayed integrals converge absolutely,

\[
 \boxed{
 W(f,f)
 =\Gamma(f)
  +R_{\mathrm{low}}(f)
  +\int_0^\infty \Theta(t)w_f'(t)\,dt,
 }
 \tag{AF.1}
\]

where

\[
 \boxed{
 R_{\mathrm{low}}(f)
 =\int_0^\infty e^{-t/2}S_f(t)\,dt.
 }
 \tag{AF.2}
\]

Thus the pole and the continuum main term of the prime sum cancel **exactly**; the only prime fluctuation left is the completed Chebyshev discrepancy.

### Proof

The Guinand--Weil formula in the imported normalization gives

\[
 W(f,f)=\Gamma(f)+P(f)-\mathcal P(f),
 \tag{AF.3}
\]

with

\[
 P(f)
 =\int_{\mathbb R}k_f(t)(e^{-t/2}+e^{t/2})\,dt
 =\int_0^\infty(e^{t/2}+e^{-t/2})S_f(t)\,dt
 \tag{AF.4}
\]

and

\[
 \mathcal P(f)
 =\sum_{n\ge2}{\Lambda(n)\over\sqrt n}S_f(\log n)
 =\int_{[0,\infty)}w_f(t)\,d\psi(e^t).
 \tag{AF.5}
\]

Split

\[
 d\psi(e^t)=e^t\,dt+d\Theta(t).
\]

The continuum part is

\[
 \int_0^\infty e^t w_f(t)\,dt
 =\int_0^\infty e^{t/2}S_f(t)\,dt.
 \tag{AF.6}
\]

It cancels the first term in `(AF.4)`, leaving `(AF.2)`. Since

\[
 \Theta(0)=\psi(1)-1+1=0
\]

and the boundary at infinity vanishes, Stieltjes integration by parts gives

\[
 \int_{[0,\infty)}w_f\,d\Theta
 =-\int_0^\infty\Theta(t)w_f'(t)\,dt.
 \tag{AF.7}
\]

Substitution in `(AF.3)` proves `(AF.1)`. Compactly supported `C^2` tests follow directly from the paper's formula; the Schwartz statement follows by the usual form-domain approximation. `square`

## 2. The exact terminal Gaussian cardinal

Fix

\[
 z=x+iy,
 \qquad x\in\mathbb R,
 \qquad 0<y<\frac12,
\]

and `sigma>0`. Put

\[
 a=\sigma^2y^2,
 \qquad
 D=e^{2a}-1,
\]

and define

\[
 \boxed{
 f_{\sigma,z}(u)
 ={e^{-u^2/(2\sigma^2)}
   (e^{-i\overline z u}-e^{-izu})
  \over
   \sqrt{2\pi}\,\sigma D}.
 }
 \tag{AF.8}
\]

Its Fourier transform is

\[
 \boxed{
 F_{\sigma,z}(w)
 ={e^{-\sigma^2(w-\overline z)^2/2}
   -e^{-\sigma^2(w-z)^2/2}
  \over D}.
 }
 \tag{AF.9}
\]

Hence

\[
 \boxed{
 F_{\sigma,z}(z)=1,
 \qquad
 F_{\sigma,z}(\overline z)=-1.
 }
 \tag{AF.10}
\]

For real `tau`,

\[
 \boxed{
 |F_{\sigma,z}(\tau)|^2
 ={4e^{a-\sigma^2(\tau-x)^2}
   \sin^2(\sigma^2y(\tau-x))
  \over D^2}.
 }
 \tag{AF.11}
\]

## 3. Closed autocorrelation and the final scalar

Define

\[
 A_{\sigma,y}
 ={e^a\over\sqrt\pi\,\sigma D^2}
 \tag{AF.12}
\]

and the even three-Gaussian shell

\[
 \boxed{
 H_{\sigma,y}(t)
 =e^{-t^2/(4\sigma^2)}
 -\frac12e^{-(t-2\sigma^2y)^2/(4\sigma^2)}
 -\frac12e^{-(t+2\sigma^2y)^2/(4\sigma^2)}.
 }
 \tag{AF.13}
\]

Fourier inversion of `(AF.11)` gives exactly

\[
 \boxed{
 k_{\sigma,z}(t)
 =A_{\sigma,y}e^{-ixt}H_{\sigma,y}(t).
 }
 \tag{AF.14}
\]

Therefore

\[
 S_{\sigma,z}(t)
 =2A_{\sigma,y}H_{\sigma,y}(t)\cos(xt),
 \tag{AF.15}
\]

and

\[
 w_{\sigma,z}(t)
 =2A_{\sigma,y}e^{-t/2}H_{\sigma,y}(t)\cos(xt).
 \tag{AF.16}
\]

Put

\[
 \boxed{
 \mathfrak A_\sigma(x,y)
 =2A_{\sigma,y}
  \int_0^\infty\Theta(t)
  {d\over dt}
  \left[e^{-t/2}H_{\sigma,y}(t)\cos(xt)\right]dt.
 }
 \tag{AF.17}
\]

The general normal form becomes

\[
 \boxed{
 W(f_{\sigma,z},f_{\sigma,z})
 =\mathfrak A_\sigma(x,y)
  +\Gamma(f_{\sigma,z})
  +R_{\mathrm{low}}(f_{\sigma,z}).
 }
 \tag{AF.18}
\]

This is the requested arithmetic floor evaluated on the explicit terminal-pair direction. It is a scalar, not a matrix inequality.

## 4. The discarded terms really vanish

The real-axis spectral mass is exactly

\[
 \boxed{
 \int_{\mathbb R}|F_{\sigma,z}(\tau)|^2d\tau
 ={2\sqrt\pi\,(e^a-1)\over\sigma(e^{2a}-1)^2}
 =O_y(\sigma^{-1}e^{-3a}).
 }
 \tag{AF.19}
\]

Since `mu(tau)=O(1+log(2+|tau|))`, for fixed `x,y`,

\[
 \boxed{
 \Gamma(f_{\sigma,z})=o(1).
 }
 \tag{AF.20}
\]

Also

\[
 \|f_{\sigma,z}\|_1
 \le {2e^{a/2}\over e^{2a}-1},
 \tag{AF.21}
\]

so Young's inequality gives

\[
 \|k_{\sigma,z}\|_1
 \le\|f_{\sigma,z}\|_1^2
 =O(e^{-3a}).
\]

Consequently

\[
 \boxed{
 R_{\mathrm{low}}(f_{\sigma,z})=o(1).
 }
 \tag{AF.22}
\]

Combining `(AF.18)`, `(AF.20)`, and `(AF.22)`,

\[
 \boxed{
 W(f_{\sigma,z},f_{\sigma,z})
 =\mathfrak A_\sigma(x,y)+o(1).
 }
 \tag{AF.23}
\]

## 5. Exact relation to the corrected-kernel floor

PR #364 proposes that, if RH is false, there is a terminal off-line pair

\[
 z=x+iy,
 \qquad \overline z=x-iy,
\]

of multiplicity `m` for which the complete nuisance leakage of `(AF.8)` tends to zero. Its zero-side Weil value is therefore

\[
 W(f_{\sigma,z},f_{\sigma,z})=-2m+o(1).
 \tag{AF.24}
\]

Equation `(AF.23)` then gives

\[
 \boxed{
 \mathfrak A_\sigma(x,y)=-2m+o(1).
 }
 \tag{AF.25}
\]

Under RH, Weil positivity gives `W(f,f)>=0`; hence `(AF.23)` gives

\[
 \liminf_{\sigma\to\infty}\mathfrak A_\sigma(x,y)\ge0
 \qquad(x\in\mathbb R,\ 0<y<1/2).
 \tag{AF.26}
\]

Therefore, conditional only on the already-declared terminal-pair/capture interfaces,

\[
 \boxed{
 \mathrm{RH}
 \iff
 \forall x\in\mathbb R\ \forall 0<y<\frac12:\
 \liminf_{\sigma\to\infty}\mathfrak A_\sigma(x,y)\ge0.
 }
 \tag{AF.27}
\]

By PR #199, this is also equivalent to the complete corrected-kernel floor

\[
 B_{\mathrm{ker},j}
 -Z_{\mathrm{ker},j}^*C_j^{-1}Z_{\mathrm{ker},j}
 \succeq-\varepsilon_jG_{\mathrm{ker},j},
 \qquad\varepsilon_j\to0.
\]

Thus all matrix and interpolation obligations have been removed. The unresolved theorem is exactly the one-sided scalar inequality `(AF.26)`.

## 6. Why the ordinary PNT envelope does not prove the sign

A phase-blind use of the classical PNT error has the form

\[
 |\Theta(t)|\le e^{t-o(t)}.
 \tag{AF.28}
\]

Apply this absolute envelope to the shifted Gaussian in `(AF.17)`. The relevant saddle exponent is

\[
 \max_{t\ge0}
 \left\{
 {t\over2}
 -{(t-2\sigma^2y)^2\over4\sigma^2}
 -3\sigma^2y^2
 \right\}
 =\sigma^2\left({1\over4}+y-3y^2\right).
 \tag{AF.29}
\]

For every `0<y<1/2`,

\[
 {1\over4}+y-3y^2
 =3\left({1\over2}-y\right)\left(y+{1\over6}\right)>0.
 \tag{AF.30}
\]

Hence direct absolute-value insertion of every standard zero-free-region/PNT envelope produces an exponentially **growing** upper bound. It cannot yield the `o(1)` error required in `(AF.26)`. The missing input must use oscillation at the exact frequency `x`, not merely the size of `psi(X)-X`.

This is a method firewall, not a proof that no arithmetic argument exists.

## 7. Why more bandwidth-one trace moments do not see one pair

Let a compact window have support length `L=lambda log T`. For one off-line pair of depth `y`, its complete-frame negative eigenvalue is bounded in magnitude by

\[
 O(e^{yL}),
 \tag{AF.31}
\]

because `cosh(2yu)<=e^{yL}` on `|u|<=L/2`.

Suppose an `r`-th prime-side trace moment is available only in the unconditional Rudnick--Sarnak resource range

\[
 r\lambda<2.
\]

Then the largest possible contribution of that one pair to the `r`-th trace is

\[
 e^{ryL}
 \le T^{2y+o(1)}
 =o(T)
 \qquad(y<1/2),
 \tag{AF.32}
\]

whereas the compression dimension is of order `T log T`. Thus normalized raw trace moments remain unable to detect one isolated pair even when their order grows while their support shrinks.

The scalar `(AF.17)` escapes this averaging barrier because it is a captured, pair-adapted direction rather than a normalized global trace.

## 8. Exact remaining theorem

The arithmetic corrected-kernel floor is now reduced to:

> **Terminal Gaussian Chebyshev gate.** For every fixed `x in R` and `0<y<1/2`,
> \[
> 2A_{\sigma,y}
> \int_0^\infty
> [\psi(e^t)-e^t+1]
> {d\over dt}
> \left[e^{-t/2}H_{\sigma,y}(t)\cos(xt)\right]dt
> \ge-o(1).
> \]

A proof of this statement proves the requested corrected-kernel floor, and therefore RH. Under a hypothetical terminal off-line pair it fails by the fixed amount `2m`.

## 9. Proof boundary

Proved here, subject to independent analytic review:

1. the exact completed-Chebyshev representation `(AF.1)`;
2. the closed Gaussian cardinal transform and autocorrelation;
3. exact cancellation of the pole's growing main term against the continuous prime main term;
4. vanishing of the archimedean and lower-pole remainders;
5. reduction of the matrix floor to one explicit scalar Gaussian transform;
6. the phase-blind PNT and global-trace-moment firewalls.

Not proved here:

1. the terminal Gaussian Chebyshev gate;
2. the arithmetic corrected-kernel floor;
3. RH.
