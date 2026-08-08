# L-28004 — Critical binary–ternary compact Riesz source

Claim ID: `L-28004`  
Title: Ordinary and half-pole Euler differences at two and three turn the complete reciprocal-zeta Riesz signal into one compact physical window with positive inverse data and a finite carry transition  
Status: **PROPOSED COMPLETE EXACT ADAPTER PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: elementary Dirichlet convolution, Laplace transforms, and `L-28002`

## 1. Critical source

Define the real algebraic Dirichlet-convolution source

\[
\boxed{
\sigma_{2,3}
=\mu
*(\varepsilon-\delta_2)
*(\varepsilon-\sqrt2\,\delta_2)
*(\varepsilon-\delta_3)
*(\varepsilon-\sqrt3\,\delta_3).}
\tag{L-28004.1}
\]

Its Dirichlet series is

\[
\boxed{
\Sigma_{2,3}(s)
=
\frac{
(1-2^{-s})(1-2^{1/2-s})
(1-3^{-s})(1-3^{1/2-s})
}{\zeta(s)}.}
\tag{L-28004.2}
\]

The ordinary Euler factors will make the carry image finite.  The two half-pole
factors vanish at `s=1/2` and cancel the complete logarithmic Riesz denominator.
No factor can cancel a zeta zero in the open critical strip.

## 2. Positive inverse and generalized primes

Let `A_sigma=Sigma_(2,3)^(-1)`.  At `p=2`, its local series is

\[
\frac1{(1-x)^2(1-\sqrt2x)},
\]

and at `p=3` it is

\[
\frac1{(1-y)^2(1-\sqrt3y)}.
\]

Thus, for `r>=0`, put

\[
\alpha_p(r)
=\sum_{j=0}^{r}(r-j+1)p^{j/2}>0.
\tag{L-28004.3}
\]

If `n=2^a3^bm` with `(m,6)=1`, the inverse coefficient is

\[
\boxed{
a_\sigma(n)=\alpha_2(a)\alpha_3(b)>0.}
\tag{L-28004.4}
\]

Logarithmic differentiation gives the generalized von Mangoldt sequence

\[
\boxed{
\Lambda_\sigma(q)=
\begin{cases}
(2+2^{r/2})\log2,&q=2^r,\\
(2+3^{r/2})\log3,&q=3^r,\\
\log p,&q=p^r,\ p\ne2,3,\\
0,&q\text{ not a prime power}.
\end{cases}}
\tag{L-28004.5}
\]

Every coefficient is nonnegative.  The generalized Selberg identity is exactly

\[
\boxed{
\sigma_{2,3}*(a_\sigma\log^2)
=\Lambda_\sigma\log
+\Lambda_\sigma*\Lambda_\sigma.}
\tag{L-28004.6}
\]

## 3. Compact physical Riesz window

Put

\[
a=\log2,
\qquad b=\log3,
\]

and define the positive box convolution

\[
B_{a,b}=\mathbf1_{[0,a]}*\mathbf1_{[0,b]}.
\tag{L-28004.7}
\]

Its Laplace transform is

\[
\widehat B_{a,b}(z)
=\frac{(1-e^{-az})(1-e^{-bz})}{z^2}.
\tag{L-28004.8}
\]

Define the ordinary weighted-difference operator

\[
\mathcal D_{a,b}
=(I-2^{-1/2}\tau_a)(I-3^{-1/2}\tau_b)
\tag{L-28004.9}
\]

and the compact real window

\[
\boxed{H_{2,3}=\mathcal D_{a,b}B_{a,b}.}
\tag{L-28004.10}
\]

It is supported on

\[
[0,2a+2b]=[0,\log36].
\]

Let

\[
\alpha_\mu
=\sum_{n\ge1}\frac{\mu(n)}{\sqrt n}\delta_{\log n}.
\]

Then the complete critical Riesz signal

\[
\mathcal R_\sigma(T)
=\sum_{n\le e^T}
\frac{\sigma_{2,3}(n)}{\sqrt n}(T-\log n)
\tag{L-28004.11}
\]

has the exact physical representation

\[
\boxed{
\mathcal R_\sigma
=H_{2,3}*\alpha_\mu.}
\tag{L-28004.12}
\]

Indeed, at `s=z+1/2`, the two critical factors in (L-28004.2) are
`1-e^{-az}` and `1-e^{-bz}` and produce (L-28004.8); the two ordinary factors
produce (L-28004.9).

