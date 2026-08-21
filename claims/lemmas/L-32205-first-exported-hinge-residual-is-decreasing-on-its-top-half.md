# L-32205 — The first exported critical-hinge residual is decreasing on its top half

Claim ID: `L-32205`

Status: **PROPOSED COMPLETE COFINAL ELEMENTARY THEOREM — INDEPENDENT REVIEW REQUESTED**

Created: 2026-08-09

Dependencies: `L-32201`, `L-32204`

Scope: first exported residual of the critical square-root hinge; proves positivity of the complete second dyadic band of its carry inverse.  It does not prove that the second elimination preserves lower nonnegativity, full CHS, or RH.

## 1. Setup

Fix an integer endpoint

\[
T\ge26,
\qquad
N=\lfloor T/2\rfloor\ge13,
\]

and the critical square-root hinge

\[
h_T(q)=q^{-1/2}-T^{-1/2},
\qquad2\le q\le T.
\]

Put

\[
\delta_m=m^{-1/2}-(m+1)^{-1/2}>0.
\tag{L-32205.1}
\]

Apply the exact positive top-half inverse of `L-32201` on rows `N<n<=T`, and let

\[
r_1(q)
=h_T(q)-\sum_{n=N+1}^{T}c_1(n)\beta_{nq},
\qquad2\le q\le N,
\tag{L-32205.2}
\]

be the exported lower residual.  `L-32204` proves already that

\[
\boxed{r_1(q)\ge0\qquad(2\le q\le N).}
\tag{L-32205.3}
\]

The new statement is that the part of this residual seen by the *next* top-half inverse is automatically decreasing.

## 2. Exact difference formula

Retain from `L-32204`

\[
A_N(q)=\sum_{j=0}^{N}\left\lfloor\frac jq\right\rfloor
\]

and the lower residual of one step endpoint `m>N`,

\[
k_m(q)
=1-\left\lfloor\frac mq\right\rfloor
 +\frac{2mA_N(q)}{N(N+1)}.
\tag{L-32205.4}
\]

The hinge decomposition gives

\[
r_1(q)
=\sum_{m=q}^{N}\delta_m
 +\sum_{m=N+1}^{T-1}\delta_m k_m(q).
\tag{L-32205.5}
\]

Therefore, for `q<N`,

\[
\boxed{
\begin{aligned}
r_1(q)-r_1(q+1)
={}&\delta_q-L_q
 +\frac{2B_q}{N(N+1)}S,\\
B_q:={}&A_N(q)-A_N(q+1),\\
S:={}&\sum_{m=N+1}^{T-1}m\delta_m,\\
L_q:={}&\sum_{m=N+1}^{T-1}\delta_m
\left(
\left\lfloor\frac mq\right\rfloor
-
\left\lfloor\frac m{q+1}\right\rfloor
\right).
\end{aligned}}
\tag{L-32205.6}
\]

No estimate has entered yet.

## 3. Top-half floor geometry collapses to two tiny blocks

Assume now

\[
\boxed{N/2<q<N.}
\tag{L-32205.7}
\]

Since `2q>N`, one has exactly

\[
\boxed{B_q=1.}
\tag{L-32205.8}
\]

Indeed, for `0<=j<=N`, the difference

\[
\left\lfloor\frac jq\right\rfloor-
\left\lfloor\frac j{q+1}\right\rfloor
\]

is one only at `j=q` and zero elsewhere.

More generally,

\[
\left\lfloor\frac mq\right\rfloor-
\left\lfloor\frac m{q+1}\right\rfloor
\]

is the indicator sum of the short intervals

\[
[kq,k(q+1)-1],\qquad k\ge1.
\tag{L-32205.9}
\]

Since `m<=T-1<=2N` and `q>N/2`, no interval with `k>=4` can meet the exported range `N<m<T`.  The `k=1` interval lies below that range.  Thus only

```text
k=2:  {2q,2q+1},

k=3:  {3q,3q+1,3q+2}
```

can contribute, with either block possibly truncated by the endpoint.

Consequently

\[
L_q
\le
(\delta_{2q}+\delta_{2q+1})
+
\mathbf1_{3q\le2N}
(\delta_{3q}+\delta_{3q+1}+\delta_{3q+2}).
\tag{L-32205.10}
\]

The square-root source makes these blocks scale *exactly*:

\[
\boxed{
\delta_{2q}+\delta_{2q+1}
=\frac{\delta_q}{\sqrt2},
}
\tag{L-32205.11}
\]

and

\[
\boxed{
\delta_{3q}+\delta_{3q+1}+\delta_{3q+2}
=\frac{\delta_q}{\sqrt3}.
}
\tag{L-32205.12}
\]

These are just the telescopes

\[
(2q)^{-1/2}-(2q+2)^{-1/2}
=2^{-1/2}[q^{-1/2}-(q+1)^{-1/2}]
\]

and the analogous factor-three identity.

Hence

\[
\boxed{
L_q\le
\begin{cases}
\delta_q/\sqrt2,&q>2N/3,\\[1mm]
\delta_q(1/\sqrt2+1/\sqrt3),&N/2<q\le2N/3.
\end{cases}}
\tag{L-32205.13}
\]

