# Sources, provenance, and limits of attribution

## Actual source and delivered predecessor

The literal factorial source, its removable-value convention, compact inverse,
and periodic-Bernoulli remainder were read at:

- `GettysburgResearch/riemann` PR #804,
  `0f6ee91f1a8c8bece1618bde155d62fb0bfb4cad`,
  `standalone/2026-09-06-astra-compact-domain-completion/PROOF.md`.
  https://github.com/GettysburgResearch/riemann/blob/0f6ee91f1a8c8bece1618bde155d62fb0bfb4cad/standalone/2026-09-06-astra-compact-domain-completion/PROOF.md

The complete OC26 optimal-tail manuscript and eleven-file packet were available
as the user's delivered archive `riemann_optimal_tail.zip`. The manuscript was
read in full. It supplies the fixed-horizon optimal-cost interpretation and
arithmetic future hierarchy, not a growing-horizon rate. At the checks performed
in this session the anticipated parent branch was not yet returned by the ref
endpoint. Its publication is therefore NOT claimed as independently verified.
No dependency on the other agent's unpublished work is needed here.

`interval_core.py` is preserved byte-for-byte from that delivered packet's
`mathcore.py`, including its unused legacy routines. Its actual SHA-256, Git
blob identity and length are in SOURCE_LOCK.json. The new driver compiles it
only after authentication. The new certificate and tests do not execute the
parent's earlier producer, checker, or test suites. Reuse of code is not called
an independent implementation; the new finite polynomial-moment evaluator is
new, and the precise arithmetic imports remain explicit.

## Classical analytical inputs

1. Hardy H2 inner--outer factorization, the Poisson formula for an outer
   function's logarithm, Jensen's boundary inequality, and Cayley/Laplace
   Plancherel. These are standard theorems, for example in P. Duren,
   *Theory of H^p Spaces* (1970). We do not claim a new factorization theorem
   or a newly verified digital copy of that book. The source-domain use is
   also explicitly present in the pinned #804 predecessor. The actual finite
   Gram floor and all its constants are derived in PROOF Section 1.
2. Stirling normalization and Bernoulli remainders:
   NIST DLMF 5.11, https://dlmf.nist.gov/5.11 . The formula and uniform
   all-real remainder needed by the code are reconstructed in PROOF Sections
   3 and 7 rather than equating an asymptotic expansion with a certificate.
3. Classical existence of critical-line zeta zeros:
   NIST DLMF 25.10, https://dlmf.nist.gov/25.10 . This is used only to show
   that the actual Gram matrices have no rank-independent positive floor.
   No zero ordinate, multiplicity value, or verified-height table is imported.
4. The approximation setting and the warning about natural-cutoff convergence:
   L. Baez-Duarte, *Arithmetical Aspects of Beurling's Real Variable
   Reformulation of the Riemann Hypothesis*, arXiv:math/0011254,
   https://arxiv.org/abs/math/0011254 . Its abstract/metadata were checked;
   no theorem from it is silently used to close the present missing rate.

No external novelty or priority is asserted for Hardy factorization, Gram
conditioning arguments, all-pass filters, shift averaging, compact input
approximation, or the general projection method. The contribution is the
explicit source specialization, complete constants, and bounded actual-source
certificate with its preserved horizon and full tails.

## What is not imported or proved

No RH-conditional Mertens estimate, outer property of the actual source,
zero-free critical half-plane, full-source block gain, all-horizon contraction,
remote CI result, or independent referee acceptance is used or claimed.
