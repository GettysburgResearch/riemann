# RLC35 — native radical/logarithmic calculus

**Proposed, unreviewed component mathematics. No RH proof or native asymptotic
energy improvement is claimed.** Third separately published pass on PR #907,
after NJV34 at `4f769249e35d23a9cf955fbab620e70d07117e58`.

Read [PROOF.md](PROOF.md). For the native log source f with squared norm E_N,

```
a_phi(n) = sum_{d|n} mu(d) phi(log d)
C_a f = phi f - R(phi' f),       ||R|| <= 2.
```

Bounded logarithmic profiles control the COMPLETE divisor sum, including
arbitrarily many distinct primes, with constants independent of the cutoff.
The algebraic compatible kernels are exactly the radical-invariant ones;
small derivative cost is a separate requirement, not automatic.

For phi(u)=exp(i*tau*u), the exact coefficient is
`product_{p|n}(1-p^(i*tau))`, and the energy lies between
`kappa(tau)^(-2) E_N` and `kappa(tau)^2 E_N`, with
`kappa=sqrt(1+tau^2)+abs(tau)`. The constant is sharp for the universal
logarithmic multiplier family, not claimed sharp on the Möbius vector.

The polynomial profiles give an all-order quadratic covariance identity with
positive bulk and endpoint terms. They include a fully specified two-prime
kernel, but not arbitrary replacements of its coefficients.

For the actual capped source, the transfer produces a nonzero defect. The
packet gives its exact tensor/Hankel identity, retaining complex phases.
The quadratic error vanishes below a PRODUCT-COEFFICIENT cutoff; an earlier
observation time is not enough once the microscopic mask is applied. A
separate exact control shows why reciprocal balancing costs cannot be omitted.

## Replay

Python standard library only:

```sh
python -I -S -B check.py --check receipt.json
python -I -S -B -O check.py --check receipt.json
sha256sum -c SHA256SUMS
```

See [VALIDATION.md](VALIDATION.md) for executed coverage and exclusions, and
[SOURCES.md](SOURCES.md) for attribution and exact inspected repository heads.

The next unresolved task is a quantitative bound for the defect pairings in
PROOF §6, or a controlled inverse on the relevant kernel range. Neither is
assumed or supplied. The original RAB33 and NJV34 directories are unchanged;
this packet does not promote a canonical claim or request a merge.
