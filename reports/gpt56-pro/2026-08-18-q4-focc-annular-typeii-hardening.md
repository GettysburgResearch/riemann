# Q4 FOCC attack: safe annularization and the separated coprime Type-II frontier

## Executive conclusion

The requested FOCC proof was attacked through all of the proposed coordinates. No complete unconditional proof survived the interface audit, so RH is not claimed.

The pass nevertheless produces a substantial exact reduction:

1. a safe three-factor scale filter kills the entire cubic small-`x` tail;
2. the Q4 packet becomes one factor-1024 annulus with ten exact `Q(sqrt(2))` bands;
3. the diagonal improves to `O(log^2 X)`;
4. every polylog-width near-diagonal and large-gcd sector is closed absolutely;
5. every remaining pair has bounded ratio and admits an exact pairwise-coprime `m=da,n=db` form;
6. the source-faithful Type I/II, Mellin and log-Fourier forms are explicit;
7. generic PSD, square-function, Mellin-window and log-Sobolev closures are ruled out.

The sole remaining theorem is the separated small-gcd coprime Type-II estimate `SACF`.

## Why the standard attacks did not close

### Type I/II

The log-weighted channel has an exact prime-divisor expansion, but the large-prime piece retains a bilinear Möbius sum at critical square-root normalization. Absolute values cost `sqrt(X)`.

### Dispersion and gcd

Common divisors are sign free and large gcd is harmless. After removing them, the full sign character remains on two coprime ratio variables. No local positivity follows.

### Large sieve / Mellin almost orthogonality

Logarithmic frequencies on a length-`X` annulus have spacing `1/X`; a fixed Mellin window retains an `O(X)` loss. Compact log support gives an entire Fourier transform, not compact frequency support.

### Pretentious distance

Nonpretentious first-moment bounds do not reach the critical square-root scale. The exact Mellin transform still contains `1/zeta(s+1/2)`.

### Positive-kernel completion

A diagonal Schur completion of the rank-one cross kernel requires a factor equal to the number of active cores. This reproduces the macroscopic wall.

### Square functions / log Sobolev

The Möbius source is a top parity character on the prime cube. Uniform-cube normalization introduces an exponential denormalization factor; the arithmetic support and global signs remain essential.

## Exact final chain

```text
SACF
 -> annular FOCC
 -> stable inverse to PR #573 packet
 -> OCHD critical centered-cubic bound
 -> frozen Mellin pole exclusion
 -> RH.
```

`SACF` is open and RH-bearing.

## Scientific status

```text
new exact reduction: yes
complete FOCC proof: no
complete unconditional RH proof: no
Riemann Hypothesis: unproved
```
