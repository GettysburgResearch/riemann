# Independent-review handoff and attempted full-proof boundary

## Review request

Review the new centered gluing and sharpness theorem, not a full RH proof.
CGG1, CGG2 and the explicit finite-source witnesses have complete proposed
arguments. CGG3's upper half imports the scoped all-support theorem from #825;
its lower half is new. No author checker establishes the unbounded analytic
claims or creates independent referee acceptance.

The most load-bearing checks are:

1. S is the UNION of two boxes on disjoint prime alphabets, not their product.
   They share exactly one vertex of mass 1. Verify both the absence of cross
   edges and the exact negative term in the global-variance identity (3.1).
2. Check the root Green vector's normalization, probability versus unnormalized
   harmonic energies, and the extra second-moment term H_A/G_A in the trial's
   CENTERED quotient. The trial is not the anchored eigenfunction.
3. Verify the upper bound (1.4), and that the explicit mean contrast is orthogonal
   to the global constant. Min-max bounds lambda_2, not lambda_1.
4. Verify existence and first-crossing overshoot of P_r(y). The two-sided Euler
   MASS bounds, not PNT or a prime-gap bound, give log P_r(y) comparable to
   (log y)^2. A real y is just a fixed cutoff for its ordinary prime alphabet.
5. Check the root-capacity asymptotic and its use in (6.1)-(6.2). Those capacity
   ingredients overlap the credited parent papers; the centered union does not.
6. Check the all-large-P filling argument for CGG3 and the scope of its imported
   upper bound. The theorem excludes an absolute gap on arbitrary downsets,
   NOT on the ordinary complete intervals 1,...,N.
7. For the large finite example, check why the second box contributes exactly
   zero edge energy but contributes its ENTIRE mass to global centering. No
   omitted B vertex can be treated as absent from the norm.

## Sources and exact reading scope

The immutable commits and paths are in SOURCE_LOCK.json. Principal inputs:

- #829, `f782788933dc21a0fe6a844950f5ca532eba7d86`,
  `standalone/2026-09-08-astra-coherent-channel-synthesis/PROOF.md`.
  Fresh full proof read, matched to the supplied local manuscript's Git blob
  `0c249620fd818f5fcfe3e18f077a2419d82badac`. Its individual-box spectra,
  root capacity and log-log asymptotic are reconstructed here.
- #828, `528b33ac8d57b5a046260ee45d585cd3fe720f4c` has the parallel root-capacity
  result and geometric-exponent extension. Credit is shared, not double-counted.
  The geometric extension is not needed here.
- #825, `e4a486d3fd4009e3722e9e93f35710b834fbd195`, gives the all-divisor-closed
  upper bound 48[1+log(16log P)]. Only the last worst-case upper comparison
  imports this component. The new two-box upper bound is proved directly.
- #803, `db175de165a9077e709b1cb482998171ffc0c6e7`, arithmetic-norm-transfer
  PROOF.md: fresh reading. Its Y/log Y lower transfer cost rules out another
  coefficient-uniform route to the native physical norm. Not a premise of CGG1/2.
- #827, `29237183dc6973cfa9bd953ac1710b7f00929d04`, pass4/REPAIRS.md: fresh
  reading. The infinite Schur domain condition is respected; this new graph
  theorem is finite-dimensional. Source histories are not edited.
- #804 at `0f6ee91f1a8c8bece1618bde155d62fb0bfb4cad`, RESONANCE.md: fresh
  reading. Its boundary-zero input lower bounds already cover a possible
  alternative explored in this pass; they are not republished as new work.

General root gluing, spectral min-max, variance decomposition and graph capacity
are classical. The proof includes the needed algebra. No exhaustive external
priority search or assertion of a new general graph method is made. The zeta
values in CGG2 are used only at REAL arguments greater than 1, via absolutely
convergent Euler products and the elementary pole at 1.

## What the attempted end-to-end argument did NOT establish

The literal coherent energy from #829 is

```
J_N = sum_(k<N) M(k)^2/[k(k+1)] + M(N)^2/N
    = sum_(n<=N) mu(n)^2/n + 2sum_(n<=N)mu(n)M(n-1)/n.
```

The retained future M(N)^2/N is mandatory. Its first work term is O(log N).
The source-specific upper bound on the signed second term remains unproved.
An unbounded subpower sequence of J_N would supply the previously proved
RH implication; no such sequence is produced here. No generic lower graph
estimate becomes that upper bound by changing its sign or dropping the common
function channel. The current theorem also cannot be transferred to all full
intervals by tensorizing its selected union support.

This pass therefore resolves a sharpness question and identifies a single
explicit slow contrast. It does not shrink the known zero-free gap or prove
the original condition (10). The quantity still needed for an RH proposal must
be stated as an open arithmetic premise, not assigned to reviewers as routine.
