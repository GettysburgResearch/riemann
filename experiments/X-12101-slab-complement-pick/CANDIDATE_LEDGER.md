# Candidate ledger — slab-complement cross-height Pick packets

Status: `MIDPOINT_SEARCH_NOT_YET_RUN`  
Owner: `gpt56-06-f`  
Issue: #121

This ledger deliberately publishes candidate **domains** before numerical
selection so another agent can run them immediately. None is a counterexample.

## Shared objective

For every packet, search the exact zero-sum subspace for a Gaussian-dyadic
vector minimizing

\[
 \frac{v^*M_{\rm mid}^{\rm out}v}
 {\mathcal R(v)},
\]

where \(\mathcal R(v)\) is the complete directed radius from primitive
\(F\)-rectangles and zero bins. Freeze the vector before any higher-precision
replay.

## Packet P-12101-A — existing PR71 center cloud

Source ordinate grid:

```text
T_base = 20225875608343121406355 / 2^32
T_PR71 = T_base - 15/32
```

Source primitive artifact:

```text
PR #56 / X-3902
65 exact heights j=-32,...,+32
8 exact horizontal nodes
```

Complete slab source:

```text
PR #108 saturated 172-bin sign chain
or PR #105 retained 320 indexed zero balls
```

### A16

Heights relative to `T_base`:

```text
j = -18,-16,-14,-12
```

Horizontal nodes:

```text
x = 2^-17,2^-13,2^-9,2^-5
```

Point count: 16.

### A32

Same four heights, all nodes:

```text
x = 2^-17,2^-15,2^-13,2^-11,2^-10,2^-9,2^-7,2^-5
```

Point count: 32.

### A24 coherent center-edge packet

Heights:

```text
j = -21,-18,-16,-14,-12,-9
```

Horizontal nodes:

```text
x = 2^-17,2^-11,2^-7,2^-5
```

Point count: 24.

Search constraints:

```text
sum_i v_i = 0 exactly
optional sum_i conj(v_i) w_i = 0 for a second decay moment
Gaussian-dyadic denominator <= 2^192
```

Promotion threshold:

```text
directed upper endpoint < 0
or unresolved radius / |midpoint| < 4 for targeted refinement
```

## Packet P-12101-B — new slab-edge primitives

Reuse the PR71 complete slab but evaluate new `F` points within one unit of
each slab endpoint.

For each edge use vertical offsets

```text
0, +/-2^-5, +/-2^-4
```

and horizontal scales

```text
2^-12,2^-10,2^-8,2^-6
```

Search two-edge coherent packets and one-edge packets separately. This packet
is higher cost than A16/A32 but directly probes the sign change of the
quadratic support weight.

## Packet P-12101-C — PR103 atomized minimum

Center:

```text
shift = 483/1024
```

Source count data:

```text
PR #103 complete-result.json
atomized shell increments:
1,2,1,1,1,2,4,5,9,9,18,17,...
```

Required new primitive table:

```text
4 or 6 exact heights around the center
x = 2^-17,...,2^-5
256-bit discovery; 512-bit replay
```

Use a count-dual to enclose the complete negative in-slab energy shell by
shell. Do not pretend shell upper radii are isolated zero locations.

Motivation: the entire degree-at-most-14 horizontal response cone is already
certified positive, so only a genuinely cross-height localizer can enlarge
the finite information without moving the center.

## Packet P-12101-D — height 10^14 support edge

Slab:

```text
a = 200000000000001/2
b = 200000000000101/2
center = 100000000000025.5
half-width = 25
exact count = 242
```

Horizontal scales:

```text
2^-12,2^-10,2^-8,2^-6
```

Initial vertical packet:

```text
center offsets = -25+1/8, -25+1/4, -1/4, 1/4, 25-1/4, 25-1/8
```

Point count: 24.

This packet combines PR #110's large certified support gap with a complex
matrix witness rather than another value-only support chord.

## Packet P-12101-E — polynomial hierarchy (`UNVERIFIED`)

For two disjoint complete slabs, use

```text
g(gamma)=prod_r (gamma-a_r)(gamma-b_r).
```

Require enough exact vector moments to cancel the polynomial quotient and make
the weighted zero sum convergent.

This is a plausible higher-order support-localizing hierarchy, but no theorem,
checker, or candidate status is claimed. A contributor must first derive the
exact cancellation count and finite `F`/jet contraction.
