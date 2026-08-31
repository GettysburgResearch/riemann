# Independent source review: mixed-rank canonical degree

Reviewed scientific freeze: `fa31cf56d00c2f3b898e9908ee991fb0545b9804`.
Reviewer: the extension-order lane, which did not author this packet.
Conclusion: no mathematical or implementation blocker found at the stated scope.

I read the complete proof, producer, replay contract, and all 21 test sources.
Git comparison confirmed that all five packet files, including the fixture,
still agree with the reviewed freeze. I inspected the fixture's source binding,
owned-file manifest, and representative exact outputs. I did not run Ruff,
Python, tests, polynomial calculations, or a fixture regeneration; execution
belongs to root's separate serialized record.

The grouped symmetric source really defines the polynomial-base action.
The basepoint/section-ring argument supports finiteness and the stated
Cohen–Macaulay dimension. The lowest canonical piece, determinant character,
terminal Tor duality, and regularity bound give the displayed top coefficient
with the correct sign. The unequal-rank canonical dimension obstruction is
distinct from a scalar trace zero. In the 2-by-4 example the two recurrence
roots and four positive distinct eigenvalues yield eight distinct nonzero
exponential terms; this proves noncancellation independently of the bounded
polynomial gcd control.

The producer forms symmetric coefficients and polynomial-base weights by
separate exact routes. The heldout reversed multiplicities, trace-zero
deformation, companion-matrix recurrence, rational gcd, and squarefree
denominator controls match the proof. No computed character loss is described
as a change in the fixed Tor module. Canonical serialized checking distinguishes
Boolean and floating-point replacements from integers even with an unchanged
stored digest; the added counterfeit tests exercise that boundary.

The captured T-108510 source blob is
`f6c22bf9116de00959a7024b62faaf3a370f2754`. Its upstream commit
`ac1cc5eaf229087b6d805e908897c7c8c99a58b7` is not in this worktree's local Git
object store. A read-only GitHub contents API lookup at the exact declared
commit and path returned that same blob. The replay authenticates the captured
source bytes directly, so it does not silently depend on fetching that missing
ancestor during execution.

The frozen status text predates execution. This review does not rewrite it or
claim that the reviewer reran the packet. Classical Segre/Chow and canonical
module inputs remain credited; no new global arithmetic, ramified, or operator
conclusion is inferred from this finite character comparison.
