# X-91306 — Product-sector and pole-bridge replay

This replay checks finite algebra and numerical asymptotics for `L-91327`–`L-91330` and `R-91309`:

1. local inverse coefficient and H2 norm formulas;
2. weighted Dirichlet–Hardy specializations;
3. exact translated-overlap deficiency;
4. Green/Dirichlet-convolution commutation on finite data;
5. the gamma residue identity for the pole bridge;
6. Suzuki endpoint asymptotics at two sample omega values;
7. the free Green hard-range growth/decay law;
8. finite-Euler amplification of the pole coefficient;
9. the small-a pole-node source/model normalization mismatch.

It does not prove the infinite-prime PNT asymptotics, `EPBOT_omega`, the renewal estimate, innerness, or RH.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```
