# Beta carrier moments form an all-order Legendre and pole-magnification tower

Status: **exact all-order field/source moment transform, exact
fixed-order signed-moment RH criteria, an RH-forward growing-order
window, exact shifted-Legendre Pythagorean tower, and exact
autocorrelation moment identities; no new beta estimate, proof of RH,
GRH, or growing-order converse**

Bounded replay:
[ffps_beta_carrier_legendre_moment_tower.py](ffps_beta_carrier_legendre_moment_tower.py).
Canonical summary:
[ffps_beta_carrier_legendre_moment_tower.json](ffps_beta_carrier_legendre_moment_tower.json).

Frozen source: the moving-support carrier phase diagram at commit
**fb5e545bcfceb8aeac1059d72e5cf94f99132d09**. The producer pins all
four source blobs and imports no live predecessor module.

## 0. Outcome

Let \(Q\) be one fixed compactly supported integrable real carrier on
\([0,S]\), with

\[
 \int_{\mathbb R}Q(u)\,du=1,
 \qquad
 J=DQ\in L^2(\mathbb R),
\tag{0.1}
\]

where the derivative is taken after zero extension. Put

\[
 a_n={\beta(n)\over\sqrt n},
 \qquad
 \beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67),
\tag{0.2}
\]

and

\[
 H_X(t)=\sum_{n\le X}a_nJ(t-\log n).
\tag{0.3}
\]

Define the carrier, beta-prefix, and field moments

\[
\begin{aligned}
 q_j&=\int_{\mathbb R}u^jQ(u)\,du,\\
 B_r(X)&=\sum_{n\le X}a_n(\log n)^r,\\
 M_k(X)&=\int_{\mathbb R}t^kH_X(t)\,dt.
\end{aligned}
\tag{0.4}
\]

Then, for every \(k\ge1\),

\[
\boxed{
 M_k(X)
 =
 -k\sum_{j=0}^{k-1}
 \binom{k-1}{j}q_jB_{k-1-j}(X).}
\tag{0.5}
\]

Because \(q_0=1\), this is triangular with leading term
\(-kB_{k-1}(X)\). Equivalently,

\[
\boxed{
 B_r(X)
 =-{M_{r+1}(X)\over r+1}
 -\sum_{j=1}^{r}\binom rj q_jB_{r-j}(X).}
\tag{0.6}
\]

The first-moment identity in the frozen source is only the first member
of this exact tower.

More strongly, for every one fixed integer \(k\ge1\),

\[
\boxed{
 \mathrm{RH}
 \quad\Longleftrightarrow\quad
 M_k(X)=X^{o(1)}.}
\tag{0.7}
\]

Thus each individual signed field moment is an RH-exact scalar
detector. An off-critical zeta zero of multiplicity \(m\) appears in
the corresponding differentiated beta Dirichlet series as a pole of
order \(m+k-1\). Higher moments magnify the pole order, but do not
provide the missing arithmetic bound.

At the level of power-growth exponents this is not a hierarchy of
progressively stronger criteria.  For every fixed nonzero polynomial
\(P\), the two prefixes

\[
 \sum_{n\le X}a_n
 \quad\hbox{and}\quad
 \sum_{n\le X}a_nP(\log n)
\tag{0.8}
\]

have the same infimal power-growth exponent.  The forward and reverse
transfers are elementary Abel transforms and cost only fixed powers of
\(\log X\).  Thus the pole magnification is analytically real but does
not, by itself, improve the Mertens exponent.

Here the power-growth exponent of a prefix \(C\) means
\(\inf\{\theta\ge0:C(X)=O_\varepsilon(X^{\theta+\varepsilon})\}\).

There is also an exact positive-energy organization. Let

\[
 L_X=\log X+S
\tag{0.9}
\]

and let \(P_k\) be the ordinary Legendre polynomial. Define

\[
\begin{aligned}
 d_k(X)
 &=
 \int_0^{L_X}
 H_X(t)P_k\!\left({2t\over L_X}-1\right)\,dt,\\
 A_{k-1}(X)
 &=
 -{L_X^k\over k\binom{2k}{k}}d_k(X).
\end{aligned}
\tag{0.10}
\]

Then \(A_{k-1}\) is a triangular combination of
\(B_0,\ldots,B_{k-1}\), with leading coefficient one. For every
\(R\ge1\),

\[
\boxed{
 \mathcal E_Q(X)
 =
 \sum_{k=1}^{R}
 {(2k+1)k^2\binom{2k}{k}^2\over L_X^{2k+1}}
 |A_{k-1}(X)|^2
 +\|\mathcal H_{X,>R}\|_2^2.}
\tag{0.11}
\]

