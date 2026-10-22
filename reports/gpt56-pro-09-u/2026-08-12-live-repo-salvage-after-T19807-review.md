# Live-repository salvage after the T-19807 review

Agent: `gpt56-pro-09-u`  
Review cutoff: `2026-08-12T21:18:03Z`  
Scientific status: **review + PROPOSED salvage architecture; RH is not claimed proved**

## Frozen live state

| object | frozen head |
|---|---|
| `main` | `b837c12199dd407116f604ce6c938039d1a76da4` |
| PR #150 finite Hardy--prolate criterion | `feefc9fa68330a9821f730d634a7b9e4001cfba0` |
| PR #164 source-bound prolate wrapper | `a46b6bb9269b46caa205aebe50a7f19ccc9d86da` |
| PR #202 positive-path/audit ledger | `891d86023ed0ade06f9c46e317b3a18f85c0d5eb` |
| PR #219 independent prolate/prime-polygon review | `4a472026d140c3c2d8fdd80da12a36fdb4151d48` |
| PR #361 Anthropic Zeta23 import | `c13b8836f6c7f4e36f17ab1c4ebe41e4cf072f2e` |
| PR #373 Gaussian Fredholm--Pontryagin | `34fe2037ba33bc61fc1e6ce04c7e74ab7b13e794` |
| PR #392 first-Hermite linear-resolution rigidity | `d2387cd21eb891a8801fd122bc8d0ddd7c1c0fc4` |
| PR #398 safe-Jordan/Pick firewall | `043180519da90af2ea242a5055cbdad9ca40bc62` |
| PR #400 completed Jordan/Fisher first-chaos stack | `7dc9fec9eb5fab4ee9340ddbc5a52e36a6ab617e` |
| PR #401 Brownian--theta passive network | `82fe81e52d8c221c8649376d759aa8d0ee64c0c7` |
| PR #402 critical-renewal innerness boundary | `f5e8be06dfed171baca362316a24b1ce017ad235` |
| PR #403 triune adelic scattering / one-node reduction | `885716b9cf97c7c4deea3b4590b99e5faf13bc1f` |
| PR #404 prime/Fisher covariant completion | `ab71aa1fe0b1fd192011bbf40f032d2f42889ea0` |

## 1. Verdict on the review of `T-19807`

The independent review `R-19805-quarter-power-and-complete-d8-gap.md` is
**accurate and load-bearing**.

### False step A — support translation / large-sieve derivative

The old argument treated

```text
exp(-i s x_R),   x_R=(1/2)log(R/(2 pi)),
```

as a quarter-power amplitude cost.  In the polarized zero-side product the
translation factors cancel exactly.  More importantly, the parent large-sieve
lemma requires

```text
||A_gamma|| + T ||partial_R A_gamma|| <= B_T.
```

The disputed proof supplied only an unscaled derivative estimate.  If the real
oscillation remains in the amplitude, then

```text
R partial_R exp(-i gamma x_R)
 =-(i gamma/2) exp(-i gamma x_R),
```

which is of order `T` on the working band.  The claimed mean-square decay does
not follow.  A correct continuation must first extract every real WKB phase and
then prove scaled derivative control branch by branch, including Airy folds and
endpoint aliases.

### False step B — the complete `d8` complement gap

The full finite CCM space contains both Fourier-sign sectors.  Source vectors
built from modes `(0,4)` and `(2,6)` give two exact constraint-repaired low
profiles.  The Xi-like target can have residual scale `d4`, while an almost
orthogonal complement direction has residual scale `d6`.  Therefore a complete
complement lower bound at scale `d8` is false.  Any signed prolate hierarchy
must expose the `d6` sector or quotient it explicitly.

### Stronger later obstruction

Even after repairing both analytic errors, the historical ground-state
conclusion cannot be recovered by better constants.  `R-19846` constructs, in a
false-RH world, an even off-line Xi-cardinal vector with fixed negative Weil
value.  Its finite Hardy projections retain a negative Rayleigh moat, whereas
the Xi target tends to a global radical with value zero.  Thus any one-sided
cofinal theorem making the Xi line the complete finite ground line already
excludes every off-line zero; it is RH-bearing rather than a routine producer
estimate.

## 2. What survives from the old prolate proposal

The following pieces remain valuable and, at their stated conditional scope,
are not invalidated by the review.

