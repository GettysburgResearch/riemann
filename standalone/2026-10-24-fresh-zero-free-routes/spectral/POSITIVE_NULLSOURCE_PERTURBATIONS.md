# Exact positive nullsources do not identify the Riemann theta density

Status: proposed component theorems with proofs and exact polynomial checks.
Scope: the actual full Weil convolution operator and its theta annihilator.
No zero-free improvement is claimed.

Use the source, normalization, and operator of
`THETA_JUMP_FORM_AND_RESOLVENT_DELOCALIZATION.md`: \(\phi>0\),
\(\int\phi=1\), \(\widehat\phi=X=\Xi/\Xi(0)\), and
\(K_W*\phi=0\). The operator is unchanged. Every perturbation below
annihilates **all** of it, including every prime power and both pole terms.

The motivation was constructive: replace the delocalizing resolvent
selection by a positive nullsource with minimum variance, or by a
positive nullsource with finitely many prescribed moments. The following
explicit calculations show why those replacements do not select theta.
They concern auxiliary source functions, not zeros of the Riemann zeta
function itself.

## 1. Any fixed moment prefix admits a downward perturbation

**Theorem 1.** For every integer \(m\ge0\) and every \(c>0\), there is
\(\epsilon_0>0\) such that, for \(0<\epsilon<\epsilon_0\),

\[
 f_{\epsilon,m}=
 \phi+\epsilon\big(\phi^{(2m+4)}-c\phi^{(2m+2)}\big)             \tag{1}
\]

is a strictly positive, smooth, even probability density with
\(K_W*f_{\epsilon,m}=0\). Its moments through degree \(2m\) equal
those of \(\phi\), while

\[
 \int x^{2m+2}f_{\epsilon,m}(x)dx
 =\int x^{2m+2}\phi(x)dx-c\epsilon(2m+2)!.                      \tag{2}
\]

Its Fourier transform has nonreal zeros, irrespective of whether Xi
itself has any. Its leading tail rate is still
\(\log f_{\epsilon,m}(x)\sim-\pi e^{2|x|}\).

*Proof.* Direct differentiation of the \(n=1\) theta term gives, for
each fixed \(k\),

\[
 \phi^{(2k)}(x)/\phi(x)
  \sim (2\pi)^{2k}e^{4k|x|}\qquad(|x|\to\infty).                \tag{3}
\]

All \(n\ge2\) terms are exponentially smaller even after fixed
differentiation. Consequently the continuous ratio
\(R=(\phi^{(2m+4)}-c\phi^{(2m+2)})/\phi\) tends to \(+\infty\)
at both ends and has a finite global minimum. Choose \(\epsilon>0\)
small enough that \(1+\epsilon R\ge1/2\). This proves positivity.
All derivative tails are integrable with every polynomial and
exponential weight. Integration by parts proves normalization and (2).
Differentiation of the full convolution identity proves annihilation.

The Fourier multiplier is

\[
 \widehat f_{\epsilon,m}(z)
 =X(z)H_{\epsilon,m}(z),\qquad
 H_{\epsilon,m}(z)=
 1+\epsilon(-1)^{m+2}z^{2m+2}(z^2+c).                           \tag{4}
\]

If \(m\) is even, \(H\) is positive on the whole real axis, so all
of its \(2m+4\) roots are nonreal. If \(m\) is odd, the function
\(x^{2m+2}(x^2+c)\) is strictly increasing for \(x>0\), so \(H\)
has exactly two real roots. Its remaining \(2m+2\) roots are nonreal.
Every root of \(H\) is a root of the entire product \(XH\).
Equation (3) also proves the stated leading tail rate. QED.

In particular, the actual theta density is **not** a minimum-variance
positive annihilator of the full Weil source: take \(m=0\). Nor does
minimizing the next moment after fixing any finite prefix identify it.
The extra zeros in this first construction need not lie in the inherited
quasi-RH strip. A different construction in Section 3 addresses that
additional constraint while making the variance error arbitrarily small.

## 2. One completely explicit positive density

There is no unspecified small parameter in the example

\[
 f_*=\phi+\frac{\phi^{(4)}-\phi''}{10000}.                       \tag{5}
\]

Its variance is exactly \(V_X-1/5000\), and its Fourier multiplier is
\(1+(z^4+z^2)/10000\). Thus its four added zeros are exactly

\[
                  z=\pm\frac{\sqrt{199}}2
                      \pm i\frac{\sqrt{201}}2.                 \tag{6}
\]

Here is a global positivity certificate for (5), requiring no numerical
theta summation. Put \(u=\pi n^2e^{2x}\), for \(x\ge0\). Apart from
the common positive normalization, the \(n\)-th theta term is
\(e^{x/2}P_0(u)e^{-u}\), with \(P_0=4u^2-6u\), and its \(j\)-th
derivative is \(e^{x/2}P_j(u)e^{-u}\), where

\[
 P_{j+1}(u)=(1/2-2u)P_j(u)+2uP_j'(u).                           \tag{7}
\]

