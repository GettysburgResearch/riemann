# X-26201 — Exact dyadic parity-dipole algebra

This standard-library-only regression checks the finite algebra used by
`L-26201`--`L-26203`.

Run:

```bash
python experiments/X-26201-dyadic-parity-dipole/verify.py
```

Expected classification:

```text
EXACT_DYADIC_PARITY_DIPOLE_ALGEBRA_VERIFIED
```

The verifier exhaustively checks through `n=192`:

- the Möbius-adjoint affine carry row;
- the four-layer source
  `1,-5/2,2,-1/2`;
- the compact factor-four positive/negative carry dipole;
- the binary-digit convolution
  `c_2*omega_2=epsilon-(5/2)delta_2+delta_4`;
- positivity and exact convolution inverse of `a_2^star`;
- pointwise inversion between the new source and the dyadic Mertens shell;
- exact positive bipartite defect-to-slack block transport;
- fail-closed mutations for a missing sibling, absolute values, a wrong
  coefficient, reversed endpoints, wrong-side incidence, and overfilled slack.

The retained run reports:

```text
affine rows          18,336
dipole rows          18,336
local coefficients      192
digital rows            192
inverse rows            192
shell inversions        192
transport rows           20
mutations rejected        6
```

## Proof boundary

This experiment verifies finite algebra only. It does not establish the
source-specific two-frequency reflected Hall identity, the existence of
cofinal transport certificates, or RH.
