# The sharp Chebyshev step has a finite atomic autocorrelation normal form

Status: **exact jump measure, finite atomic curvature, small-lag cusp law,
low-frequency notch, and quadratic resolution scale; the local cusp predicts
the first zero only through order three; no beta cancellation estimate and no
proof of RH**

Bounded replay:
[ffps_chebyshev_step_autocorrelation_normal_form.py](ffps_chebyshev_step_autocorrelation_normal_form.py).
Canonical summary:
[ffps_chebyshev_step_autocorrelation_normal_form.json](ffps_chebyshev_step_autocorrelation_normal_form.json).

Frozen source: the sharp universal-BV phase diagram at commit
**c223f8fe1b7d89f457db07ce6cc44940fa215aeb**. The producer pins all four
source blobs and imports no live predecessor module.

## 0. Outcome

The previous packets identify a unique BV-optimal order-\(r\) step. This
packet solves its compact autocorrelation geometry.

On \((0,1)\), write

\[
 K_r(t)=(-1)^rh_r\operatorname{sgn}U_r(2t-1),
 \qquad
 h_r=r!4^r b,
\tag{0.1}
\]

and zero-extend it. Its \(r+1\) alternating cells have boundaries

\[
 y_j=\frac{1-\cos(j\pi/(r+1))}{2},
 \qquad 0\le j\le r+1.
\tag{0.2}
\]

Put \(c_0=c_{r+1}=1\) and \(c_j=2\) in the interior. The complete
distributional derivative is

\[
 \boxed{
 dK_r=h_r\sum_{j=0}^{r+1}(-1)^jc_j\delta_{y_j}.}
\tag{0.3}
\]

For the even autocorrelation

\[
 R_r(s)=\int_{\mathbb R}K_r(t)K_r(t+s)\,dt,
\tag{0.4}
\]

the entire piecewise-linear function is encoded by one finite signed atomic
measure:

\[
 \boxed{
 -R_r''=\widetilde{dK_r}*dK_r
 =h_r^2\sum_{j,k=0}^{r+1}
 (-1)^{j+k}c_jc_k\,\delta_{y_k-y_j}.}
\tag{0.5}
\]

Here the tilde denotes reflection. Thus every breakpoint is a difference of
two Chebyshev cell boundaries. No numerical integration or root search is
needed.

The smallest cell width is

\[
 \boxed{
 \delta_r
 =\sin^2\!\left(\frac{\pi}{2(r+1)}\right).}
\tag{0.6}
\]

Before distinct jump neighborhoods overlap, the autocorrelation is exactly
linear:

\[
 \boxed{
 \frac{R_r(s)}{R_r(0)}
 =1-(2r+1)|s|,
 \qquad |s|\le\delta_r.}
\tag{0.7}
\]

The normalized cusp becomes steeper linearly in \(r\), but its certified
window shrinks quadratically:

\[
 \delta_r\sim\frac{\pi^2}{4(r+1)^2}.
\tag{0.8}
\]

This is the first kernel-specific geometry beyond the universal BV constant.
It also supplies a warning: a steep local cusp is not a macroscopic
decorrelation theorem.

## 1. The jump measure

The sign of \(U_r(2t-1)\) alternates at its \(r\) simple roots. The prefactor
in (0.1) makes the first cell height exactly \(h_r\), regardless of parity:
\(U_r(-1)=(-1)^r(r+1)\).

The zero extension jumps from zero to \(h_r\) at \(y_0=0\), changes by
\(2(-1)^jh_r\) at every interior boundary, and jumps back to zero at
\(y_{r+1}=1\). This is exactly (0.3). Its total mass vanishes, as a derivative
of a compactly supported function must, while

\[
 \|dK_r\|_{\mathrm{TV}}
 =2(r+1)|h_r|.
\tag{1.1}
\]

This agrees with the sharp variation theorem
\(2^{2r+1}(r+1)!|b|\).

The squared jump mass is

\[
 \sum_{j=0}^{r+1}|h_rc_j|^2
 =2(2r+1)h_r^2.
\tag{1.2}
\]

It will become the atom of \(-R_r''\) at the origin.

## 2. Atomic curvature determines the complete correlation

Since

\[
 R_r=\widetilde K_r*K_r,
\tag{2.1}
\]

distributional differentiation gives (0.5). The measure on its right is even,
has total mass zero, and has finite support inside \([-1,1]\). Together with
\(R_r=0\) outside \([-1,1]\), it determines the complete continuous
piecewise-linear autocorrelation.

At the origin, only the diagonal pairs \(j=k\) contribute. Equation (1.2)
therefore gives

\[
 \bigl[-R_r''\bigr](\{0\})
 =2(2r+1)h_r^2.
\tag{2.2}
\]

An even cusp \(R_r(0)-a|s|\) contributes \(2a\delta_0\) to \(-R_r''\).
Thus the origin atom already predicts the slope
\((2r+1)h_r^2\) in (0.7).

## 3. The exact small-lag law

For \(0\le s\le\delta_r\), the intervals on which
\(K_r(t+s)-K_r(t)\) sees different jumps are disjoint. An endpoint jump
contributes \(s h_r^2\) to the squared translation difference, while each of
the \(r\) interior jumps contributes \(4s h_r^2\). Hence

\[
 \|K_r(\cdot+s)-K_r\|_2^2
 =2(2r+1)h_r^2s.
\tag{3.1}
\]

The polarization identity

\[
 \|K_r(\cdot+s)-K_r\|_2^2
 =2\bigl(R_r(0)-R_r(s)\bigr)
\tag{3.2}
\]

