# Continuation: balanced-only closure and the remaining arithmetic source

**Proposed component proofs, not an arithmetic moment theorem or a new zero-free result. Independent mathematical review remains required.**

The preceding eight-file packet is now actually published in draft PR #916 at `dabd6da99fb92eead7c99f941331ed9cbd2ec4ad`. Its earlier failed-publication statements are preserved historical records. This continuation adds new files only; it does not alter that packet, PR #910, sibling research, or main.

## 1. The main advance removes the rectangular hypothesis

The preceding reconstruction required a mean square for pairwise-coprime factors at every rectangle of lengths. The new argument needs only the **equal-length, fixed-exclusion** estimate, with the same complete physical row range at every smaller scale.

At the slightly enlarged weight sigma=1/2+delta, one fixed finite-prime cutoff makes the entire nonidentity inverse-kernel mass q at most 1/3. Holder controls unequal products by the same finite diagonal-moment envelope. An absorption argument then proves

\[
 (1-q)^2M_\sigma\le B_\sigma\le C_\sigma\le(1+q)^2M_\sigma,
 \qquad M_\sigma\le\tfrac94B_\sigma,\quad C_\sigma\le4B_\sigma.
\]

Here M is the higher-moment envelope, B the balanced collision-free envelope, and C its rectangular version. The comparison is unconditional for any finite row measure. It does not say these quantities are small.

An explicit cutoff, exact reinsertion of the finitely excluded primes, and a moving-exclusion adapter are all proved. With arbitrarily small fixed delta, the resulting loss is absorbed into D^epsilon. Thus neither unequal factor lengths nor a changing exterior common divisor needs to remain an independent analytic hypothesis.

**The full-row condition remains:** at H=D^h the balanced input must cover all 1/b<=X<=D using that same H, not merely the curve H=X^h. The fixed cutoff and constants may depend on k and epsilon, but not on D or a moving row.

Read [BALANCED_CLOSURE.md](BALANCED_CLOSURE.md), especially Theorems 3.1 and 4.1.

## 2. Inspecting the arithmetic source rather than arbitrary coefficients

[CYCLE_FACTORIZATION.md](CYCLE_FACTORIZATION.md) gives a self-contained primitive-necklace factorization, explicitly attributed to the classical multivariate Witt identity. Applied to the literal coloured Möbius Euler source, it identifies all finite-degree L-factors and a nonvanishing analytic remainder, retaining every row-prime zero.

The pair correction is cubic in the sextic row phase; the triple correction is quadratic. Crucially, a hypothetical zero right of 1/2 is not cancelled by the pair correction. The factorization therefore rules out a tempting shortcut rather than asserting a zero-free result. Its Dirichlet-variable diagonal is carefully distinguished from equal physical factor windows.

## 3. A quantitative attack target

[DEFECT_BOOTSTRAP.md](DEFECT_BOOTSTRAP.md) compares the target with the inherited moment bound reported by sibling PR #913. At the reference boundary 7/8, a moment-exponent saving greater than 1/12 relative to that baseline would suffice for a strict improvement, in the limiting near-linear row range.

A further conditional proposition shows that a reusable fixed fractional improvement of the k-dependent defect would iterate a common boundary toward 1/2. That fractional-saving theorem is **not proved**. The example fractions 335/384 and 53/64 are conditional consequences only, not achieved bounds.

## Validation and limits

The new isolated checker passes 2,032 exact rational/cyclotomic predicates in normal and optimized Python, with identical output, and rejects three deliberate algebraic errors. It includes independently enumerated primitive rotation orbits and finite balanced-envelope tests. A separately modified result file is rejected. The earlier checker also freshly reproduced its 50,357 predicates and four rejected errors.

These are finite algebra fixtures, not numerical evidence for the genuine higher moments. No independent reviewer, Lean build, full upstream proof audit, or integration promotion is claimed. See [VALIDATION_AND_SOURCES.md](VALIDATION_AND_SOURCES.md).

The smallest remaining arithmetic obligation is now the literal **balanced, fixed-exclusion, full-row mean square** in BALANCED_CLOSURE.md (4.3), with a useful defect exponent. The continuation proves why that smaller statement suffices; it does not prove the statement itself.
