# Uniform reciprocal bounds and signed removal of the principal factor

Date: 20 October 2026. Status: proposed analytic consequences of an
explicit zero-free premise. Neither proposition below supplies that
premise or improves a zero-free boundary for a target L-function.

The finite-order argument is inherited from
[the previous packet](../../2026-10-20-liu-all-field-artin-and-barrier/uniform_mobius_consequence.md).
The two additions are uniformity in the archimedean conductor, and a
signed dilation estimate for the actual factor-removal operator. No
novelty is claimed for the classical complex-analysis implication.

## 1. The family premise and the analytic conductor

Fix a number field \(F\), of degree \(n\), and a family \(\mathcal X\)
of primitive unitary Hecke characters. Suppose that a single
\(\beta\in[1/2,1)\) satisfies

\[
 L_F(s,\chi)\ne0\quad(\Re s>\beta,\ \chi\in\mathcal X),
 \tag{1}
\]

allowing the translated simple pole when \(\chi=N^{i\tau}\).
This is a hypothesis about every member of the family, with a common
boundary. There is no hypothesis that the proof of (1) has uniform
constants. With \(L(s,N^{i\tau})=\zeta_F(s-i\tau)\), that pole is at
\(1+i\tau\). Changing the convention for a norm twist changes both
occurrences of \(\tau\), not the argument below.

Write the archimedean factors in the unitary convention as
\(\Gamma_{\mathbb R}(s+\epsilon_v+i t_v)\) at real places, and
\(\Gamma_{\mathbb C}(s+|m_v|/2+i t_v)\) at complex places. Define

\[
 \mathcal C(\chi,t)=
 |D_F|N\mathfrak f_\chi
 \prod_{v\ {\rm real}}(3+|t+t_v|)
 \prod_{v\ {\rm complex}}(3+|m_v|+|t+t_v|)^2.
 \tag{2}
\]

The factor 3 makes this a conductor bounded away from zero. Equivalent
conductor conventions change only fixed constants. For a pure norm twist
as above, all local shifts have \(t_v=-\tau\).

**Proposition 1.** For every \(\delta,\epsilon>0\), and integer \(j\ge0\),

\[
 \left|\frac{d^j}{ds^j}\frac1{L_F(s,\chi)}\right|
 \ll_{F,\delta,\epsilon,j}\mathcal C(\chi,\Im s)^\epsilon
 \qquad(\Re s\ge\beta+\delta,\ \chi\in\mathcal X).
 \tag{3}
\]

The reciprocal at a translated principal pole means its holomorphic
continuation. Also, for \(X\ge2\),

\[
 \left|\sum_{N\mathfrak a\le X}
       \mu_F(\mathfrak a)\chi(\mathfrak a)\right|
 \ll_{F,\epsilon}\mathcal C(\chi,0)^\epsilon X^{\beta+\epsilon}.
 \tag{4}
\]

All constants are uniform in the finite conductor, angular degrees, and
radial parameters of actual global characters in \(\mathcal X\).

### Proof

We record why the usual growth input is uniform. On \(\Re s=1+\eta\),
the Euler product bounds \(L_F(s,\chi)\) uniformly by \(\zeta_F(1+\eta)\).
Apply the Hecke functional equation on \(\Re s=-\eta\). Stirling's
formula, uniformly in nonnegative angular shifts, bounds the quotient
of each pair of gamma factors by a fixed power of
\(3+|m_v|+|t+t_v|\). The exponential factors cancel. The finitely many
bounded gamma arguments can be absorbed into the constant, using the
entire reciprocal gamma function at its zeros. The conductor in the
functional equation contributes a fixed power of \(N\mathfrak f_\chi\).
Phragmen--Lindelof therefore gives a bound

\[
 |F_\chi(\sigma+it)|\ll_{F,I}\mathcal C(\chi,t)^{A_{F,I}}
 \tag{5}
\]

on each fixed bounded real strip \(I\Subset(-1,\infty)\), for the
pole-removed function below. This excludes its artificial pole at
\(-1+i\tau\); only positive strips are used in the logarithm argument.

\[
 F_\chi(s)=
 \begin{cases}
 \dfrac{s-1-i\tau}{s+1-i\tau}L_F(s,\chi),
       &\chi=N^{i\tau},\\
 L_F(s,\chi),&\text{otherwise}.
 \end{cases}
 \tag{6}
\]

Only a polynomial bound is needed. The standard finite-order growth
used in Phragmen--Lindelof follows from the completed Hecke function;
the gamma quotient just checked keeps its constants uniform. This
argument uses the classical Hecke functional equation, not a uniform
version of the proposed zero detector.

