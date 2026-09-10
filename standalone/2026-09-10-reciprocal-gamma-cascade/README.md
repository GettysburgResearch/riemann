# A reciprocal gamma cascade from a Bessel model to xi

**Research proposal; independent review required. RH and the zero-confinement theorem remain open.** This packet does not change the integrated scientific baseline.

The proposed direction is constructive: begin with a model whose Fourier zeros really are governed by a positive Sturm–Liouville operator, then add a prescribed sequence of positive gamma modes until the whole-source transform becomes xi. A geometric reciprocal projection enforces reflection symmetry at every stage.

For independent shape-two unit-rate gamma variables, let

    X_N = sum_(n=1)^N G_n/n^2, with density f_N;
    h_N(t) = sqrt[f_N(pi exp(2t)) f_N(pi exp(-2t))];
    F_N(z) = integral h_N(t) exp(izt) dt / integral h_N(t) dt.

The classical infinite gamma-sum/xi identity is credited to Biane–Pitman–Yor. This packet supplies a detailed proposed construction and convergence argument, rather than claiming priority for that representation.

## What is established in the written component arguments

- The densities have an explicit finite rational partial-fraction formula and the exact positive update `(d/dx+(N+1)^2)^2 f_(N+1)=(N+1)^4 f_N`.
- The normalized reciprocal projection is the unique reverse-relative-entropy projection of the tilted log-law onto even probability densities.
- The entire functions F_N converge to **Xi(z)/Xi(0)** with an explicit O(N^-1/2) absolute error uniformly on every full horizontal strip, including arbitrarily large real frequency. The whole omitted gamma tail and both real-space tails are paid.
- The first function is `K_(iz/2)(pi)/K_0(pi)`. A positive half-line Schrödinger energy identity proves its zeros real.
- There is an exact continuous gamma-resolvent update and an exact auxiliary translation tangent involving Phi(z±2i). These supply concrete source equations for the spectral attack, not a zero-motion estimate.

These are proposed paper arguments, not independently accepted theorems or machine-verified infinite proofs. Read [PROPOSAL.md](PROPOSAL.md) for definitions, full proofs, source qualifications and the conditional ending to RH.

## What not to assume

A non-directed numerical stress-test finds an apparent nonreal zero of F_4 near `28.0555855384 + 2.6219979333 i`, reproduced on two quadrature grids. This is a changed finite approximant, **not zeta**, and not an interval/Rouche certificate. Global real-rootedness of every finite approximant is therefore not a safe working conjecture.

The proposed target is instead a growing-window theorem: along a cofinal sequence, all approximant zeros in an expanding critical-band rectangle must lie in a strip shrinking onto the real axis. The complete source convergence would then prove RH by Rouche. **That source-specific confinement theorem is not supplied.** Positivity, symmetry and convergence alone do not prove it.

The next useful contribution is an analytic bound for the reciprocal gamma score, informed by certified finite parameter continuation that includes collisions and boundary winding. Another moment fit or an unstructured zero scan is not the proposed proof mechanism.

## Reproduce the bounded work

    python -I -S -B check.py --check checks.json
    python -I -S -B -O check.py --check checks.json
    python -I -S -B test_check.py
    python -I -S -B -O test_check.py

The checker reconstructs exact finite partial fractions, complete rational moments, differential coefficients and telescoping tail products. It does not compute xi or certify a zero. The separate optional scout requires mpmath and is explicitly non-certifying:

    python -B scout.py --output /tmp/gamma-scout.json

[VALIDATION.md](VALIDATION.md) records actual executions and exclusions. [SOURCE_LOCK.json](SOURCE_LOCK.json) records source versions and reading depth. Original repository files and the earlier local trace/Hankel packet are untouched. No remote publication or merge is claimed by this local packet.
