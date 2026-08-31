# The fixed-prime native current at infinite product horizon

Status: proof-only continuation; no new numerical experiment is asserted.
The source is the actual L-102707 half-source, the factor two is retained,
and the observation measure is the original L-102880 measure. The principal
panel is \(P=\{2,3,5\}\). Statements with \(r=|P|\) apply to any specified
finite set of distinct primes. They do not take a limit over primes.

The new conclusion is an actual completion of the product-horizon fields:
the full current exists uniformly over all monotone paths and all real
observation parameters, with an explicit \(H^{-1/2}\) error. The original
Hilbert energies and their global minimum values converge uniformly.
This does not identify a finite-horizon optimizer with an infinite-horizon
optimizer.

## 1. Source, path category, and unchanged observation

For \(x=(x_p)_{p\in P}\in[0,1]^r\), put
\[
 \ell_x(z)=(1-x)\sqrt{1-z^2}+x\sqrt{1-z},
 \qquad
 \Lambda_x(\mathbf z)=\prod_{p\in P}\ell_{x_p}(z_p)
       =\sum_{n\in\mathcal N_P}a_n(x)\mathbf z^{v_P(n)}.       \tag{1.1}
\]
Here \(\mathcal N_P\) consists of the positive integers supported on \(P\),
including 1, and both square roots mean their power series with constant
term 1. Each \(a_n\) is an actual real polynomial, affine in each source
coordinate.

Let \(\mathcal P\) be the continuous coordinatewise nondecreasing paths
from \(\mathbf0\) to \(\mathbf1\), with pauses and monotone changes of
parameter identified. Coordinatewise vertical segments are permitted.
Integrals below are ordinary continuous-path Riemann--Stieltjes integrals.
Every such path has a Lipschitz representative parametrized by
\(\sum_p x_p\), so this introduces no jump convention.

The ordered arithmetic current and its finite physical observation are
\[
 B_{n,m}(\gamma)=2\int_\gamma a_m\,da_n,\qquad
 F_H(t;\gamma)=
 \sum_{\substack{n,m\in\mathcal N_P\\nm\le H}}
 \frac{B_{n,m}(\gamma)}{\sqrt{nm}}\,
       e^{it\log(n/m)},\qquad H\ge1.                           \tag{1.2}
\]
Thus the derivative is on the \(n\) factor. In particular the left unit
is zero and the right unit is retained. Equal ratios are combined only
after their actual \(1/\sqrt{nm}\) weights are applied.

For provenance, (1.1) is the source of
L-102707, and (1.2) is the convention in
GLOBAL_NATIVE_GEODESIC_VARIATION.md. The two source lemmas are available
at commit ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc:

| Source | Git blob |
| --- | --- |
| L-102707-continuous-half-divisor-geodesic-and-polarized-hankel-current.md | 6810bcece309b0c54ae6c8fc84b314990004549c |
| L-102880-logarithmic-derivative-outer-detector-has-zero-square-lattice-moment.md | d7330d114ebba1a7a16e22fa9ba6aa6b5eb7cdd6 |

Use exactly
\[
 \kappa(u)=K_L(e^u),\qquad
 d\nu(t)=\frac{|\widehat\kappa(t)|^2}{2\pi}\,dt,\qquad
 I_H(\gamma)=\|F_H(\,\cdot\,;\gamma)\|_{L^2(\nu)}^2.           \tag{1.3}
\]
No diagonal coefficient norm, atomic replacement measure, or new path
probability measure is used.

## 2. Exact local absolute sums, including the endpoint

