# Exact finite representation and directed numerical evaluation

The energy in this packet is the COMPLETE norm in the original weighted
step space. It is not a finite prefix of that norm. PROOF.md GE26.2 first
sums its infinite Fourier kernel analytically. Numerical work then evaluates
only a finite positive Green form.

## Literal source

For M=4,8,16,32, mathcore.py constructs mu, phi and J_2 by integer factorization
and computes the unique rational balanced source from the divisor formulas.
The replay also checks its exact KKT equations and both scalar constraints.
It generates every reduced r/q with q odd, 3<=q<=M, 0<r/q<1/2, sorts these
fractions exactly, and constructs L_q from all multiples. Odd composite and
nonsquarefree indices are included. Counts are 1,6,24,106 respectively.
No zero data, external special-function values, fitted Gram, or guessed
asymptotic supplies a numerical input.

Every Green interval length is positive. Its cumulative charge is assembled
WITH SIGNS before squaring. The total and truncated endpoint integrals are
finite sums over that complete mesh. All their sine/cotangent and pi errors
are propagated by outward intervals.

## Rounding and transcendental constants

The independent mathcore.py interval class stores endpoints as integers in
units of 2^(-224). Addition is exact on that grid. Products and quotients
range over all endpoint choices and round down/up by integer division;
divisors meeting zero are refused. Squaring a zero-containing interval uses
lower endpoint zero. Only exact ints and Fraction values are admitted; bools
and floats are rejected as numerical inputs.

Pi is enclosed by Machin's identity 16 atan(1/5)-4 atan(1/239). Each arctangent
uses 96 alternating rational terms and a symmetric bound by the first omitted
term. Tangent addition fixes the elementary identity and its branch: the
tangent of 4 atan(1/5)-atan(1/239) is one and the angle lies in (0,pi/2).

For sin(pi*q) and cos(pi*q), rational q is reduced modulo 2 into [-1,1]. Thus
the real argument has absolute value below 4. The sine polynomial contains
80 terms, degrees 1 through 159, and the cosine polynomial contains 80 terms,
degrees 0 through 158. Taylor's theorem, including the intervening zero
coefficient, bounds their respective absolute remainders by

    4^161/161! and 4^160/160!.

All arithmetic in those polynomials is outward-rounded, and the remainder is
added on BOTH sides. All mesh sines and cosines must have strictly positive
lower bounds before division. Adjacent tangent intervals must be separated;
a truncated integration endpoint that overlaps a mesh breakpoint is refused,
not silently assigned to a side. The fixed tests do not require refinement.

Logs use exact rational range reduction q=2^e*y with 1<=y<2. The atanh series
for log(y), with z=(y-1)/(y+1)<=1/3, has 96 terms and nonnegative remainder
at most 2*z^193/[193*(1-z^2)]. The same formula evaluates log 2. No logarithm
is required for the full energy itself, only the displayed cutoff 1/log(2M).

## Independent comparisons and finite checks

The new Green-energy intervals at M=4,8,16 overlap the predecessor's separately
constructed infinite-Gram enclosures. The predecessor's 3,884-control replay
was also rerun separately in normal and optimized Python; its result is not
counted as new controls. The new driver does NOT execute predecessor code.
It authenticates the predecessor proof and retained verification bytes.

The complete finite sine reconstruction is compared against exact floor
values on 64 paired cells for each of the four sources. A direct min-kernel
quadratic form is compared with the cumulative interval form. A rational
physical prefix through cell 512, with the rigorous elementary amplitude
tail, independently encloses the energy. At M=4 the exact formula is
pi/(2 sqrt(3)); its algebraic relation is checked separately.

The all-scale coefficient bounds are NOT inferred from numerical panels.
Their proof is GE26.4. The selected rational panels M=128 and 256 only check
normalization, the k-dependent correction, the coefficient constants, and the
exact total-coefficient formula. Cotangent remainder tests use odd k<=63.
The tridiagonal inverse is checked on independent rational meshes.

These are research-level analytic proofs and exact/directed programs, not a
proof-kernel-verified interval library. No finite test proves the unbounded
endpoint estimate or RH. No Windows run or historical portability repair is
claimed.

The compact verification JSON retains the full rational mesh and frequency
coefficient column. All intermediate directed mesh values are reconstructed
and their canonical serialization is bound by directed_mesh_sha256; they
are not repeated verbatim in the retained JSON. The full energy and endpoint
enclosures retain exact dyadic endpoints as well as display decimals.
