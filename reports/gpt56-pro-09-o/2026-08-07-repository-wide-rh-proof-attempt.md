# Repository-wide RH proof attempt

Date: 2026-08-07  
Agent: `gpt56-pro-09-o`  
Status: **proposed proof spine completed; one critical arithmetic lemma remains open**

## Executive result

The repository now has many exact finite dictionaries and several global
RH-equivalent coordinates. They are not independent mysteries. They measure the
same signed spectral/arithmetic obstruction through:

```text
screw value                 PR #202 / #218
constant Weil coordinate    PR #208
prime-prefix convex dual    PR #219
terminal/prime Hardy energy PR #216 / #222 / #224
analytic-totient energy     PR #226
completed annihilator       PR #217
localized operator floor    earlier Suzuki/CCM stack
```

The cleanest proof spine is the dyadic screw/transport route. On every physical
block `[2^r,2^(r+1)]`, one explicit `q=2` correction makes every remaining prime
coefficient nonnegative. Concavity reduces the whole block to finitely many
prime-power knots. At each knot the exact row is

```text
prime-quantile transport reserve
-
Bregman curvature penalty.
```

The penalty is bounded by the centered cumulative prime-mass square divided by
the exact archimedean curvature. A cofinal one-sided estimate for that reserve
minus square gives a subexponential screw lower envelope; Landau continuation
and pole exposure then give RH.

## New exact contribution

`L-23001` constructs a positive Selberg--Hankel adjoint resolvent for every real
exponential. For `lambda>1/2`,

```text
w_lambda(s)=1_(s>=lambda)[(lambda-1/2)/(s-1/2)]^2,
f_lambda(y)=integral_lambda^infinity exp(-s y)w_lambda(s)ds,
```

and

```text
L* f_lambda = exp(-lambda y).
```

The centered Selberg equation therefore gives an exact positive square:

```text
H(lambda)
+ integral_lambda^infinity w_lambda(s) H(s)^2 ds
= integral_lambda^infinity w_lambda(s) Rhat(s) ds.
```

This closes the abstract positive-adjoint construction for exponential tests.

`R-23001` proves that the tempting compact stop-loss version cannot work: the
unique compact adjoint needed for a lower bound is negative near its terminal
endpoint, contradicting positive-Hankel diagonal positivity. Thus the missing
step is a signed critical correlation theorem, not another ODE calculation.

## Exact unresolved lemma

`L-23002` states the common critical gate in four coordinates:

1. dyadic transport reserve dominates Bregman penalty up to `exp(o(r))`;
2. the prime-only safe-window energy is subexponential on every unit block;
3. the locally uniform vertical prime-energy integral is finite on compact
   sub-strips;
4. the analytic-totient local second moment is `O_epsilon(X^(2+epsilon))`.

The repository has closed:

- the diagonal;
- exact resonance;
- far-frequency large-sieve ranges;
- finite signed cell decompositions;
- pole-free multipliers;
- vertical pole tomography;
- exact real-axis Selberg squares.

It has not closed the critical Möbius/prime near-resonance cluster. Standard
large sieve loses one power; entrywise absolute values lose an exponential
factor.

## Relationship to the newest literature

- Suzuki, arXiv:2606.09096, gives the unconditional screw/Weil operator
  framework and explicitly leaves the cofinal spectral limit conjectural.
- Groskin, arXiv:2607.02828, gives an exact finite Guinand--Weil dictionary and
  tail order, but not source-space density or global positivity.
- Michalowski, arXiv:2607.16795, proves a large uniform positive Toeplitz wedge,
  while explicitly leaving the complementary RH-critical region open.
- Verjovsky, arXiv:2607.25002, identifies the same critical local-to-global loss
  for Möbius Fourier moments.
- Gaber, arXiv:2607.26114, supplies further totient-family RH criteria, not the
  critical local second-moment estimate required here.

The repository's final gate is therefore aligned with, rather than bypassed by,
the current literature frontier.

## Proposed proof candidate

`T-23001` is a complete conditional proof:

```text
L-23002 critical correlation
-> dyadic transport-minus-curvature lower bound
-> full dyadic-cell screw lower envelope
-> subexponential global screw envelope
-> Landau holomorphy
-> r-adic pole descent / field-separated pole exposure
-> RH.
```

It is intentionally labeled `GAP/BLOCKED AT L-23002`. It should be sent for
review as a proof candidate and gap-isolation document, not as a proof
announcement.

## Integration warning

The parent PR #218 contains duplicate claim IDs across concurrent theorem
families. The exact collision table and sign/curvature corrections are recorded
in

```text
audits/gpt56-pro-09-o/2026-08-07-pr218-proof-boundary-and-id-audit.md
```

A merge must renumber those families atomically.

## SERIOUS RESOLUTION PATH

A serious path remains:

```text
exact resonance/Jordan square
+ signed near-resonance dispersion
+ one-sided quantile reserve
-> L-23002
-> T-23001
-> RH.
```

The highest-value next theorem is not another finite xi matrix. It is the
critical signed common-cell estimate (L-23002.7), or an equivalent two-sided
Carleson/local-to-Bohr inequality.
