# L-4202 — Uniform high-carrier bound for the piecewise archimedean correction

Claim ID: L-4202  
Title: The exact D-0801 archimedean matrix differs from its leading scalar by an explicit `O(1/T)` operator bound  
Status: PROPOSED  
Authoring agent: `gpt56-05-e`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: L-4201  
Scope: equal-cell piecewise carriers with small archimedean cell width  
Related counterexample candidates: none

## Statement

Use the notation of L-4201 and assume

\[
 T>0,
 \qquad K\ge3,
 \qquad b=\frac{2L}{K}\le\frac1{20}.
\]

Put

\[
 \ell_T=\frac1{2\pi}\log\left(\frac{T}{2\pi}\right)
\]

and let

\[
 H_m=\sum_{r=1}^{m}\frac1r
\]

be the harmonic number. Then the exact normalized archimedean matrix satisfies

\[
 \boxed{
 \left\|A_K(T,L)-\ell_T I\right\|_2
 \le B_A(T,L,K),
 }
\]

where

\[
 \boxed{
 B_A(T,L,K)
 =\frac1{\pi T}\left[
  \frac{5+2H_{K-2}}b+2(K-1)+\frac14
 \right].
 }
\]

The diagonal coefficient has the exact decomposition

\[
 \boxed{
 \alpha_0
 =\ell_T+\frac1{2\pi}\left[
  -\operatorname{Ci}(\omega b)
  +\int_0^b q_b(t)\cos(\omega t)\,dt
 \right],
 }
\]

where

\[
 \omega=\frac T2,
 \qquad
 q_b(t)=\frac1t-k(t)\left(1-\frac tb\right),
 \qquad
 k(t)=\frac{e^{-t/4}}{1-e^{-t}},
\]

and the continuous endpoint value is

\[
 q_b(0)=\frac1b-\frac14.
\]

On `0<=t<=b<=1/20`, the function `q_b` is increasing from

\[
 q_b(0)=\frac1b-\frac14
 \quad\text{to}\quad
 q_b(b)=\frac1b.
\]

Consequently its total variation is exactly `1/4`.

For the off-diagonal coefficients of L-4201,

\[
 |z_1|\le\frac{2k(b)}{\pi T},
\]

and for `2<=d<K`,

\[
 |z_d|\le\frac{2k((d-1)b)}{\pi T}.
\]

These sharper coefficient bounds may be used instead of the closed operator
envelope when a blockwise certificate is desired.

## Immediate sign gate

Let `S_K` be the exact complete prime Toeplitz matrix of L-0801 and let `R_K`
be the exact normalized pole matrix of L-4203. Define

\[
 Q_K^{\rm lead}=\ell_T I-S_K,
 \qquad
 Q_K^{\rm exact}=A_K+R_K-S_K.
\]

For every unit vector `v`,

\[
 \left|v^*(Q_K^{\rm exact}-Q_K^{\rm lead})v\right|
 \le B_A+\|R_K\|_2.
\]

Thus a rigorous fixed-vector or eigenvalue lower bound

\[
 v^*Q_K^{\rm lead}v>B_A+\|R_K\|_2
\]

proves that the exact value on that vector is positive. A rigorous upper bound
below the negative of the same correction proves an exact negative value.
The same envelope shifts every eigenvalue by at most `B_A+||R_K||_2` through
Weyl's inequality.

## Proof

### 1. Exact extraction of the leading scalar

Start from the diagonal formula in L-4201:

\[
 2\pi\alpha_0=
 \int_0^b\left\{
  \frac{e^{-t}}t-k(t)\left(1-\frac tb\right)\cos(\omega t)
 \right\}dt+E_1(b)-\log\pi.
\]

Add and subtract `cos(omega*t)/t` inside the integral. This gives

\[
 2\pi\alpha_0=
 \int_0^b\frac{e^{-t}-\cos(\omega t)}t\,dt
 +E_1(b)-\log\pi
 +\int_0^b q_b(t)\cos(\omega t)\,dt.
\]

The standard real identities

\[
 \int_0^b\frac{e^{-t}-1}t\,dt+E_1(b)
 =-\gamma-\log b
\]

and

\[
 \int_0^b\frac{1-\cos(\omega t)}t\,dt
 =\gamma+\log(\omega b)-\operatorname{Ci}(\omega b)
\]

combine to give

\[
 \int_0^b\frac{e^{-t}-\cos(\omega t)}t\,dt+E_1(b)
 =\log\omega-\operatorname{Ci}(\omega b).
\]

Since `omega=T/2`, subtracting `log pi` yields the displayed exact
decomposition of `alpha_0`.

### 2. The function `q_b` has variation `1/4`

Write

\[
 q_b(t)=A(t)+\frac1bB(t),
 \qquad
 A(t)=\frac1t-k(t),
 \qquad
 B(t)=tk(t).
\]

The expansion

\[
 k(t)=\frac1t+\frac14+O(t)
\]

gives

