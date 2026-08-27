# The fixed-support beta ladder is a mesoscopic spectral microscope

Status: **exact scaling bridge between the fixed-support and diffusive
detector flows, derivative-Gaussian physical and Fourier phase diagram,
subpower-order RH forward theorem, and exact nonmonotonicity firewall; no
growing-order reverse implication, beta cancellation estimate, RH, or GRH
result**

Bounded replay:
[ffps_fixed_support_beta_mesoscopic_microscope.py](ffps_fixed_support_beta_mesoscopic_microscope.py).
Canonical summary:
[ffps_fixed_support_beta_mesoscopic_microscope.json](ffps_fixed_support_beta_mesoscopic_microscope.json).

Frozen sources:

| source quartet | commit |
|---|---|
| zero-free fixed-support beta-energy ladder | **3658d4c31cc866e15d48ab1fc9d8d119136da424** |
| tilted-tent detector renormalization flow | **46ea68808e238b0c9b85050158ba149649b1b37e** |

The producer pins all eight Git blobs. No live source module is imported.

## 0. Outcome

Let

\[
 \Phi(x)=e^{x-1}(1-|x-1|)_+,\qquad
 P={\Phi\over\int\Phi},
\tag{0.1}
\]

and write

\[
 \mu=\mathbf E_PX={2\over e-1},\qquad
 \sigma^2=\operatorname {Var}_P X
 ={2(e^2-3e+1)\over(e-1)^2}.
\tag{0.2}
\]

There are three natural versions of the order-\(m\) detector:

\[
\begin{aligned}
 U_m(x)&=D(P^{*m})(x),\\
 C_m(x)&=D\!\left[mP^{*m}(mx)\right],\\
 G_m(y)&=m\sigma^2U_m(m\mu+\sigma\sqrt m\,y).
\end{aligned}
\tag{0.3}
\]

Here \(U_m\) is the uncompressed causal detector, \(C_m\) is the
fixed-support beta-ladder detector, and \(G_m\) is the centered diffusive
detector. They are not merely analogous:

\[
\boxed{
 C_m(x)=m^2U_m(mx)
 ={m\over\sigma^2}
 G_m\!\left({\sqrt m(x-\mu)\over\sigma}\right).}
\tag{0.4}
\]

This identity turns the two predecessor packets into one phase diagram.
If \(\mathcal R_m^C\) and \(\mathcal R_m^G\) are the two detector
autocorrelations, then

\[
\boxed{
 {\sigma^3\over m^{3/2}}
 \mathcal R_m^C\!\left({\sigma v\over\sqrt m}\right)
 =\mathcal R_m^G(v)
 \longrightarrow
 {1\over4\sqrt\pi}
 \left(1-{v^2\over2}\right)e^{-v^2/4}}
\tag{0.5}
\]

uniformly in \(v\in\mathbb R\). The fixed ratio band remains
\(e^{-2}\le a/b\le e^2\), but its dominant signed geometry contracts to
logarithmic width \(m^{-1/2}\).

On the Fourier side, if

\[
 w_m(t)=|\widehat C_m(t)|^2,
\qquad
 \widetilde w_m(\tau)
 ={\sigma^2\over m}
 w_m\!\left({\sqrt m\over\sigma}\tau\right),
\tag{0.6}
\]

then

\[
\boxed{
 \widetilde w_m(\tau)
 =\tau^2
 \left|\widehat P\!\left({\tau\over\sigma\sqrt m}\right)\right|^{2m}
 \longrightarrow \tau^2e^{-\tau^2}}
\tag{0.7}
\]

locally uniformly and in \(L^1(\mathbb R)\). Thus increasing the
fixed-support order does not keep suppressing Fourier frequencies. It
creates a spectral microscope whose natural frequency scale is
\(\sqrt m/\sigma\).

For the literal beta Dirichlet polynomial

\[
 D_X(t)=\sum_{n\le X}{\beta(n)\over n^{1/2+it}},
\tag{0.8}
\]

