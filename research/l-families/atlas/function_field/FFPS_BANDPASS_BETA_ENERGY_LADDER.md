# Fixed band-pass beta energies form an exact RH-equivalent ladder

Status: **exact fixed-parameter kernel, Mellin, spectral, Gram, and
RH-equivalence theorem; no band-pass estimate and no proof of RH or GRH**

Bounded exact replay:
[`ffps_bandpass_beta_energy_ladder.py`](ffps_bandpass_beta_energy_ladder.py).
Canonical summary:
[`ffps_bandpass_beta_energy_ladder.json`](ffps_bandpass_beta_energy_ladder.json).

Frozen source: PR #757 head
`b870366141fe8d5f43d5b81f6e50a67d2a888070`. The replay pins the Markdown,
producer, JSON, and test blobs imported from the extra-notched consumer, the
fixed-mollified beta criterion, the boundary-field packet, and the boundary
near-correlation packet.

## 0. Outcome

Let

\[
 \beta(n)=\mu(n)-\mathbf 1_{67\mid n}\mu(n/67),
\tag{0.1}
\]

and let `K_bd` be the source-locked compact bounded-variation boundary
kernel. Thus

\[
 \operatorname{supp}K_{\rm bd}\subset[0,4\log2],
 \qquad DK_{\rm bd}=K_{\rm ext}.
\tag{0.2}
\]

Use the causal translation convention

\[
 (\tau_a f)(t)=f(t-a)
\]

and fix, once and for all,

\[
 \varepsilon>0,\qquad \ell>0,\qquad
 r\in\mathbf Z_{\ge1},\qquad j\in\mathbf Z_{\ge0}.
\tag{0.3}
\]

Put

\[
 \Delta_\varepsilon={1-\tau_\varepsilon\over\varepsilon},
 \qquad
 \eta_\ell={1\over\ell}\mathbf1_{[0,\ell]},
 \qquad \eta_\ell^{*0}=\delta_0,
\tag{0.4}
\]

and define the fixed **band-pass kernel**

\[
 \boxed{
 B_{r,j}=\eta_\ell^{*j}*\Delta_\varepsilon^rK_{\rm bd}.}
\tag{0.5}
\]

The finite differences supply the high-pass notch. The causal boxes supply
optional fixed low-pass smoothing. The kernel is a nonzero compact BV
function supported in

\[
 [0,S_{r,j}],
 \qquad
 S_{r,j}=4\log2+r\varepsilon+j\ell.
\tag{0.6}
\]

For `X>=1`, define

\[
 H_{r,j;X}(t)
 =\sum_{n\le X}{\beta(n)\over\sqrt n}
 B_{r,j}(t-\log n),
 \qquad
 \mathcal E_{r,j}(X)
 =\int_{\mathbf R}|H_{r,j;X}(t)|^2dt.
\tag{0.7}
\]

Then every fixed member of this ladder is an exact RH criterion:

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \mathcal E_{r,j}(X)=X^{o(1)}.}
\tag{0.8}
\]

More precisely, if `H_(r,j)` denotes the complete causal field, then

\[
 \boxed{
 \begin{aligned}
 \mathrm{RH}
 &\Longleftrightarrow
 \int_0^T|H_{r,j}(t)|dt=e^{o(T)}\\
 &\Longleftrightarrow
 \int_0^T(H_{r,j}(t))_-dt=e^{o(T)}\\
 &\Longleftrightarrow
 \mathcal E_{r,j}(X)=X^{o(1)}.
 \end{aligned}}
\tag{0.9}
\]

Here, as in the source packets, `e^(o(T))` means
`O_delta(e^(delta T))` for every `delta>0`, and `X^(o(1))` has the analogous
all-positive-exponent meaning.

The autocorrelation

\[
 \mathcal R_{r,j}(u)
 =\int_{\mathbf R}B_{r,j}(v)B_{r,j}(v+u)dv
\tag{0.10}
\]

has Fourier weight

