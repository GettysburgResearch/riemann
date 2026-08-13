# CFFP three-route review packet

Date: 2026-08-13  
Branch: `research/gpt56-pro/91355-causal-packet-budget`  
Status: **three ambitious closure routes; RH remains unproved pending independent review**

## Executive map

All three routes start from the exact `P_61` stopping-line decomposition and the same-index child functor. They differ only in how the complete current finite block is realized.

```text
Route A  canonical finite-Euler row
Route B  provenance-causal generator packets
Route C  Hall / interval-seed / butterfly finite cone
```

The routes have deliberately different proof risks. A failure in one does not automatically invalidate the others.

# Route A — Direct canonical row

## Claim

Use

\[
D_{P,X}(j)=\sum_{d\mid P_{61}}\frac{\mu(d)}{\sqrt d}Q_{X/d}(j).
\]

The branch theorem `L-91364` proposes that this row is globally nonnegative. `L-91363` gives its exact positive ordinary and radix-four capacities, and PR #437 gives a strict literal entropy surplus over the declared score.

## New attack

`L-91370` closes an implicit first-activation-strip step in the large-row proof:

\[
0\le j^{3/2}Q_{jv}(j)<8\sqrt v-7-\frac32\log v
\]

for `j>=7` and `1<=v<1+1/j`. Thus negative-parity first-strip terms are automatically conservative; only positive-parity activations require the finite loss already charged in `L-91364`.

`L-91371` removes the label-duplication ambiguity. The two current finite labels form one joint packet with target row `(1,2)` and score row `(2,1)`. They are summed before physical packing, while rough children remain labelled.

`T-91310` records the resulting candidate composition:

```text
joint finite source
 -> globally nonnegative canonical row
 -> exact positive ordinary/detail capacities
 -> literal entropy surplus
 -> factor-67 packet recurrence
 -> O(log X) endpoint deficit
 -> endpoint RH criterion.
```

## Review burden

1. Re-run and independently reconstruct `X-91138`.
2. Check every analytic estimate in `L-91364`, including `L-91370`.
3. Verify the joint target/score/row dictionary in `L-91371`.
4. Replay the frozen PR #437 score theorem at identical normalization.
5. Rebuild the root endpoint criterion and finite base.

## Status

```text
canonical row sign                 PROPOSED COMPLETE
capacity                            EXACT
literal entropy                     STRICTLY FAVORABLE
label dictionary                    CLOSED
normalization audit                 REQUIRED
RH                                  UNPROVEN
```

# Route B — Provenance-causal packets

## Claim

Do not invert the complete finite Euler row. Instead use the exact first-hazard source partition and realize each causal generator

\[
P_X-rU_pP_{X/p}
\]

as a positive current packet, while passing only the safe contracted child.

The provenance proposal on the branch retains exact source identity, target spent once, same-index capacity covariance and literal row entropy.

## New attack

`T-91311` observes that the provenance coefficients are not merely substochastic: their total contracted-child mass is below `1/8`. Therefore a mass-proportional local generator theorem yields the stronger envelope

\[
\Lambda(X)\le C+\frac18\Lambda(X/67+C_0),
\]

and hence

\[
\boxed{\Lambda(X)=O(1)}.
\]

This is stronger than the logarithmic deficit required by the endpoint theorem.

## Review burden

1. Rebuild the exact first-hazard source identity.
2. Verify that the physical child mass uses the same additive normalization as the packet envelope.
3. Check every current generator in rows, ordinary/detail columns, entropy and any port coordinate.
4. Confirm that current-generator debt is uniformly mass proportional.
5. Rebuild the root endpoint implication.

## Status

```text
source provenance                    EXACT
child coefficient sum <1/8           EXACT
subcritical consumer                  CLOSED / T-91311
physical generator typing             REVIEW-CRITICAL
RH                                    UNPROVEN
```

# Route C — Hall, interval seeds and butterflies

## Claim

Use no-upward parity Hall transports, convert matched edges into nonnegative interval seeds, and realize those seeds by compact adjacent endpoint butterflies plus explicit positive boundary atoms.

## New attack

`L-91372` identifies the complete dual cone. For an endpoint functional `y_T`, put `g_T=y_T/alpha_T`. Then

\[
\langle y,\mathcal B_T\rangle
=\alpha_T[\theta_Tg_{T-1}+(1-\theta_T)g_{T+1}-g_T].
\]

Thus a functional is nonnegative on every adjacent butterfly exactly when `g` is convex on the endpoint-state nodes.

Consequently every failure of the finite shadow producer has a fail-closed witness:

```text
nonnegative row/detail/port multipliers
+ one discrete convex endpoint potential
+ a positive separating margin.
```

Score is not an obstruction because every butterfly strictly improves literal entropy. Any separator must use a genuine physical row, detail column or boundary port.

## Review burden

1. Fix the exact finite primal cone on endpoints through `55`.
2. Produce either nonnegative butterfly intensities and boundary allocation, or an explicit convex dual separator.
3. Verify all ordinary/radix-four destinations and final endpoint coefficients.
4. Charge the one boundary atom and any port once.

## Status

```text
Hall-to-interval seed                   EXACT
positive butterfly factorization        EXACT
score orientation                        FAVORABLE
finite convex dual                       CLOSED
primal feasibility / no separator        OPEN FINITE PROBLEM
RH                                       UNPROVEN
```

# Comparative verdict

The recommended order is:

1. **Route A first.** It is the shortest and now has one explicit exact row plus an exact capacity and entropy dictionary.
2. **Route B second.** It is independent of global canonical-row positivity and, if typed correctly, gives a uniform rather than logarithmic deficit.
3. **Route C third.** It is the fail-closed finite fallback and the best adversarial audit mechanism for the first two routes.

No route should be promoted from candidate to proof by summary agreement. The load-bearing theorem, its exact replay, and the endpoint normalization must be reconstructed line by line.

# Reviewer path

```text
L-91370
L-91371
L-91364 + X-91138
L-91363
PR #437 literal entropy theorem
T-91310

T-91311
provenance generator claims and replays

L-91372
L-91320/L-91321
L-91102
```

# Final status

```text
CFFP Route A             CANDIDATE COMPLETE / REVIEW REQUIRED
CFFP Route B             ONE PHYSICAL GENERATOR GATE
CFFP Route C             ONE FINITE CONE FEASIBILITY GATE
Riemann Hypothesis       UNPROVEN
```