The required polynomial is \(Q(u)=10000P_0(u)+P_4(u)-P_2(u)\).
Since \(u\ge\pi>3\), it suffices to prove \(Q>0\) on \([3,\infty)\).
On \([3,10]\), the Bernstein coefficients of degree six, in order
\(0,\ldots,6\), are

\[
\left(
\frac{1551429}{8},\frac{6801147}{16},\frac{4709161}{6},
\frac{18462881}{16},\frac{8691051}{8},\frac{3777125}{48},
\frac{21472625}{4}
\right).                                                       \tag{8}
\]

All are positive. On \([10,\infty)\), write \(u=10+y\). The
coefficients of \(P_4(10+y)-P_2(10+y)\), in ascending powers of
\(y\), are

\[
\left(
\frac{7872625}{4},\frac{30350625}{8},\frac{7550805}{4},
422000,48360,2784,64
\right),                                                       \tag{9}
\]

also positive. Since \(P_0>0\) there, \(Q>0\). Every summand in (5)
is positive, proving the claimed density globally. Evenness handles
\(x<0\), and differentiation of the theta transformation supplies
smoothness at zero. The standard-library checker reconstructs (7)--(9)
using rational arithmetic and checks the polynomial for (6).

## 3. Exact insertion at any prescribed small strip width

The previous example moves zeros too far vertically to preserve a narrow
strip. The next family avoids that limitation.

**Theorem 2.** Fix \(\eta>0\). For sufficiently small \(\epsilon>0\),
put

\[
 \delta=4\eta^2\epsilon(1+\eta^2\epsilon),\qquad
 \psi_{\epsilon,\eta}=
 \frac{(1+\delta)\phi+2\epsilon\phi''+
                         \epsilon^2\phi^{(4)}}{1+\delta}.       \tag{10}
\]

This is a strictly positive, even probability density annihilating
\(K_W\). Its variance is

\[
 V_X+\frac{4\epsilon}{1+\delta},                               \tag{11}
\]

and its Fourier transform is \(X(z)\) times the normalized polynomial

\[
 P_{\epsilon,\eta}(z)=
 \frac{(1-\epsilon z^2)^2+\delta}{1+\delta},                    \tag{12}
\]

whose zeros are exactly

\[
                    z=\pm\sqrt{\epsilon^{-1}+\eta^2}
                                \pm i\eta.                    \tag{13}
\]

*Proof.* Both \(\phi''\) and \(\phi^{(4)}\) are eventually positive
by (3). On a remaining fixed compact interval, \(\phi\) has a positive
minimum, and the derivative terms are uniformly small as
\(\epsilon\to0\). This proves global positivity for sufficiently
small \(\epsilon\). Normalization, moments, and annihilation follow
by integration by parts and differentiation of (3) of the companion
note. Fourier transformation gives (12). For
\(R=\sqrt{\epsilon^{-1}+\eta^2}\), the square of \(R+i\eta\) is
\(\epsilon^{-1}+2iR\eta\), so
\((1-\epsilon(R+i\eta)^2)^2=-4\epsilon^2R^2\eta^2=-\delta\).
The four roots in (13) are distinct, proving the full root list. QED.

If all zeros of \(X\) are known to lie in \(|\Im z|\le\Delta\),
choose any \(0<\eta\le\Delta\). Then this *auxiliary* function retains
that same strip, has the exact full-source annihilator property, and
has a variance arbitrarily close to the theta variance, while containing
an extra nonreal quartet at arbitrarily large real height. This does not
put such zeros into Xi; it shows why these controls do not identify Xi.

The second construction does not preserve the variance exactly. The
first preserves a prescribed finite moment prefix but does not promise
the same narrow strip. These scopes must not be combined into a stronger
statement without a separate construction.

## 4. Consequence for the new spectral attack

The natural replacement for safely shifted resolvents is a legal,
source-sensitive spectral selection, such as the exact variance equation
in the companion note. Theorem 1 rules out a shortcut through unconstrained
minimum variance in the positive nullsource class. Theorem 2 shows that
approximate variance matching, a fixed strip, positivity, and the exact
all-prime annihilator still leave source ambiguity.

The resolvent selection retains additional de Branges structure absent
from these countermodels. It remains worth investigating the narrow
spectral window identified in the companion note. Neither construction
here refutes that possibility, supplies its existence theorem, or moves
the ordinary-zeta zero-free boundary.

## Sources and review scope

The source is the classical theta formula and the explicit formula,
in the convention pinned at PR #1017 commit
`450dd8abecf58dfe60b3bc39bda0f792ea82ce95`. The derivative construction,
explicit positivity polynomial, and prescribed-width quartet above are
the deductions proposed here. The last family was developed during
parallel mathematical review. No claim of external priority is made.

The exact checker covers the finite polynomial identities and the
specified global polynomial positivity certificate. It does not replace
the analytic theta/Weil arguments, certify any zeros of zeta, or prove
any zero-free region.
