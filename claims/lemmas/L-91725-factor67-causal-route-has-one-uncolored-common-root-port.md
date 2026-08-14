# L-91725 — The factor-67 causal route has one uncolored common root port

Claim ID: `L-91725`  
Status: **PROVED EXACT POSITIVE-LINEAR PORT THEOREM ON FROZEN FIBER INPUTS**  
Created: 2026-08-14  
Inputs: the uncolored matrix-port inequality of `L-91320`, complete physical causal generators `L-91654`, positive endpoint integration `L-91674`, fixed-window mass bound `L-91689`  
Replay: `X-91725-factor67-common-uncolored-port`  
RH status: **unproved**

## 1. Scope correction from the older colored route

`L-91320` proves the matrix inequality

\[
 \mathcal P_x=
 \begin{pmatrix}
  \mathcal V_x&\mathcal B_x\\
  \mathcal B_x&\mathcal V_x
 \end{pmatrix}
 \succeq\frac19\mathcal V_x I_2
\tag{L-91725.1}
\]

and the normalized port-mass bound

\[
 m_{\rm port}<\frac{14}{3}.
\tag{L-91725.2}
\]

That theorem also constructs a colored affine Pascal lift and explicitly leaves
the later colored-to-physical projection open.

The factor-67 SONTR route does not need that projection.  Its rough current
difference is the complete **physical** endpoint datum of `L-91654`:

```text
component rows are physical rows;
ordinary and radix-four responses are physical columns;
the causal generator has zero finite-boundary reserve;
all collar, mismatch, omission and common-port data stay in the root current
packet.
```

The present theorem imports only the uncolored root matrix port
(L-91725.1), not the colored affine lift.

## 2. Abstract one-port fiber ledger

Let `(S,mu)` be a finite positive endpoint space.  For every fiber `s`, let

\[
 P_s\in\mathbb S_+^2
\]

be its available root port and let

\[
 D_s\in\mathbb S_+^2,\qquad D_s\preceq P_s
\tag{L-91725.3}
\]

be the complete current correction demand after the fiber's Hall operation.

Let `b_s>=0` be the current coefficient retained by the source-owned
current/child split.  Every recursive child has port coordinate zero, as in
`L-91654`.

Define the common parent port and demand only after the positive sum:

\[
 P=\int_S b_sP_s\,d\mu(s),
 \qquad
 D=\int_S b_sD_s\,d\mu(s).
\tag{L-91725.4}
\]

Since the positive-semidefinite cone is closed under positive integration,

\[
 \boxed{
 0\preceq D\preceq P.
 }
\tag{L-91725.5}
\]

This is one parent port inequality.  No fiber and no rough owner is tested
against an independent copy of the full port.

## 3. Current/child source ownership

At each root fiber the causal identity has the form

\[
 P_s^{\rm src}
 =P_s^{\rm cur}
 +\sum_i\alpha_i(s)U_{p_i}P_{s,i}^{\rm child}.
\tag{L-91725.6}
\]

The target/row/ordinary/detail data of the child are carried by the same-index
physical functor.  Its boundary/port coordinate is zero.  Therefore the
complete port coordinate of (L-91725.6) is simply

\[
 \operatorname{Port}(P_s^{\rm src})
 =\operatorname{Port}(P_s^{\rm cur}).
\tag{L-91725.7}
\]

The row bonuses from root Hall are also current.  Thus the root port has
exactly one owner before integration.

## 4. One global thinning and one global correction

Let `0<=tau<=1` be any source-owned safety thinning applied once to the complete
labelled parent measure.  Then

\[
 \tau D\preceq\tau P.
\tag{L-91725.8}
\]

All endpoint fibers, Hall bonuses and causal current packets are summed before
the single global quantizer and before the port inequality is tested.
A fixed collar, finite mismatch, terminal omission, taper or finite-base
correction is inserted once into the aggregate current demand.  It is not
inserted into each child or into each endpoint color.

Hence neither the all-column thinning of `L-91723` nor the knot-collar omission
of `L-91724` creates a second port:

```text
square-root thinning scales the available port and its linear demand once;
activation collars remove positive parent source before the split;
barycentric endpoint weights sum to one;
recursive children retain zero port.
```

## 5. Uniform integrated port mass

On the factor-67 root window, the unsigned root certificate mass is at most
`54` by `L-91689`.  The normalized port mass per unit root packet is below
`14/3` by (L-91725.2).  Positive integration therefore gives

\[
 \boxed{
 m_{\rm port}^{\rm root}
 <54\cdot\frac{14}{3}=252.
 }
\tag{L-91725.9}
\]

The common port is uniformly bounded independently of `X`.

## 6. Why no colored-to-physical projection remains

The only operation which forgets endpoint labels is the positive common-parent
sum in (L-91725.4).  Physical row and response coordinates have already been
formed by `L-91654` before this sum.  The port is a separate additive matrix
coordinate and is not projected into a physical radix-four column.

Consequently:

\[
 \boxed{
 \text{the open colored-capacity projection of `L-91320` is not an input to
 the factor-67 causal route.}
 }
\tag{L-91725.10}
\]

Any proposal which instead uses the colored affine Pascal lift still inherits
the old open projection.  This theorem applies only to the physical causal
generator route.

## 7. Boundary

```text
uncolored P61 matrix-port inequality                 imported exact
positive endpoint integration of port inequalities  exact
recursive child port                                 exactly zero
one parent port after Hall and rough grouping        exact
uniform integrated port mass                         <252
old colored-to-physical projection                   not used by this route
analytic construction of each frozen correction      separate review input
Riemann Hypothesis                                   unproved
```
