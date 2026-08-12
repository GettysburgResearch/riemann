# L-91020 — The Cauchy-square gate has an all-order positive dyadic storage hierarchy

Claim ID: `L-91020`  
Status: **EXACT POSITIVE-KERNEL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91012`, elementary Laplace calculus  
RH status: **unproved**

## 1. The dimensionless dyadic gate

For `a>0` put

\[
 n_a(u)=\frac{a^4}{(a^2+u^2)^2}.
\]

The critical-line kernel of the dyadic gate is

\[
 D_a^{(0)}(u)=n_{2a}(u)-n_a(u).
\]

With

\[
 y=\frac{u^2}{a^2},
\]

this is the scale-free function

\[
 \boxed{
 F_0(y)=\frac{16}{(y+4)^2}-\frac1{(y+1)^2}.
 }
 \tag{L-91020.1}
\]

Define recursively, for `m>=0`,

\[
 \boxed{
 F_{m+1}(y)
 =F_m(y)-4^{-(m+2)}F_m(y/4).
 }
 \tag{L-91020.2}
\]

Equivalently,

\[
 D_a^{(m+1)}(u)
 =D_a^{(m)}(u)-4^{-(m+2)}D_{2a}^{(m)}(u),
 \tag{L-91020.3}
\]

where `D_a^(m)(u)=F_m(u^2/a^2)`.

The coefficient `4^(-(m+2))` is the unique coefficient cancelling the leading tail of `F_m`.

## 2. Positive transport densities

Define nonnegative densities on the positive half-line by

\[
 \boxed{
 W_0(r)=r\,\mathbf 1_{[1,4]}(r),
 }
 \tag{L-91020.4}
\]

and

\[
 \boxed{
 W_{m+1}(r)=\int_{r/4}^{r}W_m(v)\,dv.
 }
 \tag{L-91020.5}
\]

Then `W_m>=0`, and its support is exactly contained in

\[
 [1,4^{m+1}].
\]

The main identity is

\[
 \boxed{
 F_m(y)
 =(m+2)!\,y
 \int_0^\infty
 \frac{W_m(r)}{(y+r)^{m+3}}\,dr
 \qquad(y>=0).
 }
 \tag{L-91020.6}
\]

In particular,

\[
 \boxed{F_m(y)>=0\quad(m>=0,y>=0).}
 \tag{L-91020.7}
\]

### Proof

For `m=0`, direct integration gives

\[
 2y\int_1^4\frac{r}{(y+r)^3}\,dr
 =\frac{16}{(y+4)^2}-\frac1{(y+1)^2}.
\]

Assume (L-91020.6). A change of variables gives

\[
 4^{-(m+2)}F_m(y/4)
 =(m+2)!y\int_0^\infty
 \frac{\frac14W_m(r/4)}{(y+r)^{m+3}}\,dr.
\]

Since

\[
 W_{m+1}'(r)=W_m(r)-\frac14W_m(r/4),
\]

subtraction and one integration by parts yield

\[
 F_{m+1}(y)
 =(m+3)!y\int_0^\infty
 \frac{W_{m+1}(r)}{(y+r)^{m+4}}\,dr.
\]

The boundary terms vanish because `W_(m+1)` is compactly supported and vanishes at both endpoints. This proves the induction.

## 3. Exact lower-end suppression

On the first geometric cell `1<=r<=4`, the recursion never sees the lower endpoint `r/4`, and repeated integration gives

\[
 \boxed{
 W_m(r)
 =\frac{(r-1)^m}{m!}
 +\frac{(r-1)^{m+1}}{(m+1)!}.
 }
 \tag{L-91020.8}
\]

Thus the dangerous lower endpoint is suppressed to order `m` with a factorial denominator. This is the exact quantitative mechanism behind the increasingly high-order Cauchy cancellation.

For moments

\[
 M_k^{(m)}=\int_0^\infty r^kW_m(r)\,dr,
\]

one has

\[
 \boxed{
 M_k^{(m+1)}
 =\frac{4^{k+1}-1}{k+1}M_{k+1}^{(m)}.
 }
 \tag{L-91020.9}
\]

Consequently

\[
 F_m(y)
 \sim (m+2)!M_0^{(m)}y^{-(m+2)}
 \qquad(y\to\infty).
 \tag{L-91020.10}
\]

This proves that the storage factor in (L-91020.2) is sharp: replacing `4^(-(m+2))` by a larger coefficient makes the next residual negative at sufficiently large `y`.

## 4. First sharp storage step

At `m=0`, the first residual is

\[
 \boxed{
 F_1(y)
 =\frac{27y(14y^2+163y+224)}
 {(y+1)^2(y+4)^2(y+16)^2}.
 }
 \tag{L-91020.11}
\]

Equivalently,

\[
 \boxed{
 D_a^{(0)}(u)-\frac1{16}D_{2a}^{(0)}(u)
 =F_1(u^2/a^2)>=0.
 }
 \tag{L-91020.12}
\]

This is the sharp sixteenfold storage law.

## 5. Stable minimum-phase spectral factor

Let `alpha,beta` be the positive roots determined by

\[
 \alpha+\beta=\frac{163}{14},
 \qquad
 \alpha\beta=16.
 \tag{L-91020.13}
\]

Thus

\[
 \alpha=\frac{163-5\sqrt{561}}{28},
 \qquad
 \beta=\frac{163+5\sqrt{561}}{28}.
\]

Define the right-half-plane transfer function

\[
 \boxed{
 \Psi_a(s)
 =\sqrt{378}\,a^3
 \frac{s(s+\sqrt\alpha\,a)(s+\sqrt\beta\,a)}
 {(s+a)^2(s+2a)^2(s+4a)^2}.
 }
 \tag{L-91020.14}
\]

Then

\[
 \boxed{
 |\Psi_a(iu)|^2
 =D_a^{(0)}(u)-\frac1{16}D_{2a}^{(0)}(u).
 }
 \tag{L-91020.15}
\]

All poles and nonzero zeros lie in the open left half-plane. Moreover

\[
 \boxed{
 \begin{aligned}
 \Psi_a(s)
 ={}&\frac{\sqrt{378}\,a^3}
 {(s+a)(s+2a)(s+4a)}\\
 &\times\frac{s}{s+a}
 \frac{s+\sqrt\alpha a}{s+2a}
 \frac{s+\sqrt\beta a}{s+4a}.
 \end{aligned}
 }
 \tag{L-91020.16}
\]

Because

\[
 0<\sqrt\alpha<2,
 \qquad
 0<\sqrt\beta<4,
\]

each of the last three factors is a scalar Schur multiplier of the right half-plane. Thus the first storage residual is not merely a pointwise square: it is a stable minimum-phase Hardy-space channel followed by a three-stage contractive cascade.

Also

\[
 \Psi_a(0)=0,
 \qquad
 \Psi_a(s)=O(s^{-3})
 \quad(|s|\to\infty,\ \Re s>=0),
\]

so its causal impulse has zero total mass and two additional degrees of high-frequency decay.

## 6. Coefficient-one normalization

Put

\[
 \widetilde D_a^{(m)}(u)
 =a^{-2(m+2)}D_a^{(m)}(u).
\]

Then (L-91020.3) becomes

\[
 \boxed{
 \widetilde D_a^{(m)}(u)
 -\widetilde D_{2a}^{(m)}(u)
 =a^{-2(m+2)}D_a^{(m+1)}(u)>=0
 }
 \tag{L-91020.17}
\]

on every critical-line coordinate. The inherited state returns with coefficient exactly one at the doubled scale.

## 7. Scope

Established here:

1. the sharp factor `4^(-(m+2))` at every cancellation order;
2. a positive integral representation for every residual;
3. factorial suppression of the lower geometric endpoint;
4. the sharp sixteenfold first storage law;
5. a stable minimum-phase scalar factor for the first innovation;
6. a coefficient-one normalized scale recurrence on the critical line.

Not established here:

1. positivity of the corresponding completed Weil form for actual zeta data;
2. a source-side intertwiner carrying the positive generalized-Jordan cocycle to `Psi_a`;
3. RH.
