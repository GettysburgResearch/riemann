# HBR30: fractional-factorial positivity and the Gumbel-smoothing threshold

**Proposed component research; independent mathematical/code review required.
RH and unbounded-parameter positivity remain OPEN.**

Parent: #879, `5645f787183edefacf6402b0cff60a991fa31ba4`.
This separate sibling packet changes no predecessor source, main, canonical
status or workflow. It is not an integration or an approval of earlier claims.

## Result

For the actual theta cumulant sequence

    q_n=(-1)^(n+1) kappa_(2n)/[2(2n-1)!],

both Hankel towers with moment weights `Gamma(1+n/p)` are positive definite
at EVERY finite dimension, for EVERY real `1<=p<=16384`. This weakens the
factorial weights in the newer #842 reciprocal-subordinator result.

The proof retains every unknown high zero. It imports Platt--Trudgian only for
centrality through `2^40`, proves a complete powered-heat tail estimate, and
freshly reconstructs a real anchor in (14,15) from the full theta integral.
This is NOT a new verified height or a proof that unknown zeros are central.

The exact probability law obeys

    E exp(iu log X_p)=Gamma(1+iu/p) Zcal(1+iu)/q_1,

where Zcal sums reciprocal powers of squared Xi zeros. A convergent independent
Bernoulli/exponential series explicitly transports a less-smoothed law to a
more-smoothed one, with its whole variance tail paid. Reversing that operation
is not positive. After a deterministic centering, the smoothing error at a fixed
moment is O(n^2/p^2), not uniformly small over all moments.

All-rank feasibility is a closed initial parameter interval; it is unbounded
exactly when RH holds. The paper supplies the full polynomial-separation proof.
An explicit rational three-node countermodel has every proved finite-p property
but an unsmoothed negative quadratic form equal to -2. It is NOT zeta.

Read PROOF.md Sections 3--7, then Section 10 for the native certificate.
SOURCES.json separates source reading, classical imports and reconnaissance.

## Reproduce

From this directory:

```sh
python -I -S -B check.py --check result.json --self-test
python -I -S -B -O check.py --check result.json --self-test
```

Each accepting invocation reconstructs the complete anchor and bounded algebra;
it does not merely authenticate a stored result. The self-test executes one
pristine copied CLI and eight actual refusal processes. `--write PATH` is
producer-only. Write exploratory outputs outside the sealed directory.

The 512-bit outward ball primitive is the unchanged attributed BRN27 file.
Normal and optimized runs are the SAME backend and author, not independent
mathematical review. No actual powered heat trace, fractional-gamma matrix,
large zero census, full repository build, Lean proof or remote CI is computed.

The remaining theorem is positivity for UNBOUNDED p (or an equivalent native
arithmetic bound). Neither the finite p limit, all matrix dimensions, the positive
noise law, nor the already known finite zero region supplies that theorem.
Publication metadata and the verified remote head are recorded separately in
the PR and delivery receipt to avoid self-referential file hashes.
