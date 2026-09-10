# A collision-index route: certify the boundary, count every collision

**PROPOSED research direction and component proofs; RH remains unproved.**
No actual theta boundary rectangle has been certified in this packet. The
included exact executable verifies polynomial heat models, not a new zeta range.

The new direction for this thread is to work with the exact theta heat flow
rather than make an infinite trace tower positive or symmetrize a nonnormal
operator. For the backward heat equation H_t=-H_xx, consider the real jet
G=(H,H_x) in the (time,height) plane.

At a double zero, det DG=-H_xx^2<0. The proposed complete local proof extends
this to every multiplicity: an m-fold collision has degree -floor(m/2).
Consequently a zero boundary winding of H+iH_x excludes ALL collisions inside:
there are no opposite-sign events to cancel them. For the actual even theta
source, collisions occur in +/-height pairs, so a strict boundary-winding lower
bound greater than -2 already forces zero.

## What is supplied

- The all-multiplicity index proof, complete boundary count, and positive-
  amplitude normalization rule, retaining its derivative correction.
- An end-to-end conditional RH route from an explicit positive-time exhaustion.
  The imported uniform large-height theorem pays the possibility of zeros
  escaping through infinity. No simplicity assumption at time zero is made.
- A continuum-safe exact boundary verifier: complete ordered edge partitions,
  full chord-error bounds, exact rational winding and adverse tests.
- Literal-theta derivative recurrences and explicit bounds for BOTH omitted
  theta indices and the entire integration tail, defining the missing real-
  source endpoint/derivative oracle without using numerical zero data.
- A rigorous changed-source stress test: even strongly log-concave positive
  double-exponential densities can have positive-time collisions. Generic shape
  positivity cannot supply the needed arithmetic boundary theorem.

**Open target:** prove the source-specific one-sided phase budget on every
rectangle [2^-j,1] x [-2^j,2^j], or another exhaustive family. This is an RH-
strength assertion, not a routine last check. Its prospective advantage is a
one-dimensional integer-valued certificate and analytic phase interface, not a
claim that the mathematical problem has become weak.

Read [PROOF.md](PROOF.md), especially Sections 2--5, then the exact source bounds
in Section 6 and countermodel in Section 7. The first bounded contribution is a
full-theta collision-free collar for a moving root, with certified boundary
rather than sampled phase. A global completion needs uniform source control,
not merely additional finite collars.

## Reproduce the bounded controls

```sh
python -I -S -B check.py --check results.json
python -I -S -B -O check.py --check results.json
python -I -S -B test_check.py
python -I -S -B -O test_check.py
```

Acceptance authenticates the package, regenerates all 22 model boundary
certificates and formal source-derivative checks, and compares strict typed
receipts. `--write` is unauthenticated producer mode. All accepting numerical
arithmetic is Python integer/Fraction arithmetic; no zeta oracle or floating
root solver is used. See [VALIDATION.md](VALIDATION.md) for executions and limits.

De Bruijn--Newman deformation, Hermite collision normal forms, Sturm theory,
Brouwer degree and chord interpolation are classical. They are credited, not
claimed newly discovered. This is separate from PR #842's Lee--Yang synthesis
and does not alter any current integration or mathematical acceptance status.
