# Chebyshev notch depth and max-cusp refill obey a compensation law

Status: **exact primitive energy, exact max-cusp linear refill coefficient,
global Stieltjes positivity, quadratic refill decay, strictly decreasing
cost-refill compensation product, exact second-primitive energy, a sharp
moving-tilt phase profile with a zero-free right-half-plane continuation,
sharp all-order bounds, and a sharp uniform-in-order Young remainder
envelope; no full imaginary-axis Perron estimate, no new beta cancellation,
and no proof of RH**

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

The compensation has a sharp real-positive scale boundary. With \(n=r+1\),
width-normalized tilt \(u=zW\), and

\[
 \Phi(c)=\frac{288}{\pi^2c^3}
 \left[c-\frac4\pi\int_0^\pi
 \tanh\left(\frac{c\pi\sin\theta}{8}\right)d\theta\right],
 \qquad c>0,
\tag{0.11}
\]

the relative refill tends to \(1\), \(\Phi(c)\), or \(0\) according as
\(u/n\to0\), \(u/n\to c\in(0,\infty)\), or \(u/n\to\infty\). Thus the
sublinear regime is the maximal real-positive scale on which the full
linear refill survives.

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

The hypothesis \(u_X\to0\) can be widened substantially when the information
order grows. Put \(n=r+1\), use the angular coordinate

\[
 t=\frac{1-\cos\theta}{2},
 \qquad0\le\theta\le\pi,
\tag{4.10}
\]

and let \(s(x)=\operatorname{sgn}(\sin x)\). The unit-height Chebyshev step
is exactly \(s(n\theta)\). Introduce the mean-zero periodic primitives

\[
 T(x)=-\frac4\pi\sum_{\substack{k\ge1\\k\ {\rm odd}}}
 \frac{\cos(kx)}{k^2},
 \qquad
 U(x)=-\frac4\pi\sum_{\substack{k\ge1\\k\ {\rm odd}}}
 \frac{\sin(kx)}{k^3},
\tag{4.11}
\]

so \(T'=s\) away from the jumps and \(U'=T\). Repeated integration by
parts against the bounded next periodic primitives gives, uniformly in
\(\theta\),

\[
 \frac{P_1(t(\theta))}{h_r}
 =\frac{\sin\theta}{2n}T(n\theta)
 -\frac{\cos\theta}{2n^2}U(n\theta)
 +O(n^{-3}),
\tag{4.12}
\]

and

\[
 \frac{P_2(t(\theta))}{h_r}
 =\frac{\sin^2\theta}{4n^2}U(n\theta)
 +O(n^{-3}).
\tag{4.13}
\]

Parseval gives

\[
 \langle T^2\rangle=\frac{\pi^2}{12},
 \qquad
 \langle U^2\rangle=\frac{\pi^4}{120}.
\tag{4.14}
\]

Periodic averaging in \(dt=(\sin\theta/2)d\theta\), together with
\(\int_0^\pi\sin^3\theta\,d\theta=4/3\) and
\(\int_0^\pi\sin^5\theta\,d\theta=16/15\), now yields

\[
 \frac{\|P_1\|_2^2}{h_r^2}
 =\frac{\pi^2}{72n^2}+O(n^{-3}),
 \qquad
 \frac{\|P_2\|_2^2}{h_r^2}
 =\frac{\pi^4}{3600n^4}+O(n^{-5}).
\tag{4.15}
\]

Put \(v=\sin^2(\pi/(2n))\). The cell primitives in fact give the following
exact refinement for every \(r\ge2\):

\[
 \boxed{
 \frac{\|P_2\|_2^2}{h_r^2}
 =\frac{v^2(8-9v)}
 {120(3-4v)(16v^2-20v+5)},
 \qquad
 \frac{\|P_2\|_2^2}{\|P_1\|_2^2}
 =\frac{v(8-9v)}{20(16v^2-20v+5)}.}
\tag{4.16}
\]

Indeed, on cell \(j\), with \(x=t-y_j\), one has

\[
 \frac{P_2(y_j+x)}{h_r}
 =(-1)^j\left(\frac{x^2}{2}-B_jx-C_j\right),
 \qquad
 C_j=\frac{\tan^2a\tan(2a)}{16}\sin(2j\theta).
\]

