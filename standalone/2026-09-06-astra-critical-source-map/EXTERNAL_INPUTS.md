# Classical inputs and overlap

1. Euler summation for zeta, NIST DLMF 25.2.8:
   https://dlmf.nist.gov/25.2
   CONSTRUCTION derives the needed one-step formula directly from floor(exp t)
   and absolute convergence, then uses its analytic continuation on Re w>0.
2. Euler's beta integral and gamma recurrence:
   https://dlmf.nist.gov/5.12
   Used only with positive beta parameters/positive real parts. Gamma log
   convexity and gamma_E<1 supply the elementary short-time estimate. The
   infinite analytic identities are not proved by the finite checker.
3. Standard Hardy Paley--Wiener, inner--outer factorization, and cyclic
   subspaces. A. Beurling, On two problems concerning linear transformations
   in Hilbert space, Acta Math. 81, 239--255, DOI 10.1007/BF02395019; P. D.
   Lax, Translation invariant spaces, Acta Math. 101 (1959), 163--178,
   DOI 10.1007/BF02559553. Only the classical scalar theorem is used. The
   absence of singular inner factors for the actual D_b is justified in text.
4. M. Suzuki, A canonical system of differential equations arising from the
   Riemann zeta-function, arXiv:1204.1827 (v2, 2016):
   https://arxiv.org/abs/1204.1827
   Prior work on these actual xi quotients, arithmetic kernels, innerness and
   canonical systems. Its small-shift innerness is not imported as a theorem.
5. L. Baez-Duarte, A strengthening of the Nyman--Beurling criterion for the
   Riemann Hypothesis, arXiv:math/0202141:
   https://arxiv.org/abs/math/0202141
   F. Alouges, S. Darses and E. Hillion, Polynomial approximations in a
   generalized Nyman--Beurling criterion, arXiv:2006.02953:
   https://arxiv.org/abs/2006.02953
   These establish the relevant approximation lineage. We do not import an
   unproved coefficient bound or claim the general cyclicity idea is new.

Web retrieval in this pass checked bibliographic/abstract and DLMF HTML
sources. No PDF page audit or exhaustive specialist novelty comparison is
claimed. All theorem uses are explicitly stated rather than inferred from an
abstract. No PNT, zero density, finite zero verification, RH-conditional
formula, or distribution of hypothetical zero ordinates is an input.

Exact repository predecessors are in SOURCES.tsv. In particular PR403 already
contains the Hardy/model-space defect mechanism, which is credited rather
than claimed as an independent discovery here.
