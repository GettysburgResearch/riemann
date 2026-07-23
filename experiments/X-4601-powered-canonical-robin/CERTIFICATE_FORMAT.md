# X-4601 certificate format

Schema: `riemann.robin.powered-canonical-tree.v1`

The certificate header fixes the exact integer region, dyadic arithmetic
parameters, finite dual ladder, prime prefix, and root-summary precision. It
then stores one deterministic terminal stream per support.

## Tokens

```text
P:e1,e2,...       separate-cap internal terminal
J:a,d:e1,e2,...   powered shared-budget internal terminal
S:e1,e2,...       satisfied leaf
B:e1,e2,...       below-domain leaf
U:e1,e2,...       unresolved leaf
V:e1,e2,...       violation leaf
```

Tokens are ordered by exact depth-first traversal with exponents descending.
The verifier must regenerate the tree. It may consume an internal token only
when its prefix equals the current prefix. A support is accepted only when the
stream is exhausted exactly.

A `J` token is intentionally minimal. The verifier recomputes the full powered
proof from `(a,d)`, the current prefix, the global integer bound, and the exact
tail primes. No supplied DP table or floating ranking is trusted.

The outer `certificate_sha256` is the SHA-256 digest of canonical compact JSON
after removing that field. The release manifest separately binds the pretty
JSON bytes, deterministic gzip bytes, terminal stream, verifier output, and
source snapshots.
