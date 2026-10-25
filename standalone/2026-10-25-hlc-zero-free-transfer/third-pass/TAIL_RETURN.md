# The coherent large-ratio return and its surviving inverse factors

Status: **exact algebra and a contour-scale audit; independent review
requested**. This note examines the remaining large reduced-numerator
range in `GCD_NATIVE_COEFFICIENT.md`. It proves a local coherent-return
identity and identifies the same-character inverse factors that survive
there. It does not prove a saving for the complete remaining tail or
license a new global contour shift.

The positive component theorem in that companion is unchanged. In
particular, the complete tail above \(U^{9/20}\) in its equation (32)
is still an unresolved input. The calculations below retain the two
Möbius signs, the coprimality of the reduced numerator and denominator,
and the primitive versus natural zero distinction.

## 1. The local series before taking any absolute value

Use the exact smooth Heath--Brown coefficient and gcd grouping from
`GCD_NATIVE_COEFFICIENT.md` (6)--(12). Let s,z be the two Mellin
variables of the original short Möbius cutoffs. Work first at a prime
ideal p outside the full natural puncture P, and abbreviate its norm
by q. Put

\[
 r=q^{-s},\qquad t=q^{-z},\qquad
 \Delta=(1-r/q)(1-t/q).
\]

For exponent zero, one, and two of p in the reduced numerator a,
the local gcd coefficients before dividing out their common scalar
factor are respectively

\[
             \Delta,\qquad -(r+t-rt/q),\qquad rt.             \tag{1}
\]

This can be checked directly from the original two Möbius factors:
their local product coefficients at exponents zero, one and two are
\(1,-(r+t),rt\). Summing the residual gcd with its \(1/Nd\)
weight gives (1). Equivalently, (1) is the one-prime instance of the
three-way allocation in the companion note. Its second term includes
the original repeated-prime contribution \(rt/q\).

Let h denote the Mellin variable of a reduced-numerator cutoff, so
that its contribution to a coefficient is \((Na)^{-h}\). Let v be
the Mellin variable of the reflected ratio kernel and put

\[
 w=1-v,\qquad
 X=\psi(p)q^{-w-h},\qquad Y=\overline{\psi(p)}q^{-v},\qquad
 u=q^{-1-h}.
\]

Because p is on the unit support, \(XY=u\). The coprimality
\((a,b)=1\) must be kept. If the local exponent of a is zero,
the local denominator b contributes \((1-Y)^{-1}\). If the
exponent of a is one or two, the local exponent of b is zero.
Consequently the complete local factor is exactly

\[
\begin{split}
 \frac{\Delta}{1-Y}-(r+t-rt/q)X+rtX^2
   &=\frac{\mathcal N_p}{1-Y},\\
 \mathcal N_p
   &=\Delta+\{-(r+t-rt/q)X+rtX^2\}(1-Y)\\
   &=(1-rX)(1-tX)
      +(u-1/q)(r+t-rt/q-rtX).                               \tag{2}
\end{split}
\]

The last line follows by expanding and using \(XY=u\). It is an
exact polynomial identity; no estimate and no choice of contours is
part of it. In particular, at h=0,

\[
              \boxed{\quad\mathcal N_p=(1-rX)(1-tX).\quad}   \tag{3}
\]

This cancellation requires the whole denominator Euler series and
the full two-sign gcd coefficient. Dropping the repeated-prime
term, or replacing \((a,b)=1\) by independent a and b factors,
changes (2).

At primes in the primitive conductor, the original character values
are zero and are retained directly; the unit relation \(XY=u\)
is not asserted there. At a redundant natural puncture, the reduced
numerator has its original zero while the primitive denominator need
not. Its full Euler series and the outside e-divisor factor from the
primitive reflection must both be retained. No false condition
\((b,Q_s)=1\) is inserted. These finite factors are checked globally
by the original primal identity in the next section.

## 2. What the complete return at h=0 actually contains

Write

\[
 L_\psi(w)=\sum_n\frac{\psi(n)}{(Nn)^w}
       =L(w,\psi^*)\prod_{p\mid Q_s}(1-\psi^*(p)Np^{-w}),
\]

