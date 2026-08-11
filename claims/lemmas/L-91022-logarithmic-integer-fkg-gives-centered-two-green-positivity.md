# L-91022 — Logarithmic integers and Harris–FKG give unconditional centered two-Green positivity

Claim ID: `L-91022`  
Status: **PROPOSED COMPLETE ARITHMETIC/BERNSTEIN THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-9506`; Harris association for product measures  
RH status: **unproved**

## 1. The generalized-totient logarithmic sum

For `s>0`, define

\[
 F_s(n)=\prod_{p\mid n}(1-p^{-s}),
 \qquad
 c_s=\frac1{\zeta(1+s)}.
 \tag{L-91022.1}
\]

Put

\[
 A_s(N)=\sum_{n\le N}\frac{F_s(n)}n,
 \qquad
 H_N=\sum_{n\le N}\frac1n.
 \tag{L-91022.2}
\]

Then for every integer `N>=1`,

\[
 \boxed{
 \frac{A_s(N)}{H_N}
 \ge
 \prod_{p\le N}(1-p^{-1-s})
 >c_s.
 }
 \tag{L-91022.3}
\]

Consequently, for every real `x>=1`,

\[
 \boxed{
 \sum_{n\le x}\frac{F_s(n)}n
 \ge c_s\log x.
 }
 \tag{L-91022.4}
\]

The inequality is strict for `x>1`.

## 2. Product-measure proof

Let `P_N` be the primes not exceeding `N`. For each `p in P_N`, let `E_p` be independent geometric variables with

\[
 \Pr(E_p=k)=(1-p^{-1})p^{-k},
 \qquad k=0,1,2,\ldots.
 \tag{L-91022.5}
\]

Define the random `P_N`-smooth integer

\[
 M=\prod_{p\le N}p^{E_p}.
\]

Its unconditioned mass is proportional to `1/M`. Conditional on the decreasing event

\[
 \mathcal D_N=\{M\le N\},
\]

one has exactly

\[
 \boxed{
 \Pr(M=n\mid\mathcal D_N)=\frac1{nH_N}
 \qquad(1\le n\le N).
 }
 \tag{L-91022.6}
\]

The function

\[
 G(E)=\prod_{p:E_p>0}(1-p^{-s})=F_s(M)
\]

is coordinatewise decreasing, and so is the indicator of `D_N`. Harris–FKG association for the product law gives

\[
 \mathbb E[G\mid\mathcal D_N]\ge\mathbb E[G].
 \tag{L-91022.7}
\]

The two sides are

\[
 \mathbb E[G\mid\mathcal D_N]=\frac{A_s(N)}{H_N},
\]

and, by independence,

\[
 \mathbb E[G]
 =\prod_{p\le N}
 \left[(1-p^{-1})+p^{-1}(1-p^{-s})\right]
 =\prod_{p\le N}(1-p^{-1-s}).
\]

This proves (L-91022.3). Since `H_N>=log(N+1)` and `x<N+1` for `N=floor(x)`, (L-91022.4) follows.

## 3. Positive cumulative discrepancy

Put

\[
 \boxed{
 E_s(t)
 =\sum_{\log n\le t}\frac{F_s(n)}n-c_st
 \qquad(t\ge0).
 }
 \tag{L-91022.8}
\]

Then

\[
 \boxed{E_s(t)>0\quad(t\ge0).}
 \tag{L-91022.9}
\]

The arithmetic ratio

\[
 Z_s(q)=\frac{\zeta(1+q)}{\zeta(1+s+q)}
 =\sum_{n\ge1}\frac{F_s(n)}{n^{1+q}}
 \qquad(q>0)
 \tag{L-91022.10}
\]

therefore satisfies

\[
 \boxed{
 \frac1q\left[Z_s(q)-\frac{c_s}{q}\right]
 =\int_0^\infty e^{-qt}E_s(t)\,dt.
 }
 \tag{L-91022.11}
\]

Hence the regularized arithmetic channel becomes completely monotone after one Green division.

## 4. Completed centered two-Green lift

Retain the positive rational and beta/Gamma factors of `L-9506`,

\[
 R_s(q)=\frac{q+1}{(q+s)(q+s+1)},
 \qquad
 B_s(q)=\pi^{s/2}
 \frac{\Gamma((1+q)/2)}{\Gamma((1+s+q)/2)}.
\]

The centered completed one-Green channel is

\[
 \mathcal G_s(q)
 =R_s(q)B_s(q)
 \left[Z_s(q)-\frac{c_s}{q}\right].
 \tag{L-91022.12}
\]

Since `R_s`, `B_s`, and the right side of (L-91022.11) are completely monotone, their product is completely monotone. Therefore

\[
 \boxed{
 \frac{\mathcal G_s(q)}q
 \text{ is completely monotone on }(0,\infty).
 }
 \tag{L-91022.13}
\]

Equivalently, every finite matrix

\[
 \boxed{
 \left(
 \frac{\mathcal G_s((q_i+q_j)/2)}{(q_i+q_j)/2}
 \right)_{i,j}
 \succeq0
 }
 \tag{L-91022.14}
\]

for positive `q_i`.

The representing positive density is the additive convolution of:

1. the rational density `r_s` of `L-9506`;
2. the beta/Gamma density `b_s` of `L-9506`;
3. the positive cumulative arithmetic discrepancy `E_s(t)dt`.

## 5. Exact significance and firewall

This theorem closes the first centered arithmetic domination in the Jordan/Volterra stack. It is stronger than positivity of the uncentered one-Green ratio: the canonical pole density has already been subtracted.

It still does not prove RH. The extra Green division is load-bearing. A derivative or boundary-removal step is needed to recover the Cauchy-storage innovation of `T-91007`, and positivity need not survive that step automatically.

The control models of PR #398 also remain applicable as a firewall: separate safe-side positivity, even after centering and smoothing, does not by itself imply the target critical-boundary Pick kernel. The exact completed output coupling must still be constructed.

## 6. Special totient case

At `s=1`,

\[
 F_1(n)=\frac{\varphi(n)}n,
 \qquad c_1=\frac6{\pi^2}.
\]

Equation (L-91022.4) gives the elementary inequality

\[
 \boxed{
 \sum_{n\le x}\frac{\varphi(n)}{n^2}
 \ge\frac6{\pi^2}\log x
 \qquad(x\ge1).
 }
 \tag{L-91022.15}
\]

This is the cumulative positive reserve underlying the semicircle-totient and centered one-Green routes.

## 7. Boundary

```text
finite logarithmic Jordan domination            PROPOSED COMPLETE
positive cumulative discrepancy E_s             PROPOSED COMPLETE
regular arithmetic channel / q is CM             PROPOSED COMPLETE
completed centered two-Green lift                 PROPOSED COMPLETE
removal of the final Green division               OPEN / RH-BEARING
completed Cauchy--Jordan boundary intertwiner      OPEN / RH-EQUIVALENT
Riemann Hypothesis                                UNPROVED
```
