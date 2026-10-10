# Exact published-commit seal: amplification reviews

**Reviewer:** research subagent \(\texttt{/root/amplification}\).

**Date:** 2026-10-10.

**Verdict:** IDENTITY SEAL PASS. I explicitly extend only the prior scoped PASS verdicts identified below to the unchanged files at the exact published source commit. This is an identity and provenance extension of completed reviews, not a new theorem, a repeated computation, or a blanket approval of the repository.

## 1. Published source identity

- Repository: GettysburgResearch/riemann.
- Draft pull request: [#926](https://github.com/GettysburgResearch/riemann/pull/926).
- Exact source commit: [a0a31c4f9775c5516a78d5c9eb69088b9c83595a](https://github.com/GettysburgResearch/riemann/commit/a0a31c4f9775c5516a78d5c9eb69088b9c83595a).
- Source tree: 5082fe79296a9d701bef4e8e88691b80e818cb33.
- Sole source parent: 6b4723042b3d250024eef45cb1924f88f28e902c.
- Exact packet prefix: standalone/2026-10-10-mobius-overlaps-and-sampled-moments/.

I fetched the Git commit object through the GitHub connector at the exact commit identifier. Its returned commit, tree, and parent fields match the identities above. I did not substitute a branch name, the current default branch, or a later pull-request head for this source commit.

## 2. What was fetched and how identity was checked

I fetched all seven requested proof, summary, checker, and result files from the exact repository paths at the exact commit, requesting the complete base64 content. I also fetched the four published copies of my existing review reports so the review links themselves are authenticated.

For each of these eleven files, I independently decoded the returned base64 and computed:

\[
\operatorname{SHA256}(\text{raw bytes})
\]

and the ordinary Git blob identifier

\[
\operatorname{SHA1}\bigl(
\texttt{blob } \Vert
\operatorname{decimal}(\text{byte length})\Vert
\texttt{NUL}\Vert
\text{raw bytes}
\bigr).
\]

No line endings, Unicode text, final newlines, or whitespace were normalized. The recomputed Git blob identifier was required to equal the blob identifier returned by GitHub. The SHA-256 was required to equal the exact identity in my existing review, and the fetched bytes were also compared directly with the retained reviewed or independently replayed local bytes.

All eleven comparisons passed. The remote content was processed in memory; no frozen packet file or previous receipt was modified. This task created only this new sealing receipt.

## 3. The sealed proof, summary, checker, and result files

The prefix in Section 1 and the relative paths below together specify each exact repository path. Every link is pinned to the source commit in Section 1.

| Exact path relative to the packet prefix | Bytes | SHA-256 | Git blob SHA-1 |
| --- | ---: | --- | --- |
| [QUADRATIC_INVERSE_PRODUCTS.md](https://github.com/GettysburgResearch/riemann/blob/a0a31c4f9775c5516a78d5c9eb69088b9c83595a/standalone/2026-10-10-mobius-overlaps-and-sampled-moments/QUADRATIC_INVERSE_PRODUCTS.md) | 15001 | 7cc4f91049d6e8b22a24080099a2947e4f30d5be68ea050bb7bcdf52a94c0696 | efd637c097693a45ba09a74cc544f28db59b80df |
| [JOINT_REFLECTED_BLOCKS.md](https://github.com/GettysburgResearch/riemann/blob/a0a31c4f9775c5516a78d5c9eb69088b9c83595a/standalone/2026-10-10-mobius-overlaps-and-sampled-moments/JOINT_REFLECTED_BLOCKS.md) | 37494 | c75be63f43de6efb0d9f820da008f256afc53351fdbfe38870f9e97207955bd5 | 626c3c7fea879065f8a41891d5e0a25ab0e15aa1 |
| [README.md](https://github.com/GettysburgResearch/riemann/blob/a0a31c4f9775c5516a78d5c9eb69088b9c83595a/standalone/2026-10-10-mobius-overlaps-and-sampled-moments/README.md) | 16403 | 63dc04d705bade6c4a3d7714ac82dfee9bfe96da4bbe1bce2ff646c4e6772cf3 | 5125b610fc06d1607b66acc385190d9352b34903 |
| [checks/check_quadratic_masks.py](https://github.com/GettysburgResearch/riemann/blob/a0a31c4f9775c5516a78d5c9eb69088b9c83595a/standalone/2026-10-10-mobius-overlaps-and-sampled-moments/checks/check_quadratic_masks.py) | 6768 | 622af30d6efd58eea1703b329799a9c6812568c12296e36d1d71eed682584ad0 | e6777a216089bae8e5b490d4e3a029f6479dbb6a |
| [results/quadratic_masks.json](https://github.com/GettysburgResearch/riemann/blob/a0a31c4f9775c5516a78d5c9eb69088b9c83595a/standalone/2026-10-10-mobius-overlaps-and-sampled-moments/results/quadratic_masks.json) | 1545 | 11abaa05d4e6399ee04f206632af0ca498c84a6fc655106c39e7674d70c30cfe | 48e3a9a94c1353d16732a3862ce9f793755c35f4 |
| [checks/check_reflected_blocks.py](https://github.com/GettysburgResearch/riemann/blob/a0a31c4f9775c5516a78d5c9eb69088b9c83595a/standalone/2026-10-10-mobius-overlaps-and-sampled-moments/checks/check_reflected_blocks.py) | 19678 | f156b99c452f514b0bcf0ae4913d8becb24a64612746d06a5e0143ccb8027266 | 1eef8195a803117c15fef086fc6b9c06d65c9ac3 |
| [results/reflected_blocks.json](https://github.com/GettysburgResearch/riemann/blob/a0a31c4f9775c5516a78d5c9eb69088b9c83595a/standalone/2026-10-10-mobius-overlaps-and-sampled-moments/results/reflected_blocks.json) | 7498 | 19ec6c46f7bcda904b4f3efb549d731c780b203f448a6125774dbb39bc0870bb | 69d4b01d5d16797706cee664e4cae2e72716a5f7 |

The quadratic result is byte-identical to the previously produced independent normal and optimized replay outputs. Those executions passed 35,737 exact finite predicates. The reflected result is byte-identical to the corresponding independent normal and optimized replay outputs, which passed 302,676 exact finite predicates.

Those computations were not rerun for this sealing task: both executable source files and both output files are unchanged, and their original executions and strict acceptance rules are recorded in the reviews linked below. Renaming the files into the packet did not change their bytes.

## 4. Existing scoped reports, fetched unchanged at the same commit

| Exact path relative to the packet prefix | Bytes | SHA-256 | Git blob SHA-1 |
| --- | ---: | --- | --- |
| [reviews/quadratic_review.md](https://github.com/GettysburgResearch/riemann/blob/a0a31c4f9775c5516a78d5c9eb69088b9c83595a/standalone/2026-10-10-mobius-overlaps-and-sampled-moments/reviews/quadratic_review.md) | 12234 | ff516d0bb256b00bed79921c38e79bc3c128c381bcdc1a8e5d4f38bb4afa841c | ac4328623b230c9752c7dd77402bebc2bb504e3b |
| [reviews/reflected_blocks_review.md](https://github.com/GettysburgResearch/riemann/blob/a0a31c4f9775c5516a78d5c9eb69088b9c83595a/standalone/2026-10-10-mobius-overlaps-and-sampled-moments/reviews/reflected_blocks_review.md) | 14802 | cca571ec0ab061e2197b435b6568a97868f5b5f1e9ee91fa65e25455197a320b | 22014baaf4efdea1a2a8430c038ef6fbcacb27b7 |
| [reviews/reflected_checker_review.md](https://github.com/GettysburgResearch/riemann/blob/a0a31c4f9775c5516a78d5c9eb69088b9c83595a/standalone/2026-10-10-mobius-overlaps-and-sampled-moments/reviews/reflected_checker_review.md) | 6608 | 242d31d330ea81c321439d19865ab2e7a30d0e8e9f3886878dc7a099a8a84358 | 32da298978597f76d077e6bfcf79a2463086dbe0 |
| [reviews/readme_review.md](https://github.com/GettysburgResearch/riemann/blob/a0a31c4f9775c5516a78d5c9eb69088b9c83595a/standalone/2026-10-10-mobius-overlaps-and-sampled-moments/reviews/readme_review.md) | 7627 | fb829d38b22128b71c2d9b24aba3146ac46dc9504de6fc0562f5a08877a08762 | 218b4304b51018517c4403463b051b3978f6c1da |

The four linked reports contain the original mathematical reconstructions, replay commands, finite coverage, assumptions, and limitations. Their content was not rewritten to make this exact-commit association. The historical review record is retained.

## 5. Explicit extension of the prior verdicts

### Quadratic inverse products

I extend the scoped PASS in [quadratic_review.md](https://github.com/GettysburgResearch/riemann/blob/a0a31c4f9775c5516a78d5c9eb69088b9c83595a/standalone/2026-10-10-mobius-overlaps-and-sampled-moments/reviews/quadratic_review.md) to QUADRATIC_INVERSE_PRODUCTS.md at source commit a0a31c4f9775c5516a78d5c9eb69088b9c83595a.

This covers the Perron sharp-interval deduction under the stated reciprocal premise, the physical product grouping on squarefree rows, the all-row square-part interpolation, and the stated degree-three interface. It retains the imported quadratic large sieve and the explicit uniform pointwise or reciprocal-L assumptions. The separate conditional numerical use of exponent \(7/8\) is not independently certified.

The same report's finite checker verdict extends to checks/check_quadratic_masks.py and results/quadratic_masks.json at that commit. The finite diagnostics remain finite diagnostics.

### Joint reflected blocks

I extend the scoped PASS in [reflected_blocks_review.md](https://github.com/GettysburgResearch/riemann/blob/a0a31c4f9775c5516a78d5c9eb69088b9c83595a/standalone/2026-10-10-mobius-overlaps-and-sampled-moments/reviews/reflected_blocks_review.md) to JOINT_REFLECTED_BLOCKS.md at the same exact commit.

This covers the trilinear squarefree-row deduction and its explicitly source-qualified physical applications, including the local Euler interpolation and all-row summation. The all-row physical theorem remains restricted to the fixed cube dyad and fixed smooth profile on a compact positive annulus of the actual transformed-weight ratio. Its reflected length shortens with the square part of the row. It is not an arbitrary-coefficient all-row theorem at a fixed column length, nor a bound for the sum of all small-ratio components.

The scoped finite PASS in [reflected_checker_review.md](https://github.com/GettysburgResearch/riemann/blob/a0a31c4f9775c5516a78d5c9eb69088b9c83595a/standalone/2026-10-10-mobius-overlaps-and-sampled-moments/reviews/reflected_checker_review.md) extends to checks/check_reflected_blocks.py and results/reflected_blocks.json at this commit. Its selected prime-ideal panels, finite row masks, valuation range, and exponent tests are exactly those already reviewed.

### Packet README and the sampled small-gcd target

I extend the scoped PASS in [readme_review.md](https://github.com/GettysburgResearch/riemann/blob/a0a31c4f9775c5516a78d5c9eb69088b9c83595a/standalone/2026-10-10-mobius-overlaps-and-sampled-moments/reviews/readme_review.md) to the packet README.md at the same exact commit.

This includes the validity of its Section 6 sufficient target. Under the stated pointwise premise, a sampled diagonal bound for the remaining small-gcd polynomial, combined with the proved large-gcd bound and the positive inequality for the two polynomial pieces, would give the full sampled fourth moment. Interpolation is then applied to the original smooth fixed-row \(A_u\), with the common lower row budget. The small-gcd arithmetic estimate remains open. The conditional limit as \(h\downarrow1\) concerns the open half-plane \(\Re s>17/24\), not its boundary line.

## 6. Authorship and independence boundaries

I am a nonauthor reviewer of QUADRATIC_INVERSE_PRODUCTS.md, JOINT_REFLECTED_BLOCKS.md, the two checkers sealed here, and the root-authored README. The detailed reports identify the corresponding review scope.

I authored SAMPLED_MOMENT_CRITERION.md and its sampling diagnostic during this collaboration. This receipt does not extend a nonauthor verdict to those authored objects. My README review expressly distinguishes checking the root's new sufficient-target composition and summary from an independent review of my own sampling proof.

This receipt also does not extend a full independent verdict to MOBIUS_OVERLAP_TAILS.md. The README review checked the relevant summaries and composition against that proof, including the grouped cubic additions; its complete nonauthor review belongs to the separately designated reviewer. No other packet source, review, manifest, release script, or later commit is silently included in the present verdict.

## 7. Unchanged assumptions and remaining limitations

The displayed classical quadratic and cubic sieves remain imported analytic inputs. The physical theta applications retain the pinned reflection, support, all-cusp coefficient, active-conductor, and bad-row adapters. The angular comparison retains its separate reciprocal input. This sealing operation does not reprove any of those sources or independently validate the imported \(7/8\) premise.

The exact finite computations do not establish an analytic large sieve, infinite Euler-product convergence, theta automorphy, an infinite moment estimate, or zero absence. The all-row reflected improvement controls its specified component; the long, small-cube frequency terms and the needed moving-auxiliary moment interface remain outside the proved result.

The full short-row fourth moment, generalized diagonal moment hierarchy, and RH remain unproved. The sampled small-gcd arithmetic target and the surviving singleton cancellation problem remain substantive gaps. No human acceptance, formal proof-assistant validation, external novelty, or blanket repository approval is asserted.

**Blockers found in this identity-sealing task:** none.

**Signed:** \(\texttt{/root/amplification}\), independent reviewer within the scopes above, 2026-10-10.

