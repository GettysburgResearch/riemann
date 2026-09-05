# R-105271 — Scope correction for the pure-carrier firewall

Claim ID: `R-105271`  
Status: **BINDING SCOPE CORRECTION**  
Created: 2026-08-24  
RH status: unproved

R-105270 gives a counterexample to any **source-generic derivation** asserting
that the complementary contour of a positive holomorphic safe-line carrier is
small.  It does not, by itself, prove that the Xi-specific numerical statement
`EDGEFLUX105260` is false: the nonconstant Xi terms could in principle offset
the mandatory carrier cancellation.

The correct disposition is therefore:

```text
source/taper-only proof of EDGEFLUX105260      REFUTED;
Xi-specific EDGEFLUX105260 inequality          OPEN / CONCLUSION-BEARING;
T-105260 conditional implication               LOGICALLY VALID;
unconditional ninety-percent conclusion       UNPROVED.
```

Any proof of the Xi-specific edge inequality must exhibit the compensating
nonconstant contribution explicitly.  Calling the edge a routine taper,
endpoint, zero-count, or omitted-prime error is invalid.  In the pure-carrier
fixture its normalized negative trace is one.

R-105271 supersedes any broader wording in the first T-105270 deposit that
called the actual Xi-specific edge statement itself refuted.
