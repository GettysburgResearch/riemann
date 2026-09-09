# Validation record

## Executed

From this directory:

```sh
python code/verify.py --write
python code/verify.py --check
python -O code/verify.py --check
python -m unittest discover -s tests -v
python -O -m unittest discover -s tests -v
```

The producer freshly recomputed **447 exact rational controls** and matched the retained result under both interpreter modes. **17 unit/rejection tests** passed under each mode. Ordinary and optimized test logs are retained in `results/`.

The direct authoring prototype separately checked the Hilbert identity in rational matrix algebra and the sixth-order Taylor coefficient in SymPy before the standard-library producer was written. Those prototype runs are not counted as an independent referee review or included in the 447 controls.

## What the controls authenticate

- Exact finite weighted-companion determinant polynomials at enough rational points to determine each bounded-degree polynomial.
- A coefficient-independent negative tail quadratic direction.
- Vacuum/forced-mode covariance and exact finite mixture cumulant identities.
- Forward/inverse summation by parts.
- The factored sharp Fourier multiplier inequality and exact equality cases.
- Eight finite rational Hilbert models with distinct support and retained multiplicities.
- Pair energies reconstructed both as matrix Hilbert–Schmidt norms and as ordered kernel sums.
- Intrinsic-flag surplus, horizontal Schur complements, positivity via exact principal minors, and single-pair equality.
- Monic Legendre projection residuals and the rational coefficients `1/1575` and `1/14175` in the screening series.
- Rejection of singular inverses, malformed source supports, wrong multiplicities/symmetries, and a deliberately false acceptance condition even under `python -O`.

The finite time-grid models are **SYNTHETIC_CONTROL / EXACT_RATIONAL**, not sampled or certified zeta zeros. Their full Gram data are independently recomputed; no stored positivity flag is accepted in place of algebra.

## Not executed and not claimed

No Lean build or formal analytic proof. No independent mathematical reviewer. No parent repository-wide suite. No broad prime, zero, conductor, or matrix sweep. No directed theta integration. No imported paper PDF audit. No RH-bearing arithmetic gate closed.

The exact finite checker does not certify infinite trace-class convergence, the theta representation, Fourier norm sharpness, the continuous screening limit, or a zeta asymptotic. Those are mathematical arguments in the proof files and must be reviewed as such.

## Local integrity

`SHA256SUMS` binds the retained text, code and result files. `code/validate_packet.py` recomputes those hashes, checks local Markdown links and mathematical delimiter balance, and checks that the expected packet files are resident. Its integrity verdict is not a mathematical proof.
