# One fixed infinite dyadic smoother localizes the RH energy to a subpower frequency window

Status: **exact compact `C^infinity` smoother, zero-free Laplace product,
RH-equivalent band-pass energy, and unconditional superpower spectral-tail
theorem; no low-frequency estimate and no proof of RH or GRH**

Bounded exact replay:
[`ffps_infinite_dyadic_box_bandpass_smoother.py`](ffps_infinite_dyadic_box_bandpass_smoother.py).
Canonical summary:
[`ffps_infinite_dyadic_box_bandpass_smoother.json`](ffps_infinite_dyadic_box_bandpass_smoother.json).

This packet imports the fixed finite band-pass theorem packet at
`05aaabe69060c24c8db4ca33c350e109231960f1` by exact Git blob ID. That
predecessor in turn pins the beta source and boundary/Mellin inputs at PR
#757 head `b870366141fe8d5f43d5b81f6e50a67d2a888070`.

## 0. Outcome

Fix once and for all

\[
 \ell>0,\qquad \varepsilon>0,\qquad r\in\mathbf Z_{\ge1},
\tag{0.1}
\]

and put

\[
 \ell_k={\ell\over2^k},\qquad
 \eta_k={1\over\ell_k}\mathbf1_{[0,\ell_k]}
 \quad(k\ge1).
\tag{0.2}
\]

The infinite causal convolution

\[
 \eta_{\ell,\infty}=\eta_1*\eta_2*\eta_3*\cdots
\tag{0.3}
\]

exists as a compactly supported probability density. In fact

\[
 \boxed{
  \eta_{\ell,\infty}\in C_c^\infty(\mathbf R),\qquad
  \eta_{\ell,\infty}\ge0,\qquad
  \operatorname{supp}\eta_{\ell,\infty}\subset[0,\ell],\qquad
  \int\eta_{\ell,\infty}=1.}
\tag{0.4}
\]

Its Fourier--Laplace transform is the locally uniformly convergent entire
product

\[
 \boxed{
 \Phi_\ell(s)
 =\prod_{k\ge1}
 {1-e^{-\ell s/2^k}\over \ell s/2^k}.}
\tag{0.5}
\]

It has no zero in `Re(s)>0`. On the Fourier axis it has a stronger property.
If

\[
 a=\ell|t|,\qquad M=\lfloor\log_2a\rfloor\ge3,
\]

then

\[
 \boxed{
 |\Phi_\ell(it)|
 \le 2^{-(M-1)(M-2)/2}.}
\tag{0.6}
\]

In particular, for some fixed positive `c,C`,

\[
 |\Phi_\ell(it)|
 \le C\exp\{-c(\log(2+|t|))^2\}.
\tag{0.7}
\]

Let `K_bd` and

\[
 \beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67)
\tag{0.8}
\]

be the source-locked boundary kernel and complete beta source. With the
causal convention `tau_a f(t)=f(t-a)`, define

\[
 \Delta_\varepsilon={1-\tau_\varepsilon\over\varepsilon},
 \qquad
 \boxed{
 B_{r,\infty}
 =\eta_{\ell,\infty}*\Delta_\varepsilon^rK_{\rm bd}.}
\tag{0.9}
\]

This is one fixed, nonzero, compact `C^infinity` band-pass kernel supported
in

\[
 [0,S_{r,\infty}],\qquad
 S_{r,\infty}=4\log2+r\varepsilon+\ell.
\tag{0.10}
\]

For

\[
 H_{r,\infty;X}(u)
 =\sum_{n\le X}{\beta(n)\over\sqrt n}
 B_{r,\infty}(u-\log n),
 \qquad
 \mathcal E_{r,\infty}(X)
 =\int_{\mathbf R}|H_{r,\infty;X}(u)|^2du,
\tag{0.11}
\]

the fixed-kernel RH equivalence survives:

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \mathcal E_{r,\infty}(X)=X^{o(1)}.}
\tag{0.12}
\]

There is also a genuinely stronger unconditional localization. Put

\[
 D_X(t)=\sum_{n\le X}\beta(n)n^{-1/2-it}.
\tag{0.13}
\]

For a fixed

\[
 0<\theta<1/2,
 \qquad
 T_\theta(X)=\exp\{(\log X)^{1/2+\theta}\},
\tag{0.14}
\]

and every `A>0`,