Write \(b_j=[z^j]\sqrt{1-z}\). Then \(b_0=1\), \(b_j<0\) for \(j\ge1\),
and \(|b_j|\) strictly decreases. For example,
\[
 b_j=-\frac{\binom{2j}{j}}{4^j(2j-1)}\quad(j\ge1).
\]
The coefficient \(c_j(x)=[z^j]\ell_x(z)\) is nonpositive for every
\(j\ge1\). Consequently, for \(0\le q\le1\),
\[
 \begin{aligned}
 A_x(q)&=\sum_{j\ge0}|c_j(x)|q^j\\
 &=2-\big((1-x)\sqrt{1-q^2}+x\sqrt{1-q}\big)
 \le A(q):=2-\sqrt{1-q}.                                    \tag{2.1}
 \end{aligned}
\]
For the derivative coefficients
\[
 d_j=b_j-\mathbf1_{2\mid j}b_{j/2},\qquad d_0=0,
\]
the odd coefficients are negative and the positive even coefficients
are \(|b_{j/2}|-|b_j|\). Separating even and odd terms gives the exact sum
\[
 D(q):=\sum_{j\ge0}|d_j|q^j
       =\sqrt{1+q}-\sqrt{1-q^2}.                             \tag{2.2}
\]
These identities include \(q=1\), where
\[
                         A(1)=2,\qquad D(1)=\sqrt2.          \tag{2.3}
\]
For completeness, absolute convergence at this endpoint follows by
monotone convergence from
\(\sum_{j\ge1}|b_j|q^j=1-\sqrt{1-q}\) as \(q\uparrow1\).
It is not an estimate obtained by substituting into a divergent series.

For \(\sigma\ge0\), define explicit finite constants
\[
 \begin{aligned}
 q_p&=p^{-\sigma},&
 A_\sigma&=\prod_{p\in P}A(q_p),\\
 T_\sigma&=\sum_{p\in P}D(q_p)\prod_{q\in P\setminus\{p\}}A(q_q),&
 C_\sigma&=2A_\sigma T_\sigma
   =2\left(\prod_{p\in P}A(q_p)^2\right)
      \sum_{p\in P}\frac{D(q_p)}{A(q_p)}.                     \tag{2.4}
 \end{aligned}
\]
In particular
\[
                 C_0=r\sqrt2\,4^r;
 \qquad C_0=192\sqrt2\ \text{for }P=\{2,3,5\}.               \tag{2.5}
\]

**Uniform source estimate.** For every \(\gamma\in\mathcal P\),
\[
 \boxed{\displaystyle
 \sum_{n,m\in\mathcal N_P}|B_{n,m}(\gamma)|(nm)^{-\sigma}
       \le C_\sigma.}                                      \tag{2.6}
\]
Indeed, unique prime factorization and (2.1)--(2.2) give
\[
 \sum_n|a_n(x)|n^{-\sigma}\le A_\sigma,\qquad
 \sum_n|\partial_p a_n(x)|n^{-\sigma}
       \le D(q_p)\prod_{q\ne p}A(q_q).
\]
Each coordinate has total variation exactly 1. The ordinary polynomial
chain rule, integrated against the positive measures \(dx_p\), therefore
implies
\[
 \sum_n n^{-\sigma}\int_\gamma|da_n|\le T_\sigma.
\]
Tonelli and the actual factor two in (1.2) prove (2.6).
This also bounds the total absolute contribution before derivative sites
are summed, so cancellations between sites are not needed for the bound.

## 3. The product current and a uniform endpoint tail

Set
\[
 z_p(t)=p^{-1/2+it},\qquad
 S(t,x)=\prod_{p\in P}
 \big((1-x_p)\sqrt{1-z_p(t)^2}+x_p\sqrt{1-z_p(t)}\big).
                                                                    \tag{3.1}
\]
The roots are the same analytic power-series branches as in (1.1);
\(|z_p(t)|<1\) for every real \(t\). Then
\[
 \boxed{\displaystyle
 F_\infty(t;\gamma)=2\int_\gamma\overline{S(t,x)}\,dS(t,x)
   =\sum_{n,m\in\mathcal N_P}
       \frac{B_{n,m}(\gamma)}{\sqrt{nm}}e^{it\log(n/m)}.}      \tag{3.2}
\]
The double series is absolutely and uniformly convergent over all real
\(t\) and all \(\gamma\in\mathcal P\). In particular
\[
                |F_H(t;\gamma)|,\ |F_\infty(t;\gamma)|
                         \le C_{1/2}.                      \tag{3.3}
\]

