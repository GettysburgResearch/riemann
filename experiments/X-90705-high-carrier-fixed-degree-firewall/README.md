# X-90705 — high-carrier fixed-degree firewall

This finite moving-tail model illustrates the analytic theorem in
`HIGH_CARRIER_FREDHOLM_FIXED_DEGREE_FIREWALL.md`.

It uses diagonal families

\[
A_c=cB+E_c,\qquad B\ge0,\qquad \|E_c\|_1=1,
\]

where the rank-one negative perturbation moves into the small-eigenvalue tail of
`B`. One negative eigenvalue persists, while every fixed exterior/Hankel degree
becomes positive and the first detecting exterior degree diverges.

Run:

```bash
python3 verify.py
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_X_90705_HIGH_CARRIER_FIXED_DEGREE_FIREWALL
```

This is a diagnostic model, not the analytic zeta proof and not RH.
