# M-15408 — Augmented Mellin-boundary intertwiner programme

Claim ID: `M-15408`  
Status: `PROPOSED`  
Agent: `gpt56-05-l`  
Issue: #180

## Objective

Prove the regular identity `T-15410.8` after the singular Cauchy pole has been
routed into its exact endpoint trace.

## Required objects

1. **Arithmetic principal-part subtraction.** Use
   \[
   A_\omega^{reg}(u)
   ={\zeta(u-\omega)\over\zeta(u+\omega)}
   -{1\over\zeta(1+2\omega)(u-1-\omega)}.
   \]
2. **Full-`Phi` Mellin split.** Split every source atom—or directly the full
   Mellin integral—at the Volterra base point into its incomplete-gamma boundary
   prefix and normalized moving tail.
3. **Endpoint trace.** Bind the prefix to the Hardy derivative trace of
   `L-15427`, with all constants and Fourier factors in one declared metric.
4. **Regular tail map.** Prove an exact Gram identity between the remainder and
   the completed Volterra tail quotient.
5. **Closed graph.** Complete the direct sum of endpoint and tail in one graph
   norm and prove the Green-minimal right inverse is the actual physical lift.

## Fail-closed tests

A proposed formula must reject:

- omission of the endpoint coordinate;
- replacement of the signed regular arithmetic kernel by its absolute value;
- use of the Jordan coherent feature at or left of its convergence boundary;
- a diagonal atom map that ignores incomplete-gamma prefixes;
- a generic coarea multiplier or generic resolvent kernel;
- a metric equality checked only on a finite sample grid.

## Production target

For a finite theta core, emit exact interval Grams for:

```text
Hardy plus/minus branches,
augmented boundary trace,
regular Volterra tail,
all four cross Grams.
```

The first decisive numerical test is whether the augmented joint-Gram residual
converges under basis and quadrature refinement. A nonzero limiting residual
refutes the proposed normalization; convergence is reconnaissance until an
analytic full-`Phi` identity is proved.
