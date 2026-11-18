# Rational-inner / finite auxiliary boundary campaign checkpoint

Date/cutoff:2026-11-17. Task: investigate finite products of projection-valued Blaschke factors, establish a physically realized selfadjoint model, and derive a finite counting cost. The director then proposed the arbitraryHermitianΩ,G generalization, which is now proved in the campaign.

## Main mathematical output

`proposals/independent_campaigns/factored_inner_round2.md` supplies all details.

- Factored class: S=C∏(I−Pj+bjPj), bj=(k−dj−iaj)/(k−dj+iaj),aj>0; total degreeM=ΣrankPj. Positive phase velocity holds despite noncommuting projections.
- Exact positive-root count uses right-continuous fractional eigenphasesF∈[0,E), retainsF(0), includesK and excludes0.
- Asymmetric curvature: **−3E−2M<ΔN<3E+M**. Therefore positive Riemann–vonMangoldt target curvature forces **3E_K+M_K≥Klog2/π−6ε_K K−O(logK)** for three-height error≤ε_K K.
- Explicit matrix-cascade full-domain realization on edgeL2⊕C^M: boundaryη−C*ξ=Gq, action(-if′,Ωq+iG*μ). Ω off-diagonal signs make the real-energy elimination matrix upper triangular with nonzero complex diagonal. No real center is divided away, and the cascade has no dark modes.
- Stronger general theorem: arbitrary finite HermitianΩ and arbitraryG in the same boundary model are selfadjoint/compact. DarkspaceD=⊕λ(ker(Ω−λ)∩kerG) reduces the operator. VisibleA=Ωv−iGv*Gv/2 has strictly lower poles. Transfer derivativeGvR*RGv* is positive; determinant phase budget2πMv plus at mostMd dark levels gives the same bound with totalM, without minimality assumptions.
- Correct treatment of zero modes, dark/visible coincident multiplicities, real-pole removability after dark decomposition, and full-domain density.

## Negative controls retained

1. Inverse scalar Blaschke factor is unitary onR but has opposite phase velocity. With length1,width1/2 the total velocity at its center is−3. Arbitrary real-axis unitarity does not imply the theorem.
2. Scalarγ0 leaves a dark auxiliary level omitted by the reduced secular equation. γ≠0 matters in the original scalar realization; the general theorem restores dark counts explicitly.
3. At k=d the original scalar eigenvalue survives exactly when exp(idℓ)=−1. Elimination by division(k−d) would lose it.
4. Coupled scalar/reference periodic⊕[d] common domains requirez=0, so their intersection is nondense. The earlier dense-common-S interlacing theorem cannot remove the auxiliaryM cost. General domain intersections similarly imposeGq=0.
5. One port/rankG1 can support two visible auxiliary states. Auxiliary phase degree is not bounded by rankG or edge count.

## Source reading and exact provenance

- **PAPER-D301:** Alpay–Jorgensen–Lewkowicz, arXiv1410.0283v2 (revision2015-01-04); OpusculaMathematica36(6)(2016),695–716, DOI10.7494/OpMath.2016.36.6.695. Actual primary readings: conventions, Theorem2.1/proofpp5–6, Theorem3.1/proof and cancellation remarkspp10–11. Full19-page preprint not read/audited; whole-paperL0, substantive_reading=false.
- **PAPER-D302:** Tabak–Mabuchi, arXiv1510.08942v2(revision2016-03-02); EPJQuantumTechnology3,article3(2016), DOI10.1140/epjqt/s40507-016-0041-9. Actual primary readings: passive preliminaries, §5equations15–20pp6–7, §9equations39–43p18. Full26-page preprint, simulations and all appendix factorization prerequisites not audited; whole-paperL0, substantive_reading=false.

Version histories were inspected on primary arXiv landings; journal identities/dates verified via Crossref and publisher-indexed metadata. Publisher pages were unavailable via the web reader; preprint/journal numbering was not assumed identical. PDF internal compilation dates differ from arXiv revisions; no new author version is inferred from recompilation. The original Potapov1950s papers were not read. No literature novelty claim is made.

Private PDFs/HTML/full extracted text are under `sources/inner_round2`; source_manifest.jsonl records exact hashes and versioned URLs. Do not distribute source PDFs/full text by default.

## Files and validation

- `papers/PAPER-D301.md`, `PAPER-D302.md`, `papers/inner_round2_records.jsonl`:2 targeted source records; **zero** completed whole-paperL1s.
- `theorems/inner_round2.jsonl`:8 nodes, separating source context, independently reconstructed theorems, conditional model consequence and negative controls.
- `connections/inner_round2.jsonl`:2 precise connections, including failed dense-common-S hypothesis matching.
- `experiments/code/factored_inner_round2.py`: standard-library exact Gaussian rationals, no floating point in its checked identities.
- `experiments/results/factored_inner_round2.json`: passed noncommutingE2/M3 cascade at29rationalenergies, arbitraryHermitianΩ,G, resonance centers, dark-real-pole removal and one-port/two-state model. Also exact wrong-half-plane velocity−3.
- `scripts/inner_round2_records.py`:rebuilds source records from private hashes.

The parent independently reviewed positive phase/cost algebra, the entire matrix-cascade domain/compactness/elimination proof, and general dark/visible transfer identities. Child supplied independent derivations and exact tests. Separate third reconstruction is pending. Finite checks supplement the full all-energy proof, not establish it.

## Continuation

1. Third reviewer should check maximal adjoint domain using independent endpoint averages and q, the Ω off-diagonal signs/cascade ordering, darkspace maximality and all-real invertibility, detphase with Jordan multiplicity, and counts at dark/visible coincidences and0.
2. Search prior spectral-counting literature for these exact inequalities before assigning novelty. Source passive realization/factorization theory is established background.
3. For any actual RH spectral proposal, identifyΩ,G,E,M and its full fixed domain, including dark levels. Then evaluate the stated three-height cost. Do not substitute an arbitrary unitaryS(k).
4. If considering infinite products, singular inner factors or infinitely many auxiliary states, specify convergence, compactness and an explicit replacement for finite phase budgetM. No result for that class was established here.
5. No zeta-zero location theorem, zero-count approximation construction, or classical RH proof resulted from this campaign.
