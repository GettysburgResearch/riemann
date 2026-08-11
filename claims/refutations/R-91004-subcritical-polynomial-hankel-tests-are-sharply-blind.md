# R-91004 — Subcritical polynomial Hankel tests are sharply high-carrier blind

Claim ID: `R-91004`  
Status: **PROPOSED COMPLETE ASYMPTOTIC FIREWALL — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `T-91005`, `L-91011`  
RH status: **unproved**

## 1. The closed strategy class

Consider any test formed from the first `2n+1` safe-line moments by a polynomial square:

\[
 Q_x[p]
 =\sum_{i,j=0}^n\overline{u_i}u_j a_{i+j}(x),
 \qquad
 p(\lambda)=\sum_{j=0}^nu_j\lambda^j.
\]

Equivalently, this is any Rayleigh quotient of the complete Hankel matrix

\[
 H_n(x)=(a_{i+j}(x))_{0\le i,j\le n}.
\]

`T-91005` proves unconditionally that for every fixed `epsilon>0`, all such tests are positive at high carrier whenever

\[
 n\le
 \left(
  \frac1{2\log3}-\varepsilon
 \right)
 \log\log|x|.
\tag{R-91004.1}
\]

This conclusion does not use RH.

## 2. Matching sharpness from a deepest hypothetical pair

`L-91011` proves that a matching pair of depth `y` can compete optimally with the universal Catalan background only at degree

\[
 n\sim
 \frac{\log\log|x|}{4\operatorname{artanh}y}.
\]

As `y` tends to `1/2`, this becomes

\[
 \boxed{
 n\sim
 \frac{\log\log|x|}{2\log3}.
 }
\tag{R-91004.2}
\]

Thus the unconditional positive range and the earliest possible deepest-pair detection range have the same leading constant.

## 3. Exact firewall

The following programme cannot prove RH:

```text
choose any polynomial p_x of degree n(x);
form the safe-line moment square Q_x[p_x];
prove positivity by the high-carrier safe-Euler asymptotic;
keep n(x) below (1/(2 log 3)-epsilon) log log|x|;
conclude all zeros are on the line.
```

Every such positivity statement is already true in a hypothetical false-RH world with one sufficiently high off-line pair.

The obstruction is not a poor choice of basis. `L-91011` uses the exact Christoffel function and therefore optimizes over **all** degree-`n` polynomials.

## 4. What remains viable

A conclusion-producing polynomial-Hankel continuation must do at least one of the following:

1. reach the critical degree
   \[
   n=\frac{\log\log|x|}{2\log3}+O(\log\log\log|x|);
   \]
2. use depth-adapted Christoffel vectors and control all nuisance blocks;
3. continue the Pick/Stieltjes structure into the annulus and use rational rather than polynomial test functions;
4. subtract the universal beta-`(3/2,3/2)` background while preserving a positive arithmetic form;
5. use carrier-specific prime information unavailable to the safe-Euler asymptotic.

`L-91012` develops item 3 as a new exact amplifier family.

## 5. Boundary

```text
all degree-n polynomial SOS tests below edge      HIGH-CARRIER POSITIVE
Christoffel vector is degree-n optimal            EXACT
edge constant 1/(2 log 3)                         SHARP AT LEADING ORDER
subcritical polynomial-Hankel RH strategy          CLOSED
critical/supercritical matrix theorem              OPEN / RH-BEARING
rational safe-pole acceleration                    EXACT NEW INTERFACE
Riemann Hypothesis                                 UNPROVED
```
