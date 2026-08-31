# Growing endpoint inertia of the exact completed period matrix

Status: PROPOSED ANALYTIC THEOREM; independent frozen-source review required.
Scope: actual level-one Petersson period, real endpoint parameter; no
simplicity, monotone eigenvalue motion, or scalar-quotient cancellation claim.
This is a new direct-symbol argument, not a uniform use of a fixed-weight
Laurent expansion. RH and GRH are not addressed.

## 1. Exact source and theorem

Use the space, metric, Eisenstein normalization, and Poincare block from
[the cusp operator packet](CUSP_KRONECKER_SPECTRAL_LAW.md). For real
\(0<\varepsilon\le1/4\), let \(\mathcal M_k(\varepsilon)\) be the
Petersson form operator of \(I_{1-\varepsilon}\). Define

\[
 C=\Lambda(2-2\varepsilon)>0,\quad
 D=-\Lambda(1-2\varepsilon)>0,\quad \beta=1-2\varepsilon,
 \quad Y=(D/C)^{1/\beta}.
 \tag{P1}
\]

Positivity of \(D\) follows from \(\zeta(u)<0\) for \(0<u<1\), for example
from the alternating eta series. The exact Eisenstein expansion gives

\[
 E^*(z,1-\varepsilon)=h_\varepsilon(y)+R_{1-\varepsilon}(z),
 \quad h_\varepsilon(y)=Cy^{1-\varepsilon}-Dy^\varepsilon
 =Dy^\varepsilon[(y/Y)^\beta-1],
 \quad |R_{1-\varepsilon}|\le R_0.
 \tag{P2}
\]

The same \(R_0=2e^{-2\pi a_0}/(1-e^{-2\pi a_0})^2\) works for every
\(0<\varepsilon\le1/4\). This is the complete Fourier-tail bound LS8--LS9
in the accepted parent, not a truncation of the period matrix.

**Theorem P.** For EVERY sequence of even weights \(k\to\infty\) and real
parameters \(\varepsilon_k\downarrow0\) such that \(k\varepsilon_k\to\infty\),

\[
 \boxed{n_+(\mathcal M_k(\varepsilon_k))
                 \sim\frac{k\varepsilon_k}{12}.} \tag{P3}
\]

Here \(n_+\) counts strictly positive eigenvalues with multiplicity. It is
not itself a zero count. Section 5 states a separately justified determinant
zero consequence, with its multiplicity limitation explicit.

## 2. Finite upper certificate: a negative coefficient flag

Put \(\nu=k-1\). Suppose a positive integer \(J\) satisfies

\[
 C+R_0<Da_0^\varepsilon,\qquad
 C\left(1+\frac{\nu+\varepsilon}{4\pi J}\right)^\beta+R_0<D.
 \tag{P4}
\]

Then the period is strictly negative on
\(W_J=\{a_1=\cdots=a_{J-1}=0\}\), so

\[
 n_+(\mathcal M_k(\varepsilon))+n_0(\mathcal M_k(\varepsilon))
 \le J-1. \tag{P5}
\]

**Proof.** Below height one, (P2) is at most
\(C-Da_0^\varepsilon+R_0<0\). Above height one, Parseval diagonalizes the
constant term for all \(n\ge J\). Relative to the positive density
\(y^{\nu-1+\varepsilon}e^{-4\pi ny}dy\) on \([1,\infty)\), the ratio of the
positive and negative constant-term integrals is \(\mathbb E[y^\beta]\).
Concavity and the truncated-Gamma integration-by-parts estimate give

\[
 \mathbb E[y^\beta]\le(\mathbb E[y])^\beta
 \le\left(1+\frac{\nu+\varepsilon}{4\pi n}\right)^\beta.
 \tag{P6}
\]

The boundary estimate remains valid for the real shape \(\nu+\varepsilon>1\).
The nonconstant remainder contributes at most \(R_0\) times the original
norm, which is at most its \(y^\varepsilon\)-weighted norm on this cusp.
Thus (P4) makes the full cusp contribution negative. No sign of an omitted
Fourier coefficient is assumed. The full form is negative on \(W_J\);
its codimension is at most \(J-1\), proving (P5).

## 3. Finite lower certificate: high-cusp mass of a Poincare block

Assume \(Y\ge1\), choose \(H>Y\), and define

\[
 m=CH^{1-\varepsilon}-DH^\varepsilon-R_0,
 \qquad M=DY^\varepsilon+R_0,
\]
\[
 \alpha=(1-\delta_{k,J})Q(k-1,4\pi JH). \tag{P7}
\]

If

\[
 \delta_{k,J}<1,\quad m>0,\quad m\alpha>M(1-\alpha), \tag{P8}
\]

then \(n_+(\mathcal M_k(\varepsilon))\ge J\).

**Proof.** For \(y\ge Y\),

\[
 h_\varepsilon'(y)
 =Dy^{\varepsilon-1}[(1-\varepsilon)(y/Y)^\beta-\varepsilon]>0.
\]

Hence (P2) is at least \(m\) on \(y\ge H\). On the entire fundamental
domain it is at least \(-M\): if \(y\le Y\), discard the positive term and
use \(y^\varepsilon\le Y^\varepsilon\); above \(Y\), the constant term is
nonnegative. This global lower bound is independent of how large \(k\) is.

For any nonzero \(f=\sum_{n=1}^Jc_nv_n\), Parseval above \(H\), followed by
the full Gram bound (K10), gives the actual mass estimate

