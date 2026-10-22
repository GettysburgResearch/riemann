# L-105106 — Primary-cardinal selector conditioning

Claim ID: L-105106

Status: **PROPOSED EXACT FINITE-WINDOW REDUCTION**

Created: 2026-08-23

Depends on: L-105103; L-105105

RH status: **unproved**

## 1. Top-primary data

Let \(\Omega\) be a bounded regular domain and let \(h\) be meromorphic on
a neighbourhood of \(\overline\Omega\).  Its complete actual-pole manifest is

\[
\mathcal S=\{(a,d_a):a\in S,\ d_a\ge1\},
\qquad
M(z)=\prod_{a\in S}(z-a)^{d_a},
\qquad
D=\sum_{a\in S}d_a.
\tag{L-105106.1}
\]

Thus \(G=Mh\) is holomorphic on a neighbourhood of
\(\overline\Omega\).  Let \(\mathcal T\subseteq S\) be a target set and
prescribe only the top local primary coefficient

\[
W(z)\equiv \gamma_c(z-c)^{d_c-1}
 \pmod{(z-c)^{d_c}}
\quad(c\in\mathcal T),
\tag{L-105106.2}
\]

with the zero congruence modulo \((z-a)^{d_a}\) at every nontarget
\(a\in S\setminus\mathcal T\).  Put

\[
M_c(z)=\frac{M(z)}{(z-c)^{d_c}}.
\tag{L-105106.3}
\]

The word *actual* in (L-105106.1) is load-bearing: the orders are the
post-cancellation orders supplied by L-105103, not the raw orders of a
denominator product.

## 2. Closed primary-cardinal formula

The unique representative of degree less than \(D\) is

\[
\boxed{
W(z)=\sum_{c\in\mathcal T}
 \gamma_c(z-c)^{d_c-1}\frac{M_c(z)}{M_c(c)}.
}
\tag{L-105106.4}
\]

Indeed, the \(c\)-summand has the desired top coefficient because
\(M_c(z)/M_c(c)=1+O(z-c)\).  Every other summand contains the full primary
factor \((z-c)^{d_c}\).  Each summand has degree at most \(D-1\), and primary
CRT gives uniqueness below degree \(D\).

