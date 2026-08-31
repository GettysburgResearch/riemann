# Extension order: boundary module and two scalar shadows

Status: proposed reviewable mathematics, outside canonical integration.
Source: the actual coherent S3 algebra and standard relation sheaf, pinned
at `c3cdd2528595cbf22c31d88a40c8a611b6385752`.

The [proof](EXTENSION_ORDER_DEFECT.md) constructs the natural injection
from extending before adjoining generators to extending the generic tensor
algebra afterward. Its cokernel is an actual graded boundary module, not
a quotient algebra. Every S3 ramification type and residual Frobenius is
retained in exact all-grade factors.

Two consequences must be distinguished. The ordinary finite-grade
L-function of the additive cokernel multiplies in the exact sequence.
The nonlinear full-place Euler functions differ instead by a finite
rational ratio of local Hilbert series. At old C2 inertia the two scalar
constructions agree in degree three and already disagree in degree four.
Nonsplit infinity has a thirteen-dimensional degree-four defect with
trace one; its two eigenspaces have dimensions seven and six.

The reverse-order source has the same entire interior arithmetic pole
divisor as the prior pole-cleared source, but different local factors
and a provably nontrivial global rational correction. The proof transfers
the existing sharp coefficient-growth dichotomy and unit-circle natural
boundary. It does not classify all sources with the same scalar function.

## Primitive replay and limits

The producer authenticates the frozen source and proof before importing
their chain. Its new primitive calculation starts with literal permutation
modules: V is the sum-zero part of W, and the added S is V. C2 invariants
are actual orbit sums. The after-source injection is written in those
coordinates and has disjoint nonzero column supports. At C3 the exact
Fourier vectors over Q[omega]/(omega^2+omega+1) diagonalize the literal
permutation action; residual reflection permutes the invariant monomial
basis. Cokernel dimensions and Frobenius eigenspaces are thereby computed
without using the displayed rational Hilbert formulas.

Primitive S3 checks stop at degree eight. A separate S4 standard/permutation
C2 holdout stops at degree three and checks120 versus125, without claiming
a global S4 Euler theorem. Source Molien identities are checked through
degree24. Actual branch degrees and residue-field signs reuse the frozen
three field panels and their exact degree-four norm reconstruction; no
new extension field is enumerated. Rational corrections and ordinary
cokernel determinants are separately replayed and deliberately unequal.

The infinite pole-transfer theorem rests on the complete proof, including
the characteristic p>3 norm argument and the common good-place extraction.
No cutoff is treated as evidence sufficient for that conclusion.

From the repository root, using the serialized Python runtime:

```text
python -B research/l-families/atlas/generalized/extension-order-defect/replay.py --check
python -B -O research/l-families/atlas/generalized/extension-order-defect/replay.py --check
python -B -m unittest discover -s tests -p test_extension_order_defect.py
python -B -O -m unittest discover -s tests -p test_extension_order_defect.py
```

Execution is pending root's serialized run; no passing test count or
independent exact-freeze review is claimed yet. The producer binds this
README, the proof, its source and the complete substantive test file.
Repairs receive a new freeze rather than changing authenticated history.