\[
 \boxed{
 \widehat{\mathcal R}_{r,j}(t)
 ={\lvert1-e^{-i\varepsilon t}\rvert^{2r}\over\varepsilon^{2r}}
 \lvert\widehat\eta_\ell(t)\rvert^{2j}
 \lvert\widehat K_{\rm bd}(t)\rvert^2.}
\tag{0.11}
\]

It has an exact zero of order `2r` at `t=0`, while the `j` boxes give

\[
 \widehat{\mathcal R}_{r,j}(t)
 =O_{r,j,\varepsilon,\ell}((1+|t|)^{-2j-2})
 \qquad(|t|\longrightarrow\infty).
\tag{0.12}
\]

Thus one may suppress the exact zero-frequency Gram channel to arbitrary
fixed order and independently add arbitrary fixed polynomial
high-frequency decay, without destroying the Mellin pole detector. This is
a coordinate theorem, not an estimate for the resulting arithmetic energy.

## 1. Frozen inputs

The packet imports four results, all source-locked by the replay.

1. `K_ext` is a compact finite signed logarithmic measure supported in
   `[0,4log2]`, has total mass zero, and has the factor `D`.
2. Its causal primitive `K_bd` is a nonzero compact BV function on the same
   interval and

   \[
    \widehat K_{\rm bd}(s)={M_{\rm ext}(s)\over s}.
   \tag{1.1}
   \]

3. The complete beta field with kernel `K_bd`, and its first fixed
   difference, have the source-locked Mellin--Landau pole mechanism.
4. The beta-square diagonal satisfies

   \[
    \sum_{n\le X}{\beta(n)^2\over n}
    ={2379\over2278\zeta(2)}\log X+O(1).
   \tag{1.2}
   \]

For clarity, the explicit source multiplier is

\[
 M_{\rm ext}(s)
 ={q(s)^2\rho_0(s)^2(s-1)(5s+3/2)\over s(s-1/2)},
\tag{1.3}
\]

where

\[
 q(s)=1-\sqrt2\,2^{-s},
 \qquad
 \rho_0(s)=1-2^{-s}.
\]

The notation `rho_0` here is only an elementary multiplier and has no
connection to a zeta zero or to the `rho` tilt of the primitive-pair packet.
The imported audit proves that `M_ext` is nonzero in

\[
 0<\operatorname{Re}s<1/2.
\tag{1.4}
\]

No broader carrier nonvanishing assertion is needed below.

## 2. Compactness, BV, support, and nontriviality

For a compact BV function `f`, every translate is compact BV and

\[
 \operatorname{Var}((1-\tau_\varepsilon)f)
 \le2\operatorname{Var}(f).
\tag{2.1}
\]

Iteration gives

\[
 \operatorname{Var}(\Delta_\varepsilon^rf)
 \le(2/\varepsilon)^r\operatorname{Var}(f).
\tag{2.2}
\]

Convolution by the probability density `eta_ell` does not increase total
variation. Consequently `B_(r,j)` is BV. It is also bounded and belongs to
`L1 intersect L2`.

The translation `tau_epsilon` moves `[0,A]` to
`[epsilon,A+epsilon]`. Hence

\[
 \operatorname{supp}(\Delta_\varepsilon^rK_{\rm bd})
 \subset[0,4\log2+r\varepsilon].
\]

Each causal box adds `[0,ell]` under convolution, proving (0.6).

Finally `B_(r,j)` is not identically zero. Indeed its entire
Fourier--Laplace transform is the product in the next section. The transform
of `K_bd` is not identically zero, and neither finite-difference nor box
factor is the zero entire function. Their product therefore cannot vanish
identically.

## 3. Exact Mellin multiplier and pole preservation

For `Re(s)>0`, the causal box has transform

\[
 \widehat\eta_\ell(s)
 ={1-e^{-\ell s}\over\ell s},
\tag{3.1}
\]

with the value at `s=0` understood by removal. Translation gives

