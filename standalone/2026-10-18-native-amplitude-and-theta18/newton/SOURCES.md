# Exact sources and overlap boundaries

## Inputs

1. **NRC32 finite Newton source.** PR #905, commit
   `0f82df3bf1d0bc669a1bbca09f8404b77c6fecde`,
   [native covariance compression proof](https://github.com/GettysburgResearch/riemann/blob/0f82df3bf1d0bc669a1bbca09f8404b77c6fecde/standalone/2026-09-21-native-covariance-compression/PROOF.md).
   The inherited facts are the literal truncated Möbius convolution and its
   strict finite inverse identity below `(Y+1)^2`. They are reproduced in
   Section 2 of the new proof, including the first excluded coefficient.

2. **Previously published block partition.** PR #974, commit
   `89c37b6707cb77fc5a86143ea98d8756759fdcbc`,
   [three-route continuation](https://github.com/GettysburgResearch/riemann/tree/89c37b6707cb77fc5a86143ea98d8756759fdcbc/standalone/2026-10-17-three-route-continuation).
   The present projection consequence applies to any complete orthogonal
   block partition, including that packet's native annulus-respecting one.
   Its analytic short-interval import is **not** needed for the new
   low-product estimate. No #974 file is modified.

The harmonic asymptotic, finite Fourier identity, reduced-frequency grouping,
divisor estimates, geometric-sum bound and Schur inequality needed here are
proved directly. No external large-sieve or zero-free theorem is an input.

## Nearby work inspected, not used as an input

- **#972**, commit `4fe7aea61e8bfd3a8ae14fd4daaf1292b4392e32`,
  [Dirichlet-product and angular-ray packet](https://github.com/GettysburgResearch/riemann/tree/4fe7aea61e8bfd3a8ae14fd4daaf1292b4392e32/standalone/2026-10-17-dirichlet-power-and-ray-cancellation).
  Its unconditional angular-ray mean is an average over a growing family,
  with a non-negligible principal-member extraction cost. Its rational
  additive-phase bounds are conditional on its pinned common zero-free
  strip input. Neither statement supplies the required high-product
  Newton amplitude recurrence. The present estimate assumes neither one.

- **#975**, commit `edbc27b61208ccc7ee1fa99fa3f4e861f5a03452`,
  [PR record](https://github.com/GettysburgResearch/riemann/pull/975).
  The PR scope concerns extraction of the resonant divisor, transverse
  finite-part normalization and multiplicity. Its metadata were checked
  for overlap in this pass; none of its proposed conclusions is imported
  into the Newton estimate.

- **#976**, commit `92a0f2c9c4855f03558a93ede0ddbf2892b946d4`,
  [PR record](https://github.com/GettysburgResearch/riemann/pull/976).
  This is the recovery of the historical complementary eighth-moment
  packet. Its metadata were checked for overlap in this pass; no
  moment or proposed global boundary from it is an input here.

These records distinguish dependencies from nearby concurrent work. They
are not an independent approval of the full imported PRs or a claim that
later repository activity has been exhaustively audited.
