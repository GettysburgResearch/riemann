# Extra-high redo of the final passes and renewed full-problem attack

Date: 2026-08-08  
Agent: `gpt56-sol`  
Repository: `gfreund123/riemann`

## 1. Why this redo was necessary

The preceding two passes moved too quickly from useful boundary identities to a claimed "final frontier."  Re-reading the live graph at current heads changes the assessment.

Two corrections are essential.

### PR #309 was an advance, not a completion

The following results survive:

- ordinary terminal atomization of the complete critical boundary has `Omega(X)` weighted atomic norm;
- complete recombination has only logarithmic reciprocal-eta/Mersenne sparse variation;
- the same logarithmic regularity persists for every **fresh** analytic support-halving endpoint layer.

But the already-emitted boundary bank still has to propagate through the later central/Pascal cascade.  The reciprocal-eta Mersenne ledger is itself RH-sensitive.  Fresh-layer regularity alone does not bound that complete propagated ledger.

### PR #321 was not a final unconditional proposal

Its transition certificate was an explicit open theorem.  It was a useful coordinate choice, but calling that object the final attack did not satisfy the standard that reviewers receive a proof rather than a construction assignment.

The present redo therefore does not treat PR #321 as a completion.

## 2. Live-graph corrections

The live repository also invalidates several tempting shortcuts which became visible only after those passes.

- PR #323 corrects the five-adic finite-state picture: nonzero residue modes carry nonprincipal Dirichlet `L`-functions, and the zeta mode is neutral.  There is no source-free finite automaton contraction.
- PR #318 corrects the Brownian/Robin-fiber route: positive mixtures of individually real-rooted fibers need not remain real-rooted.
- PR #317 shows that exact eta terminalization algebraically returns to the pure central producer; pointwise positivity is not recovered by merely changing gauge.
- PR #311 shows generic central-band variation can amplify.  Any boundary estimate must remain source coupled.

These are now mandatory firewalls.

## 3. New exact refutation: source-independent monotonicity is insufficient

`R-32401` gives a `337`-edge integer Farkas certificate at endpoint `50` showing that the decreasing target

```text
w(q)=1  for 2<=q<=23,
w(q)=0  for q>=24
```

is outside the quarter-balanced carry cone.

Thus a proof of the critical carry theorem cannot follow from generic monotonicity/decreasingness.  The critical source must be used at a stronger arithmetic level.

The exact checker gives

```text
balanced edges                         337
separator zero edges                    30
separator positive edges               307
target pairing                           -1
```

## 4. New analytic reserve: radius one half

`L-32401` strengthens PR #286's shifted analytic contraction from coefficient radius `1/4` to the natural dyadic radius `1/2`.

For every critical half-integer exponent `s=1/2+h`, the exact weighted row sum is bounded by

```text
B(s)=(8/3)(2/3)^s-(5/3)(1/2)^s,
```

which decreases with `h`, and

```text
B(1/2)<5993/6000<999/1000.
```

Hence the complete shifted analytic bulk satisfies

```text
||C f||_(1/2) <= (999/1000)||f||_(1/2).
```

The proof uses only the elementary rational bound `zeta(3/2)<8/3`.

This is materially stronger than the former `1/4`-radius reserve and aligns with the dyadic square-root weights used by the discrete boundary/capacity programme.

## 5. New parity-filter reserves

The parity-paired Euler source on PR #263 remains one of the few fixed source transformations which is both zero-safe and exactly invertible.

`L-32402` proves in the **same multiplier coordinate** that the exact positive Bézout synthesis satisfies

```text
|U(z)|^2+|U(-z)|^2 <= (697-252 sqrt(2))/36
```

throughout the complete critical annulus, while the analysis pair satisfies

```text
|p(z)|^2+|p(-z)|^2 >= 45/4.
```

The strict gap is

```text
(63 sqrt(2)-73)/9 > 0.
```

`L-32403` then uses the exact block length `log 2`: all synthesis delays are whole blocks.  The reconstructed unfiltered block obeys

```text
O_m <= q_sigma * sum_(j=0)^3 E_(m-j),
q_sigma < 3,
```

so the synthesis charge normalized by the fixed analysis reserve is strictly below

```text
4/15.
```

This removes the finite inverse filter and delay bookkeeping as possible reasons for failure of the parity route.

It does **not** supply the missing reflected Selberg upper estimate.

## 6. Renewed global attack

The live graph now has two genuinely source-specific routes worth pursuing, rather than the previous abstract transition certificate.

### A. Square-root hinge flow

PR #295 proves exactly that the critical target is a positive combination of

```text
h_T(q)=q^(-1/2)-T^(-1/2),  q<=T.
```

A positive balanced flow for every `h_T` would therefore give the critical flow by positive superposition.  Finite LP reconnaissance shows these hinges remain feasible far beyond the ranges at which fixed central/ternary producers become negative, so the correct theorem is an adaptive Pascal-cycle/parity construction, not a stationary branching law.

No all-`T` proof is asserted in this report.

### B. Full parity-paired reflected source

PRs #263/#269 prove:

- exact closed-strip parity frame;
- positive finite Bézout reconstruction;
- positive generalized-prime synthesis;
- factor-five localization of every negative Kummer row;
- a strict individual-wavelet carry reserve;
- exact zero/first/second source moments.

The remaining issue is the complete source-coupled independent-frequency reflected matrix.  The new analysis/synthesis bounds show that any failure must come from the Selberg/prime source coupling, not from loss of the inverse-zeta mode or a large finite reconstruction charge.

## 7. Honest status after the redo

```text
fixed-order Abel positivity                 false
monotone-target balanced feasibility        false generically
atomic endpoint closure                     false
five-adic source-free automaton              false
positive Brownian-fiber mixture closure      false

shifted analytic half-radius bulk            strictly contractive
parity analysis/synthesis filter bank        strict finite reserve
finite parity block synthesis delay charge   <4/15 of analysis reserve

square-root hinge positive flow              open / RH-bearing
source-coupled reflected Selberg matrix       open / RH-bearing
Riemann Hypothesis                            unproved
```

The project should not be declared closed until one of the last two source-specific statements is actually proved with all rows and cross terms emitted.

## 8. Exact replay

`X-32401-extra-high-crosschecks` verifies the finite cone separator and every rational constant used in `L-32401`.

```text
verdict
PASS_EXACT_EXTRA_HIGH_REDO_CROSSCHECKS

proof-object SHA-256
b5aeccb0edb8738152af5e339f96d6592d12601a3e7c19be14e182c986e1d965
```

No finite regression is represented as an RH proof.