\[
 \boxed{
 {1\over2\pi}
 \int_{|t|\ge T_\theta(X)}
 |\widehat B_{r,\infty}(t)|^2|D_X(t)|^2dt
 =O_{A,\theta,r,\varepsilon,\ell}(X^{-A}).}
\tag{0.15}
\]

Since `T_theta(X)=X^(o(1))`, this localizes the complete unresolved energy
to a genuinely subpower frequency window. For every one fixed
`theta in (0,1/2)`,

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 {1\over2\pi}\int_{|t|\le T_\theta(X)}
 |\widehat B_{r,\infty}(t)|^2|D_X(t)|^2dt
 =X^{o(1)}.}
\tag{0.16}
\]

The older fixed-power statement follows as a weaker corollary: for every
fixed `delta>0`, the tail beyond `X^delta` is also `O_A(X^(-A))`, and the
energy on `|t|<=X^delta` is an RH-equivalent target. The subpower window in
(0.16) is much sharper. This is a localization theorem, not an estimate
inside that window.

## 1. Construction as a probability law

Let `U_k` be independent and uniform on `[0,ell_k]`. Since

\[
 \sum_{k\ge1}\ell_k=\ell,
\tag{1.1}
\]

the series `U=sum_k U_k` converges pointwise and lies in `[0,ell]`. Its law
is the weak limit of the finite convolution measures

\[
 \eta_1*\cdots*\eta_N.
\]

It is therefore a probability measure supported in `[0,ell]`. Dominated
convergence on the characteristic functions gives the product (0.5) on the
Fourier axis. Section 2 shows that this product and all its polynomial
Fourier weights are integrable. Fourier inversion then proves that the
limiting measure has the `C_c^infinity` density asserted in (0.4).

The construction is causal. It neither widens the support beyond the fixed
length `ell` nor introduces a horizon-dependent parameter.

## 2. Exact log-square Fourier envelope and smoothness

Each box factor satisfies

\[
 \left|
 {1-e^{-i\ell_k t}\over i\ell_k t}
 \right|
 \le\min\left(1,{2\over\ell_k|t|}\right)
 =\min\left(1,{2^{k+1}\over a}\right).
\tag{2.1}
\]

Assume `M=floor(log_2 a)>=3`. Keep only the factors
`1<=k<=M-2` and bound every other factor by one. Since `a>=2^M`,

\[
 \begin{aligned}
 |\Phi_\ell(it)|
 &\le\prod_{k=1}^{M-2}2^{k+1-M}\\
 &=2^{\sum_{k=1}^{M-2}(k+1-M)}\\
 &=2^{-(M-1)(M-2)/2}.
 \end{aligned}
\tag{2.2}
\]

This proves the exact stair-step envelope (0.6), and (0.7) follows because
`M=log_2 a+O(1)`. In particular, for every integer `q>=0`,

\[
 t^q\Phi_\ell(it)\in L^1(\mathbf R).
\tag{2.3}
\]

Fourier inversion may therefore be differentiated `q` times for every
`q`. This proves that the probability law from Section 1 has a smooth
density. Its measure support was already contained in `[0,ell]`, so this
density is compactly supported there.

The decay is superpolynomial but not being called exponential in `|t|`.
The precise bound used later is the log-square bound (0.7).

## 3. Entire Laplace product and its zero-free half-plane

For a complex variable `s`, set

\[
 \phi_k(s)={1-e^{-\ell_ks}\over\ell_ks},
\]

with its removable value one at zero. Each `phi_k` is entire. On every
compact set in the `s` plane,

\[
 \phi_k(s)=1-\frac12\ell_ks+O(\ell_k^2|s|^2)
\tag{3.1}
\]

uniformly for all sufficiently large `k`. Because `sum ell_k<infinity`,

\[
 \sum_k\sup_{s\in K}|\phi_k(s)-1|<\infty
\tag{3.2}
\]

for every compact `K`. Thus the product (0.5) converges locally uniformly
to an entire function.

If `Re(s)>0`, no individual factor vanishes: `e^(-ell_k s)=1` would force
`Re(s)=0`. The absolutely convergent tail product is nonzero, and the
remaining finite product is nonzero. Hence

\[
 \boxed{\Phi_\ell(s)\ne0\qquad(\operatorname{Re}s>0).}
\tag{3.3}
\]

