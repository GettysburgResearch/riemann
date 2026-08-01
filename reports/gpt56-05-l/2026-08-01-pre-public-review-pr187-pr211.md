# Pre-public review: PRs #187, #190, #191, #192, #196, #199, #200, #202, #204, #206, #208, #209, #210, #211

Date: 2026-08-01  
Reviewer: `gpt56-05-l`  
Scope: independent review of the exact frozen commits below. Later pushes are outside this ledger.

## Review method and status meanings

I recorded each head before reading substantive files and then fetched load-bearing claims and code by the frozen commit SHA. I did not rerun expensive computations. I inspected formulas, quantifiers, source dependencies, checkers, manifests, and workflow provenance; only small algebraic spot checks were used.

- **VERIFIED**: correct within its expressly stated hypotheses and proof boundary.
- **VERIFIED WITH FIXES**: the mathematical core passes, but listed repairs are mandatory before integration or promotion.
- **GAP/BLOCKED**: a required artifact, source binding, trust-boundary check, or result is absent or invalid at the frozen commit.
- **REJECTED**: a load-bearing conclusion is false in its stated scope. None of the assigned PRs is classified REJECTED.

`VERIFIED` never promotes an inherited `PROPOSED` theorem or turns a finite result into a global one.

## Frozen heads

| PR | Frozen head SHA |
|---:|---|
| #187 | `5da398e7a0112c7a165bd9c1155a86dc3a1b1b8f` |
| #190 | `a5c8ef654b18c4f82e84ecab391958a6b991257b` |
| #191 | `be7118ea650ccbed82f036d23e5b329d5957a8b3` |
| #192 | `6c1a3a73de6b020aabaf1dff6cda9b8c7129af3` |
| #196 | `09fc8cf5418872262721feae2a1a450c1a56e0e8` |
| #199 | `4158e0d3e7f91829a6c545308605ea8177023aa3` |
| #200 | `ceb4378a166680db73d840e1aeba6f216db6b6a9` |
| #202 | `f675940e8f493b5cfc1166af0398577078be2d61` |
| #204 | `4b770cf245ca2253efb0db2b807f4eab37775333` |
| #206 | `ff659984de0ab0c397ebefad393bc585c9007bc2` |
| #208 | `f3b5a9cad45f352c79236b9966aa3f7c117de33b` |
| #209 | `400aeb3faecc8e640866577fd10bd210441a5b90` |
| #210 | `5b139c5c2227fd1cc96dd9aab9ea70bb3fec981f` |
| #211 | `54c884c3dccb8618b706ae3d7bdd6edf47c59bc9` |

## Classification summary

| PR | Classification | Integration verdict |
|---:|---|---|
| #187 | **GAP/BLOCKED** | Trigger only; no workflow run or result artifact at the frozen SHA. |
| #190 | **VERIFIED WITH FIXES** | Exact filter/spline algebra passes; repair the two-tap uniqueness hypothesis and retain inherited conditionality. |
| #191 | **VERIFIED WITH FIXES** | Finite/form algebra passes; harden `X-18509` Hermitian interval binding and pin the simple-line-zero citation. |
| #192 | **VERIFIED** | Exact canonical deficit augmentation relative to the declared lower model. |
| #196 | **VERIFIED** | Correctly scoped empirical/truncated-Φ reconnaissance only. |
| #199 | **VERIFIED** | Correct RH-equivalence classification under explicit complete form/metric capture. |
| #200 | **GAP/BLOCKED** | Exact algebra passes, but directed endpoints are serialized with nearest decimal rounding and then trusted as bounds. |
| #202 | **VERIFIED WITH FIXES** | Square-sampling/Landau core passes; repair `T-19806` scope and duplicate claim IDs. |
| #204 | **VERIFIED** | Exact local Möbius reconstruction and explicit residual; quantitative tail remains open. |
| #206 | **VERIFIED** | Exact finite two-frame/Schur algebra; cofinal residual moat remains open. |
| #208 | **VERIFIED WITH FIXES** | Exact square-coordinate/resolvent algebra passes; bind the unseen-zero radius and merge only after #202 repairs. |
| #209 | **GAP/BLOCKED** | Immutable trigger/config change only; no workflow run or result. |
| #210 | **GAP/BLOCKED** | Rerun marker only; no workflow run or result. |
| #211 | **GAP/BLOCKED** | Finite transfer theorem is repairable, but the claimed first-growing bundle is incomplete and unreconstructible. |

## Per-PR review

### PR #187 — GAP/BLOCKED

Frozen file `experiments/X-17801-fourier-window-enclosure/RUN_PHASE_BAND.md` correctly says it is only a trigger and asserts no sign. GitHub reports no workflow run associated with the frozen commit. There is therefore no finite phase-band verdict to review or integrate.

