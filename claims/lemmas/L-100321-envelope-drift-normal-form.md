# L-100321 — Exact envelope normal form: fixed budget minus one critical drift

Claim ID: `L-100321`  
Status: **PROVED EXACT STIELTJES NORMAL FORM**  
Created: 2026-08-20  
Depends on: `L-100320`; the exact envelope cell derivative of PR #679  
RH status: **unproved**

Let

\[
\Delta_{3/2}=\prod_i(1-q_i^{-3/2})
\]

and let `e(y)` be the normalized quadratic-envelope Euler transform

\[
e(y)=\sum_A(-1)^{|A|}q_A^{-3/2}f(y/q_A),
\]

with

\[
f(v)=\begin{cases}
16,&0<v<1,\\
24v^{-1/2}-9v^{-1},&v\ge1.
\end{cases}
\]

Put

\[
H(t)=4\sqrt t\,S_1(t)-3S_{1/2}(t),
\]

where `S_alpha(t)` denotes the corresponding product-threshold Euler prefix.
Then, with right-continuous activation convention,

\[
\boxed{
e(y)=16\Delta_{3/2}-S_{3/2}(y)
-3\int_1^y H(t)\frac{dt}{t^2}.
}
\tag{L-100321.1}
\]

## Proof

At `y=1`, only the empty subset is active.  The completed inactive carrier is
`16`, while the active empty carrier is `15`, so

\[
e(1)=16\Delta_{3/2}-1.
\]

At an activation `y=q_A`, the carrier changes from `16` to `15`.  Therefore the
jump of the `A`-term is

\[
-(-1)^{|A|}q_A^{-3/2}.
\]

The cumulative jump through `y` is exactly

\[
1-S_{3/2}(y).
\]

On every open activation cell, PR #679 gives

\[
e'(t)=-3t^{-2}H(t).
\]

Integrating the absolutely continuous part and adding the jumps gives
(L-100321.1).

By `L-100320`,

\[
0<S_{3/2}(y)\le1.
\]

Thus every discontinuous contribution is now explicitly bounded; the only
remaining conclusion-producing arithmetic is the continuous critical drift.

## Strong sufficient gate

Define `CDTG100320` by

\[
\boxed{
3\int_1^yH(t)\frac{dt}{t^2}
\le16\Delta_{3/2}-S_{3/2}(y)
\qquad(y\ge1).
}
\]

Then `e(y)>=0` for every `y`, the quadratic envelope is nonnegative, and the
zero-safe Mellin-Landau consumer yields RH.

`CDTG100320` is not proved here.
