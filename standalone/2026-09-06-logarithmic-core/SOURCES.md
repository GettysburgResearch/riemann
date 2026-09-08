# Sources, independence, and attempted closure

## Repository source reads

1. `GettysburgResearch/riemann`, main
   `051808c1f8367b4320c52f94b40908eb2173d622`, root tree
   `115c71ffd64b5f9ab3568185634c9efd07c89333`.
   Read AGENTS.md, docs/REVIEWING.md, and research/RESULTS_INDEX.md.
   Main has advanced beyond the earlier reviewer baseline. This research
   preserves the September 6 integration and makes no new review acceptance.
2. PR #792, head `465cb28ed8cbfa1bb071d9a85eeda9890decfe6b`:
   - `standalone/2026-09-05-bernstein-chebyshev-growth/finite-window-coercivity/PROOF.md`,
     blob `35d8d38a77bee896b0b2e729b095ccdef5d7a50f`.
   - `standalone/2026-09-05-bernstein-chebyshev-growth/energy-schur-reduction/PROOF.md`,
     blob `0d12ff6039dcc79f6576538edeebd2a0c5b539c0` (19,085 bytes).
   Both actual proof texts were read. They supply the source normalization,
   exact tail, constrained multiplier, energy completion and residual
   inequality. PROOF.md rederives the identities used here. The original
   producer/certificate campaigns were not rerun; their sampled actual signs
   remain explicitly noncertifying. This is an extension, not an independent
   approval of the whole PR.
3. PR #790, head `6b309554bf1e2f83a83325cd54038f5a0b9b0014`:
   `HEAT_BERNSTEIN.md` and `pass2/SMALL_TIME_ALL_ORDERS.md` in
   `standalone/2026-09-05-astra-theta-count-closure/` were read. They already
   contain the scalar Bernstein/infinitely-divisible construction initially
   considered in this pass. That result is NOT relabeled as new here. No
   mathematical conclusion in the logarithmic-core proof depends on these
   heat statements or their external finite-zero inputs.
4. A default-branch code search for `Carleman` returned no matches. This is
   narrow discovery evidence, NOT an exhaustive branch or external novelty
   search. Prior A/C review work motivated the question; changing roles does
   not create independent acceptance of our own work.

## Classical analytic inputs

The following are imported background theorems. The new finite checker does
not prove them, and no global RH conclusion is inferred from their names.

- Digamma partial fractions and vertical asymptotics, e.g. NIST DLMF 5.7.6
  and 5.11.2: https://dlmf.nist.gov/5.7 and https://dlmf.nist.gov/5.11 .
  Section 5.11 was read. These give the logarithmic principal symbol and
  bounded remainder on the fixed vertical line. No asymptotic is used as a
  numerical interval bound without a remainder.
- Fourier Plancherel, Schur's test, the representation theorem for closed
  semibounded forms, the compactness criterion in L2, and elementary
  distribution theory at isolated support points. Carleman's bound itself,
  the leakage constant and the interval graph-core argument are proved in
  PROOF.md rather than imported as an opaque domain assertion.
- Classical entire xi, functional equation, genus-zero invariant Hadamard
  product, Riemann--von Mangoldt count and Laplace uniqueness. The actual
  kernel's Laplace identity is verified with its prime and gamma factors
  in PROOF.md. Entire xi always includes its removable values.
- Only for the RH-to-STRICT-positive-certificate direction, the classical
  Littlewood consequence under RH
  `S_arg(T)=O(log T/log log T)` is imported. The needed superlinear DISTINCT
  zero count is derived from its jump bound and Riemann--von Mangoldt.
  A primary published source explicitly stating this input is R. R. Hall,
  "On the Zeros of the Riemann Zeta-Function", Journal of the London
  Mathematical Society 59 (1999), 65--75,
  DOI 10.1112/S0024610798006942:
  https://academic.oup.com/jlms/article-abstract/59/1/65/809995 .
  The publisher's opening/abstract text, including the displayed Littlewood
  bound, was inspected; the full PDF and Hall's subsequent short-interval
  theorem were not audited or imported. No optimized constant is required.
  Carneiro--Chirre, arXiv:1702.04099, abstract, independently identifies the
  classical Littlewood scale; no theorem from its uninspected full text is
  used. The converse certificate-to-RH direction does not use Littlewood.

## Relation to existing theory and the attempted leap

Friedrichs operators, logarithmic multipliers, integral-operator bounds,
regularized least squares, and Fourier uniqueness at dense zero sets are
classical. No external priority claim is made for them or for Weil criteria.
The proposed new repository object is their exact composition for the
source-specific residual left open in #792, with the complete domain and
primitive error contracts.

The attempted final estimate is `C-b^2 G* A_L^(-1)G >= 0` for every L.
A_L is positive, but that does not compare its inverse Gram with C.
Cauchy--Schwarz on the full indefinite form would be circular. The proof
stops at this exact arithmetic inequality. The new strictness theorem is
CONDITIONAL ON RH; using it unconditionally would reverse its hypothesis.
The family of finite certificates is not a single finite proof of RH.

## Not performed

No actual-W positive/negative matrix certificate, large prime or zero scan,
new prime cancellation, external numerical certificate reproduction, formal
Lean/Comparator/kernel build, repository-wide CI, public-release audit, or
independent referee acceptance. Primitive budget existence is proved, but
its complete interval implementation remains to be built. Integer window
lengths make the effective-computability claims explicit.