\[
 \mathbb P_f(y\ge H)
 \ge Q(k-1,4\pi JH)\frac{\|Kc\|^2}{c^*Kc}\ge\alpha. \tag{P9}
\]

The probability here is in the complete Petersson measure, including the
compact part of the domain. Thus the period Rayleigh quotient is at least
\(m\alpha-M(1-\alpha)>0\). The Poincare span has dimension \(J\), so min--max
proves the lower certificate. In particular the potentially negative
contribution outside the cusp has been paid, not dropped.

## 4. Proof of the growing-parameter theorem

The scalar Laurent expansions at one give

\[
 C\longrightarrow\pi/6,\quad D\sim1/(2\varepsilon),\quad
 Y\sim\frac3{\pi\varepsilon},\quad Y^\varepsilon\longrightarrow1.
 \tag{P10}
\]

For the last two assertions,
\(\log Y=(1-2\varepsilon)^{-1}\log(D/C)\) and
\(\varepsilon\log(1/\varepsilon)\to0\). These are scalar estimates; they
are not multiplied by an uncontrolled \(k\)-dependent operator norm.

Fix \(0<\eta<1\). Choose

\[
 J_+=\left\lceil(1+\eta)k\varepsilon/12\right\rceil,
 \qquad
 J_-=\left\lfloor(1-\eta)k\varepsilon/12\right\rfloor.
\]

Both tend to infinity and are \(o(k)\). For \(J_+\), the first condition in
(P4) holds because \(D\to\infty\); for the second,

\[
 \frac C D\left(1+\frac{\nu+\varepsilon}{4\pi J_+}\right)^\beta
 =\left(\frac{1+(\nu+\varepsilon)/(4\pi J_+)}Y\right)^\beta
 \longrightarrow\frac1{1+\eta}<1,
\]

while \(R_0/D\to0\). Thus (P5) supplies the required upper bound.

For \(J_-\), take \(H=(1+\eta/2)Y\). Then

\[
 \frac{4\pi J_-H}{k-1}\longrightarrow
 (1-\eta)(1+\eta/2)<1.
\]

The Gamma lower-tail Chernoff bound implies
\(Q(k-1,4\pi J_-H)\to1\). Explicitly, for a fixed \(0<r<1\), a Gamma
variable of shape \(\nu\) has
\(\mathbb P(Z\le r\nu)\le[r e^{1-r}]^\nu\), by optimizing the negative
exponential Markov bound. Also \(\delta_{k,J_-}\to0\) by (K13).
Consequently \(\alpha\to1\). Finally

\[
 \frac mM\longrightarrow\eta/2>0,
\]

by substituting \(H/Y=1+\eta/2\) into (P7) and using (P10).
Therefore (P8) holds eventually. The two finite certificates sandwich the
positive inertia between \(J_-\) and \(J_+-1\). Letting \(\eta\downarrow0\)
proves (P3).

This proof allows, for example, \(\varepsilon=1/\log k\), as well as power
scales. It does not require \(k\varepsilon^2\log k=o(1)\), which is the
restriction introduced by a crude global Laurent-remainder estimate.

## 5. A determinant zero consequence, with multiplicity retained

For each fixed \(k\), the matrix is analytic for real
\(0<\varepsilon<1/4\), and its pole at zero is
\(-I/(2\varepsilon)\). Hence it is negative definite sufficiently near
zero. The pole-cleared determinant is analytic and nonzero at zero, so its
zeros in a compact endpoint interval are isolated and finite.

Along a real analytic Hermitian matrix path, the increase of positive
inertia at an isolated singular point is at most its nullity. The determinant
vanishes there to order at least that nullity: use constant invertible row
and column changes to put the value at that point in a rank-normal form and
expand the determinant. Summing these inequalities gives

\[
 \sum_{0<\varepsilon<\varepsilon_k}
    \operatorname{ord}_{\varepsilon}\det\mathcal M_k(\varepsilon)
 \ge n_+(\mathcal M_k(\varepsilon_k)). \tag{P11}
\]

Positive eigenvalues at the endpoint must have crossed earlier, so an
endpoint nullity does not invalidate this open-interval bound. In particular
(P3) implies at least \((1-o(1))k\varepsilon_k/12\) real determinant zeros
COUNTING MULTIPLICITY in \(1-\varepsilon_k<s<1\). Reflection supplies the
corresponding left-endpoint conclusion.

Neither (P11) nor the inertia theorem says these zeros are simple or gives
their distinct count asymptotically. They do not identify which survive a
particular determinant quotient. Differences of independently certified
inertias at two parameters can certify crossings in disjoint intervals;
the complete crossing direction and microscopic cluster splitting remain
separate questions.

## 6. Review boundary

Load-bearing inputs are the exact Eisenstein Fourier expansion and uniform
remainder, the full Petersson Poincare Gram estimate, Parseval on the complete
cusp rectangle, and elementary Gamma inequalities. The proof retains the
compact-domain mass and the negative part outside the selected cusp.
Finite ball certificates of (P4),(P8) instantiate these analytic bounds;
they are not direct numerical evaluations of every entry of the period.

The first falsifiers to check are: the exponent \(\nu-1+\varepsilon\) in
(P6); the shape \(k-1\), not \(k\), in (P7),(P9); the full block factor
\(1-\delta\); and the distinction between inertia and divisor multiplicity.
