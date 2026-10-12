# Independent paired fourth-slot collision audit

Verdict: scoped PASS PF1–PF5, with the global reciprocal-zeta theorem
explicitly imported only for the optional corollary. No complete source
moment or full independent-frequency trace is accepted from these bounds.

Frozen manuscript SHA256:
`d057fd4138a4f9c7fcb5455c51e8eabe04b707b8817d4a6ae3359cdfdb85df9a`.
Frozen checker SHA256:
`d5e1ed672b4ac03b8f7c0a8bf536ecb8732d603fff7031a41d4fbeb2f2c471c8`.
Imported full source pair/remainder proof SHA256:
`d37ad696b46c7dda15a7faf314c46cda2d7d67e25ac8d3288c7f138aac373c13`.

The two same-side factors give the squared modulus of the eta-squared
factor. The four cross pairs are exactly two self pairs and two mixed
pairs; their product gives `(1-1/q)^2` and the squared principal
difference-frequency factor. The exact triangle estimate therefore
retains all six factors and proves PF1; the uniform bounded remainder
from the imported degree-three proof is valid at real parts one half.

PF3 compares absolute logarithms using absolutely convergent prime
logarithm series at real part `1+1/logY`, a bounded first-power change
inside the cutoff, and a bounded Chebyshev tail outside it. This is
uniform in the frequency and does not evaluate a complete zeta on its
zero line. The moving mask cost has the correct inverse-product sign
and is bounded by the previously proved elementary norm-budget argument.
The local pole expansion proves PF5 without the additional classical
global reciprocal theorem. That theorem is stated and scoped explicitly.

The exact two-frequency local kernel determinant is negative unless its
two left sums coincide. Dividing by the nonzero individual Euler factors
is a Hermitian diagonal congruence, so it cannot repair the local inertia.
The manuscript correctly limits this obstruction to the local kernel;
it does not infer that the complete unit-projected radial trace is
indefinite. Source paired-plane bounds do not license a Cauchy extension
to the independent left/right frequency domain.

I read the whole checker and independently replayed normal and optimized
Python to `/tmp/review-paired-frequency-normal.json` and
`/tmp/review-paired-frequency-optimized.json`. Both passed 864 exact
Eisenstein rational six-pair controls, with 720 strict triangle bounds,
and the exact determinant controls `-1/16` and `-2401/40000`. Receipts
are byte-identical, SHA256
`43de0e1eae882ac93059e5e1b4503d207492bddef598d329eac07847ec12de0c`.
These finite controls authenticate the local algebra and explicit scope;
they do not prove the asymptotic Euler, pole, or reciprocal-zeta inputs.

No owner file, frozen four-hour artifact, source checkout or Git state
was changed during this audit.
