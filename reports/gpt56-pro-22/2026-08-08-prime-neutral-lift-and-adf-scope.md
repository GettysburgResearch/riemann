# Prime-neutral lift: exact ordinary-prime closure and the surviving logarithmic obstruction

Date: 2026-08-08  
Agent: `gpt56-pro-22`  
Issue: #273  
Parent: draft PR #267 at `6d370d5a8c1a2ab11eb1af0581fe3c605863a757`

## Executive result

The annular divisor-frame proposal was pushed and then stress-tested in its
most dangerous exact direction.

That test shows that its proposed `L^2` repair norm is not the minimal RH-facing
quantity.  On the von-Mangoldt ray, the annular denominator is only
`O(X^-3/2)`, so a subpower annular flow would force the complete prime-ramp
error to be `X^-3/2+o(1)`.  The proposal remains sufficient but has been
demoted from “sole hinge.”

The same stress test produced a new exact finite theorem.

For ordinary primes alone, every nonnegative strongly additive dual potential
which is nondecreasing through `X>=8` vanishes below the endpoint.  Since the
parabolic residual at the endpoint prime is exactly zero, finite LP duality
proves that a coordinatewise nonnegative repair of **all ordinary-prime
constraints always exists**.

The graph obstruction is therefore gone.

## What remains

The ordinary-prime objective is not coordinatewise positive.  To preserve the
sharp entropy score, the repair must be neutral, or nearly neutral, on proper
prime powers.

The exact remaining theorem is:

```text
find h_m>=0
repair every ordinary-prime row
leave every proper-prime-power row unchanged
(or pay only X^o(1) in their weighted total).
```

This Proper-Power-Neutral Lift gives the ordinary-prime ramp
`4 sqrt(X)-X^o(1)` and hence RH.

Its finite Farkas dual is explicit: a nondecreasing additive arithmetic
potential whose first prime increments are nonnegative and whose higher
prime-power increments are free.  The complete logarithmic potential
`L(n)=log n` is an admissible ray, and its source pairing is precisely the
prime-ramp deficit.  Thus the remaining theorem retains the full RH burden;
nothing has been hidden in a soft feasibility statement.

## New exact files

```text
R-27301  ADF logarithmic overstrength
L-27301  ordinary-prime monotone-dual collapse
L-27302  proper-power-neutral Farkas dual
T-27301  corrected full elementary proposal
M-27301  fail-closed review protocol
X-27301  exact standard-library regression
```

## Correct status

```text
annular ADF                       sufficient / overstrong
ordinary-prime feasibility        proposed complete
proper-power-neutral lift         open / RH-bearing
full unconditional RH proof       not obtained
Riemann Hypothesis                unproved
```
