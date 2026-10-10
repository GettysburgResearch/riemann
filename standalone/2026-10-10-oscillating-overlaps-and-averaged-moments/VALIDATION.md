# Validation and reproducible finite evidence

All three checkers use Python's standard library and exact integer or rational arithmetic. Every acceptance predicate raises an explicit exception on failure; no Python `assert` statement remains in the released checker sources. Optimized execution therefore retains the checks. The runtime used for the recorded executions was Python 3.12.14.

These checkers authenticate the stated finite algebra, primitive finite-field normalizations, and explicit exponent certificates. They do not prove a large-sieve theorem by sampling, estimate the infinite moment, authenticate theta automorphy, or prove a zero-free half-plane.

## 1. Operator algebra and actual ideal counts

[verify_operators.py](checks/verify_operators.py) performs **5,988 exact predicates**. It enumerates all **311 Eisenstein ideals of norm at most 512**, using the six-unit orbits of lattice points. At each individual norm it independently checks the count against rational-prime factorization of the ideal zeta coefficients.

It then checks:

- The actual split prime ideals `(7, omega-2)` and `(13, omega-3)`, including invariance of divisibility under all six units.
- Exact radical-divisibility counts at 11 base cutoffs and all exponent pairs from 0 through 4.
- The coefficients of the finite averaged mask operator against those directly counted bases.
- The explicit local inverse through exponent 16, for prime norms 3, 7, 13 and 19, with all six unit phases and the zero value.
- Hermitian symmetry and exact principal minors of three-mode Gram matrices over the actual finite base sets.

The Gram fixture uses the two specified local prime responses, equivalently setting eta to zero at every other prime. It is not a computation of all Euler factors for a fixed Hecke character. Its exact positive definiteness for the tested ranges is finite evidence for the local mechanism only.

The root ran the checker normally. A second agent inspected its source and independently ran normal and optimized Python; both captured outputs agree byte for byte. The reviewed source has SHA-256

`da375b646729871e48130d9179b2153e97f3735502d60b274c1c170385e40332`.

The recorded [operators.json](results/operators.json) has SHA-256

`9a5ed4b551e6ed1d3c35d7c8dbf6ae16bd3dadf627bc32bd56814d5ef485b13d`.

See the [independent checker review](reviews/operator_checker_review.md).

## 2. Primitive theta phases and Ramanujan factors

[verify_theta.py](checks/verify_theta.py) performs **2,122 exact predicates**. Its prime ideals have the primary generators `-2-3 omega` and `1-3 omega`, of norms 7 and 13, with omega residues 4 and 9. These are the conjugate prime choices to those in the operator fixture; each check uses its own stated embedding consistently.

The additive character is fixed from the source convention. For a denominator `a+b omega` of norm q, an integer representative t has additive phase `exp(2 pi i (-b)t/q)`. Gauss sums are evaluated as integer vectors modulo the exact cyclotomic polynomials of orders 42, 78 and 546. Thus the normalization test is a primitive finite computation rather than a test of already simplified derived formulas.

The raw products G_2 G_4 are exactly 7, 13 and 91. The composite CRT phase is zeta_6^4, which is nontrivial; omitting it fails an explicit predicate. Complete residue-system tests cover Ramanujan sums and their squared energies. Further predicates cover every local exponent, active and inactive sixth-power cases, denominator scaling, the quadratic divisor mask, and the reciprocal Euler correction through degree 12.

The author's optimized run and the root's independent normal run agree byte for byte. The source has SHA-256

`aabf77a3f75f4a0ce7dc6af5784e2dda93804fa8089f02147d21344388d2c7f5`.

The recorded [theta.json](results/theta.json) has SHA-256

`3b0d17f7f6dd369668559c179e26babf6642a5b8b316cfc1a16ade2243edd619`.

The [execution record](reviews/theta_execution.md) gives the complete fixture and canonical source identity. The imported automorphy theorem and infinite contour shifts were not independently rebuilt by this computation.

## 3. Cubic overlap certificates and exact incidence coverage

