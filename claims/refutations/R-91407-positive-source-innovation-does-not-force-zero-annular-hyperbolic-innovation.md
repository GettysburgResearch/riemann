# R-91407 — Positive source innovation does not force zero annular hyperbolic innovation

Claim ID: `R-91407`  
Status: **EXACT ONE-NODE EXHAUSTION FIREWALL**  
Created: 2026-08-12  
Depends on: `L-91420`, `L-91421`; `L-91318/L-91319` on PR #403  
RH status: **unproved**

## 1. Two positive telescopes

The arithmetic pole-node source has the positive dyadic innovation

\[
 I(a)
 =F(a)-F(2a)
 =\int t\,d\nu_{a,1+2a}(t)>0,
 \tag{R-91407.1}

\]

where

\[
 F(a)=\gamma-\frac{\zeta'}{\zeta}(1+2a).
\]

Independently, the model hyperbolic diagonal has the positive annular
innovation

\[
 H_a(\eta)-H_{2a}(\eta)
 =|B_{2a}(\eta)|^{-2}
  H_{a,2a}^{\rm ann}(\eta)\ge0.
 \tag{R-91407.2}

\]

Positivity and telescoping of both sequences do not identify them.

## 2. Abstract countermodel

Let `(I_j)` be any positive summable sequence and let `(h_j)` be any second
positive sequence with

\[
 0<h_j<I_j.
\]

Define source, stable and hyperbolic innovation norms by

\[
 \|s_j\|^2=I_j,
 \qquad
 \|k_j^{\rm st}\|^2=I_j-h_j,
 \qquad
 \|k_j^{\rm hyp}\|^2=h_j.
 \tag{R-91407.3}

\]

Every innovation is positive, every coefficient-one telescope converges, and
the source norm equals the sum of stable and hyperbolic outputs.  Yet the
hyperbolic port is nonzero.

Thus the positive arithmetic innovation telescope of `L-91319` does not by
itself delete any crossed-zero annulus.

## 3. Safe scalar values do not repair the gap

A planted finite Blaschke factor can be multiplied into the model quotient.
It changes `H_a(eta)` by a strictly positive term while leaving all safe
real-axis source scalars available for a compensating stable output.  Therefore
positivity, monotonicity, or exact evaluation of the one-Green source norm is
not sufficient.

The missing statement is an actual source-ordered map identifying which part
of each arithmetic innovation is consumed by the critical and deterministic
stable outputs.

## 4. Correct conclusion-producing theorem

At every dyadic annulus, one must construct the innovation map

\[
 s_j
 \longmapsto
 k_j^{\rm crit}\oplus k_j^{\rm st}
  \oplus k_j^{\rm hyp}
 \tag{R-91407.4}

\]

from the declared prime/gamma/pole source and prove the coefficient-one
exhaustion

\[
 \boxed{
 \|s_j\|^2
 =\|k_j^{\rm crit}\|^2
  +\|k_j^{\rm st}\|^2.
 }
 \tag{R-91407.5}

\]

Only (R-91407.5) forces the annular hyperbolic norm to vanish.

## 5. Exact boundary

```text
positive source dyadic innovations                    EXACT
positive model annular innovations                    EXACT
positivity/telescoping alone -> annular zero           FALSE
safe scalar norm alone -> annular zero                 FALSE
source-ordered critical/stable exhaustion              OPEN / RH-BEARING
Riemann Hypothesis                                     UNPROVED
```