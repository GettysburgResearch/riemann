# Independent review of the fractional-window and norm-twist notes

Reviewer: `spectral_selector`, a separate agent from the author.
Date: 25 October 2026.
Disposition: no blocking mathematical defect found in the checked component statements at the exact hashes below. This is a mathematical review, not a formal proof certificate. It does not certify imported moment/detector frameworks or any new zero-free region.

## Reviewed artifacts

| Artifact | Exact SHA-256 |
|---|---|
| `fractional/UNIFORM_FRACTIONAL_WINDOW.md` | `18df393da1423c33256237a7f739409b4cbe26bae6d2b63ede6dbc05b118b6e0` |
| `fractional/NORM_TWIST_AND_BAND_TRANSFER.md` | `836be1511e47c4dc2f6848e0bab1393af0659327253f607d601b97c5627f950e` |

I read both complete files, checked their main arguments independently, read the relevant PR #1021 source notes at mathematical commit `742e952be4ef7843de86ea12678c0bdd3d3579c3`, and opened the cited primary papers. The review covers these bytes; later edits require a new review.

## 1. Fractional-window argument

The coefficient estimate is valid for the stated fixed-field ideal family. Expanding the square of the number of distinct prime factors reduces the second moment to single- and double-prime divisibility counts. Ordinary ideal counting and the prime reciprocal harmonic bound give the displayed `D(1+loglogD)^2` estimate. The pointwise inequality `|z^k-1|<=k(1-z)` on `[0,1]` then supplies the exact squared coefficient norm needed for the arbitrary-coefficient sieve.

The Hilbert-space triangle inequality proves the window estimate directly. It does not differentiate an endpoint theorem or substitute a varying row-dependent coefficient vector. The row weights, common masks, norm twist and fixed profile remain in their proper places.

I checked the four-term sixth-power-free sieve input against Xu--Sang [arXiv:2610.17675v2](https://arxiv.org/html/2610.17675v2), equation (2.3). It is stated for sixth-power-free rows and columns. Squarefree columns form a permitted subspace, so no invented powerful-row summation factor is needed. The ordinary endpoint is explicitly conditional on the pinned framework of the earlier packet; I have not independently certified that entire framework.

The exponent arithmetic is correct. For `D=U^r`, `1<=r<=3/2`, the dominating sieve exponent is `1/3+5r/6`; subtracting the target exponent and dividing by two gives the two stated window formulas and the corner values `1/12`, `29/288`, `13/120`. The power-thin window is too small to make the earlier polynomial extrapolation bound a subpower cost. The note therefore preserves the actual remaining gap.

The Euler-ratio expansion also checks: the coefficient at `p^j` is `eta(-1)^j`, and its absolute value is `eta` for every positive prime power. The prime sub-sum alone prevents the separate absolute-convolution estimate from being subpower at the desired logarithmic window. This is correctly described as a limitation of that estimate, not a lower bound for the original character mean.

The phase-average identity is Parseval in the coefficient parameter, and its transfer to the Mobius coefficient uses only Cauchy--Schwarz over the degree. Its positive prime stratum is a necessary target. I checked the quoted source prime exponent and the source's squarefree-row restriction in Theorem 1.2. During review I requested one scope clarification: specialize explicitly to `nu=1`, `sign=+1`, fixed `S`, and no extra moving puncture when quoting that literal theorem. The author made precisely that correction; the reviewed hash above includes it. No unproved character/mask adapter is now attributed to that source.

The complex-disk extension has the indicated `exp(eta r_D)` cost from `|z^k-1|<=eta k(1+eta)^(k-1)`. On the stated power-thin windows this cost is bounded. It does not supply a fixed parameter interval.

## 2. Norm-twist argument

The reciprocal estimate is explicitly conditional on the fixed zero-free half-plane `ZF(beta)`, with `1/2<beta<1`. I checked the contour mechanism. A logarithm continued from the Euler product exists on the high horizontal rectangles; Borel--Caratheodory and polynomial vertical growth give the needed `O(log|t|)` bound there. The shifted Mellin contour stays away from the pole at one. Its left edge lies between the Gamma poles at zero and minus one, so only the residue at zero is crossed. The exponential Gamma decay controls the horizontal sides and truncated tails.

Taking the smoothing scale as a fixed power of `log|t|` makes the shifted-contour error bounded. The absolute smoothed Euler logarithm is `loglogY+O(1)`: its higher-prime-power part is bounded; comparison with the real Euler product at `1+1/logY` follows from elementary Chebyshev bounds. Exponentiating the lower bound for the real logarithm yields the stated reciprocal bound of order `loglog|t|`. The finite omitted Euler factors do not change the argument or its leading logarithmic size.

At `sigma_X=1+1/logX`, the primes above `X` and all higher prime powers contribute a uniform bounded error. The negative-phase approximation therefore makes the reciprocal at least a fixed positive power of `logX`. Combining it with the conditional reciprocal estimate proves the asserted double-logarithmic height obstruction. The mean-square harmonic version is exactly the same cosine calculation, and the polynomial-height lower bound for the harmonic discrepancy has the correct three logarithms.

The prime-band approximation `t_P=pi/logP` is valid. Its telescoping error is proportional to the number of prime factors. The discussion correctly identifies costs specific to its proposed use: arithmetic prime-factor restrictions are not automatically licensed smooth profiles, the literal excluded-prime product is generally too large for the imported puncture scope, and controlling the separate approximation error by the available arbitrary-coefficient sieve requires a growing number of bands. These conclusions do not claim impossibility of every arithmetic band method.

I also checked the limited source description of Lü--Wang--Wu [arXiv:2610.20242v1](https://arxiv.org/html/2610.20242v1), Section 4.2 and Proposition 4.3. Its parity conjugacy is the stated coordinate transformation between determinant operators on restricted state spaces. The note does not turn it into an unproved replacement of a squarefree coefficient by a Mobius coefficient in this different character family. I did not review the entire paper's main theorem.

## 3. Limits retained after review

The positive result is the explicit thin fractional window, conditional on the named source inputs. The norm-twist theorem is conditional on `ZF(beta)` and excludes one quantitatively specified transfer method. Neither note establishes the fixed/non-power-thin coefficient control needed by the native consumer, a new prime-stratum bound, a faithful determinant-kernel embedding, or an improved zero-free boundary.

No numerical character-sum experiment was used to certify these analytic statements.
