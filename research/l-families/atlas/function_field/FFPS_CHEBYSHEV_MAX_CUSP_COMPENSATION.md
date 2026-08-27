# Chebyshev notch depth and max-cusp refill obey a compensation law

Status: **exact primitive energy, exact max-cusp linear refill coefficient,
global Stieltjes positivity, quadratic refill decay, strictly decreasing
cost-refill compensation product, sharp all-order bounds, and a sharp
uniform-in-order Young remainder envelope; no moving-order Perron estimate,
no new beta cancellation, and no proof of RH**

Bounded replay:
[ffps_chebyshev_max_cusp_compensation.py](ffps_chebyshev_max_cusp_compensation.py).
Canonical summary:
[ffps_chebyshev_max_cusp_compensation.json](ffps_chebyshev_max_cusp_compensation.json).

Frozen source: the Chebyshev-step autocorrelation normal form at commit
**f3ae060d1bba0a7855e09d88b856baf991fc844a**. The producer pins all four
source blobs and imports no live predecessor module.

## 0. Outcome

The exact order-\(2r\) Fourier notch of the Chebyshev step is refilled by the
absolute-lag/max cusp in every fixed positive order. The refill remains
linear, but its coefficient can now be evaluated exactly.

For \(r\ge1\), let

\[
 K_r(t)=(-1)^rh_r\operatorname{sgn}U_r(2t-1),
 \qquad
 h_r=r!4^rb,
\tag{0.1}
\]

on \((0,1)\), zero outside, and put

\[
 F_r(t)=\int_{-\infty}^tK_r(u)\,du.
\tag{0.2}
\]

Then

\[
 \boxed{
 \frac{\|F_r\|_2^2}{h_r^2}
 =\kappa_r
 =\frac{\tan^2 a_r}{6(3-\tan^2a_r)},
 \qquad
 a_r=\frac{\pi}{2(r+1)}.}
\tag{0.3}
\]

Equivalently,

\[
 \kappa_r
 =\frac{1-\cos(\pi/(r+1))}
 {12(1+2\cos(\pi/(r+1)))}.
\tag{0.3a}
\]

If

\[
 R_r(s)=\int K_r(t)K_r(t+s)\,dt,
\tag{0.4}
\]

the universal absolute-lag identity becomes

\[
 \boxed{
 \int_{\mathbb R}|s|R_r(s)\,ds
 =-2\|F_r\|_2^2.}
\tag{0.5}
\]

Therefore the max-cusp/Perron tilt has the exact zero-mode expansion

\[
 \boxed{
 \int_{\mathbb R}R_r(s)e^{-z|s|/2}\,ds
 =z\|F_r\|_2^2+O(z^2),
 \qquad z\to0.}
\tag{0.6}
\]

The sign is positive. In fact this local statement belongs to a global law.
For every real \(z>0\),

\[
 \boxed{
 0<J_r(z)<z\|F_r\|_2^2,
 \qquad
 J_r(z)=\int_{\mathbb R}R_r(s)e^{-z|s|/2}\,ds.}
\tag{0.6a}
\]

Moreover \(J_r(2\sqrt q)/(2\sqrt q)\) is a strictly completely monotone
Stieltjes function of \(q>0\), decreasing from \(\|F_r\|_2^2\) to zero.
Thus the positive max cusp refills the notch at every positive tilt, not only
infinitesimally. The untilted zero mode vanishes because \(K_r\) has mean
zero, while the absolute-lag moment is negative.

Each additional vanished moment generates another exact causal-primitive
term in a global alternating Stieltjes expansion. At information order \(r\),
the first nonanalytic endpoint is the forced even cusp

\[
 (-1)^rb^2\left(\frac{z^2}{4}\right)^r.
\tag{0.6b}
\]

Thus the order-\(2r\) Fourier notch, the positive real refill, and the
terminal cusp coefficient are three faces of one resolvent hierarchy.

Normalized by \(R_r(0)=h_r^2\), the refill coefficient decays quadratically:

\[
 \boxed{
 \kappa_r
 =\frac{\pi^2}{72(r+1)^2}
 \left(1+O(r^{-2})\right).}
\tag{0.7}
\]

This looks like a growing-notch gain until it is charged against the sharp
universal BV safe constant

