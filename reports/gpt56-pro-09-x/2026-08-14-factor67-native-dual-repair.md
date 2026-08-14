# Factor-67 native-dual repair after the normalization firewall

Authoring agent: `gpt56-pro-09-x`  
Date: 2026-08-14  
Status: **corrected candidate closure on frozen inputs; RH unproved pending reconstruction**

## 1. Why the old final scalar had to be removed

The previous factor-67 composition recursed a normalized equality-packet
deficit and then asserted

\[
4\sqrt X-\mathcal H(d_X)=O(1).
\]

That cannot be the conclusion of a native-feasible construction.  Exact native
feasibility gives

\[
\mathcal H(d_X)\le J_\Lambda(X),
\]

and under the claimed RH consequence

\[
J_\Lambda(X)=4\sqrt X-\kappa_0\log X+O(1),
\qquad\kappa_0>0.
\]

Thus the absolute continuum-score conclusion is misnormalized.  This does not
invalidate the factor-67 Hall, source labels or finite column bounds.

## 2. The correct metric

The literal native deficit is

\[
\Delta_X
 =J_\Lambda(X)-\mathcal H(d_X)
 =\sum_qY_4(q)s_X(q).
\]

The exact source-owned capacity partition gives the cocycle

\[
\Delta_X
 =\delta_X+\sum_b\alpha_b\Delta_{Y_b},
\qquad
\delta_X=\sum_qY_4(q)r_X(q).
\]

The only quantitative question is the root cost `delta_X`.

## 3. New arithmetic fact: Y4 is extremely sparse

The dual weight has the exact form

\[
Y_4(2^e)
 =(2^{\lceil e/2\rceil}-1)\log2,
\]

\[
Y_4(4^vp^a)=2^v\log p
\quad(p\text{ odd prime}),
\]

and vanishes elsewhere.  Therefore

\[
\sum_{q\ge2}\frac{Y_4(q)}{q^{3/2}}<11
\]

and

\[
\sum_{q\le X}\frac{Y_4(q)}q
 \le3+2\log(2X)+2\log^2(2X).
\]

These estimates require no prime number theorem.

## 4. Direct native cost of every physical correction

The factor-67 finite/continuum mismatch obeys

\[
|e_X^{\rm mis}(q)|<\frac{285}{8}q^{-3/2},
\]

so its complete native cost is

\[
\sum_qY_4(q)|e_X^{\rm mis}(q)|<392.
\]

The quantization collar obeys

\[
|e_X^{\rm col}(q)|<\frac{200}{q\sqrt K},
\]

and therefore has native cost `o(1)` for `K>X/67`.

The global safety factor removes less than `178/K` of a full native packet.
The elementary bound

\[
J_\Lambda(X)\le2\sqrt X\log^2(2X)
\]

makes this cost `o(1)` as well.

The top omission is a positive endpoint packet and hence its `Y4` cost equals
its literal entropy.  The frozen top theorem gives bounded cost.  The same
frozen positive-packet ledger supplies bounded base and common-port cost.

Consequently

\[
\delta_X=O(1).
\]

## 5. Corrected factor-67 conclusion

Since

\[
\sum_b\alpha_b<1/8,
\qquad
Y_b\le X/67+1,
\]

the exact native cocycle gives

\[
\boxed{
J_\Lambda(X)-\mathcal H(d_X)=O(1).
}
\]

This is stronger than the required `o(log^2 X)` native slack.  It is compatible
with RH and does not assert that the continuum target `4 sqrt(X)` is physically
attained.

On the frozen common-parent, positive endpoint and endpoint-consumer inputs,
this repairs the factor-67 `SONTR/NRCT` composition.  The packet remains a
candidate pending hostile reconstruction of those dependencies.

## 6. Exact review frontier

```text
Y4 support and summability                         NEW EXACT / L-19885
factor-67 mismatch native cost <392                NEW EXACT ON FROZEN BOUND
collar and safety native cost o(1)                 NEW EXACT
top/base/port native cost O(1)                     FROZEN INPUT / REVIEW
common-parent full-capacity identity               FROZEN INPUT / REVIEW
exact native slack recurrence                      NEW EXACT / L-19882
corrected native deficit O(1)                      CANDIDATE COMPLETE ON INPUTS
endpoint consumer                                  FROZEN INPUT / REVIEW
Riemann Hypothesis                                 UNPROVED
```

The independent radial `DGGC_a` and passive `PSI_a` routes remain open and are
not needed by the corrected Route A composition.
