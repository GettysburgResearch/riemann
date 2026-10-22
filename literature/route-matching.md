# Literature-to-project route matching

Agent: `gpt56-03`  
Issue: #3  
Date: 2026-07-22

## Ranking rule

A route scores highly when it has:

1. a logically finite witness;
2. an exact or compact independently checkable certificate;
3. a search space that can be pruned without assuming RH;
4. numerical conditioning compatible with interval arithmetic;
5. assumptions independent of other active routes.

This is a counterexample-search ranking, not a ranking of mathematical
importance.

## Active routes already claimed

### Issue #1 — finite Weil positivity

**Literature match.** Weil 1952; Bombieri--Lagarias 1999; Bombieri 2000; recent
finite-dictionary work listed on agent #1's branch.

**Reusable contribution here.** `L-0310` proves the elementary support-to-finite
prime-power reduction. `L-0311` proves that a genuinely negative finite
Hermitian form has a rational/dyadic witness. `M-0301` requires exact
provenance and normalization records.

**Unresolved kernel.** The specific cutoff-free matrix identity used by
`D-0001/L-0001` still needs the independent source and sign reconstruction
requested by `Q-0004`.  This atlas intentionally does not assign `T-0305` to a
generic "Weil criterion" statement with unstated transforms.

### Issue #2 — Robin arithmetic witness

**Literature match.** Robin 1984; Lagarias 2002; Choie et al. 2007.

**Reusable contribution here.** `T-0301`, `T-0302`, `L-0320`, `L-0321`.

**Unresolved kernel.** The exact extremal reduction used in the search must be
proved.  Monotone exponents are safe by `L-0321`, but "search only colossally
abundant numbers" needs the exact minimal-counterexample theorem and its
hypotheses.

### Issue #7 — direct off-critical zeta rectangle

**Literature match.** Turing 1953; Booker 2006; Platt--Trudgian 2021; standard
argument principle and Rouché theorem.

**Reusable contribution here.** `L-0301`--`L-0304` and `T-0310`.

**Hard boundary.** No off-line zeta zero exists at height at most `3*10^12`.
Reconnaissance must start above that height, and a final certificate must count
zeros of an analytic normalization without crossing the critical line.

## Ranked unclaimed routes opened by this contribution

### 1. Issue #14 — Li coefficient negativity

**Why promising.** The witness is one integer index and one strict sign.
Bombieri--Lagarias supply both a zero-side and an arithmetic explicit-formula
view, permitting independent implementations.

**Starting kernel.** `L-0340` maps each zero by `z_rho=1-1/rho` and proves
`|z_rho|=1` exactly on the critical line.  It explains exponential sensitivity
to an off-line zero but also records the convergence caveat.

**Main risk.** Catastrophic cancellation grows with `n`.  A finite zero
truncation without a rigorous tail is unusable.

### 2. Issue #15 — Nicolas primorial inequality

**Why promising.** One-dimensional indexing, exact multiplicative recurrence,
no exponent-vector combinatorics.

**Starting kernel.** `L-0322` rewrites the two sides as
`prod_{p<=p_k} p/(p-1)` and `e^gamma log theta(p_k)`.

**Main risk.** The first violation, if any, may be astronomically remote.
Segmented prime enumeration must itself be certifiable.

### 3. Issue #16 — bounded-prime-sum `h(n)`

**Why promising.** It is a finite arithmetic witness with a natural
proof-producing dynamic-programming verifier.

**Starting kernel.** `L-0370` gives the exact recurrence.

**Main risk.** Exact global optimality is harder than finding a high-product
subset; scalable search needs safe dominance rules and compressed
certificates.

### 4. Issue #17 — Speiser derivative zero

**Why promising.** It converts disproof to a local zero-count problem for
`zeta'`, which may have different geometry from direct zeta zeros.

**Starting kernel.** `L-0330` composes Speiser with `L-0302`--`L-0304`.

**Main risk.** Zeros of a derivative can be ill-conditioned and close to the
critical line; contour lower bounds may dominate cost.

### 5. Issue #18 — positive-time de Bruijn--Newman zero

**Why promising.** A qualitatively different entire function and a one-way
finite witness at any explicit `t>0`.

**Starting kernel.** `L-0360` gives the exact threshold implication.

**Main risk.** Uniform complex-domain tail bounds for the defining integral,
especially the growth of `cos(zu)`, are technically demanding.

## Useful but lower-ranked routes

### Lagarias harmonic criterion

Finite and elementary, but its left side is the same divisor-sum object as
Robin while its right side introduces a large harmonic/exponential expression.
It is a valuable independent verifier for a Robin candidate rather than the
first search space.

### Pólya--Jensen

A nonhyperbolic polynomial is finite, but `T-0308` plus `T-0310` proves that no
such witness can occur for any shift below degree `9*10^24`.  This is a
rigorous search barrier, not a heuristic pessimism.

### Báez-Duarte/Nyman--Beurling

Excellent for functional-analytic structure and basis design.  Not presently a
finite-witness route: failure of a finite least-squares approximation does not
prove a positive distance from an infinite closed span.

### Extend the verified height

Mathematically useful, but extending `3*10^12` upward only removes possible
counterexamples.  It is verification infrastructure, not a counterexample-first
search unless paired with targeted off-line rectangles.

## Cross-route opportunities

1. **One certificate language.** `L-0304` supports both zeta, zeta-prime, and
   de Bruijn--Newman contour certificates.
2. **Two-formula sign checks.** Li and Robin/Lagarias candidates should be
   checked by independent exact identities before transcendental enclosure.
3. **Prime-stream infrastructure.** Issues #2, #15, and #16 can share certified
   segmented prime generation while keeping search logic independent.
4. **Dyadic witness conventions.** Issue #1's exact checker suggests a common
   schema: dyadic inputs, outward-rounded analytic enclosures, exact rational
   final inequality.
5. **Barrier registry.** Platt--Trudgian and Jensen bounds should be encoded as
   machine-readable exclusion regions so future agents do not repeat
   impossible searches.
