# STAR26 execution, scope and failed attempts

Date: 2026-09-12. These are author-run checks, not independent acceptance. The paper and implementation require review. No RH or all-order realization proof is claimed.

## Completed native reconstruction

The clean packet was checked in both normal and optimized Python:

```text
python -S -B verify.py --check result.json --self-test
python -S -B -O verify.py --check result.json --self-test
```

Both reconstruct the same complete canonical internal record (including its terminating newline), SHA256:

```text
5bb25fa347172a1fd53daedda3c70cf9a9f14c9bd202f2b5dd2e18a46faae4cd
```

Each authenticates thirteen payload hashes and the complete fourteen-file inventory. It then recalculates all nine raw native moments, three Fourier values, their entire tails and rounding bounds, two seven-dimensional root-box arguments and both sixteenth-moment inequalities. Neither cached native integrals nor scouting values enter these runs. The readable result.json binds the entire internally reconstructed record by SHA256 and reports the checked margins. `--dump-full PATH_OUTSIDE_PACKET` exports all exact native balls, separate tails, root intervals and inverse hashes; no stored digest replaces any mathematical reconstruction or inequality check.

The source cover is 192 degree-128 cells and all ten specified theta terms per cell: 667 are expanded and 1253 are paid by complete pointwise bounds. Every subsequent theta index, cell Taylor remainder and all t>=3 are included. The finite and harmonic root displacement bounds are below 4.481e-61 and 1.337e-29, respectively; both row-sum derivative bounds are below 1.267e-11. The box radius is 10^-24. Both roots' standardized sixteenth-moment differences are strictly between -.115 and -.114, with center approximately -.11438319548843916.

Each run also performs 1064 rational ball controls, 112 independent biased-sign coefficient checks, 204 complete small-spin moment/cumulant comparisons, 102 independently enumerated score-derivative comparisons, 15 monotone-coupling variance identities, 27 star phase-square identities, and seven elementary/disk controls. Each root reconstructs 98 scalar exact inverse identities. These counts describe finite algebra controls, not independently proved analytic theorems.

## Actual rejection tests

The built-in self-test accepts one fresh pristine comparison, refuses eight altered records through the actual canonical comparison function and rejects duplicate-key JSON through the parser. The altered records cover a false RH claim, false all-order claim, changed spin count, Boolean alias in an integer count, enlarged moment scope, missing source cell, false whole-theta identification and a changed primitive moment integer. They are NOT nine complete numerical CLI subprocesses.

The separate executable-mutation test was run for each case in both normal and optimized Python:

```text
python -S -B mutation_test.py --case native-theta-coefficient
python -S -B mutation_test.py --case star-bias-rule
python -S -B -O mutation_test.py --optimized --case native-theta-coefficient
python -S -B -O mutation_test.py --optimized --case star-bias-rule
```

All four calls completed with the test harness reporting success: each altered verifier itself exited unsuccessfully, AFTER authenticating a newly resealed manifest. Changing the source coefficient from 4*pi^2 to 5*pi^2 failed the mathematical root condition with displacement approximately 1218.01. Changing the star bias from a/100 to a/101 failed it with displacement approximately .000653373. These are not checksum-only refusals. Neither altered source/model was published.

Initial bundled wrapper calls were interrupted by the execution environment and were not counted as complete checks. The split case runs completed; their full logs are retained in the downloadable execution archive. A receipt producer also ran, but a producer output is not mislabeled as a stored-receipt verification.

## Exploration that led to the exact rational centers

The reconnaissance read current repository direction and scope records before changing approach. A broad positive-kernel alternative was not promoted as novel: Suzuki/Hardy already isolates the missing domination problem. The constructive attack instead joined the current Ising work, with the failed Brownian native sign and the gamma approximants' finite nonreal defects as explicit warnings.

Ordinary SciPy/mpmath searches of several small stars, chains and dense block graphs stalled at the desired higher moments. A successful independent-sign/Gaussian-reservoir candidate suggested a star seed. Non-directed continuation first introduced common bias 1/1024, reduced a small-sign reservoir from 65536 leaves to 64, then changed the biases continuously to a_i/100. The final leaf-group counts are (1,1,1,1,1,1,1,24,64); with the hub these give 96 spins. The selected smaller-reservoir N=32 solve failed; no impossibility or minimality conclusion is inferred.

The rational centers were selected from the resulting high-precision numerical output. Their exact-root interpretation was established only afterward by the fresh full-source ball computation. A selected-coordinate attempt to extend the star from order 14 to order 16 failed at its first attempted 1/16 interpolation step. It is not a proof that all such stars fail at order 16. Some exploratory output was only terminal output and was not uniformly retained as files; the archive contains the surviving scripts, candidate sequence and logs, without claiming a complete record of every trial.

The infinite harmonic extension is different: no sampled harmonic sum is used. Its entire conditional cumulants are bounded by the integral-test inequalities in the paper, then the same seven-coordinate head is re-solved in a complete interval box. This proves a second exact model, not that the finite root is unchanged after adding infinitely many leaves.

## What was not done

No remote CI, full repository checkout/validator, Lean build, independent referee review, or full replay of earlier PR certificates was performed. The general Ising route, source identity, independent zero-tripling obstruction and arithmetic-core ancestry are credited. No complete review of every recent PR or claim of external novelty for the general methods is made.

The executable checks establish the stated finite predicates under the supplied analytic/arithmetic contract. The analytic proofs of source identity, star zero exclusion, homogeneous-star obstruction, infinite-product compactness and conditional RH ending remain paper proofs requiring independent review. OPEN-STAR is an unsolved construction problem, not a routine reviewer task.
