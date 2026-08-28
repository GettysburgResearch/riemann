# Hostile self-audit of T-107020

Audited base: PR #759 at `d1b8aa57b08db1ba9f2edf3b68238c2a129b7c33`  
Disposition: **STRUCTURAL COMPRESSION SURVIVES; HNBV107020 AND RH REMAIN OPEN**

## Checks which survived

1. With the stated Fourier convention, the bilateral Laplace factor is
   `exp(1-cos s)`, which is entire and zero-free.
2. The Fourier contour may be shifted only through `|Im t|<pi/2`. Choosing
   the fixed shift `sigma=1` is legal and exceeds the native field's growth
   exponent `1/2`.
3. The noncausal negative-time correction is holomorphic in `Re(s)<1`, not
   in a right half-plane. This is exactly the direction needed: it contains
   the entire detector strip `0<Re(s)<1/2`. The initial draft had the
   half-plane direction reversed; the theorem file is corrected.
4. The prefix-to-complete comparison uses `X_T=e^(7T)`. A constant-factor
   enlargement of `log X` preserves an `X^o(1)` hypothesis.
5. Poisson sampling is approximate through explicit physical aliases. The
   first alias is separated from the compact-prefix autocorrelation by
   `2R_X`, and `R_X=C_A log X` pays the trivial `O(X)` source mass.
6. The spectral multiplier is double-exponential. Bandwidth
   `loglog X+O_A(1)` pays the trivial `O(X)` Dirichlet-polynomial bound.
7. The resulting coordinate count is `O(log X loglog X)`.

## Boundary

Nothing in this audit estimates the native vector. The low-rank coherent
countermodel remains binding. RH is unproved.