Thus the reciprocal-zeta Riesz signal is no longer represented by a growing
stop-loss kernel.  It is one fixed compact physical window.

The transform of `H_(2,3)` has no zero in `Re z>0`.  The critical factors can
vanish only on `Re z=0`; the ordinary factors have modulus strictly less than
one there after a positive real shift.  Hence every hypothetical zero of zeta
with real part greater than `1/2` remains an uncancelled pole.

## 4. Finite carry image

Convolution with the constant-one sequence cancels `mu`, so

\[
\mathbf1*\sigma_{2,3}
=(\varepsilon-\delta_2)
*(\varepsilon-\sqrt2\delta_2)
*(\varepsilon-\delta_3)
*(\varepsilon-\sqrt3\delta_3).
\tag{L-28004.13}
\]

This finite sequence is supported on divisors of `36`.  Let its coefficients be
`q_(2,3)(d)` and put

\[
G_{2,3}(x)
=\sum_{d\mid36}q_{2,3}(d)\mathbf1_{x\ge d}.
\tag{L-28004.14}
\]

Because the ordinary factors vanish at the coefficient sum point,

\[
G_{2,3}(x)=0
\qquad(x\ge36).
\tag{L-28004.15}
\]

At scale `m`, the pointwise carry wavelet is exactly

\[
\boxed{
Z^\sigma_{n,m}(j)
=G_{2,3}(n/m)
-G_{2,3}(j/m)
-G_{2,3}((n-j)/m).}
\tag{L-28004.16}
\]

For the declared binary and ternary splits, every parent and child lies beyond
`36m` once

\[
n\ge108m-2.
\]

Therefore

\[
\boxed{
\overline Z^\sigma_{n,m}=0
\qquad(n\ge108m-2).}
\tag{L-28004.17}
\]

The complete critical physical source has only one finite factor-108 carry
transition band.

## 5. Stable return to the binary–ternary and dyadic sources

The critical source factors as

\[
\boxed{
\sigma_{2,3}
=\omega_{2,3}
*(\varepsilon-\sqrt2\delta_2)
*(\varepsilon-\sqrt3\delta_3).}
\tag{L-28004.18}
\]

For complete Riesz signals, the normalization cancels the square-root
coefficients and gives

\[
\boxed{
\mathcal R_\sigma(T)
=\mathcal R_{2,3}(T)
-\mathcal R_{2,3}(T-a)
-\mathcal R_{2,3}(T-b)
+\mathcal R_{2,3}(T-a-b).}
\tag{L-28004.19}
\]

On every finite horizon the inverse is the finite double prefix sum

\[
\boxed{
\mathcal R_{2,3}(T)
=\sum_{i,j\ge0\atop ia+jb\le T}
\mathcal R_\sigma(T-ia-jb),}
\tag{L-28004.20}
\]

up to the explicitly checked bounded initial interval.  The number of summands
is `O(T^2)`, so subexponential pointwise or block-energy bounds transfer from
`R_sigma` to `R_(2,3)`.

Finally,

\[
\omega_{2,3}=b_2*(\varepsilon-\delta_3)
\]

gives the exponentially stable inverse from `R_(2,3)` to the dyadic source.
Hence a subexponential bound for the compact signal (L-28004.12) implies the
dyadic shell/Riesz bound and RH.

## 6. Physical proof target

The source-specific physical theorem may now be stated directly:

\[
\boxed{
\int_0^T|\mathcal R_\sigma(t)|^2dt=e^{o(T)}.}
\tag{L-28004.21}
\]

By (L-28004.12), this is a fixed compact-window reciprocal-zeta energy.  By
(L-28004.17), its binary–ternary carry source has only a finite transition band.
By (L-28004.6), the associated generalized-prime forcing is nonnegative.

A proof still requires the correct independent-frequency source map and strict
physical reserve.  The exact adapter removes growing kernels, infinite
inversion, and uncontrolled far carry rows from that theorem.

## 7. Proof boundary

Closed exactly or elementarily:

1. critical source and positive inverse;
2. nonnegative generalized-prime weights;
3. compact physical Riesz window;
4. absence of right-half-plane multiplier zeros;
5. finite factor-108 carry localization;
6. polynomially stable return to `omega_(2,3)` and `b_2`.

Open:

1. the subexponential compact-window energy (L-28004.21);
2. the physical source-image transition theorem proving it;
3. RH.
