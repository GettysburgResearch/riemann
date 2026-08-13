# R-91560 — The same-index typed child is not the affine Pascal child lift

Claim ID: `R-91560`  
Status: **EXACT FINITE COMPOSITION FIREWALL / PR #424 AFFINE JOINT INVALID AS WRITTEN**  
Created: 2026-08-13  
Frozen target: PR #424 at `7c0927e9364e191c720d5a618928d99847ac8edd`  
Depends on: `L-91318`, `L-91540`, `L-91547`, `L-91549`  
RH status: **unproved**

## 1. The two child operations

For a component row

\[
 Q_Y(j)=(j+1)\Delta^2\left[\frac{S_Y(j)}{j-1}\right],
 \qquad
 S_Y(j)=\sum_{m\ge j}m^{-1/2}\log(Y/m)\mathbf1_{m\le Y},
\]

`L-91540` uses the same-index identity

\[
 Q_Y(j)=Q_{Y/p}(j)+[Q_Y(j)-Q_{Y/p}(j)],
 \qquad Q_Y(j)-Q_{Y/p}(j)\ge0.
\tag{R-91560.1}
\]

The affine Pascal lift of `L-91318` is a different operation.  It sends

\[
 j\longmapsto \Phi_p(j)=p(j+1)-1,
 \qquad
 d(j)\longmapsto p^{-1/2}d(j).
\tag{R-91560.2}
\]

There is no implication

\[
 Q_Y(\Phi_p(j))\ge p^{-1/2}Q_{Y/p}(j).
\tag{R-91560.3}
\]

## 2. Exact witness

Take

\[
 p=67,
 \qquad Y=201,
 \qquad Y/p=3,
 \qquad j=2,
 \qquad \Phi_{67}(2)=200.
\]

At the parent row `200`, only the term `m=200` contributes because the
`m=201` logarithm vanishes. Hence

\[
 Q_{201}(200)
 =\frac{201}{199\sqrt{200}}\log\frac{201}{200}
 <\frac{201}{199\cdot200\sqrt{200}}
 <\frac1{2000}.
\tag{R-91560.4}
\]

The last inequality follows from `sqrt(200)>14`.

At the child row `2`,

\[
 Q_3(2)=\frac3{\sqrt2}\log\frac32.
\]

Using

\[
 \log\frac32>\frac25,
 \qquad
 \sqrt{134}<12,
\]

one gets

\[
 67^{-1/2}Q_3(2)
 =\frac{3\log(3/2)}{\sqrt{134}}
 >\frac1{10}.
\tag{R-91560.5}
\]

Therefore

\[
\boxed{
 Q_{201}(200)-67^{-1/2}Q_3(2)<0.
}
\tag{R-91560.6}
\]

## 3. Consequence for PR #424

`L-91547.5` proves positivity of the residual after retaining the child at the
same row indices.  Section 5 of `L-91547` then says that the child row is lifted
by the affine map, and `L-91549/T-91551` use that affine row in the parent
assembly.  The witness above shows that the same residual cannot simply be
retained after this replacement.

Thus the chain

```text
same-index positive typed split
 -> replace child by affine Pascal lift
 -> keep the same positive parent residual
```

is false.

This does not refute the same-index typed split or the affine covariance theorem
separately.  It refutes their unproved composition.

## 4. Correct repair direction

After Hall has erased arithmetic color provenance, there is no need to apply an
affine lift to the recursively chosen child packing.  The radix-four detail
target is monotone in the endpoint, so the child row may be included at the
same indices.  `L-91560` records that exact replacement.

```text
same-index Q-row heredity                         EXACT
fixed affine Pascal lift                          EXACT
identifying the two child rows                    FALSE
PR #424 affine residual joint                     BROKEN AS WRITTEN
same-index physical child inclusion               REPAIR / L-91560
Riemann Hypothesis                                UNPROVEN
```
