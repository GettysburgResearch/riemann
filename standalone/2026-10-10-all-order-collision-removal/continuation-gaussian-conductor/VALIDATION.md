# Scope, sources and actual validation

## 1. Mathematical status

PROOF.md supplies a proposed complete proof of an unconditional component bound for the low product-conductor part of the actual balanced covariance. HORIZON_TRANSFER.md supplies an elementary cutoff adapter and a conditional consequence. No human or independent AI mathematical review, Lean build, whole-repository validation, full OpenAI proof reconstruction, or proof of the remaining moment inequality occurred in this pass.

The load-bearing new statement is PROOF.md Theorem 1.1. Its sensitive point is Lemma 4.1: the exact shared-prime mask lowers the row scale and must be summed before one claims a conductor saving. A wrong primitive Gauss normalization would affect equation (3.3), but the theorem only needs the modulus bound (3.4). The other sensitive adapter is HORIZON_TRANSFER.md Proposition 1.1: positivity is used on full energies, not on individual signed covariance terms.

## 2. Frozen source objects

- Repository: GettysburgResearch/riemann.
- PR: 916, open draft when read.
- Parent/last remotely verified head: `f5c089e33ccce4eae4307d4f6475b9977485cb78`.
- Branch: `research/all-order-collision-removal-20261010`.
- Predecessor source: `standalone/2026-10-10-all-order-collision-removal/continuation-integrated-window/INTEGRATED_CRITERION.md`.
- Predecessor Git blob: `34928b0d8531e8cbe8764edbabb188bcb72d5ff1`.
- AGENTS.md Git blob read at the same head: `c2181ad9ebf037614f3daa8957df640159f8d968`.
- Sibling #919 was inspected at PR metadata level only, head `9b04a887e171b3104a66cf57296ce5b0b2920d78`; it is not a proof dependency.

The new files do not change the earlier source, its status, any integrated result, main, or a sibling branch. These objects were read through the live GitHub connector, not inferred from conversational memory.

## 3. Classical primary references inspected

- Peng Gao and Liangyi Zhao, *Moments and One level density of sextic Hecke L-functions*, arXiv:2201.01885v2 (24 July 2022), HTML https://arxiv.org/html/2201.01885v2. Sections 2.1--2.2 record residue symbols, zero extensions and Gauss sums; Section 2.10 provides the Poisson setting. PROOF.md derives its particular Gaussian normalization and product-character extension directly.
- Alexandre de Faveri, *Optimal large sieve for fixed order characters*, arXiv:2610.04045v1 (2 October 2026), https://arxiv.org/html/2610.04045v1. Abstract/source inspected as current context, but this paper's new large-sieve theorem is NOT used in the component proof.

The component proof attributes classical Gauss/Poisson ingredients. It does not assert priority for those ingredients or independently establish literature novelty of this application.

## 4. Executed exact checks

The checker is Python standard-library-only and uses exact integers and fractions. Sixth roots lie in Z[omega], represented by pairs (a,b); conjugation is (a-b,-b), and squared absolute value is a^2-ab+b^2. There is no floating-point arithmetic in the accepted replay.

### Local residue fields

The checker constructs the two split prime ideals for each of rational primes 7, 13 and 19, as well as the inert residue fields of sizes 25 and 121. Every element and every multiplicative pair in each declared finite field is tested. Complete additive autocorrelations are computed: q-1 at zero shift and -1 at each nonzero shift. These are finite arithmetic checks supporting the Gauss norm mechanism, not a substitute for the general proof.

### Literal row kernels and nonunit masks

All 128 squarefree product columns from the seven prime ideals of norm at most 26 are tested against each other on all 72 nonzero Eisenstein integers with Nu<=19. The checker verifies 16,384 exact shared-prime mask identities and 13,648 exact cross-unit-sector zero identities.

It also finds literal counterexamples to erasing the common-prime mask and to erasing the dilation character phase. The examples are retained in result.json. Their product-mask indexing is determined by the checker rather than an undocumented random model.

### Exact integrated source panels

The step window W=1_[1,2] is declared explicitly. The factor ideals are enumerated independently in two ways: complete primary lattice enumeration followed by factorization, and complete norm-bounded prime-subset enumeration. These agree.

The panels use k=2,3,4, horizons D=25,13,13, and complete rows Nu<=100. Their scale exponents 2k sigma are the integers 3,4,5, respectively. All contributing ordered coprime allocations are included. Every scale breakpoint is rational. The integrals are evaluated exactly using (x^(-p)-y^(-p))/p on each interval, not numerical quadrature. Direct nonnegative energies equal diagonal plus the signed conductor-split covariance in every panel.

These tests do not purport to evaluate the predecessor's infinite-convolution smooth window W_* or an infinite Gaussian row sum. The analytic proofs, not the tests, justify those objects.

### Results

Both commands succeed and produce byte-identical stdout:

```sh
python -I -S -B check_eisenstein_covariance.py --write result.json
python -I -S -B -O check_eisenstein_covariance.py --check result.json
```

Each execution passes **48,427 explicit predicates**. Predicates are guarded by explicit exceptions, not Python assertions, so optimized execution retains them.

The separate negative-control runner actually executes three mutated checker sources in each mode:

1. erase shared-prime inclusion-exclusion;
2. erase its dilation character phase;
3. use the wrong quadratic-field conjugation.

Each exits nonzero at its intended named arithmetic predicate, not at a syntax or import error. In addition, a tampered recorded predicate count is rejected after full reconstruction in each mode: eight executed refusals in total. negative_controls.json records the checks.

During development, a missing bracket and a tuple-versus-JSON-list comparison were corrected before the retained passing runs. These were implementation defects, not mathematical counterexamples. The accepted checker canonicalizes its result to JSON types before exact comparison.

## 5. Publication boundary

This session discovered all 48 currently available GitHub actions; none writes files, commits, refs or comments. A plugin search resolved only the already installed hybrid GitHub connector. The terminal's actual read attempt

    git ls-remote https://github.com/GettysburgResearch/riemann.git \
       refs/heads/research/all-order-collision-removal-20261010

failed with exit code 128 and `Could not resolve host: github.com`. No credential was printed or requested, no write workaround bypassing permissions was attempted, and no remote commit/branch/PR was created in this pass.

An add-only patch is packaged against the named parent. Applying it in a clean local Git fixture tests syntax and added-file bytes only; it is not a clone of the whole repository or a remote integration check. The outer PUBLICATION.md records that fixture result and guarded publication instructions.
