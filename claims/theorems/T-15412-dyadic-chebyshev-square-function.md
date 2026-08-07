# T-15412 — A dyadic Chebyshev square function carries the exact rightmost-zero exponent

Claim ID: `T-15412`  
Title: One raw dyadic difference of the Chebyshev function has cumulative square-function exponent exactly equal to the rightmost zeta-zero displacement  
Status: `PROPOSED — COMPLETE GLOBAL TRANSFER THEOREM; DYADIC ENERGY BOUND OPEN`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-07  
Dependencies: the classical Euler-product logarithmic derivative; half-plane Paley–Wiener/Hardy theory; the standard zero-free line and prime number theorem  
Cross-route connections: `T-15404`, `L-19801`, `L-19802`, `L-20704`, `T-21501`  
Scope: a raw-prime, zero-free-filter, one-dimensional global criterion with no continuous main subtraction in the final statistic  
Related counterexample candidates: none

## 1. Chebyshev prefix and the exponential pole-canceling filter

Let

\[
 \psi(Y)=\sum_{n\le Y}\Lambda(n),
 \qquad
 C(Y)=\frac{\psi(Y)}Y,
 \tag{T-15412.1}
\]

with `psi(Y)=0` below the first prime power. Put

\[
 h=\log4.
 \tag{T-15412.2}
\]

Define the one-sided exponential kernel

\[
 g(u)=e^{-u/2}\mathbf1_{[0,\infty)}(u)
 \tag{T-15412.3}
\]

and its pole-canceling dyadic difference

\[
 \boxed{
 G_\diamond(u)=g(u)-2g(u-h).}
 \tag{T-15412.4}
\]

Its bilateral Laplace transform is

\[
 \boxed{
 \widehat G_\diamond(z)
 =\frac{1-2e^{-hz}}{z+1/2},
 \qquad \Re z>-1/2.}
 \tag{T-15412.5}
\]

The numerator vanishes exactly on

\[
 \Re z=\frac12,
 \qquad
 \Im z\in\frac{2\pi}{h}\mathbb Z,
 \tag{T-15412.6}
\]

and nowhere in

\[
 0<\Re z<\frac12.
 \tag{T-15412.7}
\]

In particular, the zero at `z=1/2` cancels the shifted zeta pole while no
shifted off-critical zero can be canceled.

Define the raw prime-power signal

\[
 \boxed{
 Q_\diamond(x)
 =\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 G_\diamond(x-\log n).}
 \tag{T-15412.8}
\]

The sum is finite for every real `x`: the condition `G_diamond(x-log n) != 0` forces `n <= e^x`.

## 2. Exact arithmetic formula

Let `Y=e^x`. Since

\[
 \frac{\Lambda(n)}{\sqrt n}
 g(x-\log n)
 =e^{-x/2}\Lambda(n)\mathbf1_{n\le Y},
\]

and `e^(h/2)=2`, the translated term contributes four times the prefix through
`Y/4`. Therefore

\[
 \boxed{
 Q_\diamond(\log Y)
 =\frac{\psi(Y)-4\psi(Y/4)}{\sqrt Y}.}
 \tag{T-15412.9}
\]

The normalization in `C` makes the pole cancellation literal:

\[
 4\psi(Y/4)=Y C(Y/4),
\]

so

\[
 \boxed{
 Q_\diamond(\log Y)
 =\sqrt Y\left[C(Y)-C(Y/4)\right].}
 \tag{T-15412.10}
\]

Thus the final signal uses no zero ordinate, no continuous main subtraction,
no prime tail, and no finite-dimensional spectral packet. It is simply one
dyadic discrepancy of the ordinary Chebyshev function.

## 3. Exact dyadic square-function identity

For `Y>=1`, put

\[
 \boxed{
 \mathcal E_\diamond(Y)
 =\int_1^Y|C(t)-C(t/4)|^2\,dt.}
 \tag{T-15412.11}
\]

With the convention in (T-15412.1), the change of variables `t=e^x`, together with (T-15412.10), gives exactly