The cell norm contains only the midpoint harmonics \(1,3,5\); summing them
with
\(\sum_{j=0}^{n-1}\sin(m(j+1/2)\pi/n)=\csc(m\pi/(2n))\)
gives (4.16). Expanding it yields

\[
 \frac{\|P_2\|_2^2}{\|P_1\|_2^2}
 =\frac{\pi^2}{50n^2}
 +\frac{61\pi^4}{4800n^4}
 +\frac{1157\pi^6}{144000n^6}
 +O(n^{-8}).
\tag{4.16a}
\]

Since \(0<v\le1/4\), the denominator polynomial in (4.16) is at least one,
and \(v<\pi^2/(4n^2)\). In particular,

\[
 0<\frac{\|P_2\|_2^2}{\|P_1\|_2^2}<\frac1{n^2}
 \qquad(n\ge3).
\tag{4.16b}
\]

Apply the first two levels of (2.5k) with \(q=u^2/4\). Since
\(0<G_{P_1}(q)<\|P_2\|_2^2\),

\[
 \boxed{
 0<
 1-\frac{\mathcal L_{r,W}(z)}{\kappa_r}
 <
 \frac{u^2}{4}\frac{\|P_2\|_2^2}{\|P_1\|_2^2}
 =\frac{\pi^2u^2}{200n^2}+O\left(\frac{u^2}{n^4}\right)
 <\frac{u^2}{4n^2}.}
\tag{4.17}
\]

This bound holds for every positive real \(u\); its right side is useful
uniformly throughout the much larger sublinear-tilt regime \(u=o(r)\).
Consequently, whenever

\[
 r_X\to\infty,\qquad z_XW_X=o(r_X),\qquad
 (r_X+1)\log\left(1+\frac{\ell}{W_X}\right)\to\tau,
\tag{4.18}
\]

the limit in (4.9) still holds. In particular, the cost-charged refill tends
to \(\pi^3/36\) for \(z_XW_X=o(r_X)\) and
\(r_X\log(1+\ell/W_X)\to0\). Thus the compensation floor is not merely a
small-\(zW\) Taylor artifact; it persists across every sublinear positive
tilt.

This sublinear condition is sharp. Let

\[
 q_0=1,\qquad q_n=(-1)^n,\qquad q_j=2(-1)^j\quad(0<j<n),
\]

be the jump masses of the unit-height step, and set

\[
 S_n(z)=\sum_{j,k=0}^nq_jq_k
 \exp\left(-\frac z2|y_j-y_k|\right).
\]

The finite-jump identity (2.5f) reduces exactly to

\[
 \frac{J_r(z)}{h_r^2}=\frac{4(z-S_n(z))}{z^2}.
\tag{4.19}
\]

Suppose \(z_n/n\to c\in(0,\infty)\). In a bulk row
\(j/n\to x\), a fixed displacement \(m\) has

\[
 n(y_{j+m}-y_j)\longrightarrow
 \frac{\pi m}{2}\sin(\pi x).
\]

The resulting bilateral alternating row sum is

\[
 4\sum_{m\in\mathbb Z}(-1)^m
 e^{-c\pi|m|\sin(\pi x)/4}
 =4\tanh\left(\frac{c\pi\sin(\pi x)}8\right).
\tag{4.20}
\]

Alternating-series bounds keep every row uniformly bounded, including the
flat endpoint layers. Truncating away from the endpoints, passing to the
Riemann integral, and then removing the truncation gives

\[
 \frac{S_n(z_n)}n\longrightarrow
 \frac4\pi\int_0^\pi
 \tanh\left(\frac{c\pi\sin\theta}{8}\right)d\theta.
\tag{4.21}
\]

Combining (4.19), (4.21), and \(n^2\kappa_r\to\pi^2/72\) proves the
scale-sharp profile

\[
 \boxed{
 \frac{J_r(z_n)}{z_nh_r^2\kappa_r}\longrightarrow\Phi(c),
 \qquad
 \Phi(c)=\frac{288}{\pi^2c^3}
 \left[c-\frac4\pi\int_0^\pi
 \tanh\left(\frac{c\pi\sin\theta}{8}\right)d\theta\right].}
\tag{4.22}
\]

The inequalities \(\tanh x<x\) and
\(\tanh x>x-x^3/3\) show directly that

\[
 0<\Phi(c)<1.
\tag{4.23}
\]

