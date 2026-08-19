# X-99050 — Score-last finite-tree replay

The standard-library checker verifies:

```text
exact causal coefficients;
finite-depth actual-prime scale contraction;
complete physical-row tree identity;
literal-score isometry;
unique Hall-bonus ownership mutation;
explicit top omission bound <60;
explicit thinning cost <792;
complete root score loss <852;
RH status firewall.
```

Run:

```bash
python3 verify.py --output results/verification.json
python3 -m unittest discover -s tests -v
```

The replay does not rerun the compact Hall, endpoint-frame, all-column, or
Mellin--Landau campaigns and does not establish RH.
