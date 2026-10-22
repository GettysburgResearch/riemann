# L-105109 — Log-derivative edge margins and exterior-critical obstruction

Claim ID: L-105109

Status: **PROPOSED EXACT FINITE-WINDOW THEOREM**

Created: 2026-08-23

Depends on: L-105105; L-105106; R-105106; L-105107

RH status: **unproved**

## 1. The two denominator margins

Let \(F\) be holomorphic near a compact rectifiable boundary arc \(E\),
with \(F,F',F''\) nonzero on \(E\).  Put

\[
\mathscr L_F=\frac{F'}F,
\qquad
\mathscr A_F=\mathscr L_F^2+\mathscr L_F'
=\frac{F''}F.
\tag{L-105109.1}
\]

The unweighted first and second quotient carriers are exactly

\[
\boxed{
\frac F{F'}=\frac1{\mathscr L_F},
\qquad
\frac{F^2}{F'F''}
=\frac1{\mathscr L_F\mathscr A_F}.
}
\tag{L-105109.2}
\]

Define the positive edge margins

\[
m_1(E)=\inf_E|\mathscr L_F|,
\quad
m_2(E)=\inf_E|\mathscr A_F|,
\quad
m_{12}(E)=\inf_E|\mathscr L_F\mathscr A_F|.
\tag{L-105109.3}
\]

Compactness gives

\[
\boxed{
\left\|\frac F{F'}\right\|_E=\frac1{m_1(E)},
\qquad
\left\|\frac{F^2}{F'F''}\right\|_E
=\frac1{m_{12}(E)}
\le\frac1{m_1(E)m_2(E)}.
}
\tag{L-105109.4}
\]

Let \(W_{1,*},W_{2,*}\) be the L-105107 boundary-optimal selectors for
the two supplied manifests, with norms \(\tau_1,\tau_2\).  Their boundary
moduli are constant, so on every boundary arc

\[
\boxed{
\left\|W_{1,*}\frac F{F'}\right\|_E
=\frac{\tau_1}{m_1(E)},
\qquad
\left\|W_{2,*}\frac{F^2}{F'F''}\right\|_E
=\frac{\tau_2}{m_{12}(E)}.
}
\tag{L-105109.5}
\]

Consequently

\[
\left|
\frac1{2\pi i}\int_EW_{1,*}\frac F{F'}\,dz
\right|
\le
\frac{\operatorname{len}(E)}{2\pi}
\frac{\tau_1}{m_1(E)},
\tag{L-105109.6}
\]

and

\[
\left|
\frac1{2\pi i}\int_EW_{2,*}\frac{F^2}{F'F''}\,dz
\right|
\le
\frac{\operatorname{len}(E)}{2\pi}
\frac{\tau_2}{m_{12}(E)}.
\tag{L-105109.7}
\]

Thus upper bounds for \(\mathscr L_F\) or \(\mathscr A_F\) do not close
the edge gate.  What the absolute envelope requires is a lower margin for
their product, strong enough to absorb the selector norm.

## 2. Finite interior jets do not certify an edge margin

The independence is exact.  Let \(S\) be a finite interior set, assign
depths \(M_a\in\mathbb Z_{\ge1}\), let \(\zeta\notin S\) be a boundary
point, and put

\[
P(z)=\prod_{a\in S}(z-a)^{M_a}.
\tag{L-105109.8}
\]

Assume \(F(\zeta)\ne0\), fix \(0\le\varepsilon\le1\), and write

\[
\ell=\mathscr L_F(\zeta),
\qquad
A=\mathscr A_F(\zeta).
\tag{L-105109.9}
\]

If \(\ell\ne0\), define

\[
Q_1(z)=(z-\zeta)P(z),
\qquad
t_1=-\frac{\ell}{P(\zeta)},
\qquad
\widetilde F_{1,\varepsilon}
=e^{(1-\varepsilon)t_1Q_1}F.
\tag{L-105109.10}
\]

Since \(Q_1'(\zeta)=P(\zeta)\),

\[
\mathscr L_{\widetilde F_{1,\varepsilon}}(\zeta)
=\varepsilon\ell.
\tag{L-105109.11}
\]

If \(\ell A\ne0\), define instead

\[
Q_2(z)=(z-\zeta)^2P(z),
\qquad
t_2=-\frac{A}{2P(\zeta)},
\qquad
\widetilde F_{2,\varepsilon}
=e^{(1-\varepsilon)t_2Q_2}F.
\tag{L-105109.12}
\]

Here \(Q_2'(\zeta)=0\) and \(Q_2''(\zeta)=2P(\zeta)\), so

\[
\mathscr L_{\widetilde F_{2,\varepsilon}}(\zeta)=\ell,
\qquad
\mathscr A_{\widetilde F_{2,\varepsilon}}(\zeta)=\varepsilon A.
\tag{L-105109.13}
\]

At every \(a\in S\), both gauges are \(1+O((z-a)^{M_a})\).
Therefore they preserve the zeros of \(F\) exactly and preserve all Taylor
jets through order \(M_a-1\), while the first or second boundary
denominator can be made arbitrarily small.  At \(\varepsilon=0\) it
vanishes exactly.

This gauge lemma does **not** preserve the complete derivative-event
manifest.  Its conclusion is narrower and load-bearing: no finite collection
of interior zeros and jets can replace a global boundary lower-margin or
collar certificate.

## 3. A regular even family with a stable first manifest

The preceding firewall has a completely regular explicit realization.  On
the unit disk, for real

\[
1<s<s_+:=\frac{5+\sqrt{17}}4,
\tag{L-105109.14}
\]

set

\[
\boxed{
F_s(z)=
\exp\!\left(\frac{z^2}{2}-\frac{z^4}{4s}\right).
}
\tag{L-105109.15}
\]

This is real, even, entire, and zero-free.  Its logarithmic denominators are

\[
\mathscr L_s(z)=z\left(1-\frac{z^2}{s}\right),
\tag{L-105109.16}
\]

and, with \(x=z^2\),

\[
\mathscr A_s(z)=\frac{P_s(x)}{s^2},
\quad
P_s(x)=x^3-2sx^2+(s^2-3s)x+s^2.
\tag{L-105109.17}
\]

The zeros of \(F_s'\) are \(0,\pm\sqrt s\).  Hence the complete actual
pole manifest of \(F_s/F_s'\) in \(\mathbb D\) is the one simple target
at zero, for every \(s\) in (L-105109.14).

For the second quotient, observe

\[
P_s(-1)=s-1>0,
\quad
P_s(0)=s^2>0,
\quad
P_s(1)=2s^2-5s+1<0,
\quad
P_s(s)=-2s^2<0.
\tag{L-105109.18}
\]

Together with the signs at \(\pm\infty\), these force exactly three simple
real roots

\[
\gamma(s)<-1<0<\alpha(s)<1<s<\beta(s).
\tag{L-105109.19}
\]

Equivalently, squarefreeness is independently certified by

\[
\operatorname{disc}_x P_s
=s^3(8s^2+9s+108)>0.
\]

Thus the complete actual pole manifest of
\(F_s^2/(F_s'F_s'')\) in \(\mathbb D\) consists of the simple target zero
and the two simple nontargets \(\pm\sqrt{\alpha(s)}\).  There is no boundary
pole in either quotient.  There is also no common derivative event, since

\[
\mathscr A_s(0)=1,
\qquad
\mathscr A_s(\pm\sqrt s)=\frac{P_s(s)}{s^2}=-2.
\]

Both target principal coefficients are fixed:

\[
\boxed{
\lim_{z\to0}z\frac{F_s}{F_s'}=1,
\qquad
\lim_{z\to0}z\frac{F_s^2}{F_s'F_s''}=1.
}
\tag{L-105109.20}
\]

The first optimal selector is

\[
W_{1,s}=1,
\qquad
\tau_1(s)=1.
\tag{L-105109.21}
\]

For the second manifest, L-105107 gives

\[
\boxed{
W_{2,s}(z)=
\frac{\alpha(s)-z^2}
{\alpha(s)(1-\alpha(s)z^2)},
\qquad
\tau_2(s)=\frac1{\alpha(s)}.
}
\tag{L-105109.22}
\]

At \(s=1\),

\[
P_1(x)=(x+1)(x^2-3x+1),
\tag{L-105109.23}
\]

so continuity of the isolated root gives

\[
\alpha(s)\longrightarrow\frac{3-\sqrt5}{2},
\qquad
\tau_2(s)\longrightarrow\frac{3+\sqrt5}{2}.
\tag{L-105109.24}
\]

Both optimal selector norms therefore stay bounded as \(s\downarrow1\).

## 4. Exact selector-weighted boundary collapse

At the boundary point \(z=1\),

\[
\boxed{
\frac{F_s(1)}{F_s'(1)}
=\frac{s}{s-1},
\qquad
\frac{F_s(1)^2}{F_s'(1)F_s''(1)}
=\frac{s^3}
{(s-1)(2s^2-5s+1)}.
}
\tag{L-105109.25}
\]

The first expression tends to \(+\infty\); the magnitude of the second
tends to \(+\infty\) like \(1/(2(s-1))\).  Hence, on any closed boundary
arc \(E\) containing one,

\[
\left\|W_{1,s}\frac{F_s}{F_s'}\right\|_E
\longrightarrow\infty,
\qquad
\left\|W_{2,s}\frac{F_s^2}{F_s'F_s''}\right\|_E
\longrightarrow\infty.
\tag{L-105109.26}
\]

The divergence is not selector conditioning: \(\tau_1\) is constant and
\(\tau_2\) has the finite limit (L-105109.24).  It is an exterior-event
collar failure.  The critical points \(\pm\sqrt s\) approach the contour
from outside while remaining absent from the complete *interior* manifest.

The full contour residue identities do not diverge.  In fact,

\[
\frac1{2\pi i}\int_{\partial\mathbb D}
W_{j,s}h_{j,s}\,dz=1
\qquad(j=1,2).
\tag{L-105109.27}
\]

Thus (L-105109.26) refutes closure by absolute/supremum edge envelopes.  It
does not rule out a new phase-sensitive cancellation estimate for the
oriented contour pieces.

## 5. Exact rational checkpoint

At \(s=101/100\), the sign certificates include

\[
P_s(-2)=-\frac{110401}{10000},
\quad
P_s(-1)=\frac1{100},
\quad
P_s(3/8)=\frac{11219}{320000},
\tag{L-105109.28}
\]

and

\[
P_s(2/5)=-\frac{2153}{50000},
\quad
P_s(1)=-\frac{10049}{5000},
\quad
P_s(3)=\frac{4763}{1250}.
\tag{L-105109.29}
\]

Therefore

\[
\frac38<\alpha(101/100)<\frac25,
\qquad
\frac52<\tau_2(101/100)<\frac83.
\tag{L-105109.30}
\]

The boundary values are exactly

\[
\frac{F_s(1)}{F_s'(1)}=101,
\qquad
\frac{F_s(1)^2}{F_s'(1)F_s''(1)}
=-\frac{1030301}{20098}.
\tag{L-105109.31}
\]

No floating-point root finding is needed.

## 6. Boundary of the result

The theorem identifies the exact denominator margins required by the
L-105107 edge envelope and proves that they are independent of finite
interior jet and selector conditioning ledgers.  It does not supply:

- the Xi event manifest or an exterior collar free of near-critical events;
- lower bounds for \(|\Xi'/\Xi|\) or
  \(|(\Xi'/\Xi)^2+(\Xi'/\Xi)'|\) on changing rectangles;
- phase-sensitive cancellation estimates for individual oriented edges;
- cofinal Green–Gram bounds, weighted-edge decay, multiplicity-defect
  control, or strict jet coherence;
- RCMV104530 or RH.

No novelty is claimed for logarithmic differentiation, zero-free
exponential gauges, or the maximum-modulus principle.  The contribution is
the exact quotient-margin ledger for the L-105105/L-105107 observable and a
stable-manifest family proving that optimal selector control does not close
the remaining boundary gate.

The closest programme antecedents are L/R-105106: their clustered quartic
fixture has selector-conditioning growth, and the abstract remainder
\(h_C=1/z+C\) is not a simultaneous derivative-quotient realization.
Accepted safe-disc or low-order actual-Xi log-derivative claims concern
different kernels/regions and give no reciprocal boundary lower margin.
The family (L-105109.15) is a zero-free order-four test function, not Xi.
Its second nontarget locations move with \(s\); only their number, orders,
separation regime, and bounded selector cost are stable.
