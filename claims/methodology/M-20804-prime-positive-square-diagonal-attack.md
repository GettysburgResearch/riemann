# M-20804 — Prime-positive square-diagonal completion programme

Claim ID: `M-20804`  
Status: `PROPOSED RESEARCH PROGRAMME`  
Authoring agent: `gpt56-03-w`  
Created: 2026-08-07  
Primary theorem: `T-20804`

## 1. Exact target

Fix a prime-free base `0<a<log2`, put

\[
 r_n=\left\lceil{2\log n\over a}\right\rceil,
 \qquad t_n={2\log n\over r_n},
\]

and define

\[
 \mathcal J_a(n)
 =r_n^2A(t_n)-A(2\log n)
 +\sum_{q\le n^2}{\Lambda(q)\over\sqrt q}\log{n^2\over q}.
\]

Every arithmetic coefficient is nonnegative. `T-20804` proves

\[
 \mathrm{RH}
 \iff
 (-\mathcal J_a(n))_+=n^{o(1)},
\]

and in particular RH is equivalent to eventual nonnegativity.

The proof programme must therefore establish the cofinal upper envelope

\[
 A(2\log n)
 -\sum_{q\le n^2}{\Lambda(q)\over\sqrt q}\log{n^2\over q}
 \le r_n^2A(t_n)+n^{o(1)}.
\]

The right side is only `O(log^2 n)`. The left side is the complete centered
square-screw scalar.

## 2. Mandatory cancellation order

Never estimate the following channels separately:

```text
A(2 log n)                  size Theta(n)
positive prime ramp         size Theta(n)
final centered difference   RH scale
```

A valid proof must assemble the first two channels before applying an absolute
value, norm, or asymptotic remainder. The direct producer and the prefix-moment
producer must share the same prime-power manifest but otherwise remain
independent.

## 3. Three serious completion mechanisms

### A. Selberg triangular-kernel square

Integrate Selberg's exact identity

\[
 \Lambda\log+\Lambda*\Lambda=\mu*\log^2
\]

against the positive triangular square-cutoff kernel. Preserve
`Lambda*Lambda` as a prime-pair Gram rather than bounding it absolutely. The
objective is an identity of the form

\[
 \mathcal J_a(n)
 =\mathcal E_n^{\rm pair}
  +\mathcal R_n,
 \qquad
 \mathcal E_n^{\rm pair}\ge0,
 \qquad
 (-\mathcal R_n)_+=n^{o(1)}.
\]

PR #216 supplies the matching balanced-semiprime/prime-pair coordinates.

### B. Finite Euler flow with joint centering

`L-20813` rewrites the shifted logarithmic derivative as

```text
positive base-prime drift
+ positive retained-power Selberg convolution.
```

Transport this positive flow from the shrinking strip back to the square
ramp, retaining the exact cumulant defect of `T-20803`. The square and higher
prime-power layers must be centered jointly with the Lerch/gamma correction;
completed Euler factors without the finite cutoff adapter are forbidden.

### C. Convex-polygon contact transport

`T-20802` and PR #219 identify the prime-power polygon and the smooth Fenchel
barrier. The diagonal criterion chooses one explicit tangent budget at each
square cutoff. A block transport proof should show that the incoming polygon
reserve pays every contact drawdown before the next square level. Entrywise
prime domination is not required; cumulative barycentric domination is.

## 4. Directed production object

For each selected `n`, emit:

1. exact `n`, `r_n`, and rational enclosure of `t_n`;
2. duplicate-free prime-power manifest through `n^2`;
3. termwise positive ramp interval;
4. prefix-moment ramp interval;
5. complete directed `A(t_n)` and `A(2log n)` intervals, including monotone
   Lerch tails;
6. overlap of the two ramp producers;
7. final interval for `J_a(n)`;
8. optional Selberg pair-energy and Euler-flow decompositions.

A mutation suite must reject

- omitted prime powers;
- duplicate prime powers;
- endpoint inclusion mistakes;
- a lower base point reaching `log2`;
- independently rounded order-`n` channels with no shared cancellation ledger;
- replacement of the finite prime-power stream by completed Euler factors.

## 5. Block rather than brute force

A finite positive diagonal is not a proof. The intended cofinal certificate is a
block theorem. For a block `N<=n<=N'`, bound the maximum drawdown of the jointly
centered scalar and prove that the incoming reserve covers it. The block may be
represented in any of the following exact coordinates:

- the prime-prefix Fenchel recurrence of `L-20808`;
- the positive shrinking-strip flow of `L-20813`;
- the balanced semiprime Gram of PR #216;
- the convex polygon of PR #219.

The final theorem must quantify over every sufficiently large integer square
cutoff, not merely a sparse subsequence.

## 6. Proof boundary

This methodology identifies a one-scalar, all-positive-prime production target.
It does not supply the required Selberg, Euler-flow, or block-transport bound.
Any successful completion of the displayed cofinal inequality proves RH through
`T-20804`.