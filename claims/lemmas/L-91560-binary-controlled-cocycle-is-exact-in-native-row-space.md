# L-91560 — The binary controlled cocycle is exact in target, native score, and the literal component row

Claim ID: `L-91560`  
Status: **PROVED EXACT ONE-PRIME THREE-LEDGER COCYCLE — GLOBAL LEAST-PRIME PARTITION REPLAY REQUIRED**  
Created: 2026-08-13  
Depends on: `O-91310`, `L-91452`, `L-91542`, `L-91556`, `L-91559`  
Closes: the component-row transfer identity left open in `L-91542`  
RH status: **unproved**

## 1. Raw arithmetic residual and exact child

Put

\[
 r=p^{-1/2},
 \qquad
 A=1-r^2,
 \qquad
 d=r(1-r),
 \qquad
 z=\sqrt{x/n}.
 \tag{L-91560.1}
\]

The active one-prime sector has `rz>=1`.  Suppress the common positive source
factor `n^-1/2`.

The native parent target and score are

\[
 T_0=4z-3,
 \qquad
 S_0=5z-3.
 \tag{L-91560.2}
\]

The canonically scaled exact child at endpoint `x/p` is

\[
 T_c=r(4rz-3),
 \qquad
 S_c=r(5rz-3).
 \tag{L-91560.3}
\]

Hence the exact arithmetic residual is

\[
 T_a=T_0-T_c,
 \qquad
 S_a=S_0-S_c.
 \tag{L-91560.4}
\]

At the component-row level, write

\[
 Y=x/n=z^2.
 \tag{L-91560.5}
\]

The exact one-prime row in `O-91310.2` is built pointwise from

\[
 \boxed{
 R_a(Y)=Q_Y-rQ_{Y/p},
 }
 \tag{L-91560.6}
\]

and its exact raw child is

\[
 \boxed{
 R_c(Y)=rQ_{Y/p}.
 }
 \tag{L-91560.7}
\]

Therefore, before any positivity projection,

\[
 \boxed{
 (T_a,S_a,R_a)+(T_c,S_c,R_c)
 =(T_0,S_0,Q_Y).
 }
 \tag{L-91560.8}
\]

This is the one-use arithmetic residual-plus-child identity.

## 2. Controlled binary target

The positive binary return of `L-91452` has targets

\[
 T_s=(1-r)[2(r+2)z-(r+3)],
 \tag{L-91560.9}
\]

\[
 T_h=r[(2r+2)z-(r+2)].
 \tag{L-91560.10}
\]

Direct algebra gives

\[
 \boxed{
 T_s+T_h=T_0=T_a+T_c.
 }
 \tag{L-91560.11}
\]

Thus the controlled branches use exactly the target of the raw residual and its
unique exact child together.  No target is copied.

## 3. Controlled native score

Use the row-budgeted native branch scores of `L-91556`:

\[
 \widetilde S_s=A(5z-3),
 \qquad
 \widetilde S_h=r^2(5z-3).
 \tag{L-91560.12}
\]

Since `A+r^2=1`,

\[
 \boxed{
 \widetilde S_s+\widetilde S_h
 =S_0=S_a+S_c.
 }
 \tag{L-91560.13}
\]

The full binary score is even larger:

\[
 S_s+S_h
 =S_0+d(z-1).
 \tag{L-91560.14}
\]

The term `d(z-1)>=0` is target-null favorable current-generation surplus.  It
is not required to balance the native row score.

## 4. Controlled literal row

Assign the branch row coefficients

\[
 \kappa_s=A,
 \qquad
 \kappa_h=r^2.
 \tag{L-91560.15}
\]

The controlled rows are

\[
 R_s(Y)=AQ_Y,
 \qquad
 R_h(Y)=r^2Q_Y.
 \tag{L-91560.16}
\]

Again `A+r^2=1`, so

\[
 \boxed{
 R_s(Y)+R_h(Y)
 =Q_Y
 =R_a(Y)+R_c(Y).
 }
 \tag{L-91560.17}
\]

