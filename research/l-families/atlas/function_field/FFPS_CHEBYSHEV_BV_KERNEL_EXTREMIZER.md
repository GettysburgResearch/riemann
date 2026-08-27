# Chebyshev alternation gives the unique sharp-BV information-order kernel

Status: **sharp zero-extended variation and supremum theorems, unique
alternating step extremizer, exact optimum for the complete BV forward size,
and smooth-versus-BV Pareto comparison; uses the classical monic Chebyshev
minimax theorem and an internal second-kind Chebyshev duality argument; no new
beta cancellation or RH estimate**

Bounded replay:
[ffps_chebyshev_bv_kernel_extremizer.py](ffps_chebyshev_bv_kernel_extremizer.py).
Canonical summary:
[ffps_chebyshev_bv_kernel_extremizer.json](ffps_chebyshev_bv_kernel_extremizer.json).

Frozen source: the compact-kernel information-order theorem at commit
**ad78ecf6ac7e9dc099cb5fc3b1d40fca9aaa2b3f**. The producer pins all
four source blobs and imports no live predecessor module.

## 0. Outcome

Fix an information order \(r\in\mathbb Z_{\ge0}\). Let \(K\) be a real compact BV kernel
supported in \([0,1]\), zero-extended to \(\mathbb R\), with

\[
 \int_0^1t^qK(t)\,dt=0
 \quad(0\le q<r),
\tag{0.1}
\]

and normalized sensitivity

\[
 b=\frac{(-1)^r}{r!}\int_0^1t^rK(t)\,dt\ne0.
\tag{0.2}
\]

Then its zero-extended total variation satisfies the sharp inequality

\[
 \boxed{
 \operatorname{Var}_{\mathbb R}K
 \ge 2^{2r+1}(r+1)!\,|b|.}
\tag{0.3}
\]

Its supremum norm independently satisfies the sharp inequality

\[
 \boxed{
 \|K\|_\infty
 \ge r!2^{2r}|b|.}
\tag{0.3a}
\]

Equality has a unique derivative measure and therefore a unique kernel almost
everywhere. Put \(n=r+1\), define the shifted Chebyshev--Lobatto nodes

\[
 x_j=\frac{1+\cos(j\pi/n)}2,
 \qquad 0\le j\le n,
\tag{0.4}
\]

and endpoint-half weights

\[
 c_0=c_n=\frac12,
 \qquad
 c_j=1\quad(0<j<n).
\tag{0.5}
\]

The extremal distributional derivative is

\[
 \boxed{
 dK_*(t)
 =(-1)^{r+1}\operatorname{sgn}(b)\,
 r!2^{2r+1}|b|
 \sum_{j=0}^{n}(-1)^jc_j\delta_{x_j}.}
\tag{0.6}
\]

Its cumulative kernel alternates between the two values

\[
 \boxed{
 K_*(t)=\pm r!2^{2r}|b|}
\tag{0.7}
\]

on consecutive open Lobatto intervals. The same kernel simultaneously attains
(0.3) and (0.3a). Consequently it is the unique minimizer of the complete
forward BV size, with

\[
 \boxed{
 \|K_*\|_\infty=r!2^{2r}|b|,}
\tag{0.8}
\]

\[
 \boxed{
 \|K_*\|_\infty+\operatorname{Var}K_*
 =r!2^{2r}(2r+3)|b|,}
\tag{0.9}
\]

and

\[
 \boxed{
 \|K_*\|_2^2=(r!)^2\,2^{4r}b^2.}
\tag{0.10}
\]

Thus the BV-optimal detector is a finite Chebyshev step wavelet, not the smooth
beta/Legendre energy optimizer. The two solve different extremal problems.

## 1. From information moments to a measure problem

Let

\[
 \nu=dK
\tag{1.1}
\]

be the distributional derivative of the zero-extended BV kernel. Then

\[
 \|\nu\|_{\mathrm{TV}}
 =\operatorname{Var}_{\mathbb R}K,
 \qquad
 \nu(\mathbb R)=0.
\tag{1.2}
\]

Integration by parts gives, for \(q\ge0\),

