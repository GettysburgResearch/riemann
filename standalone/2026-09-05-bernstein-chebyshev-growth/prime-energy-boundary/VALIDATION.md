# Validation and independent-review contract

Status: author-run finite exact verification; analytic review pending.
The original all-epsilon inequality and RH are not proved.

## Executed from the locally extracted, blob-authenticated parent packet

The new checker has 1,192 exact rational/Gaussian-rational controls. The
coincidence with the older higher-power check count is only numerical: these
are separate suites, with different files and distinct output hashes.

New normal and optimized outputs are byte-identical and match result.json:

    SHA256 536ac173d9301fc36ed119e95bb47d0287b4c47ff44f87002cdfbc7c75080086

The new suite checks ordinary/minus-one polynomial conversion, derivatives,
recurrences, exact weighted moments through degree 32, complete bivariate
CD identities through degree 20, 500 confluent/distinct evaluation controls,
finite signed Gram contractions, the two continuum corrections, the cubic
diagonal normalization, the boundary-weight telescoping sum, Gaussian-rational
Cayley poles and their coefficients, repeated-multiplicity residues, and the
local area-defect constant. Rational model weights are not prime data.

Three inherited suites were freshly rerun in normal and optimized Python:

- original: 1,922 controls per mode; output hash
  08e78f90039edaa845819384e412803b31a8c84d658b183224b2b3f421311cb6;
- arithmetic: 1,795 controls per mode; output hash
  13d64322e8fb14797c8a6615c098b66e860e45f6b00411d5e17ddd30ae9b0b67;
- higher powers: 1,192 controls per mode; output hash
  94cef00a3e0887c257b81c6cb7e69824e651e9d308032ac2e601e0a18145952c.

The exact commands, exit codes and outputs are in REPLAY_LOG.json. No
repository-wide suite, GitHub Actions job, or independent execution is
implied by these packet runs.

## Twelve deliberate refusals

Each mutation was made in an isolated temporary copy and run in both normal
and optimized mode. Every run returned exit code one for its intended reason:

- saved continuous-diagonal slope changed from 2/3 to 1/3;
- integer degree 32 replaced by float 32.0;
- new PROOF.md bytes changed;
- new BOUNDARY.md bytes changed;
- parent commit in SOURCE_LOCK.json changed;
- authenticated higher-prime-powers/PROOF.md bytes changed.

The checker uses explicit exceptions rather than Python assertions. It rejects
duplicate JSON keys and performs recursive type-sensitive comparison. Its
source lock is checked against literal parent commit/blob constants, not just
a mutually consistent caller-supplied manifest.

## What the checker does NOT prove

It does not prove PNT, large-degree asymptotics, infinite prime sums, global
radial norms, infinite Fourier means, meromorphic continuation, the absence
of off-line zeros, or the source-specific energy inequality. Nor does it
certify the numerical values of any actual prime-weighted coefficient.

The independent proof-review targets are:

1. PE-1: the 1/9 measure normalization, the 6n weighted moment, integration
   endpoints, the O(n) full variation and localized O(T+sqrt(nT)) variation,
   and the PNT split at T proportional to log^2 n.
2. PE-2: the alpha=-1 recurrence telescope, the sign of its confluent limit,
   and absolute fixed-degree double integration against the signed source.
3. PE-3: no claim that a cubic diagonal alone blocks a subexponential proof;
   any genuine polynomial-loss comparison would suffice. Check the factor
   16/9 and squared multiplicities in the conditional energy limit.
4. PE-4: the perturbed source uses the same ordinary primes but different
   weights; verify the 1/4-m residue and the prime-series continuation near
   the two shifted arguments. This is not a zeta counterexample.
5. BR-1: verify the normally convergent Cauchy representation away from
   poles, summability for p>1/2, extension to all p<1 by norm monotonicity,
   and the distinction between meromorphic integrals and analytic H^p.
6. BR-2: verify the normalized area weights, the local log divergence,
   factor 243/16, and the fact that global area finiteness is still open.

No proof files were silently amended in the parent. An independent reviewer
should review the exact published continuation head, not assume acceptance
from the fact that the finite checks pass.
