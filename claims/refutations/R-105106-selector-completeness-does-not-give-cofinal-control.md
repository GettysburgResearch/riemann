# R-105106 — Selector completeness does not give cofinal control

Claim ID: R-105106

Status: **PROPOSED EXACT REFUTATION**

Created: 2026-08-23

Depends on: L-105105; L-105106

RH status: **unproved**

## Refuted inference

The following implication is false:

> A complete finite-window CRT manifest, together with real/even symmetry,
> gives selector bounds uniform enough for a cofinal weighted-edge limit.

## Symmetric exact obstruction

In \(|z|<B\), put a simple target at zero and nontarget primary nodes
\(\pm i\varepsilon\), each of order \(m\).  The unique reduced selector is

\[
W_{m,\varepsilon}(z)
=\left(1+\frac{z^2}{\varepsilon^2}\right)^m.
\tag{R-105106.1}
\]

It is real and even, yet

\[
\deg W_{m,\varepsilon}=2m=D-1,
\qquad
\|W_{m,\varepsilon}\|_{|z|=B}
=\left(1+\frac{B^2}{\varepsilon^2}\right)^m.
\tag{R-105106.2}
\]

Every holomorphic selector satisfying the same zeros and value at zero obeys

\[
\|W\|_{|z|=B}\ge(B/\varepsilon)^{2m}
\tag{R-105106.3}
\]

by finite Blaschke factorization.  Higher polynomial degree cannot repair the
conditioning.

The family \(F'(z)=z(z^2+\varepsilon^2)^m\), with a generic real integration
constant, realizes this as the first L-105105 selector: zero is the only real
target and the clustered events are nonreal nontargets.

## Simultaneous first/second obstruction

For

\[
F_\varepsilon(z)=1+\varepsilon^2z^2/2+z^4/4,
\]

all denominator events are simple, the target set is \(\{0\}\), and

\[
W_1=1+z^2/\varepsilon^2,
\qquad
W_2=(1+z^2/\varepsilon^2)(1+3z^2/\varepsilon^2).
\tag{R-105106.4}
\]

At \(\varepsilon=1/5\), their exact unit-circle norms are \(26\) and
\(1976\), while the all-holomorphic Blaschke lower bounds are \(25\) and
\(1875\).  The selectors are therefore asymptotically sharp as the events
coalesce.

## Edge remainder obstruction

Pole data also do not control the pole-cancelled holomorphic factor.  The
family

\[
h_C(z)=1/z+C,
\qquad M(z)=z,
\qquad M(z)h_C(z)=1+Cz
\tag{R-105106.5}
\]

has identical pole and principal-part data for every \(C\), while its
boundary norm is unbounded.  Closed-contour charges stay fixed because the
added term is holomorphic, but large individual edge contributions can
cancel.  A closed residue identity is not an individual-edge estimate.

## Consequence

An Xi continuation must control the exact barycentric products
\(|M_{\nu,c}(c)|^{-1}\), target-to-boundary distance, and the normalized
holomorphic factors \(M_1F/F'\) and \(M_2F^2/(F'F'')\).  Completeness,
multiplicity labels, and parity alone do not supply those bounds.  The
unweighted fixed-ladder decay in draft PR #720 cannot be multiplied by a
growing selector without a new proof.
