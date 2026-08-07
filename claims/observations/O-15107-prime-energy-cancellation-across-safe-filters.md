# O-15107 — Prime-energy cancellation across two safe filters

Claim ID: `O-15107`  
Status: **EMPIRICAL / DISCOVERY ONLY**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Sources: PR #216 at frozen head `850d9315d23fdb2d950b4c194cb6e85993f379bb`; `X-15122`  
Scope: reconnaissance for the global off-diagonal theorem; no RH evidence

## 1. PR #216 compact triangular energy

PR #216 evaluated every complete unit logarithmic block of its compact
piecewise-linear safe window using all `665134` prime powers through `10^7`.
Its retained long-double table gives, among other rows,

| block `j` | total | diagonal | off diagonal | total / diagonal |
|---:|---:|---:|---:|---:|
| 5 | `0.00203813` | `6.61923` | `-6.61719` | `3.08e-4` |
| 8 | `0.00149011` | `16.57970` | `-16.57821` | `8.99e-5` |
| 12 | `0.00126627` | `29.70407` | `-29.70280` | `4.26e-5` |
| 16 | `0.00156048` | `42.49387` | `-42.49231` | `3.67e-5` |

Thus the compact filter spends more than `99.996%` of its later diagonal through
signed off-diagonal cancellation.

## 2. The cancellation survives before compact smoothing

`L-15145` proves that the compact PR #216 signal is a finite signed convolution
of the simpler scale-four Chebyshev signal

\[
 Q_4(\log t)
 =t^{-1/2}[\psi(t)-4\psi(t/4)].
\]

`X-15122` evaluates this unsmoothed scale signal on the same complete
prime-power range. Its retained rows include

| block `j` | total | diagonal | off diagonal | total / diagonal |
|---:|---:|---:|---:|---:|
| 5 | `0.35533816` | `10.03775746` | `-9.68241929` | `3.54e-2` |
| 8 | `0.21907206` | `19.43522289` | `-19.21615083` | `1.13e-2` |
| 12 | `0.27588238` | `31.67041649` | `-31.39453411` | `8.71e-3` |
| 15 | `0.24916641` | `40.71256393` | `-40.46339752` | `6.12e-3` |

At the last complete block, approximately `99.39%` of the diagonal is canceled.
The compact triangular profile strengthens the cancellation dramatically, but
it does not create it. The underlying two-scale Chebyshev difference already
contains the coherent arithmetic mechanism.

## 3. Scale reconnaissance

The integer-scale scan over blocks `5,...,15` gives:

| scale | mean total | mean total / diagonal | last total / diagonal |
|---:|---:|---:|---:|
| 2 | `0.19123` | `0.02337` | `0.01394` |
| 3 | `0.26585` | `0.01809` | `0.00961` |
| 4 | `0.25648` | `0.01276` | `0.00612` |
| 5 | `0.40144` | `0.01594` | `0.00658` |
| 8 | `0.52754` | `0.01512` | `0.00516` |
| 16 | `1.26139` | `0.02612` | `0.00493` |

Scale two has the smallest retained absolute energy. Scale four has the smallest
mean relative energy among the tested scales and is exactly aligned with the
pole-annihilating factor in PR #216. Larger scales can improve the final
relative ratio while increasing absolute energy.

## 4. Mathematical interpretation

The data support three conclusions about proof strategy:

1. The global theorem is a signed off-diagonal theorem. Entrywise absolute
   values discard nearly the whole answer.
2. The cancellation is stable under two substantially different safe filters:
   a bounded-ratio compact spline and a causal cumulative scale difference.
3. The causal representation exposes the same phenomenon without pair
   enumeration:
   \[
   Q_4(\log t)=t^{-1/2}[\psi(t)-4\psi(t/4)].
   \]
   This is a better interface for Selberg recursion and multiplicative
   martingale or Poincare ideas.

The empirical scale of the later energies is consistent with bounded or
polylogarithmic behavior, but fifteen finite blocks cannot distinguish that
from eventual exponential growth with a very small exponent.

## 5. Proof boundary

- Both computations enumerate the complete declared prime-power range.
- Both use ordinary long-double arithmetic and are not directed certificates.
- The producers are algorithmically different but have not yet received an
  independent compiler/backend replay.
- No asymptotic conclusion and no RH evidence is claimed.
- The only promoted outputs are the exact algebraic identities in `L-15145` and
  `T-15119`, which remain proposed pending independent review.