# R-92000 — One off-line orbit breaks reciprocal concavity at order three

Claim ID: `R-92000`  
Status: **EXACT ORBITWISE FIREWALL**  
Created: 2026-08-13  
Depends on: `L-92000/L-92002`; `R-91902`  
RH status: **unproved**

## 1. One symmetric off-line orbit

Take

\[
 \lambda=a+ib,
 \qquad
 0<|a|<\frac12,
\]

and the even real orbit

\[
 \{\lambda,-\lambda,\overline\lambda,-\overline\lambda\}.
\]

Put

\[
 c=b^2-a^2,
 \qquad
 B=2ab,
 \qquad
 U=t+c.
\]

Its contribution to

\[
 p(t)=\frac{F(\sqrt t)}{\sqrt t}
\]

is

\[
 \boxed{
 p_{a,b}(t)=\frac{4mU}{U^2+B^2}.
 }
 \tag{R-92000.1}
\]

## 2. Reciprocal curvature has the wrong sign

The reciprocal is

\[
 \frac1{p_{a,b}(t)}
 =\frac1{4m}\left(U+\frac{B^2}{U}\right).
 \tag{R-92000.2}
\]

Therefore

\[
 \boxed{
 \left(\frac1{p_{a,b}}\right)''(t)
 =\frac{B^2}{2mU^3}>0.
 }
 \tag{R-92000.3}
\]

Thus an off-line orbit is strictly **convex** in the reciprocal Clark
coordinate, whereas a critical-line Stieltjes orbit is affine there.

For ordinates larger than `sqrt(3)`, `L-92001` gives

\[
 (t p_{a,b})''<0.
\]

The two curvature factors in `L-92000` therefore have opposite signs.  Every
sufficiently confluent three-node packet has a negative determinant.

## 3. Exact rational separated packet

For

\[
 a=\frac25,
 \qquad b=14,
\]

and safe nodes

\[
 x_1=\frac35,
 \qquad x_2=8,
 \qquad x_3=36,
\]

`R-91902` gives

\[
 \boxed{
 \det\mathcal H
 =-\frac{
 201516024836691562500
 }{
 1055839030806150723363641645963
 }<0.
 }
 \tag{R-92000.4}
\]

The verifier on the present branch reconstructs the same value from the two
curvature factors in `L-92000`.

## 4. Consequence

The order-three sign cannot be proved by applying a positive estimate to each
zero orbit separately.  Critical-line and off-line orbit contributions must be
combined before reciprocal curvature is taken.

This is a lower-order analogue of the lesson in Claude's finite-compression
argument: the signed geometry must be read at the level of the complete
Hermitian object, not by assigning a favourable sign term by term.  The new
curvature formulation identifies exactly where the collective information
enters.

## 5. Exact boundary

```text
single off-line reciprocal curvature       STRICTLY POSITIVE
single off-line tp curvature               STRICTLY NEGATIVE AT ZETA HEIGHTS
local three-node determinant               STRICTLY NEGATIVE
separated exact rational packet            STRICTLY NEGATIVE
orbitwise positivity route                 REFUTED
collective actual-Xi curvature              OPEN
Riemann Hypothesis                          UNPROVED
```