For the L-105105 first selector, use its actual \(F/F'\) pole support and

\[
d_{1,c}=r_c,\qquad \gamma_{1,c}=1.
\tag{L-105106.5}
\]

For the second selector, use the actual \(F^2/(F'F'')\) pole support and

\[
d_{2,c}=2r_c-1,\qquad \gamma_{2,c}=r_c.
\tag{L-105106.6}
\]

These equalities hold at every L-105105 target because it is noncommon and
\(r_c\) is odd.  In particular, the selectors needed there are top-primary
data; no confluent Vandermonde inversion or lower-jet Taylor recurrence is
needed.

## 3. Exact conditioning ledger

Define the primary-cardinal condition numbers

\[
\kappa_c=|M_c(c)|^{-1}
=\prod_{a\ne c}|c-a|^{-d_a},
\qquad
\Lambda=\sum_{c\in\mathcal T}|\gamma_c|\kappa_c.
\tag{L-105106.7}
\]

Formula (L-105106.4) gives the pointwise envelope

\[
|W(z)|\le
\sum_{c\in\mathcal T}|\gamma_c|\,|z-c|^{d_c-1}
\prod_{a\ne c}
\left(\frac{|z-a|}{|c-a|}\right)^{d_a}.
\tag{L-105106.8}
\]

Fix a centre \(z_0\).  If all nodes satisfy \(|a-z_0|\le R\) and the set on
which the selector is measured satisfies \(|z-z_0|\le B\), then

\[
\boxed{
\|W\|_\infty\le(B+R)^{D-1}\Lambda.
}
\tag{L-105106.9}
\]

Writing \(W(z_0+\zeta)=\sum_kw_k\zeta^k\), the same proof in the weighted
coefficient norm gives the stronger algebraic statement

\[
\sum_k|w_k|B^k\le(B+R)^{D-1}\Lambda.
\tag{L-105106.10}
\]

Consequently \(|w_k|\le B^{-k}(B+R)^{D-1}\Lambda\) for \(B>0\).  If the
pairwise node separation is at least \(\delta>0\), then

\[
\kappa_c\le\delta^{-(D-d_c)}.
\tag{L-105106.11}
\]

The exact products in (L-105106.7) are normally sharper than replacing all
distances by \(\delta\).  The leading coefficient is also explicit:

\[
[z^{D-1}]W=\sum_{c\in\mathcal T}\frac{\gamma_c}{M_c(c)}.
\tag{L-105106.12}
\]

Thus the degree \(D-1\) is attained unless this signed barycentric sum
cancels.

## 4. Pole-cancelled weighted-edge reduction

Dividing (L-105106.4) by the complete primary modulus collapses every
confluent factor:

\[
\boxed{
\frac{W(z)}{M(z)}
=\sum_{c\in\mathcal T}
\frac{\gamma_c}{M_c(c)(z-c)}.
}
\tag{L-105106.13}
\]

Let \(E\) be an oriented boundary edge and
\(\eta_{E,c}=\operatorname{dist}(E,c)>0\).  Since \(Wh=(W/M)G\),

\[
\boxed{
\left|\frac1{2\pi i}\int_EW(z)h(z)\,dz\right|
\le
\frac{\operatorname{len}(E)}{2\pi}\,
\|G\|_E
\sum_{c\in\mathcal T}
\frac{|\gamma_c|\kappa_c}{\eta_{E,c}}.
}
\tag{L-105106.14}
\]

Only a first power of the target-to-edge distance remains after exact pole
cancellation.  For L-105105, take

\[
(h,G,M)=(F/F',\ M_1F/F',\ M_1)
\quad\hbox{or}\quad
(F^2/(F'F''),\ M_2F^2/(F'F''),\ M_2).
\tag{L-105106.15}
\]

This is an exact finite-window edge envelope, not an estimate of either
holomorphic factor in (L-105106.15).

## 5. Reality, parity, and degree drop

Conjugation-compatible manifests and data force real coefficients by
uniqueness.  On a sign-stable manifest an even selector is forced when

\[
\gamma_{-c}=(-1)^{d_c-1}\gamma_c.
\tag{L-105106.16}
\]

Both L-105105 target powers are even, so sign stability forces its selectors
to be even without averaging or norm loss; conjugation compatibility
separately forces their coefficients to be real.  If \(D\) is even, evenness
forces the nominal degree-\(D-1\) coefficient to vanish and improves the
degree to at most \(D-2\).  The exact four-edge and parity identities of
L-105101 and L-105102 therefore remain available after weighting.

## 6. Sharp conditioning obstruction

Completeness and symmetry do not make the envelope uniform.  In the disk
\(|z|<B\), take target \(0\) of order one and nontargets \(\pm i\varepsilon\),
each of order \(m\).  The unique reduced selector is real and even:

\[
W_{m,\varepsilon}(z)
=\left(1+\frac{z^2}{\varepsilon^2}\right)^m,
\qquad D=2m+1.
\tag{L-105106.17}
\]

It satisfies

\[
\|W_{m,\varepsilon}\|_{|z|=B}
=\left(1+\frac{B^2}{\varepsilon^2}\right)^m.
\tag{L-105106.18}
\]

Moreover every function holomorphic on the disk, continuous on its closure,
equal to one at zero, and vanishing to order \(m\) at both nontargets obeys

\[
\|W\|_{|z|=B}\ge\left(\frac B\varepsilon\right)^{2m}.
\tag{L-105106.19}
\]

To prove (L-105106.19), divide by the two disk Blaschke factors, each raised
to order \(m\), and apply the maximum principle at zero.  Hence allowing a
higher-degree polynomial—or any other holomorphic selector—does not remove
the coalescence loss.  The exponent \(D-1\), reality, and even parity are all
simultaneously sharp.

The family is realized by the first L-105105 quotient after taking
\(F'(z)=z(z^2+\varepsilon^2)^m\) and a generic real integration constant.
The only real derivative zero is the simple target at zero; the clustered
nontargets are nonreal.

For both quotients at once, the elementary family

\[
F_\varepsilon(z)=1+\frac{\varepsilon^2z^2}{2}+\frac{z^4}{4}
\tag{L-105106.20}
\]

has target \(0\), first selector
\(1+z^2/\varepsilon^2\), and second selector

\[
\left(1+\frac{z^2}{\varepsilon^2}\right)
\left(1+\frac{3z^2}{\varepsilon^2}\right).
\tag{L-105106.21}
\]

Their unit-circle norms are respectively
\(1+\varepsilon^{-2}\) and
\((1+\varepsilon^{-2})(1+3\varepsilon^{-2})\); Blaschke gives lower bounds
\(\varepsilon^{-2}\) and \(3\varepsilon^{-4}\).

## 7. Exact boundary of the result

Equations (L-105106.4), (L-105106.9)--(L-105106.14) close the exact
finite-window degree, coefficient, conditioning, and pole-cancelled edge
reduction.  They do **not** provide:

- a complete Xi pole manifest on cofinal windows;
- cofinal bounds for \(D_\nu\), \(M_{\nu,c}(c)^{-1}\), or node separation;
- target-to-boundary distance bounds;
- estimates for \(M_1F/F'\) or \(M_2F^2/(F'F'')\) on the four edges;
- weighted-edge decay, a cofinal limit, or a strict jet-coherence margin;
- RCMV104530 or RH.

In particular, the unweighted fixed-ladder edge estimates in draft PR #720
do not survive multiplication by a growing selector as a formal matter.
The moving-order Vandermonde claim L-92302 is marked `GAP_BLOCKED` and
`QUARANTINE` in the integrated registry and is not used here.

No novelty is claimed for primary CRT, cardinal polynomials, or the Blaschke
bound.  The new contribution is their exact top-jet specialization to the
L-105105 residue bridge, the pole-cancelled edge formula, and the explicit
cofinal-conditioning firewall.
