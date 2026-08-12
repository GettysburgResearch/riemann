# L-91621 — Approximate log exhaustion gives quantitative zero moats

Claim ID: `L-91621`  
Status: **PROVED EXACT STABILITY INEQUALITY; EXACT EXHAUSTION OPEN**  
Created: 2026-08-12  
Depends on: `L-91620`; `L-91520`  
RH status: **unproved**

## 1. One-zero moat

For a crossed-zero coordinate

\[
 \zeta=x+iy,
 \qquad x>0,
\]

`L-91620` gives

\[
 g_\eta(\zeta)
 =\log\left(1+
  \frac{4\eta x}{(\eta-x)^2+y^2}
 \right).
\]

Using

\[
 \log(1+t)\ge\frac{t}{1+t}
 \qquad(t\ge0),
\]

we obtain the quantitative Green moat

\[
 \boxed{
 g_\eta(x+iy)
 \ge
 \frac{4\eta x}{(\eta+x)^2+y^2}.
 }
\]

The bound is strict for every crossed zero.

## 2. Packet inequality

For an annular zero packet `Z_(a,b)`, counted with multiplicity,

\[
 \boxed{
 \Lambda_{a,b}^{\rm ann}(\eta)
 \ge
 \sum_{\zeta=x+iy\in Z_{a,b}}
 m_\zeta
 \frac{4\eta x}{(\eta+x)^2+y^2}.
 }
\]

Thus any certified upper bound

\[
 \Lambda_{a,b}^{\rm ann}(\eta)\le\varepsilon
\]

immediately bounds the total weighted crossed-zero content of the annulus.

## 3. Explicit box exclusion

For centered zeta coordinates one has

\[
 0<x<\frac12.
\]

Fix `delta>0` and `Y>0`.  Every crossed zero with

\[
 x\ge\delta,
 \qquad
 |y|\le Y
\]

contributes at least

\[
 \boxed{
 \mathfrak m(\eta,\delta,Y)
 =\frac{4\eta\delta}
 {\left(\eta+\frac12\right)^2+Y^2}.
 }
\]

Consequently,

\[
 \boxed{
 \Lambda_{a,b}^{\rm ann}(\eta)
 <\mathfrak m(\eta,\delta,Y)
 }
\]

excludes every crossed zero in that depth-height box.

More generally, the number of such zeros counted with multiplicity is at most

\[
 \boxed{
 \frac{\Lambda_{a,b}^{\rm ann}(\eta)}
      {\mathfrak m(\eta,\delta,Y)}.
 }
\]

## 4. Approximate arithmetic exhaustion

Suppose a source construction gives, on one dyadic annulus,

\[
 \mathscr L_j^{\rm arith}
 =\mathscr L_j^{\rm crit}
  +\mathscr L_j^{\rm st}
  +\Lambda_j^{\rm ann}
  +\mathscr L_j^{\rm aux}
\]

with

\[
 \Lambda_j^{\rm ann}\ge0,
 \qquad
 \mathscr L_j^{\rm aux}\ge0,
\]

and an arithmetic estimate

\[
 0\le
 \mathscr L_j^{\rm arith}
 -\mathscr L_j^{\rm crit}
 -\mathscr L_j^{\rm st}
 \le\varepsilon_j.
\]

Then

\[
 \boxed{
 0\le\Lambda_j^{\rm ann}\le\varepsilon_j.
 }
\]

Hence any quantitative source exhaustion gives a correspondingly quantitative
zero-free box by Section 3.

## 5. Cofinal implication

For a fixed hypothetical off-line zero, its depth `x>0` and ordinate offset
`y` are finite.  If the annulus containing it admits a sequence of source
factorizations whose exhaustion error tends to zero, then the moat above
forces a contradiction.

Thus exact exhaustion is sufficient but not logically necessary: a cofinal
family of genuinely source-identified errors tending to zero also proves the
same annular zero-free conclusion.

The source identification is essential.  An arbitrary numerical upper bound
on a scalar not already proved equal to the annular model remainder cannot be
inserted here.

## 6. Exact boundary

```text
one-zero quantitative moat                    EXACT
annular weighted zero-count bound             EXACT
finite depth-height box exclusion             EXACT
approximate source exhaustion -> zero moat    EXACT CONDITIONAL
source/model identification                   OPEN / RH-BEARING
Riemann Hypothesis                            UNPROVED
```
