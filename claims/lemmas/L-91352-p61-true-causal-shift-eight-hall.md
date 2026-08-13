# L-91352 — The true causal `P_61` one-prime splice has a uniform shifted-eight target/score Hall transport

Claim ID: `L-91352`  
Status: **PROVED DIRECTED FINITE/ANALYTIC HALL THEOREM — ROW/CAPACITY TYPING SEPARATE**  
Created: 2026-08-13  
Depends on: `L-91328`; `R-91310`; exact replay `X-91130`  
RH status: **unproved**

## 1. Causal Hall margin

Let

\[
P_{61}=\prod_{q\le61}q,
\qquad p\ge67,
\qquad1\le y<67,
\qquad x=py.
\]

For `a=4` (SHARP target) or `a=5` (endpoint score), put

\[
K_a(d;p,y)=
\frac{a\sqrt{x/d}-3}{\sqrt d}\mathbf1_{d\le x}
-\frac1{\sqrt p}\frac{a\sqrt{y/d}-3}{\sqrt d}\mathbf1_{d\le y}.
\tag{L-91352.1}
\]

For an active odd `P_61` threshold `t`, define the **actual causal** shifted-eight margin

\[
\boxed{
\mathcal H_{a,t}^{\rm cau}(p,y)=
\sum_{\substack{e\le t+8\\\mu(e)=1}}K_a(e;p,y)
-
\sum_{\substack{o\le t\\\mu(o)=-1}}K_a(o;p,y).
}
\tag{L-91352.2}
\]

Every summand in (L-91352.2) retains both indicators in (L-91352.1). In particular, a formal capacity `e<=t+8` contributes nothing until `e<=py`.

## 2. Exact activation-cell formula

On a cell where the active parent and child prefixes are fixed, write

\[
A_P=\sum_{\rm parent}\frac{\mu_{\rm Hall}(d)}d,
\quad
B_P=\sum_{\rm parent}\frac{\mu_{\rm Hall}(d)}{\sqrt d},
\]

\[
A_C=\sum_{\rm child}\frac{\mu_{\rm Hall}(d)}d,
\quad
B_C=\sum_{\rm child}\frac{\mu_{\rm Hall}(d)}{\sqrt d},
\]

where `mu_Hall=+1` on even capacities and `-1` on odd demands. Then

\[
\boxed{
\mathcal H_{a,t}^{\rm cau}
=aA_P\sqrt x-3B_P-
\frac{aA_C\sqrt y-3B_C}{\sqrt x}.
}
\tag{L-91352.3
}

The relevant domain is

\[
x\ge\max(t,67y).
\tag{L-91352.4}
\]

The parent prefixes change at `t` and at the at most eight positive sources in `(t,t+8]`; the child prefixes change at the finitely many `P_61` divisors below `67`.

## 3. Finite minimization

The child Hall numerator

\[
C_a(y)=aA_C\sqrt y-3B_C
\]

is positive on every child cell. For fixed `y`, (L-91352.3) is therefore concave in `sqrt(x)`, so its minimum on a parent activation interval occurs at a boundary.

For fixed `x`, the margin is a quadratic polynomial in `sqrt(y)`. If `A_C>=0` it is concave and the minimum is at a child-cell endpoint. If `A_C<0`, the only possible interior minimum is its explicit quadratic vertex; the checker tests that vertex only when its directed interval intersects the active cell.

On the moving lower boundary `x=67y`, the margin is affine in `sqrt(y)` and again has an endpoint minimum.

Thus every minimum is reduced to a finite directed gate while retaining all causal activation cuts.

## 4. Directed finite certificate

`X-91130` uses only the Python standard library, exact `Fraction` arithmetic, and outward fixed-point square-root intervals of scale `10^42`. It checks:

```text
all 319 odd P_61 thresholds t<4096;
every parent activation in (t,t+8];
every parent boundary y=d/67;
every child activation in 1<=y<67;
the constraint py>=t;
both a=4 and a=5;
every endpoint and every possible convex-cell vertex.
```

It proves `55,052` directed parent-cell gates and `55,200` child-Hall gates. The retained strict minima are

\[
\boxed{
\mathcal H_{4,t}^{\rm cau}>2.08044,
\qquad
\mathcal H_{5,t}^{\rm cau}>2.09101
}
\tag{L-91352.5}

throughout the finite region. Both minima occur on the boundary `x=67y` at threshold `t=66`.

The proof-object digest is

```text
d68de10aedfdc73033a2f21038164cd4a3a675284df89cc3475e84d461aa5d39
```

## 5. All large thresholds

For `t>=4096`, ignore the additional eight even capacities. `L-91328` gives, for the finite `P_61` forcing,

\[
F_1(z)>\frac3{40}\sqrt z,
\qquad
F_2(z)>\frac9{100}\sqrt z,
\qquad z\ge67.
\]

By affine interpolation,

\[
3F_{4/3}(z)>\frac6{25}\sqrt z,
\qquad
3F_{5/3}(z)>\frac{51}{200}\sqrt z.
\]

The complete child forcing is bounded above by `a sqrt(y)`. Since `x>=t` and `y<67`,

\[
\mathcal H_{4,t}^{\rm cau}
>\frac6{25}\sqrt t-\frac{4\cdot67}{\sqrt t},
\]

\[
\mathcal H_{5,t}^{\rm cau}
>\frac{51}{200}\sqrt t-\frac{5\cdot67}{\sqrt t}.
\]

At `t=4096` these are respectively

\[
\frac{4469}{400}>0,
\qquad
\frac{17737}{1600}>0,
\]

and both lower bounds increase thereafter.

## 6. Conclusion and scope

The nested-neighborhood Hall theorem yields target-mass and score-mass transports supported on

\[
\boxed{e\le o+8}
\]

for every `p>=67`, `1<=y<67`, and every threshold.

This theorem repairs the finite support-cutoff failure in `L-91350`. It proves Hall feasibility only. It does not identify a common target/score transport, reproduce the signed arithmetic row, or establish the global reset recurrence.

```text
true causal finite Hall gates             DIRECTED EXACT
true causal large-prefix Hall gates       EXACT
shift-eight target transport              EXISTS
shift-eight score transport               EXISTS
common positive row packet                SEPARATE
factor-54 reset                           OPEN
Riemann Hypothesis                        UNPROVED
```
