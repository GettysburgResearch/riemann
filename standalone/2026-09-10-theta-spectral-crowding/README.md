# Spectral crowding after the infinite derivative cut

**Proposed component proofs; independent review required. RH remains unproved.**
This continuation of PR #834 answers the metric question left at the end of its
centered-theta determinant packet. It does not change that packet's statements.

Even after removing ALL adjoint-chain directions, no bounded coercive positive
metric makes the actual centered integration operator skew-adjoint, or its odd
square self-adjoint. Known simple real zeros already force the obstruction.
The proof does not use, assume or produce an off-line zero.

With sigma^2 the exact second moment of the theta probability law, real-zero
pairs of separation Delta force metric condition number at least
4/(sigma^2 Delta^2)-1 for K, and at least 1/(4sigma^2 Delta^2)-1 for T.
Classical positive-proportion simple-zero results provide pairs with
Delta<=24pi/log U in every sufficiently large band (U,4U], so any finite-mode
metrics have condition numbers growing at least as a constant times log^2 U.
The exact Riesz projections have corresponding logarithmic lower bounds.

A local finite positive-measure norm cannot orthogonalize all those exponential
eigenvectors either, even when it is not equivalent to the original theta norm.
The result does not exclude a genuinely nonlocal unbounded metric or a different
Hilbert--Polya realization. Spectral reality itself remains the missing theorem.

Read [PROOF.md](PROOF.md), especially Sections 2--5. Review the distinction between
the adjoint of a restriction and a restricted adjoint; retain the squared-norm
convention in the sine calculation. The external simple-zero proportion is an
imported classical theorem, not a result of the bounded checker.

```
python -I -S -B check.py --check result.json
python -I -S -B -O check.py --check result.json
```

The 56 finite fixtures concern two-dimensional rational geometry, synthetic
pigeonhole configurations and constants. They are not actual zero computations,
a formal proof, an external literature replay, or independent review.
See [SOURCES.json](SOURCES.json) and [VALIDATION.md](VALIDATION.md).