The remainder is the orthogonal complement of the first \(R\) shifted
Legendre modes. Equation (0.11) is an all-order refinement of the
sharp \(12|B_0|^2/L_X^3\) decomposition.

As \(R\to\infty\), polynomial density in \(L^2([0,L_X])\) makes the
remainder decrease monotonically to zero.  Hence the infinite version
of (0.11) is a complete Parseval identity, not merely a finite lower
bound.

## 1. One exponential generating identity

Introduce the finite/entire exponential generating functions

\[
\begin{aligned}
 \mathscr Q(z)
 &=\int_{\mathbb R}e^{zu}Q(u)\,du
 =\sum_{j\ge0}q_j{z^j\over j!},\\
 \mathscr B_X(z)
 &=\sum_{n\le X}a_ne^{z\log n}
 =\sum_{r\ge0}B_r(X){z^r\over r!},\\
 \mathscr H_X(z)
 &=\int_{\mathbb R}e^{zt}H_X(t)\,dt
 =\sum_{k\ge0}M_k(X){z^k\over k!}.
\end{aligned}
\tag{1.1}
\]

Distributional integration by parts gives

\[
 \int_{\mathbb R}e^{zu}DQ(u)\,du
 =-z\mathscr Q(z).
\tag{1.2}
\]

Translation and finite summation therefore give the complete tower in
one line:

\[
\boxed{
 \mathscr H_X(z)
 =-z\mathscr Q(z)\mathscr B_X(z).}
\tag{1.3}
\]

Taking the coefficient of \(z^k/k!\) proves (0.5). Since
\(\mathscr Q(0)=1\), the formal power series
\(\mathscr Q(z)^{-1}\) exists, proving triangular recovery (0.6).

No positivity is used. Compact support, unit mass, and differentiation
after zero extension are load-bearing.

## 2. Every fixed signed moment is RH-equivalent

For fixed \(k\ge1\), define the monic degree-\((k-1)\) polynomial

\[
 R_{k-1}(x)
 =\int_{\mathbb R}(x+u)^{k-1}Q(u)\,du.
\tag{2.1}
\]

Equation (0.5) is equivalently

\[
 M_k(X)
 =-k\sum_{n\le X}a_nR_{k-1}(\log n).
\tag{2.2}
\]

### Forward direction

Under RH, the standard beta Mertens consequence is

\[
 B_0(X)=O_\varepsilon(X^\varepsilon)
\tag{2.3}
\]

for every \(\varepsilon>0\). Repeated partial summation gives

\[
 B_r(X)=O_{\varepsilon,r}(X^\varepsilon(\log X)^r)
 =X^{o(1)}
\tag{2.4}
\]

for each fixed \(r\). Equation (0.5) proves
\(M_k(X)=X^{o(1)}\).

### Elementary exponent equivalence

The fixed-polynomial equivalence can also be seen without the Dirichlet
series. Put

\[
 C_P(X)=\sum_{n\le X}a_nP(\log n)
\tag{2.5}
\]

for one fixed nonzero polynomial \(P\). Abel summation gives

\[
 C_P(X)
 =P(\log X)B_0(X)
 -\int_{1^-}^{X}B_0(t)P'(\log t){dt\over t}.
\tag{2.6}
\]

Conversely, choose a fixed \(T\) beyond the last positive \(t\) for
which \(P(\log t)=0\). Stieltjes division by the nonvanishing weight
gives

