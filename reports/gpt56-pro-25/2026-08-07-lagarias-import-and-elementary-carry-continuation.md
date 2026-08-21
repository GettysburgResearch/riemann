# Lagarias import and corrected elementary carry attack — 2026-08-07

Status: `PROPOSED / EXACT REDUCTIONS + REFUTATIONS / RH UNPROVED`  
Issue: #245  
PR: #248

## 1. Paper imported

The branch imports Jeffrey C. Lagarias's paper

```text
An Elementary Problem Equivalent to the Riemann Hypothesis
arXiv:math/0008177
```

through:

- `T-24502`: the harmonic-number divisor-sum equivalence;
- `L-24506`: the elementary harmonic envelope used in the proof;
- `O-24502`: connections to Robin, colossally abundant numbers, and the carry
  route;
- `L-24521`: an exact prime-exponent increment-slope ledger for colossally
  abundant numbers;
- `literature/lagarias-2000-elementary-rh-equivalence.md`;
- `integration/gpt56-pro-25-245-lagarias-import.md`.

The dependency boundary is explicit. Lagarias's harmonic wrapper is elementary;
the global RH equivalence imports Robin's maximal-order divisor theorems.

## 2. Exact equivalence triangle

`T-24504` proves the synthesis

```text
Lagarias harmonic divisor inequality
<=> critical ordinary-prime ramp
<=> finite signed carry-block certificate
<=> RH.
```

The ordinary-prime and prime-power ramps differ by only `O(log^2 X)` by
`L-24517`.

## 3. New exact carry algebra

The strongest finite results now are:

1. `L-24501`: carry and entropy second differences; exact von Mangoldt dual;
2. `L-24502`: a non-arithmetic parabolic seed with objective
   `4 sqrt(X)-O(log X)`;
3. `L-24507`: proof-grade outer seed feasibility for `q>=X/28` beyond an
   explicit finite threshold;
4. `L-24508`: signed `b`-coordinates suffice; coefficient positivity is not
   needed;
5. `L-24509`: endpoint-projected divisor corrections are an exact positive
   Dirichlet Gram;
6. `L-24514`: a continuum objective-4 minorant is Möbius-unique;
7. `L-24517`: all higher prime powers can be removed at `O(log^2 X)` cost;
8. `L-24520`: a constant block in the `b`-coordinates transports residual
   exactly between two ordinary-prime incidences, with no third-row leakage;
9. `L-24521`: colossally abundant integers are sorted prefixes of an explicit
   prime-exponent slope ledger.

## 4. Refutations absorbed

The continuation did not preserve attractive false shortcuts.

### Monotone cover

`R-24501` proves that a nonnegative divisibility cover pays order `sqrt(X)` on
a fixed large-prime band. The old floating LP reconnaissance is retained only
as superseded provenance in `O-24501`.

### Nonnegativity of the convexified coordinates

`L-24508` proves this was an artificial burden. The von Mangoldt dual consumes
any real feasible vector.

### Generic Green energy

`R-24502` shows that the logarithmic vector `Lambda(q)` is itself dual-feasible.
A generic Green estimate would assume the prime-ramp deficit under another
name.

### `q+1` descent

`R-24503` corrects the sign: subtracting at `b_(q+1)` increases the `q` row. The
correct local coordinate is `b_q`.

### Flow plateau

`L-24518` records the corrected identity: a plateau in the flow variable
transports endpoint jumps, not endpoint incidences. Pure two-prime transport is
instead supplied by a constant block in the `b`-coordinates (`L-24520`).

## 5. Current proof boundary

The finite ordinary-prime geometry is completely soluble. Given any residual
vector, constant prime-endpoint blocks can set it to any prescribed terminal
vector. The exact minimum weighted loss is therefore the same scalar that the
prime-ramp criterion asks us to bound:

\[
J_{\mathbb P,X}(b_X^{(0)})-P_X.
\]

Thus generic transport, total positivity, a frame bound, or an LP solver cannot
finish the proof. A successful proof must supply new source-specific arithmetic
cancellation in that scalar.

The same phenomenon appears in Lagarias's coordinates: the CA slope ledger is
finite and explicit, but its cumulative comparison with the harmonic envelope
retains Robin's RH-bearing discrepancy.

## 6. Exact finite regression

`X-24503-carry-incidence-transport` checks with integer/Fraction arithmetic:

- the carry second difference;
- endpoint-incidence block transport;
- pure ordinary-prime transfers;
- the exact objective telescope;
- the reversed `q+1` sign;
- the corrected one-pass descending algorithm and its recurrence.

This authenticates finite algebra only.

## 7. Strongest current full proposal

The branch now presents two elementary coordinates on one final theorem.

### Prime-ramp coordinate

Prove

\[
P_X\ge4\sqrt X-X^{o(1)}.
\]

### Lagarias coordinate

Prove for every integer `n>=1`

\[
\sigma(n)\le H_n+e^{H_n}\log H_n.
\]

`T-24504` proves these are equivalent, and `L-24521` localizes the second to an
explicit sorted prime-exponent prefix ledger after importing Robin's CA
localization.

No proof of either final scalar is claimed in this report. The contribution is
a corrected, exact, reviewer-auditable elementary synthesis with several
formerly open geometric burdens removed and several false shortcuts formally
refuted.

## Review order

1. `T-24502/L-24506` and the literature note;
2. `L-24501/L-24502`;
3. `L-24507/L-24508`;
4. `R-24501/R-24502/R-24503`;
5. `L-24509/L-24514/L-24517`;
6. `L-24518/L-24520`;
7. `L-24521`;
8. `T-24504`;
9. `X-24503`;
10. the final prime-ramp or Lagarias scalar.
