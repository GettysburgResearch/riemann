# L-91345 — The `P_79` one-prime splice has a monotone target/score kernel and a uniform large-prefix Hall reserve

Claim ID: `L-91345`  
Status: **PROVED EXACT KERNEL/PREFIX THEOREM — FINITE LOW-PREFIX CORRECTION OPEN**  
Created: 2026-08-12  
Depends on: `L-91328`, `L-91339`–`L-91344`; exact checker `X-91124`  
RH status: **unproved**

## 1. One-prime target and score atoms

Fix a prime `p>=83`, put

\[
 r=p^{-1/2},
 \qquad1\le y<83,
\]

and let `d` be a squarefree divisor of `P_79`.  Define causally

\[
 K_\Psi(d)
 =W_\Psi(py,d)-rW_\Psi(y,d),
\]

\[
 K_S(d)
 =W_S(py,d)-rW_S(y,d),
\]

where

\[
 W_\Psi(x,d)=d^{-1/2}[4\sqrt{x/d}-3]\,1_{d\le x},
\]

\[
 W_S(x,d)=d^{-1/2}[5\sqrt{x/d}-3]\,1_{d\le x}.
\]

Both splice atoms are strictly positive whenever `d<=py`.

Put

\[
 t_d=\sqrt{py/d}.
\]

If `d<=y`, then

\[
 \boxed{
 K_\Psi(d)
 =\frac{1-r}{\sqrt d}
  [4(1+r)t_d-3],
 }
\tag{L-91345.1}
\]

\[
 \boxed{
 K_S(d)
 =\frac{1-r}{\sqrt d}
  [5(1+r)t_d-3].
 }
\tag{L-91345.2}
\]

If `y<d<=py`, then

\[
 \boxed{
 K_\Psi(d)=\frac{4t_d-3}{\sqrt d},
 \qquad
 K_S(d)=\frac{5t_d-3}{\sqrt d}.
 }
\tag{L-91345.3}

## 2. Score per target unit is ordered

Let

\[
 q(u)=\frac{4u-3}{5u-3},
 \qquad u\ge1.
\]

Then

\[
 q'(u)=\frac3{(5u-3)^2}>0.
\]

Equations (L-91345.1)--(L-91345.3) give

\[
 \frac{K_\Psi(d)}{K_S(d)}
 =
 \begin{cases}
  q((1+r)t_d),&d\le y,\\
  q(t_d),&y<d\le py.
 \end{cases}
\tag{L-91345.4}

The variable `t_d` decreases with `d`.  At the interface `d=y`, the argument
jumps downward from `(1+r)sqrt(p)=sqrt(p)+1` to `sqrt(p)`. Therefore

\[
 \boxed{
 d_1\le d_2
 \Longrightarrow
 \frac{K_\Psi(d_1)}{K_S(d_1)}
 \ge
 \frac{K_\Psi(d_2)}{K_S(d_2)}.
 }
\tag{L-91345.5
 }

Consequently every no-upward transport in target-mass units is automatically
score-superordinate, exactly as in the terminal theorem `L-91342`.

## 3. Three exact `P_79` prefix gates

For an odd squarefree divisor threshold `t`, define

\[
 A_0(t)
 =\sum_{\substack{e\le t\\\mu(e)=1}}\frac1e
  -\sum_{\substack{o\le t\\\mu(o)=-1}}\frac1o,
\tag{L-91345.6}
\]

\[
 A_8(t)
 =\sum_{\substack{e\le t+8\\\mu(e)=1}}\frac1e
  -\sum_{\substack{o\le t\\\mu(o)=-1}}\frac1o,
\tag{L-91345.7}
\]

and

\[
 B_8(t)
 =\sum_{\substack{e\le t+8\\\mu(e)=1}}\frac1{\sqrt e}
  -\sum_{\substack{o\le t\\\mu(o)=-1}}\frac1{\sqrt o}.
\tag{L-91345.8}
\]

The standard-library checker `X-91124` streams all

\[
 2^{22}=4,194,304
\]

divisors of `P_79` in increasing order.  The `1/d` sums are exact integers over
the common denominator `P_79`; the square-root sum uses directed rational
intervals. It proves

\[
 \boxed{
 A_0(t)>\frac1{25}
 \qquad(t\ge83),
 }
\tag{L-91345.9}
\]

\[
 \boxed{
 A_8(t)>\frac1{5000}
 \qquad(t\ge1),
 }
\tag{L-91345.10}
\]

and

\[
 \boxed{
 B_8(t)<\frac32
 \qquad(t\ge1).
 }
\tag{L-91345.11}

The exact minima are:

```text
raw reciprocal prefix:       t=105;
8-shifted reciprocal prefix: t=73;
maximum shifted sqrt prefix: t=399.
```

The exact rational minimum in (L-91345.10) is

\[
 \frac{693080260501195886848851250}
 {3217644767340672907899084554130}
 >\frac1{5000}.
\]

## 4. Large-prefix one-prime Hall theorem

Let an active odd threshold satisfy

\[
 t\ge4096.
\]

Use only even capacities `e<=t`; the additional capacities through `t+8` are
nonnegative and may be ignored.  Since `t<=py`, the parent part of the target
Hall margin is at least

\[
 4\sqrt{py}\,A_0(t)-3B_8(t).
\]

Because `t>=83>y`, the child prefix contains the complete finite `P_79` target
forcing at endpoint `y`.  Positivity of the finite Euler factors and the global
upper corridor give

\[
 0<F_\Psi^{(79)}(y)<4\sqrt y.
\]

Hence the one-prime Hall margin obeys

\[
\begin{aligned}
 \mathcal H_{p,y,t}
 &>\frac4{25}\sqrt{py}-\frac92
   -\frac4{\sqrt p}\sqrt y\\
 &\ge\frac4{25}\sqrt t-rac92-rac{332}{\sqrt t}.
\end{aligned}
\tag{L-91345.12
 }

The right side increases for `t>0`. At `t=4096`, it equals

\[
 \frac{256}{25}-\frac92-rac{83}{16}
 =\frac{221}{400}>0.
\]

Therefore

\[
 \boxed{
 \mathcal H_{p,y,t}>\frac{221}{400}
 \qquad
 (p\ge83,\ 1\le y<83,\ t\ge4096).
 }
\tag{L-91345.13
 }

No large-prime or large-threshold Hall obstruction remains.

## 5. Finite low-prefix gate

The complete one-prime target Hall problem is now reduced to

\[
 \boxed{
 t<4096.
 }
\]

Only divisors of the fixed finite product `P_79` occur, the child parameter is
in the compact interval `1<=y<83`, and each Hall margin is affine in `sqrt(y)`
on finitely many activation cells. A displacement-eight reconnaissance is
strictly positive, while displacement seven has negative examples.

However, displacement `e<=o+8` does not automatically preserve the score and
row inequalities of Section 2.  The remaining finite theorem must construct the
bounded upward correction from positive interval/butterfly or common endpoint
port packets, and verify target, score and every inherited row simultaneously.

## 6. Proof boundary

```text
one-prime target/score atoms positive             EXACT
score-per-target ratio decreases with source node EXACT
P_79 raw reciprocal prefix >1/25                  EXACT
P_79 shifted reciprocal prefix >1/5000            EXACT
P_79 shifted sqrt prefix <3/2                     DIRECTED EXACT
all thresholds t>=4096 Hall-positive              EXACT
finite low-prefix displacement-eight Hall          FINITE / CHECKABLE
positive bounded upward correction                 OPEN / RH-BEARING
Riemann Hypothesis                                 UNPROVEN
```
