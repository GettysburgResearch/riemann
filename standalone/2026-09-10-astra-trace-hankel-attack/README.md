# THA26 — a whole-xi trace/Hankel proof attempt

**Research only; proposed component proofs requiring independent review. A full
RH proof is not obtained.** No canonical status or integration record is changed.
The complete written argument is [PROOF.md](PROOF.md); the end-to-end attempt
and its exact failure are separated in [ATTEMPT.md](ATTEMPT.md).

Starting from the full xi source, and motivated by the explicit trace-class
operator in PR #834, this packet establishes the following proposed components.

**A positive Gaussian zero sum at every time.** For every positive-real-part xi
zero z_j, retaining multiplicity, set theta(u)=sum exp(-z_j^2 u). A real low-zero
reserve pays every potentially negative high-zero contribution, using the
imported finite-height theorem and a complete tail bound proved here. The sum
is strictly positive for every u>0. Therefore

    log[xi(1/2+sqrt(t))/xi(1/2)] is a Bernstein function, t>=0.

All its reciprocal exponentials are completely monotone. In particular every
scalar trace s_m=sum z_j^(-2m) is positive, and the factorial-weighted Hankel
matrices ((n+i+j-1)! s_(n+i+j)) are positive definite at every rank. These are
statements in the squared coordinate t, not in the original complex variable.

**Unweighted Hankel positivity through rank 25 for every shift n>=2.** Exact
Lagrange interpolation at 25 imported, widely enclosed low zeros and a bound
for the entire remaining tail give a relative error below 1/5,000,000. Rank
nine also works for every shift n>=1. This is not a truncated zero matrix or
a finite sweep in the shift. It is not a rank-25 statement about value-node
Pick matrices, and does not assert that rank 25 is maximal.

**An exact obstruction to the attempted finishing step.** An arbitrarily small
positive symmetric-translation perturbation of the actual theta density
preserves all real xi zeros, the finite verified height, the positive Gaussian
sum, the Bernstein property and the retained Hankel conclusions, yet inserts
explicit nonreal zeros at much greater height. It changes the infinite theta
source. A separate compact probability density has all positive scalar traces
but an exactly negative 4-by-4 unweighted Hankel determinant.

**The missing condition is stronger.** RH is equivalent to unweighted Hankel
positivity at every rank (one fixed shift n=2 suffices), and to complete
monotonicity of theta(u), not just positivity of theta(u). The positive
factorial-weighted hierarchy cannot be converted to the unweighted one by
removing factorials. The written proof includes the precise classical
moment/Stieltjes implications and identifies the still-unproved trace-square
inequality. No new easy criterion, external novelty or scientific acceptance
is claimed.

## Inputs and assurance

The Platt--Trudgian verified height 3*10^12 and the first 25 LMFDB ordinate
intervals are imported. This packet does not recompute actual zeros or actual
xi moments. The coarse all-height count N(T)<=T log T for T>=100 is proved
by a theta/Jensen argument, so the complete tail is not supplied by a finite
census alone. Classical products/moment theorems and exact repository reading
boundaries are listed in [SOURCES.json](SOURCES.json).

## Reproduce the exact finite checks

From this directory, with an unmodified packet:

```sh
sha256sum -c SHA256SUMS
python3 -I -S -B check.py --expect result.json
python3 -I -S -B -O check.py --expect result.json
python3 -I -S -B test_check.py
python3 -I -S -B -O test_check.py
```

The checker uses standard-library integers and rational arithmetic only. It
regenerates its complete bounded result, checks the pinned imported input and
rejects ambiguous JSON. The separate test program executes a pristine full
CLI reconstruction and eleven actual corrupted-input/receipt refusals per
mode, plus four arithmetic/API controls. The manifest is transport integrity,
not a mathematical proof or authentication of the external zero computation.
See [VALIDATION.md](VALIDATION.md) for exact performed and unperformed scopes.

## Delivery status

Prepared locally for a new research branch; **not pushed** in this session.
GitHub reads succeeded, but no write actions were exposed and direct Git
transport failed. The intended add-only destination is
`standalone/2026-09-10-astra-trace-hankel-attack/`, on a separate research branch
based on current main, not on the integration candidate. No existing file,
review record, main branch or integration branch has been changed.
