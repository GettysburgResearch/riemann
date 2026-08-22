# L-105105 — Fixed-window CRT jet selectors

Claim ID: L-105105

Status: **PROPOSED EXACT HOLOMORPHIC WINDOW IDENTITY; review pending**

Created: 2026-08-23

Depends on: L-105103; L-105104

RH status: **not assumed**

## 1. Actual pole manifest

Let \(F\) be holomorphic on a neighborhood of the closure of a bounded
regular domain \(\Omega\), with \(F'\) and \(F''\) not identically zero and
with no zero of \(F'F''\) on \(\partial\Omega\). At every point in the finite
interior denominator support write

\[
F=w^mU,\qquad F'=w^rV,\qquad F''=w^sW,
\qquad U(0)V(0)W(0)\ne0.
\]

For

\[
P=\frac F{F'},\qquad Q=\frac{F^2}{F'F''},
\]

the actual pole orders are

\[
d_1(a)=(r_a-m_a)_+,
\qquad
d_2(a)=(r_a+s_a-2m_a)_+.
\tag{L-105105.1}
\]

Thus removable common events are not assigned artificial selector debt, and
an \(F''\)-only pole is retained in the second manifest.

Let \(\mathcal T\) be the complete finite set of real, noncommon, odd-order
zeros of \(F'\) in \(\Omega\). For \(c\in\mathcal T\), put

\[
r_c=\operatorname{ord}_cF',\qquad
\rho_c^{\rm jet}=\frac{r_c!F(c)}{F^{(r_c+1)}(c)}.
\tag{L-105105.2}
\]

For this finite target set define the window charges

\[
A_{\rm jet}(\mathcal T)
=-\sum_{c\in\mathcal T}\rho_c^{\rm jet},
\qquad
B_{\rm jet}(\mathcal T)
=\sum_{c\in\mathcal T}(\rho_c^{\rm jet})^2.
\tag{L-105105.2a}
\]

When \(F\) is real analytic on the real interval cut out by the window,
these are exactly the corresponding L-105104 jet charges.

At such a point \(m=0\), \(s=r-1\), \(d_1=r\), and \(d_2=2r-1\).

## 2. Selector congruences

There is a polynomial \(W_1\) satisfying, at every actual \(P\)-pole,

\[
W_1(z)\equiv
\begin{cases}
(z-c)^{r_c-1}\pmod{(z-c)^{r_c}},&c\in\mathcal T,\\
0\pmod{(z-a)^{d_1(a)}},&a\notin\mathcal T.
\end{cases}
\tag{L-105105.3}
\]

There is a polynomial \(W_2\) satisfying, at every actual \(Q\)-pole,

\[
W_2(z)\equiv
\begin{cases}
r_c(z-c)^{2r_c-2}
 \pmod{(z-c)^{2r_c-1}},&c\in\mathcal T,\\
0\pmod{(z-a)^{d_2(a)}},&a\notin\mathcal T.
\end{cases}
\tag{L-105105.4}
\]

The primary moduli at distinct support points are coprime. The finite
Chinese remainder theorem therefore gives both selectors. Each has a unique
representative of degree below the degree of its full primary modulus.

The factor \(r_c\) in (L-105105.4) is load bearing. L-105104 gives the
leading coefficient of \(Q\) as \((\rho_c^{\rm jet})^2/r_c\).

## 3. Exact weighted charges

At a target point, (L-105105.3) kills every Laurent term except the leading
\(w^{-r_c}\) coefficient of \(P\), moving it to residue degree. At every
nontarget pole it cancels the full actual pole. Hence

\[
\operatorname{Res}_c(W_1P)=\rho_c^{\rm jet}\qquad(c\in\mathcal T),
\qquad
\operatorname{Res}_a(W_1P)=0\quad(a\notin\mathcal T).
\tag{L-105105.5}
\]

Similarly,

\[
\operatorname{Res}_c(W_2Q)=(\rho_c^{\rm jet})^2,
\qquad
\operatorname{Res}_a(W_2Q)=0\quad(a\notin\mathcal T).
\tag{L-105105.6}
\]

The residue theorem now yields the exact fixed-window bridge

\[
\boxed{
\frac1{2\pi i}\int_{\partial\Omega}W_1(z)\frac{F(z)}{F'(z)}\,dz
=\sum_{c\in\mathcal T}\rho_c^{\rm jet}
=-A_{\rm jet}(\mathcal T),
}
\tag{L-105105.7}
\]

\[
\boxed{
\frac1{2\pi i}\int_{\partial\Omega}W_2(z)
\frac{F(z)^2}{F'(z)F''(z)}\,dz
=\sum_{c\in\mathcal T}(\rho_c^{\rm jet})^2
=B_{\rm jet}(\mathcal T).
}
\tag{L-105105.8}
\]

These are new weighted charges. They are not the unweighted \(\Phi_1,B\) of
L-105101--L-105103.

If \(F\), the domain, and the full event manifest are conjugation stable and
\(\mathcal T\) is real, the reduced selectors have real coefficients. If, in
addition, the domain, event manifest, and complete target set are stable
under \(z\mapsto-z\), the even local target exponents make both congruence
systems sign-stable. The reduced selectors may then be taken even, so the
weighted quotients retain the odd parity needed by the Xi edge reduction.

## 4. Root-free polynomial corollary

For \(f\in K[z]\) with \(\deg f\ge2\) over a characteristic-zero field,
write the unique
square-free multiplicity decomposition

\[
f'=\kappa\prod_{r\ge1}A_r^r,
\]

where the nonconstant \(A_r\) are monic, square-free, and pairwise coprime.
Put

\[
D_r=\frac{f'}{A_r^r}(A_r')^r.
\]

Then \(D_r\) is a unit modulo \(A_r\). For
\(S_{\rm odd}=\prod_{r\ \mathrm{odd}}A_r\), CRT gives a unique reduced \(R\)
such that

\[
R\equiv fD_r^{-1}\pmod{A_r},
\qquad r\text{ odd},
\tag{L-105105.9}
\]

For every root \(c\) of \(A_r\) in an algebraic closure, define the algebraic
leading carrier

\[
\widetilde\rho_{r,c}=\frac{r!f(c)}{f^{(r+1)}(c)}.
\]

It equals \(\rho_c^{\rm jet}\) at an eligible real turn and is zero at a
common root. Put \(H\equiv R^2\pmod{S_{\rm odd}}\). Then at every root of an
odd stratum,

\[
R(c)=\widetilde\rho_{r,c},\qquad
H(c)=\widetilde\rho_{r,c}^{\,2}.
\]

Consequently \(RS_{\rm odd}'/S_{\rm odd}\) and
\(HS_{\rm odd}'/S_{\rm odd}\) are coefficient-level all-root jet encoders.
Common roots contribute zero and even strata are absent. This corollary uses
only polynomial gcd, inversion, and CRT; it does not find roots.

The all-root traces are not automatically real-window moments. An
irreducible factor may mix real and nonreal embeddings, so localization or
explicit nonreal correction is still required before using this corollary as
a window estimate.

## 5. Scope

For \(F=\Xi^{(k-1)}\), (L-105105.7)--(L-105105.8) prove exact selector
existence on every regular finite window **conditional on the complete event
manifest**. They do not construct that manifest, control selector degree or
boundary norm, estimate the weighted edges, pass to cofinal windows, prove a
jet-coherence margin, establish RCMV104530, or prove RH.
