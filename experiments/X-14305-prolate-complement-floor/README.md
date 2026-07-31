# X-14305 — Exact prolate complement-floor checker

This experiment checks the finite scalar inequalities in `L-14310`.  It
performs no special-function, prime, prolate-eigenfunction, or zeta evaluation.
After JSON parsing, it uses only Python integers and `fractions.Fraction`.

## Certified inequality

Given safe directed data

```text
Omega <= omega_upper,
log Omega >= log_omega_lower,
pi >= pi_lower,
C0 >= C0_lower,
kappa(a) <= kappa_upper,
0 < eta < 1,
```

the theorem gives, outside the high-concentration prolate packet,

```text
q_a(w)/||w||^2
 >= C0_lower - 2/pi_lower
    + (1-eta) log_omega_lower
    - kappa_upper.
```

The packet rank is bounded by

```text
ceil(2 omega_upper/(pi_lower eta)).
```

A production certificate is rejected unless its inputs are bound to a
`CERTIFIED_SUZUKI_PERTURBATION_AND_CONSTANT_BOUNDS` gate.

## Synthetic control

The exact control uses

```text
omega_upper       100
log_omega_lower     4
eta                 1/2
pi_lower            3
C0_lower            0
kappa_upper         1
```

and proves

```text
required rank cap   134
complement floor    1/3
```

with proof-object SHA-256

```text
ee5a5195f7fc51828bbc5126481c274f8be87f7141951bb2e542a876c3cf4097
```

## Reproduction

```bash
python experiments/X-14305-prolate-complement-floor/verify.py \
  experiments/X-14305-prolate-complement-floor/certificates/synthetic.json \
  --output /tmp/x14305-result.json

python -m unittest discover \
  -s experiments/X-14305-prolate-complement-floor/tests -v
```

Expected result: seven tests passing.

## Production obligations outside the checker

1. Independently match Suzuki's constants and Fourier convention.
2. Enclose the complete prime-power translation norm and smooth remainder.
3. Prove every concentration mode above `eta` is included in the low packet,
   either by directed prolate eigenvalue enclosures or a stronger packet test.
4. Preserve outward bounds for `pi`, `log Omega`, and `C0` in the safe direction.
5. Combine the resulting complement floor with `X-14304`; the low packet may
   still contain a negative direction.

The crude perturbation majorant can make the rank cap enormous.  The theorem
closes the infinite-complement logic, not the remaining finite-block problem.
