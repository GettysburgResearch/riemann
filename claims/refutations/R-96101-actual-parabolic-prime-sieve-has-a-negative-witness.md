# R-96101 — The actual parabolic endpoint row does not survive finite initial-prime sieving

Claim ID: `R-96101`  
Status: **EXACT REFUTATION OF THE NATURAL PARABOLIC REPAIR**  
Created: 2026-08-16  
Depends on: the local parabolic row in `R-96100.1`  
RH status: **unproved**

## 1. Candidate repair being tested

After separating the two rows in `R-96100`, the most direct attempted repair is
to keep the actual parabolic endpoint row

\[
 D_Y(j)=(j+1)\Delta_j^2
 \left[
  \frac{2\sqrt m}{m-1}
  \left(
   \log\frac Ym-2+2\sqrt{\frac mY}
  \right)\mathbf1_{m\le Y}
 \right]_{m=j}
\tag{R-96101.1}
\]

and ask whether

\[
 \sum_{d\mid P_r}
 \frac{\mu(d)}{\sqrt d}D_{Y/d}(j)\ge0
\tag{R-96101.2}
\]

holds for every finite initial prime segment.

It does not.

## 2. Exact finite witness

Take

\[
 P_r=2\cdot3\cdot5\cdot7\cdot11=2310,
 \qquad j=7,
 \qquad Y=105.
\]

Only divisors `d<=15` can contribute. The complete finite sum is

\[
 \mathcal P
 =\sum_{d\mid2310}
   \frac{\mu(d)}{\sqrt d}D_{105/d}(7).
\tag{R-96101.3}
\]

`X-96100` encloses every square root by an integer-square-root rational interval
and every logarithm by range reduction plus the rational atanh series. It gives

\[
 \boxed{
 -0.014986302853216604281889124017
 <\mathcal P<
 -0.014986302853216604281889124016
 <-\frac1{100}.
 }
\tag{R-96101.4}
\]

Thus (R-96101.2) is false.

## 3. Scope

This witness refutes only the attempted parabolic substitution. It does not
refute the separately defined discrete-tail row of PR #542.

```text
actual parabolic finite sieve       FALSE
witness                              P=2310, j=7, Y=105
transcendental enclosure             directed rational
parabolic repair of L-94200          unavailable
discrete-tail global sieve           OPEN
Riemann Hypothesis                    UNPROVEN
```
