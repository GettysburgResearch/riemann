# X-91130 — direct Euler score-interface audit and physical repair

This replay checks the finite and rational parts of `R-91310` and `L-91352`.

It verifies:

1. the exact `P_79` prefix at `x=83`;
2. the exact negative coefficient in
   `S_(P*83)(83)-T_(P*83)(83)`;
3. a directed lower bound for the nine-term von Mangoldt ramp at `x=83`;
4. the rational derivative moat used to reduce every `p>=83`, `1<=y<83` to
   `(83,1)`;
5. the exact `P_30` source target/score upper slopes `16/15` and `4/3`.

Run:

```bash
python3 verify.py
sha256sum -c SHA256SUMS
```

The replay does **not** reprove the imported formal inequality

```text
psi(x) >= 0.9 x for x >= 41,
```

nor does it replay `L-91346`'s directed inherited-row positivity certificate.
It certifies neither the complete factor-54 composition nor RH.