At the two ends of the phase curve,

\[
 \Phi(c)=1-\frac{\pi^2c^2}{200}
 +\frac{17\pi^4c^4}{627200}+O(c^6),
 \qquad c\downarrow0,
\tag{4.24}
\]

and

\[
 \Phi(c)=\frac{288}{\pi^2c^2}
 -\frac{1152}{\pi^2c^3}+O(c^{-4}),
 \qquad c\to\infty.
\tag{4.25}
\]

The quadratic term in (4.24) agrees exactly with the second-primitive
coefficient in (4.16a). Finally, if \(z_n/n\to\infty\), the global bound
\(J_r(z)<4h_r^2/z\) gives

\[
 0<\frac{J_r(z_n)}{z_nh_r^2\kappa_r}
 <\left(\frac{288}{\pi^2}+o(1)\right)
 \left(\frac n{z_n}\right)^2\longrightarrow0.
\tag{4.26}
\]

After dilation, replace \(z_n\) by \(u_n=z_nW_n\). With the continuous
extension \(\Phi(0)=1\), the full cost-charged real-positive limit is

\[
 \boxed{
 n\to\infty,\quad u_n>0,\quad
 \frac{u_n}{n}\to c\in[0,\infty),\quad
 n\log\left(1+\frac{\ell}{W_n}\right)\to\tau\in[0,\infty)
 \quad\Longrightarrow\quad
 \mathcal G^*_{r,W}(X)\mathcal L_{r,W}(z)
 \to\frac{\pi^3}{36}e^{2\tau}\Phi(c).}
\tag{4.27}
\]

For \(u_n/n\to\infty\) and bounded cost exponent, the same product tends to
zero. Thus the universal \(\pi^3/36\) compensation floor survives exactly on
the sublinear real-positive side; linear tilt retains only the explicit
fraction \(\Phi(c)\), and superlinear tilt loses the refill.

There is also a proof-grade complex continuation, though not yet one that
reaches the full Perron axis. The Toeplitz-row argument above is locally
uniform when \(c\) ranges over a compact subset of \(\Re c>0\). Hence

\[
 \frac{J_{n-1}(nc)}{nc\,h_{n-1}^2\kappa_{n-1}}
 \longrightarrow\Phi(c)
\tag{4.28}
\]

locally uniformly on the open right half-plane. A Mittag--Leffler expansion,

\[
 \frac{\tanh x}{x}
 =\sum_{k\ge0}\frac8{\pi^2(2k+1)^2+4x^2},
\]

turns (4.22) into the positive Stieltjes representation

\[
 \boxed{
 \Phi(c)=\frac{72}{\pi^4}
 \sum_{k\ge0}\frac1{(2k+1)^2}
 \int_0^\pi
 \frac{\sin^3\theta\,d\theta}
 {(2k+1)^2+(c^2/16)\sin^2\theta}.}
\tag{4.29}
\]

Equivalently, \(\Psi(q)=\Phi(\sqrt q)\), defined by the right side of
(4.29), is a positive Stieltjes transform whose spectral support starts at
\(q=16\). It follows that

\[
 \boxed{
 \Phi(c)\ne0\quad\text{on}\quad
 \mathbb C\setminus
 \left(i[4,\infty)\cup-i[4,\infty)\right).}
\tag{4.30}
\]

Indeed, off the negative \(q\)-axis the imaginary part of a positive
Stieltjes transform has a strict sign, while on \(q>-16\) the integral is
positive. In particular, \(\Phi\) is zero-free throughout \(\Re c>0\).
Local uniform convergence then implies that every compact subset of that
half-plane is zero-free for the finite-order normalized transforms once
\(n\) is sufficiently large.

The same resolvent estimates give a complex trichotomy in any fixed acute
right-half sector \(|\arg z|\le\pi/2-\delta\):

\[
 \frac{|z_n|}{n}\to0\Longrightarrow R_n(z_n)\to1,\qquad
 \frac{z_n}{n}\to c\Longrightarrow R_n(z_n)\to\Phi(c),\qquad
 \frac{|z_n|}{n}\to\infty\Longrightarrow R_n(z_n)\to0,
\tag{4.31}
\]

