# O-93300 — Proof DAG after the cubic-shell and Vaughan reductions

Status: **ROUTE TAXONOMY / HANDOFF**  
Created: 2026-08-16

```text
complete compact-Q4 source
  -> centered Bernoulli projection
  -> cubic Riesz sum A_circ(N)
  -> zero-safe Mellin pole audit

  -> scale-four wavelet F
  -> small prime bases and all prime powers: O(sqrt(N) log N)
  -> large-prime shell only

  -> two exact Mellin moments
  -> exact discrete grid cancellation

  -> Vaughan identity
  -> Type I: O(N^(1/3) log N)
  -> low-product Type II: O(sqrt(N) log^3 N)

  -> BCD:
     truncated-Mobius x von-Mangoldt covariance
     N^(1/3)<m,l<=N^(2/3)
     N^(3/4)<ml<=N
     exact piecewise cubic F(ml/N)

  -> sqrt(N) polylog bound
  -> Mellin pole exclusion
  -> RH.
```

The first five arrows after the analytic spine are unconditional theorems in
this packet.  `BCD` is the sole remaining arithmetic estimate and remains
open.

Equivalent attack coordinates retained for BCD:

```text
near-hyperbola bilinear form;
additive Fourier dispersion with h!=0;
Mellin band-pass product of two finite Dirichlet polynomials;
First-Hermite heat-wavelet carrier integral.
```

`R-93254` and `R-93300` prohibit a block-count or magnitude-only closure.
