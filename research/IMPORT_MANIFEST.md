# Prioritized proof-import manifest

**Status:** integration plan, not a theorem. RH remains unsolved.

This manifest records why the reviewed Weil/screw and operator stacks are not yet resident proof packets, and the exact order in which safe extraction should proceed.

## Import rule

An object is ready only when:

1. its source SHA and review are exact;
2. the extracted claim is no broader than the frozen verdict;
3. all source, domain, normalization, and artifact prerequisites are named;
4. claim-ID collisions and supersessions are resolved append-only;
5. finite algebra is separated from every cofinal or global hypothesis.

No source PR should be merged whole merely to satisfy this order.

---

## A. Weil, screw, carrier, and terminal-prime spine

### A0. Canonical explicit-formula source contract — prerequisite

**Candidates**

- PR #4 at `a02020fcfdd90a10fffe31f397f7cffeb8d6eed7` — `GAP/BLOCKED`; D-0001 source, admissibility, and normalization interface.
- PR #49 at `6fa9b278811eba563305510e58caa3409b8a95f4` — `VERIFIED WITH FIXES`; self-contained T-2801 Guinand–Weil transport and exact correction infrastructure.
- PR #51 at `6e51017578544a0cff4f2614b6ed893886ce64e7` — `VERIFIED WITH FIXES`; exact archimedean Toeplitz and pole corrections.

**Conflict**

The branches use overlapping D-0001/T-2801 conventions. The recent dictionary source may corroborate the formulas but cannot silently replace a classical source derivation. Correction schemas must not be selectable by convention at runtime.

**First safe extraction**

One packet fixing:

- \(\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)\);
- zero coordinate, multiplicity, Fourier sign, and \(2\pi\) convention;
- admissible test family and strip decay;
- prime, higher-prime-power, pole, and archimedean terms;
- exact transport from the classical explicit formula;
- a normalization fingerprint consumed by every finite artifact.

Until A0 exists, no RH-facing carrier result is ready.

### A1. Finite carrier exclusion

- PR #65 at `7296bf55449a4b510e4823028744deb793516e14` — `VERIFIED`, finite.
- Principal files:
  - `experiments/X-2805-directed-prime-producer/results/target-c1e11/final/complete-result.json`
  - `experiments/X-2805-directed-prime-producer/results/target-c1e11/final/verdict-dual-p192-p256.json`
  - associated exact checker and frozen vector.

**Safe statement**

One frozen \(K=1024,c=10^{11}\) vector has a strictly positive complete finite contraction under the declared producer/checker contract.

**Not safe**

Matrix positivity, another vector, or evidence for RH.

**Import after:** A0.

### A2. Pole-free terminal-prime scalar criteria

- PR #165 at `3a4c4f77271596fef6af4aa7262503c7cde28cc0` — `VERIFIED WITH FIXES`.
- Candidate claims: `L-15405`, `T-15403`, `T-15404`, `T-15405`.

**Required repairs**

- pin the exact smoothed von-Mangoldt explicit formula;
- state support and endpoint conventions;
- use one precise compactness topology;
- group coincident ordinates and cite the exact almost-periodic Parseval theorem;
- keep the scalar criterion independent of later Suzuki packet interpretations.

**Import after:** A0.

### A3. Finite notch/Fourier-tail repair

- PR #184 at `3da1c059ac6f22f1d147f8e43d3fbd400e89fd07` — `VERIFIED`.

**Safe statement**

The finite Fourier-tail/interpolation theorem and all-MPFR replay refute the old interpolation nomination.

**Not safe**

A complete RH phase-band certificate.

**Import after:** A0 and the exact inherited phase-band theorem.

### A4. Square-screw criterion

- PR #202 at `f675940e8f493b5cfc1166af0398577078be2d61` — `VERIFIED WITH FIXES`.
- Candidate claims: `L-19801`, `L-19802`; conditional theorem layer after repair.

**Required repairs**

- remove the inference in `T-19806` that an unrelated internal quotient defect must vanish;
- resolve duplicate `L-19815` IDs;
- pin the exact zero-count theorem version and normalization;
- keep eventual/subpolynomial hypotheses explicitly cofinal.