Parseval and (0.6) give the exact identity

\[
\boxed{
 {\sigma^3\over m^{3/2}}\mathcal E_m(X)
 ={1\over2\pi}\int_{\mathbb R}
 \widetilde w_m(\tau)
 \left|D_X\!\left({\sqrt m\over\sigma}\tau\right)\right|^2d\tau.}
\tag{0.9}
\]

At the already isolated critical frequency

\[
 T_*(X)=\exp\sqrt{(\log2)(\log X)},
\tag{0.10}
\]

choose

\[
\boxed{
 m_*(X)=\left\lceil\sigma^2T_*(X)^2\right\rceil=X^{o(1)}.}
\tag{0.11}
\]

Then the Gaussian microscope in (0.9) is centered on the same frequency
scale as the remaining beta witness window. This is an exact scale match,
not an estimate of \(D_X\).

There is one unconditional growing-order implication:

\[
\boxed{
 \mathrm{RH}
 \Longrightarrow
 \mathcal E_{m(X)}(X)=X^{o(1)}
 \quad\text{for every integer }m(X)=X^{o(1)}.}
\tag{0.12}
\]

The converse is not proved. The weights are not pointwise ordered in
\(m\), so positivity supplies no comparison back to a fixed RH-equivalent
rung.

## 1. Exact bridge between the two flows

Put

\[
 K_m=P^{*m}.
\tag{1.1}
\]

The fixed-support density is

\[
 Q_m(x)=mK_m(mx).
\tag{1.2}
\]

Differentiation gives

\[
 C_m(x)=Q_m'(x)=m^2K_m'(mx)=m^2U_m(mx).
\tag{1.3}
\]

The centered density from the renormalization packet is

\[
 f_m(y)=\sigma\sqrt m\,
 K_m(m\mu+\sigma\sqrt m\,y),
\tag{1.4}
\]

