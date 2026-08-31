# Independent audit: archimedean ladder boundary

Audited source: `86f41e9dce082677508eb79e37f3a3bf417027aa`.

Status: **mathematics survives within its stated local scope; bounded replay
and provenance repairs required and implemented with this report**. This is
not canonical integration, a new arithmetic realization, or an RH/GRH claim.

The audit used a fresh isolated worktree from the exact source, independently
rederived the identities, checked the primary analytic references, and ran
normal/optimized replay. Neither main programme worktree was edited.

## Findings at the audited source, ranked by severity

1. **P1: fresh-checkout replay failure.**
   `archimedean_ladder_boundary.py:188` hashed raw manifest bytes. The source
   fixture was generated with LF while the fresh Windows checkout had CRLF.
   Both producer modes failed, and the frozen-fixture test failed among the
   original 15 tests. The mathematical data were unchanged. Repair: hash
   canonical typed JSON for the manifest; use LF-normalized artifact hashes.
   Explicit LF, CRLF, and compact-JSON manifest tests now agree.

2. **P2: incomplete source and fixture type contracts.**
   At lines 178--180 only four manifest fields were checked, leaving the
   declared schema, analytic references, and scope outside that validation.
   At line 260 ordinary Python dictionary equality allowed, for example,
   Boolean `true` to replace integer multiplicity `1` in a fixture. Repair:
   compare the complete source contract and rebuilt fixture using typed
   canonical JSON; read the frozen Git blob and check its LF SHA-256 as well
   as its Git ID; bind note, producer, tests, and manifest to the fixture.
   Hostile source, reference, Boolean/integer, and blob-content tests reject
   the altered inputs.

3. **P2: public replay helpers were not resource bounded.**
   The unguarded `range(k)` at line 52 scaled with the supplied shift; even a
   zero-multiplicity term with an enormous shift could request an enormous
   loop. No such hanging input was run. Repair: explicit tuple/term checks,
   exact-input bit limits, recurrence-step/multiplicity/total-work limits,
   and basis-degree bounds. These are computation caps, not restrictions on
   the finite-list or complex-shift mathematical theorems.

4. **P3: algebraic category and localization wording.**
   The repaired note explicitly restricts scalar morphisms to endomorphisms
   of a type, with zero morphisms between distinct types; it identifies the
   differential-ring Leibniz rule and distinguishes algebraic balanced
   tensoring from completed Hilbert tensoring. The localized positive-time
   diagonal exponential is unbounded under the same monomial norm, not just
   non-trace-class. These clarify scope; they do not reverse a theorem.

## Independent mathematical verdict

- **Complex gamma-divisor theorem:** correct for finite products with
  integer multiplicities and unit-slope shifts `s+mu_j`. Within each
  `C/(2Z)` coset, sufficiently far-tail divisor orders equal the negative
  total multiplicity. Distinct cosets have disjoint pole progressions.
  Vanishing totals reduce by gamma recurrence to a rational function;
  nonvanishing totals force an infinite zero or pole divisor, also excluding
  rational times entire nowhere-zero. Negative multiplicities, zero
  multiplicities, repeated shifts, and the empty product are consistent.
  An important complex control is `Gamma_R(s+i)/Gamma_R(s-i)`: its total
  multiplicity vanishes, but the two imaginary offsets define different
  cosets, so it is not rational. Real-part parity alone is insufficient.

- **Effective versus virtual finite rank:** correct as stated. The
  obstruction applies to effective products with a positive multiplicity
  and fixed finite affine
  determinant pencils, not arbitrary matrix entries, nonlinear spectral
  substitution, or regularization. Balanced virtual quotients are genuine
  rational exceptions. Backward shifts produce poles, and canceled poles
  must be interpreted meromorphically rather than as an unevaluated `0/0`.

- **Hurwitz normalization:** correct. Writing `z=s+mu`, direct substitution
  gives `-Z'(0)=(z/2)log(pi)+(1/2)log(2)-log Gamma(z/2)`, hence
  `det_zeta=sqrt(2)/Gamma_R(z)`. For spacing one the same calculation gives
  `z log(2pi)-log Gamma(z)`, hence `2/Gamma_C(z)`. The normalization constants
  therefore agree under the direct-sum split. The real-positive Hurwitz
  values and their continuation are correctly identified as classical
  analytic inputs, not outputs of rational replay. See
  [DLMF 25.11.13 and 25.11.18](https://dlmf.nist.gov/25.11).

- **Tensor and carry maps:** correct over the specified differential ring.
  Ordinary complex tensoring retains the `k+1` pairs of nonnegative degrees
  adding to `k`; balanced `A` tensoring identifies polynomial coefficients
  and has rank one over `A`. The induced connection obeys the balancing
  relation. The exponent `epsilon*eta` gives precisely the parity carry;
  all associativity defects vanish by its two-cocycle identity. This is a
  lax monoidal assignment relative to the chosen polynomial coordinate,
  not a strong or arithmetic realization.

- **Dual direction and localization:** correct. The character-dual ladder
  is `F_{-mu+2epsilon}` and maps by `u^epsilon` into the connection dual
  `F_{-mu}`. For odd parity evaluation has image `(u)` and cokernel
  `A/(u)`; it is not perfect. Localization makes `u` invertible but introduces
  arbitrarily negative monomial degrees. At `mu=0`, `t=log(2)/2`, their
  exponential weights are exactly `2^{-n}`, unbounded as `n -> -infinity`.
  The one-sided heat/zeta prescription is not preserved.

- **Literature and proof boundary:** the gamma divisor, recurrence, and
  duplication references are correct ([DLMF 5.2](https://dlmf.nist.gov/5.2),
  [DLMF 5.5](https://dlmf.nist.gov/5.5)). The cited
  [Connes--Consani paper](https://arxiv.org/abs/1211.4239) explicitly concerns
  archimedean factors as regularized determinants from cyclic homology.
  The packet appropriately claims no novelty over that territory, no
  analytic certification by finite replay, and no finite-place/global
  transfer or RH estimate.

## Verification and remaining risks

The repaired packet has 29 normal/optimized unit tests, covering the original
fixtures plus negative/zero multiplicities, meromorphic cancellation at
individual poles, divisor boundary states, invalid exact/formal inputs,
bounded-work guards, normalization coefficients, dual-map direction,
localized heat weights, line-ending invariance, full source validation, and
typed fixture tampering. Both producer modes, Ruff, and whitespace checks
pass. Finite checks support the implementation; the proofs supply the
all-order, infinite-dimensional, and arbitrary-complex statements.

No actionable theorem-level defect remains from this audit. The open
scientific risk is whether an independently motivated arithmetic carrier
can realize these operations and connect them to finite places and an
explicit-formula trace law. The ladder calibration itself supplies none of
those bridges. Analytic inputs remain imported classical theorems; this
audit does not replace them with a proof-producing analytic computation.
