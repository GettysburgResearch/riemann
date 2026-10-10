# Validation and review scope

Date: 2026-10-10. **The component proofs have internal scoped reviews and exact finite controls. The requested full moment is not proved.**

## Reproduce the finite controls

From the repository root, run:

    python standalone/2026-10-10-sextic-moment-conductor-core/checks/check_local_structure.py \
      --output /tmp/riemann-local-structure.json
    python -O standalone/2026-10-10-sextic-moment-conductor-core/checks/check_local_structure.py \
      --output /tmp/riemann-local-structure-optimized.json
    python standalone/2026-10-10-sextic-moment-conductor-core/checks/check_a2_projection.py \
      --output /tmp/riemann-a2-projection.json
    python -O standalone/2026-10-10-sextic-moment-conductor-core/checks/check_a2_projection.py \
      --output /tmp/riemann-a2-projection-optimized.json

Both scripts require only Python's standard library. Acceptance uses explicit exceptions, not assertions disabled by optimization. The independent executions used Python 3.12.14.

| Control | Ordinary execution | Independent optimized execution | Exact predicates | Stored output SHA-256 |
| --- | --- | --- | ---: | --- |
| Conductor/incidence and interaction structure | PASS | PASS | 222,127 | 6fabde7e386feca8fdd143a2fff4a0a065cb5fe41d6cbe355aab31b30a457f92 |
| A2 twisted gluing and inverse projection | PASS | PASS | 167,052 | f72d14714236c407a3f29d3aed931a0451e4e193d539b8610b2374e4fd2228a5 |

The ordinary and optimized outputs agree byte for byte with [local_structure.json](results/local_structure.json) and [a2_projection.json](results/a2_projection.json).

### What these controls actually check

The conductor script enumerates all local left/right incidence subsets through k = 7, verifies the residual sextic exponent and zero mask in an exact root-of-unity ring, tests complete finite-field character tables, and checks the reflection matrices. Its five moment panels use a sharp half-open column norm band, nu = 1, and every element in a small sharp Eisenstein norm ball. An independent direct row evaluation equals the full grouped Hermitian expansion in each panel.

| D | H | k | Rows | Columns | Exact moment |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 16 | 23 | 2 | 84 | 2 | 444 |
| 32 | 47 | 2 | 162 | 5 | 7,314 |
| 64 | 97 | 2 | 360 | 7 | 33,534 |
| 16 | 23 | 3 | 84 | 2 | 1,452 |
| 32 | 47 | 3 | 162 | 5 | 93,054 |

These finite sharp-weight examples are bookkeeping controls, not asymptotic tests for the smooth target.

The A2 script takes the six-point local coefficient table as an input. It glues 216 global local patterns by the unreduced four-factor twisted multiplicativity and compares that result with the five-label formula. It then checks forward completion and the signed inverse in 82,944 total row/auxiliary/exclusion configurations using actual prime ideals of norms 7, 13, and 19. The arithmetic includes sixth roots of unity, nonunit zeros, the auxiliary update, auxiliary/exclusion overlaps, and the two different normalized scalar costs. A further finite check verifies the diagonal Möbius mask recombination.

The A2 checker does **not** compute primitive Gauss sums to prove the local table; the manuscript supplies that normalization proof. Neither checker tests analytic continuation, a functional equation, uniform estimates over infinitely many conductors, or an infinite moment theorem.

## Independent mathematical reviews

| Review | Source and scope |
| --- | --- |
| [Conductor and checker review](reviews/conductor_and_checker_review.md) | Independent audit of the conductor sectors, interaction graph, and first checker; ordinary and optimized execution. |
| [Initial A2 review](reviews/a2_initial_review.md) | Exact coefficient table, twisted gluing, inverse projection, normalizers, and conditional norm envelope at its frozen earlier hash; also the graph and first checker. |
| [A2 tail and diagonal supplement](reviews/a2_tail_and_diagonal_review.md) | Final A2 source; the actual all-row/tail bound, reversible signed diagonal identity, original Poisson normalization, row zero, and uniform divisor-mass estimate. |
| [A2 checker review](reviews/a2_checker_review.md) | Independent inspection and optimized run of the root-authored gluing/projection checker. |
| [Replica and assembly review](reviews/replica_and_assembly_review.md) | Root's independent audit of the moving averaging inverse, rough-record extraction, saturation examples, and final claim reconciliation. |

The initial and supplemental review manifests preserve their original source paths and byte hashes. Scratch snapshot paths in those manifests are records of the review process, not required build dependencies. The final A2 note is byte-identical to the final author snapshot, and its supplemental review binds that hash. All other final proof hashes are listed in [PROVENANCE.json](PROVENANCE.json).

These are source-bound reviews by separate research agents, not peer-reviewed acceptance or machine-checked proof certificates. The source paper and the parent sieve retain their own dependency and verification scope.

## Checks that were not performed or claims not established

No Lean formalization, global zero computation, new conductor-uniform A2 reflection theorem, or proof of the required strict signed off-diagonal was completed. There is no claimed full fourth moment, 17/24 attainment, unbounded hierarchy, or new RH result.

The completion estimate is a positive norm statement. The centered signed form has cross terms between different correction triples and different auxiliary ideals; it does not follow from that norm statement. Likewise, the exact diagonal cancellation uses the entire signed auxiliary sum and does not generally hold block by block after dyadic separation.
