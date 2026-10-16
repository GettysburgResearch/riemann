# Critical-power factorization and the literal Gaussian detector

**Status: PROPOSED, NOT PUSHED.** This packet was developed after reading live
PRs #948 and #949. No full RH proof, native higher-moment bound, or improved
zero-free exponent is claimed. No independent mathematical review was run.

## Results

For every integer m>=2, the coupled local polynomial

    1-(1-1/q)a_p x-b_p q^(m/2-1)x^m

factors into

    (1-a_p x)(1-b_p q^(m/2-1)x^m) U_p(x).

With all primes above 2 and 3 excluded, U and U^-1 have phase-uniform absolute
Dirichlet coefficient norm at weight 1/2 at most exp(5[F:Q]), independent of m.
They are holomorphic and nonzero for Re(s)>m/(2(m+1)); the m=6 correction has
critical coefficient tail O(T^(-1/14+rho)). The 3/7 threshold is a threshold
for this correction, NOT a zeta zero-free region.

The two-channel comparison keeps the degree-(m+1) shared-prime term. Dropping
it would falsely impose coprimality and break the source identity. Literal
row masks, equal-norm distinct prime ideals, and all shortened scales remain.

The infinite convolution is then proved for the SAME Gaussian used by the
Dedekind detector. This completes the explicitly open compact/Gaussian adapter
in #948 and matches #949's normalized signed probe to a physical coefficient
sum. Its critical all-epsilon estimate remains equivalent to a native scalar
Gaussian Mobius estimate, not an independently controlled new source.

## Read

- PROOF.md: exact theorem, critical norms, continuation, kernel tails.
- GAUSSIAN_ADAPTER.md: infinite sums, same-height contracts, source matching,
  and an explicitly OPEN sufficient dyadic mean-square estimate.
- SOURCES.md: original credit, latest-work reading levels, and access limits.
- VALIDATION.md and RESULTS.json: exactly what was executed.
- chks/check.py: standard-library exact diagnostic, with negative controls.
- draft_pr.md: prepared publication description.

## Publication

The target base is #949 commit cdb0666fc48d5166f5edd81f394b13e2001a6b5d.
Proposed directory: standalone/2026-10-16-critical-power-factorization/.
The accompanying patch and apply_to_repo.py are add-only, reject an existing
target directory, and do not commit, push, or alter earlier work automatically.
The active GitHub connector supplied only read actions; CLI publication failed
because the container could not resolve github.com. No remote commit or PR
number has been manufactured. A local fixture is not a clone of the full repo.

## Assessment

The new gain is removal of residual correction costs and an actual Gaussian
interface, not proof of the critical signed estimate. The next substantive
calculation must estimate B (or OPEN-G2) in GAUSSIAN_ADAPTER.md using the original
signed theta/Poisson representation. A norm bound for U alone cannot do that.
