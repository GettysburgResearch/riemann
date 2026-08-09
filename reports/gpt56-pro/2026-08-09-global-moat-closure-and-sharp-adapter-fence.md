# Global prime-power moat closure and the SHARP-adapter fence

Date: 2026-08-09  
Authoring agent: `gpt56-pro`  
Status: **zero-insensitive correction globally closed; RH-facing upper wall open**

## 1. Global moat closure

The exact endpoint decomposition is

```text
A(X)=Delta_Lambda(X)+M(X),
```

where every original zeta-zero pole lies in `Delta_Lambda` and cancels from
`M`.

`L-90012` proves analytically for `X>=2000` that

```text
X M'(X)<-0.30.
```

`L-90014` closes the finite base. On an interval `(N,N+1)`,

```text
D M(X)=C_N-2S_1(N)/sqrt(X)-2sqrt(X).
```

Writing `y=sqrt(X)`, the exact interval maximum is attained at

```text
sqrt(N), sqrt(S_1(N)), or sqrt(N+1),
```

according as `S_1(N)` lies below, inside, or above `[N,N+1]`. A directed
70-digit certificate checks all `2<=N<2000`. The least-negative interval is
`(2,3)`, with exact upper value `-2sqrt(2)`.

Since

```text
M(2)=-4sqrt(2),
```

one obtains globally

```text
X M'(X)<-0.30,
M(X)<-4sqrt(2)-0.30 log(X/2)<0
```

for every real `X>=2`.

The prime-only correction is therefore completely settled on its natural
domain: it is explicit, zero-insensitive, negative, and strictly decreasing.

## 2. Corrected proof line

A final adversarial read found one invalid intermediate inequality in
`L-90012.8`: the upper bound

```text
log(m/(m-1)) <= 1/sqrt(m(m-1))
```

cannot be inserted into the negative coefficient of the same expression.

`R-90006` records the repair. Split the two terms and use

```text
log(m/(m-1)) <= 1/sqrt(m(m-1))
```

for the positive term, but

```text
log(m/(m-1)) >= 1/m
```

for the negative term. The final bound

```text
D J_Lambda <= 2S_(N-1)-2(N-1)/sqrt(X)
```

is unchanged, so every downstream constant and theorem survives. This repair
must be folded into `L-90012` during integration.

## 3. SHARP contact and exact failure

The endpoint derivative seed is exactly

```text
D b_X(q)=2q(q^-1/2-X^-1/2),
```

a node-weighted square-root hinge.

The most direct hoped-for adapter was that SHARP average-row positivity survives
multiplication by `q`. `R-90005` refutes this exactly. For

```text
g_T(q)=2sqrt(q)-2q/sqrt(T),
```

the average-row inverse first becomes negative at

```text
T=18, row=3,
a_18(3) in (-0.016357533249176,-0.016357533249175).
```

A larger witness is

```text
a_24(4)<-0.385666938614628.
```

Therefore full SHARP does not directly imply endpoint monotonicity through the
average-row representation. Pascal-cycle corrections, general balanced flows,
and source-coupled adapters are not refuted.

## 4. Exact remaining theorem

All unresolved sign is now carried by

```text
Delta_Lambda(X)
 =4sqrt(X)-sum_(n<=X)Lambda(n)/sqrt(n)log(X/n).
```

The minimal upper-wall gate is

```text
Delta_Lambda(X)<-M(X).
```

At derivative level it is

```text
psi_1/2(X)-2sqrt(X) >= X M'(X).
```

The right side is now an explicit globally negative function with a proved
uniform bound below `-0.30`. Eventual endpoint monotonicity follows from this
lower wall and implies RH. Proving the wall remains the entire conclusion-
producing problem.

## 5. Replay order

```text
X-90012  finite constants for analytic tail;
X-90014  all intervals below 2000;
X-90009  five-million endpoint reconnaissance;
X-90013  node-weighted average-row refutation.
```

Expected lines:

```text
PASS_EXPLICIT_PRIME_POWER_MOAT_DECREASE_CONSTANTS
PASS_GLOBAL_PRIME_POWER_MOAT_FINITE_BASE
PASS_PRIME_POWER_MOAT_AND_MONOTONICITY_RECONNAISSANCE
PASS_NODE_WEIGHTED_SHARP_AVERAGE_ROW_REFUTATION
```

RH remains unproved.
