# Chebyshev notch depth and max-cusp refill obey a compensation law

Status: **exact primitive energy, exact max-cusp linear refill coefficient,
quadratic refill decay, strictly decreasing cost-refill compensation product,
sharp all-order bounds, and a uniform-in-order relative remainder; no
moving-order Perron estimate, no new beta cancellation, and no proof of RH**

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

The sign is positive. The untilted zero mode vanishes because \(K_r\) has
mean zero, while the absolute-lag moment is negative.

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

For \(r\ge2\), the first moment of \(K_r\) also vanishes, so
\(\int F_r=0\) and the remainder in (0.6) improves from \(O(z^2)\) to
\(O(z^3)\). The linear refill itself remains.

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

On \(0<a_r\le\pi/4\), monotonicity of \(\tan x/x\) gives
\((r+1)^2t_r\le4\), while \(3-t_r\le3\). Therefore

\[
 \boxed{
 \left|
 \frac1{h_r^2}\int R_r(s)e^{-z|s|/2}\,ds-z\kappa_r
 \right|
 \le\frac9{32}z^2\kappa_r}
\tag{2.8}
\]

for every \(r\ge1\). Hence the linear term is relatively dominant as
\(z\to0^+\) uniformly in \(r\); no condition such as \(zr^2\to0\) is needed
for this isolated zero mode. After dilation to width \(W\), the corresponding
small parameter is \(zW\).

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

## 4. What this does and does not say

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

## 5. Scope ledger

| statement | grade |
|---|---|
| exact Chebyshev primitive energy (0.3) | **PROVED** |
| absolute-lag identity specialized to the step | **PROVED** |
| exact positive linear max-cusp refill (0.6) | **PROVED** |
| uniform-in-order relative remainder (2.8) | **PROVED** |
| quadratic normalized refill decay (0.7) | **PROVED** |
| finite nonzero compensation limit (0.9) | **PROVED** |
| strict descent and sharp bounds (0.10) | **PROVED** |
| uniform moving-order Perron estimate | **NOT PROVED** |
| new beta cancellation, RH, or GRH | **NOT PROVED** |

No external novelty or priority is claimed.

## 6. Bounded replay

The producer:

- verifies the frozen autocorrelation quartet by full Git blob ID;
- checks (0.3) independently by analytic cell integration through order
  eight;
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
