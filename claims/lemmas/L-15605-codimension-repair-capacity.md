# L-15605 — Codimension repair lower bound for radical capacity

Claim ID: `L-15605`  
Title: Imposing the exact source constraints costs only their finite codimension in any uniformly concentrated packet  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-09-d`  
Created: 2026-07-31  
Dependencies: rank--nullity; linearity of the source, localization, and residual maps; `L-15301/L-15303`  
Scope: lower bounds for `C(a,epsilon)`

## Abstract statement

Let `P` be a finite-dimensional source packet of dimension `p`.  Let

\[
 \ell_1,\ldots,\ell_r:P\to\mathbb C
 \tag{L-15605.1}
\]

be the exact linear source constraints required by the global arithmetic radical
map.  Put

\[
 P_0=\bigcap_{j=1}^r\ker\ell_j.
 \tag{L-15605.2}
\]

Then

\[
 \boxed{\dim P_0\ge p-r.}
 \tag{L-15605.3}
\]

Suppose linear maps

\[
 J:P\to H_a,
 \qquad
 T:P\to X_a
 \tag{L-15605.4}
\]

produce localized trial vectors and their discarded tails, and suppose every
`f in P` satisfies the uniform inequalities

\[
 \|Jf\|^2\ge g_a\|f\|^2,
 \qquad g_a>0,
 \tag{L-15605.5}
\]

\[
 |Q_a(Jf,Jg)|
 \le \alpha_a\|Jf\|\|Jg\|,
 \tag{L-15605.6}
\]

and

\[
 \|Q_a(Jf,\cdot)\|_{Y_a^*}
 \le\beta_a\|Jf\|.
 \tag{L-15605.7}
\]

If every `f in P_0` is an exact admissible radical source, then the localized
packet

\[
 L=J(P_0)
 \tag{L-15605.8}
\]

has dimension at least `p-r` and satisfies the same form and residual bounds.
Consequently

\[
 \boxed{C(a,\max\{\alpha_a,\beta_a\})\ge p-r.}
 \tag{L-15605.9}
\]

### Proof

The map

\[
 f\mapsto(\ell_1(f),\ldots,\ell_r(f))
\]

has rank at most `r`; rank--nullity proves (L-15605.3).  The lower norm bound
(L-15605.5) makes `J` injective, so `dim J(P_0)=dim P_0`.  The inequalities are
uniform on `P`, hence remain valid on the subspace `P_0`.  QED.

## Two-constraint Weil source

For the Connes--Consani even source space, the declared constraints are

\[
 f(0)=0,
 \qquad
 \widehat f(0)=\int f=0.
 \tag{L-15605.10}
\]

Therefore a `p`-dimensional uniformly concentrated packet always contains an
exact source packet of dimension at least

\[
 p-2.
 \tag{L-15605.11}
\]

Inside a self-dual Fourier sector, the two functionals agree:

\[
 \widehat f(0)=f(0).
 \tag{L-15605.12}
\]

Only one independent condition remains, and the guaranteed dimension is

\[
 p-1.
 \tag{L-15605.13}
\]

This recovers the fixed-rank construction of `L-15303` and makes its rank loss
explicit.

## Prolate pre-plunge application

Let `P=P(a,eta)` be the span of concentration eigenmodes whose time--frequency
leakage is at most `eta`.  Whenever the source-to-tail continuity estimate is
uniform on this whole packet, L-15605 gives

\[
 C(a,\varepsilon(a,\eta))
 \ge
 \#\{\chi_n(a)\ge1-\eta\}-r.
 \tag{L-15605.14}
\]

Thus a sufficient numerical dimension comparison is

\[
 D(a,t,\Gamma)+r
 \le
 \#\{\chi_n(a)\ge1-\eta\}.
 \tag{L-15605.15}
\]

The newest sharp pre-plunge estimates can supply the right-hand lower bound.
They do not supply the left-hand arithmetic low-index count or the uniform
Weil-form tail continuity, both of which remain separate proof gates.

## Growing-rank warning

For every fixed `p`, one may choose a support large enough that the first `p`
source modes have arbitrarily small tails.  This does **not** imply a single
cofinal estimate for a support-dependent rank `p=p(a)`.

A production theorem must give one uniform leakage/form estimate over the entire
packet used at that same support.  Diagonalizing first in `p` and then in `a`
does not prove the scalar capacity inequality when the count `D(a)` grows.

## Relation to L-15603

L-15605 supplies the capacity lower bound.  L-15603 shows that this capacity is
already a lower bound on the actual low spectral count.  To obtain the reverse
inequality, one must still prove the saturation/complement condition of
L-15604.  Dimension abundance alone cannot exclude an extra low mode.

## Proof boundary

- The rank loss `r` is exact elementary algebra.
- Uniform packet estimates are hypotheses, not consequences of fixed-mode
  convergence.
- Source-domain normalization, injectivity, and form continuity remain imported
  in the intended zeta application.
- This lemma does not prove cofinal capacity saturation or RH.
