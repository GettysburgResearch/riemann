# M-9501 — Proof-carrying screw-witness pipeline

Claim ID: M-9501  
Title: Certificate architecture for prime-knot scalar, metric, and Gaussian witnesses  
Status: PROPOSED  
Authoring agent: `gpt56-08`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: D-9501, L-9501, L-9502, L-9503  
Scope: Issue #95 implementation and verification plan  
Related counterexample candidates: none yet

## Objective

Turn Suzuki's explicit zeta screw function into a small trusted proof object.
The discovery implementation may use fast ordinary arithmetic, but every
promoted witness must be replayed from exact inputs with directed intervals
and independently checked.

The route has three escalating levels:

```text
scalar prime-knot minimum
        -> three-value Hilbert-metric defect
        -> finite screw / Schoenberg-Gaussian Rayleigh defect.
```

A failure at any level is sufficient; later levels are not logical gates for
earlier ones.

## Phase A — normalization and source gate

Before a candidate receives a `Z-####` identifier, two independent reviewers
must check:

1. the repository and Suzuki use
   `xi(s)=s(s-1)pi^(-s/2)Gamma(s/2)zeta(s)/2`;
2. Suzuki's `g` is exactly `-Psi`;
3. the PSD screw kernel is exactly
   `Psi(t)+Psi(u)-Psi(t-u)`;
4. the prime formula uses `n<=exp(t)` and all prime powers with
   `Lambda(p^k)=log(p)`;
5. the implication used by the certificate is genuinely `RH => predicate`,
   not its reverse alone;
6. the source's zero and Fourier conventions introduce no hidden factor of
   `2`, `pi`, or `i`.

This gate is logical and cannot be repaired by a wider numerical interval.

## Phase B — manifest and smooth-function gate

### Prime-power manifest

A production manifest is a sequence of records

```text
(q, p, k, shard_id, ordinal)
```

with exact integer checks

```text
q == p**k
p prime
k >= 1
strictly increasing q
no duplicate q
complete declared interval coverage.
```

Completeness should be established by an independent segmented prime sieve
plus repeated multiplication, not inferred from the producer's row count.
Every shard receives a cryptographic digest and exact lower/upper integer
coverage endpoints.

### Directed primitive rows

For each prime power, produce balls for

```text
tau = log(q)
w   = log(p)/sqrt(q)
w*tau.
```

Use positive-square-root and real-log branches only.  Store sufficient
precision that cumulative prefix widths remain below a declared budget.

### Smooth evaluator

Implement both:

1. the elementary series and tail bound in `L-9503.12`;
2. an independent Arb evaluation of the original Lerch/digamma formula.

The two enclosures must intersect at random and adversarially selected points,
including `log(2)`, knots, near-knot dyadics, and the smallest discovery
margins.

## Phase C — complete scalar cell certificates

For each cell `[tau_j,tau_{j+1}]`:

1. enclose the right derivative at `tau_j` and the left derivative at
   `tau_{j+1}` using the same exact prefix;
2. if both force monotonicity, certify the appropriate endpoint;
3. otherwise bracket the unique root of `A'(t)=P_0,j` by directed bisection or
   interval Newton;
4. evaluate the strong-convexity lower bound
   \[
      Psi(x)-Psi'(x)^2/(2A''(tau_j));
   \]
5. record a positive lower endpoint for the entire cell or a negative upper
   endpoint at one exact node;
6. update the knot through the local recurrence and checkpoint against the
   independent two-prefix formula.

A **complete positivity certificate through `Q`** contains a Merkle-style
summary of every cell lower bound and the smallest global lower endpoint.  It
does not prove RH; it excludes a scalar screw witness only through that finite
cutoff.

A **negative scalar certificate** contains only the exact node, the manifest
prefix digest, the smooth enclosure, the prime enclosure, and a final interval
whose upper endpoint is below zero.

## Phase D — targeted metric search

Use the smallest scalar cells and the largest derivative jumps as a node pool.
Search the polynomial defects

\[
 \Delta_\pm(t,u)=4\Psi(t)\Psi(u)
 -\left(\Psi(t)+\Psi(u)-\Psi(t\pm u)\right)^2.
\]

The discovery optimizer may move nodes continuously, but a nomination is
frozen to exact dyadics or symbolic knots before replay.  Search priority:

1. first deposition cells around `t`, `u`, and `t+u`;
2. pairs whose scalar values are unusually small;
3. pairs whose normalized determinant is unusually small;
4. pairs stable under precision doubling and node perturbation.

The proof checker recomputes the three shared `Psi` values once and contracts
the exact polynomial.  It must not evaluate duplicated copies with unrelated
intervals, because that destroys correlation and can fabricate width.

## Phase E — finite matrix and Gaussian search

For selected exact nodes, construct the primitive distance table

\[
 D_{ij}=\Psi(t_i-t_j).
\]

Search four related objects:

1. the anchored screw matrix `S`;
2. the restriction of `-D` to an exact rational basis of the zero-sum
   subspace;
