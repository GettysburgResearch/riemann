# Research report — third-Abel source-specific attack on the binary–ternary carry producer

Date: 2026-08-08  
Agent: `gpt56-sol`  
Parent: PR #277 at `d5be8262c80a1debcf86922b45a4d00a406803f1`  
Status: **SERIOUS FULL CONDITIONAL PROPOSAL; TWO EXPLICIT SIGN GATES OPEN; RH UNPROVED**

## Executive result

The scope audit suggested attacking a surviving source-specific statement instead of its failed generic surrogate. I selected PR #277's binary–ternary producer positivity theorem because `L-23814` shows that positivity alone automatically gives the required `O(log^2 X)` weighted variation and therefore the sharp prime ramp.

The attack produced one exact failure and one new reduction.

### Failure

The producer is not positive on arbitrary nonnegative targets:

```text
K_8(3,4)=-1.
```

More importantly, even the natural second-Abel cumulative kernel is not positive. For the ramp target

```text
w(q)=60-q,  2<=q<=59,
```

at endpoint `X=60`, the exact producer coefficient is

```text
A(11)=-13/16.
```

So convexity of the critical target is not enough.

### Advance

The third cumulative kernel

```text
S_X(n,Q)=sum_(q<=Q) binom(Q-q+2,2) K_X(n,q)
```

is the first Abel order that survived exact rational stress testing. `X-27801` checks every `2<=Q,n<=80`, 6,241 rows, with no negative value.

The actual source

```text
w_X(q)=q^-1/2 log(X/q)
```

has a stronger property than convexity: its continuous extension is completely monotone on `(0,X]`. Hence every interior third forward/backward source difference in the exact Abel identity has the correct sign.

This yields the new split:

```text
all-scale third-prefix positivity
+ exact endpoint collar positivity
-> producer positivity.
```

The only place the RH-sensitive source is needed is the collar; the interior kernel theorem is a rational combinatorial statement.

## Exact mathematics

`L-27801` proves the third-Abel identity

```text
A_X(n)=sum_Q S_X(n,Q)
 [w_X(Q)-3w_X(Q+1)+3w_X(Q+2)-w_X(Q+3)],
```

with zero extension beyond `X` retained explicitly.

For

```text
f_X(x)=x^-1/2 log(X/x),
```

one has

```text
(-1)^k f_X^(k)(x)=x^(-k-1/2) P_k(log(X/x)),
P_0(L)=L,
P_(k+1)(L)=(k+1/2)P_k(L)+P_k'(L).
```

Every coefficient of `P_k` is nonnegative, so the source is completely monotone. Repeated integral finite differences give nonnegative third differences before the endpoint zero-extension collar.

## Proposed closing theorem — TACP

For an explicit collar width `L_X`, prove:

```text
TACP-I:
S_X(n,Q)>=0
for Q<=X-L_X-1;

TACP-B:
sum_(Q in endpoint collar) S_X(n,Q) Delta^3 w_X(Q)>=0
for every n.
```

Then the exact Abel identity proves `A_X(n)>=0`.

PR #277 `L-23814` supplies

```text
A_X>=0
-> sum A_X(n)sqrt(n)=O(log^2 X)
-> BTF
-> prime ramp >=4sqrt(X)-polylog(X).
```

The inherited square-screw/Landau consumer gives RH.

## Why this looks attackable

TACP-I contains no zeta values, logarithms, or asymptotics. It is a finite combinatorial positivity statement about:

```text
Möbius inversion of a quadratic discrete spline
+ the fixed four-child binary/ternary ancestry graph.
```

Its likely proof variables are quotient cells, Pascal cycles, and binary/ternary residue classes. The squarefree collector algebra of PR #274 may provide local rewrites for a negative forcing cell without requiring generic target positivity.

TACP-B is source-specific and small. The obstruction is exactly the endpoint introduced by zero extension, not the whole interval. A proof can target the complete collar sum rather than every source difference separately.

## Exact checker

`experiments/X-27801-third-abel-kernel/verify.py` uses only integers and `fractions.Fraction`.

Retained output:

```text
PASS_EXACT_THIRD_ABEL_KERNEL_RECONNAISSANCE
generic_negative_K_3_4 -1
second_prefix_witness_Q59_n11 -13/16
third_prefix_rows_checked 6241
third_prefix_minimum 0
third_prefix_argmin (2, 3)
```

Verifier SHA-256:

```text
3b9558d89aba2e3eb2d5610b0e8cbdcacb75df78b7588e03065c910cb3b87ba7
```

This is finite evidence only.

## Honest boundary

```text
source complete monotonicity                  proved
third-Abel finite identity                    proved
raw target positivity                         refuted
second-prefix positivity                      refuted exactly
third-prefix all-scale positivity             open
endpoint collar positivity                    open
producer positivity                           open
TACP -> sharp carry route -> RH               conditional chain
Riemann Hypothesis                            unproved
```

The main research value is that the sign theorem is no longer one opaque Möbius recurrence. It is split into a universal third-prefix kernel problem and a sharply localized source boundary problem, while exact lower-order failures prevent accidental return to a false ambient positivity argument.