with primitive zero factors included by their actual zero values.
Thus \(L_\psi\) uses the same natural presentation and every original
puncture. All statements are made separately for a licensed
multiplicative ray presentation; the original finite outer linear
combination is preserved when presentations are summed.

The h=0 product of the good local identities (3), followed by the
ordinary functional equation for the full denominator L function,
returns

\[
              \boxed{\quad
 \mathcal R_\psi(w;s,z)
     =\frac{L_\psi(w)}{L_\psi(w+s)L_\psi(w+z)}.
                         \quad}                            \tag{4}
\]

There is a direct global check which avoids inferring a contour shift
from a local Euler calculation. Let the common short cutoff be
\(w_0\), put

\[
 m_y(w;\psi)=\sum_n\frac{\mu(n)\psi(n)}{(Nn)^w}w_0(Nn/y),
\]

and let \(\widehat V\) and \(\widehat w_0\) be the ordinary
Mellin transforms. In an initial region of absolute convergence,

\[
 m_y(w;\psi)=\frac1{2\pi i}\int
        \widehat w_0(s)y^s L_\psi(w+s)^{-1}\,ds.
\]

The exact smooth Heath--Brown identity on the original V annulus,
with its vanishing short term, therefore gives

\[
\begin{split}
 M_u(D;V)={}&-\frac1{(2\pi i)^3}
    \iiint D^{w-1/2}y^{s+z}\widehat V(w)
               \widehat w_0(s)\widehat w_0(z)\\
 &\hspace{20mm}\times
       \frac{L_\psi(w)}{L_\psi(w+s)L_\psi(w+z)}
                        \,dw\,ds\,dz .                      \tag{5}
\end{split}
\]

For example, take all three initial real parts positive and
\(\Re w>1\). The finite cutoff sums and rapid Mellin decay justify
the displayed identities there. Equation (5) also confirms every
finite puncture factor in (4), without replacing the primitive dual
character by the natural character on its enlarged zero set.

The full smooth outer support \(Nr<8D\) remains in (5), including
the terms which were individually zero in the primal sum. The
identity is meromorphic in the displayed L arguments. Moving its
contours across reciprocal poles requires a separate argument and
is not authorized by (2)--(5).

At s=z=0, (4) is exactly \(1/L_\psi(w)\). At equal negative real
shifts it is one full L function multiplied by two reciprocal factors
of the same original character. A single Mellin point is not a
positive-mass contribution, so this observation is not a lower
bound for any signed tail. It identifies the analytic factor whose
uniform moment still needs to be controlled when this route is used.

## 3. No division by a possibly vanishing local polynomial

The reduced-numerator polynomial, after the harmless scalar factor
is removed, is

\[
 \mathcal D_p(X)=1-
       \frac{r+t-rt/q}{\Delta}X+\frac{rt}{\Delta}X^2.        \tag{6}
\]

One must not restore \((a,b)=1\) by dividing by
\(\mathcal D_p(X)\) and then claim that the quotient is bounded
using only ordinary local L factors. This polynomial can vanish
where those ordinary factors do not.

An exact example uses the good norm q=7 and r=t=5/4. These real
shifts have \(\beta=1-\log_7(5/4)>7/8\), since \((5/4)^8<7\).
With \(\Delta=(23/28)^2\),

\[
                    \mathcal D_p(2/5)>0,
                  \qquad\mathcal D_p(1/2)<0.                \tag{7}
\]

Thus there is a real zero between 2/5 and 1/2. At that zero both
\(1-rX\) and \(1-tX\) are nonzero. Its real Dirichlet exponent
is even to the right of \(2-2\beta\), because
\(X<1/2<16/25=7^{-(2-2\beta)}\). Therefore convergence of a
correction product to the right of \(2-2\beta\) would not by
itself license division by its local factors.

Equation (2) avoids this issue: it sums the common coprimality
condition directly. If a denominator b is fixed instead, the
safe alternative is a direct product over primes not dividing b,
with the omitted ordinary local L factors restored explicitly.
Neither approach divides by (6).