1. `T-14301`: finite simple-even real-zero approximants converging to Xi in a
   moving Hardy strip imply RH by Hurwitz.
2. `L-14302/L-14303`: exact weighted residual, sector-gap, reciprocal-Hardy and
   rational Schur certificates.
3. PR #164: substantial finite source-bound profile and alias infrastructure;
   useful as finite producer/reconnaissance, not an emitted infinite proof.
4. `L-19867`: an exact simple even Xi-like line in the positive exterior-residual
   pencil with a constant complement gap and exponentially small residual.
5. `L-19868`: the complete moving-Hardy target rate, including periodization,
   aliases, endpoint channels and directed-enclosure scheduling.
6. `L-19873`: a source-bound derivative-intertwining estimate controls the total
   vertical defect of finite zeros.

Two attempted conclusion bridges are closed negatively:

- a generic non-ground CCM eigenline need not have a real-zero transform;
- free positive symmetrizer optimization is spectrally tautological, and the
  isotropic complement retains a parity-area defect.

Thus prolate/CCM remains an excellent **finite validation and approximation
engine**, but no longer supplies the primary conclusion mechanism.

## 3. Repository-wide route sweep

### Unconditional headline

PR #361 imports the strongest established unconditional advance in the live
repository: the Zeta23 proportion theorem, including the optimized on-line,
simple-on-line and distinct-zero proportions.  It is a genuine theorem but not
a route from `2/3` or `5/6` to all zeros without new mixed moments or support.

### Exact global criteria, not closures

- PR #373 gives a Gaussian trace-class Weil operator whose negative index is
  proposed to equal the number of off-line reflected pairs.  Fredholm,
  exterior-power and moment-Hankel criteria are exact global reformulations;
  all-order prime-side positivity remains RH-equivalent.
- PR #392 pushes first-Hermite positivity to linear heat resolution outside a
  set of arbitrarily small logarithmic density and proves a many-prime inverse
  theorem.  One prescribed resonant carrier remains, which is exactly the
  pointwise RH obstruction.
- PR #219's difference-Selberg repair preserves a positive quadratic channel,
  but the conditional-Hankel / balanced Type-II closure remains open.

### Prolate/CCM route

The finite convergence engine survives, but global ground selection is blocked
by the off-line-cardinal theorem and the generic non-ground real-zero theorem is
false.  The remaining source-specific anisotropic commutator theorem is a valid
conclusion-bearing target, but no source construction currently proves it.

### Suzuki/Jordan/Fisher/Hardy route

This is the strongest constructive architecture in the current graph.

- PR #400 imports Suzuki's exact completed amplitude embedding, proves the
  positive generalized-Jordan first-chaos curvature and identifies the
  canonical model-space tangent reserve `J_a^*J_a`.
- PR #404 gives the ordinary-prime tail-Hankel Julia dilation, the gamma/pole
  covariant connection, the completed Fisher/model-space factorization and the
  exact compressed-delay semigroup preserving every mixed-delay cross term.
- PR #401 gives a positive theta supersymmetric bulk and a coupled Brownian
  sum/difference reservoir, but leaves the exact Xi boundary response open.
- PR #398 supplies the necessary firewall: safe-side complete monotonicity,
  boundary unitarity and cocycle identities do not imply target Pick
  positivity.  Any proof must couple arithmetic and archimedean channels in one
  source map.
- PR #402 proves that the tempting factor-four renewal estimate in the hard
  range is exactly innerness, so it cannot be treated as a soft tail bound.
- PR #403 reduces the complete crossed-zero content to one fixed interior node.

## 4. PROPOSED full salvage — source-ordered one-node exhaustion

Everything in this section is **PROPOSED pending independent review**.

The best full proposal is to abandon complete ground selection and construct one
common conservative source map at each safe offset `a>0`.

### Source space

Use the direct sum of:

```text
ordinary-prime generalized-Jordan/Poisson first chaos;
explicit gamma and pole tangent channels;
full theta/Brownian coupled (S,Delta) reserve;
p=2 zero-safe boundary port;
both Hardy orientations and the bridge;
compressed-delay leakage environment.
```

Every component except the common renormalization map already has an explicit
positive metric or exact isometric dilation on PRs #400--#404.

### Output space

Use Suzuki's completed inner/model-space geometry:

```text
completed Fisher-Hankel source;
critical and stable Krein--Langer Cauchy kernels;
model-space tangent leakage J_a;
hyperbolic crossed-zero port.
```