where \(R_n(z)=J_{n-1}(z)/(z h_{n-1}^2\kappa_{n-1})\). The first implication
uses \(|G_{P_1}(q)|\ll_\delta\|P_2\|_2^2\); the last uses
\(|G_K(q)|\ll_\delta\|K\|_2^2/|q|\).

The excluded imaginary rays are structural, not a defect of notation. The
first Stieltjes branch point is \(c=\pm4i\). Convergence on compact subsets
of \(\Re c>0\) is not uniform as \(\Re c\downarrow0\), and the limits
\(n\to\infty\) and \(\Re c\to0\) need not commute. Thus (4.28)--(4.31) do
not prove a zero-free Perron contour or justify passage along the full
imaginary axis.

Within the sublinear-tilt schedules \(z_XW_X=o(r_X)\), the limiting floor
\(\pi^3/36\) is approached exactly when
\(r_X\log(1+\ell/W_X)\to0\). In the wide-support regime \(W_X\gg\ell\),
this is equivalent to \(W_X\gg r_X\ell\). At linear tilt, (4.27) permits a
different balance between the support-cost factor and \(\Phi(c)\).

This is an exact real-positive geometric phase diagram for the BV-optimal
Chebyshev family.
It is not a universal lower bound over all compact BV kernels: the sharp
lower bound for the BV cost and the refill coefficient of an unrelated
kernel cannot simply be multiplied. The elementary local chart requires
\(z_XW_X\to0\); the primitive hierarchy covers \(z_XW_X=o(r_X)\), and the
Toeplitz limit resolves linear and superlinear positive real tilt. These
results control only the isolated zero mode and supply no complex
vertical-contour, reciprocal-zeta, height-truncation, or beta primitive-pair
estimate.

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
| exact second-primitive norm and ratio (4.16) | **PROVED** |
| sublinear real-positive refill limit (4.17)--(4.18) | **PROVED** |
| linear-scale profile \(\Phi(c)\) (4.19)--(4.25) | **PROVED FOR REAL POSITIVE TILT** |
| superlinear real-positive collapse (4.26) | **PROVED** |
| cost-charged real-positive phase diagram (4.27) | **PROVED FOR THE CHEBYSHEV FAMILY** |
| complex right-half-plane profile (4.28) | **PROVED LOCALLY UNIFORMLY ON COMPACTS** |
| Stieltjes representation and limiting zero-free domain (4.29)--(4.30) | **PROVED** |
| acute-sector complex scale trichotomy (4.31) | **PROVED FOR THE KERNEL TRANSFORM** |
| uniform-in-order relative remainder (2.8) | **PROVED** |
| sharp \(3/16\) Young-envelope coefficient | **PROVED** |
| uniform complex zero-free half-disk (2.11) | **PROVED FOR THE KERNEL TRANSFORM ONLY** |
| quadratic normalized refill decay (0.7) | **PROVED** |
| finite nonzero compensation limit (0.9) | **PROVED** |
| strict descent and sharp bounds (0.10) | **PROVED** |
| cost-charged moving local floor (4.7) | **PROVED FOR THE CHEBYSHEV FAMILY AND \(zW=o(r)\)** |
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
- checks the exact second-primitive formula against independent cell
  integration and replays the linear-scale profile at order \(127\);
- tabulates only sixteen fixed orders, bounded asymptotic spot evaluations,
  and one deterministic \(4096\)-panel Simpson integral for the explicit
  profile;
- records the exact trigonometric formula, sharp rational \(A_r\), and
  compensation limit;
- performs no beta sum, prime enumeration, zeta evaluation, root search,
  random sampling, adaptive quadrature, or curve computation.

~~~text
python -B research/l-families/atlas/function_field/ffps_chebyshev_max_cusp_compensation.py --check
python -O -B research/l-families/atlas/function_field/ffps_chebyshev_max_cusp_compensation.py --check
python -B -m unittest tests.test_ffps_chebyshev_max_cusp_compensation
python -O -B -m unittest tests.test_ffps_chebyshev_max_cusp_compensation
python -m ruff check research/l-families/atlas/function_field/ffps_chebyshev_max_cusp_compensation.py tests/test_ffps_chebyshev_max_cusp_compensation.py
python -m ruff format --check research/l-families/atlas/function_field/ffps_chebyshev_max_cusp_compensation.py tests/test_ffps_chebyshev_max_cusp_compensation.py
~~~