By (1), \(F_\chi\) is holomorphic and nowhere zero in \(\Re s>\beta\),
including its removed pole. Choose a holomorphic logarithm \(h_\chi\)
by its Euler-product value on \(\Re s>1\), adding the logarithm of the
rational factor in (6) when necessary. On \(\Re s\ge3/2\),
\(|h_\chi(s)|\ll_F1\) uniformly in \(\chi\) and \(t\).

It suffices to prove (3) for \(0<\delta<1-\beta\). Center disks at
\(2+it\) and use radii

\[
 r_0=\tfrac12,\quad r=2-\beta-\delta,\quad
 R=2-\beta-\tfrac{\delta}{2},\quad
 R_+=2-\beta-\tfrac{\delta}{4}.
\]

The conductor (2) is comparable at points in these disks, uniformly
in all the parameters. Equation (5) bounds
\(\Re h_\chi=\log|F_\chi|\) by \(O_{F,\delta}(\log\mathcal C)\) on the
largest disk. Borel--Caratheodory on the next disk, followed by
Hadamard's three-circles theorem using the Euler bound on the
smallest, gives

\[
 |h_\chi(\beta+\delta+it)|
 \ll_{F,\delta}(\log\mathcal C(\chi,t))^\theta,\qquad
 \theta=\frac{\log(r/r_0)}{\log(R/r_0)}<1.
 \tag{7}
\]

The same disk controls all real parts between \(\beta+\delta\) and 2;
the Euler product controls the rest. Exponentiating (7) gives
\(|1/F_\chi|\ll\mathcal C^\epsilon\). The rational factor in (6)
has modulus at most one when \(\Re s>0\), so the same holds for \(1/L\).
Cauchy's integral formula on a disk of radius less than \(\delta/2\)
proves all derivative statements, first using the reciprocal bound
with gap \(\delta/2\).

For (4), write \(L(s,\chi)^{-1}=\sum_m a_\chi(m)m^{-s}\) on
\(\Re s>1\). The uniform bound \(|a_\chi(m)|\le d_n(m)\) follows by
counting ideals at each rational prime. Truncated Perron at
\(x=\lfloor X\rfloor+1/2\), \(c=1+1/\log x\), \(T=x^2\), has error
\(O_{F,\eta}(x^\eta)\), using \(|x-m|\ge1/2\).
Move to \(\sigma=\beta+\epsilon/2\). The reciprocal has no poles.
Since

\[
 \mathcal C(\chi,t)\ll_F\mathcal C(\chi,0)(1+|t|)^n,
\]

use (3) with exponent \(\epsilon/(8n)\). The vertical integral is
\(\ll\mathcal C(\chi,0)^{\epsilon/(8n)}
x^{\beta+3\epsilon/4}\), and the horizontal integrals are smaller.
Taking \(\eta\) small and absorbing logarithms proves (4). \(\square\)

The same statements hold after deleting a fixed or growing set \(S\)
of Euler factors, with a factor \((N\prod_{\mathfrak p\in S}
\mathfrak p)^\epsilon\). Indeed for \(\sigma\ge\beta+\delta>0\),
\(\prod_{\mathfrak p\in S}(1-(N\mathfrak p)^{-\sigma})^{-1}\)
is at most that factor times a constant depending on the fixed gap
and \(\epsilon\). Characters in (4) can equivalently be extended by
zero at the additional primes.

## 2. What this does and does not add to the angular packet

If the family theorem proposed in
[the angular packet](../../2026-10-20-angular-hecke-continuation/README.md)
is correct, its *common* boundary automatically implies (3)--(4) for
its stated nonresonant family, including growing archimedean conductor.
No bound on that proof's character-dependent threshold is needed.
For finite-order characters, the imported Liu premise gives the same
consequence without invoking that proposed angular extension.

This does not make an estimate for a growing family of metaplectic
test vectors uniform. Constants in a separate Gauss-sum transform,
Sobolev norm, or inverse moment still require their own accounting.
Only the Hecke reciprocal and its signed ideal coefficients are
uniformized here.

## 3. The signed dilation operator

The principal-factor identity inherited from the previous packet is

\[
 H_\eta(s)=L_F^S(6s-3,\nu)K_\eta(s),
 \qquad \nu=(\overline\Lambda\eta)^6,
 \tag{8}
\]

where \(K_\eta\) is a holomorphic unit for \(\Re s>1/2\). Let \(c\)
be fixed and define its actual inverse operator by

\[
 (\mathcal T_\nu f)(Z)=
 \sum_{\mathfrak a}\mu_F(\mathfrak a)\nu(\mathfrak a)
 (N\mathfrak a)^{3-6c}
 f\left(\frac{Z}{(N\mathfrak a)^6}\right).
 \tag{9}
\]

