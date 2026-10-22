# L-19842 — Complete holomorphic Bessel/fold/endpoint/alias theorem

Claim ID: `L-19842`  
Status: **PROPOSED COMPLETE ANALYTIC THEOREM FOR THE GROWING LOW PROLATE PACKET**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-07  
Dependencies: the exact radial spheroidal equation and normalization of `L-16217/L-16222/L-16229`; the uniform point-value window of `L-16219`; no RH assumption  
Scope: theorem 3 in the repaired prolate programme; includes the shrinking complex strip, one support derivative, the cubic endpoint fold, collective endpoint summation, and all Poisson aliases

## 1. Statement

Put

\[
 R=2\pi\lambda^2,
 \qquad
 L=\log R,
 \qquad
 m_R\le C_0L^2.
 \tag{L-19842.1}
\]

Let `Phi_(n,R)(z)` be the exactly normalized radial leakage profile for the even
prolate mode `n`, with

\[
 0\le n\le m_R,
 \qquad n\ \text{even},
 \tag{L-19842.2}
\]

and with both Fourier-sign sectors retained. Let `F_R` denote first-alias
synthesis and `H_R` the sum of every alias `k>=2`, including its endpoint
channels, in first-alias-normalized coordinates.

There is a set `mathcal A_R` of admissible supports in every sufficiently large
dyadic radial block such that

\[
 \frac{|\mathcal A_R|}{R}\longrightarrow1
 \tag{L-19842.3}
\]

and, at every selected support in `mathcal A_R`, the following hold.

### Holomorphic branch theorem

For

\[
 z=x+i\eta/R,
 \qquad |\eta|\le1/2,
 \tag{L-19842.4}
\]

the profile has a fixed finite branch decomposition away from the endpoint
fold,

\[
 \Phi_{n,R}(z)
 =\sum_{\sigma=\pm}
 a_{n,\sigma,R}(z)e^{i\sigma R\xi(z)}
 +\mathcal E_{n,R}(z),
 \tag{L-19842.5}
\]

where

\[
 \xi(z)=\sqrt{z^2-1}-\arccos(1/z),
 \qquad
 \xi'(z)=\frac{\sqrt{z^2-1}}{z},
 \tag{L-19842.6}
\]

with the branch fixed by positivity for real `z>1`. Uniformly on compact radial
ratio bands and throughout (L-19842.4),

\[
 \boxed{
 |a|+|\partial_za|+R|\partial_Ra|
 \le L^C,}
 \tag{L-19842.7}
\]

and

\[
 \boxed{
 |\mathcal E|+R|\partial_R\mathcal E|
 \le L^C R^{-1}.}
 \tag{L-19842.8}
\]

At `z=1` the two branches are replaced by one uniform Bessel fold profile; after
its cubic change of variable it obeys the same bounds with the ordinary
`R^{-1/3}` endpoint scale.

### Complete alias estimates

The normalized first/rest Hermitian cross satisfies

\[
 \boxed{
 \|F_R^*H_R+H_R^*F_R\|
 \le
 L^C e^{CL^{1/3}}R^{-1/3}
 =o(1).}
 \tag{L-19842.9}
\]

The complete synthesis, including endpoint self-energy, satisfies

\[
 \boxed{
 \|F_R+H_R\|+
 R\|\partial_R(F_R+H_R)\|
 \le L^Ce^{CL^{1/3}}
 =R^{o(1)}.}
 \tag{L-19842.10}
\]

The infinite non-endpoint alias ledger is absolutely summable after one
nonstationary integration:

\[
 \boxed{
 \|\mathcal C_{n,m,k}(R)\|
 +R\|\partial_R\mathcal C_{n,m,k}(R)\|
 \le L^CR^{-1/3}k^{-2},
 \qquad k\ge2.}
 \tag{L-19842.11}
\]

The leading endpoint `1/k` channel is not summed absolutely. It is summed first,
exactly, as a logarithm/sawtooth. Its self-energy is retained; its cross with
the first alias is contained in (L-19842.9).

These estimates are dimension-uniform for `m_R=O(L^2)`: all packet losses are
polynomial in `L`, and are defeated by `R^{-1/3}`.

## 2. Exact radial Volterra equation

After the Liouville transform in `L-16229`, the normalized radial equation can
be written

\[
 \mathcal L_RY=V_{n,R}(z)Y,
 \tag{L-19842.12}
\]

where `mathcal L_R` is the order-zero Bessel comparison operator associated to
`xi` and

\[
 \sup_{n\le C_0L^2}
 \left(
 |V_{n,R}(z)|+|\partial_zV_{n,R}(z)|
 +R|\partial_RV_{n,R}(z)|
 \right)
 \le CL^C/R
 \tag{L-19842.13}
\]

on every fixed complex neighborhood of a compact radial band. The reason is
that the angular eigenvalue enters only through

\[
 \sigma_{n,R}=O((n+1)/R)=O(L^2/R),
 \tag{L-19842.14}
\]

