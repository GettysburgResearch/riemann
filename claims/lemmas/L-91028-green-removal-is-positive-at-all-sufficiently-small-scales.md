# L-91028 — The final arithmetic Green removal is positive at all sufficiently small scales

Claim ID: `L-91028`  
Status: **PROPOSED COMPLETE UNCONDITIONAL SMALL-SCALE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-12  
Depends on: `L-91023`, `L-91026`; continuity theorem for Laplace transforms of positive measures  
RH status: **unproved**

## 1. Scaled discrepancy

Write the generalized-Jordan parameter as `s>0` and put

\[
 e_s(y)=E_{s,0}(y/s),
 \qquad
 I_s(y)=sE_{s,1}(y/s)=\int_0^y e_s(v)\,dv.
 \tag{L-91028.1}
\]

The functions are nonnegative by `L-91023`.

Their Laplace transform is

\[
 \boxed{
 \int_0^\infty e^{-zy}e_s(y)\,dy
 =\frac1z
 \left[
 Z_s(sz)-\frac{c_s}{sz}
 \right],
 \qquad z>0.
 }
 \tag{L-91028.2}
\]

As `s downarrow 0`, the pole normalization of zeta gives

\[
 s\zeta(1+s)\longrightarrow1,
\]

and, for every fixed `z>0`,

\[
 Z_s(sz)
 =\frac{\zeta(1+sz)}{\zeta(1+s(1+z))}
 \longrightarrow\frac{1+z}{z},
\]

while

\[
 \frac{c_s}{s}\longrightarrow1.
\]

Therefore

\[
 \boxed{
 \int_0^\infty e^{-zy}e_s(y)\,dy
 \longrightarrow\frac1z.
 }
 \tag{L-91028.3}
\]

The right side is the Laplace transform of Lebesgue measure on `[0,infinity)`.

Since `e_s(y)dy` are positive Radon measures, the continuity theorem for Laplace transforms yields vague convergence

\[
 e_s(y)\,dy\Longrightarrow dy.
\]

Consequently

\[
 \boxed{
 I_s(y)\longrightarrow y
 }
 \tag{L-91028.4}
\]

for every `y>=0`, locally uniformly in `y`, because the distribution functions `I_s` are nondecreasing and the limiting distribution function is continuous.

## 2. One-sided slope upgrades the convergence

Put

\[
 r_s=\frac{c_s}{s}.
\]

Then `0<r_s<1` and `r_s->1`. Moreover

\[
 \boxed{
 e_s(y)+r_sy
 =\sum_{\log n\le y/s}\frac{F_s(n)}n
 }
 \tag{L-91028.5}
\]

is nondecreasing in `y`.

This one-sided slope property upgrades the integrated convergence to the lower pointwise estimate

\[
 \boxed{
 \liminf_{s\downarrow0}
 \inf_{\delta\le y\le Y}e_s(y)\ge1
 \qquad(0<\delta<Y<\infty).
 }
 \tag{L-91028.6}
\]

### Proof

If (L-91028.6) failed, there would be `epsilon>0`, `s_j->0`, and `y_j in [delta,Y]` with

\[
 e_{s_j}(y_j)\le1-\epsilon.
\]

For sufficiently large `j`, `r_(s_j)<=2`. By monotonicity of (L-91028.5), for

\[
 y_j-\epsilon/4\le y\le y_j
\]

(after reducing the fixed interval length if necessary to remain above `delta/2`),

\[
 e_{s_j}(y)
 \le e_{s_j}(y_j)+r_{s_j}(y_j-y)
 \le1-\epsilon/2.
\]

This forces a fixed deficit in

\[
 I_{s_j}(y_j)-I_{s_j}(y_j-\epsilon/4),
\]

contradicting the locally uniform convergence `I_s(y)->y`.

## 3. Scaled Green-removal density

Align the Cauchy scale by `a=s/2`, and retain

\[
 \kappa=\sqrt{275/14}.
\]

Define

\[
 b_s(y)
 =\frac2s\mathcal B_{s,s/2}(y/s).
\]

By `L-91026`,

\[
 \boxed{
 b_s(y)
 =-2r_s+\kappa e_s(y)+2I_s(y).
 }
 \tag{L-91028.7}
\]

For every fixed `0<delta<Y`, (L-91028.4), (L-91028.6), and `r_s->1` give

\[
 \liminf_{s\downarrow0}
 \inf_{\delta\le y\le Y}b_s(y)
 \ge\kappa-2+2\delta>0.
 \tag{L-91028.8}
\]

## 4. Uniform control near zero

Because (L-91028.5) starts from the unit atom,

\[
 e_s(y)\ge1-r_sy,
\]

and hence

\[
 I_s(y)\ge y-\frac{r_s}{2}y^2.
\]

Therefore

\[
 \boxed{
 b_s(y)
 \ge
 \kappa+2y-r_s(2+\kappa y+y^2)
 \ge
 \kappa-2+(2-\kappa)y-y^2.
 }
 \tag{L-91028.9}
\]

The last quadratic is positive on

\[
 0\le y\le\frac7{10}.
\]

Indeed its positive root is approximately `0.7615394489`.

Thus the small-`y` region is controlled uniformly for every `s>0`, without a limiting argument.

## 5. Uniform control at large scaled time

Fix `Y=2`. From (L-91028.4), for all sufficiently small `s`,

\[
 I_s(2)>\frac32.
\]

Since `I_s` is nondecreasing and `e_s>=0`, for every `y>=2`,

\[
 b_s(y)
 \ge-2r_s+2I_s(y)
 >-2+3=1.
\]

On the remaining compact interval `[7/10,2]`, (L-91028.8) gives uniform positivity for all sufficiently small `s`.

Combining the three regions proves:

\[
 \boxed{
 \exists s_0>0\ \text{such that}\
 \mathcal B_{s,s/2}(t)>0
 \quad
 (0<s<s_0,\ t>=0).
 }
 \tag{L-91028.10}
\]

Equivalently, there exists `a_0>0` such that

\[
 \boxed{
 \mathcal B_{2a,a}(t)>0
 \quad
 (0<a<a_0,\ t>=0).
 }
 \tag{L-91028.11}
\]

## 6. Consequence

Together with the terminal theorem `L-91027`, the unresolved arithmetic Green-removal scales lie in one compact interval

\[
 \boxed{
 a_0\le a<\frac12.
 }
\]

For each such scale, `L-91026` further restricts the time variable to a compact interval of knot left limits.

Thus the remaining arithmetic gate is compact in both the scale and logarithmic-time variables.

This theorem is non-effective as stated: no numerical value of `a_0` is claimed. Making it effective requires quantitative uniform control in the zeta pole-scaling limit. The completed critical-boundary intertwiner remains a separate RH-bearing obligation.