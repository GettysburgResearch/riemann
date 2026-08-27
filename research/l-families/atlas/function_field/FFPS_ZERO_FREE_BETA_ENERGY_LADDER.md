# A zero-free compact beta-energy ladder is exactly RH-equivalent

Status: **exact compact-BV kernel ladder, Fourier weight positive away
from its forced zero, open-RH-strip carrier nonvanishing, compact-ratio Gram
identity, and fixed-order RH equivalence; no energy estimate, off-diagonal
bound, RH, or GRH result**

Bounded replay:
[ffps_zero_free_beta_energy_ladder.py](ffps_zero_free_beta_energy_ladder.py).
Canonical summary:
[ffps_zero_free_beta_energy_ladder.json](ffps_zero_free_beta_energy_ladder.json).

Frozen inputs are the spectral-nonalignment theorem at commit
**fc7ee1304746d3c5b50d02592ccb0d8cdf329c4f** and the band-pass beta-energy
equivalence theorem at commit
**05aaabe69060c24c8db4ca33c350e109231960f1**. The replay pins both
quartets by Git blob ID and checks the imported working-tree producer
before executing it.

## 0. Outcome

Let

\[
 \beta(n)
 =\mu(n)-\mathbf1_{67\mid n}\mu(n/67).
\tag{0.1}
\]

Define the compact positive tent

\[
 \Phi(x)=e^{x-1}(1-|x-1|)_+.
\tag{0.2}
\]

Its mass is

\[
 M=\widehat\Phi(0)=4\sinh^2(1/2),
 \qquad P=\Phi/M.
\tag{0.3}
\]

For every fixed integer \(m\ge1\), form the density of the compressed
average of \(m\) independent \(P\)-variables and differentiate it:

\[
\boxed{
 Q_m(x)=mP^{*m}(mx),
 \qquad J_m=DQ_m.}
\tag{0.4}
\]

Each \(J_m\) is a nonzero real compact BV function supported on the
same interval \([0,2]\), has mean zero, and has the exact Laplace
transform

\[
\boxed{
 \widehat J_m(s)
 =s\left[{\widehat\Phi(s/m)\over M}\right]^m,
 \qquad
 \widehat\Phi(z)
 =4e^{-z}{\sinh^2((z-1)/2)\over(z-1)^2}.}
\tag{0.5}
\]

Its only carrier zeros are

\[
 s=0,
 \qquad
 s=m(1+2\pi ik)\quad(k\in\mathbf Z\setminus\{0\}).
\tag{0.6}
\]

Therefore

\[
\boxed{
 \widehat J_m(s)\ne0
 \qquad(0<\Re s<1/2).}
\tag{0.7}
\]

On the Fourier axis, with

\[
 A_m(t)=\sinh^2(1/2)+\sin^2(t/(2m)),
\tag{0.8}
\]

the autocorrelation weight is

\[
\boxed{
 w_m(t)
 :=|\widehat J_m(it)|^2
 =t^2\left[
  {A_m(t)^2\over
   \sinh^4(1/2)(1+(t/m)^2)^2}
 \right]^m.}
\tag{0.9}
\]

Since \(A_m(t)\ge\sinh^2(1/2)>0\),

\[
\boxed{
 w_m(t)>0\quad(t\ne0),\qquad
 w_m(t)\asymp_m |t|^{2-4m}\quad(|t|\to\infty).}
\tag{0.10}
\]

The sole real notch is \(t=0\), always of order two in weight. Increasing
\(m\) adds four powers of fixed-order high-frequency decay without
introducing a real side notch or widening the compact ratio band.

For \(X\ge1\), define the prefix field and energy

\[
\begin{aligned}
 H_{m;X}(t)
 &=\sum_{n\le X}{\beta(n)\over\sqrt n}
   J_m(t-\log n),\\
 \mathcal E_m(X)
 &=\int_{\mathbf R}|H_{m;X}(t)|^2\,dt.
\end{aligned}
\tag{0.11}
\]

Let \(H_m\) denote the complete causal field. Then every one fixed ladder
member is an exact RH criterion:

\[
\boxed{
\begin{aligned}
 \mathrm{RH}
 &\Longleftrightarrow
 \mathcal E_m(X)=X^{o(1)}\\
 &\Longleftrightarrow
 \int_0^T|H_m(t)|\,dt=e^{o(T)}\\
 &\Longleftrightarrow
 \int_0^T(H_m(t))_-\,dt=e^{o(T)}.
\end{aligned}}
\tag{0.12}
\]

