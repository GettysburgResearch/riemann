# Fixed-prime physical coercivity: pre-computation design

Status: preregistered finite proof target, not a certificate.

Authoring base: `8f01064df805624c045877655893c324a220975d`.
The protected tuple-source audit shares this branch but is a separate question.

## Frozen source and question

Use exactly the finite-prime source at PR #770 head
`9421846721cd788ab01615c8b6d459d9de849df7`, in
`research/riemann-structures/native-six-hour/`:

- `FIXED_PRIME_INFINITE_HORIZON_COMPLETION.md`;
- `INFINITE_NATIVE_PHYSICAL_FAITHFULNESS.md`;
- `EFFECTIVE_FULL_SUPPORT_THEOREM.md`.

The prime set is `(2,3,5)`. The local functions are
`A(z)=sqrt(1-z*z)`, `C(z)=sqrt(1-z)`, on their value-one branches.
For `a,b in {0,1}^3`, the 64 literal completed tensor fields are
`phi_ab(t)=s_a(p^(-1/2+it))*s_b(p^(-1/2-it))`, with `s_a` the product
of the selected A/C local factors. Use the original measure
`dnu=|kappahat(t)|^2 dt/(2*pi)`, with the exact three-piece K_L from the
completion proof. No Fourier-coefficient counting norm replaces this measure.

The proposed result is an explicit, possibly extremely small, lower bound
`c*||M||_F^2 <= ||sum_ab M_ab phi_ab||_L2(nu)^2` for this fixed source.
It is not uniform in the prime set, does not reconstruct retained gamma,
and does not assert that all tensor coordinates are attainable paths.

## Fixed arithmetic panel, before evaluation

- Nodes: exactly `t_j=j`, `j=1,...,64`.
- Node order: increasing j; binary lexicographic A/C tensor coordinates.
- Arithmetic: python-flint directed complex balls at exactly 1024 bits.
- Compute the 64 by 64 evaluation matrix and its verified inverse.
- Independently evaluate the same source matrix using opposite phases and
  conjugation symmetry; retain a source-equivalence check.
- Evaluate kappahat at all 64 nodes from the exact elementary antiderivatives.
- Record every failure. No replacement nodes, precision ladder, adaptive
  subset, or new prime is authorized by this design.

An inverse bound and all 64 strictly positive kappahat-modulus lower bounds
are acceptance prerequisites. A failure is unresolved, not noncoercivity.

## Analytic bridge to be proved independently

Bound the global derivative of the literal vector phi from the local
radicals. Thicken each node to a small common disjoint interval, using the
evaluation inverse to maintain a lower singular-value bound throughout.
Bound kappahat's derivative from its original compact kernel and retain
positive density on those intervals. Integrate over those intervals to
obtain the original physical norm lower bound. All displayed final constants
will be rational powers of two with outward directed bounds.

The finite coefficient-row inverse of PR #783 is not an input to this
bridge. Its conditioning theorem is a different post-observation norm.

No native numerical evaluations were performed before this design freeze.
