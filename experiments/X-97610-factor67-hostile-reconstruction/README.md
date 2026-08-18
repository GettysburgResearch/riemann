# X-97610 factor-67 hostile reconstruction replay

This replay verifies:

- the exact `5:3` scalar algebra;
- the `x=184` refutation of the `1/40` bias;
- the PR #565 source and depth-one countermodels;
- the PR #566 reserve and Hall-prefix countermodels;
- the corrected `1/42` directed finite/tail certificate.

Run:

```bash
./build_and_replay.sh
```

The replay proves only the declared finite arithmetic and interface refutations. It does not prove `CPSL67`, global scalar positivity, or RH.
