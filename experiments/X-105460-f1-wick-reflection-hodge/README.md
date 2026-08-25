# X-105460 — F1 Boolean/Wick and reflection-Hodge replay

Run

```bash
python experiments/X-105460-f1-wick-reflection-hodge/verify.py
python experiments/X-105460-f1-wick-reflection-hodge/tests/test_verify.py
```

The replay checks:

```text
Boolean Chow multiplication and h star h = mu_sf;
balanced half-source square identities;
the codimension-two Beta incidence Green;
minimum-energy and Hodge projections of pair owners;
the open-configuration / diagonal-contraction partition;
reflection-even/odd Hilbert identities;
the four roots of the differential detector;
the exact negative TP3 determinant.
```

It authenticates finite algebra and the stated firewall.  It does not estimate
`F1VAR105460`, prove `BCI102990`, or prove RH.