\[
 \widehat{\Delta_\varepsilon f}(s)
 ={1-e^{-\varepsilon s}\over\varepsilon}\widehat f(s).
\tag{3.2}
\]

Thus

\[
 \boxed{
 \widehat B_{r,j}(s)
 =\left({1-e^{-\varepsilon s}\over\varepsilon}\right)^r
  \left({1-e^{-\ell s}\over\ell s}\right)^j
  {M_{\rm ext}(s)\over s}.}
\tag{3.3}
\]

The two added filter factors have no zero in `Re(s)>0`: an equality
`e^(-as)=1`, with `a>0`, forces `Re(s)=0`. The denominator in (3.1) has
only a removable singularity at zero.

This statement must not be misread as claiming that the whole carrier
`M_ext(s)/s` is zero-free throughout the right half-plane. What the RH
consumer needs is exactly the source-audited strip (1.4). In
`0<Re(s)<1/2`, every factor in (3.3) is nonzero.

Initially in `Re(s)>1/2`, absolute Mellin--Stieltjes Fubini gives the complete
field transform

\[
 \boxed{
 \widehat H_{r,j}(s)
 =\widehat B_{r,j}(s)
 {1-67^{-(s+1/2)}\over\zeta(s+1/2)}.}
\tag{3.4}
\]

If a zeta zero `zeta_zero` has `Re(zeta_zero)>1/2`, then

\[
 s_0=\zeta_{\rm zero}-1/2
\]

lies in the source strip. Neither the duplicate-`67` numerator, the imported
carrier, nor either fixed filter multiplier vanishes there. Therefore the
pole at `s_0` is genuine. Every fixed member of the band-pass ladder retains
the same off-line-zero detector.

## 4. Exact low- and high-frequency behavior

Use the real Fourier convention

\[
 \widehat f(t)=\int_{\mathbf R}f(x)e^{-itx}dx.
\]

Since `B_(r,j)` is real and in `L2`, Wiener--Khinchin gives

\[
 \widehat{\mathcal R}_{r,j}(t)=|\widehat B_{r,j}(t)|^2,
\tag{4.1}
\]

which proves (0.11).

The order at zero is exact rather than merely a lower bound. From (1.3),

\[
 \rho_0(s)=(\log2)s+O(s^2)
\]

and hence

\[
 \boxed{
 \widehat K_{\rm bd}(0)
 =\lim_{s\to0}{M_{\rm ext}(s)\over s}
 =3(1-\sqrt2)^2(\log2)^2\ne0.}
\tag{4.2}
\]

Moreover

\[
 {1-e^{-i\varepsilon t}\over\varepsilon}
 =it+O(t^2),
 \qquad
 \widehat\eta_\ell(t)=1+O(t).
\]

Therefore

\[
 |\widehat B_{r,j}(t)|^2
 =|\widehat K_{\rm bd}(0)|^2|t|^{2r}(1+O(|t|)),
\tag{4.3}
\]

proving exact order `2r`.

For high frequency,

\[
 |\widehat\eta_\ell(t)|
 \le\min\left(1,{2\over\ell|t|}\right).
\tag{4.4}
\]

A compact BV function has Fourier transform `O(1/|t|)`, while the fixed
difference factor is bounded by `(2/epsilon)^r`. This proves (0.12).

At the first rung, `r=1,j=0`, expand the two differences directly to get

\[
 \boxed{
 \mathcal R_{1,0}(u)
 ={2\mathcal R_{\rm bd}(u)
   -\mathcal R_{\rm bd}(u-\varepsilon)
   -\mathcal R_{\rm bd}(u+\varepsilon)
  \over\varepsilon^2}.}
\tag{4.5}
\]

This is the exact bridge from the boundary-field Gram kernel to the
fixed-mollified current kernel.

## 5. The RH-equivalent energy theorem

### 5.1 RH implies the prefix energy bound

Under RH, the source-locked normalized beta summatory function satisfies

