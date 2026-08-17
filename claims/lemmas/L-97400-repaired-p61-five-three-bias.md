# L-97400 — The complete `P_61` annular `5:3` scalar has the repaired global bias `1/42 <= F/M <= 1/8`

Claim ID: `L-97400`  
Status: **UNCONDITIONAL DIRECTED FINITE-PLUS-ANALYTIC THEOREM**  
Created: 2026-08-18  
Frozen analytic input: PR #497 `L-93600` at `bd2a3c32ab50d8a8cec39c4b51ccd63349b23a74`  
RH status: **not assumed**

Use the definitions of `R-97400`.  Then
\[
\boxed{
0\le F(x)\le M(x)\qquad(1\le x<67),
}
\tag{L-97400.1}
\]
and
\[
\boxed{
\frac1{42}M(x)\le F(x)\le\frac18M(x)
\qquad(x\ge67).
}
\tag{L-97400.2}
\]
The lower constant `1/42` is valid for every real `x`; the formerly asserted
constant `1/40` is false by `R-97400`.

## 1. Exact finite coefficient reduction

For any integer sequence `b(n)` define
\[
\mathscr H_b(x)=\sum_{n\ge1}\frac{b(n)}{\sqrt n}H_x(n).
\]
Finite divisor switching gives
\[
F(x)=\mathscr H_f(x),
\qquad
M(x)=\mathscr H_m(x),
\]
where
\[
f(n)=\sum_{\substack{d\mid P\\d\mid n}}\mu(d)q_*(n/d),
\qquad
m(n)=\sum_{\substack{d\mid P\\d\mid n}}q_*(n/d).
\tag{L-97400.3}
\]
These are generated exactly by the finite convolutions
\[
f=q_*\ast\prod_{p\le61}(\delta_1-\delta_p),
\qquad
m=q_*\ast\prod_{p\le61}(\delta_1+\delta_p).
\]
For an integer `N`, put `K=floor(N/4)`.  Then
\[
\boxed{
\mathscr H_b(N)=
(\log4)\sum_{n\le K}\frac{b(n)}{\sqrt n}
+(\log N)\sum_{K<n\le N}\frac{b(n)}{\sqrt n}
-\sum_{K<n\le N}\frac{b(n)\log n}{\sqrt n}.
}
\tag{L-97400.4}
\]
Every activation and saturation breakpoint is an integer (`n` or `4n`).  On
`N<x<N+1`, every expression in (L-97400.1)--(L-97400.2) is affine in `log x`.
Consequently directed positivity at all integer endpoints proves the all-real
statement.

A 256-bit MPFR producer, with every `sqrt`, `log`, `zeta(1/2)` and conversion
rounded outward and every subsequent `long double` operation expanded by one
`nextafterl`, proves:

```text
F(N)>0,                         3 <= N <= 66;
M(N)-F(N)>0,                    5 <= N <= 66;
42F(N)-M(N)>0,                 67 <= N <= 1,000,000;
M(N)-8F(N)>0,                  67 <= N <= 1,000,000.
```

The retained strict minima are
\[
42F(184)-M(184)>3.272741705897984,
\]
\[
M(67)-8F(67)>135.51661277216024.
\tag{L-97400.5}
\]
The omitted initial cells are exact zeros or positive single-hinge cells.

## 2. Uniform asymptotic for the positive scalar source

Let
\[
S(Y)=\sum_{n\le Y}n^{-1/2}\log(Y/n).
\]
The directed analytic theorem `L-93600` gives
\[
S(Y)=4\sqrt Y+\zeta(1/2)\log Y+\zeta'(1/2)+R(Y),
\qquad |R(Y)|<5Y^{-3/2}.
\]
For `Y>=16`, finite algebra therefore gives
\[
\boxed{
A_*(Y)=12\sqrt Y+C_0+E(Y),
}
\tag{L-97400.6}
\]
where
\[
C_0=\left(6\zeta(1/2)-\frac{15}{2}+\frac9{\sqrt2}\right)\log4
\]
and
\[
|E(Y)|<270Y^{-3/2}<5.
\]
A separate directed compact check on `2<=Y<=16`, with mesh `1/100` and a
rigorous derivative enclosure on every unit activation cell, proves
\[
|A_*(Y)-12\sqrt Y-C_0|<3.268<5.
\tag{L-97400.7}
\]
The same certificate proves `|C_0|<20`.

## 3. Complete analytic tail

For either choice
\[
a_d=42\mu(d)-1
\quad\text{or}\quad
a_d=1-8\mu(d),
\]
let
\[
D_x=\{d\mid P:2d\le x\}.
\]
Equations (L-97400.6)--(L-97400.7) imply the rigorous lower bound
\[
\begin{aligned}
\sum_{d\in D_x}\frac{a_d}{\sqrt d}A_*(x/d)
\ge{}&12\sqrt x\sum_{d\in D_x}\frac{a_d}{d}
-20\left|\sum_{d\in D_x}\frac{a_d}{\sqrt d}\right|\\
&-5\sum_{d\in D_x}\frac{|a_d|}{\sqrt d}.
\end{aligned}
\tag{L-97400.8}
\]
The active set changes only at the `524,288` thresholds `x=2d`.  Between two
successive thresholds the right side is affine in `sqrt x`, so its minimum is
at an endpoint.  Exhaustive directed enumeration of all `262,144` divisors of
`P_61` proves, for every real `x>=1,000,000`,
\[
42F(x)-M(x)>119.8715,
\]
\[
M(x)-8F(x)>40007.49.
\tag{L-97400.9}
\]
Combining (L-97400.5), (L-97400.9), and the integer-knot interpolation proves
(L-97400.1)--(L-97400.2).

## Proof-object contract

The exact producer is
`experiments/X-97400-p61-bias/src/certify.cpp`.  It records MPFR version,
precision, `long double` mantissa width, finite coverage, divisor count, all
strict margins and the explicit `1/40` counterexample.  The retained result is
accepted only when every strict lower endpoint has the required sign.
