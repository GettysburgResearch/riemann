# X-91620 — Annular Clark-entropy replay

This finite replay supports `L-91620`, `L-91621`, and the normal-form statements
of `T-91620`.

It checks:

1. additivity of zero-by-zero logarithmic Green charges;
2. the exact Clark resolvent identity
   ```text
   log(1+q)=int_0^1 q/(1+tq) dt;
   ```
3. the Green–Laplace representation of one crossed-zero charge;
4. the quantitative moat
   ```text
   g_eta(x+iy)>=4 eta x/[(eta+x)^2+y^2];
   ```
5. the weighted hyperbolic recurrence and the unweighted logarithmic dyadic
   telescope on synthetic annuli;
6. one explicit depth-height exclusion threshold.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_ANNULAR_CLARK_ENTROPY
```

The synthetic zero packets validate exact model identities and quantitative
moats.  They do not identify the arithmetic source map, prove CEAE, or prove
RH.