\[
 \int_0^1t^{q+1}\,d\nu(t)
 =-(q+1)\int_0^1t^qK(t)\,dt.
\tag{1.3}
\]

The information-order conditions therefore say that \(\nu\) annihilates every
polynomial of degree at most \(r\), while

\[
 \int_0^1t^{r+1}\,d\nu(t)
 =(-1)^{r+1}(r+1)!\,b.
\tag{1.4}
\]

For every polynomial \(p\) of degree at most \(r\),

\[
 (r+1)!|b|
 =\left|\int_0^1(t^{r+1}-p(t))\,d\nu(t)\right|
 \le\|t^{r+1}-p\|_{\infty,[0,1]}\|\nu\|_{\mathrm{TV}}.
\tag{1.5}
\]

The entire problem is now the best uniform approximation of one monomial by
one lower polynomial degree.

## 2. The monic Chebyshev minimax input

The unique monic degree-\(n\) polynomial of least uniform norm on \([-1,1]\)
is \(2^{1-n}T_n\). Rescaling to \([0,1]\), the monic residual is

\[
 R_n(t)=2^{1-2n}T_n(2t-1),
\tag{2.1}
\]

with

\[
 \boxed{
 \min_{\deg p\le n-1}\|t^n-p(t)\|_{\infty,[0,1]}
 =2^{1-2n}.}
\tag{2.2}
\]

For \(n=r+1\), the error is \(2^{-2r-1}\). Substitution in (1.5) proves
(0.3).