**Import after:** A0 and independent review of the repaired SHA.

### A5. Matrix-coordinate connection

- PR #208 at `f3b5a9cad45f352c79236b9966aa3f7c117de33b` — `VERIFIED WITH FIXES`.
- Candidate claim: `L-20704`.

**Safe statement**

The constant D-0001 coordinate equals the square-screw statistic divided by \(\log M\) in the declared normalization.

**Required repairs**

- bind the exact unseen-zero radius source;
- consume the repaired #202 theorem;
- avoid any cofinal inference from a finite ladder.

**Import after:** A0 and A4.

---

## B. Kernel and operator spine

### B0. Source, metric, and simple-zero interfaces — prerequisite

The operator chain requires one pinned centered Weil/\(\Xi\) normalization, the exact form/metric domain, and certified-simple-line-zero interfaces. It also requires the zero-evaluation split used by later Schur blocks.

Relevant upstream objects include:

- PR #150 at `feefc9fa68330a9821f730d634a7b9e4001cfba0` — `VERIFIED`, finite conditional prolate/Hardy reductions;
- PR #159 at `0c94e4bd1997b47e0bd54027ed9e64ac9f7e97ce` — `VERIFIED WITH FIXES`, visible/near-kernel split;
- PR #191 at `be7118ea650ccbed82f036d23e5b329d5957a8b3` — `VERIFIED WITH FIXES`, simple-line and finite deficit interfaces; the Hermitian interval checker requires repair.

No later packet should silently assume B0.

### B1. Cardinal/radical finite section — first theorem import

- PR #168 at `2a3667399b4a16311e1875932f9361c6aa6c8d0d` — `VERIFIED`.
- Candidate files:
  - `claims/lemmas/L-14321-xi-cardinal-weil-decomposition.md`
  - `claims/theorems/T-14306-cardinal-radical-diagonal-closes-requested-pair.md`

**Safe statement**

The exact Xi-cardinal decomposition and finite-section radical repair close the requested pair for the constructed packet.

**Boundary**

