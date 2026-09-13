# GPP26: exact Padé phase and the complete Gauss–Thorin trace

**Proposed component mathematics. Independent mathematical review required. RH and all-height xi-zero confinement remain unproved.**

Start with [PROOF.md](PROOF.md), then [VALIDATION.md](VALIDATION.md).

This additive continuation of PR #877 establishes proposed exact identities between the actual Gaussian nodes, a diagonal Padé approximation to an exponential, and its phase slope. The gamma shapes are precisely reciprocal phase slopes at the node crossings. A complete Poisson trace formula turns this into a global complex Mellin identity while retaining the singular-origin compensation and both infinite tails. Its kernel changes sign at explicitly described points at every order, so monotone Padé phase alone does not prove a Mellin zero theorem.

A separate full-tail second-order expansion identifies the next shifted-eta correction. It uses eta(s+2) and eta(s+4), and yields a corrected reflected approximation to xi with locally uniform o(A_m^-2) error. A fixed zero of multiplicity h is tracked to o(A_m^(-2/h)). This is not a global zero location theorem; a hypothetical off-central xi zero would be tracked too.

The Padé phase coordinate is **not the xi spectral coordinate**. Bulk node bounds certify quadrature geometry, not Riemann zeros. The separate mpmath diagnostics are ordinary high precision, not directed certificates.

## Contents and execution

`check.py` reconstructs bounded exact algebra from factorial Padé coefficients and an independent sinh-series source, including a finite Laurent/hyperbolic polynomial check of the second correction. Its receipt explicitly denies machine verification of the analytic limits and records zero native zero certificates.

```
python -I -S -B check.py --check results.json
python -I -S -B -O check.py --check results.json
python -I -S -B test_check.py
python -I -S -B -O test_check.py
```

The optional numerical diagnostic requires mpmath, not used by the exact checker:

```
python -B diagnostic.py --dps 65 --out /tmp/diagnostics65.json
```

Do not overwrite sealed packet files merely to rerun a producer. Output new diagnostics outside the packet. The manifest is a byte-integrity check relative to its trusted original, not protection against replacement of the entire checker and manifest.

## Research versus publication

The preceding packet is live as PR #877, head `ec60ea46318143e9a7908aab3239fbdb327045df`. **This continuation was not pushed by its authoring session.** [PUBLICATION.md](PUBLICATION.md) supplies an additive delivery instruction and records that boundary. Do not treat a local patch hash as a remote commit or PR receipt.
