# Review contract and sources

Status: author-submitted component proofs; no independent verdict.

## Inspect first

1. The Cayley normalization, A(0)=1, and absence of a singular inner factor.
   Equation (1.3) prices the EXPONENTIAL target of norm one, not the ramp.
2. The projection formula for 1-w and the sharp cubic loss. Derive the two
   first coefficients of P_+(conjugate(B)(1-w)); a sign error changes the cost.
3. The strip constraint Re a<=|a|^2, logarithmic-derivative summation, and
   convergence with multiplicity. Check the interval 0<=J<1 in Section 3.
4. The Toeplitz cofactor relation and direction of the entropy approximation.
   Every finite quantity is an UPPER approximation to J. HC1 is a separate
   pending-review dependency only for its quantitative rate.
5. The fixed certificate: genuine source g, all primitive integration states,
   target exp(-t/2), all signed polynomial terms, and the infinite tail.
6. The OPEN assertion J<=0. It must not be inferred from J<0.027, projection
   monotonicity, functional-equation symmetry, or a rate toward a true floor.

## Exact project sources

- PR #817 at 1f97efdcf9dacd24351ecff0819c524f9bf40ec3:
  standalone/2026-09-07-astra-quantitative-capture/PROOF.md,
  Git blob 47c51b2f91a2d52c9f9ab91c642ed207042992ca, 23351 bytes.
  Only the rate corollary invokes HC1. Its manuscript was read; its code and
  infinite analytic proof were not newly independently reviewed or rerun.
- FR26 at cc5277c34fdbc48787cf650b4627a44a77862f1d:
  standalone/2026-09-07-astra-future-realization/interval_core.py,
  Git blob 92f484bc6bc7b12bf26313bd7d323c637cd834b9, 9799 bytes.
  This file is copied byte-for-byte. It implements 160-bit directed integers,
  logarithm/atan remainders and rational/Gaussian-rational operations. Reuse
  is disclosed, not described as an independent arithmetic implementation.
- The original source formula, analytic removable normalization and
  polynomial all-pass realization are reconstructed in Section 0; their
  project lineage runs through PR #804, FR26 and the optimal-tail manuscript.

SOURCE_LOCK.json records SHA-256 as well as Git identities. The runtime checks
its copied executable core. It does not fetch or execute the remote HC1 proof.

## Classical primary sources and limits of inspection

- M. Balazard, E. Saias and M. Yor, *Notes sur la fonction zeta de Riemann, 2*,
  Advances in Mathematics 143 (1999), 284-287. The weighted logarithmic
  equality and zero sum are classical; no priority is claimed.
- H. M. Bui, S. J. Lester and M. B. Milinovich,
  *On Balazard, Saias, and Yor's equivalence to the Riemann Hypothesis*,
  arXiv:1306.0856v1; J. Math. Anal. Appl. 409 (2014), 244-253.
  https://arxiv.org/abs/1306.0856
  The primary abstract/bibliographic record was consulted for attribution.
  Its RH-conditional truncation estimates are NOT used as unconditional inputs.
- M. Kunik, *Logarithmic Fourier integrals for the Riemann Zeta Function*,
  arXiv:0804.4829v2. https://arxiv.org/abs/0804.4829
  The primary abstract was consulted to identify prior Poisson--Schwarz and
  Blaschke-factor work. No theorem from an uninspected full paper is imported.
- NIST DLMF 25.4, https://dlmf.nist.gov/25.4:
  the classical functional equation and xi reflection, with original references.
- NIST DLMF 5.11, https://dlmf.nist.gov/5.11:
  Stirling normalization and periodic-Bernoulli remainder background. The
  full source-tail inequality used by certificate.py is derived in PROOF.md.

Other classical inputs are Hardy factorization/outer cyclicity, Jensen,
Schwarz--Pick, the outer Poisson formula and Parseval. Their precise uses are
spelled out; finite tests do not certify these analytic theorems. The finite
prediction identity is a Szego-type identity, not claimed new.

## Research assessment

This pass is useful as an exact assessment of what remains and how different
targets measure it. It does not make the intrinsic defect an easier problem
than the classical logarithmic criterion. The sharp sensitivity result and
new full-tail certificate should be reviewed separately from the open equality.
