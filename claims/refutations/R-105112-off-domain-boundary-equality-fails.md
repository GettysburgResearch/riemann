# R-105112 — Off-selector-domain-boundary equality fails

Claim ID: R-105112

Status: **PROPOSED EXACT REFUTATION / ERRATUM FIXTURE**

Created: 2026-08-23

Depends on: L-105107; L-105109; L-105112

RH status: **unproved**

## Refuted inference

The following literal domain-free inference is false:

> If \(W_*\) is an optimal selector of norm \(\tau\) and \(E\) is a boundary
> arc of some region on which the quotient is regular, then
> \(\|W_*F/F'\|_E=\tau/m_1(E)\), regardless of whether \(E\) belongs to the
> boundary of the domain used to construct \(W_*\).

“Off-selector-domain-boundary” includes an interior curve that happens to be
the boundary of a smaller region.  It does not mean that the curve must lie
outside the selector domain.

## Exact counterexample

Let

\[
\Omega=\mathbb D,
\qquad
F(z)=e^{z^4/4},
\qquad
\frac{F'}F=z^3.
\tag{R-105112.1}
\]

The complete first manifest in \(\mathbb D\) is the single order-three
target at zero, with principal coefficient one for \(F/F'=z^{-3}\).
The exact L-105107 optimum is

\[
W_*(z)=z^2,
\qquad
\tau=1.
\tag{R-105112.2}
\]

Indeed any admissible selector is \(z^2H\) with \(H(0)=1\); on the unit
circle its norm is at least one, and \(z^2\) attains one.

Let

\[
E_{1/2}=\left\{\frac12e^{it}:0\le t\le\pi\right\}.
\tag{R-105112.3}
\]

This is the upper boundary semicircle of the radius-\(1/2\) disk, but it is
not a subset of \(\partial\Omega\).  Since

\[
F'=z^3F,
\qquad
F''=z^2(z^4+3)F,
\tag{R-105112.4}
\]

all of \(F,F',F''\) are nonzero on \(E_{1/2}\); in particular
\(|z^4+3|\ge47/16\).  Moreover

\[
m_1(E_{1/2})=\frac18,
\qquad
\|W_*\|_{E_{1/2}}=\frac14,
\tag{R-105112.5}
\]

and

\[
W_*\frac F{F'}=\frac1z.
\tag{R-105112.6}
\]

Therefore

\[
\boxed{
\left\|W_*\frac F{F'}\right\|_{E_{1/2}}=2
\ne
8=\frac\tau{m_1(E_{1/2})}.
}
\tag{R-105112.7}
\]

The repaired inequality uses the actual edge norm and is exact:

\[
2=\frac{\|W_*\|_{E_{1/2}}}{m_1(E_{1/2})}.
\tag{R-105112.8}
\]

On the unit upper semicircle \(E_1\subset\partial\Omega\), one instead has
\(m_1(E_1)=1\), \(|W_*|=\tau=1\), and

\[
\left\|W_*F/F'\right\|_{E_1}=1=\frac\tau{m_1(E_1)}.
\tag{R-105112.9}
\]

## What is not refuted

The counterexample does not refute the same-selector-domain equality.  It
also does not refute the actual T-105109 unit-circle obstruction, whose
relevant edges lie on the boundary of its unit-disk selector domain.  It
refutes only the unqualified transport of the scalar \(\tau\) to another
boundary or interior curve.

This packet does not modify or retrospectively verify the frozen T-105109
artifacts.  No Xi, cofinal, RCMV104530, or RH conclusion follows.