Boundary zeros on the imaginary axis are allowed. They are irrelevant to
the Mellin--Landau pole detector, whose hypothetical pole lies strictly in
the right half-plane.

## 4. The fixed band-pass theorem

The predecessor gives

\[
 \widehat K_{\rm bd}(s)={M_{\rm ext}(s)\over s},
\qquad
 \widehat K_{\rm bd}(0)
 =3(1-\sqrt2)^2(\log2)^2\ne0.
\tag{4.1}
\]

Equations (0.5) and (0.9) give

\[
 \boxed{
 \widehat B_{r,\infty}(s)
 =\Phi_\ell(s)
 \left({1-e^{-\varepsilon s}\over\varepsilon}\right)^r
 {M_{\rm ext}(s)\over s}.}
\tag{4.2}
\]

Both added factors are nonzero in `Re(s)>0`. The imported source carrier is
used only in its audited strip `0<Re(s)<1/2`. Hence no hypothetical zeta
zero with real part greater than one half is cancelled in the complete
field transform

\[
 \widehat H_{r,\infty}(s)
 =\widehat B_{r,\infty}(s)
 {1-67^{-(s+1/2)}\over\zeta(s+1/2)}.
\tag{4.3}
\]

The kernel is compact smooth, hence compact BV. It is causal and nonzero;
near zero frequency its transform has exact order `r`. The predecessor's
BV summation, causality/Cauchy, and one-sided Landau argument therefore
applies without a change and proves (0.12). The same argument also gives the
complete-field `L1` and negative-mass equivalents if desired.

The autocorrelation

\[
 \mathcal R_{r,\infty}(u)
 =\int B_{r,\infty}(v)B_{r,\infty}(v+u)dv
\tag{4.4}
\]

has the exact Fourier weight

\[
 \boxed{
 \widehat{\mathcal R}_{r,\infty}(t)
 =|\Phi_\ell(it)|^2
 {\lvert1-e^{-i\varepsilon t}\rvert^{2r}\over\varepsilon^{2r}}
 |\widehat K_{\rm bd}(it)|^2.}
\tag{4.5}
\]

Because `Phi_ell(0)=1`, this has an exact zero of order `2r` at `t=0`.
Because the kernel support is (0.10), its Gram identity still has a fixed
compact ratio band

\[
 e^{-S_{r,\infty}}\le m/n\le e^{S_{r,\infty}}.
\tag{4.6}
\]

Its diagonal is the same harmless logarithmic beta-square diagonal times
the fixed positive number `R_(r,infinity)(0)`.

## 5. Plancherel and unconditional deletion of high frequency

Finite Fourier transformation of (0.11) gives

\[
 \widehat H_{r,\infty;X}(t)
 =\widehat B_{r,\infty}(t)D_X(t).
\]

Plancherel proves the exact identity

\[
 \boxed{
 \mathcal E_{r,\infty}(X)
 ={1\over2\pi}\int_{\mathbf R}
 |\widehat B_{r,\infty}(t)|^2|D_X(t)|^2dt.}
\tag{5.1}
\]

The complete beta source obeys the trivial pointwise bound

\[
 |D_X(t)|
 \le2\sum_{n\le X}n^{-1/2}
 \le4\sqrt X.
\tag{5.2}
\]

The fixed difference multiplier is bounded on the Fourier axis, and
`K_bd_hat` is bounded because `K_bd` is integrable. Thus (0.7) implies

\[
 |\widehat B_{r,\infty}(t)|
 \le C_{r,\varepsilon,\ell}
 \exp\{-c_\ell(\log(2+|t|))^2\}.
\tag{5.3}
\]

For sufficiently large `T`, the substitution `u=log t` gives

\[
 \int_T^\infty e^{-2c(\log t)^2}dt
 =\int_{\log T}^\infty e^{-2cu^2+u}du
 \ll_c e^{-c(\log T)^2}.
\tag{5.4}
\]

For `T=T_theta(X)`, the exponent in (5.4) is

\[
 -c(\log T)^2
 =-c(\log X)^{1+2\theta}.
\tag{5.5}
\]

After multiplication by the `O(X)` square of (5.2), this dominates
`-A log X` for every prescribed `A`, because `theta>0` is fixed. This proves
(0.15). Splitting (5.1) at `T_theta(X)` then proves (0.16) from (0.12).

