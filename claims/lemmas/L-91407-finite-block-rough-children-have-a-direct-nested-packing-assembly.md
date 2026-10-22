# L-91407 — Finite-block rough children have a direct nested physical packing assembly

Claim ID: `L-91407`  
Status: **PROVED ABSTRACT IDENTITY-ASSEMBLY THEOREM — FINITE FORCING NORMALIZATION STILL REQUIRES REPLAY**  
Created: 2026-08-13  
Frozen source partition: PR `#399` at `e210d06a588b191f102345ec75f2a0efce1b1650` (`L-91404`)  
Frozen capacity theorem: PR `#424` at `20b6cc5c4b9d4c9191a83e1f7fcf24c73dd7e7bb` (`L-91559`)  
Depends on: positive source disjointness; literal component-row/capacity maps; packet-envelope loss homogeneity and subadditivity  
RH status: **unproved**

## 1. Positive packet decomposition

Let a positive parent packet at endpoint `X` have an exact source-disjoint
decomposition

\[
 \boxed{
 P_X=F_X^{\rm fin}+\sum_b P_b,
 }
 \tag{L-91407.1}
\]

where each child packet `P_b` is evaluated at an endpoint

\[
 1\le Y_b\le X.
 \tag{L-91407.2}
\]

For the finite-block expansion of `L-91404`, one has the stronger contraction

\[
 Y_b\le X/59<c_0X
 \tag{L-91407.3}
\]

and an additive mass equality

\[
 m(F_X^{\rm fin})+\sum_bm(P_b)=m(P_X).
 \tag{L-91407.4}
\]

No affine row map is used below.

## 2. Canonical literal rows and capacities

For a positive packet `P` and endpoint `Z`, write

\[
 R_Z(P)\ge0
 \tag{L-91407.5}
\]

for its canonical positive component row.  Let

\[
 C_Z(P;q),
 \qquad
 \Theta_Z(P;q)
 \tag{L-91407.6}
\]

be its literal ordinary and radix-four detail responses.  These maps are
positive and additive in `P`.

The source-measure form of `L-91559` gives, whenever `Y<=X`,

\[
 \boxed{
 R_X(P)-R_Y(P)\ge0,
 }
 \tag{L-91407.7}
\]

and the exact response identities

\[
 \boxed{
 C_{R_X(P)-R_Y(P)}(q)
 =C_X(P;q)-C_Y(P;q),
 }
 \tag{L-91407.8}
\]

\[
 \boxed{
 \mathcal D_4C_{R_X(P)-R_Y(P)}(q)
 =\Theta_X(P;q)-\Theta_Y(P;q)\ge0.
 }
 \tag{L-91407.9}
\]

Thus the child row already lies in the parent row space; the unused parent
capacity is represented by the positive row difference.

## 3. Identity embedding of arbitrary child packings

Suppose `d_b>=0` is any feasible packing for child `P_b` at endpoint `Y_b`:

\[
 C_{d_b}(q)\le C_{Y_b}(P_b;q),
 \tag{L-91407.10}
\]

\[
 \mathcal D_4C_{d_b}(q)
 \le\Theta_{Y_b}(P_b;q)
 \qquad(q\ge2).
 \tag{L-91407.11}
\]

Define its parent replacement by

\[
 \boxed{
 \widehat d_b
 =R_X(P_b)-R_{Y_b}(P_b)+d_b.
 }
 \tag{L-91407.12}
\]

Equation (L-91407.7) gives `widehat d_b>=0`.  Equations
(L-91407.8)--(L-91407.11) give

\[
 \boxed{
 C_{\widehat d_b}(q)
 \le C_X(P_b;q),
 }
 \tag{L-91407.13}
\]

\[
 \boxed{
 \mathcal D_4C_{\widehat d_b}(q)
 \le\Theta_X(P_b;q).
 }
 \tag{L-91407.14}
\]

This is an exact identity embedding.  Row indices and coefficients of `d_b` are
unchanged, so no matched/unmatched affine fiber exists.

## 4. Assembly with the finite forcing packet

