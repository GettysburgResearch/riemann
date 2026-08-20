# T99810 — Hardy-tail and divisor-GCD owner-square integrators

This packet continues the canonical scalar spine of PR #659 at exact head
`83c17b32a99ac9e1aa5aec3168535550eb286636` and imports the exact native
first-owner identity of PR #660 at
`ca3c055307e6804ae904cb9105594dd3f2408ba3`.

**Scientific status:** exact new positive normal forms and a strengthened
native-owner composition theorem. **The Riemann Hypothesis remains unproved.**

## Main result

For a finite coefficient packet `c=(c_n)` and `tau>0`, the Cauchy--Poisson
quadratic form used by `GPMOC99800` has the exact Hardy-tail representation

```text
Q_tau(c)
 = |sum_n c_n|^2
   + 2 tau integral_1^infinity t^(2 tau-1)
       |sum_(n>=t) c_n|^2 dt.
```

Thus the allegedly opaque off-diagonal term is precisely a positive square of
all truncated native tails.

A second, multiplicative Poisson construction gives

```text
|sum_n c_n|^2
 <= sum_(m,n) c_m conjugate(c_n) gcd(m,n)^(2 tau)
 =  sum_d J_(2 tau)(d) |sum_(d|n) c_n|^2.
```

This is an exact positive divisor-owner square aligned with the multiplicative
source.

Finally, the coefficient-exact first-owner identity is contractive after
mapping into the Hardy-tail Hilbert space by convexity:

```text
Q_tau(F f)
 <= s_k Q_tau(f) + sum_i lambda_i Q_tau(Delta_i^fut f).
```

No arbitrary labelled-to-physical collapse is used in this inequality.

## What remains

The packet isolates two equivalent/sufficient arithmetic packing gates:

```text
HTOC99810  -- subpower packing of the exact truncated-tail squares;
DGOC99810  -- subpower packing of the exact divisor-GCD owner squares.
```

Either gate, with PR #659's positive inverse weights, implies `GPMOC99800` or
bypasses it and therefore implies RH. Neither gate is proved here.

An exact clustered-frequency counterexample proves that diagonal or
source-blind labelled energy alone cannot establish either gate: the Poisson
quadratic form can exceed its diagonal by an arbitrarily large factor even on
distinct integer frequencies.

## Replay

```bash
python3 experiments/X-99810-hardy-gcd-owner/verify.py
```

Expected:

```text
PASS_T99810_HARDY_GCD_OWNER_SQUARE_INTEGRATORS
8451fe0ea2e97815cc9300b462e07774d132483638f47e6879ee893cd2299be1
```
