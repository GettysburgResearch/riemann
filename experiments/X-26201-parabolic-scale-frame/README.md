# X-26201 — Parabolic endpoint-scale frame checks

This experiment supports `L-26201`--`L-26203` and `T-26201`.

Run from the repository root:

```bash
python experiments/X-26201-parabolic-scale-frame/verify.py
```

The script has two deliberately separated assurance layers.

## Exact rational-interval layer

Using only `fractions.Fraction`, integer square roots, and an `atanh` series with
an explicit rational remainder, it proves the two finite gates used in
`L-26202`:

```text
K_16 < -1/2;
H_N'(theta) > 7/25
for 2 <= N <= 14 on the complete reciprocal cell.
```

The logarithm and square-root enclosures are outward rational intervals.  No
floating result is consumed by this layer.

## High-precision reconnaissance layer

Using `decimal.Decimal` at 70 digits, it constructs the actual parabolic row
vectors, endpoint atoms, response columns, and endpoint-scale greedy packing at

```text
X = 64, 128, 256.
```

It records:

- the smallest positive endpoint-atom coefficient;
- total scale slack;
- prime-power weighted objective gap;
- every positive off-diagonal blocker;
- maximum blocker loss and loss divided by `sqrt(T)`;
- maximum scale weight.

This layer is classified

```text
HIGH_PRECISION_DECIMAL_RECONNAISSANCE.
```

It is a mutation/discovery check, not an interval certificate and not evidence
for the cofinal `ESBT` theorem.

## Retained result

```text
sha256_without_digest
3bb2311307155cb36a96017bf0b60d446dd0d54cf0622f3d7ffbd40196f51fe9
```

File hashes are recorded in `SHA256SUMS`.

## What the experiment does not prove

It does not prove:

- positivity of every endpoint atom by computation; that is the analytic proof
  in `L-26201`;
- finite-floor transfer of the continuum tail coupling;
- `ESBT` or `ESGS`;
- a cofinal prime-ramp estimate;
- RH.