To justify the integral identity, the coefficient maps in (1.1) and
their coordinate derivatives take values continuously in the weighted
\(\ell^1\) space, by (2.1)--(2.2). Their Stieltjes integrals may therefore
be expanded coefficientwise. The product of the two absolutely
convergent coefficient sums gives (3.2) by (2.6). Its phase is positive
\(it\log(n/m)\) because \(dS\) supplies the \(n\) factor and
\(\overline S\) supplies the \(m\) factor.

More generally, for \(0\le\eta\le1/2\),
\[
 \sup_{\gamma\in\mathcal P,\ t\in\mathbb R}
       |F_\infty(t;\gamma)-F_H(t;\gamma)|
       \le C_{1/2-\eta}H^{-\eta}.                            \tag{3.4}
\]
For \(nm>H\), factor
\((nm)^{-1/2}=(nm)^{-(1/2-\eta)}(nm)^{-\eta}\) and use (2.6).
The endpoint estimate is thus
\[
 \boxed{\displaystyle
 \sup_{\gamma,t}|F_\infty-F_H|
             \le r\sqrt2\,4^r H^{-1/2}.}                    \tag{3.5}
\]
No loss in the exponent is required. This is an upper bound, not a claim
that this rate or its constant is optimal.

## 4. The original measure is finite, with an exact mass

The original source kernel is
\[
 K_L(y)=
 \begin{cases}
 8-4\sqrt y,&1\le y<2,\\
 -8(1+\sqrt2)+4\sqrt2\sqrt y,&2\le y<4,\\
 8\sqrt2-2\sqrt y,&4\le y<8,\\
 0,&\text{otherwise}.
 \end{cases}                                                \tag{4.1}
\]
Thus \(\kappa\) is real, bounded, and compactly supported. Plancherel
gives the finite positive mass
\[
 \begin{aligned}
 \nu_0:=\nu(\mathbb R)
 &=\int_{\mathbb R}|\kappa(u)|^2\,du
   =\int_1^8K_L(y)^2\,\frac{dy}{y}\\
 &=\boxed{128(3+\sqrt2)\log2-288}>0.                          \tag{4.2}
 \end{aligned}
\]
This exact integral follows from the three pieces
\[
 \begin{array}{c|c}
 [1,2]&64\log2+144-128\sqrt2\\
 [2,4]&(192+128\sqrt2)\log2-192\\
 [4,8]&128\log2-240+128\sqrt2 .
 \end{array}
\]
Positivity also follows directly from the nonzero real kernel, without
numerical evaluation of the displayed expression.

Combining (3.3)--(3.5) with this unchanged measure proves
\[
 \boxed{\displaystyle
 \sup_\gamma\|F_\infty-F_H\|_{L^2(\nu)}
       \le\sqrt{\nu_0}\,C_0H^{-1/2},}                        \tag{4.3}
\]
and, writing \(I_\infty=\|F_\infty\|_{L^2(\nu)}^2\),
\[
 \boxed{\displaystyle
 \sup_\gamma|I_\infty(\gamma)-I_H(\gamma)|
       \le 2\nu_0 C_{1/2}C_0H^{-1/2}.}                     \tag{4.4}
\]
Here both fields in the difference-of-squares bound have norm at most
\(\sqrt{\nu_0}C_{1/2}\). Every equal-ratio alias and every cross term of
the original Gram form remains present.

## 5. The real part is fixed by the endpoints