The word fixed is load-bearing. The construction holds the physical
support fixed by compressing an average; its large-\(m\) limit is not a
uniformly smoothing kernel theorem.

This synthesis removes the spectral-blind-spot caveat from an
RH-equivalent beta-energy criterion. It does not prove any estimate in
(0.12).

## 1. Kernel construction and zero-free carrier

The centered tent has the convolution identity

\[
 (1-|y|)_+
 =\mathbf1_{[-1/2,1/2]}*
  \mathbf1_{[-1/2,1/2]}(y).
\tag{1.1}
\]

Exponential tilting and translation give

\[
 \widehat\Phi(s)
 =4e^{-s}{\sinh^2((s-1)/2)\over(s-1)^2}.
\tag{1.2}
\]

The value at \(s=1\) is removable and nonzero. Scaling the convolution
in (0.4) gives

\[
 \widehat Q_m(s)
 =\left[{\widehat\Phi(s/m)\over M}\right]^m.
\tag{1.3}
\]

The density \(Q_m\) is continuous, compact, supported on \([0,2]\), and
vanishes at both endpoints. Its distributional derivative therefore has
no boundary atom, so

\[
 \widehat J_m(s)
 =s\widehat Q_m(s)
 =s\left[{\widehat\Phi(s/m)\over M}\right]^m,
\tag{1.4}
\]

proving (0.5).

The zero at \(s=0\) comes from the derivative factor. The remaining zeros
occur when \(s/m\) is a nonremovable zero of \(\widehat\Phi\), namely

\[
 s=m(1+2\pi ik),
 \qquad k\in\mathbf Z\setminus\{0\}.
\tag{1.5}
\]

The row \(k=0\) is canceled by the removable denominator at \(s/m=1\);
every \(k\ne0\) zero has multiplicity \(2m\). All have real part \(m\).
This proves (0.6)--(0.7), and in fact gives a zero-free carrier on the
larger strip \(0<\Re s<m\).

Compact convolution preserves bounded variation in this setting:

