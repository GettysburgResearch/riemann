# Validation and trust boundary

The mathematical claims are PROPOSED, not independently accepted. This is research, not an audit or integration approval. The six test methods and exact bounded reconstructions do not machine-prove the complex-analytic theorems.

## Accepting arithmetic and coverage

`check.py --check results.json` authenticates all nine manifest entries and the complete ten-file flat packet inventory, rejects symlink/nonregular files, reconstructs the entire expected bounded result, and compares both JSON types and values. Duplicate keys, floating/nonfinite JSON numbers, missing/extra fields and Boolean/integer aliases are not accepted. Producer mode `--emit` is explicitly not acceptance.

All acceptance arithmetic is Python integers and `Fraction`. Gaussian rationals are pairs of Fractions. No mpmath, binary64 quadrature, zeta/gamma oracle, actual zero ordinate or parent module enters acceptance.

The complete reconstruction covers:

| Group | Exact executed scope |
|---|---|
| Gamma/simplex derivatives | 252 identities, N=1,...,12, including the full order-(2N-1) zero and eight subsequent coefficients |
| Positive tilted series | 108 exact coefficient identities |
| Laplace source binding | 84 exact rational evaluations of the full partial-fraction and rate-product expressions |
| Finite gamma densities | 36 complete rational-interval enclosures, three prescribed positive x values at each N=1,...,12; separate partial-fraction comparison |
| Quartet repair | 24 exact factor controls in the declared finite models |
| Trace/cumulant convention | 204 power sums compared with formal-logarithmic coefficient extraction |
| Finite Hankel inertia | 102 exact symmetric-congruence calculations on synthetic spectra with zero through three nonreal pairs and multiplicity weights |
| Variance-flow attempt | Six exact double-root panels; a=2 is positive while a=4 gives -8768, guarding the relevant sign |
| Boundary controls | Six negative-real-node Hankels and two zero-diagonal/zero-block inertia controls |

These are overlapping mathematical controls, not 824 independent theorems or a native zero census. The actual finite-gamma density enclosures are source evaluations, not Fourier-transform zeros or an evaluation of Delta_N.

### Complete density remainders

For exp(-x), 0<=x<=4, the program sums the 101 terms through degree 100 of exp(x), then bounds the ENTIRE future by the next term divided by 1-x/102. Reciprocal bounds reverse the interval endpoints. For the positive tilted simplex density it sums 49 terms through degree 48. Every later coefficient is bounded by v^k/k!, so the full tail is bounded by the next term divided by 1-v/50. PROOF Section 2 establishes the required probability-moment comparison. Thus no giant cancellation near zero or zero tail is assumed. The separate partial-fraction expression uses the same exponential backend; it is a second algebraic expression, not an independent transcendental primitive implementation.

## Test contract

`test_check.py` has six methods. Each mode executes one pristine accepting subprocess and twelve ACTUAL altered-copy refusal subprocesses. Cases include a resealed false RH flag, Boolean/float aliases, duplicate JSON, wrong variance value, reduced coverage, a false native-index claim, changed unsealed proof, missing/extra files, a symlink, and a resealed producer mutation of the radial factor 4 to 5. The last fails a separately reconstructed Gaussian-rational identity, not merely a stale hash.

Linux symlink refusal is exercised when supported. A host without symlink permission records an explicit skipped subtest; the summary is computed from the actual unittest result and never prints an unconditional all-refusals PASS after an error. No Windows execution is claimed by this author session.

The reported final commands are:

```sh
python3 -I -S -B check.py --check results.json
python3 -I -S -B -O check.py --check results.json
python3 -I -S -B test_check.py
python3 -I -S -B -O test_check.py
```

Normal and optimized outputs use the same implementation. The structured summaries and reconstructed JSON are compared, not elapsed-time stderr. The delivery receipt outside the research directory records the final command statuses, source hashes and roundtrip results.

## Separate numerical scout

`scout.py` uses mpmath at 120 decimal digits with composite Gauss-Legendre grids (32,6) and (40,8), after t=T_4 sin(theta). A positive small-argument simplex expression avoids the worst partial-fraction cancellation. Both grids locate the apparent centered N=4 nonreal root recorded in `scout.json`, agreeing to more than 45 decimal places.

This is NONDIRECTED and supplies NO ROUCHE COUNT, quadrature/primitive enclosure, complete nonreal census, q_4, Delta_4 or all-plane cutoff B_4. The entire numerical scout is excluded from the accepting result and from the proofs' hypotheses. The same arithmetic backend is used by both grids. Parent raw/intermediate zero certificates are different objects and are not rerun.

## Prepublication corrections and unperformed work

An exploratory N=8 calculation stopped after losing density positivity to cancellation at insufficient precision; no N=8 root conclusion was retained. In checker development, a Python integer division in one formal coefficient test introduced a float and was corrected to explicit Fraction arithmetic. Exact Gaussian-rational reconstruction also caught a hand-expanded sign error in the attempted variance-flow counterexample: the corrected identity is -64(a^4-29a^2/4-3), so the counterexample is at a=4, not a=2. Both signs now have explicit tests. These prepublication errors are not accepted mathematical evidence.

The endpoint theorem is an analytic fixed-N result. No explicit B_N generator, full centered-stage zero census, native Hankel index, actual defect/Jensen integral, cofinal defect bound, or new xi zero-free region has been computed or proved by this code. No full repository checkout/validator, parent numerical suite, Lean build, remote CI, independent referee or comprehensive external novelty review is claimed.

GitHub read access worked. The session exposed no connector write action; installed-provider discovery found the same GitHub connection, and direct Git transport failed DNS. The author packet is local, not a claimed remote commit. The add-only patch is intended for a separate branch from the exact source SHA in SOURCE_LOCK.json.
