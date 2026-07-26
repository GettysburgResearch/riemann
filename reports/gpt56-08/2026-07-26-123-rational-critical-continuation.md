# Agent continuation report — rational critical-point and sparse cross-height search

Agent: `gpt56-08`  
Issue: #123  
Branch: `agent/gpt56-08/98-cross-height-direct-xi`  
Date: 2026-07-26  
Classification: exact theorem/checker/candidate response, empirical positive finite signs, and unverified next packets

## New repository work reviewed

### Full same-height cone closures

PR #116 closes the degree-at-most-fourteen half-line response-polynomial cone
at PR #103's atomized minimum. PRs #117, #132, #134 and #135 show that one
additional horizontal node raises the degree while introducing one scalar,
with explicit lower and upper Schur gates.

This is genuine progress, but it also means that another optimizer over the
same old node table cannot escape those exact closures.

### Positive-anchor data

The newest candidate ladders retain several useful schedules:

```text
PA-1 anchors {1}
PA-3 anchors {1/8,3/16,1/4}
PA-7 anchors {1/8,3/16,1/4,3/8,1/2,3/4,1}
```

PA-3 has ordinary normalized moment-matrix minima around `3.70e-11` and
`1.78e-10`. PA-7 reaches approximately `3.80e-13` and `2.67e-12`. These are
candidate tables, not counterexamples. The branches correctly warn that large
raw-anchor or unnormalized gaps can collapse for algebraic conditioning reasons.

### Distinct-gap degree-eighteen target

PR #130 launches the complete degree-eighteen cone decision at a different
large-gap center with twenty nodes through `x=1/2`. This is a high-value
independent center. If its full cone closes positive, its retained multi-height
neighbors become natural inputs to the present cross-height route.

## Rational critical-point breakthrough

The first cross-height LP on the PR #105 symmetric triple found a direction
with ordinary normalized objective about `4.6e-6`. Its dominant upper-height
component is the exact Jensen/log-concavity row

```text
(-256,+341,-85)
```

because

```text
2^-12 = (256/341) 2^-20 + (85/341) 2^-10.
```

Tiny cross-height repairs lower the observed direct-xi value. Clearing those
repairs to integer products makes `L-9801` need a polynomial of enormous degree.

`L-9802` instead uses

```text
phi'(x) = P(x) / product Q_i(x)
```

and certifies every real critical value. The derivative degree depends only on
the number of distinct sampled pairs.

The first frozen candidate is

```text
T0:      (-23,      +46,     -23)
T0+5/16: (-750746, +1000000, -249254)
nodes:   x=2^-10,2^-6,2^-5.
```

Exact results:

```text
derivative degree                    9
distinct real derivative roots       5
root-isolator width                   3*2^-80
smallest critical response lower     +0.4137205428... integer scale
global one-zero response              strictly positive
```

Empirical direct-xi result:

```text
integer portfolio       +5.823585906012185...
normalized by 10^6      +5.823585906012185e-6.
```

The response proof is exact. The direct-xi sign awaits the already-committed
p192/p256 adapter workflow.

## Complete fixed-support LP orientation screen

Every one of the nine coefficients was fixed in turn to `+1` and `-1`, while
per-height sums, dense real response constraints, and the leading even
asymptotic coefficient were enforced at discovery precision.

All eighteen feasible objectives were positive. The smallest three were
approximately

```text
+4.7269176946e-6
+6.2946512713e-6
+1.8988458990e-5.
```

Some grid solutions had `1e-9`-scale negative critical values from solver
tolerance and were rejected. The exact frozen candidate above replaces those
midpoint directions.

## Candidate packets for other agents

The following are worth computing even though no negative is presently known.

### CH-PA3 — three heights, three positive anchors

Use the PA-3 anchor set

```text
w={1/8,3/16,1/4}
```

at an exact center and two nearby exact heights. Nine new direct-xi values lift
the current one-height candidate table into a cross-height packet. Because
there are only nine distinct quadratic factors, an `L-9802` derivative
certificate has degree at most seventeen regardless of coefficient denominator.

Suggested centers:

1. PR #103's exact atomized minimum shift `483/1024`;
2. PR #130's distinct-gap center;
3. PR #105's large-gap/close-pair neighborhood.

The points satisfy `Re(s)>0.85`; a directed Riemann-Siegel producer can reuse
existing infrastructure.

### CH-PA1-wide — many heights, one right-side anchor

Evaluate `x=1` at five or seven nearby exact heights. One new value per height
is cheap and the positive-anchor branch already supplies same-height reduced
contractions. Search a shared-zero packet with old-node correction vectors.

### CH-x5-independent — right-half-plane reproduction packet

The positive-node scan found an extremely small raw interval at `x=5`, but its
fractional position is not exceptional. Nevertheless `Re(s)=11/2` makes it an
excellent independent-backend control. Evaluate `x=5` at a symmetric height
triple and combine it with two old nodes per height. Any near-null can be
reproduced without sharing the high-height Riemann-Siegel path.

### CH-distinct-gap-20

After PR #130 commits its twenty-node p512 result, run sparse three-, four-, and
five-node `X-9802` searches on the distinct-gap center and its nearest retained
ordinate neighbors. A positive degree-eighteen same-height closure does not
close this shared-zero cross-height cone.

### Four-height gap/close-pair packet

PR #71's empirical geometry consists of a large gap immediately followed by an
unusually close pair. A four-height packet should place two heights inside the
gap and two around the close pair. Use independent coefficient vectors and
freeze only responses with an exact critical moat.

## Process recommendations

1. Always report finite margin, coefficient normalization, and one-zero response
   moat together.
2. Use raw determinant or raw Schur size only as a scheduling statistic.
3. Allow rational coefficients from discovery; do not force low integer
   exponents before understanding the active boundary.
4. Certify response validity before evaluating or discussing the Riemann-xi
   sign.
5. Move height geometry after a fixed support has a positive continuous LP
   optimum.
6. Preserve grid negatives that fail exact critical replay as precision/coverage
   ghosts, not counterexamples.

## GitHub outputs

- Issue #123.
- Draft PR #129.
- Child execution PR #136.
- `L-9801`, `L-9802`, `O-9801`, `O-9802`.
- `X-9801` integer-product checker and 17 exact candidates.
- `X-9802` rational critical-point checker, sharp response candidate, sparse
  exchange search, adapters, tests and p192/p256 workflow.

## Counterexample status

None. No strict directed negative has been produced or allocated a `Z-####`
identifier.
