# X-90603 — Bohr syndetic recurrence diagnostic

This finite diagnostic constructs an exact torus zero of

\[
1+2^{-2z}+3^{-2z},
\]

searches recurrent vertical phases of the untwisted polynomial, and Newton-refines
one actual zero from each successive phase block.

Run:

```bash
python3 verify.py
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_X_90603_BOHR_SYNDETIC_RECURRENCE
```

The theorem uses Kronecker minimality, compactness and Rouché. The finite scan
only illustrates the recurrence and does not prove the Brownian applications or
RH.