and the exact point-value normalization removes the exponentially small
unscaled leakage.

Let `B_R(z)` be the normalized comparison solution

\[
 B_R(z)
 =\sqrt{2R}\,A(z)\xi(z)^{1/2}J_0(R\xi(z)),
 \tag{L-19842.15}
\]

with the analytic prefactor `A` fixed by the exact radial Wronskian. Variation
of parameters gives the exact Volterra equation

\[
 \Phi_{n,R}(z)
 =B_R(z)
 +\int_1^zG_R(z,w)V_{n,R}(w)\Phi_{n,R}(w)\,dw.
 \tag{L-19842.16}
\]

The Bessel Green kernel satisfies, in the standard weighted norm,

\[
 \sup_z\int_1^z|G_R(z,w)|\,|dw|\le C
 \tag{L-19842.17}
\]

and after one `z` or scaled `R` derivative the bound is polynomial in the fixed
endpoint weight. Equations (L-19842.13), (L-19842.16), and Gronwall therefore
give

\[
 \Phi_{n,R}=B_R+O(L^C/R)
 \tag{L-19842.18}
\]

with one `z` derivative and one scaled support derivative. The same contour
proof works for `|Im z|<=1/(2R)` because that strip remains inside the fixed
analytic neighborhood and its contour length changes by `O(1/R)`.

This is the missing complex-strip argument: it is a Volterra estimate for the
exact analytic ODE, not an extrapolation of a real-axis error bar.

## 3. Horizontal displacement after phase extraction

For `z=x+i eta/R`, analytic Taylor expansion gives

\[
 R\xi(x+i\eta/R)
 =R\xi(x)+i\eta\xi'(x)+O(R^{-1}),
 \tag{L-19842.19}
\]

uniformly away from the endpoint. Hence

