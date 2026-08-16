# X-93022 - Positive scale-four Q4 source

This exact finite replay supports `L-93022`, `R-93022`, and `L-93023`.

It checks:

- the explicit positive coefficients of `G4=1/A4`;
- the exact Dirichlet inverse `a4*g4=epsilon`;
- positivity of `Lambda4` and `Lambda+`;
- the formal prime-log identity
  `c_circ=(epsilon-2 delta_2)*Lambda+`;
- the exact prefix Haar factorization;
- the complete endpoint row as a positive source-owned fibre sum;
- the principal/transverse atomwise bounds;
- the one-atom principal-channel no-go;
- five hostile mutations.

The checker uses only integer arithmetic and exact dictionaries whose keys
represent formal logarithms of primes.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected classification:

```text
PASS_X_93022_Q4_POSITIVE_SCALE_FOUR
```

The replay does not prove the aggregate transverse Gram estimate, the Q4 mean
bound, OPB, or RH.
