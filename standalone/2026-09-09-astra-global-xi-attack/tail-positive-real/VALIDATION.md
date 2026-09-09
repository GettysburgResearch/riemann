# TPR26 — scope, external inputs, and replay contract

Date: 2026-09-09. Author evidence, not independent referee acceptance.
The code checks bounded algebra and a source-bound finite transfer. It does not
prove the all-N analytic statements or the missing full Laguerre sign.

## Exact source scope

Read freshly: #835 metadata, its complete GLOBAL_ATTEMPT.md at
`815ccae329a17327b873d21f05bc30c24db13e7e`, and its discussion (empty at the read).
The supplied parent ZIP was extracted, and the three consumed files were
matched to their known Git blob identities, SHA256 hashes and byte lengths.
The fixed identities are in SOURCE_LOCK.json and in the checker. No mutable
branch name determines primitive acceptance. All seven original parent files
are preserved in the downloadable combined bundle, not republished as new work.

The original finite certificate is for F_3, not for Xi. Its actual defining
integrals include all152 prescribed cells, degree80 Taylor-Cauchy quadrature,
384-bit outward integer intervals, all three infinite tails, and a complete
Rouche disk inequality. The backend is the parent's original implementation;
this continuation does not describe its replay as an independent numerical
backend or as a large new zeta-zero campaign.

## Mathematical inputs and reading

1. G. Csordas, *Fourier transforms of positive definite kernels and the Riemann
   xi-function*, arXiv:1309.0055, especially its complex Laguerre criterion.
   https://arxiv.org/abs/1309.0055
   The full PDF's criterion page was inspected. The criterion is classical;
   its actual-Xi application remains unproved here.
2. NIST DLMF25.2(iii), Euler-Maclaurin representations of zeta.
   https://dlmf.nist.gov/25.2
3. NIST DLMF5.11, Stirling expansion and error regime.
   https://dlmf.nist.gov/5.11
4. Parent #835, exact theta normalization, modular evenness, and its supplied
   finite certificate. https://github.com/GettysburgResearch/riemann/pull/835

The convex-cosine identity, strip Schwarz estimate, coefficient recurrence,
relative Laplace estimate, and disk-transfer inequalities are proved explicitly
in PROOF.md. General convex Fourier, Schwarz-Pick, Laplace asymptotic and
Rouche methods are classical. No literature-priority claim is made.
Other search hits on theta/orthogonal expansions were orientation only and are
not mathematical dependencies. No suggested RH solution from an unread paper
is imported. The main tail estimates do not use PNT, an off-line-zero assumption,
zero simplicity, or a computational zero table.

## The accepting interface

Eight regular files and exactly seven checksum entries are required. Parent
proof, source code and output have separate fixed Git/SHA256/length checks.
JSON must be a nonempty object without duplicate keys, float or nonfinite
numbers. Canonical typed comparison distinguishes booleans from integers.
Expected-result equality is against a fresh reconstruction. Normal checks do
not trust a supplied false theorem flag; rh_proved and full_laguerre_sign_proved
are fixed false. Acceptance never uses Python assert.

The exact finite work consists of:

- derivative-polynomial generation from the defining theta summand, independent
  comparison with the stated first/second derivative polynomials;
- five all-Q shifted-polynomial certificates, their curvature factorization,
  exponential-moment/ratio constants and the rescaled derivative coefficients;
- fifteen Gaussian-rational evaluations of the first Laplace correction;
- exact recombination of the parent's source-bound derivative/residual receipt
  with the new complete-tail lower bound and the radius10^-35 disk margins.

These are bounded controls, not a finite proof of an infinite quantifier.
All new acceptance arithmetic uses standard-library integers and Fractions.
No floating-point value, gamma, zeta, quadrature oracle, or approximate root
finder is used by this continuation. The original root center was selected by
the parent's disclosed scout; the bound comes from its directed replay.

`--emit` is explicitly a producer mode. It skips the new package seal, but still
requires the exact fixed consumed parent blobs. It must not be cited as a PASS.
Default `--check` authenticates and transfers the fixed parent's bounds.
`--full --check` additionally executes the authenticated parent producer, and
requires its complete output bytes to equal the frozen parent receipt. Results
from the two modes are the same mathematics, not independent implementations.

## Commands and completed run scope

Run from this directory in the combined repository-shaped bundle:

```
python -I -S -B check.py --check verification.json
python -I -S -B -O check.py --check verification.json
python -I -S -B test_check.py
python -I -S -B -O test_check.py
python -I -S -B check.py --full --check verification.json
python -I -S -B -O check.py --full --check verification.json
```

The final execution receipt delivered alongside the archive records actual
exit codes and output identities. Normal and optimized parent-only runs also
completed, with byte-identical2638-byte output matching root_certificate.json.
Those runs used the unchanged parent command
`python -I -S -B [-O] certify_truncation.py --check root_certificate.json`.
The parent-only run times were29.106 and30.676 seconds; these are measured past
execution durations, not estimates of a future task.

Four new test methods include one pristine copied-package CLI control and
seventeen distinct actual CLI refusals in each mode: six resealed semantic
result changes; two resealed producer changes; source-lock and parent-byte
drift; duplicate and floating JSON; changed unsealed proof; missing/extra file;
empty manifest; and a proof-file symlink. Source-level mutations are tested
against reconstruction, not merely stale hashes. Linux symlink execution is
recorded; no Windows execution is claimed.

An attempted streaming container command failed because interactive sessions
are unavailable. The subsequent ordinary subprocess runs completed; the failed
streaming request is not counted as a completed validation. A combined full-replay
orchestration also hit its tool timeout without a completed receipt. The later
standalone runner completed the two full checks in sequence; only those retained
completed commands are counted. No mathematical source change was required.

The final bundle is replayed after clean extraction. A temporary-Git add-only
application preserves the seven original parent files and an unrelated sentinel;
this is not a full Riemann checkout/build. Remote byte verification and exact
head publication are recorded separately, so publication is not asserted by a
local document alone. No predecessor unit-test suite, full repository audit,
Lean build, remote CI success, or independent analytic acceptance is claimed.

## Review first

Check (i) the sign in the tilted curvature inequality with P1<0;
(ii) complete omitted-index summation and its uniform ratio estimate;
(iii) both frequency regimes of the relative Laplace bound, especially the
endpoint derivative in the second integration by parts; (iv) the real-to-complex
strip map and its constants; (v) the raw-truncation horizon's logarithmic term;
and (vi) the transfer from a changed-source root to the original zero-free disk.

The numerical disk statement is deliberately small. The uniform tail reference
has relative error256/q, which need not be small for the first few indices.
Positive real part of T_N does not give the full Laguerre sign of F_N+T_N.
The logarithmic-derivative estimates retain the mixed term in PROOF.md(30).
The missing assertion is the original global sign, not routine tail bookkeeping.
