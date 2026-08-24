# X-106050 — Temperature–Kummer fibre replay

Standard-library exact replay for `L-106050--L-106051`, `R-106050`, and
`T-106050`.

It checks:

```text
character-twisted complementary-temperature flatness;
common chi^2 completion for the two quadratic roots;
Hadamard conversion of a quadratic root fibre into two source charts;
owner-class invariance of P*a^2;
simultaneous midpoint energy minimization;
failure of positivity for a nonprincipal character-square inverse;
2^omega(q) tensor root-sector count.
```

Run:

```bash
python3 verify.py --output /tmp/x106050.json
cmp /tmp/x106050.json results/verification.json
```

The checker uses exact rational arithmetic in finite cyclic group rings. It
does not prove the physical assembly `TKCA106050`, `GMBC102893`,
`HBCQDSP102888`, or RH.