\[
 B_0(X)-B_0(T^-)
 ={C_P(X)\over P(\log X)}-{C_P(T^-)\over P(\log T)}
 +\int_T^X {C_P(t)P'(\log t)\over tP(\log t)^2}\,dt.
\tag{2.7}
\]

Thus each direction loses at most a fixed logarithmic factor. In
particular, \(C_P(X)=X^{o(1)}\) if and only if
\(B_0(X)=X^{o(1)}\), and their infimal power-growth exponents agree.
Taking \(P=R_{k-1}\) gives an elementary proof of the scalar
equivalence in (0.7). The pole argument below records additional local
analytic information that this exponent comparison does not see.

### A safe growing-order forward window

Although the converse above is deliberately fixed-order, the RH
forward direction has one useful uniform form. Define

\[
 B_0^*(X)=\sup_{1\le t\le X}|B_0(t)|.
\tag{2.8}
\]

For \(r\ge1\), partial summation gives

\[
 |B_r(X)|\le2B_0^*(X)(\log X)^r.
\tag{2.9}
\]

Since \(|q_j|\le\|Q\|_1S^j\), equation (0.5) and the binomial theorem
give, simultaneously for every \(k\ge1\),

\[
\boxed{
 |M_k(X)|
 \le 2k\|Q\|_1L_X^{k-1}B_0^*(X).}
\tag{2.10}
\]

Consequently RH implies \(M_{k(X)}(X)=X^{o(1)}\) throughout the safe
window

\[
 \log k(X)+k(X)\log L_X=o(\log X).
\tag{2.11}
\]

For fixed carrier support this includes
\(k=o(\log X/\log\log X)\). This is only a forward theorem: the
polynomial and differential operator move with \(X\), so the
fixed-operator converse below does not apply to a diagonal
\(k=k(X)\).

### Reverse direction and pole magnification

Let

\[
 F(s)=\sum_{n\ge1}{a_n\over n^s}.
\tag{2.12}
\]

In the original absolute-convergence half-plane,

\[
 F(s)
 ={1-67^{-(s+1/2)}\over\zeta(s+1/2)}.
\tag{2.13}
\]

The coefficient Dirichlet series attached to (2.2) is

\[
 G_k(s)
 =-kR_{k-1}(-\partial_s)F(s).
\tag{2.14}
\]

If \(M_k(X)=X^{o(1)}\), Abel summation makes \(G_k\) holomorphic on
\(\Re s>0\).

Suppose \(\rho\) were a zeta zero with \(\Re\rho>1/2\), of
multiplicity \(m\), and put \(s_0=\rho-1/2\). The exceptional numerator
in (2.13) is nonzero because \(|67^{-\rho}|<1\). Hence \(F\) has a pole
of order \(m\) at \(s_0\). Since \(R_{k-1}\) is monic, the top
derivative in (2.14) has a nonzero pole of order

\[
 m+k-1,
\tag{2.15}
\]

while every lower derivative has strictly smaller pole order. No
cancellation is possible. This contradicts holomorphy of \(G_k\).
The functional equation supplies the reflected half, proving (0.7).

This is pole-order magnification, not a new estimate or a theorem about
the multiplicity of zeros on the critical line.

## 3. Shifted-Legendre Pythagorean tower

The shifted Legendre polynomial has the exact expansion

\[
 P_k(2x-1)
 =
 \sum_{m=0}^{k}
 (-1)^{k-m}
 \binom km\binom{k+m}{m}x^m
\tag{3.1}
\]

and orthogonality

\[
 \int_0^L
 P_j\!\left({2t\over L}-1\right)
 P_k\!\left({2t\over L}-1\right)\,dt
 ={L\over2k+1}\mathbf1_{j=k}.
\tag{3.2}
\]

Because \(M_0=\int H_X=0\), the constant mode vanishes. Orthogonal
projection gives

\[
 \mathcal E_Q(X)
 =
 \sum_{k=1}^{R}{2k+1\over L_X}|d_k(X)|^2
 +\|\mathcal H_{X,>R}\|_2^2.
\tag{3.3}
\]

The leading coefficient of (3.1) is
\(\binom{2k}{k}\). Combining it with the leading term
\(-kB_{k-1}\) in \(M_k\) shows that the normalization in (0.10)
makes

\[
 A_{k-1}(X)
 =B_{k-1}(X)
 +\text{a linear combination of }B_0,\ldots,B_{k-2}.
\tag{3.4}
\]

Substituting (0.10) into (3.3) proves (0.11).

The projection is sharp for its complete moment vector: equality after
truncation occurs exactly when \(H_X\) lies in the span of the first
\(R\) shifted Legendre modes.

## 4. The first three exact channels

Write \(L=L_X\). The first adjusted beta moments are

\[
 A_0=B_0,
\tag{4.1}
\]

\[
 A_1
 =B_1+\left(q_1-{L\over2}\right)B_0,
\tag{4.2}
\]

and

\[
 A_2
 =
 B_2+(2q_1-L)B_1
 +\left(q_2-Lq_1+{L^2\over5}\right)B_0.
\tag{4.3}
\]

Therefore

\[
\boxed{
\begin{aligned}
 \mathcal E_Q(X)
 &=
 {12|B_0|^2\over L^3}
 +{720|A_1|^2\over L^5}\\
 &\quad
 +{25200|A_2|^2\over L^7}
 +\|\mathcal H_{X,>3}\|_2^2.
\end{aligned}}
\tag{4.4}
\]

The constants are the first values of

\[
 C_k=(2k+1)k^2\binom{2k}{k}^2:
 \qquad
 12,\ 720,\ 25200,\ldots.
\tag{4.5}
\]

These channels separate the ordinary beta prefix, its first centered
logarithmic drift, and its second centered logarithmic curvature.

## 5. Autocorrelation moment tower

For the signed autocorrelation

\[
 \mathcal C_X(u)
 =\int_{\mathbb R}H_X(v)H_X(v+u)\,dv,
\tag{5.1}
\]

finite support and the substitution \(w=v+u\) give, for every
\(r\ge0\),

\[
\boxed{
 \int_{\mathbb R}u^r\mathcal C_X(u)\,du
 =
 \sum_{j=0}^{r}
 (-1)^j\binom rj M_j(X)M_{r-j}(X).}
\tag{5.2}
\]

The odd rows vanish by symmetry. Since \(M_0=0\), the first two
nontrivial even rows are

\[
 \int u^2\mathcal C_X(u)\,du
 =-2M_1^2=-2B_0^2,
\tag{5.3}
\]

and

\[
 \int u^4\mathcal C_X(u)\,du
 =6M_2^2-8M_1M_3.
\tag{5.4}
\]

With the Fourier convention
\(\widehat H(\omega)=\int H(t)e^{-i\omega t}dt\), the positive spectral
density \(\mathcal P(\omega)=|\widehat H(\omega)|^2\) satisfies

\[
 \mathcal P^{(2r)}(0)
 =(-1)^r\int u^{2r}\mathcal C_X(u)\,du.
\tag{5.5}
\]

Thus (5.3) corresponds to the positive curvature
\(\mathcal P''(0)=2B_0^2\). Total energy is the autocorrelation at zero
lag; the moment tower sees the local spectral jet at zero frequency.

## 6. Scope and firewalls

| statement | grade |
|---|---|
| exponential generating identity (1.3) | **PROVED EXACT** |
| triangular field/source moment transform (0.5)--(0.6) | **PROVED EXACT** |
| each fixed signed field moment is RH-equivalent | **PROVED** |
| fixed-polynomial power-exponent equivalence | **PROVED** |
| RH-forward window \(k\log L_X=o(\log X)\) | **PROVED** |
| off-line pole order becomes \(m+k-1\) | **PROVED** |
| shifted-Legendre Pythagorean tower (0.11) | **PROVED EXACT** |
| first three constants and adjusted moments | **PROVED EXACT** |
| all-order autocorrelation moment identity | **PROVED EXACT** |
| new unconditional subpower estimate for any moment | **NOT PROVED** |
| growing \(k=k(X)\) converse/equivalence | **NOT PROVED** |
| zero-multiplicity theorem on the critical line | **NOT PROVED** |
| RH or GRH | **NOT PROVED** |

The carrier is fixed before \(X\) varies. The analytic converse fixes
the order \(k\) as well. If \(Q=Q_X\) moves with the horizon, its
moment polynomial in (2.1) also moves and the fixed
differential-operator converse no longer applies without another
uniform argument.

This failure is concrete, not merely technical. Equation (0.5) gives

\[
 M_2=-2(B_1+q_1B_0).
\tag{6.1}
\]

Whenever \(B_0\ne0\), a horizon-dependent signed normalized smooth
carrier can choose \(q_1=-B_1/B_0\) and force \(M_2=0\). Such a carrier
exists: two fixed smooth compact bumps with distinct centers have an
invertible mass/first-moment matrix, and their linear combination
realizes any prescribed \(q_1\), with \(DQ\in L^2\). Therefore an
isolated moving higher-moment bound cannot inherit the fixed-operator
RH converse.

The higher shifted-Legendre modes depend on \(L_X\). An isolated bound
for one such moving mode is not asserted to imply RH. The complete
tower is a positive geometric organization of the field, while the
fixed raw moments \(M_k\) are the individual analytic criteria.

No external novelty or priority is claimed without a dedicated
literature comparison.

## 7. Bounded replay

The producer:

- verifies the frozen moving-support quartet by full Git blob ID;
- checks (0.5) for orders \(1\) through \(6\);
- verifies shifted-Legendre orthogonality exactly through degree \(6\);
- checks the triangular leading coefficients and constants
  \(12,720,25200\);
- checks the autocorrelation moment convolution through order \(8\);
- uses rational/integer polynomial arithmetic only;
- performs no beta sum, prime enumeration, zeta evaluation, random
  sampling, quadrature, or curve computation.

~~~text
python -B research/l-families/atlas/function_field/ffps_beta_carrier_legendre_moment_tower.py --check
python -O -B research/l-families/atlas/function_field/ffps_beta_carrier_legendre_moment_tower.py --check
python -B -m unittest tests.test_ffps_beta_carrier_legendre_moment_tower
python -O -B -m unittest tests.test_ffps_beta_carrier_legendre_moment_tower
python -m ruff check research/l-families/atlas/function_field/ffps_beta_carrier_legendre_moment_tower.py tests/test_ffps_beta_carrier_legendre_moment_tower.py
python -m ruff format --check research/l-families/atlas/function_field/ffps_beta_carrier_legendre_moment_tower.py tests/test_ffps_beta_carrier_legendre_moment_tower.py
~~~