\[
 \boxed{
 \mathcal E_\diamond(Y)
 =\int_0^{\log Y}|Q_\diamond(x)|^2\,dx.}
 \tag{T-15412.12}
\]

Equivalently,

\[
 \boxed{
 \mathcal E_\diamond(Y)
 =\int_1^Y
 \frac{|\psi(t)-4\psi(t/4)|^2}{t^2}\,dt.}
 \tag{T-15412.13}
\]

This is a dyadic square function of one elementary arithmetic prefix. Its
expected RH scale is logarithmic or polylogarithmic; a right-of-line zero forces
polynomial growth in `Y`.

## 4. Laplace transform and visible singularities

For `Re z>1/2`, absolute convergence and a change of variables give

\[
\begin{aligned}
 \mathcal LQ_\diamond(z)
 &=\int_{\mathbb R}e^{-zx}Q_\diamond(x)\,dx\\
 &=\widehat G_\diamond(z)
   \sum_{n\ge2}\frac{\Lambda(n)}{n^{z+1/2}}\\
 &=\boxed{
 -\frac{1-2e^{-hz}}{z+1/2}
  \frac{\zeta'}{\zeta}\!\left(z+\frac12\right).}
\end{aligned}
 \tag{T-15412.14}
\]

At `z=1/2`, the numerator has a simple zero and the zeta logarithmic derivative
has the shifted pole, so the product is regular. Every nontrivial zero `rho`
with `Re rho>1/2` creates a pole at

\[
 z_\rho=\rho-\frac12.
\]

Equation (T-15412.7) shows that this pole is not canceled.

Let

\[
 \Theta_\zeta
 =\sup_{\zeta(\rho)=0}
  \left(\Re\rho-\frac12\right).
 \tag{T-15412.15}
\]

## 5. Weighted-Hardy abscissa

Define

\[
 \sigma_2(Q_\diamond)
 =\inf\left\{
 \sigma>0:
 \int_{\mathbb R}e^{-2\sigma x}|Q_\diamond(x)|^2dx<\infty
 \right\}.
 \tag{T-15412.16}
\]

Then

\[
 \boxed{
 \sigma_2(Q_\diamond)=\Theta_\zeta.}
 \tag{T-15412.17}
\]

### Lower bound

If the weighted integral is finite at `sigma`, Cauchy–Schwarz makes its Laplace
transform holomorphic on `Re z>sigma`. It agrees with (T-15412.14) on
`Re z>1/2`, hence throughout the connected overlap by analytic continuation.
An uncanceled pole with real part larger than `sigma` is impossible. Therefore

\[
 \Theta_\zeta\le\sigma_2(Q_\diamond).
\]

### Upper bound

Fix `sigma>Theta_zeta`. The product in (T-15412.14) is analytic in
`Re z>=sigma`; the apparent pole at `z=1/2`, when present in the larger
continuation region, is removable. On every fixed vertical strip a positive
distance from the shifted zero set, the standard logarithmic-derivative bound
is polylogarithmic in `|t|`. Meanwhile

\[
 \left|\widehat G_\diamond(u+it)\right|
 \ll_\sigma(1+|t|)^{-1}.
 \tag{T-15412.18}
\]

The square is integrable after the polylogarithmic factor. For large `u`, the
Euler-product Dirichlet series is uniformly bounded and

\[
 \int_{\mathbb R}|u+1/2+it|^{-2}dt=\frac\pi{u+1/2}.
\]

Thus the analytically continued product lies in the Hardy space `H^2` of the
half-plane `Re z>sigma`. Half-plane Paley–Wiener gives a causal weighted `L2`
inverse. Uniqueness of the Laplace transform identifies that inverse with the
prime signal. Hence every `sigma>Theta_zeta` is admissible, proving the reverse
inequality.

The single inverse power in (T-15412.18) is sufficient; the compact triangular
window of `T-21501` is not required for the global Hardy transfer.

## 6. Exact cumulative exponent and RH criterion

For a nonnegative locally finite energy density, the Laplace abscissa equals
the upper exponential exponent of its cumulative mass. Combining this fact
with (T-15412.12) and (T-15412.17) yields

\[
 \boxed{
 \Theta_\zeta
 =\limsup_{Y\to\infty}
 \frac{\log\left(1+\mathcal E_\diamond(Y)\right)}
      {2\log Y}.}
 \tag{T-15412.19}
\]

Consequently

\[
 \boxed{
 \mathrm{RH}
 \iff
 \mathcal E_\diamond(Y)=Y^{o(1)}.}
 \tag{T-15412.20}
\]

Equivalently,

\[
 \boxed{
 \mathrm{RH}
 \iff
 \int_1^Y
 \left|
 \frac{\psi(t)}t-
 \frac{\psi(t/4)}{t/4}
 \right|^2dt
 =Y^{o(1)}.}
 \tag{T-15412.21}
\]

More generally, if

\[
 \mathcal E_\diamond(Y)
 \le C_\varepsilon Y^{2\theta+\varepsilon}
 \tag{T-15412.22}
\]

for every `epsilon>0`, then zeta has no zero in

\[
 \Re s>\frac12+\theta.
\]

## 7. Stable equivalence with the classical Chebyshev mean square

Define the one-sided exponential prime prefix

\[
 P_1(x)=e^{-x/2}\psi(e^x)
 \tag{T-15412.23}
\]

and its centered form

\[
 \boxed{
 F(x)=P_1(x)-e^{x/2}\mathbf1_{[0,\infty)}(x).}
 \tag{T-15412.24}
\]

The coefficient `1` is the exact residue of

\[
 \frac{-\zeta'/\zeta(z+1/2)}{z+1/2}
\]

at `z=1/2`. Thus the transform of `F` is regular there and has precisely the
same shifted off-critical poles as (T-15412.14).

Let `tau_hF(x)=F(x-h)`. Since

\[
 \left(I-2\tau_h\right)e^{x/2}=0
 \qquad(x\ge h),
\]

one has

\[
 \boxed{
 Q_\diamond
 =F-2\tau_hF+K_0,}
 \tag{T-15412.25}
\]

where `K_0` is supported in the fixed interval `[0,h]`.

For a weight `0<sigma<1/2`, conjugation by `e^{-sigma x}` turns
`I-2tau_h` into the Fourier multiplier

\[
 1-a_\sigma e^{-ith},
 \qquad
 a_\sigma=2e^{-\sigma h}>1.
 \tag{T-15412.26}
\]

Therefore

\[
 a_\sigma-1
 \le|1-a_\sigma e^{-ith}|
 \le a_\sigma+1.
 \tag{T-15412.27}
\]

The delay filter is boundedly invertible on every such weighted `L2` space. The same is true for `sigma>1/2`, with lower bound `1-a_sigma`; the single boundary value `sigma=1/2` does not change an abscissa. The compact `K_0` does not affect an abscissa. Hence

\[
 \boxed{
 e^{-\sigma x}Q_\diamond\in L^2
 \iff
 e^{-\sigma x}F\in L^2
 \qquad(0<\sigma<1/2).}
 \tag{T-15412.28}
\]

This supplies the second exact global coordinate

\[
 \boxed{
 \Theta_\zeta
 =\limsup_{Y\to\infty}
 \frac{\log\left(1+\mathcal V(Y)\right)}{2\log Y},}
 \tag{T-15412.29}
\]

where

\[
 \boxed{
 \mathcal V(Y)
 =\int_1^Y
 \frac{|\psi(t)-t|^2}{t^2}\,dt.}
 \tag{T-15412.30}
\]

Thus the raw dyadic square function and the classical normalized Chebyshev mean
square have the same exact rightmost-zero exponent.

## 8. Exact anti-causal renewal

The prime number theorem gives

\[
 F(x)=o(e^{x/2}).
 \tag{T-15412.31}
\]

For all sufficiently large `x`, the compact term in (T-15412.25) is absent, so

\[
 Q_\diamond(x)=F(x)-2F(x-h).
\]

Solving this relation toward the future gives

\[
 \boxed{
 F(x)
 =-\sum_{j=1}^{\infty}2^{-j}
 Q_\diamond(x+jh).}
 \tag{T-15412.32}
\]

Indeed, iteration leaves the remainder `2^-N F(x+Nh)`, which tends to zero by
(T-15412.31) and `e^(h/2)=2`.

This is a stable renewal representation on every subcritical exponential
weight. It may be used to transfer estimates between the raw dyadic signal and
the centered prime-prefix error without a zero expansion.

## 9. A remarkably simple full-energy kernel

The exponential profile has the explicit form

\[
 G_\diamond(u)
 =e^{-u/2}
 \begin{cases}
 0,&u<0,\\
 1,&0\le u<h,\\
 -3,&u\ge h.
 \end{cases}
 \tag{T-15412.33}
\]

Its full autocorrelation is

\[
 \boxed{
 C_\diamond(r)
 =\int_{\mathbb R}G_\diamond(u)G_\diamond(u+r)du
 =
 \begin{cases}
 4e^{-|r|/2}-e^{|r|/2},&|r|\le h,\\
 0,&|r|\ge h.
 \end{cases}}
 \tag{T-15412.34}
\]

Thus the complete prime-pair energy couples only multiplicative ratios at most
four. If `m>=n` and `m<=4n`, then

\[
 \frac{\Lambda(m)\Lambda(n)}{\sqrt{mn}}
 C_\diamond(\log(m/n))
 =\boxed{
 \Lambda(m)\Lambda(n)
 \left(\frac4m-\frac1n\right).}
 \tag{T-15412.35}
\]

The coefficient is nonnegative exactly on `n<=m<=4n`, and vanishes at the
outer ratio. Formula (T-15412.35) gives an exceptionally simple bounded-ratio
prime-pair interface for Selberg dispersion. For a finite cumulative energy,
the only additional terms are explicit upper-boundary truncations of the same
piecewise exponential kernel.

The stationary kernel is not by itself an upper bound for the cumulative
energy: boundary terms are load-bearing. Production estimates must retain the
complete finite kernel or the exact square form (T-15412.13).

## 10. Relation to the repo-wide global attack

The strongest global coordinates now read

```text
square interval Weil ray:
    Psi(2 log Y),

dyadic Chebyshev square function:
    integral |psi(t)/t-psi(t/4)/(t/4)|^2 dt,

compact-window finite prime-pair energy:
    integral |Q_G(x)|^2 dx,

Hausdorff/Stieltjes hierarchy:
    H_(m,k)(R).
```

Subject to independent review of their normalization bridges, all have the same
rightmost-zero exponent or the same complete positivity content. The present
coordinate is the most elementary on the prime side: one Chebyshev prefix, one
dyadic rescaling, and one ordinary integral.

A direct full-problem attack can now target

\[
 \boxed{
 \int_1^Y|C(t)-C(t/4)|^2dt=Y^{o(1)}}
 \tag{T-15412.36}
\]

through Selberg's exact coefficient identity, multiplicative dispersion, the
bounded-ratio kernel (T-15412.35), or a scale-recursive energy inequality. No
finite positive ladder can substitute for this cofinal estimate.

## 11. Proof boundary

Closed here:

- the exact raw-prime formula;
- the zero-free dyadic filter geometry;
- the dyadic square-function identity;
- equality of its weighted-Hardy and cumulative exponents with
  `Theta_zeta`;
- stable equivalence with the classical Chebyshev mean square;
- the anti-causal renewal identity;
- the compact-ratio full autocorrelation formula.

Open:

\[
 \mathcal E_\diamond(Y)=Y^{o(1)}.
\]

That estimate is a full RH-strength arithmetic theorem. This claim does not
assert it, and no RH resolution is claimed.