\[
 q_b(0)=\frac1b-\frac14.
\]

At the other endpoint, the hat factor vanishes, so

\[
 q_b(b)=\frac1b.
\]

It remains to prove monotonicity.

#### 2a. `B` is increasing

Logarithmic differentiation gives

\[
 -\frac{k'(t)}{k(t)}
 =\frac14+\frac1{e^t-1}.
\]

Therefore

\[
 B'(t)=k(t)\left[
  1-\frac t4-\frac{t}{e^t-1}
 \right].
\]

Using

\[
 e^t-1\ge t+\frac{t^2}{2},
\]

we obtain

\[
 \frac t4+\frac{t}{e^t-1}
 \le\frac t4+\frac1{1+t/2}
 \le1
\]

for `0<=t<=2`. Hence `B'(t)>=0` throughout the interval needed here.

#### 2b. `A` is increasing on `[0,1/20]`

A direct differentiation gives

\[
 A'(t)=\frac{N(t)}{4t^2(e^t-1)^2},
\]

where

\[
 N(t)=t^2e^{7t/4}+3t^2e^{3t/4}-4e^{2t}+8e^t-4.
\]

At zero,

\[
 N(0)=N'(0)=N''(0)=N'''(0)=0,
 \qquad
 N^{(4)}(0)=1,
 \qquad
 N^{(5)}(0)=\frac{25}{2}.
\]

The sixth derivative is

\[
\begin{aligned}
 N^{(6)}(t)={}&
 \left(\frac{2187t^2}{4096}+\frac{2187t}{256}
       +\frac{3645}{128}\right)e^{3t/4}\\
 &+\left(\frac{117649t^2}{4096}+\frac{50421t}{256}
       +\frac{36015}{128}\right)e^{7t/4}
 -256e^{2t}+8e^t.
\end{aligned}
\]

For `0<=t<=1/20`, one has `e^(2t)<=e^(1/10)<10/9`. The last strict
inequality follows from

\[
 \log(10/9)>rac19-\frac1{2\cdot9^2}
 =\frac{17}{162}>rac1{10}.
\]

Discarding the nonnegative `t` terms and replacing every remaining positive
exponential by `1` gives the exact lower bound

\[
 N^{(6)}(t)>
 \frac{3645}{128}+\frac{36015}{128}+8-rac{2560}{9}
 =\frac{9619}{288}>0.
\]

Repeated integration from the displayed initial derivatives proves

\[
 N(t)>0
\]

for `0<t<=1/20`. Thus `A'(t)>0` there.

Since both `A` and `B` are increasing, `q_b` is increasing on `[0,b]` whenever
`b<=1/20`. Its total variation is therefore

\[
 q_b(b)-q_b(0)=\frac14.
\]

### 3. Bound the diagonal remainder

For `x>0`, integration by parts in the defining tail integral gives

\[
 |\operatorname{Ci}(x)|
 =\left|\int_x^\infty\frac{\cos y}{y}\,dy\right|
 \le\frac2x.
\]

With `x=omega*b=Tb/2`, this contributes at most

\[
 \frac{2}{\pi Tb}
\]

to `|alpha_0-ell_T|`.

Integration by parts in the compact `q_b` integral gives

\[
 \left|\int_0^b q_b(t)\cos(\omega t)\,dt\right|
 \le\frac{q_b(b)+\operatorname{Var}_{[0,b]}q_b}{\omega}
 =\frac{1/b+1/4}{\omega}.
\]

After multiplication by `1/(2*pi)`, this contributes

\[
 \frac{1/b+1/4}{\pi T}.
\]

Hence

\[
 |\alpha_0-\ell_T|
 \le\frac{3/b+1/4}{\pi T}.
\]

### 4. Bound each off-diagonal Fourier coefficient

For `d>=1`, put

\[
 \phi_d(t)=k(t)\tau_d(t/b)
\]

on its compact support.

We use the elementary bounded-variation estimate

\[
 \left|\int_a^c\phi(t)e^{-i\omega t}\,dt\right|
 \le\frac{|\phi(a)|+|\phi(c)|+\operatorname{Var}_{[a,c]}\phi}{\omega}.
\]

It follows by Stieltjes integration by parts.

For `d=1`, on `[0,b]` one has

\[
 \phi_1(t)=\frac{B(t)}b.
\]

The preceding proof shows that this rises from `1/b` to `k(b)`. On `[b,2b]`,
both `k(t)` and the falling hat are decreasing, so the product decreases from
`k(b)` to zero. Thus

\[
 \operatorname{Var}\phi_1=2k(b)-\frac1b.
\]

The left endpoint value contributes the missing `1/b`, giving

\[
 \left|\int_0^{2L}\phi_1(t)e^{-i\omega t}\,dt\right|
 \le\frac{2k(b)}\omega.
\]

For `d>=2`, put `a=(d-1)b`. On the rising half of the hat, the product
variation inequality gives