Complete-low capture is separate; inverse-\(\Xi'(\gamma)\) conditioning remains a production issue.

**Import after:** B0.

### B2. Three-block Schur algebra

- PR #169 at `06d1d133c2c786447e6c126861cc2d6a31f82a8b` — `VERIFIED`.
- Candidate files:
  - `claims/lemmas/L-15306-triangular-three-block-schur-floor.md`
  - `claims/lemmas/L-15308-cofinal-diagonal-radical-row-and-exact-assembly.md`

**Safe statement**

Ordered completion of squares, the corrected cross term, and fixed-packet diagonal extraction are exact.

**Boundary**

The visible Schur margin and form-tail convergence remain hypotheses; diagonal extraction is not complete capture.

**Import after:** B0 and B1.

### B3. Canonical deficit augmentation

- PR #192 at `6c1a3a73de6b020aabaf1dff6cda9b8c7129af3f` — `VERIFIED`.
- Candidate file: `claims/lemmas/L-18901-canonical-deficit-complement-augmentation.md`.

**Safe statement**

For the declared lower model, the high spectral subspace of the compressed deficit is the minimal-rank augmentation that certifies the complement floor.

**Boundary**

Minimality is relative to the declared lower model, not the unknown true operator.

**Import after:** B2 and the lower-symbol/deficit interface.

### B4. Kernel-defect boundary classifier

- PR #199 at `4158e0d3e7f91829a6c545308605ea8177023aa3` — `VERIFIED`.
- Candidate files:
  - `claims/lemmas/L-19701-schur-corrected-offline-cardinal-gap.md`
  - `claims/theorems/T-19701-kernel-floor-equivalent-to-rh.md`

**Safe statement**

Positive-complement Schur elimination cannot repair an off-line cardinal negative direction. Under explicit complete form/metric capture, the complete corrected-kernel floor is an RH-equivalence classification.

**Boundary**

The theorem identifies the RH-bearing sign; it does not prove complete capture or the sign.

**Import after:** B1–B3.

### B5. Local Möbius residual

- PR #204 at `4b770cf245ca2253efb0db2b807f4eab37775333` — `VERIFIED`.
- Candidate file: `claims/lemmas/L-20301-local-mobius-radical-extension.md`.

**Safe statement**

Finite Möbius inversion reconstructs the local source exactly and leaves an explicit residual supported below the local interval.

**Boundary**

Quantitative smallness in the Weil/Schur metric remains open. Correct the recorded notation typo before publication.

**Import after:** B4.

### B6. Conditional two-frame and joint residual

- PR #206 at `ff659984de0ab0c397ebefad393bc585c9007bc2` — `VERIFIED`.
- Candidate files:
  - `claims/lemmas/L-20501-conditional-simple-line-schur-matrix.md`
  - `claims/lemmas/L-20504-joint-corrected-residual-moat.md`
  - `claims/lemmas/L-20505-optimal-split-negative-part-identity.md`

**Safe statement**

The graph kernel, conditional evaluation Schur matrix, and optimized corrected-residual identities are exact finite algebra.

**Boundary**

Depends on repaired #191 and B5. Finite frame existence is not a uniform cofinal moat.

**Import after:** B0–B5.

---

## C. Conflicts that must remain visible

- PR #152 at `bad48a791146218bb2d76a0345d7b60a6d729b64` contains duplicate `143xx` IDs and mixed source/cofinal variants.
- PR #163 at `c3ebadec228d79b802af89c8a01759c3290c32bf` contains a verified finite capacity subset but duplicate IDs and an unproved profile-soft/Suzuki LMI.
- PRs #177, #179, and #181 collide in the `156xx` namespace; #177 also has an endpoint-domain failure and #181 incomplete shell coverage.
- PR #211 at `54c884c3dccb8618b706ae3d7bdd6edf47c59bc9` is missing one required bundle segment.
- A later repair must receive a new identity and exact-SHA review; it cannot be used to broaden the frozen verdict.

## First safe next import

The dependency-minimal next proof-bearing packet is **B1**, but only after B0 is pinned. The corresponding integration task should extract the two #168 claim files, state the centered-Weil and simple-zero assumptions at the top, and exclude `T-14307` or any complete-kernel conclusion not independently discharged.

---

## D. External exact-source imports

### D1. OpenAI prime-gap repositories, published 2026-09-02

```text
Status: IMPORTED / REVIEW_PENDING
Import branch: research/gpt56-pro/20260903-prime-gaps-import
Riemann base: 6dda8b5125457ed936330229f8c9eb6491728e76
Dossier: research/exploratory/openai-prime-gaps-2026-09-02/
```

#### `openai/PrimeGaps186`

- Exact source: `61340d0b74163003b32756bb16e91d9209a5e330`.
- Local gitlink: `research/exploratory/imports/openai-prime-gaps-2026-09-02/PrimeGaps186`.
- License: Apache-2.0.
- Toolchain: Lean 4.34.0-rc2.
- Boundary: `primeGapLiminf <= 186` is proved conditional on `kloosterman3_bound`, `kloosterman2_correlation_bound`, and `physical_integral_bounds`.
- Reproducibility: upstream Python/FLINT certificate corroborates the 152 physical inequalities but is not consumed by Lean; no local replay was performed in the import pass.
- Review: upstream self-assessment only; independent exact-SHA semantic review required.

#### `openai/LongGapsBetweenPrimes`

- Exact source: `8f5fa88c88b4750028c05b66b081d56a92418054`.
- Local gitlink: `research/exploratory/imports/openai-prime-gaps-2026-09-02/LongGapsBetweenPrimes`.
- License: Apache-2.0.
- Toolchain: Lean 4.33.0, matching the current Riemann generation.
- Boundary: the eventual Erdos-Rankin-scale long-gap theorem is reported with no project-specific axioms.
- Reproducibility: clean build, comparator, `#print axioms`, and statement-equivalence replay remain to be independently deposited.
- Review: upstream self-assessment only; independent exact-SHA semantic review required.

#### Integration decision

Both repositories remain exploratory submodules. Neither modifies the trusted formal spine or creates an RH implication. The source lock, theorem audit, improvement plan, and RH firewall are in the dossier named above. Promotion requires exact-SHA review and modular extraction; the conditional 186 endpoint cannot be registered as unconditional while any of its three project assumptions remains.
