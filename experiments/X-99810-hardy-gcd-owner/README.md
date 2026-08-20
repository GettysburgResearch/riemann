# X-99810 — Hardy-tail and divisor-GCD owner-square replay

This lightweight exact replay verifies the finite algebra behind `L-99810`
through `L-99812` and the clustered-frequency firewall `R-99810`.

```bash
python3 experiments/X-99810-hardy-gcd-owner/verify.py
```

Expected:

```text
PASS_T99810_HARDY_GCD_OWNER_SQUARE_INTEGRATORS
8451fe0ea2e97815cc9300b462e07774d132483638f47e6879ee893cd2299be1
```

The replay checks:

- minimum-kernel = truncated-tail-square at `2 tau=1`;
- GCD quadratic = Jordan divisor-square at exponent one;
- exact factor-67 hazard weights sum to one;
- Hilbert-space Jensen on a nontrivial rational fixture;
- a 64-frequency distinct-integer cluster with Poisson/diagonal ratio above 63.

It explicitly records:

```text
HTOC99810 proved       false
DGOC99810 proved       false
GPMOC99800 proved      false
RH established         false
```

The replay authenticates exact identities and firewalls; it does not substitute
for the open signed squarefree-core packing theorem.