# Independent review of the absolute Frobenius cutoff

Reviewed scientific commit: `3537e8aee15ebb3d5ba4084806f9a1cfefa7bcb3`.

I read the complete proof, preregistration, replay contract, producer, and all 27 tests, then inspected the frozen six-file identities. The current six packet paths have no diff from this commit, and all five LF-normalized owned-file bindings in the artifact match their current bytes. I did not run the producer or scientific tests.

The root reviewer reports Ruff, all three producer modes, and 27 tests in each mode passing. The frozen replay note still contains its pre-execution status sentence. That sentence is stale relative to the root's reported validation; it is not evidence that the reviewer independently executed the packet. No frozen source was edited during this review.

## Finding

No mathematical or acceptance blocker was found. The absolute cutoff `p_(e,n)=ceil(C_n/e)` gives the stated same-family cyclic norm law. The root-of-unity sum selects the Frobenius power `h`, and the phase on the extended side is `xi^d`. The elementary ceiling identity supplies a literal block identity before summing grades. Normal convergence extends that identity without dividing by values at zeros.

The proof correctly separates literal cutoff rules from actual source blocks. The latter retain the odd-power zero-trace ambiguity, and the classification concerns individual blocks at phase one. It does not classify accidental identities of products over different grades or arbitrary arithmetic sources. The boundary and zero-divisor claims are restricted to phase one; the zero-phase constant product is explicitly excluded from those claims.

The orientation `U=log(A_D/A_C)` agrees with the finite counterterm formula and the code. Coherence does not determine the choice of the sequence C, and the exact nonintegral coefficient controls preserve the distinction from the native normalization. The result is an operation law for a declared scalar regularization of the fixed Frobenius source, not a full place-Euler or ramification base-change theorem.

## Producer and acceptance

The producer authenticates the frozen grading-genus proof and executable before import, then reauthenticates the predecessor chain. Direct proper characteristic polynomials with exponential counterterms are compared with independently selected absolute trace sums. Coverage includes twelve primary panels, twelve same-family norm panels, six nontrivial/zero phase controls, ceiling composition, actual single-block ambiguity, and oriented frame changes.

The tests retain wrong relative-slope, wrong phase, wrong sieve, and type-changing JSON controls. Canonical serialized comparison with `allow_nan=False` prevents Python numeric-equality aliases from accepting a modified fixture. Bounded controls support the source calculations; the infinite convergence and classification assertions remain proof obligations discharged in the mathematical note.

## Frozen identities

- Mathematical note: `09d50e6d1e3448398800cf21aea010ebf64a7fc1`.
- Preregistration: `9cfefe1596e380e407369e07fa776129f7f7b311`.
- Replay contract: `046666d5d277a80fa7673f47b38dd671ae0697ca`.
- Producer: `eee6004053c77b05dc9f365fb131d81759ada783`.
- Tests: `e2398671cafcd06a082041465276a0af625ada09`.
- Artifact: `5c6c09fd20b18b6832e1fb00e38910c4312b99df`.
- Artifact schema: `absolute-frobenius-cutoff-v1`.
- Artifact proof-object digest: `9df66ad2524e8b7724c45b328620f762a3720c91faeee64240f4ec7f6a9643c0`.

Reviewer scope: independent proof and code read, exact frozen identity and owned-binding inspection, no independent scientific execution.