## 4. The large-B scale calculation

The following is a finite exponent calculation about one possible
buffered-contour bound. It is not a theorem asserting that its
contours can be shifted or that its Euler corrections have a
particular global analytic continuation.

Let \(D=U^r\), and allow even unequal original cutoff scales
\(y_1=U^\alpha\), \(y_2=U^{r-\alpha}\), with
\(0<\alpha<r\). Constant factors required by the exact
Heath--Brown support do not affect these exponents. The unequal
identity is \(\mu=m_{y_1}+m_{y_2}-m_{y_1}*m_{y_2}*1\)
through norm \(y_1y_2\); both short terms vanish on the original
annulus for sufficiently large U and fixed interior alpha. Write
\(s_0=\Re s\), \(z_0=\Re z\), and \(h_0=\Re h\).
At reduced-numerator scale \(B\asymp D\), the power of U outside
the same-character factors is

\[
       r(\Re w-1/2)+rh_0+\alpha s_0+(r-\alpha)z_0.
                                                                  \tag{8}
\]

Suppose a buffered zero-free line for the two reciprocals forces

\[
 \Re w+h_0+s_0\ge a,\qquad
 \Re w+h_0+z_0\ge a.
\]

Even if the numerator and every correction factor are granted
subpower cost, (8) is at least

\[
\begin{split}
 &r(a-1/2)
   +\alpha(s_0-\min(s_0,z_0))
   +(r-\alpha)(z_0-\min(s_0,z_0))\\
 &\hspace{25mm}\ge r(a-1/2).                                \tag{9}
\end{split}
\]

For interior alpha, equality holds precisely when the two real
shifts agree and the reciprocal line is used without an extra
buffer. In the balanced symmetric case, moving s,z left by theta
multiplies the cutoff weight by \(D^{-\theta}\), but the required
move of w to the right multiplies it by \(D^\theta\). The two
powers cancel exactly. Unequal shifts add the nonnegative terms
in (9). When \(a=(1+\delta)/2\), the surviving amplitude cost is
\(U^{\delta r/2}\), the ordinary inverse cost.

The same conclusion follows for the h=0 complete return (5)
without introducing a reduced-numerator contour. For B smaller
than D the h contribution is different; that distinction is
consistent with the proved small-ratio gain in the companion.

For scale context, insert the already imported density resource

\[
                      R(a)=\frac{31-32a}{21-12a}
\]

from `second-pass/CAPPED_NATIVE_MOMENT.md`. The optimistic bound
based on (9) has the familiar upper-envelope exponents
\(R(a)+(2a-1)r\), before any additional numerator cost. One
admissible bin, \(a=4/5\), already contributes the resource

\[
                         \frac9{19}+\frac35r.                \tag{10}
\]

Throughout \(29/25\le r\le117/100\), this is larger than
\((1+5r)/6-1/1000\). At the actual critical r, optimizing that
existing contour envelope gives approximately 1.17209533,
whereas the proposed improved full moment would need approximately
1.13562798. These are comparisons of available upper-bound
resources, with the critical length as recorded in
`SHORT_INVERSE.md`, not lower bounds on the actual moments or on the actual
population of any zero bin.

Thus the direct two-variable contour estimate does not supply the
missing full-tail saving. A coherent estimate for the surviving
same-character product, or cancellation that uses its complete
outside coefficients, would be additional analytic input. The
local identities do not rule such an estimate out.

## 5. Verification scope

`check_tail_return.py` compares the exact polynomial coefficients
in (2), checks the h=0 specialization, checks the nonvanishing of
the ordinary factors at the explicit sign-changing local
polynomial, and verifies (9)--(10) using rational arithmetic.
Negative controls remove the repeated-prime term and ignore the
required contour displacement.

The checker does not establish a moment bound or a global contour
deformation. The imported arithmetic premises and common smooth
calculus are those pinned in `SIGNED_NATIVE.md` and
`GCD_NATIVE_COEFFICIENT.md`. This note adds no zero-free premise and
claims no improvement to the complete inverse.
