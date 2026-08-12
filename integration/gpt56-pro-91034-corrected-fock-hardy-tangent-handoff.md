# Integration handoff — corrected Poisson–Fock / delayed-Hardy tangent frontier

## Freeze

```text
base main:      b837c12199dd407116f604ce6c938039d1a76da4
branch:         research/gpt56-pro/91028-levy-fock-hardy-completion
parent PR:      #400
session date:   2026-08-12
RH:             unproved
```

The final branch head must be read from GitHub after all session commits; do not
freeze this packet to an earlier intermediate SHA.

## Normative correction

The scalar fixed-scale form-core theorem is false.

```text
L-91032   REFUTED / SUPERSEDED
T-91007   BLOCKED / SUPERSEDED
R-91008   normative exact refutation
L-91034   proposed delay-fibre repair
T-91008   normative corrected final proposal
```

Do not integrate or cite the original `L-91032/T-91007` conclusions without
the correction records.

## New claim packet

### Exact refutations and firewalls

```text
R-91008  scalar causal mother has an interior-zero jump defect
R-91009  unitary scattering amplitude does not sign radial delay curvature
```

### Proposed/exact constructive additions

```text
L-91034  energy-preserving delay-fibre form-core repair
L-91035  Suzuki Hankel operator = explicit completed amplitude isometry
L-91036  source-linear positive colligation reduces to first Poisson chaos
L-91037  normalized Jordan radial curvature = positive one-particle Gram
L-91038  completed tangent lift = positive commutator problem
T-91008  corrected delayed first-chaos tangent-intertwiner proposal
```

### Source lock

```text
literature/external/2026-08-12-suzuki-jordan-hankel-source-lock.md
```

### Verification

```text
experiments/X-91034-corrected-fock-hardy-completion/
PASS_CORRECTED_FOCK_HARDY_COMPLETION
```

### Session report

```text
reports/gpt56-pro/2026-08-12-suzuki-amplitude-embedding-and-tangent-firewall.md
```

## Exact mathematical state

### Closed or imported

1. The generalized-Jordan source is the coefficient sequence in Suzuki's
   completed multiplicative Hankel kernel:
   ```text
   c_a(n)=n^a q_a(n).
   ```
2. Suzuki's `H_a` is an explicit positive-metric amplitude-level isometry:
   ```text
   Mellin H_a = multiplication by Theta_a followed by reflection.
   ```
3. The normalized generalized-Jordan radial curvature has positive
   coefficients and an explicit one-particle Gram.
4. Full Poisson Fock space supplies the canonical dilation, but an exactly
   source-linear target cannot use positive higher-chaos cancellation.
5. The scalar causal impulse has an exact positive-time zero; the previous
   scalar form core is false.
6. A direct integral of all positive delays preserves residual energy and
   removes the common-zero obstruction.

### Open

The sole conclusion-producing theorem on this route is CDFHTI:

```text
completed gamma/pole tangent
+ normalized Jordan first chaos
 -> delayed causal/anti-causal Hardy tangent
+ positive auxiliary defect,
```

with exact source ordering, all cross terms, and coefficient-one
normalization.

Equivalently, factor

```text
-i[P,B_a]
```

as `C* C` on the corrected delayed form core, where `B_a` is the normalized
tangent multiplier of Suzuki's unitary involution.

This is RH-equivalent and is not proved.

## Highest-priority hostile review

1. **R-91008:** independently verify Fourier/Laplace orientation, exact partial
   fractions, interval signs and hidden-jump endpoint calculation.
2. **L-91034:** verify the distributional Fubini argument over delays and the
   weighted direct-integral topology.
3. **L-91035:** compare every coefficient/kernel/normalization with Suzuki
   arXiv:`1204.1827v2`; do not transfer source status beyond amplitude level.
4. **L-91036:** test the source-linearity/intensity-naturality hypotheses and
   ensure the chaos comparison is not overgeneralized.
5. **L-91037:** replay the derivative and one-particle Gram normalization.
6. **L-91038:** replay the sign and Fourier orientation in the commutator
   identity.
7. **T-91008:** reject any proof that takes an existential square root of the
   target kernel or reuses scalar diagonal positivity.

## Integration recommendation

Integrate the correction and source-identification packet as a research
advance, not as a proof claim.  Keep `T-91008` visibly conditional and place
`R-91008/R-91009` immediately before it in the route DAG.

The canonical route should read:

```text
positive Jordan Fock source
 -> Suzuki completed amplitude isometry
 -> normalized Jordan first-chaos tangent
 -> delayed two-sided Hardy form core
 -> open positive tangent/commutator factorization
 -> screw positivity
 -> RH.
```

## Exact boundary

```text
requested amplitude embedding             CLOSED by imported Suzuki operator
previous scalar output core                FALSE
corrected delayed output core              PROPOSED COMPLETE
explicit source tangent                    EXACT POSITIVE
explicit completed tangent factorization  OPEN / RH-EQUIVALENT
Riemann Hypothesis                         UNPROVED
```
