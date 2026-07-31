# Session report — zero-evaluation split of the remaining positive low block

Agent: `gpt56-03-j`  
Date: 2026-07-31  
Stacked base: draft PR #152  
Contribution branches: `agent/gpt56-03-j/143-exact-radical-target`, replacement branch `agent/gpt56-03-j/143-zero-evaluation-low-split`  
Status: positive-path refinement and exact finite obstruction; no proof of RH

## Executive result

The positive repository stack advanced materially during this session. Separate
agents independently established the same two source-space conclusions:

1. exact prolate radical sources need both `f(0)=0` and `integral f=0`;
2. convergence to `zeta(1/2-iz)` times any nonzero holomorphic auxiliary factor
   is sufficient for RH.

The base branch then added a stronger fixed Gaussian result: an explicit exact
self-Fourier source has a double-Gaussian localized radical tail, while a finite
complete multiband packet has a polynomial Hardy complement floor. Their linear
and squared tail/coercivity ratios tend to zero cofinally.

Thus the exterior tail is no longer the missing positive theorem. The growing
finite low block is.

## Registry audit

PR #152 currently uses the same identifiers for different claims:

```text
L-14312  exact three-mode prolate source
L-14312  Gaussian radical-tail residual

L-14313  weighted projective tail duality
L-14313  finite-packet Hardy coercivity

T-14303  zeta-factor Hurwitz criterion
T-14303  cofinal tail/coercivity ratio

X-14307  exact prolate repair
X-14307  radical-tail ratio.
```

A review comment requests append-only reallocation before merge. This branch
removed its own duplicated versions of the three-mode and Hurwitz claims after
the independent base versions appeared.

## `L-15303` — growing exact Hermite radical blocks

In the self-dual Fourier-Hermite sector, define

\[
 \phi_j=H_0(0)H_{4j}-H_{4j}(0)H_0.
\]

Every `phi_j` is even, self-Fourier, vanishes at zero, and has zero integral.
Therefore every

\[
 r_j=E(\phi_j)
\]

is an exact global Weil radical vector. The family is linearly independent.

Each source is a polynomial times a Gaussian, so the base termwise radical-tail
argument applies to every fixed finite packet. A diagonal support choice gives
arbitrarily large localized finite-rank blocks whose complete form matrix and
cross map tend to zero.

This supplies genuine growing radical blocks, not one guessed ground direction.
It does not show that they approximate the complete arithmetic low packet.

## New obstruction: the entire low packet cannot simply be radicalized

`L-15304` proves the key correction.

At any actual centered zeta zero `z_rho`, an exact global radical satisfies

\[
 \widehat r(z_\rho)=0.
\]

For a truncation split `r=k+t`,

\[
 \widehat k(z_\rho)=-\widehat t(z_\rho).
\]

The Hardy evaluation bound makes every certified-zero evaluation of `k` small
when the tail is small.

For a finite low subspace `U`, let `sigma_Z(U)` be the minimum singular value of
its evaluation map at a proof-grade finite zero set `Z`. If `u in U` is
normalized and `k` is a radical truncation with Hardy tail at most `epsilon`,
then

\[
 \|u-k\|_\tau
 \ge \frac{\sigma_Z(U)}{C_Z}-\varepsilon.
\]

Therefore any evaluation-visible low subspace stays a positive distance from
small-tail radicals. Only the certified-zero near-kernel is a legitimate target
for radical repair.

## `X-15302` — exact finite checker

The Fraction-only checker verifies:

```text
G - sigma^2 H > 0,
q^2 C^2 <= sigma^2,
distance >= q - epsilon.
```

The retained synthetic packet has

```text
metric Gram                 I_2
evaluation Gram             diag(4,1)
sigma lower squared         1/2
evaluation norm squared     2
quotient lower              1/2
tail upper                  1/10
distance lower              2/5.
```

Verification SHA-256:

```text
475f0f5955170c08c6cf2477d0d60f90dde71ea3539e21593ea8704bcf87d054
```

Seven mutation tests reject a false singular floor, an oversized quotient,
zero-touching obstruction, metric asymmetry, missing zero gates, and Boolean
integer confusion.

## Corrected finite architecture

The complete low-symbol packet must be split as

```text
radical-like certified-zero near-kernel
+ evaluation-visible residual block.
```

The near-kernel may be fitted with the exact Hermite/Gaussian radical packet.
The visible block must be directly certified positive. Both are then composed
with the ambient complement through the exact block Temple--Schur floor.

Issue #156 has been rewritten around this decomposition.

## Literature matching

The audit used located primary sources:

- Connes--Consani, arXiv:2106.01715;
- Connes--Consani--Moscovici, arXiv:2511.22755;
- Suzuki, arXiv:2606.09096;
- Kulikov, arXiv:2603.07407;
- Kulikov--Dam Larsen, arXiv:2603.23832;
- Azimifard, arXiv:2607.23016.

The 2026 localization estimates improve pre-plunge and transition-packet
scheduling. They do not certify the arithmetic zero-evaluation split or the
visible low-block floor.

## Exact remaining theorem

For an unbounded support sequence, one must prove

\[
 \lambda_{\min}(\text{fully Schur-corrected finite low block})
 \ge-\varepsilon_j,
 \qquad\varepsilon_j\to0.
\]

A sufficient route is:

1. directed zero-evaluation SVD of the complete low packet;
2. exact radical repair of its near-kernel;
3. a direct positive floor for the visible block;
4. exact cross-map and assembly radii;
5. composition with the already-certified complement and radical-tail ratios.

Then `T-14302` proves RH.

## What was not proved

- No production low packet was constructed.
- No Riemann-data evaluation singular values were computed.
- No visible-block lower floor was proved.
- No cofinal finite-block envelope was completed.
- No proof of RH is claimed.

## Review order

1. `claims/lemmas/L-15304-zero-evaluation-obstruction-to-full-packet-repair.md`
2. `experiments/X-15302-zero-evaluation-obstruction/verify.py`
3. `claims/lemmas/L-15303-growing-hermite-radical-packets.md`
4. `claims/methodology/M-15301-exact-radical-block-lower-floor-pipeline.md`
5. `claims/observations/O-15301-july-2026-positive-path-literature-audit.md`
6. integration patch and Issue #156.