\[
 J_m(x)
 =m^2 M^{-m}
  (\Phi'*\Phi^{*(m-1)})(mx),
\tag{1.6}
\]

For \(m=1\), this says directly that \(J_1=\Phi'/M\) is compact BV. For
\(m\ge2\), \(\Phi^{*(m-1)}\) is compact \(L^1\), so (1.6) again gives
compact BV. The function is nonzero because its transform in (0.5) is
not identically zero. Its integral vanishes because it is a compact
derivative.

## 2. Exact Fourier weight and smoothing without side notches

On \(s=it/m\),

\[
 |\sinh(-1/2+it/(2m))|^2
 =\sinh^2(1/2)+\sin^2(t/(2m))
 =A_m(t).
\tag{2.1}
\]

Also \(|it/m-1|^2=1+(t/m)^2\). Taking absolute values in (0.5),
then dividing by \(M^{2m}=16^m\sinh^{4m}(1/2)\), proves (0.9). The
strict lower bound in (0.8) proves positivity for \(t\ne0\).

At zero,

\[
 {\widehat\Phi(0)\over M}=1,
\tag{2.2}
\]

so \(\widehat J_m(it)\) has exactly a simple amplitude zero and \(w_m\)
has exactly a double zero, independently of \(m\).

For fixed \(m\) and large \(|t|\), \(A_m(t)\) stays between two fixed
positive constants, while
\((1+(t/m)^2)^{-2m}\asymp_m |t|^{-4m}\). Hence the two-sided decay in
(0.10) follows.

This contrasts with repeated box smoothing. A box multiplier introduces a
new sinc lattice. Compressed convolution powers of \(\Phi\) retain the
same sole real zero, add decay, and preserve the support \([0,2]\).

## 3. Mellin transform of the complete beta field

Causality and compact support imply that, initially in a right
half-plane,

\[
\begin{aligned}
 \int_0^\infty H_m(t)e^{-st}\,dt
 &=\widehat J_m(s)
   \sum_{n\ge1}{\beta(n)\over n^{s+1/2}}\\
 &=\widehat J_m(s)
   {1-67^{-(s+1/2)}\over\zeta(s+1/2)}.
\end{aligned}
\tag{3.1}
\]

The exceptional numerator cannot vanish when \(\Re(s+1/2)>0\) at a
candidate zeta zero: equality \(67^{-(s+1/2)}=1\) would force real part
zero. Equation (0.7) shows that the new kernel also cannot cancel a zeta
zero with

\[
 1/2<\Re\rho<1.
\tag{3.2}
\]

Thus every hypothetical right-of-line zero produces a genuine pole at
\(s=\rho-1/2\). The functional equation handles the reflected half of the
critical strip exactly as in the frozen Mellin--Landau consumer.

The carrier conclusion is exact, but it is not an estimate for \(H_m\).

## 4. Proof of the RH-equivalence ladder

### RH implies the prefix-energy bound

Under RH, the normalized beta summatory function satisfies

\[
 A_\beta(x)
 :=\sum_{n\le x}{\beta(n)\over\sqrt n}
 =O_\delta(x^\delta)
\tag{4.1}
\]

for every \(\delta>0\). Bounded-variation Stieltjes summation against one
translate of fixed \(J_m\) gives

\[
 |H_{m;X}(t)|=O_{\delta,m}(X^\delta)
\tag{4.2}
\]

uniformly in \(t\). Its support lies in the order-independent interval
\([0,\log X+2]\), so

\[
 \mathcal E_m(X)
 \ll_{\delta,m}(1+\log X)X^{2\delta}
 =X^{o(1)}.
\tag{4.3}
\]

### Prefix energy implies the complete \(L^1\) gate

Set \(X=e^T\). For \(0\le t\le T\), causality gives

\[
 H_{m;e^T}(t)=H_m(t).
\tag{4.4}
\]

Therefore Cauchy--Schwarz gives

\[
\begin{aligned}
 \int_0^T|H_m(t)|\,dt
 &\le T^{1/2}
 \left(\int_0^T|H_m(t)|^2\,dt\right)^{1/2}\\
 &\le T^{1/2}\mathcal E_m(e^T)^{1/2}
 =e^{o(T)}.
\end{aligned}
\tag{4.5}
\]

### One-sided negative mass implies RH

Assume only

\[
 \int_0^T(H_m(t))_-\,dt=e^{o(T)}.
\tag{4.6}
\]

The Laplace transform of the negative part is holomorphic in
\(\Re s>0\). The trivial bound \(|\beta(n)|\le2\), compact support, and
boundedness of \(J_m\) give the positive part a finite Laplace abscissa.
The signed transform (3.1) is holomorphic at every positive real point.

If the positive part had a positive abscissa, (3.1) and the negative
transform would analytically continue its nonnegative Laplace transform
through that abscissa, contradicting Landau's theorem. Both Jordan
transforms are therefore holomorphic in \(\Re s>0\).

The genuine poles described after (3.2) are impossible. The functional
equation then proves RH. Together with (4.1)--(4.5), this proves (0.12).

This is an equivalence theorem, not progress on the estimate (4.6).

## 5. Compact-ratio Gram identity

Define the autocorrelation

\[
 \mathcal R_m(u)
 =\int_{\mathbf R}J_m(v)J_m(v+u)\,dv.
\tag{5.1}
\]

Finite Fubini gives

\[
\boxed{
 \mathcal E_m(X)
 =\sum_{a,b\le X}
 {\beta(a)\beta(b)\over\sqrt{ab}}
 \mathcal R_m\!\left(\log{a\over b}\right).}
\tag{5.2}
\]

Because \(\operatorname{supp}J_m\subset[0,2]\),

\[
 \operatorname{supp}\mathcal R_m\subset[-2,2].
\tag{5.3}
\]

Only pairs in the fixed ratio band

\[
\boxed{
 e^{-2}\le{a\over b}\le e^2}
\tag{5.4}
\]

contribute.

The Fourier transform of \(\mathcal R_m\) is exactly \(w_m\). Since
\(w_m>0\) almost everywhere, every finite Gram matrix built from distinct
translates is strictly positive definite. This positivity does not prove
that the signed beta vector has small energy.

The diagonal is explicit:

\[
\begin{aligned}
 \mathcal E_m^{\rm diag}(X)
 &=\|J_m\|_2^2
   \sum_{n\le X}{\beta(n)^2\over n}\\
 &=\|J_m\|_2^2
   {2379\over2278\zeta(2)}\log X+O_m(1).
\end{aligned}
\tag{5.5}
\]

At the first rung,

\[
 \boxed{
 \|J_1\|_2^2
 ={1+\sinh(2)/2\over16\sinh^4(1/2)}.}
\tag{5.6}
\]

Indeed, in the centered variable \(y=x-1\),

\[
\begin{aligned}
 \int_{-1}^0e^{2y}(y+2)^2\,dy
 &= {5\over4}-{e^{-2}\over4},\\
 \int_0^1e^{2y}y^2\,dy
 &= -{1\over4}+{e^2\over4}.
\end{aligned}
\tag{5.7}
\]

Their sum is \(\|\Phi'\|_2^2=1+\sinh(2)/2\). Since
\(J_1=\Phi'/M\), division by \(M^2=16\sinh^4(1/2)\) proves (5.6).

## 6. What this changes for the analytic programme

The ladder separates two issues that were previously entangled:

~~~text
spectral blind spots
  -> removed exactly by w_m(t)>0 for every t != 0;

high-frequency tail
  -> tunable by the fixed order m;

arithmetic cancellation
  -> still exactly the open RH-equivalent energy estimate.
~~~

The fixed support removes the most obvious smoothing tradeoff: every rung
sees exactly the same ratio band \(e^{-2}\le a/b\le e^2\). The Gram
profile and its constants still change with \(m\), so no estimate follows
automatically.

There is also a sharp noncommuting-limit warning. For fixed \(t\), the
normalized characteristic function of the compressed average satisfies

\[
 \left[{\widehat\Phi(it/m)\over M}\right]^m
 \longrightarrow e^{-i\mathbb E_P[X]t},
 \qquad
 w_m(t)\longrightarrow t^2.
\tag{6.1}
\]

Thus the \(|t|^{2-4m}\) tail in (0.10) is a fixed-\(m\), large-\(|t|\)
statement and is not uniform as \(m\to\infty\). The increasing order
pushes the onset of strong tail damping outward even though it never
widens the physical support.

The zero at \(t=0\) is forced by the mean-zero band-pass condition. It
misses every critical-line zero because the elementary eta identity gives
\(\zeta(1/2)<0\).

## 7. Fixed-order firewall

- \(m\) is fixed independently of \(X,T\), every zeta zero, and every
  Fourier frequency.
- Constants may deteriorate with \(m\); no growing-order theorem is
  inferred.
- The high-frequency asymptotic is not uniform in \(m\); equation (6.1)
  prevents reading the ladder as monotone pointwise damping.
- The carrier theorem uses no zeta-zero census.
- Positivity of \(w_m\) removes nonalignment, not the need for an
  \(O_T(1/c)\), \(L^1\), or energy estimate.
- The prefix criterion concerns the literal beta source (0.1), not a
  family average or function-field surrogate.

## 8. Claim ledger

| statement | grade |
|---|---|
| compact BV ladder and support | **PROVED EXACT** |
| Laplace transform and carrier zero set | **PROVED EXACT** |
| positive nonzero Fourier weight (0.9)--(0.10) | **PROVED EXACT** |
| fixed-order RH equivalence (0.12) | **PROVED FROM THE FROZEN LANDAU ARGUMENT** |
| compact-ratio Gram identity | **PROVED EXACT** |
| strict finite Gram positivity | **PROVED FROM POSITIVE-A.E. SPECTRAL WEIGHT** |
| diagonal asymptotic and first-rung norm | **PROVED EXACT / IMPORTED BETA DIAGONAL** |
| any prefix-energy or off-diagonal estimate | **NOT PROVED** |
| growing \(m\) with the horizon | **OUT OF SCOPE** |
| RH or GRH | **NOT PROVED** |

Equivalent criteria for RH are common. No external novelty claim is made
without a dedicated literature comparison.

## 9. Bounded replay

The replay checks all eight frozen blobs and the live imported source,
orders \(1\) through \(6\), exact fixed support and decay exponents,
positivity at six bounded nonzero frequencies per order, and exact
agreement of the normalized first rung with the frozen universal kernel.

It evaluates no zeta zero, numerical zeta value, prime interval, curve,
random sample, or contour integral. The analytic RH equivalence is proved
in this document from the pinned general argument; bounded floating-point
weight samples are regression checks only.

~~~text
python -B research/l-families/atlas/function_field/ffps_zero_free_beta_energy_ladder.py --check
python -B -O research/l-families/atlas/function_field/ffps_zero_free_beta_energy_ladder.py --check
python -B -m unittest tests.test_ffps_zero_free_beta_energy_ladder
python -B -O -m unittest tests.test_ffps_zero_free_beta_energy_ladder
python -B -m ruff check research/l-families/atlas/function_field/ffps_zero_free_beta_energy_ladder.py tests/test_ffps_zero_free_beta_energy_ladder.py
python -B -m ruff format --check research/l-families/atlas/function_field/ffps_zero_free_beta_energy_ladder.py tests/test_ffps_zero_free_beta_energy_ladder.py
~~~