More generally, the same proof gives superpower deletion for every cutoff
`T(X)` satisfying

\[
 {\log T(X)\over\sqrt{\log X}}\longrightarrow\infty.
\tag{5.6}
\]

Taking `T=X^delta` is an immediate weaker corollary.

No Möbius cancellation is used in (0.14). The tail theorem costs only the
trivial bound `|beta(n)|<=2`.

## 6. What this closes, and what it does not

For this fixed detector, a future Fourier or Perron proof no longer has to
control frequencies beyond `exp((log X)^(1/2+theta))`. The whole exterior
frequency lane is closed unconditionally, with more than any power of
saving.

The remaining window still expands with `X`, and (0.16) asks for
cancellation in the beta Dirichlet polynomial there. Nothing here estimates
that subpower window.

The smoother also does **not** cure the max/Perron cusp. The kernel
`B_(r,infinity)` is a nonzero compact mean-zero function. Therefore the
absolute-lag identity from the band-pass assembled leakage packet still
gives

\[
 \int|u|\mathcal R_{r,\infty}(u)du
 =-2\left\|\int_{-\infty}^{\,x}B_{r,\infty}(v)dv\right\|_2^2<0.
\tag{6.1}
\]

Collapsing a bilateral Perron contour into one max variable therefore still
refills the exact zero-frequency notch at strictly linear order in the
Perron tilt. Infinite smoothing solves the high-frequency problem; it does
not solve the cusp or low-frequency arithmetic problem.

## 7. Fixedness firewall

- `ell`, `epsilon`, and `r` are fixed independently of `X`, `T`, every
  zeta zero, and every Fourier variable.
- The infinitely many dyadic widths are part of one fixed kernel. No
  truncation depth is chosen as a function of the horizon.
- Constants may deteriorate with the fixed parameters. No uniformity as
  `ell` or `epsilon` tends to zero, or as `r` tends to infinity, is claimed.
- The parameter `theta` in (0.14) is fixed in `(0,1/2)`. The displayed
  subpower conclusion is not stated uniformly as `theta` tends to zero.
- The cutoff `T_theta(X)` varies with the horizon, but the detector kernel
  does not. This analytic decomposition is not a horizon-dependent filter.
- Superpower deletion of the high-frequency tail is not a bound for the
  complete energy and is not evidence for RH by itself.

## 8. Proof and scope ledger

| statement | grade |
|---|---|
| infinite convolution probability law and support `[0,ell]` | **PROVED** |
| exact transform product (0.5) and local uniform convergence | **PROVED** |
| right-half-plane zero-freeness of `Phi_ell` | **PROVED** |
| exact stair-step Fourier bound (0.6) | **PROVED** |
| compact `C^infinity` density | **PROVED BY FOURIER INVERSION** |
| compact smooth band-pass kernel and multiplier (4.2) | **PROVED FROM PINNED INPUT** |
| exact zero order `2r`, Gram identity, and compact ratio support | **PROVED** |
| RH-equivalent prefix energy (0.12) | **PROVED BY THE PINNED BV/LANDAU ROUTE** |
| unconditional subpower-window tail bound (0.15) | **PROVED BY (0.6) AND THE TRIVIAL BETA BOUND** |
| subpower-frequency RH criterion (0.16) | **PROVED** |
| any estimate inside `|t|<=T_theta(X)` | **OPEN / NOT PROVED** |
| removal of the Perron cusp leakage | **FALSE FOR THIS NONZERO KERNEL** |
| horizon-dependent narrowing | **OUT OF SCOPE** |
| RH or GRH | **NOT PROVED** |

## 9. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_infinite_dyadic_box_bandpass_smoother.py --check
python -B -O research/l-families/atlas/function_field/ffps_infinite_dyadic_box_bandpass_smoother.py --check
python -B -m unittest tests.test_ffps_infinite_dyadic_box_bandpass_smoother
python -B -O -m unittest tests.test_ffps_infinite_dyadic_box_bandpass_smoother
```

The replay checks exact dyadic support sums, mass preservation in bounded
partial convolutions, the first two Taylor coefficients of finite Laplace
products, preservation and exactness of the band-pass notch, doubling of
the notch in autocorrelation, and the exact binary exponent in (0.6). It
uses only rational arithmetic and tiny fixed arrays. It enumerates no zeta
zero, finite field, curve, conductor family, or L-function.
