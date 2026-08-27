# The universal BV safe factor has an exact Chebyshev phase diagram

Status: **sharp fixed-width minimum, unique equality shape, strict
information-order monotonicity and log-concavity, variable-order normalized RH
corollary, and exact moving-width phase boundary; no unconditional beta
cancellation, no claim about the actual convolution norm beyond the universal
BV envelope, and no proof of RH**

Bounded replay:
[ffps_sharp_bv_safe_factor_phase_diagram.py](ffps_sharp_bv_safe_factor_phase_diagram.py).
Canonical summary:
[ffps_sharp_bv_safe_factor_phase_diagram.json](ffps_sharp_bv_safe_factor_phase_diagram.json).

Frozen source: the sharp Chebyshev BV extremizer at commit
**798feab0bb333efd8b45ab197131cd13658a5ca9**. The producer pins all four
source blobs and imports no live predecessor module.

## 0. Outcome

Let \(K\) be a nonzero real compact BV kernel whose essential-support hull has
width \(W>0\). Let its information order be the nonnegative integer \(r\), and
write

\[
 b=\frac{(-1)^r}{r!}\int t^rK(t)\,dt\ne0,
 \qquad
 M(K)=\|K\|_\infty+\operatorname{Var}_{\mathbb R}K.
\tag{0.1}
\]

The preceding two Chebyshev duals now give the exact width-scaled theorem

\[
 \boxed{
 M(K)\ge
 \frac{r!4^r(2r+3)}{W^{r+1}}\,|b|.}
\tag{0.2}
\]

Equality is attained, uniquely almost everywhere up to translation, jump
values, and the forced scalar normalization, by the sensitivity-preserving
\(W\)-dilate of the alternating Chebyshev step.

Put

\[
 \ell=\log X,\qquad L=W+\ell,
\tag{0.3}
\]

and recall the universal normalized BV safe factor

\[
 \mathcal G_X(K)
 =\frac{L^{2r+2}M(K)^2}{|b|^2C_r},
 \qquad
 C_r=(r!)^2(2r+1)\binom{2r}{r}^2.
\tag{0.4}
\]

Then (0.2) solves its complete fixed-\((r,W)\) shape optimization:

\[
 \boxed{
 \inf_K\mathcal G_X(K)
 =A_r\left(1+\frac{\ell}{W}\right)^{2r+2},}
\tag{0.5}
\]

where

\[
 \boxed{
 A_r=\frac{16^r(2r+3)^2}
 {(2r+1)\binom{2r}{r}^2}.}
\tag{0.6}
\]

The information-order constants grow strictly:

\[
 A_0=9,\qquad A_1=\frac{100}{3},\qquad
 A_2=\frac{3136}{45},\qquad\cdots,
\tag{0.7}
\]

and

\[
 \boxed{
 \frac{A_{r+1}}{A_r}
 =\frac{4(r+1)^2(2r+5)^2}
 {(2r+1)(2r+3)^3}>1.}
\tag{0.8}
\]

Thus the universal BV geometry never rewards an extra vanished moment. At a
common width, order zero is the global winner whenever low-pass kernels are
admissible; among zero-mean kernels, order one is the winner. Any benefit from
higher information order must come from structure deliberately discarded by
the BV triangle bound: beta-specific cancellation, Fourier localization,
autocorrelation geometry, or a genuinely different norm inequality.

## 1. Scaling the sharp unit-interval theorem

Translate the support hull to \([0,W]\), and define

\[
 \widetilde K(u)=W^{r+1}K(Wu),\qquad 0\le u\le1.
\tag{1.1}
\]

Translation preserves \(r\) and \(b\), while this sensitivity-preserving
rescaling also preserves \(b\). It gives

\[
 M(\widetilde K)=W^{r+1}M(K).
\tag{1.2}
\]

The sharp unit-width theorem says

\[
 M(\widetilde K)\ge r!4^r(2r+3)|b|.
\tag{1.3}
\]

Equations (1.2)--(1.3) prove (0.2). Equality in (1.3) already has a unique
almost-everywhere shape, so the equality classification survives translation
and dilation. Explicitly, on a hull \((a,a+W)\), one may write it as

\[
 K_{r,W}(t)
 =(-1)^rr!4^r b\,W^{-r-1}
 \operatorname{sgn}U_r\!\left(2\frac{t-a}{W}-1\right),
\tag{1.4}
\]

with the usual irrelevance of its finitely many jump values.

