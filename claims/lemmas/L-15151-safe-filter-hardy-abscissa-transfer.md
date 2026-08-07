# L-15151 — Safe-filter Hardy abscissa transfer

Claim ID: `L-15151`  
Title: A zero-free safe filter transfers the rightmost meromorphic pole exactly to weighted `L2` and cumulative-energy growth  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Dependencies: half-plane Paley–Wiener; standard logarithmic-derivative estimates on a fixed zero-free half-plane  
Scope: standalone repair of the analytic interface used by `T-15119`, `T-21501`, and `T-21502`

## 1. Abstract causal statement

Let `q` be locally square-integrable, supported in `[x0,infinity)`, and let

\[
 F(z)=\int_{x_0}^{\infty}q(x)e^{-zx}\,dx
 \tag{L-15151.1}
\]

initially converge on `Re z>sigma_0`. Suppose that `F` has a meromorphic continuation to `Re z>0`. Put

\[
 \Theta(F)=\sup\{\operatorname{Re}p:p\text{ is a nonremovable pole of }F,
 \ \operatorname{Re}p>0\},
 \tag{L-15151.2}
\]

with the empty supremum interpreted as zero.

Assume that, for every `sigma>Theta(F)`, the continued function is analytic on `Re z>=sigma` and satisfies

\[
 \boxed{
 \sup_{u\ge\sigma}
 \int_{\mathbb R}|F(u+it)|^2dt<\infty.}
 \tag{L-15151.3}
\]

Then

\[
 \boxed{
 \Theta(F)=
 \inf\left\{\sigma>0:
 \int_{x_0}^{\infty}e^{-2\sigma x}|q(x)|^2dx<\infty
 \right\}.}
 \tag{L-15151.4}
\]

If

\[
 E_q(X)=\int_{x_0}^{X}|q(x)|^2dx,
 \tag{L-15151.5}
\]

then also

\[
 \boxed{
 \Theta(F)=
 \limsup_{X\to\infty}
 {\log(1+E_q(X))\over2X}.}
 \tag{L-15151.6}
\]

### Proof of the lower bound

If `e^{-sigma x}q(x)` belongs to `L2`, then for every `u>sigma`, Cauchy–Schwarz gives absolute convergence of (L-15151.1), locally uniformly in `Re z>sigma`:

\[
 \int_{x_0}^{\infty}|q(x)|e^{-ux}dx
 \le
 \|e^{-\sigma x}q\|_2
 \left(\int_{x_0}^{\infty}e^{-2(u-\sigma)x}dx\right)^{1/2}.
\]

Thus the Laplace transform is holomorphic in `Re z>sigma`. It agrees with the original `F` on the common initial half-plane, so uniqueness of analytic continuation forbids a nonremovable pole with real part greater than `sigma`. Hence `Theta(F)<=sigma`.

### Proof of the upper bound

Fix `sigma>Theta(F)`. Condition (L-15151.3) says that `F` belongs to Hardy `H2` of the half-plane `Re z>sigma`. Half-plane Paley–Wiener supplies a unique function `q_sigma in L2([x0,infinity))` whose Laplace transform is `F(z+sigma)` after the harmless translation by `x0`. On the original convergence half-plane this is also the transform of `e^{-sigma x}q(x)`. Uniqueness of the Laplace transform identifies the two functions, so the weighted energy is finite.

### Cumulative exponent

For the nonnegative measure `dE_q=|q(x)|^2dx`, the abscissa of convergence of

\[
 \int e^{-2\sigma x}dE_q(x)
\]

is its upper exponential growth exponent. The two elementary implications follow from Stieltjes integration by parts and from

\[
 \int_{x_0}^{X}e^{-2\sigma x}dE_q(x)
 \ge e^{-2\sigma X}E_q(X).
\]

This proves (L-15151.6).

## 2. A sufficient vertical estimate

Condition (L-15151.3) follows if, for every `sigma>Theta(F)`, there are constants `C,B` and `epsilon>0` such that

\[
 |F(u+it)|
 \le C(1+\log(2+|t|))^B(1+|t|)^{-1/2-\epsilon}
 \tag{L-15151.7}
\]

uniformly for `u>=sigma`. A finite set of removable singularities inside a compact rectangle is filled in before taking the bound.

For a logarithmic derivative, the standard fixed-zero-free-half-plane estimate is polylogarithmic in `|t|`. Therefore one inverse power of `t` from the safe filter is sufficient; two inverse powers give ample reserve.

## 3. Chebyshev dilation corollary

For the causal filter of `L-15145`,

\[
 \widehat W_a(z)={1-\sqrt a\,a^{-z}\over z+1/2},
 \]

and

\[
 \mathcal LQ_a(z)
 =-\widehat W_a(z){\zeta'\over\zeta}(z+1/2).
 \tag{L-15151.8}
\]

The factor `widehat W_a` cancels the shifted zeta pole at `z=1/2`, has no zero in

\[
 0<\operatorname{Re}z<1/2,
\]

and is `O((1+|t|)^-1)` on every closed substrip. If

\[
 \Theta_\zeta=\sup_{\zeta(\rho)=0}(\operatorname{Re}\rho-1/2),
\]

then the nonremovable poles of (L-15151.8) in the right half-plane have rightmost real part `Theta_zeta`. For `sigma>Theta_zeta`, the product is analytic on `Re z>=sigma`; on bounded real-part strips the logarithmic derivative has a uniform polylogarithmic vertical bound, and for large real part its Euler series is uniformly bounded. Hence (L-15151.3) holds and

\[
 \boxed{
 \Theta_\zeta=\limsup_{Y\to\infty}
 {\log(1+\mathcal E_a(Y))\over2\log Y},}
 \]

with

\[
 \mathcal E_a(Y)=\int_2^Y
 \left|{\psi(t)\over t}-{\psi(t/a)\over t/a}\right|^2dt.
\]

This supplies the standalone analytic step requested in the second-pass review of `T-15119`.

## 4. Compact and prime-only corollaries

The compact triangular filter of `T-21501` has two inverse powers of vertical decay and the same open-strip zero-free property, so the argument above applies verbatim.

For the ordinary-prime signal of `T-21502`, Möbius inversion gives

\[
 P_1(s)=\sum_{r\ge1}\mu(r)\left[-{\zeta'\over\zeta}(rs)\right].
\]

On `s=1/2+z` and `Re z>=sigma>0`, the `r=2` and all `r>=3` terms are uniformly represented in an absolute-convergence half-plane; only the `r=1` term carries nontrivial-zero poles. The extra boundary difference cancels the `z=0` pole, while the compact safe factor cancels `z=1/2` and no zero in the open counterexample strip. The same uniform `H2` estimate therefore proves the prime-only rightmost-pole transfer.

## 5. Proof boundary

Closed here:

- the lower analytic-continuation implication;
- the upper half-plane `H2` implication;
- the cumulative-energy exponent;
- the explicit uniformity needed for the Chebyshev, compact, and prime-only safe filters.

The lemma does not prove that the common exponent is zero. It closes the analytic transfer interface only.