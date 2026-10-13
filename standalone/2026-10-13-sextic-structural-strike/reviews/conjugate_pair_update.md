# Bilinear review: updated hash binding after clarifications

**Current reviewed manuscript:** `pass3_bilinear_attack.md`, 22,931 bytes,
SHA-256

`220d767a03ed6c61b8e5a3ea34b48a0a2adae92607047fbfa0bb96e5be876ef2`.

**Historical review:** `pass3_bilinear_review_extraction.md`, SHA-256
`910732baf00a49e7a9d865cc212bd8f9af7c7cee6dab15d6f7f71ea9fb34f04c`.
That review binds the original 21,258-byte manuscript at
`0dd707c8181160a8347cafd9b1cadec962755001981ce32a9e0da2a09563d0e6`.
The author preserved its exact bytes in
`pass3_bilinear_attack_0dd707c8181160a8.md`; I verified that hash.

I compared the complete current file against the preserved original
using a unified textual diff and inspected every changed passage.
There are four changes:

1. An explicit Cauchy--Schwarz estimate for the two coefficient vectors
   after Mellin separation. It retains the common row mask until the
   resulting quadratic expressions are nonnegative. This is the step
   reconstructed in Section 4 of my historical review, and the new
   displayed inequality is correct. Its coefficient normalization is
   unchanged.
2. An explicit convention that the background Hecke character is its
   primitive associate, with additional imprimitive exclusions handled
   as separate masks. This removes the coefficient-zero ambiguity
   identified in the historical review.
3. The explicit assumption that the native radial majorant lies in
   \(C_c^\infty(\mathbb C)\), is nonnegative and dominates the unit
   disk. This makes the inherited row-test hypothesis self-contained.
4. A clarification about locally exact residue order: the two powers
   \(\pm1\) exhaust the locally exact-order powers precisely when
   \(\varphi(n)=2\), namely \(n=3,4,6\) among \(n\geq3\). A good
   prime's residue character has order \(n\); its power has exact
   order \(n\) exactly when that exponent is coprime to \(n\).
   Hence the added statement is correct. It does not extend the proof
   to exponent patterns of smaller local order, or certify the
   separately mentioned conductor corollary.

**Verdict:** the historical review's source-qualified pass applies to
the current hash, with all three requested proof clarifications now
implemented. No new load-bearing gap was found. Theorems 3.1, 4.1 and
5.1 retain the same hypotheses, normalization and numerical exponents,
with the primitive and row-test conventions now made explicit.

The external fixed-order sieve remains an imported theorem. This
update does not independently certify that foundation, the separate
corollary file, the author's finite checker, or a full signed native
moment. The exact-hash and independence limitations of the historical
review remain in force.
