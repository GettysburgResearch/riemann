# T-108507 — The cube-defect bridge: the obstruction to cubing is the L-datum of the trace-doubled deformation

```text
Claim ID: T-108507
Status:   PROVED (Theorems 1-4 of the standalone proof; elementary complete
          proofs, machine-verified) + CONDITIONAL corollary labelled as
          such (imported Estermann/Kurokawa-type criterion, not reproved)
Created:  2026-08-31 (continuation pass)
Programme: #764, axes A/B, central question 9; sharpens T-108500 Theorem 2
          and O-108506 into one structural statement
Depends on: T-108500, O-108506; imported inputs cited in the proof
Proof:    standalone/2026-08-31-cube-defect-bridge/PROOF.md
Replay:   experiments/X-108507-cube-defect-bridge/  (EXACT_RATIONAL + one
          labelled floating quadrature)
RH status: RH and GRH are unproved; this claim does not address them.
```

## Statement (summary)

Let `A_2` be the TRACE-DOUBLED deformation of the degree-2 local object
`A` (Satake polynomial `1 - 2aT + bT^2`: trace doubled, determinant kept),
with inverse roots `gamma, delta`. Then:

1. **Bridge:** `N_3(T) = det(1 + b A_2 T) = (1 + b gamma T)(1 + b delta T)`
   — the m=3 defect IS the local L-datum of the trace-doubled deformation,
   det-rescaled and sign-twisted. (Machine check V1 reads the deformation's
   data `(2a, b)` off the Berlekamp-Massey-reconstructed defect at 24
   instantiations.)
2. **Splitting field:** the defect's splitting field
   `Q(a,b)(sqrt(a^2-b))` is exactly `A_2`'s Satake field — EXPLAINING the
   character-ring exit of T-108500 Theorem 2: the defect's roots are weight
   monomials of a different, non-functorially-related object.
3. **Stratification transfer:** the defect's purity stratification
   (O-108506) is `A_2`'s temperedness stratification: `A_2` violates the
   Ramanujan bound exactly on `{a_p^2 > p}` (Sato-Tate density
   `2/3 - sqrt(3)/(2 pi) = 0.391...` for non-CM data; ST imported as a
   labelled theorem).
4. **Global reduction (formal, good primes):**
   `sum' a_n^3 n^{-s} = L^{good}(Sym^3, s) x D(s)` with
   `D(s) = prod_p det(1 + p (A_2)_p p^{-s})` — verified exactly
   coefficient-by-coefficient on all good-support `n <= 300` for 11a1.
   Hence: the cube of a GL(2) L-function survives as an L-object iff the
   trace-doubled deformation does — an exact instance of issue #764's
   question 9.

**Conditional corollary (labelled, NOT claimed as theorem):** under the
applicability of the Estermann/Dahlquist/Kurokawa meromorphy criteria
(Estermann ~1928; Dahlquist ~1952; Kurokawa, Proc. LMS 1986 I-II) to this
non-uniform family — equidistributed per Sato-Tate, non-tempered on a
density-0.391 stratum — `D(s)` has a natural boundary and the cubed series
occupies stratum S3 of the survival trichotomy: cubing destroys L-ness
irreparably. Verifying the criterion's applicability is the named
follow-up target.

## Structural reading (the pass's sharpest new statement)

Three previously separate exact facts — defect self-duality, character-
ring exit, angle-stratified purity — are one fact seen three ways:
**deformations obstruct each other**: the failure of the cube point of the
deformation space to be functorial is measured by the local L-data of the
trace-doubling point. First data on the extension of this obstruction
duality (matrix/layer_probes.json): `N_5` is irreducible over `Q(a,b)`,
and under the symmetric self-dual-pair ansatz it splits into two
self-dual quadratics over `Q(a,b)(sqrt(16a^4 - 48a^2 b + 41b^2))` — so if
an m=5 bridge exists, its "deformation" is a CONJUGATE PAIR over a new
quadratic extension (versus m=3's single deformation over
`sqrt(a^2-b)`); the obstruction-duality tower appears to deepen with m.
Deposited as an exact observation + open question, not a claim.

**Pass-3 addendum (2026-08-31):** the open question above is now CLOSED
by T-108509 (deformation spectrum): for every m the defect is a
canonical product of `floor((m-1)/2)` self-dual rank-2 deformations of
determinant `b^m`, with spectrum polynomial `M_m` (`M_3 = z + 2ab`
recovers this bridge; `M_4 = z + b(3a^2-2b)` is the next one) and tower
invariants `D_m = disc_z M_m` (`D_5` derives the m=5 ansatz invariant).
Additionally, campaign C4 (matrix/c4_boundary_telescope.json) places
the CONJECTURAL accumulation line for the corollary's natural boundary
at `Re s = 3/2` (the zero constellation of `D(s)`: tempered primes
exactly on the line, untempered band `O(1/log p)`), with the honest
control that dense local zeros alone do not imply a boundary.

## Novelty position

The ingredients are elementary; the m=2 analogue (Rankin-Selberg) is
classical, and the coefficient identity `a_p^3 = lambda_{Sym^3} + 2p
lambda` at k=1 is classical. Believed new, subject to the pass-1 audit's
standing verdicts on this claim family (PARTIAL_OVERLAP on defect
extraction generally): the all-`k` factorization of the full defect as
the exact local system of a NAMED coefficient deformation, the
splitting-field and stratification identifications, and the resulting
equivalence "cube survives iff trace-doubling survives".
```
