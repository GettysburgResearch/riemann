# Validation and limitations

## Exact code actually executed

The two README checker commands pass, normally and under `-O`. They reconstruct the same digest:

`4e25c431ac76efb00e89001315345d8fe41e3d4843297b96e11ca4c3d2407d4a`.

The finite coverage is: 17 sinh/fixed-moment comparisons; 15 linearized companion eigenmode identities; 221 full finite-depth companion moment identities (depths 0–12, moments 0–16); 26 variance identities; 119 rational chord-factorization panels; 16 complete inverse-moment majorants; 208 formal differential/dilation coefficients. Further normalization and factorial-majorant guards also run.

The fixed moments are generated from reciprocal sinh coefficients and compared with the independent fixed-point recurrence. Finite companion moments are generated from their separate positive density/tilted affine recursion and compared with the difference of the two source laws. This is same-author algebraic cross-checking, not independent mathematical review.

Each mode runs a pristine copied-receipt CLI and eight altered-receipt refusals, covering false RH status, false phase status/type alias, wrong contraction, missing depth/coverage, wrong digest, floating-number alias and duplicate JSON. No acceptance check is an optimized-away assertion. Integers and Fraction arithmetic supply all accepting calculations. The receipt is reconstructed; it is not accepted merely by hashing supplied JSON. The checker does not authenticate an external primitive computation or machine-prove any analytic theorem.

## Floating exploration actually executed

The three source-flow commands and two companion commands in README completed. SCOUTS.json selects seven first-guess depth panels, the depth-four/five transient panels, two direct depth-one quadratures and the paired thirty-point phase grid. Selection is not a zero census. Rounded solver guesses were exploratory choices near low-height features, not an authenticated zero-data source or a proof of root indices. Failed local searches and other returned roots are still observable by running the supplied programs.

The source-flow code uses a logarithmic grid [-40,28], 48-point Gauss integration over the exact U law, 12-node interpolation, and exact rational moments through 16 converted to binary64 for the small-t series. It includes a finite Taylor integral over the entire left tail, but **does not enclose its omitted Taylor terms, quadrature, interpolation, roundoff or right-tail error**. The source functions are changed approximants, not xi. The direct depth-one calculation uses independent 96x96 and 160x160 Gauss panels after a beta/homogeneity reduction, not the log-grid recurrence.

The companion code uses the closed sinh Laplace transform, a 96-step tilted perpetuity, 64-point Gauss integration, and two grid/angle settings. Both settings remain inside Re(t)>0. Gamma evaluations, quadrature and interpolation are binary64, not intervals. The all-future perpetuity *mean* bound is proved in PROOF, but is not combined here with directed quadrature into an accepting certificate.

The inspected points are x in {0,2,5,10,14,17,20,21,25,30}, y in {0.05,0.2,0.4}. All thirty normalized phase values were positive in each configuration. The minimum was about 0.013089; the maximum cross-configuration discrepancy was about 1.86e-7. These numbers are ordinary approximate diagnostics, **not rigorous lower bounds**. There is no coverage between the points, at larger x, or as y tends to zero. No zeta/gamma-directed oracle, zero table, interval isolation, contour count, true zero index, or global phase result is claimed. The numerical programs do use ordinary SciPy loggamma where needed; it is not used by check.py.

## Failed and superseded exploration

An early source-flow prototype omitted the analytic left tail. Its root outputs were excluded. A later configuration at angle -1.2 had unstable or failed low-depth/high-frequency local searches. The retained fine upper-source comparison uses angle -1.5. Even in retained configurations, not every reported solver root is stable; only the specified diagnostic panels are summarized. A tiny local residual is not a root enclosure.

Earlier exploratory upper-flow runs used angles outside the right Laplace half-plane. They are not the supplied final implementation and are not accepting evidence. The final source and companion commands restrict angles to the right half-plane. An exploratory companion scan also included y=1, outside the proposed critical-band target; some of those comparisons were badly unstable (up to about 0.23 in normalized score). They are not counted among the thirty band panels or used to assert an upper-half-plane theorem.

A combined orchestration completed the fine upper-source command but timed out while starting a companion run. The later separate companion commands both completed and are the retained executions. No interrupted run is counted as a successful receipt.

## What was not executed or established

No full repository checkout/validator, Lean proof, prior-branch checker, independent referee acceptance, Windows run, remote CI result, all-depth phase induction, all-band numerical certificate, complete zero census or RH proof is claimed. The literature search is not a novelty audit. The all-order written results rely on the mathematical arguments and credited classical source, not finite extrapolation.
