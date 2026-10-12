# Directed continuum run for the phase-aware dimension-eight sector

Date: 2026-10-10. This applies the independently reviewed continuum source
calculation and weighted primitive mechanism to the phase-aware sector.
The long run is pending. Sampled signs below are discovery evidence only.

`enclose_residual_phase8.py` is a parameter-specialized copy of the reviewed
`enclose_residual.py`. Differences affecting the mathematical enclosure:

* exactly five removed sine modes (all other removed counts are rejected);
* exact supporting line/gap from `CODIMENSION_8_PHASE_REFINEMENT.md`;
* the scalar lower cost is27/2, rather than15/8;
* omitted normalized intervals useepsilon2^-50;
* Gaussian order76, with the same error8hB2^-2n;
*636 exact contiguous panels replace696 because the endpoint cutoff is wider.

The whole derivation in `CONTINUUM_RESIDUAL_DERIVATION.md` applies with these
substitutions. The actual length is stillL=1; no window extension or source
approximation is made. Every omitted physical interval has length at most
2^-50. The source-modulus and four exact-anchor checks give variation below
0.000155 and anchorabs(F)<1, henceabs(F)<2 there. The resulting FF andpF
entry radii are24epsilon and36epsilon, respectively.

The larger scalar residual lower bound is expected to be inconclusive.
An ordinary2000-node experiment found two negative scalar lower eigenvalues.
The independently reviewed weighted primitive estimate, using128 exact
cosine moments and an enclosed infinitecosinetail, gives a sampled minimum
ofapproximately3.49e-10. This is not a certified sign: the quadraticR integral
in that experiment is ordinary quadrature.

The directed run encloses that actual quadraticR integral. Its final receipt
may report the scalar lower bound as inconclusive while still supplying a
valid completeR enclosure. `enclose_weighted_lower.py` then applies the
weighted dual matrix bound to that enclosure; only strict outwardLDL
acceptance establishes a single-window conditional sign. It cannot establish
all-window positivity, thexi/Weil adapter, orRH.