Combining Sections 2--4 gives the exact three-ledger cocycle

\[
 \boxed{
 (T_a,S_a,R_a)+(T_c,S_c,R_c)
 =(T_s,\widetilde S_s,R_s)
  +(T_h,\widetilde S_h,R_h).
 }
 \tag{L-91560.18}
\]

The identity holds pointwise in every source node and every finite component-row
coordinate.  It is not inferred from scalar target equality.

This is the component-row transfer normal form which `L-91542` correctly left
open.

## 5. Finite `P_61` packet

For the preferred splice, let

\[
 P_{61}=\prod_{q\le61}q,
 \qquad
 p\ge67,
 \qquad
 1\le y<67.
 \tag{L-91560.19}
\]

For each `d|P_61`, use

\[
 Y_d=py/d.
 \tag{L-91560.20}
\]

Multiply (L-91560.18) by the signed source coefficient

\[
 \frac{\mu(d)}{\sqrt d}
 \tag{L-91560.21}
\]

and sum.  The raw row side is exactly

\[
\begin{aligned}
 &\sum_{d\mid P_{61}}
  \frac{\mu(d)}{\sqrt d}
  [Q_{py/d}-rQ_{y/d}]\\
 &\qquad+
 r\sum_{d\mid P_{61}}
  \frac{\mu(d)}{\sqrt d}Q_{y/d},
\end{aligned}
 \tag{L-91560.22}
\]

namely the arithmetic one-prime residual `O-91310.2` plus its unique exact
child.  Their sum is the signed parent component packet

\[
 \sum_{d\mid P_{61}}
  \frac{\mu(d)}{\sqrt d}Q_{py/d}.
 \tag{L-91560.23}
\]

The controlled side is the sum of the signed survival and hazard packets with
row coefficients `A` and `r^2`.  Their target Hall graphs are exactly those of
`L-91454`; their row-budgeted score and row normalizations are those of
`L-91556`.

Thus Hall may be applied to the controlled branches **after** the raw residual
and child have been recombined, with every arithmetic source coefficient used
once.

## 6. Source-disjoint least-prime induction

In the full finite rough Euler expansion, assign every nontrivial rough monomial
to its least rough prime.  This is a disjoint partition of the arithmetic
source.  At a node with least prime `p`, equation (L-91560.18) consumes:

```text
the raw one-prime residual at that node;
the unique exact child carrying the remaining rough tail.
```

It replaces their sum by two controlled positive-type branch labels.  Since the
raw child appears on the left side exactly once, it is not also retained as an
independent branch.  Repeating over the finite least-prime tree gives, by the
abstract induction of `L-91330`, an exact row/source cocycle at every finite
rough depth.

No product identity between controlled and raw one-prime matrices is asserted.
At each step only the one-step equality (L-91560.18) is used.

A repository replay should still reconstruct this induction directly from the
finite divisor expansion, recording the unique least-prime label of every
monomial.  That is a combinatorial provenance check, not a missing analytic
inequality.

## 7. Physical capacity after control

After target Hall, `L-91545/L-91556` turn the two signed controlled branches into
positive residual sources plus positive row bonuses without changing the
literal row.  `L-91559` then supplies the exact fixed-67 identity embedding of
all recursive child packings in physical ordinary and radix-four columns.

Thus the controlled cocycle introduces no endpoint-measure or affine-fiber
normalization joint:

```text
raw residual + exact raw child
 -> controlled survival + hazard rows
 -> target-Hall residual sources + row bonuses
 -> fixed-67 nested identity embedding.
```

## 8. Boundary

```text
raw residual + raw child target identity             EXACT
raw residual + raw child native-score identity       EXACT
raw residual + raw child literal-row identity        EXACT
controlled target partition                          EXACT
controlled row-budgeted score partition              EXACT
controlled literal-row partition                     EXACT
finite P_61 one-prime cocycle                         EXACT
all-depth least-prime source provenance               FINITE REPLAY REQUIRED
post-Hall fixed-67 physical capacity                  EXACT / L-91559
Riemann Hypothesis                                   UNPROVEN
```
