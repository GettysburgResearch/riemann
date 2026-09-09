# Sources, self-audit, and validation — pass 2

Status: author reconstruction and self-audit, NOT independent referee review. No external novelty or priority claim. No RH proof.

## Exact parent and repository state

The live repository resolved from `gfreund123/riemann` to `GettysburgResearch/riemann`, repository ID 1309150028. PR #793 was read at:

    branch research/astra/20260905-three-route-assault
    head   7275b956b278051504da4befeb3b37924f83fd58
    base   6dda8b5125457ed936330229f8c9eb6491728e76
    tree   773e950c5e8d3f969c4eae17b4b8a95f0214a88a

The PR had no review/comment thread when inspected. This is not an approval. Its first-pass publication receipt states that the publisher checked artifact integrity, not the mathematical claims.

The uploaded first-pass ZIP was extracted locally. Its 19 manifest entries were verified and compared with the SHA256SUMS fetched at the exact remote head. The remote manifest blob was `7ab1f400b8e7b57ce1225fd5a9d919610f6e7bb4`. The four consumed proof hashes are:

| Parent proof | SHA-256 |
|---|---|
| R1_SOURCE_DETERMINANT_AND_MARKED_OBSTRUCTION.md | 6a139e4267d1ae58b7ca10d5a27a217707735123a801df6e22d6ed59edb8d71b |
| R2_FIXED_FREQUENCY_AND_SHARP_TRANSPORT.md | 3c8458904a79339d19a97c3d56883fad4489391cf3737cb194a43bc79eb51e4f |
| R3_HORIZONTAL_SURPLUS_IDENTITY.md | 73fc33b65543409a30bc02445cf998c1f492917b3a11375008d114931341fd50 |
| R3_SCREENING_AND_CONDITIONING.md | 6540a2505394c442b99acb3fa15e6be086d880a21433e6cacf4caa80c097c78e |

No parent file, old manifest, canonical registry, integrated theorem, production experiment, or formal-library file is changed. Local claim labels A1--A7, B1--B7, C1--C7, D1--D6 belong only to the named notes in this directory; no global claim ID is allocated or recycled.

## Mathematical dependency ledger

### Standard inputs, not claimed as new

Riemann's completed-zeta normalization and reflection; the theta integral; meromorphic continuation; the even canonical product for Xi; a coarse Riemann--von Mangoldt bound; the classical conditional RH-to-Mertens implication; Euler--Maclaurin with periodic Bernoulli remainder; gamma/polygamma values at 1/2; elementary symmetric functions and Newton identities; finite-dimensional inverse function theorem; trace-class determinant continuity; Laplace/Plancherel theory; and Hardy-space Blaschke multiplication and reproducing kernels.

The notes rederive the particular coefficient, pole, Cauchy, and tail formulas used. Standard general theorems remain imported mathematical inputs, not newly formalized results.

### Primary-source verification and boundary

Checked online on 2026-09-05:

- NIST DLMF 25.2, especially 25.2.4--5 (Stieltjes sign convention), 25.2.8--9 (Euler--Maclaurin), 25.2.11 (Euler product), and 25.2.12 (zero product): https://dlmf.nist.gov/25.2
- NIST DLMF 25.4 (completed xi and reflection): https://dlmf.nist.gov/25.4
- NIST DLMF 25.10 (zero distribution background): https://dlmf.nist.gov/25.10
- NIST DLMF 5.15 (polygamma identities): https://dlmf.nist.gov/5.15
- Masatoshi Suzuki, *Aspects of the screw function corresponding to the Riemann zeta function*, arXiv:2206.03682: https://arxiv.org/abs/2206.03682

DLMF's odd-periodic-Bernoulli remainder and the note's even-periodic-Bernoulli remainder are equivalent integration-by-parts versions. The actual interval bounds are derived explicitly in D5; the code does not trust displayed decimal constants from a website.

The Suzuki record is a literature-boundary reference for the pre-existing Weil/screw/Hilbert positivity programme. No theorem from its abstract is used to discharge the new operator's positivity or to claim novelty. Later related search results were reconnaissance, not additional analytic assumptions. No PDF was analyzed or copied for this pass.

The parent packet retains the earlier PR #785 theta, PR #779 Mobius coarea, and PR #788 Hilbert/pair-correlation receipts. This pass does not rerun those branches or promote their review status. The new noncompact Route-3 metric does not automatically inherit compact-support pair-correlation bounds.

