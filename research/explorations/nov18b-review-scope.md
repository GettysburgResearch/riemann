# What was checked in the final review

The analytic notes in this branch are research proposals. Internal proof reading, exact arithmetic replays and verification of an external formal artifact have different scopes. This record identifies the checks on the results highlighted in the [index](nov18b-results.md).

## Centered Goldbach mass

A separate mathematical reader checked the source identification in Goldston and Suriajaya, their upper bounds under RH and at a general zero abscissa, and the signed Laplace-transform and compact-limit arguments. A second pass on the stronger local theorem checked the barycentric sign at the selected nonzero Laplace value, positivity and size of the divided-difference kernel, both discarded tails, and the quantifiers in the small-window criterion. The exact files reviewed for these last two statements have SHA-256 digests below.

| Checked proof | SHA-256 |
|---|---|
| [Theta kernel and ordinary cumulative limit](nov18b-goldbach-review.md) | 9c03169b80770f7e6b6151a3324459f5db7ec4b86733544c2f36fa1675840814 |
| [Divided differences and the localized one-sided criterion](nov18b-goldbach-local.md) | b62c8fd0e23f87ad45d6da775d493e40ee21fef401b8dc434c38b917f68ed397 |
| [Compact-filter dependency](nov18b-compact-zero-filter.md) | 2d775bcd5680ec970d029597e47806c62c4b65d63e06b9704f1d69c016a2c6f9 |

The nonnegative measure dominating the complex isolating test, the contour bound for the reciprocal zeta function at a separated vertical line and the multiple-pole residue received a separate hostile read. These are internal reviews. The open arithmetic statement is a square-root-scale upper estimate for the actual prime or Möbius observable, or the corresponding Goldbach mass estimate on an unbounded sequence.

## Exact heat-flow computation

The final replay ran the included checker anew at time-step denominator 8,192,000. Each endpoint below is the exact result *including* the cost of de Bruijn strip contraction after the last active step. The positive-height computations used python-flint rationals. The checker source for these runs has SHA-256 3222661ae430d3345d58a6bce114e33dade309c5a6c8092201fbd8f5a7711109.

| Zero-free seed | Steps | Exact upper endpoint |
|---|---:|---|
| $7/8$ | 884,448 | $431859422735991684619374093/4000000000000000000000000000$ |
| $10499/12000$ | 884,277 | $431776142786157950357274647/4000000000000000000000000000$ |
| $873345856107/10^{12}$ | 881,056 | $2151016308875269172515792441/20000000000000000000000000000$ |

All 67 archived signed-kernel rows were also replayed, totaling 2,712,495 boundary coefficient checks and 4,001 own-derivative coefficient checks. A separate reader checked the analytic first-contact comparison and the treatment of the old row-55 height tube. The remaining imported results include Raymond's wall and bounds on the physical source. The computation uses the zero-free seed as an input; it does not establish that seed. [Reproduction commands and input hashes](../../experiments/X-nov18b-heat-seed/README.md) · [Individual row receipt](../../experiments/X-nov18b-heat-seed/kernel-replay.json) · [External formal certificates](nov18b-reciprocal-formal-audit.md)

## Limits of the spectral claims

For the finite prime-divisor matrix a separate pass checked the large-prime pruning and transfer of bounded-energy vectors to the product measure, including the two boundary estimates in the min–max proof. For the balanced Weil packets, the final argument accounts for individual divisor aliases and identifies an exact theta null near the small mode. A negative contribution from a single displaced pair can remain almost entirely in the orthogonal complement. Positivity restricted to these matrices cannot establish full Weil positivity. [Divisor spectrum](nov18b-weil-divisor-edge.md) · [Balanced packets](nov18b-weil-balanced.md)

The cubic-theta investigation identifies the precise long-dual estimate and shows that substituting arbitrary bounded coefficients can saturate it. Its obstruction theorem concerns that relaxation and the specified arithmetic prime marks. It does not provide such a lower bound for the true cubic theta coefficients. [Proof and remaining arithmetic input](nov18b-operator-reflected-marks.md)

Under RH the parity argument also gives both signs of total mass $\gg X^2$ in every sufficiently large $[X,1.14X]$. Its directed 96-bit FLINT computation uses the first 160 positive zeta ordinates and bounds the entire remaining double sum. A separate rerun reproduced the total upper interval $0.494726512906853848187120\ \pm1.48\cdot10^{-25}$, strictly below the parity lower threshold $1/2$. The finite computation verifies this inequality. The passage from it to the interval theorem uses RH and the explicit-formula argument in the note. [Proof](nov18b-goldbach-parity.md) · [Checker](nov18b-goldbach-parity-check.py)