3. exact frozen Rayleigh vectors from approximate negative eigenmodes;
4. Gaussian kernels `exp(-lambda D)` over an exact dyadic scale ladder.

Do not certify an eigenvalue by calling a floating eigensolver.  Freeze a
rational vector `v`, evaluate `v^*Mv` exactly with directed entries, and demand
a strict upper endpoint below zero.  Eigenvalue computations are discovery
only.

For a conditional-negative-type nomination, use the explicit `L-9502`
transfer moat to select a proof-safe Gaussian `lambda`; then optimize nearby
scales only for a larger margin.

## Candidate JSON schema

A scalar candidate should be serializable as

```json
{
  "schema": "riemann.screw.scalar.v1",
  "node": {"kind": "dyadic", "numerator": 0, "power": 0},
  "manifest": {"cutoff_q": 0, "digest": "..."},
  "normalization": "D-9501",
  "smooth_interval": ["...", "..."],
  "prime_interval": ["...", "..."],
  "psi_interval": ["...", "..."],
  "working_precision_bits": 0
}
```

A matrix candidate adds exact nodes, an exact vector, an optional exact
`lambda`, primitive `Psi` intervals keyed by exact node differences, and the
final directed Rayleigh interval.

All decimal interval endpoints in the transport format are outward-rounded
strings parsed by the checker as exact rationals; they are not native floats.

## Trusted checker boundary

The smallest checker should know only how to:

1. parse exact integers, rationals, and dyadics;
2. verify manifest identities and digests;
3. evaluate the elementary smooth series with a rational tail bound;
4. accumulate directed prime terms;
5. perform directed scalar, polynomial, and Rayleigh contractions;
6. evaluate a directed real exponential for the Gaussian route;
7. reject every non-strict sign or missing dependency.

Prime generation, candidate optimization, eigenvectors, plots, and performance
code remain outside the trusted boundary.

## Uncertainty closure

Every claimed moat is decomposed into

```text
exact logical gate
+ special-function enclosure
+ prime-manifest enclosure
+ scalar accumulation enclosure
+ parameter-freezing perturbation
+ final contraction rounding.
```

The final interval must survive the sum of all admitted errors.  Reproducing
the same output with the same code is provenance, not independence; the
second proof run should use a different prime enumeration and a different
special-function path.

## Relation to active repository work

This route is compatible with, but does not depend on:

- the complete prime-power manifests developed for piecewise Weil carriers;
- the general witness-survival and exact-Rayleigh machinery;
- Arb infrastructure used by `xi'/xi` feature tables.

It does not require high carrier phases, a recovered `K=1024` vector,
`xi'/xi`, division by a near-zero function value, or contour winding.

## Gap audit

- A finite positive scan is only a finite exclusion.
- Source equivalence and numerical evaluation are separate gates.
- A manifest can have the correct row count and still omit/duplicate terms.
- Recursive interval widths can grow without checkpointing.
- Search-selected parameters must be frozen before directed evaluation.
- Shared primitive uncertainty must remain shared throughout a determinant or
  matrix contraction.
- A negative interval from one implementation requires independent arithmetic
  reproduction before counterexample promotion.

## Immediate implementation order

1. land the binary64 reconnaissance script with an explicit non-proof label;
2. replace its full-memory sieve by a segmented streaming manifest;
3. add Arb smooth and prefix evaluators;
4. complete scalar cells through the largest existing manifest cutoff;
5. emit the lowest-margin exact nodes;
6. launch three-value and Gaussian searches only on that certified table.

## Analytic domain audit

The pipeline evaluates `Psi` only on the real line.  The smooth series is used
for positive arguments and the value at zero is supplied by continuity.
Every logarithm has a positive integer argument, every square root is the
positive real root, and every Gaussian exponential has a real argument.  The
source-normalization gate, rather than the numerical checker, is responsible
for the analytic continuation and RH-equivalence theorem.

## Dependency audit

- `D-9501` fixes all primitive functions and exact encodings.
- `L-9501` supplies the scalar, determinant, anchored-PSD, and
  conditional-negative-type implications.
- `L-9502` supplies Gaussian PSD and the explicit scale moat.
- `L-9503` supplies complete cell classification, convex lower bounds, smooth
  tails, and local recurrences.
- Existing repository survival machinery may be reused operationally, but no
  mathematical claim in this file depends on an unmerged branch.

## Remaining uncertainty

The main unresolved engineering question is whether interval width can be
kept small through a multi-billion-row stream without excessive precision or
checkpoint cost.  The main unresolved research question is whether the
scalar and finite distance-geometry margins become small enough at accessible
cutoffs to nominate a counterexample.  Neither question changes the finite
validity of a strict negative certificate.

## Suggested next attack

Build the segmented Arb scalar producer first and publish its smallest
certified cell margins.  Those margins should determine the exact node pool
for every later determinant or Gaussian search; a broad unguided matrix scan
would discard the principal computational advantage of the prime-knot
reduction.
