# X-27202 — Directed countercertificate to pure ternary fragmentation

This experiment certifies the sign of the deterministic ternary-flow coefficient

```text
X = 10,000,000
n = 63
```

for the logarithmic carry target. It evaluates the exact path-count formula

```text
A_X(n)
 = u_n + sum_(m>n) [c_m-c_(m-1)] u_m
```

with outward MPFR rounding, where

```text
c_n=1,
c_m=c_(ceil(m/3))+c_(floor(2m/3)),

u_m=m^(-1/2)[log(X/m)P0(floor(X/m))-P1(floor(X/m))].
```

The retained 256-bit and 512-bit intervals are both strictly negative, and the
512-bit interval is nested inside the 256-bit interval.

## Build and run in the retained environment

The exact executed source uses the stable MPFR ABI directly because the runtime
container exposes `libmpfr.so.6` without development headers:

```bash
gcc -O3 -march=native -DCERT_PREC=256 certify.c \
  /lib/x86_64-linux-gnu/libmpfr.so.6 -lgmp -o certify-256
./certify-256

gcc -O3 -march=native -DCERT_PREC=512 certify.c \
  /lib/x86_64-linux-gnu/libmpfr.so.6 -lgmp -o certify-512
./certify-512
```

On systems with `mpfr.h`, the manual declarations may be replaced by the normal
header without changing the arithmetic.

## Scope

The certificate refutes universal nonnegativity of the pure ternary producer.
It does not refute the full balanced MFT cone, a Pascal-cycle repair, or RH.
