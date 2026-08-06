# X-21503 — Prime-layer and prime-only energy reconnaissance

Classification: `LONG_DOUBLE_RECONNAISSANCE`  
Claim: `O-21502`  
Theorem interface: `T-21502`

This experiment reuses the complete duplicate-free prime-power manifest and the
exact piecewise-linear window of X-21502, but keeps five channels separate:

```text
ordinary primes
prime squares
prime cubes
prime fourth powers
prime powers of exponent >=5
```

It integrates the complete channel Gram on every unit logarithmic block. It
also evaluates the ordinary-prime-only boundary-difference signal

```text
H(u)=G(u)-G(u-1).
```

The purpose is structural:

1. identify which prime-power layers create the very large cancellation in
   O-21501;
2. test the Möbius-inversion prediction that prime squares are the main partner;
3. calibrate the prime-only criterion of T-21502.

The arithmetic is deterministic long double, not directed. No sign or RH claim
is made. The retained blocks are complete for the `10^7` manifest and the
window support.
