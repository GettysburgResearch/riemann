# The normalized first beta rung has an exact signed Gram geometry

Status: **exact physical autocorrelation formula, unique interior node,
complete ratio-annulus sign theorem, and exact low moments; no beta
correlation estimate, positivity shortcut, RH, or GRH result**

Bounded replay:
[ffps_beta_gram_sign_geometry.py](ffps_beta_gram_sign_geometry.py).
Canonical summary:
[ffps_beta_gram_sign_geometry.json](ffps_beta_gram_sign_geometry.json).

The only mathematical source imported here is the normalized first rung in
the zero-free beta-energy ladder at frozen commit
`3658d4c31cc866e15d48ab1fc9d8d119136da424`.  The replay pins the complete
source quartet:

| frozen path | Git blob |
|---|---|
| `FFPS_ZERO_FREE_BETA_ENERGY_LADDER.md` | `bd4cbb842e78c1dad5d380c8d20ff14c39bba15e` |
| `ffps_zero_free_beta_energy_ladder.py` | `df80000192292cc5fc1cd08013f152fb257054f9` |
| `ffps_zero_free_beta_energy_ladder.json` | `7e8889aa0dd1b01674e20158a52502cff0d8dffa` |
| `tests/test_ffps_zero_free_beta_energy_ladder.py` | `983a1320f89087028f6724fe36aaca5ca1309b15` |

No live source module is imported by the replay.  The formulas below are an
independent elementary derivation from the frozen normalization.

## 0. Outcome

Let

