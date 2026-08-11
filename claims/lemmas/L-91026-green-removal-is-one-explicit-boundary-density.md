# L-91026 — Removing the final Green factors produces one explicit boundary density

Claim ID: `L-91026`  
Status: **EXACT BOUNDARY-JET REDUCTION + UNCONDITIONAL PARTIAL POSITIVITY**  
Created: 2026-08-12  
Depends on: `L-91020`, `L-91023`  
RH status: **unproved**

## 1. General boundary-jet identity

Let `rho` be supported on `[0,infinity)`, piecewise smooth with distributional derivatives, and suppose

\[
 \rho(0)=\rho'(0)=0.
\]

Write

\[
 F(q)=\int_0^\infty e^{-qt}\rho(t)\,dt,
 \qquad q>0.
\]

For positive constants `A,B`, Laplace differentiation gives

\[
 \boxed{
 q(q+A)(q+B)F(q)
 =\rho''(0)
 +\int_0^\infty e^{-qt}
 \bigl[\rho'''+(A+B)\rho''+AB\rho'\bigr](t)\,dt.
 }
 \tag{L-91026.1}
\]

Thus multiplying a three-Green channel by the cubic Cauchy numerator creates exactly one boundary contact plus one interior distribution. There is no unspecified endpoint term.

## 2. Apply the identity to the Jordan hierarchy

Retain

\[
 E_{s,m}(t)
 =
 \sum_{n\ge1}\frac{F_s(n)}n
 \frac{(t-\log n)_+^m}{m!}
 -c_s\frac{t^{m+1}}{(m+1)!}
\]

from `L-91023`. Put `rho=E_(s,2)`. Near zero,

\[
 E_{s,2}(t)=\frac{t^2}{2}-c_s\frac{t^3}{6},
\]

so

\[
 \rho(0)=\rho'(0)=0,
 \qquad
 \rho''(0)=1.
\]

Distributionally on the open half-line,

\[
 \rho'=E_{s,1},
 \qquad
 \rho''=E_{s,0},
\]

and

\[
 \rho'''
 =-c_s\,dt
 +\sum_{n\ge2}\frac{F_s(n)}n\delta_{\log n}.
\]

Therefore

\[
 \boxed{
 \begin{aligned}
 &q(q+A)(q+B)
 \frac{Z_s(q)-c_s/q}{q^3}\\
 &\quad=1+
 \sum_{n\ge2}\frac{F_s(n)}n n^{-q}
 +\int_0^\infty e^{-qt}
 \mathcal B_{s;A,B}(t)\,dt,
 \end{aligned}
 }
 \tag{L-91026.2}
\]

where the sole continuous boundary density is

\[
 \boxed{
 \mathcal B_{s;A,B}(t)
 =-c_s+(A+B)E_{s,0}(t)+AB E_{s,1}(t).
 }
 \tag{L-91026.3}
\]

Every atom in (L-91026.2) is positive. Hence

\[
 \boxed{
 \mathcal B_{s;A,B}(t)>=0\ \forall t
 \quad\Longrightarrow\quad
 q(q+A)(q+B)
 \frac{Z_s(q)-c_s/q}{q^3}
 \text{ is completely monotone.}
 }
 \tag{L-91026.4}
\]

This is the exact Green-removal gate.

## 3. The Cauchy-storage parameters

For the sharp sixteenfold factor of `L-91020`, let

\[
 \alpha+\beta=\frac{163}{14},
 \qquad
 \alpha\beta=16,
\]

and set

\[
 \kappa=\sqrt\alpha+\sqrt\beta
 =\sqrt{\frac{275}{14}}.
\]

Take

\[
 A=\sqrt\alpha\,a,
 \qquad
 B=\sqrt\beta\,a.
\]

Then

\[
 A+B=\kappa a,
 \qquad
 AB=4a^2,
\]

and the boundary density becomes

\[
 \boxed{
 \mathcal B_{s,a}(t)
 =-c_s+\kappa a E_{s,0}(t)+4a^2E_{s,1}(t).
 }
 \tag{L-91026.5}
\]

The source parameter naturally aligned with the Cauchy dilation is `s=2a`.

## 4. Exact first-cell positivity

Put `c=c_(2a)` and `L=log 2`. On `0<=t<L`, only the unit atom is active, so

\[
 E_{2a,0}(t)=1-ct,
 \qquad
 E_{2a,1}(t)=t-\frac c2t^2.
\]

Hence

\[
 \mathcal B_{2a,a}(t)
 =-c+\kappa a(1-ct)
 +4a^2\left(t-\frac c2t^2\right).
 \tag{L-91026.6}
\]

This is concave in `t`, so its minimum on the first cell occurs at an endpoint.

At `t=0`,

\[
 \mathcal B_{2a,a}(0)=\kappa a-c>0,
\]

because

\[
 c=\zeta(1+2a)^{-1}<2a<\kappa a.
\]

At `t=L`, split into two ranges.

If `0<a<=1/2`, use `c<2a` to obtain

\[
 \mathcal B_{2a,a}(L)
 >a\left[(\kappa-2)+(4-2\kappa)La-4L^2a^2\right].
\]

The bracket decreases on this interval, and at `a=1/2` it equals

\[
 (\kappa-2)(1-L)-L^2>0.
\]

If `a>=1/2`, use `c<1` to obtain

\[
 \mathcal B_{2a,a}(L)
 >\kappa(1-L)a+(4L-2L^2)a^2-1.
\]

The right side increases in `a` and is positive at `a=1/2`. Therefore

\[
 \boxed{
 \mathcal B_{2a,a}(t)>0
 \qquad(0<=t<=\log2,\ a>0).
 }
 \tag{L-91026.7}
\]

The elementary numerical inequalities in the endpoint check may be certified, for example, by

\[
 \kappa>4.43,
 \qquad
 \log2<0.694.
\]

## 5. Eventual positivity and a finite-window reduction

Let

\[
 \delta=1-\log2>0.
\]

At a left-limit knot

\[
 t=\log(N+1),
\]

apply the weighted FKG theorem `L-91023` to the decreasing weight

\[
 h(n)=\kappa a+4a^2(t-\log n),
 \qquad n\le N.
\]

The elementary left-sum bounds are

\[
 H_N\ge t+\delta,
\]

and

\[
 \sum_{n\le N}\frac{t-\log n}{n}
 \ge
 \frac{t^2}{2}+\delta t+\frac{(\log2)^2}{2}.
\]

The second bound follows by comparing with the integral on `[1,N+1]` and retaining the complete surplus from the first cell `[1,2]`.

Since the finite Euler product is larger than `c_(2a)`, these inequalities give

\[
 \boxed{
 \mathcal B_{2a,a}(t)
 >c_{2a}
 \left[
 -1+\kappa a\delta
 +4a^2\delta t
 +2a^2(\log2)^2
 \right].
 }
 \tag{L-91026.8}
\]

Between logarithmic knots, `E_(2a,0)` is affine and `E_(2a,1)'=E_(2a,0)`, so

\[
 \mathcal B_{2a,a}''(t)=-4a^2c_{2a}<0.
\]

At every knot the density jumps upward by

\[
 \kappa a\frac{F_{2a}(n)}n>0.
\]

Therefore minima occur at knot left limits. Equation (L-91026.8) proves

\[
 \boxed{
 \mathcal B_{2a,a}(t)>0
 \quad\text{whenever}\quad
 t>
 T(a):=
 \frac{[1-\kappa a\delta-2a^2(\log2)^2]_+}
 {4a^2\delta}.
 }
 \tag{L-91026.9}
\]

Thus, for every fixed `a`, the Green-removal problem is reduced to the explicit compact interval

\[
 \log2<t\le T(a).
\]

No asymptotic tail remains.

## 6. Exact frontier

Closed here:

1. the complete boundary-jet formula;
2. the unique continuous density after all three Green factors are removed;
3. positivity on the entire first logarithmic cell;
4. unconditional positivity beyond an explicit finite threshold;
5. reduction to one compact arithmetic interval at every scale.

Open:

\[
 \boxed{
 \mathcal B_{2a,a}(t)>=0
 \qquad(a>0,t>0).
 }
\]

Only the compact middle range remains. Proving this scalar density inequality would make the centered arithmetic Cauchy numerator a positive Laplace measure. The separate completed gamma/pole coupling still has to be inserted in the final CJHI assembly; no RH conclusion is claimed here.