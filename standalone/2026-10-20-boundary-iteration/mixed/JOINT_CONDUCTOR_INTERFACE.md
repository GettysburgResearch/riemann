# The joint conductor mean and the coherent terminal gap

20 October 2026. Status: exact interface and obstruction audit; no new
joint mean is asserted. The fixed-conductor theorem is in
[QUADRATIC_PAIR_ABSORPTION.md](QUADRATIC_PAIR_ABSORPTION.md).

## 1. The exact reflected orientation

Write the good sextic character as \(\chi_6\), so that
\(\chi_3=\chi_6^2\) and the quadratic character is \(\xi=\chi_6^3\).
The closed pair in (Q1) has characters

\[
 \xi_S\chi_{3,S}^{,j}\overline{\chi_{3,r}},\qquad j=0,2.
\]

Thus its two sextic exponent patterns are \((4,3)\) and
\((4,1)\) at \((r,S)\), respectively. In particular the second
member has **positive** sextic orientation at \(S\).
It is not the digit-five family. Both series retain the quadratic
cube factor and all zeros at \(rS\).

For the squarefree core of this second member, put

\[
 \mathcal J(R,H,D)=\sum_{r\asymp R}^{*}\sum_{S\asymp H}^{*}
 \left|\sum_n\frac{C_\ell(n)\nu(n)}{\sqrt{Nn}}
       \chi_n(S)\chi_n(r)^4 W(Nn/D)\right|^2.             \tag{J1}
\]

The positive summands may be restricted by \((r,S)=1\), and a fixed
puncture is retained throughout. The fixed finite sector decomposition
does not depend on the growing lengths.

The variables in (J1) are exactly the positive fourth-label family of
[rStation paper 5, Theorem 5](https://rstation.ai/problems/riemann_hypothesis/papers/5):
\(f=r,z=S,F=R,K=H\). With trivial puncture its bounds imply

\[
 \mathcal J(R,H,D)\ll(RHD)^\epsilon
          \min\{RH+DR^2,\ RH+HR^2\}.                    \tag{J2}
\]

The extra factor \(R\) here reverses that theorem's normalized
\(1/F\) label average; it must not be omitted. Its completed
long-column estimate, before cube inversion, is

\[
 \mathcal J_{\mathrm{comp}}(R,H,D)
       \ll(RHD)^\epsilon\left(RH+\frac{H^2R^2}{D}\right).
                                                               \tag{J3}
\]

At the conductor-balanced length \(D=R^{1/2}H\), the second term
in (J3) is \(HR^{3/2}\). A direct route to a natural-count mean
would reduce the label dependence in (J3) from \(R^2\) to
\(R^{3/2}\). The existing proof freezes the label before its
reflected estimate, so this saving is not already available from it.

## 2. Why an arbitrary-coefficient replacement is false

Consider the proposed operator-norm bound

\[
 RH+D+(RD)^{2/3}.                                      \tag{J4}
\]

It cannot hold for the closed pair with arbitrary normalized column
coefficients. Set \(R=1\) in the positive sextic member. This gives
an ordinary sextic large sieve bounded by \(O(H)\) when
\(D=H^{3/5}\). The sextic lower bound of
[Xu--Sang, arXiv:2610.17675v1](https://arxiv.org/html/2610.17675v1)
in its stated interior range is

\[
 H^{5/6}D^{1/3}=H^{31/30},                              \tag{J5}
\]

which is strictly larger. The range condition is satisfied because
\(H=D^{5/3}\), with \(16/11<5/3<2\). Multiplication of arbitrary
coefficients by a fixed unit-modulus angular or Gauss phase cannot
remove this counterexample. Therefore a useful joint theorem must
retain the prescribed coefficients, or another genuinely restricted
coefficient class.

The cubic conductor-order argument of
[de Faveri, arXiv:2610.04045v1, Proposition 8.1](https://arxiv.org/html/2610.04045v1)
does not immediately transfer. Its two cubic row orientations are
conjugates. After Poisson they merge as a product of two row variables.
For (J1), sextic Poisson instead gives a new frequency containing
\(r^2\). This square is the same fourth-label inflation visible in
the exact frequency \(h r^2g^2/d\); replacing it by \(r\) is not
an algebraically valid conductor ordering.

## 3. A natural-count mean is still not a strict terminal saving

Suppose, optimistically, that the full completed joint mean satisfied

\[
 \sum_{r\le R}^{*}\sum_{S\asymp H}^{*}
   \|\mathbf Q_{r,S}(1/2+\delta+it)\|^2
   \ll(RH)^\epsilon RH(1+|t|)^C.                      \tag{J6}
\]

The exact reflection (Q9), summed also over \(S\), would give on the
opposite line

\[
 \sum_{r,S}\|\mathbf Q_{r,S}(1/2-\delta+it)\|^2
     \ll(RH)^\epsilon R^{1+2\delta}H^{1+4\delta}
       (1+|t|)^C.                                    \tag{J7}
\]

At the physical terminal, the Type-I variables are \(A=U,B=L\),
the cubic row is the prime label \(r=P\), and the quadratic
conductor has norm \(K\). The coefficient \(b_P(S)\) may depend
on the quadratic row. Cauchy in the \(P\) sum and the original
\(1/\sqrt{UL}\) normalization turn (J7) into

\[
 U^{-2\delta}L^{1+2\delta}K^{1+4\delta}.                \tag{J8}
\]

At the binding scale \(U=KL\), this is \(KL K^{2\delta}\).
At \(\delta=0\), (J6) only recovers \(KL\). Therefore even a
natural-count completed mean, by itself and used with this Cauchy
step, does not give a strict saving on that face. A boundary-improving
argument must preserve more of the coherent label sum, or establish
a stronger feature for its particular smoothed block. This calculation
does not preclude such an argument; it states the exact strength needed
beyond (J6).

No improvement of the current numerical zero-free boundary is claimed
from (J1)--(J8).
