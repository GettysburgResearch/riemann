# Review of the overview, sources, and root replay receipt

Date: 25 October 2026.
Reviewer: `spectral_selector`, separate from the root author of the overview and source/replay description.
Verdict: **PASS for summary fidelity, source qualification, and finite-replay receipt consistency at the exact hashes below, after the two parameter-domain corrections recorded in Section 2.** No improved zero-free region is certified.

## 1. Independence and exact reviewed objects

I authored the underlying spectral component notes and the original selector diagnostic script. This report is an independent review of the root author's overview, source descriptions, and replay receipt; it is **not** an independent review of my own spectral proofs. The separate marked-count agent supplied that latter review in `SPECTRAL_CONSUMERS_REVIEW.md`, SHA-256 `c85345c53b579152893c66897a55c9918aebb7d25827926111f3af719ad5979d`.

I previously reviewed the fractional notes independently of their author. For the marked summaries here, I read all three marked component notes and their separate fractional-track review. This report checks that the overview states those components with their actual hypotheses and limits; it does not replace the complete component reviews.

| Reviewed object, relative to packet root | SHA-256 |
|---|---|
| `README.md` | `136bea7d5fda5c3fbd6ea5195a51e5dcaaec851f57f8e65344e7593f820dbac8` |
| `SOURCES.md` | `369c3958f68bb1e19a677715891b74ac8278d0356c482b041a9b6470b995d418` |
| `reviews/ROOT_REPLAY.json` | `4b6f497bc06e90d0e97766946341f47378254f938c3b4a16a928cd59786c99e0` |
| `spectral/selector_root_replay.json` | `ed09c4d8441962209009b75b8e35eeb623458c37696c1c9dcc7d1de077f622e4` |

The component files used for this comparison have these hashes, matching their separate review receipts:

| Component | SHA-256 |
|---|---|
| `marked/MATCHED_PRIME_SQUAREFREE_REMAINDER.md` | `6cf6a71909f23fa29f7b1d7a0833da477fc2b1a58d9c81aeab8bdc19032348b0` |
| `marked/GROWING_INTEGER_RESONANCE.md` | `5a42b1ce61200a33e5bef112f5691fe03e3b9a9457779f8515952e46875347d2` |
| `marked/GEVREY_INTEGER_WINDOW.md` | `2eabc9818994e00d8113c237d95eb76a7dae46675000c45adf60f97279d9d216` |
| `fractional/UNIFORM_FRACTIONAL_WINDOW.md` | `18df393da1423c33256237a7f739409b4cbe26bae6d2b63ede6dbc05b118b6e0` |
| `fractional/NORM_TWIST_AND_BAND_TRANSFER.md` | `836be1511e47c4dc2f6848e0bab1393af0659327253f607d601b97c5627f950e` |
| `spectral/SPECTRAL_GROWTH_AND_TIGHT_POSITIVE_SELECTION.md` | `4db61773b675f4926731360eee769cd49cb66690a56f2a66cd02f902bf38e083` |
| `spectral/EVEN_FINITE_SELECTOR_CONSUMER.md` | `6c0a67ede84942a31287716661d5fe85644445a0517a296eed36be23c8036e74` |

## 2. Corrections requested and verified

The initial overview had SHA-256 `5163ee28424c559de58bd1c2f4a054a24285a91fffe6458b2add343b18859984`. I requested two precise corrections, both already present in the final reviewed version:

1. State `eta >= 0` before the finite spectral-growth implication. The component theorem has this hypothesis. Allowing negative eta would make the overview's implication false.
2. State `0 <= z <= 1` for the real fractional-window inequality with factor `1-z`. The complex-disk extension has an absolute-distance factor and an additional bounded cost on the stated power-thin scale; it is not the same literal inequality for arbitrary complex z.

The root author made these changes. No component file was changed during this overview review. I found no remaining blocking summary or source-scope defect at the reviewed hashes.

## 3. Mathematical summary fidelity

### Spectral target

The overview gives the exact even subspace, inherited L2 normalization, zero-extension convention, and cofinal cutoff `N_k=ceil(k^3)`. The full prime-power coverage, archimedean term, and both pole terms are retained. The growth exponent converts correctly: `2 eta` in the interval half-width becomes the zero-strip width `eta`, so `eta=1/4` gives `Re s>3/4` and `eta=0` gives RH under the all-scale hypothesis.

The even-sector reduction and finite projection reduction are described as proved implications, not as proofs of the matrix lower bound. The note does not reverse the Rayleigh comparison and does not infer a continuum lower bound from finite minima. Its account of the one-sided Laplace argument and the Gevrey/logarithmic-domain estimates matches the component notes.

The selection version retains exact finite legality, global physical nonnegativity, and uniform tightness. Bounded second moments supply tightness only together with nonnegative mass-one densities. The overview correctly keeps those premises and warns that imposing constraints in a different minimization does not produce the required unconstrained resolvent equation. It therefore does not claim that the variance equation or physical positivity has been solved.

### Matched marked discrepancy

The definitions of `J`, `J_0`, `R`, and `Delta_W` agree with the component proof. The overview retains the cutoff integral with its correct sign and the full higher-prime-power correction. Absorbing the correction remainder into `O(X^c)` is justified because `c>1/2`. The stated cutoff size `O(X^b/log X)` is the actual fixed-profile endpoint estimate.