Substituting (0.2) into (0.4) cancels \(r!\) and \(b\), and yields (0.5)--
(0.6). This is why neither amplitude dilution nor a different scalar
normalization can evade the floor.

## 2. Information order is strictly costly in the BV envelope

Using

\[
 \frac{\binom{2r+2}{r+1}}{\binom{2r}{r}}
 =\frac{2(2r+1)}{r+1},
\tag{2.1}
\]

one obtains (0.8). Subtracting its denominator from its numerator leaves

\[
 32r^3+132r^2+172r+73>0,
\tag{2.2}
\]

which is an elementary all-order certificate of strict growth.

There is a little more rigidity. The consecutive ratios themselves decrease
strictly to one. After putting them over a common positive denominator, the
numerator of

\[
 \frac{A_{r+1}}{A_r}-\frac{A_{r+2}}{A_{r+1}}
\tag{2.3}
\]

is

\[
 256r^5+2496r^4+9408r^3+17216r^2+15392r+5444.
\tag{2.4}
\]

Thus \((A_r)\) is strictly increasing and strictly log-concave. Central-
binomial asymptotics give

\[
 \boxed{
 A_r=2\pi r^2\left(
 1+\frac{11}{4r}+\frac{53}{32r^2}+O(r^{-3})\right).}
\tag{2.5}
\]

At fixed \(\ell/W\), the full optimum in (0.5) grows even faster, because
raising \(r\) also contributes another factor
\((1+\ell/W)^2\). Therefore:

- if all information orders are allowed, \(r=0\) uniquely wins;
- if an application imposes \(r\ge r_{\min}\), the lowest admissible order
  \(r_{\min}\) wins;
- a spectral notch or zero-mean constraint may still require \(r>0\), but its
  purpose cannot be an improvement of this universal BV constant.

## 3. Width floors and nonattainment

For \(X>1\), the right side of (0.5) is strictly decreasing in \(W\). At each
prescribed finite width it is attained by (1.4), but over all finite widths

\[
 \inf_{W>0}\inf_K\mathcal G_X(K)=A_r
\tag{3.1}
\]

is approached only as \(W/\log X\to\infty\). It is not attained at finite
\(W\). Across both width and order, the infimum is therefore \(9\), approached
by increasingly wide order-zero steps. Among zero-mean kernels it is
\(100/3\), approached by increasingly wide first-order steps.

These positive floors are not obstructions to an \(X^{o(1)}\) theorem:
constants themselves are subpower. They prevent a fictitious gain from
driving the geometric normalization to zero.

For fixed information order, the three width regimes are transparent. With
\(\rho=W/\ell\):

\[
 \inf_K\mathcal G_X(K)\longrightarrow
 \begin{cases}
 \infty,&\rho\to0,\\
 A_r(1+\rho_0^{-1})^{2r+2},&\rho\to\rho_0\in(0,\infty),\\
 A_r,&\rho\to\infty.
 \end{cases}
\tag{3.2}
\]

## 4. A variable-information-order normalized corollary

The predecessor stated its moving theorem for one fixed \(r\). Its two proof
inequalities are pointwise and retain their exact \(C_r\), so they can be
rerun without a hidden uniformity constant when \(r=r_X\) varies.

Let \(K_X\) have actual hull width \(W_X\), order \(r_X\), sensitivity
\(b_X\ne0\), and put \(L_X=W_X+\log X\). Define the *fully normalized* energy

\[
 \mathcal R_X
 =\frac{L_X^{2r_X+1}}{|b_X|^2C_{r_X}}
 \|K_X*\mu_X\|_2^2
\tag{4.1}
\]

and the corresponding geometric factor

\[
 \mathcal G_X
 =\frac{L_X^{2r_X+2}M(K_X)^2}
 {|b_X|^2C_{r_X}}.
\tag{4.2}
\]

The exact moment reverse bound is uniform in the displayed parameters:

\[
 \mathcal R_X\ge |B(X)|^2.
\tag{4.3}
\]

Under RH, BV Abel summation gives

\[
 \mathcal R_X\le\mathcal G_X(B^*(X))^2.
\tag{4.4}
\]

Consequently, provided the estimates hold for every sufficiently large \(X\),

\[
 \boxed{
 \mathcal G_X=X^{o(1)}\quad\Longrightarrow\quad
 \left[\mathrm{RH}\Longleftrightarrow
 \mathcal R_X=X^{o(1)}\right].}
\tag{4.5}
\]

