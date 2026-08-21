# M-21501 — Full RH attack through prime-power polygon domination

Claim ID: `M-21501`  
Title: Replace the packet/capture forest by one convex-order theorem on finite prime-power prefixes  
Status: `PROPOSED RESEARCH PROGRAM`  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Dependencies: `L-21501`, `T-21501`, `L-19801`--`L-19804`, `L-20704/L-20705`

## 1. Strategic reset

The current repository contains many correct finite adapters:

```text
radical and Xi-cardinal coordinates;
weighted-deficit packet capture;
three-block/direct Schur shorting;
terminal-prime and square-screw scalar channels;
finite directed positive and negative interfaces.
```

They all meet the same immutable arithmetic obstruction. The constant D-0001 coordinate is the square-screw statistic, and the square-screw negative exponent is the rightmost-zero displacement. More matrix conditioning cannot change that scalar.

`L-21501/T-21501` therefore make the scalar obstruction the front-stage attack:

```text
explicit strictly convex archimedean curve F*
versus
finite prime-power moment polygon through (A_j,B_j).
```

RH is exactly eventual polygon domination.

## 2. Convex-order interpretation

The second derivatives are

\[
G''=\sum_j a_j\delta_{\nu_j},
\qquad
F''(t)
=e^{t/2}-{e^{-5t/2}\over1-e^{-2t}}
\quad(t\ge\log2).
\tag{M-21501.1}
\]

Thus the arithmetic object is a discrete positive measure on logarithmic prime-power locations, while the reference is an explicit positive continuous measure with the trivial-zero correction already included.

The derivatives of the conjugates are their quantile functions:

\[
(G^*)'(A)=\nu_j
\quad(A_{j-1}<A<A_j),
\qquad
(F^*)'(A)=t(A).
\tag{M-21501.2}
\]

Hence

\[
B_j-F^*(A_j)
=
\text{constant}
+
\int_0^{A_j}
\bigl((G^*)'(A)-(F^*)'(A)\bigr)dA.
\tag{M-21501.3}
\]

The full RH theorem is therefore a one-sided integrated-quantile, Lorenz-order, or stop-loss domination statement. This opens a constructive route: build a mass transport from the archimedean reference measure to prime-power atoms whose cumulative barycentric cost is never negative.

## 3. Three serious attack modes

### A. Block transport / majorization

Partition the prime-power mass axis at prefixes

\[
0=j_0<j_1<j_2<\cdots.
\]

A sufficient block certificate is

\[
B_{j_r}-B_{j_{r-1}}
\ge
F^*(A_{j_r})-F^*(A_{j_{r-1}})
\tag{M-21501.4}
\]

for every block, together with one finite initial moat. The right side is the exact first moment of the reference quantile on the same mass interval. This permits negative individual arrivals but forbids a cumulative transport deficit.

The useful question is no longer “bound every prime error absolutely.” It is:

```text
Can Selberg-type convolution identities or a multiplicative allocation
construct these barycentric blocks with a one-sided remainder?
```

### B. Finite Euler curvature

For

\[
\mathcal Z_Q(s)=
\exp\sum_{p^k\le Q}{1\over kp^{ks}},
\]

one has

\[
A_Q=-(\log\mathcal Z_Q)'(1/2),
\qquad
B_Q=(\log\mathcal Z_Q)''(1/2).
\]

The target is the nonlinear curvature barrier

\[
(\log\mathcal Z_Q)''(1/2)
\ge
F^*\bigl(- (\log\mathcal Z_Q)'(1/2)\bigr).
\tag{M-21501.5}
\]

Ordinary log-convexity is insufficient: it yields only

\[
B_Q\log\mathcal Z_Q(1/2)\ge A_Q^2,
\]

and PNT asymptotics show that this generic bound misses the sharp threshold by order `sqrt(Q)/log Q`, whereas the RH-sensitive gap is order one. Any successful curvature proof must use multiplicative structure beyond Cauchy--Schwarz.

### C. Directed negative search

`T-21501.7` gives a complete finite semidecision for false RH. Enumerate prime-power prefixes and rational trial radii `r>=sqrt(2)`, and certify

\[
2A_j\log r-F(2\log r)-B_j>0.
\tag{M-21501.6}
\]

No zero table is needed. If RH is false, a strict certificate exists and exhaustive directed search eventually finds one. The exact verifier `X-21501` contracts such a proof object.

This search should run in parallel with the positive transport attack. It is not a heuristic sign scan: a passing witness is an unconditional disproof.

## 4. Why the polygon is stronger operationally than square sampling

The square criterion evaluates one prescribed support `t=2log N`. The polygon criterion optimizes the archimedean tangent against every complete prime-power prefix. It has four advantages:

1. every candidate is a complete finite prefix rather than an arbitrary support;
2. the one-dimensional optimizer is explicit and strictly convex;
3. a violated vertex automatically manufactures the negative screw point;
4. the vertex-deficit exponent is exactly `Theta_zeta`.

The criterion remains RH-equivalent, but the geometry identifies the correct proof object: a cumulative moment polygon, not a low eigenvector or a phase sample.

## 5. Ordinary reconnaissance, not evidence

A small non-directed Python reconnaissance using all 18,120 prime powers through `199999` found

```text
min_j [B_j-F*(A_j)] approximately 0.02752057335
attained near q_j=3089;
no negative vertex was observed.
```

This is only a normalization and implementation check. It is neither a directed certificate nor evidence for the cofinal inequality.

The same experiment verifies numerically that scaling the prime masses by `1.02` creates a positive dual deficit and that the sampled maximum of `G-F` agrees with the maximum vertex deficit, as predicted by `L-21501.14`.

## 6. Exact next theorem

The highest-value mathematical target is not another equivalence. It is one of the following genuinely stronger statements:

1. an explicit block transport proving (M-21501.4) cofinally;
2. a multiplicative curvature inequality proving (M-21501.5) cofinally;
3. a new one-sided Selberg identity whose remainder is the polygon gap plus a positive square.

Any one of these proves RH through `T-21501`. A proof that only gives comparable growth, average sign, or an absolute PNT error does not reach the threshold.

## 7. Status boundary

- `L-21501/T-21501` are proposed theorems pending independent review.
- The finite negative checker is exact algebra conditional on its directed input bindings.
- The positive transport/curvature theorem is not proved.
- No public RH claim is made.
