# X-91430 — Eta-paired dyadic sector-change replay

This finite replay supports `L-91430`, `L-91431`, `R-91408`, and the source
bookkeeping of `T-91405`.

It checks:

- the exact eta/dyadic factorization of the horizontal Jordan quotient;
- the simple dyadic zero at the free pole node;
- the exact local coefficient `zeta(1-2 omega)`;
- convergence of the paired eta series inside `Re s>0`, against an elementary
  tail bound;
- the explicit positive Householder map between normalized paired eta vectors;
- orthogonality of that reflection;
- the Gram mismatch showing that the same one-vector unitary cannot intertwine
  a complete carrier family.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_ETA_DYADIC_SECTOR_CHANGE
```

The replay checks finite truncations and analytic identities.  It does not
construct the completed eta/gamma source-to-model map, prove EPDOB, or prove
RH.