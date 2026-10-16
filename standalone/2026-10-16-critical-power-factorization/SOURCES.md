# Sources, versions, and scope of the comparison

Reviewed against connected GitHub on 2026-10-16.

1. GettysburgResearch/riemann PR #949, cdb0666fc48d5166f5edd81f394b13e2001a6b5d:
   standalone/2026-10-16-dedekind-quasi-rh-import/RENORMALIZED_CERTIFICATE.md.
   Read in full. Existing result: multiply out the original sixth-power
   denominator; obtain a nonvanishing numerator on Re(s)>1/2 and the exact
   weighted Mobius dilation. The critical estimate is explicitly open.
   https://github.com/GettysburgResearch/riemann/blob/cdb0666fc48d5166f5edd81f394b13e2001a6b5d/standalone/2026-10-16-dedekind-quasi-rh-import/RENORMALIZED_CERTIFICATE.md

2. PR #948, 05b6f2172c686356ccd9900d33ffc5f526c5e98b:
   standalone/2026-10-16-dedekind-quasi-rh/EULER_STRIPPING.md,
   Git blob 80f6d1061098c666bcc06a4c949c145a148bf358.
   Read in full, as was IMPORT.md. Existing results: the same normalized
   numerator, the 0/1/6 source, two-way critical logarithmic comparisons,
   general-field extraction, and the warning that the Gaussian adapter was
   separate. Those are credited, not rediscovered as new claims here.
   https://github.com/GettysburgResearch/riemann/blob/05b6f2172c686356ccd9900d33ffc5f526c5e98b/standalone/2026-10-16-dedekind-quasi-rh/EULER_STRIPPING.md

3. Cureton--Thorner, A quasi-Riemann hypothesis for Dedekind zeta functions,
   Hexagon 2610.00200. Live search found a v1 landing record advertising 31/32
   and a history listing v2 (October 14). Direct PDF and TeX requests failed
   in THIS pass. PR #948 reports that the v1 PDF instead states 5999/6000,
   while v2 states 31/32. This distinction is recorded as #948's inspected
   source report, not a PDF verification independently repeated here.
   The preceding answer's 31/32 statement concerned the formal release;
   it should not be treated as verification of the linked v1 PDF theorem.
   https://hexagonmath.org/2610.00200v1
   https://hexagonmath.org/2610.00200v2

4. AxiomMath/DedekindZetaZeroFree formal release at
   09afbb4ce6570c1615d58509dc197fc9f0956b7d, preserved in #949's selected
   import. The pinned local Euler polynomial is the starting datum here.
   The live upstream README reports a 31/32 Dedekind/finite-order Hecke
   theorem and standard Lean axioms. No Lean build, comparator, transitive
   axiom audit, or full automorphic proof was run in this pass. No statement
   about broad mathematical acceptance is inferred from that README.

5. PRs #944--#947: current descriptions read in the live newest-PR search;
   previously discussed source-qualified results retained. Their conductor
   localization, compensated phases, positive singleton flow, and coherent-row
   separation are strategic context, not analytic premises of PROOF.md.
   The branch #946 still leaves I_k<=D_k+diagonal open. #947 explains why a
   large finite degree cancellation ratio does not supply a power saving.

The new algebraic generalization to m>=2 has not been supplied with an
automorphic realization. No theorem for all covers or growing fields follows.
The formulas deliberately retain field degree in constants and use finite
row measure rather than an infinite norm-only element ball in positive unit
rank. Exclusions over 2 and 3 are explicit, not silently inserted later.

Classical credit: Euler products, Dirichlet convolution, Gaussian Mellin
inversion, Minkowski, and Euler's divergence of prime reciprocals. Every
estimate needed for the new correction norm and Gaussian adapter is proved
in the two local notes. No new subconvexity, large sieve, prime-ideal theorem,
or imported quasi-RH estimate is needed for those component estimates.
