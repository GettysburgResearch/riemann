# Independent review of the finite A2 projection checker

**Verdict:** PASS for the finite algebraic scope described here. This review does not establish the six-point Gauss table, an analytic functional equation, a uniform infinite estimate, or a moment theorem.

**Reviewer role:** the balanced-core mathematics agent independently inspected the checker authored by the root agent, compared its operations with the source coefficient law and the five-label identities, and reran it with Python optimization enabled. The checker was not edited during this review.

## Exact reviewed inputs

| File | SHA-256 |
| --- | --- |
| `checks/check_a2_projection.py` | `3c4666ec71c9021fb1b7806813a1800c95d9e03ffb0f219f2b59ced54f32bdf5` |
| Imported helper `checks/check_local_structure.py` | `76cc2e5147175829804820a632fb4cd60a633c1510d784dd483294d1ad95970d` |
| Repository result `results/a2_projection.json` | `f72d14714236c407a3f29d3aed931a0451e4e193d539b8610b2374e4fd2228a5` |
| Independently reproduced result `a2_projection_balanced_independent.json` | `f72d14714236c407a3f29d3aed931a0451e4e193d539b8610b2374e4fd2228a5` |

The repository files were read under `/workspace/scratch/6ec6134c1535/riemann/standalone/2026-10-10-sextic-moment-conductor-core/`. The independent result was written outside that repository, under `/workspace/scratch/6ec6134c1535/`.

## Command actually run

```bash
python -O /workspace/scratch/6ec6134c1535/riemann/standalone/2026-10-10-sextic-moment-conductor-core/checks/check_a2_projection.py --output /workspace/scratch/6ec6134c1535/a2_projection_balanced_independent.json
```

The process exited with code zero and emitted `status: PASS`. Its output is byte-identical to the recorded repository result. Every acceptance predicate calls `require`, which raises `RuntimeError` on failure; the predicates remain active under `python -O`.

## What was inspected independently

1. **Two exact coordinate rings.** `ring_mul` computes multiplication in the Eisenstein ring with relation `omega^2 + omega + 1 = 0`. The separate `root_mul` computes in the sixth-root coefficient ring with relation `zeta_6^2 - zeta_6 + 1 = 0`. The `UNITS` and `ROOTS` arrays represent the same six complex roots in these two bases. No floating-point phase comparison is used.
2. **Actual prime ideals and symbols.** The three generators `(-2,-3)`, `(1,-3)`, `(-2,3)` have norms 7, 13, 19 and are congruent to 1 modulo 3. Their chosen residue roots are 4, 9, 7. Each generator vanishes in its own residue field. `symbol` evaluates the sextic Euler exponent and returns a separate zero marker on nonunits. Cubic reciprocity is checked for each pair.
3. **Unreduced source gluing.** `source_phase` retains all four types of symbol in the rigorous twisted multiplication law, equation (20) of Brubaker–Bump–Chinta–Friedberg–Hoffstein, *Weyl Group Multiple Dirichlet Series I*, March 30, 2006, <https://chinta.ccny.cuny.edu/publ/wmd1.pdf>. The six local support points are treated as an assumed table. Their independent formal parameters `A_p` and `B_p` are compared coefficientwise, so successful phase checks do not depend on selecting numerical Gauss sums.
4. **The five-label formula.** For each prime label the local monomial is respectively 1, `A_p`, `A_p`, `B_p`, `B_p`, or `B_p A_p`. The source twist agrees with the CRT phase on the squarefree product of the two axis labels and the `(2,2)` label. This is the local content of the exact global formula.
5. **Forward and inverse projections.** Every subset of correction primes is considered. The child exclusion gains those primes, preventing their reuse. The child auxiliary gains precisely the primes with label `(2,2)`. That auxiliary shift supplies the cross-phase required when the outer and child Gauss factors are recombined. Actual zeros are retained in the moving row, auxiliary, and exclusion factors, including overlaps between the child auxiliary and its exclusion.
6. **Exact scale identities.** The scales are reconstructed from the actual support exponents. `Fraction` checks the child normalizer `Sigma'/Sigma = 1/(NC)^3`, averaged squared norm cost `1/(NC)^2`, and fixed-auxiliary squared norm cost `1/((Nc)^2 (Nd)^2 (Ne)^3)` with exact rational arithmetic.
7. **Signed diagonal algebra.** Separate finite predicates verify the three-allocation continuum identity `1 - Np + (Np - 1) = 0`, and the stronger nonunit-mask recombination in the inverse source bijection. These predicates test the finite Möbius identities only; they do not test the smooth lattice discrepancy estimate.

## Coverage and its limits

There are 216 global patterns, the full Cartesian product of six local labels at the three selected primes. For each pattern there are 384 selected row/auxiliary/exclusion configurations, hence 82,944 configurations in total. Both the forward and inverse identity are checked on all of them. Together with the local arithmetic, norm, and diagonal controls, the run executes **167,052 explicit predicates**.

This is complete coverage of that declared finite grid. It is not complete coverage of all primes, residue fields, rows, or ideals. The general identities require the proofs in the mathematical note. In particular, the local Gauss normalization and all analytic assertions remain outside the computation's acceptance scope. The output does not authenticate a primitive Gauss-sum replay or an infinite moment argument, and it states these exclusions explicitly.

## Review conclusion

No defect was found in the declared finite controls. The independently reproduced output agrees with the root agent's result, and the code's exact arithmetic and zero-mask handling support the claimed finite validation. This review approves only the frozen checker and output hashes above for that scope.