**Required action:** retain only as provenance, or replace it with a result-bearing commit containing the immutable workflow artifact, checker output, source hashes, and exact scope.

### PR #190 — VERIFIED WITH FIXES

- `L-17802`: translation, Laplace factor, support, derivative-`L1`, resonance, displacement, and sensitivity comparisons are exact.
- `T-17801`: valid only subject to inherited `T-15404/T-15604`; it does not independently prove the explicit-formula/Laplace criterion.
- `L-17803`: finite B-spline formula, transform, support, and critical-line decay are exact.
- `X-17802`: sound Fraction-only algebraic replay; it is not a Riemann zero/prime certificate.

**Mandatory fix:** Section 6 of `L-17802` says the extremal two-tap filter is unique up to sign while allowing apparently complex coefficients. For real filters this is correct; for complex filters uniqueness is only up to a unimodular phase. Add “real two-tap filter” or replace “sign” by “phase.”

**Merge order:** after the accepted `T-15404/T-15604` normalization stack; numerical frontier claims must bind the exact verified-height source.

### PR #191 — VERIFIED WITH FIXES

- `L-18511`: the finite-dimensional Jensen argument and one-uniform-height conclusion are valid. The cited Pratt–Robles–Zaharescu–Zeindler paper explicitly reports `κ* ≥ 0.407511` for simple zeros on the critical line, so the needed `N_0^*(T) ≫ T log T` input is available. Cite the exact section/equation rather than only the paper title.
- `L-18512`: exact trial-lift/residual Schur identity and coercive lower matrix are correct.
- `X-18505`: the `c=5,N=1` consumer checks off-diagonal overlap, source bindings, exact compression, and strict pivots appropriately.
- `L-18517`: the `c=10,N=2` deficit projector is a finite spectral statement only and is scoped that way.

**Mandatory checker fix:** `experiments/X-18509-complete-spectral-deficit-c10N2/verify.py` parses a full interval matrix, but `interval_ldl` consumes one triangle without first requiring `A[i][j]` and `A[j][i]` to overlap and without intersecting them into one Hermitian interval. A malicious asymmetric primitive can therefore influence the accepted lower triangle while the unused upper triangle disagrees. Add a fail-closed Hermitian intersection step for `P`, `E`, and every derived matrix before LDL, then regenerate the retained proof object and mutation tests.

**Merge order:** after the D-0001/Suzuki normalization and the three-block base. Downstream PRs #204/#206 must consume the corrected simple-line citation and checker contract.

### PR #192 — VERIFIED

`L-18901` is an exact functional-calculus theorem: the high spectral subspace of the compressed positive deficit is the minimal-rank augmentation that makes the *declared lower model* certify the complement floor. The file correctly does not claim minimality for the true operator independently of that model and correctly leaves all possible negativity in the enlarged finite packet. `X-18901` checks symmetry, metric positivity, exact orthogonal decomposition, lower-model slack, high/safe deficit inequalities, and the final complement floor.

**Merge order:** after the complete lower-symbol/deficit interface; it does not establish that the augmentation is empty.

### PR #196 — VERIFIED

`O-8455b` and the accompanying report are consistently labeled empirical. The finite and continuum double-root systems and the observed `N^{-3}` approach are useful reconnaissance. The Arb Jacobian statement is explicitly a **truncated-Φ directed probe**; the report correctly says the Φ-tail and interval Newton uniqueness are absent. No RH or full-continuum certificate is asserted.

**Integration:** merge only as observation/experiment material, not as a theorem claim.

### PR #199 — VERIFIED

`L-19701` correctly observes that positive-complement Schur elimination subtracts a PSD term and therefore cannot repair an off-line Xi-cardinal negative direction. The `-2m` cardinal signature and fixed negative gap are valid under the declared Xi-cardinal domain and complete form/metric capture assumptions. `T-19701` states those assumptions explicitly and is therefore a classification/equivalence theorem, not a proof of capture.

**Merge order:** after #192 and the accepted Xi-cardinal/finite-section normalization stack. It must never be cited as supplying complete capture itself.

### PR #200 — GAP/BLOCKED

`L-17804`’s cumulative-moment identity and local polynomial-cell recursion are exact. The C producer also uses directed MPFR rounding internally. The retained proof object is nevertheless not directed at the serialization boundary:

```c
mpfr_printf("prime_lower=%.150Re\n", total.lo);
mpfr_printf("prime_upper=%.150Re\n", total.hi);
```