and \(G_m=f_m'\). Hence

\[
 G_m(y)=m\sigma^2
 U_m(m\mu+\sigma\sqrt m\,y).
\tag{1.5}
\]

Substitute

\[
 y={\sqrt m(x-\mu)\over\sigma}
\tag{1.6}
\]

into (1.5) to obtain (0.4).

If

\[
 \mathcal R_m^C(u)=\int C_m(x)C_m(x+u)\,dx,
\quad
 \mathcal R_m^G(v)=\int G_m(y)G_m(y+v)\,dy,
\tag{1.7}
\]

then (0.4) and \(dx=\sigma\,dy/\sqrt m\) give the exact
autocorrelation bridge

\[
 \boxed{
 \mathcal R_m^C(u)
 ={m^{3/2}\over\sigma^3}
 \mathcal R_m^G\!\left({\sqrt m\,u\over\sigma}\right).}
\tag{1.8}
\]

The uniform derivative-Gaussian autocorrelation theorem in the pinned
renormalization packet now proves (0.5).

## 2. The physical sign tubes

The limiting kernel

\[
 \mathcal R_\infty(v)
 ={1\over4\sqrt\pi}
 \left(1-{v^2\over2}\right)e^{-v^2/4}
\tag{2.1}
\]

is positive for \(|v|<\sqrt2\), zero at \(|v|=\sqrt2\), and negative
for \(|v|>\sqrt2\).

Fix

\[
 0<\varepsilon<\sqrt2,\qquad A>\sqrt2+\varepsilon.
\tag{2.2}
\]

Uniform convergence in (0.5) implies that, for all sufficiently large
\(m\),

\[
\begin{aligned}
 \mathcal R_m^C(u)&>0
 &&\left(|u|\le{\sigma(\sqrt2-\varepsilon)\over\sqrt m}\right),\\
 \mathcal R_m^C(u)&<0
 &&\left(
 {\sigma(\sqrt2+\varepsilon)\over\sqrt m}
 \le|u|\le{\sigma A\over\sqrt m}
 \right).
\end{aligned}
\tag{2.3}
\]

There is therefore at least one sign-changing node between the two tubes.
No uniqueness theorem for the finite-\(m\) node is asserted.

For source indices \(a,b>0\), \(u=\log(a/b)\). The positive tube is

\[
 \exp\!\left(-{\sigma(\sqrt2-\varepsilon)\over\sqrt m}\right)
 \le {a\over b}\le
 \exp\!\left({\sigma(\sqrt2-\varepsilon)\over\sqrt m}\right),
\tag{2.4}
\]

while the two reciprocal negative tubes begin at
\(\exp(\pm\sigma(\sqrt2+\varepsilon)/\sqrt m)\).

This is a mesoscopic localization theorem, not a cancellation theorem.
The products \(\beta(a)\beta(b)\) retain their own signs, and the full
quadratic form must remain assembled.

## 3. Fourier microscope and noncommuting scales

The fixed-support transform is

\[
 \widehat C_m(t)
 =it\,\widehat P(t/m)^m.
\tag{3.1}
\]

At

\[
 t={\sqrt m\over\sigma}\tau,
\tag{3.2}
\]

equation (3.1) gives (0.6)--(0.7) exactly. The pinned Fourier-splitting
theorem supplies both local uniform convergence and global
\(L^1\)-convergence.

The phase diagram is:

~~~text
fixed t, m -> infinity
  w_m(t) -> t^2;

t = sqrt(m) tau / sigma
  (sigma^2/m) w_m(t) -> tau^2 exp(-tau^2);

fixed m, |t| -> infinity
  w_m(t) is of order |t|^(2-4m).
~~~

These limits do not commute. High-frequency decay begins progressively
farther out as \(m\) grows.

The weights are not even pointwise monotone in the order. At
\(t=4\pi\),

\[
 {w_1(4\pi)\over(4\pi)^2}
 ={1\over(1+16\pi^2)^2},
\qquad
 {w_2(4\pi)\over(4\pi)^2}
 ={1\over(1+4\pi^2)^4}.
\tag{3.3}
\]

Since

\[
 (1+4\pi^2)^2-(1+16\pi^2)
 =8\pi^2(2\pi^2-1)>0,
\tag{3.4}
\]

\[
 \boxed{w_2(4\pi)<w_1(4\pi).}
\tag{3.5}
\]

But (0.7) at fixed \(t\) gives

\[
 w_m(4\pi)\longrightarrow(4\pi)^2>w_1(4\pi).
\tag{3.6}
\]

Thus the order first lowers and later raises this exact frequency weight.
There is no Loewner comparison of the full energies coming from
pointwise Fourier domination.

## 4. Norm, Jordan, and moment laws

The exact bridge and the pinned norm expansion give

\[
\boxed{
 \|C_m\|_2^2
 ={m^{3/2}\over4\sqrt\pi\,\sigma^3}
 \left(
 1+{5\lambda_4\over16m}+O(m^{-2})
 \right).}
\tag{4.1}
\]

The density \(f_m\) is log-concave. The pinned Jordan theorem and (0.4)
give

\[
\boxed{
 \int(C_m)_+\,dx
 =\int(C_m)_-\,dx
 ={\sqrt m\over\sigma\sqrt{2\pi}}(1+o(1)).}
\tag{4.2}
\]

The cumulative of \(C_m\) is \(Q_m\), and

\[
 \|Q_m\|_2^2
 ={\sqrt m\over\sigma}\|f_m\|_2^2
 ={\sqrt m\over2\sqrt\pi\,\sigma}
 \left(1+{\lambda_4\over16m}+O(m^{-2})\right).
\tag{4.3}
\]

For every compact mean-zero derivative detector,

\[
 \int_{\mathbb R}|u|\mathcal R(u)\,du
 =-2\|\text{cumulative}\|_2^2.
\tag{4.4}
\]

Consequently

\[
\boxed{
 \int_{\mathbb R}|u|\mathcal R_m^C(u)\,du
 =-{\sqrt m\over\sqrt\pi\,\sigma}
 \left(1+{\lambda_4\over16m}+O(m^{-2})\right).}
\tag{4.5}
\]

Two other moments are exact for every \(m\):

\[
\boxed{
 \int\mathcal R_m^C(u)\,du=0,
 \qquad
 \int u^2\mathcal R_m^C(u)\,du=-2.}
\tag{4.6}
\]

The first follows from \(\int C_m=0\). For the second,

\[
 \int xC_m(x)\,dx=-\int Q_m(x)\,dx=-1,
\tag{4.7}
\]

and expansion of \((y-x)^2\) gives (4.6). These exact moment constraints
explain why the increasingly tall and narrow signed core cannot converge
as an ordinary integrable kernel.

## 5. Exact beta-energy rescaling

For

\[
 \beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67),
\tag{5.1}
\]

