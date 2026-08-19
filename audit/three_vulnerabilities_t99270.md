# Hostile audit — the three most vulnerable points after T-99250

## Verdict

The scalarization in PR #647 is a real simplification, but three points deserve
special protection.

### 1. The unbounded pointwise tail

This is the only genuinely new global arithmetic assertion in T-99250.  It is
not proved, and it may be strictly stronger than RH.  A future negative cell
would destroy the pointwise route even if the Mellin programme remained viable.

**Repair:** `L-99270` replaces pointwise positivity by either eventual
positivity of one zero-free logarithmic box average or subpower total negative
mass.  `L-99271` supplies a positive inverse renewal and source-owned
prime-power martingale for attacking the latter.

### 2. The surrounding row/common-parent composition

PR #642's positive kernel and PR #647's Radon-Nikodym repair are useful, but the
direct scalar Mellin transform does not depend on them.  Keeping them in the
normative chain unnecessarily exposes the conclusion to Hall, child-placement,
Volterra, and calibration disputes, including the alternate PR #648 route.

**Repair:** `L-99272/R-99270` sever those arrows.  They are retained only as
cross-checks.  The scalar theorem begins with `beta` and `T`.

### 3. Analytic and finite-certificate authentication

The earlier Landau paragraph compressed the abscissa argument, while the fast
finite verifier authenticated only the reported minimizer and hashes; its full
mode reran the same producer.

**Repair:** `L-99272` proves the specialized Landau theorem, the positive-real
zeta sign, the cancellation at `s=1/2`, and the pole-order audit.  `T-99271`
uses an independent global-Möbius sieve and independent integer-square-root
engine to test both sides of all `10^8` cells.

## Scientific boundary

All three vulnerabilities are repaired at interface/theorem scope.  The new
weaker global producers remain open.  RH remains unproved.
