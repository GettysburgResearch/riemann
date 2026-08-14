# X-19885 — Exact Y4 sparsity and factor-67 root-cost regression

The checker represents `Y4(q)` as a formal integer combination of symbols
`log p`. It verifies the exact support formula through `q=200000` without
floating-point logarithms, and checks the rational constants used by
`L-19885`:

```text
two-power 3/2 contribution       <5/3;
odd-prime-power contribution     <26/3;
total                            <11;
(285/8)*11                       <392.
```

It also records finite exact majorants for the collar and global safety terms.

```bash
python3 verify.py certificates/control.json --output /tmp/x19885.json
cmp /tmp/x19885.json results/verification.json
python3 -m unittest discover -s tests -v
sha256sum -c SHA256SUMS
```

The replay does not prove the frozen common-parent realization or RH.
