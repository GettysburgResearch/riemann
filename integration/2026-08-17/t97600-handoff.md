# T-97600 handoff

Publication base: PR #577 at `ae85922195c12a29944e624337bae2167091929b`.
The mathematical source remains frozen at PR #566 and the adversarial heads
listed in the source lock.

The v3 paper is a hostile reconstruction and exact downgrade of PR #566.  It is
not a completed proof of RH.

The first unsupported arrow is the uniform completed-parity scalar Lorenz
inequality `CPSL67`.  In PR #566 this was hidden inside `L-96651` as
"reserve-preserving grouped Hall" and `g>=Tg`.

A successor should either:

1. prove `CPSL67` directly, preferably by an exact arithmetic invariant for the
   one-dimensional dual threshold; or
2. produce an exact finite endpoint and dual separator refuting it; or
3. replace the target/scalar coupling by another source-faithful producer that
   still yields eventual nonnegativity of the 5:3 scalar.

Do not attempt to repair the proof by checkerboard minors, leafwise canonical
Hall, scalar-to-row promotion, unrestricted rough stores, or omission of the
`r-2r^2` compensation source.
