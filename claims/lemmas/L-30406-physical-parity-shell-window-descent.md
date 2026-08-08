# L-30406 — Physical parity-shell Euler renormalization and safe-order descent

Claim ID: `L-30406`  
Title: The analytically regularized dyadic half-pole shell equals one explicit compact lower-safe-order window packet plus an exponentially small Euler remainder  
Status: **PROPOSED COMPLETE ANALYTIC LEMMA — INDEPENDENT REVIEW REQUESTED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: `L-30405`; first-order Euler summation  
Scope: the physical output of the regularized parity source; no estimate of the final zero-order packet and no RH conclusion

## 1. Regularized parity-shell source

Let `L=log 2`. Retain from `L-30405` the critical analytically regularized source

\[
\boxed{
\Sigma_N(m)
={1\over\sqrt m}
\left[
\sqrt2\,\mathbf1_{m>N/2}
-\mathbf1_{m>N}
\right].}
\tag{L-30406.1}
\]

This is not used as an absolutely summable divisor source. For a compact window
`W`, however, its physical output is an ordinary finite sum:

\[
\boxed{
\mathcal S_{N,W}(x)
=\sqrt2\sum_{m>N/2}{W(x-\log m)\over\sqrt m}
-\sum_{m>N}{W(x-\log m)\over\sqrt m}.}
\tag{L-30406.2}
\]

Only finitely many terms meet the compact support of `W`.

Assume throughout that `W` is continuous, compactly supported, piecewise `C^1`,
and half-pole null:

\[
\boxed{
\int_{\mathbb R}e^{-u/2}W(u)\,du=0.}
\tag{L-30406.3}
\]

## 2. Continuous parity shell

Define

\[
F_W(y)=\int_{-\infty}^{y}e^{-u/2}W(u)\,du.
\tag{L-30406.4}
\]

Because of (L-30406.3), `F_W` vanishes both below and above a compact interval.
Set

\[
\boxed{
(\mathcal R_2W)(y)
=e^{y/2}
\left[
\sqrt2F_W(y+L)-F_W(y)
\right].}
\tag{L-30406.5}
\]

Then `R_2 W` is compactly supported and piecewise `C^1`.

For every positive real `A`, direct substitution `u=x-log t` gives

\[
\int_A^\infty {W(x-\log t)\over\sqrt t}\,dt
=e^{x/2}F_W(x-\log A).
\tag{L-30406.6}
\]

Taking `A=N/2` and `A=N`, and writing

\[
y=x-\log N,
\]

yields the exact continuous identity

\[
\boxed{
\begin{aligned}
&\sqrt2\int_{N/2}^\infty
 {W(x-\log t)\over\sqrt t}\,dt
-
\int_N^\infty
 {W(x-\log t)\over\sqrt t}\,dt\\
&\hspace{25mm}=\sqrt N\,(\mathcal R_2W)(x-\log N).
\end{aligned}}
\tag{L-30406.7}
\]

Thus the macroscopic part of the parity source is one explicit scale-`N` packet,
not an uncontrolled collection of endpoint atoms.

## 3. Exact window equation

The coefficient `sqrt(2)` in (L-30406.5) is precisely the half-pole scaling.
Changing variables in the first integral gives the equivalent formula

\[
\sqrt2F_W(y+L)-F_W(y)
=\int_{-\infty}^{y}e^{-u/2}
 [W(u+L)-W(u)]\,du.
\tag{L-30406.8}
\]

Consequently

\[
\boxed{
\left({d\over dy}-{1\over2}\right)
\mathcal R_2W(y)
=W(y+L)-W(y).}
\tag{L-30406.9}
\]

Let

\[
\widehat W(z)=\int_{\mathbb R}e^{-zy}W(y)\,dy.
\]

Integration by parts in (L-30406.9) gives

\[
\boxed{
\widehat{\mathcal R_2W}(z)
={e^{zL}-1\over z-1/2}\widehat W(z).}
\tag{L-30406.10}
\]

No boundary term occurs because `R_2W` is compact.

## 4. Safe-order descent

Suppose `widehat W` has a zero of order `r>=1` at `z=1/2`. The numerator in
(L-30406.10) has the nonzero value

\[
e^{L/2}-1=\sqrt2-1.
\]

Therefore

\[
\boxed{
\operatorname{ord}_{z=1/2}
\widehat{\mathcal R_2W}
=r-1.}
\tag{L-30406.11}
\]

The parity-shell transform lowers the half-pole safe order by exactly one. It
does not destroy compact support and introduces no inverse-zeta factor.

In particular, for a high-order safe window `H^[r]`, the continuous terminal
parity shell is routed to one explicit window packet of complexity `r-1`.

## 5. Euler remainder

For fixed `x`, put

\[
f_x(t)=t^{-1/2}W(x-\log t).
\]

On every interval where it is nonzero,

\[
f_x'(t)
=-t^{-3/2}
\left[
{1\over2}W(x-\log t)+W'(x-\log t)
\right].
\tag{L-30406.12}
\]

Hence

\[
\int_0^\infty|f_x'(t)|dt
\le C_W e^{-x/2},
\tag{L-30406.13}
\]

where

\[
C_W=
\int_{\mathbb R}e^{u/2}
\left({1\over2}|W(u)|+|W'(u)|\right)du.
\]

The endpoint discrepancy between a real cutoff and its first integer is also
at most

\[
C'_W e^{-x/2}.
\]

First-order Euler summation therefore gives, uniformly in `A>0`,

\[
\boxed{
\left|
\sum_{m>A}f_x(m)-\int_A^\infty f_x(t)dt
\right|
\le C''_W e^{-x/2}.}
\tag{L-30406.14}
\]

Applying (L-30406.14) at `A=N/2` and `A=N`, and using (L-30406.7), proves

\[
\boxed{
\mathcal S_{N,W}(x)
=\sqrt N\,(\mathcal R_2W)(x-\log N)
+O_W(e^{-x/2}).}
\tag{L-30406.15}
\]

On the active block `x=log N+O_W(1)`, the remainder is `O_W(N^(-1/2))`.

## 6. Consequence for the corrected terminal programme

Combining `L-30405` and (L-30406.15), the complete terminal boundary has the
following exact architecture after correct recombination:

```text
one current-scale window packet with half-pole order lowered by one
+ a finite shift source of N^(o(1)) atomic cost
+ at most one constant-cost collar atom
+ an O(N^(-1/2)) physical Euler remainder.
```

This is a genuine finite-complexity descent. It explains simultaneously:

- why the absolute atomic ledger is linearly large (`R-30404`);
- why the one-step shift itself is not the RH-bearing obstruction (`L-30405`);
- why high-order null windows can still be useful after the absolute route is
  rejected.

## 7. What this theorem does not prove

After `r` descents, one reaches a compact zero-order packet. Equation
(L-30406.15) does not estimate that final packet, nor does it supply a strict
lower-scale recurrence for it. Calling the terminal family closed without such
an estimate would merely move the RH-bearing source to the base of the
complexity induction.

A complete proof must either:

1. identify the zero-order packet with an already controlled positive or
   lower-scale channel; or
2. retain it inside a signed independent-frequency normal Gram and prove the
   required contraction.

This is a proof boundary, not an exercise assigned to a reviewer.

## 8. Proof boundary

Proved exactly here:

- the continuous parity-shell formula;
- compactness of the transformed window;
- the differential and transform identities;
- exact loss of one half-pole zero order;
- the uniform Euler remainder;
- the corrected finite-complexity terminal reduction.

Not proved here:

- control of the final zero-order packet;
- a Cycle-Debt, WSTS, or Hardy recurrence;
- RH.
