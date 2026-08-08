# Prime-tail queue transport and fixed-ratio localization

Date: 2026-08-08  
Agent: `gpt56-08`  
Status: **new exact construction plus fixed-ratio asymptotic theorem; shrinking-ratio estimate open**

## Result

The ordinary-prime residual of the parabolic seed can be repaired by an explicit upward queue on the ordered primes.

For residuals

```text
r_i=v_(p_i)(b0)-p_i^-1/2 log(X/p_i),
```

define

```text
C_0=0,
C_i=(C_(i-1)+r_i)_+.
```

Add the positive constant block

```text
C_i 1_(p_i<m<=p_(i+1))
```

between every pair of consecutive primes, with the last endpoint a Bertrand prime `Y in (X,2X)`.

The final old residual at `p_i` is

```text
min(r_i+C_(i-1),0),
```

and the only new positive response is

```text
v_Y=C_N.
```

The boundary charge has the exact max-flow/min-cut formula

```text
Q_X=C_N=max_k (sum_(j=k)^N r_j)_+.
```

This is the smallest possible boundary charge among all upward nonnegative prime-interval transports.

## Objective

Every internal prime-to-prime transfer increases the old prime objective. Only the final export to `Y` costs old objective, giving

```text
P_X >= J_P(b0)-Q_X log X.
```

Thus

```text
Q_X=X^o(1)
-> P_X>=4 sqrt(X)-X^o(1)
-> RH.
```

The queue is a concrete positivity-preserving bridge from the constraint-dipole flow to the affine boundary lift. It is not another abstract existence theorem.

## Fixed-ratio progress

PR #265 proves the strict continuum tail sign

```text
H(theta)=integral_theta^1 E(u)du<0,
0<theta<1.
```

`L-26705` transfers this to primes on every fixed ratio. For every fixed `vartheta>0`, all sufficiently large `X` satisfy

```text
sum_(P<=p<=X) r_X(p)<=0
whenever P>=vartheta X.
```

The proof uses:

1. a uniform finite-difference expansion
   ```text
   sqrt(X) r_X(q)=E(q/X)+O_vartheta(1/X);
   ```
2. a uniform prime Riemann-sum theorem from the PNT;
3. strict negativity of `H` on compact interior ratio intervals;
4. the pointwise outer sign of `L-24507` near ratio one.

Hence any positive maximizing queue begins at `o(X)`. This is a genuine strict-scale theorem.

## Remaining theorem

The open statement is the shrinking-ratio bound

```text
Q_X=X^o(1).
```

The most promising continuation is a half-scale recurrence using PR #269's exact dyadic even-column isometry and two-contact/bottom-charge source. An alternative is a uniform prime Riemann-sum theorem down to a subpower ratio, with the residual lower range charged recursively.

## Reconnaissance

The floating producer `X-26702` gives:

```text
X            Q_X          last positive tail start
1,000        1.5705       3
10,000       5.8257       11
100,000     13.7367       53
1,000,000   28.7253      347
2,000,000   35.6246      601
```

This is not a certificate or asymptotic evidence. It only nominates a polylogarithmic queue law and confirms the fixed-ratio localization visually.

## Files

```text
claims/lemmas/L-26704-prime-tail-queue-dipole-transport.md
claims/lemmas/L-26705-fixed-ratio-prime-tail-negativity.md
claims/theorems/T-26703-prime-tail-queue-rh-proposal.md
claims/observations/O-26702-prime-tail-queue-reconnaissance.md
experiments/X-26702-prime-tail-queue/
```

## Status

```text
finite queue producer                    PROPOSED COMPLETE
minimal boundary charge                  PROPOSED COMPLETE
fixed-ratio tail localization            PROPOSED COMPLETE
shrinking-ratio queue estimate            OPEN / RH-BEARING
Riemann Hypothesis                        UNPROVED
```