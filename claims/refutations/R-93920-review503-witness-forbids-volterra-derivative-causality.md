# R-93920 — Review #503 is correct: the Volterra derivative fibres are not a hereditary causal cone

Claim ID: `R-93920`  
Status: **PROVED EXACT REFUTATION / NORMATIVE FIREWALL**  
Created: 2026-08-16  
Frozen proposal: PR #495 at `50f45b46cbe3c471d6e702c41c7ef178b530e1ab`  
Frozen review: PR #503 at `db77e5792966edf080604fd4b69fb00f07739681`  
RH status: **unproved**

## 1. Retained results

The following PR #495 claims survive the frozen review and remain imported at their exact scope:

```text
L-91760  exact Volterra antiderivative and finite/continuum split;
L-91761  rank-one Möbius source ownership on a positive-density fibre;
L-91762  rough-lift/Volterra Fubini and first-owner Jacobian.
```

`L-91762` is retained only as a normalization and provenance audit in the successor below. It is not used as the physical parent marginal.

## 2. Exact negative witness

For

\[
g_s(n)=\left(\sqrt n-\frac n{\sqrt s}\right)\mathbf1_{n\le s}
\]

and

\[
p_s(j)=(j+1)\left[
 \frac{g_s(j)}{j-1}
 -\frac{2g_s(j+1)}j
 +\frac{g_s(j+2)}{j+1}
\right],
\]

take

```text
p = 67,
y = 15,
s = py = 1005,
j = 14.
```

Then

\[
\begin{aligned}
D
&=p_{1005}(14)-67^{-1/2}p_{15}(14)\\
&=4+\frac{15\sqrt{14}}{13}
 -\frac{15\sqrt{15}}7
 -\frac1{91\sqrt{1005}}
 -\frac{15\sqrt{14}-14\sqrt{15}}{13\sqrt{67}}.
\end{aligned}
\]

Directed rational square-root intervals give

\[
\boxed{
-\frac{184291}{10^9}
<D<
-\frac{184290}{10^9}<0.
}
\]

Thus

\[
p_s-p^{-1/2}U_pp_{s/p}
\]

is not a nonnegative physical row in general.

## 3. Normative consequence

Every successor to PR #495 must fail closed if it:

1. invokes `L-91763` or `T-92910`;
2. forms a current atom `p_s-p^{-1/2}U_pp_{s/p}`;
3. assumes that positive integration can repair a negative derivative fibre;
4. substitutes the full rough lift for the native input marginal.

The repair in `L-93920--L-93922` uses no such operator. Bulk Volterra fibres are inserted directly as positive rows. The complementary finite cells are realized by the finite Target–Lorenz leaf theorem. No derivative fibre is inherited by a child.

```text
L-91760--L-91762                         retained
L-91763 / T-92910                        rejected / forbidden
exact witness                            mandatory regression
new route uses derivative causality      no
Riemann Hypothesis                        unproved
```