This is a normalized variable-order extension proved by repeating the
pointwise argument; it is not an appeal to the predecessor's fixed-order
wording. Raw energy is not interchangeable with (4.1) when \(r_X,b_X,W_X\)
move.

For the optimal Chebyshev family, (0.5) makes the BV safe window exact:

\[
 (r_X+1)\log\left(1+\frac{\log X}{W_X}\right)
 +\log(r_X+2)=o(\log X).
\tag{4.6}
\]

Here (2.5) absorbs only fixed multiplicative constants. Useful consequences
include:

- fixed width permits \(r_X=o(\log X/\log\log X)\);
- \(W_X\asymp\log X\) permits \(r_X=o(\log X)\);
- \(W_X\gg\log X\) reduces the main width cost to
  \(r_X/W_X=o(1)\), together with \(\log r_X=o(\log X)\).

For the power-law chart

\[
 r_X\asymp(\log X)^\alpha,\qquad
 W_X=(\log X)^\sigma,
\tag{4.7}
\]

away from bounded-order conventions, the strict safe region is

\[
 \boxed{\alpha<\max(1,\sigma).}
\tag{4.8}
\]

Equality is the phase boundary, not part of the safe region.

## 5. Interpretation and firewalls

This is an optimization and no-go theorem for one *specific universal proof
envelope*. It says that once the forward argument retains only
\(\|K\|_\infty+\operatorname{Var}K\), higher information order cannot improve
the certificate.

It does **not** say that higher-order kernels have larger actual beta energy.
The Abel bound took a triangle inequality before seeing arithmetic signs.
Source-specific Fourier cancellation, compact autocorrelation, coherent
ensembles, and endpoint localization may reverse the practical comparison.

It also does not cover complex or vector-valued kernels, non-BV distributions,
or a criterion with a different normalization. Failure of (4.6) says only
that this BV route does not certify the moving family. It does not disprove RH,
RH equivalence, or a sharper forward estimate.

A criterion on a sparse subsequence of \(X\) cannot be promoted to all \(X\)
without a separate gap argument. Equation (4.5) is stated for all sufficiently
large horizons for that reason.

## 6. Scope ledger

| statement | grade |
|---|---|
| sharp fixed-\((r,W)\) BV shape minimum | **PROVED** |
| unique translated/dilated Chebyshev equality shape | **PROVED** |
| strict growth and strict log-concavity of \(A_r\) | **PROVED** |
| order zero wins the universal BV envelope when admissible | **PROVED** |
| variable-order normalized RH corollary (4.5) | **PROVED SUFFICIENT** |
| exact Chebyshev moving safe chart (4.6)--(4.8) | **PROVED** |
| higher order never improves actual beta energy | **NOT PROVED** |
| failure outside the chart precludes another RH argument | **NOT PROVED** |
| new unconditional beta cancellation | **NOT PROVED** |
| RH or GRH | **NOT PROVED** |

No external novelty or priority is claimed. The central-binomial asymptotic is
used only for interpretation; the sharp inequalities and monotonicity are
finite exact identities.

## 7. Bounded replay

The producer:

- verifies the frozen Chebyshev quartet by full Git blob ID;
- computes \(A_r\), its consecutive ratio, both positive polynomial
  certificates, and the sharp shape constant with exact integer/rational
  arithmetic through order twelve;
- checks sample finite-width minima for four orders and three widths;
- records the power-law phase rule without performing a horizon sweep;
- performs no beta sum, prime enumeration, zeta evaluation, root search,
  random sampling, quadrature, or curve computation.

~~~text
python -B research/l-families/atlas/function_field/ffps_sharp_bv_safe_factor_phase_diagram.py --check
python -O -B research/l-families/atlas/function_field/ffps_sharp_bv_safe_factor_phase_diagram.py --check
python -B -m unittest tests.test_ffps_sharp_bv_safe_factor_phase_diagram
python -O -B -m unittest tests.test_ffps_sharp_bv_safe_factor_phase_diagram
python -m ruff check research/l-families/atlas/function_field/ffps_sharp_bv_safe_factor_phase_diagram.py tests/test_ffps_sharp_bv_safe_factor_phase_diagram.py
python -m ruff format --check research/l-families/atlas/function_field/ffps_sharp_bv_safe_factor_phase_diagram.py tests/test_ffps_sharp_bv_safe_factor_phase_diagram.py
~~~
