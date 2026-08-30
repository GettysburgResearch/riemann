# Actual-Xi companion components have infinite global zero height

Status: NEW CONDITIONAL COMPONENT-BOUNDARY RESULT; exact-SHA review required.
Scope: the actual standard Xi function, each fixed real lambda > 0, and the
zeroth and fifth derivative companions, conditional on RH or the explicit
real-zero/Hermite--Biehler premise below. This is not a statement about the
native quotient after common-inner cancellation. RH remains unsolved.

Arithmetic: MIXED, with CERTIFIED_INTEGER_COVERAGE and EXACT_RATIONAL components.
The finite checker has no floating-point or transcendental evaluation and no
rounding. Its bounded algebra is not a machine proof of the analytic limits.
Seven literal Git/blob/LF-SHA source identities are in the adjacent manifest.

## 1. Statement, normalization, and native allocation

Use the actual full-line kernel and normalization of pinned XL1--XL4:
\[
 \Xi(z)=\xi_{\rm R}(1/2+iz)=\int_{\mathbb R}\Phi(u)e^{izu}\,du,\qquad
 \xi_{\rm R}(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
 \tag{GH1}
\]
Here Phi is positive, even, and superexponentially decreasing; in particular
it is twice the historical phi_0 in XL2. There is no frequency rescaling.
Put \(f_k=\Xi^{(k)}\), for \(k=0,5\), and fix lambda > 0 independently of z.
Define, with removable common real zeros canceled,
\[
 \Theta_{k,\lambda}(z)
   =\frac{f_k(z)-i\lambda f_k'(z)}{f_k(z)+i\lambda f_k'(z)}.
 \tag{GH2}
\]

**Conditional component theorem.** Assume RH. More explicitly it is enough
to assume that Xi has only real zeros; Section 2 proves the needed same
property for \(f_5\) and the Hermite--Biehler inequality. One may instead
assume directly that both displayed quotients are inner in the upper
half-plane; for a single-component conclusion only its own inner premise
is needed. Under the two-component premise, both quotients in (GH2) are
meromorphic PURE Blaschke products up to unimodular constants, and
\[
 \boxed{\quad
   \sum_{\Theta_{0,\lambda}(b)=0,\ \Im b>0}\Im b
   =\sum_{\Theta_{5,\lambda}(b)=0,\ \Im b>0}\Im b
   =+\infty.\quad}
 \tag{GH3}
\]
Every zero is counted with its full multiplicity. The parameter lambda = 0
is excluded: after removal its quotient is 1 and its height sum is zero.

The source allocation is important. Pinned L-106620.4--.6 identifies
\[
 U_{5,j}=\frac{R_{0,j}C_{5,j}}{C_{0,j}R_{5,j}}
 =\frac{(\Xi-i\lambda_j\Xi')(\Xi^{(5)}+i\lambda_j\Xi^{(6)})}
        {(\Xi+i\lambda_j\Xi')(\Xi^{(5)}-i\lambda_j\Xi^{(6)})}
 =\Theta_{0,\lambda_j}/\Theta_{5,\lambda_j}.
 \tag{GH4}
\]
Under the premise, the plus companions have no upper-half-plane zeros.
Thus Theta_0 supplies the unreduced numerator inner divisor and Theta_5
the unreduced denominator inner divisor. The first component is NOT itself
the native denominator. If G is their maximal common Blaschke divisor,
write \(\Theta_0=G B_0,\ \Theta_5=G B_5\), absorbing harmless constants.
This note does NOT prove \(\sum_{B_5(b)=0}\Im b=\infty\).

The quantitative imaginary-axis facts used below are, for fixed lambda,
\[
 \begin{split}
 y[-\log|\Theta_{k,\lambda}(iy)|]&\sim
           \frac{4y}{\lambda\log y}\longrightarrow\infty
           \quad(k=0,5),\\
 \log|\Theta_{5,\lambda}(iy)/\Theta_{0,\lambda}(iy)|
   &\sim\frac{40}{\lambda y(\log y)^3}.
 \end{split}                                                   \tag{GH5}
\]
The second line is a signed comparison, not an unsigned divisor bound.

## 2. Real zeros, correct half-plane, and removable factors

UC3 supplies \(\log^+\max_{|z|\le R}|f_k(z)|=O(R\log(R+2))\);
thus their order is at most one. We import the classical Hadamard
factorization theorem for finite-order entire functions. Under the real-zero
premise, evenness pairs the genus-one factors of Xi, giving
\[
 \Xi(z)=\Xi(0)\prod_{\gamma>0}(1-z^2/\gamma^2)^{m_\gamma},
 \qquad \sum_{\gamma>0}m_\gamma/\gamma^2<\infty.              \tag{GH6}
\]
The possible linear exponential is constant by evenness. Xi(0)>0 follows
from GH1. Its nonzero high even derivatives, also from the positive kernel,
exclude a constant or finite-degree Xi. Finite partial products in GH6
converge locally uniformly. Their fifth derivatives have only real zeros
by repeated Rolle; local uniform convergence of derivatives and Hurwitz
therefore give real zeros for the nonzero \(f_5\). Its oddness similarly
removes the linear exponential in its Hadamard product. Its zero at 0 is
simple, since \(\Xi^{(6)}(0)=-\int u^6\Phi(u)\,du\ne0\).

For either f, the paired logarithmic derivative is a locally normally
convergent sum of terms \(m/(z-r)\), \(r\in\mathbb R\), with possible
origin term \(1/z\). Consequently
\[
 \Im\frac{f'(z)}{f(z)}<0\quad(\Im z>0).                     \tag{GH7}
\]
There is at least one real zero: otherwise the order-one factorization
and parity would make f constant or a multiple of z, contrary to its
kernel derivatives. Each individual summand has negative imaginary part;
pairing only ensures convergence and does not change this sign.

Put \(w=i\lambda f'/f\). Then \(\Re w>0\), so
\(|(1-w)/(1+w)|<1\) and \(1+w\ne0\). This proves holomorphy and strict
contractivity of GH2 in the upper half-plane. On the real line its modulus
is 1 wherever the denominator is nonzero. A real denominator zero requires
both f and f' to vanish. If \(f(z)=(z-r)^m g(z)\), \(g(r)\ne0\), each
companion contains exactly \((z-r)^{m-1}\), and their quotient tends to
\((-i\lambda m g(r))/(i\lambda m g(r))=-1\). After cancellation GH2
extends holomorphically and unimodularly across every finite real point.
In particular, multiple real zeros of Xi do not require a simplicity
assumption. Nor do they create an upper-half-plane common f/f' zero.

## 3. Actual imaginary-axis asymptotics, including the fifth derivative

Let \(h(y)=\Xi(iy)=\xi_{\rm R}(1/2+y)>0\). The equality uses the functional
equation; positivity and differentiation under the integral follow from GH1.
For y > 0, every \(h^{(r)}(y)>0\): the half-line integrals use \(u^r\cosh(yu)\)
for even r and \(u^r\sinh(yu)\) for odd r, with positive weight \(2\Phi(u)\).
The exact phase is
\[
 \Xi^{(r)}(iy)=(-i)^r h^{(r)}(y),\quad
 \Xi^{(5)}(iy)=-i h^{(5)}(y),\quad
 \Xi^{(6)}(iy)=-h^{(6)}(y).
 \tag{GH8}
\]
In particular \(D_k=h^{(k+1)}/h^{(k)}\) is well defined for y > 0 and
\[
 \Theta_{k,\lambda}(iy)=\frac{1-\lambda D_k(y)}
                            {1+\lambda D_k(y)}.             \tag{GH9}
\]

For \(s=y+1/2>1\), the literal completed function gives
\[
 D=D_0=\frac1s+\frac1{s-1}-\frac{\log\pi}{2}
           +\frac12\psi(s/2)+\frac{\zeta'(s)}{\zeta(s)}
   =\tfrac12\log(y/(2\pi))+O(y^{-1}).                        \tag{GH10}
\]
The gamma and polygamma expansions further give
\[
 D'=\frac1{2y}+O(y^{-2}),\qquad
 D^{(j)}=O_j(y^{-j})\quad(1\le j\le5).
 \tag{GH11}
\]
These differentiated bounds are not obtained by differentiating an arbitrary
O-term: they follow directly by differentiating the rational terms and using
the polygamma expansion for each indicated order. On the positive real axis
the differentiated zeta Dirichlet series are exponentially small: for fixed
r and s >= 4,
\(\sum_{n\ge2}(\log n)^r n^{-s}\le
2^{-s/2}\sum_{n\ge2}(\log n)^r n^{-2}\);
division by zeta(s), which tends to 1, preserves these estimates.

For clarity the necessary Bell-polynomial computation is written out.
Let \(P_r=h^{(r)}/h\), so \(P_0=1\) and \(P_{r+1}=DP_r+P_r'\). Then
\[
 P_5=D^5+10D^3D'+10D^2D''+15D(D')^2
          +5DD'''+10D'D''+D^{(4)}.                         \tag{GH12}
\]
Using GH11, \(P_5/D^5=1+O(1/(yD^2))\). Differentiating this *polynomial*
through the exact recurrence, rather than an asymptotic remainder, gives
\[
 \begin{split}
 D_5-D&=P_5'/P_5=\frac{5D'}D+
                       O\!\left(\frac1{y^2D^2}\right)
                  \sim\frac5{y\log y}.
 \end{split}                                             \tag{GH13}
\]
Indeed the numerator \(D P_5'-5D'P_5\) is
\[
 \begin{split}
 &10D^4D''-20D^3(D')^2+10D^3D'''+5D^2D^{(4)}
       -60D(D')^3-10DD'D'''\\
 &\hspace{6mm}+10D(D'')^2+DD^{(5)}
       -50(D')^2D''-5D'D^{(4)}.
 \end{split}                                               \tag{GH14}
\]
Every term is \(O(D^4/y^2)\), and \(DP_5\sim D^6\).

It follows that \(D_k\sim\tfrac12\log y\) and Theta_k(iy) tends to -1.
For sufficiently large y, \(\lambda D_k>1\), so the elementary real expansion
\[
 -\log|\Theta_k(iy)|
 =\log\frac{\lambda D_k+1}{\lambda D_k-1}
 \sim\frac2{\lambda D_k}
 \tag{GH15}
\]
proves the first line of GH5. For the ratio, write
\(F(x)=\log((\lambda x-1)/(\lambda x+1))\).
Then \(F'(x)=2\lambda/((\lambda x)^2-1)\).
The mean value theorem, GH10 and GH13 give
\(F(D_5)-F(D_0)\sim[8/(\lambda(\log y)^2)]
\,[5/(y\log y)]\), namely the second line of GH5.
The product of these two leading factors is
\(40/(\lambda y(\log y)^3)\); no uniform-in-lambda error is asserted.

## 4. Singular factors and the extended height identity

The classical meromorphic-inner factorization is
\(\Theta=c e^{iaz}B\), \(|c|=1,\ a\ge0\), B a pure Blaschke product.
There is no finite-boundary singular measure when the function continues
meromorphically across the whole real line. Our stronger holomorphic
unimodular continuation in Section 2 verifies that condition directly.
Since \(|\Theta(iy)|\to1\), the bound
\(|\Theta(iy)|\le e^{-ay}\) forces a = 0. This argument does not assume
finite exponential type or a finite unweighted zero-height sum.

Here is the required identity for ANY pure upper-half-plane Blaschke product,
with zeros \(b_j=a_j+i\eta_j\), \(\eta_j>0\), repeated with multiplicity:
\[
 \boxed{\quad \lim_{y\to\infty}y[-\log|B(iy)|]
                      =2\sum_j\eta_j\quad}
 \tag{GH16}
\]
in the extended interval [0,infinity]. Unimodular normalizing constants do
not matter. The empty product has both sides zero. At zeros logarithms
take value +infinity, with the usual limiting interpretation.

For each factor put
\[
 t_j(y)=\tfrac12\log\left(1+
                 \frac{4y\eta_j}{a_j^2+(y-\eta_j)^2}\right).
 \tag{GH17}
\]
The product modulus gives \(-\log|B(iy)|=\sum_j t_j(y)\), with nonnegative
summands. For each fixed j, \(yt_j(y)\to2\eta_j\). If
\(S=\sum_j\eta_j<\infty\), every eta_j <= S and for y >= 2S,
\[
 0\le yt_j(y)\le
 \frac{2y^2\eta_j}{a_j^2+(y-\eta_j)^2}\le8\eta_j.
 \tag{GH18}
\]
Dominated convergence proves GH16 for finite S. If S is infinite,
each finite subproduct gives a lower bound with limit twice its height;
letting its height tend to infinity proves the extended limit. GH15 and
GH16 now prove GH3. Nothing about finite-band traces enters this proof.

## 5. The cancellation gate, and a nonnative comparison control

The common divisor G in Section 1 is well defined by minimum multiplicities;
its zero set is a subsequence of either Blaschke sequence. Its removal
leaves pure Blaschke products B_0 and B_5. Their quotient is still GH4.
The ratio asymptotic in GH5 implies
\[
 \lim_{y\to\infty}y\log|B_5(iy)/B_0(iy)|=0.                \tag{GH19}
\]
Applying GH16 separately shows this exact dichotomy: either both reduced
height sums are infinite, or both are finite and equal. If one were finite
and the other infinite, their difference would diverge. Infinity minus
infinity is not assigned a value in this argument. GH19 does not decide
between the two alternatives.

Even the displayed log-corrected leading term cannot decide this for
general pure Blaschke pairs. Here is a NONNATIVE example with a full proof.
Fix c > 0, let \(S=c\sum_{n\ge1}n^{-4}=c\zeta(4)\), let V_0 have its single
zero at iS, and let V_5 have zeros \(e^n+i c/n^4\), n >= 1.
They are pure meromorphic Blaschke products with no common zeros and
identical finite unweighted heights S. Nevertheless
\[
 \log|V_5(iy)/V_0(iy)|
 =\frac{2c}{3y(\log y)^3}
   +O_c\left(\frac1{y(\log y)^4}+\frac1{y^3}\right).
 \tag{GH20}
\]
Thus c = 60/lambda reproduces exactly the leading coefficient in GH5.
One may also multiply both by a common pure Blaschke G with zeros
\(-2^n+i\), n >= 1. Its Blaschke sum converges geometrically but its
unweighted height is infinite; it is disjoint from both displayed zero
sets. The resulting two components both have infinite height, their
coprime reductions still have equal finite height S, and GH20 is unchanged.

To prove it, for bounded eta > 0, uniformly in real a as y tends to infinity,
\[
 t(a,\eta;y)=\operatorname{arctanh}
    \frac{2y\eta}{a^2+y^2+\eta^2}
   =\frac{2y\eta}{a^2+y^2}+O(\eta^3/y^3).                 \tag{GH21}
\]
For y >= 2eta the argument is <= 4/5; the arctanh power series bounds
its remainder by a constant times the cube. Replacing its denominator
by \(a^2+y^2\) costs at most \(2\eta^3/y^3\). Summing the errors is
legitimate because \(\sum(c/n^4)^3<\infty\). The single factor of V_0
has the analogous expansion with eta = S. Setting t = log y yields
\[
 \log|V_5(iy)/V_0(iy)|
  =\frac{2c}{y}\sum_{n\ge1}\frac{n^{-4}}{1+e^{2(t-n)}}
          +O_c(y^{-3}).
\]
The sum differs from \(\sum_{n>t}n^{-4}\) by \(O(t^{-4})\):
the n <= t/2 part is \(O(e^{-t})\), and on n > t/2 the discrepancy
from the step function is bounded by \(O(t^{-4})\) times uniformly
bounded geometric sums in |n-t|. Integral comparison gives
\(\sum_{n>t}n^{-4}=1/(3t^3)+O(t^{-4})\), proving GH20.
This is not a model of Xi's zero divisor or its source admissibility.

## 6. Consequences and exact source boundaries

HC1 requires a PURE denominator with finite *global unweighted* height.
By GH3 this premise fails for the unreduced Theta_5 component even if RH
holds. HC itself is not contradicted. For the source-reduced denominator
B_5 the premise remains unresolved because the common-inner divisor is
unpaid. Likewise no finite polynomial height bound or geographic count
has been refuted: UC2 is an \(O(R\log R)\) disk count and UC10--UC12
concern selected finite shallow geographic packets.

Each physical lambda_j is frozen before y tends to infinity. GH3 therefore
applies componentwise for each positive lambda_j; it is not a uniform
interchange of the cofinal y-limit with T or lambda_j tending to zero.
This packet neither repairs historical raw-value jets nor substitutes them
for the adjoint physical coefficients required by the pinned IW source.
It does not prove actual reduced-denominator infinite height, infinite
finite-band trace, failure of native cofinal capture, a total-charge bound,
a zero-density percentage, or RH. No novelty claim is made for Hadamard
factorization, meromorphic-inner factorization, or GH16.

The primitive manifest pins seven sources: XL normalization and kernel;
UC actual companion count; HC finite-height hypothesis; IW adjoint interface;
the explicit frozen-lambda L-106620; the native T-106620 quotient and
reduction ledger; and historical L-106621, used only as finite-window
context, not imported as a global height theorem. In particular the
L-106620 gauge lemma and T-106620 frontier theorem are different files.

External imports are the classical Hadamard factorization theorem and
standard normal-family/Rolle/Hurwitz facts, together with the following
explicit primary/reference contracts. The xi formula and reflection are
[DLMF 25.4.3--4](https://dlmf.nist.gov/25.4); the differentiated gamma
estimates use [DLMF 5.11.2](https://dlmf.nist.gov/5.11.E2) and
[5.15.9](https://dlmf.nist.gov/5.15.E9).
The meromorphic-inner factorization and the unique possible singular mass
at infinity are stated in A. Poltoratski, "Toeplitz Order", Section 2.1,
printed page 4, [author's paper](https://people.math.wisc.edu/~poltoratski/ToeplitzOrder.pdf).
These are manually inspected mathematical imports; remote bytes are not
authenticated by the checker. The source-specific conclusions GH3--GH5
and the explicit cancellation discussion are proved above.

## 7. Bounded exact replay

The producer audits phases for orders 0 through 6, finite real-root Cayley
identities and multiple-root removability, Bell polynomials through order 6
and every monomial in GH14, finite Blaschke modulus/height identities,
domination algebra, and multiplicity-aware cancellation examples.
It does not evaluate Xi, gamma, logarithms, exponentials, or infinite sums;
in particular neither RH nor any analytic limit is inferred from its panel.
Rational finite-prefix controls for GH20 audit only height bookkeeping,
not the e^n placement or its proved asymptotic.

Inputs have strict rational/integer types (booleans are not numbers here),
explicit degree, multiplicity, bit and byte caps, and duplicate-node
rejection. Source bytes are authenticated against literal Git blob and
LF-normalized SHA-256 identities; changing a manifest and resealing a
derived payload does not bypass primitive replay. The fixture binds the
current note, producer, tests and source manifest. Its taxonomy and exact
no-rounding contract are enforced in tests under normal Python and -O.

Replay completed: 35 unit tests passed in normal Python and under -O;
both producer checks and byte-identical report/manifest emissions passed;
Ruff lint and format checks passed. The test implementation independently
reconstructs Bell polynomials by the partition-factorial formula and checks
the Cayley quotient by direct polynomial evaluation. A separate bounded
read-only mathematical check rederived GH16, GH19 and GH20 before freezing.
That check is not an independent exact-SHA review of the full packet.

    python -B -m unittest discover -s tests -p test_xi_companion_global_height_boundary.py
    python -B -O -m unittest discover -s tests -p test_xi_companion_global_height_boundary.py
    python -B research/exploratory/xi_companion_global_height_boundary.py --check
    python -B -O research/exploratory/xi_companion_global_height_boundary.py --check

Smallest result-invalidating burden: the imaginary-axis asymptotic for each
actual companion, its pure-inner factorization under the explicit premise,
or the extended height identity GH16. All three have written proofs here.
Smallest remaining native burden: control the common-inner divisor G well
enough to determine the two reduced height sums, or bypass that premise with
a source-matched cofinal-tail theorem. This packet does not close that gate.