define

\[
 H_{m;X}(x)=\sum_{n\le X}{\beta(n)\over\sqrt n}
 C_m(x-\log n),
\qquad
 \mathcal E_m(X)=\|H_{m;X}\|_2^2.
\tag{5.2}
\]

Finite Parseval gives

\[
 \mathcal E_m(X)
 ={1\over2\pi}\int_{\mathbb R}
 w_m(t)|D_X(t)|^2dt.
\tag{5.3}
\]

Use (0.6) and \(dt=\sqrt m\,d\tau/\sigma\). This proves (0.9)
without a limit, endpoint smoothing, or discarded frequency.

The critical scale (0.10) was obtained independently from the infinite
dyadic beta smoother: frequencies above \(T_*(X)\) are already harmless
at the \(X^{o(1)}\) level, while the inside remains RH-bearing. Equation
(0.11) gives

\[
 {\sqrt{m_*(X)}\over\sigma}
 =T_*(X)(1+o(1))
\tag{5.4}
\]

and

\[
 \log m_*(X)
 =2\sqrt{(\log2)(\log X)}+O(1)
 =o(\log X).
\tag{5.5}
\]

Thus one fixed-support detector flow naturally reaches the unresolved
frequency frontier while keeping both its order and its norm cost
subpower. No bound for the right side of (0.9) follows from this scale
match.

## 6. RH implies every subpower-order energy bound

Assume RH. The classical Mertens formulation and the finite
duplicate-\(67\) source relation give, for every fixed \(\delta>0\),

\[
 \sum_{n\le y}\beta(n)=O_\delta(y^{1/2+\delta}).
\tag{6.1}
\]

Partial summation gives

\[
 B(y):=\sum_{n\le y}{\beta(n)\over\sqrt n}
 =O_\delta(y^\delta).
\tag{6.2}
\]

The kernel cost is polynomial in \(m\). Since

\[
 C_m(x)=m^2D(P^{*m})(mx),
\tag{6.3}
\]

convolution by the probability density \(P^{*(m-1)}\) contracts total
variation. The explicit piecewise exponential-linear \(P\) has a finite
second distributional derivative, so

\[
 \operatorname {Var}(C_m)
 \le m^2\|D^2P\|_{\mathrm {TV}},
\qquad
 \|C_m\|_\infty\ll m^2.
\tag{6.4}
\]

Abel summation of (5.2) against (6.2), on the fixed causal support
\([0,2]\), yields

\[
 \sup_{x\le\log X+2}|H_{m;X}(x)|
 \ll_\delta m^2X^\delta.
\tag{6.5}
\]

The field has support of length \(O(\log X)\). Hence

\[
 \mathcal E_m(X)
 \ll_\delta m^4X^{2\delta}(1+\log X).
\tag{6.6}
\]

If \(m=m(X)=X^{o(1)}\), then for each prescribed \(\varepsilon>0\)
choose a fixed sufficiently small \(\delta\). Eventually the right side
of (6.6) is at most \(X^\varepsilon\). This proves (0.12), including the
critical choice \(m_*(X)\).