All sums omit \(S\). The rapid small-argument hypothesis below makes
(9) convergent, even before using cancellation.

**Proposition 2.** Suppose the signed partial sums obey

\[
 A_\nu(T):=\sum_{N\mathfrak a\le T}
           \mu_F(\mathfrak a)\nu(\mathfrak a)
 \ll C_\nu^\epsilon T^{\beta+\epsilon}
 \tag{10}
\]

for every \(\epsilon>0\). Suppose \(f\) is continuously differentiable
on \((0,\infty)\), and, with \(D=y\,d/dy\),

\[
 |f(y)|+|Df(y)|\le M y^{b-c}\quad(y\ge1),
 \tag{11}
\]

while for every \(L>0\),
\(|f(y)|+|Df(y)|\le M_Ly^L\) for \(0<y\le1\).
Then, for \(Z\ge2\),

\[
 \boxed{|(\mathcal T_\nu f)(Z)|
 \ll_{\epsilon,\beta,b,c}C_\nu^\epsilon
 (M+M_L)\,
 Z^{\max\{b,(3+\beta)/6\}-c+\epsilon}.}
 \tag{12}
\]

One sufficiently large fixed \(L\), depending on the displayed
parameters, suffices. If \(b>(3+\beta)/6\), the exponent \(b-c\)
is preserved with no \(Z^\epsilon\) loss, after using (10) with a
small exponent depending on this strict gap; the conductor loss can
still be any prescribed positive power.

### Proof

Apply partial summation to
\(g_Z(t)=t^{3-6c}f(Z/t^6)\). Its derivative is exactly

\[
 g'_Z(t)=t^{2-6c}\{(3-6c)f(Z/t^6)-6Df(Z/t^6)\}.
 \tag{13}
\]

There is no boundary term at infinity, by the small-argument
condition. With \(A_\nu(t)=0\) for \(t<1\), Stieltjes integration gives
\(\mathcal T_\nu f(Z)=-\int_1^\infty A_\nu(t)g'_Z(t)\,dt\),
including the atom at norm one.

For \(1\le t\le Z^{1/6}\), use (10)--(11) to bound the integrand by

\[
 \ll C_\nu^\epsilon M Z^{b-c}
       t^{\beta+2-6b+\epsilon}.
 \tag{14}
\]

Its integral is bounded by
\(Z^{\max\{b,(3+\beta)/6\}-c+O(\epsilon)}\);
at equality one may use a logarithm or absorb it into the displayed
\(\epsilon\). For \(t\ge Z^{1/6}\), the small-argument bound gives

\[
 \ll C_\nu^\epsilon M_L Z^L
 \int_{Z^{1/6}}^\infty t^{\beta+2-6c-6L+\epsilon}\,dt
 \ll C_\nu^\epsilon M_L Z^{(3+\beta)/6-c+\epsilon/6},
 \tag{15}
\]

once \(L\) is large enough. Renaming the small exponent proves (12).
If \(b>(3+\beta)/6\), choose the exponent in (10) less than
\(6b-3-\beta\), so (14) is integrable to infinity uniformly in \(Z\);
(15) is then strictly smaller. \(\square\)

## 4. The precise improvement and remaining gap

Using only absolute values of the Mobius coefficients amounts to
\(\beta=1\), with the threshold \(2/3\). Using (4) for the *actual*
character \(\nu\) changes that threshold to

\[
 c_\beta=\frac{3+\beta}{6}.
 \tag{16}
\]

At the candidate angular boundary \(B_\flat\), this is
\(0.645814441173327\ldots\). Thus signed removal preserves any
strict decay exponent \(b>c_\beta\); it is no longer necessary to
assume \(b>2/3\). The gain is a statement about this operator and its
principal factor, not a zero-free region for the target.

For a Mellin profile
\(f(Z)=\int Z^{s-c}G(s)L_F^S(6s-3,\nu)\,ds\) on an initial line
where both sums converge absolutely, (9) gives exactly
\(\mathcal T_\nu f(Z)=\int Z^{s-c}G(s)\,ds\).
Proposition 2 controls the same signed operation after continuation
when (10)--(11) have been established independently. It does not
establish (11), does not assume the desired target zero-free region
to prove itself, and does not replace a row-dependent divisor mark
by an independent coefficient.

The complete mixed moment and the detector's critical class count
still require additional estimates. In particular, neither (3) nor
(12) changes the currently imported \(B_\flat\) for finite-order
Hecke L-functions or proves the Riemann hypothesis.