MPFR’s `R` format defaults to round-to-nearest unless a rounding selector is supplied. The official MPFR manual specifies `D` for downward and `U` for upward output rounding. The Python consumer then parses these nearest-rounded decimal strings as exact Fractions and trusts them as lower/upper bounds.

**Required repair:** output lower with `RNDD` and upper with `RNDU` (or exact binary/hex mantissa plus exponent), bind the exact output format, regenerate every precision row and summary, and independently replay at least one backend. Until then the claimed directed prime interval is not a proof-grade enclosure.

### PR #202 — VERIFIED WITH FIXES

- `L-19801`: the unconditional derivative budget, square-mesh interpolation, and Landau one-sign transfer are coherent. The eventual/subpolynomial sampled inequalities are genuinely global and no finite ladder is promoted.
- `L-19802`: the rightmost-zero exponent follows from the absolute zero expansion plus `L-19801`; it does not assert a finite determination.
- `L-19807`: the Trudgian normalization is correct: `N_K(T)` counts both signs with `|γ|≤T`, and Theorem 2 gives the constants `0.317`, `6.333`, `3.482` for `K=Q`. Production use should pin the exact theorem version.
- Abstract Green/Cayley defect identities are valid but leave theta accretivity open.

**Mandatory fixes:**

1. `T-19806` correctly proves an integration-by-parts congruence from the normalized full form to the original `K_0` form. It overreaches when it infers that the internal quotient repair `D_q` must equal zero merely because the physical primitive integration has no boundary term. Those are distinct decompositions. Retain: “positivity of the complete normalized form pulls back to `K_0` positivity.” Remove: the inference that this identifies or forces the internal quotient defect to vanish.
2. The frozen branch contains two different files carrying Claim ID `L-19815` (`green-cayley-defect-factorization` and `green-cayley-dissipativity-factorization`). Consolidate or renumber before registry integration and scan the branch for further ID collisions.

**Merge order:** after `T-15404` and the screw/Laplace normalization audit. PR #208’s RH consequence must wait for these repairs.

### PR #204 — VERIFIED

`L-20301`’s finite Möbius inversion, source correction, exact reconstruction on `[a,b]`, and explicit residual support below `a` are correct. The Mellin residual identity makes the zero-evaluation obstruction transparent. The weak-radical conclusion remains an inherited normalization/form-domain dependency, and the file says so. The construction proves existence of exact local extensions; it does not prove smallness of the lower tail in the Weil/Schur metric.

**Minor cleanup:** replace the acknowledged `nu` typo in `L-20301.18` by `u` before publication.

**Merge order:** after `L-16205` and #199.

### PR #206 — VERIFIED

`L-20501`’s graph kernel, conditional evaluation Schur matrix, determinant factorization, induced metric, and positive conditional Gram are exact finite algebra. The later joint-corrected-residual and optimized negative-part identities correctly show that changing the split does not weaken the immutable corrected kernel. Finite frame existence inherits #191’s corrected simple-line uniqueness theorem; no cofinal lower rate is claimed.

**Merge order:** after repaired #191 and #204. Do not represent finite conditional frames as a uniform cofinal moat.

### PR #208 — VERIFIED WITH FIXES

- `L-20704`: the constant D-0001 coordinate equals the square-screw statistic divided by `log M`; the polar, prime-power, and archimedean term matching is exact in the declared normalization.
- `T-20701`: correctly marks the RH consequence as cross-branch and conditional on #202.
- `L-20801` and the source-resolvent/Schur algebra are exact finite identities.
- `X-20702` is explicitly a fixed-height, noncofinal lower model; the fixed-point transcendental arithmetic is structured to be outward.

**Mandatory source binding:** the unseen-zero radius in `X-20702` is described as the imported off-line-safe `L-15127` bound, but the frozen PR does not place the derivation/theorem hash in the verifier’s trust boundary. Before promoting the finite result, bind the exact claim/source version, constants, centered-zero convention, multiplicity convention, and verified-height theorem into the certificate or checker.

**Merge order:** after the #202 repairs and the common D-0001 admissibility/normalization audit. A finite verified-height ladder remains finite.

### PR #209 — GAP/BLOCKED

The frozen commit changes only a trigger nonce in a configuration bound to source commit `34d8391395d1e08ae986bf5c1c10439f90f9cb57`. No workflow run is associated with the frozen trigger SHA and no result artifact is present. It asserts no sign, so it is not false; it is simply not a reviewable result.

### PR #210 — GAP/BLOCKED

The frozen commit adds only `RERUN-2026-08-01.md`, listing required outputs. No workflow run or produced ladder is associated with the frozen SHA. There is no finite sign or cofinal result to verify.

### PR #211 — GAP/BLOCKED

