# TMC26 — whole-theta traces and the cost of a spectral metric

**Proposed research; independent mathematical and code review required. No full RH proof was obtained.** Main, the integration candidate, existing research and canonical/formal status are not changed.

This is a proof-oriented continuation of the whole-xi centered-operator programme, using the integrator's view of its exact remaining gap. Read [PROOF.md](PROOF.md), then [NUMERICS.md](NUMERICS.md). The actual all-order scalar sign remains open, rather than being assigned to reviewers as a routine last lemma.

## What is proved in the submitted manuscripts

**The remaining bounded-metric escape fails on the actual nonzero spectral space.** Even after every derivative constraint is imposed, critical-line eigenvectors force any orthogonalizing metric through height T to have, for all sufficiently large T,

```
condition(G_T) >= exp(T^(1/1000) log(T)/1000).
```

The nonoptimal threshold is not numerically instantiated. The proof combines exact clustered-exponential cancellation, a complete theta-moment bound, and a classical positive proportion of simple critical-line zeros. It uses no computed zero ordinate and no RH assumption. Bounded self-adjointization and polynomially conditioned finite-height metrics are excluded; real spectrum, unbounded metrics and other operators are not.

**A scalar route does not need that metric.** With the literal theta probability density, cumulants kappa_n and

```
s_m=(-1)^(m+1) kappa_(2m)/[2(2m-1)!],
H_N=(s_(i+j+1))_(0<=i,j<=N),
```

the full positivity tower H_N >= 0 is RH-equivalent, preserving multiplicities. The paper supplies a complete power-sum/moment proof and credits the classical mechanism; it is not presented as a new easier RH criterion.

**The actual 4x4 matrix is strictly positive.** A new standard-library outward implementation integrates the defining theta density through moment 14. All omitted theta indices, all times beyond 3, skipped small terms and every Taylor remainder are enclosed. The final determinant is between 1.1775e-41 and 1.1777e-41. No zeta/gamma oracle or zero sum enters acceptance. This certifies H_3, not the whole tower.

**Generic positivity/log-concavity cannot supply the induction.** Explicit modified positive even strictly log-concave double-exponential densities have a negative third trace. They satisfy the relevant integrability and compact-operator conditions but are not the theta source. They are not zeta counterexamples.

The useful remaining task is a theta-specific all-order Schur-pivot or equivalent positivity argument. The manuscript supplies the end-to-end conditional consumer and explicitly stops at this missing sign.

## Reproduce the bounded evidence

Use an isolated environment without repository credentials:

```sh
python -I -S -B verify_packet.py --full
python -I -S -B -O verify_packet.py --full
python -I -S -B verify_packet.py --self-test
python -I -S -B -O verify_packet.py --self-test
python -I -S -B test_checks.py --cli --output /tmp/theta-tests-normal.json
python -I -S -B -O test_checks.py --cli --optimized --output /tmp/theta-tests-optimized.json
```

The first two commands authenticate this packet and freshly reconstruct the entire source certificate. `--emit` in the underlying program is producer mode, not acceptance. [VALIDATION.md](VALIDATION.md) records completed runs, controls, prior timeouts and unperformed work. [SOURCES.json](SOURCES.json) fixes exact input versions and reading depths; [CLAIMS.json](CLAIMS.json) separates component statements from the open conclusion. No novelty, non-author acceptance, full-checkout, Lean or CI success is implied.
