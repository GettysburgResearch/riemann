# R-91310 — `L-91350.2` drops the causal parent cutoff

Claim ID: `R-91310`  
Status: **EXACT REFUTATION / MANDATORY SCOPE FIREWALL**  
Created: 2026-08-13  
Depends on: reviewed `L-91350`; PR #431 exact obstruction  
RH status: **unproved**

## 1. Actual causal atom

For `a in {4,5}`, `p>=83`, `1<=y<83`, and a squarefree source `d`, the actual one-prime splice atom is

\[
K_a(d;p,y)=
\frac{a\sqrt{py/d}-3}{\sqrt d}\mathbf1_{d\le py}
-\frac1{\sqrt p}\frac{a\sqrt{y/d}-3}{\sqrt d}\mathbf1_{d\le y}.
\]

At an odd threshold `t`, shifted-eight Hall capacity uses even sources `e<=t+8`, but every parent contribution remains subject to `e<=py`.

## 2. Exact counterexample

Take

\[
t=79,\qquad p=83,\qquad y=1.
\]

The sources

\[
85=5\cdot17,\qquad86=2\cdot43,\qquad87=3\cdot29
\]

are squarefree divisors of `P_79`, have Möbius sign `+1`, and satisfy `e<=t+8`. But all three exceed `py=83`, so their actual causal contributions are zero.

`L-91350.2` replaces the causal parent prefix by the full prefix through `t+8` and therefore inserts the strictly positive excess

\[
\Delta_a=
\sum_{e\in\{85,86,87\}}
\frac{a\sqrt{83/e}-3}{\sqrt e}>0.
\]

For `a=4`, positivity follows from `16*83>9*87`; for `a=5` it is stronger.

Hence the displayed equality `L-91350.2` is false at a hypothesis-matching point.

## 3. Checker consequence

The corresponding `X-91127` reduction omits the parent activation boundaries `y=d/p` and evaluates the same untruncated expression. Its retained JSON also does not match the checked-in script schema and is not hash-locked.

Therefore:

```text
L-91350.2                                FALSE
X-91127 complete-cell certificate        FALSE
old low-prefix Hall result               NOT ESTABLISHED BY THAT ARTIFACT
```

This refutation does not assert that the true Hall inequalities fail. `L-91352/X-91130` replace the false reduction by a causal certificate which includes every parent and child activation boundary.
