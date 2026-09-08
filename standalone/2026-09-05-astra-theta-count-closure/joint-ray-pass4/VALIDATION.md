# Executed validation and limitations

Executed locally with the same source bytes:

    python verify.py --write checks.json
    python -O verify.py --check checks.json

Both runs produced byte-identical complete JSON with 2148 checks each.
Four modified output records were rejected by a fresh normal-mode run:
RH flag, analytic-machine-proof flag, total check count, verifier hash.
The results are in refusals.json. No large numerical scan was performed.

The checker uses only Python's standard library, Fraction and integers. It
reconstructs binomial/Gamma weights in two ways, mean/tail bounds, the exact
root-Gamma score identity, the time-derivative and Hermite Fourier polynomials,
Fourier mass, endpoint vanishing, the Poisson division factor, contour
completion of squares, and atom-level gain/phase constants. Finite periodic
Gaussian-rational spectra test the negative-density algebra and its required
positive-real exclusion. They are synthetic controls, not actual xi zeros.

The checker does NOT establish an infinite probability-density inequality,
a contour deformation, the explicit formula, the complete prime sum, normal
convergence, a Cesaro limit, or any RH statement. Those arguments are in the
manuscript and await independent proof review.

No inherited heavy suite, finite zero verification, or interval-Gamma run
was repeated. No Lean or external proof assistant was run. No remote CI
success, independent reviewer verdict, or external novelty is claimed.

All new files are confined to joint-ray-pass4/. Existing source and formal
files are untouched. The checksum manifest seals eight companion files;
the manifest does not hash itself. Source-lock hashes authenticate exact
bytes, not the truth of the mathematical arguments.