## Self-audit of the load-bearing steps

### Route 1

1. The trace bound alone is NOT trace-norm compactness. A1 retains the escaping exponential; A2 is an exact counterexample; actual xi growth removes that term.
2. The extracted positive operator need not be source-canonical or a compatible compression of prior matrices. Only unmarked scalar determinant existence is proved conditionally on finite approximants.
3. D1 uses the alternating Stieltjes convention and the invariant change of variable, not raw xi derivatives as if they were invariant coefficients.
4. The lower-rank cubic obstruction follows by summing a pointwise cubic inequality. It does not rely on an unverified numerical optimizer.
5. The rank-32 eigenvalues are defined by a unique exact cubic root. Decimal endpoints are rational enclosures, not approximate substitutions.
6. The Bernoulli remainder is differentiated with explicit log-moment bounds; rational outward rounding is used at every numerical operation.
7. Minimal ranks 15 and 32 are finite facts. Neither a general rank-growth law nor an unbounded positive-matrix producer is proved.
8. The finite-sector approximation certificate is a theorem template only; no new xi sector verification was executed.

### Route 2

1. All sums inside the finite-horizon arithmetic formula are finite. Infinite passage uses monotonicity of the original positive integral, not of the signed off-diagonal.
2. The q-free diagonal divides by 1+q^(-s), whereas the reciprocal Mobius series divides by 1-q^(-s). The checker tests the first identity independently by coefficients.
3. Reciprocal-line Plancherel is asserted only when the causal norm is finite. A finite meromorphic boundary integral alone is insufficient; B6 exhibits the anti-causal substitute.
4. B5 applies to any one off-line zero, with its true multiplicity. Infinity is allowed and only a liminf lower bound is claimed, not a rightmost-pole/full-norm asymptotic.
5. The initial absolute-convergence region sigma>1/2 is paid. No new estimate in the RH-sensitive region is obtained by moving a contour across unaccounted poles.

### Route 3

1. Reproducing-kernel phases and the scalar factors s_z are kept in the Cauchy Schur identity; an independent exact matrix elimination checks them.
2. Zeros are counted with multiplicity in the source sum, but projection uses one vector per DISTINCT location. A repeated real zero is not a nonreal defect.
3. The zero-product/Laplace identity sums BOTH signs of Xi zeros. Its factor and the removable r=b value have independent finite checks.
4. Infinite background survival uses the actual Blaschke summability condition from the coarse zero count. It does not assume a uniform lower frame bound or zero spacing.
5. The negative vector is explicit. The omitted-zero trace norm and finite-time error are both paid before declaring a negative full-source test.
6. The original compact-band screening obstruction remains true. The new operator changes the metric and its weights; the old numerical surplus constants are NOT asserted for the new weighted vectors.
7. Source-defined operator existence and complete capture do NOT establish its positivity. The remaining gamma-plus-prime quadratic inequality is RH-strength.
8. The new Route-3 operator's determinant is not identified with invariant xi, and it is not silently substituted for the Route-1 target operator.

## What was actually run

First-pass source: 19/19 manifest entries; 447 exact controls normally and under `-O`; 17 unit/rejection tests normally and under `-O`.

This pass: `source_certificate.py` freshly computes the 15 actual-xi strict interval signs; `verify.py` reconstructs all 640 finite controls, including those same 15 signs; and its 13 unit/rejection tests pass in ordinary and optimized Python. Stored JSON is compared byte-for-byte with fresh output. Acceptance checks use explicit exceptions, so optimized Python does not suppress them.

The arithmetic is exact rational, exact Gaussian rational, or rational outward intervals with the analytic remainder proof in D5. The accepted scripts import only the Python standard library. Small symbolic/high-precision development cross-checks were diagnostic, not the proof certificate. No zeta-zero data is used by the actual-xi rank certificate; the Route-3 computational fixtures are explicitly synthetic finite zero configurations.

The final manifest hashes the proof notes, code, source certificate, and finite-results record. A manifest authenticates bytes, not a mathematical proof. The PR publication receipt/comment carries the final remote head; a tracked file does not self-reference its own commit SHA.

## Not performed or not established

No independent referee review; no Lean build or formal proof; no repository-wide test suite; no broad zero, prime, conductor, or matrix sweep; no actual off-line zeta zero; no improved zero proportion; no all-order positive xi determinant; no new signed Mobius power saving; no prime-side positivity proof for the new Hardy operator; no RH proof.
