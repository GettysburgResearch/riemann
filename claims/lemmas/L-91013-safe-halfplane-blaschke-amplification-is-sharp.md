# L-91013 — The repeated boundary pole is optimal among all safe-half-plane Blaschke amplifiers

Claim ID: `L-91013`  
Status: **EXACT RATIONAL GREEN-FUNCTION EXTREMAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91012`  
RH status: **unproved**

## 1. Radial coordinate

Write

\[
 \lambda=\frac1{1-r^2}.
\tag{L-91013.1}
\]

The critical-line support `0<lambda<=1` corresponds to `r=iu`, `u in R`. A possible off-line depth corresponds to a real point

\[
 r=y,
 \qquad 0<y<\frac12.
\]

Absolute Euler evaluation is safe at every pole with

\[
 \Re r>\frac12.
\]

Thus the final arithmetic boundary is a vertical line in the `r`-plane.

## 2. General safe rational inner product

Let

\[
 a_j=c_j+iv_j,
 \qquad c_j\ge\frac12,
 \qquad 1\le j\le n,
\]

and define the half-plane Blaschke product

\[
 B(r)
 =e^{i\theta}
  \prod_{j=1}^n
  \frac{r+\overline{a_j}}{r-a_j}.
\tag{L-91013.2}
\]

For `r=iu`,

\[
 |B(iu)|=1.
\tag{L-91013.3}
\]

Hence the even symmetrization

\[
 R_B(r)
 =\frac12\left(B(r)+B(-r)\right)
\tag{L-91013.4}
\]

or, in the real-pole case, `(B+B^-1)/2`, has modulus at most one on the critical-line support and is rational in `r^2`, hence rational in `lambda`.

The repeated-real-pole family of `L-91012` is the special case

\[
 a_1=\cdots=a_n=a>\frac12.
\]

## 3. Exact Green-function bound

At a target depth `y`, one factor satisfies

\[
 \left|
 \frac{y+\overline a}{y-a}
 \right|^2
 =\frac{(c+y)^2+v^2}{(c-y)^2+v^2}.
\tag{L-91013.5}
\]

For `c>=1/2`, the right-hand side decreases as either `c` or `|v|` increases. Therefore

\[
 \boxed{
 \left|
 \frac{y+\overline a}{y-a}
 \right|
 \le
 \frac{1/2+y}{1/2-y}.
 }
\tag{L-91013.6}
\]

Multiplying the factors gives

\[
 \boxed{
 |B(y)|
 \le
 \left(
  \frac{1/2+y}{1/2-y}
 \right)^n
 =\exp\left(2n\operatorname{artanh}(2y)\right).
 }
\tag{L-91013.7}
\]

Equality in the exponential rate is approached only when every pole tends to the nearest boundary point

\[
 a_j\longrightarrow\frac12.
\]

Thus the half-plane Green function from the target depth to the safe Euler boundary is exactly

\[
 \boxed{g_{\rm safe}(y)=2\operatorname{artanh}(2y).}
\tag{L-91013.8}
\]

## 4. Optimal rational-square rate

A quadratic moment test squares the amplifier. Consequently every degree-`n` rational inner architecture with all poles in the safe Euler half-plane has target/background exponential rate at most

\[
 \boxed{
 \exp\left(4n\operatorname{artanh}(2y)\right).
 }
\tag{L-91013.9}
\]

The repeated boundary-pole Chebyshev family of `L-91012` attains this rate. Therefore its formal detection complexity

\[
 \boxed{
 n_{\rm rat}(x,y)
 \sim
 \frac{\log\ell_x}{4\operatorname{artanh}(2y)}
 }
\tag{L-91013.10}
\]

is optimal throughout the complete safe-half-plane rational-inner class.

## 5. Strategic consequence

Allowing many distinct safe poles, complex poles, or a general finite Blaschke product cannot improve the leading target exponent beyond `L-91012`. Any further acceleration must leave this class by using at least one of:

1. poles entering the annulus, hence samples with `Re(s)<1`;
2. non-inner rational functions with a growing critical-line norm;
3. matrix-valued or noncommutative source information;
4. carrier-specific arithmetic cancellation rather than pure analytic amplification.

This closes a broad class of apparently more sophisticated multipole designs before expensive implementation.

## 6. Boundary

```text
safe radial coordinate                         EXACT
critical-line unit-modulus Blaschke family      EXACT
per-pole Green bound                            EXACT
repeated boundary pole is rate-optimal          EXACT
optimal rational-square exponent                EXACT
uniform arithmetic sign at optimal rate         OPEN / RH-BEARING
Riemann Hypothesis                              UNPROVED
```
