# X-23801 — Exact Gamma–carry algebra replay

This standard-library `Fraction` verifier checks the finite algebra used by the
Gamma–carry proposal:

1. every carry coefficient through `n=64` equals the left-endpoint continuum
   kernel sample `K_-((n+1)/q)`;
2. every harmonic interval mass through `m=64` is exactly `1/[m(m+1)]`;
3. the partial Mellin telescoping identity is exact for six integer exponents
   and six cutoffs;
4. the rational partial-fraction decomposition producing the Möbius–Riesz
   density is exact.

Retained verdict:

```text
PASS_EXACT_GAMMA_CARRY_ALGEBRA
```

Certificate SHA-256:

```text
b3f629008dd4432c22e3d8059e9d64c52d0baf4fc3561861564fe00bd8edd51d
```

The verifier does **not** certify GCF, the density sign, a prime-ramp asymptotic,
or RH. Its purpose is to bind the exact finite and Mellin normalization before
the load-bearing sign is reviewed.