Let `d_fin>=0` be a feasible packing for the complete finite forcing packet at
the parent endpoint:

\[
 C_{d_{\rm fin}}(q)
 \le C_X(F_X^{\rm fin};q),
 \tag{L-91407.15}
\]

\[
 \mathcal D_4C_{d_{\rm fin}}(q)
 \le\Theta_X(F_X^{\rm fin};q).
 \tag{L-91407.16}
\]

Put

\[
 \boxed{
 d_X=d_{\rm fin}+\sum_b\widehat d_b.
 }
 \tag{L-91407.17}
\]

Every term is nonnegative.  By source disjointness and additivity,

\[
 C_X(P_X;q)
 =C_X(F_X^{\rm fin};q)+\sum_bC_X(P_b;q),
 \tag{L-91407.18}
\]

and the identical equality holds for `Theta`.  Hence

\[
 \boxed{
 C_{d_X}(q)\le C_X(P_X;q),
 }
 \tag{L-91407.19}
\]

\[
 \boxed{
 \mathcal D_4C_{d_X}(q)\le\Theta_X(P_X;q).
 }
 \tag{L-91407.20}
\]

The parent target is spent exactly once.  No child packing is dilated and no
global sum-before-quantize assertion is needed for recursive children.

## 5. Exact score ledger

Let

\[
 \mathcal E_Z(P)=\mathcal S(R_Z(P))
 \tag{L-91407.21}
\]

be the literal canonical component-row score.  Linearity gives

\[
 \boxed{
 \mathcal S(\widehat d_b)
 =\mathcal E_X(P_b)-\mathcal E_{Y_b}(P_b)
  +\mathcal S(d_b).
 }
 \tag{L-91407.22}
\]

Define the packet deficit

\[
 \Delta_Z(P)
 =\mathcal E_Z(P)
  -\sup\{\mathcal S(d):d\text{ feasible for }P\text{ at }Z\}.
 \tag{L-91407.23}
\]

Choose child packings arbitrarily close to their optima.  If the complete finite
forcing producer satisfies

\[
 \Delta_X(F_X^{\rm fin})
 \le C\,m(F_X^{\rm fin}),
 \tag{L-91407.24}
\]

then (L-91407.17)--(L-91407.22) imply

\[
 \boxed{
 \Delta_X(P_X)
 \le C\,m(F_X^{\rm fin})
  +\sum_b\Delta_{Y_b}(P_b).
 }
 \tag{L-91407.25}
\]

Using (L-91407.4),

\[
 \boxed{
 \Delta_X(P_X)
 \le C\,m(P_X)
  +\sum_b\Delta_{Y_b}(P_b).
 }
 \tag{L-91407.26}
\]

This is exactly the local packet-envelope inequality required by `T-91401`.
The child losses remain attached to the actual child packets.

## 6. Application to the finite-block programme

Combine:

```text
L-91404 exact finite-block/rough-child source partition;
L-91559 literal component-capacity identity embedding;
T-91401 packet-envelope consumer.
```

Then the affine-capacity interface refuted by `R-91403/R-91558` is removed.
The surviving proof-facing obligations are now:

1. verify that the balanced and reserve packets of `L-91404` use exactly the
   canonical component-row/capacity normalization of `L-91559`;
2. replay the complete finite forcing producer against those literal capacities;
3. prove the finite forcing debt bound (L-91407.24) in the same additive mass
   used by (L-91407.4);
4. audit the root-packet mass and endpoint-to-RH implication imported by
   `T-91401`.

The recursive child assembly itself is no longer an open affine problem.

## 7. Boundary

```text
identity embedding of each actual child packing      EXACT
ordinary/radix-four parent feasibility                EXACT
source-disjoint one-use capacity                      EXACT
literal score telescoping                             EXACT
packet-envelope local recurrence                      EXACT CONDITIONAL
finite-block source identity                          FROZEN INPUT / L-91404
finite forcing literal normalization                  REPLAY REQUIRED
finite forcing mass-proportional debt                 REPLAY REQUIRED
root endpoint implication                             REPLAY REQUIRED
Riemann Hypothesis                                    UNPROVEN
```