The reciprocal-moment identity and the bound `Delta_W=O(X^beta)` are explicitly conditional on the stated prime-error estimate, with `1/2<beta<1`. The overview correctly says this removes the separate hyperbola loss and recovers the input exponent; it does not claim an improvement of beta. The local-zero discussion is presented as explaining the remaining power exponent, without substituting a local Hankel germ for a global zero expansion.

### Growing positive integer marks

The positive theorem is restricted to the specified smooth profile and to scalar squarefree counts with the complete pole polynomial removed. The range `0<theta<1` and exponent `max(1/2,theta)+epsilon` match the component result. For `theta>1/2`, the separate near-real resonance gives the claimed necessary threshold, up to the arbitrary small loss in the upper theorem. The larger-window obstruction is also stated for the same scalar model.

The overview does not claim optimality at or below `theta=1/2`, does not transfer the obstruction to a varying character-family mean, and retains the factorial in the local high-order calculation. Its use of the word “matching” is supported in the explicitly stated `theta>1/2` range.

### Fractional native mean and norm twists

The fractional estimate remains conditional on the pinned ordinary endpoint and arbitrary-coefficient sieve inputs. It uses the actual sixth-power-free row family, common puncture and profile/height scope, rather than a selected squarefree row subfamily. The three displayed window exponents agree with the component calculations. The complex-disk sentence concerns the same scale, without claiming the identical real inequality there.

The overview says that the power-thin window is insufficient for the earlier generic continuation bound, and leaves the logarithmic-width window open. It does not convert failure of a generic interpolation guarantee into an impossibility theorem for the actual arithmetic family. The norm-twist result remains conditional on a fixed zero-free half-plane and concerns its specific uniform or harmonic approximation criterion. The shifted-prime paper is not used as an unproved native-kernel transfer.

## 4. Numerical and source-authentication checks

I compared the stored `a=0.4`, 16-mode case from `selector_n16.json` directly against `selector_root_replay.json`. Every equality flag in the root receipt agrees with the corresponding JSON data. The eight listed matrix/endpoint quantities agree exactly as stored. The selected shift, finite margin, variance, variance residual, complete coefficient list, and physical-grid record also agree exactly as stored. The linear-system residual differs, consistently with the stated change from 110 to 125 decimal digits. The replay's recorded quadrature order is 192 rather than 160.

The overview calls this agreement of reported digits from the same matrix implementation. It does not call it an independent implementation, interval computation, global positivity proof, or continuum legality certificate. The eight original cases and their bracket descriptions agree with the original reports. The failed-bracket interpretation is appropriately limited to the tested endpoint pair. The sample signs and the very small selected shift at `a=1.3` are not promoted to asymptotic conclusions.

I reran the marked finite checker with Python isolation, no site packages or bytecode, in both normal and optimized modes. Both outputs agree byte for byte with the recorded JSON, SHA-256 `bc65833e77f89f0b558d94dbbdc80e50f4fa39d253646ed37ab2e37523b1b0f6`. Its 2,048 coefficient cases, 340 prime powers, 17 smoothing cases, and 418 prime-only mutation failures, first at 4, match the overview and receipt. The report correctly marks its analytic and zero-free assertions as uncertified.

I also independently reconstructed the PR #1017 archive in memory from the listed Git objects at `450dd8abecf58dfe60b3bc39bda0f792ea82ce95`, checking each part's object identifier and byte count. The concatenated SHA-256 is `8185bfe6f9a5e2899cae78083a2d9e232f7b723d02a76eb88fb6116c0db03646`. The two copied members match the archive bytes exactly:

| Member | Bytes | SHA-256 |
|---|---:|---|
| `experiment.py` | 9128 | `79563f448d916f400ecc22f3461d6d3583c5604100cba6c7c61c705ebf500463` |
| `NUMERICS.md` | 5860 | `7bcd7d3ef3889ba582dea04a062a2c94e9f6fc2f13be4894c14ca8ef4ea7e1ec` |

This agrees with the root receipt. The overview correctly identifies the copied numerical note as historical provenance whose old reproduction commands refer to its original complete package. The new experiment has its own reproduction document.

The tracked first packet has no diff from its stated parent publication commit under `standalone/2026-10-24-fresh-zero-free-routes`. This supports the stated additive scope. A final publication commit/tree review is a separate step from this working-file review.

## 5. Source descriptions and retained limits

The repository source identifiers and artifact hashes are consistent. I checked the relevant primary-source statements for Xu--Sang and Lü--Wang--Wu during the fractional review, and opened the Kohnen and Liu sources during this overview review. Kohnen's title, bibliographic data, and introduction's reference to Wolke agree with the source description. Liu is described as a source-qualified possible input to explicitly conditional statements, not as a framework newly verified by this packet.

The source sheet does not attribute a native coefficient transfer to the determinant conjugacy, does not enlarge the literal prime-moment theorem beyond its canonical squarefree subfamily, and makes no novelty claim for the general fractional-series/zero-order principle. It correctly separates the elementary upper bounds used for the positive integer theorem from the prime number theorem used for its resonance argument.

The review descriptions are also scoped correctly: the reports are independent agent scrutiny of the specified components, not external peer review or formal verification. The imported full moment/detector frameworks remain imports. The decisive all-scale matrix bound, globally positive tight selector family, improved signed marked discrepancy, and sufficiently wide fractional native estimate remain open.

No remote write or publication approval is covered by this report. Its verdict applies to the exact local artifact hashes in Section 1.
