# L-91686 — The Target-Lorenz row gate holds through the fifth quotient wall

Claim ID: `L-91686`  
Status: **PROVED EXACT LOW-QUOTIENT THEOREM**  
Created: 2026-08-14  
Depends on: `L-91682`, `L-91684`, `L-91685`  
Replay: `X-91685-target-lorenz-vector-primal-dual`  
RH status: **unproved**

## 1. Statement

Let

\[
 p\ge67,
 \qquad 1\le y<67,
 \qquad x=py,
 \qquad 2\le j\le66.
\]

For the Target-Lorenz submeasure `U` of `L-91684`, one has

\[
 \boxed{
 R_j(U)-O_R^{(j)}>0
 \qquad\text{whenever }x<5j.
 }
 \tag{L-91686.1}
\]

This extends the first-cell result `x<2j` in `L-91684` across every activation
wall below quotient five.

## 2. Active row sources

If `x<5j`, then

\[
 y=\frac{x}{p}<\frac{5j}{67}<j.
 \tag{L-91686.2}
\]

Thus every child row is inactive. Since `Q_{x/d}(j)=0` for `d>x/j`, the only
possible row-active squarefree `P_61` divisors below quotient five are

```text
even: 1;
odd:  2 and 3.
```

The divisor `5` is inactive because the inequality is strict, and `4` is not
squarefree.

Write the causal target atoms as `T_d=K_T(d)`. It is enough to prove

\[
 \boxed{T_1>T_2+T_3.}
 \tag{L-91686.3}
\]

Indeed `O_T>=T_2+T_3`. The leftmost target removal therefore uses at least
`T_2+T_3` units of target at `d=1`: if `O_T<=T_1`, it uses `O_T`; otherwise it
uses all of `T_1`.

By the row-per-target order of `L-91682`,

\[
 \frac{R_1}{T_1}\ge\frac{R_2}{T_2},
 \qquad
 \frac{R_1}{T_1}\ge\frac{R_3}{T_3}.
\]

Hence the used row at `d=1` alone dominates `R_2+R_3`; every other used even
row is nonnegative.

## 3. Exact target domination

Put

\[
 A=\sqrt x,
 \qquad r=\sqrt{y/x}.
\]

An atom is in the inner regime when `d<=y` and in the parent-only frontier when
`d>y`.

Define the positive constant

\[
 C=\frac3{\sqrt2}+\sqrt3-3>\frac45.
 \tag{L-91686.4}
\]

### Case I: `1<=y<2`

Only `d=1` is inner. Direct subtraction gives

\[
 T_1-T_2-T_3
 =\frac23A+C-\frac{4y}{A}+3r.
 \tag{L-91686.5}
\]

Since `x>=67` and `y<2`,

\[
 T_1-T_2-T_3
 >\frac23\sqrt{67}-\frac8{\sqrt{67}}+C
 >5.
 \tag{L-91686.6}
\]

### Case II: `2<=y<3`

The atoms `1,2` are inner and `3` is frontier. One obtains

\[
 T_1-T_2-T_3
 =\frac23A-\frac{2y}{A}+C
  +3\left(1-\frac1{\sqrt2}\right)r.
 \tag{L-91686.7}
\]

Now `x>=67y>=134`, so

\[
 T_1-T_2-T_3
 >\frac23\sqrt{134}-\frac6{\sqrt{134}}+C
 >8.
 \tag{L-91686.8}
\]

### Case III: `3<=y<5`

All three atoms are inner, and the common factor gives

\[
 \boxed{
 T_1-T_2-T_3
 =(1-r)
 \left[
  \frac23\sqrt y(\sqrt p+1)+C
 \right]>0.
 }
 \tag{L-91686.9}
\]

These cases prove (L-91686.3), hence (L-91686.1).

## 4. Consequence for the arithmetic campaign

Every remaining row cell satisfies

\[
 \boxed{py\ge5j.}
 \tag{L-91686.10}
\]

The lowest quotient walls, including the numerical minimum seen in current
reconnaissance, are therefore removed analytically. The first unresolved
sector begins when the odd divisor `5` becomes row active.

## 5. Exact boundary

```text
Target-Lorenz row gate for py<2j       PREVIOUSLY PROVED
Target-Lorenz row gate for py<5j       PROVED EXACT HERE
child-row subtraction in this sector   ABSENT EXACTLY
remaining sector py>=5j                OPEN / ARITHMETIC
Riemann Hypothesis                      UNPROVEN
```
