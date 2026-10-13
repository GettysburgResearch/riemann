# Cubic fibers, Riesz products, and the cost of reversing parity damping

**Status:** proposed research mathematics, 2026-10-12. The finite identities,
comparison inequalities, product-measure assertions, and subsequential noise
floor below have complete proofs. The zero-extraction statements retain the
stated detector and causal-inversion input. No full native moment, improvement
of a zero-free boundary, or RH conclusion is asserted.

**Main result.** Parity damping is an exact positive change of measure on
quadratic signs, and those signs have a native realization along cubic
multiples of an element row. The full change-of-measure cost is very large
below damping \(1/2\). After respecting the actual moment's finite frequency
support, its optimal generic \(L^2\) comparison cost has a precise, smaller
power: \(D^{k(1-2s)}\) when reversing to fixed \(s<1/2\). That loss is linear
in the order. Neither result excludes a better comparison for the particular
Möbius polynomial.

**Sources and boundaries.**

- The native family, the fixed compact detector, and the moving sixth-power
  extraction are from PR #926 at
  [086bf0560c0c2679a1fe41418f583d2c5ca743c3](https://github.com/GettysburgResearch/riemann/blob/086bf0560c0c2679a1fe41418f583d2c5ca743c3/standalone/2026-10-10-mobius-overlaps-and-sampled-moments/SAMPLED_MOMENT_CRITERION.md),
  equations (1.1)-(1.2), Proposition 2.1, and Section 6. Its fetched SHA-256 is
  18bf2fdad438eb21ae3318eba7d42e9c03803b2dd1abc4d8f6448fb3b04499de.
- The new conductor and Gaussian developments were read at PR #929,
  [97bf40329489992e9384c34d7595af6d01a40774](https://github.com/GettysburgResearch/riemann/blob/97bf40329489992e9384c34d7595af6d01a40774/standalone/2026-10-10-conductor-averages/README.md).
  Their positive conductor estimates do not supply a comparison between the
  two probability laws studied here.
- [PARITY_DAMPED_MOMENTS.md](PARITY_DAMPED_MOMENTS.md) defines and estimates
  the same damped functional. We repeat its definition with positive-mean
  quadratic signs, so that the native cube action is transparent. Its
  pointwise hypothesis is explicitly restated in Section 6.3; no numerical
  zero-free exponent is independently validated here.
- [ARITHMETIC_PARITY_OBSTRUCTION.md](ARITHMETIC_PARITY_OBSTRUCTION.md)
  treats a different obstruction, using actual prime-column faces and
  constant prime-count deformations. The elementary prime singularity
  needed below is also proved in Section 4.1.

The exact checker exercises finite residue fields, literal zeros, complete
CRT averages, finite product laws, and centered-chaos projections. It does
not establish an infinite moment or replace any analytic proof.

## 1. Native variables and the damped law

Let \(K=\mathbb Q(\sqrt{-3})\), \(\mathcal O=\mathbb Z[\omega]\), and let
\(S\) be a fixed finite set containing the primes above \(2,3\) and the
conductor of the fixed finite-order coefficient character \(\nu\).
Ideal columns are squarefree and prime to \(S\). All nonzero element rows
are present. For a good prime ideal \(p\), put \(q=Np\) and
\[
\chi_p(u)=(u/p)_6,\qquad
Q_p(u)=\chi_p(u)^3,\qquad C_p(u)=\chi_p(u)^4.
\tag{1.1}
\]
Thus \(\chi_p=Q_pC_p\), including at zero; \(Q_p\) is the nontrivial
quadratic character of the odd residue field, and \(C_p\) is cubic.

Fix a nonzero \(W\in C_c^\infty((1,2))\). It may be the nonnegative
universal test of the pinned source. For \(D\ge2\), let
\(\mathcal P_D=\{p\notin S:Np\le2D\}\). This finite set contains every
prime of every contributing column. Define the finite sign polynomial
\[
\mathcal A_u(D;\boldsymbol z)
=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D)z(n),
\quad z(n)=\prod_{p\mid n}z_p,\quad z_p\in\{-1,1\}.
\tag{1.2}
\]
For \(t\ge0\), let \(\mathbb P_{t,D}\) be the product law with
\[
\mathbb P_{t,D}(z_p=\pm1)=\frac{1\pm q^{-t}}2.
\tag{1.3}
\]
The law at \(t=0\) is the point mass at all \(+1\). Put
\[
F_{k,t}(D,H)=
\sum_{0<Nu\le H}\mathbb E_{t,D}|\mathcal A_u(D;\boldsymbol z)|^{2k}.
\tag{1.4}
\]
Then \(F_{k,0}=M_{2k}(D,H;W)\). The companion note instead uses
\(\epsilon_p=-z_p\), whose mean is \(-q^{-t}\), and omits \(\mu(n)\)
from its polynomial. These are exactly the same functional.

All uses of a fixed \(t>0\) below keep \(t\) fixed as \(D\) tends to
infinity. Constants are not asserted uniform as \(t\downarrow0\).

## 2. Cubic fibers are an exact arithmetic realization

### Proposition 2.1. Cube multiplication, with the masks retained

For every nonzero element \(u,a\) and every squarefree good \(n\),
\[
\chi_n(ua^3)=\chi_n(u)Q_n(a),\qquad
C_n(ua^3)=C_n(u)\mathbf1_{(a,n)=1},
\qquad Q_n(ua^3)=Q_n(u)Q_n(a).
\tag{2.1}
\]
Consequently
\[
A_{ua^3}(D;W)=\mathcal A_u(D;(Q_p(a))_p),
\tag{2.2}
\]
where (1.2) is evaluated with \(Q_p(a)=0\) at a nonunit.

**Proof.** Multiplicativity gives
\(\chi_n(a^3)=\chi_n(a)^3=Q_n(a)\). The cubic power is
\(\chi_n(a)^{12}\), which is one at a unit and zero otherwise.
The quadratic power is \(\chi_n(a)^9=\chi_n(a)^3\), again including
zero. These are the three identities. No condition \((a,u)=1\)
is required. \(\square\)

In particular, a cubic Walsh coefficient at \(ua^3\) equals the
corresponding coefficient at \(u\) with each column divisible by a prime
of \(a\) deleted. It is unchanged only when those auxiliary masks are
absent. An unconditional assertion that cube multiplication preserves
the whole coefficient array would be false.

Let \(\mathfrak f_D=\prod_{p\in\mathcal P_D}p\), and average over
\((\mathcal O/\mathfrak f_D)^\times\). The Chinese remainder theorem and
the equal sizes of the two quadratic classes in each residue field imply
that the \(Q_p(a)\) are independent fair signs on this complete unit set.
Define the positive Riesz product
\[
\mathcal R_{t,D}(a)
=\prod_{p\in\mathcal P_D}\bigl(1+q^{-t}Q_p(a)\bigr).
\tag{2.3}
\]
Its complete-unit mean is one, also at \(t=0\).

### Theorem 2.2. Exact complete-residue representation

For every fixed physical row \(u\),
\[
\boxed{
\mathbb E_{t,D}|\mathcal A_u(D;\boldsymbol z)|^{2k}
=\frac1{\varphi_K(\mathfrak f_D)}
\sum_{a\in(\mathcal O/\mathfrak f_D)^\times}
\mathcal R_{t,D}(a)|A_{ua^3}(D;W)|^{2k}.}
\tag{2.4}
\]
Any lift of \(a\) may be used on the right: the displayed polynomial
depends only on its residue. The original \(u\)-rows have not been
restricted. The auxiliary unit restriction is explicit.

**Proof.** A local quadratic value \(z\) has fair probability \(1/2\);
multiplication by \(1+q^{-t}z\) changes this to (1.3).
CRT multiplies these local laws. Apply (2.2). \(\square\)

At \(t=0\), (2.3) selects precisely the classes with every
\(Q_p(a)=+1\); (2.2) then equals \(A_u\). This also fixes the plus sign
in (2.3). A minus sign would represent a different law.

### 2.3. The physical cost of that representation

The norm is
\[
N(ua^3)=Nu\,(Na)^3.
\tag{2.5}
\]
Thus a fiber inside height \(H\) has \(Na\le (H/Nu)^{1/3}\).
The map from nonzero auxiliary elements to cube rows has multiplicity
three. Fixing one generator of each auxiliary ideal gives an injection,
but its unit choice must then be retained in the quadratic symbols.

Here is an elementary, fully paid completion estimate. Write
\(f=N\mathfrak f_D\), \(c_K=2\pi/\sqrt3\), and let \(B\ge1\).
For every residue class modulo \(\mathfrak f_D\), lattice counting gives
\[
\#\{a:Na\le B,\ a\equiv b\bmod\mathfrak f_D\}
=c_KB/f+O_K(1+\sqrt{B/f}).
\tag{2.6}
\]
The error is uniform in the class: the ideal lattice is a rotated
copy of the Eisenstein lattice scaled by \(\sqrt f\).
For every nonnegative periodic \(G\) supported on the unit classes,
\[
\left|\sum_{0<Na\le B}G(a)
-\frac{c_KB}{f}\sum_{b\bmod\mathfrak f_D}G(b)\right|
\le C_K(1+\sqrt{B/f})\sum_{b\bmod\mathfrak f_D}G(b).
\tag{2.7}
\]
The deletion of \(a=0\) is harmless, since \(G(0)=0\) when the modulus
is nontrivial; the trivial-modulus case is absorbed by the error.

Apply this to \(\mathcal R_{t,D}\) and to
\(\mathcal R_{t,D}|A_{ua^3}|^{2k}\), both extended by zero at nonunits.
Their normalized fiber ratio agrees with (2.4), with relative error
\(O_K(\sqrt{f/B}+f/B)\), whenever that error is sufficiently small.
This elementary guarantee therefore costs \(B\gg f\), and physical
height at least a constant multiple of \(Nu\,f^3\).
The full modulus contains every column prime; it is not the conductor
of one Hermitian tuple. Nothing here places a complete residue system
inside \(H=D^h\). The Riesz weights also cannot be discarded from a
weighted fiber average without paying for them.

## 3. Exact reverse comparison of the product laws

Fix \(0\le s<t<\infty\). Let \(a_p=q^{-s}\), \(b_p=q^{-t}\), and
\(\Delta_p=a_p-b_p\). The base law is \(\mathbb P_{t,D}\), which has
positive mass at every sign vector; the target is
\(\mathbb P_{s,D}\), possibly degenerate when \(s=0\).
Its likelihood ratio is
\[
L_{s,t,D}(\boldsymbol z)
=\prod_{p\in\mathcal P_D}\frac{1+a_pz_p}{1+b_pz_p}
=\prod_{p\in\mathcal P_D}
\left(1+\frac{\Delta_p(z_p-b_p)}{1-b_p^2}\right).
\tag{3.1}
\]

### Proposition 3.1. The full finite comparison cost

\[
\boxed{
\Gamma_{s,t}(D):=\mathbb E_{t,D}L_{s,t,D}^2
=\prod_{p\in\mathcal P_D}
\left(1+\frac{(q^{-s}-q^{-t})^2}{1-q^{-2t}}\right).}
\tag{3.2}
\]
For arbitrary \(Y\) on the finite sign cube,
\[
|\mathbb E_{s,D}Y|
\le \Gamma_{s,t}(D)^{1/2}\|Y\|_{L^2(\mathbb P_{t,D})}.
\tag{3.3}
\]
The constant is exact for this unrestricted linear comparison,
with equality at \(Y=L_{s,t,D}\).

**Proof.** Each centered variable \(z_p-b_p\) has mean zero and
variance \(1-b_p^2\). Squaring the local factor in (3.1) gives
the corresponding factor in (3.2). Independence and
Cauchy--Schwarz prove the assertions. \(\square\)

The unrestricted product is larger than the relevant comparison
space for a fixed-order moment. We now keep its actual frequency bound.

### Theorem 3.2. Optimal comparison on the moment's finite frequency space

Let \(\mathcal V_X(D)\) be the span of the sign monomials \(z(r)\)
over squarefree ideals \(r\) supported on \(\mathcal P_D\) with \(Nr\le X\).
Define
\[
\boxed{
K_X(s,t;D)^2
=\sum_{\substack{r\ {\rm squarefree}\\Nr\le X\\p\mid r\Rightarrow p\in\mathcal P_D}}
\prod_{p\mid r}
\frac{(q^{-s}-q^{-t})^2}{1-q^{-2t}}.}
\tag{3.4}
\]
Then, for every \(Y\in\mathcal V_X(D)\),
\[
|\mathbb E_{s,D}Y|\le K_X(s,t;D)\|Y\|_{L^2(\mathbb P_{t,D})}.
\tag{3.5}
\]
This is the exact norm of the expectation functional on that space.
For every \(\epsilon>0\),
\[
K_X(s,t;D)^2\ll_{s,t,K,S,\epsilon}
X^{\max(1-2s,0)+\epsilon}.
\tag{3.6}
\]
If \(s>1/2\), the right side can be replaced by a constant.

**Proof.** The functions
\[
e_r(\boldsymbol z)
=\prod_{p\mid r}\frac{z_p-b_p}{\sqrt{1-b_p^2}}
\tag{3.7}
\]
are orthonormal under the base law. The index set \(Nr\le X\) is
closed under taking divisors, so passing between the \(z(r)\) and
\(e_r\) bases preserves this exact space. Expansion of (3.1) gives
the coefficient
\[
d_r=\prod_{p\mid r}\frac{\Delta_p}{\sqrt{1-b_p^2}}
\]
at \(e_r\). The orthogonal projection of \(L_{s,t,D}\) onto
\(\mathcal V_X(D)\) has squared norm (3.4). It represents the
expectation functional there, proving both (3.5) and optimality.

Each local weight in (3.4) is at most \(C_{s,t}q^{-2s}\).
For fixed \(C\), \(C^{\omega(r)}\ll_\eta(Nr)^\eta\):
absorb each sufficiently large prime into its \(\eta\)-power and
the finitely many smaller primes into the constant. The elementary
ideal count \(I(x)\ll_Kx\) therefore gives (3.6) by partial summation.
For \(s>1/2\), the full Euler product converges, proving the stronger
constant bound. \(\square\)

### Corollary 3.3. A rigorously paid reverse-noise inequality

For each fixed \(u\),
\[
|\mathcal A_u(D;\boldsymbol z)|^{2k}
\in\mathcal V_{(2D)^{2k}}(D).
\tag{3.8}
\]
Indeed the radical of the product of the \(2k\) contributing columns
has norm at most their product, which is at most \((2D)^{2k}\).
Consequently, with \(J_H=\#\{u:0<Nu\le H\}\),
\[
\boxed{
F_{k,s}(D,H)
\le J_H^{1/2}K_{(2D)^{2k}}(s,t;D)
F_{2k,t}(D,H)^{1/2}.}
\tag{3.9}
\]
Here \(F_{2k,t}\) is the \(4k\)-th moment, not another \(2k\)-th
moment. Apply (3.5) row by row and Cauchy--Schwarz over the rows.

Thus a diagonal bound at order \(4k\) and damping \(t\) gives
\[
F_{k,s}(D,H)\ll_\epsilon
H D^{k+k\max(1-2s,0)+\epsilon}.
\tag{3.10}
\]
The constants are allowed to depend on fixed \(k,s,t\).
Section 4 shows that the extra exponent supplied by this generic
comparison is the actual power of its optimal linear-space norm.

Optimality in Theorem 3.2 concerns the entire linear space
\(\mathcal V_X(D)\). Its extremizer need not be nonnegative or
of the form \(|\mathcal A_u|^{2k}\). Neither this optimality nor
(3.10) rules out a stronger estimate for that special polynomial.

## 4. The three comparison regimes, proved without a prime number theorem

### 4.1. A sufficient prime-count subsequence

The Eisenstein lattice count, divided by its six units, gives
\[
I(x)=\frac{\pi}{3\sqrt3}x+O_K(\sqrt x).
\tag{4.1}
\]
Partial summation gives a meromorphic continuation of
\(\zeta_K(w)\) to \(\Re w>1/2\) near \(w=1\), with a simple
pole of positive residue there. On \(\Re w>1\),
\[
\sum_{p\notin S}(Np)^{-w}=\log\zeta_K(w)-E(w),
\tag{4.2}
\]
where \(E\) is holomorphic near \(1\): the prime-power terms of
degree at least two converge absolutely for \(\Re w>1/2\),
and the deleted first-prime terms are finite.

For any nonnegative nonzero \(V\in C_c^\infty((1,2))\), this implies
\[
\limsup_{D\to\infty}
\frac{\log(1+\sum_p V(Np/D))}{\log D}=1.
\tag{4.3}
\]
For completeness, the Mellin transform of the prime sum is
\(\widehat V(w)\sum_p(Np)^{-w}\) on \(\Re w>1\).
If the sum were \(O(D^{1-\delta})\) for any \(\delta>0\),
its Mellin integral would be holomorphic to the right of
\(1-\delta\). Its lower scale endpoint is positive by compact
support. This contradicts the logarithmic singularity at \(1\),
since \(\widehat V(1)>0\). The trivial ideal-count upper bound
proves (4.3). In particular, for every \(\delta>0\), there are
arbitrarily large \(D\) with at least \(D^{1-\delta}\) good prime
ideals in \((D,2D)\), after a harmless constant is absorbed by
decreasing \(\delta\).

### Theorem 4.1. Full-product and finite-frequency costs

Fix \(0\le s<t\).

1. If \(s>1/2\), \(\Gamma_{s,t}(D)\) remains uniformly bounded.
2. If \(s=1/2\), it tends to infinity but
   \(\Gamma_{s,t}(D)\ll_t(\log(3D))^{C_t}\).
   Thus its finite-\(D\) cost is subpower, despite the infinite-law
   singularity in Section 5.
3. If \(s<1/2\), then for every \(0<\delta<1-2s\), there are
   arbitrarily large \(D\) with
   \[
   \log\Gamma_{s,t}(D)\ge D^{1-2s-\delta}.
   \tag{4.4}
   \]
   In particular the full comparison cost is superpolynomial
   along those scales.
4. For every fixed integer \(k\ge1\) and \(s<1/2\), the relevant
   finite-frequency cost has the exact power
   \[
   \boxed{
   \limsup_{D\to\infty}
   \frac{\log K_{(2D)^{2k}}(s,t;D)}{\log D}
   =k(1-2s).}
   \tag{4.5}
   \]

**Proof.** For all sufficiently large primes, depending only on \(s,t\),
the logarithm of the local factor in (3.2) is bounded above and below
by positive fixed multiples of \(q^{-2s}\). This includes \(s=0\),
where the local factor is \(2/(1+q^{-t})\).
Absolute convergence gives the first claim.

The sum \(\sum_pq^{-1}\) diverges by (4.2). For the upper bound at
\(s=1/2\), put \(\sigma=1+1/\log(2D)\). For \(q\le2D\),
\(q^{-1}\le e q^{-\sigma}\), while
\(\sum_pq^{-\sigma}\le\log\zeta_K(\sigma)
=O_K(\log\log(3D))\) by (4.1).
Exponentiating proves the asserted polylogarithmic upper bound.

If \(s<1/2\), use the prime subsequence (4.3) and
\(q^{-2s}\ge(2D)^{-2s}\) on \((D,2D)\).
The number of such primes yields (4.4), after shrinking the
chosen error exponent to absorb the fixed constants.

The upper bound in (4.5) is (3.6). For its lower bound, use
\(2k\) distinct primes from \((D,2D)\). Each squarefree product
has norm at most \((2D)^{2k}\), different sets give different
ideals, and its summand in (3.4) is at least
\(c_{s,t,k}D^{-4ks}\). There are at least
\(c_kD^{2k(1-\eta)}\) such sets on the subsequence from (4.3).
Thus \(K^2\gg D^{2k(1-2s-\eta)}\) there.
Let \(\eta\) tend to zero. \(\square\)

The distinction matters: it would be incorrect to charge a fixed
moment the full superpolynomial product in (4.4) while ignoring
(3.8). The sharpened comparison still loses a positive multiple
of \(k\) for every fixed \(s<1/2\). At \(s=0\), (3.10) only
recovers the coefficient-trivial power \(HD^{2k+\epsilon}\).

## 5. Infinite product laws: equivalence above \(1/2\), singularity below

Let \(\mathbb P_s,\mathbb P_t\) denote the corresponding countable
product laws over all good prime ideals. These abstract probability
laws must not be confused with an incomplete disk of arithmetic rows.

### Theorem 5.1. Exact dichotomy for distinct fixed parameters

For \(0\le s<t<\infty\), the laws are equivalent if \(s>1/2\),
and mutually singular if \(s\le1/2\).

**Proof above \(1/2\).** The finite likelihood ratios (3.1) have
uniformly bounded \(L^2(\mathbb P_t)\) norm by Theorem 4.1.
More explicitly, for two nested finite prime sets their squared
\(L^2\) difference is the earlier squared norm times the later
local product minus one. The convergent product makes them
\(L^2\)-Cauchy. Their limit has expectation one and the correct
integrals on every cylinder set, hence is a density for
\(\mathbb P_s\). Reversing the laws gives the local factor
\(1+\Delta_p^2/(1-a_p^2)\), which also has a convergent product
when \(s>1/2\). Thus absolute continuity holds both ways.

**Proof at and below \(1/2\).** Here
\(V_{\mathcal P}=\sum_{p\in\mathcal P}\Delta_p^2\) tends to
infinity. Define
\[
Z_{\mathcal P}=\sum_{p\in\mathcal P}\Delta_p(z_p-b_p).
\tag{5.1}
\]
Under \(\mathbb P_t\), its mean is zero and variance at most
\(V_{\mathcal P}\). Under \(\mathbb P_s\), its mean is
\(V_{\mathcal P}\) and its variance is again at most that value.
Choose increasing finite sets with \(V_{\mathcal P_j}\ge j^3\).
Chebyshev's inequality and Borel--Cantelli give
\[
Z_{\mathcal P_j}/V_{\mathcal P_j}\longrightarrow0
\quad\mathbb P_t\text{-almost surely},\qquad
Z_{\mathcal P_j}/V_{\mathcal P_j}\longrightarrow1
\quad\mathbb P_s\text{-almost surely}.
\tag{5.2}
\]
These disjoint full-measure events prove mutual singularity.
The argument includes \(s=0\), where the target law is a point
mass. \(\square\)

Thus finite positivity does not supply a uniformly bounded change
of measure as damping decreases. In particular, distinct parameters
inside \(0<t\le3/8\) already give mutually singular infinite laws.
This is a statement about probability comparison, not about zeros
of a Hecke \(L\)-function. The endpoint \(s=1/2\) illustrates why
infinite singularity alone is insufficient to claim a power loss:
the finite products there still have only polylogarithmic cost.

## 6. The noise floor and its precise zero-extraction calibration

### Theorem 6.1. A diagonal floor at every fixed positive damping

Fix \(h>0\), \(k\ge1\), and \(t>0\). Then
\[
\boxed{
\lambda_{k,h}(t):=
\limsup_{D\to\infty}
\frac{\log(1+F_{k,t}(D,D^h))}{\log D}
\ge h+k.}
\tag{6.1}
\]
This is unconditional and subsequential; no prime number theorem
or pointwise Möbius estimate is used.

**Proof.** Center the signs: \(X_p=z_p-q^{-t}\). Expanding (1.2)
in products of the independent centered variables gives
\(\mathcal A_u=\sum_d b_d(u)\prod_{p\mid d}X_p\).
These products are pairwise orthogonal in \(L^2\), so
\[
\mathbb E_t|\mathcal A_u|^2
=\sum_d|b_d(u)|^2\prod_{p\mid d}(1-q^{-2t}).
\tag{6.2}
\]
If \(p\) contributes to \(W(Np/D)\), then \(D<Np<2D\).
Every proper multiple \(pm\), \(Nm>1\), is outside the column
support. Hence the centered coefficient at this prime is exactly
\[
b_p(u)=-\nu(p)\chi_p(u)W(Np/D).
\tag{6.3}
\]
No shorter-scale terms have been dropped from a general coefficient:
the support is what makes (6.3) exact.

Put \(P_W(D)=\sum_{p\notin S}|W(Np/D)|^2\).
A row \(0<Nu\le D^h\) has at most \(h\) distinct prime-ideal
divisors with norm greater than \(D\); otherwise the norm of their
product would exceed \(D^h\). Thus, uniformly in every such row,
\[
\mathbb E_t|\mathcal A_u|^2
\ge(1-D^{-2t})\bigl(P_W(D)-h\|W\|_\infty^2\bigr).
\tag{6.4}
\]
Use (4.3) with \(V=|W|^2\). On arbitrarily large scales the bracket
has size at least \(D^{1-\eta}\), with any prescribed \(\eta>0\)
after constants are absorbed. Jensen gives
\(\mathbb E_t|\mathcal A_u|^{2k}\ge
(\mathbb E_t|\mathcal A_u|^2)^k\).
There are \(\asymp_KD^h\) physical rows. Sum and let \(\eta\)
tend to zero. \(\square\)

At \(t=0\), the variances in (6.2) vanish. This proof supplies no
diagonal lower bound for the original Möbius moment.

### 6.2. Jensen shifts the detector and retains the damping loss

For fixed \(t\ge0\), put \(W_t(y)=y^{-t}W(y)\). Independence gives
\[
\mathbb E_t\mathcal A_u(D;\boldsymbol z)
=D^{-t}A_u(D;W_t).
\]
Therefore
\[
\boxed{
F_{k,t}(D,H)\ge D^{-2kt}M_{2k}(D,H;W_t).}
\tag{6.5}
\]
Also \(\widehat W_t(z)=\widehat W(z-t)\).
Choose the fixed compact universal test of PR #926, so that
\(\widehat W(z)\ne0\) for \(\Re z>0\).
The pinned sixth-power mask inversion and Mellin argument then give:
if, for fixed \(e\ge0\),
\[
F_{k,t}(D,D^h)\ll_\epsilon D^{h+k+e+\epsilon}
\quad\text{for every }\epsilon>0,
\tag{6.6}
\]
each fixed induced primitive twist is zero-free in
\[
\boxed{\Re z>\frac12+t+\frac{5h}{12k}+\frac e{2k}.}
\tag{6.7}
\]
The shifted detector is nonzero in this region. Equation (6.7)
is the original extraction applied to (6.5); it is not a new
zero-free theorem without (6.6).

Equivalently, a fixed induced zero \(\rho\), with
\(\beta=\Re\rho>t\), forces
\[
\lambda_{k,h}(t)\ge 2k(\beta-t)+h/6.
\tag{6.8}
\]
Here is the precise contrapositive behind this growth formulation.
If the exponent on the left were smaller, choose
\(t<\sigma<\beta\) with
\(\lambda_{k,h}(t)<2k(\sigma-t)+h/6\).
Equations (6.5) and the definition of limsup would make the
sixth-replica mean integrable against \(D^{-2k\sigma}dD/D\),
with a strictly negative dyadic exponent.
The pinned causal inverse gives the same weighted integrability
for the fixed row. Its Mellin transform is holomorphic to the
right of \(\sigma\), whereas
\(\widehat W(z-t)E_r(z)/L_K(z,\psi_r)\) has a pole at \(\rho\).
The finite Euler correction \(E_r\) is nonzero there. This is
the contradiction. No simultaneous choice of record scales at
different orders is required.

### 6.3. Separate the zero lower bound from the uniform pointwise input

For clarity, a sufficient pointwise hypothesis for the companion
upper theorem is the following, for a specified \(B\in[1/2,1]\):
for every fixed compact smooth \(V\) and every \(\epsilon>0\),
\[
|A_u(x;V)|\ll_{V,\nu,S,\epsilon}
(1+Nu)^\epsilon x^{B+\epsilon},
\qquad x\ge1,\quad u\ne0.
\tag{PW\(_B\)}
\]
Bounded scales below one are included at a changed constant.
The constants are uniform in the row. This is a uniform
pointwise assumption, not the definition of a supremum over zeros.
Finite moving column exclusions follow with a subpower factor
from the exact Euler-removal series: a deletion at \(d\) costs
at most \(\prod_{p\mid d}(1-q^{-B})^{-1}\ll_\epsilon(Nd)^\epsilon\).

The companion centered-sign proof, under this input, gives
\[
F_{k,t}(D,D^h)
\ll_{\epsilon,k,h,t}D^{h+k\max(1,2B-2t)+\epsilon}.
\tag{6.9}
\]
The coefficient estimate behind it is
\(|b_d|\ll D^\epsilon(D/Nd)^{B-t}\).
Symmetrization and the ordinary sign-cube moment inequality bound
the \(2k\)-norm by a fixed-degree weighted square sum of these
coefficients; ideal counting gives
\(\sum_d C_k^{\omega(d)}|b_d|^2
\ll D^{\max(1,2B-2t)+\epsilon}\).
This recalls the mechanism, while the full proof and its
quantifiers remain in the companion note.

Consequently, for fixed \(t>0\), the complete, separately qualified
comparison is
\[
\max\{h+k,\ 2k(\beta-t)+h/6\}
\le\lambda_{k,h}(t)
\le h+k\max(1,2B-2t),
\tag{6.10}
\]
where the second lower term is used only for an actual fixed
zero with \(\beta>t\), and the upper bound requires
\(({\rm PW}_B)\).

For fixed \(t>0\), along any cofinal sequence of fixed orders with
\(h_k=o(k)\),
the normalized lower frontier is at least \(1/2\) and at least
\(\beta-t\) for every such fixed zero. Its upper frontier under
\(({\rm PW}_B)\) is at most \(\max(1/2,B-t)\).
Equality follows only if those independently supplied lower and
upper exponents match. We do not identify a supremum of zero
real parts with a conductor-uniform pointwise exponent.

At \(t=B-1/2\), the companion diagonal bound and (6.7) recover
only the boundary \(B\) in the cofinal limit. When \(B=1/2\) and
\(t=0\), this assertion is conditional on \(({\rm PW}_{1/2})\);
it does not use or assert the positive-noise floor at zero damping.
Thus the forward
damping theorem does not improve the pointwise input by itself.
Crossing a positive interval of damping while retaining the
specific Möbius cancellation is the missing step.

## 7. What has changed, and what remains to prove

The native cube action gives an arithmetic realization of the biased
sign law. The exact Riesz products reveal a probability-measure
transition at \(1/2\). The finite-frequency projection replaces an
excessive full-product comparison by its exact fixed-order cost,
and proves that its remaining generic loss is linear in the order.
The diagonal noise floor and the Jensen adapter calibrate what a
given positive damping estimate can actually imply.

These results do not control an incomplete disk of cube parameters,
remove its moving masks, or prove decorrelation of the actual
quadratic signs from their cubic coefficients. A sharper estimate
could exploit the special Möbius polynomial and outperform the
linear-space comparison norm. Such an estimate is not contradicted
by the infinite-law singularity or by Theorem 3.2, and it is not
provided by them.
