# Sources, reading scope, and credit

All local claims are proposed. No independent mathematical review, external proof replay, or new accepted zero-free theorem is asserted.

## Pinned repository sources

- #949, cdb0666fc48d5166f5edd81f394b13e2001a6b5d:
  https://github.com/GettysburgResearch/riemann/blob/cdb0666fc48d5166f5edd81f394b13e2001a6b5d/standalone/2026-10-16-dedekind-quasi-rh-import/RENORMALIZED_CERTIFICATE.md
  Read in full. Parent of this packet. Supplies the phase-correct local normalization, physical signed transform, and actual-source Mellin contract. Its local supplied ZIP was inspected; its upstream snapshot remains a selected import, not a complete Lean build.
- #948, 05b6f2172c686356ccd9900d33ffc5f526c5e98b:
  https://github.com/GettysburgResearch/riemann/blob/05b6f2172c686356ccd9900d33ffc5f526c5e98b/standalone/2026-10-16-dedekind-quasi-rh/EULER_STRIPPING.md
  Read in full. Already proves the coupled 0/1/6 polynomial, the critical log^(12[F:Q]) comparison and the isolated-stripping cost. Its Section 5 explicitly separates the Gaussian adapter. These are predecessors, not new claims of this packet.
- #946, c90818b3a671bb3d124019f3be93a439697deab1:
  https://github.com/GettysburgResearch/riemann/blob/c90818b3a671bb3d124019f3be93a439697deab1/standalone/2026-10-13-positive-singleton-flow/MATHEMATICS.md
  Sections 1--6 read, including the Mammen law, Peano kernel, coercive remainder and signed restoration. The local positivity mechanism is credited to that argument. The law and Peano technique are classical.
- #936, eb8d23decc003d36ded287dc98868308192cc889:
  https://github.com/GettysburgResearch/riemann/blob/eb8d23decc003d36ded287dc98868308192cc889/standalone/2026-10-13-rough-conductor-localization/checks/check_rough_projection.py
  The primitive Eisenstein helper is copied unchanged as checks/eisenstein_source.py, Git blob 64d21a7f400f5bf5654fd67735743ff1befab067. Its code was inspected. The new direct and polynomial checks share this helper; they are not independent primitive backends.
- #940--#947 and #948 FIELD_MOMENT_BRIDGE.md: the current conversation's pinned reports and live PR descriptions supply the comparison map only, except for the full #946 source listed above. Their complete analytic proofs are not silently treated as new imported premises. No full historical priority audit was performed.

## External source and version limits

Cureton--Thorner, A quasi-Riemann hypothesis for Dedekind zeta functions:
https://hexagonmath.org/2610.00200v1
https://hexagonmath.org/2610.00200v2

The landing index records v1 on 12 October 2026 and v2 on 14 October. Direct manuscript access failed again in this pass. Sibling #948 reports that the v1 PDF states 1-1/6000 while v2 states 31/32. This packet does not independently verify that PDF comparison; it relies on the pinned FORMAL LOCAL ALGEBRA and the already-transcribed source contract, not a claim that the v1 PDF was read.

Formal source pin:
https://github.com/AxiomMath/DedekindZetaZeroFree/tree/09afbb4ce6570c1615d58509dc197fc9f0956b7d

The authors report a Lean formalization of the all-number-field and finite-order Hecke 31/32 statements. No Lean executable is installed in the execution environment, and no build, comparator or transitive axiom audit was run. The imported 31/32 theorem is not needed for the new coefficient bounds or the random-reference theorem. The identification with the actual theta detector does retain its explicit source dependencies from #949.

## Classical mathematical inputs

Euler multiplication, unrestricted Dirichlet convolution, Gaussian Fourier/Mellin inversion, the Weierstrass criterion for normally convergent products, Minkowski, Holder and Peano's formula are standard. Their relevant uses are proved or explicitly calculated in the notes.

The fixed-field count I_F(T)<=A_F T is a classical ideal-counting fact; A_F is permitted to depend on the field. The prime-ideal upper bounds used in the growing-order calculation follow from the rational Chebyshev bound and at most [F:Q] primes over each rational prime. The lower bound demonstrating a necessary logarithm is restricted to F=Q and proved via the elementary squarefree inversion formula. No discriminant-uniform ideal asymptotic, GRH, theta-moment improvement, or finite-order assertion about the angular b-profile is assumed.