\[
 A_r=\frac{16^r(2r+3)^2}
 {(2r+1)\binom{2r}{r}^2}
 \sim2\pi r^2.
\tag{0.8}
\]

The two scales exactly compensate, with the sharper expansion

\[
 \boxed{
 A_r\kappa_r
 =\frac{\pi^3}{36}\left(
 1+\frac{3}{4r}
 +\frac{8\pi^2-27}{32r^2}
 +O(r^{-3})\right).}
\tag{0.9}
\]

Moreover the products decrease strictly at every order:

\[
 \boxed{
 \frac{\pi^3}{36}<A_r\kappa_r\le\frac{25}{9}
 \qquad(r\ge1).}
\tag{0.10}
\]

For \(r\ge2\), the sharper upper bound is \(196/135\).

Thus growing information order makes the max-cusp refill coefficient small,
but not for free in the universal normalized geometry. The product has a
finite nonzero limit.

## 1. Exact primitive on the Chebyshev cells

Set

\[
 \theta=\frac{\pi}{r+1},
 \qquad
 a=\frac\theta2,
\tag{1.1}
\]

and write the cell boundaries as

\[
 y_j=\frac{1-\cos(j\theta)}2,
 \qquad0\le j\le r+1.
\tag{1.2}
\]

The cell widths are

\[
 \ell_j=y_{j+1}-y_j
 =\sin a\,\sin((2j+1)a).
\tag{1.3}
\]

After dividing by \(h_r\), the primitive at the left boundary of cell \(j\)
is the alternating partial sum

\[
 S_j=\sum_{k=0}^{j-1}(-1)^k\ell_k
 =(-1)^{j+1}\frac{\tan a}{2}\sin(j\theta).
\tag{1.4}
\]

Define

\[
 B_j=\frac{\tan a}{2}\sin(j\theta).
\tag{1.5}
\]

On cell \(j\), the normalized primitive runs linearly from
\((-1)^{j+1}B_j\) to \((-1)^jB_{j+1}\). Hence

\[
 \int_{y_j}^{y_{j+1}}\left|\frac{F_r(t)}{h_r}\right|^2dt
 =\frac{B_j^3+B_{j+1}^3}{3}.
\tag{1.6}
\]

Since \(B_0=B_{r+1}=0\), summing gives

\[
 \frac{\|F_r\|_2^2}{h_r^2}
 =\frac{\tan^3a}{12}
 \sum_{j=1}^r\sin^3(j\theta).
\tag{1.7}
\]

Now

\[
 \sum_{j=1}^r\sin(j\theta)=\cot a,
 \qquad
 \sum_{j=1}^r\sin(3j\theta)=\cot(3a),
\tag{1.8}
\]

and \(\sin^3x=(3\sin x-\sin3x)/4\). Thus

\[
 \frac{\|F_r\|_2^2}{h_r^2}
 =\frac{\tan^3a}{48}\bigl(3\cot a-\cot3a\bigr).
\tag{1.9}
\]

The triple-angle identity reduces (1.9) to (0.3).

The first two values are

\[
 \kappa_1=\frac1{12},
 \qquad
 \kappa_2=\frac1{48}.
\tag{1.10}
\]

The same cell geometry also gives an exact \(L^1\) primitive size. On cell
\(j\), the absolute area is
\((B_j^2+B_{j+1}^2)/2\). Since
\(\sum_{j=1}^r\sin^2(j\theta)=(r+1)/2\),

\[
 \boxed{
 \frac{\|F_r\|_1}{|h_r|}
 =\lambda_r
 =\frac{r+1}{8}\tan^2a_r.}
\tag{1.11}
\]

## 2. Why the max cusp refills every fixed notch

For any compact real mean-zero kernel \(K\), with primitive \(F\) and
autocorrelation \(R\), the absolute-lag identity is

\[
 \int|s|R(s)\,ds=-2\|F\|_2^2.
\tag{2.1}
\]

The integrals are absolute because all functions are compactly supported.
Applying (2.1) to \(K_r\) proves (0.5).

Expand the even tilt:

\[
 e^{-z|s|/2}=1-\frac z2|s|+O(z^2s^2).
\tag{2.2}
\]

The constant term contributes

