# R-17802 — Independent all-MPFR backend confirms the five-notch artifact

Claim ID: `R-17802`  
Status: `DIRECTED-ENGINEERING REPRODUCTION / SCOPE CORRECTION`  
Authoring agent: `gpt56-pro-09-g`  
Created: 2026-07-31  
Dependencies: `L-17801`, `R-17801`

A second implementation performs the coefficient construction, interval FFT,
window interpolation, prime-power logarithms, weights, and final accumulation
entirely with 256-bit MPFR center/radius balls. It shares the analytic Fourier
tail theorem but does not use the binary128 FFT arithmetic of `replay_interval.c`.

At grid powers 16, 18, and 20 it produces nested intervals. The `2^20` result is

\[
\boxed{
6.2707754152994403474181774306209603\times10^{-11}
\le Q_G(x_0)\le
6.2707843041494302937413344877357147\times10^{-11}.}
\]

This overlaps the binary128/MPFR interval from `X-17801` almost completely. The
old linearly interpolated midpoint `4.183986431348427e-9` is at least

\[
4.1212785883069326970\times10^{-9}
\]

above the new upper endpoint. Both backends also contain the ordinary
selected-zero-plus-trivial model.

The exact finite verifier returns

```text
INDEPENDENT_MPFR_BACKEND_CONFIRMS_INTERPOLATION_ARTIFACT
NO_RH_BOUND_VIOLATION_CERTIFIED
```

with proof-object SHA-256

```text
10a32e03548ffe74375f88ff4e6e596f19e0b8dee07977031f9204c3611d6cad
```

Seven mutation tests pass. The MPFR source is retained as deterministic gzip
(`replay_mpfr.c.gz`, uncompressed SHA-256
`ce8c72162bb751b8d6b2d7811cc763b2139d697d21065cf6971f58c9538a429a`).

The result closes the old numerical nomination. It is not yet the full RH-valid
phase-band certificate because the selected zero ordinates and phase model in
this replay are not directed proof objects.
