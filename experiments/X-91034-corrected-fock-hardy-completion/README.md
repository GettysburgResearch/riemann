# X-91034 — Corrected Poisson–Hardy completion regression

This finite replay supports:

- `R-91008`: the scalar causal Cauchy mother has a genuine interior zero and a hidden jump vector;
- `L-91034`: an energy-preserving delay fibre removes the common-zero defect;
- `L-91036`: higher Poisson chaoses cannot supply an exactly source-linear positive target;
- `L-91035`: the generalized-Jordan coefficient sequence is the one used in Suzuki's completed Hankel scattering construction;
- `R-91009`: inner amplitude unitarity does not sign the normalized radial delay curvature.

It checks:

- the exact algebraic partial-fraction formula for the causal impulse;
- outward interval signs locating a root in `(31/20,8/5)`;
- high-precision localization of that root;
- the hidden-jump orthogonality against five carrier modulations;
- the direct-integral delay isometry;
- positive delay-fibre energy at several points, including the scalar root;
- a nonzero second Poisson-chaos coefficient;
- positivity of finite generalized-Jordan coefficients and the local Euler identity;
- an inner all-pass control with negative radial soft curvature.

The replay does **not** evaluate the actual zeta screw Gram, prove the delayed form-core theorem, differentiate Suzuki's Hankel isometry in the required positive metric, construct CDFHTI, or prove RH.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_CORRECTED_FOCK_HARDY_COMPLETION
```
