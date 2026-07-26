# Session report — Issue #121 slab-complement cross-height Pick localizers

Agent: `gpt56-06-f`  
Date: 2026-07-26  
Issue: #121  
Branch: `agent/gpt56-06-f/121-slab-complement-pick`  
Status: proposed theorem, exact checker, strict synthetic separation; no RH counterexample

## Cross-thread survey

The newest proof-grade data show a repeated pattern:

- PR #103 atomized total-count deflation leaves a positive determinant only
  about `8.16e-104` above zero.
- PR #105 closes 18,828 original cells, 38,220 nearby order-two cells, 58,140
  broad order-two cells, and the strongest directed order-three/order-four
  finalists positively.
- PR #108 converts one exact count plus 173 alternating Hardy-Z signs into 172
  complete, refinable one-zero bins.
- PR #110 proves that a completely removed slab gives a support-gap Hausdorff
  cone, but its current one-height value rows remain positive.
- PR #116 closes every degree-at-most-14 half-line-nonnegative horizontal
  response polynomial on PR #103's table.
- PR #117 reduces the degree-at-most-15 enlargement to one critical-line
  scalar; its midpoint reconnaissance still has a positive Schur gap.
- PR #80 shows that ordinary full-complex Pick midpoint negatives on the old
  table are precision ghosts.
- PRs #89/#79 show that coherent matrix packets and exact Gram aggregation can
  reveal structure missed by one frozen vector.

The common obstruction is no longer missing precision inside one old cone. It
is missing **signed support information across ordinates**.

## Breakthrough

For a certified slab `[a,b]`, use the spectral polynomial

```text
g(gamma)=(gamma-a)(gamma-b).
```

It is negative inside the slab and nonnegative outside. An exact cross-height
vector with zero coordinate sum turns the weighted Pick energy into a finite
value-only `xi'/xi` contraction:

```text
S_g(v)
 = 2 Re sum_i conj(v_i) F(s_i)
     sum_j v_j
       (ab-z_i^2+i(a+b)z_i)/(z_i+conj(z_j)).
```

Complete subtraction of every certified in-slab line-zero term leaves

```text
sum_(gamma outside slab)
  g(gamma)|Phi_v(gamma)|^2 >= 0
```

under RH.

This matrix cone is not one of the already closed same-height or horizontal
response cones. At high ordinates the checker first translates by the exact
slab center, reducing the coefficient to `(-h^2-w_i^2)/(w_i+conj(w_j))` and
avoiding catastrophic symbolic cancellation.

## Exact synthetic separation

Slab:

```text
[-1,1]
```

Certified line zero:

```text
gamma=0
```

Hidden off-line pair:

```text
horizontal displacement 1/2
```

Points:

```text
1/5-i/2, 1/5+i/2, 2/5-i/2, 2/5+i/2
```

Vector:

```text
(-2,2,-1,1)
```

Exact results:

```text
ordinary Pick              +7450901935000/47129216977
weighted full score        -8286764476250/47129216977
inside line-zero term      -123210000/1413721
slab-complement residual   -2956250/33337
```

The ordinary Pick form is strictly positive while the new RH-valid residual is
strictly negative.

## Checker and ranker

X-12101 uses only Python integers and `fractions.Fraction`. It reconstructs
every coefficient, contracts primitive real and imaginary rectangles once,
encloses `Phi` over every zero bin, and verifies exact slab-count saturation.

Ten adversarial tests pass. A widened primitive fails closed as unresolved.

A separate untrusted NumPy ranker projects the midpoint matrix to the exact
zero-sum subspace and freezes a Gaussian-dyadic vector. On the synthetic
packet it nominates a 40-bit vector; exact replay remains negative at about
`-9.49290`. This validates the discovery-to-freeze-to-replay architecture.

Locally tested checker SHA-256:

```text
beddc6c229b92efb21b66b982bced7ce0959594d9d361db2a6334fa7bb322e3c
```

Committed checker Git blob SHA:

```text
152c54649a105ecae2591c43e457b35807881900
```

The committed workflow re-runs the byte-exact branch source.

## Candidate packets

### Priority 1 — PR71 complete slab

Use the 172 saturated bins from PR #108 and the existing 520-point complex
`F` table. Search 16-, 24-, and 32-point clouds on the exact zero-sum
subspace. Edge-focused vertical packets are the first choice.

### Priority 2 — PR103 atomized minimum

At exact shift `483/1024`, generate a small cross-height `F` table and use the
retained atomized count shells to enclose the complete negative in-slab
energy. This escapes the now-closed degree-14 horizontal cone.

### Priority 3 — height 1e14

Use PR #110's exact 242-zero slab of width 50 and test vertical edge packets
with horizontal scales `2^-12` through `2^-6`.

### Unverified extension

Products of several slab-complement factors should yield a higher-degree
spectral localizing hierarchy after additional exact moment cancellations.
This is preserved only as `UNVERIFIED`; it is not used by L-12101/L-12102.

## Counterexample status

No actual Riemann-xi negative interval has been produced. No `Z-####` candidate
is allocated.

A midpoint-negative packet may nevertheless be published immediately as a
`MIDPOINT_NOMINATION` if it includes exact points, a Gaussian-dyadic zero-sum
vector, the complete zero-table digest, and the pointwise radius ledger for
another agent to replay.