The continuous BV chain rule gives
\[
 d|S|^2=2\operatorname{Re}(\overline S\,dS).
\]
Consequently
\[
 \boxed{\displaystyle
 \operatorname{Re}F_\infty(t;\gamma)
  =|S(t,\mathbf1)|^2-|S(t,\mathbf0)|^2
  =\prod_{p\in P}|1-z_p(t)|
     -\prod_{p\in P}|1-z_p(t)^2|.}                          \tag{5.1}
\]
Only the imaginary current can vary with the path. The coefficients are
real, so \(F_\infty(-t)=\overline{F_\infty(t)}\): the real part is even
and the imaginary part is odd. In particular, for the original even
measure,
\[
 I_\infty(\gamma)=
 \|\operatorname{Re}F_\infty\|_{L^2(\nu)}^2+
 \|\operatorname{Im}F_\infty(\,\cdot\,;\gamma)\|_{L^2(\nu)}^2. \tag{5.2}
\]
The first term is a common lower bound for all path energies. This
identity alone does not assert that the second term can be made zero.

For comparison, the finite fields also have path-independent real
parts: \(B_{n,m}+B_{m,n}=2[a_na_m]_{\mathbf0}^{\mathbf1}\), and the
condition \(nm\le H\) is symmetric under swapping \(n,m\).
Their uniform limit is exactly (5.1).

## 6. Actual minimum values converge, and minimizers have limit points

Use the total-coordinate parametrization
\[
 \mathcal P_*=\{x:[0,r]\longrightarrow[0,1]^r:
        x_p\text{ nondecreasing},\ \sum_p x_p(s)=s\}.         \tag{6.1}
\]
The endpoints follow from this definition. Every coordinate is
1-Lipschitz, so this is a compact set in the uniform topology by
Arzela--Ascoli. It represents exactly \(\mathcal P\): if the original
sum of coordinates is constant on an interval, then every coordinate
is constant there, and deleting those pauses makes the parametrization
well-defined.

Every finite coefficient \(B_{n,m}\) is continuous on \(\mathcal P_*\).
In fact, if \(x^{(j)}\to x\) uniformly, then
\(dx_p^{(j)}\) converges weakly to \(dx_p\), with uniformly bounded
mass 1, and the polynomial integrands
\(a_m(x^{(j)})\partial_pa_n(x^{(j)})\) converge uniformly.
Their Stieltjes integrals therefore converge. Finite \(F_H\) and \(I_H\)
are continuous. The uniform bounds (3.5) and (4.4) then prove the
continuity of \(F_\infty\) into \(C_b(\mathbb R)\) and of \(I_\infty\).

Both the finite and infinite original energies thus attain minima:
\[
 m_H=\min_{\gamma\in\mathcal P}I_H(\gamma),\qquad
 m_\infty=\min_{\gamma\in\mathcal P}I_\infty(\gamma).
\]
The same error applies to these actual optimization problems:
\[
 \boxed{\displaystyle
             |m_H-m_\infty|
             \le2\nu_0C_{1/2}C_0H^{-1/2}.}                 \tag{6.2}
\]
If \(H_j\to\infty\) and \(\gamma_j\) is a global minimizer at \(H_j\),
then every convergent subsequence in \(\mathcal P_*\) limits to a global
minimizer of \(I_\infty\). The same is true for additive
\(\epsilon_j\)-minimizers with \(\epsilon_j\to0\). Compactness supplies
at least one such subsequence.

No uniqueness or convergence rate for the minimizing paths follows
from (6.2). In particular the certified H25 path need not remain optimal
at a higher horizon.

## 7. Scope of this completion

The arithmetic exponents at the fixed primes are unbounded, and the
cutoff is the actual physical product \(nm\le H\). This is an infinite
source completion in the original finite observation measure, with an
ordinary product-current formula and a uniform pathwise error. It uses
neither Schatten regularization nor a change of scalar frame.

The endpoint local absolute sums, source current, and fixed-measure
estimates are the inputs specific to this source. Tonelli, Plancherel,
the continuous BV chain rule, and compactness of Lipschitz paths are
classical. No claim of a new abstract integration or compactness theorem
is made.

There is no limit over all primes, no identification with a full
post-renewal or amplified family, and no RH conclusion. Faithfulness
of the infinite observed source and eventual ranks of finite
observations are separate questions; they are not needed for the
existence, error bounds, or minimum-value convergence proved here.
