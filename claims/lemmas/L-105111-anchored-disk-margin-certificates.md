# L-105111 — Anchored logarithmic-variation and disk-cover edge margins

Claim ID: L-105111

Status: **PROPOSED EXACT FINITE-EDGE THEOREM**

Created: 2026-08-23

Depends on: L-105107; L-105109; L-105110

RH status: **unproved**

## 1. Exact anchored logarithmic drop

Let \(E=\gamma([0,\ell])\) be a compact parametrized rectifiable arc, with
\(\gamma\) piecewise \(C^1\).  Let \(G\) be holomorphic in a neighborhood of
\(E\) and nonzero on \(E\).  Fix \(s_*\in[0,\ell]\), write
\(z_*=\gamma(s_*)\), and define

\[
\boxed{
D_G(E;s_*)
=
\max_{0\le s\le\ell}
\left\{
-\int_{s_*}^{s}
\Re\!\left[
\frac{G'}G(\gamma(t))\gamma'(t)
\right]dt
\right\}.
}
\tag{L-105111.1}
\]

Since the anchor itself is included, \(D_G\ge0\).  The logarithmic-modulus
identity

\[
\log|G(\gamma(s))|-\log|G(z_*)|
=
\int_{s_*}^{s}
\Re\!\left[
\frac{G'}G(\gamma(t))\gamma'(t)
\right]dt
\tag{L-105111.2}
\]

gives the exact margin ledger

\[
\boxed{
\inf_E|G|
=|G(z_*)|e^{-D_G(E;s_*)}.
}
\tag{L-105111.3}
\]

Define the total logarithmic-modulus variation

\[
V_G(E)
=
\int_0^\ell
\left|
\Re\!\left[
\frac{G'}G(\gamma(t))\gamma'(t)
\right]
\right|dt.
\tag{L-105111.4}
\]

Then \(D_G\le V_G\), so the checkable sufficient certificate

\[
|G(z_*)|\ge a>0,
\qquad
V_G(E)\le\log R
\tag{L-105111.5}
\]

implies

\[
\boxed{
\inf_E|G|\ge\frac aR.
}
\tag{L-105111.6}
\]

One may replace (L-105111.4) by the larger complex log-variation
\(\int_E|G'/G|\,|dz|\).  The real-part form is the sharper load-bearing
quantity.

## 2. The two programme denominators

For a zero-free \(F\) near \(E\), put

\[
L=\frac{F'}F,
\qquad
A=\frac{F''}F=L^2+L',
\qquad
B=\frac{F'''}F,
\tag{L-105111.7}
\]

and

\[
G_1=L,
\qquad
G_{12}=LA.
\tag{L-105111.8}
\]

Their exact derivatives are

\[
\boxed{
G_1'=A-L^2,
\qquad
G_{12}'=A^2+LB-2L^2A.
}
\tag{L-105111.9}
\]

When the relevant denominators are nonzero,

\[
\boxed{
\frac{G_1'}{G_1}=\frac AL-L,
\qquad
\frac{G_{12}'}{G_{12}}
=\frac AL+\frac BA-2L.
}
\tag{L-105111.10}
\]

Thus L-105109's margins have the exact anchored representations

\[
m_1(E)=|L(z_*)|e^{-D_L(E;s_*)},
\qquad
m_{12}(E)=|L(z_*)A(z_*)|e^{-D_{LA}(E;s_*)}.
\tag{L-105111.11}
\]

If \(E\subset\partial\Omega\) is a boundary arc of the same selector domain
\(\Omega\) used in L-105107, then the boundary-optimal selectors have
constant modulus and

\[
\boxed{
\left\|W_{1,*}\frac F{F'}\right\|_E
=\frac{\tau_1e^{D_L}}{|L(z_*)|},
\qquad
\left\|W_{2,*}\frac{F^2}{F'F''}\right\|_E
=\frac{\tau_2e^{D_{LA}}}{|L(z_*)A(z_*)|}.
}
\tag{L-105111.12}
\]

Replacing the exact drops by the corresponding total variations gives
explicit sufficient upper envelopes.  For a general weight without constant
boundary modulus, replace \(\tau_j\) by \(\|W_j\|_E\) and retain only the
upper bound.

## 3. A noncircular finite-disk certificate

The log-drop identity assumes nonvanishing has already been authenticated.
A finite disk cover can prove both nonvanishing and a quantitative margin.
Suppose

\[
E\subset\bigcup_{j=1}^J\overline D(c_j,r_j),
\tag{L-105111.13}
\]

where every closed disk lies in the holomorphy domain of \(G\).  Suppose

\[
|G(c_j)|\ge a_j,
\qquad
\sup_{\overline D(c_j,r_j)}|G'|\le M_j,
\qquad
\mu_j:=a_j-r_jM_j>0.
\tag{L-105111.14}
\]

The line segment from \(c_j\) to any point of its disk stays inside that
disk, so

\[
|G(z)-G(c_j)|\le r_jM_j.
\tag{L-105111.15}
\]

Consequently

\[
\boxed{
\inf_E|G|\ge\min_j\mu_j>0.
}
\tag{L-105111.16}
\]

For \(G_1\) and \(G_{12}\), (L-105111.9) turns the derivative obligations
into the normalized-derivative bounds

\[
M_{1,j}\ge\sup_{D_j}|A-L^2|,
\qquad
M_{12,j}\ge\sup_{D_j}|A^2+LB-2L^2A|.
\tag{L-105111.17}
\]

Any rigorous Taylor majorant for \(|G(z)-G(c_j)|\) may replace \(r_jM_j\).
The logical point is the positive local slack, not the particular
first-derivative enclosure.

## 4. Exact rational fixture

On \(E=[0,1]\), take

\[
F_0(z)=\exp(z-z^2/8),
\qquad
u=1-\frac z4.
\tag{L-105111.18}
\]

Then

\[
L=u,
\qquad
A=u^2-\frac14,
\qquad
B=u^3-\frac34u,
\tag{L-105111.19}
\]

and

\[
G_{12}=u\left(u^2-\frac14\right),
\qquad
G_{12}'=-\frac14\left(3u^2-\frac14\right).
\tag{L-105111.20}
\]

Both \(L\) and \(G_{12}\) are positive and decreasing on \(E\).  With anchor
\(z_*=0\),

\[
L(0)=1,
\qquad
G_{12}(0)=\frac34,
\tag{L-105111.21}
\]

while

\[
\boxed{
m_1=\frac34,
\quad
m_{12}=\frac{15}{64},
\quad
D_L=\log\frac43,
\quad
D_{LA}=\log\frac{16}{5}.
}
\tag{L-105111.22}
\]

Both anchored identities are attained with equality.

The two disks

\[
\overline D(1/4,1/4),
\qquad
\overline D(3/4,1/4)
\tag{L-105111.23}
\]

cover \(E\).  For \(G_1=L\), the center values are \(15/16,13/16\), the
derivative bound is \(1/4\), and the slacks are

\[
\frac78,
\qquad
\frac34.
\tag{L-105111.24}
\]

Thus the disk certificate recovers the exact first margin.  For \(G_{12}\),
the center values and exact disk derivative suprema are

\[
\begin{array}{c|cc}
c_j&1/4&3/4\\
\hline
G_{12}(c_j)&2415/4096&1365/4096\\
M_{12,j}&11/16&131/256
\end{array}
\tag{L-105111.25}
\]

and hence

\[
\boxed{
\mu_{12,1}=\frac{1711}{4096},
\qquad
\mu_{12,2}=\frac{841}{4096}.
}
\tag{L-105111.26}
\]

The certified product margin \(841/4096\) is below but close to the exact
\(15/64=960/4096\), using rational polynomial arithmetic only.

## 5. Two sharp independence checks

First, a fixed anchor does not control the log drop.  For \(0<q<1\),

\[
F_q(z)=\exp\!\left(z-\frac{1-q}{2}z^2\right)
\tag{L-105111.27}
\]

has, on \([0,1]\),

\[
L_q(0)=1,
\qquad
m_1=q,
\qquad
D_L=\log(1/q).
\tag{L-105111.28}
\]

The exponential loss in (L-105111.3) is therefore sharp.

Second, control of \(L\) alone does not control \(LA\).  For

\[
0<a<2-\sqrt3,
\qquad
F_a(z)=\exp(z-az^3/3),
\tag{L-105111.29}
\]

one has

\[
L_a=1-az^2,
\qquad
A_a=(1-az^2)^2-2az.
\tag{L-105111.30}
\]

Both are positive and decreasing on \([0,1]\), and

\[
m_1=1-a,
\qquad
m_{12}=(1-a)(1-4a+a^2).
\tag{L-105111.31}
\]

As \(a\uparrow2-\sqrt3\), \(m_{12}\to0\) while
\(m_1\to\sqrt3-1>0\).  At the rational checkpoint \(a=1/4\),

\[
m_1=\frac34,
\qquad
m_{12}=\frac3{64}.
\tag{L-105111.32}
\]

## 6. Finite anchors and a complete first manifest are insufficient

Let \(S\subset(0,\infty)\) be finite and define

\[
Q_S(z)=z^2\prod_{s\in S}(z^2-s^2),
\qquad
L_C(z)=z e^{-CQ_S(z)^2},
\tag{L-105111.33}
\]

for \(C>0\).  Let

\[
F_C(z)=
\exp\!\left(\int_0^zL_C(w)\,dw\right).
\tag{L-105111.34}
\]

Then \(F_C\) is real, even, entire, and zero-free.  Its derivative has
exactly the one global simple zero \(0\), with first-quotient residue one.
For every \(s\in S\),

\[
L_C(s)=s,
\qquad
L_C'(s)=1,
\qquad
A_C(s)=s^2+1.
\tag{L-105111.35}
\]

Thus the \(G_1\) and \(G_{12}\) anchor values are independent of \(C\).  At
every real \(\zeta\notin\{0,\pm S\}\),

\[
L_C(\zeta)\longrightarrow0,
\qquad
A_C(\zeta)\longrightarrow0.
\tag{L-105111.36}
\]

Indeed, if \(q=Q_S(\zeta)\ne0\) and \(q'=Q_S'(\zeta)\), then

\[
A_C(\zeta)
=e^{-Cq^2}
\left(
1-2C\zeta qq'
+\zeta^2e^{-Cq^2}
\right),
\tag{L-105111.37}
\]

which makes the polynomial-times-exponential collapse explicit.

For the exact fixture

\[
S=\{1/2,1\},
\qquad
E=[1/2,1],
\qquad
\zeta=3/4,
\tag{L-105111.38}
\]

one has

\[
Q_S(3/4)=-\frac{315}{4096},
\qquad
Q_S(3/4)^2=\frac{99225}{16777216},
\tag{L-105111.39}
\]

and the fixed endpoint data

\[
\begin{array}{c|cc}
z&1/2&1\\
\hline
G_1(z)&1/2&1\\
G_{12}(z)&5/8&2.
\end{array}
\tag{L-105111.40}
\]

Nevertheless both denominators at \(3/4\) collapse.  Hence finitely many
anchor values, the complete global first-event manifest, fixed target
residue, and first optimal selector norm one cannot replace a variation or
disk-tail certificate.

The second-derivative event manifest is not stable in this family and is not
claimed to be.

## 7. Boundary of the result

The theorem supplies two finite authentication formats for the absolute
quotient-margin branch.  It does not provide:

- Xi anchor values, \(F\)-zero-free cover disks, denominator holomorphy, or
  rigorous disk enclosures;
- cofinal bounds for \(D_L,D_{LA},V_L,V_{LA}\), \(F'''/F\), disk count, or
  minimum slack;
- absorption of Green--Gram selector growth or changing edge length;
- the L-105110 pole-subtracted remainder, corner, or principal-part ledger;
- a stable second manifest for the counterfamily;
- strict jet coherence, RCMV104530, or RH.

The family (L-105111.33) varies with \(C\), has infinite order, and is not an
Xi-class or fixed-function cofinal counterexample.

No novelty is claimed for logarithmic integration, the line-segment
derivative estimate, or disk-cover/Rouché reasoning.  The contribution is
their exact placement in the L-105109/L-105110 programme fork and the
denominator-specific identities through \(F'''/F\).

No L/T/R/M/X-105111 collision exists across the current tree or fetched
refs.  The closest antecedents are L/T-105109, which identify the missing
margins; L/T/R-105110, which develop the alternative cancellation route;
draft PR #720 L-104521, which reduces a limiting vertical flux to horizontal
argument variation without bounding this edge; and L-91009, which assumes an
upper zeta log-derivative bound for a different annular Pick problem.
Across-ref L-91810 and L-20001 contain classical completed-Xi
logarithmic-modulus identities, not reciprocal denominator margins or
finite-disk certificates.
