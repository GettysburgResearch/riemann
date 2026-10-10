# Validation and review record

Date: 10 October 2026. Runtime for the new local diagnostic: Python 3.12.14.

The packet contains analytic arguments, exact finite arithmetic diagnostics, and preserved source material. These have different evidence scopes. No finite calculation is used to establish an infinite moment estimate or a zero-free region.

## Mathematical review

The [independent review](INDEPENDENT_CRITICAL_CORE_REVIEW.md) records the exact content hashes and review roles. The coupled completion, its standard-cusp improvement, the negative-branch quotient, reunited Euler product, anisotropic moment portion, polynomial horizon and replicated-spike arguments were read by an agent distinct from their respective authors. The full scalar calculation and high-value note were independently reviewed by another agent; their author does not count as their independent reviewer.

The parent agent also read the proofs and checked their main normalizations, local factors, exponent conversions and scope. The README's divisor-bounded outer multiplier corollary was independently checked against the two component-bound proofs. This is AI-agent mathematical review, not external peer review or proof-assistant verification.

Substantive issues found during review were repaired before the recorded bindings: the negative Ramanujan term permits overlaps with the theta index; repeated character squares retain nonunit masks; reflected bad-prime theta factors must remain in the every-cusp result; the angular factor cannot be hidden in a finite-order twist; and a fixed-index Euler product cannot silently replace the full deformed theta sum. Editorial formula and source-path corrections were also made before binding.

## Exact local arithmetic diagnostic

The [checker](checks/check_local_identities.py) and [saved output](results/local_identity_checks.json) use exact integer arithmetic in explicit finite fields and cyclotomic rings. No floating-point tolerance is used.

| Check class | Counted predicates |
| --- | ---: |
| Finite-field character multiplicativity | 1,584 |
| Cubic and quadratic Gauss products | 14 |
| Full-residue Fourier inversion | 206 |
| Mixed local reflection, exponents 1 and 4 | 1,236 |
| Ramanujan allocations and retained row masks | 272 |
| Moving Euler coefficients for two through six axes | 10,912 |
| **Total** | **14,224** |

The fixtures are both split residue embeddings over each of 7, 13 and 19, and the inert field of norm 25. Each local reflection checks every frequency residue for the explicitly listed finite choices of its other unit parameters. The Euler check covers local exponent vectors from zero through three. Additional field preconditions and inverse identities are also enforced.

The author ran the checker in normal and optimized Python. The independent reviewer read it, repeated both runs, and compared their JSON outputs with the saved result byte for byte. All runs passed. Acceptance gates use explicit exceptions, so optimized Python does not disable them. A temporary corrupted local Ramanujan factor was rejected by the reviewer in both modes without producing a passing output.

To reproduce from this directory, run Python on checks/check_local_identities.py with the argument --output results/local_identity_checks.json. The saved JSON records the checker SHA-256. Optimized Python with the same arguments gives identical JSON.

This diagnostic does not verify the global Gauss/angle normalization, an arbitrary-conductor CRT theorem, theta automorphy, a large sieve, meromorphic continuation, or any infinite moment theorem. Those steps are mathematical arguments or explicitly retained source inputs.

## Source identity and literature matching

All twelve adjacent source snapshots were independently compared with the Git objects at the exact #911 and #912 commits. Their original bytes, Git blob identifiers and SHA-256 values agree with [the snapshot manifest](adjacent-sources/MANIFEST.json). Original relative links inside the unmodified copies retain their source-tree meaning.

[SOURCE_LOCK.json](SOURCE_LOCK.json) records the exact parent commit, imported OpenAI commit, and the three load-bearing upstream files used or compared in this pass. The October 5 manuscript remains at the same imported bytes. The two family 023 files were checked against their pinned Git objects, including the actual background-type1.tex path.

The primary-source comparison checks the coefficient and uniformity hypotheses of the cited results. It establishes no direct matching theorem for the deformed outer Gauss series among the examined sources. The existing periodic-theta machinery remains a possible building block, with its hypotheses attached.

## Repository and publication scope

The intended payload consists of this new standalone directory and a navigation section in the root README. Earlier research packets and the external import are unchanged. The file manifest binds every packet file except itself.

Before publication, the packet is checked for manifest consistency, review bindings, JSON validity, internal links outside unchanged source snapshots, unexpected control characters, whitespace errors and unintended staged paths. The GitHub tree is then compared with the exact locally staged tree, and its commit parent and published files are verified. The PR and accompanying delivery message identify the resulting immutable commit.

The full fourth moment at near-linear arithmetic row length, the general moment hierarchy, the proposed \(17/24\) boundary and a shrinking zero band are not established here. No Lean build or zero-search computation was performed for this packet.
