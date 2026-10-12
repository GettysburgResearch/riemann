# Height mechanisms: a finite compact Pick hierarchy and its boundary

Status: proposed research mathematics, reviewed during the research wave;
not added to the integrated theorem catalogue.

Scope: safe **real horizontal** nodes of `E(z)=xi(1/2+z)`, at imaginary
evaluation height zero. The height H is the first possible off-line zero
height supplied by a complete finite-height verification. This is not the
arbitrary-height kernel `R_T` or an RH proof.

Exact sources/dependencies: the complete entire-source zero-orbit expansion
in the repository's current xi repair; classical xi/theta/Gamma/Jensen
interfaces; the published Platt--Trudgian height through the conservative
H=3*10^12; directed low Hardy-Z endpoint signs; and exact rational finite
matrix bounds. The imported high-zero computation was not rerun.

What was actually run: 48 low critical-pair existence certificates and
`xi(1/2)>1/4` regenerated with Arb at 128 bits from a 256-bit artifact;
exact anchor determinant, denominator-frame, and inverse-trace identities;
two exact quartet square decompositions; rational full-tail sufficient
inequalities; exact synthetic countermodels; and optimized Python replay.

Smallest remaining global gap: make the lower bound dominate the complete
negative kernel for unbounded node ranges and cofinally increasing order,
including mixed-scale packets. This packet does not supply that estimate.

## What the wave established at proposed scope

The finite-order compact theorem uses several independent low critical
pairs and a Newton frame that remains controlled as real nodes collide.
An exact quartet decomposition isolates two negative rank-one features.
Recompleting its odd block moves those features to degrees two and three,
improving the complete high-zero tail from `H^-3` to `H^-7`.

A separate scalar lemma proves alternating signs of p and its derivatives
through order `4.5*10^12-1` on every `t>=0` with the classical strip, or
through `6*10^12-1` with the imported 7/8 strip. This is a finite
complete-axis statement for individual derivatives; it does not imply
matrix positivity at the same order.

The following examples pass strict exact sufficient inequalities. They
hold with the classical strip width A=1/2; importing the quasi-RH bound
A=3/8 reduces the negative-error budget to at most 9/16 and improves margins.

| Maximum packet size | All nodes in | Mechanism |
| --- | --- | --- |
| 8 | `0<x<=500` | first negative-feature bound |
| 12 | `0<x<=200` | first negative-feature bound |
| 18 | `0<x<=100` | first negative-feature bound |
| 32 | `0<x<=40` | first negative-feature bound |
| 96 | `0<x<=1` | recompleted negative features; 48 directed anchors |

Distinct-node packets are positive definite; repeated evaluation nodes
give PSD by coefficient-summing congruence. These are full compact-domain
statements under the source/height hypotheses, not positive sampled tables.
The size-96 classical-strip certificate has a sufficient margin ratio
greater than 3,431,758. Its larger-node fail control is retained.

Read the proofs in dependency order:

1. [PROOF.md](PROOF.md): normalization, sharp finite derivative-sign
   threshold, signed-shadow estimate, first compact theorem, and a negative
   four-node single-reserve example.
2. [DENOMINATOR_FRAME.md](DENOMINATOR_FRAME.md): stronger finite-order
   compact theorem and its exact inverse bound.
3. [NEGATIVE_FEATURES.md](NEGATIVE_FEATURES.md): complete positive/negative
   quartet decomposition and the H^-5/H^-7 upgrades.
4. [COARSE_ZERO_COUNT.md](COARSE_ZERO_COUNT.md): elementary complete
   `N_+(T)<T log T` count for T>=1024 from theta positivity and Jensen,
   with the directed finite xi value as an explicit primitive.
5. [SIMPLE_COFINAL_COUNTERMODEL.md](SIMPLE_COFINAL_COUNTERMODEL.md): why an
   arbitrarily high, narrow, *simple* exceptional spectrum plus one fixed
   low reserve does not imply global four-node positivity.

## Reproduce

Use the environment's pinned Python tools, including python-flint 0.9.0:

```bash
source /workspace/.riemann-tools/activate.sh
python research/exploratory/2026-10-10-four-hour-wave/heights/verify.py
python -O research/exploratory/2026-10-10-four-hour-wave/heights/verify.py
```

`verify.py` regenerates the directed low-anchor primitives and checks all
finite inequalities with `fractions.Fraction`. It assumes the paper theorem
is the correct bridge from those inequalities to the full kernel; checking
the rational inequalities alone is not a proof of that bridge. Normal and
optimized receipts are [verification.json](verification.json) and
[verification_optimized.json](verification_optimized.json).

The extended endpoint producer uses an Arb zero finder only to place short
rational intervals. Strict opposite Hardy-Z signs at exact rational
endpoints and disjointness establish the existence actually used; no
ordinal completeness or simplicity claim is required. The artifact is
[extended_anchor_certificate.json](extended_anchor_certificate.json),
produced by [certify_extended_anchors.py](certify_extended_anchors.py).

## Relation to recent work

The 7/8 quasi-RH theorem corresponds to horizontal strip half-width 3/8.
It improves the explicit error constant and the sharp finite scalar
derivative-sign threshold. It does not by itself give all-order PSD.
These compact certificates already pass with the older half-width 1/2;
their new gain is the source-faithful Gram preconditioning and signed
quartet-square bookkeeping.

The newly inspected PR #910 source at
`670a76c1a3a8f325c43c1755b1cfc24d313a3e3c`,
`standalone/2026-10-10-quasi-riemann-height-descent/NATIVE_HEIGHT.md`, concerns
coherent height twisting, inverse/plain Dirichlet-polynomial moments and a
local off-diagonal zero detector. The present finite safe-axis kernel
theorem does not establish its missing arithmetic cancellation estimate.
