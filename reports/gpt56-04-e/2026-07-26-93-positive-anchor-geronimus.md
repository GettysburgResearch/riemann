# Agent report — positive-anchor direct-xi Geronimus extension

Agent: `gpt56-04-e`  
Issue: #93  
Branch: `agent/gpt56-04-e/93-positive-anchor-geronimus`  
Date: 2026-07-26

## Inspiration surveyed

This continuation read the newest direct-xi, carrier-Weil, and proof-production
work before selecting a target.

- PR #103 retained a rigorously positive but extraordinarily small atomized
  direct-xi minimum at an ordinate only `0.0161703125...` below the independent
  optimized carrier-Weil basin.
- PR #116 closed the entire degree-at-most-14 half-line-nonnegative polynomial
  response cone on that exact table with a robust moment-matrix certificate.
- PR #117 showed that adjoining the critical-line zero anchor raises the degree
  by one while introducing one scalar moment.
- O-9311 proposed, but did not prove, the analogous positive-node recurrence.

The positive-node extension was selected because it escapes the cone closed by
PR #116 while reusing all fifteen directed old moments and requiring only one
new completed-xi point.

## Mathematical results

### L-9314

Adding one exact positive node `w` gives the recurrence

```text
a_k = b_(k+1) + w b_k.
```

Hence all degree-15 moments depend on one scalar `b0`. In the adapted basis

```text
1, (y+w), (y+w)y, ..., (y+w)y^(m-1),
```

the two new Hankel matrices have fixed positive-definite inherited blocks and
opposite scalar Schur complements. The full degree-15 half-line cone is positive
if and only if

```text
theta0(w) <= b0 <= theta1(w).
```

Failure below or above yields the explicit responses `q0(y)^2` or
`y q1(y)^2`.

### L-9315

The new response-1 moment can be replayed as

```text
b0 = beta_w * (F(w)-F(u_ref)) + sum_k p_k a_k.
```

Thus one new point, one old reference, and the old moment table replace a direct
17-point barycentric contraction. The direct contraction can be retained as an
independent overlap check.

## Exact implementation

X-9312 adds standard-library exact arithmetic for:

- recurrence and adapted Schur matrices;
- exact rational linear solves and LDL pivots;
- explicit failed-gate directions;
- response-map inversion;
- one-new-point reduced replay coefficients;
- exact old-moment interval-width accounting;
- strict negative interval verification along both Schur witness directions.

Ten tests pass, including recurrence, adapted-block contractions, lower and upper
negative controls, zero-touch rejection, reduced/direct identity, zero-anchor
limit, exact PR #103 `w=4` regression, and malformed-anchor rejection.

## Empirical nomination

At PR #103's exact ordinate and `w=4` (`x=2`), the midpoint gate is

```text
[27375115.77715610683338270942781224884018...,
 27375115.77715610684289268397858616575745...].
```

A 70-digit ordinary direct-xi replay gave

```text
b0 = 27375115.77715610683624020837623539349038...
```

inside the gate, only about `2.8575e-12` above its lower boundary. The new-point
coefficient is about `-2.3291e-10`, so this corresponds to a primitive repair
moat near `0.01227`. The exact old moment-box width contributes below `7.071e-33`.

This is a cheap directed target, not a counterexample claim.

## Candidate counterexamples

None. No strict negative directed interval exists and no `Z-####` identifier was
allocated.

## Recommended exact run

1. Emit one completed-xi point at `x=2`, 512 and 640 bits.
2. Preserve the PR #103 ordinate, common scale, normalization, and atomized
   count profile.
3. Require nested primitive rectangles.
4. Replay `b0` both directly and through L-9315; require overlap.
5. Contract both L-9314 Schur witnesses.
6. Nominate only a strict negative upper endpoint.

After this control, scan rational-square anchors and rank them by
primitive-normalized repair moat rather than raw Schur distance.

## Uncertainty

- L-9314/L-9315 are proposed until independently reviewed.
- The `w=4` direct-xi value is an ordinary high-precision midpoint.
- The direct-xi/count-deflation theorem chain remains an inherited logical gate.
- A positive `w=4` result closes only that finite positive-anchor extension.
