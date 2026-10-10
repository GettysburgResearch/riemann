# Sources, reproducibility and mathematical boundaries

## Publication and source locks

The saved nine-file Gaussian packet was published unchanged as `e5d68883991b390798d993b0bafa7975ab801886`, sole parent `1b55960ec9fb23425231dc281b70b640d8154104`, root tree `ab561e07b2fa3f6455d50b1a8a031484777bacc8`. The GitHub comparison shows only its nine additions and no deletions. All its nine returned blob IDs match the delivered files, including the saved manifest. Its source-level historical failed-push text remains unchanged.

The new Hermitian packet is add-only on that publication. Exact mathematical dependencies are:

- `continuation-balanced-closure/BALANCED_CLOSURE.md`, blob `09d1086f64a03df9ed87b12f9b3cfbd103073c6e`: the explicit inverse coefficients and small-mass calculation. Its source was read at the publication base. The new proof restates and extends it to 2k mixed conjugate colours.
- `continuation-integrated-window/INTEGRATED_CRITERION.md`, blob `34928b0d8531e8cbe8764edbabb188bcb72d5ff1`: fixed window and norm/Mellin extraction. The new proof states the exact adapter it uses, not an imported quasi-RH conclusion.
- `continuation-gaussian-conductor/PROOF.md`, blob `d8f7ac2045ccec55d8ccea6e0d2cccef3f6775dd`: primitive Gaussian Poisson normalization and original zero conventions.
- `continuation-gaussian-conductor/check_eisenstein_covariance.py`, blob `08ca528df9074ff8e418a29ba240b5cc1057b93d`: exact arithmetic helper, checked before loading by the new script.

The compact radial checkpoint was read at commit/source-overview level to preserve its scope and avoid claiming its already published low-conductor theorem as a fresh result. Its complete proof is not an additional dependency. Sibling PR proofs are not silently composed here.

The classical residue/Gauss/Poisson setting was checked against Gao--Zhao, arXiv:2201.01885v2, HTML https://arxiv.org/html/2201.01885v2. No new external large-sieve or Burgess theorem is imported. The Hermitian absorption proof is elementary from the displayed kernel and Holder; no literature-priority claim is made.

## What was actually replayed

The saved Gaussian source was rerun normally and optimized against its original result: 48,427 predicates per mode, identical stdout. Its three algebraic mutations and tampered-result refusal were rerun in both modes and match the saved negative receipt.

The new script was run normally to write result.json, then optimized to check it. The stdout is identical. It performs **12,028 new explicitly guarded predicates**, not Python assert statements. These counts exclude additional helper-module checks invoked during arithmetic construction.

The new coverage is:

1. Full local inverse convolution for every valuation vector in {0,1,2}^m at m=2,4,6,8: 7,380 vectors. This is finite coverage of the general coefficient identity proved in the manuscript.
2. Exact mixed-conjugate, shifted-scale reconstruction at k=1,2,3, all 72 nonzero Eisenstein rows with norm at most 19, and all five declared scale intervals. The finite alphabet consists of the specifically identified prime ideals of norms 7 and 13. Characters can and do vanish at row primes.
3. Fully signed norm comparisons, separately for each row and then in aggregate, in three finite prime alphabets. The fourth-order alphabet has both split primes over 19,31,37; the sixth-order alphabet both split primes over 61,67,73; the eighth-order alphabet both split primes over 193,199,211,223. Exact rational upper bounds on the local kernel mass give q<1 in each fixture. The parameters are sigma=3/4, 2/3, 5/8, respectively.
4. Pointwise negative examples, including C=-12 versus |A|^4=49 in the fourth-order fixture. These refute pointwise positivity of the disjoint statistic, while every integrated comparison is checked directly.
5. Exact rational exponent bookkeeping and the Gaussian double-transform scale involution. The latter tests only normalization algebra, not a finite approximation to an infinite Gaussian sum.

The finite norm fixtures use W=1_[1,2]. They are not computations of the infinite-convolution smooth W_* or asymptotic full-field moments. The declared finite alphabets and horizons ensure that no composite factor ideal is missing from those fixtures. The general proof, not a finite alphabet test, supplies the infinite fixed-prime-cutoff theorem.

Two mutations are executed in each optimization mode: the wrong inverse coefficient, and omission of the conjugate dilation phase. They are rejected at the intended named arithmetic checks. A separately tampered result is rejected after full replay in both modes. This makes six actual refusals, not a claimed test of errors that were never run. The receipts are negative_controls.json and tamper_controls.json.

## Where the mathematical risk remains

The crucial comparison puts an absolute value OUTSIDE the completed signed scale integral. It does not bound the termwise absolute overlap mass and does not preserve a decomposition into nonnegative pieces. Its proof holds the row measure fixed during every scale substitution and uses a larger fixed cutoff for 2k, not the old k-colour cutoff without verification.

The primitive low-conductor estimate concerns the NEW fully disjoint scalar. It does not upgrade the old shared-gcd covariance to exponential decay. Its use for the original moment passes through the relative comparison and finite-prime reinsertion, with the constants and losses displayed.

The remaining statement is DUAL_CORE.md (3.3). It is an unproved one-sided upper bound with a useful excess lambda. The packet does not claim a full fourth/sixth moment, an achieved 17/24 boundary, a new zero-free half-plane, or RH. No independent mathematical review, full upstream reconstruction, Lean build, or integration promotion occurred.