[verify_overlaps.py](checks/verify_overlaps.py) first verifies symbolic nonnegative-monomial certificates on both branches of `max(A,B)`, and exact rational affine budgets at the endpoints of the stated parameter intervals. Because those expressions are affine or monomials with nonnegative powers, these particular checks certify their whole displayed real parameter domains; they are not fitted samples.

The checker exhausts **415,325 candidate designated divisors** over every factor tuple and every index subset of size at least two in the following finite models:

| Number of formal primes | Polynomial degree |
|---:|---:|
| 3 | 2 |
| 3 | 3 |
| 3 | 4 |
| 2 | 5 |
| 2 | 6 |

For each eligible decomposition it independently reconstructs the complete prime multiplicity vector and zero support. The degree-six panel includes positive sixth-power phases with a nonunit zero. A further **104,976 cubic row identities** run over valuation triples from 0 through 8, all squarefree column supports, all six unit powers, and three fixed unit-phase patterns. Primes of the cube base are allowed to overlap both remainder components. Explicit counterexamples detect the replacement of a cube or sixth-power zero mask by one.

This is a finite multiplicative ideal model. Its chosen cross phases are algebraic fixtures, not a claim about the distribution of actual Eisenstein residue characters. The independently normalized theta checks above supply separate actual finite-field evidence.

After replacing bare assertions with explicit exceptions, the author ran normal and optimized Python to separate output files and compared them. The root inspected the revised source and replayed optimized Python from the published-path copy. All three final outputs agree byte for byte. The earlier optimized execution with disabled bare assertions is not counted as validation.

The released checker has SHA-256

`b20b521729b2f87b207ff263ecf4f2998b10c5fbecbfb98277e88c967eb37919`.

The recorded [overlaps.json](results/overlaps.json) has SHA-256

`a36c55ab859cf3d0a86f6a184fc055fdcae71e732d13335bbfc68d02b84498c8`.

The report records the companion note hash for association. Reading that hash is not an automated validation of the written analytic proof.

## 4. Reproduction

Run these commands from the repository root. They write fresh outputs outside the recorded packet:

```bash
python standalone/2026-10-10-oscillating-overlaps-and-averaged-moments/checks/verify_operators.py > /tmp/riemann-operators.json
python -O standalone/2026-10-10-oscillating-overlaps-and-averaged-moments/checks/verify_theta.py --output /tmp/riemann-theta.json
python -O standalone/2026-10-10-oscillating-overlaps-and-averaged-moments/checks/verify_overlaps.py --note standalone/2026-10-10-oscillating-overlaps-and-averaged-moments/OSCILLATING_OVERLAPS.md --json /tmp/riemann-overlaps.json
```

The resulting files should match the recorded JSON byte for byte:

```bash
cmp /tmp/riemann-operators.json standalone/2026-10-10-oscillating-overlaps-and-averaged-moments/results/operators.json
cmp /tmp/riemann-theta.json standalone/2026-10-10-oscillating-overlaps-and-averaged-moments/results/theta.json
cmp /tmp/riemann-overlaps.json standalone/2026-10-10-oscillating-overlaps-and-averaged-moments/results/overlaps.json
```

The theta and overlap outputs include their source hashes. A source mutation therefore changes their expected result identity even if it does not cause a predicate failure. All exact publication hashes are also recorded in [PROVENANCE.json](PROVENANCE.json).

## 5. Analytic and publication boundaries

The written proofs are reviewed at exact file hashes, as recorded in [REVIEW.md](REVIEW.md). Classical large-sieve statements were checked against their primary papers, but not independently re-proved. The source-qualified theta result assumes the pinned reflection formula. The optional signed-overlap extension assumes its displayed uniform second-moment premise.

No empirical higher-moment panel, numerical zero census, Lean build, or full independent reconstruction of the imported quasi-Riemann proof was performed in this continuation. The full arithmetic moment premise is explicitly open.

The release is intended to contain only this standalone directory and a navigation addition to the root README, on a new branch based at PR #912's frozen head. The final Git commit and pull request identify the published snapshot; the manifest binds its non-self-referential file hashes and exact dependencies. Remote byte and changed-path verification is performed after creation of that snapshot.
