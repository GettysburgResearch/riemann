# L-91454 — Both binary-return branches have target-exact, score-superordinate positive row projections

Claim ID: `L-91454`  
Status: **PROVED EXACT ONE-PRIME TARGET PROJECTION — RECURSIVE SOURCE IDENTIFICATION OPEN**  
Created: 2026-08-12  
Depends on: both one-prime Hall theorems `L-91331`, `L-91330`, `L-91342`, `L-91452/L-91453`  
RH status: **unproved**

## 1. Why target transport is stronger here

`L-91453` transports in score units and obtains score-exact,
target-subordinate branch measures. For recursive capacity accounting, one can
instead transport in **target units**. The same no-upward support then gives the
opposite favorable inequality: target is exact and score is superordinate.

Retain the branch target and score atoms from `L-91453` and write

\[
 q(z)=\frac{\text{target atom}}{\text{score atom}},
 \qquad z=\sqrt{x/n}\ge1.
\]

For both survival and hazard branches, `L-91453` proves

\[
 q'(z)>0.
\tag{L-91454.1}
\]

Moreover direct substitution at `z=1` gives

\[
\boxed{
 q_s(1)=q_h(1)=\frac12.
}
\tag{L-91454.2}
\]

Hence every positive residual target measure has score at most twice its target
and lies in the positive physical two-ledger cone.

## 2. Survival target Hall

The survival target is

\[
 T_s=(1-r)(r+3)U_{\alpha_s},
 \qquad
 \alpha_s=\frac{2(r+2)}{r+3}
 \in\left(\frac43,\frac32\right).
\]

The one-prime SHARP Hall theorem on the live parent proves a uniform no-upward
Hall margin throughout this complete parameter interval. Therefore every odd
survival target demand transports to even target capacity with support

\[
 e\le o.
\]

## 3. Hazard target Hall

The hazard target is

\[
 T_h=r(r+2)U_{\alpha_h},
 \qquad
 \alpha_h=\frac{2(r+1)}{r+2}
 =1+\frac r{r+2}.
\]

For `p>=67`,

\[
 1<\alpha_h<1+r\le1+67^{-1/2}.
\]

Thus the reserve-corridor Hall theorem applies and gives a no-upward target
transport with its directed margin `>8/25`.

## 4. Target exactness and score superordination

For either branch let `t_(o,e)>=0` be its Hall transport in target-mass units.
Let `q_s` or `q_h` be the corresponding target-per-score ratio. Since
`e<=o`, one has `z_e>=z_o`, and (L-91454.1) gives

\[
 q(e)\ge q(o).
\]

The score of the positive residual target measure minus the signed branch score
is therefore

\[
\boxed{
 \sum_{o,e}t_{o,e}
 \left[
  \frac1{q(o)}-\frac1{q(e)}
 \right]
 \ge0.
}
\tag{L-91454.3}
\]

Consequently each branch has a positive coefficient measure satisfying

```text
represented target = exact branch target;
represented score >= exact branch score.
```

No target capacity is discarded.

## 5. Exact finite-row lift

The target channels have parameters

\[
 \alpha_s\in(4/3,3/2),
 \qquad
 \alpha_h\in(1,1+67^{-1/2}).
\]

The universal component-row theorem of `L-91330` gives monotonicity of

\[
 \frac{Q_Y(j)}{\alpha\sqrt Y-1}
\]

for every `alpha>=1` on the reset window. Therefore every no-upward target edge
lifts to a nonnegative exact component-row difference, and every residual even
row is nonnegative.

Thus the survival and hazard target transports are each simultaneously:

```text
target-exact;
score-superordinate;
coefficientwise nonnegative in every exact finite row.
```

## 6. Binary assembly

`L-91452` gives the exact target identity

\[
 T_s+T_h=T_{parent}
\]

and the favorable exact branch score identity

\[
 S_s+S_h=S_{parent}+dR\ge S_{parent}.
\]

Applying Sections 2--5 to the two disjoint branch labels yields positive row
packets whose targets sum **exactly** to the parent target and whose scores sum
to at least the parent score. Hence one rough-prime step has no target slack to
track and no positive score debt.

The hazard packet is sent through the affine child lift; the survival packet is
retained for the next ordered prime. Because the target measures are exact,
`L-91329` may sum all colors in parent coordinates and quantize once without a
branchwise collar.

## 7. Remaining recursive identification

The one-prime physical row/capacity theorem is now target-exact rather than
merely target-subordinate. The remaining statement is to identify the residual
positive target measures with the recursively typed child sources before the
next prime is processed. Equivalently, prove that the unique-next-prime color
can be carried through Hall disintegration, affine lifting and the common
endpoint-port correction without altering the target telescope.

```text
survival target Hall projection                    EXACT FROM DIRECTED INPUT
hazard target Hall projection                      EXACT FROM DIRECTED INPUT
target exactness                                    EXACT
score superordination                               EXACT
positive physical two-ledger ratio                  EXACT
exact finite-row positivity                         EXACT
one-prime target-exact physical recurrence          PROPOSED COMPLETE
all-generation colored source identification        OPEN / RH-BEARING
Riemann Hypothesis                                  UNPROVEN
```
