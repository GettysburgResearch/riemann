# Degree 18, rather than another 0.9 adjustment

**PROPOSED finite theorem with a directed-arithmetic existence certificate. Independent mathematical review required. This is not RH or a new zero-free half-plane.**

There exists a connected **282-spin, 281-edge ferromagnetic tree** whose weighted observable matches the original standardized theta law exactly through degree **18**, including variance. All couplings lie strictly between **1/200000 and 2**. All observed weights are positive except the zero-weight hub. The entire finite-model characteristic function has only real zeros by the classical Lee--Yang theorem, with the hub handled by Hurwitz.

This closes the degree-18 realization left open in #974, whose connected 281-spin model matched degree 16 and retained a positive raw degree-18 discrepancy in (0.034,0.035). The change replaces its largest single-spin component with a dimer and retunes the other parameters. It uses a larger allowed upper coupling bound, not the old 1/4 box. It does not claim a certified path from the old model or a degree-20 construction.

## What makes this exact

The rational centers in parameters.json are not presumed exact roots. A 9-dimensional radius-10^-30 box around them has

- directed center-correction bound below 8.404e-41;
- directed contraction bound below 7.131e-12;
- every physical positivity constraint strict throughout the box.

Banach's theorem supplies an exact root for the actual infinite-source target intervals. The complete theta density is reconstructed on every full run with 320-bit integer outward arithmetic, six explicit theta indices, 98 Taylor cells, degree 120, and rigorous bounds for every time/index tail. No optimizer, floating-point value, stored moment oracle or external package is used by the acceptance test.

The source backend is explicitly adapted from #974/#886; this is not an independent transcendental implementation. Direct enumeration checks the complete seven-spin fixture, not all 2^282 configurations. The large tree is evaluated by exact conditional independence, retaining its whole Gibbs law.

## Read and reproduce

Read PROOF.md, then COFINAL_COMPACTNESS.md and VALIDATION.md. Run:

    python certify.py > fresh.json
    cmp fresh.json CERTIFICATE.json
    python -O certify.py > fresh-O.json
    cmp fresh-O.json CERTIFICATE.json
    python controls.py

The cofinal note credits and specializes classical Lee--Yang compactness: finite variance-one Lee--Yang laws automatically obey |f(z)|<=exp(|z|^2/2). Therefore matching at unbounded orders would already give the needed local uniform convergence, without a separate graph-size or growing-constant assumption. **The unbounded-order feasibility premise is still OPEN.** One finite model cannot prove RH.

The companion recovery directory preserves the missing twelve-file reflected-classes packet unchanged. The older eighteen-file tilted packet was already archived in #973 and is not duplicated. Recovery of a proposed historical 271/300 argument is publication only; it is not newly endorsed by this degree-18 certificate.

No main or integrated mathematical-status file is changed. No independent referee, proof-assistant build, full upstream theorem replay or remote CI result is claimed.

Full standard-library replay: `python replay.py`. See the manifest and validation scope before interpreting the finite certificate.