and \(R_r(0)=h_r^2\) prove (0.7). Evenness handles negative \(s\).

The formal zero of this local line is

\[
 s_r^{\mathrm{lin}}=\frac1{2r+1}.
\tag{3.3}
\]

It lies inside the certified cusp window exactly for \(r=0,1,2,3\). For
\(r\ge4\),

\[
 \delta_r<\frac1{2r+1},
\tag{3.4}
\]

so the local line ends before reaching zero. The cases through three are
checked directly. For \(r\ge4\), \(\sin x<x\) reduces (3.4) to
\(\pi^2(2r+1)<4(r+1)^2\), whose gap is already positive at four and
increases thereafter.

Thus the attractive extrapolation “cusp slope \(2r+1\), therefore first zero
\(1/(2r+1)\)” is false from order four onward. The later Chebyshev difference
atoms intervene.

For \(r\ge1\), a negative value must still occur somewhere: the zero-mean
identity gives

\[
 \int_{\mathbb R}R_r(s)\,ds
 =\left(\int K_r\right)^2=0,
\tag{3.5}
\]

while \(R_r(0)>0\). This existence statement does not locate the first zero.

## 4. Fourier normal form and the notch

With

\[
 \widehat K_r(\xi)=\int K_r(t)e^{-i\xi t}\,dt,
\tag{4.1}
\]

equation (0.3) gives the exact finite exponential sum

\[
 \boxed{
 i\xi\widehat K_r(\xi)
 =h_r\sum_{j=0}^{r+1}
 (-1)^jc_j e^{-i\xi y_j}.}
\tag{4.2}
\]

Consequently

\[
 \widehat R_r(\xi)=|\widehat K_r(\xi)|^2,
\qquad
 \xi^2\widehat R_r(\xi)
 =h_r^2\left|
 \sum_{j=0}^{r+1}(-1)^jc_je^{-i\xi y_j}
 \right|^2.
\tag{4.3}
\]

The information moments give the low-frequency expansion without expanding
the finite sum:

\[
 \widehat K_r(\xi)
 =b(i\xi)^r+O(\xi^{r+1}),
\tag{4.4}
\]

and hence

\[
 \boxed{
 \widehat R_r(\xi)
 =b^2\xi^{2r}+O(\xi^{2r+2}).}
\tag{4.5}
\]

The improvement by one power follows because \(\widehat R_r\) is an even
real-analytic function. Thus the BV-optimal step retains the exact order-
\(2r\) autocorrelation notch.
At high frequency, (4.2) yields the robust bound

\[
 |\widehat K_r(\xi)|
 \le\frac{2(r+1)|h_r|}{|\xi|}.
\tag{4.6}
\]

The step sacrifices smooth high-frequency decay in exchange for sharp BV
geometry.

## 5. Interpretation and next analytic use

The atomic curvature formula is a finite exact coordinate system for testing
the Chebyshev detector against the beta ratio kernel. It separates three
scales:

- an order-\(2r\) notch at frequency zero;
- a local correlation cusp of slope \(2r+1\);
- a shortest geometric cell of scale \(r^{-2}\).

These scales do not collapse to one “resolution.” In particular, growing
notch order does not justify extrapolating the first local linear branch.

A useful next experiment is to pair the finite difference spectrum in (4.3)
with the assembled beta primitive-pair kernel before applying absolute
values. That is where a source-specific gain could live. This packet does not
claim such a gain.

## 6. Scope ledger

| statement | grade |
|---|---|
| exact Chebyshev jump measure (0.3) | **PROVED** |
| finite atomic autocorrelation curvature (0.5) | **PROVED** |
| exact small-lag cusp law (0.7) | **PROVED** |
| quadratic cusp-window asymptotic (0.8) | **PROVED** |
| low-frequency order-\(2r\) autocorrelation notch | **PROVED** |
| local line reaches its zero for all \(r\) | **REFUTED FOR \(r\ge4\)** |
| first zero is located for \(r\ge4\) | **NOT PROVED** |
| this geometry improves beta cancellation | **NOT PROVED** |
| unconditional beta estimate, RH, or GRH | **NOT PROVED** |

No external novelty or priority is claimed.

## 7. Bounded replay

The producer:

- verifies the frozen safe-factor quartet by full Git blob ID;
- constructs at most nine cells and one hundred raw curvature pairs;
- the producer and focused tests check the exact jump pattern, origin mass,
  curvature symmetry and total mass, and interval-overlap cusp law;
- records the analytic low-frequency theorem without sampling zeta or beta;
- performs no beta sum, prime enumeration, zeta evaluation, root search,
  random sampling, quadrature, or curve computation.

~~~text
python -B research/l-families/atlas/function_field/ffps_chebyshev_step_autocorrelation_normal_form.py --check
python -O -B research/l-families/atlas/function_field/ffps_chebyshev_step_autocorrelation_normal_form.py --check
python -B -m unittest tests.test_ffps_chebyshev_step_autocorrelation_normal_form
python -O -B -m unittest tests.test_ffps_chebyshev_step_autocorrelation_normal_form
python -m ruff check research/l-families/atlas/function_field/ffps_chebyshev_step_autocorrelation_normal_form.py tests/test_ffps_chebyshev_step_autocorrelation_normal_form.py
python -m ruff format --check research/l-families/atlas/function_field/ffps_chebyshev_step_autocorrelation_normal_form.py tests/test_ffps_chebyshev_step_autocorrelation_normal_form.py
~~~
