# FPCB23: common Dickman structure and a critical quotient remainder

**Status:** unconditional hardening and exact reduction; `CPQR23`, `FPCB23`, and RH remain unproved.

## 1. Literal two-row states

Retain the exact dictionaries

```text
q2(n):      0 for n<2, 3 at n=2, 0 at n=3, 1 for n>=4;
q3sharp(n): 0 for n<3, 6 at n=3, -2 at n=4, 1 for n>=5.
```

The physical third row is one third of the sharp row. Define

```text
B_j(y) = sum_(n<=y) q_j(n)/sqrt(n),
A_j(Y,z) = sum_(m<=Y, squarefree, P^-(m)>=z)
           mu(m)/sqrt(m) * B_j(Y/m).
```

Every activation is literal: the summand is active exactly when `mn<=Y`.

## 2. Exact common Dickman decomposition

Both base dictionaries have constant tail one. Put

```text
e_j(y) = B_j(y) - 2 sqrt(y).
```

Direct inspection of the initial cells and integral comparison of the common tail give

```text
-2 sqrt(2) <= e_2(y) <= 0,
-2 sqrt(3) <= e_3(y) <= 0              (y>=1).
```

Define

```text
S(Y,z) = sum_(m<=Y, squarefree, P^-(m)>=z) mu(m)/m,
E_j(Y,z) = sum_(same m) mu(m)/sqrt(m) * e_j(Y/m).
```

Then, exactly,

```text
A_j(Y,z) = 2 sqrt(Y) S(Y,z) + E_j(Y,z),   j=2,3.
```

Thus the two literal rows share one identical homogeneous arithmetic term.

Using the discrete rough-prime Dickman comparison from frozen PR #603,

```text
S(Y,z) = rho(u) + O(u/log z),
u = log Y/log z,
```

and a dimension-one upper-bound sieve,

```text
sum_(m<=Y, P^-(m)>=z) 1/sqrt(m) << sqrt(Y)/log z.
```

Hence simultaneously for both rows,

```text
A_j(Y,z) = 2 sqrt(Y) rho(u)
           + O(sqrt(Y) (u+1)/log z).
```

No scalar-only projection, rough-density surrogate, or smoothed activation appears.

## 3. Uniform positive corridor

Fix epsilon>0. De Bruijn's Dickman asymptotic gives, uniformly when

```text
2 <= u <= (1-epsilon) log log Y / log log log Y,
```

that

```text
rho(u) >= (log Y)^(-1+epsilon/2),
(u+1)/log z = u(u+1)/log Y = (log Y)^(-1+o(1)).
```

Therefore, for all sufficiently large Y,

```text
A_2(Y,z) > 0,
A_3sharp(Y,z) > 0.
```

Every future-prime quotient state outside the complementary critical corridor is closed unconditionally.

## 4. Exact transverse three-band correction

Because the dictionaries agree from index five onward,

```text
d(y) = B_3(y)-B_2(y)
```

is exactly

```text
0                                         for 1<=y<2;
-3/sqrt(2)                                for 2<=y<3;
2sqrt(3)-3/sqrt(2)                        for 3<=y<4;
2sqrt(3)-3/sqrt(2)-3/2                    for y>=4.
```

Consequently

```text
A_3sharp(Y,z)-A_2(Y,z)
 = sum_(m<=Y, P^-(m)>=z) mu(m)/sqrt(m) d(Y/m).
```

Thus the two hard errors are not independent: they consist of one common discrete-Dickman discrepancy plus one compact three-band transverse correlation.

## 5. Exact quotient/Bellman recurrence

Let p+ be the prime after p and let `A_(j,>=p)` denote the state whose rough factors are at least p. Partitioning the squarefree source according to whether p is absent or present gives

```text
A_(j,>=p)(Y)
 = A_(j,>=p+)(Y) - p^(-1/2) A_(j,>=p+)(Y/p).
```

The coefficient, accumulated sign, and activation are literal because

```text
p^(-1/2) r^(-1/2) = (pr)^(-1/2),
(Y/p)/r = Y/(pr).
```

A single root value is therefore not Markov. The smallest exact state is the complete descending future-prime quotient profile.

## 6. Sharp remaining theorem

Write

```text
R_j(Y,z) = A_j(Y,z) - 2 sqrt(Y) rho(u).
```

Whenever rho(u)>0, define

```text
Theta_23(Y,z)
 = max(-R_2(Y,z), -R_3sharp(Y,z))
   / (2 sqrt(Y) rho(u)).
```

Pointwise,

```text
A_2(Y,z)>=0 and A_3sharp(Y,z)>=0
<=> Theta_23(Y,z)<=1.
```

Define `CPQR23` as `Theta_23<=1` at every critical quotient state reachable from PR #592's future-prime owner tree. The complementary quotient states are positive by the corridor theorem, so finite backward induction in the quotient recurrence gives

```text
CPQR23 -> FPCB23 -> LPTRP23 -> RH.
```

`CPQR23` and `FPCB23` remain open and RH-bearing.

## 7. Negative controls

The following shortcuts are invalid:

```text
positive 5:3 scalar -> two positive rows;       false, e.g. (-1,2);
SACF square/energy -> one-sided sign;            phase-blind;
fixed-depth LAPBR67 -> all-depth state;          refuted by PR #589;
one root value -> exact future-prime state;      child quotient is required;
absolute Dickman remainder -> critical sign;     critical-sharp loss.
```

**RH status:** unproved.
