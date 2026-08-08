# X-21704 — Correct centered Brownian Robin fiber

Run:

```bash
python verify.py
```

Expected verdict:

```text
PASS_EXACT_CORRECT_BROWNIAN_ROBIN_FIBER
```

The checker verifies with exact rational arithmetic that:

- centered Mellin symmetrization produces only even powers of `z`;
- the correct fiber is `cosh(ell z/2)+2z sinh(ell z/2)`;
- the withdrawn `cosh(ell z/2)+sinh(ell z/2)/ell` expression has nonzero odd coefficients;
- the corrected expression equals the Neumann-Robin boundary determinant up to a nonzero scalar.

The spectral classification and failure of finite reflected-tail domination are
proved analytically in `L-21709` and `R-21703`. The checker proves neither BLNRZ
nor RH.
