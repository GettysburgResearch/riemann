# O-0901 — Complete optimized-carrier cutoff ladder remains positive through `c=10^11`

Claim ID: O-0901  
Title: Complete prime-power continuation of the optimized D-0801 carrier basin  
Status: EMPIRICAL  
Authoring agent: `gpt56-01-c`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: D-0801 and L-0801 in stacked PR #37; the high-carrier leading approximation  
Scope: complete ordinary-floating prime-side computation, not an RH theorem  
Related counterexample candidates: none

## Observation

At carrier

\[
T=4709203636353.65,
\]

the complete D-0801 `K=1024` high-carrier leading margin

\[
m(c,K)=\frac{\log(T/(2\pi))}{2\pi}-\lambda_{\max}S_K(T,c)
\]

was recomputed with every prime and every higher prime power through each cutoff:

| `c` | prime powers | `K` | leading margin |
|---:|---:|---:|---:|
| `10^8` | `5,762,859` | 1024 | `+6.643091775833554e-3` |
| `10^9` | `50,851,223` | 1024 | `+2.3504233978552946e-3` |
| `10^10` | `455,062,595` | 1024 | `+6.076603725748697e-4` |
| `10^10` | `455,062,595` | 2048 | `+6.027589005261902e-4` |
| `10^11` | `4,118,082,969` | 1024 | `+2.6896626427230785e-4` |

Every displayed value is positive. No `Z-####` candidate is created.

## Coverage facts

The `c=10^11` result merged 50 contiguous shards of 100 integer segments each, with segment size `20,000,000`. The merger checked:

- segment coverage `[0,5000)` with no gap or overlap;
- identical cutoff, carrier, cell count, and segment size;
- exactly one higher-prime-power stream;
- `4,118,054,813` primes;
- `28,156` higher prime powers;
- `4,118,082,969` total prime-power terms.

The leading eigenpair had infinity-norm residual about `1.18e-15` and unit norm to binary64 rounding.

## Resolution audit

At `c=10^10`, doubling from `K=1024` to `K=2048` improved the margin by only

\[
4.9014720486795\times10^{-6}.
\]

Thus equal-cell discretization is nearly saturated at this point. This is a finite numerical observation, not a convergence theorem for the continuous envelope problem.

## Local carrier audit

For the `c=10^10`, `K=1024` leading vector, complete fixed-vector moments through order six reconstructed the direct prime Rayleigh value to `8.9e-16`. The local margin derivatives were

\[
q'(0)\approx5.9770487\times10^{-6},\qquad
q''(0)\approx5.82986775.
\]

The quadratic stationary shift was approximately `-1.02525e-6` and changed the margin by only about `3.1e-12`. An order-six Taylor scan with the explicit absolute remainder

\[
W e^{\eta}\frac{\eta^7}{7!},
\qquad W\approx493.75461046,
\quad \eta=|\delta|\log(10^{10}),
\]

found no fixed-vector crossing. At `|delta|=0.01` the remainder bound is about `4.23e-6`, still far below the positive midpoint margin.

## Independent pointwise cross-check

A no-remainder Riemann--Siegel curvature grid of 401 points on

\[
T-4\le t\le T+4
\]

with spacing `0.02` found no negative critical-line curvature. Its smallest ordinary value was approximately `30.7582` near `t=4709203636353.6309`.

At that point, simultaneous high-precision Riemann--Siegel evaluation gave

\[
\operatorname{Re}\frac{\xi'}{\xi}(0.5001+it)
\approx 0.00307585840221>0,
\]

with additional positive controls at real parts `0.501` and `0.505`. These are ordinary high-precision evaluations, not interval certificates.

## Interpretation

The optimized basin narrows substantially as the finite prime cutoff increases, but it did not cross zero. The rate from `10^10` to `10^11` slowed relative to the previous decades. Neither finite positivity nor apparent convergence toward zero is evidence for RH outside this finite family.

## Gap audit

1. The displayed matrix replaces the exact archimedean and pole blocks by the high-carrier leading scalar.
2. Phase reduction, accumulation, and eigensolving use ordinary floating arithmetic.
3. D-0801/L-0801 and the Guinand--Weil normalization remain `PROPOSED`.
4. Positive values do not certify positivity of the exact matrix or of untested cutoffs.
5. The pointwise xi checks use mpmath Riemann--Siegel arithmetic without directed balls.

## Suggested next attack

Before another full decade continuation, derive the exact cellwise archimedean correction along the frozen vector and implement directed phase balls. In discovery, optimize cutoff and carrier jointly rather than assuming decade endpoints contain the deepest basin.
