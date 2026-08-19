# L-99600 — The compact SHARP Hall gate and the endpoint Radon--Nikodym cocycle are exact

Claim ID: `L-99600`  
Status: **PROVED EXACT / DIRECTED FINITE THEOREM**  
Created: 2026-08-20  
Frozen inputs: the SHARP target and row kernel of PRs #642 and #647  
RH status: **not assumed**

## 1. Compact target Hall

For `1 <= x < 67` and `1 <= t < 67`, put

\[
 A_t=\sum_{n\le t}\frac{\mu(n)}n,\qquad
 B_t=\sum_{n\le t}\frac{\mu(n)}{\sqrt n},
\]

and

\[
 H_t(x)=4\sqrt x\,A_t-3B_t.
\tag{L-99600.1}
\]

These are exactly the nested-neighbourhood SHARP Hall-prefix slacks used by the
compact root theorem.

On the active interval `t <= x <= 67`, `H_t` is affine in `sqrt(x)`. Hence its
minimum is attained at

\[
 x_t=
 \begin{cases}
 t,&A_t\ge0,\\
 67,&A_t<0.
 \end{cases}
\tag{L-99600.2}
\]

where `67` denotes the boundary value controlling the left limit when the
physical compact interval is half-open.

The replay computes every Möbius value through `66` exactly. Square roots and
inverse square roots are enclosed by integer-square-root intervals with
denominator \(2^{40}\); all signed products are rounded outward.

It proves

\[
\boxed{H_t(x)>\frac7{20}}
\qquad(1\le t<67,\ t\le x<67).
\tag{L-99600.3}
\]

The unique infimum is the state

\[
(t,x)=(13,67^-),
\]

with directed boundary enclosure

\[
\boxed{
0.359317660596810
<
H_{13}(67)
<
0.359317660601486.
}
\tag{L-99600.4}
\]

Thus the compact target Hall flow exists with a strict moat exceeding

\[
0.009317660596810
\]

above `7/20`. This finite gate no longer needs to be imported as an opaque
heavy campaign.

## 2. Exact SHARP endpoint source

Put

\[
 T(y)=(4\sqrt y-3)\mathbf1_{y\ge1}.
\]

For a fixed row \(j\), PR #642 gives the positive source measure

\[
 dM_Y^{(j)}(t)
 =
 \mathbf1_{t\le Y}T(Y/t)\kappa_j(t)\frac{dt}{t},
 \qquad \kappa_j(t)>0.
\tag{L-99600.5}
\]

For `1 <= Z <= Y`, define

\[
 R_{Z\mid Y}(t)
 =
 \mathbf1_{t\le Z}\frac{T(Z/t)}{T(Y/t)}.
\tag{L-99600.6}
\]

Then

\[
\boxed{dM_Z^{(j)}=R_{Z\mid Y}\,dM_Y^{(j)}},
\qquad 0\le R_{Z\mid Y}\le1.
\tag{L-99600.7}
\]

A raw support cutoff is not the child map. At `(Y,Z,t)=(16,4,4)`,

\[
T(Y/t)=5,\qquad T(Z/t)=1,
\qquad R_{4\mid16}(4)=\frac15.
\tag{L-99600.8}
\]

## 3. Projective cocycle

For `1 <= W <= Z <= Y`, the exact densities satisfy

\[
\boxed{
R_{W\mid Z}(t)R_{Z\mid Y}(t)
=
R_{W\mid Y}(t)
}
\tag{L-99600.9}
\]

on the support of \(M_Y^{(j)}\), with the standard zero convention outside the
child supports. Indeed, the middle target factor cancels:

\[
\frac{T(W/t)}{T(Z/t)}
\frac{T(Z/t)}{T(Y/t)}
=
\frac{T(W/t)}{T(Y/t)}.
\]

Thus endpoint restriction is functorial through arbitrarily many generations.
The same physical micro-source can be followed down the full source DAG
without changing its accumulated density according to the chosen subdivision.

## 4. Consequence and boundary

The following interfaces are closed:

```text
compact SHARP Hall prefix inequalities   exact finite theorem
worst compact state                       t=13, x=67-
same-index child domination              exact RN derivative
multigeneration endpoint consistency     exact RN cocycle
raw support cutoff                       false / replaced
```

This theorem does not identify the contracted `alpha`-child operator with the
native rough Euler source. That separate coefficient issue is addressed by
`R-99600` and `L-99601`.
