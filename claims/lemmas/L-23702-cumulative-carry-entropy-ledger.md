# L-23702 — Cumulative carry and positive entropy ledger

Claim ID: `L-23702`  
Title: A nonnegative cumulative Green profile is enough; pointwise carry coefficients are not required  
Status: `PROPOSED — COMPLETE EXACT FINITE ALGEBRA`  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Scope: finite, unconditional, exact  
Depends on: `L-23701`, Legendre's formula

## 1. Cumulative carry kernel

For `m>=2`, define

\[
\Delta_{mq}
 =(m+1)\beta_{mq}-m\beta_{m-1,q},
\qquad \beta_{m-1,q}=0\text{ if }q>m-1.
\tag{L-23702.1}
\]

Then

\[
\boxed{
\Delta_{mq}
 =m\mathbf1_{q\mid m}-\left\lfloor\frac mq\right\rfloor.}
\tag{L-23702.2}
\]

If `s_m` is the tail in (L-23701.8), summation by parts gives

\[
\boxed{
w(q)=\sum_{m=q}^{X}s_m\Delta_{mq}.}
\tag{L-23702.3}
\]

### Proof of (L-23702.2)

Subtract (L-23701.4) at `n=m-1` from the same identity at `n=m`. If `q` does
not divide `m`, the two floors are equal and the result is `-floor(m/q)`. If
`q|m`, the floor jumps by one and the result is `m-floor(m/q)`.

## 2. Average logarithmic binomial row

Put

\[
G_n=\frac1{n+1}\sum_{j=0}^{n}\log\binom nj.
\tag{L-23702.4}
\]

Legendre's formula and Kummer's carry interpretation give exactly

\[
\boxed{
G_n=\sum_{q=p^k\le n}\Lambda(q)\beta_{nq}.}
\tag{L-23702.5}
\]

Let

\[
F_n=(n+1)G_n.
\tag{L-23702.6}
\]

The factorial identity

\[
F_n=(n+1)\log(n!)-2\sum_{j=0}^{n}\log(j!)
\tag{L-23702.7}
\]

implies

\[
\boxed{
F_m-F_{m-1}
 =(m-1)\log m-\log((m-1)!)
 =\log\frac{m^{m-1}}{(m-1)!}>0.}
\tag{L-23702.8}
\]

Write

\[
L_2=\log2,
\qquad
L_m=\log\frac{m^{m-1}}{(m-1)!}\quad(m\ge3).
\tag{L-23702.9}
\]

## 3. Exact prime-ramp ledger

For the critical prime ramp

\[
P_X=\sum_{q=p^k\le X}
 \frac{\Lambda(q)}{\sqrt q}\log\frac Xq,
\tag{L-23702.10}
\]

and the exact triangular inverse of `w_X`, one has

\[
P_X=\sum_{n=2}^{X}c_X(n)G_n.
\tag{L-23702.11}
\]

Using (L-23701.14) and summation by parts again,

\[
\boxed{
P_X=s_{X,2}\log2+\sum_{m=3}^{X}s_{X,m}L_m.}
\tag{L-23702.12}
\]

Every basis weight in (L-23702.12) is strictly positive.

## 4. A weaker positive certificate

The exact inverse is not sacred. Let `\sigma_2,...,\sigma_X` be **any**
nonnegative numbers and define

\[
W_\sigma(q)=\sum_{m=q}^{X}\sigma_m\Delta_{mq}.
\tag{L-23702.13}
\]

If

\[
\boxed{W_\sigma(q)\le w_X(q)\qquad(2\le q\le X),}
\tag{L-23702.14}
\]

then, since every von Mangoldt weight is nonnegative,

\[
\begin{aligned}
P_X
&\ge\sum_{q=p^k\le X}\Lambda(q)W_\sigma(q)\\
&=\sigma_2\log2+
  \sum_{m=3}^{X}\sigma_mL_m.
\end{aligned}
\tag{L-23702.15}
\]

Therefore the following finite assertion is sufficient for the critical lower
bound:

\[
\boxed{
\begin{gathered}
\sigma_m\ge0,\qquad W_\sigma(q)\le w_X(q),\\
\sigma_2\log2+\sum_{m=3}^{X}\sigma_mL_m
 \ge4\sqrt X-X^{o(1)}.
\end{gathered}}
\tag{L-23702.16}
\]

This certificate does **not** require `\sigma_m` to be decreasing. Equivalently,
its induced coefficients

\[
d_m=(m+1)(\sigma_m-\sigma_{m+1})
\tag{L-23702.17}
\]

may have either sign. Positivity is carried by the cumulative entropy increments
`L_m`, not by the original row coefficients.

This is the first main simplification of the proposal:

\[
\boxed{
\text{Carry Saturation is stronger than the RH-facing positive ledger.}}
\tag{L-23702.18}
\]

## 5. Row-positive sufficient form

A more concrete but stronger certificate uses `d_m>=0` and

\[
\sum_{m=q}^{X}d_m\beta_{mq}\le w_X(q).
\tag{L-23702.19}
\]

Then

\[
P_X\ge\sum_m d_mG_m.
\tag{L-23702.20}
\]

The elementary entropy bound

\[
G_m\ge\frac m2-\log(m+1)-3
\tag{L-23702.21}
\]

reduces the task to a main half-moment and a logarithmic defect budget:

\[
\frac12\sum_m m d_m\ge4\sqrt X-X^{o(1)},
\qquad
\sum_m d_m(\log(m+1)+3)=X^{o(1)}.
\tag{L-23702.22}
\]

The phase-band construction in `T-23701` uses this row-positive form because its
atoms come from the already proved outer positive carry region. The cumulative
form (L-23702.16) is retained as an even weaker fallback target.

## 6. Exact replay

`X-23701` verifies (L-23702.2) and the formal-prime-vector version of
(L-23702.8) through `m=72`. The checker never evaluates a prime asymptotic or an
RH statement.
