# Independent source and normalization review of the unit-neutral local kernel

Status: ACCEPTED as an exact local counterexample to an automatic
positive-kernel Cauchy adapter after the source unit projector. No
indefiniteness of a complete radial trace or full source moment is claimed.

Reviewer: `/root/final_height_review/collision_review`, 2026-10-10.
What was actually run: source/checker reads and SHA-256 authentication.
No checker execution or independent normal/optimized replay by this reviewer.

Frozen continuation `literature/` sources:

* `UNIT_NEUTRAL_LOCAL_KERNEL.md`:
  `676cdb524d9a7bb4dd1b5905f33c8cfb3432765e3a2147f3f416e95b3a035b82`.
* `check_unit_neutral_local_kernel.py`:
  `9738aabcfe92f61e7286ef72988cdf502241ee9cde6adf06a7249e4d668b598d`.
* Kernel conventions in `PAIRED_FREQUENCY_COLLISION.md`:
  `d057fd4138a4f9c7fcb5455c51e8eabe04b707b8817d4a6ae3359cdfdb85df9a`.

In the convention `omega^2+omega+1=0`, the stated generators are
conjugate: `conj(7+3omega)=4-3omega`. Their norms are both 37 and
their coefficient pairs are `(1,0)` modulo 3, the source primary
condition. Since 37 is a rational prime, both are prime generators.
The roots 10 and 26 solve the quadratic modulo 37 and respectively
annihilate these generators. Thus the two residue fields are the actual
source prime fields, not a substituted character model.

Every sixth unit maps to a nonzero sixth root in either residue field.
The source sextic residue exponent is `(37-1)/6=6`, so each unit has
symbol exactly one. Multiplication of a row by a sixth unit therefore
preserves the character at this prime; in particular the orbit of u=1
preserves its local kernel. The fixed nu phase also stays unchanged and
can be absorbed into a Mellin frequency when choosing the displayed
local phases. At a nonunit the residue symbol remains zero. Averaging
this one local kernel over the six units leaves it exactly unchanged.

Every desired unit phase is realized by `q^(-it)` at the fixed prime.
The first vector has local variables `i/sqrt37,-i/sqrt37`, with sum
zero and single-factor product `F1=1+1/37=38/37`. The second uses
conjugate phases with `cos(theta)=sqrt37/8`, which is feasible because
37<64. Its sum is 1/4 and product of its two variables is 1/37, hence
`F2=1-1/4+1/37=115/148`.

The literal local coprime factor is `K(x,y)=1-A(x)-conj(A(y))`.
Its two-vector matrix therefore has entries 1, 3/4, 1/2 and determinant
`1/2-9/16=-1/16`. Both diagonal entries are positive. The collision
matrix divides these entries by `F_x*conj(F_y)`; it is the exact
diagonal congruence with `diag(1/F1,1/F2)`. Its entries are
`1369/1444`, `4107/4370`, and `10952/13225`, and its determinant is

    (-1/16)/(F1^2*F2^2) = -1874161/19096900 < 0.

The unit average consequently fails to supply positivity for this local
factor or its collision normalization. This proves only the stated local
adapter obstruction. Other prime factors, other row orbits, physical norm
filtering and the full radial sum can change the aggregate kernel.
No inference about their inertia, no impossibility of a different trace
estimate, and no source moment or RH claim is licensed by this example.

The checker directly binds the earlier kernel conventions, uses the two
actual finite-field reductions and all six unit values, preserves the zero
at 0, and compares the rational matrices with explicit exception gates.
Its implementation matches the stated finite local predicate. Reading
that implementation does not independently authenticate its reported runs.
