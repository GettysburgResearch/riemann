# L-91002 — Positive fractional-part convolution powers and a strict safe-line contraction

Claim ID: `L-91002`  
Title: Every power of the reciprocal Li amplifier is the Laplace transform of a positive fractional-part convolution, while on the fixed safe line `Re s=3` the complete multiplier is uniformly smaller than `3/4`  
Status: **PROPOSED COMPLETE EXACT ANALYTIC LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-12  
Dependencies: `L-91001`; elementary convolution and an integral bound for `zeta(3)`  
Scope: positive kernel and one-sided safe-line contraction; the reflected critical-boundary term is not controlled here

## 1. Positive time-domain kernel

Put

\[
\theta(t)=\{e^t\},
\qquad t\ge0.
\tag{L-91002.1}
\]

Then `0<=theta(t)<1` and `L-91001` gives

\[
A(s)=s\,\mathcal L\theta(s)
=s\int_0^\infty\theta(t)e^{-st}\,dt,
\qquad \operatorname{Re}s>0.
\tag{L-91002.2}
\]

For every integer `r>=1`, the Laplace convolution theorem gives

\[
\boxed{
A(s)^r
=s^r\int_0^\infty\theta^{*r}(t)e^{-st}\,dt.
}
\tag{L-91002.3}
\]

The convolution density is pointwise nonnegative.

## 2. Universal simplex bound

Since every factor `theta` is bounded by one,

\[
0\le\theta^{*r}(t)
\le\operatorname{vol}
\{(t_1,\ldots,t_r)\ge0:\ t_1+\cdots+t_r=t\}.
\]

Therefore

\[
\boxed{
0\le\theta^{*r}(t)
\le\frac{t^{r-1}}{(r-1)!}.
}
\tag{L-91002.4}
\]

For real `sigma>0`, (L-91002.2) has the probability form

\[
A(\sigma)=
\int_0^\infty \theta(t)\,\sigma e^{-\sigma t}\,dt,
\tag{L-91002.5}
\]

so

\[
\boxed{0<A(\sigma)<1.}
\tag{L-91002.6}
\]

The strict inequalities hold because `theta` is nonzero on a positive-measure set and is strictly below one almost everywhere.

## 3. Uniform contraction on `Re s=3`

From the definition,

\[
A(s)
=\frac1{s-1}-[\zeta(s)-1].
\tag{L-91002.7}
\]

Hence, for `Re s=3`,

\[
|A(s)|
\le\frac1{|s-1|}+\sum_{n=2}^\infty n^{-3}
\le\frac12+\sum_{n=2}^\infty n^{-3}.
\tag{L-91002.8}
\]

The elementary decreasing-integral bound gives

\[
\sum_{n=2}^\infty n^{-3}
<\frac18+\int_2^\infty x^{-3}\,dx
=\frac14.
\tag{L-91002.9}
\]

Therefore

\[
\boxed{
\sup_{t\in\mathbb R}|A(3+it)|<\frac34.
}
\tag{L-91002.10}
\]

In particular,

\[
\boxed{
|A(3+it)|^r\le(3/4)^r.
}
\tag{L-91002.11}
\]

This is a genuine exponential contraction on a fixed absolutely convergent Euler line.

## 4. Safe Euler representation

On `Re s=3`, both terms in

\[
A(s)=\frac1{s-1}-\sum_{n=2}^\infty n^{-s}
\tag{L-91002.12}
\]

are absolutely convergent. Hence every finite power admits a completely explicit convergent Euler expansion. Equivalently, (L-91002.3) expresses the same power through one positive convolution kernel.

Thus the nonlinear moment route has two complementary exact coordinates:

```text
Euler coordinate:
    finite products of an absolutely convergent Dirichlet series;

physical coordinate:
    positive fractional-part convolution theta^{*r}.
```

## 5. What the contraction does and does not prove

The strict line bound (L-91002.10) controls the right safe boundary of a contour argument. It does not control the reflected boundary. A symmetric completed-zero multiplier necessarily introduces `A(1-s)^r`, and on `Re s=3` that reflected factor is not covered by (L-91002.10).

This obstruction is made explicit in `R-91001`. Therefore no RH conclusion is inferred from the one-sided contraction alone.

## 6. Proof boundary

Closed exactly here:

1. positive convolution powers;
2. the simplex majorant;
3. strict real-axis contraction;
4. the uniform `3/4` safe-line bound;
5. the absolutely convergent Euler representation.

Open:

1. cancellation/control of the reflected critical boundary;
2. subexponential growth of the weighted zero moments;
3. RH.