# One-node annular exhaustion attack — 2026-08-12

## Verdict

This is the smallest conclusion-producing route presently visible.

At one fixed interior node `eta=1`, the crossed-zero Blaschke products form an
exact dyadic positive telescope.  The terminal scale `a=1/2` is zero-free by
the classical half-plane `Re s>1`; every lower scale adds one nonnegative
annular hyperbolic increment.

The same Cauchy node diagonalizes every physical translation port, turns the
singular short compensation into scalar Laplace transforms, and automatically
dominates the adverse long odd port by the long even port.

## Exact advance

- `L-91420`: fixed-node dyadic hyperbolic-annulus telescope;
- `L-91421`: one Cauchy vector scalarizes every translation and compensation
  port and aligns with a safe one-Green vector;
- `R-91407`: positive arithmetic and model telescopes alone do not imply
  exhaustion;
- `T-91404`: coefficient-one annular source exhaustion at this one node, for
  every dyadic annulus, proves RH.

## Why it is promising

The route discards most of the CPPD burden:

```text
no all-carrier operator order;
no arbitrary delay packet;
no two-orientation matrix as an independent target;
no Gram capture;
no cofinal interpolation.
```

The remaining object is one scalar source-to-model map per dyadic depth
annulus.

## Immediate next calculation

1. restrict the quasi-Levy/Hardy colligation of PR #404 to `r_1`;
2. express its prime and gamma/pole innovations at scales `a` and `2a`;
3. compute the critical and stable one-node outputs from the Suzuki model
   kernel;
4. show the difference equals the annular Blaschke increment of `L-91420`;
5. prove the source innovation is already exhausted before that component.

The first nonzero annular increment under false RH is a particularly sharp
hostile test.

## Boundary

```text
one-node annular telescope            EXACT
one-node source scalarization         EXACT
positive telescope alone              INSUFFICIENT
annular source exhaustion              OPEN / RH-EQUIVALENT
RH                                     UNPROVED
```