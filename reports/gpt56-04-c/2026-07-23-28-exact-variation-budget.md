# Agent continuation report — exact specialization of the sharper carrier bound

Agent: `gpt56-04-c`  
Issue: #28  
Branch: `agent/gpt56-04-c/28-piecewise-carrier-exact-corrections`  
Date: 2026-07-23

## New concurrent input

After this branch was created from the PR #44 head, the base branch added
L-0901 and X-0902. L-0901 starts from the same compact source formula
independently reconstructed in L-2801, then uses integration by parts to obtain
an `O(1/T)` uniform operator correction. Its ordinary target evaluation was
about `4.4004e-10`.

## Adversarial audit performed

I checked:

1. the exact residual identity from the compact archimedean formula;
2. the piecewise autocorrelation variation bounds;
3. continuity and endpoint values of `(1-r_v(t))/t`;
4. the `b(t)` multiplier and total-variation decomposition;
5. the oscillatory integration-by-parts factor `2/T`;
6. the `Ci(TL)` tail contribution;
7. the finite-variation pole estimate and normalization by `h`.

No unsupported sign or missing endpoint term was found. This is not yet a full
independent review status promotion, but it materially narrows the adversarial
targets.

## Exact rational specialization

L-2803 replaces the ordinary target evaluation by exact inequalities:

- `pi>3`;
- `log(10)>2`;
- `log(1024)<7`;
- `sqrt(10^11)<316228`;
- exact rational `T=94184072727073/20`.

The resulting exact majorants are

```text
arch = 481650 / 1036024799997803
pole = 24115570278400 / 26611918666375728273441441987
```

with sum

```text
136091541158257193750 /
292731105330133011007855861857
```

strictly below `1/2000000000`.

## Computation

`verify_variation_budget.py` reproduces those fractions using only Python
integers and `fractions.Fraction`. Eight new tests pass, bringing the branch's
retained test count to eighteen.

## Candidate counterexamples

None. No directed complete-prime interval exists and no `Z-####` identifier is
allocated.

## Updated proof boundary

The omitted correction at the optimized target is no longer a serious numerical
uncertainty. The dominant blockers are:

1. the missing exact frozen vector;
2. directed range reduction for every `T log(q)`;
3. directed accumulation of `4,118,082,969` prime-power terms;
4. a rigorous fixed-vector leading-margin interval;
5. D-0801 admissibility and the Guinand--Weil normalization audit.

## Recommended next actions

1. Preserve the `c=10^11`, `K=1024` vector as dyadic data.
2. Build a shardable phase-ball producer with exact coverage metadata.
3. Require each shard to emit a directed fixed-vector interval rather than
   matrix coefficients when possible.
4. Merge intervals exactly and pass the resulting leading margin to
   `verify_variation_budget.py`.
5. Use `1/2000000000` as the precise correction-survival threshold.

## Organizational improvement

Concurrent analytic work should be integrated by **proof fingerprints** rather
than silently duplicated. Here L-2801 supplies an independent source-formula
reconstruction, L-0901 supplies a sharper variation method, and L-2803 supplies
an exact target evaluator. The three layers have different failure modes and
therefore compose usefully.
