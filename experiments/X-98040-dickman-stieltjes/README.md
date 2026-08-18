# X-98040 — Dickman–Stieltjes corridor replay

Run:

```bash
python3 verify.py
```

The replay checks:

- an exact rational step-source Stieltjes identity;
- the exact `P_61` residue and Mellin finite-part constants;
- the `3/8,-3/4` exponent balance;
- fail-closed status flags.

It does not reconstruct the Vinogradov--Korobov zero-free region, de Bruijn's
Dickman ratio estimates, or the fixed-`P_61` variation theorem, and it does not
prove GPC67 or RH.
