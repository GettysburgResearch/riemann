# L-34009 — The adverse Brownian shifts have the exact square threshold N = 4 i^2

Claim ID: `L-34009`

Status: **PROPOSED COMPLETE EXACT ALL-PARAMETER THEOREM — INDEPENDENT REVIEW REQUESTED**

Created: 2026-08-09

Dependencies: `L-34003`, `L-34007`

Scope: exact sign classification of every linear shift in the all-`N` Brownian exponential numerator; no half-plane zero-free theorem and no RH claim

## 1. The shifts

Recall

\[
H_N(z)
=\sum_{i=1}^N
 C_{N,i}i^{-2z}(z+\alpha_{N,i}),
\qquad C_{N,i}>0,
\]

with

\[
\boxed{
\alpha_{N,i}
=i\bigl(H_{N+i}-H_{N-i}\bigr)-\frac12
=i\sum_{k=N-i+1}^{N+i}\frac1k-\frac12.
}
\tag{L-34009.1}
\]

The first low-frequency shifts become negative as `N` grows.  Their sign has an exact closed classification.

## 2. The theorem

For every

\[
1\le i\le N,
\]

one has

\[
\boxed{
\alpha_{N,i}<0
\iff
N\ge4i^2.
}
\tag{L-34009.2}
\]

Equivalently,

\[
\boxed{
\alpha_{N,i}>0
\iff
N\le4i^2-1.
}
\tag{L-34009.3}
\]

There is no zero case.  Thus the complete adverse packet is exactly

\[
\boxed{
1\le i\le\left\lfloor\frac{\sqrt N}{2}\right\rfloor.
}
\tag{L-34009.4}
\]

## 3. Positive side: N <= 4 i^2 - 1

For fixed `i`, the harmonic block

\[
\sum_{k=N-i+1}^{N+i}\frac1k
\]

strictly decreases with `N`.  Hence it is enough to take

\[
N=4i^2-1.
\]

For a positive decreasing function, the left-endpoint sum dominates its integral. Therefore

\[
\begin{aligned}
\sum_{k=4i^2-i}^{4i^2+i-1}\frac1k
&>
\int_{4i^2-i}^{4i^2+i}\frac{dx}{x}\\
&=\log\frac{4i^2+i}{4i^2-i}\\
&=2\operatorname{artanh}\frac1{4i}.
\end{aligned}
\tag{L-34009.5}
\]

Since `artanh t>t` for every `t>0`,

\[
2\operatorname{artanh}\frac1{4i}
>\frac1{2i}.
\tag{L-34009.6}
\]

Multiplying by `i` gives

\[
i\sum_{k=N-i+1}^{N+i}\frac1k>\frac12,
\]

and hence

\[
\boxed{\alpha_{N,i}>0}
\tag{L-34009.7}
\]

for every `N<=4i^2-1`.

## 4. Negative side: N >= 4 i^2

Again the harmonic block decreases with `N`, so it is enough to prove negativity at

\[
N=4i^2.
\]

The function `x -> 1/x` is strictly convex.  Hence on every unit interval centered at an integer,

\[
\frac1k
<\int_{k-1/2}^{k+1/2}\frac{dx}{x}.
\]

Summing the `2i` intervals gives

\[
\begin{aligned}
\sum_{k=4i^2-i+1}^{4i^2+i}\frac1k
&<
\log\frac{4i^2+i+1/2}{4i^2-i+1/2}\\
&=2\operatorname{artanh}x_i,
\end{aligned}
\tag{L-34009.8}
\]

where

\[
x_i
=\frac{i}{4i^2+1/2}.
\tag{L-34009.9}
\]

Put

\[
t=\frac1{4i}\le\frac14.
\]

Then exactly

\[
\boxed{x_i=\frac{t}{1+2t^2}.}
\tag{L-34009.10}
\]

We claim

\[
\operatorname{artanh}x_i<t.
\tag{L-34009.11}
\]

Indeed, for `0<x<1`,

\[
\operatorname{artanh}x
=x+\sum_{r\ge1}\frac{x^{2r+1}}{2r+1}
\le x+\frac{x^3}{3(1-x^2)}.
\tag{L-34009.12}
\]

Since `x_i<=t<=1/4`,

\[
\frac{x_i^3}{3(1-x_i^2)}
\le\frac{16}{45}t^3.
\tag{L-34009.13}
\]

On the other hand

\[
t-x_i
=\frac{2t^3}{1+2t^2}
\ge\frac{16}{9}t^3,
\tag{L-34009.14}
\]

because `2t^2<=1/8`.  Equations (L-34009.13)--(L-34009.14) give the strict inequality (L-34009.11).

Therefore (L-34009.8) gives

\[
\sum_{k=N-i+1}^{N+i}\frac1k
<2t=\frac1{2i}.
\]

Multiplying by `i`,

\[
i\sum_{k=N-i+1}^{N+i}\frac1k<\frac12,
\]

so

\[
\boxed{\alpha_{N,i}<0}
\tag{L-34009.15}
\]

for `N=4i^2`, and hence for every larger `N` as well.

Sections 3--4 prove (L-34009.2).

## 5. Canonical-product interpretation

By `L-34007`,

\[
\alpha_{N,i}
=-\frac12
+2i^2\sum_{k>N}\frac1{k^2-i^2}.
\tag{L-34009.16}
\]

Thus the exact transition `N=4i^2` says:

> the positive Stieltjes score contributed by the undeleted sine-product tail falls below the critical square-root derivative `1/2` precisely when the deletion depth reaches four times the square of the sampled zero index.

This gives an intrinsic meaning to the square-root packet scale.

## 6. Consequence for the global Brownian attack

The low-frequency packet which cannot be treated termwise has cardinality

\[
\boxed{
\#\{i:\alpha_{N,i}<0\}
=\left\lfloor\frac{\sqrt N}{2}\right\rfloor.
}
\tag{L-34009.17}
\]

This explains the phenomenon seen in the `N=4` stability proof and in large-`N` reconnaissance:

```text
fixed N=2,3:      no adverse shifts;
N=4,...,15:       exactly one adverse shift;
N=16,...,35:      exactly two;
N=36,...,63:      exactly three;
...
general N:        sqrt(N)/2 adverse packet.
```

Therefore a cofinal sector/Rouche proof cannot be based on a fixed number of specially handled low-frequency terms.  The correct target is a **growing packet theorem on the natural i~sqrt(N) scale**.

At the same time, the classification reduces the rest of the numerator to the manifestly positive-shift sector

\[
i>\sqrt N/2.
\]

Any future canonical/Hermite argument may therefore concentrate all delicate sign geometry into one explicitly delimited packet.

## 7. Proof boundary

Closed exactly:

1. the sign of every `alpha_(N,i)`;
2. the sharp transition `N=4i^2`;
3. exact cardinality of the adverse packet;
4. the square-root scaling law as an exact theorem rather than an asymptotic observation.

Open:

1. collective control of the `i<=sqrt(N)/2` packet;
2. cofinal half-plane stability;
3. RH.