\[
 \Phi(x)=e^{x-1}(1-|x-1|)_+,
 \qquad
 M=\int_{\mathbb R}\Phi(x)\,dx=4\sinh^2(1/2),
 \qquad
 J_1={\Phi'\over M}.
\tag{0.1}
\]

Define the physical autocorrelation

\[
 \mathcal R(u)=\int_{\mathbb R}J_1(v)J_1(v+u)\,dv.
\tag{0.2}
\]

Put \(q=|u|\) and \(C(q)=M^2\mathcal R(u)\). Then

\[
\boxed{
C(q)=
\begin{cases}
\displaystyle {1\over4}\left[
 \bigl(e^2+4-(e^2+2)q\bigr)e^{-q}
 -\bigl(2q+e^{-2}(q+1)\bigr)e^q
\right],&0\le q\le1,\\[6pt]
\displaystyle -{1\over2}\left[
 \sinh(2-q)+(2-q)\cosh(2-q)
\right],&1\le q\le2,\\[6pt]
0,&q\ge2.
\end{cases}}
\tag{0.3}
\]

There is a unique number

\[
 \boxed{\xi\in(0,1),\qquad C(\xi)=0.}
\tag{0.4}
\]

It has the display value

\[
 \xi\approx0.6392132705465206,
 \qquad
 e^\xi\approx1.89498944869236.
\tag{0.5}
\]

The decimal is not used in the proof.  The exact sign geometry is

\[
\boxed{
\begin{aligned}
 \mathcal R(u)&>0 &&(|u|<\xi),\\
 \mathcal R(u)&=0 &&(|u|=\xi),\\
 \mathcal R(u)&<0 &&(\xi<|u|<2),\\
 \mathcal R(u)&=0 &&(|u|\ge2).
\end{aligned}}
\tag{0.6}
\]

Thus the compact Gram kernel is positive definite as a translate kernel but
is not pointwise nonnegative.  Its entire physical outer annulus is
strictly negative.

## 1. Direct derivation of the two pieces

The weak derivative of the continuous compact function \(\Phi\) has the
almost-everywhere representative

\[
 \Phi'(x)=
 \begin{cases}
  e^{x-1}(x+1),&0<x<1,\\
  e^{x-1}(1-x),&1<x<2,\\
  0,&x\notin[0,2].
 \end{cases}
\tag{1.1}
\]

Values at the three breakpoints do not affect (0.2).  Write the two active
branches as

\[
 g_-(x)=e^{x-1}(x+1),
 \qquad
 g_+(x)=e^{x-1}(1-x).
\tag{1.2}
\]

Autocorrelations of real functions are even, so it is enough to take
\(q=u\ge0\). When \(0\le q\le1\), the overlap crosses both breakpoints and
splits as

\[
\begin{aligned}
C(q)
={}&\int_0^{1-q}g_-(v)g_-(v+q)\,dv\\
&+\int_{1-q}^{1}g_-(v)g_+(v+q)\,dv\\
&+\int_1^{2-q}g_+(v)g_+(v+q)\,dv.
\end{aligned}
\tag{1.3}
\]

When \(1\le q\le2\), only the cross-branch overlap remains:

\[
 C(q)=\int_0^{2-q}g_-(v)g_+(v+q)\,dv.
\tag{1.4}
\]

Each integrand is \(e^{2v+q-2}\) times a quadratic polynomial. The single
elementary primitive

\[
\begin{aligned}
\int e^{2v}(Av^2+Bv+D)\,dv
=e^{2v}\biggl[
 {A\over2}v^2+{B-A\over2}v+{2D-B+A\over4}
\biggr]
\end{aligned}
\tag{1.5}
\]

evaluates (1.3)--(1.4) and gives exactly (0.3).  This also supplies an
independent direct-integration route used by the bounded replay.

At the joins,

\[
 C(0)=1+{\sinh2\over2},
 \qquad
 C(1)=-{e\over2},
 \qquad
 C(2)=0.
\tag{1.6}
\]

The two displayed branches therefore agree at \(q=1\), and compact support
gives the zero branch beyond \(q=2\). In particular,

\[
 \mathcal R(0)=\|J_1\|_2^2
 ={1+\sinh(2)/2\over16\sinh^4(1/2)},
\tag{1.7}
\]

in agreement with the frozen first-rung norm.

## 2. The unique node and the complete sign proof

Differentiate the inner branch of (0.3):

\[
\begin{aligned}
4C'(q)
={}&\bigl((e^2+2)q-2e^2-6\bigr)e^{-q}\\
&-\bigl((2+e^{-2})q+2+2e^{-2}\bigr)e^q.
\end{aligned}
\tag{2.1}
\]

For \(0\le q\le1\), the first parenthesis satisfies

\[
 (e^2+2)q-2e^2-6
 \le -e^2-4<0,
\tag{2.2}
\]

while the second parenthesis is strictly positive.  Hence

\[
 \boxed{C'(q)<0\qquad(0\le q\le1).}
\tag{2.3}
\]

Together with \(C(0)>0\) and \(C(1)=-e/2<0\), continuity and strict
monotonicity prove the existence and uniqueness in (0.4), and give the
first three sign rows of (0.6) through \(q=1\).

For \(1\le q<2\), put \(t=2-q\in(0,1]\). The outer formula becomes

\[
 C(q)=-{1\over2}\bigl(\sinh t+t\cosh t\bigr)<0.
\tag{2.4}
\]

At \(q=2\), \(t=0\) and the same expression vanishes. Disjoint support
gives \(C(q)=0\) for \(q>2\). This completes the global sign theorem; no
finite sampling or root approximation is involved.

For reproducibility only, 128 steps of 80-digit Decimal bisection give the
display bracket

~~~text
0.63921327054652060848458059623449389674052859102219953924961666229265738695360745
  < xi <
0.6392132705465206084845805962344938967434673268992552580195385036357130011481541
~~~

This is a regression bracket, not a directed-rounding certificate.  The
analytical proof above is the certificate.

## 3. Exact ratio annuli

For positive source indices \(a,b\), define the unoriented ratio radius

\[
 \rho(a,b)=\max\left({a\over b},{b\over a}\right)
 =\exp\left|\log{a\over b}\right|\ge1.
\tag{3.1}
\]

Substituting \(u=\log(a/b)\) into (0.6) gives

\[
\boxed{
\begin{array}{c|c}
\text{ratio radius}&\mathcal R(\log(a/b))\\ \hline
1\le\rho<e^\xi&>0\\
\rho=e^\xi&=0\\
e^\xi<\rho<e^2&<0\\
\rho\ge e^2&=0.
\end{array}}
\tag{3.2}
\]

In oriented coordinates, the central positive annulus is

\[
 e^{-\xi}<{a\over b}<e^\xi.
\tag{3.3}
\]

The two negative outer annuli are

\[
 e^{-2}<{a\over b}<e^{-\xi},
 \qquad\text{or}\qquad
 e^\xi<{a\over b}<e^2.
\tag{3.4}
\]

The scalar vanishes on the two interior nodal ratios \(e^{-\xi},e^\xi\),
on the support boundaries \(e^{-2},e^2\), and everywhere outside the
closed ratio band.  Numerically, the positive annulus is approximately

\[
 0.52770742374848<{a\over b}<1.89498944869236,
\tag{3.5}
\]

but (3.2)--(3.4), not these decimals, are the theorem.

## 4. Integral and moment identities

The mean-zero derivative normalization has consequences that are invisible
from support alone.  Finite Fubini gives

\[
 \boxed{
 \int_{\mathbb R}\mathcal R(u)\,du
 =\left(\int_{\mathbb R}J_1(x)\,dx\right)^2=0.}
\tag{4.1}
\]

Thus pointwise nonnegativity was impossible before any explicit
calculation.  The sign theorem locates the required negative mass exactly,
and in particular

\[
 \int_{|u|<\xi}\mathcal R(u)\,du
 =-\int_{\xi<|u|<2}\mathcal R(u)\,du>0.
\tag{4.2}
\]

The two unit half-shell integrals obtained directly from (0.3) are

\[
 \boxed{
 \int_0^1\mathcal R(u)\,du={\sinh1\over2M^2},
 \qquad
 \int_1^2\mathcal R(u)\,du=-{\sinh1\over2M^2}.}
\tag{4.3}
\]

There are also two useful low moments.  Set

\[
 F(x)=\int_{-\infty}^xJ_1(t)\,dt={\Phi(x)\over M}.
\tag{4.4}
\]

For

\[
 h(x)=\int_{\mathbb R}|x-y|J_1(y)\,dy,
\]

mean zero gives \(h'(x)=2F(x)\). Compact integration by parts therefore
gives

\[
\begin{aligned}
 \int_{\mathbb R}|u|\mathcal R(u)\,du
 &=\iint_{\mathbb R^2}|y-x|J_1(x)J_1(y)\,dx\,dy\\
 &=-2\int_{\mathbb R}F(x)^2\,dx.
\end{aligned}
\tag{4.5}
\]

The elementary branch integral is

\[
 \int_{\mathbb R}\Phi(x)^2\,dx={\sinh2\over2}-1.
\tag{4.6}
\]

Since \(M^2=16\sinh^4(1/2)\), (4.5) becomes

\[
 \boxed{
 \int_{\mathbb R}|u|\mathcal R(u)\,du
 ={2-\sinh2\over16\sinh^4(1/2)}<0.}
\tag{4.7}
\]

Finally,

\[
\begin{aligned}
 \int_{\mathbb R}u^2\mathcal R(u)\,du
 &=\iint (y-x)^2J_1(x)J_1(y)\,dx\,dy\\
 &=-2\left(\int xJ_1(x)\,dx\right)^2.
\end{aligned}
\tag{4.8}
\]

The terms containing \(\int J_1\) vanish. Integration by parts in (0.1)
gives

\[
 \int xJ_1(x)\,dx
 ={1\over M}\int x\Phi'(x)\,dx=-1,
\tag{4.9}
\]

because \(\Phi\) vanishes at both support endpoints and has mass \(M\).
Consequently

\[
 \boxed{\int_{\mathbb R}u^2\mathcal R(u)\,du=-2.}
\tag{4.10}
\]

All Fubini and integration-by-parts steps above are absolute on compact
support.

## 5. Consequence for the beta-energy programme

The frozen first-rung energy expands as

\[
 \mathcal E_1(X)=
 \sum_{a,b\le X}{\beta(a)\beta(b)\over\sqrt{ab}}
 \mathcal R\!\left(\log{a\over b}\right).
\tag{5.1}
\]

The autocorrelation is a positive-definite translate kernel: for every
finite scalar vector \(c\),

\[
 \sum_{a,b}c_a\overline{c_b}\,
 \mathcal R(t_a-t_b)
 =\int_{\mathbb R}\left|\sum_ac_aJ_1(v-t_a)\right|^2dv\ge0.
\tag{5.2}
\]

Equation (0.6) shows exactly why this does not provide a pointwise
positivity shortcut.  Positive-definite kernels may have negative
off-diagonal entries, and this one is negative on every ratio radius
\(e^\xi<\rho<e^2\). Moreover, the source product
\(\beta(a)\beta(b)\) has its own sign. Therefore:

- the central ratio annulus is not a sum of positive beta terms;
- the two outer annuli cannot be discarded as a nonnegative error;
- Fourier-weight positivity applies only to the fully assembled quadratic
  form;
- replacing \(\mathcal R\) by \(|\mathcal R|\) destroys the exact zero-mass
  cancellation (4.1) and asks for a different, stronger estimate.

The exact geometry suggests a faithful decomposition of (5.1) into one
central and two reciprocal outer annuli, but it proves no cancellation
between them.  A subpower estimate for (5.1), or for its signed
off-diagonal part after subtracting the logarithmic diagonal, remains the
same RH-bearing burden identified in the frozen ladder.

## 6. Scope ledger

| statement | grade |
|---|---|
| normalized physical autocorrelation (0.3) | **PROVED EXACT** |
| one unique interior node and global sign geometry (0.6) | **PROVED EXACT** |
| central/outer ratio annuli (3.2)--(3.4) | **PROVED EXACT** |
| zeroth, absolute-first, and second moments | **PROVED EXACT** |
| strict translate-Gram positivity | **IMPORTED FROM / CONSISTENT WITH THE FROZEN FOURIER WEIGHT** |
| pointwise nonnegativity of the physical kernel | **FALSE** |
| beta-energy or signed off-diagonal subpower estimate | **NOT PROVED** |
| RH or GRH | **NOT PROVED** |

Equivalent criteria for RH are common.  No external novelty claim is made
without a dedicated literature comparison.

## 7. Bounded replay

The replay checks the four frozen Git blobs, independently compares (0.3)
with the branch integrals (1.3)--(1.4) at nine rational shifts, performs 128
bounded bisection steps, checks 129 inner-derivative and 257 sign samples,
and uses 512-panel-per-piece Simpson regressions for (4.1), (4.7), and
(4.10).  Decimal root data and quadrature are regression checks only; the
continuous claims are proved above.

It evaluates no zeta zero, prime, curve, finite field, random sample, or
L-function.

~~~text
python -B research/l-families/atlas/function_field/ffps_beta_gram_sign_geometry.py --check
python -B -O research/l-families/atlas/function_field/ffps_beta_gram_sign_geometry.py --check
python -B -m unittest tests.test_ffps_beta_gram_sign_geometry
python -B -O -m unittest tests.test_ffps_beta_gram_sign_geometry
python -B -m ruff check research/l-families/atlas/function_field/ffps_beta_gram_sign_geometry.py tests/test_ffps_beta_gram_sign_geometry.py
python -B -m ruff format --check research/l-families/atlas/function_field/ffps_beta_gram_sign_geometry.py tests/test_ffps_beta_gram_sign_geometry.py
~~~
