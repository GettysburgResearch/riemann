# X-20806 — Prime-prefix transport reconnaissance

This experiment implements the finite discovery side of `T-20802` and
`L-20808`.

For every prime-power prefix through a declared integer cutoff it computes

```text
P_j = sum Lambda(q)/sqrt(q)
Q_j = sum Lambda(q) log(q)/sqrt(q)
M_j = Q_j - A_+^*(P_j)
```

where `A_+^*` is the constrained Fenchel conjugate of the complete smooth
Suzuki term on `[log 2,infinity)`.

## Reproduction

```bash
python experiments/X-20806-prime-prefix-transport/recon.py \
  --limit 10000000 \
  --digits 80 \
  --output experiments/X-20806-prime-prefix-transport/results/recon-1e7.json
```

The producer:

1. enumerates primes and prime powers by exact integer arithmetic;
2. hashes rows as ASCII `q,p,k\n`;
3. ranks every prefix with a binary64 Newton solve;
4. replays the record-low prefix with mpmath at the requested precision.

## Preserved result

```text
prime-power rows             665,134
record-low prefix            q=3089
next knot                    q=3109
record-low margin            0.02752057335362080482041457506913378...
manifest SHA-256             ad1fe1520966ca5c41885166f4a28a0d543922f087881175c0c15e89425fc56a
```

The record-low minimizer lies strictly between the two displayed knots and
agrees with the independent prime-knot scan retained on PR #98.

## Proof boundary

This experiment is **not directed**.

It supplies:

- exact finite source enumeration;
- deterministic discovery arithmetic;
- one high-precision same-derivation replay.

It does not supply:

- outward prime-moment intervals;
- a directed Fenchel/entropy barrier;
- a proof that all finite prefixes through the cutoff are positive;
- any conclusion beyond the cutoff;
- RH.

The intended successor is a directed block producer that emits transport
reserve and drawdown ledgers for use in a cofinal analytic proof.
