# Sources, dependencies, and inspection boundaries

## Repository sources

The live GitHub connector was used, rather than treating conversation memory
as current repository state. The latest PR search in this pass returned #952
as newest; #948 through #952 are unmerged research drafts, not integrated
mathematical approval. Root AGENTS.md and the README reading guide were read.

1. **#952**, head `3b7d2948840446c752bbf284f6f90f6592395a29`,
   `standalone/2026-10-16-critical-gaussian-energy/ENERGY_THEOREM.md`.
   The live source was read through E1--E11 and the explicit open energy
   target. Its coefficient counts, exact second-energy kernel, logarithmic
   literal ideal diagonal and warning about distinct equal-norm ideals
   motivate this continuation. The relevant formulas are reconstructed in
   THEOREM.md rather than silently assuming its full-moment target.
   No #952 code, independent review, or whole-repository validator was run.

2. **#950**, head `5a6418b021a35c95bbc2c80775353ee33506faee`,
   `standalone/2026-10-16-critical-geometric-lift/`.
   The user-provided archive supplies the geometric source used here. Its
   local factor, with exponents 1,7,13,..., is retained. The new estimates
   are proved directly for all four stated factors; they do not use the
   pre-Poisson identity or its unproved signed bound as analytic inputs.
   This is the frozen application base for the add-only patch, not a claim
   that the full base was cloned into the current container.

3. **#951**, head `aba76e1df38dc438b9f5c5f20b698fb26fb1716e`:
   PR-description scope in this pass. The general m coupled/two-channel
   factors and Gaussian scope are credited. Its critical comparison and
   compensation theorem are not inputs to the norm-fiber proof.

4. **#948**, `05b6f2172c686356ccd9900d33ffc5f526c5e98b`, and **#949**,
   `cdb0666fc48d5166f5edd81f394b13e2001a6b5d`: earlier import/normalization
   provenance. Their imported quasi-RH theorem is not an input here.
   This pass did not obtain a fresh Hexagon manuscript body, PDF, or Lean
   build and does not certify an upstream formalization.

5. **#940/#942/#944/#947**: their sector descriptions in the supplied project
   context and live PR metadata are used only to delimit the comparison:
   smooth singletons, low total radical, conductor-divisor windows, and
   coherent physical rows are not identical to rational product-norm
   equality. The conjugate-prime witness is proved directly. This is not
   an exhaustive comparison with every old sector or a dominance claim.

6. **Unpushed ramified-dilation packet**, provided as
   `riemann-ramified-dilation-20261016.zip`. All nine original files, including
   the original manifest, are copied unchanged into the sibling directory.
   Its checker and manifest were freshly replayed in both Python modes.
   None of its Gauss-sum operator bounds is required for the new theorem.
   Old source-reading statements belong to that prior packet, not this pass.

Useful exact source URLs:
- https://github.com/GettysburgResearch/riemann/blob/3b7d2948840446c752bbf284f6f90f6592395a29/standalone/2026-10-16-critical-gaussian-energy/ENERGY_THEOREM.md
- https://github.com/GettysburgResearch/riemann/blob/5a6418b021a35c95bbc2c80775353ee33506faee/standalone/2026-10-16-critical-geometric-lift/MATHEMATICS.md
- https://github.com/GettysburgResearch/riemann/pull/951

## External primary literature and classical inputs

**Benjamin Durkan, Nilmoni Karak, Kamalakshya Mahatab**, *Sharp Upper Bounds
for Moments of Dedekind Zeta Functions*, arXiv:2606.27516v3, dated 27 July 2026.
HTML Introduction, the definition of Z_ij, Theorem 1.1, Corollaries 1.2/1.4
and their permutation-character discussion were inspected directly:
https://arxiv.org/html/2606.27516v3

That source explicitly records the double-coset/ordered-embedding-pair
invariant and the corresponding product of fixed-field Dedekind zetas.
Its critical-line moment theorem assumes GRH. We DO NOT use that theorem.
We use the same classical algebraic structure only for a positive coefficient
Euler series on the right of one, proving the required local comparison.
The paper itself also states the positive simple-pole facts used here.
This is not a claim to discover the covariance invariant or to remove GRH
from their full-moment theorem.

The following are named standard unconditional inputs, not discoveries:
- fixed-field ideal counting I_F(T)<=A_F T;
- the positive simple pole of Dedekind zeta at one;
- finite etale algebra decomposition and finite-field tensor products;
- Euler products, positive Rankin bounds, Cauchy/Schur and Fubini/Tonelli.

THEOREM.md proves the finite-field tensor description, the local coefficient
majorant, all Gaussian identities, and the particular positive Laplace
Tauberian implication used for the asymptotic. The latter is a reconstruction
of the classical Karamata method, not a new Tauberian theorem. No original
Karamata paper or general Tauberian text was independently re-proved or
fully reviewed here. EXAMPLES.md derives the quadratic Euler factors and
its elementary L(1,chi_-3) integral explicitly.

No Chebotarev, prime ideal distribution, quasi-RH, RH/GRH, Artin holomorphy,
new large sieve, theta foundation, or conjectural cancellation is an input
to NF1--NF3. The example using unbounded split primes is only illustrative;
the analytic estimates do not rely on it. No global literature-priority
claim or independent mathematical referee report is made.
