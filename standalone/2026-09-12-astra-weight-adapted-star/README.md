# STAR26: guaranteed-real-zero models first, theta realization second

**PROPOSED component mathematics and directed computer-assisted existence. Independent review required. RH and unbounded-order realization remain OPEN.**

This add-only continuation links the repository's Brownian-companion failure and its Ising/gamma realization programmes. It does not introduce the general Lee–Yang route as a new idea. It supplies a more explicit candidate class, a finite constructive improvement, a whole-law extension, and a restriction showing why a simpler interacting class cannot work.

## Results and exact limits

1. **A connected 96-spin, 95-edge star exactly matches native theta moments of orders 2,4,6,8,10,12,14.** Its biases are weight-adapted: tanh(J_i)=a_i/100. All actual edge couplings lie between .0004 and .004. The defining parameters are exact roots in rational boxes, not the printed decimal centers. No minimal-size claim is made.
2. **The star's companion inequality is proved throughout the upper half-plane.** It follows from an elementary factor-by-factor modulus identity. Unlike the earlier failed Brownian candidate, the constructed model's real-zero geometry has no remaining phase-sign assumption. This does NOT identify that model with Xi.
3. **An infinite harmonic-star extension also exactly matches those seven moments**, has unbounded support, no Gaussian component and the same leading MGF growth coefficient as standardized theta: log M(y)=[1/(2 sigma)]y log y+O(y). The entire harmonic tail is paid analytically. The finite head is adjusted to a separate certified root. Subleading growth is not matched.
4. **Every bounded-variance sequence of homogeneous-coupling stars fails to converge to the theta law.** A common nonvanishing bias would force compact support; a vanishing bias collapses to a fair-independent-sign limit. The latter has zero tripling, contradicted by freshly certified literal theta values. Heterogeneous stars and general graphs are not excluded.
5. **The entire limiting class and a complete conditional RH ending are supplied.** Small weights can produce Gaussian variance plus a mandatory bias shift; actual theta growth excludes such Gaussian dust. A successful realization must retain square-summable, non-summable heterogeneous weights. Constructing native matches at unbounded order remains the decisive unproved step.

Both exhibited models have a certified standardized sixteenth-moment error in **(-.115,-.114)**. Thus neither is Xi. The attempted sixteen-moment continuation did not produce a solution; it did not prove that all stars fail at order sixteen. Matching a finite jet and the leading growth order has not completed the source identification.

## Read and replay

Read [PROOF.md](PROOF.md), then [CERTIFICATE.md](CERTIFICATE.md). [SOURCES.json](SOURCES.json) records exact repository versions and reading boundaries; [VALIDATION.md](VALIDATION.md) records executed scope and failed attempts.

From a clean packet directory, using the Python standard library only:

```bash
python -S -B verify.py --check result.json --self-test
python -S -B -O verify.py --check result.json --self-test
python -S -B mutation_test.py
python -S -B -O mutation_test.py --optimized
```

The verifier reconstructs the full source integral, all Fourier controls, both exact root certificates, both sixteenth-moment inequalities, and finite algebra checks. The two mutation commands alter producer code in temporary copies and reseal the manifests; each must fail after authentication. Run logs should be redirected OUTSIDE this directory because a clean complete file inventory is part of the contract.

`python -S -B verify.py --emit new-result.json` is a producer, not an acceptance of an existing result; emit outside the clean packet when preserving its inventory. No mpmath/SciPy/NumPy, stored zeta values or zero table enters acceptance. The inherited arithmetic core is attributed to the exact BRN27 blob, not claimed newly authored. No full repository validator, remote CI, Lean build, independent referee acceptance, or modification of prior work is claimed.

## Concrete next research task

Prove reachability of the actual theta moment target at unbounded order in this positive star class, or find a source-specific obstruction and broaden the graph. A local nonzero Jacobian is not such a theorem. The exact finite/infinite seeds, tail bounds, explicit phase formula and homogeneous-star obstruction define where a genuine new argument must enter.

The small `result.json` is a binding receipt, not a cached source table. To inspect every reconstructed ball and tail, add `--dump-full PATH_OUTSIDE_PACKET` to a full verification command.
