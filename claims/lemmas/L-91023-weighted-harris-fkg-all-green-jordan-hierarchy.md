# L-91023 — Weighted Harris–FKG gives the complete all-Green Jordan hierarchy

Claim ID: `L-91023`  
Status: **PROPOSED COMPLETE ARITHMETIC/BERNSTEIN THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-12  
Depends on: `L-91022`; Harris association for product measures  
RH status: **unproved**

## 1. Weighted logarithmic domination

For `s>0`, put

\[
 F_s(n)=\prod_{p\mid n}(1-p^{-s}),
 \qquad
 c_s=\frac1{\zeta(1+s)},
 \qquad
 P_s(N)=\prod_{p\le N}(1-p^{-1-s}).
\]

Let `h:N->R_{>=0}` be nonincreasing and supported on `1,...,N`. Then

\[
 \boxed{
 \sum_{n\le N}\frac{F_s(n)}n h(n)
 \ge
 P_s(N)\sum_{n\le N}\frac{h(n)}n
 >
 c_s\sum_{n\le N}\frac{h(n)}n.
 }
 \tag{L-91023.1}
\]

This strictly strengthens the unweighted inequality of `L-91022`.

### Proof

Use the independent geometric prime-exponent model of `L-91022`:

\[
 \Pr(E_p=k)=(1-p^{-1})p^{-k},
 \qquad
 M=\prod_{p\le N}p^{E_p}.
\]

The two functions

\[
 E\longmapsto F_s(M),
 \qquad
 E\longmapsto h(M)\mathbf 1_{M\le N}
\]

are coordinatewise nonincreasing. Harris association gives

\[
 \mathbb E\!\left[F_s(M)h(M)\mathbf 1_{M\le N}\right]
 \ge
 \mathbb E[F_s(M)]
 \mathbb E\!\left[h(M)\mathbf 1_{M\le N}\right].
\]

The common product-measure normalization cancels, while

\[
 \mathbb E[F_s(M)]=P_s(N).
\]

This proves the first inequality. The second follows because the finite Euler product is strictly larger than the complete product `c_s`.

## 2. Every truncated logarithmic power is positive

For `m>=0` and `t>=0`, define

\[
 h_{t,m}(n)=\frac{(t-\log n)_+^m}{m!}.
\]

This is nonnegative and nonincreasing in `n`. Put

\[
 \boxed{
 E_{s,m}(t)
 =
 \sum_{n\ge1}\frac{F_s(n)}n
 \frac{(t-\log n)_+^m}{m!}
 -c_s\frac{t^{m+1}}{(m+1)!}.
 }
 \tag{L-91023.2}
\]

Then

\[
 \boxed{E_{s,m}(t)>=0\qquad(s>0,m>=0,t>=0),}
 \tag{L-91023.3}
\]

with strict inequality for `t>0`.

Indeed, with `N=floor(e^t)`, (L-91023.1) gives the finite-product lower bound. The function

\[
 x\longmapsto \frac{(t-\log x)^m}{m!x}
\]

is decreasing on `[1,e^t]`, so its left Riemann sum dominates its integral:

\[
 \sum_{n\le e^t}\frac{(t-\log n)^m}{m!n}
 \ge
 \int_1^{e^t}\frac{(t-\log x)^m}{m!x}\,dx
 =\frac{t^{m+1}}{(m+1)!}.
\]

Combining this with `P_s(N)>c_s` proves (L-91023.3).

## 3. Exact all-Green Laplace hierarchy

Let

\[
 Z_s(q)=\frac{\zeta(1+q)}{\zeta(1+s+q)}
 =\sum_{n\ge1}\frac{F_s(n)}{n^{1+q}},
 \qquad q>0.
\]

Termwise Laplace integration gives

\[
 \int_0^\infty e^{-qt}
 \frac{(t-\log n)_+^m}{m!}\,dt
 =\frac{n^{-q}}{q^{m+1}}.
\]

Therefore

\[
 \boxed{
 \int_0^\infty e^{-qt}E_{s,m}(t)\,dt
 =
 \frac{Z_s(q)-c_s/q}{q^{m+1}}.
 }
 \tag{L-91023.4}
\]

Consequently, for every integer `m>=0`,

\[
 \boxed{
 q\longmapsto
 \frac{Z_s(q)-c_s/q}{q^{m+1}}
 \text{ is completely monotone.}
 }
 \tag{L-91023.5}
\]

This is the complete Volterra/Green tower, not merely the first centered channel.

## 4. Phase-resolved positive kernels

For complex `z,w` with positive real parts, define

\[
 \boxed{
 K_{s,m}(z,w)
 =
 \frac{Z_s(z+\overline w)-c_s/(z+\overline w)}
 {(z+\overline w)^{m+1}}.
 }
 \tag{L-91023.6}
\]

Using (L-91023.4),

\[
 K_{s,m}(z,w)
 =\int_0^\infty
 e^{-zt}\overline{e^{-wt}}E_{s,m}(t)\,dt.
\]

Hence every finite matrix

\[
 \boxed{
 \bigl(K_{s,m}(z_i,z_j)\bigr)_{i,j}
 \succeq0.
 }
 \tag{L-91023.7}
\]

Vertical phases are retained exactly; no absolute value is taken termwise in the Dirichlet series.

## 5. Completed factors

The positive rational and beta/Gamma factors used in `L-9506` and `L-91022` are Laplace transforms of positive measures. Multiplying (L-91023.4) by any finite product of these factors corresponds to additive convolution of positive representing measures. Thus the complete centered Jordan channel remains positive after an arbitrary finite number of Green divisions.

## 6. Exact boundary

Closed here:

1. weighted logarithmic Jordan domination for every decreasing test;
2. positivity of every truncated logarithmic-power discrepancy;
3. complete monotonicity after every finite Green division;
4. phase-resolved PSD kernels on the safe half-plane.

Still open:

1. removal of the final Green factors by the Cauchy-storage numerator;
2. the completed critical-boundary Cauchy–Jordan intertwiner;
3. RH.

The next legitimate operation is therefore not another smoothing. It is the exact finite-order boundary jet that removes the Green factors while accounting for every boundary contact.