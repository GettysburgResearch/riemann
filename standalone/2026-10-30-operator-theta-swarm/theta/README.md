# Theta lane: exact obstruction and a source-faithful Bessel approximation

This packet gives three proposed mathematical results and one explicit open route. RH and a better zero-free boundary remain unproved.

1. **An exact arithmetic obstruction.** For the actual theta kernel, the eighth derivative of `exp(2*pi*cosh(2*t))*Phi(t)` at zero lies strictly between `-8951861` and `-8951860`. Positive-cosh and nonnegative-Taylor constructions cannot supply this fixed Pólya envelope even locally.
2. **A global obstruction and escape requirement.** The theta cusp at `t=i*pi/4` rules out any fixed positive Pólya-envelope parameter with an entire multiplier. A successful positive-cosh approximation must send both `a` and `bandwidth/a` to infinity.
3. **A constructive repair with full-source convergence.** Explicit Skellam weights `I_n(a)*Phi(asinh(n/a)/2)` give positive kernels converging to the actual theta density in every exponentially weighted L1 norm when `a→∞` and `M/a→∞`. Their Fourier transforms are explicit finite sums of modified Bessel functions with shifted order and converge locally uniformly to Xi. The first correction is `(1/(8a))*d/dt[sech(2t)*Phi'(t)]`.
4. **A precise remaining target.** Show that the complete Bessel sums have a vanishing nonreal-zero strip along a cofinal sequence. An elementary Lee–Yang multiplier shortcut is proved impossible for these exact coefficients; it is the Bessel sum itself that must be studied.

[Full proof](PROOF.md) · [Source and novelty scope](SOURCES.md) · [Rational certificate](POLYA_OBSTRUCTION_CERTIFICATE.json) · [Exploratory numerical output](SKELLAM_DIAGNOSTIC.json)

## Direct Bessel boundary continuation

[BESSEL_BOUNDARY.md](BESSEL_BOUNDARY.md) reduces the complete Bessel transform to a rational spectral boundary condition. [The general self-adjoint construction](../spectral/BESSEL_SELFADJOINT_GATE.md) proves its all-zero consequence, handles common factors and poles, and gives a weaker local criterion sufficient on expanding disks. Positive mixtures through order two satisfy the global construction. The actual order-three weights pass it at six certified parameter values and fail it at two; failure is not a nonreal-zero theorem.

The exact order-three certificate can be reproduced with:

```sh
python -I -S -B verify_bessel_m3.py
```

[Independent theta review](REVIEW_THETA.md) and [independent boundary review](REVIEW_BESSEL.md) specify their exact file identities and limits. Higher-order J-fraction and low-pole outputs use ordinary Decimal arithmetic and supply diagnostics only.

## Reproduce the exact component

```sh
python -I -S -B verify_polya_obstruction.py
python -O -I -S -B verify_polya_obstruction.py
```

Only the standard library is required. The script reconstructs pi by Machin's formula, bounds exponentials by rational Taylor intervals, differentiates the first four literal source terms, and bounds all omitted source terms. It proves the eighth-derivative interval; it does not verify the full analytic approximation theorem or any zero-free region.

`skellam_diagnostic.py` needs NumPy and SciPy. Its computations are ordinary floating point and are explicitly separated from the rational certificate. The diagnostic output records roots found by a limited search, not a complete census or exclusion of nonreal roots.
