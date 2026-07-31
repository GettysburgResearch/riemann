# L-17801 — Periodized Fourier enclosure for smooth box-convolution windows

Claim ID: `L-17801`  
Title: A compact infinite box convolution admits a finite Fourier, tail, and cubic-interpolation certificate  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-09-g`  
Created: 2026-07-31  
Dependencies: `L-15405`, `L-15406`, `L-15408`; elementary Fourier series and interpolation  
Scope: proof-producing evaluation of the five-notch pole-free prime window in Issue #178

## 1. Exact periodic coefficients

Let `r_1,...,r_m>0` be finitely many notch-box widths and append the dyadic
box widths `2^-j`, `j>=1`. Put

\[
 S=\sum_{i=1}^m r_i+\sum_{j\ge1}2^{-j}
  =1+\sum_{i=1}^m r_i.
\]

Let `f` be the probability density of the sum of the corresponding independent
uniform random variables and let

\[
 F_0=f*f.
\]

Then `F_0` is smooth, nonnegative, and supported on `[0,2S]`. Choose any period
`P>2S`, extend `F_0` periodically, and put

\[
 \omega_k=\frac{2\pi k}{P},\qquad \operatorname{sinc}x=\frac{\sin x}{x}.
\]

Its exact Fourier series is

\[
 \boxed{F_0(y)=\sum_{k\in\mathbb Z}c_ke^{i\omega_ky}}
\]

with

\[
 \boxed{
 c_k=\frac1P e^{-i\omega_kS}
 \prod_{i=1}^m\operatorname{sinc}^2\!\left(\frac{\omega_kr_i}{2}\right)
 \prod_{j=1}^{\infty}\operatorname{sinc}^2\!\left(\frac{\omega_k2^{-j}}2\right).
 }
 \tag{1}
\]

The formula follows by multiplying the transforms of the uncentered box laws
and squaring for the independent convolution copy. Since the compact density and
all derivatives vanish at the support endpoints, the periodic extension is
`C^infinity`.

## 2. Closed coefficient and derivative tails

For integers `J>=1`, `q>=0`, and `2J>q+1`, the first `J` dyadic factors give

\[
 |c_k|\le \frac1P 2^{J(J+3)}|\omega_k|^{-2J}.
\]

Therefore, for every integer cutoff `K>=1`,

\[
 \boxed{
 \sum_{|k|>K}|\omega_k|^q|c_k|
 \le
 \frac2P2^{J(J+3)}
 \left(\frac{2\pi}{P}\right)^{q-2J}
 \frac{K^{q+1-2J}}{2J-q-1}.
 }
 \tag{2}
\]

Proof: use `|sinc x|<=min(1,1/|x|)` on the first `J` dyadic factors and the
integral bound for the decreasing power tail.

For the production parameters

```text
P=8, J=10, K=4096,
```

and the elementary lower bound `pi>3`, (2) gives exactly

\[
 \sum_{|k|>4096}|c_k|
 <\frac1{76379785638971469800505606144}
 <1.4\times10^{-29},
 \tag{3}
\]

\[
 \sum_{|k|>4096}|\omega_k|^4|c_k|
 <\frac1{677066377789440}
 <1.5\times10^{-15}.
 \tag{4}
\]

Thus a finite coefficient table plus (2) rigorously encloses both the window and
the fourth derivative needed below.

## 3. Finite dyadic-product enclosure

For every real `x`,

\[
 \operatorname{sinc}^2x\ge 1-\frac{x^2}{3}.
\]

Consequently, after retaining the first `J_0` dyadic factors,

\[
 \boxed{
 1-\frac{\omega^2 4^{-J_0}}{36}
 \le
 \prod_{j>J_0}\operatorname{sinc}^2
       \left(\frac{\omega2^{-j}}2\right)
 \le1,
 }
 \tag{5}
\]

whenever the displayed lower endpoint is nonnegative. The left inequality uses
`prod(1-a_j)>=1-sum a_j` and the geometric series. This gives a directed finite
coefficient producer without truncating the infinite-convolution definition.

## 4. Four-point cubic enclosure

Let `h=P/N`, `y_n=nh`, and let `I_3F_0(y)` be the cubic interpolant through
`y_(n-1),y_n,y_(n+1),y_(n+2)` when `y in [y_n,y_(n+1)]`. The interpolation
remainder is

\[
 F_0(y)-I_3F_0(y)
 =\frac{F_0^{(4)}(\xi)}{4!}
 h^4(t+1)t(t-1)(t-2),\qquad t=\frac{y-y_n}{h}.
\]

Since

\[
 \max_{0\le t\le1}|(t+1)t(t-1)(t-2)|=\frac9{16},
\]

one has

\[
 \boxed{
 |F_0(y)-I_3F_0(y)|
 \le\frac3{128}h^4\|F_0^{(4)}\|_\infty.
 }
 \tag{6}
\]

If the argument is known only within radius `rho_y`, add

\[
 \|F_0'\|_\infty\rho_y.
 \tag{7}
\]

The derivative norms are bounded by the retained Fourier coefficients plus (2).
All four grid intervals, interpolation arithmetic, and argument radii may be
combined outward.

## 5. Pole-free window and prime sum

For `h_0=log 4`, define

\[
 G_*(u)=F_0(u-2)-2F_0(u-h_0-2).
 \tag{8}
\]

At an exact translation `x`, every prime-power argument is enclosed from a
directed logarithm interval. Evaluating the two correlated periodic values by
(1)--(7), multiplying by the directed weight `Lambda(n)/sqrt(n)`, and summing
outward encloses the complete finite pole-free statistic.

No FFT interpolation midpoint enters the trust boundary: the FFT supplies a
finite trigonometric-polynomial grid with propagated arithmetic discs; (2), (5),
and (6) supply the analytic tail and off-grid moat.

## 6. Production specialization

The five-notch design uses the exact decimal-rational ordinates

```text
14.13472514173469379045725198356247
21.02203963877155499262847959389690
25.01085758014568876321379099256282
30.42487612585951321031189753058409
32.93506158773918969066236896407490
```

with widths `r_i=2*pi/gamma_i`, period `P=8`, coefficient cutoff `K=4096`,
64 explicitly enclosed dyadic factors, and grid `N=2^20`.

The theorem is exact. The retained C producer is a first implementation using
256-bit MPFR input intervals and a conservative binary128 complex-disc FFT. Its
roundoff propagation is intentionally over-wide and requires an independent
implementation audit before the resulting prime interval is promoted as a
project certificate.

## Proof boundary

- The Fourier, tail, and interpolation inequalities are analytic statements.
- A production result also requires a reviewed floating-disc arithmetic proof,
  complete prime-power enumeration, and independent replay.
- The exact decimal design ordinates define the window; their relation to actual
  zeta-zero balls is a separate notch-attenuation gate.
- This lemma evaluates the prime window. It does not itself supply the RH-valid
  zero-side phase band.