\[
 \int R_r(s)\,ds
 =\left(\int K_r\right)^2=0.
\tag{2.3}
\]

The linear term, by (0.5), is \(z\|F_r\|_2^2\), proving (0.6). Since
\(F_r\ne0\), the coefficient is strictly positive for every fixed
\(r\ge1\). No finite notch order survives multiplication by the nonconstant
absolute-lag tilt.

There is also an exact remainder identity. Put
\(C_{F_r}=\widetilde F_r*F_r\). Since \(R_r=-C_{F_r}''\) and, for
\(a=z/2\),

\[
 (e^{-a|s|})''=a^2e^{-a|s|}-2a\delta_0,
\tag{2.4}
\]

distributional integration by parts gives

\[
 \boxed{
 \int R_r(s)e^{-z|s|/2}\,ds
 =z\|F_r\|_2^2
 -\frac{z^2}{4}
 \int C_{F_r}(s)e^{-z|s|/2}\,ds.}
\tag{2.5}
\]

The remainder in (2.5) has a definite sign. More precisely, for any nonzero
compact real mean-zero \(K\) and real \(z>0\), Fourier inversion gives, with
\(a=z/2\),

\[
 \boxed{
 \frac{J_K(z)}z
 =\frac1{2\pi}\int_{\mathbb R}
 \frac{|\widehat K(\xi)|^2}{a^2+\xi^2}\,d\xi.}
\tag{2.5a}
\]

If

\[
 \Phi_K(q)=\frac{J_K(2\sqrt q)}{2\sqrt q},
\tag{2.5b}
\]

then for every integer \(m\ge0\) and \(q>0\),

\[
 \boxed{
 (-1)^m\Phi_K^{(m)}(q)
 =\frac{m!}{2\pi}\int_{\mathbb R}
 \frac{|\widehat K(\xi)|^2}{(q+\xi^2)^{m+1}}\,d\xi>0.}
\tag{2.5c}
\]

Because \(\widehat K(\xi)=i\xi\widehat F(\xi)\), Plancherel also gives

\[
 \lim_{q\downarrow0}\Phi_K(q)=\|F\|_2^2.
\tag{2.5d}
\]

Equations (2.5a)--(2.5d) prove (0.6a), show that the correction in (2.5)
is strictly negative, and rule out every positive-tilt zero. At the opposite
endpoint, the exponential approximate identity gives

\[
 \lim_{z\to\infty}zJ_K(z)=4\|K\|_2^2.
\tag{2.5e}
\]

For the Chebyshev step there is also a finite exact coordinate. Put
\(\mu_j=h_r(-1)^jc_j\), where \(c_0=c_{r+1}=1\), \(c_j=2\) in the
interior, and
\(y_j=(1-\cos(j\pi/(r+1)))/2\). Then

\[
 \boxed{
 J_r(z)=
 \sum_{j,k=0}^{r+1}\mu_j\mu_k
 \frac{1-e^{-a|y_j-y_k|}-a|y_j-y_k|}{a^2},
 \qquad a=\frac z2.}
\tag{2.5f}
\]

The additive constant in the displayed Green kernel is harmless because
\(\sum_j\mu_j=0\). Formula (2.5f) turns the complete positive-tilt refill
into the same finite Chebyshev difference spectrum that controls
\(-R_r''\); it uses no root search or quadrature.

Equivalently, with \(q_j=(-1)^jc_j\),

\[
 \boxed{
 \frac{J_r(z)}{h_r^2}
 =\frac4{z^2}\left[
 z-\sum_{j,k=0}^{r+1}q_jq_k
 e^{-z|y_j-y_k|/2}\right].}
\tag{2.5f.1}
\]

The positivity is also a literal square. For every compact real \(K\) and
real \(z>0\),

\[
 \boxed{
 J_K(z)=z\int_{\mathbb R}
 \left|
 \int_{-\infty}^x e^{-(z/2)(x-t)}K(t)\,dt
 \right|^2dx.}
\tag{2.5f.2}
\]

For the unit-support Chebyshev step this sharpens the global sandwich to

\[
 0<\frac{J_r(z)}{h_r^2}
 <\min\left\{\kappa_rz,\frac4z\right\}.
\tag{2.5f.3}
\]

