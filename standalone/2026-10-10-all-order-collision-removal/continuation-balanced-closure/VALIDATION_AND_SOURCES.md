# Validation, source scope, and publication record

## Preservation and actual first publication

Repository: GettysburgResearch/riemann. Draft PR: #916. Branch: `research/all-order-collision-removal-20261010`. Stacked base: PR #910 at `670a76c1a3a8f325c43c1755b1cfc24d313a3e3c`.

The original eight files were published unchanged at commit `dabd6da99fb92eead7c99f941331ed9cbd2ec4ad`, root tree `0cea9b7a34919844f213ede4385515f4b0c36c4f`. The original packet's failed-push statements describe its previous authoring session. They are not edited away. The successful GitHub branch creation and PR response establish the later publication; the PR body records the distinction.

This continuation is intended as an add-only child of that published commit. Its actual child commit is identified by the PR history and publication comment, rather than a self-referential SHA inside a file. No change to main or a sibling branch is requested.

## Fresh executable replay

From the original packet directory, the original SHA-256 manifest passes. Both commands below reconstruct the original result, and their stdout is byte-for-byte identical:

    python -I -S -B checks/check_all_order.py --check results/exact_checks.json
    python -O -I -S -B checks/check_all_order.py --check results/exact_checks.json

They execute 50,357 successful exact predicates and reject four deliberate algebraic errors per mode. Those counts belong to the original checker, not to the new proof.

From this continuation directory:

    python -I -S -B check_balanced.py --output exact_checks.json
    python -O -I -S -B check_balanced.py --check exact_checks.json

Both exit 0 with byte-identical stdout. Each mode executes **2,032 successful exact predicates** and rejects **three deliberate algebraic errors**. A separate tampering run increments the retained successful-predicate count; optimized full reconstruction rejects that file with exit status 1 and `FAIL: Recorded result differs from exact reconstruction`. The original result is unchanged.

The new checker first authenticates the exact bytes of its original local algebra dependency, SHA-256 `8e5b599ec43662f6fc634e8339228f79c33b37f8385e55c30d34cb136edfc4d9`. It then uses exact integer, Fraction and Q(zeta_6) arithmetic. No removable assert statement is used for acceptance.

Coverage includes local contraction inequalities at 152 rational arguments, 95 cutoff budgets, nine balanced-envelope panels, 114 unequal-length comparisons, 84 finite-prime reinsertions, 319 comparisons with independently enumerated primitive rotation-orbit counts, a separate truncated cyclotomic product reconstruction, and exact defect/threshold fractions. There are 1,183 primitive rotation orbits in the independently enumerated word fixtures.

The finite envelope fixtures use a two-prime free ideal monoid of norms 7 and 13, a finite downward-closed scale set, rational compact weights, structural sixth-root phases including zeros, and three row measures. They are not samples of the actual full Hecke/sextic row family. Their rational weights are not the smooth analytic tests. Their sigma=1 and finite primes test the operator identities without asserting the conservative infinite-prime cutoff is satisfied by those fixture primes.

## What the checks do not prove

The finite tests do not establish the analytic prime-tail bound, the all-scale absorption theorem, absolute convergence of the multivariate remainder, or the moment-to-zero implications. Those rely on the written mathematical proofs. No independent mathematical review, human peer review, Lean formalization/build, complete upstream reconstruction, or whole-repository validation was performed in this continuation.

No actual new higher moment or zero-free boundary is established. The fractional-defect arithmetic hypothesis remains unproved. Source-conditioned baselines are distinguished from the unconditional norm comparison throughout.

## Inspected sources and exact coverage

1. PR #910, frozen at `670a76c1a3a8f325c43c1755b1cfc24d313a3e3c`: live PR metadata and AGENTS.md (blob `c2181ad9ebf037614f3daa8957df640159f8d968`) were read. Its fourth-moment and extraction definitions are preserved in the original packet's source ledger. The complete imported OpenAI analytic proof was not reaudited.
2. This branch's original PROOF.md and MOMENT_FRONTIER.md: full contents used. Their exact files and original executable dependency were checked against the retained packet. The new inverse identity and the extraction reference point to those precise source objects.
3. Sibling PR #913, `6498d6cc2eded03159c7332b25fd224ad07f89c1`: live PR metadata and its `standalone/2026-10-10-sextic-moment-descent/README.md` were read. Its stated all-row sieve and conductor-uniform weaker moment are used only as expressly labeled comparison/imported baselines. No new independent audit of their complete proof is claimed.
4. Sibling PR #915, `9959364671f89b86f3992ec5ed5e19f804eb607b`: live PR metadata was read to avoid overwriting related work. Its coupled theta/Euler component proofs were not imported or independently reviewed here. The coloured Möbius Dirichlet series in the new note is not identified with that sibling's completed theta series.
5. D. Blessenohl and H. Laue, *Algebraic combinatorics related to the free Lie algebra*, Section 1, printed page 3: the multivariate Witt formula and primitive-word interpretation were checked in parsed text and the page image. URL: https://radon.mat.univie.ac.at/~slc/s/s29laue.pdf . Only the relevant statement was inspected, not the entire article. The identity is classical and is reproved locally; external novelty is not claimed.

The comparison literature on higher-order character sieves (Blomer-Goldmakher-Louvel, arXiv:1112.1650) is not a dependency of balanced closure or cycle factorization. It is not used to silently claim a new bound for long balanced columns.

## Load-bearing review points

- BALANCED_CLOSURE.md Lemma 2.1: explicit cutoff and absolute inverse-tail mass; fixed before scales.
- Theorem 3.1: finite-envelope absorption, with exact zero masks and the same row measure at all scales.
- Theorem 4.1 and Section 5: fixed-prime reinsertion, epsilon allocation, and full-row quantifiers; no inference from the shorter-row curve.
- CYCLE_FACTORIZATION.md Theorem 2.1: literal character-power presentations and nonvanishing remainder domain; no confusion between a product-norm diagonal and balanced factor windows.
- DEFECT_BOOTSTRAP.md Proposition 2.1: the reusable fractional improvement is an explicit new premise at every updated common boundary, not a derived theorem.

The only new analytic premise needed for the advertised moment improvement is still an unproved arithmetic estimate: BALANCED_CLOSURE.md (4.3). The reduction and the conditional endpoint calculations must not be relabeled as its proof.