\[
 A_\beta(x)=\sum_{n\le x}{\beta(n)\over\sqrt n}
 =O_\delta(x^\delta)
\tag{5.1}
\]

for every `delta>0`. Stieltjes summation against one translate of the fixed
compact BV kernel `B_(r,j)` gives, uniformly in `t`,

\[
 |H_{r,j;X}(t)|
 =O_{\delta,r,j,\varepsilon,\ell}(X^\delta).
\tag{5.2}
\]

The prefix field is supported in `[0,log X+S_(r,j)]`. Hence

\[
 \mathcal E_{r,j}(X)
 \ll_{\delta,r,j,\varepsilon,\ell}
 (1+\log X)X^{2\delta}=X^{o(1)}.
\tag{5.3}
\]

### 5.2 Prefix energy implies the complete `L1` gate

Put `X=e^T`. Causality and the support in the nonnegative half-line give

\[
 H_{r,j;e^T}(t)=H_{r,j}(t)
 \qquad(0\le t\le T).
\tag{5.4}
\]

Therefore a subpower prefix energy gives

\[
 \int_0^T|H_{r,j}(t)|^2dt\le\mathcal E_{r,j}(e^T)=e^{o(T)}.
\]

Cauchy--Schwarz then yields

\[
 \int_0^T|H_{r,j}(t)|dt
 \le T^{1/2}
 \left(\int_0^T|H_{r,j}(t)|^2dt\right)^{1/2}
 =e^{o(T)}.
\tag{5.5}
\]

### 5.3 The one-sided Landau converse

The two-sided bound in (5.5) implies the corresponding negative-mass bound.
For completeness, the negative-mass bound alone is enough.

Assume

\[
 \int_0^T(H_{r,j}(t))_-dt=e^{o(T)}.
\tag{5.6}
\]

The transform of the negative part is holomorphic in `Re(s)>0`. The trivial
bound `|beta(n)|<=2` and compact boundedness of `B_(r,j)` give the positive
part a finite Laplace abscissa. Formula (3.4) is holomorphic at every positive
real point. If the positive abscissa were positive, (3.4) and the negative
transform would continue the positive transform through that abscissa,
contradicting Landau's theorem for a nonnegative density. Thus both Jordan
transforms are holomorphic in `Re(s)>0`.

The genuine poles from hypothetical zeros with real part greater than one
half are therefore impossible. The functional equation excludes their
reflections, proving RH. Together with Sections 5.1--5.2, this proves
(0.8)--(0.9).

## 6. Gram identity, compact ratio band, and diagonal

Finite Fubini gives

\[
 \boxed{
 \mathcal E_{r,j}(X)
 =\sum_{m,n\le X}{\beta(m)\beta(n)\over\sqrt{mn}}
 \mathcal R_{r,j}\!\left(\log{m\over n}\right).}
\tag{6.1}
\]

The autocorrelation is even, continuous, and positive definite. Two
translates of a function supported in `[0,S_(r,j)]` are disjoint when their
separation exceeds `S_(r,j)`. Consequently every nonzero pair in (6.1)
satisfies

\[
 \boxed{
 e^{-S_{r,j}}\le {m\over n}\le e^{S_{r,j}}.}
\tag{6.2}
\]

Equivalently, the original ratio-16 band expands only by the fixed factor
`exp(r epsilon+j ell)`.

Because `B_(r,j)` is nonzero,

\[
 \mathcal R_{r,j}(0)=\|B_{r,j}\|_2^2>0.
\]

The diagonal in (6.1) is therefore

\[
 \boxed{
 \mathcal D_{r,j}(X)
 =\mathcal R_{r,j}(0)
 {2379\over2278\zeta(2)}\log X
 +O_{r,j,\varepsilon,\ell}(1).}
\tag{6.3}
\]

It is harmless at subpower scale. Writing `O_(r,j)(X)` for the signed
off-diagonal part gives the exact equivalence

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 |\mathcal O_{r,j}(X)|=X^{o(1)}.}
\tag{6.4}
\]

