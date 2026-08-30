# R-32703 — Adjacent Jordan row pairing already fails on the `T=4` square-root hinge

Claim ID: `R-32703`  
Status: **EXACT FINITE REFUTATION OF A NATURAL JORDAN-CARRY SHORTCUT**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-09  
Dependencies: `L-32702`; the average-carry coefficient `beta_(nq)`; PR #329/#332 square-root hinge coordinate  
Scope: refutes adjacent `(2m,2m+1)` row pairing as a positivity mechanism; does not refute the quadratic Jordan source or a global cycle-optimized flow

## 1. Average Jordan charge of one row

Let

\[
H(N)=(-1)^{N-1}\frac{N(N+1)}2,
\qquad H(0)=0,
\]

be the exact floor potential of the quadratic Jordan parity source `L-32702`.
For the uniform average of all splits of a parent `n`, the source charge is

\[
\overline Y_n
=H(n)-\frac2{n+1}\sum_{j=0}^nH(j).
\tag{R-32703.1}
\]

Direct summation gives

\[
\sum_{j=0}^{2m}H(j)=-m(m+1),
\qquad
\sum_{j=0}^{2m+1}H(j)=(m+1)^2.
\]

Hence

\[
\boxed{
\overline Y_{2m}
=-\frac{m(4m^2+2m-1)}{2m+1}<0,}
\tag{R-32703.2}
\]

and

\[
\boxed{
\overline Y_{2m+1}=2m(m+1)>0.}
\tag{R-32703.3}
\]

Equal coefficients would give a positive adjacent-pair residue,

\[
\overline Y_{2m}+\overline Y_{2m+1}
=\frac{m(4m+3)}{2m+1}>0.
\tag{R-32703.4}
\]

This makes adjacent pairing tempting. The exact hinge inverse disproves it.

## 2. Exact `T=4` square-root hinge inverse

For

\[
h_4(q)=q^{-1/2}-\frac12,
\qquad q\le4,
\]

write its exact average-carry expansion

\[
h_4(q)=\sum_{n=q}^{4}c_4(n)\beta_{nq},
\qquad
\beta_{nq}=
\frac{\lfloor n/q\rfloor(q-1-(n\bmod q))}{n+1}.
\tag{R-32703.5}
\]

Triangular back substitution gives

\[
\boxed{
c_4(2)=-\frac32+\frac{3\sqrt2}{2}>0,}
\tag{R-32703.6}
\]

\[
\boxed{
c_4(3)=-1+\frac{2\sqrt3}{3}>0,}
\tag{R-32703.7}
\]

and `c_4(4)=0`.

Thus even this control uses a genuinely positive hinge inverse.

## 3. The adjacent Jordan pair is nevertheless negative

At `m=1`, equations (R-32703.2)--(R-32703.3) give

\[
\overline Y_2=-\frac53,
\qquad
\overline Y_3=4.
\]

Therefore the complete nonzero hinge contribution is

\[
\begin{aligned}
 c_4(2)\overline Y_2+c_4(3)\overline Y_3
 &=
 -\frac32-\frac{5\sqrt2}{2}+\frac{8\sqrt3}{3}.
\end{aligned}
\tag{R-32703.8}
\]

This is strictly negative. Indeed

\[
\frac{8\sqrt3}{3}<\frac{3+5\sqrt2}{2}
\]

because, after squaring the positive sides, it is enough to check

\[
256<177+90\sqrt2,
\]

and the latter follows from

\[
79<90\sqrt2
\]

since `79^2=6241<16200=2*90^2`.

Hence

\[
\boxed{
 c_4(2)\overline Y_2+c_4(3)\overline Y_3<0.}
\tag{R-32703.9}
\]

## 4. Consequence

The attractive local rule

```text
negative even Jordan parent
+ next positive odd Jordan parent
-> nonnegative adjacent pair
```

is false even when the row coefficients themselves are all positive.

A valid quadratic-Jordan completion must therefore use one of:

- a nonlocal pairing of multiple parent sizes;
- the full Pascal cycle space;
- a source-specific weighted transport;
- a Hermitian/energy recombination before taking signs.

The deterministic odd/even source theorem `L-32702` remains exact and useful. What fails is only the naïve adjacent-row consumption of its negative sector.

## 5. Proof boundary

```text
quadratic Jordan source/sign classification    RETAINED
adjacent equal-row source charge                positive algebraically
actual hinge coefficients are adjacent-equal   FALSE
naive adjacent Jordan pairing                   REFUTED at T=4
cycle-optimized Jordan transport                OPEN
RH                                              UNPROVED
```