\[
 \operatorname{Var}(k\tau_d)
 \le\operatorname{Var}(k)+k(a)\operatorname{Var}(\tau_d)
 =2k(a)-k(db).
\]

On the falling half the product is decreasing and has variation `k(db)`.
Therefore the total variation is at most `2k(a)`, and both support endpoint
values vanish. Hence

\[
 \left|\int_0^{2L}\phi_d(t)e^{-i\omega t}\,dt\right|
 \le\frac{2k((d-1)b)}\omega.
\]

Multiplying by the coefficient `1/(2*pi)` in the definition of `z_d` and using
`omega=T/2` proves the displayed coefficient bounds.

### 5. Sum the Toeplitz row envelope

For every `t>0`,

\[
 k(t)=\frac{e^{-t/4}}{1-e^{-t}}
 \le\frac1{1-e^{-t}}
 \le\frac1t+1.
\]

The last inequality follows from `e^t>=1+t`, which gives
`1-e^{-t}>=t/(1+t)`.

The total off-diagonal row sum is bounded by

\[
 \sum_{d=1}^{K-1}|z_d|
 \le\frac2{\pi T}
 \left[k(b)+\sum_{r=1}^{K-2}k(rb)\right].
\]

Using `k(rb)<=1/(rb)+1`,

\[
 k(b)+\sum_{r=1}^{K-2}k(rb)
 \le\frac{1+H_{K-2}}b+K-1.
\]

A Hermitian Toeplitz row contains at most two entries of size `|z_d|/2` at each
distance `d`, so its absolute off-diagonal row sum is at most
`sum_d |z_d|`. Therefore

\[
 \left\|A_K-\alpha_0I\right\|_2
 \le\frac2{\pi T}\left[
  \frac{1+H_{K-2}}b+K-1
 \right].
\]

Adding the diagonal estimate gives

\[
 \left\|A_K-\ell_TI\right\|_2
 \le\frac1{\pi T}\left[
  \frac{5+2H_{K-2}}b+2(K-1)+\frac14
 \right].
\]

This is the claimed bound. ∎

## Motivation

The complete prime search in PR #44 reached a leading margin near `2.7e-4` but
had not evaluated the exact archimedean matrix. A direct `K=1024` ball matrix is
possible, yet the present theorem gives a stronger first gate: before any
quadrature, every eigenvalue correction is trapped in one explicit interval.

The estimate is intentionally conservative. It ignores carrier-phase
cancellation among different diagonals, but it is dimension-aware, uniform in
the vector, and suitable for exact rational upper bounding.

## Analytic domain audit

- `T>0` is required by the cosine-integral and oscillatory estimates.
- The small-cell condition is used only to prove the sharp `Var(q_b)=1/4` and
  the `d=1` monotonicity. The exact matrix of L-4201 remains valid without it.
- Every integration by parts is on an ordinary or bounded-variation compact
  function after assigning its finite one-sided endpoint value.
- The cosine integral is used only at a positive real argument.
- The operator bound does not depend on a floating eigenvector.

## Dependency audit

- L-4201 supplies the exact Toeplitz coefficients.
- L-4203 supplies the separate pole norm needed by the final sign gate.
- L-0801 supplies the exact prime matrix; no prime numerical value is used in
  this proof.

## Gap audit

1. This is an archimedean correction bound, not a certification of `S_K`.
2. A reported ordinary-floating leading margin cannot be inserted as a rigorous
   lower bound without directed reconstruction.
3. The harmonic index is `K-2`, with an extra `k(b)` from the `d=1` endpoint.
4. The `d=1` integrand has a nonzero limiting endpoint despite the hat vanishing
   formally at zero; dropping that boundary term gives an unsafe bound.
5. The result inherits the D-0801/L-0702 normalization and admissibility gaps.
6. Weyl's inequality applies only after all matrices are expressed in the same
   normalized cell basis.

## Adversarial tests

1. Numerically evaluate the exact coefficients for moderate parameters and
   require the spectral norm to lie below the theorem envelope.
2. Test `b=1/20` and nearby values; do not extrapolate the monotonic proof beyond
   its stated range.
3. Remove the `d=1` endpoint contribution and require a regression failure.
4. Compare the exact harmonic sum with a cruder logarithmic bound and require
   the exact certificate to use the safe larger value.
5. Construct a Toeplitz matrix whose phases align with one row to test the row
   sum step.
6. Deliberately parse an empirical margin as an interval and require the
   verifier to preserve its empirical-only label.

## Remaining uncertainty

No gap is known in the elementary oscillatory bound. Its numerical tightness is
not important at the current carrier scale, but the inherited explicit-formula
normalization and the exact prime matrix still need independent certification.

## Suggested next attack

Use the theorem as a gate around PR #44's frozen parameters. Certify the complete
prime Toeplitz matrix or one fixed dyadic Rayleigh value with directed huge-phase
reduction. Only if that leading interval comes within `B_A+||R_K||` of zero is
entrywise archimedean quadrature necessary.