No estimate for this off-diagonal expression is supplied here.

## 7. What the ladder changes

The boundary autocorrelation has a live value at zero frequency. For every
`r>=1`, (0.11) instead annihilates that exact frequency to order `2r`.
The boxes can then force any prescribed fixed polynomial decay at high
frequency. Both operations preserve every hypothetical off-line pole.

This gives a source-faithful design space for a future Fourier--hyperbola or
divisor-wavelet attack:

```text
complete beta source
  -> compact boundary kernel K_bd
  -> fixed high-pass Delta_epsilon^r
  -> optional fixed box smoothing eta_ell^(*j)
  -> compact positive Gram kernel R_(r,j)
  -> signed compact-ratio beta correlation.
```

It does not show that the low but nonzero frequency window is harmless.
It also does not automatically transport any primitive-ray, `PRIMCAR`, or
divisor-wavelet implication: those adapters must be rerun with
`R_(r,j)` and its enlarged fixed support.

## 8. Fixed-parameter firewall

The word **fixed** is load-bearing.

- `r`, `j`, `epsilon`, and `ell` are chosen independently of `X`, `T`, every
  zeta zero, and every Fourier frequency.
- Constants may deteriorate rapidly with `r`, `j`, `epsilon^(-1)`, or
  `ell^(-1)`. No uniformity in these parameters is claimed.
- Taking `r=r(X)`, `j=j(X)`, or shrinking a width with the horizon is not a
  consequence of this theorem.
- The filter multipliers are zero-free in the open right half-plane only
  because the parameters are positive and fixed. Their boundary zeros are
  deliberate and do not cancel a pole with positive real part.
- Arbitrarily high fixed vanishing at exactly `t=0` does not itself prove
  cancellation on a shrinking neighborhood of zero.

## 9. Proof and scope ledger

| statement | grade |
|---|---|
| compact BV kernel and support (0.5)--(0.6) | **PROVED FROM FROZEN COMPACT-BV INPUT** |
| exact Laplace multiplier (3.3) | **PROVED EXACT** |
| nonvanishing of added filters in `Re(s)>0` | **PROVED EXACT** |
| source-carrier nonvanishing in `0<Re(s)<1/2` | **IMPORTED FROM PINNED AUDIT** |
| persistence of every hypothetical right-half-plane zeta pole | **PROVED EXACT FROM PINNED SOURCE** |
| exact Fourier autocorrelation and zero order `2r` | **PROVED EXACT** |
| high-frequency decay `O(|t|^(-2j-2))` | **PROVED FROM COMPACT BV AND BOX MULTIPLIERS** |
| prefix `L2` criterion and one-sided criterion (0.8)--(0.9) | **PROVED FROM BV, CAUSALITY, CAUCHY, AND LANDAU** |
| Gram identity, ratio support, and logarithmic diagonal | **PROVED EXACT / IMPORTED BETA-SQUARE ASYMPTOTIC** |
| any band-pass off-diagonal estimate | **OPEN / NOT PROVED** |
| any primitive-pair or wavelet estimate | **OPEN / NOT PROVED** |
| horizon-dependent spectral design | **OUT OF SCOPE / NOT IMPLIED** |
| RH or GRH | **NOT PROVED** |

## 10. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_bandpass_beta_energy_ladder.py --check
python -B -O research/l-families/atlas/function_field/ffps_bandpass_beta_energy_ladder.py --check
python -B -m unittest tests.test_ffps_bandpass_beta_energy_ladder
python -B -O -m unittest tests.test_ffps_bandpass_beta_energy_ladder
```

The replay checks the pinned source blobs, the beta-square local factors,
the exceptional residue ratio, exact finite-difference moments, preservation
of the zero order under normalized box convolution, the first
autocorrelation second-difference identity, doubling of the zero order in
the autocorrelation, and one exact finite band-pass Gram identity. It uses
only rational arithmetic and fixed tiny arrays. It enumerates no zeta zero,
finite field, curve, conductor family, or L-function.
