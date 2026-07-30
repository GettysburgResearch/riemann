# Integration handoff — finite prolate capture of the infinite complement

Agent: `gpt56-pro-09-b`  
Issue: #143  
PR: #152

## New artifacts

- `L-14310` — time-band trace theorem plus complete Suzuki perturbation charge.
- `X-14305` — exact rational scalar/rank checker with seven tests.

## Exact usable bound

For support parameter `a`, band `Omega>1`, and concentration threshold
`0<eta<1`, include every prolate concentration mode above `eta` in the low
packet.  Its rank is at most

```text
ceil(2 Omega/(pi eta)).
```

The complete orthogonal complement satisfies

```text
q_a(w)/||w||^2
 >= C0 - 2/pi + (1-eta) log Omega - kappa(a),
```

with

```text
kappa(a)
 = |log a + 2 A_zeta + 1|
   + 2 sum_(n<=exp(2a)) Lambda(n)/sqrt(n)
   + integral_(-2a)^(2a) |r''(u)| du.
```

## Immediate implementation tasks

1. independently audit the exact constants in Suzuki (4.5)–(4.6);
2. produce directed bounds for the finite prime sum and smooth remainder;
3. enclose enough prolate concentration eigenvalues to certify packet
   containment;
4. run `X-14305` to obtain a complement floor;
5. feed the packet and complement into `X-14304`.

## Most valuable sharpening

The absolute prime sum makes the rank cap enormous.  Replace it by a directed
operator norm of the complete finite translation polynomial.  Every unit
improvement in `kappa(a)` reduces the required `Omega` exponentially.

## Status

The infinite complement is now closed at the theorem level.  The finite low
prolate block and its cofinal Schur floor remain unresolved.  RH is not claimed.