### Required map

Construct an explicit source-ordered conservative map

```text
W_a:
  completed arithmetic source
   -> completed Fisher/model-space source
      + positive environment
```

with all normalizations equal to one, preserving:

```text
prime carriers;
gamma/pole connection;
compressed delays and their cross terms;
both Hardy orientations;
bridge channels;
radial/source generator.
```

At one fixed interior node, say `eta=1`, let `Phi_(a,1)` be the explicit
arithmetic source vector.  The minimal conclusion-producing theorem is

```text
ONAE_a:
||Phi_(a,1)||_src^2
 =||k_(a,1)^critical||^2
  +||k_(a,1)^stable||^2.
```

The Krein--Langer ledger decomposes the same source norm as

```text
critical + stable + hyperbolic.
```

Therefore `ONAE_a` forces the hyperbolic port to vanish.  A nonconstant Blaschke
factor is strictly contractive at every interior node, so vanishing at one node
removes every zero in

```text
Re(s)>1/2+a.
```

Proving `ONAE_(a_j)` for one explicit sequence `a_j->0` proves RH by functional
equation symmetry.

## 5. New cross-stack connection: the same `W_a` repairs the prolate route

The renormalized source map should also be required to intertwine the radial
source generator `A` with the finite/model-space generator `Lambda_a`:

```text
A W_a-W_a Lambda_a
 =|g_a><eta_a|+R_a.
```

If the relative Hilbert--Schmidt error tends to zero on a finite Galerkin
sequence, `L-19873` gives

```text
total vertical finite-zero defect ->0.
```

Together with the already proved moving-Hardy rate `L-19868`, this supplies an
independent finite-approximation validation of the same source map.

Thus the two strongest positive routes are not competitors:

```text
one-node norm exhaustion
    -> zero-free half-plane directly;

derivative intertwining + prolate Galerkin
    -> finite zeros approach the real axis + Xi convergence.
```

Both should be consequences of one source-ordered `W_a`.  This is the most
important connection exposed by the current sweep.

## 6. Exact missing theorem packet

A complete proof proposal now has four concrete obligations.

1. **Common source construction.**  Define one Hilbert source space containing
   the prime Poisson, gamma/pole, theta/Brownian, bridge and compressed-delay
   channels with source-bound normalization.
2. **Renormalized intertwiner.**  Construct `W_a` explicitly and prove the full
   Pythagorean/source norm identity, not only amplitude unitarity.
3. **One-node exhaustion.**  Prove `ONAE_a` at `eta=1`, including the bridge
   arithmetic norm and showing no hidden positive environment remains.
4. **Generator covariance.**  Prove the relative source-intertwining estimate
   needed by `L-19873`; this gives a finite CCM/prolate audit of the same map and
   protects against normalization errors.

No current PR proves obligations 1--3.  Obligation 4 is formulated but open.

## 7. Why this is preferable to the alternatives

- It does not assume the Xi-like vector is the global Weil ground state.
- It does not require a generic non-ground CCM real-zero theorem, which is false.
- It does not require pointwise prime-phase exclusion at one exceptional carrier.
- It does not optimize a metric after seeing finite roots.
- It is falsified at a precise location by the planted controls of PR #398.
- It retains every cross-channel term that the positive-source firewalls show
  cannot be discarded.
- It has a fixed-node scalar completion test, while also supporting a full
  finite-Galerkin audit through the repaired prolate machinery.

# SERIOUS RESOLUTION PATH

**YES — the live repository contains a serious full proposal, but no proof of
RH.**

The recommended spine is:

```text
explicit Suzuki completed amplitude
+ ordinary-prime Julia first chaos
+ gamma/pole covariant connection
+ theta/Brownian positive reserve
+ compressed-delay two-sided Hardy colligation
-> construct source-ordered renormalized W_a
-> prove one-node arithmetic exhaustion at eta=1
-> crossed-zero/hyperbolic port vanishes
-> Re(s)>1/2+a is zero-free
-> repeat for a_j->0
-> RH.
```

The repaired prolate/CCM work should be retained as a cofinal Galerkin and
moving-Hardy validation layer for this source map, not as a complete-ground
proof.

The decisive next task is therefore not another support-average or scalar sign:
it is an explicit coefficient-one formula for `W_a` and a proof of its one-node
source norm identity.