The external classical input is exactly the monic minimax theorem recorded in
[DLMF §18.38](https://dlmf.nist.gov/18.38). The alternation criterion is also
summarized in [DLMF §3.11(i)](https://dlmf.nist.gov/3.11#i). No novelty or
priority is claimed for those approximation-theory facts.

## 3. Equality and uniqueness

At the nodes (0.4),

\[
 R_n(x_j)=2^{1-2n}(-1)^j.
\tag{3.1}
\]

The signed Lobatto weights

\[
 \lambda_j=(-1)^jc_j
\tag{3.2}
\]

annihilate every polynomial of degree at most \(n-1\). This is the classical
Chebyshev--Lobatto barycentric null vector; it also follows directly by taking
the leading divided difference at the \(n+1\) nodes.

Their absolute mass is

\[
 \sum_{j=0}^{n}c_j=n.
\tag{3.3}
\]

Scaling by

\[
 r!2^{2r+1}|b|
\tag{3.4}
\]

and applying the global sign in (0.6) gives the target moment (1.4). The total
variation is

\[
 n\cdot r!2^{2r+1}|b|
 =(r+1)!2^{2r+1}|b|,
\tag{3.5}
\]

so equality is attained.

Equality in (1.5) forces the derivative measure to live only where the
minimax residual reaches its extreme values, with matching alternating signs.
Those are precisely the \(n+1\) nodes (0.4). The \(n\) annihilation constraints
together with the target moment form a nonsingular Vandermonde system on those
nodes, so the weights are unique. This proves uniqueness of \(dK_*\), and the
zero boundary condition fixes \(K_*\) almost everywhere.

When the nodes are ordered from \(0\) to \(1\), cumulative endpoint-half and
interior-full weights alternate between plus and minus one half of the scale
(3.4). This proves (0.7)--(0.8) for the variation extremizer. Since the
absolute height is constant on the whole unit interval up to finitely many
nodes, (0.10) follows immediately. The remaining assertion that (0.9) is the
*complete* optimum follows from the independent supremum bound below.

### 3.1 The independent sharp supremum bound

For \(r\ge0\), put

\[
 P_r(t)=4^{-r}U_r(2t-1),
\tag{3.6}
\]

where \(U_r\) is the Chebyshev polynomial of the second kind. This is monic of
degree \(r\), and the substitution \(2t-1=\cos\theta\) gives

\[
 \int_0^1|P_r(t)|\,dt
 =\frac{4^{-r}}2\int_0^\pi|\sin((r+1)\theta)|\,d\theta
 =4^{-r}.
\tag{3.7}
\]

This candidate is the exact monic \(L^1[0,1]\) extremizer. Here is a short
internal dual proof. The function

\[
 \sigma_r(t)=\operatorname{sgn}U_r(2t-1)
\tag{3.8}
\]

annihilates every polynomial of degree below \(r\). Indeed, after the same
cosine substitution, a polynomial of degree below \(r\), multiplied by
\(\sin\theta\), is a linear combination of \(\sin(k\theta)\) with
\(1\le k\le r\); each is orthogonal to
\(\operatorname{sgn}\sin((r+1)\theta)\). Therefore, for every monic degree-
\(r\) polynomial \(P=t^r-p\) with \(\deg p<r\),

\[
 \int_0^1|P(t)|\,dt
 \ge \int_0^1\sigma_r(t)P(t)\,dt
 =\int_0^1|P_r(t)|\,dt
 =4^{-r}.
\tag{3.9}
\]

Apply (3.9) to the information moments (0.1)--(0.2):

\[
 r!|b|
 =\left|\int_0^1(t^r-p(t))K(t)\,dt\right|
 \le \|K\|_\infty\int_0^1|t^r-p(t)|\,dt.
\tag{3.10}
\]

Choosing the best \(p\) proves (0.3a). The alternating step kernel has exactly
this height, so it attains both independent lower bounds. Adding them gives

\[
 \boxed{
 \inf_K\bigl(\|K\|_\infty+\operatorname{Var}_{\mathbb R}K\bigr)
 =r!2^{2r}(2r+3)|b|.}
\tag{3.11}
\]

Any equality case in (3.11) must in particular attain the variation bound;
the uniqueness argument above therefore forces \(K=K_*\) almost everywhere.

## 4. First extremizers

The displayed examples use the normalization \(b=1\).

At order zero,

\[
 dK_*=\delta_0-\delta_1,
 \qquad
 K_*=\mathbf1_{(0,1)},
\tag{4.1}
\]

with

\[
 \operatorname{Var}K_*=2,
 \quad
 \|K_*\|_\infty=1,
 \quad
 \|K_*\|_2^2=1.
\tag{4.2}
\]

At order one, the nodes are \(0,1/2,1\) and

\[
 dK_*=4\delta_0-8\delta_{1/2}+4\delta_1.
\tag{4.3}
\]

Thus

\[
 K_*(t)=
 \begin{cases}
 4,&0<t<1/2,\\
 -4,&1/2<t<1,\\
 0,&\text{otherwise},
 \end{cases}
\tag{4.4}
\]

with

\[
 \operatorname{Var}K_*=16,
 \quad
 \|K_*\|_\infty=4,
 \quad
 \|K_*\|_2^2=16.
\tag{4.5}
\]

At order two, the nodes are \(0,1/4,3/4,1\). The step height is \(32\), and

\[
 \operatorname{Var}K_*=192,
 \quad
 \|K_*\|_\infty+\operatorname{Var}K_*=224,
 \quad
 \|K_*\|_2^2=1024.
\tag{4.6}
\]

The construction requires only \(r+2\) atoms at information order \(r\).

## 5. The energy--variation Pareto comparison

The smooth beta/Legendre carrier uniquely minimizes \(L^2\) detector energy at

\[
 C_r=(r!)^2(2r+1)\binom{2r}{r}^2.
\tag{5.1}
\]

The sharp-BV step detector has energy (0.10). Their exact ratio is

\[
 \boxed{
 \frac{\|K_*\|_2^2}{C_rb^2}
 =\frac{2^{4r}}
 {(2r+1)\binom{2r}{r}^2}.}
\tag{5.2}
\]

The first values are

\[
 1,\quad \frac43,\quad\frac{64}{45},\quad\frac{256}{175},\ldots
\tag{5.3}
\]

for \(r=0,1,2,3,\ldots\). Using the central-binomial asymptotic gives

\[
 \boxed{
 \frac{\|K_*\|_2^2}{C_rb^2}
 \longrightarrow\frac\pi2.}
\tag{5.4}
\]

So the exact price of optimizing variation rather than energy remains bounded:
as information order grows, the BV extremizer pays asymptotically a factor
\(\pi/2\) in \(L^2\) energy.

Conversely, the smooth beta optimizer has a larger BV cost. At \(r=1\), its
detector \(6-12t\) has zero-extended variation \(24\) and supremum \(6\),
whereas the step extremizer has variation \(16\) and supremum \(4\). The
tradeoff is genuine rather than a normalization artifact.

## 6. Consequence for the universal moving-kernel bound

The compact information-order theorem controls the RH-forward direction
through

\[
 M(K)=\|K\|_\infty+\operatorname{Var}_{\mathbb R}K.
\tag{6.1}
\]

For the sharp complete-BV step kernel,

\[
 M(K_*)=r!2^{2r}(2r+3)|b|.
\tag{6.2}
\]

After the sensitivity-preserving dilation
\(K_{*,S}(t)=S^{-r-1}K_*(t/S)\), the generic sufficient factor becomes

\[
 \mathcal G_X
 =\left(\frac{L_X}{S}\right)^{2r+2}
 \frac{2^{4r}(2r+3)^2}
 {(2r+1)\binom{2r}{r}^2}.
\tag{6.3}
\]

This is the exact all-order optimum for the universal BV forward constant, not
merely a certified family. A trade of larger variation for smaller supremum
cannot improve it: (0.3) and (0.3a) are independent lower bounds attained by
the same kernel. Formula (6.3) can therefore be compared sharply with the
smooth beta and exponential-tilt windows.

Nor does lower BV geometry provide beta cancellation. Under RH it sharpens a
forward constant; without RH, the hard Dirichlet-polynomial estimate remains.

## 7. Scope and firewalls

| statement | grade |
|---|---|
| sharp zero-extended variation bound (0.3) | **PROVED FROM CLASSICAL MINIMAX INPUT** |
| unique alternating Chebyshev step extremizer | **PROVED** |
| exact supremum, variation, BV size, and energy | **PROVED EXACT** |
| sharp supremum bound via the monic second-kind \(L^1\) extremal | **PROVED** |
| energy-gap ratio and \(\pi/2\) limit | **PROVED** |
| step kernel uniquely minimizes \(\|K\|_\infty+\operatorname{Var}K\) | **PROVED** |
| new beta cancellation or unconditional estimate | **NOT PROVED** |
| RH or GRH | **NOT PROVED** |

The support interval is normalized to \([0,1]\). Translation and
sensitivity-preserving dilation give the corresponding theorem on every finite
interval.

The minimizer is a BV step function. Point values at its finitely many jumps
are irrelevant; uniqueness is almost everywhere.

No function values, zeta zeros, primes, or curve data enter this extremal
theorem.

## 8. Bounded replay

The producer:

- verifies the frozen compact-kernel quartet by full Git blob ID;
- constructs \(T_n(2t-1)\) and its monic minimax normalization with exact
  rational polynomial arithmetic through information order six;
- constructs \(U_r(2t-1)\), its monic \(L^1\) normalization, and the exact
  sharp supremum constants through information order six;
- verifies the closed variation, step height, BV size, energy, and energy-gap
  formulas exactly;
- checks the \(r+2\) Lobatto atoms, moment annihilation, and target moment with
  a capped floating replay through order six; no root search is performed;
- records the DLMF minimax theorem as the one classical external input rather
  than pretending to prove it computationally;
- performs no beta sum, prime enumeration, zeta evaluation, random sampling,
  quadrature, or curve computation.

~~~text
python -B research/l-families/atlas/function_field/ffps_chebyshev_bv_kernel_extremizer.py --check
python -O -B research/l-families/atlas/function_field/ffps_chebyshev_bv_kernel_extremizer.py --check
python -B -m unittest tests.test_ffps_chebyshev_bv_kernel_extremizer
python -O -B -m unittest tests.test_ffps_chebyshev_bv_kernel_extremizer
python -m ruff check research/l-families/atlas/function_field/ffps_chebyshev_bv_kernel_extremizer.py tests/test_ffps_chebyshev_bv_kernel_extremizer.py
python -m ruff format --check research/l-families/atlas/function_field/ffps_chebyshev_bv_kernel_extremizer.py tests/test_ffps_chebyshev_bv_kernel_extremizer.py
~~~