`L-18513`’s level-wise transfer conclusion is correct: if the full finite matrix satisfies `A≽δG`, every exact `G`-orthogonal profile-soft Schur complement has the same lower floor. Its quantitative proof should use the variational characterization of a Schur complement (or an `ε` regularization); the displayed inverse of `A_HH-δG_H` need not exist when the lower bound is attained.

The principal first-growing artifact is not reconstructible at the frozen commit. `BUNDLE.md` requires `bundle.part00` through `bundle.part07`, but `bundle/bundle.part02` is absent. Consequently the advertised archive hash, ledger, checker, and verdict cannot be reproduced.

**Required action:** add the missing chunk or replace the transport with a normal immutable archive/artifact, verify its SHA, rerun the checker/mutations, and repair the quantitative proof. Until then the `c=10,N=2` production claim is blocked.

## Cross-PR connections missed or underemphasized

1. **The square-screw and matrix programmes share one immutable scalar.** `L-20704` identifies PR #202’s square-screw statistic with the constant D-0001 coordinate. Therefore any cofinal matrix floor in #208 must already prove the scalar subpolynomial negative-part estimate from #202. Conditioning, Leja selection, or Schur bookkeeping cannot bypass it.

2. **The finite-block stack has removed algebraic ambiguity, not the RH-strength tail.** PR #192 moves all danger into a finite canonical packet; #199 proves an off-line cardinal survives every positive-complement Schur elimination; #204 constructs exact Möbius radical extensions and localizes the entire obstruction into a lower tail; #206 rewrites the same corrected kernel through exact two-frame algebra. The remaining estimate is precisely form/metric control of that tail, and false RH gives a fixed negative obstruction.

3. **PR #200 can become a shared proof backend after one small but mandatory fix.** Its local finite-spline contraction is an attractive independent arithmetic producer for the first-difference windows of #190 and the square-schedule checks of #202/#208. The nearest-rounded decimal boundary currently prevents that integration.

4. **Profile-soft transfer is downstream consistency, not new sign information.** Once a finite full matrix is positive, #211’s transfer makes every exact soft split positive automatically. The profile ledger is then valuable for source identity and implementation checking, but it cannot replace the cofinal arithmetic lower law.

## Merge-order summary

A safe high-level order is:

1. shared Weil/D-0001/screw/explicit-formula normalization claims;
2. #190 after its uniqueness wording fix;
3. #202 after `T-19806` scope repair and claim-ID cleanup;
4. #191 after citation and `X-18509` Hermitian hardening;
5. #192, then #199, then #204, then #206;
6. #208 only after #202 and the unseen-zero radius are bound;
7. #200 only after directed serialization and artifact regeneration;
8. #211 only after bundle reconstruction and proof repair;
9. triggers #187/#209/#210 only with their result-bearing artifacts, not as mathematical results alone.

## SERIOUS RESOLUTION PATH

**YES — a serious exact resolution programme is present, but no reviewed PR supplies the decisive arithmetic estimate.** Two interfaces now appear to be the same obstruction in different coordinates.

### Path A: finite square-screw arithmetic

1. Independently close the screw/Laplace normalization and the corrected `L-19801/T-19801` Landau transfer.
2. Prove on the all-integer square schedule
   \[
   (-\Psi(2\log M))_+=M^{o(1)},
   \]
   or the stronger eventual sign.
3. Use `L-20704` as an exact overlap check: the same estimate must hold in the constant D-0001 coordinate of every matrix packet.

This path is fully finite at each `M`, uses all prime powers through `M^2`, and avoids an independent infinite-dimensional capture theorem. Its missing step is a new global arithmetic estimate far stronger than a finite verified-height calculation or ordinary PNT error bound.

### Path B: complete-kernel synthesis

1. Independently close the Xi-cardinal and weak-radical normalization/domain claims.
2. Use #192 to place every unresolved direction in a finite canonical packet and #204 to construct an explicit global-radical extension of the complete selected-real-zero kernel.
3. Prove uniformly that the explicit Möbius lower-tail Weil form and the complete Schur cross are `o(1)` in the packet metric.
4. Emit a cofinal directed assembly with all source, metric, prime, archimedean, and harmonic residual bindings.

PR #199 proves that false RH creates a fixed negative cardinal gap, so a valid proof of this tail estimate would genuinely resolve RH rather than merely improve conditioning.

At present, neither path has its load-bearing arithmetic theorem. The repository has legitimately isolated the target and produced multiple exact finite consumers, but **RH remains unproved and undisproved**.

## Final boundary

- No assigned PR proves RH or produces a counterexample.
- Finite directed positivity is retained as finite.
- Conditional equivalences remain conditional.
- Repairs proposed in this review do not retroactively verify the affected frozen artifacts.
