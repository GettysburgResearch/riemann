# Full-source variance-selector diagnostics

Status: completed arbitrary-precision finite calculations; no interval certificate, global sign certificate, continuum legality certificate, or asymptotic selector theorem.
Date: 25 October 2026.
Scope: the full semilocal Weil matrix from PR #1017 at `450dd8abecf58dfe60b3bc39bda0f792ea82ce95`, including every prime power through `exp(2a)`, both pole terms, and the analytic archimedean tail. The physical sign is sampled only.

## 1. What was asked of the actual source

The proposed selector in PR #1021 solves the mass-normalized resolvent variance equation

\[
V_{a,N}(\kappa)=V_X,
\qquad V_X=-X''(0)=0.0462099862308379415778676208606780280067635\ldots.
\]

The new analytic consumers show that a cofinal family of exact legal selectors with globally nonnegative, uniformly tight physical densities would imply RH without a separate identification theorem for the entire limit. These calculations test finite brackets and sampled signs for that specific proposal. They do not prove the open all-scale hypotheses.

The matrix is assembled in modes `-N,...,N`. Its even block has dimension `N+1` and its odd block dimension `N`. The experiment conservatively uses the smaller of the two computed parity minima as its finite spectral boundary. It solves the even block because the forcing is constant. This is separate from the even-sector theorem in `EVEN_FINITE_SELECTOR_CONSUMER.md`, which shows that the exact cofinal even-matrix growth bound would itself suffice.

For each case the script compares the variance at the source's explicit safe shift with the variance at

\[
\kappa_{\rm near}=\lambda_{\rm finite}
                   -10^{-15}|\lambda_{\rm finite}|.
\]

If those two computed variances lie on opposite sides of `V_X`, it bisects in the spectral representation of the finite resolvent. The requested variance residual is `10^(-36)`. No monotonicity of the variance is assumed: an opposite-sign endpoint bracket is enough for the bisection of this continuous finite rational function below the computed bottom. A failed endpoint bracket does not establish nonexistence of a root between other endpoints.

Xi enters only through the declared target second derivative. No numerical zeta zeros enter matrix assembly, shift selection, or sign sampling.

## 2. Completed runs

The first run used `N=16`, 110 decimal digits, 160 Gauss--Legendre nodes, and 513 equally spaced sample points on the nonnegative half-interval. The second used `N=32`, 180 digits, 320 nodes, and the same sign grid.

| Half-width `a` | Modes `N` | Variance at near-bottom endpoint | Endpoint bracket | Selected shift, when bracketed | Smallest sampled density |
|---:|---:|---:|:---:|---:|---:|
| 0.4 | 16 | 0.02506893991865 | yes | -0.7786654924241 | 0.6794919718208 |
| 0.6 | 16 | 0.03290481060790 | yes | -2.820676810094e-5 | 7.00931482146e-3 |
| 0.8 | 16 | 0.03760442924823 | yes | -1.733303920633e-12 | 1.60947625133e-6 |
| 1.0 | 16 | 0.04136106752616 | yes | -5.679953223204e-22 | 2.01196682605e-11 |
| 1.3 | 16 | 0.04945446585279 | no | — | — |
| 1.0 | 32 | 0.04059067413976 | yes | -2.759110599226e-24 | 1.74793264130e-12 |
| 1.3 | 32 | 0.04431376816026 | yes | -8.934974760511e-46 | 1.73530106229e-23 |
| 1.8 | 32 | 0.05362113991211 | no | — | — |

At `a=1.3`, increasing the cutoff from 16 to 32 modes repairs the failed endpoint bracket. At `a=1.8`, 32 modes again fail that same bracket test. This is direct evidence that a fixed small cutoff cannot decide the selector question uniformly as the interval expands. It does not establish that either finite or continuum variance roots cease to exist at those widths.

In every bracketed case, all sampled densities were positive, and the trapezoidal estimate of the exponentially weighted negative part was zero. Those are grid observations. The exact finite polynomial could have negative values between samples. A nonnegativity certificate would require a global trigonometric-polynomial argument, such as outward-rounded interval bounds or a verified positive factorization, coupled to certified matrix/selector errors. No such certificate was produced.

The selected negative shifts rapidly approach zero in these experiments. Their numerical magnitude is strongly dependent on the cutoff: at `a=1.0` it changes by over two orders of magnitude when `N` doubles. Thus their smallness is a diagnostic, not an established asymptotic rate or a lower bound for the continuum spectral bottom.

## 3. What is and is not exact

The source's matrix formulas are exact identities. They integrate the actual overlaps of zero-extended basis functions rather than imposing periodic wrap-around. Every supported prime-power translation is enumerated. The archimedean tail beyond `2a` is evaluated from its closed expression `2 atanh(exp(-2a))`.

The finite archimedean integral is evaluated by ordinary high-precision Gauss--Legendre quadrature. The eigensystems and bisection are also ordinary arbitrary-precision arithmetic, without outward rounding. The stored tiny linear-system residuals measure the solve for that numerical matrix; they are not error bounds for the exact matrix, its spectral bottom, or the continuum operator.

For `a=1.0`, the complete prime-power list is `2,3,4,5,7`; for `a=1.3`, it is `2,3,4,5,7,8,9,11,13`; for `a=1.8`, it is `2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,29,31,32`. The reports retain the lists for every case, both parity minima, all selected normalized cosine coefficients, variance residuals, and sign-grid diagnostics.

These runs use selected finite widths and cutoffs. They are not executions of all members of the cofinal schedule `N_k=ceil(k^3)` in the analytic theorem. No finite number of computations could verify its all-scale premise.

## 4. Reproduction and provenance

Requires Python and `mpmath==1.3.0`. From this directory:

```sh
python -B selector_experiment.py --a 0.4 0.6 0.8 1.0 1.3 --modes 16 --dps 110 --order 160 --points 512 --output selector_n16.json
python -B selector_experiment.py --a 1.0 1.3 1.8 --modes 32 --dps 180 --order 320 --points 512 --output selector_n32.json
```

The dependency `source/experiment.py` is copied without modification from the authenticated PR #1017 archive member `standalone/2026-10-22-weil-resolvent-selection/experiment.py`. Its SHA-256 is `79563f448d916f400ecc22f3461d6d3583c5604100cba6c7c61c705ebf500463`. The archived source package itself has SHA-256 `8185bfe6f9a5e2899cae78083a2d9e232f7b723d02a76eb88fb6116c0db03646`.

Completed diagnostic artifact hashes:

| Artifact | SHA-256 |
|---|---|
| `selector_experiment.py` | `45277fb3500b1bb45724eb4f06bf618e1a1bdeb47f5784925fe3cf452713fa68` |
| `selector_n16.json` | `a1b0dfa9a4532fbc8be2f493b1c8eaf3a5abd7ebbc70c61a8d8fb6a0eff6063e` |
| `selector_n32.json` | `d64ff1df0b40b578063681beaebf8d11d1aba38760ac15bcab1dfa1e59e4ae67` |

The local dependency installation and interpreter bytecode are disposable execution files and are not part of the deliverable.