It also gives the fixed-order real large-tilt expansion as \(z\to+\infty\),

\[
 \frac{J_r(z)}{h_r^2}
 =\frac4z-\frac{16r+8}{z^2}
 +O_r\left(\frac{e^{-z\delta_r/2}}{z^2}\right),
\qquad
 \delta_r=\sin^2\frac{\pi}{2(r+1)}.
\tag{2.5f.4}
\]

The absolute value of the displayed error is at most
\((16r^2+16r+8)e^{-z\delta_r/2}/z^2\). This is a fixed-order statement
unless \(z\delta_r\) is controlled.

The Stieltjes law also exposes the complete moment-cancellation hierarchy,
not just the first refill. For a compact real information-order-\(r\) kernel
\(K\), define its causal primitives by

\[
 P_0=K,\qquad
 P_m(t)=\frac1{(m-1)!}\int_{-\infty}^t(t-u)^{m-1}K(u)\,du
 \quad(1\le m\le r).
\tag{2.5g}
\]

The vanished moments make every \(P_m\) in (2.5g) compact, with
\(P_m'=P_{m-1}\). Under the sensitivity convention

\[
 b=\frac{(-1)^r}{r!}\int t^rK(t)\,dt,
\tag{2.5h}
\]

repeated integration by parts gives \(\int P_r=b\). For any compact real
\(f\), put

\[
 G_f(q)=\frac1{2\pi}\int_{\mathbb R}
 \frac{|\widehat f(\xi)|^2}{\xi^2+q}\,d\xi.
\tag{2.5i}
\]

Since \(\widehat{P_{m-1}}=i\xi\widehat P_m\),

\[
 G_{P_{m-1}}(q)=\|P_m\|_2^2-qG_{P_m}(q).
\tag{2.5j}
\]

Iteration gives, for every \(1\le M\le r\),

\[
 \boxed{
 G_K(q)=
 \sum_{m=1}^M(-q)^{m-1}\|P_m\|_2^2
 +(-q)^M G_{P_M}(q).}
\tag{2.5k}
\]

The final factor is strictly positive. Thus every truncation has a global,
exact alternating error sign: odd \(M\) gives an upper bound and even \(M\)
gives a lower bound. At the terminal primitive,

\[
 G_{P_r}(q)=\frac{b^2}{2\sqrt q}+O(1)
 \qquad(q\downarrow0).
\tag{2.5l}
\]

Combining (2.5k) and (2.5l), with \(q=z^2/4\), yields the full local normal
form

\[
 \boxed{
 J_K(z)=
 z\sum_{m=1}^r
 \left(-\frac{z^2}{4}\right)^{m-1}\|P_m\|_2^2
 +(-1)^rb^2\left(\frac{z^2}{4}\right)^r
 +O(z^{2r+1}).}
\tag{2.5m}
\]

The analytic terms have odd powers. The absolute-lag cusp first appears as
the terminal even power, with its sign and coefficient forced exactly by the
first surviving moment. For \(r=1\) it is \(-b^2z^2/4\); for \(r=2\) it is
\(+b^2z^4/16\). In particular, when \(r\ge2\), the \(O(z^2)\) remainder in
(0.6) improves first to \(O(z^3)\), while the positive linear refill itself
remains.

More importantly, the relative linear approximation is uniform in
information order for real \(z\ge0\). Young's \(L^1\) inequality and (2.5)
give

\[
 \left|
 \frac1{h_r^2}\int R_r(s)e^{-z|s|/2}\,ds-z\kappa_r
 \right|
 \le\frac{z^2}{4}\lambda_r^2.
\tag{2.6}
\]

The relative coefficient is

\[
 \frac{\lambda_r^2}{4\kappa_r}
 =\frac{3(r+1)^2t_r(3-t_r)}{128},
 \qquad t_r=\tan^2a_r.
\tag{2.7}
\]

The exact maximum of (2.7) is smaller than the crude product of separate
factor bounds. Put \(n=r+1\), \(x=\pi/(2n)\), \(y=\tan x\), and

\[
 H(x)=\left(\frac{\tan x}{x}\right)^2(3-\tan^2x).
\tag{2.7a}
\]

For \(n\ge3\), so \(0<x\le\pi/6\), the sign of \(H'(x)\) is the sign of

\[
 \arctan y-
 \frac{y(3-y^2)}{(1+y^2)(3-2y^2)}.
\tag{2.7b}
\]

The derivative of (2.7b), as a function of \(y\), is

\[
 \frac{y^2(6y^4-25y^2+9)}
 {(1+y^2)^2(3-2y^2)^2}>0
 \qquad(0<y^2\le1/3).
\tag{2.7c}
\]

Indeed \(6u^2-25u+9\) decreases on \(0\le u\le1/3\) and equals \(4/3\)
at the right endpoint. The difference in (2.7b) tends to zero with \(y\),
so it is strictly positive thereafter. Thus \(H\) increases with \(x\), so
(2.7) decreases strictly from \(r=2\) onward. Directly, its values at both
\(r=1\) and \(r=2\) equal \(3/16\). Therefore

\[
 \boxed{
 \left|
 \frac1{h_r^2}\int R_r(s)e^{-z|s|/2}\,ds-z\kappa_r
 \right|
 \le\frac3{16}z^2\kappa_r}
\tag{2.8}
\]

for every \(r\ge1\) and real \(z\ge0\). The coefficient \(3/16\) is sharp
for this exact \(L^1\)/Young envelope and is attained exactly at \(r=1,2\).
It then decreases to \(9\pi^2/512\), with

\[
 \frac{\lambda_r^2}{4\kappa_r}
 =\frac{9\pi^2}{512}\left(
 1+\frac{\pi^2}{12(r+1)^2}
 -\frac{\pi^4}{240(r+1)^4}
 +O(r^{-6})\right).
\tag{2.9}
\]

The same argument is analytic in \(z\). When \(\Re z\ge0\),
\(|e^{-z|s|/2}|\le1\), so

\[
 \boxed{
 \left|\frac{J_r(z)}{h_r^2}-z\kappa_r\right|
 \le\frac3{16}|z|^2\kappa_r.}
\tag{2.10}
\]

The linear term therefore dominates throughout the uniform half-disk

\[
 \boxed{
 \Re z\ge0,\qquad0<|z|<\frac{16}{3}
 \quad\Longrightarrow\quad J_r(z)\ne0}
\tag{2.11}
\]

for every information order. Under width-\(W\) dilation, the condition is
\(|z|W<16/3\). This is a local kernel-transform zero-free region, not a
reciprocal-zeta or full Perron-contour zero-free theorem.

Hence the linear term is relatively accurate as \(z\to0^+\) uniformly in
\(r\); no condition such as \(zr^2\to0\) is needed for this isolated zero
mode. The guaranteed relative-error window from this envelope is
\((3/16)z<1\). After dilation to width \(W\), the corresponding small
parameter is \(zW\).

## 3. The compensation limit

As \(r\to\infty\),

\[
 \tan a_r
 =\frac{\pi}{2(r+1)}+O(r^{-3}),
\tag{3.1}
\]

so (0.3) gives (0.7). The sharp safe-factor packet gives

\[
 A_r=2\pi r^2\left(1+O(r^{-1})\right).
\tag{3.2}
\]

Multiplication, retaining the displayed terms from the central-binomial and
tangent expansions, proves (0.9).

To prove all-order descent, put

\[
 t_r=\tan^2\!\left(\frac{\pi}{2(r+1)}\right),
 \qquad P_r=A_r\kappa_r.
\tag{3.3}
\]

Then

\[
 \frac{P_{r+1}}{P_r}
 =\frac{A_{r+1}}{A_r}
 \frac{t_{r+1}}{t_r}
 \frac{3-t_r}{3-t_{r+1}}.
\tag{3.4}
\]

The last factor is below one. Since \(\tan x/x\) is strictly increasing on
\((0,\pi/2)\) (differentiate; the numerator
\(x\sec^2x-\tan x\) starts at zero and has positive derivative),

\[
 \frac{t_{r+1}}{t_r}
 <\left(\frac{r+1}{r+2}\right)^2.
\tag{3.5}
\]

Combining (3.5) with the exact ratio for \(A_{r+1}/A_r\) yields

\[
 \frac{P_{r+1}}{P_r}
 <Q_r
 =\frac{4(r+1)^4(2r+5)^2}
 {(r+2)^2(2r+1)(2r+3)^3}.
\tag{3.6}
\]

Finally,

\[
 1-Q_r
 =\frac{12r^4+60r^3+99r^2+60r+8}
 {(r+2)^2(2r+1)(2r+3)^3}>0.
\tag{3.7}
\]

Thus \(P_r\) decreases strictly to the limit in (0.9), proving (0.10).

The first products are

\[
 A_1\kappa_1=\frac{25}{9},
 \qquad
 A_2\kappa_2=\frac{196}{135},
\tag{3.8}
\]

The second value supplies the \(r\ge2\) upper bound.

## 4. The cost-charged moving local chart

The compensation law has a precise moving-order interpretation. Let
\(\ell=\log X\), \(W>0\), and dilate the Chebyshev step to width \(W\) while
preserving its order-\(r\) sensitivity. Write

\[
 E_{r,W}=R_{r,W}(0),\qquad
 u=zW,\qquad
 j_r(u)=\frac{J_{r,1}(u)}{R_{r,1}(0)}.
\tag{4.1}
\]

Exact dilation gives

\[
 \frac{J_{r,W}(z)}{E_{r,W}}=Wj_r(u).
\tag{4.2}
\]

The Barnes/Perron factor \(1/z\) cancels the trivial linear tilt. The natural
per-unit-tilt zero-mode coefficient is therefore

\[
 \mathcal L_{r,W}(z)
 =\frac{J_{r,W}(z)}{zW^2E_{r,W}}
 =\frac{j_r(u)}u.
\tag{4.3}
\]

For positive real \(u\), (0.6a) and (2.8) give the uniform local chart

\[
 \left(1-\frac3{16}u\right)\kappa_r
 \le\mathcal L_{r,W}(z)\le\kappa_r
 \qquad(0<u<16/3).
\tag{4.4}
\]

The sharp BV safe factor is

\[
 \mathcal G^*_{r,W}(X)
 =A_r\left(1+\frac{\ell}{W}\right)^{2r+2}.
\tag{4.5}
\]

Consequently, for any schedule \(r=r_X\ge1\), \(W=W_X>0\), and
\(u_X=z_XW_X\to0^+\), the cost-charged refill satisfies

\[
 \boxed{
 \mathcal G^*_{r,W}(X)\mathcal L_{r,W}(z)
 =P_r\left(1+\frac{\ell}{W}\right)^{2r+2}
 (1+O(u_X)),
 \qquad P_r=A_r\kappa_r,}
\tag{4.6}
\]

with an absolute relative-error constant at most \(3/16\). In particular,

\[
 \liminf_{X\to\infty}
 \mathcal G^*_{r,W}(X)\mathcal L_{r,W}(z)
 \ge\frac{\pi^3}{36}.
\tag{4.7}
\]

The uncharged coefficient \(\mathcal L_{r,W}\sim\kappa_r\) vanishes when
\(r_X\to\infty\), but it cannot vanish after the sharp BV cost is charged.
More precisely, if

\[
 (r_X+1)\log\left(1+\frac{\ell}{W_X}\right)\longrightarrow\tau
 \in[0,\infty),
\tag{4.8}
\]

then, provided \(r_X\to\infty\),

\[
 \mathcal G^*_{r,W}(X)\mathcal L_{r,W}(z)
 \longrightarrow\frac{\pi^3}{36}e^{2\tau}.
\tag{4.9}
\]

Within schedules with \(r_X\to\infty\), the limiting floor \(\pi^3/36\) is
approached exactly when \(r_X\log(1+\ell/W_X)\to0\). In the wide-support
regime \(W_X\gg\ell\), this is equivalent to \(W_X\gg r_X\ell\).

This is an exact local geometric barrier for the BV-optimal Chebyshev family.
It is not a universal lower bound over all compact BV kernels: the sharp
lower bound for the BV cost and the refill coefficient of an unrelated
kernel cannot simply be multiplied. It also requires \(z_XW_X\to0\), controls
only the isolated zero mode, and supplies no vertical-contour, reciprocal-zeta,
height-truncation, or beta primitive-pair estimate.

## 5. What this does and does not say

The result sharpens the earlier statement that the max cusp refills every
fixed Fourier notch linearly. The \(R_r(0)\)-normalized coefficient
\(\kappa_r\) is not uniform in \(r\): it shrinks like \(r^{-2}\). Any
moving-order analysis that treated that normalized coefficient as a fixed
positive constant would therefore be wrong.

Conversely, the same moving order enlarges the best available universal BV
normalization like \(r^2\). Equation (0.9) is a compensation law between those
two exact geometric quantities.

This is not yet a Perron estimate. A contour argument also contains the
reciprocal-zeta pair, height truncation, the support factor, and the precise
order in which \(r_X\), \(z\), and \(X\) move. The finite limit neither proves
that growing order cannot help through source arithmetic nor supplies such a
gain.

In particular:

- it does not control the signed beta primitive-pair sum;
- it does not by itself justify interchanging \(r\to\infty\) and \(z\to0\)
  inside the complete Perron contour and reciprocal-zeta factors;
- it does not replace the fully normalized moving-order criterion;
- it does not turn a local zero-mode expansion into a uniform contour bound.

## 6. Scope ledger

| statement | grade |
|---|---|
| exact Chebyshev primitive energy (0.3) | **PROVED** |
| absolute-lag identity specialized to the step | **PROVED** |
| exact positive linear max-cusp refill (0.6) | **PROVED** |
| global positive-tilt Stieltjes law (0.6a), (2.5a)--(2.5e) | **PROVED** |
| finite exact Chebyshev difference formula (2.5f) | **PROVED** |
| positive-square form and global two-envelope bound (2.5f.2)--(2.5f.3) | **PROVED** |
| fixed-order large-tilt expansion (2.5f.4) | **PROVED** |
| global alternating primitive hierarchy (2.5k) | **PROVED** |
| terminal even cusp coefficient (2.5m) | **PROVED** |
| uniform-in-order relative remainder (2.8) | **PROVED** |
| sharp \(3/16\) Young-envelope coefficient | **PROVED** |
| uniform complex zero-free half-disk (2.11) | **PROVED FOR THE KERNEL TRANSFORM ONLY** |
| quadratic normalized refill decay (0.7) | **PROVED** |
| finite nonzero compensation limit (0.9) | **PROVED** |
| strict descent and sharp bounds (0.10) | **PROVED** |
| cost-charged moving local floor (4.7) | **PROVED FOR THE CHEBYSHEV FAMILY AND \(zW\to0^+\)** |
| uniform moving-order Perron estimate | **NOT PROVED** |
| new beta cancellation, RH, or GRH | **NOT PROVED** |

No external novelty or priority is claimed.

## 7. Bounded replay

The producer:

- verifies the frozen autocorrelation quartet by full Git blob ID;
- checks (0.3) independently by analytic cell integration through order
  eight;
- checks the global tilted transform independently from the jump Green kernel
  and direct analytic cell-pair integration;
- integrates the causal primitives cell by cell and checks their alternating
  Stieltjes bounds and terminal sensitivity;
- checks positivity, the Stieltjes monotonicity rows, fixed-order large-tilt
  scaling, the sharp \(3/16\) Young envelope, and the cost-charged dilation
  chart;
- tabulates only sixteen fixed orders and two constant-time asymptotic spot
  evaluations;
- records the exact trigonometric formula, sharp rational \(A_r\), and
  compensation limit;
- performs no beta sum, prime enumeration, zeta evaluation, root search,
  random sampling, quadrature, or curve computation.

~~~text
python -B research/l-families/atlas/function_field/ffps_chebyshev_max_cusp_compensation.py --check
python -O -B research/l-families/atlas/function_field/ffps_chebyshev_max_cusp_compensation.py --check
python -B -m unittest tests.test_ffps_chebyshev_max_cusp_compensation
python -O -B -m unittest tests.test_ffps_chebyshev_max_cusp_compensation
python -m ruff check research/l-families/atlas/function_field/ffps_chebyshev_max_cusp_compensation.py tests/test_ffps_chebyshev_max_cusp_compensation.py
python -m ruff format --check research/l-families/atlas/function_field/ffps_chebyshev_max_cusp_compensation.py tests/test_ffps_chebyshev_max_cusp_compensation.py
~~~
