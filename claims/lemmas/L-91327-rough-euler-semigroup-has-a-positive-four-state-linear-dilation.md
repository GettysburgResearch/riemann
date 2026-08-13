# L-91327 — The rough Euler semigroup has an exact positive four-state dilation with a linear conservative defect ledger

Claim ID: `L-91327`  
Status: **PROPOSED COMPLETE EXACT POSITIVE LINEAR-DILATION THEOREM — PARITY PROJECTION ASSEMBLY OPEN**  
Created: 2026-08-12  
Depends on: `L-91109`, `L-91311`, `L-91317`, `L-91326`  
RH status: **unproved**

## 1. Positive and negative diagonal modes

Retain

\[
 X=L-R,
 \qquad
 Y=L-2R.
\]

Write their Jordan decompositions as

\[
 X=X_+-X_-,
 \qquad
 Y=Y_+-Y_-,
 \qquad
 X_\pm,Y_\pm\ge0.
\tag{L-91327.1}

In the arithmetic application these are not abstract positive parts.  They are
the positive even- and odd-squarefree measures in the two diagonal weight
channels:

\[
 X(x)=\sqrt x\sum_{n\le x}\frac{\mu(n)}n,
 \qquad
 Y(x)=\sum_{n\le x}\frac{\mu(n)}{\sqrt n}.
\]

Define the positive four-state vector

\[
 \boxed{
 z=\begin{pmatrix}X_+\\X_-\\Y_+\\Y_-\end{pmatrix}.
 }
\tag{L-91327.2}

The observation back to `(L,R)` is

\[
 \boxed{
 J_4=
 \begin{pmatrix}
  2&-2&-1&1\\
  1&-1&-1&1
 \end{pmatrix},
 \qquad
 \binom LR=J_4z.
 }
\tag{L-91327.3}

## 2. Exact positive rough action

A finite rough packet has diagonal multipliers

\[
 0\le B\le A\le1.
\]

Define

\[
 \boxed{
 \widetilde D_4(A,B)
 =\operatorname{diag}(A,A,B,B).
 }
\tag{L-91327.4}

This matrix is entrywise nonnegative.  The exact intertwining identity is

\[
 \boxed{
 J_4\widetilde D_4(A,B)=M(A,B)J_4,
 }
\tag{L-91327.5}

where `M(A,B)` is the signed physical matrix of `L-91326`.

Thus every rough Euler packet has a positive four-state realization which is
already adapted to the squarefree parity measures.  Unlike the three-state
rank-one port, no new auxiliary sign or quadratic coordinate is introduced.

## 3. Arbitrary multiprime composition

For a sequence `(A_j,B_j)`,

\[
 \widetilde D_4(A_k,B_k)\cdots\widetilde D_4(A_1,B_1)
 =\widetilde D_4\!\left(\prod_jA_j,\prod_jB_j\right)
\tag{L-91327.6}

and remains entrywise nonnegative. Repeated use of (L-91327.5) gives

\[
 \boxed{
 J_4\prod_j\widetilde D_4(A_j,B_j)
 =\left(\prod_jM(A_j,B_j)\right)J_4.
 }
\tag{L-91327.7}

Distinct-prime composition therefore has an exact finite-dimensional positive
semigroup. The failure of scalar endpoint-port tensorization in `R-91303` does
not affect this state dilation.

## 4. Linear conservative defect ledger

Let

\[
 \mathfrak m(z)=X_++X_-+Y_++Y_-.
\tag{L-91327.8}

Then

\[
 \boxed{
 \mathfrak m(z)-
 \mathfrak m(\widetilde D_4(A,B)z)
 =(1-A)(X_++X_-)+(1-B)(Y_++Y_-)
 \ge0.
 }
\tag{L-91327.9}

For a causal sequence `z_j=widetilde D_j z_(j-1)`, the losses telescope exactly:

\[
\boxed{
 \mathfrak m(z_0)-\mathfrak m(z_k)
 =\sum_{j=1}^{k}
 \left[
  (1-A_j)(X_{+,j-1}+X_{-,j-1})
  +(1-B_j)(Y_{+,j-1}+Y_{-,j-1})
 \right].
}
\tag{L-91327.10
}

Every summand is nonnegative.  This is a coefficient-one **linear** port ledger
for arbitrary distinct-prime composition.

The Hilbert identity of `L-91326` controls squared amplitudes. The present theorem
controls actual positive parity mass. Together they provide both the linear
packing budget and the quadratic Schur reserve.

## 5. Conclusion-relevant observations

The SHARP and endpoint-score functionals become

\[
 \boxed{
 \Psi=L+2R
 =4X-3Y
 =(4,-4,-3,3)z,
 }
\tag{L-91327.11
}

and

\[
 \boxed{
 2L+R
 =5X-3Y
 =(5,-5,-3,3)z.
 }
\tag{L-91327.12
}

Their signs are not automatic in the positive four-state cone.  The finite
no-upward Hall transport of `L-91320` and the exact component-row lift of
`L-91322` are precisely positive projections which cancel the adverse parity
coordinates on each factor-54 window.

Because the rough semigroup never mixes `+` and `-` coordinates, parity
projection may be postponed until a reset boundary without losing source
provenance.

## 6. Compatibility with support and physical columns

`L-91317` routes each rough source atom by its unique least prime to either the
already paid outer block or a contracted child. Apply the same routing to each
of the four positive coordinates.

`L-91318` supplies the exact positive affine Pascal lift for each coordinate,
and `L-91324` proves ordinary physical color erasure for every already assigned
positive branch. Therefore the four-state semigroup has an exact positive
ordinary-row/carry realization on the rough tree.

There is no distinct-prime port duplication: each positive parity atom occurs in
one state coordinate and follows one least-prime branch, while the total
variation loss is charged once by (L-91327.10).

## 7. Exact remaining projection

At the end of one reset generation one must apply the certified parity shadow to
turn the four positive coordinates into:

```text
nonnegative endpoint rows used by the current packing;
nonnegative residual equality/reserve state at the contracted endpoint;
finite positive interval/boundary packets;
and bounded score debt.
```

The local ingredients are resident:

- balanced no-upward Hall transport: `L-91320`;
- positive butterfly lift: `L-91321`;
- direct exact component-row lift: `L-91322`;
- finite mismatch and terminal collars: `L-91114/L-91115`.

What remains is to write their all-generation composition against the linear
ledger (L-91327.10).  No signed rough inverse, scalar port tensorization, or
colored-column estimate remains.

## 8. Verification

The companion exact replay checks:

```text
J4 Dtilde = M J4;
three-factor positive composition;
linear total-variation telescope;
SHARP and score observation vectors;
compatibility with the diagonal product law.
```

Retained verdict:

```text
PASS_POSITIVE_FOUR_STATE_ROUGH_DILATION
```

## 9. Proof boundary

```text
positive four-state parity dilation             EXACT
arbitrary distinct-prime composition             EXACT
linear coefficient-one defect telescope          EXACT
source/least-prime provenance                     AVAILABLE
ordinary positive physical realization            AVAILABLE
local factor-54 parity projection                 AVAILABLE
explicit recursive parity-projection ledger       OPEN
bounded all-generation score recurrence           OPEN / RH-BEARING
Riemann Hypothesis                                UNPROVEN
```
