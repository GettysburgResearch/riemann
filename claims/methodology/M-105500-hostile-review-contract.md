# M-105500 — Hostile review contract for the ninety-percent Wick–Pick packet

Claim ID: `M-105500`  
Status: **FAIL-CLOSED REVIEW SPECIFICATION**

A review must reject any promotion of `T-105500` unless all of the following
are checked.

1. **Index convention.**  A pole `+1/(x-c)` has Cauchy index `+1`, and the
   residue block has signature `-1`.  Test `F=x`, `x^2-1`, `x^2+1`, repeated
   roots, and nonreal conjugate factors.
2. **Common factors.**  Zeros shared by `F` and `F'` cancel in `F/F'` but still
   contribute one distinct zero through `F'/F`.  No separate simplicity
   hypothesis may be reintroduced silently.
3. **Full dimension.**  The signature formula uses the reduced total pole
   order `M`, not an arbitrary compression dimension.  Only `M<=N_1` is used
   asymptotically.
4. **No nuisance subtraction.**  Nonreal and even confluent blocks have zero
   signature; odd blocks are priced by their literal leading coefficient.
   They are not discarded and not declared positive.
5. **Wick coefficients.**  Recompute
   `m d_m=sum_(j=3)^m d_(m-j)`, verify `d_1=d_2=0`, and verify the rational
   energy bound `9181/9504000<1/1000`.
6. **Normalization.**  The Hermitian symbol pays twice the one-sided energy,
   giving `501/500`; the 99/101 perturbation gives exactly
   `1633500/1703567` and line output `1563433/1703567`.
7. **Trust boundary.**  The replay authenticates finite algebra, rational
   bounds, and polynomial regressions.  It does not machine-prove the PNT,
   Montgomery--Vaughan, the actual-Xi transfer, ninety percent, or RH.
8. **Boundary price.**  `W_2` contains an `A_X^2` exponential term.  A proof
   for the `K=1` horizontal bound cannot be cited as a `K=2` bound without an
   explicit estimate.

Required adversarial regression: structured multiplicity/nonreal polynomial
families plus seeded random rational polynomials, with exact Sturm distinct
root counts and exact rational inertia.
