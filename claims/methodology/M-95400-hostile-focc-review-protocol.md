# M-95400 — Hostile review protocol for the annular FOCC hardening

Review in this order:

1. Freeze PR #573 at `0865242eb9dc0ed6094afc8a87a52b974c6f1307`.
2. Reconstruct `L-95400`, especially the endpoint-halving convention and the support cutoff `2^-10`.
3. Compare every band coefficient against `exact_kernels.json` using exact `Q(sqrt(2))` arithmetic.
4. Check the stable inverse coefficient mass `64/21` and the location of every Mellin zero.
5. Reconstruct the ten-band pair partition and the constants in `L-95401`.
6. Verify the gcd substitution preserves pairwise coprimality and removes the common-divisor sign exactly.
7. Check the Type I/II expansion retains `(d,p)=1`, the literal activation and the `J1` boundary.
8. Treat all numerical signs as reconnaissance only.
9. Treat `SACF` as open.

Immediate rejection conditions:

```text
one nonzero J0/J1 coefficient below x=2^-10;
a missing scale factor in Q(S);
a Mellin zero in Re z>0;
a ratio greater than 1024 in an active pair;
a common-divisor Mobius sign retained after m=da,n=db;
an omitted J1 boundary channel;
a diagonal or randomized estimate promoted to deterministic FOCC;
a fixed-window large-sieve estimate with the CX term deleted;
a source-blind PSD or log-Sobolev argument used after R-95400;
a floating scan represented as SACF, FOCC or RH.
```

The correct final status is:

```text
SACF / FOCC / OCHD / RH: open and conclusion-producing.
```
