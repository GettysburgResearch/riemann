# X-20808 — Prime-positive square-diagonal reconnaissance

This experiment calibrates the diagonal criterion `T-20804` at the simple
prime-free base

```text
a = log(2)/2,
r_n = ceil(2 log(n)/a),
t_n = 2 log(n)/r_n.
```

Thus

```text
exp(t_n) <= sqrt(2) < 2,
```

so the lower-scale screw value contains no prime-power deposition. Each level is
computed from

```text
J_a(n)
 = r_n^2 A(t_n)
   - A(2 log n)
   + sum_(q<=n^2) Lambda(q)/sqrt(q) log(n^2/q),
```

and every prime coefficient is nonnegative.

## Run

```bash
python3 recon.py \
  --limit 10000000 \
  --digits 80 \
  --output results/recon-1e7.json
```

The integer prime-power manifest is exact. The full transcendental scan is
binary64, with 80-decimal-place mpmath replays at the record-low and final
levels. This is **ordinary reconnaissance**, not interval arithmetic.

## Retained result

```text
prime-power limit       10,000,000
prime-power rows        665,134
integer n levels        2,...,3162
all scanned margins     positive
maximum lower cutoff    < sqrt(2)
```

At the final level `n=3162`, `r=47`, the high-precision decomposition is

```text
positive prime ramp     12600.9672192272113120387039902564...
A(2 log n)              12601.0051209049633386503562836244...
base reserve            97.7098679914833611349042671096...
J_a(n)                  97.6719663137313345232519737416...
```

The pole-sized prime and archimedean terms cancel before the explicit
polylogarithmic base reserve is applied. The retained manifest SHA-256 is

```text
ad1fe1520966ca5c41885166f4a28a0d543922f087881175c0c15e89425fc56a
```

## Proof boundary

- A finite positive scan does not establish eventual positivity.
- The result is not directed and is not a sign certificate.
- The exact theorem is `T-20804`; the missing statement is the cofinal
  all-positive prime-ramp inequality.
- A strict directed negative value at any level would contradict RH, subject to
  the inherited screw-normalization review.