## 4. The positive floor-prefix term supplies the exact missing margin

The first case of (L-32205.13) already gives

\[
\delta_q-L_q
\ge\delta_q(1-1/\sqrt2)>0,
\]

so suppose

\[
N/2<q\le2N/3.
\]

We now lower-bound the final positive term in (L-32205.6).

For every integer `m>=2`,

\[
\boxed{
m\delta_m\ge\frac1{3\sqrt m}.}
\tag{L-32205.14}
\]

Indeed (L-32205.14) is equivalent to

\[
3m\ge(m+1)+\sqrt{m(m+1)},
\]

and after subtracting `m+1` and squaring it reduces to

\[
3m^2-5m+1\ge0,
\]

which holds for `m>=2`.

Whether `T=2N` or `T=2N+1`, the sum defining `S` contains at least the `N-1` integers

\[
N+1,\ldots,2N-1.
\]

Using `m<=2N`,

\[
S
\ge\frac{N-1}{3\sqrt{2N}}.
\tag{L-32205.15}
\]

Thus, since `B_q=1`,

\[
\frac{2S}{N(N+1)}
\ge
\frac{2(N-1)}{3\sqrt2(N+1)}N^{-3/2}.
\tag{L-32205.16}
\]

For `N>=13`,

\[
\frac{2(N-1)}{3\sqrt2(N+1)}
\ge\frac{2\sqrt2}{7}.
\tag{L-32205.17}
\]

On the other hand convexity of `x^{-1/2}` gives

\[
\delta_q\le\frac1{2q^{3/2}}
<\sqrt2\,N^{-3/2}
\qquad(q>N/2).
\tag{L-32205.18}
\]

Combining (L-32205.16)--(L-32205.18),

\[
\boxed{
\frac{2S}{N(N+1)}>\frac27\delta_q.
}
\tag{L-32205.19}
\]

Finally the elementary radical inequality

\[
\boxed{
\frac1{\sqrt2}+\frac1{\sqrt3}-1<\frac27
}
\tag{L-32205.20}
\]

closes the margin.  For completeness, (L-32205.20) is equivalent to

\[
\frac1{\sqrt2}+\frac1{\sqrt3}<\frac97.
\]

Squaring once reduces it to

\[
\frac2{\sqrt6}<\frac{241}{294},
\]

and squaring again is the integer inequality

\[
57624<58081.
\]

Using (L-32205.13), (L-32205.19), and (L-32205.20) in (L-32205.6) gives

\[
\boxed{
r_1(q)-r_1(q+1)>0}
\tag{L-32205.21}
\]

for every

\[
N/2<q<N.
\]

## 5. Consequence: the complete second dyadic band has positive inverse coefficients

Equation (L-32205.3) gives `r_1(q)>=0` on its whole support, while (L-32205.21) shows that its restriction to the top half

\[
\lfloor N/2\rfloor<q\le N
\]

is nonincreasing (the last endpoint is followed by the declared zero value at `N+1`).

Therefore `L-32201` applies a second time.  The unique carry coefficients solving the residual on rows

\[
\boxed{
\lfloor N/2\rfloor<n\le N
}
\tag{L-32205.22}
\]

are all nonnegative.

Equivalently, for every `T>=26`, the exact critical-hinge carry inverse is unconditionally nonnegative throughout the two outer dyadic bands

\[
\boxed{
 n>\frac14\lfloor T/2\rfloor\ \text{in the staged sense, i.e. }\ 
 n>\frac12N\text{ after the first exact elimination},
}
\]

or, more transparently,

```text
first stage:   floor(T/2) < n <= T,
second stage:  floor(floor(T/2)/2) < n <= floor(T/2).
```

No Möbius estimate is used.

## 6. Exact scope

This theorem deliberately separates two properties which were conflated in the tempting naive induction:

```text
first exported residual is convex:             FALSE in general;
first exported residual is decreasing where
  the second top-half solve needs it:           TRUE cofinally here.
```

Thus a second positive inverse band is now proved, but a second application of the *no-lower-overfill* theorem `L-32204` is not justified: that theorem requires convexity, and `r_1` need not be convex.

The next exact target is correspondingly narrower:

> prove that eliminating the now-positive second band does not overfill the still lower columns for this specific square-root residual.

That is a source-specific **two-stage floor-kernel inequality**, not a generic cone-preservation theorem.

## 7. Proof boundary

Closed here, subject to independent review:

1. exact difference formula for the first exported residual;
2. exact collapse of the relevant floor-difference geometry to the `2q` and `3q` blocks;
3. exact square-root scaling of those blocks;
4. a uniform positive reserve margin for every `N>=13`;
5. strict decrease of `r_1` on its top half;
6. nonnegativity of the complete second-stage top-half inverse coefficients for every `T>=26`.

Still open:

1. second-stage no-lower-overfill;
2. indefinite staged repetition / CHS;
3. Carry Saturation;
4. RH.
