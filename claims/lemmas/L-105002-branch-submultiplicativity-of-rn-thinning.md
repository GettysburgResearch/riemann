# L-105002 — Branch submultiplicativity of RN thinning: why free currents do not compose to Euler products

Claim ID: `L-105002`
Status: **PROVED EXACT**
Created: 2026-08-21
Agent: claude (external reviewer lane)
RH status: not assumed, not addressed

Used by `T-105000 §4` (structural explanation) and `R-105000`.
Machine checks: `X-105000` S1, S2.

## 1. Statement

The RN thinning system `R_{Z\mid Y}(t) = \mathbf 1_{t\le Z}\,T(Z/t)/T(Y/t)`
is chain-multiplicative (`L-99600.9`: `R_{W\mid Z}R_{Z\mid Y} = R_{W\mid Y}`
along nested endpoints) but **branch-submultiplicative**: for distinct rough
primes `p, q` and every `t` in the common support,

```
R_{Y/pq | Y/p}(t)   <=   R_{Y/q | Y}(t),
```

with strict inequality for every `t` in the interior of the common support
`1 \le t \le Y/(pq)` (equality only where both sides vanish). Proof: both
sides are values of `z \mapsto T(z/q)/T(z)`, at `z = Y/(pt)` and `z = Y/t`
respectively; this function is strictly increasing in `z` by the derivative
computation of `L-105001 §1`, and `Y/(pt) < Y/t`. ∎

## 2. Consequence: the free cone is not closed under Euler composition

For the two-prime Euler block applied to the parent measure, with
`R_p = R_{Y/p\mid Y}`, `R_q = R_{Y/q\mid Y}`, `R_{pq\mid p} =
R_{Y/pq\mid Y/p}`, the exact density identity

```
(1 - r_p R_p)(1 - r_q R_q) - [ 1 - r_p R_p - r_q R_q + r_p r_q R_{pq|p} R_p ]
      =  r_p r_q R_p ( R_q - R_{pq|p} )  >=  0
```

(verified symbolically, S2) shows the true two-prime block density is
**below** the product of the two free one-prime current densities, with
deficit `r_p r_q R_p (R_q - R_{pq\mid p})`. Positivity of each factor
therefore does not transfer to the composition: iterating free one-prime
currents exits the free cone, and the deficit accumulates along every branch
pair.

## 3. Why this matters

This is the structural reason the hierarchical program exists at all: the
native operator `\prod_p (I - r_p U_p)` is a composition of blocks each of
which is individually free (one-prime currents are inside the `L-105001 §1`
cap), yet the composition is not free — the branch deficit is exactly the
cross-prime interaction that every scheme then tries to re-own (reserves,
coboundaries, owner martingales). Together with the budget identity
(`T-105000` A.1–A.3) it closes the two natural hopes simultaneously:
composition does not stay free (this lemma), and re-owning the interaction
costs more than the unit budget once `\sum_{67\le p\le Y} 1/p > 1`
(the budget theorem).

## 4. Scope

Exact pointwise statements about the SHARP kernel family only. No claim is
made about other kernels (for `G(y) = a\sqrt y + b` the same derivative
computation applies with the numerator constant `-ab(\sqrt p - 1)` up to
positive factors, so the direction flips with the sign of `ab` — not needed
here and not asserted).
