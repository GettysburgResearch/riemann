# LT26: exact late-tail controls expose a nonrobust zero-defect inference

Status: proposed component proofs and bounded algebra checks. Independent review
required. **RH, J=0 and the requested growing-horizon upper bound remain unproved.**
This is a research continuation of PR819, not an independent acceptance verdict.

For the actual positive factorial source d, every finite horizon T, every finite
number r of prescribed safe derivatives, and every positive tolerance, the
manuscript constructs a CHANGED positive source d_alpha which:

- equals d through T and retains those derivatives exactly;
- differs from d by an arbitrarily small pointwise RELATIVE amount on the WHOLE
  half-line, and has an arbitrarily small additive disk H-infinity perturbation;
- retains every original interior zero and acquires a new right-half-plane pair;
- has strictly larger Jensen entropy tending to the entropy of d.

Classical critical-line zero existence is the sole zero input, used to make
adversarial changed-source examples. No actual zero is numerically evaluated.
These are NOT off-line zeros of zeta, NOT new Euler products, and NOT RH
counterexamples. The unmodified infinite factorial formula is not preserved.

A stronger domain statement is important: d_alpha is itself in the original
closed source domain, obtained by a future-only closed-domain correction. But
its use as a new GENERATOR loses a proper subspace. The two domain projections
converge strongly on every fixed test while their operator-norm distance stays
exactly ONE. Finite Gram predictions can be made arbitrarily close too.

This rules out the proposed completion by finite-data/positivity stability.
It does not invalidate source-exact arithmetic proofs, the prior finite
certificates, or the convergence-to-floor theorem. It supplies no proof that
the actual entropy vanishes. The remaining estimate must retain the literal
infinite arithmetic source, rather than replace it by a nearby positive model.

## Read and replay

Read PROOF.md, then REVIEW_AND_SOURCES.md and VALIDATION.md. To replay from the
repository root:

```sh
python -B standalone/2026-09-08-astra-late-tail-zero-insertion/check.py
python -B -O standalone/2026-09-08-astra-late-tail-zero-insertion/check.py
python -B standalone/2026-09-08-astra-late-tail-zero-insertion/test_check.py
python -B -O standalone/2026-09-08-astra-late-tail-zero-insertion/test_check.py
```

The exact parent manuscript must be at its source-locked sibling path. It is
included unchanged as context in the delivery ZIP, not added again in Git.
No third-party Python library, zero table, floating-point calculation or large
arithmetic campaign is needed. Finite checks authenticate the stated algebra
and inventory; they do not machine-prove the analytic theorems.
