# X-91682 — Post-Hall complete profile and debt replay

Run:

```bash
python3 verify.py
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_POST_HALL_COMPLETE_PROFILE_AND_DEBT_PACKET
```

The script uses the Python standard library, exact `Fraction` arithmetic, integer square-root enclosures, and 120-digit `Decimal` logarithms enclosed by a rational interval wider than the correctly-rounded ulp.  Display decimals never decide a sign.

The replay verifies finite gates and constants only.  The analytic reductions are stated in `L-91682` and `L-91683`.  It explicitly does not certify the remaining row determinant or RH.