The proof uses RH. It is not an unconditional estimate of the critical
window.

## 7. Why the reverse direction remains open

For every one fixed \(m\), the pinned Mellin--Landau argument proves

\[
 \mathrm{RH}\Longleftrightarrow
 \mathcal E_m(X)=X^{o(1)}.
\tag{7.1}
\]

This does not permit \(m=m(X)\). The carrier, BV constants, and field all
change with the horizon. A pole created by one hypothetical off-line zero
is being tested by a different entire multiplier at each \(X\).

The most tempting shortcut would compare the growing-order weight to one
fixed weight. Equations (3.3)--(3.6) refute global pointwise monotonicity,
so positivity of the spectral integral gives no such comparison.

The exact open gate isolated by this packet is:

\[
 \mathcal E_{m_*(X)}(X)=X^{o(1)}
 \quad\stackrel{?}{\Longrightarrow}\quad
 \mathrm{RH}.
\tag{7.2}
\]

No implication in (7.2) is claimed. A successful reverse theorem would
need one of:

- a uniform moving-carrier Landau theorem;
- a comparison preserving signed frequency assembly;
- a rigidity theorem forcing a fixed-frequency witness to survive the
  moving Gaussian microscope;
- or a reconstruction of one fixed detector from a controlled bank of
  subpower orders.

The last option is a genuine inverse-design problem. It cannot be replaced
by taking absolute values frequency by frequency.

## 8. Scope ledger

| statement | grade |
|---|---|
| exact three-flow scaling identity (0.4) | **PROVED EXACT** |
| scaled autocorrelation and weight limits (0.5), (0.7) | **PROVED FROM THE PINNED RENORMALIZATION THEOREM** |
| mesoscopic positive and negative tubes (2.3) | **PROVED** |
| norm, Jordan, and moment laws | **PROVED** |
| exact rescaled beta energy (0.9) | **PROVED EXACT** |
| critical scale match (0.11) | **PROVED EXACT ASYMPTOTICALLY** |
| RH forward theorem for every \(m(X)=X^{o(1)}\) | **PROVED** |
| pointwise order monotonicity | **FALSE** |
| critical growing-order reverse implication | **NOT PROVED** |
| beta cancellation estimate | **NOT PROVED** |
| RH or GRH | **NOT PROVED** |

No external novelty or priority is claimed without a dedicated literature
comparison.

## 9. Bounded replay

The producer:

- checks all eight frozen Git blobs;
- evaluates orders \(4,16,64\) at five bounded scaled frequencies;
- performs three \(8192\)-panel compact Simpson regressions for the
  normalized energy and five autocorrelation points per order;
- verifies the exact \(t=4\pi\) nonmonotonicity control numerically after
  the displayed symbolic proof;
- records the critical-scale ratios at three logarithmic horizons.

The quadrature is a regression only. Equations (0.4)--(7.2) are proved
analytically above. The replay evaluates no zeta zero, numerical zeta
value, prime, curve, finite field, random sample, long beta sum, or
contour.

~~~text
python -B research/l-families/atlas/function_field/ffps_fixed_support_beta_mesoscopic_microscope.py --check
python -O -B research/l-families/atlas/function_field/ffps_fixed_support_beta_mesoscopic_microscope.py --check
python -B -m pytest -q tests/test_ffps_fixed_support_beta_mesoscopic_microscope.py
python -O -B -m pytest -q tests/test_ffps_fixed_support_beta_mesoscopic_microscope.py
python -m ruff check research/l-families/atlas/function_field/ffps_fixed_support_beta_mesoscopic_microscope.py tests/test_ffps_fixed_support_beta_mesoscopic_microscope.py
python -m ruff format --check research/l-families/atlas/function_field/ffps_fixed_support_beta_mesoscopic_microscope.py tests/test_ffps_fixed_support_beta_mesoscopic_microscope.py
~~~
