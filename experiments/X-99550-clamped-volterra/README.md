# X-99550 — Exact clamped-Volterra replay

Run:

```bash
python3 verify.py
```

The checker uses only the Python standard library. It verifies:

- the Euler-operator action on all four basis functions;
- the unique coefficients \((-12,12)\) forced by the two clamps;
- exact Green-integral coefficient reconstruction;
- vanishing lower-boundary modes;
- vanishing activation-knot derivative jumps;
- the scaling law on an exact square fixture;
- double clamping of the physical parabolic endpoint packet;
- two mutation firewalls.

It deliberately records:

```text
heavy_inherited_campaigns_replayed = false
rh_established = false
```
