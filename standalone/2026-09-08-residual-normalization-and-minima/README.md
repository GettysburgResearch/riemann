# Normalization and certified positive-residual minima

**RH is not proved. The subpower upper bound on growing-prefix residual norms
is not proved.** Proposed component proofs and four finite minimum certificates;
independent mathematical/code review required.

This continuation of PR #803 preserves its literal integer Mobius prefix and
entire positive residual norm. It does not change the arithmetic source.

Read PROOF.md, especially Sections 2, 3, 5 and 7. New local results:

* Any finite balanced prefix completion can be normalized to p'(1)=1 with
  support increased only to max(N,2Y) and E_new <= E_old/log 2. This is an
  exact oblique projection, not an iterative contraction. Its coefficient
  correction also has an explicit cost bounded by the OLD full norm.
* On balanced variations supported in [Y,N], the true quadratic Gram obeys
  v*Gv >= ||v||^2/[4 floor(N/Y)^2 N(N+1)]. This is a polynomial conditioning
  result in the actual integer coefficient coordinates, not a bound on the
  affine minimum or a comparison with another basis's condition number.
* Every Gram entry is computed using only its own period lcm(m,n)<=N^2,
  with the entire infinite tail enclosed by explicit Euler--Maclaurin bounds.
* A primal/dual residual plus the proved Gram floor encloses the GLOBAL
  finite-support constrained minimum, not just a candidate objective.

| Exact prefix below Y | Support through N | Certified minimum interval |
|---:|---:|---|
| 2 | 4 | [0.072123117281951, 0.072123117281952] |
| 4 | 8 | [0.026111243144081, 0.026111243144082] |
| 8 | 16 | [0.023695806559291, 0.023695806559292] |
| 16 | 32 | [0.022118909935520, 0.022118909935521] |

Each class requires p(1)=0 AND p'(1)=1. Every tail integer is allowed. These
four rows are not an infinite convergence theorem or a zero-free record.
At N=32 a whole-residual period would have 144403552893600 cells; the largest
pair period actually used is 992. All its infinitely repeated weights are
still included, not truncated without error.

A normalized completion must, for any hypothetical off-line zero rho=beta+i gamma,
pay E >= (2beta-1)Y^(2beta-1)/|1-rho|^2. Hence an unbounded subpower family
would finish RH. No such upper bound follows from the finite minima or the
conditioning theorem. The previous 625Y upper bound is not replaced by a
subpower estimate. The norm normalization is idempotent and cannot be repeated
to force a decreasing sequence.

## Replay

```
python -I -S -B verify.py --check result.json
python -I -S -B -O verify.py --check result.json
python -I -S -B test_rejections.py
python -I -S -B test_rejections.py --optimized
```

Acceptance uses only Python integers/Fraction and 192-bit outward intervals.
Floating SciPy computations suggested the rational candidates but are excluded
from acceptance. There is no numerical zeta/zero oracle, digamma evaluation,
numerical contour integral, unproved spectral cutoff, or parent-code execution.
See VALIDATION.md for actual execution and limitations.

## Review targets

Check the full weighted norm, exact prefix and p'(1) repair, the distinction
between the sharp abstract projection constant and arithmetic attainability,
the finite-cell Mobius inversion in the Gram floor, every pair-period tail,
exact (not approximate) feasibility of the proposed candidates, dual signs,
and the still-unproved all-Y upper bound. No canonical or formal status is
promoted by publication.
