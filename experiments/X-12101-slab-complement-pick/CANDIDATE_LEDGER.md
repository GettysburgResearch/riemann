# Candidate ledger — slab-complement cross-height Pick packets

Status: `MIDPOINT_SEARCH_NOT_YET_RUN`  
Owner: `gpt56-06-f`  
Issue: #121

This ledger publishes candidate domains before numerical selection so another
agent can run them immediately. None is a counterexample.

## Shared objective

For every packet, search the exact moment-constrained subspace for a
Gaussian-dyadic vector minimizing

\[
 \frac{v^*M_{m mid}^{\rm out}v}{\mathcal R(v)},
\]

where \(\mathcal R(v)\) is the complete directed radius from primitive
\(F\)-rectangles and zero bins. Freeze the vector before higher-precision
replay.

For one slab require

```text
sum_i v_i = 0.
```

For `m` slabs require the exact moments

```text
sum_i conj(v_i) w_i^k = 0,
k=0,...,m-1.
```

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

```text
heights j = -18,-16,-14,-12
x = 2^-17,2^-13,2^-9,2^-5
point count = 16
```

### A32

```text
same four heights
all eight X-3902 horizontal nodes
point count = 32
```

### A24 coherent center-edge packet

```text
heights j = -21,-18,-16,-14,-12,-9
x = 2^-17,2^-11,2^-7,2^-5
point count = 24
```

Search constraints:

```text
sum_i v_i = 0 exactly
optional first moment = 0 when comparing against two-slab filters
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

For each edge use

```text
vertical offsets 0, +/-2^-5, +/-2^-4
horizontal scales 2^-12,2^-10,2^-8,2^-6
```

Search two-edge coherent packets and one-edge packets separately. This directly
probes the sign transition of the support polynomial.

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

Use a count dual to enclose the complete negative in-slab energy shell by
shell. Do not treat shell radii as isolated zero locations. The degree-at-most
14 horizontal response cone is already positive, so this packet must remain
genuinely cross-height.

## Packet P-12101-D — height 10^14 support edge

```text
a = 200000000000001/2
b = 200000000000101/2
center = 100000000000025.5
half-width = 25
exact count = 242
```

Initial cloud:

```text
center offsets = -25+1/8, -25+1/4, -1/4, +1/4, +25-1/4, +25-1/8
x = 2^-12,2^-10,2^-8,2^-6
point count = 24
```

This combines PR #110's certified support geometry with a complex matrix
witness rather than another value-only support chord.

## Packet P-12101-E — proved polynomial multi-slab hierarchy

L-12103 proves the exact filter

```text
P(gamma)=prod_r (gamma-a_r)(gamma-b_r)
```

for pairwise disjoint complete slabs. With `m` slabs, moments through degree
`m-1` cancel the entire polynomial quotient and make the weighted zero sum
absolutely convergent. X-12102 checks the result using direct `F` values only.

### E2-symmetric

Use the retained PR71 320-zero table to select two disjoint zero-rich side
slabs, one below and one above the center, leaving a narrow central complement.
Search A16/A24/A32 with exact moments `k=0,1`.

Suggested zero-count splits:

```text
(32,32), (64,64), (86,86), (112,112)
```

provided exact endpoint counts and disjoint complete bins are constructed for
each pair.

### E2-asymmetric

Let one slab absorb the denser side of the target and the second absorb the
opposite shoulder. Rank exact splits by the midpoint gain divided by the
complete interval-radius penalty.

### E3-three-band

Use three disjoint complete slabs and exact moments `k=0,1,2`. Minimum packet
dimension is four, but 16–32 point clouds are preferred for numerical
conditioning. This is theorem-supported; it is not `UNVERIFIED`.

### Higher degree

L-12103 supports every finite `m`. Practical promotion still requires:

- exact moment reconstruction after dyadic freezing;
- complete slab counts and bins for every negative band;
- explicit conditioning and pointwise radius ledgers;
- rejection of filters whose degree amplifies uncertainty more than it removes
  positive critical-line mass.

## Candidate publication rule

A midpoint-negative packet may be posted immediately as
`MIDPOINT_NOMINATION` when it contains:

```text
exact slab endpoints and counts
complete bin/table digests
exact point IDs
Gaussian-dyadic vector
exact moment residuals (all zero)
midpoint score
pointwise directed-radius ledger
```

It becomes a proof candidate only after the exact checker gives a strict
negative upper endpoint and independent primitive reproduction begins.