\[
 e^{i\sigma R\xi(x+i\eta/R)}
 =e^{i\sigma R\xi(x)}
  e^{-\sigma\eta\xi'(x)}
  [1+O(R^{-1})].
 \tag{L-19842.20}
\]

Because `xi'` is bounded on every compact radial band, horizontal zero
displacement changes only the amplitude by a bounded factor. At the endpoint,
`xi'(1)=0`, so the same assertion is easier. This proves the branchwise
translation-free support adapter of `L-19822` and confirms the reviewer's exact
cancellation objection to `L-19821`.

Differentiating after phase extraction gives

\[
 |A_\rho(R)|+R|A_\rho'(R)|\le L^C,
 \tag{L-19842.21}
\]

which is the actual hypothesis of the Hilbert-valued support large sieve.

## 4. The endpoint fold

Near `z=1`,

\[
 \xi(z)=\frac{2\sqrt2}{3}(z-1)^{3/2}
 [1+O(z-1)].
 \tag{L-19842.22}
\]

Put

\[
 u=R^{2/3}(z-1).
 \tag{L-19842.23}
\]

The exact Bessel comparison solution and its first derivative are bounded by a
fixed linear combination of the canonical cubic-fold functions on every
bounded `u`-window. Outside that window the two Hankel branches of
`J_0(Rxi)` apply. Splitting at `|u|=L^B` and integrating the bounded fold window
directly gives

\[
 \left|\int_{|z-1|\le L^BR^{-2/3}}
 b_R(z)e^{iR\varphi_R(z)}\,dz\right|
 \le L^CR^{-1/3},
 \tag{L-19842.24}
\]

with one scaled support derivative. On the complement, ordinary integration by
parts gives the stronger `O(L^C/R)` estimate. Thus the complete transition,
including a fold that lands on the endpoint, costs at most `L^CR^{-1/3}`.

No unproved real-variable Airy continuation is used: (L-19842.24) follows from
the exact Bessel comparison and the cubic coordinate (L-19842.23).

## 5. Nonstationary alias separation

For `k>=2`, every cross phase between the first radial branch and the `k`th
radial branch is, up to signs,

\[
 \varphi_{\sigma,\tau,k}(v)
 =\sigma\xi(v)+\tau\xi(kv).
 \tag{L-19842.25}
\]

If the signs agree, the derivative never vanishes. If they disagree, then for
`v>=1`,

\[
 k\xi'(kv)-\xi'(v)
 =\frac{\sqrt{k^2v^2-1}-\sqrt{v^2-1}}{v}
 \ge c(k-1).
 \tag{L-19842.26}
\]

Thus there is no hidden interior stationary point in a first-versus-later
radial cross. The only degeneration is the first-branch endpoint fold already
treated in Section 4.

The normalized radial amplitude has the far-field bound

\[
 |a_{n,\sigma,R}(kv)|
 +|\partial_v a_{n,\sigma,R}(kv)|
 \le \frac{L^C}{k(1+v)}.
 \tag{L-19842.27}
\]

One integration by parts using (L-19842.26) therefore supplies a second factor
`1/k`:

\[
 \left|
 \int_1^\infty
 a_{j,\sigma,R}(v)
 \overline{a_{n,\tau,R}(kv)}
 e^{iR\varphi_{\sigma,\tau,k}(v)}\,dv
 \right|
 \le L^CR^{-1}k^{-2},
 \tag{L-19842.28}
\]

away from the endpoint window. Adding (L-19842.24) gives (L-19842.11). The
scaled `R` derivative is identical after the real phase is extracted: it falls
on amplitudes satisfying (L-19842.7), while differentiation of the extracted
phase is not charged to the amplitude.

The series `sum_(k>=2) k^-2` closes the complete stationary/fold alias ledger.

## 6. Endpoint jet decomposition and collective summation

For a compact-BV source with endpoint jets, repeated integration by parts gives,
uniformly in the growing low packet,

\[
 r_n(kv)
 =\sum_{j=0}^{p-1}
 \frac{c_{n,j}(v)e^{ik\vartheta_R(v)}}{k^{j+1}}
 +R_{n,k,p}(v),
 \tag{L-19842.29}
\]

where

\[
 \sum_{k\ge2}
 \left(
 \|R_{n,k,p}\|+
 R\|\partial_RR_{n,k,p}\|
 \right)
 \le L^C
 \tag{L-19842.30}
\]

for fixed `p>=3`. For `j>=1`, the explicit channels are absolutely summable.
For `j=0`, sum before taking a norm:

\[
 \sum_{k\ge2}\frac{e^{ik\vartheta}}k
 =-\log(1-e^{i\vartheta})-e^{i\vartheta}.
 \tag{L-19842.31}
\]

The logarithm belongs locally to `L2` across a resonance. Its support derivative
is

\[
 \partial_R\log(1-e^{i\vartheta_R})
 =-
 \frac{i\vartheta_R'e^{i\vartheta_R}}
      {1-e^{i\vartheta_R}}.
 \tag{L-19842.32}
\]

Delete supports on which any of the polynomially many endpoint phases lies
within

\[
 e^{-L^{1/3}}
 \tag{L-19842.33}
\]

of an integer multiple of `2pi`. The deleted relative measure is
`e^{-L^{1/3}+O(log L)}=o(1)`. On the remainder,

\[
 \left|\log(1-e^{i\vartheta_R})\right|
 +R\left|\partial_R\log(1-e^{i\vartheta_R})\right|
 \le L^Ce^{L^{1/3}}
 =R^{o(1)}.
 \tag{L-19842.34}
\]

This proves the complete upper bound (L-19842.10). It also identifies precisely
why the old claim `sum ||r_n(k dot)||<infinity` was false: the leading endpoint
channel is conditional, but its exact aggregate is harmless at the
subpolynomial scale.

## 7. First/rest cross moat

Expand the Hilbert--Schmidt square of the first/rest cross over modes and
branches. There are `O(L^C)` finite branch, reflected, fold, and endpoint
families. Equations (L-19842.24), (L-19842.28), and (L-19842.30) give, after the
collective `j=0` sum,

\[
 \frac1R\int_R^{2R}
 \|F_s^*H_s+H_s^*F_s\|_{HS}^2\,ds
 \le L^Ce^{CL^{1/3}}R^{-2/3}.
 \tag{L-19842.35}
\]

The `O(L^2)` packet dimension is already included. Markov's inequality with
threshold

\[
 L^Ce^{CL^{1/3}}R^{-1/3}
 \tag{L-19842.36}
\]

removes another `o(1)` support fraction. On the remaining set, operator norm is
bounded by Hilbert--Schmidt norm, proving (L-19842.9).

Intersecting this set with the endpoint nonresonance set and the zeta
nonresonance set of `L-19840` still leaves relative measure tending to one.

## 8. Proof boundary and adversarial checks

1. The shrinking complex strip is proved from the exact analytic Volterra
   equation, not inferred from a real-axis citation.
2. The support derivative is always measured **after** extracting the real
   oscillatory phase; this is why the required factor `R` is present in
   (L-19842.21).
3. The endpoint fold is handled in its `R^{-2/3}` cubic window and contributes
   `R^{-1/3}`. It is not silently treated by nondegenerate stationary phase.
4. Every `k>=2` channel gets an explicit `k^-2` bound. The first `1/k` endpoint
   jet is summed collectively as (L-19842.31), never absolutely.
5. The positive rest/rest Gram is retained. Only the first/rest cross is made
   small.
6. The theorem is uniform only for the declared low packet
   `n=O(log^2 R)`. It does not claim a uniform theorem through the full prolate
   Shannon transition.
7. Equations (L-19842.13), (L-19842.17), and (L-19842.27) are direct consequences
   of the exact radial equation, Wronskian normalization, and point-value window
   cited in the dependencies. A reviewer should audit those three substitutions
   first; no numerical checker can replace them.
8. No RH conclusion is claimed by this theorem alone.
