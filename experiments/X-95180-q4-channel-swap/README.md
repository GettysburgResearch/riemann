# X-95180 — Scale-four channel-swap and Peano-flux exact replay

Run:

```bash
python3 verify.py --output /tmp/x95180.json
cmp /tmp/x95180.json results/verification.json
sha256sum -c SHA256SUMS
```

Arithmetic class:

```text
EXACT_INTEGER_RATIONAL_AND_FORMAL_PRIME_LOG
```

The replay checks finite coefficient/channel identities, the exact energy constant, dyadic pairing, polynomial Peano curvature, finite scale-four Peano flux identities, and hostile mutations. It does not prove CCFE, the centered cubic bound, or RH.
